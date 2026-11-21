# Example 3 — Replacing in-request processing with persist, acknowledge, and queue

Corrects IN-105 (with IN-103): the request verifies, stores, and returns; the worker does the slow work, so timeouts never trigger duplicate retries.

## Before

```js
// Everything happens inside the request: a provider API call, a PDF
// render, two emails. The handler takes ~20s, the provider times out,
// retries the delivery — and the duplicate grants and emails twice.
app.post("/webhooks/stripe", verifySignature, async (req, res) => {
  const event = req.body;
  await fulfillOrder(event);            // provider re-read + DB writes
  await renderAndStoreInvoice(event);   // slow
  await sendReceiptEmail(event);        // slow, external
  await sendOwnerNotification(event);   // slow, external
  res.sendStatus(200);
});
```

## After

```js
// Request path: verify (middleware), persist, acknowledge. Target: <1s.
app.post("/webhooks/stripe", verifySignature, async (req, res) => {
  const stored = await storeEventIfNew(req.event); // unique on provider event ID
  if (stored) await queue.enqueue("process-webhook-event", { eventId: req.event.id });
  res.sendStatus(200); // 2xx promises "stored", not "processed"
});

// Worker path: slow work lives here, where a retry is safe.
queue.process("process-webhook-event", async ({ eventId }) => {
  const event = await loadEvent(eventId);
  await fulfillOrder(event);            // converging handler (IN-106)
  await renderAndStoreInvoice(event);
  await sendReceiptEmail(event);
  await recordOutcome(eventId, "processed"); // every outcome logged (IN-110)
});
```

Note: the "before" handler does heavy processing before responding, so provider timeouts manufacture duplicates; the "after" handler persists and acknowledges immediately and processes from the queue, per IN-105.
