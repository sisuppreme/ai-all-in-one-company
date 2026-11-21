# Example 3 — Check-then-act race made atomic

## Before

```ts
app.post("/orders/:id/fulfill", async (req, res) => {
  const item = await db.items.findById(req.body.itemId);
  if (item.stock < 1) {
    return res.status(409).json(problem(409, "Out of stock"));
  }
  await db.items.update(item.id, { stock: item.stock - 1 });
  await db.orders.markFulfilled(req.params.id);
  res.status(200).json({ ok: true });
});
```

Two concurrent requests both read `stock = 1`, both pass the check, and both
decrement — the last unit is sold twice. The logic is sequentially correct
and concurrently wrong.

## After

```ts
app.post("/orders/:id/fulfill", async (req, res) => {
  const result = await db.transaction(async (tx) => {
    // Atomic conditional decrement: the database arbitrates the race.
    const decremented = await tx.items.decrementStockIfAvailable(req.body.itemId);
    if (decremented === 0) return { ok: false as const };
    await tx.orders.markFulfilled(req.params.id);
    return { ok: true as const };
  });

  if (!result.ok) {
    return res.status(409).json(problem(409, "Out of stock"));
  }
  res.status(200).json({ ok: true });
});
```

where the decrement is a single statement:

```sql
UPDATE items SET stock = stock - 1 WHERE id = $1 AND stock > 0;
-- affected rows: 1 = reserved, 0 = out of stock
```

The check and the write are now one atomic operation inside one transaction,
so exactly one of two racing requests can win the last unit.

Note: corrects BE-004 — check-then-act sequences run inside a transaction or behind an atomic update/constraint; the database arbitrates races, not application hope.
