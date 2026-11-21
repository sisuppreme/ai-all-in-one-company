# Example 2 — The checkout that confirmed orders it never placed

Scenario: "Atlas Store" (a hypothetical prototype shop) demos beautifully:
every checkout ends on an "Order confirmed" page. The DX-161 ledger exercise
tells a different story — submit checkout while the payment provider is
unreachable, reload the orders page, and inspect the store — and classifies
checkout as SIMULATED: no order row exists, nothing was charged, and a
double-click on the pay button would have charged twice if it had been
(DX-162).

## Before

```js
// server/checkout.js — as shipped in the prototype
app.post('/api/checkout', async (req, res) => {
  const { cartId, cardToken, qty } = req.body; // trusted as sent (no DX-166)
  try {
    await payments.charge({ token: cardToken, amount: req.body.amount });
    await db.query(
      "INSERT INTO orders (cart_id, qty) VALUES ('" + cartId + "', " + qty + ")",
    );
  } catch (err) {
    // TODO: handle errors properly before launch
  }
  res.json({ ok: true, message: 'Order confirmed' });
});
```

Four separate defects, all visible in eleven lines:

- The `catch` block is empty: a declined card, a provider timeout, and a
  failed insert all fall through to the success response — BAN-DX-086,
  success-on-failure.
- The amount is taken from the request body, and `qty` / `cartId` are never
  validated server-side — a direct DX-166 violation.
- The order insert is string-built from user input — BAN-DX-085.
- Charge and insert are not one transaction and carry no idempotency key,
  so a failure between them leaves money taken with no order, and a
  resubmission charges again — a direct DX-168 violation.

## After

```js
// server/checkout.js — hardened
app.post('/api/checkout', async (req, res) => {
  const requestId = req.id; // correlation id, logged on every path (DX-167)

  // 1. Validate at the boundary, server-side (DX-166). The amount is never
  //    accepted from the client; it is recomputed from the stored cart.
  const parsed = CheckoutRequest.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: 'Please check your order details.' });
  }
  const { cartId, cardToken, idempotencyKey } = parsed.data;
  const cart = await carts.getOwned(cartId, req.user.id);
  if (!cart) return res.status(404).json({ error: 'Cart not found.' });

  // 2. Reserve the order first, in one short transaction (DX-168): the
  //    row — and its unique idempotency key — exists before any money
  //    moves, so a resubmission finds it instead of starting over.
  const reserved = await db.tx(async (t) => {
    const existing = await t.oneOrNone(
      'SELECT * FROM orders WHERE idempotency_key = $1', [idempotencyKey]);
    if (existing) return existing;
    return t.one(
      `INSERT INTO orders (cart_id, user_id, amount_cents,
                           idempotency_key, status)
       VALUES ($1, $2, $3, $4, 'pending_payment') RETURNING *`,
      [cartId, req.user.id, cart.totalCents, idempotencyKey]);
  });
  if (reserved.status === 'paid') {
    return res.status(201).json({ ok: true, orderId: reserved.id });
  }

  // 3. Charge OUTSIDE the transaction. A database transaction cannot roll
  //    back a provider charge: charging inside one recreates the Before
  //    bug — if the insert then fails, the money is taken, no order
  //    exists, and "you have not been charged" becomes a lie. The provider
  //    receives the same idempotency key, so a retry never charges twice.
  let charge;
  try {
    charge = await payments.charge({
      token: cardToken, amount: cart.totalCents, idempotencyKey,
    });
  } catch (err) {
    // Handled, logged, safe to show (DX-167): the reserved row is marked
    // payment_failed — retained for audit, never shown as an order placed —
    // and the user gets a generic message with no provider internals. The
    // message is honest: this path runs only when the charge did not happen.
    await db.query(
      "UPDATE orders SET status = 'payment_failed' WHERE id = $1",
      [reserved.id]);
    logger.error({ requestId, op: 'checkout', cartId, err },
                 'checkout failed');
    return res.status(502).json({
      error: 'Payment could not be completed. You have not been charged; ' +
             'please try again.',
    });
  }

  // 4. Finalize with a single atomic update. If the process dies between
  //    the charge and this update, the row stays in pending_payment under
  //    its idempotency key: a retry finds the row, looks the charge up at
  //    the provider under that key instead of charging again, and
  //    finalizes — the state is visible and reconcilable, never silent.
  const order = await db.one(
    `UPDATE orders SET status = 'paid', charge_id = $2
     WHERE id = $1 RETURNING *`,
    [reserved.id, charge.id]);
  return res.status(201).json({ ok: true, orderId: order.id });
});
```

Supporting schema change (DX-168), applied as a reversible migration:

```sql
ALTER TABLE orders
  ADD COLUMN idempotency_key text,
  ADD COLUMN status text NOT NULL DEFAULT 'pending_payment',
  ADD CONSTRAINT orders_idempotency_key_unique UNIQUE (idempotency_key),
  ALTER COLUMN cart_id SET NOT NULL,
  ALTER COLUMN amount_cents SET NOT NULL,
  ADD CONSTRAINT orders_cart_fk FOREIGN KEY (cart_id) REFERENCES carts (id);
```

Tests name the failure and duplicate cases explicitly (DX-170):

```js
test('provider failure returns an error, never a confirmation', async () => {
  payments.failNextCharge(new Error('provider timeout'));
  const res = await checkout(validCart, { idempotencyKey: 'k-fail-1' });
  expect(res.status).toBe(502);
  const orders = await ordersFor(validCart.id);
  expect(orders.filter((o) => o.status === 'paid')).toHaveLength(0);
  expect(orders[0].status).toBe('payment_failed'); // retained for audit,
  // never presented to the customer as an order placed
});

test('double submission charges once and creates one order', async () => {
  const first  = await checkout(validCart, { idempotencyKey: 'k-dupe-1' });
  const second = await checkout(validCart, { idempotencyKey: 'k-dupe-1' });
  expect(second.body.orderId).toBe(first.body.orderId);
  expect(payments.chargeCount).toBe(1);
  expect(await ordersFor(validCart.id)).toHaveLength(1);
});
```

The area is proven with the G-DX-084 failure and integrity drill in staging
under production configuration: the provider is forced to fail once (user
sees the generic error, the log line carries `requestId`), the checkout
form is double-submitted (one charge, one order), and the process is
killed between the charge and the finalize update — the order sits in
`pending_payment` under its idempotency key, and the retry reconciles it
against the provider instead of charging again: no charge without an
order, no duplicate, no silent partial state. Checkout is then
closed HARDENED under DX-174.

## Note

Corrected under DX-167 (every I/O boundary has an error path; failures are
logged with context and shown generically), DX-168 (constraints,
transactions, and idempotent writes enforced by the store), and DX-166
(server-side validation, parameterized queries). Removes the violations in
BAN-DX-086 (swallowed errors and success-on-failure) and BAN-DX-085
(string-built queries). Verified by G-DX-084 and the DX-170 tests above.
