# theme-library

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-23
- **Sources:** this folder — `INDEX.md` (the library index and canonical-source rule), the four range indexes (`themes-001-025.md`, `themes-026-050.md`, `themes-051-075.md`, `themes-076-100.md`), the 100 canonical specs in `expanded/theme-NNN.md`, and `EXPANSION-STANDARD.md` (the depth standard every expanded spec was written and verified against)
- **Depends on:** design-intelligence (theme choice is a decision-record act), design-system, motion, scroll-experiences
- **Feeds into:** frontend-core, layout-responsive, component-library, typography, webgl-3d

## When to use / Do NOT use

- **Use when:** a build has a chosen theme (or a theme family from design-intelligence §1.2) and the builder needs the theme's full specification — its world and one law, palette anchors and derived tokens, type pairing, layout system, full motion system, signature animated elements with build specs, page application map, worked examples, anti-slop failures, quality gate, component inventory, copywriting voice, scroll choreography map, performance budget, and build order. This skill is the library itself: it supplies the worlds; design-intelligence decides which world and how far to bend it.
- **Do NOT use when:** no theme has been chosen yet and the open question is *which* theme or *how much* motion (design-intelligence decides; this skill is then read for the chosen theme's spec), the question is a token value (design-tokens), a single animation's technique (motion), or scroll mechanics in the abstract (scroll-experiences). Never build a themed page from memory, from a summary, or from the range indexes — they contain no specifications.

## Rules

1. **FE-341 — Build from the canonical expanded spec.** The canonical full specification for theme *N* is `expanded/theme-NNN.md` (zero-padded). Before designing anything, read the chosen theme's expanded file end to end. The four range files are indexes only — they list themes and point here; a build that follows an index entry, a summary, or the builder's memory of a theme is not a themed build (gate G-FE-171).
2. **FE-342 — The theme is chosen, not browsed into existence.** A theme enters a build only through a design-intelligence decision record (theme, layout family, dial, postures, one rejected alternative). If the record names a family, pick the specific theme by its material metaphor: the theme's world must be one the brand's own content can live in without explanation.
3. **FE-343 — The theme's one law governs.** Every expanded spec declares one law (§1 of the spec) and one declared record (§6.17 or its equivalent) from which every figure on the page derives. Honour both: no number, total, name, or date appears on the page unless it traces to the record, and totals must re-add exactly wherever they are printed (gate G-FE-172).
4. **FE-344 — Signature elements are built as specified, merged into content.** Each spec's §6 elements carry full build specs (structure, millisecond choreography, state matrix, breakpoints, edge cases, accessibility, tokens). Build them to spec, at the sizes and grid homes the spec assigns: an element must carry the content it accompanies — if removing it loses only decoration, it was pasted on (BAN-FE-172) — and it must never cover that content at any scroll position.
5. **FE-345 — The cursor is the system cursor.** No theme in this library uses a custom cursor. Hover and focus delight lives on the elements themselves, feather-light and transform-only; a cursor effect that can impede pointer movement is a defect, not a signature (BAN-FE-173).
6. **FE-346 — Content is readable with no JavaScript.** The page ships complete in the DOM: every heading, figure, table, and form is present and legible before any script runs. Animation is an enhancement layered over a finished page, never the mechanism that delivers content (gate G-FE-173).
7. **FE-347 — Every reveal has a watchdog fallback.** Any state a script arms (hidden, dimmed, unlit, unexposed) carries the spec's named watchdog: a timeout that forces the final, visible state if the animation path fails, stalls, or is interrupted. A reveal that can leave content invisible is a build failure (BAN-FE-174).
8. **FE-348 — The reduced-motion variant ships in the same pass.** Each spec defines per-element reduced-motion variants and a complete static state of the page. Build them with the page, not after it: under `prefers-reduced-motion`, the page is the same page — full content, final states, no loops (BAN-FE-175).
9. **FE-349 — One shared rAF loop, lerped progress.** All scroll-driven and ambient motion in a theme runs on a single requestAnimationFrame loop reading one smoothed (lerped) scroll progress, animating transform and opacity only. Raw scroll values are never applied per event, and no element runs a private loop against the page's rhythm.
10. **FE-350 — Nothing enters from outside the theme's world.** Every element, figure, and effect on the page comes from the theme's own spec and the brand's real content. Generic effect-library material — particle rain, blobs, waves, stock counters — is filler wherever it appears, however polished (the anti-filler law, EXPANSION-STANDARD.md).
11. **FE-351 — The spec's performance budget is a ceiling, not a target.** Build inside the page performance budget in the spec (§14): total weight, per-frame cost, particle/element caps, and its cut order when something must go. When budget and spectacle conflict, the budget wins and the dial drops (design-intelligence §3.2).
12. **FE-352 — Apply the theme whole, bend it by the rules.** Palette roles, type pairing, and element vocabulary are taken from the spec intact. Adapting a theme to another product type bends dial, layout family, and pacing only (design-intelligence §6) — never a reskin that keeps a different theme's skeleton under this theme's colours.

## BAN list

- **BAN-FE-171 — Building from the index, a summary, or memory.** Banned: producing a "themed" page from a range-index entry, a catalogue card, or what the builder remembers of the theme, without reading `expanded/theme-NNN.md`. Defeats: DET-VIS-006. Bad: a "Sonar Room" page built from its one-line catalogue description ships a generic dark dashboard with a sweep graphic — the formula hero wearing the theme's name. Instead: read the canonical spec end to end first (FE-341); the decision record cites the expanded file. Severity: BLOCK.
- **BAN-FE-172 — Pasted-on spectacle.** Banned: animated elements imported from a generic effects library or invented ad hoc, instead of the theme's own §6 signature elements built to spec. Defeats: DET-VIS-028. Bad: floating blobs and a particle starfield behind a ledger theme's pricing table, because "the page felt empty". Instead: build the spec's elements from the content's own material, sized into the grid — or leave the space quiet (FE-344, FE-350). Severity: BLOCK.
- **BAN-FE-173 — The heavy custom cursor.** Banned: any custom cursor — trailing, magnetic, morphing, or lagged — in a themed build. Defeats: DET-VIS-042. Bad: a glowing jar follows the pointer at 200 ms lag through a census page; visitors overshoot every link. Instead: the normal system cursor, with feather-light hover responses on the elements themselves (FE-345). Severity: BLOCK.
- **BAN-FE-174 — The stranding reveal.** Banned: shipping any reveal, exposure, or aggregation whose failure path can leave content invisible, dimmed, or unformed. Defeats: DET-VIS-032. Bad: headings sit at opacity 0 after a fast scroll because their trigger never fired and no watchdog exists; the page reads as broken, not premium. Instead: JS-gated pre-states only, each with the spec's named watchdog forcing the final state (FE-347). Severity: BLOCK.
- **BAN-FE-175 — Reduced motion as an afterthought.** Banned: shipping a themed page whose reduced-motion or no-JS state is missing, partial, or content-poor, with a promise to add it later. Defeats: DET-VIS-041. Bad: with reduced motion on, the hero's counted figure never forms and its section is an empty dark panel. Instead: build the spec's per-element reduced-motion variants and the complete static page in the same pass (FE-348). Severity: BLOCK.

## Gates

- **G-FE-171 — Canonical-source check.** Verifies: FE-341, FE-342. Check: manual — the decision record names the theme and cites its `expanded/theme-NNN.md`; spot-check the build's palette anchors, type pairing, and three signature elements against that file. Pass: every spot-check matches the spec. Fail: the build restarts from the spec. Recorded in: progress.md.
- **G-FE-172 — Record reconciliation.** Verifies: FE-343. Check: manual — pick the spec's declared record and re-derive every total printed on the page (hero figure, tables, footer); each must match the record or a function printed in the spec. Pass: all figures trace and re-add exactly. Fail: block the milestone; the untraced figure is removed or corrected at the record. Recorded in: progress.md.
- **G-FE-173 — Never-invisible drill.** Verifies: FE-346, FE-347, FE-348. Check: manual + browser — load the page with JavaScript disabled, then with reduced-motion emulated, then scroll at maximum speed with scripts on. Pass: in all three passes the full content is present and readable, and every armed state resolves to its final state. Fail: block shipment. Recorded in: progress.md.
- **G-FE-174 — Budget and loop audit.** Verifies: FE-349, FE-351. Check: manual + device — profile the page on a mid-range phone: one rAF loop drives scroll-linked motion, transform/opacity only, totals inside the spec's §14 budget. Pass: budget holds with the cut order untriggered or applied as specified. Fail: apply the spec's cut order; never cut content or the reduced-motion variant. Recorded in: progress.md.

## Anti-patterns

- **Theme tourism.** Skimming five specs and mixing their elements into one page. Catch it: G-FE-171 — one theme per site world; borrowed elements fail FE-350 on sight.
- **Spec drift.** The build starts from the spec, then improvises durations, palettes, and element behaviour "to taste" until it matches nothing. Catch it: spot-checks at G-FE-171 compare the build to the file, not to the builder's intent.
- **Index as spec.** Treating a range file's one-line entry as enough to build from because the expanded file is long. Catch it: the indexes state their own rule — they contain no specifications (BAN-FE-171).
- **Demo as ceiling.** Copying a theme's living demo page instead of building from its spec for the actual content. Catch it: the demo proves the level; the spec, applied to the real content, is the deliverable (FE-344).

## Examples

The files in `examples/` show this skill being applied — choosing from the index, building from the canonical spec, and rescuing a build that skipped it.

- `examples/example-1.md` — Theme #71 The Bioluminescent Census: a generic dark dashboard replaced by the census built from `expanded/theme-071.md`, every glow traced to the sheet's record.
- `examples/example-2.md` — Finding and opening a theme: index card and memory on one side; the canonical expanded spec and a decision record on the other.
- `examples/example-3.md` — A stranding reveal in a themed build, fixed with the spec's watchdog pattern and the reduced-motion variant it already defined.

## Recall anchors

- The canonical spec is `expanded/theme-NNN.md`; the range files are indexes, not specs.
- Every figure traces to the theme's one declared record — or it is cut.
- The cursor is the system cursor; delight lives on the elements.
- JS off and reduced motion are the same page: complete, readable, final states.
- One theme, one law, one shared loop — nothing enters from outside the theme's world.

## Checklist

- [ ] Theme chosen through a design-intelligence decision record; rejected alternative recorded (FE-342).
- [ ] The theme's `expanded/theme-NNN.md` read end to end before designing (FE-341).
- [ ] Palette anchors, type pairing, and element vocabulary taken from the spec intact (FE-352).
- [ ] Every §6 signature element built to spec and merged into the content it accompanies (FE-344).
- [ ] Every printed figure traces to the theme's declared record; totals re-add (G-FE-172).
- [ ] System cursor only; hover/focus delight is feather-light and on-element (FE-345).
- [ ] Page complete and readable with JavaScript disabled (FE-346).
- [ ] Every armed state carries its named watchdog fallback (FE-347).
- [ ] Reduced-motion variant built in the same pass; static page is complete (FE-348).
- [ ] One shared rAF loop, lerped progress, transform/opacity only (FE-349).
- [ ] Page inside the spec's §14 performance budget; cut order followed if triggered (FE-351, G-FE-174).
