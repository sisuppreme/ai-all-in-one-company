# Example 1 — Object access scoped to the owner

## Before

```js
// GET /invoices/:id — any authenticated user can read any invoice
app.get('/invoices/:id', requireAuth, async (req, res) => {
  const invoice = await db.invoices.findById(req.params.id);
  res.json(invoice);
});
```

## After

```js
// Ownership is resolved from the authenticated principal, never the request
app.get('/invoices/:id', requireAuth, async (req, res) => {
  const invoice = await db.invoices.findOne({
    id: req.params.id,
    ownerId: req.user.id, // from the verified session, not the request body
  });
  if (!invoice) return res.status(404).json({ error: 'not_found' });
  res.json(invoice);
});
```

Note: demonstrates SE-042 — an object ID is a claim; the server authorizes it against the caller's ownership (API1/BOLA).
