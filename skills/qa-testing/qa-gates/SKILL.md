# qa-gates

## Metadata

- **Owner department:** D8 QA & Testing (QA)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://docs.github.com/en/actions/get-started/continuous-integration ; https://web.dev/articles/vitals
- **Depends on:** test-strategy (TESTING.md names the gates, thresholds, and cadences this skill wires)
- **Feeds into:** bug-triage (escaped defects name the gate that should have caught them), placeholder-scan (its sweep runs as a required check), all D8 layer skills (their suites are enforced here)

## When to use / Do NOT use

- **Use when:** defining or changing the merge/release gates; wiring required status checks and branch protection; a gate goes red and someone proposes a bypass, a threshold change, or a re-run; a flaky gate needs quarantine; a release needs its gate evidence assembled.
- **Do NOT use when:** deciding what must be proven or what the budgets are (test-strategy — this skill enforces the strategy, it does not set it); writing the tests a gate runs (the owning layer skill); triaging a defect a gate caught (bug-triage).

## Rules

1. **QA-221 — A gate is a command with an exit code.** Every automated gate is a named command whose exit code decides pass/fail; if a human must judge whether it passed, it is a review checklist item, labeled as such in TESTING.md, and never reported as an automated gate.
2. **QA-222 — Gate definitions predate the work they judge.** Gate configuration and thresholds live in files (workflow files, branch-protection config, the budget file) committed before the change they gate; a gate invented or edited inside the PR it judges does not judge that PR.
3. **QA-223 — Threshold and test changes in the same PR need a waiver.** Changing a threshold, or the tests a gate runs, in the same PR as the code that failed it requires a waiver record in the project log naming the owner, the reason, and an expiry date; without the record the PR does not merge.
4. **QA-224 — The required-checks list is single-sourced.** The branch-protection required status checks match the gate list in TESTING.md exactly; any difference between the two lists is a defect, reconciled in a reviewed change, never by quietly editing one side.
5. **QA-225 — Every gate has a witnessed failure.** When a gate is created and after any pipeline change, a seeded fault of its class (broken assertion, removed form label, shifted layout header, tightened k6 threshold) is run against it and must make it exit non-zero; a gate never seen red is unverified and is not reported as protection.
6. **QA-226 — Negative controls run on a schedule.** The seeded-fault suite runs in a named nightly job, one fault per gate class; a gate that reports green on its seeded fault is filed as a blocker defect against the gate itself, and the release is blocked until the gate bites again.
7. **QA-227 — Bypasses are logged and counted.** Every admin merge, `[skip ci]`, and manual override is recorded with who, when, and why; the bypass count is reported per release, and a rising count is itself a quality finding with a named owner.
8. **QA-228 — Quarantine is a counted, expiring state.** A flaky gate or test enters quarantine only with a named owner and an expiry date, and appears in the release's quarantine count; an expired quarantine without a fix or a justified extension blocks the release — re-running until green is not a state.
9. **QA-229 — Baselines update only through reviewed diffs.** Visual, contract, and performance baselines change only via a diff whose description names the intentional change being accepted; a bulk regenerate-all-baselines commit is rejected, because it accepts regressions sight unseen.
10. **QA-230 — A gate result is an artifact, not a claim.** Each gate run records the command, the exit code, and a link to the CI run in progress.md; "passed locally" or a green screenshot with no run behind it is not a result.
11. **QA-231 — A coverage gate must prove the tests assert.** A coverage-threshold gate runs alongside a mutation sample or seeded-fault check on the covered code (G-QA-115); a suite that stays green under seeded faults fails the gate no matter what its coverage percentage says.
12. **QA-232 — Every gate names its cadence and its job.** TESTING.md lists each gate as per-PR, merge/nightly, or per-release, with the job that runs it; a gate with no scheduled job, or a job that has not run inside its cadence, does not exist for reporting purposes.

## BAN list

- **BAN-QA-111 — Echo-only pipeline.** Banned: a CI pipeline whose test step is `echo ok`, a no-op script, or a suite of assertions that assert nothing, presented as a passing gate. Defeats: DET-INF-002. Bad: the merge gate shows green for six months because its only step prints "tests passed"; the figure never moves when behavior breaks. Instead: wire the gate to the real suite command, and prove it can fail with a seeded fault (QA-225) before counting it as protection. Severity: BLOCK.
- **BAN-QA-112 — Same-PR threshold loosening without a waiver.** Banned: lowering a threshold, widening a budget, or deleting the failing test inside the same PR that failed it, with no waiver record. Defeats: DET-NONE — no DET parameter names this signal; governed by QA-223. Bad: the performance gate fails at LCP 2.9s, so the PR edits the budget to 3.5s and merges green — the bar reset to whatever the code already does. Instead: fix the code, or record a waiver with owner, reason, and expiry and review the threshold change as a standards change (QA-223). Severity: BLOCK.
- **BAN-QA-113 — Re-run until green.** Banned: merging after re-running a flaky gate until it happens to pass, with no quarantine entry and no fix. Defeats: DET-FAKE-022. Bad: the e2e gate fails three times and passes on the fourth re-run; the PR merges under a "Passed" indicator that the code never earned. Instead: quarantine the flake with owner and expiry (QA-228) or fix it; the merge waits for a green run that is not a lottery win. Severity: BLOCK.
- **BAN-QA-114 — Routine admin bypass.** Banned: using admin merge, `[skip ci]`, or a disabled required check as the normal path past a red gate, unlogged. Defeats: DET-INF-002. Bad: branch protection lists nine required checks, but the maintainer merges red PRs with the admin override weekly and nothing records it — enforcement exists only in the settings screenshot. Instead: fix the failure, or log the bypass with who and why and count it in the release report (QA-227). Severity: BLOCK.
- **BAN-QA-115 — Bulk baseline regeneration.** Banned: regenerating all visual, contract, or performance baselines in one unreviewed commit to turn a red gate green. Defeats: DET-NONE — no DET parameter names this signal; governed by QA-229. Bad: a layout change breaks 40 snapshots; the fix is `update-snapshots --all`, and the regression the gate existed to surface disappears from view. Instead: update baselines through a reviewed diff whose description names the intentional change (QA-229), one cause at a time. Severity: BLOCK.

## Gates

The five check scripts these gates cite — `negative_controls.py`, `check_required_checks.py`, `check_gate_provenance.py`, `gate_ledger.py`, and `mutation_sample.py` — ship in this repository at `scripts/qa/` as reference implementations, each documented in its own header. A project may replace any of them with its own equivalent provided the gate's behavior is preserved exactly (same inputs, same pass/fail semantics), and the substitution is recorded in progress.md; an unrecorded or behavior-changing substitution is a gate failure, not a customization.

- **G-QA-111 — Negative-control meta-gate.** Verifies: QA-225, QA-226. Check: run the shipped runner, `scripts/qa/negative_controls.py`, in one of its two forms. Nightly form: the named nightly job runs `python3 scripts/qa/negative_controls.py --branch qa/seeded-faults`; the branch carries one seeded fault per gate class. Local form (the manifest-driven invocation, for a project without the branch — a scratch workspace, a pre-push check, a single agent): `python3 scripts/qa/negative_controls.py --project <project>` reads the project's own controls manifest (default `<project>/scripts/qa/negative-controls.json`; `--manifest` overrides the path) and runs each control against a scratch copy of the local tree — a control seeds its fault with its `apply` command, or the tree is already seeded — and each control's `check` command must exit non-zero with its fault present. Either form: the script exits non-zero if any gate reports green on its own fault (exit 1), and exit 2 is a setup error (no manifest, no controls, unusable project). The script's header documents the controls-manifest format. The runner also reports any gate declared in TESTING.md that has no negative control; that gap fails the run unless `--allow-missing` is passed, which downgrades it to a printed warning — the `--allow-missing` disposition is legitimate only for a consciously partial control set, and its use is recorded in progress.md with the uncovered gates named. Pass: exit 0 — every gate went red on its fault, and no declared gate lacks a control (or the gap is an `--allow-missing` warning recorded as above). Fail: block the release; file a blocker defect against the non-biting gate. Recorded in: progress.md.
- **G-QA-112 — Required-checks diff.** Verifies: QA-224. Check: `python3 scripts/qa/check_required_checks.py` reads the branch-protection required status checks through the platform API and diffs them against the gate list parsed from TESTING.md; it exits non-zero on any difference. The script ships in this repo at `scripts/qa/check_required_checks.py`; where the platform API is unreachable it diffs against the checked-in snapshot `.github/required-checks.txt` or the workflow job definitions, and prints which source it used. Pass: exit 0. Fail: block merge; reconcile the lists in a reviewed change. Recorded in: progress.md.
- **G-QA-113 — Gate provenance and waiver check.** Verifies: QA-222, QA-223. Check: `python3 scripts/qa/check_gate_provenance.py` compares commit timestamps for gate-config and threshold files against the code they gate, and exits non-zero if a same-PR threshold or test change lacks a waiver entry with a named owner and an unexpired date in the project log. The script ships in this repo at `scripts/qa/check_gate_provenance.py` and evaluates the commit range `--base..HEAD`; its `--log-trace` mode also verifies that gate results recorded in progress.md trace to gate IDs defined in the skills. Pass: exit 0. Fail: block merge until the change predates the work or the waiver exists. Recorded in: progress.md.
- **G-QA-114 — Bypass and quarantine ledger audit.** Verifies: QA-227, QA-228. Check: `python3 scripts/qa/gate_ledger.py --fail-on-expired` reads the bypass/quarantine ledger and exits non-zero if any bypass lacks who/why, any quarantine entry is expired without resolution, or the release's bypass count rose over the previous release with no linked quality finding. The script ships in this repo at `scripts/qa/gate_ledger.py`; its header documents the ledger format (default `scripts/qa/gate-ledger.json`). Pass: exit 0. Fail: block the release; resolve or formally extend each entry. Recorded in: progress.md.
- **G-QA-115 — Mutation sample behind the coverage gate.** Verifies: QA-231. Check: `python3 scripts/qa/mutation_sample.py --sample 20` seeds 20 faults (or applies 20 sampled mutations) into covered production code and runs the unit suite; it exits non-zero if the suite stays green on more faults than the TESTING.md allowance. The script ships in this repo at `scripts/qa/mutation_sample.py`; its header documents the sample-config format (default `scripts/qa/mutation-sample.json`). Pass: exit 0. Fail: block the release; the hollow tests are rewritten before the coverage figure is reported again. Recorded in: progress.md.

## Anti-patterns

- **Gate sprawl without ownership.** A gate is added after every incident and none is ever removed, until nobody can say what each one protects; catch it by reviewing the gate list against TESTING.md each release and deleting or adopting the orphans.
- **Human judgment in gate costume.** A "gate" whose check reads "the agent confirms the page looks right" — no command, no artifact, no diff; catch it by asking for the command and its exit code, and reclassify it as a checklist item when there is none.
- **The nightly graveyard.** Expensive gates are scheduled nightly, but the job has been disabled or failing unattended for weeks, so the cadence is fictional; catch it by checking the last successful run artifact for every scheduled gate before reporting it.
- **Threshold archaeology.** A budget whose number nobody can trace to a source document, loosened so long ago that the original standard is lost; catch it by requiring every threshold to cite its budget or SLO source, and treating an unsourced number as unwritten.

## Examples

- [Example 1 — A gate that had never failed](examples/example-1.md) — violates/corrects QA-225.
- [Example 2 — The threshold that moved with the code](examples/example-2.md) — violates/corrects QA-223.
- [Example 3 — Re-run until green, replaced by quarantine](examples/example-3.md) — violates/corrects QA-228.

## Recall anchors

- A gate is a command with an exit code, or it is a checklist item — never both stories.
- Gate files are committed before the work they judge.
- A gate never seen red is unverified.
- Bypasses and quarantines are counted, owned, and expiring — or they are hiding places.
- Baselines change by named intention, never by bulk regeneration.

## Checklist

- [ ] Every automated gate is a named command with an exit code; judgment calls are labeled checklist items (QA-221).
- [ ] Gate configuration and thresholds predate the changes they gate (QA-222).
- [ ] Any same-PR threshold or test change carries a waiver with owner, reason, and expiry (QA-223).
- [ ] Branch-protection required checks match the TESTING.md gate list exactly (QA-224).
- [ ] The nightly negative-control run is inside its cadence and every gate went red on its seeded fault (QA-225, QA-226).
- [ ] All bypasses this release are logged with who and why, and the count is reported (QA-227).
- [ ] No quarantine entry is expired without a fix or a justified extension (QA-228).
- [ ] Baseline changes this release are reviewed diffs naming the intentional change (QA-229).
- [ ] The coverage gate's latest mutation sample is on file and within allowance (QA-231).
