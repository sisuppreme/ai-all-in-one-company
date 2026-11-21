# sql-fundamentals

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** PostgreSQL documentation, "Text Search Functions and Operators" (operator/function precision) — https://www.postgresql.org/docs/10/functions-textsearch.html
- **Depends on:** schema-design
- **Feeds into:** data-access, query-performance, search-engines

## When to use / Do NOT use

- **Use when:** writing or reviewing any SQL or ORM query — selects, joins, aggregates, updates — in application code, jobs, or reports.
- **Do NOT use when:** designing the tables themselves (use schema-design), tuning a query already known to be slow (use query-performance), or choosing indexes (use indexing).

## Rules

1. **DB-021 — Parameters, always.** Every value reaches SQL as a bound parameter. No value is ever concatenated or interpolated into a query string, in any layer, including admin scripts and seeds.
2. **DB-022 — Identifiers come from allowlists.** Table names, column names, and sort directions cannot be bound parameters, so they are selected from a server-side allowlist keyed by the client's token. A request value is never used as an identifier directly.
3. **DB-023 — Name the columns.** Application queries list their columns explicitly. `SELECT *` does not appear in application code.
4. **DB-024 — See the generated SQL.** Every query's generated SQL is inspected at least once in development (query logging on) before the change merges. An ORM call nobody has seen the SQL for is unreviewed.
5. **DB-025 — No N+1.** Collection loads are eager or batched. A loop that issues one query per row of a previous result is a defect, verified by query counts in tests, not by reading the code hopefully.
6. **DB-026 — Aggregate in the database.** Filtering, grouping, and aggregation happen in SQL. Fetching rows to count, sum, or filter them in application memory is a defect.
7. **DB-027 — NULL is explicit.** Comparisons use `IS NULL` / `IS NOT NULL`; `COALESCE` states the fallback; the author knows how the engine's unique constraint treats NULLs on each unique column they touch.
8. **DB-028 — Know your join cardinality.** Before aggregating over a join, state whether it can multiply rows. Totals computed across a one-to-many join are verified against the pre-join count.
9. **DB-029 — Think in sets.** Multi-step read logic uses CTEs and window functions inside one query instead of row-by-row processing loops in application code.
10. **DB-030 — Bound every result.** Any query that can return a collection carries an explicit limit or is consumed through pagination/streaming. "The table is small" is not a bound.

## BAN list

- **BAN-DB-011 — Interpolated values.** Banned: building SQL by string concatenation or template interpolation of any value (`"... WHERE id = " + id`, `` `SELECT ... ${req.params.q}` ``). Defeats: DET-CODE-017. Bad: a search endpoint interpolates the `q` parameter; `q = ' OR '1'='1` returns the whole users table. Instead: bound parameters for every value, in every query, with no "internal use only" exceptions. Severity: BLOCK.
- **BAN-DB-012 — Interpolated identifiers.** Banned: using a request value as a column name, table name, or sort direction (`ORDER BY ${sort}`), even when all other values are parameterized. Defeats: DET-CODE-017. Bad: `?sort=email; DROP TABLE users--` reaches the query because the developer parameterized the filters and forgot the sort. Instead: map the client's token through a fixed allowlist (`{ "name": "name", "date": "created_at" }`) and reject unknown tokens. Severity: BLOCK.
- **BAN-DB-013 — `SELECT *` in application code.** Banned: wildcard column lists in shipped queries. Defeats: DET-CODE-033. Bad: a list endpoint selects every column including a `bio text` and an `avatar_blob`, shipping megabytes per page of JSON. Instead: name exactly the columns the caller uses. Severity: WARN.
- **BAN-DB-014 — Fetch-then-compute.** Banned: loading a table (or an unbounded slice of it) into application memory to filter, count, sum, or loop over it row by row. Defeats: DET-CODE-033. Bad: the dashboard loads all orders for the year and sums them in a `for` loop; it works on the 50-row demo data and times out in the first real month. Instead: `GROUP BY`/`HAVING`, window functions, or a batched eager load in SQL. Severity: WARN.

## Gates

- **G-DB-011 — Static SQL lint.** Verifies: DB-021, DB-022, DB-023. Check: automated — CI greps the data-access layer for string concatenation/template interpolation inside query calls and for `SELECT *`; zero hits allowed. Pass: zero hits. Fail: block shipment. Recorded in: progress.md.
- **G-DB-012 — Query-count assertion.** Verifies: DB-025. Check: automated — integration tests for list endpoints assert the executed query count stays at or below the stated bound (e.g. ≤ 3) as the fixture row count grows from 5 to 50. Pass: count is flat. Fail: block shipment. Recorded in: progress.md.
- **G-DB-013 — Injection probe.** Verifies: DB-021, DB-022. Check: automated — the test suite sends quote and boolean payloads (`' OR '1'='1`, `email; DROP TABLE users--` as a sort token) to filter and sort parameters; every payload must return literal-match results or a 4xx, never extra rows. Pass: no payload alters the result set. Fail: block shipment. Recorded in: progress.md.
- **G-DB-014 — SQL inspection record.** Verifies: DB-024. Check: manual — the change description includes the logged generated SQL for each new or changed query; a reviewer confirms it was read. Pass: SQL attached for every query. Fail: warn and hold merge until attached. Recorded in: progress.md.

## Anti-patterns

- **The ORM mirage.** The code calls tidy model methods and nobody has ever seen the SQL, so the N+1 and the accidental full-table scan ship invisibly. Catch it: turn on query logging and read one request end to end.
- **The NULL surprise.** `WHERE status = NULL` returns nothing, and the author "fixes" it by deleting the filter instead of writing `IS NULL`. Catch it: any comparison against a nullable column names its NULL behavior.
- **Join fan-out.** Totals quietly double after a one-to-many join is added upstream of a `SUM`. Catch it: compare the aggregate against the pre-join row count whenever a join is added.
- **Demo-data tuning.** The query is declared fast because the development table has twelve rows. Catch it: ask what the row count is in production and whether the query was ever run against a realistic volume.

## Examples

- [Example 1 — Parameterizing a search query](examples/example-1.md) — corrects DB-021, DB-022.
- [Example 2 — Killing an N+1](examples/example-2.md) — corrects DB-025.
- [Example 3 — Aggregating in SQL with explicit NULL handling](examples/example-3.md) — corrects DB-026, DB-027.

## Recall anchors

- Values are parameters; identifiers are allowlists.
- If you have not seen the generated SQL, you have not reviewed the query.
- Aggregate in the database, not in a loop.
- NULL is a case you handle, not a surprise you meet.
- Every collection result is bounded.

## Checklist

- [ ] No query in the change interpolates a value or an identifier (DB-021, DB-022, G-DB-011).
- [ ] The injection probe passes for filter and sort parameters (G-DB-013).
- [ ] No `SELECT *` in application queries; column lists are named (DB-023).
- [ ] Generated SQL for each new query was logged and read (DB-024, G-DB-014).
- [ ] List endpoints pass the query-count assertion at growing fixture sizes (DB-025, G-DB-012).
- [ ] Aggregates run in SQL; NULL handling is explicit on every nullable column touched (DB-026, DB-027).
