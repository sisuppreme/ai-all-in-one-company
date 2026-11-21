# Example 3 — Building an index without locking the table

## Before

```sql
-- A plain CREATE INDEX inside the migration transaction takes a lock that
-- blocks writes on a 40-million-row table for the whole build.
BEGIN;
CREATE INDEX orders_user_id_idx ON orders (user_id);
COMMIT;
```

## After

```sql
-- Built concurrently, outside a transaction block: reads and writes continue
-- during the build. (In migration frameworks this is the
-- `algorithm: :concurrently` / disable_ddl_transaction! equivalent.)
CREATE INDEX CONCURRENTLY orders_user_id_idx ON orders (user_id);
```

Corrects DB-126 (indexes on large production tables are built concurrently, outside a transaction block where required).
