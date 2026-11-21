# Example 2 — Scattered provider calls consolidated behind an adapter

## Before

The shipping provider's SDK is imported wherever a label or rate is needed:

```js
// checkout.js
import ShipCo from "shipco";
const client = new ShipCo(process.env.SHIPCO_KEY);
const rate = await client.rates.get(zip); // response used raw

// admin/labels.js
import ShipCo from "shipco";
const client2 = new ShipCo(process.env.SHIPCO_KEY);
await client2.labels.create(order); // no timeout, no error mapping
```

Each call site parses the provider's response shape itself, handles errors
differently (one swallows them), and sets no timeouts. When the provider
renames a field, three files break in three different ways.

## After

One adapter module owns the provider; domain code sees only project types:

```js
// integrations/shipping/adapter.js — the only file importing "shipco"
export async function getRate(zip) {
  const raw = await call("rates.get", () => client.rates.get(zip));
  return validateRate(raw); // schema check, then map to { cents, days }
}

// checkout.js
import { getRate } from "../integrations/shipping/adapter.js";
const rate = await getRate(zip); // { cents, days } — no provider types
```

Timeouts, retries, the circuit breaker, and response validation live in the
adapter's shared `call` helper. A provider field rename is now a one-file
fix, and the contract suite (G-IN-091) tests the adapter alone.

Note: corrects IN-181 — one adapter per provider, and no provider SDK type or response object leaks past it.
