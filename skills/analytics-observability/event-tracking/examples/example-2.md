# Example 2 — The product name inside the event name

## Before

A store instruments purchases by interpolating the product into the event name: `Purchased - Blue Mug`, `Purchased - Desk Lamp`, `Purchased - Gift Card`. Every new product creates a new event, the taxonomy grows past a thousand names, and "total purchases" requires summing an ever-changing list that nobody maintains.

## After

One event, `Order Completed`, carries the varying data as properties: `product_id`, `category`, `revenue`. Product-level reports group by the property, the event count stays one, and a new product changes no instrumentation.

_Rule: AN-023 — no dynamic values in event names; the value goes in a property._
