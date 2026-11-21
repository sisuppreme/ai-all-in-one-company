# Example 2 — The cross-context table read, replaced

## Before

The fulfillment module needs order totals, so it connects to the sales
database and joins `sales.orders` and `sales.order_lines` directly. The join
encodes sales' discount rules inside fulfillment's queries. Sales later
changes how discounts are stored; fulfillment's totals silently change with
it, and no contract, test, or changelog anywhere registers the break.

## After

Sales publishes an `OrderConfirmed` event carrying the confirmed totals —
the figures sales itself computed under its own rules. Fulfillment stores
what it needs in its own model at confirmation time and never touches the
sales schema. When sales remodels its tables, its event contract is the
compatibility surface, checked in CI like any API.

Note: corrects AR-226 — contexts communicate through the context map's declared mechanisms (here, published events); direct reads of another context's tables are forbidden.
