# Example 1 — One generic 500 replaced by classified problem details

## Before

```js
// Every failure — bad input, missing record, dead database — comes
// back as the same 500. Clients cannot react; operators cannot tell
// the failures apart from the response alone.
app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).json({ error: "Something went wrong" });
});
```

## After

```js
// Typed errors carry their class; the single handler maps each class
// to a problem-details body with a distinct type and the right status.
class ValidationError extends Error {
  constructor(fields) { super("Validation failed"); this.fields = fields; }
}
class NotFoundError extends Error {}
class DependencyError extends Error {
  constructor(service) { super(`${service} unavailable`); this.service = service; }
}

app.use((err, req, res, next) => {
  const correlationId = req.correlationId;
  if (err instanceof ValidationError) {
    return res.status(422).type("application/problem+json").json({
      type: "https://api.example.com/problems/validation",
      title: "Validation failed", status: 422,
      detail: "One or more fields are invalid",
      instance: req.path, correlationId, errors: err.fields,
    });
  }
  if (err instanceof NotFoundError) {
    return res.status(404).type("application/problem+json").json({
      type: "https://api.example.com/problems/not-found",
      title: "Not found", status: 404, instance: req.path, correlationId,
    });
  }
  if (err instanceof DependencyError) {
    return res.status(503).type("application/problem+json").json({
      type: "https://api.example.com/problems/dependency",
      title: "A dependency is unavailable", status: 503,
      detail: "Retry after a short delay", instance: req.path, correlationId,
    });
  }
  logger.error({ correlationId, err }); // full exception, server-side only
  return res.status(500).type("application/problem+json").json({
    type: "https://api.example.com/problems/internal",
    title: "Internal error", status: 500, instance: req.path, correlationId,
  });
});
```

Note: the slop version returned one identical 500 for every failure; the corrected version classifies errors by who can fix them and gives each class a distinct problem type and status — BE-286, BE-289.
