# Example 2 — Two revenues reconciled to one definition

## Before

Two dashboards answer "what was revenue last month?" with two definitions.

Sales dashboard:

```sql
SELECT sum(total_cents) FROM orders
WHERE status = 'paid';            -- refunds never subtracted
```

Finance dashboard:

```sql
SELECT sum(total_cents) FROM orders
WHERE status IN ('paid', 'refunded')
  AND refunded_cents = 0;         -- partially refunded orders vanish
```

Both queries are plausible, both are wrong in different ways, and the two
figures disagree in the same meeting. There is no fact of the matter, because
"revenue" is defined wherever it is used.

## After

Revenue is defined once, in one named warehouse model that every consumer
references:

```sql
-- models/marts/fct_revenue.sql  (the single definition of revenue)
SELECT
  order_id,
  order_date,
  total_cents,
  refunded_cents,
  total_cents - refunded_cents AS net_revenue_cents
FROM warehouse.stg_orders
WHERE status IN ('paid', 'partially_refunded', 'refunded');
```

Both dashboards now select `sum(net_revenue_cents)` from `fct_revenue` and
nothing else. Changing the definition means changing this one model,
recording the change and its effective date (DB-308), and re-checking the
consumers — never editing a dashboard's private SQL.

Note: corrects DB-302 — every headline metric has exactly one definition, in one named model, referenced by all consumers.
