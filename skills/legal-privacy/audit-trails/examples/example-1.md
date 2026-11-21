# Example 1 — The refund nobody recorded

## Before

A customer disputes a duplicate charge. Support opens the database console, runs an UPDATE to mark the order refunded, and issues the refund from the payment dashboard. No trail entry is written: a week later, nobody can say who authorized the refund, when, or why — the billing system shows money out, and the only record is a chat message saying "done."

## After

The refund is issued from the product's refund flow, which writes the trail entry in the same transaction: actor `support-agent-EXAMPLE-07 (role: support-lead)`, action `refund.issued`, subject `order REF-EXAMPLE-2211`, server timestamp, basis `duplicate-charge dispute DSAR-EXAMPLE-118; approved per refunds policy row R-3`. The dispute can be answered from the trail alone.

*Demonstrates LG-162 and LG-163 — the entry is written in the same flow as the action and carries actor, action, subject, timestamp, and basis.*
