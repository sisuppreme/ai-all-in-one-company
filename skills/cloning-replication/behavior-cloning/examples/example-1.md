# Example 1 — "Verified" from the screenshot

## Before

```text
Behavior record (excerpt)
Flow: Checkout — submit order
Status: VERIFIED (matches source screenshots, button and totals render
        identically)
Notes: Form posts the order. Success screen shows order number.
```

Nobody ever submitted the form. The screenshots match, so the flow was declared cloned — but the source actually validates stock and address before charging, and rejects with inline messages the rebuild never reproduced.

## After

```text
Behavior record (excerpt)
Flow: Checkout — submit order
Spec: tests/checkout-submit.spec.ts (recorded 2026-11-21, frozen set)
  1. Fill cart + valid address → submit enabled
  2. Submit with out-of-stock item → inline error at the item row,
     no charge request fired (network: POST /validate only)
  3. Submit with valid cart → POST /orders, state change to
     confirmation page with order number
Edge cases recorded: double-submit (button disables, one POST),
invalid postcode (inline message, no request)
```

## Note

Violates CL-082 and CL-083 (behavior must be an executable spec recording trigger, action, and observed state change — appearance is not behavior); corrected by recording the flow as a scripted interaction test, including its validation and network behavior.
