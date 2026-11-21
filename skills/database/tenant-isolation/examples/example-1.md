# Example 1 — A tenant table with a complete policy

## Before

```sql
-- No tenant column, no RLS: isolation is a promise in application code.
CREATE TABLE invoices (
  id         bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  amount_cents integer NOT NULL
);
```

## After

```sql
CREATE TABLE invoices (
  id           bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  tenant_id    uuid NOT NULL,
  amount_cents integer NOT NULL CHECK (amount_cents >= 0)
);

CREATE INDEX invoices_tenant_id_idx ON invoices (tenant_id);

ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;
ALTER TABLE invoices FORCE ROW LEVEL SECURITY;

-- USING restricts reads; WITH CHECK restricts writes to the caller's own tenant.
CREATE POLICY invoices_tenant_isolation ON invoices
  USING (tenant_id = current_setting('app.tenant_id')::uuid)
  WITH CHECK (tenant_id = current_setting('app.tenant_id')::uuid);
```

Corrects DB-102 (every tenant-owned table carries a non-null, indexed tenant_id) and DB-103 (RLS is enabled, forced, and covers writes with WITH CHECK).
