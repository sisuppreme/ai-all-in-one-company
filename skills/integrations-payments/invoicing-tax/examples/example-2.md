# Example 2 — Replacing an edited invoice with a credit note

## Before

A customer was charged the annual price on a monthly plan. Support
"fixes" the paperwork directly:

```text
Invoice INV-1042 (issued, paid)
  line: Pro plan — 5900
  → admin edits the line to 4900 and re-sends the PDF
```

The stored invoice now totals 4900, but the provider charged 5900. The
customer's copy, the provider record, and the books disagree, and the
sequence gives no hint that anything was ever corrected.

## After

The issued invoice is never touched; the correction is its own document:

```text
Invoice INV-1042 (issued, paid) — unchanged
  line: Pro plan — 5900        provider charge: 5900 ✓

Credit note CN-0317
  references: INV-1042
  line: price correction — −1000
  reason: charged annual price on monthly plan

Refund of 1000 issued against the original payment (refunds-disputes)
Invoice status and totals now reconcile: 5900 − 1000 = amount kept
```

Anyone auditing later sees the original charge, the correction, and the
reason — as three records, not one silently rewritten one.

Note: corrects IN-067 — an issued invoice is immutable; corrections are credit notes that reference the original invoice number.
