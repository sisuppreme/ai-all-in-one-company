# Example 2 — Cutover on a README

## Before

```markdown
The new pricing engine implements the rules in docs/pricing.md, which
describes the legacy engine's behavior. The implementation was reviewed
against the document and matches it. Routing 100% of pricing traffic
to the new engine on Friday.
```

"Equivalent" is asserted from a document written about the legacy system, not from the legacy system's observed behavior. The document never mentioned that totals are rounded per line item rather than per invoice, so the new engine disagrees with every multi-line invoice it prices — discovered from customer complaints after cutover.

## After

```markdown
Characterization set: 412 recorded production-shaped pricing cases
(inputs + legacy outputs), stored in tests/parity/pricing/.

IMPL=legacy npm run test:parity -- pricing   → 412 passed
IMPL=new    npm run test:parity -- pricing   → 409 passed, 3 diffs

Diffs (all recorded as intended changes, decider: product owner, 2026-11-18):
- Case 087: per-line rounding replaces per-invoice rounding (documented
  in the changelog as a behavior change).
- Cases 204, 311: expired-coupon error now names the coupon code.

Parallel run: one week of shadow calls in production, diff rate 0 after
the intended changes were excluded. Cutover approved.
```

The replacement was built to match the legacy behavior as recorded by tests, the parallel run compared real outputs, and every remaining difference is an enumerated, owned decision rather than a surprise.

## Note

Corrected under DX-122 and DX-125: characterization tests pin legacy behavior before anything moves, and old and new run in parallel with compared outputs before cutover.
