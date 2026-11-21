# data-quality

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Datadog, "Implement dbt data quality checks with dbt-expectations" — https://www.datadoghq.com/blog/dbt-data-quality-testing/
- **Depends on:** schema-design, etl-pipelines, data-ingestion
- **Feeds into:** data-warehousing, pipeline-orchestration, seed-data

## When to use / Do NOT use

- **Use when:** datasets need executable quality assertions — uniqueness, not-null, accepted values, referential integrity, range, freshness, row counts, business rules — declared, run, and enforced as pipeline gates.
- **Do NOT use when:** the question is application-level input validation at a user boundary (use validation in D4), or a one-off exploratory analysis. Quality checks guard datasets that other people and systems build on; exploration guards itself.

## Rules

1. **DB-381 — Keys are always tested.** Every primary key carries unique and not-null tests; every foreign key carries a relationships test. No exceptions, no tolerance.
2. **DB-382 — Every boundary has a check.** Every pipeline layer boundary (raw → cleaned → modeled) has at least one row-count or freshness check on each dataset that crosses it.
3. **DB-383 — Failure fails the run.** A failing check fails the run with a non-zero exit and an alert naming the dataset and the check. A check that cannot fail a run is a report, not a gate.
4. **DB-384 — Results are stored and trended.** Check results are persisted per run and reviewed as a trend. A check's history is part of the dataset's record, not console output.
5. **DB-385 — Money paths have business-rule checks.** Every money path carries an arithmetic business-rule check (e.g. order totals equal the sum of their line items), in addition to structural tests.
6. **DB-386 — Tolerance is written and bounded.** A `mostly`-style tolerance is permitted only on noisy real-world columns, with the threshold written next to the check and a reason. Integrity rules — keys, references, money sums — get zero tolerance, always.
7. **DB-387 — Checks live with the model.** Checks are declared next to the model or dataset they guard, in the same repository, and run in CI and in the pipeline. A check defined only in a dashboard tool guards nothing upstream.
8. **DB-388 — Sudden perfection is investigated.** A check that has always passed and keeps passing unchanged after a source change is investigated, not celebrated: the likeliest explanations are a broken check or a disconnected dataset.
9. **DB-389 — The suite is proven against faults.** Before a check suite is trusted, it is run against a fixture with injected faults (a duplicate key, an orphaned foreign key) and must catch them. An unproven suite is assumed decorative.
10. **DB-390 — Every check set has an owner.** Each dataset's checks name an owner who receives the failure alert and owns the fix-or-quarantine decision.

## BAN list

- **BAN-DB-191 — Warning-only gates.** Banned: configuring quality checks to warn and exit zero, so failures never stop a run. Defeats: DET-INF-002. Bad: the dbt suite is set to `severity: warn` across the project "temporarily"; duplicates land in the warehouse for a month while every pipeline run reports success with warnings nobody reads. Instead: checks fail the run with a non-zero exit (DB-383); a deliberate exception is one check, time-boxed, with an owner — never the project default. Severity: BLOCK.
- **BAN-DB-192 — Tolerance on integrity.** Banned: applying a `mostly`-style tolerance threshold to key, reference, or money checks so a known fraction of violations passes. Defeats: DET-CODE-012. Bad: the orders primary-key test is set to pass at 99% uniqueness "because the source is messy"; the 1% duplicates are double-counted revenue. Instead: integrity checks get zero tolerance (DB-386); messy sources are fixed at ingestion quarantine, not averaged away at the gate. Severity: BLOCK.
- **BAN-DB-193 — The unreconciled money path.** Banned: shipping a money dataset with structural tests only and no business-rule check tying its totals to their components. Defeats: DET-CODE-013. Bad: order totals are tested not-null and unique while a transformation bug drops a line item from 4% of orders; every structural test passes and the money is wrong. Instead: the money path carries an arithmetic check — totals equal line-item sums — that fails the run on any mismatch (DB-385). Severity: BLOCK.
- **BAN-DB-194 — Disposable check results.** Banned: running checks without persisting their results, or deleting failure history when it becomes embarrassing. Defeats: DET-INF-013. Bad: check output exists only in CI console logs that expire in 14 days; when finance questions a figure from last quarter, there is no record of what the checks said at the time. Instead: results are stored per run and trended (DB-384), retained with the dataset's record. Severity: WARN.

## Gates

- **G-DB-191 — Suite gate wiring.** Verifies: DB-383, DB-387. Check: automated — the check suite (`dbt build` or the project's checkpoint command) is wired into CI and into the orchestrator's promotion steps, and a deliberately failing test model in a scratch schema makes both runs exit non-zero. Pass: both runs fail on the planted failure. Fail: block; a suite that cannot fail a run is re-wired before anything ships. Recorded in: progress.md.
- **G-DB-192 — Negative test.** Verifies: DB-389, DB-381. Check: automated — inject a duplicate primary key and an orphaned foreign key into a staging fixture and run the suite. Pass: the suite catches both faults and names the datasets. Fail: block; the suite is fixed and re-proven before it is trusted as a gate. Recorded in: progress.md.
- **G-DB-193 — Coverage scan.** Verifies: DB-381, DB-382, DB-385. Check: automated — scan model and check declarations and assert every primary key has unique + not-null tests, every foreign key has a relationships test, every layer boundary has a row-count or freshness check, and every money dataset has a business-rule check. Pass: zero gaps. Fail: block the dataset's promotion. Recorded in: progress.md.
- **G-DB-194 — Results retention check.** Verifies: DB-384, DB-390. Check: automated — query the check-results store and assert results exist for every scheduled run in the retention window and every dataset's check set names an owner. Pass: complete history and owners. Fail: block until result persistence and ownership are in place. Recorded in: progress.md.

## Anti-patterns

- **Tolerance creep.** A noisy column's threshold is loosened a little at every failure until the check is decorative. Catch it: threshold changes are reviewed like code and the history is trended (DB-384, DB-386); three loosenings in a row is a source problem, not a threshold problem.
- **Happy-path suites.** Checks cover the columns everyone already trusts and skip the messy joins where corruption actually happens. Catch it: the coverage scan (G-DB-193) counts checks per dataset, and the money and join-heavy datasets are checked first, not last.
- **Alert fatigue farming.** So many flaky checks fire that the team reflexively acknowledges and ignores them. Catch it: a check that fires without a real defect is itself a defect — it is fixed, re-scoped, or removed with a record, never left to cry wolf (DB-390).
- **Snapshot amnesia.** Results are stored but never looked at, so a slow degradation — rising null rates, shrinking row counts — crosses no threshold and surprises everyone at once. Catch it: trends are reviewed on a schedule (DB-384); a check whose trend nobody has opened in a month is flagged in the review.

## Examples

- [Example 1 — Warning-only checks made into a real gate](examples/example-1.md) — corrects DB-383.
- [Example 2 — Key and relationship tests that catch injected faults](examples/example-2.md) — corrects DB-381.
- [Example 3 — A money path reconciled by a business-rule check](examples/example-3.md) — corrects DB-385.

## Recall anchors

- Keys and references get tests, always, at zero tolerance.
- A check that cannot fail the run is a report, not a gate.
- Money totals tie to their line items or the run stops.
- Tolerance is written next to the check, with a reason.
- Prove the suite against injected faults before trusting it.

## Checklist

- [ ] Every primary key has unique + not-null tests; every foreign key a relationships test (G-DB-193).
- [ ] Every layer boundary has a row-count or freshness check (DB-382).
- [ ] A planted failure makes CI and the pipeline exit non-zero (G-DB-191).
- [ ] The suite catches an injected duplicate key and orphaned foreign key (G-DB-192).
- [ ] Money datasets carry an arithmetic business-rule check (DB-385).
- [ ] Tolerances exist only on noisy columns, written with thresholds and reasons (DB-386).
- [ ] Check results are persisted, trended, and owned (G-DB-194).
