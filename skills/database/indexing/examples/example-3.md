# Example 3 — Fossil index found by audit and dropped by migration

## Before

The per-release audit is skipped, so `idx_orders_legacy_ref` — created for a retired import flow — stays in place for a year, taxing every insert and never serving a read:

```sql
-- pg_stat_user_indexes shows idx_scan = 0 for idx_orders_legacy_ref
-- across the full audit window, but nobody looks, and the index stays.
```

## After

The audit query runs per release; the zero-scan index is dropped through a normal, reversible migration and the disposition is recorded:

```sql
-- Audit (run per release):
SELECT relname, indexrelname, idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0
ORDER BY relname;

-- Migration (up):
DROP INDEX CONCURRENTLY idx_orders_legacy_ref;
-- Migration (down, if the retired flow ever returns):
-- CREATE INDEX CONCURRENTLY idx_orders_legacy_ref ON orders (legacy_ref);
```

**Corrects DB-167** — index usage is audited on a schedule; unused indexes are dropped through a migration, not kept by inertia.
