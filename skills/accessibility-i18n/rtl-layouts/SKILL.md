# rtl-layouts

## Metadata

- **Owner department:** D13 Accessibility & i18n (AC)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** "Internationalization Best Practices: Handling Right-to-left Scripts in HTML", W3C — https://www.w3.org/International/geo/html-tech/tech-bidi.html ; CSS Logical Properties and Values, W3C (via MDN) — https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_logical_properties_and_values
- **Depends on:** internationalization (supplies correct `lang`/`dir` metadata and flexible containers)
- **Feeds into:** localization-workflow (RTL renders are part of its in-context review), wcag (mirrored focus order and reading order feed conformance)

## When to use / Do NOT use

- **Use when:** Building or reviewing any layout that must serve a right-to-left locale (Arabic, Urdu, Persian, Hebrew) — setting document direction, writing directional CSS, deciding which icons and components flip, isolating embedded LTR content, and running the per-script RTL visual QA pass.
- **Do NOT use when:** Extracting strings, wiring ICU/`Intl` formatting, or setting `lang` (internationalization), running the translation pipeline and its review states (localization-workflow), or judging general WCAG conformance (wcag, accessibility-audit).

## Rules

1. **AC-161 — Direction is declared on the root, never faked or inferred.** Every RTL locale is served with `dir="rtl"` on the document root element, set from the locale's metadata. Direction is never inferred from `lang` by hand-rolled code, never guessed from text content, and never simulated by transforming an LTR layout.
2. **AC-162 — Directional layout uses CSS logical properties only.** Spacing, positioning, borders, radii, and alignment are written as `margin-inline-start`, `padding-inline`, `inset-inline-start`, `border-start-start-radius`, `text-align: start`, and their siblings, so one stylesheet serves both directions and flipping `dir` flips the layout. A physical directional property in component code is a defect.
3. **AC-163 — Flexbox and grid are left to follow direction.** Flex rows and grid inline axes already run in the inline direction; no `row-reverse`, manual `order` shuffling, or direction-detection JavaScript is added to compensate for physical CSS elsewhere — the physical CSS is fixed instead.
4. **AC-164 — What mirrors is decided once, in the design system.** Navigation order, breadcrumb order, progress indicators, pagination, back/forward chevrons, directional flow diagrams, and media-player progress follow the inline direction. The flip/no-flip decision for every icon and component class lives in one design-system list, not in per-screen judgment calls.
5. **AC-165 — Semantic direction never flips.** Clocks and time representations, chart and graph axes tied to data conventions, logos and brand marks, phone keypads, and the media content itself (photos, video) are never mirrored. Play icons are decided once in the tokens per AC-164, not per screen.
6. **AC-166 — Embedded opposite-direction runs are isolated.** An English product name, number, price, or code fragment inside an RTL sentence is wrapped in `<bdi>`, an inline element with an explicit `dir`, or Unicode isolate characters (U+2066–U+2069), so the Unicode Bidirectional Algorithm places numbers and punctuation on the correct side.
7. **AC-167 — Inherently LTR content stays LTR.** Code blocks, URLs, email addresses, and phone numbers inside an RTL page render with `dir="ltr"` (and `unicode-bidi: isolate` where they sit inside RTL text), so they read and select in their native order.
8. **AC-168 — Scroll regions, carousels, and sliders start at inline-start.** Horizontal scroll regions begin scrolled to the inline-start edge, carousel advance follows the inline direction, slider value increases toward inline-end, and the scrollbar sits where the platform places it for the document direction — none of these is hard-coded to the left.
9. **AC-169 — Text truncation and alignment follow the logical end.** Body text aligns to `start`; truncation clips at the logical end of the line with the ellipsis there. A deliberate exception (centered display type, justified legal text) is recorded in the design system, not improvised per component.
10. **AC-170 — Numbers and dates are formatted, never hand-reversed.** Digits use the locale's CLDR numbering system as decided per locale, and dates render through `Intl.DateTimeFormat` for the RTL locale. A date or number string is never reversed, reordered, or re-punctuated by string manipulation to "look RTL".
11. **AC-171 — RTL QA is per script, with real text.** Each target script is checked with real content in that script: Arabic (Naskh) passing does not certify Urdu — Nastaliq has far taller line boxes, so line-height, clipping, and truncation are verified separately for Nastaliq, and again for Persian and Hebrew where targeted.
12. **AC-172 — Charts, maps, and diagrams are individually reviewed in RTL.** No chart, map, or annotated diagram ships in an RTL locale until a human has reviewed its RTL render: axis and legend order, label placement, and annotation direction are checked against the data conventions in AC-165.

## BAN list

- **BAN-AC-081 — Physical directional CSS in component code.** Banned: `margin-left`, `padding-right`, `left: 0`, `float: left`, `text-align: right` used to position or align layout in a component. Defeats: DET-UX-023. Bad: the checkout summary is placed with `margin-left: auto` and `left`-positioned step icons; under `dir="rtl"` the summary overlaps the form and the primary pay button is pushed out of the usable flow. Instead: the same layout in logical properties (`margin-inline-start: auto`, `inset-inline-start: 0`, `text-align: start`) mirrors automatically when `dir` flips. Severity: BLOCK.
- **BAN-AC-082 — Mirroring faked with transforms.** Banned: `transform: scaleX(-1)` (or a flipped duplicate stylesheet) applied to a container or page to simulate RTL. Defeats: DET-VIS-037. Bad: a wrapper flips the settings page visually, but text renders mirrored-glyph by glyph in screenshots, focus order still runs left-to-right, and embedded images and logos are flipped too — the layout was collapsed into place, not adapted. Instead: set `dir="rtl"` on the root and build on logical properties (AC-161, AC-162) so content, focus order, and reading order all follow direction. Severity: BLOCK.
- **BAN-AC-083 — Un-isolated embedded LTR run in RTL text.** Banned: interpolating a Latin-script product name, number, or price directly into an RTL string with no `<bdi>`, inline `dir`, or Unicode isolate. Defeats: DET-NONE — no DET parameter names this signal; pattern owned by this skill. Bad: "Order Pro Max 12 today" inside an Arabic sentence renders with the "12" and the trailing punctuation jumped to the wrong side of the product name, so the offer text is garbled at reading size. Instead: the interpolated value is isolated — `<bdi>Pro Max 12</bdi>` — so the bidi algorithm orders the sentence around it correctly. Severity: BLOCK.
- **BAN-AC-084 — Blanket-flipping icons and media.** Banned: a global rule such as `[dir="rtl"] svg { transform: scaleX(-1) }` or flipping every icon, logo, and image in RTL. Defeats: DET-UX-015. Bad: the same clock icon that reads correctly in LTR now runs counter-clockwise, the logo is mirrored, and a play glyph flips on one screen but not another because a component opted out ad hoc — the same element behaves differently across screens. Instead: only the directional icons on the design-system flip list (AC-164) flip, via a named utility or token; semantic icons, logos, and media never do (AC-165). Severity: BLOCK.
- **BAN-AC-085 — Fixed line-height or height tuned to Latin/Arabic text shipped for Nastaliq.** Banned: shipping an Urdu (or any new-script) locale with line-height, fixed-height headings, or single-line truncation carried over from the LTR or Arabic build without a per-script render check. Defeats: DET-VIS-039. Bad: card titles get a fixed 1.2 line-height and a fixed hero height from the English design; Nastaliq ascenders and descenders are clipped in every heading — the fixed height clips the script itself. Instead: line-height and container heights are verified per script with real Urdu text (AC-171) and fixed heights on text containers are removed or raised until nothing clips. Severity: BLOCK.

## Gates

- **G-AC-081 — Physical-property scan.** Verifies: AC-162, AC-163. Check: run stylelint with a logical-properties rule set (e.g. `stylelint-use-logical-spec` / `liberty/use-logical-spec`) over all component CSS, plus `grep -rnE "(margin|padding)-(left|right)|(^|[^-])(left|right)\s*:|float:\s*(left|right)|text-align:\s*(left|right)" src/ --include='*.css'` as a backstop. Pass: zero findings outside the recorded exception list (e.g. print stylesheets). Fail: block shipment; convert each finding to its logical equivalent and re-run. Recorded in: progress.md.
- **G-AC-082 — RTL render pass.** Verifies: AC-161, AC-164, AC-168, AC-169. Check: with the browser/Playwright, load every key template in an RTL locale and assert `document.documentElement.dir === "rtl"`, `document.documentElement.scrollWidth <= window.innerWidth` (no page-level horizontal overflow), and screenshot each template beside its LTR counterpart for the human diff review. Pass: all assertions hold and a reviewer has signed the LTR/RTL screenshot diff set, including icon flips and scroll-region start positions. Fail: block shipment for that locale; fix and re-render. Recorded in: progress.md.
- **G-AC-083 — Bidi test-string check.** Verifies: AC-166, AC-167, AC-170. Check: render the agreed bidi test set — mixed Arabic/English/number strings, a price with currency, a phone number, a URL, and a code snippet — on the data-dense screens (product, checkout, account) and inspect each render against the expected ordering recorded in the test file. Pass: every test string renders with numbers, punctuation, and embedded LTR runs on the correct side, and code/URL/phone render LTR. Fail: block shipment; add or fix the isolation and re-render. Recorded in: progress.md.
- **G-AC-084 — Per-script visual QA.** Verifies: AC-171, AC-172. Check: for each targeted script beyond the first RTL script (Urdu/Nastaliq, Persian, Hebrew as applicable), screenshot the key templates with real content in that script; a reviewer checks line-height, clipping, truncation direction, and every chart/map/diagram render individually. Pass: signed checklist per script with zero clipped or overflowing text blocks and every chart reviewed. Fail: block shipment for that locale only; the Arabic pass does not substitute. Recorded in: progress.md.
- **G-AC-085 — Icon flip-list conformance.** Verifies: AC-164, AC-165. Check: diff the set of icons flipped in the RTL render (from the G-AC-082 screenshots) against the design-system flip list; grep the codebase for blanket flip rules (`scaleX(-1)` on icon or container selectors). Pass: flipped set matches the list exactly and no blanket flip rule exists. Fail: block shipment; correct the icon utility or the list — in the design system, not per screen. Recorded in: progress.md.

## Anti-patterns

- **The Arabic-pasted LTR page.** `dir="rtl"` is set and the words are Arabic, but the layout still runs on physical CSS, so columns, icons, and scroll regions stay in LTR positions — an LTR page with Arabic pasted in. Catch it in the G-AC-082 side-by-side screenshots, not by reading the markup.
- **The pseudo-RTL shortcut.** QA tests a mechanically flipped or pseudo-locale build and signs off, so real bidi ordering and Nastaliq shaping defects survive to production. Catch it by requiring real text in the real script for G-AC-083 and G-AC-084 — pseudo-RTL catches flips, never shaping.
- **The one-off flip.** A developer flips a single icon or component inline "for the Arabic page," outside the design-system list, so the next screen — or the next locale — makes the opposite choice. Catch it at G-AC-085: any flip not traceable to the list is rework.
- **The reversed string.** A date, price, or tracking number is reversed character-by-character in code to "look right" in RTL, corrupting the value for copy-paste, screen readers, and search. Catch it by selecting and copying rendered values during the G-AC-083 pass — a correct render copies in logical order.

## Examples

- [Example 1 — Physical CSS converted to logical properties](examples/example-1.md) — violates/corrects AC-162, AC-163.
- [Example 2 — Transform mirroring replaced by `dir="rtl"`, and blanket icon flip replaced by the flip list](examples/example-2.md) — violates/corrects AC-161, AC-164, AC-165.
- [Example 3 — Un-isolated product name and price isolated with `<bdi>`](examples/example-3.md) — violates/corrects AC-166, AC-167.

## Recall anchors

- Flip the document, not the stylesheet: `dir="rtl"` plus logical properties, and mirroring is automatic.
- Physical left/right in a component is a defect, not a style choice.
- Directional icons flip; clocks, charts, logos, and media never do — the list lives in the design system.
- Isolate every embedded run: numbers, names, code, and URLs keep their own direction inside RTL text.
- Arabic passing does not certify Urdu — Nastaliq gets its own visual QA.

## Checklist

- [ ] Every RTL locale serves `dir="rtl"` on the root from locale metadata; no transform-based mirroring exists anywhere.
- [ ] G-AC-081 physical-property scan is clean outside the recorded exception list.
- [ ] G-AC-082 RTL render pass: correct `dir`, zero page-level horizontal overflow, screenshot diff set human-reviewed.
- [ ] Icon and component flips match the design-system flip list exactly — G-AC-085; clocks, charts, logos, and media unflipped.
- [ ] Bidi test strings render with correct ordering on data-dense screens, and code/URLs/phone numbers render LTR — G-AC-083.
- [ ] Scroll regions, carousels, and sliders start at inline-start and advance in the inline direction.
- [ ] Each additional script (Urdu/Nastaliq, Persian, Hebrew) has its own signed visual QA, including every chart and map — G-AC-084.
