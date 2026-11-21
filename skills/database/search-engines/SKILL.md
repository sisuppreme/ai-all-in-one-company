# search-engines

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** PostgreSQL documentation, "Text Search Functions and Operators" — https://www.postgresql.org/docs/10/functions-textsearch.html ; PROJECT_ANATOMY.md Part 3, *Search*
- **Depends on:** indexing, data-access, schema-design
- **Feeds into:** vector-db, caching, data-warehousing

## When to use / Do NOT use

- **Use when:** building or reviewing user-facing search — choosing between PostgreSQL full-text search and a dedicated engine, wiring index updates, setting a freshness contract, or evaluating ranking changes.
- **Do NOT use when:** the lookup is an exact key or ID fetch (that is data-access), or the "search" is an admin filter over a few hundred rows that a plain indexed query serves honestly. Do not adopt a dedicated engine to look serious; adopt it for a named need.

## Rules

1. **DB-261 — Start with PostgreSQL full-text search.** `tsvector`/`tsquery` with weighted fields, `ts_rank`, and a GIN index is the default. A dedicated engine (Elasticsearch/OpenSearch/Typesense class) is adopted only for a named need: typo tolerance, faceting at scale, language analyzers, or search load isolation.
2. **DB-262 — The index is a derived artifact.** It is updated from the write path — transactional outbox or change events — never by periodic manual re-indexing or by editing the index directly.
3. **DB-263 — Freshness is a contract.** The maximum lag between a write and its searchability is stated in writing and monitored like any other SLO.
4. **DB-264 — Deletes and updates travel with the write.** A record leaves or changes in the index in the same flow that changes it in the database. Deleted records never linger in results.
5. **DB-265 — Ranking is evaluated, not felt.** Ranking changes are tested against a fixed query set with expected top results, before and after, and the comparison is recorded.
6. **DB-266 — The index rebuilds by one command.** The full index can be dropped and rebuilt from the source of truth by a single documented command, and the rebuild is exercised in staging.
7. **DB-267 — Filters are structured parameters.** Facets and filters reach the search layer as structured parameters, never as string-built query fragments.
8. **DB-268 — Search shows index use.** The search query's plan uses its index (GIN or the engine's equivalent); a sequential scan over the catalog per keystroke is a defect.
9. **DB-269 — The database stays the source of truth.** Search returns identifiers and ranking; records that may have changed since indexing are verified or re-fetched from the database before display or action.
10. **DB-270 — Language handling is explicit.** Analyzer, stemming, and stop-word configuration is chosen per field and recorded, never inherited silently from engine defaults.

## BAN list

- **BAN-DB-131 — LIKE-as-search.** Banned: shipping `LIKE '%term%'` (or `ILIKE`) against the primary table as the product's search feature. Defeats: DET-CODE-003. Bad: the catalog search runs `WHERE name LIKE '%shoe%'` — unindexed, unordered by relevance, and presented to users as "search". Instead: PostgreSQL full-text search with a `tsvector` column, GIN index, and `ts_rank` ordering (DB-261). Severity: BLOCK.
- **BAN-DB-132 — The sequential-scan search.** Banned: a search path whose plan scans the full table on every request. Defeats: DET-CODE-033. Bad: each keystroke in the search box triggers a full scan of the two-million-row products table on the primary, so typing becomes a denial-of-service on the database. Instead: an indexed search path, verified by `EXPLAIN` in CI (DB-268). Severity: BLOCK.
- **BAN-DB-133 — The unrebuildable index.** Banned: a search index that exists only because a one-off script or manual process built it once. Defeats: DET-INF-004. Bad: the index was populated from a laptop script during launch week; after corruption, nobody can recreate it and search stays broken for days. Instead: one documented rebuild command from the source of truth, tested in staging (DB-266). Severity: BLOCK.
- **BAN-DB-134 — Ranking by feel.** Banned: changing ranking weights, boosts, or ordering in production with no fixed evaluation set. Defeats: DET-CODE-013. Bad: a title boost is doubled because results "looked off"; nobody can say whether search improved or regressed, and the next change starts from folklore. Instead: run the fixed query set with expected top results before and after every ranking change (DB-265). Severity: BLOCK.

## Gates

- **G-DB-131 — Search correctness test.** Verifies: DB-262, DB-264, DB-268. Check: automated — create a record containing a distinctive word and assert it appears in results; run `EXPLAIN` on the search query and assert index use; delete the record and assert it disappears from results. Pass: all three assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-DB-132 — Rebuild parity test.** Verifies: DB-266. Check: automated — in staging, drop the index, run the documented rebuild command, and assert the fixed query set returns identical top results to the pre-drop run. Pass: full parity. Fail: block shipment. Recorded in: progress.md.
- **G-DB-133 — Freshness check.** Verifies: DB-263. Check: automated — write a record and measure time-to-searchable against the stated lag contract, on a schedule in staging and by metric alert in production. Pass: lag within contract. Fail: warn in staging, block a search launch. Recorded in: progress.md.
- **G-DB-134 — Ranking evaluation gate.** Verifies: DB-265. Check: automated — the fixed query set's expected top results are asserted in CI; any ranking change must keep the suite green or update expectations with a recorded before/after comparison. Pass: suite green. Fail: block shipment of the ranking change. Recorded in: progress.md.

## Anti-patterns

- **Engine-first adoption.** A dedicated search cluster is stood up for five hundred rows that PostgreSQL full-text search serves trivially, and its operations burden arrives immediately. Catch it: DB-261 demands the named need in writing before the engine exists.
- **The bypassed write path.** One import job writes the database directly, skipping the events that update the index, and its records are unsearchable forever. Catch it: every write path is enumerated; the index update hangs off the write, not off the application endpoint.
- **Relevance by recency.** Results are sorted by `created_at` because ranking was never configured, so the best match sits under last week's additions. Catch it: if `ts_rank` or an engine score is not in the ordering, it is not search ranking.
- **Ghost results.** Deleted products keep appearing because deletes were never wired to the index. Catch it: the correctness gate deletes a record and looks for it — run it, don't assume it.

## Examples

- [Example 1 — LIKE '%term%' replaced by full-text search with ranking](examples/example-1.md) — corrects DB-261.
- [Example 2 — Deleted record lingering in results, fixed by same-flow index delete](examples/example-2.md) — corrects DB-264.
- [Example 3 — One-off index build replaced by a documented rebuild with parity test](examples/example-3.md) — corrects DB-266.

## Recall anchors

- PostgreSQL full-text first; a dedicated engine needs a named need.
- The index is derived: written by the write path, rebuilt by one command.
- Freshness is a contract with a number, monitored like an SLO.
- Deletes leave the index in the same flow as the database.
- Ranking changes pass a fixed query set, never a vibe check.

## Checklist

- [ ] The engine choice names its need, or PostgreSQL full-text search is used (DB-261).
- [ ] The correctness test passes: create appears, plan uses the index, delete disappears (G-DB-131).
- [ ] The freshness contract is stated and the freshness check passes (DB-263, G-DB-133).
- [ ] The rebuild command is documented and the parity test passes in staging (DB-266, G-DB-132).
- [ ] The fixed ranking query set is green (G-DB-134).
- [ ] Filters and facets are structured parameters, not string-built fragments (DB-267).
