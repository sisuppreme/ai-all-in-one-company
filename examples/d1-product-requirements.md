# D1 Example — Requirements, Fact Sheet, and Acceptance Criteria for a Billing Feature

## Scenario

A two-person SaaS team is adding team plans with per-seat billing. Before any
code is written, D1 produces the requirements set, the product fact sheet, the
acceptance criteria for the first story, and the release scope. This is the
end-to-end D1 pass: every downstream department will build against these
documents, so errors here become code.

## Before

Requirements excerpt, as first drafted:

```markdown
REQ-1: The system shall provide a fast, intuitive billing experience that
handles plan changes, seat updates, prorations, refunds, and tax invoices.
REQ-2: The system shall use a modern payment library.
REQ-3: Checkout shall be quick and seamless for all users.
```

Fact sheet excerpt:

```markdown
- Teams waste an average of 6 hours per week on manual billing admin.
- 98% of customers say billing is their top frustration.
- Pricing: Pro plan, $12 per seat per month.
```

Acceptance criteria for "Admin changes plan": one scenario — plan changes,
success message shows. Scope list: 14 Must items, no Won't-have section.
Marketing draft already promises "automatic tax invoices in every country."

## What the skills caught

- **BAN-PR-032 — The adjective requirement** and **PR-063 — Vague terms need
  numbers**: "fast", "intuitive", "quick", "seamless" are untestable. Caught
  by the requirement lint, **G-PR-031**.
- **BAN-PR-031 — The compound requirement**: REQ-1 bundles five obligations
  (plan changes, seats, prorations, refunds, invoices) into one sentence,
  violating **PR-061 — One obligation per requirement**.
- **BAN-PR-034 — Solution smuggled in as a need**: REQ-2 names a library
  instead of the need (reliable card charging), violating **PR-064**.
- **BAN-PR-062 — The invented statistic**: "6 hours per week" and "98%" have
  no source. **PR-123 — Every number traces** and **PR-126 — Unknown means
  "not measured"** require both to be removed or marked unmeasured. This is
  detection parameter **DET-CON-011 — Fabricated or unsourced statistics**.
- **BAN-PR-052 — Happy-path only**: no failure criteria at all, violating
  **PR-104 — Failure cases are mandatory** (card declined, seat count below
  current usage, mid-cycle downgrade).
- Scope: **PR-142 — Non-empty Won't-have list** fails, and the marketing line
  promises invoicing the scope never validated — **DET-CON-028 — Promises
  with no backing process**, caught by the copy-to-scope sweep **G-PR-075**.

## After

```markdown
REQ-1: When an admin submits a plan change, the system shall confirm the
new plan and the exact prorated amount before charging. (Must)
REQ-2: When a payment fails, the system shall keep the current plan active
for 72 hours and notify the admin by email within 15 minutes. (Must)
REQ-3: The system shall charge cards through a PCI-DSS SAQ-A payment
provider so card data never touches our servers. (Must)
```

Fact sheet: both statistics deleted; the sheet records "Billing admin time:
not measured" and the price exactly as configured in billing (**PR-130**).
Acceptance criteria, in Gherkin (**PR-101**), now include the failure case:

```gherkin
Scenario: Card declined on plan change
  Given an admin on the Pro plan
  When the plan change is submitted and the provider declines the card
  Then the plan remains Pro, no charge is recorded,
  and the admin sees the decline reason and a retry action
```

Scope gains a Won't-have list ("No tax invoicing outside the provider's
supported countries in this release"), and the marketing line is cut to
match — the promise now traces to a Must item (**PR-143**, **PR-149**).

## Skills used

- [requirements-writing](../skills/product-requirements/requirements-writing/SKILL.md)
- [fact-sheet](../skills/product-requirements/fact-sheet/SKILL.md)
- [acceptance-criteria](../skills/product-requirements/acceptance-criteria/SKILL.md)
- [scope-control](../skills/product-requirements/scope-control/SKILL.md)
