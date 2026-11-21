# typography

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** GOV.UK Design System, headings and typography styles — https://design-system.service.gov.uk/styles/headings/ ; Design Tokens Format Module 2025.10 (typography tokens) — https://www.designtokens.org/tr/2025.10/
- **Depends on:** design-tokens
- **Feeds into:** frontend-core, component-library, forms

## When to use / Do NOT use

- **Use when:** defining or reviewing a type system; setting headings, body, captions, or data text; choosing or loading font families; fixing flat hierarchy, arbitrary sizes, or unfinished prose detail.
- **Do NOT use when:** the question is which token file or transform pipeline holds the values — that is design-tokens. Do not use this skill to set text color pairs; contrast pairs are chosen in design-tokens and only consumed here (FE-146).

## Rules

1. **FE-141 — Sizes come only from the type scale.** Every font size in a component is a type-scale token (display, heading levels, body, caption, data). An off-scale size is a defect (DET-VIS-012).
2. **FE-142 — Hierarchy is unmistakable.** On marketing and editorial pages the largest heading is at least 2.5× body size, heading levels step down clearly, and captions are distinctly smaller than body (DET-VIS-012).
3. **FE-143 — Case and weight vary by level and purpose.** Heading levels differ in size and, where the design calls for it, weight or case; one weight and one case pattern across every level fails review (DET-VIS-015).
4. **FE-144 — Micro-typography is finished work.** Prose uses real quotation marks and en/em dashes, uppercase labels are tracked out, and tables and data use tabular numerals (DET-VIS-014).
5. **FE-145 — Emphasis is solid.** Emphasis is achieved with weight, size, italic, or a solid accent color; gradient-clipped headline text is not a default device (DET-VIS-018).
6. **FE-146 — Body text meets AA contrast.** Body and caption text — including "muted" gray styles — meet WCAG AA (4.5:1, 3:1 for large text) on the surface they sit on.
7. **FE-147 — Two families, only the weights used.** A project loads at most two font families and only the weights its scale actually uses, self-hosted or delivered with subsetting and `font-display: swap` (or the stack's equivalent).
8. **FE-148 — Line length and leading are set per size.** Body columns run near 45–80 characters, and line-height is specified per type role — display text tight, body text open — never one leading for all sizes (DET-VIS-013).
9. **FE-149 — Fluid sizing comes from tokens.** Responsive type uses `clamp()` ranges defined in the type tokens (minimum, preferred, maximum), not per-component viewport arithmetic.
10. **FE-150 — Emoji are never structural.** Emoji do not appear as heading decoration, list markers, or iconography in the interface (DET-VIS-016); icons come from the component library's icon set.
11. **FE-151 — Inherited typography law.** The WCPM TYP parameter family applies as cited in docs/WCPM_MAPPING.md §2.4, and typography work is designed to pass the G-VIS gate family.

## BAN list

- **BAN-FE-071 — Gradient headline text.** Banned: `background-clip: text` gradient fills on headlines as the default emphasis device. Defeats: DET-VIS-018. Bad: every H1 on the site is a purple-to-blue gradient. Instead: a solid token color with weight and size doing the emphasis (FE-145). Severity: WARN.
- **BAN-FE-072 — Off-scale font sizes.** Banned: any font size that is not a type-scale token value. Defeats: DET-VIS-012. Bad: components variously set 13px, 15px, 17.5px, and 22px by eye. Instead: the nearest scale step, or a new step added to the scale with a role (FE-141). Severity: BLOCK.
- **BAN-FE-073 — Emoji as iconography.** Banned: emoji used in headings, navigation, feature lists, or buttons in place of icons. Defeats: DET-VIS-016. Bad: feature headings read "🚀 Fast", "🔒 Secure", "📊 Insightful". Instead: the library's icon set, or no icon at all. Severity: BLOCK.
- **BAN-FE-074 — Monotone headings.** Banned: every heading level set in the same weight and the same case pattern. Defeats: DET-VIS-015. Bad: H1 through H4 are all uppercase 600-weight, differing only slightly in size. Instead: a per-level case/weight scheme recorded in the type tokens (FE-143). Severity: WARN.
- **BAN-FE-075 — Unexamined default pairing.** Banned: shipping the framework's or generator's default font pairing as the design without a recorded choice. Defeats: DET-VIS-011. Bad: the site launches in the starter template's fonts because nobody picked any. Instead: choose families against the brand and content, record the choice, load per FE-147. Severity: WARN.

## Gates

- **G-FE-071 — Computed-style type audit.** Verifies: FE-141, FE-142. Check: automated — a script lists distinct font families, sizes, and weights rendered on each main page and diffs them against the type-scale tokens. Pass: every rendered value is in the scale and the largest heading is ≥ 2.5× body on marketing pages. Fail: block shipment. Recorded in: progress.md.
- **G-FE-072 — Font payload check.** Verifies: FE-147, FE-149. Check: automated — the build report lists loaded families and weights; fail if families exceed two, a loaded weight is unused by the scale, or `clamp()` ranges in components are not token values. Pass: all three conditions clean. Fail: warn; a third family blocks. Recorded in: progress.md.
- **G-FE-073 — Micro-typography scan.** Verifies: FE-144. Check: manual — scan headings and prose for straight quotes, hyphens used as dashes, untracked uppercase labels, and proportional numerals in data tables. Pass: no instances on main pages. Fail: warn and fix before release. Recorded in: progress.md.
- **G-FE-074 — Text contrast verification.** Verifies: FE-146. Check: automated — run the design-tokens contrast script over every text-on-surface token pair actually used, including muted styles. Pass: all pairs ≥ 4.5:1 (3:1 large text). Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Arbitrary size creep.** A 13.5px here and a 15px there accumulate until no scale exists. Catch it: if the computed-style audit lists more sizes than the scale has steps, creep has already happened.
- **All-caps everything.** Headings, labels, buttons, and body emphasis all shouted in uppercase. Catch it: count distinct case patterns; one pattern everywhere is the tell.
- **Muted-gray body text.** Body copy set in a light gray that "looks softer" and fails AA. Catch it: run the contrast check on the muted style specifically, not just the default body pair.
- **Straight quotes in finished prose.** Prose ships with typewriter quotes and hyphens where dashes belong. Catch it: the micro-typography scan (G-FE-073) exists precisely for this.

## Examples

- [Example 1 — Flat arbitrary sizes replaced by a token scale](examples/example-1.md) — corrects FE-141, FE-142.
- [Example 2 — Gradient headline and straight quotes finished properly](examples/example-2.md) — corrects FE-145, FE-144.
- [Example 3 — Monotone headings given a per-level scheme](examples/example-3.md) — corrects FE-143.

## Recall anchors

- Sizes come from the scale or they do not ship.
- Hierarchy you can see from across the room.
- Emphasis is solid: weight, size, italic, accent.
- Quotes, dashes, and numerals are finished work.
- Two families, only the weights used.

## Checklist

- [ ] Computed-style audit matches the type scale exactly (G-FE-071).
- [ ] Largest heading is ≥ 2.5× body size on marketing/editorial pages (FE-142).
- [ ] Heading levels vary in case/weight per the recorded scheme (FE-143).
- [ ] No gradient headline text; no emoji in headings or UI structure (BAN-FE-071, BAN-FE-073).
- [ ] Font payload is ≤ 2 families with only used weights (G-FE-072).
- [ ] Muted text styles pass AA contrast (G-FE-074).
- [ ] Micro-typography scan is clean (G-FE-073).
