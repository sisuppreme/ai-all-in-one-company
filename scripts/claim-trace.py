#!/usr/bin/env python3
"""Claim-trace audit -- serves gate G-CO-061 (real-content skill, D9).

Extracts checkable facts from rendered pages and diffs them against the
project's fact-sheet.md: every fact a page states must trace to a
fact-sheet entry. A page fact with no fact-sheet counterpart is reported
as unmatched; a contradicted fact surfaces the same way, because the
page's value is the side that fails to trace (fix the copy or the stale
fact-sheet side, and record which was corrected -- G-CO-061).

Usage (the gate's command):

    python3 scripts/claim-trace.py --pages dist/ --fact-sheet fact-sheet.md

Extraction -- deterministic, and deliberately literal:

- Prices: currency-marked amounts (Rs, $, £, €, or a trailing/leading
  USD, PKR, EUR, GBP), normalized to (currency, amount).
- Percentages: "N%", normalized to the bare number.
- Dates: ISO dates, "Month D, YYYY", "D Month YYYY", and DD/MM/YYYY
  (a slash date whose first field is over 12 is read DD/MM; if the
  second field is over 12 it is read MM/DD; otherwise DD/MM), each
  normalized to ISO form. Standalone years are facts too.
- Numbers: every other standalone number (counts, limits, durations),
  normalized -- commas and trailing zeros removed, so 10,000, 10000
  and 10000.00 are the same fact.
- Names: capitalized multi-word sequences taken from <h1>-<h3>
  headings and from the name segment of <title> (the part before
  the first separator -- an em dash, |, :, or " - "; the tagline
  after a separator is a descriptor, not a name) -- where a page
  states its product, people, and place names -- with ordinary
  sentence words (The, Our, How, ...) stripped from the front.
  A name traces only if it appears verbatim in the fact sheet.

Page text is the visible text: <script>, <style>, and <noscript>
content is excluded; everything else a visitor reads is in scope,
including code samples printed on the page.

Exit codes: 0 = every extracted fact traces to the fact sheet;
1 = unmatched facts found; 2 = setup error (pages or fact sheet not
found, no HTML pages). Standard library only.
"""

import argparse
import re
import sys
from datetime import date
from decimal import Decimal, InvalidOperation
from html.parser import HTMLParser
from pathlib import Path

CUR = {"rs": "PKR", "rs.": "PKR", "pkr": "PKR", "$": "USD", "usd": "USD",
       "£": "GBP", "gbp": "GBP", "€": "EUR", "eur": "EUR",
       "dollars": "USD", "rupees": "PKR"}
PRICE_A = re.compile(
    r"(Rs\.?|USD|PKR|EUR|GBP|\$|£|€)\s*(\d[\d,]*(?:\.\d+)?)", re.IGNORECASE)
PRICE_B = re.compile(
    r"(\d[\d,]*(?:\.\d+)?)\s*(USD|PKR|EUR|GBP|dollars|rupees)\b",
    re.IGNORECASE)
PERCENT = re.compile(r"(\d[\d,]*(?:\.\d+)?)\s*%")
ISO_DATE = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
MONTHS = {m: i + 1 for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"])}
MONTH_ALT = "|".join(list(MONTHS) + [m[:3] for m in MONTHS])
DATE_MDY = re.compile(
    rf"\b({MONTH_ALT})\.?\s+(\d{{1,2}})(?:st|nd|rd|th)?,\s+(\d{{4}})\b",
    re.IGNORECASE)
DATE_DMY = re.compile(
    rf"\b(\d{{1,2}})(?:st|nd|rd|th)?\s+({MONTH_ALT})\.?,?\s+(\d{{4}})\b",
    re.IGNORECASE)
DATE_SLASH = re.compile(r"\b(\d{1,2})/(\d{1,2})/(\d{4})\b")
YEAR = re.compile(r"\b(?:19|20)\d{2}\b")
NUMBER = re.compile(r"\d[\d,]*(?:\.\d+)?")
NAME_SEQ = re.compile(r"(?:[A-Z][A-Za-z0-9&'’.-]*)(?:\s+[A-Z][A-Za-z0-9&'’.-]*)+")
STOPWORDS = {
    "The", "A", "An", "Our", "Your", "How", "Why", "What", "When",
    "Where", "Who", "Get", "Start", "Learn", "See", "Read", "More",
    "About", "Welcome", "Introducing", "Meet", "Discover", "Explore",
    "Build", "Create", "Make", "Try", "Join", "Sign", "Log", "Home",
    "Back", "Next", "Previous", "New", "Best", "Free", "Simple",
}


def fail_setup(msg):
    print(f"claim-trace: setup error: {msg}", file=sys.stderr)
    sys.exit(2)


def norm_num(s):
    try:
        return format(Decimal(s.replace(",", "")).normalize(), "f")
    except InvalidOperation:
        return s.replace(",", "")


def month_num(name):
    name = name.lower().rstrip(".")
    if name in MONTHS:
        return MONTHS[name]
    for full, num in MONTHS.items():
        if full.startswith(name):
            return num
    return None


def extract_facts(text):
    """Return {fact-key: first surface form} for one text blob."""
    facts = {}
    masked = list(text)

    def mask(m):
        for i in range(m.start(), m.end()):
            masked[i] = " "

    def add(key, surface):
        facts.setdefault(key, surface.strip())

    work = text
    for m in PRICE_A.finditer(work):
        cur = CUR[m.group(1).lower()]
        add(f"price:{cur}:{norm_num(m.group(2))}", m.group(0))
        mask(m)
    for m in PRICE_B.finditer(work):
        cur = CUR[m.group(2).lower()]
        add(f"price:{cur}:{norm_num(m.group(1))}", m.group(0))
        mask(m)
    work = "".join(masked)
    for m in PERCENT.finditer(work):
        add(f"percent:{norm_num(m.group(1))}", m.group(0))
        mask(m)
    work = "".join(masked)
    for m in ISO_DATE.finditer(work):
        add(f"date:{m.group(1)}-{m.group(2)}-{m.group(3)}", m.group(0))
        mask(m)
    work = "".join(masked)
    for rx, order in ((DATE_MDY, "mdy"), (DATE_DMY, "dmy")):
        for m in rx.finditer(work):
            if order == "mdy":
                mon, day, year = month_num(m.group(1)), int(m.group(2)), m.group(3)
            else:
                day, mon, year = int(m.group(1)), month_num(m.group(2)), m.group(3)
            if mon:
                try:
                    iso = date(int(year), mon, day).isoformat()
                except ValueError:
                    continue
                add(f"date:{iso}", m.group(0))
                mask(m)
        work = "".join(masked)
    for m in DATE_SLASH.finditer(work):
        a, b, year = int(m.group(1)), int(m.group(2)), m.group(3)
        day, mon = (a, b) if a > 12 or b <= 12 else (b, a)
        if a <= 12 and b > 12:
            day, mon = b, a
        try:
            iso = date(int(year), mon, day).isoformat()
        except ValueError:
            continue
        add(f"date:{iso}", m.group(0))
        mask(m)
    work = "".join(masked)
    for m in YEAR.finditer(work):
        add(f"year:{m.group(0)}", m.group(0))
        mask(m)
    work = "".join(masked)
    for m in NUMBER.finditer(work):
        add(f"num:{norm_num(m.group(0))}", m.group(0))
    return facts


def extract_names(title, headings):
    names = set()
    name_segment = re.split(r"\s+(?:—|\||·|:|-)\s+|\s+—\s*", title)[0]
    for blob in [name_segment] + headings:
        for m in NAME_SEQ.finditer(blob):
            words = m.group(0).split()
            while words and words[0] in STOPWORDS:
                words.pop(0)
            if len(words) >= 2:
                names.add(" ".join(words))
    return names


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip_depth = 0
        self.text = []
        self.title = ""
        self.headings = []
        self._in_title = False
        self._heading_tag = None
        self._heading_parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self.skip_depth += 1
        elif tag == "title":
            self._in_title = True
        elif tag in ("h1", "h2", "h3"):
            self._heading_tag = tag
            self._heading_parts = []

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript") and self.skip_depth:
            self.skip_depth -= 1
        elif tag == "title":
            self._in_title = False
        elif tag in ("h1", "h2", "h3") and self._heading_tag == tag:
            self.headings.append(" ".join(self._heading_parts))
            self._heading_tag = None

    def handle_data(self, data):
        if self.skip_depth:
            return
        if self._in_title:
            self.title += data
        if self._heading_tag:
            self._heading_parts.append(data)
        self.text.append(data)


def page_facts(path):
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    text = re.sub(r"\s+", " ", " ".join(parser.text))
    facts = extract_facts(text)
    return facts, extract_names(parser.title.strip(), parser.headings)


def main():
    ap = argparse.ArgumentParser(
        description="Claim-trace audit: every fact on the rendered "
                    "pages must trace to fact-sheet.md (gate G-CO-061). "
                    "See the module docstring for the extraction rules.")
    ap.add_argument("--pages", required=True,
                    help="directory of rendered pages (or one HTML file)")
    ap.add_argument("--fact-sheet", required=True,
                    help="path to the project's fact-sheet.md")
    args = ap.parse_args()

    sheet_path = Path(args.fact_sheet)
    if not sheet_path.is_file():
        fail_setup(f"fact sheet not found: {sheet_path}")
    sheet_text = sheet_path.read_text(encoding="utf-8", errors="replace")
    sheet_facts = set(extract_facts(re.sub(r"\s+", " ", sheet_text)))

    pages_arg = Path(args.pages)
    if pages_arg.is_file():
        pages = [pages_arg]
    elif pages_arg.is_dir():
        pages = sorted(p for p in pages_arg.rglob("*")
                       if p.suffix.lower() in (".html", ".htm")
                       and p.is_file())
    else:
        fail_setup(f"pages path not found: {pages_arg}")
    if not pages:
        fail_setup(f"no HTML pages under {pages_arg}")

    total_unmatched = 0
    for page in pages:
        facts, names = page_facts(page)
        unmatched = []
        for key, surface in sorted(facts.items()):
            if key not in sheet_facts:
                unmatched.append(f"fact {surface!r} ({key})")
        for name in sorted(names):
            if name not in sheet_text:
                unmatched.append(f"name {name!r} (title/heading)")
        if unmatched:
            total_unmatched += len(unmatched)
            print(f"claim-trace: {page}: {len(unmatched)} unmatched "
                  f"fact(s)")
            for u in unmatched:
                print(f"  - {u}")
    if total_unmatched:
        print(f"claim-trace: FAIL ({total_unmatched} unmatched fact(s) "
              f"across {len(pages)} page(s); G-CO-061)")
        return 1
    print(f"claim-trace: PASS ({len(pages)} page(s), every extracted "
          f"fact traces to {sheet_path.name})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
