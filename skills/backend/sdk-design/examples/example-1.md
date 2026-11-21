# Example 1 — Retry that duplicated an order, made safe with an idempotency key

## Before

```ts
const client = new ApiClient({
  baseUrl: "https://api.example.com",
  retries: 3, // applied to every method, including POST creates
});

await client.orders.create({ items, totalCents });
```

The server commits the order, the response is lost to a network stall, and
the SDK — doing exactly what it was configured to do — retries. The server
sees a brand-new request and creates a second order. The customer is
charged twice, and both sides' logs look correct.

## After

```ts
const client = new ApiClient({
  baseUrl: "https://api.example.com",
  retries: 3, // SDK policy: retries apply to idempotent operations only,
             // unless the request carries an idempotency key
});

await client.orders.create(
  { items, totalCents },
  { idempotencyKey: randomUUID() }, // generated once, reused on every retry
);
```

The SDK's retry policy refuses to replay a non-idempotent call unless it
carries an idempotency key; when a key is present, the same key goes out on
every attempt, so the server replays the first response instead of repeating
the effect. A lost response now costs a retry, not a duplicate.

Note: corrects BE-084 — retries only for idempotent operations or requests carrying an idempotency key, with the same key reused across retries.
