# Example 2 — The security file nobody missed

Demonstrates PM-001: every mandated file is present, or recorded not-applicable with a reason.

## Before

A new private project is generated. Three weeks later, a reviewer asks for the security reporting address and finds there is no SECURITY.md — and no record of why. The generator had quietly skipped it because the template author considered it "only for open source," and the gap surfaced only when an external reporter needed it. Nothing in the generation record mentions the file at all.

## After

The same generation, run under this skill, produces a generation record:

```markdown
## Generation record — project: fieldnotes-api — template v2.3.0

Emitted: README.md, LICENSE, CONTRIBUTING.md, SECURITY.md, CODEOWNERS,
.gitignore, dependabot.yml, docs/adr/, .github/ISSUE_TEMPLATE/,
.github/PULL_REQUEST_TEMPLATE.md, CHANGELOG.md, DECISIONS.md, …

Not applicable:
- CODE_OF_CONDUCT.md — private internal project (PM-010); revisit if the
  repo is ever made public.
- GOVERNANCE.md — private internal project (PM-010); same revisit trigger.
- SUPPORT.md — private internal project (PM-010); support route is the
  internal tracker named in SECURITY.md.
```

SECURITY.md is emitted (it applies to private projects too), and each genuinely inapplicable file is absent *with a stated reason and a revisit trigger* — the absence is a decision, not an oversight.
