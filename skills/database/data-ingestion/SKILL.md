# data-ingestion

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Datadog, "Implement dbt data quality checks with dbt-expectations" — https://www.datadoghq.com/blog/dbt-data-quality-testing/
- **Depends on:** data-access, secrets-management
- **Feeds into:** etl-pipelines, data-quality

## When to use / Do NOT use

- **Use when:** data is pulled from APIs, databases, files, or event streams into a landing zone — source contracts, extraction cursors, drift handling, and deduplication are being designed or changed.
- **Do NOT use when:** the data is already landed and only needs transforming (use etl-pipelines), or the flow is a user-facing API integration (use third-party-apis). Ingestion ends at a faithful, provenanced landing; everything after that is transformation.

## Rules

1. **DB-341 — Provenance on every record.** Every ingested record carries its source system, extraction timestamp, and batch or stream identifier. A record whose origin cannot be stated does not load.
2. **DB-342 — Drift goes to quarantine.** Schema drift — added, renamed, or retyped fields — fails loudly into a quarantine area with an alert. Drift never silently nulls, drops, or coerces columns downstream.
3. **DB-343 — The cursor is durable.** Incremental extraction uses a cursor (updated-at watermark, log position, or sequence) stored in durable storage outside the job's memory, advanced only after the batch it covers is safely landed.
4. **DB-344 — Redelivery is deduplicated.** Re-delivered or replayed data is deduplicated by source primary key at load. Delivering the same batch twice changes nothing downstream.
5. **DB-345 — Source contracts are explicit.** Each source has a written contract: expected schema, delivery cadence, and volume range. The contract is what drift and anomaly checks compare against.
6. **DB-346 — Anomalies are detected at the gate.** Volume anomalies and late arrivals are detected at ingestion, against the contract's ranges, before the data reaches transformation.
7. **DB-347 — Secrets stay in secret storage.** Credentials for source systems live in secret storage and are referenced, never written into pipeline code, configuration files, or the repository.
8. **DB-348 — The landing is faithful.** Ingestion preserves the source payload as received. Cleaning, typing, and reshaping happen in transformation (etl-pipelines), not during extraction.
9. **DB-349 — Quarantine has an owner and an exit.** Every quarantined batch names an owner and a resolution path — fix the contract, fix the source, or reject the batch with a record. Quarantined data is never silently auto-dropped.
10. **DB-350 — Extraction is replayable.** Re-pulling the same window from the source reproduces the same batch. An extraction that cannot be replayed cannot be audited or recovered.

## BAN list

- **BAN-DB-171 — Silently absorbed drift.** Banned: letting a changed source schema flow through by nulling new fields, dropping renamed columns, or coercing types without an error. Defeats: DET-CODE-005. Bad: the source renames `total_amount` to `totalAmount`; the loader's mapping misses it, the column lands as NULL for three weeks, and revenue reporting quietly under-reports. Instead: the batch fails the contract check and lands in quarantine with an alert (DB-342). Severity: BLOCK.
- **BAN-DB-172 — Secrets in pipeline code.** Banned: source-system credentials written into pipeline code, configuration files, or the repository. Defeats: DET-INF-005. Bad: the extraction script contains the source database's password in a connection string committed to the repo, where it survives in history even after rotation. Instead: the credential lives in secret storage and the pipeline references it by name (DB-347). Severity: BLOCK.
- **BAN-DB-173 — The in-memory cursor.** Banned: keeping the incremental extraction cursor in the job's memory or a local file on one machine. Defeats: DET-CODE-023. Bad: the job restarts after a crash with the watermark reset to zero — or worse, to a stale file — and a month of records is re-ingested as duplicates or a day is skipped entirely. Instead: the cursor is a row in durable storage, advanced transactionally after the batch lands (DB-343). Severity: BLOCK.
- **BAN-DB-174 — Check-then-insert dedup.** Banned: deduplicating by reading for an existing key and then inserting when absent, as two separate steps. Defeats: DET-CODE-030. Bad: a redelivered batch runs concurrently with the original delivery; both checks see "absent", both insert, and every record in the batch exists twice. Instead: dedup is enforced by a unique constraint on the source primary key with an idempotent merge/upsert at load (DB-344). Severity: BLOCK.

## Gates

- **G-DB-171 — Drift test.** Verifies: DB-342, DB-345. Check: automated — in staging, feed a payload with an added field and a renamed field and assert (a) the batch is quarantined, (b) an alert fires, (c) nothing from the batch reaches the landing tables. Pass: all three hold. Fail: block shipment. Recorded in: progress.md.
- **G-DB-172 — Replay test.** Verifies: DB-344, DB-350. Check: automated — deliver the same batch twice and assert destination row counts and checksums are unchanged after the second delivery. Pass: identical state. Fail: block until dedup is enforced by key, not by timing. Recorded in: progress.md.
- **G-DB-173 — Provenance completeness.** Verifies: DB-341. Check: automated — sample landed records from every source and assert 100% carry source system, extraction timestamp, and batch/stream identifier. Pass: no record missing any of the three. Fail: block the source's promotion until provenance is stamped at extraction. Recorded in: progress.md.
- **G-DB-174 — Secret scan.** Verifies: DB-347. Check: automated — scan pipeline code and configuration in the repository with a credential-pattern scanner (e.g. gitleaks) including connection-string patterns. Pass: zero findings. Fail: block, rotate any exposed credential, and move it to secret storage. Recorded in: progress.md.

## Anti-patterns

- **Trusting the API.** The source's schema is assumed stable because it has not changed yet, so no contract exists. Catch it: ask for the contract document (DB-345); "the API is stable" is not one.
- **Watermark amnesia.** After a failed run, someone manually resets the cursor "to be safe" and a window is silently re-ingested or skipped. Catch it: cursor changes outside the job's own transactional advance are the tell (DB-343); the cursor's history is auditable.
- **The quarantine graveyard.** Drifted batches pile up in quarantine unreviewed while downstream quietly runs on older data. Catch it: quarantine age is a reported number with an owner per batch (DB-349); an aging quarantine is an incident, not a backlog.
- **Provenance by folder name.** The batch identity exists only in a filename or directory, and is lost the moment records are loaded into a table. Catch it: sample a landed row and state its batch from the row itself (G-DB-173); if you need the filesystem to answer, provenance is not stored.

## Examples

- [Example 1 — Drift absorbed silently, replaced with contract check and quarantine](examples/example-1.md) — corrects DB-342.
- [Example 2 — An in-memory watermark replaced with a durable cursor](examples/example-2.md) — corrects DB-343.
- [Example 3 — A redelivered batch deduplicated by source key](examples/example-3.md) — corrects DB-344.

## Recall anchors

- Every record can state where it came from and when.
- Drift quarantines loudly; it never loads quietly.
- The cursor lives in durable storage, not in the job.
- Deliver it twice; it lands once.
- Secrets are referenced, never written down in code.

## Checklist

- [ ] Every source has a written contract: schema, cadence, volume range (DB-345).
- [ ] A drifted payload is quarantined and alerted, not loaded (G-DB-171).
- [ ] Re-delivering a batch changes no destination counts (G-DB-172).
- [ ] Sampled records all carry source, extraction time, and batch ID (G-DB-173).
- [ ] The credential scan over pipeline code and config is clean (G-DB-174).
- [ ] The cursor is stored durably and advanced only after landing (DB-343).
- [ ] Quarantined batches have named owners and an exit path (DB-349).
