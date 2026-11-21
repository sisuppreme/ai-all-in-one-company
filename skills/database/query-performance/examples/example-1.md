# Example 1 — Sequential scan to index scan, with evidence

## Before

The orders-by-customer lookup is "optimized" by rewriting it in the ORM and merging without any plan. In production it scans the whole table:

```sql
-- Query as shipped (no evidence captured)
SELECT id, total_cents, status, created_at
FROM orders
WHERE customer_id = 4815
ORDER BY created_at DESC
LIMIT 20;

-- EXPLAIN (ANALYZE, BUFFERS) on production-shaped data (2,400,000 rows):
-- Limit  (cost=0.00..51234.55 rows=20) (actual time=812.441..812.512 rows=20)
--   ->  Sort  (actual time=812.438..812.490 rows=20)
--         ->  Seq Scan on orders  (actual time=0.041..790.204 rows=1830)
--               Filter: (customer_id = 4815)
-- Planning Time: 0.412 ms / Execution Time: 812.601 ms
```

## After

The missing index is added by migration, and the before/after plans are attached to the change:

```sql
CREATE INDEX CONCURRENTLY idx_orders_customer_created
    ON orders (customer_id, created_at DESC);

-- EXPLAIN (ANALYZE, BUFFERS) after, same data:
-- Limit  (cost=0.43..31.90 rows=20) (actual time=0.052..0.118 rows=20)
--   ->  Index Scan using idx_orders_customer_created on orders
--         Index Cond: (customer_id = 4815)
-- Planning Time: 0.210 ms / Execution Time: 0.131 ms
```

Execution time drops from 812.6 ms to 0.13 ms, and the plan — not the author's claim — is the evidence in the change record.

**Corrects DB-142** — no optimization ships without before/after `EXPLAIN (ANALYZE, BUFFERS)` on production-shaped data.
