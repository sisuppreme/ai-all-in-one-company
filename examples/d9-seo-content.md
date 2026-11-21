# D9 Example — Landing Page Copy and Metadata That Invented Their Proof

## Scenario

D9 owns the landing page from the D3 example once the structure ships:
title and description, body copy, and structured data. The page must be
findable and must convert — using only claims the product can back.

## Before

```html
<title>Best Project Tool | Project Management Software | #1 Planning App for Teams</title>
<meta name="description" content="The world's leading project tool — free forever,
  unlimited everything. Sign up in seconds and transform your workflow today!">
```

```markdown
Body copy: "In today's fast-paced world, teams need a powerful, seamless,
robust solution to unlock productivity and take collaboration to the next
level. Join 10,000+ happy teams who trust us."

> "Fieldnotes changed how our whole company works." — Sarah M., Operations Lead
```

```json
{ "@type": "Product", "name": "Fieldnotes",
  "aggregateRating": { "ratingValue": "4.9", "reviewCount": "2314" },
  "offers": { "price": "0", "priceCurrency": "USD" } }
```

The product is a paid plan after a trial; there are no public reviews;
the pricing page says $12 per seat.

## What the skills caught

- **BAN-CO-011 — Keyword-stuffed title**: three keyword phrases welded
  together, violating **CO-024 — Titles state topic and offer plainly**
  and **CO-021 — One page, one primary intent** (**DET-CON-022 — Title
  and meta description mismatch**).
- **BAN-CO-013 — Meta description advertising an absent offer**: "free
  forever, unlimited everything" describes a product that does not
  exist. **CO-027 — Descriptions promise only what the page delivers**;
  the description-to-page promise check is **G-CO-013**.
- **BAN-CO-051 — Invented testimonial** and **BAN-CO-052 — Unsourced
  statistic**: the quote and "10,000+ happy teams" were written by the
  copy generator, not collected from anyone — **DET-CON-010 —
  Fabricated testimonials**, **DET-CON-011 — Fabricated or unsourced
  statistics**. **CO-106 — No invented numbers**, **CO-107 — No invented
  social proof**; the claim-trace audit **G-CO-061** finds no source for
  either claim in the fact sheet.
- **BAN-CO-055 — Hedge stack** plus the AI vocabulary cluster ("seamless,
  robust, unlock, take … to the next level") — **DET-CON-009 — Hedge
  stacks**, **DET-CON-007 — AI vocabulary cluster**, caught by the
  cluster-term editing pass **CO-103** and the competitor-verbatim test
  **CO-101**: swap in any competitor's name and the paragraph still
  "works", which means it says nothing.
- **BAN-CO-083 — Fabricated review markup**: a 4.9 rating from zero
  reviews — **DET-CON-024 — Structured data contradicts the page**,
  **DET-CON-013 — Fake review patterns**. **CO-166 — Review markup
  follows real reviews**; there are none, so there is no review markup.
- The `"price": "0"` contradicts the pricing page: **CO-167 — Prices
  match everywhere** (**DET-CON-016 — Price mismatch**). **CO-161**:
  JSON-LD is generated from the same data that renders the page, never
  hand-maintained beside it (**BAN-CO-084**).

## After

```html
<title>Fieldnotes — Team planning boards for small teams</title>
<meta name="description" content="Fieldnotes turns a small team's scattered
  tasks into one shared weekly plan. Free for up to five people; paid plans
  from $12 per seat per month.">
```

Body copy now says what the product does, in words a competitor could
not reuse: the weekly board, owners on every task, the Friday review
view. The testimonial block and the team counter are gone — **CO-127 —
Cut, don't soften**: an invented quote with "results may vary" added is
still an invented quote. When a real customer quote exists, it will be
added with the customer's name, role, and permission on record in the
evidence register (**G-CO-063**).

Structured data is generated from the page's own data at build time
(**CO-161**) and contains only what the page shows (**CO-162**): the
product name, the real starting price, and the trial terms. No
`aggregateRating` — the markup-vs-visible diff **G-CO-082** passes
because there is nothing in the markup that is not on the page.

## Skills used

- [on-page-seo](../skills/seo-content/on-page-seo/SKILL.md)
- [copywriting](../skills/seo-content/copywriting/SKILL.md)
- [real-content](../skills/seo-content/real-content/SKILL.md)
- [structured-data](../skills/seo-content/structured-data/SKILL.md)
- [technical-seo](../skills/seo-content/technical-seo/SKILL.md)
