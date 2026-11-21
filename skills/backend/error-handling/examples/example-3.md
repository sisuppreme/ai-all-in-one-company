# Example 3 — Stack trace in the response replaced by generic-out, full-in logging

## Before

```js
// The framework's debug error page ships to production: the client
// receives the stack trace, the SQL, and the file paths.
app.use((err, req, res, next) => {
  res.status(500).send(`<pre>${err.stack}</pre>`);
  // "Error: column users.emial does not exist
  //    at Query.run (/srv/app/node_modules/orm/query.js:118:4) ..."
});
```

## After

```js
// The client receives a generic problem carrying only a correlation
// ID; the full exception and request context go to structured logs
// and error tracking under that same ID.
app.use((err, req, res, next) => {
  const correlationId = req.correlationId;
  logger.error({
    correlationId,
    message: err.message,
    stack: err.stack,
    path: req.path,
    userId: req.user?.id,
  });
  errorTracking.capture(err, { correlationId });
  res.status(500).type("application/problem+json").json({
    type: "https://api.example.com/problems/internal",
    title: "Internal error",
    status: 500,
    instance: req.path,
    correlationId,
  });
});
```

Note: the slop version leaked the stack trace and SQL to the client; the corrected version returns a generic problem with a correlation ID and logs the full exception server-side under that ID — BE-284, BE-285.
