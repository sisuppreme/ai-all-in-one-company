# Example 2 — Controller SQL replaced by a paginated repository method

## Before

A reporting handler runs its own unbounded SQL inline, outside any data-access layer, and returns every matching row:

```sql
-- Inline in the HTTP handler, tenant filter remembered by hand (this time):
SELECT id, customer_id, total_cents, status, created_at
FROM orders
WHERE tenant_id = 7
ORDER BY created_at DESC;
-- No LIMIT: the full order history loads into memory on every request,
-- and the next handler that copies this forgets the tenant filter.
```

## After

The handler calls one repository method; the layer applies tenant scope from the session context and enforces the pagination ceiling:

```sql
-- Inside the data-access layer only. Tenant scope is applied by the layer
-- from the transaction's tenant context, never passed in by the caller.
-- Caller supplies: page size (capped at 100 by the layer) and a keyset cursor.
SELECT id, customer_id, total_cents, status, created_at
FROM orders
WHERE ($1::timestamptz IS NULL)
   OR (created_at, id) < ($1::timestamptz, $2::bigint)
ORDER BY created_at DESC, id DESC
LIMIT $3;  -- $3 is clamped by the layer to at most 100
```

**Corrects DB-181, DB-184** — all access goes through the one layer, and every list method is paginated with a hard maximum page size.
