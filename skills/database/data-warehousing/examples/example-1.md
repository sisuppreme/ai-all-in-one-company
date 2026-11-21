# Example 1 — A dashboard moved off the production primary

## Before

The revenue dashboard's data source is the production database itself:

```text
host=prod-primary.internal  dbname=app  user=dashboard_ro
```

Its main widget runs an unbounded aggregation over the orders table:

```sql
SELECT date_trunc('day', created_at) AS day,
       sum(total_cents)            AS revenue
FROM orders
GROUP BY 1
ORDER BY 1;
```

Every dashboard refresh — and every Monday-morning page load by the whole
leadership team — runs full scans against the same primary that serves
checkout. During the 09:00 peak, checkout latency triples while the report
renders.

## After

A scheduled pipeline load (etl-pipelines) maintains a modeled orders fact
table in the warehouse, and the dashboard points there:

```text
dataset=analytics  table=fct_orders   -- warehouse, not the primary
```

```sql
-- Runs in the warehouse, against the modeled fact table
SELECT order_date AS day,
       sum(total_cents) AS revenue
FROM fct_orders
GROUP BY 1
ORDER BY 1;
```

The primary's query log is checked on schedule (G-DB-151): zero connections
from the dashboard service account. Reporting load now scales with the
warehouse's storage/compute separation, and checkout never competes with a
chart.

Note: corrects DB-301 — no dashboard or report queries the production primary; analytical reads run against the warehouse.
