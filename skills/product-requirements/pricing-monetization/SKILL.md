# pricing-monetization

## Metadata

- **Owner department:** D1 Product & Requirements (PR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://stripe.com/resources/more/saas-pricing-and-packaging-strategy
- **Depends on:** competitive-analysis, unit-economics, fact-sheet
- **Feeds into:** fact-sheet, roadmapping

## When to use / Do NOT use

- **Use when:** setting or changing prices, designing tiers or a free plan, launching a promotion, or auditing why the prices on different surfaces disagree.
- **Do NOT use when:** the question is whether the business model works at all (use unit-economics first), or the prices are one-off negotiated quotes with no published surfaces (record them in the fact sheet instead).

## Rules

1. **PR-201 — Value metric first.** Before any price is set, the value metric is chosen and written down: the quantity the customer pays more of as they receive more value (seats, projects, usage, revenue processed). Prices set before the value metric exists are provisional and marked as such.
2. **PR-202 — Model follows the metric.** The pricing model (per seat, tiered flat rate, usage-based, or hybrid) is chosen because it fits the value metric, and the fit is stated in one sentence in the pricing document.
3. **PR-203 — Tiers graduate naturally.** Tier boundaries sit where customers actually grow into the next level of value; a customer should hit a tier limit because they succeeded, not because an arbitrary feature was fenced off.
4. **PR-204 — One configuration, every surface.** Prices are implemented as billing-provider objects (products, prices, subscriptions). The pricing page, checkout, invoices, and emails render from that single configuration. There is no second price list anywhere.
5. **PR-205 — No hard-coded prices.** No price, plan name, or billing term is typed by hand into page copy, blog posts, emails, ads, or help articles. Surfaces that cannot render from the configuration link to the pricing page instead of restating the number.
6. **PR-206 — Fact sheet mirrors the configuration.** The fact sheet's price entries are copied from the billing configuration, and any conflict between the sheet and the configuration is resolved in favor of the configuration, with the sheet corrected the same day.
7. **PR-207 — Free tier has limits and a path.** A free tier states explicit limits (quantity, time, or capability) and a designed conversion path to paid. An unlimited free tier with no conversion design is a pricing defect.
8. **PR-208 — Promotions carry dates and terms.** Every discount or promotion shows its start, its end, and its terms wherever the promotional price appears. An undated promotional price is treated as an error and removed.
9. **PR-209 — Tier splits come from the value metric.** Which features sit in which tier is decided from the value metric and the upgrade path. Copying a competitor's three price points or feature fences without that derivation is not a pricing decision.
10. **PR-210 — No-provider fallback.** Where a project has no billing provider (quoted or brochure pricing), the fact sheet is the single price source of truth, every surface copies from it verbatim, and the consistency gate (G-PR-101) runs against the sheet instead of the provider.

## BAN list

- **BAN-PR-101 — Hand-typed price in copy.** Banned: typing a price into any page, post, email, or ad instead of rendering it from the billing configuration (or, under PR-210, copying it verbatim from the fact sheet). Defeats: DET-CON-016. Bad: a blog post announces "Pro is just $29/month" six weeks after the price moved to $24 in the billing configuration; the blog, the pricing page, and checkout now state three different prices. Instead: render from the configuration, or link to the pricing page without restating the number (PR-205). Severity: BLOCK.
- **BAN-PR-102 — Undated promotion.** Banned: a discount, launch offer, or sale price shown without visible start/end dates and terms. Defeats: DET-CON-018. Bad: the homepage banner still reads "Launch offer — 50% off your first year" fourteen months after launch, with no end date anywhere. Instead: every promotion carries its dates and terms at the point of display (PR-208). Severity: BLOCK.
- **BAN-PR-103 — Invented price.** Banned: publishing a price, plan, or discount that exists in no billing configuration and no fact-sheet entry — created for one landing page or one ad. Defeats: DET-CON-016. Bad: a paid-search landing page offers a "Starter plan, $9/month" that checkout has never heard of; buyers who click through are charged the $15 entry plan. Instead: create the price in the configuration first, then advertise it (PR-204). Severity: BLOCK.
- **BAN-PR-104 — Unlimited free tier.** Banned: a free tier with no stated limit on quantity, time, or capability and no conversion path. Defeats: DET-CON-028. Bad: "Free forever — unlimited projects, unlimited seats" is published while no scope item, budget, or policy backs the unlimited commitment. Instead: state the limits and design the upgrade path before the tier is announced (PR-207). Severity: WARN.

## Gates

- **G-PR-101 — Price-consistency scan.** Verifies: PR-204, PR-205, PR-206. Check (automated): extract every price and plan mention across the site (for example `grep -rEo '\$[0-9]+(\.[0-9]{2})?/(mo|month|yr|year)' site/ | sort | uniq -c`) and diff the set against the billing provider's active price list (or the fact sheet under PR-210). Pass: every published price matches exactly one configured price, and every plan name matches. Fail: block shipment. Recorded in: progress.md.
- **G-PR-102 — Test-mode checkout and upgrade run.** Verifies: PR-203, PR-204. Check (automated where the provider supports test mode): complete a test purchase of each tier, then a mid-cycle upgrade; compare charged totals, proration, and resulting entitlements against the pricing page. Pass: totals and entitlements match the published page for every tier. Fail: block shipment. Recorded in: progress.md.
- **G-PR-103 — Promotion date sweep.** Verifies: PR-208. Check (automated): `grep -rniE "off|discount|sale|offer" site/` lists every promotional surface; each must contain a date or date range on the same page. Pass: zero undated promotions. Fail: block shipment. Recorded in: progress.md.
- **G-PR-104 — Value-metric review.** Verifies: PR-201, PR-209. Check (manual): the pricing document states the value metric, the model-fit sentence, and the derivation of each tier split. Pass: all three present and the tier splits cite the value metric rather than a competitor. Fail: warn; pricing changes pause until the document is completed. Recorded in: progress.md.

## Anti-patterns

- **Round-number gravity.** Prices land on $10/$20/$50 because they look clean, with no reference to the value metric or willingness to pay. Catch it by asking what quantity of value each price buys; if nobody can answer, gravity chose the price.
- **Feature-fence tiers.** Tiers are split by withholding whichever features were easiest to gate, so the upgrade path punishes rather than graduates. Catch it against PR-203: list what a growing customer hits first — if it is an annoyance instead of a success milestone, the fence is wrong.
- **Grandfather fog.** Legacy customers sit on unrecorded prices, so nobody can state what a given account pays or why. Catch it by sampling five old accounts and checking each price exists in the configuration's history.
- **Discount reflex.** Every stalled deal or quiet month is answered with a promotion, training customers to wait for sales. Catch it in the promotion log: more than a few promotions a year means the list price, not the calendar, is the problem.

## Examples

- [Example 1 — The $29 blog post](examples/example-1.md) — violates/corrects PR-205.
- [Example 2 — The launch offer that never ended](examples/example-2.md) — violates/corrects PR-208.
- [Example 3 — Tiers copied from a competitor](examples/example-3.md) — violates/corrects PR-209.

## Recall anchors

- Value metric first; model second; numbers last.
- One configuration renders every price surface.
- A price typed by hand is a future mismatch.
- Every promotion carries its dates, or it comes down.
- Free tiers have limits and a path, or they are defects.

## Checklist

- [ ] Value metric written down before prices were set (PR-201).
- [ ] Model-fit sentence recorded in the pricing document (PR-202, G-PR-104).
- [ ] All prices exist as billing-provider objects; no second price list (PR-204).
- [ ] No hand-typed prices anywhere in copy, email, or ads (PR-205, G-PR-101).
- [ ] Fact sheet prices match the configuration (PR-206).
- [ ] Free tier limits and conversion path stated (PR-207).
- [ ] Every live promotion shows dates and terms (PR-208, G-PR-103).
- [ ] Test checkout and upgrade totals verified against the pricing page (G-PR-102).
