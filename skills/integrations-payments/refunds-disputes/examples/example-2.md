# Example 2 — The double refund on retry

## Before

An admin clicks Refund; the request times out before the response returns, so they click again. The refund endpoint creates a fresh provider refund on each call, with no idempotency key. The customer is refunded twice, accounting finds two refund rows that match nothing in the plan, and the second refund is discovered only at month-end reconciliation.

## After

The refund request carries an idempotency key derived from the order ID and refund sequence. The timed-out first call and the admin's retry send the same key, so the provider returns the original refund instead of creating a second one. The admin UI shows the single refund and its provider status; a deliberate second, separate refund would need a new sequence value and a recorded reason.

*Demonstrates IN-042 — one idempotency key per refund request makes retries return the original refund, never a duplicate.*
