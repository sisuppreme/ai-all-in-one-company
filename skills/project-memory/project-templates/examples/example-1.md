# Example 1 — The README that arrived with customers

Demonstrates PM-003: templates ship structure and prompts, never invented facts.

## Before

The generated README for a project created this morning opens with:

```markdown
# Ledgerly

Trusted by 10,000+ teams worldwide.

> "Ledgerly cut our month-end close from three days to four hours."
> — Sarah M., Finance Manager, Northwind Retail

> "The best invoicing tool we have ever used." — ★★★★★
```

Ledgerly has no customers yet. The quotes, the user count, and Sarah M. were written into the template as "realistic sample content" so the README would look finished.

## After

The same template section, corrected:

```markdown
# {{project_name}}

<!-- Fill in: one sentence stating what this project is and who it is for,
     from fact-sheet.md. Do not add claims the fact sheet does not carry. -->

## What users say

<!-- Real testimonials only: each quote needs a named, real customer and a
     source record the business can produce (see the real-content skill).
     Until one exists, delete this section — an absent section is honest,
     an invented one is a blocker. -->
```

The generated project now starts with an honestly empty social-proof section instead of fabricated proof.
