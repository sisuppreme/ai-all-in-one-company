# legacy-migration

## Metadata

- **Owner department:** D15 Developer Experience (DX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://kindatechnical.com/software-engineering/large-scale-change-strangler-branch-abstraction.html ; https://microservices.io/post/refactoring/2023/06/21/strangler-fig-application-pattern-incremental-modernization-to-services.md.html ; https://martinfowler.com/articles/feature-toggles.html
- **Depends on:** tech-debt
- **Feeds into:** refactoring, versioning

## When to use / Do NOT use

- **Use when:** a working legacy system, module, or data shape must be replaced — a framework swap, a service extraction, a store or API migration — and the old behavior must keep serving users while the new one is built.
- **Do NOT use when:** the change preserves behavior inside one implementation with no old/new coexistence (use refactoring), the code is being deleted with no replacement (just delete it, with a decision-log entry), or the "legacy" system has no users yet (rewrite freely; there is nothing to migrate).

## Rules

1. **DX-121 — The plan is slices, seams, and rollbacks.** Every migration plan names its slices (one capability at a time), the seam for each slice (routing facade, abstraction layer, or expand–migrate–contract for data/API shapes), and the rollback for each step. A plan whose migration is one big step is rejected before work starts.
2. **DX-122 — Characterization tests pin behavior before anything moves.** Before a slice is touched, tests are written against the legacy implementation recording what it actually does today — including its quirks and error behavior — on production-shaped cases. The replacement is built to pass these tests, not to match a spec written from memory.
3. **DX-123 — The seam goes in first.** The facade, router, or abstraction layer is introduced and deployed with all traffic still flowing to the legacy implementation before any new implementation exists. A seam that only appears together with the new code cannot be rolled back independently and is not a seam.
4. **DX-124 — Legacy stays deployable and is the fallback.** The legacy implementation remains buildable, deployable, and monitored for the whole coexistence period. It is never edited into a half-migrated state, and no migration step may leave the project with only the new path working.
5. **DX-125 — Parallel run with compared outputs before cutover.** Before a slice's traffic flips, the new implementation runs against the same recorded production-shaped inputs as the legacy one (shadow calls, replayed requests, or dual execution) and the outputs are diffed. Every diff is either fixed or recorded as an intended behavior change with a decider named. Cutover on untested equivalence is a guess.
6. **DX-126 — Cutover is per slice and reversible in one change.** Traffic flips slice by slice through the routing seam (route rule or toggle), never all slices at once. Flipping back to legacy is a single configuration change, rehearsed in staging before the first production flip.
7. **DX-127 — Data migration is rehearsed and reversible, or its point of no return is explicit.** Every data move is first run against a copy of production-shaped data with row counts and checksums compared. The migration is reversible until a stated point of no return; a verified backup is taken at that point, and the point is named in the plan before the rehearsal, not discovered during it.
8. **DX-128 — No new features on scheduled legacy paths.** Once a slice is scheduled for migration, its legacy implementation receives fixes only. A feature that must land before the slice migrates is built in the new implementation, or the schedule is formally changed — building it in legacy "just this once" moves the target forever.
9. **DX-129 — Coexistence has an end date.** The plan states the date or release by which coexistence ends and the legacy path is eliminated. "Both systems for now" with no end date is not a stage of the plan; it is how migrations fail.
10. **DX-130 — Elimination is a separate, later step.** The legacy path is deleted only after its replacement has carried real production traffic for the soak period named in the plan, as its own reviewed change — never in the same change as the cutover, and never on cutover day.
11. **DX-131 — Shape changes use Parallel Change.** A breaking data or API shape change goes expand (new shape added alongside old, both written) → migrate (readers and writers moved, old shape still valid) → contract (old shape removed). No step breaks a reader that has not yet migrated.
12. **DX-132 — Migration state is recorded as it changes.** Each slice's stage (seamed, built, parallel-running, cut over, eliminated) and its current routing are recorded in the migration plan and progress.md at the moment they change. The routing table in production and the plan's stated stage must agree; disagreement is a defect found by G-DX-062, not a documentation nit.

## BAN list

- **BAN-DX-061 — Big-bang cutover.** Banned: freezing the legacy system, rewriting it wholesale, and switching everything over in one release. Defeats: DET-CODE-014. Bad: the store is rebuilt over a month behind a feature freeze and launched in one deploy; the first production bug has no partial rollback, only the whole old system or the whole new one. Instead: slice the migration behind a routing seam and flip one capability at a time (DX-121, DX-123, DX-126). Severity: BLOCK.
- **BAN-DX-062 — Legacy deleted at cutover.** Banned: removing, undeploying, or letting the legacy implementation rot in the same change that flips traffic to its replacement, leaving dead references and no fallback. Defeats: DET-CODE-002. Bad: the cutover PR deletes the old billing module and its routes; a defect found on day two cannot be rolled back because the fallback no longer builds. Instead: keep legacy deployable through the soak period and delete it in a separate elimination step (DX-124, DX-130). Severity: BLOCK.
- **BAN-DX-063 — New features built into a scheduled legacy path.** Banned: implementing new behavior in a legacy implementation whose slice is already scheduled, so the feature exists only in code about to be replaced and must be built twice. Defeats: DET-CODE-007. Bad: a discount feature is added to the legacy checkout "because the migration is still weeks away"; the replacement team re-implements it from scratch and the two versions diverge. Instead: build it in the new implementation, or formally reschedule the slice (DX-128). Severity: BLOCK.
- **BAN-DX-064 — Migration with no characterization tests.** Banned: replacing a legacy path whose current behavior is pinned by no tests, so "equivalent" is asserted from reading the code or from the original spec. Defeats: DET-CODE-013. Bad: the pricing engine is reimplemented from its README; production reveals rounding and edge-case behavior the README never mentioned, one invoice at a time. Instead: write characterization tests against the running legacy behavior first and build the replacement to pass them (DX-122). Severity: BLOCK.
- **BAN-DX-065 — Legacy kept as commented-out code after elimination.** Banned: leaving the removed implementation commented out, copied into a `legacy/` folder inside the shipped code, or otherwise retained in the working tree "just in case" after the eliminate step. Defeats: DET-CODE-010. Bad: 900 lines of the old search implementation sit commented above its replacement, still indexed, still confusing every reader and search. Instead: delete it — version control is the archive — and record the elimination in the plan (DX-130, DX-132). Severity: BLOCK.

## Gates

- **G-DX-061 — Parity suite on both implementations (automated).** Verifies: DX-122, DX-125. Check: run the slice's characterization/parity suite twice, once per implementation — `IMPL=legacy npm run test:parity -- <slice>` and `IMPL=new npm run test:parity -- <slice>` (or the project's equivalent recorded in the plan) — over the recorded production-shaped case set. Pass: exit 0 on both runs, and every output diff between the two runs is either zero or listed in the plan as an intended change with a named decider. Fail: block cutover for that slice. Recorded in: progress.md.
- **G-DX-062 — Route audit (automated).** Verifies: DX-126, DX-132. Check: dump the facade/router's effective routing table and diff it against the migration plan's stated current stage: every route the plan marks "cut over" points at the new implementation, every other route at legacy, with no unlisted routes. Pass: empty diff. Fail: block shipment; reconcile the table or the plan before proceeding. Recorded in: progress.md.
- **G-DX-063 — Rollback drill (automated/staging).** Verifies: DX-124, DX-126. Check: in staging, flip the slice's routing back to legacy using only the documented single configuration change, then run the primary-flow smoke tests against the legacy path. Pass: smoke tests green on legacy with no code change and no redeploy of the new implementation. Fail: block the production cutover — a rollback that has never been executed is assumed not to exist. Recorded in: progress.md.
- **G-DX-064 — Post-elimination dead-reference sweep (automated).** Verifies: DX-130. Check: after an eliminate step, `grep -rn '<removed module/endpoint name>' --exclude-dir=.git --exclude-dir=node_modules .` over source, config, and routing, plus a full build and test run. Pass: no references outside the migration plan and changelog; build and tests green. Fail: block shipment until references are removed or the elimination is reverted. Recorded in: progress.md.
- **G-DX-065 — Plan completeness review (manual).** Verifies: DX-121, DX-127, DX-129. Check: before the first slice is built, read the migration plan and confirm every slice names its seam, its rollback, its data point-of-no-return and backup (or "no data change"), and that the plan carries a coexistence end date. Pass: all fields present for all slices. Fail: block the start of migration work; a plan missing a rollback or an end date is not yet a plan. Recorded in: progress.md.

## Anti-patterns

- **Seam theater.** A facade exists on paper but callers still reach the legacy code directly in a dozen places, so flipping the route changes nothing for most traffic. Catch it before cutover by grepping for direct references to the legacy module outside the seam — the seam must be the only door.
- **Parity by eyeball.** The parallel run happens, someone scrolls the outputs, declares them "basically the same," and the diffs are never enumerated. Catch it by requiring the diff list as a file in the plan: if it is not written down, the comparison did not happen.
- **The permanent pilot.** One easy slice migrates, the announcement declares victory, and the remaining slices quietly never schedule — coexistence becomes the architecture. Catch it at each review by comparing slices eliminated against the plan's end date (DX-129), not against slices started.
- **Rollback by redeploy.** "We can always roll back" means checking out the old release and redeploying everything, untested, under incident pressure. Catch it with G-DX-063: if rollback is not a configuration flip that has been drilled, it is a hope, not a rollback.

## Examples

- [Example 1 — The one-release rewrite plan](examples/example-1.md) — violates/corrects DX-121.
- [Example 2 — Cutover on a README](examples/example-2.md) — violates/corrects DX-122, DX-125.
- [Example 3 — Deleted on cutover day](examples/example-3.md) — violates/corrects DX-124, DX-130.

## Recall anchors

- Slice it behind a seam, or do not start.
- Pin the behavior before you move it — tests first, replacement second.
- Legacy is the fallback until the replacement has carried real traffic.
- Cutover is a routing flip; rollback is the same flip, backwards, already drilled.
- Coexistence without an end date is the failure mode, not a stage.

## Checklist

- [ ] The plan names every slice, its seam, and its rollback; no single-step plan (DX-121, G-DX-065).
- [ ] Characterization tests pass against the legacy implementation before the replacement is built (DX-122).
- [ ] The seam is deployed with all traffic still on legacy before new code lands behind it (DX-123).
- [ ] Parity suite passes on both implementations; every diff is fixed or recorded as intended (DX-125, G-DX-061).
- [ ] The rollback flip has been drilled in staging for this slice (DX-126, G-DX-063).
- [ ] Data moves are rehearsed on a copy; the point of no return and its backup are named (DX-127).
- [ ] No new features were added to scheduled legacy paths during this work (DX-128).
- [ ] The plan's coexistence end date stands, slice stages are recorded, and elimination is scheduled as its own later change (DX-129, DX-130, DX-132).
