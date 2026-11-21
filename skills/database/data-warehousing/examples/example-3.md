# Example 3 — A load that duplicated on re-run, made idempotent

## Before

The daily warehouse load appends whatever the extract produced:

```sql
INSERT INTO fct_orders
SELECT * FROM stg_orders_extract
WHERE order_date = DATE '2026-11-20';
```

The load times out halfway, the operator re-runs it, and the extract is
appended a second time. Yesterday's order count doubles in the warehouse,
the reconciliation check fails, and nobody can tell which rows are the
duplicates because they are identical.

## After

The load merges by key, so any number of re-runs converge to the same state:

```sql
MERGE INTO fct_orders AS t
USING (
  SELECT * FROM stg_orders_extract
  WHERE order_date = DATE '2026-11-20'
) AS s
ON t.order_id = s.order_id
WHEN MATCHED THEN
  UPDATE SET status        = s.status,
             total_cents   = s.total_cents,
             refunded_cents = s.refunded_cents
WHEN NOT MATCHED THEN
  INSERT (order_id, order_date, status, total_cents, refunded_cents)
  VALUES (s.order_id, s.order_date, s.status, s.total_cents, s.refunded_cents);
```

The idempotency gate (G-DB-153) runs one day's load twice in staging and
asserts identical row counts and checksums after both runs. A timed-out load
is now boring: re-run it, and the warehouse ends in the same state as a
single clean run.

Note: corrects DB-303 — warehouse loads are idempotent; re-running a day's load produces the same warehouse state.
