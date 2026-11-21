# Example 3 — Tokens and TODOs in the first commit

Demonstrates PM-002: tokens are variables replaced at generation time, never content that ships.

## Before

A project is scaffolded by copying the template repository directly (no generator run). Its first commit contains:

```markdown
# Contributing to {{project_name}}

Thanks for helping improve {{project_name}}! TODO: add the real
maintainer contact here before launch.

## Support

TODO: fill in the support email once we decide it.
```

The tokens were never substituted — a GitHub template copy cannot substitute variables — and the TODOs were committed as if they were content.

## After

Generation runs through the generator with a complete variable set:

```bash
cookiecutter project-template/ \
  project_name="Fieldnotes API" \
  owner="Platform Team" \
  support_email="support@fieldnotes.example"   # illustrative value only
```

Generation fails outright if any declared variable lacks a value. The emitted CONTRIBUTING.md reads "Contributing to Fieldnotes API" with the named maintainer contact, and gate G-PM-002 confirms the result before the first commit:

```bash
grep -rn '{{' fieldnotes-api/        # no hits
grep -rn 'TODO\|FIXME' fieldnotes-api/   # no hits
```

No tokens, no draft markers — the scaffold that ships is the scaffold that was generated.
