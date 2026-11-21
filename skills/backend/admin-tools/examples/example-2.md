# Example 2 — A dashboard metric computed from records

## Before

The dashboard's headline number is a constant chosen to look plausible:

```js
// dashboard component
const revenueThisMonth = 48200; // rendered as "Revenue this month: $48,200"
```

Real orders never move it. Leadership reads fiction with a dollar sign.

## After

The metric is a query over live records, computed at view time, with an
honest state when the data cannot be read:

```js
app.get('/admin/metrics/revenue', requireStaffRole('viewer'), async (req, res) => {
  const startOfMonth = new Date();
  startOfMonth.setDate(1); startOfMonth.setHours(0, 0, 0, 0);

  try {
    const { total } = await db.orders
      .where({ status: 'paid' })
      .andWhere('created_at', '>=', startOfMonth)
      .sum({ total: 'amount' })
      .first();
    res.json({ metric: 'revenue_this_month', value: total ?? 0, computedAt: new Date() });
  } catch {
    // an honest "unavailable" beats an invented number
    res.status(503).json({ metric: 'revenue_this_month', value: null, state: 'unavailable' });
  }
});
```

Create or refund an order and the figure moves by exactly that amount on
the next view — the data-change test passes.

Note: corrects BE-163 — dashboard figures are computed from current records, never rendered from fixtures.
