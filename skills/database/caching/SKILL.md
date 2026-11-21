# caching

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Redis documentation, "Redis cache-aside" — https://redis.io/docs/latest/develop/use-cases/cache-aside/ ; PROJECT_ANATOMY.md Part 3, *Caching*
- **Depends on:** data-access, schema-design
- **Feeds into:** query-performance, read-replicas, search-engines

## When to use / Do NOT use

- **Use when:** adding or reviewing a cache for data that is expensive to compute or read hot, setting TTL and invalidation policy, or debugging stale-data and cache-outage behavior.
- **Do NOT use when:** the data must never be stale (balances mid-transaction, permission checks at write time) — read the database. Do not use a cache to hide an unindexed query; fix the query under query-performance/indexing first, then cache what is still hot.

## Rules

1. **DB-241 — Cache-aside is the default pattern.** Check the cache; on a miss, read the database, store the result under a deterministic key with a TTL, and return it. Other patterns are chosen explicitly, with reasons.
2. **DB-242 — Every entry has a TTL.** No cached entry lives without an expiry. "No expiry" requires a written exception naming the entry class and why it is safe.
3. **DB-243 — Invalidation is delete-on-write.** Writes update the database and delete the affected cache keys. The database is the only source of truth; the cache is a disposable copy.
4. **DB-244 — Keys come from one scoped helper.** Key construction goes through a single helper that namespaces by entity, version, and tenant/user scope. Hand-built key strings are forbidden.
5. **DB-245 — Per-user data is keyed per user, or not cached.** Data that differs by user or tenant is never stored under a key another user or tenant can hit.
6. **DB-246 — The app survives a dead cache.** With the cache flushed or down, the application runs correctly — slower — reading from the database. A cache failure must never become wrong data or an outage.
7. **DB-247 — Hot keys have stampede protection.** A hot key's expiry is guarded by a lock, request coalescing, or probabilistic early refresh, so one expiry cannot send every request to the database at once.
8. **DB-248 — Cache only the stale-tolerant.** An entry class is cached only if it is expensive or hot and safe to serve slightly stale; its staleness tolerance is stated where the caching is defined.
9. **DB-249 — Hit ratio is monitored.** Hit ratio and evictions are metrics with review; a silent 0% hit ratio is treated as a bug, not as a neutral fact.
10. **DB-250 — All writes flow through the data-access layer.** Delete-on-write works only if no write path bypasses the layer; raw-SQL jobs and scripts that write cached entities go through the same invalidation, or the cache is not trusted for that entity.

## BAN list

- **BAN-DB-121 — The eternal entry.** Banned: caching data with no TTL and no invalidation path, so it can be served stale forever. Defeats: DET-CODE-033. Bad: product prices are cached with no expiry; a price change in the database never appears on the site, indefinitely. Instead: a TTL on every entry plus delete-on-write invalidation (DB-242, DB-243). Severity: BLOCK.
- **BAN-DB-122 — The shared per-user key.** Banned: storing per-user or per-tenant data under a key that does not include that user or tenant. Defeats: DET-CODE-020. Bad: the key `dashboard:home` holds whichever user's account summary was computed last and serves it to the next user — a cross-user data leak. Instead: keys built by the scoped helper, including tenant/user scope (DB-244, DB-245). Severity: BLOCK.
- **BAN-DB-123 — The cache as the database.** Banned: keeping the only copy of any record in the cache. Defeats: DET-INF-008. Bad: order state is written only to Redis "for speed"; an eviction under memory pressure deletes live orders permanently. Instead: write to the database first; the cache holds a disposable copy (DB-243). Severity: BLOCK.
- **BAN-DB-124 — The load-bearing cache.** Banned: a design where a cache outage takes the application down or serves errors instead of falling back. Defeats: DET-INF-019. Bad: when Redis restarts, every page errors because reads hard-depend on cache hits. Instead: cache failures fall back to database reads (DB-246). Severity: BLOCK.

## Gates

- **G-DB-121 — Cache behavior test.** Verifies: DB-241, DB-243. Check: automated — an integration test with query logging on requests the same resource twice and asserts the second request issues no database query; then it updates the record and asserts the old value is no longer served. Pass: both assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-DB-122 — Key-namespace lint.** Verifies: DB-244, DB-245. Check: automated — a scan fails the build if cache keys are constructed anywhere except the scoped key helper. Pass: zero ad-hoc key constructions. Fail: block shipment. Recorded in: progress.md.
- **G-DB-123 — TTL coverage check.** Verifies: DB-242. Check: automated — a static scan of cache writes in the codebase flags any write without a TTL argument and without a registered written exception. Pass: no unflagged writes. Fail: block shipment. Recorded in: progress.md.
- **G-DB-124 — Cache-down drill.** Verifies: DB-246. Check: automated — in staging, flush and stop the cache, then run the smoke suite against the application. Pass: responses are correct (slower is acceptable); no stale or wrong data, no error pages. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Cache everything.** Cheap queries get cached too, until invalidation spans the whole schema and nobody dares change anything. Catch it: DB-248 — if you cannot state the entry's cost and staleness tolerance, it does not belong in the cache.
- **Update-instead-of-delete.** One path writes the new value into the cache while another writes only the database, and the two copies drift by write path. Catch it: there is exactly one invalidation verb — delete (DB-243).
- **TTL roulette.** The same entity gets five different TTLs from five call sites, each invented on the spot. Catch it: TTLs are defined per entry class in one place, next to the tolerance statement.
- **Miss-storm blindness.** A hot key that is absent (a 404, an unconfigured product) is re-fetched from the database on every request because misses are never cached or coalesced. Catch it: check what a cache miss storm looks like in the load test, not just the hit path.

## Examples

- [Example 1 — Price stale forever, fixed by TTL plus delete-on-write](examples/example-1.md) — corrects DB-242, DB-243.
- [Example 2 — Shared dashboard key replaced by the scoped key helper](examples/example-2.md) — corrects DB-244, DB-245.
- [Example 3 — Cache outage taking the site down, fixed by database fallback](examples/example-3.md) — corrects DB-246.

## Recall anchors

- Cache-aside: miss reads the database, stores with a TTL, writes delete.
- Every entry expires; the database is the only source of truth.
- Keys are built by one helper and carry tenant/user scope.
- A dead cache means a slower app, never a wrong one.
- Stampede protection guards every hot key.

## Checklist

- [ ] Every cached entry class has a TTL and a stated staleness tolerance (DB-242, DB-248).
- [ ] Writes delete affected keys through the data-access layer (DB-243, DB-250).
- [ ] All keys are built by the scoped helper; the lint is clean (G-DB-122).
- [ ] The cache behavior test passes: second read hits cache, update invalidates (G-DB-121).
- [ ] The cache-down drill passes with correct data throughout (G-DB-124).
- [ ] Hit ratio and evictions are monitored (DB-249).
