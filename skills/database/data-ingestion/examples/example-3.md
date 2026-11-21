# Example 3 — A redelivered batch deduplicated by source key

## Before

A webhook-driven extract is delivered twice after a network retry. The
loader checks before inserting:

```sql
-- step 1: check
SELECT 1 FROM raw_orders WHERE source_order_id = :id;

-- step 2: insert if the check found nothing
INSERT INTO raw_orders (source_order_id, total_cents, currency)
VALUES (:id, :total_cents, :currency);
```

Both deliveries run concurrently. Both checks find nothing, both insert,
and the order now exists twice. The race is rare enough to survive code
review and common enough to corrupt every month-end close.

## After

Deduplication is a property of the table, not of timing: a unique constraint
on the source primary key, and an idempotent merge at load:

```sql
ALTER TABLE raw_orders
  ADD CONSTRAINT raw_orders_source_pk UNIQUE (source_order_id);

MERGE INTO raw_orders AS t
USING (SELECT :id AS source_order_id, :total_cents AS total_cents,
              :currency AS currency) AS s
ON t.source_order_id = s.source_order_id
WHEN MATCHED THEN
  UPDATE SET total_cents = s.total_cents, currency = s.currency
WHEN NOT MATCHED THEN
  INSERT (source_order_id, total_cents, currency)
  VALUES (s.source_order_id, s.total_cents, s.currency);
```

Concurrent duplicate deliveries now serialize on the constraint: one
inserts, the other updates the same row. The replay gate (G-DB-172)
delivers the same batch twice and asserts destination counts are unchanged.

Note: corrects DB-344 — re-delivered data is deduplicated by source primary key at load, enforced by the database, not by a check-then-insert race.
