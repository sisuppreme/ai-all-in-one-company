# Example 2 — Dual write becomes a transactional outbox

## Before

```ts
await db.orders.insert(order);          // commits
await broker.publish("OrderPlaced", …); // process crashes here, sometimes
```

Every crash between the two lines leaves an order that downstream systems
never hear about. Reconciliation is a support ticket.

## After

```ts
await db.transaction(async (tx) => {
  await tx.orders.insert(order);
  await tx.outbox.insert({ type: "OrderPlaced", payload, status: "pending" });
});
// A relay process publishes pending outbox rows and marks them sent.
```

The order and its event commit or roll back together. The relay can crash
and restart safely: unpublished rows are still pending, and consumers
deduplicate on the event `id`, so a republished row applies once.

Note: corrects AR-205 — publication is atomic with the business write, via a transactional outbox or an event store.
