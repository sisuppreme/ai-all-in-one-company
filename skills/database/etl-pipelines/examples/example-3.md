# Example 3 — A hard-coded date replaced with a window parameter

## Before

The daily transform contains a literal date, edited by hand each time
someone needed a different day:

```sql
SELECT order_id, customer_id, total_cents
FROM raw_orders
WHERE updated_at >= TIMESTAMP '2026-11-20 00:00:00'
  AND updated_at <  TIMESTAMP '2026-11-21 00:00:00';
```

The pipeline fails over a three-day outage. Backfilling means editing this
SQL three times, in production, by hand — each edit a chance to type the
wrong date and silently process the wrong window twice.

## After

The window is a parameter the orchestrator supplies for every run — the
scheduled day, a retry, or any backfill range — and the transformation code
never changes:

```sql
SELECT order_id, customer_id, total_cents
FROM raw_orders
WHERE updated_at >= :window_start
  AND updated_at <  :window_end;
```

With Apache Airflow, the scheduled run passes the logical date range
(`{{ data_interval_start }}` / `{{ data_interval_end }}`) as those
parameters; a backfill is the same DAG invoked over the missed range. One
code path serves the schedule, the retry, and the recovery (DB-329).

Note: corrects DB-322 — every run is parameterized by window, so any single day can be re-run on demand.
