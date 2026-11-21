# Example 1 — The refund that was only a label

## Before

The admin panel's Refund button runs a local update: it sets `order.status = "refunded"`, shows a "Refund issued" toast, and the customer receives a "Your refund is complete" email. No call is made to the payment provider — there is no refund object, no provider refund ID, and no money moves. The customer discovers this weeks later when the charge is still on their statement, and files a dispute.

## After

The Refund action calls the provider's refund API against the original payment ID with an idempotency key derived from the order ID, and records the returned provider refund ID, amount, and reason on the order. The order displays "Refund pending" until the provider's refund event confirms it; only then does entitlement reverse per the written rule and the confirmation email go out, worded with the provider's expected-arrival window.

*Demonstrates IN-041 / IN-043 — a refund exists only as a provider object confirmed by provider state, never as a local label.*
