#!/usr/bin/env python3
"""Bypass and quarantine ledger audit -- serves gate G-QA-114 (qa-gates).

Verifies QA-227 and QA-228: every gate bypass is logged with who and
why, quarantine entries are owned and unexpired (or resolved, or
formally extended), and a release whose bypass count rose over the
previous release links the quality finding the rise produced.

Ledger (default: <project>/scripts/qa/gate-ledger.json), JSON:

    {"releases": [
        {"release": "1.2.0",
         "quality_finding": "QF-2026-014",   optional; REQUIRED when this
                            release's bypass count exceeds the previous
                            release's (a per-bypass "quality_finding"
                            field also satisfies the link)
         "bypasses": [
            {"gate": "G-QA-112",             gate that was bypassed
             "who":  "name",                 REQUIRED, non-empty
             "why":  "reason",               REQUIRED, non-empty
             "when": "2026-11-01"}],
         "quarantine": [
            {"item": "e2e checkout test",    gate or test quarantined
             "owner": "name",                REQUIRED (QA-228)
             "expires": "2026-12-01",        REQUIRED (QA-228)
             "status": "open",               open | resolved | extended
             "resolution": "...",            required when resolved
             "extended_to": "2027-01-15",    required when extended
             "extension_reason": "..."}]}    required when extended
    ]}

Releases are compared in the order listed (oldest first). An entry is
expired when its expiry date is before --today and it is neither
resolved nor extended to a date on/after --today with a stated reason.
Expired entries fail the run only under --fail-on-expired (the gate's
invocation); without the flag they are reported as warnings. Bypasses
missing who/why and an unlinked bypass-count rise always fail.

Exit codes: 0 = ledger clean; 1 = audit failures; 2 = setup error (no
ledger, unreadable ledger, no releases). Standard library only.
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path


def fail_setup(msg):
    print(f"gate_ledger: setup error: {msg}", file=sys.stderr)
    sys.exit(2)


def parse_date(value):
    try:
        return date.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None


def main():
    ap = argparse.ArgumentParser(
        description="Audit a project's bypass/quarantine ledger "
                    "(gate G-QA-114). See the module docstring for the "
                    "ledger format.")
    ap.add_argument("--project", default=".",
                    help="project tree (default: current directory)")
    ap.add_argument("--ledger", default=None,
                    help="ledger file (default: "
                         "<project>/scripts/qa/gate-ledger.json)")
    ap.add_argument("--fail-on-expired", action="store_true",
                    help="fail the run on expired quarantine entries "
                         "(without it they are warnings)")
    ap.add_argument("--today", default=None,
                    help="override today's date (YYYY-MM-DD), for tests")
    args = ap.parse_args()

    today = parse_date(args.today) if args.today else date.today()
    if today is None:
        fail_setup(f"--today is not a YYYY-MM-DD date: {args.today}")

    project = Path(args.project).resolve()
    if not project.is_dir():
        fail_setup(f"project directory not found: {project}")
    ledger_path = (Path(args.ledger).resolve() if args.ledger
                   else project / "scripts" / "qa" / "gate-ledger.json")
    if not ledger_path.is_file():
        fail_setup(f"ledger not found: {ledger_path}")
    try:
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail_setup(f"ledger unreadable: {exc}")
    releases = ledger.get("releases")
    if not releases:
        fail_setup("ledger has no 'releases' entries; nothing to audit")

    failures = []
    warnings = []

    for rel in releases:
        name = rel.get("release", "<unnamed release>")
        for i, bypass in enumerate(rel.get("bypasses") or [], 1):
            gate = bypass.get("gate", f"bypass-{i}")
            for field in ("who", "why"):
                if not str(bypass.get(field) or "").strip():
                    failures.append(
                        f"{name}: bypass of {gate} lacks '{field}' "
                        f"(QA-227: bypasses are logged with who and why)")
        for entry in rel.get("quarantine") or []:
            item = entry.get("item", "<unnamed item>")
            if not str(entry.get("owner") or "").strip():
                failures.append(
                    f"{name}: quarantine '{item}' has no owner (QA-228)")
            expires = parse_date(entry.get("expires"))
            if expires is None:
                failures.append(
                    f"{name}: quarantine '{item}' has no valid 'expires' "
                    f"date (QA-228)")
                continue
            status = str(entry.get("status") or "open").lower()
            if status == "resolved":
                if not str(entry.get("resolution") or "").strip():
                    failures.append(
                        f"{name}: quarantine '{item}' is marked resolved "
                        f"with no resolution recorded")
                continue
            effective = expires
            if status == "extended":
                extended_to = parse_date(entry.get("extended_to"))
                reason = str(entry.get("extension_reason") or "").strip()
                if extended_to is None or not reason:
                    failures.append(
                        f"{name}: quarantine '{item}' is marked extended "
                        f"without a valid 'extended_to' date and an "
                        f"'extension_reason' (a justified extension, "
                        f"QA-228)")
                    continue
                effective = extended_to
            if effective < today:
                msg = (f"{name}: quarantine '{item}' expired on "
                       f"{effective.isoformat()} without resolution "
                       f"(QA-228)")
                if args.fail_on_expired:
                    failures.append(msg)
                else:
                    warnings.append(msg + " [warning only; "
                                          "--fail-on-expired not given]")

    counts = [len(rel.get("bypasses") or []) for rel in releases]
    if len(releases) >= 2 and counts[-1] > counts[-2]:
        latest = releases[-1]
        name = latest.get("release", "<unnamed release>")
        linked = str(latest.get("quality_finding") or "").strip() or any(
            str(b.get("quality_finding") or "").strip()
            for b in latest.get("bypasses") or [])
        if not linked:
            failures.append(
                f"{name}: bypass count rose over the previous release "
                f"({counts[-2]} -> {counts[-1]}) with no linked quality "
                f"finding (QA-227: a rising count is itself a finding)")

    for w in warnings:
        print(f"gate_ledger: warning: {w}")
    if failures:
        print(f"\ngate_ledger: FAIL ({len(failures)} problem(s))")
        for f in failures:
            print(f"  - {f}")
        return 1
    total_b = sum(counts)
    total_q = sum(len(r.get("quarantine") or []) for r in releases)
    print(f"gate_ledger: PASS ({len(releases)} release(s), {total_b} "
          f"bypass(es), {total_q} quarantine entr(ies) audited)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
