# Example 2 — A reversal done as a superseding pair

## Before

ADR 0002 chose a shared-schema tenancy model. Load testing later shows one
tenant's reporting load degrading all others, so the team moves that tenant
to its own database — and edits ADR 0002's decision text to describe the
hybrid model, as if it had always said that. The original reasoning, and the
fact that it failed, are gone.

## After

ADR 0002 is left untouched except its status line, changed in the same
commit to:

```markdown
Status: superseded by 0011
```

New record:

```markdown
# 0011 — Move reporting-heavy tenants to dedicated databases (bridge model)
Status: accepted; supersedes 0002
Context: ADR 0002 chose shared schema for all tenants. Load test LT-14
(2026-11) showed tenant T-07's reporting queries degrading p95 latency for
all tenants past the agreed budget — the noisy-neighbor risk 0002 accepted
has materialized.
Decision: tenants whose reporting load exceeds the recorded threshold move
to dedicated databases, routed by the tenant catalog; all others stay
pooled. …
```

Both records now tell the truth: what was decided, why it changed, and where
to read next.

Note: corrects AR-245 and AR-246 — accepted ADRs are immutable, and a reversal is a new ADR that supersedes the old one, with the old record's status updated in the same commit.
