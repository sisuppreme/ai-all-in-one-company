# Example 3 — Swallowed write failure replaced by a typed error

## Before

A status update fails against a constraint, the error is caught and discarded, and the caller reports success:

```sql
-- Application pseudocode around the write:
BEGIN;
UPDATE orders SET status = 'refunded' WHERE id = 9917;
-- (constraint violation raised by the database)
COMMIT;  -- never reached, but the catch block swallows the error,
         -- returns "ok", and the UI shows the order as refunded.
```

## After

The write either commits and returns the persisted row, or the transaction aborts and the failure surfaces as a typed error the caller must handle:

```sql
BEGIN;
UPDATE orders
SET status = 'refunded'
WHERE id = 9917
RETURNING id, status, updated_at;
-- If the constraint rejects the value, the transaction aborts;
-- no COMMIT is issued, no success is reported, and the caller
-- receives a typed ConstraintViolation error naming the check.
COMMIT;
```

**Corrects DB-186** — writes return the persisted entity or raise an explicit error; a silent no-op write is forbidden.
