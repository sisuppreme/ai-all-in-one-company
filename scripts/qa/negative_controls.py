#!/usr/bin/env python3
"""Negative-control runner -- serves gate G-QA-111 (qa-gates skill).

Verifies that a project's gates actually bite (QA-225, QA-226): for each
negative control in the manifest, the project tree is copied to a scratch
directory, the seeded fault is applied there, and the gate command is run.
A gate command that exits 0 while its own seeded fault is present is not
protection; this script exits non-zero and names it.

Manifest (default: <project>/scripts/qa/negative-controls.json), JSON:

    {"controls": [
        {"gate":  "G-XX-NNN",          gate the control belongs to
         "fault": "what is seeded",    human description of the fault
         "apply": "shell command",     run in the scratch copy to seed the
                                       fault; omit when the tree is already
                                       seeded (e.g. a --branch checkout)
         "check": "shell command"}     the gate command; it MUST exit
                                       non-zero with the fault present
    ]}

Gate IDs mentioned in the project's TESTING.md that have no control in the
manifest are reported as gates lacking a negative control; they fail the
run unless --allow-missing is given.

With --branch BRANCH the project is first cloned at that branch into the
scratch area (the seeded-faults branch of G-QA-111's nightly job) and the
controls run against that checkout.

Exit codes: 0 = every gate went red on its fault and no gate lacks a
control; 1 = a gate stayed green on its fault, a control errored, or a
gate lacks a control; 2 = setup error (no manifest, no controls, bad
project). Standard library only.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

GATE_ID = re.compile(r"G-[A-Z]{2}-\d{3}")


def fail_setup(msg):
    print(f"negative_controls: setup error: {msg}", file=sys.stderr)
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


def main():
    ap = argparse.ArgumentParser(
        description="Run seeded-fault negative controls against a project's "
                    "gates (gate G-QA-111). See the module docstring for the "
                    "manifest format.")
    ap.add_argument("--project", default=".",
                    help="project tree to test (default: current directory)")
    ap.add_argument("--manifest", default=None,
                    help="controls manifest (default: "
                         "<project>/scripts/qa/negative-controls.json)")
    ap.add_argument("--branch", default=None,
                    help="clone the project at this branch first (the "
                         "seeded-faults branch) and run controls there")
    ap.add_argument("--allow-missing", action="store_true",
                    help="only warn about TESTING.md gates that have no "
                         "negative control, instead of failing")
    ap.add_argument("--timeout", type=int, default=300,
                    help="per-command timeout in seconds (default: 300)")
    args = ap.parse_args()

    project = Path(args.project).resolve()
    if not project.is_dir():
        fail_setup(f"project directory not found: {project}")

    scratch = Path(tempfile.mkdtemp(prefix="negative-controls-"))
    tree = project
    if args.branch:
        tree = scratch / "checkout"
        rc, out = run(f"git clone --quiet --branch {args.branch} "
                      f"{project} {tree}", scratch, args.timeout)
        if rc != 0:
            fail_setup(f"could not clone branch {args.branch}: {out}")

    manifest_path = (Path(args.manifest).resolve() if args.manifest
                     else tree / "scripts" / "qa" / "negative-controls.json")
    if not manifest_path.is_file():
        fail_setup(f"manifest not found: {manifest_path}")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail_setup(f"manifest unreadable: {exc}")
    controls = manifest.get("controls")
    if not controls:
        fail_setup("manifest has no 'controls' entries; nothing to verify")

    # Gates the project declares in TESTING.md but the manifest omits.
    testing = tree / "TESTING.md"
    declared = set(GATE_ID.findall(testing.read_text(encoding="utf-8"))) \
        if testing.is_file() else set()
    covered = {c.get("gate") for c in controls if c.get("gate")}
    missing = sorted(declared - covered)

    failures = []
    for i, control in enumerate(controls, 1):
        gate = control.get("gate", f"control-{i}")
        check = control.get("check")
        if not check:
            failures.append(f"{gate}: control has no 'check' command")
            print(f"[{gate}] ERROR: no check command in manifest")
            continue
        work = scratch / f"work-{i}"
        copy_tree(tree, work)
        apply_cmd = control.get("apply")
        if apply_cmd:
            rc, out = run(apply_cmd, work, args.timeout)
            if rc != 0:
                failures.append(f"{gate}: fault seeding failed (exit {rc})")
                print(f"[{gate}] ERROR: seeding failed: {out[-300:]}")
                continue
        rc, out = run(check, work, args.timeout)
        fault = control.get("fault", "")
        if rc is None:
            failures.append(f"{gate}: gate command timed out on its fault")
            print(f"[{gate}] FAIL: gate command timed out ({fault})")
        elif rc == 0:
            failures.append(f"{gate}: gate reported GREEN on its seeded "
                            f"fault ({fault})")
            print(f"[{gate}] FAIL: gate stayed green on its fault ({fault})")
        else:
            print(f"[{gate}] ok: gate went red (exit {rc}) on: {fault}")

    for gate in missing:
        msg = f"{gate}: declared in TESTING.md but has no negative control"
        if args.allow_missing:
            print(f"[{gate}] warning: {msg}")
        else:
            failures.append(msg)
            print(f"[{gate}] FAIL: {msg}")

    shutil.rmtree(scratch, ignore_errors=True)
    if failures:
        print(f"\nnegative_controls: FAIL ({len(failures)} problem(s))")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"\nnegative_controls: PASS ({len(controls)} control(s), "
          f"every gate went red on its fault)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
