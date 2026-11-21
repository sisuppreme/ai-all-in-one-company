# Example 1 — An append load that duplicated on retry, replaced with a merge

## Before

The transform loads the cleaned window by appending:

```sql
INSERT INTO cleaned_orders
SELECT order_id, customer_id, total_cents, updated_at
FROM raw_orders
WHERE updated_at >= TIMESTAMP '2026-11-20 00:00:00'
  AND updated_at <  TIMESTAMP '2026-11-21 00:00:00';
```

The run is killed by a deploy at 90% and the orchestrator retries it — as it
should. The retry appends the same window again. Every order in the window
now exists twice, and downstream sums double.

## After

The load merges on the natural key; a retry converges instead of duplicating:

```sql
MERGE INTO cleaned_orders AS t
USING (
  SELECT order_id, customer_id, total_cents, updated_at
  FROM raw_orders
  WHERE updated_at >= :window_start
    AND updated_at <  :window_end
) AS s
ON t.order_id = s.order_id
WHEN MATCHED THEN
  UPDATE SET customer_id = s.customer_id,
             total_cents = s.total_cents,
             updated_at  = s.updated_at
WHEN NOT MATCHED THEN
  INSERT (order_id, customer_id, total_cents, updated_at)
  VALUES (s.order_id, s.customer_id, s.total_cents, s.updated_at);
```

The idempotency gate (G-DB-162) runs the same window twice and asserts
identical destination row counts and checksums — the retry that used to
corrupt the layer is now the normal, tested path.

Note: corrects DB-323 — loads merge or replace by key, so retries and backfills converge instead of duplicating.
