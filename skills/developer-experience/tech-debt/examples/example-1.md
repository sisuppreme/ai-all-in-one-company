# Example 1 — The bare TODO

## Before

```js
// src/checkout/submitOrder.js
async function submitOrder(form) {
  // TODO: add validation later
  const order = buildOrder(form);
  return api.post('/orders', order);
}
```

The hard part is deferred to a comment with no owner, no date, and no tracking — while the task is reported complete. Six months later the comment is still there and invalid orders are reaching the API.

## After

```js
// src/checkout/submitOrder.js
async function submitOrder(form) {
  const errors = validateOrderForm(form); // format/range checks ship now
  if (errors.length) return { ok: false, errors };
  const order = buildOrder(form);
  return api.post('/orders', order);
}
```

```markdown
<!-- docs/tech-debt.md -->
| ID | Location | Quadrant | Interest | Owner | Trigger | Incurred |
|---|---|---|---|---|---|---|
| DEBT-031 | src/checkout/submitOrder.js | deliberate + prudent | Server-side duplicate of the postcode rule can drift from the client rule; one drift incident costs a support round-trip per bad order | DX | 2026-12-15, or next checkout change | 2026-11-21 |
```

The minor remainder (unifying the duplicated postcode rule) is registered with a trigger; the core behavior — validation — is implemented, not deferred. Any marker left in code would read `// TODO(DEBT-031): …`.

## Note

Corrected under DX-086 (markers must reference the register; core functionality is never a TODO) and DX-082 (the entry is complete at birth: location, quadrant, concrete interest, owner, trigger, date).
