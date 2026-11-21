#!/usr/bin/env python3
"""Gate provenance and waiver check -- serves gate G-QA-113 (qa-gates).

Two checks:

1. Same-change provenance (the gate's core; QA-222, QA-223). Over the
   commit range --base..HEAD, any commit that changes BOTH a gate-config
   or threshold file AND gated code in the same commit requires a waiver
   entry in the project log. A waiver entry is a passage in the log that
   contains the word "waiver", a named owner ("owner: NAME" or
   "owner NAME"), an expiry ("expires YYYY-MM-DD" or "until YYYY-MM-DD")
   that has not passed, and a reference to the changed config file (its
   basename) or to the commit's short SHA. Threshold changes committed
   alone, predating the code they gate, need no waiver.

   Gate-config / threshold files are matched by --config-glob patterns
   (repeatable; the defaults cover TESTING.md, budget files, Lighthouse
   config, workflow files, scripts/qa/, gates/ and any *threshold* file).
   progress.md and DECISIONS.md never count as gated code.

   Waiver window (exact): the passage examined for one waiver is the
   log line containing the word "waiver" plus the three lines that
   follow it -- a four-line window. The owner, the expiry, and the
   reference must ALL fall inside that one window; an owner named
   five lines below the word "waiver" covers nothing. The reference
   may be the changed config file's basename, the commit's short
   SHA, or the word "threshold" anywhere in the window. A waiver
   whose expiry has passed is ignored, and a passage missing an
   owner or an expiry is ignored too -- neither is a violation by
   itself; it simply covers nothing. Only the scanned log files are
   searched (--log, repeatable; by default progress.md and
   DECISIONS.md, whichever exist).

2. Log trace (--log-trace). Every gate result recorded in the project log
   (a line naming a gate ID G-XX-NNN together with a result word such as
   PASS, FAIL or WAIVED) must trace to a gate ID defined in the skills
   tree (--skills-dir, default: the skills/ directory of the repo this
   script ships in).

Exit codes: 0 = no unwaived same-change commits (and, with --log-trace,
no orphan gate results); 1 = violations found; 2 = setup error (not a
git repository, unresolvable base ref, no log). Standard library only
(git is invoked as a subprocess).
"""

import argparse
import datetime
import fnmatch
import re
import subprocess
import sys
from pathlib import Path

GATE_ID = re.compile(r"G-[A-Z]{2}-\d{3}")
RESULT_WORD = re.compile(r"\b(PASS|PASSED|FAIL|FAILED|WAIVED|GREEN|RED)\b",
                         re.IGNORECASE)
OWNER = re.compile(r"owner[:\s]+([A-Za-z][\w.'-]*(?:\s+[A-Za-z][\w.'-]*)?)",
                   re.IGNORECASE)
EXPIRY = re.compile(r"(?:expires|expiry|until)[:\s]*(\d{4}-\d{2}-\d{2})",
                    re.IGNORECASE)
LOG_BASENAMES = {"progress.md", "decisions.md"}

DEFAULT_GLOBS = [
    "TESTING.md", "budget.json", "**/budget.json", "lighthouserc*",
    "**/lighthouserc*", ".github/workflows/*", "scripts/qa/*",
    "gates/*", "**/*threshold*", "**/thresholds/*",
]


def fail_setup(msg):
    print(f"check_gate_provenance: setup error: {msg}", file=sys.stderr)
    sys.exit(2)


def git(project, *argv):
    proc = subprocess.run(["git", "-C", str(project), *argv],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          text=True)
    if proc.returncode != 0:
        fail_setup(f"git {' '.join(argv)} failed: {proc.stderr.strip()}")
    return proc.stdout


def resolve_base(project, base):
    if base:
        return base
    for cand in ("origin/main", "origin/master", "main", "master"):
        proc = subprocess.run(
            ["git", "-C", str(project), "merge-base", "HEAD", cand],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if proc.returncode == 0 and proc.stdout.strip():
            return proc.stdout.strip()
    proc = subprocess.run(["git", "-C", str(project), "rev-list", "--max-parents=0", "HEAD"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          text=True)
    if proc.returncode == 0 and proc.stdout.strip():
        return proc.stdout.strip().splitlines()[0]
    fail_setup("could not resolve a base ref; pass --base")


def commits_in_range(project, base):
    out = git(project, "log", "--no-merges",
              "--format=COMMIT%x09%H%x09%ct", "--name-only",
              f"{base}..HEAD")
    commits, current = [], None
    for line in out.splitlines():
        if line.startswith("COMMIT\t"):
            _, sha, ts = line.split("\t")
            current = {"sha": sha, "ts": int(ts), "files": []}
            commits.append(current)
        elif line.strip() and current is not None:
            current["files"].append(line.strip())
    return commits


def is_config(path, globs):
    return any(fnmatch.fnmatch(path, g) or
               fnmatch.fnmatch("/" + path, g) for g in globs)


def find_waivers(log_texts):
    """Waiver entries: (owner, expiry-date, passage-text) tuples."""
    waivers = []
    today = datetime.date.today()
    for text in log_texts:
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if "waiver" not in line.lower():
                continue
            passage = "\n".join(lines[i:i + 4])
            owner = OWNER.search(passage)
            expiry = EXPIRY.search(passage)
            if not owner or not expiry:
                continue
            try:
                exp = datetime.date.fromisoformat(expiry.group(1))
            except ValueError:
                continue
            if exp >= today:
                waivers.append((owner.group(1).strip(), exp, passage))
    return waivers


def main():
    ap = argparse.ArgumentParser(
        description="Check gate-config provenance and waivers over a "
                    "commit range (gate G-QA-113). See the module "
                    "docstring for the waiver-entry format.")
    ap.add_argument("--project", default=".",
                    help="git project to check (default: current directory)")
    ap.add_argument("--base", default=None,
                    help="base ref for the range base..HEAD (default: "
                         "merge-base with origin/main or main, else the "
                         "root commit)")
    ap.add_argument("--log", action="append", default=None,
                    help="project log file to scan for waivers "
                         "(repeatable; default: progress.md and "
                         "DECISIONS.md in the project, whichever exist)")
    ap.add_argument("--config-glob", action="append", default=None,
                    help="glob for gate-config/threshold files "
                         "(repeatable; replaces the defaults)")
    ap.add_argument("--log-trace", action="store_true",
                    help="also verify that gate results recorded in the "
                         "log trace to gate IDs defined in the skills tree")
    ap.add_argument("--skills-dir", default=None,
                    help="skills tree for --log-trace (default: the "
                         "skills/ directory of the repo shipping this "
                         "script)")
    args = ap.parse_args()

    project = Path(args.project).resolve()
    if not (project / ".git").exists():
        fail_setup(f"not a git repository: {project}")

    log_paths = [Path(p) for p in args.log] if args.log else [
        p for p in (project / "progress.md", project / "DECISIONS.md")
        if p.is_file()]
    if not log_paths:
        fail_setup("no project log found (progress.md / DECISIONS.md); "
                   "waivers have nowhere to live (QA-223)")
    log_texts = [p.read_text(encoding="utf-8") for p in log_paths]

    globs = args.config_glob or DEFAULT_GLOBS
    base = resolve_base(project, args.base)
    commits = commits_in_range(project, base)
    waivers = find_waivers(log_texts)

    violations = []
    for commit in commits:
        config_files = [f for f in commit["files"] if is_config(f, globs)]
        code_files = [f for f in commit["files"]
                      if not is_config(f, globs)
                      and Path(f).name.lower() not in LOG_BASENAMES]
        if not config_files or not code_files:
            continue
        short = commit["sha"][:7]
        covered = any(
            short in passage
            or any(Path(f).name in passage for f in config_files)
            or "threshold" in passage.lower()
            for _, _, passage in waivers)
        if not covered:
            violations.append(
                f"{short}: gate-config {config_files} changed together "
                f"with gated code {code_files[:3]} and no unexpired "
                f"waiver with a named owner covers it")
    for v in violations:
        print(f"check_gate_provenance: VIOLATION: {v}")

    trace_failures = []
    if args.log_trace:
        skills_dir = (Path(args.skills_dir).resolve() if args.skills_dir
                      else Path(__file__).resolve().parents[2] / "skills")
        if not skills_dir.is_dir():
            fail_setup(f"skills directory not found: {skills_dir}")
        defined = set()
        for skill in skills_dir.rglob("SKILL.md"):
            defined |= set(GATE_ID.findall(
                skill.read_text(encoding="utf-8")))
        for path, text in zip(log_paths, log_texts):
            for lineno, line in enumerate(text.splitlines(), 1):
                ids = GATE_ID.findall(line)
                if ids and RESULT_WORD.search(line):
                    for gid in ids:
                        if gid not in defined:
                            trace_failures.append(
                                f"{path.name}:{lineno}: recorded result "
                                f"for {gid}, which no skill defines")
        for f_ in trace_failures:
            print(f"check_gate_provenance: TRACE: {f_}")

    if violations or trace_failures:
        print(f"check_gate_provenance: FAIL ({len(violations)} unwaived "
              f"same-change commit(s), {len(trace_failures)} orphan "
              f"gate result(s))")
        return 1
    print(f"check_gate_provenance: PASS ({len(commits)} commit(s) in "
          f"range, {len(waivers)} unexpired waiver(s) on record"
          + (", log trace clean)" if args.log_trace else ")"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
