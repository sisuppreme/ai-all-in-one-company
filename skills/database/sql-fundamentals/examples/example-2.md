# Example 2 — Killing an N+1

## Before

```sql
-- 1 query for the orders, then 1 query per order for its customer: 51 queries for 50 rows.
SELECT id, customer_id, total_cents FROM orders ORDER BY created_at DESC LIMIT 50;
SELECT id, name FROM customers WHERE id = 7;
SELECT id, name FROM customers WHERE id = 12;
-- ... repeated once per order
```

## After

```sql
-- One query, regardless of row count:
SELECT o.id, o.total_cents, c.name AS customer_name
FROM orders AS o
JOIN customers AS c ON c.id = o.customer_id
ORDER BY o.created_at DESC
LIMIT 50;
```

Corrects DB-025 (collection loads are eager or batched; a query per row is a defect — the query-count gate G-DB-012 asserts this count stays flat as fixtures grow).
