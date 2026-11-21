# Example 2 — The object-level check a role check cannot replace

## Before

The endpoint checks that the caller is a member in good standing — and then
returns any invoice whose ID is supplied:

```js
app.get('/invoices/:id', requirePermission('invoices:read'), async (req, res) => {
  const invoice = await db.invoices.findById(req.params.id);
  if (!invoice) return res.status(404).end();
  res.json(invoice); // any member can read every customer's invoice
});
```

The function-level check passes. The object-level check does not exist, so
invoice IDs — sequential and guessable — expose the whole ledger. This is
OWASP API1 (broken object-level authorization).

## After

Passing the role check earns the right to ask; ownership decides the answer:

```js
app.get('/invoices/:id', requirePermission('invoices:read'), async (req, res) => {
  const invoice = await db.invoices.findById(req.params.id);
  if (!invoice) return res.status(404).end();

  const user = req.session.user;
  const ownsIt = invoice.customerId === user.id;
  const staffRole = user.role === 'admin' || user.role === 'support';
  if (!ownsIt && !staffRole) {
    audit.denied({ actor: user.id, action: 'invoices:read', target: invoice.id });
    return res.status(404).end(); // 404, not 403: do not confirm the record exists
  }
  res.json(invoice);
});
```

Another customer's invoice is indistinguishable from a missing one, and
the attempt is logged.

Note: corrects BE-124 — function-level and object-level authorization are separate checks; passing one never implies the other.
