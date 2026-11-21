# query-performance

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** PostgreSQL documentation — https://www.postgresql.org/docs/10/functions-textsearch.html ; PROJECT_ANATOMY.md Part 3, *Caching* and *Search* (EXPLAIN-based Verify lines)
- **Depends on:** schema-design, data-access, indexing
- **Feeds into:** indexing, read-replicas, caching

## When to use / Do NOT use

- **Use when:** an endpoint or job is slow, a slow-query report lands, a hot query is being written or changed, or a release needs its latency budget defended with evidence.
- **Do NOT use when:** the schema itself is wrong for the access pattern (fix it with schema-design first), or the slowness is in application code with no database involvement. Do not use it to justify engine tuning before the queries themselves are fixed.

## Rules

1. **DB-141 — Measure first.** Optimization starts from the database's own evidence — `pg_stat_statements` rankings or the slow-query log — never from a guess about which query is slow.
2. **DB-142 — Before/after plans or it didn't happen.** Every optimization records a before and after `EXPLAIN (ANALYZE, BUFFERS)` plus timing, run on production-shaped data (comparable row counts and distribution), not on an empty development database.
3. **DB-143 — Hot paths carry a latency budget.** Each registered hot query has a stated budget; a change that regresses a hot query past its budget fails review.
4. **DB-144 — Keyset pagination on large lists.** Pagination over large or unbounded result sets is cursor/keyset-based on a stable sort key. Deep `OFFSET` is a defect, not a style choice.
5. **DB-145 — Name the columns.** `SELECT` lists name the columns the caller needs. Over-fetching wide rows (especially text/blob columns) is a performance bug.
6. **DB-146 — Slow-query logging is on in production.** It runs with a stated threshold, and the top offenders are reviewed on a schedule; the review is recorded, not remembered.
7. **DB-147 — Fix in order.** Missing index → wrong join or ordering → N+1 → over-fetching → engine tuning, in that order. Engine parameters are touched only after the query-level causes are exhausted.
8. **DB-148 — No N+1.** Collection loads are eager or batched. List endpoints prove it with a query-count assertion, not by inspection.
9. **DB-149 — Compute in the database.** Aggregates, filters, and sorts that the database can do are done by the database, not by fetching rows and computing in application memory.
10. **DB-150 — Keep statistics honest.** When plans degrade without a query change, check `ANALYZE`/autovacuum health before blaming the query or the index.

## BAN list

- **BAN-DB-071 — Deep OFFSET pagination.** Banned: paging large lists with `LIMIT n OFFSET <large>` so cost grows with page depth. Defeats: DET-CODE-033. Bad: the orders API serves page 500 with `LIMIT 20 OFFSET 10000`, scanning and discarding ten thousand rows per request. Instead: keyset pagination on the sort key (`WHERE (created_at, id) < ($1, $2) ORDER BY created_at DESC, id DESC LIMIT 20`). Severity: BLOCK.
- **BAN-DB-072 — The unmeasured "optimization".** Banned: merging a change described as a performance fix with no plan or timing evidence behind it. Defeats: DET-CODE-003. Bad: a pull request titled "optimize dashboard query" rewrites the SQL, shows no `EXPLAIN`, and the sequential scan ships anyway. Instead: attach before/after `EXPLAIN (ANALYZE, BUFFERS)` output on production-shaped data, or do not call it an optimization. Severity: BLOCK.
- **BAN-DB-073 — The hot query with no plan test.** Banned: changing a registered hot query without a plan assertion in CI that would catch a sequential scan. Defeats: DET-CODE-013. Bad: the checkout query is rewritten during a refactor; nothing fails, and it scans the full orders table in production. Instead: register the query and assert its plan in CI against a seeded fixture. Severity: BLOCK.
- **BAN-DB-074 — Diagnostic logging left on in production.** Banned: shipping per-query `EXPLAIN ANALYZE` or full query logging in production code paths. Defeats: DET-CODE-029. Bad: every production query is logged with its plan, flooding the log store and adding latency to every write. Instead: threshold-based slow-query logging with sampling; full plans are captured in staging or in a bounded diagnostic window. Severity: WARN.

## Gates

- **G-DB-071 — Plan assertion suite.** Verifies: DB-142, DB-143. Check: automated — CI runs `EXPLAIN` for every registered hot query against a seeded production-shaped fixture and fails if the plan shows a sequential scan on the large table or exceeds the query's stated budget. Pass: all registered queries pass. Fail: block shipment. Recorded in: progress.md.
- **G-DB-072 — Query-count tests.** Verifies: DB-148. Check: automated — integration tests on list endpoints assert the number of executed queries stays at the registered maximum as fixture size doubles. Pass: counts flat. Fail: block shipment. Recorded in: progress.md.
- **G-DB-073 — Evidence check on performance changes.** Verifies: DB-141, DB-142. Check: manual review — every change claiming a performance improvement carries before/after plan output and timings on production-shaped data. Pass: evidence present and shows the claimed improvement. Fail: warn and return the change for measurement. Recorded in: progress.md.
- **G-DB-074 — Slow-log review record.** Verifies: DB-146. Check: manual — the scheduled review of the production slow-query log's top offenders exists in the project record with dispositions (fixed, accepted, escalated). Pass: review current within its schedule window. Fail: warn. Recorded in: progress.md.

## Anti-patterns

- **Empty-database tuning.** The plan "looks instant" against twelve rows, so the query ships and meets production volume for the first time live. Catch it: demand the fixture's row count next to every plan you review.
- **Index-first reflex.** An index is added before anyone reads the plan, and the real cause — a bad join — survives untouched. Catch it: DB-147's order is a sequence, not a menu.
- **The one-query hero.** The single worst query is optimized while the endpoint still fires two hundred small ones. Catch it: check the endpoint's query count, not just its slowest member.
- **Tuning as camouflage.** `work_mem` and buffer settings creep up release after release while the queries stay wrong. Catch it: any engine-parameter change must name the query-level causes already ruled out.

## Examples

- [Example 1 — Sequential scan to index scan, with evidence](examples/example-1.md) — corrects DB-142.
- [Example 2 — Deep OFFSET replaced by keyset pagination](examples/example-2.md) — corrects DB-144.
- [Example 3 — N+1 loop replaced by one batched load](examples/example-3.md) — corrects DB-148.

## Recall anchors

- Measure from the database's own statistics, not from suspicion.
- No before/after plan, no optimization claim.
- Keyset pages; OFFSET depth is a defect.
- Name columns; the database computes, the app does not fetch-and-filter.
- Fix queries in order; tune the engine last.

## Checklist

- [ ] Slow-query evidence (pg_stat_statements or slow log) identified the target queries (DB-141).
- [ ] Before/after `EXPLAIN (ANALYZE, BUFFERS)` recorded on production-shaped data (DB-142).
- [ ] Plan assertion suite passes for every registered hot query (G-DB-071).
- [ ] List endpoints pass their query-count assertions (G-DB-072).
- [ ] Large lists use keyset pagination; no deep `OFFSET` remains (DB-144).
- [ ] Production slow-query logging is on with a threshold, and the last review is recorded (DB-146, G-DB-074).
