# Example 2 — Adding failure behavior to a happy-path design

## Before

The design describes checkout as: "Web App calls the Payments API, which charges the card and returns success." Nothing states a timeout, what happens on a retry, or what the customer sees when the Payments API is down. The first real outage becomes an improvised incident.

## After

The design's call table gains a row per cross-container call. For Web App → Payments API: timeout 3 s; retry policy — one retry with the same idempotency key, only on network errors, never on a 4xx; callee down — checkout pauses with a "payment temporarily unavailable" state, the cart is preserved, no order is created, and the failure is logged with the idempotency key for reconciliation.

## Note

Corrects AR-003 (timeout, retry policy, and callee-down behavior stated per call) and AR-007 (failure designed in the same pass as the happy path).
