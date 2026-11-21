# Example 3 — Validate-all-then-write replaces a partial write

## Before

```ts
app.post("/orders", async (req, res) => {
  const order = await db.orders.create({ userId: req.user.id, items: req.body.items });
  const coupon = await db.coupons.findByCode(req.body.couponCode);
  if (!coupon || coupon.expired) {
    return res.status(422).json(problem(422, "Coupon is not valid"));
  }
  await db.orders.setCoupon(order.id, coupon.id);
  res.status(201).json(orderView(order));
});
```

The order is created first and validated later. The rejected request leaves
a real, unpaid order in the system — it appears in counts, dashboards, and
the customer's history, and fulfillment can act on it.

## After

```ts
app.post("/orders", async (req, res) => {
  // Phase 1: validate everything, write nothing.
  const parsed = orderSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(422).json(validationProblem(parsed.error));
  }
  let coupon = null;
  if (parsed.data.couponCode) {
    coupon = await db.coupons.findByCode(parsed.data.couponCode);
    if (!coupon || coupon.expired || coupon.usedBy(req.user.id)) {
      return res.status(422).json(problem(422, "Coupon is not valid"));
    }
  }

  // Phase 2: all checks passed — now write, in one transaction.
  const order = await db.transaction(async (tx) => {
    const created = await tx.orders.create({
      userId: req.user.id,
      items: parsed.data.items,
      couponId: coupon?.id ?? null,
    });
    if (coupon) await tx.coupons.markUsed(coupon.id, req.user.id);
    return created;
  });

  res.status(201).json(orderView(order));
});
```

Syntactic and semantic validation both complete before the first write, so
a rejection is total: no order, no coupon consumption, no side effects.

Note: corrects BE-047 — a failed validation returns 422 problem details and writes nothing; rejection leaves no partial state.
