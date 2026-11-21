# Example 2 — Deep OFFSET replaced by keyset pagination

## Before

The admin order list pages with `OFFSET`, so every deeper page re-scans and discards everything before it:

```sql
-- Page 500 of the orders list
SELECT id, customer_id, total_cents, status, created_at
FROM orders
ORDER BY created_at DESC
LIMIT 20 OFFSET 10000;
-- Scans and throws away 10,000 rows to return 20. Page 5,000 is ten times worse.
```

## After

The client passes the last seen sort key back as the cursor; the query seeks directly to it using the `(created_at, id)` index:

```sql
-- First page: pass NULL cursor. Later pages: pass the last row's (created_at, id).
SELECT id, customer_id, total_cents, status, created_at
FROM orders
WHERE ($1::timestamptz IS NULL)
   OR (created_at, id) < ($1::timestamptz, $2::bigint)
ORDER BY created_at DESC, id DESC
LIMIT 20;
-- Backed by: CREATE INDEX idx_orders_created_id ON orders (created_at DESC, id DESC);
-- Cost is constant per page regardless of depth.
```

**Corrects DB-144** — pagination over large lists is keyset-based on a stable sort key; deep `OFFSET` is a defect.
