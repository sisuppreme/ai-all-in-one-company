# Example 1 — The policy copied from another product

## Before

```markdown
## Privacy Policy (excerpt, live page)

TaskBoard collects the following information about you: your name, email
address, and patient health records. We share your data with our trusted
partners at HealthCloud Systems. We never collect location data.
```

The text came from a template written for a healthcare product. TaskBoard holds no health records and has no HealthCloud partnership — and the excerpt omits what TaskBoard actually stores: workspace content, billing identifiers, and product-analytics events. It also claims no location data is collected while the mobile check-in feature stores GPS coordinates.

## After

```markdown
## Privacy Policy (excerpt, v2.3, effective 2026-11-21)

Generated from: data inventory DI-2026-11 (RoPA rows R-01…R-09) and
processor register PR-2026-11. Diff gate G-LG-031: 0 mismatches.

TaskBoard collects: account data (name, email), workspace content you
create, billing identifiers held by our payment processor, and — only
after your consent — product-analytics events. The check-in feature
records the GPS coordinates of a check-in when you use it; coordinates
are retained for 90 days (RoPA row R-07). Processors: see the register
table below; this list is rendered from the processor register, not
maintained separately.
```

Every practice named in the notice now traces to a register row, the location collection the product really performs is stated instead of denied, and the processor list is the register's own data, so the diff gate can fail the release if the two ever diverge.

## Note

Corrected under LG-061: legal documents are generated from this product's own data inventory, processor register, and feature list — never copied from a template or another product's documents.
