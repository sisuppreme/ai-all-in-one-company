# Example 2 — A partial load made atomic with staging and swap

## Before

The transform writes directly into the table dashboards read:

```sql
DELETE FROM modeled_daily_sales WHERE sales_date = DATE '2026-11-20';

INSERT INTO modeled_daily_sales
SELECT ... -- ~1M rows, several minutes
FROM cleaned_orders
WHERE order_date = DATE '2026-11-20';
```

The job dies halfway through the insert. The delete has already committed,
so `modeled_daily_sales` now holds a partial day — and the dashboard reading
it at that moment shows revenue down 60% and triggers a panic that the data,
not the business, caused.

## After

The transform builds the new partition in a staging table and swaps it in
inside one transaction. Readers see the old complete day or the new complete
day, never a fraction of either:

```sql
BEGIN;

CREATE TABLE modeled_daily_sales_stage (LIKE modeled_daily_sales);

INSERT INTO modeled_daily_sales_stage
SELECT ...
FROM cleaned_orders
WHERE order_date = DATE '2026-11-20';

DELETE FROM modeled_daily_sales WHERE sales_date = DATE '2026-11-20';
INSERT INTO modeled_daily_sales SELECT * FROM modeled_daily_sales_stage;

DROP TABLE modeled_daily_sales_stage;

COMMIT;
```

If the job dies before `COMMIT`, nothing was published and the retry starts
clean. The failure-injection gate (G-DB-161) kills the transform mid-run in
staging and asserts exactly this: no partial output visible, retry completes
the full window.

Note: corrects DB-324 — a failed transformation publishes nothing; output appears atomically or not at all.
