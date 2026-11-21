# Example 2 — Expand-and-contract instead of a destructive migration

## Before

Release 1.4 renames `users.full_name` to `users.display_name`. The single migration runs `ALTER TABLE users RENAME COLUMN full_name TO display_name;` and the new code reads only the new column. The release misbehaves and the team rolls back to 1.3 — which reads `full_name`, a column that no longer exists. The rollback turns a bad release into a full outage.

## After

Release 1.4 expands: the migration adds `display_name`, backfills it from `full_name`, and the new code dual-writes both columns while reading the new one. Rolling back to 1.3 works because `full_name` is still there and current. Release 1.5, once 1.3 is no longer a rollback target, contracts: reads/writes move fully to `display_name` and `full_name` is dropped.

Note: demonstrates DO-305 — migrations expand and contract across releases so the old code runs against the new schema during the rollback window.
