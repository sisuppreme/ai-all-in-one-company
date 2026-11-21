# Example 1 — The payment failure that displayed "Success"

## Before

The checkout handler catches every exception and carries on as if nothing happened:

```js
try {
  await payments.charge(order);
} catch (err) {
  // TODO: handle errors later
}
return { status: "success" };
```

The charge failed, no system recorded it, and the user was told the order succeeded. The team learned about the lost orders from customer complaints a week later — this is BAN-AN-081 (swallowed errors).

## After

The failure propagates to the error boundary, which captures it in the tracker with its context and shows the user an honest failure state:

```js
try {
  await payments.charge(order);
} catch (err) {
  tracker.captureException(err, {
    release, environment,
    trace_id, request_id,
    extra: { order_id: order.id, step: "charge" },
  });
  return { status: "payment_failed", correlation_id: request_id };
}
```

The error exists as a tracked issue with a stack, the release tag, and a correlation ID the user can quote and support can look up; the synthetic-error gate (G-AN-081) proves this path works before release.

Note: the Before violates AN-161 (every unhandled error is captured in the tracker); the After corrects it.
