# Example 2 — Forwarded-header keying replaced by account keying

## Before

```js
// The limiter keys on a header the client fully controls. Rotating
// the header value mints a fresh budget on every request.
function limiterKey(req) {
  return req.headers["x-forwarded-for"] ?? "unknown";
}

app.use((req, res, next) => {
  if (limiter.hit(limiterKey(req)) > 100) {
    return res.status(429).json({ error: "Too many requests" });
  }
  next();
});
```

## After

```js
// The key is what the caller cannot forge: the authenticated account
// ID. IP keying (for unauthenticated routes) uses the address from
// the trusted proxy chain, never the raw header.
function limiterKey(req) {
  if (req.user) return `account:${req.user.id}`;
  return `ip:${req.ip}`; // Express resolves req.ip via the configured trust proxy
}

app.use((req, res, next) => {
  const verdict = limiter.hit(limiterKey(req), ROUTE_CLASS_LIMITS[req.routeClass]);
  if (!verdict.allowed) {
    res.set("Retry-After", String(verdict.retryAfterSeconds));
    return res.status(429).json({
      type: "https://api.example.com/problems/rate-limited",
      title: "Rate limit exceeded", status: 429,
      limit: verdict.limitName, retryAfterSeconds: verdict.retryAfterSeconds,
    });
  }
  next();
});
```

Note: the slop version keyed limits on a spoofable header; the corrected version keys on the authenticated account or the verified proxy-chain IP — BE-302.
