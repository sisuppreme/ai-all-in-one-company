# Example 1 — The atomic conditional update

## Before

```sql
-- Check-then-act in application code: two concurrent withdrawals both read 100,
-- both pass the ">= 80" check, and the account ends at -60.
SELECT balance_cents FROM accounts WHERE id = 42;          -- app reads 100
-- app decides: 100 >= 80, proceed
UPDATE accounts SET balance_cents = 100 - 80 WHERE id = 42;
```

## After

```sql
-- One atomic statement: the condition is evaluated against the row as it is
-- locked and updated. The second concurrent attempt matches no row and is
-- rejected by the caller checking the affected-row count.
UPDATE accounts
SET balance_cents = balance_cents - 8000
WHERE id = 42 AND balance_cents >= 8000;
-- Rows affected: 1 = withdrawal applied; 0 = insufficient funds, reject cleanly.
```

Corrects DB-082 (money movement runs with a lock, a version check, or an atomic conditional update — never a bare read-modify-write).
