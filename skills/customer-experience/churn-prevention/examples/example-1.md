# Example 1 — The cancel button that went nowhere

## Before

```text
Settings → Plan → [Cancel subscription]

Click "Cancel subscription":
  → Modal: "We're sorry to see you go! Email support@example.com
    with your account email and we'll process your cancellation
    within 3 business days." [OK]

User emails support. Inbox is checked weekly.
Renewal date passes during the wait. User is charged again.
Chargeback follows, citing the cancellation email timestamp.
```

The only cancel path leaves the product, depends on a human reading an inbox, and leaves billing running in the meantime — the request submits to no system that can act on it.

## After

```text
Settings → Plan → [Cancel subscription]

Step 1 (optional): "What's the main reason you're leaving?"
  ( ) Too expensive  ( ) Not using it  ( ) Missing a feature
  ( ) Something is broken  ( ) Other        [Skip]

Step 2 (only because reason = "Not using it"):
  "Pause instead? Your plan pauses for 2 months, no charges,
   and resumes on August 1 unless you cancel first."
  [Pause my plan]   [Cancel my subscription]

Step 3 — user clicks "Cancel my subscription":
  Billing state changes in the same session.
  Confirmation: "Cancelled. You keep access until July 31.
   No further charges will be taken."
  Churn log: voluntary · reason=not-using · offer=pause · declined.

G-CX-072 friction audit: signup 4 steps, cancel 3 steps, all in-product.
G-CX-073: billing status = cancelled, end date July 31, test clock
advanced past July 31 generates no invoice.
```

## Note

Corrected under CX-142 and CX-143 (BAN-CX-072): cancellation completes self-serve in the product in no more steps than signup — one optional reason question, at most one matched offer, one confirmation.
