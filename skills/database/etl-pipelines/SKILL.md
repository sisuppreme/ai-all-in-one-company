# etl-pipelines

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Apache Airflow documentation, "Concepts" — https://airflow.apache.org/docs/apache-airflow/2.0.0/concepts.html
- **Depends on:** data-ingestion, pipeline-orchestration, schema-design
- **Feeds into:** data-warehousing, data-quality

## When to use / Do NOT use

- **Use when:** data is moved and transformed between systems in stages — landing raw data, cleaning it, and modeling it for a warehouse or another consumer — or an existing pipeline's load semantics are changing.
- **Do NOT use when:** the movement is a one-off manual export (that is an incident waiting to be repeated; build the pipeline), or the "pipeline" is application request traffic (that is data-access and api-building). Ingestion contracts with sources belong to data-ingestion; scheduling belongs to pipeline-orchestration.

## Rules

1. **DB-321 — Raw is immutable.** Raw ingested data is never edited in place. Corrections happen in transformation, producing new cleaned output; the raw landing stays exactly as received.
2. **DB-322 — Every run is parameterized.** Each pipeline run is parameterized by date or window, so any single day can be re-run on demand. A run that only works for "today" is unfinished.
3. **DB-323 — Loads are idempotent.** Loads merge/upsert by key or replace whole partitions. Retries, re-runs, and backfills converge to the same destination state instead of duplicating rows.
4. **DB-324 — Partial loads publish nothing.** A failed transformation publishes no output: transforms write to a staging table and swap atomically, or load inside a transaction. Downstream never sees half a window.
5. **DB-325 — Transformations are reviewed code.** Every transformation is code in the repository, changed through the same review as application code. Editing transformation logic in production is forbidden.
6. **DB-326 — Quality gates sit between layers.** Data-quality checks run at each layer boundary (raw → cleaned → modeled). A dataset is promoted only when its checks pass; the checks are data-quality's, the placement is this skill's.
7. **DB-327 — Every dataset has an owner and lineage.** Each dataset names its owner and its source systems, written down where the pipeline is defined. An unowned dataset is a defect.
8. **DB-328 — Layers promote in one direction.** Data flows raw → cleaned → modeled. Consumers read the furthest layer they need; nothing reaches back and patches an earlier layer from a later one.
9. **DB-329 — Backfill is the same code path.** Backfilling a historical window runs the identical transformation and load code as a scheduled run, with the window as its parameter. There is no separate hand-written backfill procedure.
10. **DB-330 — Failures name themselves.** A failed run alerts with the dataset, the window, and the failing stage. "The pipeline failed" with no dataset or window is not an alert.

## BAN list

- **BAN-DB-161 — Editing raw in place.** Banned: updating or deleting rows in the raw landing zone to "fix" bad source data. Defeats: DET-INF-026. Bad: a malformed currency code is corrected with an `UPDATE` directly on the raw table; a month later nobody can tell what the source actually sent, and the audit trail is gone. Instead: leave raw untouched and correct the value in the transformation, where the rule is visible and re-runnable (DB-321). Severity: BLOCK.
- **BAN-DB-162 — The silent partial load.** Banned: a transformation that fails partway but lets downstream consume whatever was written before the failure. Defeats: DET-CODE-005. Bad: the nightly transform dies at row 800,000 of 1M; the exception is caught and logged, the DAG reports success, and dashboards show a day that is 20% short. Instead: stage the output and swap atomically on success only (DB-324); a failed run publishes nothing and alerts (DB-330). Severity: BLOCK.
- **BAN-DB-163 — Production-edited transforms.** Banned: changing transformation SQL or code directly in the production environment. Defeats: DET-INF-004. Bad: an engineer hot-fixes a join in the production scheduler's UI; the change is in no repository, the next deploy from code silently reverts it, and the figures change back overnight. Instead: the fix goes through the repository and the normal deploy, like any code change (DB-325). Severity: BLOCK.
- **BAN-DB-164 — Hard-coded windows.** Banned: transformation code with literal dates or "yesterday" baked in so no other window can be processed. Defeats: DET-CODE-009. Bad: the load script contains `WHERE created_at >= '2026-11-01'`; after an outage, the missed three days cannot be backfilled without editing code in production. Instead: the window is a run parameter supplied by the orchestrator (DB-322), and backfill uses the same code path (DB-329). Severity: BLOCK.

## Gates

- **G-DB-161 — Failure-injection test.** Verifies: DB-324, DB-330. Check: automated — in staging, kill a transformation mid-run and assert (a) no partial output is visible in the destination layer, (b) an alert fires naming dataset and window, (c) the retry completes the full window. Pass: all three hold. Fail: block shipment. Recorded in: progress.md.
- **G-DB-162 — Idempotency test.** Verifies: DB-323, DB-329. Check: automated — run the same window twice through the full pipeline and assert destination row counts and checksums are identical after the second run. Pass: identical state. Fail: block until the load merges or replaces instead of appending. Recorded in: progress.md.
- **G-DB-163 — Raw immutability check.** Verifies: DB-321. Check: automated — the pipeline's database role is denied UPDATE/DELETE on raw tables (permission assertion), and a checksum sample of raw partitions matches their landing checksums. Pass: writes are denied and checksums match. Fail: block; raw is restored from the source landing and the offending write path is removed. Recorded in: progress.md.
- **G-DB-164 — Layer-gate presence scan.** Verifies: DB-326, DB-327. Check: automated — scan the pipeline definitions and assert every layer promotion step references at least one data-quality check and every dataset declares an owner and its sources. Pass: no promotion step without a check, no dataset without an owner. Fail: block the pipeline's release. Recorded in: progress.md.

## Anti-patterns

- **The notebook transform.** The real transformation logic lives in an analyst's notebook or a BI tool's custom SQL, while the "pipeline" only moves files. Catch it: ask where a transformation change would be reviewed; if the answer is not the repository, the logic is in the wrong place (DB-325).
- **Silent success.** A run reports success while processing zero rows because the source was empty or the filter excluded everything. Catch it: layer-boundary checks include row-count expectations (DB-326); a zero-row promotion is a failure until a human confirms the source was truly empty.
- **Copy-paste pipelines.** Each new source gets a cloned pipeline with small edits, and the clones drift apart over months. Catch it: diff two pipelines for the same shape of job; shared stages that differ are one parameterized pipeline waiting to be written (DB-322).
- **Backfill by hand.** A missed window is repaired with one-off SQL run manually against production. Catch it: any production data write outside the pipeline's own code path is the tell; backfill is a run with a window parameter (DB-329), not a hand operation.

## Examples

- [Example 1 — An append load that duplicated on retry, replaced with a merge](examples/example-1.md) — corrects DB-323.
- [Example 2 — A partial load made atomic with staging and swap](examples/example-2.md) — corrects DB-324.
- [Example 3 — A hard-coded date replaced with a window parameter](examples/example-3.md) — corrects DB-322.

## Recall anchors

- Raw is read-only; corrections live in transformation.
- Any window can be re-run; no window is special.
- A failed transform publishes nothing.
- Transformations are code, reviewed like code.
- Retries converge; they never duplicate.

## Checklist

- [ ] Raw tables deny writes to the pipeline role and checksum clean (G-DB-163).
- [ ] Running the same window twice leaves identical counts and checksums (G-DB-162).
- [ ] Killing a transform mid-run publishes nothing and alerts with dataset + window (G-DB-161).
- [ ] Every layer promotion is gated by a data-quality check (G-DB-164).
- [ ] Every dataset names an owner and its source systems (DB-327).
- [ ] No literal dates or windows exist in transformation code (DB-322).
- [ ] Backfill runs the same code path as the scheduled run (DB-329).
