# Example 1 — One word, two contexts

## Before

One `Order` model serves the whole system. To sales, an order is a
commitment a customer can still amend or cancel; to fulfillment, an order is
a sealed picking list that must never change. Every change request starts an
argument about which meaning the code should follow this time, and the
model grows flags (`amendable`, `sealed`) to be both at once.

## After

The language shift marks the boundary:

- **Sales context** owns `Order` — the customer's commitment, amendable
  until confirmed.
- **Fulfillment context** owns `ShipmentRequest` — created from the
  confirmed order, immutable once issued.

The context map records a customer/supplier relationship: fulfillment
consumes sales' `OrderConfirmed` event and translates it through an
anti-corruption layer into its own `ShipmentRequest`. Each glossary defines
its own terms, and neither model carries the other's flags.

Note: corrects AR-223 — where the same word changes meaning, that shift marks a bounded-context boundary.
