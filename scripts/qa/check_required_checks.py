#!/usr/bin/env python3
"""Required-checks diff -- serves gate G-QA-112 (qa-gates skill).

Diffs the platform's required status checks against the required list
declared in TESTING.md (QA-224: the required-checks list is single-sourced;
any difference between the two lists is a defect). Exits non-zero on any
difference in either direction.

Platform side -- the first available source wins, and the script prints
which source it used:
  1. Platform API (GitHub): used when GITHUB_TOKEN and GITHUB_REPOSITORY
     (owner/repo) are set in the environment; reads the branch-protection
     required status checks for --branch.
  2. Snapshot file: --required-file (default <project>/.github/
     required-checks.txt), a checked-in export of the branch-protection
     list, one check name per line ('#' comments allowed).
  3. Workflow jobs: the job ids and display names defined in
     <project>/.github/workflows/*.yml -- the set of checks this repo can
     produce. This proves each required check exists and is runnable; it
     cannot see the branch-protection settings themselves.

TESTING.md side (exact parsing rules): the required-checks section
starts at the first heading whose text contains the word "required"
(case-insensitive) and runs until the next heading of the same or
higher level. Inside that section, EVERY backticked token on a line
counts as a check name -- in prose and in table cells, not only in
list items -- with two exceptions: a token that is exactly a gate ID
(G-XX-NNN) is skipped, and a line carrying no backticked token
contributes its bare list-item text (one name) when it is a list
item. The names are compared exactly, as the platform displays them:
a backticked command, file name, or other string written inside that
section is treated as a required check and diff-fails until it is
moved out of the section or the platform actually requires it.

Exit codes: 0 = the two lists are identical; 1 = differences found;
2 = setup error (no required section in TESTING.md, or no platform
source available). Standard library only.
"""

import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
BACKTICK = re.compile(r"`([^`]+)`")
LIST_ITEM = re.compile(r"^\s*(?:[-*]|\d+\.)\s+(.*)$")
GATE_ID = re.compile(r"^G-[A-Z]{2}-\d{3}$")


def fail_setup(msg):
    print(f"check_required_checks: setup error: {msg}", file=sys.stderr)
    sys.exit(2)


def declared_names(testing_path):
    """Check names declared in TESTING.md's required-checks section."""
    if not testing_path.is_file():
        fail_setup(f"TESTING.md not found: {testing_path}")
    lines = testing_path.read_text(encoding="utf-8").splitlines()
    names, in_section, level = [], False, None
    for line in lines:
        m = HEADING.match(line)
        if m:
            if in_section and len(m.group(1)) <= level:
                break
            if "required" in m.group(2).lower():
                in_section, level = True, len(m.group(1))
            continue
        if not in_section:
            continue
        tokens = BACKTICK.findall(line)
        if not tokens:
            item = LIST_ITEM.match(line)
            if item:
                tokens = [item.group(1).strip().strip("`")]
        for tok in tokens:
            tok = tok.strip()
            if tok and not GATE_ID.match(tok):
                names.append(tok)
    if not in_section:
        fail_setup("TESTING.md has no heading containing 'required'; "
                   "QA-224 needs the required status checks named there")
    if not names:
        fail_setup("the required section of TESTING.md names no status "
                   "checks (gate IDs alone cannot be diffed against the "
                   "platform list; name the checks as the platform "
                   "displays them)")
    return set(names)


def platform_names_api(branch):
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not (token and repo):
        return None
    url = (f"https://api.github.com/repos/{repo}/branches/{branch}"
           f"/protection/required_status_checks")
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as exc:  # offline, no protection, wrong repo...
        print(f"check_required_checks: platform API unavailable ({exc}); "
              f"falling back", file=sys.stderr)
        return None
    names = set(data.get("contexts") or [])
    for chk in data.get("checks") or []:
        if chk.get("context"):
            names.add(chk["context"])
    return names


def platform_names_snapshot(path):
    if not path.is_file():
        return None
    names = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            names.add(line)
    return names


def platform_names_workflows(project):
    wf_dir = project / ".github" / "workflows"
    files = sorted(wf_dir.glob("*.yml")) + sorted(wf_dir.glob("*.yaml"))
    if not files:
        return None
    names = set()
    for f in files:
        in_jobs, current = False, None
        for line in f.read_text(encoding="utf-8").splitlines():
            if re.match(r"^jobs:\s*$", line):
                in_jobs = True
                continue
            if in_jobs:
                if line and not line.startswith((" ", "\t", "#")):
                    break  # left the jobs block
                m = re.match(r"^  ([\w.-]+):\s*$", line)
                if m:
                    current = m.group(1)
                    names.add(current)
                    continue
                m = re.match(r"^    name:\s*(.+?)\s*$", line)
                if m and current:
                    names.add(m.group(1).strip("'\""))
    return names or None


def main():
    ap = argparse.ArgumentParser(
        description="Diff the platform's required status checks against "
                    "TESTING.md (gate G-QA-112). See the module docstring "
                    "for the platform sources, in priority order.")
    ap.add_argument("--project", default=".",
                    help="project tree (default: current directory)")
    ap.add_argument("--branch", default="main",
                    help="branch whose protection is read via the API "
                         "(default: main)")
    ap.add_argument("--required-file", default=None,
                    help="snapshot of the platform required-checks list "
                         "(default: <project>/.github/required-checks.txt)")
    args = ap.parse_args()

    project = Path(args.project).resolve()
    if not project.is_dir():
        fail_setup(f"project directory not found: {project}")

    declared = declared_names(project / "TESTING.md")

    snapshot = (Path(args.required_file).resolve() if args.required_file
                else project / ".github" / "required-checks.txt")
    platform, source = platform_names_api(args.branch), "platform API"
    if platform is None:
        platform, source = platform_names_snapshot(snapshot), \
            f"snapshot file {snapshot}"
    if platform is None:
        platform, source = platform_names_workflows(project), \
            "workflow job definitions"
    if platform is None:
        fail_setup("no platform source available: set GITHUB_TOKEN and "
                   "GITHUB_REPOSITORY, or provide a required-checks "
                   "snapshot, or define workflow jobs")

    print(f"check_required_checks: platform source = {source}")
    only_platform = sorted(platform - declared)
    only_declared = sorted(declared - platform)
    if only_platform or only_declared:
        print("check_required_checks: FAIL -- the lists differ (QA-224)")
        for n in only_platform:
            print(f"  required by platform, missing from TESTING.md: {n}")
        for n in only_declared:
            print(f"  declared in TESTING.md, not required by platform: {n}")
        return 1
    print(f"check_required_checks: PASS ({len(declared)} required "
          f"check(s), lists identical)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
