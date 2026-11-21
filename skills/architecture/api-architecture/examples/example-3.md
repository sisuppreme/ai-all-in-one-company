# Example 3 — Verb endpoints remodeled as resources

## Before

The API surface is RPC in HTTP clothing: `POST /createOrder`, `POST /getOrders`, `POST /cancelOrder`, `POST /deleteUser`. Every operation is a POST, status codes carry no meaning, and caching, idempotency semantics, and client generation all have nothing to build on.

## After

The surface is remodeled on the domain resources, per the house profile:

```text
POST   /v1/orders                        create an order
GET    /v1/orders                        list orders (cursor-paginated)
GET    /v1/orders/{id}                   read one order
POST   /v1/orders/{id}/cancellations     cancel an order (sub-resource action)
DELETE /v1/users/{id}                    delete a user
```

Standard operations ride the HTTP methods; the one genuine action — cancellation — is a named sub-resource, so it can carry its own payload (reason, effective date) and lifecycle.

## Note

Corrects AR-067 (resource names are plural nouns; verbs appear only as named sub-resource actions, per the house profile).
