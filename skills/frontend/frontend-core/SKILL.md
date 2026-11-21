# frontend-core

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Core Web Vitals thresholds (web.dev, reproduced) — https://aemorph.com/guides/core-web-vitals/ ; Performance budgets in CI — https://www.debugutils.dev/blog/performance-budgets/
- **Depends on:** design-system, design-tokens
- **Feeds into:** component-library, layout-responsive, typography, ui-states

## When to use / Do NOT use

- **Use when:** building or reviewing any page or view — this is the base layer every other D3 skill assumes: semantic structure, the performance budget, the accessibility floor, and the rule that the frontend renders real data and real imagery only. WCPM §1 (priority & conflicts) and §9 (engineering) land here, as do the CC and CD cure families.
- **Do NOT use when:** the decision belongs to a specialist skill — token values to design-tokens, component internals to component-library, animation to motion. This skill sets the constraints those skills work inside; it does not replace them.

## Rules

1. **FE-001 — Semantic structure first.** Landmarks, headings, and native controls come before any component styling; framework components wrap native elements, and custom widgets are the last resort. (WCPM §1 priority order, R-1.x.)
2. **FE-002 — A clickable `div` is a defect.** Anything that responds to a click is a `<button>` or `<a>` with a real href, keyboard-operable and focusable. There is no styling exception.
3. **FE-003 — Reserved media dimensions.** Every image and video ships with `width`/`height` or an `aspect-ratio` so nothing shifts after load; layout stability is part of the CLS budget, not a polish step.
4. **FE-004 — Tokens only.** No hard-coded color, spacing, radius, or duration values in page or component code — semantic tokens from design-tokens are the only source (FE-041).
5. **FE-005 — The budget is a requirement.** Each route carries a JavaScript budget and the Core Web Vitals bars at the 75th percentile. A feature that breaks the budget is redesigned or split, never shipped heavy. Thresholds are cited from the numbers registry in `gates/`, per WCPM Appendix F — not restated here or per project.
6. **FE-006 — Real imagery only.** Imagery depicts the actual product, place, or people, or is clearly generic decoration. AI artifacts in photography (malformed hands, gibberish in-image text, warped logos) are a blocker, never a shrug (DET-VIS-024).
7. **FE-007 — Render real data only.** The frontend renders data that exists: no invented logos in "trusted by" rows, no unsourced stat bands, no placeholder avatars presented as people (WCPM Appendix A data/fabrication bans, D- working IDs). A claim the data cannot support is removed, not decorated.
8. **FE-008 — In-UI copy follows the copy rules.** Interface text carries no banned filler adjectives or verification phrases (WCPM Appendix A.4/A.5 word lists, CC cures); labels name the action or the thing, in the product's own vocabulary.
9. **FE-009 — The rendering surface serves search honestly.** Titles, meta descriptions, and structured data are rendered from the page's real content (WCPM §10 rendering surface; G-SCH family is designed to pass here, content owned by D9). Metadata describing content the page does not contain is a fabrication, not SEO.
10. **FE-010 — Works degraded before it works pretty.** Every page must function at 320px wide, on keyboard alone, and with images or scripts failed, before visual enhancement is layered on. Enhancement is progressive by construction.

## BAN list

- **BAN-FE-001 — AI artifacts in shipped photography.** Banned: publishing an image with malformed hands, gibberish in-image text, or warped logos. Defeats: DET-VIS-024. Bad: a generated "team at work" hero whose laptop screen shows melted lettering and whose subject has six fingers. Instead: use real photography or a clearly illustrative graphic with no fake text or hands. Severity: BLOCK.
- **BAN-FE-002 — The clickable div.** Banned: `div`/`span` elements with click handlers standing in for buttons or links. Defeats: DET-VIS-032. Bad: `<div class="card" onclick="openPlan()">` — unreachable by keyboard, invisible to assistive tech, no focus state. Instead: a real `<button>` or `<a>` styled as the card's action. Severity: BLOCK.
- **BAN-FE-003 — The fake product mockup.** Banned: presenting a generic or blurred dashboard inside a browser/device frame as the product's UI. Defeats: DET-VIS-030. Bad: a hero showing a stock analytics dashboard in a browser chrome frame on a product that has no analytics view. Instead: a current, readable screenshot of the actual product, framed plainly or not at all. Severity: BLOCK.
- **BAN-FE-004 — The invented logo cloud.** Banned: rendering customer or "featured in" logos that are invented, misspelled, or not the real marks. Defeats: DET-VIS-034. Bad: a grayscale row containing a warped "Forbs" wordmark and three unrecognizable marks. Instead: real customer logos with permission, correctly drawn — or no logo row. Severity: BLOCK.
- **BAN-FE-005 — The unsourced stat band.** Banned: rendering a band of round metrics with no source, date, or methodology behind them. Defeats: DET-VIS-035. Bad: "10,000+ customers · 99.9% uptime · 4.9/5 rating" with no measurement anywhere in the project. Instead: specific, dated, sourced figures — or omit the band. Severity: WARN (escalates to a fabrication verdict under DET-CON-011 if no source exists).

## Gates

- **G-FE-001 — Performance budget in CI.** Verifies: FE-003, FE-005. Check: automated — Lighthouse CI assertions on key routes (`largest-contentful-paint` ≤ 2500ms, `cumulative-layout-shift` ≤ 0.1 as errors) plus a size-limit byte budget per route chunk. Local form (tool-form substitution): where Lighthouse CI is unavailable, run a local Lighthouse pass against the same routes and thresholds, or assert the byte budget locally with size-limit and record the metrics that cannot be measured locally as unmeasured rather than passed; record the substitution in progress.md, and the CI assertion remains required wherever CI exists. Pass: all assertions green (CI) or all locally assertable budgets green with unmeasured metrics recorded (local form). Fail: block shipment. Recorded in: progress.md. (Designed to pass the WCPM G-ENG engineering family.)
- **G-FE-002 — Accessibility floor scan.** Verifies: FE-001, FE-002, FE-010. Check: automated — axe-core run over key routes. Manual form (tool-form substitution): where no browser or axe-core runtime is available, perform the manual inspection instead — a keyboard-only traversal of the key routes at 320px with scripts disabled (FE-010), plus a source audit confirming landmarks and heading order (FE-001) and zero clickable `div`/`span` elements (FE-002) — and record it in progress.md as a tool-form substitution for this gate; the automated axe-core run remains required wherever tooling exists. Pass: zero critical violations (automated) or zero findings under the manual form. Fail: block shipment. Recorded in: progress.md.
- **G-FE-003 — Token-literal scan.** Verifies: FE-004. Check: automated — grep/stylelint pass over page and component style files for hex colors and raw px/ms literals outside the token source. Pass: zero hits. Fail: block until values move into tokens. Recorded in: progress.md.
- **G-FE-004 — Imagery inspection.** Verifies: FE-006, FE-007. Check: manual — inspect every photographic image at 100% zoom for hands, in-image text, and logos; read every rendered logo and statistic aloud against its source. Pass: no artifacts, every mark real, every figure sourced. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Enhancement as foundation.** The page only works once the framework hydrates and the animation library loads; with scripts failed it is a blank shell. Catch it: load the page with JavaScript disabled before calling it built (FE-010).
- **Budget amnesia.** The budget was checked on the first page and never again; by page ten the shared chunk has tripled. Catch it: the budget gate runs per route in CI, not once per project (G-FE-001).
- **Decoration dressed as evidence.** Abstract 3D blobs and smiling stock teams fill sections that should show the product. Catch it: for each image, name the real thing it depicts; "nothing specific" across a page is the tell (DET-VIS-023).
- **Copy by autocomplete.** Headings and labels assembled from filler adjectives ("seamless", "cutting-edge", "revolutionary") instead of the product's facts. Catch it: scan shipped UI copy against the WCPM A.4/A.5 lists (FE-008).

## Examples

- [Example 1 — A clickable card becomes a real button](examples/example-1.md) — corrects FE-002.
- [Example 2 — An unsized hero image becomes layout-stable](examples/example-2.md) — corrects FE-003.
- [Example 3 — A fake mockup and stat band become real evidence](examples/example-3.md) — corrects FE-007.

## Recall anchors

- Native elements first; a clickable div is a defect.
- The budget is a requirement, not a cleanup task.
- Render real data and real imagery, or render nothing.
- Works at 320px, keyboard-only, scripts failed — then pretty.
- Thresholds are cited from the registry, never restated.

## Checklist

- [ ] Landmarks, headings, and native controls carry the page structure (FE-001).
- [ ] No clickable divs or spans anywhere (G-FE-002, FE-002).
- [ ] Every image/video reserves its dimensions; CLS stays within budget (FE-003).
- [ ] Lighthouse CI and bundle budget are green for this route, or the local form is recorded as a tool-form substitution (G-FE-001).
- [ ] axe-core reports zero critical violations (G-FE-002).
- [ ] No raw color/spacing/duration literals outside tokens (G-FE-003).
- [ ] Every image inspected at 100%; no AI artifacts, no fake marks (G-FE-004).
- [ ] Every rendered statistic traces to a source with a date (FE-007).
