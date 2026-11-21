# Example 3 — Embed vs reference, decided per relationship

## Before

The document store embeds everything reachable from an order: the full
customer record, the full product records, and every review of every product.
A customer's address change requires rewriting thousands of order documents,
and product documents grow without bound as reviews accumulate.

## After

Decided per relationship, from the access patterns:

- **Order lines: embed.** Lines are read only with their order, owned by it,
  and never grow independently.
- **Customer: reference.** The order stores `customer_id`; the customer is
  shared across orders and edited in one place.
- **Reviews: reference, in their own collection.** Reviews are read without
  the product page as often as with it, and grow independently.

Each decision is recorded in the data-architecture notes with the access
pattern that drove it.

Note: corrects AR-146 — embed what is read together and owned together; reference what is shared or independently growing, decided per relationship.
