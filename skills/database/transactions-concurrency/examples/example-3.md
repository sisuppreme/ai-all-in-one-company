# Example 3 — An idempotent retried write

## Before

```sql
-- A worker charges a card and records it; on timeout it retries the whole
-- operation, and the customer ends up charged twice with two ledger rows.
INSERT INTO payments (account_id, amount_cents, status)
VALUES (42, 2000, 'captured');
```

## After

```sql
-- The caller supplies an idempotency key; the unique constraint makes the
-- effect and the key atomic in the same transaction. A retry finds the
-- existing row and returns its result instead of charging again.
ALTER TABLE payments ADD COLUMN idempotency_key varchar(80);
CREATE UNIQUE INDEX payments_idempotency_key_idx ON payments (idempotency_key);

INSERT INTO payments (account_id, amount_cents, status, idempotency_key)
VALUES (42, 2000, 'captured', 'checkout-9f27-attempt')
ON CONFLICT (idempotency_key) DO NOTHING;
-- Rows affected: 0 on a retry = already applied; select and return that payment.
```

Corrects DB-084 (retried operations are idempotent — a retry never double-applies).
