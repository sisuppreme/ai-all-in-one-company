# D4 Example — A Checkout Endpoint That Trusted the Browser

## Scenario

D4 builds `POST /orders` for the SaaS's new team-plan checkout: validate
the request, recompute the price, decrement the seat pool, persist the
order, and return a contract-shaped response. D11 owns the payment-provider
integration; this endpoint is the server boundary in front of it.

## Before

```ts
app.post("/orders", async (req, res) => {
  try {
    const { items, total, role } = req.body;      // total and role from the client
    const pool = await db.seatPool.find();
    if (pool.remaining >= items.length) {          // check...
      await db.seatPool.update({ remaining: pool.remaining - items.length }); // ...then act
      ordersInMemory.push({ items, total, role }); // "persisted"
      res.json({ ok: true });
    } else {
      res.json({ ok: false, error: "Something went wrong" });
    }
  } catch (e) {
    res.status(500).json({ error: "Something went wrong", detail: e.stack });
  }
});
```

A double-click on the buy button creates two orders. A modified client can
send `total: 0` or `role: "admin"`. Two simultaneous checkouts both pass
the seat check and oversell the pool.

## What the skills caught

- **BAN-BE-003 — Client-supplied role or owner trusted** and **BE-003 —
  The server recomputes trusted values**: price and role are server facts,
  never request fields. Audit gate **G-BE-004**.
- **BAN-BE-022 — Mass assignment**: the whole body is destructured into
  the write. **BE-041 — Schema at the edge** and **BE-043 — Allowlist over
  denylist** require a contract schema that rejects unknown fields.
- **BAN-BE-004 — Check-then-act without a constraint**: the seat check and
  decrement are two steps with a race between them — **DET-CODE-030 —
  Race-prone check-then-act sequences**. **BE-004 — The database
  arbitrates races** and **BE-010 — Multi-record writes are atomic**.
- **BAN-BE-002 — Success response with no persisted effect**: the order
  lives in an in-memory array; a restart erases paid orders while the
  client was told `ok: true` — the server side of **DET-FAKE-015 — Forms
  that submit nowhere**. **BE-002 — Persistence is the definition of
  done**, verified by **G-BE-002**.
- No idempotency: **BE-005 — Idempotency keys on non-replayable writes**;
  the duplicate-submit test **G-BE-003** fails on the second click.
- **BAN-BE-143 — The leaking error**: a stack trace in the response, and
  one identical message for a sold-out pool and a crashed database —
  **DET-CODE-022 — Identical error messages for different failures**.
  **BE-282 — Problem details only**, **BE-284 — No internals out**.

## After

```ts
app.post("/orders", authenticate, async (req, res) => {
  const input = OrderCreate.parse(req.body);        // schema rejects unknown fields (BE-041)
  const idemKey = req.header("Idempotency-Key");    // required for this route (BE-005)
  const order = await db.transaction(async (tx) => {
    const existing = await tx.orders.findByIdempotencyKey(idemKey);
    if (existing) return existing;                  // replay returns the first result
    const total = priceOrder(input.items);          // recomputed server-side (BE-003)
    const pool = await tx.seatPool.decrementIfAvailable(input.seats); // atomic, DB-arbitrated
    if (!pool) throw new ProblemError(409, "seat-pool-exhausted");
    return tx.orders.create({ items: input.items, total, ownerId: req.user.id,
                              status: "pending_payment", idempotencyKey: idemKey });
  });
  res.status(201).json(OrderView(order));           // serializer whitelists fields (BE-008)
});
```

Role comes from the session, never the body. Errors leave through the one
pipeline (**BE-001**, **BE-006**) as problem-details with a correlation
ID; the full truth is logged server-side (**BE-285**), nothing internal
reaches the client. The endpoint passes the persistence test and the
duplicate-submit test before it is called done.

## Skills used

- [api-building](../skills/backend/api-building/SKILL.md)
- [validation](../skills/backend/validation/SKILL.md)
- [error-handling](../skills/backend/error-handling/SKILL.md)
- [rate-limiting](../skills/backend/rate-limiting/SKILL.md)
