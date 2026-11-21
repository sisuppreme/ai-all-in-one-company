# chaos-testing

## Metadata

- **Owner department:** D8 QA & Testing (QA)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://principlesofchaos.org/
- **Depends on:** test-strategy
- **Feeds into:** qa-gates, bug-triage

## When to use / Do NOT use

- **Use when:** proving the system keeps serving users under a named real failure — a killed instance, a severed dependency, injected latency — in staging, or in production under a scheduled game day with a prior staging pass on record.
- **Do NOT use when:** there is no measurable steady state yet (build monitoring first, D12), the goal is raw capacity (use load-testing), or the "experiment" would run against mocks and prove nothing (see BAN list). Never use this skill to justify unplanned production breakage.

## Rules

1. **QA-141 — Steady state is defined first, from real monitoring.** Before any injection, name the user-facing steady-state metrics (successful checkouts per minute, p95 latency, error rate), their normal ranges, and the dashboard or query that measures them. No measured steady state, no experiment.
2. **QA-142 — No hypothesis, no experiment.** The record states, before injection, the hypothesis that the steady state holds under one named failure. A run written up afterward from memory is not an experiment.
3. **QA-143 — One named failure per experiment.** Each experiment injects exactly one failure (kill one instance, sever one dependency, add a stated latency). Combined failures are separate experiments, run in sequence.
4. **QA-144 — Smallest blast radius first.** Injection starts at one instance or one dependency and grows only after a clean run at the smaller radius; the radius is written in the record before the run.
5. **QA-145 — The abort switch is tested before injection.** The abort mechanism (stop injection, restore the dependency, roll back the change) is executed once in the target environment and observed to work before the real failure is injected, and stays armed for the whole run.
6. **QA-146 — Staging first; production needs a game-day record.** Experiments start in staging. A production run requires a passing staging run of the same experiment, a scheduled window, and the game-day record naming who watches the abort switch.
7. **QA-147 — The failure and the measurement are real.** Injection hits the real component in the target environment, and steady-state readings come from the production monitoring pipeline — never from stubs, fixtures, or a second simulated dashboard.
8. **QA-148 — Abort criteria are numeric and pre-set.** The record names the deviation that ends the run early (e.g., error rate above X% for Y minutes). Crossing it aborts immediately; an abort is the safety system working, not a failed experiment.
9. **QA-149 — A disproven hypothesis becomes a defect the same day.** The defect names an owner and links the experiment record; the experiment does not rerun until the fix lands and is verified.
10. **QA-150 — Experiments rerun on a cadence and after resilience-relevant changes.** The standard set (instance kill, dependency loss) reruns per the cadence in TESTING.md and after any change to failover, retries, timeouts, or topology.
11. **QA-151 — Customer-impacting windows are scheduled and announced.** Production experiments run inside an announced window per the project's incident-communication practice (D18); the surprise is for the system, never for users or support.
12. **QA-152 — Results compare experiment against steady state.** The record files before/during/after measurements for the named metrics and the verdict (hypothesis held or disproven) — a narrative without the measurements is incomplete.

## BAN list

- **BAN-QA-071 — Mocked chaos.** Banned: running the "experiment" against stubbed or mocked infrastructure and reporting resilience as proven. Defeats: DET-FAKE-022. Bad: the dependency is replaced by a stub that always recovers, the run is green, and the release notes claim dependency-loss resilience. Instead: inject the failure against the real dependency in staging and measure the real steady state. Severity: BLOCK.
- **BAN-QA-072 — Fixture steady state.** Banned: steady-state "measurements" that are constants, hand-drawn graphs, or screenshots from another run. Defeats: DET-FAKE-004. Bad: the experiment record pastes a flat, plausible latency graph that never moves when traffic changes. Instead: pull before/during/after readings from the live monitoring queries named under QA-141. Severity: BLOCK.
- **BAN-QA-073 — Timer-driven health display.** Banned: a game-day or status display whose "live" health indicators animate from a script or timer instead of the real event stream. Defeats: DET-FAKE-018. Bad: the incident dashboard cycles green/amber states on a loop while the injected failure is actually taking the service down. Instead: bind every indicator to the real metrics pipeline and verify it moves when a known change is forced. Severity: BLOCK.
- **BAN-QA-074 — Paper experiment.** Banned: a complete-looking experiment record for a run where the failure was never actually injected. Defeats: DET-FAKE-022. Bad: the record shows "injected / recovered" states and a pass verdict, but the injection tool's log shows no execution. Instead: attach the injection tool's execution log to the record; no log, no verdict. Severity: BLOCK.

## Gates

- **G-QA-071 — Record completeness check.** Verifies: QA-142, QA-144, QA-148, QA-152. Check: `grep -cE '^(Hypothesis|Steady state|Blast radius|Abort criteria|Abort-switch test|Verdict):' experiments/<latest>.md` must print 6, and the injection log file named in the record must exist. Pass: all six fields present and log attached. Fail: block the experiment's sign-off. Recorded in: progress.md.
- **G-QA-072 — Standard experiment set on the release candidate (staging).** Verifies: QA-143, QA-146, QA-150. Check: run the scripted set — `./chaos/run-standard.sh staging` (instance kill, then dependency loss) — which exits non-zero if any named steady-state metric leaves its tolerance band. Pass: exit code 0. Fail: block the release and file defects per QA-149. Recorded in: progress.md.
- **G-QA-073 — Abort-switch drill.** Verifies: QA-145, QA-148. Check: start the staging instance-kill experiment, trigger the abort at the halfway point, and run `./chaos/verify-abort.sh`, which exits 0 only if injection has fully stopped and steady state recovered inside the window named in the record. Pass: exit code 0. Fail: no production game day until the drill passes. Recorded in: progress.md.
- **G-QA-074 — Disproven-hypothesis defect linkage.** Verifies: QA-149. Check: `grep -L 'Defect:' experiments/*.md | xargs grep -l 'Verdict: disproven'` must print nothing — every disproven record names a defect ID. Pass: no output. Fail: file the missing defects before the next run. Recorded in: progress.md.
- **G-QA-075 — Production game-day authorization.** Verifies: QA-146, QA-151. Check: the game-day record contains the staging pass reference, the scheduled window, and the D18 announcement reference; verified by the same field-presence grep as G-QA-071 extended with `Game day|Window|Announcement` (9 fields). Pass: all fields present before injection starts. Fail: the run stays in staging. Recorded in: progress.md.

## Anti-patterns

- **Blast-radius creep.** The run starts at one instance, someone widens it mid-experiment "to learn more," and the record still claims the small radius. Catch it by diffing the record's stated radius against the injection log before sign-off.
- **Graph shopping.** Several metrics deviated, but the report shows only the one that stayed green. Catch it by requiring the record to file every metric named under QA-141, not a selection.
- **Abort shame.** The team treats an aborted run as a failure and quietly stops arming the abort switch. An abort that fires on criteria is the method working; the defect is in the system that deviated, not in the abort.
- **One-and-done resilience.** A single clean run last quarter is cited as permanent proof after the topology changed twice. Check the run date against QA-150's cadence before accepting any resilience claim.

## Examples

- [Example 1 — Paper experiment vs. written record](examples/example-1.md) — violates/corrects QA-142, QA-144, QA-152.
- [Example 2 — Production-first breakage vs. graduated staging run](examples/example-2.md) — violates/corrects QA-145, QA-146, QA-151.
- [Example 3 — Fixture graph vs. measured steady state](examples/example-3.md) — violates/corrects QA-141, QA-147 and BAN-QA-072.

## Recall anchors

- Steady state first, hypothesis second, injection last.
- No hypothesis, no experiment; no log, no verdict.
- Smallest blast radius that tests the hypothesis — then grow.
- Test the abort switch before you need it.
- A disproven hypothesis is a defect with an owner, filed today.

## Checklist

- [ ] Steady-state metrics, ranges, and measuring queries are named (QA-141).
- [ ] Hypothesis, blast radius, and numeric abort criteria are written before injection (QA-142, QA-144, QA-148).
- [ ] Abort switch was executed and observed working in the target environment (QA-145).
- [ ] Staging pass exists before any production run, with a scheduled, announced window (QA-146, QA-151).
- [ ] Injection hit the real component and readings came from real monitoring (QA-147).
- [ ] Before/during/after measurements and the verdict are filed with the injection log (QA-152).
- [ ] Every disproven hypothesis has a defect with an owner, filed the same day (QA-149).
