# Example 2 — Optimistic locking with a version column

## Before

```sql
-- Last write wins: two editors load the same document; the second save
-- silently overwrites the first, and nobody is told anything was lost.
UPDATE documents SET body = 'editor B text' WHERE id = 9;
```

## After

```sql
ALTER TABLE documents ADD COLUMN version integer NOT NULL DEFAULT 0;

-- Each editor saves against the version it loaded (here, 3).
-- Exactly one of two concurrent saves can match; the other affects 0 rows
-- and the application reports a conflict instead of losing work.
UPDATE documents
SET body = 'editor B text', version = version + 1
WHERE id = 9 AND version = 3;
-- Rows affected: 0 = someone else saved first; reload and merge.
```

Corrects DB-083 (isolation and contention handling are chosen deliberately — here optimistic locking for a low-contention edit path).
