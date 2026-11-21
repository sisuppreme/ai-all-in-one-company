# Example 2 — Transaction-local tenant context

## Before

```sql
-- Session-level SET on a pooled connection: the context outlives the request.
-- The next request that reuses this connection silently runs as tenant 5.
SET app.tenant_id = '00000000-0000-0000-0000-000000000005';
SELECT * FROM invoices;
```

## After

```sql
-- Context lives and dies with the transaction (the `true` makes it LOCAL),
-- so a pooled connection can never carry it into another tenant's request.
BEGIN;
SELECT set_config('app.tenant_id', '00000000-0000-0000-0000-000000000005', true);
SELECT * FROM invoices;   -- RLS sees tenant 5 for this transaction only
COMMIT;                   -- context is gone; the connection returns to the pool clean
```

Corrects DB-105 (tenant context is set per transaction, never at session level under a connection pool).
