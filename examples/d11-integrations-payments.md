# D11 Integrations & Payments — End-to-End Example

## Scenario

"NoteNest," a small note-taking SaaS, adds a paid Pro plan: hosted checkout for the
subscription, a webhook endpoint that grants Pro access, and refunds from the admin
panel. The first AI-built version "works" in a demo — and would hand out Pro for free
and double-charge real customers in production.

## Before — the slop version

```js
// Checkout: the browser names the plan AND the price
app.post('/checkout', async (req, res) => {
  const session = await provider.checkout.sessions.create({
    amount: req.body.amount,            // whatever the client posted
    currency: 'usd',
  });
  await db.orders.create({ userId: req.user.id, status: 'pending' });
  res.json({ url: session.url });
});

// The success page grants the plan
app.get('/checkout/success', async (req, res) => {
  await db.users.update(req.user.id, { plan: 'pro' });
  res.render('thanks', { message: 'Payment successful — welcome to Pro!' });
});

// The webhook trusts any POST that claims success
app.post('/webhooks/provider', async (req, res) => {
  const event = req.body;               // no signature check, parsed JSON
  if (event.type === 'payment_succeeded') {
    const seen = await db.events.findOne({ id: event.id });
    if (!seen) await db.events.insert({ id: event.id });
    await db.users.increment(req.body.userId, 'credits', 1);
  }
  res.sendStatus(200);
});
```

## What the skills caught

- **BAN-IN-002 — Client-priced checkout** (defeats DET-FAKE-006). The amount comes
  from the request body; posting `{ "amount": 100 }` buys the plan for a fraction of
  its price. **IN-001**: the client names the plan ID; the server computes amount and
  currency from the catalog.
- **BAN-IN-001 — The success-page grant** (defeats DET-FAKE-006). Anyone who guesses
  `/checkout/success` gets Pro with no charge anywhere. **IN-005**: entitlement comes
  from the verified webhook, never the redirect; the success page is a display state.
- **BAN-IN-051 — The trusted POST** (defeats DET-FAKE-006). The webhook acts on any
  unauthenticated POST. **IN-101**: verify the signature over the raw body, before
  parsing; **IN-102**: reject and log every failed verification.
- **BAN-IN-052 — Check-then-insert deduplication** (defeats DET-CODE-030). Two
  concurrent duplicate deliveries both read "not found" and both insert. **IN-104**:
  deduplication is a unique constraint on the provider event ID, not a lookup.
- **BAN-IN-053 — The incrementing handler** (defeats DET-FAKE-022). A provider retry
  credits the customer twice. **IN-106**: handlers converge the mirror to the event's
  state, so redelivery is a no-op.
- **BAN-IN-004 — The keyless charge** (defeats DET-FAKE-006). Checkout creation has
  no idempotency key; a double-click creates two charges. **IN-002**: every money
  call carries a key derived from the order ID. **IN-003** also applies: the pending
  order must exist *before* the provider session, not after it.

## After — the corrected version

```js
// Checkout: client names the plan; the server prices it (IN-001, IN-002, IN-003)
app.post('/checkout', async (req, res) => {
  const plan = catalog.getPlan(req.body.planId);            // server-side catalog
  const order = await db.orders.create({
    userId: req.user.id, status: 'pending',
    amount: plan.amountMinor, currency: plan.currency,      // integer minor units (IN-012)
  });
  const session = await provider.checkout.sessions.create(
    { amount: order.amount, currency: order.currency, metadata: { orderId: order.id } },
    { idempotencyKey: `checkout:${order.id}` },
  );
  res.json({ url: session.url });
});

// Success page grants nothing (IN-005)
app.get('/checkout/success', (req, res) =>
  res.render('thanks', { message: 'Payment processing — access activates on confirmation.' }));

// Webhook: verify raw body → persist → acknowledge → process async (IN-101..IN-106)
app.post('/webhooks/provider', express.raw({ type: 'application/json' }), async (req, res) => {
  let event;
  try {
    event = provider.webhooks.constructEvent(req.body, req.headers['provider-signature'],
                                             secrets.webhookSigningKey);   // IN-111
  } catch {
    log.warn('webhook signature failed', { source: req.ip });
    return res.sendStatus(400);                                            // IN-102
  }
  try {
    await db.events.insert({ id: event.id, type: event.type, receivedAt: now() });
  } catch (e) {
    if (isUniqueViolation(e)) return res.sendStatus(200);   // duplicate: already stored (IN-104)
    throw e;
  }
  res.sendStatus(200);                                      // stored, not yet processed (IN-103)
  await queue.enqueue('webhook', { eventId: event.id });    // worker converges state (IN-105, IN-106)
});
```

The worker reconciles each event against the expected order — account, amount,
currency, state — before fulfilling (IN-108), and a scheduled job diffs local rows
against the provider's payment list so missed events still converge (IN-109, IN-010).
The whole flow is proven in test mode first, including a decline card and a webhook
replay (IN-011).

## Skills used

- [payments](../skills/integrations-payments/payments/SKILL.md)
- [webhooks](../skills/integrations-payments/webhooks/SKILL.md)
- [subscriptions](../skills/integrations-payments/subscriptions/SKILL.md)
- [refunds-disputes](../skills/integrations-payments/refunds-disputes/SKILL.md)
