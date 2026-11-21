#!/usr/bin/env python3
"""Validate SKILL.md files against the §5.4 format (MASTER_BRIEF.md).

Usage: python3 scripts/validate-skills.py [skills/<dept-slug> ...]
With no arguments, validates every department folder under skills/ (except detection/).

Checks per skill: folder + examples/ present; >=3 example files each with Before/After;
section presence and order; <=400 lines; rule/gate/BAN IDs inside the skill's
RULE_ID_REGISTRY.md block and unique repo-wide; >=3 gates; every BAN entry cites a
DET parameter and a replacement; recall anchors <=5.
Exit code 0 = all pass, 1 = failures found.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SECTIONS = ["## Metadata", "## When to use / Do NOT use", "## Rules", "## BAN list",
            "## Gates", "## Anti-patterns", "## Examples", "## Recall anchors", "## Checklist"]

def registry_blocks():
    reg = (ROOT / "docs" / "RULE_ID_REGISTRY.md").read_text()
    blocks = {}  # skill -> (code, rlo, rhi, glo, ghi, blo, bhi)
    for m in re.finditer(r"\| ([\w-]+) \| ([A-Z]{2})-(\d+)–[A-Z]{2}-(\d+) \| G-[A-Z]{2}-(\d+)–[A-Z]{2}-(\d+) \| BAN-[A-Z]{2}-(\d+)–[A-Z]{2}-(\d+) \|", reg):
        s, code, rlo, rhi, glo, ghi, blo, bhi = m.groups()
        blocks[s] = (code, int(rlo), int(rhi), int(glo), int(ghi), int(blo), int(bhi))
    return blocks

def main():
    targets = [pathlib.Path(a) for a in sys.argv[1:]] or sorted(
        p for p in (ROOT / "skills").iterdir() if p.is_dir() and p.name != "detection")
    blocks = registry_blocks()
    seen_ids, failures, checked = set(), [], 0
    for dept in targets:
        for skill_dir in sorted(p for p in dept.iterdir() if p.is_dir()):
            name = skill_dir.name
            f = skill_dir / "SKILL.md"
            if name not in blocks:
                failures.append(f"{name}: not in RULE_ID_REGISTRY.md"); continue
            if not f.exists():
                failures.append(f"{name}: SKILL.md missing"); continue
            checked += 1
            code, rlo, rhi, glo, ghi, blo, bhi = blocks[name]
            text = f.read_text()
            lines = text.splitlines()
            if len(lines) > 400:
                failures.append(f"{name}: {len(lines)} lines > 400 cap")
            pos = [text.find(s) for s in SECTIONS]
            if -1 in pos:
                failures.append(f"{name}: missing section(s): {[SECTIONS[i] for i,p in enumerate(pos) if p==-1]}")
            elif pos != sorted(pos):
                failures.append(f"{name}: sections out of order")
            def section(a, b):
                i = text.find(a)
                j = text.find(b) if b else len(text)
                return text[i:j] if i != -1 else ""
            rules_sec = section("## Rules", "## BAN list")
            ban_sec = section("## BAN list", "## Gates")
            gates_sec = section("## Gates", "## Anti-patterns")
            def defs(sec, pat):
                return [int(n) for n in re.findall(pat, sec)]
            for label, found, lo, hi in [
                ("rule", defs(rules_sec, rf"\*\*{code}-(\d{{3}})"), rlo, rhi),
                ("gate", defs(gates_sec, rf"\*\*G-{code}-(\d{{3}})"), glo, ghi),
                ("BAN", defs(ban_sec, rf"\*\*BAN-{code}-(\d{{3}})"), blo, bhi)]:
                if len(found) != len(set(found)):
                    failures.append(f"{name}: duplicate {label} definitions inside the skill")
                for n in found:
                    key = f"{label}:{code}-{n:03d}"
                    if key in seen_ids:
                        failures.append(f"{name}: duplicate {label} ID {code}-{n:03d} (also defined elsewhere)")
                    seen_ids.add(key)
                    if not (lo <= n <= hi):
                        failures.append(f"{name}: {label} ID {code}-{n:03d} outside block {lo:03d}-{hi:03d}")
            gates = set(re.findall(rf"G-{code}-\d{{3}}", gates_sec))
            if len(gates) < 3:
                failures.append(f"{name}: only {len(gates)} gates (<3)")
            ban_section = ban_sec
            n_bans = len(set(re.findall(rf"BAN-{code}-\d{{3}}", ban_section)))
            if ban_section.count("Defeats: DET-") < len(set(re.findall(rf"BAN-{code}-\d{{3}}", ban_section))):
                failures.append(f"{name}: a BAN entry lacks a 'Defeats: DET-' reference")
            if ban_section.count("Instead:") < len(set(re.findall(rf"BAN-{code}-\d{{3}}", ban_section))):
                failures.append(f"{name}: a BAN entry lacks an 'Instead:' replacement")
            anchors = text[text.find("## Recall anchors"):text.find("## Checklist")]
            n_anchors = len([l for l in anchors.splitlines() if l.startswith("- ")])
            if n_anchors > 5:
                failures.append(f"{name}: {n_anchors} recall anchors (>5)")
            ex = skill_dir / "examples"
            ex_files = sorted(ex.glob("*.md")) if ex.exists() else []
            if len(ex_files) < 3:
                failures.append(f"{name}: only {len(ex_files)} example files (<3)")
            for ef in ex_files:
                et = ef.read_text()
                if "Before" not in et or "After" not in et:
                    failures.append(f"{name}: {ef.name} lacks Before/After")
    print(f"Checked {checked} skills. {'ALL PASS' if not failures else f'{len(failures)} FAILURE(S):'}")
    for x in failures:
        print(" -", x)
    return 0 if not failures else 1

if __name__ == "__main__":
    sys.exit(main())
