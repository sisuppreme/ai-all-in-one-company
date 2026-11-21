# Example 3 — The missed webhook the reconciliation sync repaired

## Before

The webhook endpoint is down for maintenance during a renewal window. A
customer's card is charged successfully at the provider, but the
`invoice.paid` and subscription-updated events are never delivered. The
local mirror still shows the old period end, and the entitlement check —
reading the mirror faithfully — cuts the paying customer's access the next
morning. Support restores it by editing the row by hand and filing it under
"glitch."

## After

The same outage, with the reconciliation sync in place:

1. The endpoint outage happens; events are missed exactly as before. This
   is treated as a normal operating condition, not an anomaly.
2. The periodic sync re-reads live subscriptions from the provider,
   compares status and period end against the mirror, and finds the drift:
   provider says renewed through April 30, mirror says March 31.
3. The sync repairs the row from the provider's values and logs the repair
   with both states. The customer's access never lapses.
4. The missed-webhook drill (G-IN-012) runs this scenario in test mode on
   every release, so the repair path is exercised before it is needed.

Note: corrects IN-031 — webhooks are assumed losable, and a scheduled reconciliation diff repairs the mirror without manual edits.
