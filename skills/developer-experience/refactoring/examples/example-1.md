# Example 1 — Extract Function under a green suite

## Before

```js
// src/invoice/buildInvoice.js — one 90-line function; the tax block is
// written inline, and the suite has never been run on this branch.
export function buildInvoice(order) {
  // ... 40 lines of line-item assembly ...
  let tax = 0;
  for (const line of lines) {
    const rate = line.category === 'food' ? 0.05 : 0.2;
    tax += round2(line.net * rate);
  }
  // ... 40 more lines of totals, discounts, formatting ...
}
```

The agent restructures the whole function in one sitting — extraction, renames, and a discount fix it noticed along the way — and runs the tests once at the end. Three tests fail, and nothing in the single giant diff says which of the many changes broke them.

## After

```text
Step 0: npm test on base            → 212 passed, 0 failed (recorded)
Step 1: commit "refactor: extract calculateTax from buildInvoice"
        — one catalog transformation, nothing else moves
        npm test                    → 212 passed, 0 failed
```

```js
// src/invoice/tax.js
export function calculateTax(lines) {
  let tax = 0;
  for (const line of lines) {
    const rate = line.category === 'food' ? 0.05 : 0.2;
    tax += round2(line.net * rate);
  }
  return tax;
}
```

```js
// src/invoice/buildInvoice.js
import { calculateTax } from './tax.js';
// ... line-item assembly unchanged ...
const tax = calculateTax(lines);
// ... totals and formatting unchanged; the discount fix is a separate,
// later change wearing the other hat ...
```

Each step is one named transformation with the suite green on both sides of it; when a step does go red, the diff to inspect is one extraction, not ninety lines.

## Note

Corrected under DX-104 (small, named steps with the suite run between them) and DX-102 (the suite is green and recorded on the base commit before the first structural step).
