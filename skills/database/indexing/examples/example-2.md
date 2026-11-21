# Example 2 — Covering index with INCLUDE reaching an index-only scan

## Before

The account-summary query uses the `(account_id)` index but still fetches the heap for every row to read `status` and `balance_cents`:

```sql
CREATE INDEX idx_entries_account ON ledger_entries (account_id);

SELECT status, balance_cents
FROM ledger_entries
WHERE account_id = 2201 AND kind = 'posted';

-- EXPLAIN: Index Scan using idx_entries_account
--   -> Heap Fetches: 4,812  (every matching row costs a heap visit)
```

## After

The filter column joins the key and the returned columns ride along via `INCLUDE`, so the planner answers from the index alone:

```sql
DROP INDEX idx_entries_account;
CREATE INDEX idx_entries_account_kind
    ON ledger_entries (account_id, kind)
    INCLUDE (status, balance_cents);

SELECT status, balance_cents
FROM ledger_entries
WHERE account_id = 2201 AND kind = 'posted';

-- EXPLAIN: Index Only Scan using idx_entries_account_kind
--   Heap Fetches: 0
```

**Corrects DB-164** — hot read paths get covering indexes so the planner can answer with an index-only scan.
