#!/usr/bin/env python3
"""Mutation sample behind the coverage gate -- serves gate G-QA-115.

Verifies QA-231: a coverage figure is only protection if the tests
assert. This script samples seeded faults (mutations) in covered
production code, runs the project's unit suite against each one in a
scratch copy of the tree, and counts how many faults the suite stays
green on ("survivors"). It exits non-zero when the survivors exceed the
allowance -- the suite is hollow no matter what its coverage says.

Config (default: <project>/scripts/qa/mutation-sample.json), JSON:

    {"suite": "shell command",       the unit-suite command, run in the
                                      (possibly mutated) tree; REQUIRED
     "allowance": 2,                 optional; survivors tolerated
     "mutations": [
        {"file": "src/calc.py",      path relative to the project root
         "find": "return a + b",     exact text; its FIRST occurrence in
                                      the file is replaced
         "replace": "return a - b",
         "description": "addition becomes subtraction"}]}

The allowance is resolved in this order: --allowance, the config's
"allowance", a "mutation allowance: N" line in the project's
TESTING.md, else 0. When more mutations are defined than --sample
asks for, the sample is drawn with a fixed seed (default 0) so runs
are reproducible; pass --seed to vary it.

The suite is first run once against an unmutated copy: a suite that
is already red cannot judge mutations, so that is a setup error.

Exit codes: 0 = survivors within the allowance; 1 = survivors exceed
the allowance, or a mutation could not be applied or its run errored;
2 = setup error (no config, no mutations, baseline suite red).
Standard library only.
"""

import argparse
import json
import random
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def fail_setup(msg):
    print(f"mutation_sample: setup error: {msg}", file=sys.stderr)
    sys.exit(2)


def run(cmd, cwd, timeout):
    try:
        proc = subprocess.run(
            cmd, shell=True, cwd=cwd, timeout=timeout,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
        )
        return proc.returncode, (proc.stdout or "").strip()
    except subprocess.TimeoutExpired:
        return None, f"timed out after {timeout}s"


def copy_tree(src, dst):
    shutil.copytree(
        src, dst,
        ignore=shutil.ignore_patterns(".git", "__pycache__", ".scratch"),
    )


def testing_md_allowance(project):
    testing = project / "TESTING.md"
    if not testing.is_file():
        return None
    for line in testing.read_text(encoding="utf-8").splitlines():
        if "mutation" in line.lower() and "allowance" in line.lower():
            match = re.search(r"\d+", line)
            if match:
                return int(match.group())
    return None


def main():
    ap = argparse.ArgumentParser(
        description="Run a mutation sample against a project's unit "
                    "suite (gate G-QA-115). See the module docstring "
                    "for the config format.")
    ap.add_argument("--project", default=".",
                    help="project tree to test (default: current "
                         "directory)")
    ap.add_argument("--config", default=None,
                    help="sample config (default: "
                         "<project>/scripts/qa/mutation-sample.json)")
    ap.add_argument("--sample", type=int, default=20,
                    help="number of mutations to apply (default: 20, "
                         "as in the gate's check command)")
    ap.add_argument("--allowance", type=int, default=None,
                    help="surviving faults tolerated (default: config, "
                         "then TESTING.md, then 0)")
    ap.add_argument("--seed", type=int, default=0,
                    help="sampling seed when mutations outnumber "
                         "--sample (default: 0)")
    ap.add_argument("--timeout", type=int, default=600,
                    help="per-suite-run timeout in seconds "
                         "(default: 600)")
    args = ap.parse_args()

    project = Path(args.project).resolve()
    if not project.is_dir():
        fail_setup(f"project directory not found: {project}")
    config_path = (Path(args.config).resolve() if args.config
                   else project / "scripts" / "qa" / "mutation-sample.json")
    if not config_path.is_file():
        fail_setup(f"config not found: {config_path}")
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail_setup(f"config unreadable: {exc}")
    suite = config.get("suite")
    if not suite:
        fail_setup("config has no 'suite' command; nothing to run")
    mutations = config.get("mutations")
    if not mutations:
        fail_setup("config has no 'mutations' entries; nothing to sample")

    allowance = args.allowance
    if allowance is None:
        allowance = config.get("allowance")
    if allowance is None:
        allowance = testing_md_allowance(project)
    if allowance is None:
        allowance = 0
        print("mutation_sample: no allowance given by flag, config, or "
              "TESTING.md; using 0")

    if len(mutations) > args.sample:
        chosen = random.Random(args.seed).sample(mutations, args.sample)
    else:
        chosen = list(mutations)

    scratch = Path(tempfile.mkdtemp(prefix="mutation-sample-"))

    baseline = scratch / "baseline"
    copy_tree(project, baseline)
    rc, out = run(suite, baseline, args.timeout)
    if rc != 0:
        shutil.rmtree(scratch, ignore_errors=True)
        fail_setup(f"baseline suite run is not green (exit {rc}); a red "
                   f"suite cannot judge mutations: {out[-300:]}")
    print(f"mutation_sample: baseline suite green; sampling "
          f"{len(chosen)} mutation(s), allowance {allowance}")

    survivors = []
    problems = []
    for i, mutation in enumerate(chosen, 1):
        label = (mutation.get("description")
                 or f"{mutation.get('file')}: "
                    f"{mutation.get('find')!r} -> "
                    f"{mutation.get('replace')!r}")
        work = scratch / f"mutant-{i}"
        copy_tree(project, work)
        target = work / str(mutation.get("file") or "")
        find = mutation.get("find")
        replace = mutation.get("replace")
        if not target.is_file() or find is None or replace is None:
            problems.append(f"{label}: bad mutation entry (file missing "
                            f"or find/replace absent)")
            print(f"[mutant {i}] ERROR: {label}: file/find/replace "
                  f"problem")
            continue
        text = target.read_text(encoding="utf-8")
        if find not in text:
            problems.append(f"{label}: 'find' text not present in "
                            f"{mutation.get('file')}; the mutation was "
                            f"never applied")
            print(f"[mutant {i}] ERROR: {label}: find text absent")
            continue
        target.write_text(text.replace(find, replace, 1),
                          encoding="utf-8")
        rc, out = run(suite, work, args.timeout)
        if rc is None:
            problems.append(f"{label}: suite run timed out")
            print(f"[mutant {i}] ERROR: {label}: suite timed out")
        elif rc == 0:
            survivors.append(label)
            print(f"[mutant {i}] SURVIVED: {label} (suite stayed green)")
        else:
            print(f"[mutant {i}] killed: {label} (suite exit {rc})")

    shutil.rmtree(scratch, ignore_errors=True)
    if problems:
        print(f"\nmutation_sample: FAIL ({len(problems)} problem(s))")
        for p in problems:
            print(f"  - {p}")
        return 1
    if len(survivors) > allowance:
        print(f"\nmutation_sample: FAIL ({len(survivors)} survivor(s) "
              f"exceed the allowance of {allowance}; the suite "
              f"stayed green on:")
        for s in survivors:
            print(f"  - {s}")
        return 1
    print(f"\nmutation_sample: PASS ({len(survivors)} survivor(s) within "
          f"the allowance of {allowance}, {len(chosen)} sampled)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
