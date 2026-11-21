# Example 1 — An outage shown as "no orders" corrected to a degradation state

## Before

The orders page loads through the commerce provider's adapter:

```js
async function loadOrders(userId) {
  try {
    const res = await provider.orders.list({ user: userId });
    return res.data;
  } catch {
    return []; // render the empty state
  }
}
```

During a provider outage, every customer sees "You have no orders yet" —
including customers with years of order history. Support is flooded, and
several customers place duplicate orders believing the first ones vanished.

## After

The adapter returns a typed result, and the page renders three distinct
states:

```js
async function loadOrders(userId) {
  const result = await ordersAdapter.listOrders(userId);
  if (result.status === "unavailable") {
    return { state: "degraded", retryAfter: result.retryAfter };
  }
  return { state: "ok", orders: result.orders };
}
```

The degraded state renders: "Orders are temporarily unavailable — our
provider is having trouble. Your orders are safe; nothing is lost." with a
retry button. The dead-endpoint drill (G-IN-092) asserts this state appears,
within the latency budget, whenever the provider is unreachable.

Note: corrects IN-186 — a provider outage is a visible degradation state, never the user's data presented as empty.
