# Example 2 — An executed example replacing one the API rejects

## Before

The quickstart shows:

```bash
curl -X POST https://api.example.com/v1/charges \
  -d '{"amount": "10.00", "description": "Test charge"}'
```

Copy-pasting it returns 422: `amount` must be an integer in minor units, and the required `currency` field is missing entirely. The example was written from memory and never run.

## After

The quickstart shows an example that CI executes against staging on every docs build:

```bash
curl -X POST https://api.example.com/v1/charges \
  -H "Authorization: Bearer $API_KEY" \
  -d '{"amount": 1000, "currency": "usd", "description": "Test charge"}'
# → 201 {"id": "chg_9f27", "amount": 1000, "currency": "usd", "status": "pending"}
```

The execution gate (G-AR-051) asserts the documented 201 and response shape; a future contract change that breaks the example fails the docs build instead of the reader.

## Note

Corrects AR-104 (examples are real requests, verified by execution against a running instance — not checked by eye).
