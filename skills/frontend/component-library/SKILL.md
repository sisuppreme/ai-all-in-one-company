# component-library

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Structuring your Storybook (component-driven development, stories per variant and state) — https://storybook.js.org/blog/structuring-your-storybook/ ; GOV.UK Design System, button component — https://design-system.service.gov.uk/components/button/
- **Depends on:** design-tokens, design-system
- **Feeds into:** frontend-core, layout-responsive, forms, ui-states

## When to use / Do NOT use

- **Use when:** building, extending, or reviewing the components pages are assembled from — their variants, state sets, iconography, and content stress behavior. WCPM's component bans and the CMP and ICO families land here, as does the component half of WCPM §8 (components & states).
- **Do NOT use when:** the state belongs to a data view rather than a component (ui-states owns the view-level state matrix), or the question is page composition (layout-responsive, design-system). Components are built here; pages are composed elsewhere.

## Rules

1. **FE-061 — Built bottom-up, in the workshop.** Components are built and reviewed in Storybook, isolated from pages, one story per variant and per state. A component first seen inside a finished page was never reviewed.
2. **FE-062 — The full state set, or a written exception.** Every component ships its applicable states — default, hover, focus-visible, active, disabled, loading, error — or its state matrix states explicitly why a state does not apply (DET-VIS-032).
3. **FE-063 — Behavior lives in the component.** Focus order, keyboard interaction, disabled semantics, and ARIA wiring are implemented and tested once, inside the component — never re-implemented per page.
4. **FE-064 — One icon set.** One icon library or custom set, one stroke weight, one metaphor style across the whole library (DET-VIS-025). A second set is a system change (FE-024), not a per-component choice.
5. **FE-065 — Emoji are never structural icons.** Icons in headings, feature lists, and navigation are drawn icons from the set. Emoji may appear in informal copy, never as the icon for a feature (DET-VIS-016).
6. **FE-066 — Stress-tested with real content.** Components are tested with the longest real names, labels, and words the product will hold; overflow, clipping, or broken wrapping at ordinary content lengths is a component bug (DET-VIS-007).
7. **FE-067 — Variants express hierarchy.** Button and action variants differ by emphasis and context (primary / secondary / destructive / text; sizes by placement), not one treatment at one size for every action (DET-VIS-031). Destructive actions are never styled as primary.
8. **FE-068 — Badges carry actionable information.** A badge or pill states something the user can act on — a status, a genuine novelty, a filterable category. Decorative labeling is removed (DET-VIS-033).
9. **FE-069 — Cards earn their weight.** In a grid, content of unequal importance gets unequal weight: one item may be featured, span wider, or carry richer media. Identical cards are permitted only where the content is genuinely parallel — and their copy must still be specific, not interchangeable (DET-VIS-003).
10. **FE-070 — Pages assemble, they do not imitate.** A page needing something new extends the library; hand-rolled markup that duplicates a library component is a defect, found by the grep gate (G-FE-033), not by taste.

**Architecture must never leak into the UI.** Component names are for builders, not users. No component name, variant name, prop name, or slot name may surface in the UI — not as a label, a heading, an empty-state message, or an error. Buttons say what they do in the user's words; cards, modals, and tables carry the user's content, never the library's vocabulary.

## BAN list

- **BAN-FE-031 — The interchangeable card grid.** Banned: a grid of identical cards whose descriptions could be swapped between cards — or between products — without anyone noticing. Defeats: DET-VIS-003. Bad: three feature cards of identical height and two-line descriptions ("Powerful tools for modern teams", "Built for the way you work", "Everything you need to succeed") that fit any SaaS product ever made. Instead: cards weighted by importance (FE-069) with copy that names this product's specific capability. Severity: WARN.
- **BAN-FE-032 — The icon-in-tinted-circle formula.** Banned: every feature icon presented in an identical soft-tinted circle or rounded square in the accent color, in every grid on the site. Defeats: DET-VIS-026. Bad: six features, six identical lavender circles, repeated unchanged on three pages. Instead: icon treatment that varies by context or uses a distinctive brand device; the chip is one option, not the universal default. Severity: WARN.
- **BAN-FE-033 — Emoji as feature icons.** Banned: 🚀 ⚡ 🔒-style emoji prefixed to feature headings or list items in place of an icon system. Defeats: DET-VIS-016. Bad: "🚀 Fast setup", "🔒 Secure by default", "⚡ Blazing performance" as the product's feature list. Instead: drawn icons from the library's single set (FE-064). Severity: BLOCK.
- **BAN-FE-034 — One button for everything.** Banned: a single button size, radius, and treatment for every action on the site, primary and secondary differing only by fill. Defeats: DET-VIS-031. Bad: the nav CTA, the hero CTA, the delete-account action, and the form submit are the same pill at the same size; delete differs from save only by being red. Instead: a variant hierarchy by emphasis and context, with destructive actions distinctly styled and never primary (FE-067). Severity: WARN.
- **BAN-FE-035 — The template pricing table.** Banned: the three-tier, middle-highlighted, check-icon pricing table applied to a product whose model is not seat-based SaaS. Defeats: DET-VIS-036. Bad: a usage-based API product squeezed into Starter/Pro/Enterprise tiers with a "Most Popular" pill and feature rows differing by one line. Instead: pricing presentation that follows the actual model — usage bands, a calculator, one-time pricing (pricing rules owned by D1's pricing-monetization). Severity: WARN.

## Gates

- **G-FE-031 — Storybook visual regression.** Verifies: FE-061, FE-062, FE-066. Check: automated — Storybook test-runner plus screenshot visual regression over all stories runs in CI, including the long-content stress stories. Pass: all tests green, zero unreviewed screenshot diffs. Fail: block shipment. Recorded in: progress.md.
- **G-FE-032 — State matrix coverage.** Verifies: FE-062, FE-063. Check: manual — walk the state matrix per component: every applicable state (default, hover, focus-visible, active, disabled, loading, error) has a story, and every non-applicable state has its written reason. Pass: matrix complete. Fail: warn and hold the component. Recorded in: progress.md.
- **G-FE-033 — Duplicate-markup grep.** Verifies: FE-070. Check: automated — grep page code for raw `<button`/`<input`/`<select` markup duplicating a library component, and for icon imports outside the library's single set (FE-064). Pass: zero hits. Fail: block until the page uses the library. Recorded in: progress.md.
- **G-FE-034 — Icon and badge audit.** Verifies: FE-064, FE-065, FE-068. Check: manual + automated — scan headings and feature lists for emoji codepoints (automated); screenshot all icons in one view to check stroke weight and metaphor consistency; count badges per viewport and name the action each enables. Pass: no structural emoji, one icon style, every badge actionable. Fail: warn; block if emoji carry a feature list. Recorded in: progress.md.

## Intelligence — decisions & gates

> **Judgment layer.** These decisions apply the judgment layer above this skill — `skills/frontend/design-intelligence/SKILL.md` and the theme library (`skills/frontend/theme-library/`). Settle the theme's art direction there first, then decide here inside it; where a decision below and a rule above disagree, the rule above wins.

### Decision rules — growing the library

| Decision | Read the situation | Decide |
|---|---|---|
| New component or new variant | What actually differs | Emphasis, size, or content only: a variant. Behavior or anatomy differs: a new component. |
| When to abstract | Evidence of reuse | First real use may stay page-level; the second use is the signal to build the library component; a third page-level copy is a defect (FE-070). |
| Variant budget | Whether the variants can still be enumerated | Past roughly six variants, the design is asking for two components — split by purpose rather than adding a seventh. |
| Content model | The product's real data | Design and stress-test against the longest real names and labels the product holds, including other shipped languages (FE-066). |
| Icon treatment | The component's context | Dense UI (nav, toolbars): icons carry meaning and may stand alone. Marketing: icons support specific copy, never replace it (FE-064, FE-065). |
| Card weight | Whether the content is genuinely parallel | Parallel items get equal cards; unequal importance gets a featured, wider, or richer treatment (FE-069). |
| Destructive styling | The action's risk | Destructive actions get a distinct treatment and a confirmation pattern; they are never styled as primary (FE-067). |
| Badge use | Whether the user can act on it | A badge ships only if it states something actionable — a status, genuine novelty, a filter (FE-068). Decorative badges are removed. |

### Self-check gate

- **G-FE-035 — Pre-ship intelligence self-check (components).** Verifies: FE-062, FE-064, FE-066, FE-067, FE-068, FE-070 as judgment, not just compliance. Check: manual — the builder scores each item pass/fail against the library: (1) ★ every component has a story per variant and per applicable state, or a written exception in its state matrix; (2) ★ the longest real content the product holds renders in every text-bearing component without overflow or clipping; (3) every component in the library has a second real use, present or concretely planned — single-use components are demoted to page code; (4) a new hire could enumerate each component's variants from its documentation alone; (5) every badge on the page names an action the user can take; (6) destructive actions are visually distinct from, and never styled as, primary actions. Pass: both ★ items pass and at least 5 of 6 overall. Fail: fix, or log a written exception, before shipping. Recorded in: progress.md.

### Anti-pattern table — symptom → cause → fix

| Symptom | Cause | Fix |
|---|---|---|
| Component soup — forty components, half of them used exactly once | Abstraction on first use, with no reuse evidence | Demote single-use components to page code; a library entry requires a second real use. |
| Variant explosion — the button has fourteen variants nobody can list | Every page request was granted a variant instead of a decision | Cap the variants, split by purpose, and document each variant's "do not use when" (design-system FE-023). |
| State gaps debut in production — disabled and loading states are broken in the app, fine in the mockups | Stories were built for default and hover only | Ship the full state set or a written exception (FE-062); check coverage against stories (G-FE-032). |
| Placeholder-perfect, real-content broken — cards clip the longest customer name | Components were tested with "John Doe" and lorem ipsum | Stress stories with the longest real content (FE-066). |
| Lookalike duplication — pages hand-roll near-copies of library components | The library component almost fit, so the page team routed around it | Extend the component; find imitations with the grep gate (G-FE-033). |
| Prop sprawl — a component takes twenty props and behaves unpredictably in combination | Configuration was used to avoid making design decisions | Decide variants; props carry content, not layout personalities. |
| Mixed iconography — two stroke weights and two metaphor styles across pages | Icons imported ad hoc, per page and per component | One set, one stroke weight (FE-064); audit with G-FE-034. |

## Anti-patterns

- **The near-duplicate folder.** `Card`, `CardNew`, `PricingCard2`, and `FeatureCardOld` coexist because extending the original felt risky. Catch it: inventory the library at review; duplicates merge into variants of one component or are deleted.
- **The bypass page.** Under deadline, a page hand-rolls its markup "just this once" and the exception becomes the template for the next three pages. Catch it: the grep gate (G-FE-033) runs on every page, not just new components.
- **Props as a junk drawer.** A component accumulates boolean props (`isAlt`, `noIcon`, `wide2`) until no story shows the real combinations. Catch it: count props at review; a component whose variants cannot be enumerated becomes two components.
- **States designed, never rendered.** The state matrix exists on paper but the loading and error stories were never built, so the states debut in production. Catch it: coverage is checked against stories, not documents (G-FE-032).

## Examples

- [Example 1 — Interchangeable feature cards become weighted, specific cards](examples/example-1.md) — corrects FE-069.
- [Example 2 — A mixed icon drawer becomes one icon set](examples/example-2.md) — corrects FE-064.
- [Example 3 — A button with two states becomes a full state matrix](examples/example-3.md) — corrects FE-062.

## Recall anchors

- One story per variant and state, or it wasn't reviewed.
- Behavior is built once, inside the component.
- One icon set, one stroke weight; emoji are not icons.
- Test with the longest real content, not the placeholder.
- Pages assemble from the library — they never imitate it.

## Checklist

- [ ] Every variant and state has a Storybook story (G-FE-031).
- [ ] State matrix complete, with written reasons for non-applicable states (G-FE-032).
- [ ] Longest real content renders without overflow or clipping (FE-066).
- [ ] All icons come from the single set at one stroke weight (FE-064).
- [ ] No emoji serve as structural icons anywhere (FE-065).
- [ ] No raw component-duplicating markup in page code (G-FE-033).
- [ ] Every badge names an action the user can take (FE-068).
- [ ] Button variants express hierarchy; destructive is never primary (FE-067).
