# Example 2 — A reversible migration pair

## Before

```sql
-- Up only. There is no down: rollback means improvising SQL during an incident.
ALTER TABLE orders ADD COLUMN discount_cents integer;
```

## After

```sql
-- Up:
ALTER TABLE orders ADD COLUMN discount_cents integer NOT NULL DEFAULT 0;

-- Down (tested in CI by gate G-DB-061: apply all, roll back one, re-apply):
ALTER TABLE orders DROP COLUMN discount_cents;

-- If a migration genuinely cannot reverse (e.g. a one-way data transform),
-- its header says so and names the recovery instead:
--   IRREVERSIBLE: merges duplicate accounts. Recovery: restore the
--   pre-migration snapshot `accounts_premerge_2026_11` and replay orders
--   created after it (runbook RB-14).
```

Corrects DB-123 (every migration is reversible, or explicitly marked irreversible with a named recovery procedure).
