# Example 1 — The cancel button that only hid the row

## Before

The settings page has a Cancel button. Its handler runs one local update:

```ts
await db.subscriptions.update({ where: { id }, data: { hidden: true } });
toast("Your subscription has been canceled.");
```

No call reaches the payment provider. The subscription object there stays
`active`, the renewal invoice is generated on schedule, and the customer is
charged again — while the app, which filters out hidden rows, shows them no
subscription to manage. The first signal is a support ticket and a refund
request.

## After

Cancellation is a provider state change with a confirmation, in order:

1. The confirm screen states the configured behavior first: "You keep Pro
   until March 31, the end of the current period. No further charges."
2. The server calls the provider to cancel at period end, with an
   idempotency key derived from the subscription ID and the request.
3. The webhook event converges the local mirror: status `active` with
   `cancel_at_period_end` recorded and the period end stored on the row.
4. The customer receives a confirmation naming what access remains and the
   date it ends; entitlement reads the mirror and keeps access until that
   date, then stops — driven by the provider's end-of-period event, not a
   local timer.

Note: corrects IN-027 — cancellation writes to the provider and the mirror converges to the returned state; a UI-only cancel is banned (BAN-IN-011).
