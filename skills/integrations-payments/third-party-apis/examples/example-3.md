# Example 3 — An unbounded, retry-everything call given timeouts and safe retries

## Before

A webhook-forwarding job calls a customer's endpoint like this:

```js
async function forward(url, payload) {
  while (true) {
    try {
      return await fetch(url, { method: "POST", body: payload });
    } catch {
      // retry immediately, forever
    }
  }
}
```

There is no timeout, so one hung endpoint parks the worker indefinitely.
When the endpoint is merely slow, the immediate retry loop fires the same
non-idempotent POST again and again — the customer receives the event
eleven times, and the loop never backs off or gives up.

## After

The call is bounded, timed, and safe to retry because it carries a key:

```js
const MAX_ATTEMPTS = 4;

async function forward(url, payload, eventId) {
  for (let attempt = 1; attempt <= MAX_ATTEMPTS; attempt++) {
    try {
      return await fetch(url, {
        method: "POST",
        body: payload,
        headers: { "Idempotency-Key": eventId },
        signal: AbortSignal.timeout(5000), // 5s read budget
      });
    } catch (err) {
      if (attempt === MAX_ATTEMPTS) throw err;
      await sleep(backoffWithJitter(attempt)); // 1s, 2s, 4s + jitter
    }
  }
}
```

After four attempts the failure is recorded and the event stays queued for
the next scheduled pass instead of blocking the worker. The
failure-injection audit (G-IN-093) replays 500s, 429s, and dropped
connections against this code and asserts the attempt cap, the growing
backoff, and exactly-once delivery via the idempotency key.

Note: corrects IN-182 and IN-183 — every call carries a timeout, and retries are bounded, backed off, and safe for non-idempotent operations.
