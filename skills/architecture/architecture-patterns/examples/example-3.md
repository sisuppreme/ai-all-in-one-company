# Example 3 — A saga adoption with its compensations named

## Before

ADR excerpt: "We will use the Saga pattern for checkout." Nothing else. When
shipping fails after payment, support discovers there is no refund path and
no stock release; the "saga" was three service calls and a hope.

## After

ADR excerpt, adoption record for the checkout saga (choreography variant):

| Step | Action | Compensation |
|---|---|---|
| 1 | Reserve stock | Release reservation |
| 2 | Charge card | Refund to original payment method |
| 3 | Book shipment | Cancel booking (no-op if not yet created) |

Consequences accepted: the customer can briefly see "paid, not yet shipped";
support sees the saga state per order. Trigger for the orchestration variant:
a fourth step, or compensation ordering that choreography cannot express.

Note: corrects AR-164 — adopting Saga requires the compensating transactions to be named; the hard part is the deliverable, not the label.
