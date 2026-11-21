# Example 3 — Same-release column drop split into expand-and-contract

Demonstrates: DO-047 (database changes expand and contract).

## Before

One release renames `users.full_name` to `users.display_name`: the migration renames the column and the new code reads the new name. During the rolling deploy, old instances still serving traffic read `full_name`, which no longer exists — every request they handle errors until the rollout finishes, and rolling back the code cannot restore the column.

## After

Release 1 (expand): migration adds `display_name`, backfills it from `full_name`, and the new code writes both columns and reads `display_name` with a `full_name` fallback — old and new code both run correctly against this shape. Release 2, after no old code remains: reads switch fully to `display_name`. Release 3 (contract): the migration drops `full_name`. A rollback at any point returns to code that works against the current schema.
