# Example 1 — Modeling from the pattern list

## Before

```javascript
// "Flexible" collections copied from a relational schema; the app re-joins by hand.
// Pattern list: none. Every screen assembles its data from 4–5 round trips.
db.orders.findOne({ _id: orderId });
db.customers.findOne({ _id: order.customerId });
db.orderLines.find({ orderId: orderId });
db.products.find({ _id: { $in: lines.map(l => l.productId) } });
```

## After

```javascript
// Pattern list written first (excerpt):
//   P1: Order detail screen — order + customer name + lines with product names, read together.
//   P2: Customer's orders, newest first.
// The model answers P1 with one read: embed what is read together.
db.orders.insertOne({
  _id: orderId,
  customer: { id: customerId, name: "Example Customer" },  // name duplicated; source of truth: customers (see Example 3)
  lines: [
    { productId: "p-100", name: "Widget", qty: 2, priceCents: 1999 },
    { productId: "p-205", name: "Gadget", qty: 1, priceCents: 4999 }
  ],
  totalCents: 8997,
  placedAt: new Date()
});
db.orders.findOne({ _id: orderId });  // P1 served in a single read
```

Corrects DB-041 (access patterns are listed before the data model) and DB-043 (embed what is read together, reference what is shared or unbounded).
