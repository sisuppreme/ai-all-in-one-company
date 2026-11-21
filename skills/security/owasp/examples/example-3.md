# Example 3 — Generic production errors

Note: demonstrates SE-007 — clients get a generic message and a correlation ID, never internals (BAN-SE-004, DET-INF-021).

## Before

```js
// The raw exception — stack trace, SQL text, file paths — is sent to the
// client, and debug mode is on in every environment, including production.
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.message, stack: err.stack });
});
// config: DEBUG = true (all environments)
```

## After

```js
// Full detail goes to the server log under a correlation ID the user can
// quote in a support report; the response itself reveals nothing internal.
// Debug mode is off in production, enforced by environment config (SE-011).
app.use((err, req, res, next) => {
  const id = req.correlationId;
  logger.error({ id, err });
  res.status(500).json({ error: "Internal error", id });
});
// config: DEBUG = (NODE_ENV !== "production")
```
