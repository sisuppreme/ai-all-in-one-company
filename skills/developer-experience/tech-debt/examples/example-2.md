# Example 2 — The deliberate shortcut, registered

## Before

```js
// src/refunds/calcRefund.js
// Copied from checkout — clean this up later, fine for now.
export function refundTax(amount, rate) { /* same 14 lines as checkout */ }
```

The tax calculation now exists in checkout, invoice, and refund code. The review calls it "fine for now," nothing is written down, and the next tax-rule change updates two copies and misses the third — refunds are calculated at the old rate for a month.

## After

```markdown
<!-- docs/tech-debt.md — entry added in the same PR that merges the copy -->
| ID | Location | Quadrant | Interest | Owner | Trigger | Incurred |
|---|---|---|---|---|---|---|
| DEBT-014 | src/checkout/tax.js, src/invoices/tax.js, src/refunds/calcRefund.js | deliberate + prudent | Every tax-rule change requires the same edit in three places and a three-way review; a missed copy misprices refunds or invoices silently | DX | Next change to any of the three copies | 2026-11-21 |
```

```js
// src/refunds/calcRefund.js
// TODO(DEBT-014): duplicated tax calc — extract to shared module on next touch.
export function refundTax(amount, rate) { /* … */ }
```

The shortcut still ships on schedule — that is what prudent deliberate debt is for — but it is visible, owned, and its trigger ("next change to any copy") fires the extraction automatically instead of relying on memory.

## Note

Corrected under DX-083 (deliberate debt is registered in the same change that incurs it) and DX-085 (interest stated concretely: the triple edit and the silent mispricing risk, not "code is messy").
