# Example 1 — A receipt email moved from fire-and-forget to a transactional job

## Before

The order handler fires the email into the void and returns. A crash, a
rejection, or a provider outage loses the receipt with no trace:

```js
app.post('/orders', async (req, res) => {
  const order = await db.orders.create({ ...req.body, status: 'paid' });
  sendReceiptEmail(order); // not awaited, not caught, not queued
  res.status(201).json(order);
});
```

## After

The job row is written in the same transaction as the order (the outbox
pattern). If the transaction commits, the job exists; if it rolls back,
neither does. A separate worker drains the outbox into the queue:

```js
app.post('/orders', async (req, res) => {
  const order = await db.transaction(async (tx) => {
    const created = await tx.orders.create({ ...req.body, status: 'paid' });
    await tx.outbox.create({
      type: 'email.receipt',
      payload: { orderId: created.id },        // IDs only — BE-185
      idempotencyKey: `receipt:${created.id}`,
    });
    return created;
  });
  res.status(201).json(order);
});

// worker: poll the outbox, enqueue, mark dispatched
async function dispatchOutbox() {
  for (const row of await db.outbox.pending()) {
    await emailQueue.add(row.type, row.payload, { jobId: row.idempotencyKey });
    await db.outbox.markDispatched(row.id);
  }
}
```

The receipt can now fail, retry, and be inspected — it can no longer
silently not exist.

Note: corrects BE-182 — the job is enqueued in the same transaction as the state change that causes it.
