# Example 1 — A price edit that persists through the service layer

## Before

The admin handler updates local state and declares success. The database —
and the storefront — never change:

```js
// admin client component: no request is sent
function savePrice(product, newPrice) {
  product.price = newPrice;
  showToast('Price saved');
}
```

Staff "fix" prices all week; customers keep paying the old ones.

## After

The admin route calls the same product service the storefront reads from,
and confirms only after reading the persisted value back:

```js
app.patch('/admin/products/:id/price', requireStaffRole('catalog'), async (req, res) => {
  const before = await products.getById(req.params.id);

  // the domain service: same validation, cache invalidation, and events
  // as any other price change in the product
  const updated = await products.changePrice(req.params.id, req.body.price, {
    actor: req.staff.id,
  });

  await audit.record({
    actor: req.staff.id, action: 'product.price.change',
    target: req.params.id,
    before: { price: before.price }, after: { price: updated.price },
    at: new Date(),
  });

  res.json(updated); // the toast fires on this response, not before it
});
```

Reload the admin view or open the storefront anonymously: both show the
new price, because there was only ever one write path.

Note: corrects BE-161 — admin actions call the same domain services as the product; no parallel write path.
