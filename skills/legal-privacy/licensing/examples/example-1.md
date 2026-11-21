# Example 1 — The snippet with no license

## Before

```markdown
## Component inventory (excerpt)

| Component | License | Notes |
|---|---|---|
| date-range-picker snippet | — | Copied from a blog post, it's publicly posted so fine to use |
| hero photo (dashboard) | — | Downloaded from a free-images thread, no license shown |
```

Two components ship with no license recorded at all, waved through on the reasoning that public availability is permission. There is nothing to scan against the policy and nothing to generate notices from.

## After

```markdown
## Component inventory (excerpt)

| Component | Version | Origin | SPDX license | Tier (hosted) | Adopted | Decision |
|---|---|---|---|---|---|---|
| date-range-picker snippet | n/a | Personal blog post, no license statement found | NOASSERTION | Forbidden | — | Replaced with `date-utils` (`MIT`) from the package registry, 2026-11-21 |
| hero photo (dashboard) | n/a | Stock library product page | LicenseRef-Stock-Standard | Review | 2026-11-21 | Transfer to client rebuild not permitted by terms — replaced with project-owned photography for the client build (LG-112) |
```

The snippet is replaced because no license means all rights reserved, and the photo's terms are read and recorded before it ships anywhere.

## Note

Corrected under LG-103: "no license found" is forbidden-tier — default copyright applies, so the component is replaced or the rights holder's written permission is filed; public availability is never permission.
