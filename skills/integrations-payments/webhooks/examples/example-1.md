# Example 1 — Replacing a trusted POST with signature verification over the raw body

Corrects IN-101 (and IN-102): the endpoint must verify the provider signature over the exact bytes received, before parsing, and reject failures.

## Before

```js
// Any POST to this URL is believed. A hand-written curl with a made-up
// "payment succeeded" body marks orders paid and grants access.
app.post("/webhooks/stripe", express.json(), async (req, res) => {
  const event = req.body;
  if (event.type === "payment_intent.succeeded") {
    await markOrderPaid(event.data.object.metadata.orderId);
    await grantAccess(event.data.object.metadata.userId);
  }
  res.sendStatus(200);
});
```

## After

```js
// The route bypasses JSON middleware so the raw bytes survive intact.
// Verification happens on those bytes; only then is the body parsed.
app.post("/webhooks/stripe", express.raw({ type: "application/json" }), async (req, res) => {
  let event;
  try {
    event = stripe.webhooks.constructEvent(
      req.body, // raw Buffer, exactly as received
      req.headers["stripe-signature"],
      process.env.STRIPE_WEBHOOK_SECRET // secret store, per endpoint — never in source
    );
  } catch (err) {
    logRejectedDelivery({ reason: err.message, source: req.ip });
    return res.sendStatus(400); // no state changes on a failed verification
  }
  await storeEvent(event); // persisted before the 2xx (IN-103)
  res.sendStatus(200);
});
```

Note: the "before" handler trusts an unsigned claim of payment and fulfills on it; the "after" handler verifies the signature over the raw body first and rejects anything that fails, per IN-101.
