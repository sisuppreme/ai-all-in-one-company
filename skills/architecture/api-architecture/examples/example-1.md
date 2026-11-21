# Example 1 — One error format replacing per-endpoint shapes

## Before

Three endpoints, three error dialects. `GET /orders` returns `{"error": "nope"}` with a 400. `POST /orders` returns `{"message": "bad input", "code": 7}`. `GET /invoices/{id}` returns a plain-text `Server Error` with a 500 for a missing invoice. Clients write a parser per endpoint, and a missing resource is indistinguishable from a crash.

## After

Every endpoint returns the house Problem Details body. The missing invoice returns:

```json
{
  "type": "https://api.example.com/problems/invoice-not-found",
  "title": "Invoice not found",
  "status": 404,
  "detail": "No invoice exists with id inv_8123."
}
```

Validation failures return status 422 with the same shape and a `type` naming the problem class. The OpenAPI document references one shared `Problem` schema for every error response.

## Note

Corrects AR-063 (one error format — Problem Details — for every endpoint; per-endpoint shapes are a blocking defect).
