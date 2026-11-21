# Example 2 — Empty catch around a payment replaced by typed translation

## Before

```js
// The charge throws, the catch swallows it, and the handler reports
// success for an order that was never paid.
app.post("/api/orders", requireAuth, async (req, res) => {
  const order = await db.orders.create(req.body);
  try {
    await payments.charge(order.id, order.total);
  } catch {
    console.log("charge failed, continuing");
  }
  res.status(201).json({ orderId: order.id, status: "placed" });
});
```

## After

```js
// The provider failure is translated into a typed error and the
// global handler answers honestly: the order exists as unpaid,
// the client gets a classified problem, and nothing claims success.
app.post("/api/orders", requireAuth, async (req, res, next) => {
  const order = await db.orders.create({ ...req.body, paymentStatus: "pending" });
  try {
    await payments.charge(order.id, order.total);
  } catch (err) {
    await db.orders.update(order.id, { paymentStatus: "failed" });
    return next(new DependencyError("payments"));
  }
  await db.orders.update(order.id, { paymentStatus: "paid" });
  res.status(201).json({ orderId: order.id, status: "placed" });
});
```

Note: the slop version swallowed the charge failure and reported a placed order; the corrected version translates the failure, records the true state, and lets the one error handler respond — BE-283, BE-287.
