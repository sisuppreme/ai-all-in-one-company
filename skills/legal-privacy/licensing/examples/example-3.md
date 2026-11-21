# Example 3 — The copyleft library nobody tiered

## Before

```markdown
## Component inventory (excerpt)

| Component | License | Notes |
|---|---|---|
| report-engine | AGPL | Popular, works well — added by the reporting feature |
```

A strong-copyleft component entered the codebase with no tier decision. Nobody recorded which distribution model it was judged against, so the same row silently covers both the hosted service and a planned self-hosted installer, where the obligations differ.

## After

```markdown
## Component inventory (excerpt)

| Component | Version | Origin | SPDX license | Tier (hosted) | Tier (distributed installer) | Decision |
|---|---|---|---|---|---|---|
| report-engine | 7.2.1 | Package registry | AGPL-3.0-only | Review | Forbidden | Hosted use approved by named reviewer, 2026-11-21: network-copyleft source-offer duty implemented as a real source download in the product's legal page (LG-108). Installer build excludes report-engine; the CI scan for the installer profile fails if it appears (G-LG-051). Re-review on any change of distribution model. |
```

The tier is decided per distribution model, the triggered duty is implemented rather than linked away, and the forbidden profile is enforced by the scan instead of by memory.

## Note

Corrected under LG-104: a copyleft license's tier is decided against the actual distribution model — the same library can be allowed in a hosted service and forbidden in a shipped artifact, and each decision is recorded with its reasoning (LG-105).
