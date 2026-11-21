# Example 3 — Aggregating in SQL with explicit NULL handling

## Before

```sql
-- The application fetches every order, then loops in memory:
SELECT id, total_cents, discount_cents FROM orders WHERE status = 'paid';
-- app code: sum(total_cents - discount_cents)   -- crashes/misbehaves when discount_cents is NULL
```

## After

```sql
-- The database aggregates; NULL discounts are handled explicitly with COALESCE:
SELECT date_trunc('day', created_at) AS day,
       count(*) AS paid_orders,
       sum(total_cents - COALESCE(discount_cents, 0)) AS net_cents
FROM orders
WHERE status = 'paid'
GROUP BY day
ORDER BY day;
```

Corrects DB-026 (aggregation happens in the database, not in application memory) and DB-027 (NULL semantics are handled explicitly).
