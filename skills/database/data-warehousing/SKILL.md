# data-warehousing

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Google Cloud documentation, "BigQuery overview" — https://cloud.google.com/bigquery/docs/introduction?hl=vi
- **Depends on:** etl-pipelines, data-ingestion, schema-design
- **Feeds into:** data-quality, revenue-analytics, dashboards

## When to use / Do NOT use

- **Use when:** reporting, dashboards, or analysis need data from operational systems — the analytical store, its models, metric definitions, and load discipline are being designed or changed.
- **Do NOT use when:** the query is part of serving a user request (that is the operational database's job, via data-access), or the "report" is a one-off operational lookup. A warehouse is never a reporting skin over the production primary.

## Rules

1. **DB-301 — The primary is not a reporting backend.** No dashboard, report, or analyst query runs against the production primary. Analytical reads run against the warehouse (or a replica explicitly provisioned for reporting, per read-replicas).
2. **DB-302 — One metric, one definition.** Every headline metric has exactly one definition, in one named model in the warehouse. Every consumer references that model; a metric re-implemented inside a dashboard is a defect.
3. **DB-303 — Loads are idempotent.** Warehouse loads are scheduled, monitored, and idempotent: re-running a day's load produces the same warehouse state, verified by row counts or checksums.
4. **DB-304 — PII is minimized on entry.** Personally identifiable data entering the warehouse is limited to what a named analysis needs, and access is controlled per dataset. The warehouse is not a full photocopy of the user table.
5. **DB-305 — Schemas are code.** Warehouse schemas and models are versioned code in the repository. A change made in a console or UI that is not in the repo does not exist and will be overwritten.
6. **DB-306 — The warehouse is a separate store.** Analytical data lives in a separate analytical store (columnar storage with storage/compute separation, e.g. BigQuery's model), loaded on a schedule from operational sources — not in extra tables on the production database.
7. **DB-307 — Freshness is stated and alerted.** Every warehouse dataset names its expected freshness (load cadence plus maximum lag). A load that misses its window alerts before a stakeholder finds a stale dashboard.
8. **DB-308 — Metric changes are migrations.** Changing a headline metric's definition updates the one owning model, records the change and its effective date, and re-points or re-checks every consumer. Silent redefinition is forbidden.
9. **DB-309 — Models, not raw dumps.** Consumers query modeled fact and dimension tables (or curated wide tables), not raw operational copies. Raw landings exist for reload and audit; they are not a reporting interface.
10. **DB-310 — Reconciliation runs on a schedule.** A headline metric computed in the warehouse is reconciled against the source system within a stated per-metric tolerance, on a schedule, and the result is recorded. A tolerance is a number written next to the check, not "close enough".

## BAN list

- **BAN-DB-151 — Dashboards on the primary.** Banned: pointing a reporting tool or dashboard at the production primary database. Defeats: DET-INF-027. Bad: the Monday revenue dashboard runs full-table aggregations on the primary at peak traffic; checkout latency triples while the report renders. Instead: load the data into the warehouse on a schedule (DB-306) and point the dashboard there. Severity: BLOCK.
- **BAN-DB-152 — The CSV warehouse.** Banned: a manually exported file (a nightly CSV emailed or shared around) serving as the analytical store. Defeats: DET-INF-004. Bad: finance downloads a spreadsheet export each morning, edits two columns by hand, and circulates it as "the warehouse"; no one can reproduce last month's figures. Instead: a scheduled, idempotent pipeline load into the warehouse, with models as code (DB-303, DB-305). Severity: BLOCK.
- **BAN-DB-153 — A metric per dashboard.** Banned: defining the same business metric independently inside multiple dashboards, queries, or reports. Defeats: DET-CODE-027. Bad: "revenue" excludes refunds in the sales dashboard and includes them in the finance dashboard; the two figures disagree in the same meeting. Instead: one definition in one named model that every consumer references (DB-302). Severity: BLOCK.
- **BAN-DB-154 — Console-edited models.** Banned: changing warehouse tables, views, or models directly in the provider console without the change existing as reviewed code. Defeats: DET-INF-024. Bad: an analyst "fixes" a view in the console during an incident; the next pipeline deploy overwrites it and the fix vanishes with no record. Instead: every warehouse change is a code change in the repository, deployed by the pipeline (DB-305). Severity: BLOCK.

## Gates

- **G-DB-151 — Primary protection check.** Verifies: DB-301. Check: automated — scan the production primary's query log for the reporting window and assert zero connections or queries from reporting tools and dashboard service accounts. Pass: zero reporting queries on the primary. Fail: block the release and move the consumer to the warehouse. Recorded in: progress.md.
- **G-DB-152 — Reconciliation check.** Verifies: DB-310, DB-302. Check: automated — on schedule, compute a headline metric (e.g. yesterday's order count and revenue) in the warehouse and in the source system; assert the difference is within the tolerance recorded for that metric. Pass: within tolerance. Fail: alert and block promotion of the affected dataset until explained. Recorded in: progress.md.
- **G-DB-153 — Idempotent reload test.** Verifies: DB-303. Check: automated — in staging, run one day's load twice and assert the destination row counts and checksums are identical after both runs. Pass: identical state. Fail: block until the load merges or replaces partitions instead of appending. Recorded in: progress.md.
- **G-DB-154 — Schema-as-code diff.** Verifies: DB-305. Check: automated — export the warehouse's live schema/model definitions and diff against the repository's model code. Pass: zero differences. Fail: block; the drift is either committed as reviewed code or reverted. Recorded in: progress.md.

## Anti-patterns

- **Tolerance creep.** Each reconciliation failure is resolved by widening the tolerance a little, until the check cannot fail. Catch it: the tolerance history is part of the check's record (DB-310); a widened tolerance needs the same review as a metric change.
- **The PII photocopy.** The warehouse ingests entire user tables "because storage is cheap", including fields no analysis uses. Catch it: every PII column in the warehouse names the analysis that needs it (DB-304); an unnamed column is dropped.
- **Load and pray.** Loads run on a schedule but nothing watches them; the first sign of a three-day-old dashboard is a stakeholder complaint. Catch it: every dataset has a stated freshness and an alert on breach (DB-307); a dataset without one is unfinished.
- **Shadow metrics.** A team's spreadsheet quietly becomes the number executives quote, diverging from the warehouse model. Catch it: reconcile quoted figures back to the one owning model (DB-302); a figure with no model behind it is withdrawn.

## Examples

- [Example 1 — A dashboard moved off the production primary](examples/example-1.md) — corrects DB-301.
- [Example 2 — Two revenues reconciled to one definition](examples/example-2.md) — corrects DB-302.
- [Example 3 — A load that duplicated on re-run, made idempotent](examples/example-3.md) — corrects DB-303.

## Recall anchors

- The primary serves users; the warehouse serves questions.
- One metric, one definition, one model.
- Re-running a load changes nothing.
- Warehouse schemas are code or they do not exist.
- Reconciliation has a number, and the number is written down.

## Checklist

- [ ] No reporting consumer connects to the production primary (G-DB-151).
- [ ] Every headline metric resolves to one named model (DB-302).
- [ ] Re-running a day's load leaves identical counts and checksums (G-DB-153).
- [ ] Live warehouse schema diffs clean against the repo models (G-DB-154).
- [ ] Every dataset states its freshness and alerts on breach (DB-307).
- [ ] PII in the warehouse is minimized and access-controlled per dataset (DB-304).
- [ ] Reconciliation runs on schedule within the recorded tolerance (G-DB-152).
