# Example 1 — Composite index reordered so the query can use it

## Before

Every tenant query filters `tenant_id` first, but the composite index leads with `created_at`, so the planner cannot use it for the tenant filter:

```sql
CREATE INDEX idx_orders_created_tenant ON orders (created_at, tenant_id);

SELECT id, total_cents, status
FROM orders
WHERE tenant_id = 7 AND created_at >= now() - interval '30 days'
ORDER BY created_at DESC;

-- EXPLAIN: Seq Scan on orders — the index's leftmost column (created_at)
-- is not the equality column, so this query gets no index scan.
```

## After

Equality columns lead, the range column comes last, and the plan proves the index is used:

```sql
DROP INDEX idx_orders_created_tenant;
CREATE INDEX idx_orders_tenant_created ON orders (tenant_id, created_at DESC);

SELECT id, total_cents, status
FROM orders
WHERE tenant_id = 7 AND created_at >= now() - interval '30 days'
ORDER BY created_at DESC;

-- EXPLAIN: Index Scan using idx_orders_tenant_created on orders
--   Index Cond: ((tenant_id = 7) AND (created_at >= now() - interval '30 days'))
```

**Corrects DB-163** — composite column order follows the queries: equality first, range last.
