# Example 3 — Replacing a copied benchmark target with an own-baseline target

## Before

```text
Quarterly planning doc
  Goal: "Reach 40% activation — the benchmark for top SaaS products
  (source: a growth blog's survey of other companies)."
  The team also adopts the same article's suggested activation
  milestone ("complete profile + invite a teammate") as the
  definition, untested on this product.

  This product's core value is a solo reporting workflow; most
  retained users never invite a teammate in their first month.
```

The target and the milestone both describe other products. The metric will punish the team for value their users actually receive.

## After

```text
Quarterly planning doc (revised)
  Candidate milestone from the article: treated as a hypothesis.
  G-CX-043 validation on this product's data: users who invited a
  teammate in week 1 retained no better than users who did not;
  users who shared a first report retained measurably better.
  → Milestone rejected; activation stays report_shared ≤ 7 days.

  Baseline (own data, trailing 3 months, reconciled per G-CX-041):
  34.1% of signups activate within 7 days.
  Target: 38% by end of quarter — set from the baseline plus the
  measured effect of the onboarding change already shipped in
  test, recorded with the computation (G-CX-044).
```

## Note

Corrects CX-087 and CX-088: another product's milestone is a hypothesis to validate or reject on your own retention data, and every target is computed from your own measured baseline — never copied from a benchmark.
