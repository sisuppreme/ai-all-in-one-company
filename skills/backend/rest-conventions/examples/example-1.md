# Example 1 — Verb URLs remodeled as resources

## Before

```text
POST /api/createOrder
GET  /api/getOrders?userId=42
POST /api/cancelOrder/:id
POST /api/deleteOrder/:id
GET  /api/getOrderById/:id
```

Every operation is a verb, the same API also grows `GET /api/orders` later,
and clients must learn a new URL shape for every capability.

## After

```text
POST   /orders                     create an order for the authenticated user
GET    /orders                     list the authenticated user's orders (paginated)
GET    /orders/{id}                read one order
DELETE /orders/{id}                delete one order (idempotent end state)
POST   /orders/{id}/cancellations cancel an order — the cancellation is a resource
```

The method carries the operation's meaning (POST creates, GET reads, DELETE
removes), ownership comes from the session instead of a `userId` parameter,
and cancellation — a state change with its own data (reason, timestamp,
refund reference) — is modeled as the sub-resource it actually is.

Note: corrects BE-023 — no verbs in URLs; non-CRUD actions are modeled as sub-resources.
