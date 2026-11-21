# Example 1 — An idempotent reference seed

## Before

```sql
-- Plain INSERTs: every run adds another copy of every row.
INSERT INTO plans (code, name, price_cents) VALUES ('pro', 'Pro', 2000);
INSERT INTO roles (code, name) VALUES ('admin', 'Administrator');
-- Run it twice (CI does, before every test batch) and "Pro" exists five times.
```

## After

```sql
-- Upsert by natural key: the second run updates in place and changes no counts.
INSERT INTO plans (code, name, price_cents) VALUES ('pro', 'Pro', 2000)
ON CONFLICT (code) DO UPDATE SET name = EXCLUDED.name, price_cents = EXCLUDED.price_cents;

INSERT INTO roles (code, name) VALUES ('admin', 'Administrator')
ON CONFLICT (code) DO NOTHING;
```

Corrects DB-062 (seed scripts are idempotent — the double-run gate G-DB-031 asserts identical row counts after two runs).
