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

**Architecture must never leak into the UI.** Type carries the user's words, never the type system's. Font names, scale names, type-role labels, and the typographic system's vocabulary must never appear in UI copy — no font names in settings or about text, no scale labels, no type-system terminology anywhere a user can read it. The reader notices the voice, never the foundry.

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

## Intelligence — decisions & gates

> **Judgment layer.** These decisions apply the judgment layer above this skill — `skills/frontend/design-intelligence/SKILL.md` and the theme library (`skills/frontend/theme-library/`). Settle the theme's art direction there first, then decide here inside it; where a decision below and a rule above disagree, the rule above wins.

### Decision rules — choosing type

| Decision | Read the situation | Decide |
|---|---|---|
| Family pairing | Expressive or editorial brand | A characterful display face for headings over a quiet text face; the display face is the brand voice, the text face disappears. |
| Family pairing | Product UI or data product | One grotesque family across a wide weight range; spend the second family only if editorial content truly needs it (FE-147). |
| Scale ratio | Long-form reading dominates | A gentler ratio (≈1.2–1.25) with more steps, so adjacent levels stay calm and scannable. |
| Scale ratio | Marketing or landing pages | A steeper ratio (≈1.333–1.5) with fewer steps; the display step does the persuading (FE-142). |
| Measure | Articles and essays vs docs and panels | 55–70 characters for essays; 45–60 for documentation and UI panels; hero lines are set deliberately, never run to the container edge (FE-148). |
| Body floor | Older or low-literacy audience | Body at 16px or above with open leading; never trade legibility for density. |
| Numerals | Prices, tables, metrics in the content | Tabular lining figures wherever data aligns; old-style figures belong to prose only (FE-144). |
| Loading strategy | Performance-sensitive audience or slow networks | One variable font or a system stack beats two static families; subset and swap (FE-147, FE-149). |
| Script coverage | Multilingual audience | Choose families with full coverage of the shipped scripts before judging aesthetics; a beautiful face missing a script is a defect, not a trade-off. |

### Self-check gate

- **G-FE-075 — Pre-ship intelligence self-check (typography).** Verifies: FE-141, FE-142, FE-143, FE-144, FE-146, FE-148 as judgment, not just compliance. Check: manual — the builder scores each item pass/fail on the shipped pages: (1) ★ squint test — blur or step back: heading levels still read as distinct bands of emphasis; (2) ★ on marketing and editorial pages the largest heading is at least 2.5× body size; (3) every rendered size is a scale step — no strays in computed styles; (4) body columns measure 45–80 characters at the widest viewport; (5) data uses tabular numerals, and quotes and dashes are finished typography; (6) muted and caption styles pass AA on the actual surfaces they sit on. Pass: both ★ items pass and at least 5 of 6 overall. Fail: fix, or log a written exception, before shipping. Recorded in: progress.md.

### Anti-pattern table — symptom → cause → fix

| Symptom | Cause | Fix |
|---|---|---|
| Hierarchy collapse — heading, subheading, and body sit within ~1.2× of each other and nothing leads | Scale ratio too flat; sizes picked per component by eye | Re-derive the scale with a steeper ratio; largest heading ≥ 2.5× body (FE-142). |
| Measure drift — line length swings from 40 to 110 characters across templates | Container widths set by layout habit, not by type role | Set measure per role in the type tokens and hold 45–80 characters (FE-148). |
| Scale without rhythm — sizes form a scale, yet pages feel uneven and restless | Type scale defined without a matching leading and spacing rhythm | Tie line-height and vertical margins to the same modular scale; leading per role, never one value for all sizes (FE-148). |
| Weight-only hierarchy — every level is the same face at similar size, separated only by bold | The display step was never created; large type felt risky | Add a display step and vary case and weight per level under a recorded scheme (FE-143). |
| Elegant gray captions nobody can read | Muted color chosen by eye on white, then placed on tinted surfaces | Verify every muted pair on its actual surface (FE-146, G-FE-074). |
| Font tourism — a fashionable display face fights the copy (condensed face, endless headlines; script face in UI) | Family chosen from a gallery, never tested against real content | Adopt a face only after it survives the product's longest real headline and a full body paragraph; record the choice (FE-147). |
| Prices and table columns jitter and refuse to align | Default proportional figures used in data | Tabular numerals for all data text (FE-144). |

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
