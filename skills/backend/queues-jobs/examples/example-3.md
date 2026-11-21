# Example 3 — An idempotent payment handler

## Before

The handler charges on every run. Delivery is at-least-once, so a worker
restart at the wrong moment charges the customer twice:

```js
new Worker('payments', async (job) => {
  const order = await db.orders.findById(job.data.orderId);
  await payments.charge(order.customerId, order.total); // runs again on redelivery
  await db.orders.update(order.id, { status: 'paid' });
});
```

## After

The effect is keyed. The job's idempotency key is passed to the provider
and recorded locally, so a redelivery finds the first charge instead of
making a second one:

```js
new Worker('payments', async (job) => {
  const order = await db.orders.findById(job.data.orderId); // re-read, never a snapshot — BE-185
  if (order.status === 'paid') return;                        // already done: succeed quietly

  const charge = await payments.charge(order.customerId, order.total, {
    idempotencyKey: `charge:${order.id}`, // the provider replays, never duplicates
  });

  await db.orders.update(order.id, { status: 'paid', chargeId: charge.id });
});
```

Kill the worker mid-job, restart it, let the job run twice: the customer
sees exactly one charge, and the order agrees.

Note: corrects BE-184 — handlers are idempotent because delivery is at-least-once.
