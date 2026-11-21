# Example 2 — Fail-closed authorization

Note: demonstrates SE-005 — an exception in an authorization path denies the action (BAN-SE-002, DET-CODE-005).

## Before

```js
// If the access check throws (database hiccup, bad token), the catch block
// swallows it and the document is served anyway — the failure opens the door.
app.get("/documents/:id", async (req, res) => {
  const doc = await loadDocument(req.params.id);
  try {
    await checkAccess(req.user, doc);
  } catch {
    // ignore — check is best-effort
  }
  res.json(doc);
});
```

## After

```js
// The check runs first, and any failure — denial or exception — stops the
// request. The error is logged as a security event (SE-009).
app.get("/documents/:id", async (req, res) => {
  const doc = await loadDocument(req.params.id);
  try {
    await checkAccess(req.user, doc);
  } catch (err) {
    logSecurityEvent("authorization_check_failed", { user: req.user.id, doc: doc.id });
    return res.status(403).json({ error: "Forbidden" });
  }
  res.json(doc);
});
```
