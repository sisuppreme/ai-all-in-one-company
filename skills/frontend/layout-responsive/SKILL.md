# layout-responsive

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** GOV.UK Design System, layout styles — https://design-system.service.gov.uk/styles/layout/ ; WCAG 2.2 criteria summary (reflow SC 1.4.10, target size SC 2.5.8) — https://convarso.com/blog/web-accessibility-guide-wcag/
- **Depends on:** design-tokens, design-system
- **Feeds into:** frontend-core, forms, data-visualisation

## When to use / Do NOT use

- **Use when:** building or reviewing any page or component layout; choosing breakpoints or container widths; fixing overflow, clipping, or a mobile view that is a squeezed desktop page.
- **Do NOT use when:** the decision is a token value (spacing, radius scales) — that is design-tokens. Do not use this skill to justify hiding content on mobile; hiding is a content decision owned by the page's requirements, and FE-131 still applies.

## Rules

1. **FE-121 — No page-level horizontal scrolling.** At every width from 320 CSS px up, the page itself never scrolls horizontally (DET-VIS-038; WCAG 1.4.10 reflow). Overflow is fixed in the layout, never by clipping the page.
2. **FE-122 — Breakpoints where content breaks.** Layouts are fluid first; a breakpoint is added at the width where the content actually fails, and breakpoints are named for the layout change (`nav-collapses`, `cards-two-up`), never for a device.
3. **FE-123 — Mobile is recomposed, not stacked.** Small-screen layouts reorder by priority — primary content and actions first — instead of stacking desktop DOM order top to bottom (DET-VIS-037).
4. **FE-124 — Targets stay tappable at every width.** Interactive targets are at least 24×24 CSS px (WCAG 2.5.8 floor) at every breakpoint; 44px is the working target for primary actions.
5. **FE-125 — Heroes size to content.** Hero height comes from `min-height` plus content and padding; fixed `100vh` or pixel heights that can clip text or CTAs on short screens are forbidden (DET-VIS-039).
6. **FE-126 — Width follows content role.** Reading content, galleries, data tables, and media each get the width their role needs; one container width applied to every section is a defect (DET-VIS-005).
7. **FE-127 — Reading measure is held.** Body-text columns stay near 45–80 characters at wide viewports instead of running to the container edge.
8. **FE-128 — Media space is reserved before load.** Every image and embed carries `width`/`height` or an `aspect-ratio`, so layout does not shift when assets arrive (CLS budget, frontend-core).
9. **FE-129 — Components respond to their own space.** A component used in both wide and narrow contexts adapts with container queries to the space it is given, not with page-level breakpoints written for one placement.
10. **FE-130 — Wide content is contained or reformatted.** Tables, code blocks, and charts get a contained scroll region or a small-screen reformat (stacked rows, priority columns); they never force page overflow and are never silently truncated.
11. **FE-131 — Nothing essential disappears on small screens.** Content or actions removed at a breakpoint must be reachable another way on that viewport; "it didn't fit" is not a removal reason (DET-VIS-037).
12. **FE-132 — Inherited layout law.** The WCPM LAY, SEC, and SPC parameter families apply as cited in docs/WCPM_MAPPING.md §2.4, and layout work is designed to pass the G-EXP gate family.

## BAN list

- **BAN-FE-061 — Fixed-height hero.** Banned: a hero with a fixed `100vh` or pixel height whose text or CTA clips on short or landscape screens. Defeats: DET-VIS-039. Bad: `.hero { height: 100vh; }` cuts the signup button off on a 667px-tall phone. Instead: `min-height` sized by content, with the CTA always in flow. Severity: BLOCK.
- **BAN-FE-062 — Page-level horizontal overflow.** Banned: shipping a page where `scrollWidth` exceeds the viewport at any width ≥ 320px. Defeats: DET-VIS-038. Bad: a 900px-wide pricing table forces sideways page scrolling on every phone. Instead: a contained scroll region or a stacked reformat for the table (FE-130). Severity: BLOCK.
- **BAN-FE-063 — Essential content hidden on mobile.** Banned: `display: none` on content or actions at small breakpoints with no alternate path to them. Defeats: DET-VIS-037. Bad: the spec sheet and the support link vanish below 768px "because they didn't fit." Instead: recompose by priority (FE-123) or move the content behind a reachable disclosure. Severity: BLOCK.
- **BAN-FE-064 — One container width for every section.** Banned: a single `.container` max-width governing prose, galleries, tables, and media alike. Defeats: DET-VIS-005. Bad: a photo gallery squeezed into the 65ch reading column. Instead: width tokens per content role (FE-126). Severity: WARN.
- **BAN-FE-065 — Uniform section template.** Banned: every section shipping with identical padding, alignment, and loudest element regardless of its role. Defeats: DET-VIS-001. Bad: hero, features, proof, and pricing all render as centered text in the same vertical rhythm. Instead: composition varies by section role, per design-system. Severity: WARN.

## Gates

- **G-FE-061 — Overflow assertion.** Verifies: FE-121, FE-130. Check: automated — Playwright loads every route at 320/390/768/1440px and asserts `document.scrollingElement.scrollWidth <= window.innerWidth` on each. Pass: zero routes overflow at any width. Fail: block shipment. Recorded in: progress.md.
- **G-FE-062 — Screenshot matrix review.** Verifies: FE-123, FE-125, FE-131. Check: manual — review screenshots at 320/390/768/1440px per main page; confirm priority order on mobile, unclipped heroes, and no essential content missing at small widths. Pass: all four widths conform. Fail: block shipment. Recorded in: progress.md.
- **G-FE-063 — Target-size audit.** Verifies: FE-124. Check: automated — a script reads computed sizes of all interactive elements at 390px and fails any below 24×24 CSS px. Pass: zero undersized targets. Fail: warn; a primary action below the floor blocks. Recorded in: progress.md.
- **G-FE-064 — Resize walk.** Verifies: FE-122, FE-127. Check: manual — drag the viewport continuously from 320px to 1920px on the main pages, watching for overlap, orphaned controls, and unreadable line lengths between breakpoints. Pass: no failure at any intermediate width. Fail: warn and log the failing width range. Recorded in: progress.md.

## Anti-patterns

- **The 768 stack.** One `max-width: 768px` query stacks everything in DOM order and calls it the mobile design. Catch it: if the mobile order is the desktop order, no recomposition happened (FE-123).
- **Desktop-first afterthought.** The desktop page is finished, then squeezed until it fits a phone. Catch it: check whether spacing, type, and targets were re-decided for small screens or merely compressed.
- **Device-named breakpoints.** Breakpoints called "tablet" or "iPhone" encode hardware, not content failure. Catch it: read the breakpoint names; a device name means the breakpoint was placed by guess.
- **Shrink-to-fit type.** Text is made smaller and smaller at narrow widths instead of the layout changing. Catch it: body text below the type scale's minimum at any width is the tell.

## Examples

- [Example 1 — Fixed-height hero that clips its CTA](examples/example-1.md) — corrects FE-125.
- [Example 2 — Wide table overflowing the page](examples/example-2.md) — corrects FE-121, FE-130.
- [Example 3 — DOM-order stack recomposed by priority](examples/example-3.md) — corrects FE-123.

## Recall anchors

- No page scroll sideways, ever, from 320px up.
- Mobile is recomposed by priority, not stacked.
- Heroes size to content; nothing essential is hidden.
- Width follows the content's role.
- Breakpoints live where content breaks, not on devices.

## Checklist

- [ ] Overflow assertion passes on every route at 320/390/768/1440px (G-FE-061).
- [ ] Mobile order follows priority, not desktop DOM order (FE-123).
- [ ] All interactive targets are ≥ 24×24 CSS px at mobile widths (G-FE-063).
- [ ] Heroes use `min-height` and cannot clip text or CTAs (FE-125).
- [ ] Container widths vary by content role (FE-126).
- [ ] Wide tables and code are contained or reformatted (FE-130).
- [ ] Nothing essential is unreachable on small screens (FE-131).
