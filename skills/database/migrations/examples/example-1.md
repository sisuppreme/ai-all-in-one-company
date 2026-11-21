# Example 1 — Expand-and-contract column rename

## Before

```sql
-- One deploy renames the column AND ships code that only reads the new name.
-- During the rolling deploy, old instances crash on the missing column.
ALTER TABLE users RENAME COLUMN full_name TO display_name;
```

## After

```sql
-- Deploy 1 (expand): add the new column; the app dual-writes both and reads the old.
ALTER TABLE users ADD COLUMN display_name varchar(200);
-- Backfill job (separate, resumable — DB-125):
UPDATE users SET display_name = full_name WHERE display_name IS NULL AND id BETWEEN $1 AND $2;

-- Deploy 2: the app reads display_name only; full_name is no longer written.

-- Deploy 3 (contract): drop the old shape.
ALTER TABLE users DROP COLUMN full_name;
```

Corrects DB-124 (risky changes follow expand-and-contract across deploys; no deploy both changes the shape and depends on it).
