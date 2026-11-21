#!/usr/bin/env python3
"""DET-CON pre-publish scan -- serves gate G-CO-062 (real-content skill).

Runs the automatable subset of the DET-CON-001...028 content-detection
parameters (skills/detection/content/PARAMETERS.md) over rendered
pages, their metadata, and their JSON-LD:

    placeholder strings   DET-CON-001, 002, 004, 005 (string half)
    template tokens       DET-CON-003
    copy signals          DET-CON-006 (filler with no specific on the
                          page), 007 (AI vocabulary cluster), 008
                          (repetitive page skeletons), 009 (hedge
                          stacks)
    fact consistency      DET-CON-014 (only with --fact-sheet; the
                          diff engine of scripts/claim-trace.py),
                          015 (site contradicts itself on founding
                          year, team size, user counts), 016 (price
                          mismatch against the pricing page / per
                          plan), 017 (name variants), 018 (stale
                          dated copy, against today's date)
    authorship            DET-CON-021 (voice fingerprints across
                          three or more bylined authors)
    metadata              DET-CON-022 (title/meta vs page), 023
                          (OG/Twitter vs page and across pages)
    structured data       DET-CON-024 (JSON-LD vs visible page)
    scale                 DET-CON-025 (near-duplicate page clusters)
    claims                DET-CON-026 (measurable superlatives with
                          no substantiation cue; unmeasurable
                          puffery is printed as a copy note, never
                          a hit), 027 (alt-text defaults)

The remaining parameters (010-013, 019, 020, 028) are worked as a
manual checklist against the evidence register, per the gate; this
script does not run them. DET-CON-005's test-message send and
DET-CON-014 without a fact sheet likewise stay manual -- the scan
reports them as not run, never as passed.

Severity follows PARAMETERS.md. Pass (the gate's criterion): zero
blocker hits and zero major hits; minor hits are reported but do not
fail the scan. Exit codes: 0 = pass; 1 = blocker or major hits;
2 = setup error. Standard library only.
"""

import argparse
import json
import re
import sys
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "claim_trace", Path(__file__).resolve().parent / "claim-trace.py")
_claim_trace = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_claim_trace)
extract_facts = _claim_trace.extract_facts  # same extraction rules
norm_num = _claim_trace.norm_num

LOREM = ["lorem", "ipsum", "dolor sit amet"]
DEFAULTS = ["hello world!", "just another wordpress site",
            "add a description here", "sample page",
            "this is your first post", "edit or delete it",
            "welcome to wordpress", "my wordpress site"]
MARKERS = ["todo", "fixme", "xxxxx", "test test", "coming soon",
           "content to follow"]
CONTACT_PATTERNS = [r"example\.com", r"example@", r"555-01",
                    r"123 main street"]
FILLER = ["revolutionize your workflow", "unlock the power of",
          "take your business to the next level",
          "take it to the next level", "unlock the full potential",
          "revolutionize the way"]
CLUSTER_TERMS = ["delve", "tapestry", "landscape", "realm",
                 "furthermore", "moreover"]
OPENERS = ["it's important to note", "it is important to note",
           "in today's fast-paced world",
           "in todays fast-paced world"]
QUALIFIERS = {"may", "might", "can", "could", "potentially",
              "possibly", "sometimes", "generally", "tend", "tends"}
TRANSITIONS = {"however", "moreover", "furthermore", "additionally",
               "meanwhile", "ultimately", "overall", "consequently"}
SUPERLATIVES = [r"#1\b", r"\bnumber one\b", r"\blargest\b",
                r"\bbiggest\b", r"\bbest-rated\b", r"\btop-rated\b",
                r"\bmarket leader\b",
                r"\bleading (?:provider|platform|company|solution)\b",
                r"\bworld'?s (?:largest|biggest|first)\b"]
SUBSTANTIATION = ["according to", "survey", "report", "study",
                  "ranked", "ranking", "gartner", "forrester"]
PUFFERY = ["most comprehensive", "sets a new standard",
           "easiest-to-use", "best-in-class", "second to none"]
ALT_DEFAULTS = {"image", "photo", "picture", "pic", "graphic",
                "banner", "placeholder", "logo image"}
TOKEN_RES = [r"\{\{[^}]*\}\}", r"\$\{[^}]*\}", r"%s\b",
             r"\bundefined\b", r"\bNaN\b", r"\[object Object\]"]
PRICE_RE = re.compile(
    r"(Rs\.?|USD|PKR|EUR|GBP|\$|£|€)\s*(\d[\d,]*(?:\.\d+)?)",
    re.IGNORECASE)
BLOCKER_PAGE_WORDS = ("checkout", "pricing", "payment", "contact")


def fail_setup(msg):
    print(f"det-con-scan: setup error: {msg}", file=sys.stderr)
    sys.exit(2)


class Page:
    def __init__(self, path):
        self.path = path
        self.name = path.name
        parser = _Parser()
        parser.feed(path.read_text(encoding="utf-8", errors="replace"))
        self.title = parser.title.strip()
        self.text = _squash(" ".join(parser.text))
        self.prose = _squash(" ".join(parser.prose))
        self.headings = parser.headings            # [(tag, text)]
        self.paragraphs = [_squash(p) for p in parser.paragraphs if p.strip()]
        self.meta = parser.metas                   # key -> [content]
        self.alts = parser.alts                    # [alt or None]
        self.jsonld_raw = parser.jsonld            # [raw strings]
        self.jsonld = []
        for raw in self.jsonld_raw:
            try:
                self.jsonld.append(json.loads(raw))
            except (ValueError, TypeError):
                self.jsonld.append(None)
        self.words = self.text.split()

    @property
    def description(self):
        return (self.meta.get("description") or [""])[0]

    def og(self, key):
        return (self.meta.get(f"og:{key}") or [""])[0]


class _Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.code = 0
        self.text = []
        self.prose = []
        self.title = ""
        self.headings = []
        self.paragraphs = []
        self.metas = {}
        self.alts = []
        self.jsonld = []
        self._in_title = False
        self._htag = None
        self._hparts = []
        self._p_parts = None
        self._ld = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "script":
            if attrs.get("type") == "application/ld+json":
                self._ld = []
            else:
                self.skip += 1
        elif tag in ("style", "noscript"):
            self.skip += 1
        elif tag in ("code", "pre"):
            self.code += 1
        elif tag == "title":
            self._in_title = True
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._htag, self._hparts = tag, []
        elif tag == "p":
            self._p_parts = []
        elif tag == "meta":
            key = attrs.get("name") or attrs.get("property")
            if key and attrs.get("content") is not None:
                self.metas.setdefault(key.lower(), []).append(
                    attrs["content"])
        elif tag == "img":
            self.alts.append(attrs.get("alt"))

    def handle_endtag(self, tag):
        if tag == "script":
            if self._ld is not None:
                self.jsonld.append("".join(self._ld))
                self._ld = None
            elif self.skip:
                self.skip -= 1
        elif tag in ("style", "noscript") and self.skip:
            self.skip -= 1
        elif tag in ("code", "pre") and self.code:
            self.code -= 1
        elif tag == "title":
            self._in_title = False
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6") \
                and self._htag == tag:
            self.headings.append((tag, _squash(" ".join(self._hparts))))
            self._htag = None
        elif tag == "p" and self._p_parts is not None:
            self.paragraphs.append(" ".join(self._p_parts))
            self._p_parts = None

    def handle_data(self, data):
        if self._ld is not None:
            self._ld.append(data)
            return
        if self.skip:
            return
        if self._in_title:
            self.title += data
        if self._htag:
            self._hparts.append(data)
        if self._p_parts is not None:
            self._p_parts.append(data)
        self.text.append(data)
        if not self.code:
            self.prose.append(data)


def _squash(s):
    return re.sub(r"\s+", " ", s).strip()


def quote(text, start=0, length=110):
    snippet = text[max(0, start - 20):start + length]
    return snippet.strip().replace("\n", " ")


class Hits:
    def __init__(self):
        self.items = []   # (param, severity, page, evidence)
        self.notes = []   # copy notes (never fail)

    def add(self, param, severity, page, evidence):
        self.items.append((param, severity, page, evidence))

    def params_on(self, page):
        return {p for p, _s, pg, _e in self.items if pg == page}


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


# --- per-parameter checks -------------------------------------------------

def check_placeholders(pages, hits):
    for pg in pages:
        low = pg.text.lower()
        title_low = pg.title.lower()
        blockerish = any(w in pg.name.lower() for w in BLOCKER_PAGE_WORDS)
        for token in LOREM:
            if token in low or token in title_low:
                sev = "blocker" if blockerish else "major"
                hits.add("DET-CON-001", sev, pg.name,
                         f"lorem fragment {token!r} on page")
        for d in DEFAULTS:
            if d in low or d in title_low:
                hits.add("DET-CON-002", "major", pg.name,
                         f"template default {d!r}")
        for rx in TOKEN_RES:
            m = re.search(rx, pg.prose) or re.search(rx, pg.title)
            if m:
                hits.add("DET-CON-003", "major", pg.name,
                         f"template token {m.group(0)!r} in rendered copy")
        marker_scopes = [("body", low), ("meta description",
                                          pg.description.lower())]
        marker_scopes += [("alt text", a.lower())
                          for a in pg.alts if a]
        for scope, blob in marker_scopes:
            for marker in MARKERS:
                if marker in blob:
                    sev = "minor" if scope == "body" else "major"
                    hits.add("DET-CON-004", sev, pg.name,
                             f"marker {marker!r} in {scope}")
        for rx in CONTACT_PATTERNS:
            if re.search(rx, low):
                sev = "blocker" if blockerish else "major"
                hits.add("DET-CON-005", sev, pg.name,
                         f"placeholder contact pattern /{rx}/")


def check_copy_signals(pages, hits):
    for pg in pages:
        low = pg.text.lower()
        facts = extract_facts(pg.text)
        filler_hits = [f for f in FILLER if f in low]
        if filler_hits and not facts:
            sev = "major" if len(pg.words) < 60 else "minor"
            hits.add("DET-CON-006", sev, pg.name,
                     f"filler {filler_hits[0]!r} and no specific "
                     f"(number, price, date) anywhere on the page")
        terms = [t for t in CLUSTER_TERMS
                 if re.search(rf"\b{t}\b", low)]
        openers = [o for o in OPENERS if o in low]
        has_note = any("important to note" in o for o in openers)
        has_fast = any("fast-paced" in o for o in openers)
        if len(terms) >= 3 and has_note and has_fast:
            per_1000 = round(len(terms) / max(len(pg.words), 1) * 1000, 1)
            hits.add("DET-CON-007", "minor", pg.name,
                     f"cluster terms {terms} ({per_1000}/1000 words) "
                     f"with both stock openers")
        windows = 0
        toks = re.findall(r"[a-z']+", low)
        for i in range(len(toks)):
            window = toks[i:i + 5]
            if sum(1 for w in window if w in QUALIFIERS) >= 3:
                windows += 1
                hits.add("DET-CON-009", "minor", pg.name,
                         f"hedge stack: {' '.join(window)!r}")
                break
    # 008: identical heading-sequence + paragraph-count skeletons.
    sigs = {}
    for pg in pages:
        if len(pg.headings) >= 2:
            sig = (tuple(t for t, _x in pg.headings), len(pg.paragraphs))
            sigs.setdefault(sig, []).append(pg)
    for sig, group in sigs.items():
        if len(group) >= 3 and len({g.text for g in group}) > 1:
            names = ", ".join(g.name for g in group)
            for g in group:
                hits.add("DET-CON-008", "major", g.name,
                         f"page skeleton identical to {names}")
    # 007 corroboration upgrade: minor -> major when 008/009 share the page.
    upgraded = []
    for param, sev, page, ev in hits.items:
        if param == "DET-CON-007" and sev == "minor":
            others = hits.params_on(page) - {"DET-CON-007"}
            if others & {"DET-CON-008", "DET-CON-009"}:
                sev = "major"
                ev += " (corroborated)"
        upgraded.append((param, sev, page, ev))
    hits.items = upgraded


def check_consistency(pages, hits, fact_sheet):
    # 015: defined fact shapes with two or more values site-wide.
    shapes = [
        ("founding year", re.compile(
            r"(?:founded|established)(?:\s+in)?\s+((?:19|20)\d{2})",
            re.IGNORECASE)),
        ("team size", re.compile(
            r"team of\s+(\d+)|(\d+)\s+(?:employees|team members)",
            re.IGNORECASE)),
        ("user count", re.compile(
            r"([\d,]+)\+?\s+(?:users|customers|teams|accounts|"
            r"downloads|businesses)\b", re.IGNORECASE)),
    ]
    for label, rx in shapes:
        values = {}
        for pg in pages:
            for m in rx.finditer(pg.text):
                val = next(g for g in m.groups() if g)
                values.setdefault(val.replace(",", ""), set()).add(pg.name)
        if len(values) > 1:
            where = "; ".join(f"{v} on {sorted(ps)}"
                              for v, ps in sorted(values.items()))
            hits.add("DET-CON-015", "major", "(site)",
                     f"{label} stated inconsistently: {where}")
    # 016: prices per plan, and prices absent from the pricing page.
    pricing_pages = [pg for pg in pages
                     if "pricing" in pg.name.lower()
                     or "pricing" in pg.title.lower()]
    canonical = set()
    for pg in pricing_pages:
        canonical |= {k for k in extract_facts(pg.text)
                      if k.startswith("price:")}
    plan_prices = {}
    for pg in pages:
        page_prices = {k for k in extract_facts(pg.text)
                       if k.startswith("price:")}
        if pricing_pages and pg not in pricing_pages:
            for key in sorted(page_prices - canonical):
                hits.add("DET-CON-016", "blocker", pg.name,
                         f"price {key} does not appear on the "
                         f"pricing page")
        for m in PRICE_RE.finditer(pg.text):
            before = pg.text[max(0, m.start() - 60):m.start()]
            plan = re.findall(r"([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)?)"
                              r"\s*$", before.strip())
            if plan:
                plan_prices.setdefault(plan[0], set()).add(m.group(0))
    for plan, prices in sorted(plan_prices.items()):
        if len(prices) > 1:
            hits.add("DET-CON-016", "blocker", "(site)",
                     f"plan {plan!r} priced inconsistently: "
                     f"{sorted(prices)}")
    # 017: proper-noun variants (case/spacing/hyphenation drift).
    variants = {}
    for pg in pages:
        for sent in sentences(pg.text):
            words = sent.split()
            for i, w in enumerate(words):
                if i == 0:
                    continue
                if w[:1].isupper():
                    key = re.sub(r"[\s-]+", "", w.strip(".,;:()")).lower()
                    variants.setdefault(key, set()).add(
                        w.strip(".,;:()"))
    for key, forms in sorted(variants.items()):
        if len(forms) > 1:
            hits.add("DET-CON-017", "minor", "(site)",
                     f"name variants: {sorted(forms)}")
    # 018: stale dated copy.
    today = date.today()
    upcoming = ["register now", "join us", "upcoming", "book now",
                "sale ends", "early bird", "coming soon"]
    for pg in pages:
        low = pg.text.lower()
        for m in re.finditer(r"\b((?:19|20)\d{2})-(\d{2})-(\d{2})\b",
                             pg.text):
            try:
                d = date(int(m.group(1)), int(m.group(2)),
                         int(m.group(3)))
            except ValueError:
                continue
            if d < today and any(u in low for u in upcoming):
                hits.add("DET-CON-018", "major", pg.name,
                         f"past date {m.group(0)} presented with "
                         f"upcoming-event copy")
        for m in re.finditer(r"new for\s+((?:19|20)\d{2})", low):
            if int(m.group(1)) < today.year:
                hits.add("DET-CON-018", "major", pg.name,
                         f"'new for {m.group(1)}' on an evergreen page")
        for m in re.finditer(r"(?:©|copyright)\s*((?:19|20)\d{2})",
                             pg.text):
            if int(m.group(1)) <= today.year - 2:
                hits.add("DET-CON-018", "major", pg.name,
                         f"copyright year {m.group(1)} is stale")
    # 014: only with a fact sheet (claim-trace's engine).
    if fact_sheet is not None:
        sheet_text = fact_sheet.read_text(encoding="utf-8",
                                          errors="replace")
        sheet_facts = set(extract_facts(
            re.sub(r"\s+", " ", sheet_text)))
        for pg in pages:
            for key, surface in sorted(
                    extract_facts(pg.text).items()):
                if key not in sheet_facts:
                    sev = "blocker" if key.startswith("price:") \
                        else "major"
                    hits.add("DET-CON-014", sev, pg.name,
                             f"fact {surface!r} contradicts or is "
                             f"absent from the fact sheet")


def check_authorship(pages, hits):
    byline_re = re.compile(r"\bby\s+([A-Z][a-z]+\s+[A-Z][a-z]+)\b")
    authored = {}
    for pg in pages:
        authors = set(byline_re.findall(pg.text))
        for obj in pg.jsonld:
            if isinstance(obj, dict):
                author = obj.get("author")
                if isinstance(author, dict) and author.get("name"):
                    authors.add(author["name"])
                elif isinstance(author, str):
                    authors.add(author)
        for a in authors:
            authored.setdefault(a, []).append(pg)
    if len(authored) < 3:
        return "not run (fewer than three bylined authors)"
    flagged = []
    fingerprints = {}
    for author, pgs in authored.items():
        pg = pgs[0]
        first = pg.paragraphs[0] if pg.paragraphs else ""
        opener = first.split()[0].lower() if first.split() else ""
        transitions = {t for t in TRANSITIONS
                       if re.search(rf"\b{t}\b", pg.text.lower())}
        fingerprints[author] = (opener, frozenset(transitions))
    groups = {}
    for author, fp in fingerprints.items():
        groups.setdefault(fp, []).append(author)
    for fp, authors in groups.items():
        if len(authors) >= 3 and fp[1]:
            flagged.append(authors)
    for authors in flagged:
        hits.add("DET-CON-021", "major", "(site)",
                 f"authors {sorted(authors)} share an identical "
                 f"voice fingerprint (opener + transition set)")
    return None


def check_metadata(pages, hits):
    titles = {}
    for pg in pages:
        titles.setdefault(pg.title, []).append(pg)
        if not pg.title:
            hits.add("DET-CON-022", "major", pg.name, "missing <title>")
        if not pg.description:
            hits.add("DET-CON-022", "major", pg.name,
                     "missing meta description")
        for d in DEFAULTS:
            if d in pg.title.lower() or d in pg.description.lower():
                hits.add("DET-CON-022", "major", pg.name,
                         f"default string {d!r} in title/meta")
        h1 = next((t for tag, t in pg.headings if tag == "h1"), "")
        sig = {w.lower() for w in re.findall(r"[A-Za-z]{4,}", pg.title)}
        h1w = {w.lower() for w in re.findall(r"[A-Za-z]{4,}", h1)}
        if pg.title and h1 and not (sig & h1w):
            hits.add("DET-CON-022", "major", pg.name,
                     f"title {pg.title!r} shares no topic word with "
                     f"H1 {h1!r}")
        for m in PRICE_RE.finditer(pg.title + " " + pg.description):
            if m.group(0) not in pg.text:
                hits.add("DET-CON-022", "major", pg.name,
                         f"price {m.group(0)!r} promised in metadata "
                         f"but absent from the page")
        og_title, og_desc = pg.og("title"), pg.og("description")
        for d in DEFAULTS:
            if d in og_title.lower() or d in og_desc.lower():
                hits.add("DET-CON-023", "major", pg.name,
                         f"default string {d!r} in OG tags")
    og_titles, og_descs = {}, {}
    for pg in pages:
        if pg.og("title"):
            og_titles.setdefault(pg.og("title"), []).append(pg)
        if pg.og("description"):
            og_descs.setdefault(pg.og("description"), []).append(pg)
    for label, groups in (("og:title", og_titles),
                          ("og:description", og_descs)):
        for value, group in groups.items():
            if len(group) > 1 and len({g.title for g in group}) > 1:
                for g in group:
                    hits.add("DET-CON-023", "major", g.name,
                             f"{label} duplicated across pages with "
                             f"different titles: {value[:60]!r}")


def _walk_json(obj, out):
    if isinstance(obj, dict):
        for k, v in obj.items():
            out.append((k, v))
            _walk_json(v, out)
    elif isinstance(obj, list):
        for v in obj:
            _walk_json(v, out)


def check_jsonld(pages, hits):
    rating_cue = re.compile(
        r"(\d(?:\.\d)?\s*(?:/\s*5|stars?)|★|reviews?\b)", re.IGNORECASE)
    for pg in pages:
        fields = []
        for i, obj in enumerate(pg.jsonld):
            if obj is None:
                hits.add("DET-CON-024", "major", pg.name,
                         f"JSON-LD block {i + 1} does not parse")
                continue
            _walk_json(obj, fields)
        visible_prices = {norm_num(m.group(2))
                          for m in PRICE_RE.finditer(pg.text)}
        for key, value in fields:
            if key in ("aggregateRating", "ratingValue", "reviewCount") \
                    and not rating_cue.search(pg.text):
                hits.add("DET-CON-024", "blocker", pg.name,
                         f"JSON-LD {key}={value!r} with no rating or "
                         f"review visible on the page")
                break
        for key, value in fields:
            if key == "price" and isinstance(value, (str, int, float)):
                val = norm_num(str(value))
                if visible_prices and val not in visible_prices:
                    hits.add("DET-CON-024", "blocker", pg.name,
                             f"JSON-LD price {value!r} differs from "
                             f"visible prices {sorted(visible_prices)}")
                elif not visible_prices:
                    hits.add("DET-CON-024", "major", pg.name,
                             f"JSON-LD price {value!r} has no visible "
                             f"counterpart on the page")


def check_scale_and_claims(pages, hits):
    def shingles(text):
        words = re.findall(r"[a-z0-9']+", text.lower())
        return {" ".join(words[i:i + 5])
                for i in range(len(words) - 4)}
    shingle_sets = {pg.name: shingles(pg.text) for pg in pages}
    clustered = set()
    names = [pg.name for pg in pages]
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            sa, sb = shingle_sets[a], shingle_sets[b]
            if sa and sb:
                sim = len(sa & sb) / len(sa | sb)
                if sim >= 0.85:
                    clustered |= {a, b}
    if len(clustered) >= 3:
        for name in sorted(clustered):
            hits.add("DET-CON-025", "major", name,
                     f"near-duplicate cluster: {sorted(clustered)}")
    for pg in pages:
        for sent in sentences(pg.text):
            low = sent.lower()
            for rx in SUPERLATIVES:
                if re.search(rx, low) and not any(
                        cue in low for cue in SUBSTANTIATION):
                    hits.add("DET-CON-026", "major", pg.name,
                             f"unsubstantiated measurable claim: "
                             f"{quote(sent, 0, 90)!r}")
                    break
            for puff in PUFFERY:
                if puff in low:
                    hits.notes.append(
                        f"DET-CON-026 copy note ({pg.name}): "
                        f"unmeasurable puffery {puff!r}")
        for alt in pg.alts:
            if alt is None or alt == "":
                continue
            low = alt.strip().lower()
            if low in ALT_DEFAULTS or \
                    re.search(r"\.(?:jpe?g|png|gif|webp)$", low) or \
                    re.match(r"(?:dsc|img|pxl)_\d+", low) or \
                    low.count(",") >= 3:
                hits.add("DET-CON-027", "minor", pg.name,
                         f"alt text default/keyword string: {alt!r}")


def main():
    ap = argparse.ArgumentParser(
        description="DET-CON pre-publish scan over rendered pages "
                    "(gate G-CO-062). See the module docstring for "
                    "the parameters implemented and the ones that "
                    "stay manual.")
    ap.add_argument("--pages", required=True,
                    help="directory of rendered pages (or one HTML file)")
    ap.add_argument("--fact-sheet", default=None,
                    help="fact-sheet.md; enables the DET-CON-014 "
                         "fact-sheet diff")
    args = ap.parse_args()

    pages_arg = Path(args.pages)
    if pages_arg.is_file():
        files = [pages_arg]
    elif pages_arg.is_dir():
        files = sorted(p for p in pages_arg.rglob("*")
                       if p.suffix.lower() in (".html", ".htm")
                       and p.is_file())
    else:
        fail_setup(f"pages path not found: {pages_arg}")
    if not files:
        fail_setup(f"no HTML pages under {pages_arg}")
    fact_sheet = None
    if args.fact_sheet:
        fact_sheet = Path(args.fact_sheet)
        if not fact_sheet.is_file():
            fail_setup(f"fact sheet not found: {fact_sheet}")

    pages = [Page(f) for f in files]
    hits = Hits()
    check_placeholders(pages, hits)
    check_copy_signals(pages, hits)
    check_consistency(pages, hits, fact_sheet)
    not_run = []
    voice_note = check_authorship(pages, hits)
    if voice_note:
        not_run.append(f"DET-CON-021 {voice_note}")
    if fact_sheet is None:
        not_run.append("DET-CON-014 not run (no --fact-sheet given)")
    not_run.append("DET-CON-005 test-message send is manual")
    not_run.append("DET-CON-010-013, 019, 020, 028 are manual per "
                   "G-CO-062")
    check_metadata(pages, hits)
    check_jsonld(pages, hits)
    check_scale_and_claims(pages, hits)

    by_param = {}
    for param, sev, page, ev in hits.items:
        by_param.setdefault(param, []).append((sev, page, ev))
    for param in sorted(by_param):
        for sev, page, ev in by_param[param]:
            print(f"det-con-scan: HIT {param} [{sev}] {page}: {ev}")
    for note in hits.notes:
        print(f"det-con-scan: NOTE {note}")
    for note in not_run:
        print(f"det-con-scan: NOT-RUN {note}")
    blockers = sum(1 for _p, s, _pg, _e in hits.items if s == "blocker")
    majors = sum(1 for _p, s, _pg, _e in hits.items if s == "major")
    minors = sum(1 for _p, s, _pg, _e in hits.items if s == "minor")
    print(f"det-con-scan: {len(pages)} page(s); {blockers} blocker, "
          f"{majors} major, {minors} minor hit(s)")
    if blockers or majors:
        print("det-con-scan: FAIL (G-CO-062 pass requires zero "
              "blocker and zero unaddressed major hits)")
        return 1
    print("det-con-scan: PASS (zero blocker and zero major hits)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
