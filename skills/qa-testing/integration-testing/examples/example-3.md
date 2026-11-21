# Example 3 — Missing tenant boundary, corrected to a cross-tenant test

## Before

The invoice endpoints have happy-path tests only: create an invoice, read
it back, list it — always as the owning tenant. Nothing ever asks what a
*different* tenant sees, so when a refactor drops the tenant filter from
the read query, every test stays green while tenants can read each other's
invoices.

## After

```js
test("a tenant cannot read or modify another tenant's invoice", async () => {
  const tenantA = await factories.tenant();
  const tenantB = await factories.tenant();
  const invoice = await factories.invoice({ tenant: tenantA });
  const tokenB = await signIn(tenantB.owner);

  // Direct read: must not surface the record.
  const read = await api.get(`/invoices/${invoice.id}`, tokenB);
  expect([403, 404]).toContain(read.status);

  // List: must not contain it either.
  const list = await api.get("/invoices", tokenB);
  expect(list.body.map((i) => i.id)).not.toContain(invoice.id);

  // Write attempt: rejected, and the record is unchanged.
  const write = await api.patch(`/invoices/${invoice.id}`, { paid: true }, tokenB);
  expect([403, 404]).toContain(write.status);
  const row = await db.query("SELECT paid FROM invoices WHERE id = $1", [invoice.id]);
  expect(row.paid).toBe(false);
});
```

Every tenant-scoped entity gets this case; G-QA-013 fails the build when
one is missing.

Note: corrects QA-027 — tenant and permission boundaries are proven at the integration layer, not assumed from the UI hiding the buttons.
