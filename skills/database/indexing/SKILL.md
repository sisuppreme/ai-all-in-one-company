# indexing

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** PostgreSQL documentation, "Text Search Functions and Operators" (GIN on `tsvector`) — https://www.postgresql.org/docs/10/functions-textsearch.html ; pgvector documentation (HNSW index construction) — https://access.crunchydata.com/documentation/pgvector/0.8.3/pdf/pgvector.pdf
- **Depends on:** schema-design, migrations, query-performance
- **Feeds into:** query-performance, search-engines, data-access

## When to use / Do NOT use

- **Use when:** designing indexes for new query patterns, reviewing why a query cannot use an existing index, auditing index bloat, or adding an index to a table that already holds production data.
- **Do NOT use when:** the query itself is malformed (fix it under query-performance first) or the table is small enough that a sequential scan is the planner's correct choice. Do not use it to paper over a schema that models the domain wrong.

## Rules

1. **DB-161 — Indexes come from the query log.** Every index is designed from an actual, named query pattern. Speculative indexes "for later" are not created.
2. **DB-162 — Foreign keys and tenant columns are indexed.** Every foreign key column and every column used in tenant scoping carries an index, by default, from the migration that creates the table.
3. **DB-163 — Composite order follows the query.** Equality columns come first, the range or sort column last. An index whose leftmost column no query filters on is dead weight and is fixed or dropped.
4. **DB-164 — Cover hot read paths.** Where a hot query's columns fit, build a covering index with `INCLUDE` so the planner can answer with an index-only scan and skip heap fetches.
5. **DB-165 — Partial indexes for hot subsets.** When the hot set is a small, stable slice (for example `status = 'active'`), index the slice, not the table.
6. **DB-166 — The index type matches the operator.** B-tree for equality/range/order; GIN for `tsvector` full-text and JSONB containment; GiST or HNSW where the operator (similarity, geometry) demands it. A mismatch means the index is silently unused.
7. **DB-167 — Usage is audited on a schedule.** `pg_stat_user_indexes` is reviewed per release; indexes with no scans are dropped through a migration, with the audit recorded.
8. **DB-168 — Large-table indexes are built concurrently.** `CREATE INDEX CONCURRENTLY` (or the engine equivalent) outside a transaction block, and the resulting index size is recorded.
9. **DB-169 — Every index names its query.** The migration or SCHEMA.md states which query each index serves. An index nobody can attribute is a removal candidate.
10. **DB-170 — Write cost is counted.** Every index taxes every insert and update on its table. An index no read uses is removed, never kept "just in case".

## BAN list

- **BAN-DB-081 — Index-on-every-column.** Banned: adding indexes speculatively across a table's columns "for performance" without a query behind each one. Defeats: DET-CODE-015. Bad: a migration indexes all fourteen columns of `orders`; write throughput drops and none of the new indexes is ever scanned. Instead: index from the query log, one named query per index (DB-161, DB-169). Severity: BLOCK.
- **BAN-DB-082 — The unusable composite.** Banned: a composite index whose column order no real query can use leftmost, shipped as if the query were indexed. Defeats: DET-CODE-003. Bad: `INDEX (created_at, tenant_id)` while every query filters `tenant_id` first; the planner ignores it and the team believes tenant queries are covered. Instead: equality columns first — `INDEX (tenant_id, created_at)` — and prove use with `EXPLAIN`. Severity: BLOCK.
- **BAN-DB-083 — The fossil index.** Banned: leaving an index with zero recorded scans in place release after release. Defeats: DET-CODE-002. Bad: `idx_orders_legacy_ref` has no scans in a year of `pg_stat_user_indexes` history and still taxes every insert. Instead: audit per release and drop unused indexes through a migration (DB-167). Severity: WARN.
- **BAN-DB-084 — The locking index build.** Banned: building an index on a large production table with a plain in-transaction `CREATE INDEX` that blocks writes for the duration. Defeats: DET-INF-018. Bad: a migration runs `CREATE INDEX` on the 40-million-row `events` table inside the deploy transaction; writes queue for half an hour. Instead: `CREATE INDEX CONCURRENTLY` outside a transaction block (DB-168). Severity: BLOCK.

## Gates

- **G-DB-081 — Hot-query plan assertions.** Verifies: DB-161, DB-163, DB-164. Check: automated — CI runs `EXPLAIN` for each registered hot query against a seeded production-shaped fixture; the plan must show `Index Scan` or `Index Only Scan`, never `Seq Scan` on the large table. Pass: all registered queries use an index. Fail: block shipment. Recorded in: progress.md.
- **G-DB-082 — FK and tenant index coverage.** Verifies: DB-162. Check: automated — a catalog query against `pg_catalog` lists every foreign key column and tenant-scoping column lacking a supporting index. Pass: the list is empty. Fail: block shipment. Recorded in: progress.md.
- **G-DB-083 — Unused-index report.** Verifies: DB-167, DB-170. Check: automated report, human sign-off — per release, dump indexes with zero scans from `pg_stat_user_indexes`; each is dropped by migration or kept with a written reason. Pass: report reviewed and dispositions recorded. Fail: warn. Recorded in: progress.md.
- **G-DB-084 — Concurrent-build check.** Verifies: DB-168. Check: automated — scan new migrations for `CREATE INDEX` without `CONCURRENTLY` on tables above the project's large-table threshold. Pass: no matches. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Index as apology.** An index is added instead of fixing the query's shape, and both the bad query and the write tax survive. Catch it: ask which rule of query-performance was checked before the index was proposed.
- **Duplicate twins.** Two indexes cover the same columns in slightly different orders and both are kept because nobody knows which one matters. Catch it: the usage audit names a survivor; the other goes.
- **The console index.** An index created by hand in a production console during an incident, never written into a migration — the next environment simply lacks it. Catch it: diff the production catalog against the migration-built schema.
- **Statistics blindness.** A good index is declared useless because stale statistics steer the planner away from it. Catch it: check `ANALYZE` freshness before judging any index (DB-150).

## Examples

- [Example 1 — Composite index reordered so the query can use it](examples/example-1.md) — corrects DB-163.
- [Example 2 — Covering index with INCLUDE reaching an index-only scan](examples/example-2.md) — corrects DB-164.
- [Example 3 — Fossil index found by audit and dropped by migration](examples/example-3.md) — corrects DB-167.

## Recall anchors

- No query, no index.
- Equality first, range last — or the planner walks past.
- Cover the hot path and skip the heap.
- Every index taxes every write; unused means dropped.
- Large tables get concurrent builds, never locking ones.

## Checklist

- [ ] Every new index names the query it serves (DB-169).
- [ ] All foreign key and tenant-scoping columns are indexed (DB-162, G-DB-082).
- [ ] Registered hot queries show index scans in CI plan assertions (G-DB-081).
- [ ] Composite column order matches the queries: equality first, range last (DB-163).
- [ ] Indexes on large tables are built concurrently, size recorded (DB-168, G-DB-084).
- [ ] The unused-index report was reviewed this release and dispositions recorded (G-DB-083).
