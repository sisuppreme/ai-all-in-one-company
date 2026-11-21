# Example 3 — Bare 429 replaced by the 429 contract

## Before

```js
// A numberless refusal. Clients cannot tell which limit they hit or
// when to come back, so they retry immediately and in lockstep.
if (tooMany) {
  return res.status(429).send("Too many requests, try again later");
}
```

## After

```js
// The 429 is a contract: it names the limit, states the budget, and
// gives an exact retry time in both the header and the body.
if (!verdict.allowed) {
  res.set("Retry-After", String(verdict.retryAfterSeconds));
  return res.status(429).type("application/problem+json").json({
    type: "https://api.example.com/problems/rate-limited",
    title: "Rate limit exceeded",
    status: 429,
    detail: `Limit '${verdict.limitName}' is ${verdict.limit} requests per ${verdict.windowSeconds}s`,
    limit: verdict.limitName,
    retryAfterSeconds: verdict.retryAfterSeconds,
    instance: req.path,
    correlationId: req.correlationId,
  });
}
```

Note: the slop version told clients to "try again later" with no number; the corrected version names the limit and states exactly when to retry — BE-306.
