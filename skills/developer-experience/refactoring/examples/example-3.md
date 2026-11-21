# Example 3 — Characterization tests before touching legacy billing

## Before

```text
Task: "Billing module is a mess — refactor it."
Coverage of src/billing/ at base: 0 test files.
```

The agent reads the module carefully, splits the 400-line `settle()` function into six smaller ones over a day, and reports "behavior preserved." There is no suite to contradict that claim — the first real test is the next production invoice run, where a reordered rounding step changes totals for multi-currency accounts.

## After

```text
commit 1f8a2c0  "test: characterize current billing settle() behavior"
  tests/billing.characterization.test.js  (+38 tests, no source changes)
```

```js
// tests/billing.characterization.test.js
// Pins CURRENT behavior of settle(), including quirks — these tests
// describe what the code does today, not what it ideally should do.
test('multi-currency order rounds per line, then sums', () => {
  expect(settle(multiCurrencyOrder).total).toBe(412.07); // observed output
});
test('zero-rate category still emits a tax line of 0.00', () => {
  expect(settle(zeroRateOrder).taxLines).toEqual([{ rate: 0, amount: 0 }]);
});
```

```text
commit 77b3d91  "refactor: extract per-line settlement from settle()"
commit c04e6aa  "refactor: rename settle steps to invoice vocabulary"
  — suite (incl. the 38 characterization tests) green before and after
    each step; the reordered-rounding mistake now fails a test in the
    step that introduces it, not in production.
```

The net is built before the structure moves: current behavior — quirks included — is pinned in its own commit, and every later step is checked against it.

## Note

Corrected under DX-102 (no safety net, no refactoring: characterization tests pin current behavior first and land in a preceding commit before any restructuring begins).
