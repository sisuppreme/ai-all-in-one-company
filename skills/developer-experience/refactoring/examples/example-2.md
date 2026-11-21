# Example 2 — The behavior change hiding in a "refactor"

## Before

```text
commit a91c3f2  "refactor: tidy pricing module"

 src/pricing/price.js        | 64 +++++++++++++--------------
 tests/pricing.test.js       |  2 +-
 2 files changed
```

```diff
-  return Math.floor(total * 100) / 100;   // truncate to cents
+  return Math.round(total * 100) / 100;   // round to cents

-  expect(price({ net: 19.995 })).toBe(19.99);
+  expect(price({ net: 19.995 })).toBe(20.00);
```

The commit is labeled a refactor, but it changes what customers are charged — and edits the test so the suite agrees. Review approves it as a tidy-up; the rounding change ships with no fix review, no changelog entry, and no one able to say when prices changed.

## After

```text
commit 41bd07e  "refactor: extract toCents helper in pricing module"
  src/pricing/price.js only — the truncation logic moves verbatim;
  tests untouched; suite green before and after.

commit 9c2e551  "fix: round prices to nearest cent instead of truncating"
  src/pricing/price.js        | 2 +-
  tests/pricing.test.js       | 2 +-
  CHANGELOG.md                | 1 +
```

The structural move and the behavior change are separate commits wearing separate hats: the fix is reviewed as a pricing decision, its test change is expected and visible, and the changelog records when charged prices changed.

## Note

Corrected under DX-101 (a change to observable behavior is not a refactoring and is renamed as what it is), DX-103 (two hats — structure and behavior in separate commits), and DX-106 (tests are read-only inside a refactoring change; a test that must change signals a behavior change).
