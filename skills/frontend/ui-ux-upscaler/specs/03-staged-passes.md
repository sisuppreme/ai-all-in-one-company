# UI/UX Upscaler — Spec 03: Staged Passes

> Companion spec to `skills/frontend/ui-ux-upscaler/SKILL.md`. Expands Protocol
> v1.3.0 Step 4 (7 staged passes, whole project, in order) and Step 6 (score gate loop).
> **SCOPE: web apps ONLY** (native: adaptation note in `02-theme-decision.md` §8 only).
> **Architecture-leak rule:** every pass is checked against `09-architecture-leak.md` —
> a pass that introduces or preserves a leak fails its exit criteria, whatever else it fixes.
> Retrofit skills (verified paths, 2026-11-24): `skills/ai-features/ai-retrofit/SKILL.md`,
> `skills/developer-experience/project-takeover/SKILL.md`,
> `skills/developer-experience/prototype-hardening/SKILL.md`. The Protocol names them
> without paths; the paths above are the corrected locations — do not use the
> `skills/frontend/` paths a reader might guess.

## 1. Pass discipline (applies to all 7 passes)

1.1 **Whole app before next pass.** Each pass runs across the ENTIRE project before the
next starts. A pass finished on the landing page only is not a pass. Per-route rollout
is allowed inside a pass (see `07-frameworks.md` §6), but the pass does not exit until
every route family has been through it or is explicitly listed as out of scope with a reason.

1.2 **One pass, one concern.** A pass changes its own concern and nothing else. If Pass 2
(typography) discovers a broken layout, the layout defect is logged for Pass 3 — not
fixed in Pass 2. Cross-pass fixes are how upgrades become unreviewable diffs.

1.3 **Verification is a test, not a look.** Every pass exit criterion names the check
(screenshot pair, grep count, automated test, measurement). "Looked good" verifies nothing.

1.4 **Rollback point per pass.** Before each pass, tag the commit (`upscale/pass-N-start`).
A pass that fails its exit criteria is reverted to its tag and re-attempted — never
patched forward on top of a failed pass.

1.5 **Leak gate per pass.** At each pass exit, run the leak checklist
(`09-architecture-leak.md` §5) on everything that pass touched. Leak count must not
increase in any pass; the final pass must reach 0.

## 2. Pass 1 — Design tokens

- **Entry criteria:** audit file exists with BEFORE score (§1 of `01-audit-and-scoring.md`);
  theme decision recorded (`02-theme-decision.md` §7); token-extraction table (Branch A)
  or theme palette table (Branch B) in hand.
- **What changes:** one token source file (CSS custom properties, or the framework's
  token layer — see `07-frameworks.md` §2). Colour, spacing (8 pt scale), radii, shadows,
  durations, easings. Every hard-coded value in app code moves into it. Token names use
  user/material concepts (`--paper`, `--ink`, `--accent`) — never stack terms
  (`--postgres-blue` is a leak; `09-architecture-leak.md` §2).
- **Forbidden to change:** any rendered value's *meaning* — a token pass renames the
  source of a value, it does not redesign the value. If a colour must change for contrast,
  that is a Pass 1 exception recorded in the audit with the before/after ratio; bulk
  redesign belongs to Passes 2–4.
- **Checklist:** [ ] token file created, single source; [ ] grep hard-coded hex outside
  token file + third-party CSS = 0; [ ] grep hard-coded spacing px outside tokens = 0
  (except 1 px hairlines, recorded); [ ] grep improvised durations/easings outside
  motion tokens = 0; [ ] dark-mode / `prefers-color-scheme` behaviour specified per token;
  [ ] token names reviewed for leaks (checklist `09-architecture-leak.md` §5.4).
- **Exit criteria + verification:** the three greps above all return 0; a before/after
  screenshot diff at 1440 px and 390 px shows zero unintended visual change (pixel-diff
  on non-token areas < 0.5% of pixels; any larger diff is investigated, not assumed).
  Token file reviewed against the theme spec's palette table (Branch B) or extraction
  table (Branch A) — every theme anchor has a token, every token has a role.
- **Common failure modes:** (a) *Token sprawl* — 80 tokens for 12 values. Fix: collapse
  by role; a token nobody can name the job of is deleted. (b) *Shadow tokens* — a second
  token file in a component library. Fix: one source; the library consumes it.
  (c) *Hard-coded values in inline styles / generated class strings.* Fix: codemod
  (`07-frameworks.md` §5); count them in the audit first.
- **Retrofit fit:** `ai-retrofit` — tokenisation is the lowest-risk retrofit: presentation
  only, behaviour untouched. Apply its "strangler" pattern: tokenise one route family
  at a time behind the pass, keeping the old values as the token file's initial values.

## 3. Pass 2 — Typography

- **Entry criteria:** Pass 1 exited (greps at 0). Type-scale recovery (Branch A, `02` §3.2)
  or theme type table (Branch B) in hand.
- **What changes:** one modular scale (ratio 1.25 or 1.333, recorded); body 16–18 px;
  display/heading/body/caption/data registers; line-length rules (45–75 ch prose);
  contrast fixes (any text < 4.5:1 body / 3:1 large is fixed here, not later);
  copy-voice fixes where copy leaks architecture (error/empty-state strings rewritten
  to user concepts — `09-architecture-leak.md` §6; the rewrite list comes from the audit).
- **Forbidden to change:** layout, component structure, motion. A heading that needs
  a different size gets the scale step — not a layout change to accommodate it.
- **Checklist:** [ ] every rendered size is on-scale (inventory re-run, 0 off-scale
  without a recorded exception); [ ] line length 45–75 ch on prose routes (measure 3
  routes per family); [ ] contrast ≥ 4.5:1 body / 3:1 large at every state (measure,
  don't eyeball — including over animated backgrounds at mid-reveal); [ ] tabular
  numerals where numbers are compared; [ ] leak strings rewritten (audit §3 table
  rows marked fixed); [ ] display face loads within budget (see `05` §7 — font weight
  ≤ 200 KB total, `font-display: swap`).
- **Exit criteria + verification:** type inventory re-run returns 0 unexcepted off-scale
  sizes; contrast audit (automated, all routes) returns 0 failures; 3-second test on
  every landing viewport passes (the type hierarchy, not just the copy, answers the
  three questions). Readability category (gate Cat. 3) re-scored: must move up ≥2 points
  from BEFORE or reach ≥9 — if it does not, the pass did not do its job; re-open it.
- **Common failure modes:** (a) *Scale drift returns* — a component imports its own
  sizes. Fix: lint rule blocking font-size literals outside the token file.
  (b) *Contrast fixed at rest, broken mid-animation.* Fix: measure at mid-reveal and
  scrolled-past states too (S-11). (c) *Copy rewritten for style, breaking meaning.*
  Fix: rewrite only leak/voice violations; working copy stays.
- **Retrofit fit:** none structural — typography is presentation. `prototype-hardening`
  applies only in that its "example" discipline (real content, never lorem) governs
  the contrast/line-length checks: measure on real copy, never placeholder text.

## 4. Pass 3 — Layout & responsive

- **Entry criteria:** Pass 2 exited. Layout family from the theme decision in hand;
  breakpoint inventory (every route's behaviour at ≥1200 / 768–1199 / <768 px) from the audit.
- **What changes:** grid (one grid per page family, per the theme's layout language);
  spacing rhythm (8 pt scale, proximity ratio ≥2:1 between groups vs within groups);
  section pacing (alternate dense/quiet; padding assigned by role, never uniform);
  breakpoint behaviour per route (what collapses, what stacks, what is cut at each size);
  overflow elimination (no horizontal scroll at any width 320–2560 px).
- **Forbidden to change:** component internals, motion, copy. A card that overflows at
  390 px gets a layout fix (stack, shrink, wrap) — not a smaller font (that would be a
  Pass 2 change smuggled into Pass 3).
- **Checklist:** [ ] no horizontal overflow at 320, 360, 390, 768, 1024, 1280, 1440, 1920 px
  (automated screenshot sweep); [ ] proximity ratio ≥2:1 verified on 3 sections per
  family; [ ] pacing plan written (dense/quiet map for every long page — at least every
  third section quiet); [ ] one grid, at most one deliberate break per page (named in
  the decision record); [ ] footer designed as a section (same focal order, theme language);
  [ ] pinned/sticky elements measured: unobstructed content height at 640 px viewport
  height ≥ 55% of the viewport (pin accumulation check, scroll-experiences anti-pattern).
- **Exit criteria + verification:** overflow sweep 0 failures; pacing map exists for every
  page >2 viewports; screenshot pairs (1440/390) for every route family reviewed against
  the theme's layout language. Hierarchy category (Cat. 1) re-scored: must move up or
  reach ≥8 — layout is the main lever on Cat. 1.
- **Common failure modes:** (a) *Desktop-only layout* — 390 px checked last and fails.
  Fix: check 390 px first in this pass, not last. (b) *Uniform padding persists*
  (S-2). Fix: assign padding by section role in the pacing map, then implement.
  (c) *Pin accumulation* — header + toolbar + summary card eat the viewport.
  Fix: pin budget — at most 2 pinned elements per page, total pinned height ≤ 120 px at 390 px.
- **Retrofit fit:** `project-takeover` — layout is where a taken-over codebase's structural
  debt lives (nested grids, competing breakpoints). Apply its inventory-first rule: map
  every breakpoint rule before changing any of them; a breakpoint deleted without an
  inventory entry is a regression waiting for a viewport nobody tested.

## 5. Pass 4 — Components & UI states

- **Entry criteria:** Pass 3 exited. Component inventory from the audit (§1 §1) in hand.
- **What changes:** every component gets its full state set per `04-component-upgrades.md`
  §1 matrix (rest/hover/focus/active/disabled/loading/empty/error) with tokens consumed,
  breakpoint behaviour, and accessibility spec. Behaviour contract preserved: the
  component must do exactly what it did before, only better presented
  (`04-component-upgrades.md` §1.3). Labels, empty states, and error messages rewritten
  to user-facing concepts only — error states must never name endpoints, schemas, tables,
  or services (`09-architecture-leak.md` §6; `04-component-upgrades.md` §2).
- **Forbidden to change:** behaviour, data, routes, APIs. A component whose behaviour
  must change for the upgrade to work is stopped, justified in the audit file, and
  approved before it is touched (Protocol Step 2).
- **Checklist:** [ ] every component in the inventory has a spec in `04` applied and a
  state-matrix check (each state rendered and screenshotted at 1440/390); [ ] focus
  visible on every interactive element (keyboard walk, all routes); [ ] touch targets
  ≥44×44 px; [ ] loading states use skeletons matching the layout for waits ≥300 ms,
  nothing for waits <300 ms; [ ] empty states carry a next action; [ ] error states
  name the user's next step, never the stack; [ ] leak check on every label/error/empty
  string touched (0 leaks).
- **Exit criteria + verification:** state-matrix screenshots for every component (7 states
  × 2 viewports where applicable); keyboard walk 0 traps, 0 invisible focus; automated
  axe pass 0 critical/serious. Integration category (Cat. 2) re-scored — components are
  its main lever after signature elements.
- **Common failure modes:** (a) *States designed for the happy path only* — loading and
  error states left as the browser default or a blank area. Fix: the matrix is the spec;
  a missing state is a failed component, not a minor gap. (b) *Hover-only states*
  (S-13). Fix: every hover state gets a tap/scroll equivalent in the same pass.
  (c) *Behaviour drift* — a "visual" change alters what a button does. Fix: behaviour
  contract test per component before/after (same clicks, same outcomes).
- **Retrofit fit:** `prototype-hardening` — its hardening discipline (real data, edge
  cases, failure modes per component) is the Pass 4 test method: test each component
  with real content, long content, empty content, and error content — never lorem.

## 6. Pass 5 — Motion system

- **Entry criteria:** Pass 4 exited. Motion system spec in hand (`05-motion-system.md`):
  every term with job, durations, easings, triggers; dial per page family (`02` §5).
- **What changes:** the full motion system, in the theme's own material language, on
  every page: scroll-triggered reveals (varied, never uniform fade-up), scroll-driven/
  scrubbed animation, parallax where the theme calls for it, staggered + masked reveals,
  counters for real numbers only, micro-interactions, page transitions, skeleton loading.
  The heavy custom cursor is REMOVED here (not lightened — removed; system cursor only).
  Every animation ships with its reduced-motion variant in the same pass.
- **Forbidden to change:** layout, component structure, copy. Motion rides on the
  existing structure; if motion needs a layout change, the layout change goes back to
  Pass 3 with a reason — it is not smuggled into Pass 5.
- **Checklist:** [ ] every animation names its job (design-intelligence §3.1 table);
  [ ] ≤1 attention moment per viewport; [ ] durations/easings resolve to motion tokens
  (lint 0 hits); [ ] transform/opacity only (0 layout-property animations without a
  recorded exception); [ ] one shared lerped rAF loop, no raw scroll handlers per element;
  [ ] every reveal JS-gated with force-reveal fallback (watchdog / timed reveal /
  visible-by-default — see `05` §6); [ ] reduced-motion variant per animation, same pass;
  [ ] cursor: system cursor confirmed, `cursor: none` grep = 0; [ ] no animation delays
  input (act-during-transition test on every primary action).
- **Exit criteria + verification:** motion-token lint 0 hits; observer-stub test strands
  0 sections; reduced-motion emulation pass 0 continuing non-essential animations;
  fast-scroll + trackpad profile on a mid-range throttled profile shows no jitter.
  Motion smoothness (Cat. 4) and Never-invisible (Cat. 6) re-scored: Cat. 6 must reach
  10 at this pass's exit — if it does not, Pass 5 has not exited, whatever else passed.
- **Common failure modes:** (a) *Global fade-up returns* (BAN-FE-041). Fix: delete it;
  entrances are per-section, varied, choreographed. (b) *Dial creep* — a dial-2 page
  acquires dial-4 techniques one "small" exception at a time. Fix: the dial table is
  the law; exceptions need a written reason. (c) *Reduced motion "planned for later".*
  Fix: it ships in the same commit as the animation (BAN-FE-042) or the animation does
  not ship. (d) *Cursor "lightened" instead of removed.* Fix: remove it; a feather-light
  cursor is permitted only with zero perceptible lag and is never the default.
- **Retrofit fit:** `ai-retrofit` — motion is the highest-risk retrofit for behaviour
  (it can gate content). Apply its incremental rule: motion lands per route family
  behind a flag (`07-frameworks.md` §6), with the no-JS + observer-stub tests run per
  family before the flag flips.

## 7. Pass 6 — Scroll experiences

- **Entry criteria:** Pass 5 exited. Scroll-system spec in hand (`05-motion-system.md`
  §3): reveals, scrub, parallax, progress (in-theme), pins where earned.
- **What changes:** the page's scroll as a designed system — scroll-triggered reveals
  choreographed per section, scroll-driven/scrubbed sequences, parallax layers (≤3 depths),
  in-theme progress indication (a filling vessel, a route line, a depth gauge — a bare bar
  only when the theme is genuinely minimal), pinned sections where a moment earns the
  viewport. One shared lerped loop drives all of it (the Pass 5 loop — no second loop).
- **Forbidden to change:** scroll behaviour itself — no scroll-jacking (no forced snapping,
  no hijacked wheel/touch, no auto-advance); the scrollbar remains the user's. No motion
  values (Pass 5 owns them); no layout (Pass 3 owns it).
- **Checklist:** [ ] no per-frame scroll handlers doing layout work (grep 0 unexcused);
  [ ] no raw scrollY application (single smoothed progress source, lerp — see `05` §3);
  [ ] progress never communicated by a bare bar alone (structure carries position:
  headings, landmarks, TOC where warranted); [ ] pinned sections respect focus
  (WCAG 2.4.11 — pinned header shrinks/yields, never covers the focused element);
  [ ] pins tested at 360×640 and 1280×600 (no clipped hero content, BAN-FE-054);
  [ ] reduced motion turns all scroll effects off (emulation pass); [ ] no dead
  stretches (ambient scroll-aware life at every depth, or deliberate stillness recorded).
- **Exit criteria + verification:** full-page scroll profile (fast, slow, trackpad-stepped)
  on a mid-range throttled profile: 0 scroll-linked long tasks, 0 visible jitter;
  no-JS visibility pass: all routes fully readable; force-reveal fallback test
  (observer disabled + anchor jumps): 0 stranded sections. Aliveness (Cat. 8) re-scored:
  must reach ≥7 — scroll is its main lever on long pages.
- **Common failure modes:** (a) *Demo scroll* — impressive in a recording, miserable to
  read. Fix: read the page top-to-bottom at your own speed; friction you feel is the
  defect (scroll-experiences FE-105). (b) *Pin accumulation.* Fix: pin budget from
  Pass 3, enforced again here. (c) *Progress bar as wayfinding* (FE-106). Fix: remove
  the bar mentally — if position is unknowable, the structure failed; fix the structure.
- **Retrofit fit:** `project-takeover` — scroll is where taken-over code hides its worst
  handlers. Its inventory-first rule applies: grep every scroll listener before changing
  any of them; the shared loop replaces them one family at a time, with the profile
  re-run after each family.

## 8. Pass 7 — Polish (signature elements)

- **Entry criteria:** Pass 6 exited. Signature-element specs in hand
  (`06-signature-elements.md`): 5–20 elements, each with a full spec (what/why, structure,
  ms choreography, state matrix, merge, fallback, reduced-motion variant, budget, mobile).
- **What changes:** the theme's signature elements, merged into the content itself
  (merge test, design-intelligence §3.3 — all four conditions). 3D where possible,
  otherwise excellently animated. Each element carries the app's real content/data.
  Elements are built from the app's user-facing concepts — never from its tables,
  endpoints, or modules (`09-architecture-leak.md` §4: an element named after a table
  fails this pass).
- **Forbidden to change:** anything structural. Polish adds elements into planned grid
  space; it does not move layout, change components, or add motion techniques. An
  element that needs layout space the grid does not have goes back to Pass 3 with a
  reason — it is not squeezed in here.
- **Checklist:** [ ] 5–20 elements, each passing all four merge tests (delete-test
  demonstrated, not asserted); [ ] each element has its full spec (§6 format) and its
  fallback verified (JS-off, observer-stub, reduced-motion); [ ] no element covers
  content at any scroll position at 1440 px or 390 px (S-19 check, both viewports);
  [ ] spectacle budget respected (≤1 spectacle moment per 3 viewport heights);
  [ ] performance budget held with all elements running (see `05` §7 — what gets cut
  first is decided here, in advance, not in a panic); [ ] footer designed as a section
  (Pass 3's work, verified again here — the footer is the last impression).
- **Exit criteria + verification:** merge-test evidence per element (screenshot with the
  element removed vs present, showing the information lost); S-19 sweep 0 overlaps;
  full scroll profile with all elements running holds the frame budget. Integration
  (Cat. 2) and Aliveness (Cat. 8) re-scored: both must reach threshold (≥8 / ≥7) —
  polish is their final lever. If either is below threshold after Pass 7, the elements
  are wrong (not merely unfinished): re-derive them from the content (`06` §2),
  do not add more decoration.
- **Common failure modes:** (a) *Pasted-on spectacle* (BAN-FE-162). Fix: rebuild into
  the content or cut it — never "make it subtler". (b) *Element covers content*
  (S-19, the Side A / Side B reel defect). Fix: size to the planned grid home with
  margins at every scroll position; content wins every overlap dispute.
  (c) *More elements = more premium.* Fix: the count is 5–20, but the test is the
  merge test — a 6th element that fails it makes the page worse, not better.
- **Retrofit fit:** `prototype-hardening` — its "real content, real data" discipline is
  the Pass 7 test: each element is verified against the app's real data (a ledger line
  that balances on real totals, a spine that holds the user's real place), never demo data.

## 9. The score-gate loop (Protocol Step 6)

After Pass 7, re-score the WHOLE app with the design-intelligence gate
(`01-audit-and-scoring.md` §5): total ≥64/80, every category at threshold, hard
categories (6, 7) at 10, **and leak score 0** (`09-architecture-leak.md` §5 —
any leak is a gate FAIL veto regardless of the /80 score). If it fails: fix the
lowest-scoring category first, re-score the whole app (pre-fix scores void), loop.
Do not declare completion below the gate. Do not average away a hard-category or
leak failure with high scores elsewhere. The loop's iterations are recorded in the
audit file §8 (pass, category fixed, before/after per category, date).

## 10. Cross-reference map

| Pass | Main spec | Retrofit skill (verified path) |
|---|---|---|
| 1 Tokens | `07-frameworks.md` §2, §5 (codemod) | `skills/ai-features/ai-retrofit/SKILL.md` |
| 2 Typography | `04-component-upgrades.md` §2 (copy/label rules) | — |
| 3 Layout | `02-theme-decision.md` §5 (dial per family) | `skills/developer-experience/project-takeover/SKILL.md` |
| 4 Components | `04-component-upgrades.md` (full) | `skills/developer-experience/prototype-hardening/SKILL.md` |
| 5 Motion | `05-motion-system.md` (full) | `skills/ai-features/ai-retrofit/SKILL.md` |
| 6 Scroll | `05-motion-system.md` §3, §6 | `skills/developer-experience/project-takeover/SKILL.md` |
| 7 Polish | `06-signature-elements.md` (full) | `skills/developer-experience/prototype-hardening/SKILL.md` |
