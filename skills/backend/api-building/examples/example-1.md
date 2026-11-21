# Example 1 — Idempotency key on order creation

## Before

```ts
app.post("/orders", async (req, res) => {
  const order = await db.orders.create({
    userId: req.user.id,
    totalCents: req.body.totalCents, // trusted from the client
    items: req.body.items,
  });
  res.status(201).json({ id: order.id, totalCents: order.totalCents });
});
```

Two defects: the total is whatever the client claims it is, and a retried or
double-clicked submit creates a second order — the customer is charged twice
for one checkout.

## After

```ts
app.post("/orders", async (req, res) => {
  const key = req.header("Idempotency-Key");
  if (!key) {
    return res.status(400).json(problem(400, "Idempotency-Key header is required"));
  }

  const bodyHash = sha256(canonicalJson(req.body));
  const prior = await db.idempotencyKeys.findByKey(key);
  if (prior) {
    if (prior.bodyHash !== bodyHash) {
      return res.status(422).json(
        problem(422, "Idempotency-Key was already used with a different request body"),
      );
    }
    return res.status(prior.status).json(prior.response); // replay, no new effect
  }

  const order = await db.transaction(async (tx) => {
    const items = await tx.items.findMany({ where: { id: { in: req.body.itemIds } } });
    const totalCents = items.reduce((sum, i) => sum + i.priceCents, 0); // server-computed
    const created = await tx.orders.create({
      data: { userId: req.user.id, totalCents },
    });
    await tx.idempotencyKeys.create({
      data: { key, bodyHash, status: 201, response: { id: created.id, totalCents } },
    });
    return created;
  });

  res.status(201).json({ id: order.id, totalCents: order.totalCents });
});
```

The key, the request hash, and the first response are stored in the same
transaction as the order, so a retry replays the stored response instead of
repeating the effect, and the total is computed from stored prices, never
from the request.

Note: corrects BE-005 — non-replayable writes store key + request hash + first response and replay on retry; and BE-003 — trusted values are recomputed server-side.
