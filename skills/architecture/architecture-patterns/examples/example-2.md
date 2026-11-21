# Example 2 — The decorative queue, made real or removed

## Before

The architecture page says "event-driven." A broker is deployed, but the
checkout request publishes `ProcessPayment` and blocks on a reply queue until
the payment service answers synchronously. The broker adds latency, a failure
mode, and an operations burden — and decouples nothing.

## After

Two honest options, one chosen in an ADR:

- **Remove the broker.** Payment is a synchronous dependency of checkout;
  call the payment API directly with a timeout and a retry policy, and say so
  in the design.
- **Make it a real pattern.** Checkout publishes an `OrderPlaced` fact
  through a transactional outbox; the payment consumer processes it
  idempotently; checkout completes without waiting, and the order page shows
  the payment state as it resolves.

The project chose the direct call: the business required a payment answer
before showing confirmation.

Note: corrects AR-165 — a queue or broker in the diagram while all interactions remain synchronous is decoration and fails review.
