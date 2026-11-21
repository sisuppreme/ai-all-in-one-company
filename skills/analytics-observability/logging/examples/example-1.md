# Example 1 — Console breadcrumbs become structured logs

## Before

A server handler is debugged with free-text console calls that ship to production:

```js
console.log("here");
console.log("user checked out, total was " + cart.total);
console.log("something went wrong??", err);
```

The lines have no timestamp discipline, no level, no request ID, and no consistent shape. In the central store they cannot be grouped, counted, or tied to the request that produced them — and "something went wrong??" is written at the same weight as a successful checkout.

## After

The same points go through the shared logger with the fixed field set:

```js
logger.info("checkout_completed", { trace_id, request_id, order_id, total_cents, duration_ms });
logger.error("checkout_failed", { trace_id, request_id, order_id, error_code: err.code, stack: err.stack });
```

Every line is single-line JSON carrying timestamp, level, service, environment, trace ID, and request ID; the failure is at `error` with its stack, and the lint gate (G-AN-041) keeps the console calls from coming back.

Note: the Before violates AN-088 (no raw console logging in production paths) and AN-081 (one logger, one format); the After corrects both.
