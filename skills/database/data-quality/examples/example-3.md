# Example 3 — A money path reconciled by a business-rule check

## Before

The orders model passes every structural test — keys unique, columns
not-null, values in range — while a transformation bug drops one line item
from roughly 4% of orders. The stored order totals no longer equal the sum
of their items, but no check compares them, because every test asks "is this
column well-formed?" and none asks "is this money right?". Finance finds
the discrepancy at quarter-end.

## After

The money path carries an arithmetic business-rule check, written as a
singular dbt test that returns the offending rows — any row returned is a
failure:

```sql
-- tests/assert_order_totals_match_items.sql
-- Fails (returns rows) when an order's stored total disagrees with
-- the sum of its line items. Tolerance: zero.
SELECT
  o.order_id,
  o.total_cents,
  COALESCE(SUM(i.line_total_cents), 0) AS items_total_cents
FROM {{ ref('orders') }} AS o
LEFT JOIN {{ ref('order_items') }} AS i
  ON i.order_id = o.order_id
GROUP BY o.order_id, o.total_cents
HAVING o.total_cents <> COALESCE(SUM(i.line_total_cents), 0)
```

The check runs in `dbt build` with the rest of the suite, in CI and at the
pipeline's layer boundary, and a single mismatched order fails the run and
alerts the dataset's owner (DB-390). Structural tests prove the data is
shaped correctly; this check proves it is *right*.

Note: corrects DB-385 — every money path carries a business-rule check tying totals to their components, in addition to structural tests.
