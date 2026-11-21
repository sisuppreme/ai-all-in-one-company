# Example 3 — A refund as a two-step, audited action

## Before

One click, one direct table update, no record of who did it or why:

```js
app.post('/admin/orders/:id/refund', requireStaffRole('support'), async (req, res) => {
  await db.orders.update(req.params.id, { status: 'refunded' }); // money never moves
  res.status(204).end();
});
```

The order says "refunded"; the provider was never told, the customer was
never repaid, and no one can reconstruct the event.

## After

Prepare shows the exact effect; confirm executes it through the payments
service, re-authenticates the operator, and writes the audit record:

```js
// step 1 — prepare: state what will happen, change nothing
app.get('/admin/orders/:id/refund/preview', requireStaffRole('support'), async (req, res) => {
  const order = await orders.getById(req.params.id);
  res.json({
    orderId: order.id,
    effect: `Refund ${order.amount} to card ${order.cardBrand} •••• ${order.cardLast4}`,
    reversible: 'Provider refund; a compensating charge requires a new payment.',
  });
});

// step 2 — confirm: re-authenticate, execute via the service, audit
app.post('/admin/orders/:id/refund', requireStaffRole('support'), reauthenticate, async (req, res) => {
  const before = await orders.getById(req.params.id);
  const refund = await payments.refundOrder(before.id, { reason: req.body.reason }); // provider call, real money path
  const after = await orders.getById(before.id);

  await audit.record({
    actor: req.staff.id, action: 'order.refund',
    target: before.id, providerRefundId: refund.id,
    before: { status: before.status }, after: { status: after.status },
    at: new Date(),
  });
  res.json({ refundId: refund.id, status: after.status });
});
```

The refund exists at the provider, the order agrees, and the audit record
names the human who did it.

Note: corrects BE-166 — destructive actions are prepared, confirmed with their effect stated, then executed and audited.
