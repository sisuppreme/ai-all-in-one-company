# Theme 10 — Risograph Confessional (Expanded, v1 + v2 standard)

## 1. Concept & world

The site is a two-colour risograph zine, printed in a community hall on a
Saturday, and it never pretends otherwise. A risograph is a stencil duplicator:
one ink drum at a time, one pass per colour, and the second pass never lands
exactly on the first. Risograph Confessional takes that mechanical honesty —
fluorescent pink laid down first, teal a beat later, the two layers sitting a
frank 3px out of register — and treats it as luxury. The imperfection is not a
filter applied over a clean design; it is the printing process itself, and the
content is what gets printed.

The "confessional" half is the editorial stance. A zine is where a scene admits
things: the band admits the tour lost money, the print shop admits the drum
jammed on sheet 40, the nonprofit admits what the grant actually bought. Every
page in this theme is structured as an admission with evidence — a shouted
headline that confesses, body copy that explains plainly, and hard numbers
(copies printed, copies left, dates, prices) set like print-run data. The
theme persuades by candour, not polish. A visitor should feel they are holding
a sheet that was stacked on the hall table an hour ago, still smelling of ink.

The world has strict physics, and the whole expansion obeys them:

- **Two inks only.** Fluoro pink and teal, plus drum black for text and paper
  for ground. There is no third ink, ever. Photographs are printed *in* the
  two inks (duotone), the way a real riso would print them.
- **Print is permanent.** Once a section has printed, it never un-prints.
  Scrolling back up shows the finished sheet, not a re-run of the press.
- **Text is single-pass.** Body text is printed once, in drum black, fully
  present from first paint. Only chromatic layers (colour blocks, image
  passes, display-headline ink copies) go through the two-pass ceremony.
  Nobody waits for a pass in order to read.
- **The machine is visible.** The drum that prints the page sits in the
  margin and turns as you scroll; the staple that binds the zine sits in the
  corner and never moves. The page admits it is being manufactured.
- **Flaws are credited, not hidden.** One leaf is printed upside down on
  purpose, and the colophon says why. Each build picks its own one flaw and
  credits it the same way.

**Best-fit sites and audiences**

- Indie music labels and bands: releases, tour diaries, merch drops with real
  pressing numbers ("300 copies, 41 left"). The audience already collects
  physical objects and reads misregistration as authenticity.
- Zine fairs, print shops, and riso studios: catalogues, price-per-copy
  tables, workshop bookings. The site is a working sample of the product.
- Youth nonprofits and community arts organisations: annual reports written
  as confessions, campaign pages, sign-up drives. Candour is the fundraising
  voice; the print-run data maps onto real impact numbers.
- Campus and DIY-scene organisations: gig listings, open calls, manifestos.
- Small publishers of pamphlets, poetry chapbooks, and comics: anywhere the
  edition size is a fact worth shouting.

**When NOT to use it**

- Brands whose promise is precision: fintech, medical, legal, enterprise
  SaaS, precision engineering. Deliberate misregistration reads as error
  there, not honesty, and no amount of craft will save it.
- Quiet luxury (jewellery, hotels, fragrance): this theme shouts in Archivo
  Black and crawls with grain. It is loud luxury — a different product.
- Photography-led portfolios: images here are two-ink duotones at sheet
  size. A photographer who needs faithful colour should choose another theme.
- Data-dense tools and dashboards: pasted sheets, torn edges, and a rotating
  drum fight tables, filters, and dense controls at every turn.
- Anything that must feel corporate-neutral or government-official. The
  confessional voice is first-person and opinionated by design.
- Clients who cannot supply true numbers. The theme runs on print-run facts;
  invented scarcity ("almost gone!") is exactly the slop §9 bans.

## 2. Palette

Two inks, one black, one paper. All colour is flat ink — no gradients except
the two specified exceptions (ink pooling at image edges, §6.9, and the
fluoro shimmer on dark sheets, §6.8), which are print phenomena, not lighting.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--paper` | `#F4EFE4` | Page ground; the unprinted sheet | ~62% of any viewport | Ground for everything. Carries `--ink` at 13.7:1 and `--teal` at 4.6:1. |
| `--ink` | `#232323` | Drum black: ALL body text, rules, data, the dark sheets | ~20% | On `--paper` 13.7:1 — AAA at every size. The only colour body text may use on light sheets; on dark sheets text flips to `--paper` (13.7:1 the other way). |
| `--pink` | `#FF4FA3` | Fluoro pink: first pass, highlights, stamps, edition badges, focus halo (decorative) | ~10% | On `--paper` only 2.6:1 — **never text, never the sole carrier of meaning**; graphics and large display ink only. On `--ink` 5.2:1, so pink MAY set large display words on dark sheets. Black text on a pink fill is 5.2:1 (AA) — the badge/button pairing. |
| `--teal` | `#007A6E` | Teal: second pass, links, secondary text accents, totals, focus ring | ~8% | On `--paper` 4.6:1 — passes AA for normal text, narrowly; teal text is therefore allowed but never below 14px and never for long passages (use `--ink`). On `--ink` only 3.0:1 — large text and graphics only on dark sheets. |

**Derived tokens** (mixes of the four anchors, labelled derived wherever used):

| Token | Derivation | Use |
|---|---|---|
| `--sheet` | `#FAF6EA` (paper lightened one step) | The pasted-sheet surface; distinguishes a sheet from the ground it lies on. |
| `--ink-soft` | `color-mix(in srgb, var(--ink) 72%, var(--paper))` | Secondary text: captions, metadata. ~7.3:1 on paper — AA at all sizes, AAA at ≥14px. The theme's only "grey", and it is made of ink, not a fifth colour. |
| `--teal-deep` | `#00594F` | Teal hover/active states and teal text on `--sheet`. ~6.4:1 on paper. |
| `--pink-wash` | `color-mix(in srgb, var(--pink) 16%, var(--paper))` | Marker-highlight swipes behind emphasised phrases; never behind body text below 20px. |
| `--teal-wash` | `color-mix(in srgb, var(--teal) 12%, var(--paper))` | Table total rows, selected tab ground. |
| `--splat` | `var(--pink)` at 55% opacity | The ink-stamp click bloom (§6.11) and error bullets (§6.16). |

**Ink-layer geometry.** Misregistration is a token, not a vibe:
`--misreg-x: 3px; --misreg-y: 2px`. At rest the pink layer sits at
(−3px, −2px) and the teal layer at (+3px, +2px) relative to the drum-black
content — a 6px total spread, quoted everywhere as "the honest 3px" (3px per
layer). These two tokens are the only offsets any element may use; an element
that invents a 5px or 8px offset fails the quality gate.

**Dark-mode behaviour.** The theme has no inverted mode; its dark passages
are drum-black *sheets* chosen editorially (§4 caps them at one dark sheet in
three). If the host product forces a system dark mode, the mapping is: ground
`#1B1B1B`, sheet `#262620`, text `--paper` on both (12.9:1 / 11.6:1), pink and
teal unchanged (fluoro inks genuinely glow on dark stock — pink holds 5.6:1
on `#1B1B1B`), teal text demoted to large-only (3.2:1) with body links
switching to pink underlined. Every motion spec in §5–§6 survives unchanged;
only the ground tokens swap.

**Pairing rules (hard)**

- Pink never touches paper as text, and never sits directly on teal (the two
  inks overlap only as offset layers of the same shape, where the overlap
  zone reads as a third, darker print tone — that overlap is the point of the
  theme and the only place the inks may "mix").
- A sheet carries at most one pink-dominant element. Pink is the shout; two
  shouts per sheet is a fight.
- Dark sheets use paper text and pink display ink; teal appears there only
  as the offset layer and large data (3.0:1 floor respected).

## 3. Typography

Two faces. **Archivo Black** — a single-weight grotesque (400 only; there is
no bold, and faux-bold is banned) — does all shouting: display headlines,
counters, prices, edition data. **Space Grotesk** (400/500/700) does
everything else: body, labels, forms, navigation. A riso drum prints what is
on the stencil; these two stencils are the whole press.

| Role | Face / weight | Size | Line-height | Tracking | Notes |
|---|---|---|---|---|---|
| Shout (display) | Archivo Black | `clamp(3.25rem, 10.5vw, 7.5rem)` | 0.92 | −0.015em | UPPERCASE always. Max 5 words per line, max 3 lines. Carries the pink/teal ink copies (§6.2). |
| Sheet headline (H2) | Archivo Black | `clamp(2rem, 5vw, 3.75rem)` | 1.0 | −0.01em | UPPERCASE. Torn-paper reveal (§6.6). One per sheet. |
| Sub-head (H3) | Space Grotesk 700 | 1.25rem / 20px | 1.25 | 0.01em | Sentence case. The calm voice under the shout. |
| Body | Space Grotesk 400 | 17px (16px <768px) | 1.55 | 0 | Measure 58–68ch. Single-pass drum black, always. |
| Confession lead | Space Grotesk 500 | 20px | 1.5 | 0 | The first paragraph of a sheet, set larger — the admission before the details. |
| Label / apparatus | Space Grotesk 500 | 12px | 1.4 | 0.14em | UPPERCASE. Issue lines, sheet numbers, form labels, table heads. |
| Data / counters | Archivo Black | 20–56px by context | 1.0 | 0 | Print-run numbers, prices, "% inked". Reserve width with `min-width` in ch so counting never reflows the line (Archivo Black has no tabular figures; the reservation is the fix, stated here so no builder "solves" it by changing face). |
| Price / edition line | Space Grotesk 700 | 15px | 1.35 | 0.02em | "£6 — 214 COPIES LEFT" style lines under cards. |

**Type rules (hard)**

- Archivo Black is never set below 20px. Below that it turns to mud under
  grain; small emphasis is Space Grotesk 700's job.
- The shout word (§6.7) is a single word inside a shout headline, never the
  whole headline.
- Italic does not exist in this press. Emphasis = pink-wash highlight swipe
  (body) or the teal pass underline (links and key phrases).
- Numbers in prose are always real and always specific: "214 copies", never
  "lots of copies" (§12).

## 4. Layout language

**The sheet stack.** The page is a stack of pasted sheets on the hall table
(the `--paper` ground). Each section is a `.sheet`: `--sheet` surface, 2px
`--ink` border, and a hard offset shadow — `10px 10px 0 color-mix(in srgb,
var(--pink) 32%, transparent)` on light sheets, teal on every third sheet so
the stack alternates its shadow ink. Hard shadows only; a soft blurred shadow
is a photograph of a sheet, not a printed one, and fails §9.

**Grid and rail.** Desktop (≥1200px): a 96px left rail holds the drum (§6.4);
content column max 1180px, sheets inset 24px from the rail. The staple (§6.5)
floats over the rail's top-left corner. Tablet (768–1199px): rail narrows to
64px. Mobile (<768px): the rail disappears; the drum moves into the fixed top
bar at 36px and the unspooling band becomes a 3px progress line across the
top of the viewport (§6.4 breakpoints).

**Rotation.** Decorative sheets (image-led, quote, banner) may rotate ±0.4°
alternating. Text-bearing sheets — anything with body copy, a form, or a
table — sit at exactly 0°. Rotation is a property of the paste-up, never of
reading matter. Rotated sheets must not cause horizontal overflow: the stack
container clips `overflow-x: clip` at the page level.

**Spacing rhythm.** 8px base. Sheet padding 40px desktop / 28px tablet /
20px mobile. Section gaps (table showing between sheets) 96px / 64px / 48px.
Inside a sheet, the confession lead follows the headline at 16px, body at
24px, data lines at 32px — the rhythm of a paste-up: shout, admit, prove.

**Density rules.** One shout per sheet. One dark sheet in three, maximum, and
never two dark sheets adjacent — the eye needs paper between printings.
Images occupy at most 45% of a sheet's area; this is a text press that
illustrates, not a gallery that captions.

**Whitespace as material.** The unprinted paper between sheets is where the
drum band, the joins (§6.10), and the grain live. Gaps are never filled with
extra ornaments; an empty stretch of paper with grain crawling on it is a
finished surface in this theme.

## 5. Full motion system

All motion is the press working. If a movement cannot be explained as ink,
paper, drum, or staple, it does not ship. One shared `requestAnimationFrame`
loop drives every scroll-scrubbed value (drum rotation, band, parallax,
progress) with lerp smoothing; CSS transitions/animations handle everything
triggered. Nothing animates `width`, `height`, `top`, or `left` — transforms
and opacity only, with the two print exceptions (clip-path tear, §6.6, and
stroke draw, §6.10) that are GPU-cheap at these sizes.

**Named easings (the press's whole vocabulary)**

| Token | Curve | Used for |
|---|---|---|
| `--ease-pass` | `cubic-bezier(0.22, 1, 0.36, 1)` | Ink landing: passes, reveals, settles. Fast contact, soft landing — a sheet hitting the stack. |
| `--ease-spring` | `cubic-bezier(0.34, 1.45, 0.44, 1)` | The off-register settle (§6.2) and card lift (§6.15). Overshoot ≈1.2×, exactly one overshoot — the layer rocks once into its offset and stops. |
| `--ease-stamp` | `cubic-bezier(0.55, 0, 0.85, 0.36)` | Stamp squash (§6.11) press-down; release is `--ease-spring`. |
| `--ease-feed` | `cubic-bezier(0.65, 0, 0.35, 1)` | Sheet feeding: print-wipe (§6.12), mobile menu sheet (§6.13), torn reveal (§6.6). |
| linear | — | Everything scrubbed (drum, band, parallax) and the feed-strip loop (§6.18). Scrubbed motion is never eased; the visitor's scroll is the easing. |

**Duration tokens**

`--dur-pass: 300ms` (pink pass) · `--dur-gap: 350ms` (the beat between
passes) · `--dur-pass2: 420ms` (teal pass) · `--dur-align: 180ms` ·
`--dur-unalign: 300ms` · `--dur-tear: 500ms` · `--dur-draw: 350ms` ·
`--dur-stamp: 120ms` · `--dur-wipe: 500ms` · `--dur-shout: 700ms` ·
`--dur-settle: 600ms` (ink-pool images) · `--dur-count: 900ms`.

**The motion vocabulary, term by term**

| Term | In this theme's language | Spec |
|---|---|---|
| Scroll-triggered reveals | Two-pass section printing (§6.1) | Pink pass on entry (300ms), teal pass 350ms later (420ms). Trigger: IntersectionObserver at 20% of the sheet visible. |
| Parallax | Misregistration drift: the pink and teal layers drift ±2px against the black content across a sheet's viewport traversal, so registration itself breathes | Scrubbed in the shared rAF loop, lerp 0.12. Total spread never exceeds 10px. Cut entirely <768px. |
| Pinned scenes | The staple pins the viewport (§6.5); the drum pins the rail (§6.4). On the detail page, the edition-data block pins beside the story for one viewport height while its counters print | Pinning is `position: sticky` only — no scroll-jacking, ever. |
| Masked line reveals | Torn-paper headline reveals (§6.6) | Clip-path tear, 500ms `--ease-feed`, synced to the sheet's print. |
| Blur-to-sharp | Wet-ink focus: a freshly printed colour layer starts at 1.5px blur (wet stencil) and dries sharp as its pass completes | Applies to image passes (§6.9) and hero ink copies (§6.2) only. **Never** to text at any size — blurred text is unreadable text, and reading outranks effect. |
| Animated counters | Print-run counters: copies printed, copies left, "% inked" (§6.4, §6.14) | 900ms `--ease-pass` count on print; digits reserve width (§3) so the line never reflows. |
| Progress indicators | The drum's unspooling band + "% inked" figure (§6.4) | Scrubbed, lerp 0.16. The only progress UI on the page; no scrollbars, no dots. |
| Marquees | The feed strip (§6.18): an announcement band moving like paper through the press | 18s linear loop with a 2px judder at each seam. One per page, top only. |
| Ambient loops | Crawling grain (900ms steps cycle) and fluoro shimmer drift on dark sheets (9s) (§6.8) | Both pause when the tab is hidden; grain freezes (does not vanish) under reduced data/power signals. |
| Micro-interactions | Hover-to-align (§6.3), ink-stamp click (§6.11), pilcrow-free link underlines drawing in the teal pass colour (200ms) | Every interactive element has one; none exceeds 300ms except the stamp's splat fade. |
| Hover physics | Card tilt-and-lift (§6.15): max 2.5° tilt toward the pointer, −4px lift, shadow ink swaps pink→teal | Desktop pointer only; touch gets the stamp instead. 200ms `--ease-spring` in, 300ms out. |
| Page transitions | Print-wipe (§6.12): pink sweep, teal sweep, fresh sheet beneath | 500ms total. Anchor jumps within a page use an instant cut — the press does not wipe for a short feed. |
| Image treatments | Two-ink duotone with ink-pool settle (§6.9) | Every photograph is duotone-mapped to teal shadows / paper highlights with the pink pass as its offset colour layer. No full-colour photography exists in this theme. |

**Global motion laws**

1. **Printed is permanent.** No element ever returns to an unprinted state.
   Re-entering the viewport replays nothing except parallax and ambient loops.
2. **Catch-up compression.** If a sheet crosses the viewport faster than its
   ceremony (fast scroll, keyboard jump, find-in-page), durations compress:
   passes drop to 120ms/180ms, and a sheet already >50% past centre on first
   sight is simply printed, no animation. The press never makes a reader wait
   for a show they have already scrolled past.
3. **The 900ms promise.** If the animation pipeline has not completed for any
   above-the-fold element within 900ms of first paint, offsets snap to their
   final printed state. Nothing may sit doubled, blurred, or hidden past
   900ms for any reason (this is the source theme's standing rule, kept).
4. **One loop.** A single rAF loop (lerp factors stated per element) drives
   all scrubbed values. A second loop is a defect.
5. **Reduced motion is a different printing, not a broken one.** Under
   `prefers-reduced-motion`, every element ships its §6 reduced variant:
   passes appear aligned and static, grain is a still texture, the drum
   stands still with the band at final length, counters show final numbers.

## 6. Signature elements

Eighteen elements: the theme's twelve signatures (§6.1–§6.12) and six
page-family elements (§6.13–§6.18). Every element carries its full build spec
plus the v2 layers — choreography timeline, state matrix, breakpoint
behaviour, edge cases, accessibility spec, and the tokens it consumes.
Timelines are milliseconds from the element's trigger unless stated.

### 6.1 Two-pass section printing

**What & why.** The theme's engine. Every sheet prints in two passes: the
fluoro-pink colour layer lands on entry, the teal colour layer lands a beat
later, and for a moment the section exists in pink only before becoming
whole. It belongs because it *is* the riso process — and because the beat of
incompleteness makes visitors watch a section arrive instead of skimming
past it.

**Structure.** Each `.sheet` holds its drum-black content (text, rules,
data) as normal DOM — present and readable from first paint. Chromatic
content (colour blocks, image passes, headline ink copies, highlight swipes)
lives in two stacked layers, `.pass-pink` and `.pass-teal`, absolutely
positioned over the sheet's colour zones, `aria-hidden` where they duplicate
a shape the black layer already describes. A single `IntersectionObserver`
adds `.is-printing`, then `.is-printed`, to each sheet.

**Motion spec.** Trigger: sheet 20% visible. Pink layer: opacity 0→1 and
translate from (−9px, −2px) to its rest offset (−3px, −2px), 300ms
`--ease-pass`. Gap 350ms. Teal layer: opacity 0→1, translate from
(+9px, +2px) to rest (+3px, +2px), 420ms `--ease-pass`, with wet-ink blur
1.5px→0 across the same 420ms. Black content never moves and never fades.

**Choreography timeline (v2).**
- t=0 — IO fires (sheet 20% visible). Sheet gains `.is-printing`.
- t=0–300 — Pink pass lands (slide + fade).
- t=300–350 — The beat. Pink-only sheet. This pause is the signature; never
  shorten it below 250ms at any breakpoint.
- t=350–770 — Teal pass lands; wet-ink blur dries 1.5px→0.
- t=770 — `.is-printed` set. Parallax registration (§5) takes over the layers
  from here; the ceremony is over and cannot replay.

**State matrix (v2).**

| State | Pink layer | Teal layer | Black content | Notes |
|---|---|---|---|---|
| Unprinted (below fold) | opacity 0, offset −9px | opacity 0, offset +9px | Fully visible, readable | A no-JS or pre-trigger sheet reads as a black-and-paper sheet — complete, just uncoloured. |
| Printing | Animating in | Waiting, then animating | Fully visible | Never more than ~770ms. |
| Printed (rest) | At (−3,−2), opacity 1 | At (+3,+2), opacity 1 | Fully visible | The honest misregistration. |
| Scrolled-past | Printed state, parallax drift only | Same | Fully visible | Never un-prints (§5 law 1). |
| Hover/focus-within | Per §6.3 align, if the sheet is a `[data-register]` block | Same | Unchanged | Printing always completes before align can engage. |
| Disabled | n/a — sheets are not controls | — | — | — |

**Breakpoint behaviour (v2).** ≥1200px: full ceremony as specced.
768–1199px: gap shortens to 300ms; slide distance shrinks to ±6px.
<768px: gap 220ms, slides ±4px, parallax registration disabled (layers lock
at rest offsets once printed) — mobile scroll is fast and the ceremony must
not chase it.

**Edge cases (v2).** Fast scroll / keyboard jump / find-in-page: catch-up
compression (§5 law 2) — passes at 120ms/180ms, or instant if the sheet is
already >50% past centre. Scrolling back up: nothing replays. Very long
sheets (>200vh): the sheet is split into two print zones at build time, each
with its own trigger, so the footer of a long sheet is not printed before
anyone can see it happen. Slow network: passes do not wait for images — an
image zone prints its paper-toned placeholder block in both passes and the
image settles later (§6.9). IO unsupported: every sheet ships `.is-printed`
in the HTML class list fallback — colour simply present.

**Accessibility (v2).** No content exists only in a colour layer; screen
readers meet the black layer only, in DOM order, unaffected by the passes.
The passes are never announced (no aria-live). Because black text contrast
is 13.7:1 at every moment including mid-print, the animation cannot create a
low-contrast reading state. Focus order is DOM order; a focused element
inside an unprinted sheet forces that sheet to print instantly (focus must
never land on an apparently blank zone).

**Content merge.** The passes are not an overlay effect: they are the
section's own colour, arriving the way the machine delivers it. Remove the
content and there is nothing left to print — the test every element here
must pass.

**Failure fallback.** JS off, IO missing, or the 900ms promise (§5 law 3)
tripped: all layers at rest offsets, full opacity. The sheet reads as a
finished print.

**Reduced motion.** Both passes present, aligned to (0,0) — the one place
the theme prints in perfect register — static, no slide, no blur.

**Performance & mobile variant.** Two composited layers per sheet; sheets
off-screen cost nothing (layers are `will-change` only while `.is-printing`,
removed on `.is-printed`). Budget: ≤2ms script per sheet print, all in the
shared loop's IO callback. Mobile variant is the breakpoint spec above.

**Tokens.** `--dur-pass`, `--dur-gap`, `--dur-pass2`, `--ease-pass`,
`--misreg-x`, `--misreg-y`, `--pink`, `--teal`.

### 6.2 Off-register spring settle (hero ink copies)

**What & why.** The hero shout headline exists three times: drum black in
front, a pink copy behind at (−3px, −2px), a teal copy behind at (+3px,
+2px). On load the two ink copies slide in from opposite sides and
spring-settle into their misregistration — overshooting once, like a sheet
slapped onto the stack and rocking into place. It is the theme's handshake:
the first thing the visitor sees is the press registering badly, proudly.

**Structure.** One real `<h1>` in `--ink` (the only headline a screen reader
or search engine meets). Two `aria-hidden` duplicate spans, `.ink-pink` and
`.ink-teal`, absolutely positioned over the h1's box, `pointer-events: none`,
`user-select: none`. All three share one text node value, kept in sync by
build discipline (they are written once in the template, never by JS).

**Motion spec.** Trigger: page load, after first paint. Pink copy:
translateX(−56px)→(−3px) with Y −6px→−2px, 650ms `--ease-spring`, delay
150ms, wet-ink blur 2px→0.8px. Teal copy: translateX(+56px)→(+3px), Y
+6px→+2px, 650ms `--ease-spring`, delay 300ms, blur 2px→0. Final resting
blur 0 — the 0.8px figure is the mid-flight value at ~60% of the curve.
Overshoot: the spring passes the rest offset by ~1.2× (≈4px) once, at
~430ms (pink) / ~580ms (teal), then settles.

**Choreography timeline (v2).**
- t=0 — First paint: black headline fully visible, copies at 0 opacity.
- t=150 — Pink copy fades in already moving (opacity over first 120ms).
- t=150–800 — Pink slides and springs; overshoot beat at ~t=580.
- t=300 — Teal copy starts.
- t=300–950 — Teal slides and springs; overshoot at ~t=730.
- t=950 — Both copies at rest offsets. The 900ms promise (§5 law 3) applies
  to the *readable* state, which existed at t=0; the copies are decoration
  catching up, and if fonts or frames stall they snap at t=1400 (hard cap).

**State matrix (v2).**

| State | Pink copy | Teal copy | Black h1 | Notes |
|---|---|---|---|---|
| Pre-load / no-JS | At rest offset, opacity 1 | At rest offset, opacity 1 | Visible | The printed state is the default state; JS adds the journey, never the destination. |
| Loading | Sliding/springing | Waiting/sliding | Visible, readable | Headline readable from t=0. |
| Rest | (−3,−2) | (+3,+2) | Visible | — |
| Hover (hero is `[data-register]`) | → (0,0) per §6.3 | → (0,0) | Unchanged | The whole hero aligns under attention. |
| Scrolled-past | Rest offsets + parallax drift ±2px | Same | Visible | Copies join the §5 parallax system. |

**Breakpoint behaviour (v2).** ≥1200px: as specced. 768–1199px: slide
distance 36px. <768px: slide distance 20px, delays compress to 80ms/160ms,
and if the headline wraps past 3 lines the copies drop the Y offset (X only)
so wrapped lines never collide with the line above.

**Edge cases (v2).** Font swap late (Archivo Black arriving after first
paint): copies are tied to the h1's box, so they follow the swap; if
`document.fonts.ready` resolves after t=1400, the settle is skipped entirely
and copies sit at rest — a late show is worse than no show. Very long
headlines (5+ words/line): per-line copies are forbidden; the whole block
moves as one stencil, as a real drum would print it.

**Accessibility (v2).** Copies are `aria-hidden`, excluded from selection
and from the accessibility tree; the h1's text is announced once. The motion
is transform-only on decorative layers; the readable headline never moves,
blurs, or fades. Contrast of the composite at rest: black on paper 13.7:1 —
the offset copies sit *behind* and never lighten the reading layer.

**Content merge.** The copies are the headline's own ink. There is no
separate graphic; delete the headline and the element ceases to exist.

**Failure fallback.** No JS: copies at rest offsets (the HTML default).
Animation frame drops below 30fps during the settle: the copies jump to
rest — a choppy spring is worse than a still print.

**Reduced motion.** Copies at rest offsets from first paint; no slide, no
spring, no blur.

**Performance & mobile variant.** Two composited text layers, one 950ms
window, then static. Cost is negligible; the mobile variant is the distance
compression above, not a removal — the settle is the theme's signature and
mobile keeps it.

**Tokens.** `--ease-spring`, `--misreg-x`, `--misreg-y`, `--pink`, `--teal`,
`--ink`.

### 6.3 Hover-to-align

**What & why.** Attention corrects the printing — briefly. Hovering (or
focusing into) any printed block animates its pink and teal layers from
their honest offsets into perfect register; releasing returns them to the
honest 3px. It rewards looking closely, and its honesty is the point: the
correction never lasts, because the press never actually fixed it.

**Structure.** Any block marked `[data-register]` — hero, cards (§6.15),
image figures (§6.9), data blocks. Its `.pass-pink`/`.pass-teal` layers (or
ink copies) transition `transform` between the misregistered and aligned
positions. One CSS class, `.is-aligned`, toggled by `:hover`/`:focus-within`
in pure CSS; JS only adds the touch behaviour.

**Motion spec.** Align: both layers to (0,0), 180ms `--ease-pass`. Release:
back to rest offsets, 300ms `--ease-pass` — slower out than in, like the
sheet relaxing. No overshoot: alignment is a correction, not a bounce.

**Choreography timeline (v2).**
- t=0 — Pointer enters / focus lands.
- t=0–180 — Layers converge to (0,0). At ~t=120 the composite visibly
  "snaps sharp" as the spread drops under 1px.
- Hold — Perfect register for exactly as long as attention lasts.
- t=release — Layers drift back over 300ms; the last 100ms is sub-pixel and
  reads as the print "breathing out".

**State matrix (v2).**

| State | Layers | Notes |
|---|---|---|
| Rest | Pink (−3,−2), teal (+3,+2) | The honest state. |
| Hover (fine pointer) | → (0,0) in 180ms | Whole block, not per-word. |
| Focus-within (keyboard) | → (0,0) in 180ms | Keyboard users get the same correction; focus outline (§6.13/§6.16 specs) is independent of layer position. |
| Active/pressed | (0,0) + §6.11 stamp if the block is a control | Align and stamp compose; neither cancels the other. |
| Touch (coarse pointer) | First tap aligns and holds; tap elsewhere or scroll >40px releases | Implemented via JS class, since touch has no hover. A tap that follows a link still navigates — align never swallows the first tap on a link (no "tap twice" trap). |
| Scrolled-past | Rest offsets | Align is an attention state, not a scroll state. |
| Disabled (sold-out card, §6.15) | Never aligns | A gone edition stays honestly misregistered; the stamp overlay carries the state. |

**Breakpoint behaviour (v2).** ≥1200px and 768–1199px: identical.
<768px: align still applies on focus and on the touch-hold, but the release
on scroll triggers at >24px (mobile scroll is the primary gesture; holding
register while reading a long card is less common than scrolling on).

**Edge cases (v2).** Pointer leaves mid-align: the return transition starts
from the current interpolated position (CSS transitions do this natively —
do not restart from (0,0)). Rapid hover flicker across a card grid: each
card is independent; no global lock. Block still printing (§6.1): align is
suppressed until `.is-printed` — the press finishes before the proofreader
touches it.

**Accessibility (v2).** Alignment is never required to read anything: black
text is single-pass and unaffected (§1). Focus-within alignment is a bonus
layer under the visible focus ring, which is drawn on the block's border,
not on a moving layer, so the ring never travels. Touch targets are the
blocks themselves (cards ≥ 44px in their shortest dimension is guaranteed
by §6.15 sizing).

**Content merge.** The layers being aligned are the block's own ink; the
gesture is proofreading the very thing you're reading.

**Failure fallback.** No JS, no hover: blocks sit at rest offsets forever —
the theme's normal face. Nothing is hidden or degraded.

**Reduced motion.** Layers are already at (0,0) everywhere (§6.1 reduced
variant), so hover-to-align has nothing to do; the block instead gains a
2px teal outline on hover/focus as its attention signal.

**Performance & mobile variant.** Pure CSS transitions on composited
layers; zero JS on desktop. Mobile variant is the touch-hold behaviour
above.

**Tokens.** `--dur-align`, `--dur-unalign`, `--ease-pass`, `--misreg-x`,
`--misreg-y`.

### 6.4 Rotating margin drum + unspooling band + "% inked"

**What & why.** The machine that is printing this page, sitting in the
margin, turning as you scroll. A riso drum graphic rotates scrubbed to
scroll; beneath it a printed band unspools — pink for the first half of the
page, teal for the second — and a figure in Archivo Black states the page's
progress as "% inked". It is the theme's only progress indicator, and it
earns the job: the band literally is the page produced so far.

**Structure.** Fixed rail (96px ≥1200px, 64px tablet, top bar on mobile).
One inline SVG drum: a circle with stencil perforations (dashed stroke
ring), a pink ink-window, and a clamp bar — drawn, never a stock image
(§9). Below it, the band: a 10px-wide vertical strip whose height is
progress × rail height, split at 50% into pink (top) and teal (bottom)
segments. Under the band, the figure: `<span class="inked-num">` in Archivo
Black. The whole assembly is `aria-hidden`; a visually hidden
`role="progressbar"` element carries the same value for assistive tech.

**Motion spec.** All scrubbed in the shared rAF loop, lerp 0.16. Drum
rotation: progress × 720° (two full turns per page — one per ink). Band
height: progress × 100% of its track. Figure: integer percent, DOM text
updated only when the integer changes (never per frame).

**Choreography timeline (v2).** Continuous, not triggered: at any moment,
drum angle, band length, and figure are the lerped image of scroll
progress, settling ~180ms after scroll stops (lerp tail). At progress 0.5
the band's teal segment begins and the drum's ink-window flips from pink to
teal over 200ms — the press is changing drums halfway down the page, and
the figure's colour follows (pink before, teal after, both as graphics
only — the figure is data, set in `--ink`; the *window* carries the colour).

**State matrix (v2).**

| State | Drum | Band | Figure | Notes |
|---|---|---|---|---|
| Top of page | 0°, ink-window pink | 0% | "0% INKED" | — |
| Mid-page | ~360° | 50%, pink segment full | "50% INKED" | Drum-change beat at exactly 50%. |
| Bottom | 720° | 100%, both segments | "100% INKED — END OF SHEET" (§12) | The end state is a small reward; keep it. |
| Tab hidden | Frozen (rAF paused globally) | Frozen | Frozen | Resumes on visibility; no catch-up spin. |
| Short page (<150vh) | Same mapping, compressed | Same | Same | Progress is relative; a short zine still gets two full turns. |
| Reduced motion | Static, 0° | Full length instantly | Static final % only when at bottom; otherwise updates instantly without lerp | See reduced variant below. |

**Breakpoint behaviour (v2).** ≥1200px: rail 96px, drum Ø72px, band track
runs from drum to viewport bottom minus 120px. 768–1199px: rail 64px, drum
Ø48px, perforation ring simplified (fewer dashes — drawn as a second SVG,
not scaled mush). <768px: rail gone; drum Ø36px sits in the fixed top bar
beside the figure (16px Archivo Black); the band becomes a 3px horizontal
line across the very top of the viewport, pink segment then teal, same 50%
logic.

**Edge cases (v2).** Page shorter than the viewport (no scroll): progress
is 1 by definition — drum at 720°, band full, figure at end state; a press
that printed a one-screen zine is done. Scroll bounce (overscroll): progress
clamps 0–1; the drum never counter-rotates past its ends. Zoom changes:
mapping is progress-based, not pixel-based, so nothing rescales wrongly.

**Accessibility (v2).** Decorative assembly is `aria-hidden`. The hidden
progressbar (`aria-valuemin 0`, `max 100`, `valuenow` = integer percent,
label "Page printing progress") updates at most every 500ms to avoid
chatter. The drum is not a control: no tabindex, no click behaviour — a
progress metaphor that pretends to be a button would fail §10.

**Content merge.** The band's length is the page's own length; the drum's
turns are the two inks the page is actually printed in. It measures this
document, not an abstraction.

**Failure fallback.** No JS: drum static at 0°, band rendered at 100% (a
finished print), figure reads "100% INKED". The HTML ships in the finished
state and JS rewinds it — never the reverse.

**Reduced motion.** Drum does not rotate; band and figure update instantly
on scroll (no lerp, no tail). Grain (§6.8) is the only ambient motion left,
and it too is stilled — the reduced page is a finished sheet, full stop.

**Performance & mobile variant.** One SVG (~1.2KB inline), three transform/
height writes per frame inside the shared loop, text write ≤1 per integer
change. Well inside the §14 frame budget. Mobile variant specified above.

**Tokens.** `--pink`, `--teal`, `--ink`, `--paper`; lerp 0.16 (shared-loop
constant, §14).

### 6.5 The immovable staple

**What & why.** A single staple, drawn in SVG, fixed at the viewport's
top-left corner. It never moves, rotates, parallaxes, or animates — while
every sheet prints and slides beneath it. Its stillness is the control
group for the whole page's motion: because the staple refuses to move,
everything else feels fed through a machine. It also states the fiction
plainly: this zine is bound, and that is its binding.

**Structure.** One inline SVG (34×12px desktop): crown and two legs, drawn
as a single stroked path in `--ink` at 70% with a 1px paper highlight offset
— a pressed metal staple, not an emoji, not a stock icon (§9). Position:
`fixed; top: 16px; left: 18px` (plus `env(safe-area-inset-*)` on notched
devices), `z-index: 90` — above sheets, below the print-wipe overlay
(§6.12, z 200) and below modals (z 150), so a fresh sheet or a modal sheet
passes *over* the staple: new paper covers the binding, correctly.

**Motion spec.** None. Ever. The staple is explicitly excluded from the
rAF loop, from parallax, from page transitions. Any transform on this
element in shipped CSS is a defect (§10 gate).

**Choreography timeline (v2).** t=0: present. t=∞: present, unchanged. The
one event in its life: during the print-wipe (§6.12) it is covered by the
sweeping sheet for ~250ms and re-emerges — covered, never moved.

**State matrix (v2).**

| State | Staple | Notes |
|---|---|---|
| Rest / hover / focus / active | Identical | It is not interactive; no states exist. |
| Scrolled (any depth) | Identical, same coordinates | The entire point. |
| Modal open | Covered by the modal sheet (z 150) | Binding goes under new paper. |
| Print-wipe | Covered mid-wipe | See timeline. |
| Print stylesheet | Hidden | Viewport furniture does not print; the sheets carry their own drawn staple in the PDF/print rendering (§6.10 ornaments remain). |

**Breakpoint behaviour (v2).** ≥1200px and 768–1199px: 34×12px at
(18px, 16px). <768px: 28×10px at (12px, 12px + safe-area). It never leaves
the corner at any size — on mobile it sits over the top bar's left end,
clear of the drum (§6.4) which occupies the bar's right side.

**Edge cases (v2).** Content sliding under it: the top-left of the first
sheet must keep a 56px clear zone at all breakpoints (a layout law in §4's
grid) so the staple never sits on text. RTL locales: the staple stays at
the *binding* edge — in RTL builds it mirrors to top-right, because a
binding follows the book, not the code. (The drum rail mirrors with it.)

**Accessibility (v2).** `aria-hidden`, no focus, no name. It conveys
nothing that is not conveyed elsewhere; a screen-reader user loses nothing
by its absence from the tree.

**Content merge.** It binds the actual stack of sheets the visitor is
scrolling. Remove the sheets and the staple is nonsense; with them, it is
the reason the page holds together.

**Failure fallback.** It is static HTML/SVG — it cannot fail. If SVG is
somehow unavailable, a 30×10px bordered `div` fallback in the same spot
keeps the composition (and is equally still).

**Reduced motion.** Identical. It was already the reduced-motion element.

**Performance & mobile variant.** Zero runtime cost. Mobile variant is the
size/position change above.

**Tokens.** `--ink`; position/size constants stated here (not tokens — they
must never be themed away).

### 6.6 Torn-paper headline reveals

**What & why.** Each sheet headline (H2, Archivo Black) is revealed through
a torn-paper edge: a jagged clip-path sweeps across the headline as its
sheet prints, as if the headline's strip was torn from a proof sheet and
pasted in. The tear is the headline's own sheet edge — the reveal edge has
the same torn profile as the sheet joins (§6.10), so the whole page tears
along one material logic.

**Structure.** The headline element carries `clip-path: polygon(...)` in
one of three precomputed torn variants (14 points each — the point count is
identical across start and end states so the path can interpolate). Start
state: the polygon collapsed to the left edge (all points at x=0 with the
torn y-profile preserved). End state: full rectangle with the torn right
edge. JS/IO adds `.is-torn-in` when the parent sheet starts its teal pass.

**Motion spec.** 500ms `--ease-feed`, clip-path interpolation, beginning at
t=+350 relative to the sheet's print trigger — the headline tears in as the
teal pass lands, so colour and headline arrive together.

**Choreography timeline (v2).**
- t=0 — Sheet print trigger (§6.1); headline still clipped shut, but see
  accessibility: the text is in the DOM and readable by AT from t=0.
- t=0–350 — Pink pass lands around the still-torn headline block (the block
  occupies its full layout box from the start — clip never affects layout).
- t=350–850 — Tear sweeps left→right; the leading edge is the jagged
  profile, so letters appear in torn slices, not a clean wipe.
- t=850 — Clip removed entirely (class swaps to `clip-path: none`) so no
  residual clipping can eat a descender or the §6.3 align transform.

**State matrix (v2).**

| State | Clip | Notes |
|---|---|---|
| Pre-print | Collapsed polygon | Visual only; layout box full-size, text present for AT. |
| Tearing | Interpolating | — |
| Printed | `clip-path: none` | Clean end state, always. |
| Hover/focus | None (no clip) | Headlines are not controls; §6.3 align may still move the sheet's layers, headline included, as one stencil. |
| Scrolled-past | None | Print is permanent (§5 law 1). |
| No-JS | None — the collapsed state is applied by JS only | The HTML ships unclipped. |

**Breakpoint behaviour (v2).** ≥1200px: full 500ms tear. 768–1199px:
420ms. <768px: 300ms and the tear sweeps top→bottom instead (narrow
headlines wrap to 3–4 lines; a horizontal tear across wrapped lines reads
as a wipe, a vertical tear reads as a feed — the press feeds downward on
mobile).

**Edge cases (v2).** Headline longer than expected (CMS copy, translation
+30%): the polygon is percentage-based, so it scales; wrapped extra lines
tear with the block as one stencil. Very short headline (one word): the
tear still runs the full box width — do not shorten the duration per word;
consistency is the material. Browser without clip-path polygon
interpolation: the class swap simply cuts from collapsed to none at t=350
— a hard cut is an acceptable print (the sheet was pasted, not torn, that
day) and §10 allows it.

**Accessibility (v2).** Clip-path does not remove content from the
accessibility tree, and the headline is never `visibility: hidden` or
transparent — a screen reader or a user with CSS animations blocked reads
it immediately. For low-vision users the tear is a reveal of already-dark
text (13.7:1) — at no frame is text shown at reduced contrast, only
partially clipped, and the full headline lands within 850ms of the sheet
entering. Focus never targets the headline itself except as a page's h1/h2
heading navigation, which is unaffected.

**Content merge.** The torn edge is the headline strip's own edge; the same
three torn profiles are reused for sheet joins and image pools, so the
headline is visibly torn from the same stock as everything else.

**Failure fallback.** JS adds the collapsed state; no JS = no clip, ever.
Watchdog (§5 law 3): if `.is-torn-in` has not fired within 1400ms of the
sheet entering, clip is forced to none.

**Reduced motion.** No clip, no tear. The headline is simply there, printed
with its sheet's static passes.

**Performance & mobile variant.** One clip-path interpolation on one
element per sheet; clip-path on large text is the most expensive animation
in the theme, so it is capped: never animate a headline taller than 4
lines — beyond that, cut (the fallback above) at every breakpoint. Mobile
variant: the vertical tear, 300ms.

**Tokens.** `--dur-tear`, `--ease-feed`, `--ink`.

### 6.7 Drum-frequency shout word

**What & why.** One word in one headline per page is printed while the drum
is still shaking: it vibrates at drum frequency — ±1.5px at ~14Hz — for a
single 700ms beat as it prints, then stills forever. It is the moment the
machine's hand is visible in the type. One word, one beat, one page: the
restraint is what keeps it premium instead of a screensaver.

**Structure.** A `<span class="shout-word">` inside a shout or H2 headline,
chosen at build time (the word the confession turns on: "LIED", "BROKE",
"FREE"). Animation is a CSS keyframe (`shout-shake`: translateX alternating
−1.5px/+1.5px, 71ms per half-cycle ≈ 14Hz) applied via `.is-shaking` for
exactly 10 half-cycles (700ms), then the class is removed by the same IO
sequence that printed the sheet. Transform only; the word's layout box
never changes.

**Motion spec.** Trigger: the moment the word's headline completes its
tear (§6.6) — or, in the hero, at t=700 of the load sequence (§6.14).
Duration 700ms, then permanently still. Amplitude ±1.5px at display sizes
≥40px; ±1px below that.

**Choreography timeline (v2).**
- t=0 — Headline printed; word at rest.
- t=0–700 — 10 half-cycles of shake, amplitude constant (a drum does not
  decay politely), last half-cycle ends at +0 — the word stops dead centre,
  not mid-swing.
- t=700+ — Still. Forever. Scrolling away and back does not re-shake it
  (§5 law 1 applies to dignity as well as ink).

**State matrix (v2).**

| State | Word | Notes |
|---|---|---|
| Pre-print | At rest | — |
| Shaking (700ms once) | ±1.5px at 14Hz | Readable throughout — amplitude is 1.5px against ≥40px type. |
| Rest (after) | Still | The permanent state. |
| Hover/focus | Still | Attention aligns layers (§6.3); it does not re-shake. Re-shaking on hover is the single most likely way this element becomes slop (§9). |
| Reduced motion | Never shakes | The word instead carries a `--pink-wash` highlight swipe — emphasis without movement. |

**Breakpoint behaviour (v2).** ≥1200px: ±1.5px. 768–1199px: ±1.25px.
<768px: ±1px, and the word must be ≥32px rendered size or the effect is
dropped entirely (small shaking text is just blurry text).

**Edge cases (v2).** Two candidate words in one headline: the build picks
the first; the class is singular by lint rule (§10). Word inside a link:
forbidden — a shaking link is unclickable-feeling and fails touch
confidence; shout words live in headlines only. Vestibular sensitivity:
the reduced-motion variant is mandatory, not optional, for this element.

**Accessibility (v2).** The word is ordinary headline text in the tree;
the shake is a transform on a span and is never announced. Amplitude and
duration keep it outside photosensitivity risk (no flashing — it is
positional, low-amplitude, and brief). Under `prefers-reduced-motion` it
never runs (see matrix).

**Content merge.** The shake is in the word's own ink, timed to its own
printing. It is not an effect applied to the page; it is a property of
that word's impression.

**Failure fallback.** No JS: the class is never added; the word is a
normal bold word in a loud headline. Nothing lost.

**Reduced motion.** Highlight swipe instead of shake (see matrix).

**Performance & mobile variant.** One CSS animation, 700ms, once per
page. Cost ~zero. Mobile: reduced amplitude per breakpoints.

**Tokens.** `--dur-shout`, `--pink-wash`.

### 6.8 Crawling riso grain + fluoro shimmer

**What & why.** Riso ink is grain — heavy, visible, alive. A grain layer
crawls continuously over the whole page (the drum never rests), and on
drum-black sheets a fluoro-pink shimmer drifts slowly, the way fluoro ink
catches light on a dark stack. This is the theme's ambient signature; it is
also its biggest performance and accessibility risk, and it is specced
accordingly — capped, pausable, and never allowed to dirty text.

**Structure.** Grain: one fixed layer (`.grain`), inset −140px on all sides
(so its steps-jumps never expose an edge), background a 140×140px tile
(WebP, ~6KB, generated noise in `--ink` at low alpha), `mix-blend-mode:
multiply` on light grounds, opacity 0.5 over paper areas / 0.35 over
sheets, `pointer-events: none`, `aria-hidden`, z-index 80 (below staple 90,
above sheets). Animation: `steps(1)` jumps between 4 background positions,
900ms cycle, infinite. Shimmer: a `::after` on `.sheet--dark` only — a
linear-gradient pink band (0% → 18% alpha → 0), width 60% of the sheet,
translating −20%→120% over 9s linear infinite, `mix-blend-mode: screen`,
delays staggered by sheet index (2.2s apart) so dark sheets never shimmer
in sync.

**Motion spec.** Grain cycle 900ms, 4 discrete jumps (a crawl, not a
drift — smooth grain movement reads as video noise; stepped grain reads as
print). Shimmer 9s linear, opacity capped 0.18. Both pause on
`visibilitychange` (hidden tab). Grain additionally freezes (holds its
current frame — it does not disappear) when `prefers-reduced-data` matches
or the device reports battery-saver via the shared loop's power check.

**Choreography timeline (v2).** Continuous from first paint. Grain is the
only element already moving before any trigger — the hall is already
printing when you arrive. Shimmer on a dark sheet starts when the sheet
prints (§6.1), not at page load, so an unprinted dark sheet sits matte.

**State matrix (v2).**

| State | Grain | Shimmer | Notes |
|---|---|---|---|
| Rest (light sheet) | Crawling, multiply, 0.35–0.5 opacity | Absent | — |
| Dark sheet | Crawling at 0.3, blend soft-light | Drifting 9s after print | Shimmer never on light sheets — fluoro glows on dark stock only. |
| Tab hidden | Paused | Paused | Both resume without a jump-cut (animation-play-state, not restart). |
| Reduced data / low power | Frozen frame | Off | Texture remains; motion goes. |
| Reduced motion | Static (single frame, no animation) | Off | The printed-paper look survives; the crawl does not. |
| Print stylesheet | Off entirely | Off | Paper is already paper. |

**Breakpoint behaviour (v2).** ≥1200px: tile 140px, opacity as specced.
768–1199px: tile 120px. <768px: tile 100px, opacity ×0.8, and the grain
layer's inset shrinks to −100px; the crawl cycle lengthens to 1200ms
(fewer composite updates per second on small GPUs).

**Edge cases (v2).** Long pages: the layer is fixed, so cost is constant
regardless of page length — the reason grain is a viewport layer and never
a per-sheet background. OLED black sections: shimmer's screen blend on
true black can band; the gradient uses 5 stops to break banding. Browser
without mix-blend-mode: grain falls back to plain low-opacity overlay
(0.18) — still textured, less integrated; acceptable, logged in §10 as a
known degradation, not a failure.

**Accessibility (v2).** The hard rule: grain must never pull text contrast
below AA. Drum-black text on paper is 13.7:1 before grain; at the capped
opacities the worst-case measured contrast stays ≥9:1 (multiply darkens
paper slightly, text is already near-black). Grain is decorative,
`aria-hidden`, and carries no information. The shimmer's motion is slow
(9s) and low-alpha — outside vestibular concern — but it still obeys
reduced-motion (off). No flashing anywhere: grain jumps are positional
texture changes at 1.1Hz, not luminance flashes.

**Content merge.** The grain is the ink's own texture — it sits *in* the
printed layers, strongest where ink is (sheets), lighter on bare paper.
It is not a noise overlay borrowed from a stock library; its tile is
generated from the theme's own ink colour.

**Failure fallback.** Tile fails to load: the layer is transparent; the
page is a clean print. Nothing depends on grain.

**Reduced motion.** Static grain frame, no shimmer (see matrix).

**Performance & mobile variant.** The most expensive ambient element in
the theme: one fixed composited layer, transform/background-position steps
only, no JS per frame (pure CSS animation). Budget: ≤1.5ms average frame
cost on a Moto G4-class GPU; if the shared loop's frame monitor sees
sustained >20ms frames, grain crawl is the second thing cut (§14 cut
order) — frozen, not removed. Mobile variant per breakpoints.

**Tokens.** `--ink`, `--pink`; cycle `--grain-cycle: 900ms`.

### 6.9 Ink-pool image settle

**What & why.** Photographs in a riso zine are printed in the two inks, and
riso ink pools at edges — heavier, darker, slightly blurred where the
stencil laid it down thick. Images here arrive the same way: a duotone
(teal shadows, paper highlights) with its pink pass offset behind it,
scaling gently into its frame while its edges pool darker and its wet blur
dries. The image doesn't fade in like a web picture; it gets printed like
one.

**Structure.** A `<figure class="ink-pool">` containing: the pink pass
`<img>` (duotone-mapped to pink, `aria-hidden`, absolute, offset
(−3px, −2px)), the main `<img>` (teal duotone, real alt text), and an
edge-pool overlay (radial-gradient, transparent centre → `--teal` 55%
alpha at edges, `mix-blend-mode: multiply`). Duotone is produced by an SVG
`feColorMatrix`/`feComponentTransfer` filter pair referenced by CSS
(`filter: url(#duotone-teal)`), with a pre-processed duotone WebP as the
no-SVG-filter fallback baked at build time for CMS images. The figure's
frame is a torn edge variant (§6.6 profiles) in a 2px `--ink` border.

**Motion spec.** Trigger: figure 30% visible (IO), synced after its
sheet's pink pass. Image scale 1.06→1, 600ms `--ease-pass`; blur 1.5px→0
over the same 600ms (wet ink drying); edge-pool gradient opacity 0→0.55
starting at t=+150, 500ms `--ease-pass`. Pink pass starts at its offset
already — it does not slide; it was printed first and the teal image
settles onto it.

**Choreography timeline (v2).**
- t=0 — Figure 30% visible; pink pass visible (printed with the sheet).
- t=0–600 — Main image scales 1.06→1 and dries (blur 1.5→0).
- t=150–650 — Edges pool: gradient deepens, corners first (the radial is
  elliptical, matched to the figure's aspect).
- t=650 — Settled. The figure joins §6.3 (hover-to-align includes the pink
  pass) and §5 parallax (pink pass only, ±2px; the main image stays put —
  a photograph's registration error lives in its colour pass, not its
  geometry).

**State matrix (v2).**

| State | Main image | Pink pass | Pool overlay | Notes |
|---|---|---|---|---|
| Unprinted | Paper-toned placeholder block with the figure's aspect ratio and its caption already readable below | Absent | 0 | Layout never shifts: aspect-ratio is reserved in CSS. |
| Settling | Scaling/drying | At offset | Deepening | ≤650ms. |
| Rest | Sharp, full | At (−3,−2) | 0.55 | — |
| Hover/focus-within | Unchanged scale | Aligns to (0,0) per §6.3 | 0.55 | The photo "registers" under attention. |
| Scrolled-past | Rest state + pink parallax | Drifting ±2px | 0.55 | — |
| Broken image | Alt text on a `--sheet` block inside the torn frame, styled as a caption card | Absent | 0 | A failed print is shown as a labelled blank plate — never a broken-image icon (§9). |

**Breakpoint behaviour (v2).** ≥1200px: full treatment. 768–1199px:
scale travel 1.04→1. <768px: the pink pass copy is dropped entirely
(single teal duotone) to halve image weight on mobile data; scale 1.03→1;
pool overlay kept (it is a gradient, ~free).

**Edge cases (v2).** Slow network: the placeholder block prints in both
passes with the sheet (§6.1 edge case), and the image settles whenever it
arrives — if it arrives after the visitor has scrolled past, it appears
already settled (no ceremony for an absent audience). Tall/portrait
images: pool gradient follows aspect via `background-size: 100% 100%`.
Images with faces: duotone mapping must keep faces legible — the teal
transfer curve preserves mid-tone separation (specified in the filter:
no output value between 30–70% input may compress by more than half) —
a face turned to mud fails §10.

**Accessibility (v2).** The main image carries real alt text; the pink
pass is `aria-hidden` and `alt=""`. Duotone is a colour treatment, so any
information in the image must survive in two inks — charts and diagrams
are NOT duotone photographs: data graphics use §11's table/ledger
treatments with labelled values, never colour-only encoding. Figure
captions are ordinary body text, present from first paint.

**Content merge.** The pooling happens at the image's own edges, the
offset is the image's own second pass. The treatment is the printing of
this photograph, not a frame effect applied to it.

**Failure fallback.** No JS: image present, sharp, pool overlay at full
0.55, pink pass at offset — the finished print, statically. SVG filter
unsupported: build-time duotone WebP serves instead; if both fail, the
original image shows in full colour inside the torn frame (a "guest print"
— logged, not hidden).

**Reduced motion.** No scale, no blur, no settle: image present and sharp,
pool at rest, pink pass aligned (0,0) per the reduced register rule.

**Performance & mobile variant.** Images are the page's weight budget
centre (§14): duotone WebP ≤120KB per figure at display size, lazy-loaded
below the fold, `decoding="async"`. The settle animates transform + filter
on one element — blur is the costly part, capped at 600ms and never on
more than one figure at a time (IO staggers concurrent settles by 90ms).
Mobile variant per breakpoints (single pass).

**Tokens.** `--dur-settle`, `--ease-pass`, `--misreg-x`, `--misreg-y`,
`--teal`, `--pink`.

### 6.10 Staple-and-tape ornament draw

**What & why.** Sheets in a paste-up are joined by fasteners. At each
section join, a small ornament — one drawn staple and one strip of
translucent tape — draws itself in SVG as the join arrives. It marks the
seam honestly: here one sheet ends and the next was stuck on. It is the
small, quiet cousin of the immovable staple (§6.5): that one binds the
whole zine; these bind sheet to sheet.

**Structure.** An inline SVG (~120×36px) centred on the join line between
two sheets: a staple path (crown + two legs, stroke `--ink`) and a tape
strip (a `--pink` rect at 45% opacity with torn short ends, slight −2°
rotation). Draw via `stroke-dasharray/dashoffset` on the staple path;
the tape fades/slides the last 100ms. The ornament sits in the gap's
layout flow (it occupies its 36px), never overlaid on text.

**Motion spec.** Trigger: join 40% visible (IO). Staple draws 350ms
`--ease-pass` (dashoffset full→0). Tape: opacity 0→0.45 + translateY
−4px→0, t=+250–350. Once drawn, permanent.

**Choreography timeline (v2).**
- t=0 — Join enters at 40%.
- t=0–350 — Staple legs draw down, then the crown connects (single path,
  drawn legs-first by path order).
- t=250–350 — Tape settles over the join's right end.
- t=350 — Join finished. The eye reads: stapled, taped, next sheet.

**State matrix (v2).**

| State | Staple | Tape | Notes |
|---|---|---|---|
| Pre-join | Undrawn (dashoffset full) — applied by JS only | opacity 0 | No-JS state is fully drawn (see fallback). |
| Drawing | Animating | Fading in at t=250 | — |
| Drawn (rest & all later states) | Full path | 0.45 opacity | Hover/focus/scroll-past change nothing — fasteners don't perform twice. |

**Breakpoint behaviour (v2).** ≥1200px and 768–1199px: as specced,
ornament 120×36px. <768px: ornament shrinks to 88×28px and the tape is
dropped (small joins get the staple only — tape at 88px wide reads as a
smudge).

**Edge cases (v2).** Sheets separated by a dark sheet: the staple stroke
flips to `--paper` for joins touching a dark sheet (contrast on the gap's
paper ground is unchanged — the gap is always ground — but the staple
visually belongs to both sheets; the rule is: if either neighbour is dark,
use the paper-stroke variant with an ink outline). Back-to-back joins in
rapid scroll: draws compress to 150ms (§5 law 2).

**Accessibility (v2).** Purely decorative: `aria-hidden`, no text, no
meaning. Its absence (no-JS, reduced motion) removes nothing.

**Content merge.** The ornament is the physical join of the two sheets it
sits between. It exists only where sheets actually join — never floated
mid-sheet as decoration.

**Failure fallback.** The SVG ships fully drawn in HTML; JS sets the
undrawn state before first paint of the join (script in head adds the
class). If that script fails, ornaments are simply present — the correct
end state by default.

**Reduced motion.** Fully drawn, static, from the start.

**Performance & mobile variant.** One tiny SVG per join, one 350ms stroke
animation. Negligible. Mobile variant per breakpoints.

**Tokens.** `--dur-draw`, `--ease-pass`, `--ink`, `--pink`.

### 6.11 Ink-stamp click

**What & why.** Pressing something in a print shop is literal: you stamp
it. Clicks on controls and stampable blocks answer with an ink-stamp
squash — the element compresses like paper under a stamp — and a pink
splat blooms at the exact contact point. It makes every press feel
registered by the machine, and it gives touch users (who get no hover
states) the theme's richest feedback.

**Structure.** On `[data-stamp]` elements (buttons, cards, the form's
submit — §6.15, §6.16): a `pointerdown` handler adds `.is-stamping` for
the squash and spawns a `<span class="splat">` at the pointer coordinates
inside the element (element is `position: relative; overflow: visible` —
the splat must be allowed to bleed 6px past the edge, like real ink; the
page-level `overflow-x: clip` (§4) catches any page-level spill). Splat:
radial-gradient blob in `--splat`, irregular via `border-radius:
58% 42% 55% 45% / 48% 55% 45% 52%`, scale 0.3→1 (6px→26px), opacity
0.9→0 over 260ms, then the node is removed. A pool of 3 splat nodes per
element is recycled.

**Motion spec.** Squash: `scaleY(0.96)` + `scaleX(1.01)`, 120ms
`--ease-stamp` down; release springs back 240ms `--ease-spring`. Splat:
260ms `--ease-pass` bloom-and-fade, starting at pointerdown (not click —
the stamp lands when the hand lands).

**Choreography timeline (v2).**
- t=0 — pointerdown: squash begins; splat spawns at contact point at 6px.
- t=0–120 — Squash to full compression; splat blooms to ~18px.
- t=120–260 — Splat reaches 26px, fading to 0 by t=260; node recycled.
- t=release (whenever the pointer lifts) — Spring back over 240ms. A
  press-and-hold holds the squash — the stamp stays down while you hold
  it, which is exactly how a stamp behaves.

**State matrix (v2).**

| State | Element | Splat | Notes |
|---|---|---|---|
| Rest | Scale 1 | Absent | — |
| Hover | No squash (hover belongs to §6.3/§6.15) | Absent | Stamp is a press feedback, not a hover effect. |
| Active/pressed | Squash held while pressed | Blooming at contact point | Keyboard activation (Enter/Space) stamps at the element's centre — keyboard users get the same ink. |
| Focus-visible | Squash only on activation | — | Focus ring is separate and never a splat (§6.16 focus spec). |
| Disabled | No squash, no splat | Absent | A disabled control is an empty drum — pressing it does nothing, visibly. |
| Touch | Identical to mouse (pointer events unify) | At tap point | The primary feedback channel on touch. |

**Breakpoint behaviour (v2).** Identical at all sizes; splat max diameter
26px ≥768px, 20px <768px (small buttons, small splats).

**Edge cases (v2).** Rapid repeated presses: splat pool recycles the
oldest node — never more than 3 live splats per element, never a DOM
leak. Press that becomes a drag (text selection, scroll): squash cancels
on `pointercancel`/leaving the element — a stamp dragged is a stamp
lifted. Clicking a link-card: the stamp fires on pointerdown, navigation
proceeds on click as normal; the stamp never delays or swallows the
action.

**Accessibility (v2).** Purely visual feedback layered on top of — never
instead of — native `:active` behaviour and visible focus. It conveys no
state that isn't conveyed by the control itself. The splat is
`aria-hidden` (a spawned decorative span). Squash amplitude (4%) is far
below vestibular concern; reduced-motion removes it anyway (below).

**Content merge.** The stamp lands on the sheet/control itself, at the
visitor's own contact point. It is the press answering the press.

**Failure fallback.** No JS: controls behave natively with CSS `:active`
scale (a CSS-only mini-squash, no splat). Nothing depends on the JS
version.

**Reduced motion.** No squash, no splat. Press feedback becomes an instant
ink swap: the control's shadow ink flips pink→teal while active.

**Performance & mobile variant.** One transform transition + one recycled
span per press. Negligible. Identical on mobile — this element is
mobile's hover.

**Tokens.** `--dur-stamp`, `--ease-stamp`, `--ease-spring`, `--splat`.

### 6.12 Two-pass loading + print-wipe transition

**What & why.** Loading and navigation are the press changing sheets.
Initial load prints the skeleton in two passes — pink blocks first, teal
detail a beat later — then the real content arrives already printed.
Route changes feed a fresh sheet through: a pink sweep, a teal sweep, and
the new page beneath. The states every other theme apologises for are
this theme's home turf.

**Structure.** Loading: skeleton sheets are real `.sheet` elements whose
colour zones are `.pass-pink`/`.pass-teal` blocks (no grey shimmer bars —
shimmer is a screen metaphor; this press prints blocks). The skeleton
prints via the §6.1 ceremony compressed (passes at 200ms/280ms — a
skeleton is a proof, printed faster). Content swap: when data lands, the
skeleton is replaced and the content sheet is already `.is-printed`.
Transition: a JS-injected overlay (two full-viewport divs, pink then
teal, z-index 200 — above the staple) translating Y. For multi-page
(non-SPA) sites, the wipe runs on leave (250ms pink cover) and the new
page's entry is its normal §6.1/§6.2 print-in.

**Motion spec.** Load ceremony: as §6.1 with compressed passes; hard cap
— if content has not arrived by 1400ms, the skeleton completes its print
and waits printed (a printed proof is a calmer wait than a half-printed
one). Wipe: pink sweep covers in 250ms `--ease-feed`, teal sweep follows
covering in 250ms offset by 90ms (the teal sheet chases the pink), hold
60ms at full cover while the route swaps, then both sweeps exit upward
in 300ms revealing the new page already printed beneath. Total ≈ 890ms
for SPA transitions; the exit is overlapped with the new page's hero
settle (§6.2) so the perceived cost is the cover only (~340ms).

**Choreography timeline (v2) — route change.**
- t=0 — Navigation committed; pink sweep starts down.
- t=90 — Teal sweep starts, chasing.
- t=340 — Viewport fully covered (pink down at 250, teal at 340).
- t=340–400 — Hold; route swaps beneath; focus is moved to the new
  page's heading (programmatically, at swap).
- t=400–700 — Sweeps exit upward (teal first, pink chasing — reverse
  order, like sheets pulled off a stack); new page visible, printed.
- t=700 — Overlay removed from DOM. `aria-busy` clears.

**State matrix (v2).**

| State | Skeleton / overlay | Content | Notes |
|---|---|---|---|
| Initial load | Skeleton printing (compressed passes) | Absent | `aria-busy="true"` on main. |
| Load >1400ms | Skeleton fully printed, static | Absent | Plus a printed line in the skeleton's apparatus voice: "THE DRUM IS WARM. STILL PRINTING…" (§12). |
| Loaded | Skeleton removed | Present, printed | No second ceremony — content never prints twice. |
| Route change | Wipe per timeline | Old page covered, new page swapped at hold | Focus management per timeline. |
| Anchor jump (same page) | No wipe | Instant cut | Short feeds don't wipe (§5). |
| Back/forward | Wipe runs; destination restored from cache already printed | Present | Scroll position restored under cover, revealed on exit. |

**Breakpoint behaviour (v2).** Identical mechanics at all sizes; on
<768px the sweeps travel horizontally (left→right) — a phone's sheet
feeds sideways through the smaller press. (Direction is a build-time
constant per breakpoint, not a runtime branch in the animation.)

**Edge cases (v2).** Slow route/data: the hold extends — sweeps stay
down, with the apparatus line appearing on the teal sheet after 1200ms
of hold ("FEEDING THE NEXT SHEET…"). Never let the overlay sit >5s: at
5s it exits regardless and the destination shows whatever it has
(usually its skeleton) — a stuck overlay is the worst state this theme
can produce, and §10 gates it. Prefetch failure mid-wipe: exit the wipe
back upward (reverse) and stay on the current page with a drum-jam alert
(§11). Browser without JS: no overlay exists (JS-injected only); links
navigate natively.

**Accessibility (v2).** `aria-busy` on `<main>` during load and wipe;
focus moves to the new page's h1 at the swap beat and is never left on a
removed node. The wipe is visual only — screen-reader navigation follows
the route change, not the sweeps. Skiplinks remain operable above the
skeleton (they bypass loading entirely, pointing at whatever content
exists). Reduced-motion variant below replaces all of it with a fade.

**Content merge.** The loading state is the theme printing its own
placeholder; the transition is the press feeding the actual next sheet.
Neither is a generic spinner wearing a costume.

**Failure fallback.** JS off: no skeleton ceremony, no overlay — content
servers-rendered or normally loaded, links native. Overlay injection
failure: navigation proceeds without the wipe (the handler is
progressive — it enhances, never gates, navigation).

**Reduced motion.** No sweeps, no skeleton passes. Loading is a static
printed skeleton; transitions are a 150ms crossfade with the same focus
management.

**Performance & mobile variant.** Skeleton blocks are pure CSS. The
overlay is two divs; its animation is transform-only. The wipe must never
delay a navigation's *start* — it decorates a navigation already
committed. Mobile variant: horizontal sweeps (above).

**Tokens.** `--dur-wipe`, `--ease-feed`, `--pink`, `--teal`.

### 6.13 Masthead navigation

**What & why.** A zine's navigation is its masthead: the strip across the
cover that says what this is and what else is inside. The nav is a paper
strip with a 2px drum-black bottom rule, the wordmark shouted in Archivo
Black, links as uppercase apparatus labels, and the current page marked by
a hand-swiped pink highlight that draws itself in — the editor marking
where you are in the issue.

**Structure.** `<header class="masthead">`: wordmark (Archivo Black,
24px, home link), nav links (Space Grotesk 500, 12px, uppercase, 0.14em
tracking, min 44px tall hit areas via padding), and the current-page
marker: an SVG-free highlight — a `--pink-wash` block behind the active
link with a torn left edge (clip-path variant), scaleX 0→1 on activation.
Sticky: the masthead sticks to the top on scroll and gains its hard
shadow (`0 6px 0 color-mix(teal 30%)`) only once stuck — unstuck, it sits
flat on the paper like part of the cover. Mobile: a "CONTENTS" button
opens the menu as a sheet feeding down beneath the masthead (§6.12's feed
motion, 300ms `--ease-feed`), links stacked as a contents list with
folio-style numbers (01, 02, 03…).

**Motion spec.** Highlight draw: 250ms `--ease-pass` (scaleX with torn
edge — a swipe, not a fade). Sticky shadow: appears over 150ms when the
stuck state engages (IntersectionObserver on a sentinel). Mobile sheet:
300ms `--ease-feed` translateY(−8px→0) + the sheet's own two-pass print
compressed (it is a small sheet; passes 150ms/200ms).

**Choreography timeline (v2) — page load / route change.**
- t=0 — Masthead present with the page (it prints with the hero sheet's
  pink pass window; it is never animated separately at load).
- On route change — the highlight swipe redraws on the new current link
  during the wipe's exit (t≈500 of §6.12), so the visitor lands already
  knowing where they are in the issue.

**State matrix (v2).**

| State | Link | Marker | Notes |
|---|---|---|---|
| Rest (not current) | `--ink` label | Absent | Hover: teal-pass underline draws in 200ms (§5 micro-interactions). |
| Current | `--ink` label, 700 weight | Pink swipe behind, drawn | `aria-current="page"` — the marker is never the only signal; weight + swipe together. |
| Hover | Underline drawn | — | On the current link, hover deepens the swipe to `--pink` at 30%. |
| Focus-visible | 3px `--teal` outline, offset 2px, plus pink halo shadow at 4px offset (decorative) | — | The theme's standard focus spec — teal carries the contrast (4.6:1 ≥ the 3:1 non-text floor), pink is garnish. Used by every interactive element in the theme. |
| Mobile menu open | Links stacked, folio numbers in `--ink-soft` | Swipe on current row's full width | Menu sheet is `aria-expanded` controlled; Esc closes and returns focus to the CONTENTS button. |
| Disabled (a section not in this issue) | `--ink-soft`, no underline | Absent | Rendered as a `<span>`, not a dead link. |

**Breakpoint behaviour (v2).** ≥1200px: full masthead, drum rail below it
starts at the masthead's bottom edge. 768–1199px: wordmark 20px, links
may wrap to a second row rather than shrink below 12px labels (a wrapped
masthead is a taller cover strip — acceptable; tiny type is not).
<768px: CONTENTS button + feeding sheet; the top bar also carries the
mobile drum (§6.4) at its right end, and the staple (§6.5) overlaps its
left corner — the bar's left padding (56px) keeps the wordmark clear of
the staple.

**Edge cases (v2).** Long wordmarks / translated labels (+30% length):
the masthead wraps before it truncates — a truncated wordmark is a
misprint (§9). Many links (8+): at ≥1200 they compress tracking to
0.08em; beyond that the build must move overflow into CONTENTS at all
sizes (a desktop contents sheet is legitimate — fairs have big issues).
Sticky + print-wipe: the masthead is *under* the wipe overlay (z 200) and
over sheets (z 60); the staple (90) stays above it.

**Accessibility (v2).** Landmark `<header>` + `<nav aria-label="Issue
contents">`. Focus order: skip link, wordmark, CONTENTS (mobile) or
links, then page. All hit areas ≥44px tall. The current-page signal is
weight + marker + `aria-current` (never colour alone). Mobile sheet:
focus moves into the sheet on open, is trapped lightly (Tab cycles the
sheet + button), Esc exits.

**Content merge.** The nav is the issue's own contents page worn at the
top; folio numbers in the mobile sheet are the sections' real order.

**Failure fallback.** No JS: masthead is a static strip, all links
visible (mobile menu renders open-stacked below the bar — the no-JS
mobile nav is a visible contents list, never a dead button).

**Reduced motion.** Highlight appears without drawing (instant), menu
sheet appears without feeding (opacity 0→1, 120ms), sticky shadow
instant.

**Performance & mobile variant.** Pure CSS + one IO sentinel. Negligible.
Mobile variant is the CONTENTS sheet above.

**Tokens.** `--ink`, `--ink-soft`, `--pink`, `--pink-wash`, `--teal`,
`--ease-pass`, `--ease-feed`.

### 6.14 Front-cover hero

**What & why.** The hero is the zine's front cover, and it is built like
one: an issue line at the top (number, place, date — real apparatus), the
shout headline with its ink copies (§6.2) and shout word (§6.7), a
confession lead paragraph, cover lines teasing the inside (with sheet
references), one duotone cover image (§6.9), and the edition data —
copies printed / copies left — counting up in Archivo Black. A visitor
should be able to judge the whole issue from this cover, the way you
judge a zine picked up off the hall table.

**Structure.** A `.sheet.sheet--cover` spanning the content column:
apparatus row (issue line left, "% inked" is *not* here — that's the
drum's job), h1 shout (with §6.2 copies + §6.7 word), lead paragraph
(Space Grotesk 500, 20px), a two-column zone ≥1200px (cover image left
55%, cover lines + edition data right), and a bottom cover strip: price
and the primary CTA ("GET A COPY" stamp button, §6.11/§11). The hero
sheet is `[data-register]` — hovering it aligns the whole cover (§6.3).

**Motion spec.** The load sequence (choreography below) composes §6.2
(settle), §6.6 (the h1 tears as part of the hero sheet's print — the hero
is above the fold, so its "print trigger" is load itself), §6.7 (shout
word at t=700), §6.9 (cover image settles), and counters: edition numbers
count 900ms `--ease-pass` from t=800.

**Choreography timeline (v2) — page load.**
- t=0 — First paint: black headline, lead, cover lines, data labels all
  readable; colour layers at pre-print states; staple already still.
- t=150–800 — Pink ink copy slides/springs in (§6.2).
- t=300–950 — Teal ink copy follows.
- t=350–850 — Headline tear completes across the same window (§6.6).
- t=400–1050 — Cover image settles and pools (§6.9, slightly delayed so
  type and image don't peak together).
- t=700 — Shout word shakes its one beat (§6.7).
- t=800–1700 — Edition counters count up; "COPIES LEFT" lands last, on
  its final real number.
- t=1700 — Cover complete. Nothing in the hero moves again except §6.3
  align, §5 parallax on the image's pink pass, and grain.

**State matrix (v2).**

| State | Headline | Image | Counters | Notes |
|---|---|---|---|---|
| Loading (pre-900ms) | Black visible; copies in flight | Settling | Counting or at final | Readable from t=0 at every beat. |
| Rest | Misregistered copies at rest | Settled, pooled | Final real numbers | — |
| Hover/focus-within | Whole cover aligns (§6.3) | Pink pass aligns | Unchanged | The proofreader's moment. |
| Scrolled-past | Rest + parallax drift | Pink pass drifts ±2px | Final | The cover stays printed below the fold line. |
| Sold out (edition gone) | Unchanged | Unchanged | "COPIES LEFT" reads 0 and the CTA becomes the §6.15 sold-out stamp state ("ALL COPIES GONE — JOIN THE REPRINT LIST") linking to §6.16's form | The cover confesses sell-out honestly rather than hiding the CTA. |

**Breakpoint behaviour (v2).** ≥1200px: two-column zone as specced.
768–1199px: single column, image above cover lines, image height capped
40vh. <768px: single column; shout at the scale's floor (3.25rem);
edition data becomes a 2-up row under the lead; CTA full-width (a thumb
stamp); the load timeline compresses — copies at 80/160ms delays, tear
300ms, counters start t=500 — total ceremony ≤1200ms, because a phone's
first screen is not a ceremony hall.

**Edge cases (v2).** No cover image (text-only issue): the cover lines
column expands to full width and the tear/settle carry the hero alone —
do not insert a decorative stock image (§9). Extremely long shout (CMS):
clamp at 3 lines with the scale stepping down one notch per extra line
(build-time class), never truncate a confession mid-word. Slow fonts:
§6.2's font rule applies — late Archivo Black = skip the settle, keep
the tear.

**Accessibility (v2).** The h1 is the headline (once); issue line is a
`<p>` in apparatus style, not a heading. Cover lines are a real list of
links to the sections they tease (with sheet numbers as visible text,
not the only cue). Counters are plain text at rest — counting is visual
only; AT reads final values from the DOM (JS writes the final value into
the node *first*, then animates a visual clone? No — simpler and
honest: the counter node has `aria-label` with the final figure, and the
animated text is `aria-hidden`). CTA is a real link/button, ≥48px tall.

**Content merge.** Every hero element is the cover's own content: the
headline is the confession, the counters are the edition, the image is
the cover art. There is no decorative layer to remove.

**Failure fallback.** No JS: the cover is complete and static at first
paint — copies at rest, counters at final numbers (HTML ships final
values; JS rewinds them to count).

**Reduced motion.** Static cover: aligned copies, no tear/shake/settle,
counters at final values, image sharp. Still unmistakably the cover.

**Performance & mobile variant.** The hero is the LCP element: its image
is the one image on the page allowed eager loading, ≤120KB duotone WebP
(§14). Total hero ceremony cost: three composited layers + one counter —
inside the frame budget. Mobile variant per breakpoints.

**Tokens.** `--ease-spring`, `--ease-pass`, `--dur-count`,
`--misreg-x`, `--misreg-y`, `--pink`, `--teal`, `--ink`, `--paper`.

### 6.15 Pasted-sheet cards

**What & why.** Listing content — releases, back-catalogue issues,
workshop dates — lives on pasted-sheet cards: small sheets stuck onto the
listing sheet, each with its duotone image, its shout-mini headline, and
its edition data (price, copies left). Cards are the theme's workhorse;
they must survive a 24-item grid without the page turning into a scrapbook
accident (§9 density rules apply per card).

**Structure.** `<article class="card">`: `--sheet` surface, 2px `--ink`
border, hard shadow `10px 10px 0` pink at 32% (alternating teal by grid
parity, matching §4's stack rule). Inside: figure (§6.9 treatment, pink
pass included ≥768px), H3 headline (Space Grotesk 700 — cards never
shout in Archivo; a grid of shouts is a riot), 2-line clamped standfirst,
data row (price Archivo Black 20px + copies-left label), and a whole-card
link (stretched-link pattern) with a visible "GET A COPY →" text link as
the focusable element. Cards are `[data-register]` and `[data-stamp]`.

**Motion spec.** Entry: the card prints with its parent sheet (§6.1) —
cards do not run their own pass ceremony; their colour layers belong to
the sheet's print. Hover (fine pointer): lift −4px, tilt toward pointer
max 2.5° (rotateX/Y from pointer position), 200ms `--ease-spring`;
shadow grows to 12px and swaps ink pink→teal over the same 200ms —
attention re-prints the card in the second ink. Release: 300ms back.
Press: §6.11 stamp (squash + splat at contact point).

**Choreography timeline (v2) — hover.**
- t=0 — Pointer enters; tilt tracking begins (rAF-throttled, lerp 0.2).
- t=0–200 — Lift and shadow swap complete; layers align (§6.3 runs in
  parallel — the card aligns *and* lifts, one gesture, two print truths).
- Hold — Tilt follows pointer within ±2.5°; beyond the card edge it eases
  back rather than snapping.
- t=leave — 300ms return to flat, misregistered, at rest.

**State matrix (v2).**

| State | Card | Shadow | Layers | Notes |
|---|---|---|---|---|
| Rest | Flat, 0° | 10px pink 32% | Misregistered | — |
| Hover | −4px, tilt ≤2.5° | 12px teal 45% | Aligned | Desktop only. |
| Focus-visible | −2px lift (no tilt) | 12px teal | Aligned | Plus the §6.13 focus ring on the card outline. Keyboard gets lift+align, not tilt. |
| Active | §6.11 squash | Compressed with card | Aligned | — |
| Scrolled-past | Rest | Rest | Rest + parallax on image pass only | Cards never re-print. |
| Disabled / sold out | Desaturated to teal-only print (pink pass removed), −0° forever | 10px `--ink-soft` 30% | Never aligns (§6.3 matrix) | A rotated "ALL COPIES GONE" stamp (Archivo Black, `--pink` at 85% on paper chip, −8°) overlays the figure — the one overlay this theme permits, because a sold-out stamp *is* content. CTA becomes "JOIN THE REPRINT LIST". |

**Breakpoint behaviour (v2).** ≥1200px: grid 3-up, full treatment.
768–1199px: 2-up, tilt max 1.5°. <768px: 1-up stack, no tilt (touch),
shadow 8px, stamp on tap; the sold-out stamp scales to the figure width.

**Edge cases (v2).** Missing image: the card's figure zone becomes a
printed title block (the issue's name in Archivo Black on `--teal-wash`)
— a text cover, common for real zines — never a grey placeholder. Long
headlines clamp at 2 lines with the full title in the link's
`aria-label`. Copies-left = "∞" for digital editions: the data row shows
"PRINTED ON DEMAND" instead of a fake number (§9: no invented scarcity,
and no fake infinity either — say what it is).

**Accessibility (v2).** One focusable element per card (the text link,
stretched over the card) — never nested interactives. Focus ring per
§6.13 spec, drawn on the card border so it survives tilt (ring is on the
flat outline, tilt is on the inner wrapper — the ring never rotates).
Sold-out state is text ("ALL COPIES GONE"), not colour alone. Card
min-height keeps tap targets ≥48px for the link's row.

**Content merge.** The card is a miniature of the thing it sells: its
image is the issue's cover, its data is the edition's data. The tilt is
the physicality of the pasted sheet, not a generic card effect.

**Failure fallback.** No JS: flat cards, correct data, working links —
tilt and align are enhancements. Images fall back per §6.9.

**Reduced motion.** No tilt, no lift, no align. Hover/focus swaps the
shadow ink instantly (pink→teal) as the attention signal.

**Performance & mobile variant.** Tilt is one rAF-throttled transform per
hovered card (only one card can be hovered at a time — the cost ceiling
is structural). Grid rendering: `content-visibility: auto` on cards
below the fold. Mobile variant per breakpoints.

**Tokens.** `--ease-spring`, `--sheet`, `--ink`, `--ink-soft`, `--pink`,
`--teal`, `--teal-wash`.

### 6.16 The confession form

**What & why.** The conversion form — newsletter signup, reprint list,
workshop booking, "send us your confession" story submission — is a
printed form torn from the zine's back page: ruled lines to write on, a
big stamp for a submit button, and errors delivered in the press
operator's voice. Forms are where themes usually abandon their world;
this one is where the world proves it can do paperwork.

**Structure.** A `.sheet` form: title (H2, torn reveal with its sheet),
one-line confession lead ("Tell us the thing. We print admissions, not
adverts."), fields as ruled lines — label above (apparatus style), input
with transparent background, 2px `--ink` bottom border, no box — a sheet
of lines, not a stack of rounded rectangles. Required fields marked with
a small pink staple glyph (drawn, §6.10's path at 12px) plus "(required)"
in the label's sr text. Submit: full-width stamp button — `--pink` fill,
`--ink` text (5.2:1), Archivo Black 20px uppercase, hard shadow; §6.11
stamp on press. Success replaces the form sheet's interior with the
stamped confirmation (below).

**Motion spec.** Field focus: the ruled line prints its second pass — a
teal line draws over the black rule (scaleX 0→1, 300ms `--ease-pass`)
while a pink tick (the staple glyph) stamps in at the label (120ms,
§6.11 squash at glyph scale). Blur with content: line stays teal. Blur
empty: line returns to black over 300ms. Error arrival: the field's line
goes pink (2px, with a 4px pink splat bullet at the message, §6.11's
blob at rest) and the message prints in two passes with the sheet
ceremony compressed (200ms/280ms) — errors are content, so they print
like content. Submit press: §6.11. Success: a big rotated stamp
("CONFESSION RECEIVED — № 042", Archivo Black, `--teal` border 3px,
−6° rotation) scales from 1.6→1 with the stamp squash curve (400ms
`--ease-stamp` + spring release) onto the confirmation sheet, with a
splat at its centre.

**Choreography timeline (v2) — submit → success.**
- t=0 — Press: button stamps (§6.11), label swaps to "PRINTING…".
- t=0–(server) — The form sheet's colour layers pulse once through a
  compressed two-pass (600ms total) — the press is running the form
  through. If the server answers sooner, the ceremony still completes
  its 600ms (a half-printed form that vanishes reads as a glitch, not a
  press).
- On success — Interior swaps (height animates 250ms `--ease-feed` only
  if the delta is <120px; larger deltas cut — do not animate a page
  lurching), stamp lands at +150ms (400ms), confirmation number counts
  (§5 counters, 600ms).
- On error — Error summary prints at the form top (two-pass, 480ms),
  focus moves to it; each invalid field's line and message per the error
  spec above, staggered 60ms per field so the eye can follow the
  operator's pencil.

**State matrix (v2).**

| State | Field line | Label/glyph | Message zone | Notes |
|---|---|---|---|---|
| Rest (empty) | 2px `--ink` | Apparatus label | Empty | — |
| Hover | Line thickens to 3px (150ms) | — | — | Inputs get hover feedback without colour change. |
| Focus | Teal pass draws (300ms) | Pink staple stamps in | Hint text (if any) in `--ink-soft` | Focus ring: the drawn teal line + the §6.13 outline on the field's row — fields are borderless, so the outline wraps the label+input row box. |
| Filled, blurred | Teal, steady | Staple stays | — | Filled = printed; it keeps its second pass. |
| Error | 2px `--pink` + splat bullet | Staple turns pink | Operator-voice message (§12), `role="alert"` per field via `aria-describedby` | Error is never colour alone: splat + message text + line weight. |
| Disabled (submitting) | `--ink-soft` | — | Button reads "PRINTING…" | Whole form `aria-busy`; fields disabled only after submission is actually in flight (never on click alone). |
| Success | Replaced by confirmation sheet | — | Stamp + number + what happens next (§12 voice) | Focus moves to the confirmation heading. |

**Breakpoint behaviour (v2).** ≥1200px: form sheet max 640px, two-column
row for name+email pairs. 768–1199px: single column, sheet full width.
<768px: single column; inputs 16px font (prevents iOS zoom — a hard
rule, not a nicety); submit button sticky at the viewport bottom within
the form's sheet bounds on long forms (the stamp stays reachable);
sticky button sits on a paper strip with the staple (§6.5's corner is
viewport — the form's strip carries its own small staple, drawn).

**Edge cases (v2).** Autofill: `-webkit-autofill` background is forced
to `--sheet` with an inset shadow trick, text to `--ink` — the browser's
yellow/blue autofill is an uninvited third ink. Long error messages
(translation +40%): messages wrap under the field, never overlay the
next field — the form's rows are in flow, always. Pasting into a field:
paste counts as filled (teal line) on the input event, no ceremony.
Server failure (network): drum-jam alert (§11) at the form top in
operator voice; the visitor's text is *kept* — "your words are safe on
the sheet" is a promise the implementation must keep (no state reset on
error, ever).

**Accessibility (v2).** Every input has a real `<label>` (visible,
apparatus style) — placeholder is never the label; placeholders are
examples in `--ink-soft` ("e.g. a gig that lost money"). Errors:
`aria-describedby` ties message to field; the summary is
`tabindex="-1"` and receives focus on error; `aria-invalid="true"` on
invalid fields. Required is stated in text, not by the staple glyph
alone. Focus order is visual order. The submit's "PRINTING…" state is
announced via a polite live region. Contrast: pink line (2.6:1) is
never the only error signal (see matrix); teal line on paper 4.6:1
passes the 3:1 non-text floor for the focus indicator, backed by the
outline.

**Content merge.** The form is a page of the zine (it prints with its
sheet, §6.1), its lines are the zine's ruled lines, its confirmation is
stamped with the press's own stamp and numbered into the print run —
the № is the submission's real queue number where the backend provides
one, or omitted where it can't (never invented, §12).

**Failure fallback.** No JS: a plain, fully working form — native
validation, server-rendered errors in the same voice, submit native.
Every enhancement (drawn lines, stamps) is progressive.

**Reduced motion.** Lines swap colour instantly; no stamp scale (the
success stamp appears, rotated, statically); no two-pass on errors —
messages appear with the summary.

**Performance & mobile variant.** All field motion is CSS transitions on
borders/transforms of single elements; the submit ceremony is capped at
600ms + server time. Mobile variant per breakpoints (16px inputs, sticky
stamp).

**Tokens.** `--ink`, `--ink-soft`, `--pink`, `--splat`, `--teal`,
`--ease-pass`, `--ease-stamp`, `--ease-feed`, `--dur-stamp`.

### 6.17 Colophon footer + the upside-down leaf

**What & why.** The footer is the zine's colophon: what inks, what
paper, who printed it, how many copies, and the credits — set as
apparatus, not as a corporate footer farm. And it keeps the theme's
credited flaw: one leaf of the colophon — the small print block — is
printed upside down, rotated 180°, with its explanation in the colophon
text ("the drum jammed on the last sheet; we kept it — see if you can
spot which leaf"). A flaw confessed is charm; the same flaw unexplained
would be a bug report.

**Structure.** A final `.sheet` (dark, `--ink` ground — the last sheet
is the night sheet, §4's ratio ends the page on the dark one by design):
colophon columns (inks & paper / the press (about links) / the run
(edition data, updated per issue)), a closing line in the confessional
voice, and the upside-down leaf: a bordered block (max 340px) containing
the copyright/small-print, `transform: rotate(180deg)`. The leaf's text
is real DOM text in normal reading order — rotation is purely visual.
Above the footer sheet, the §6.10 join ornament draws as usual. A
"REWIND THE DRUM" back-to-top link (apparatus style, teal underline)
sits at the colophon's end — smooth scroll, or instant under reduced
motion.

**Motion spec.** The footer prints with the standard §6.1 ceremony (its
dark sheet takes the shimmer, §6.8, after printing). The upside-down
leaf does not animate — it is discovered, not performed. Back-to-top:
smooth scroll 600ms `--ease-feed`-equivalent (native
`scroll-behavior: smooth` with a JS rAF scroll for the lerp feel,
§5 law: scrubbed/smooth scroll is the loop's job — implement via the
shared loop's scroll-to, 600ms, lerp profile ease-out).

**Choreography timeline (v2).**
- On entry — Footer sheet prints (770ms ceremony, §6.1).
- +200ms after print — Shimmer begins its drift (§6.8).
- Discovery beat — None. The leaf waits. (Specifying a non-event is the
  point: any animation on the leaf would announce the joke and kill it.)

**State matrix (v2).**

| State | Footer sheet | Upside-down leaf | Notes |
|---|---|---|---|
| Rest / printed | Paper text on `--ink`, shimmer drifting | Rotated 180°, static | — |
| Hover/focus on links | Teal-pass underline draw (200ms); on dark, underline is pink (teal on black is 3.0:1 — large/graphics only; underlines here are graphics paired with paper text) | Unchanged | Focus ring on dark: 3px `--pink` outline (5.2:1 on black ✓) — the dark-sheet focus variant, used by every interactive element on dark sheets. |
| Scrolled-past | Printed, shimmer continues | Rotated | Footer is the end; "past" = the §6.4 figure at 100%. |
| Print stylesheet | Footer prints as a normal colophon, leaf UN-rotated | 0° | Paper has no viewport jokes; the colophon text still credits the flaw, and the print reader is told the screen edition keeps it upside down. |

**Breakpoint behaviour (v2).** ≥1200px: three colophon columns.
768–1199px: two columns, run data full-width below. <768px: single
column; the leaf is full-width (max 340px cap lifted) — a small rotated
block on a phone is unreadable even as a joke; full-width keeps the
gag legible when the phone itself is turned.

**Edge cases (v2).** Overflow: the rotated leaf can poke outside its
box during layout — the footer sheet clips `overflow: clip` on its
padding box so the leaf never causes horizontal scroll. Text selection:
rotated text selects in DOM order (browsers handle this correctly with
transform-only rotation) — verified in the §10 gate, because a leaf you
can't copy the copyright from is a defect, not a joke. Translation: the
leaf rotates whatever text it holds; if a locale's small print exceeds
the block, the block grows (it is in flow) — never truncate legal text
for the gag.

**Accessibility (v2).** Screen readers read the leaf in normal order —
rotation is invisible to AT, which is correct: the *content* is ordinary
small print. A visually-hidden sentence in the colophon notes the
screen-edition joke for AT users who hear others mention it ("In the
visual edition, this leaf is printed upside down — the drum jammed; we
kept it."). Focus order follows DOM (visual rotation does not reorder
Tab). Dark-sheet focus ring per matrix. The colophon's contrast: paper
on ink 13.7:1; `--ink-soft` is NOT used on dark sheets (it is mixed
toward paper's light — on black it fails); secondary footer text uses
paper at 70% via `color-mix` (≈7.6:1 ✓).

**Content merge.** The colophon is the zine's real credits and data;
the leaf is its real small print. The joke is executed on genuine
content, not on a dummy block.

**Failure fallback.** No JS: footer static, printed, leaf rotated (CSS
transform is not JS). Nothing to fall back from.

**Reduced motion.** Shimmer off; back-to-top instant. The leaf, being
static, is unchanged — it is already the reduced-motion citizen of the
page.

**Performance & mobile variant.** One dark sheet + shimmer (already
budgeted in §6.8). Mobile variant per breakpoints.

**Tokens.** `--ink`, `--paper`, `--pink`, `--teal`, `--ease-feed`.

### 6.18 The feed strip (marquee)

**What & why.** One announcement per issue gets shouted along the top:
the feed strip — a drum-black band above the masthead whose message
repeats, moving like paper feeding through the press. It exists because
zines have cover banners ("SECOND PRINTING — BACK BY DEMAND"), and a
real announcement deserves the loudest furniture on the page. It is the
theme's only marquee, and it is rationed: one strip, one message, top of
page only.

**Structure.** An `<a>` (the whole strip is one link to the
announcement) with `--ink` ground, `--paper` text in Space Grotesk 700
13px uppercase, containing a repeated phrase sequence (the phrase ×4
minimum to fill ultrawide, duplicated in two identical spans for the
seamless loop), separated by drawn staple glyphs. The moving track is
`aria-hidden`; the link's accessible name is the phrase once, via
`aria-label`. Motion: translateX loop, 18s linear, with the press
judder — keyframes step the track 2px at each seam point (every 12.5%
of the loop, a 60ms hitch) so the feed feels mechanical, not like a
news ticker.

**Motion spec.** 18s per full loop (one phrase-width ≈ 4.5s — reading
speed for a shout). Pause on hover and on focus-within. The strip never
speeds up, never reverses.

**Choreography timeline (v2).** Continuous from load. The strip is
above the masthead and prints instantly with first paint (it is a cover
banner — covers don't ceremony). Judder beats at 0%, 12.5%, 25% … of
each loop.

**State matrix (v2).**

| State | Track | Notes |
|---|---|---|
| Rest | Feeding at 18s/loop | — |
| Hover | Paused | Reading a moving shout is work; the press holds the sheet while you look. |
| Focus-within | Paused + §6.17-style focus ring (paper ground context: teal ring fails on black at 3.0 for small — use the dark focus variant: 3px `--pink` outline on the strip) | Keyboard users can stop and read it. |
| Active | §6.11 stamp does NOT apply (the strip is a banner, not a button) | Click navigates; no squash on a full-width band. |
| Reduced motion | Static: the phrase shown once, left-aligned, no loop | The announcement survives intact; only the feed stops. |
| No announcement this issue | Strip absent entirely | An empty or filler strip ("WELCOME TO OUR SITE") is §9 slop. Absence is the correct state. |

**Breakpoint behaviour (v2).** ≥1200px: phrase 13px, loop 18s.
768–1199px: same size, loop 16s (narrower track). <768px: phrase 12px,
loop 14s, and the strip's height is 36px (tap target for the link is the
full strip — 36px is below the 44px ideal; compensate: the same
announcement is the hero's first cover line (§6.14), fully tappable —
the strip on mobile is a banner, the cover line is the control).

**Edge cases (v2).** Long phrases (translation): the loop duration
scales with measured track width at build/init (duration = width /
90px-per-second), so a long German announcement feeds at the same
reading speed instead of racing. Ultrawide monitors: phrase repeats
until the track is ≥2× viewport width (build computes copies; minimum
4). If JS is off: the track is static with the phrase repeated —
readable, honest, still a banner.

**Accessibility (v2).** The moving text is `aria-hidden`; the link's
name is the phrase once. Pause-on-hover/focus per matrix. Auto-moving
content that the user cannot pause is a WCAG failure — this strip can
be paused (hover/focus) and is stilled entirely under reduced motion.
Contrast: paper on ink 13.7:1.

**Content merge.** The strip carries the issue's single most important
real announcement and links to it. It is the cover banner of this exact
issue, reprinted every loop.

**Failure fallback.** No JS: static repeated banner (above). No
announcement: no strip (above).

**Reduced motion.** Static single phrase (matrix).

**Performance & mobile variant.** One CSS keyframe loop on one track —
transform only. The judder is inside the keyframes (no JS). Mobile
variant per breakpoints.

**Tokens.** `--ink`, `--paper`, `--pink`.

## 7. Page application map

**Home (the issue).** Feed strip (§6.18) if the issue has news → masthead
(§6.13) → front-cover hero (§6.14) → cover-line sections print in sequence
(§6.1): the latest confession (article lead), the back-catalogue grid
(§6.15), one dark sheet (the night confession — a single long story or
manifesto, shimmer on), the confession form (§6.16) as the final light
sheet → colophon footer (§6.17). The drum (§6.4) turns twice across the
whole read; "% inked" is the home page's quiet through-line.

**Listing (the catalogue / fair table).** Masthead → a catalogue sheet:
filters as apparatus (issue, ink, availability — real `<select>`s and
checkboxes in §11 dress) → card grid (§6.15) printing as one sheet (the
grid is ONE sheet with cards pasted on it — cards do not each run §6.1).
Pagination as folios (§11). Sold-out cards keep their places with their
stamps — a fair table shows what's gone; hiding sold-out stock is a
corporate habit this theme refuses.

**Detail (one release / one issue).** Masthead → the edition sheet:
duotone cover image large (§6.9), the confession (story of the release),
a pinned edition-data block (sticky beside the story for one viewport
height on ≥1200px: price, copies left counting on entry, per-copy data)
→ tracklist/contents as a ledger table (§11) → related cards (§6.15) →
form (§6.16) if the edition is gone (reprint list) or the stamp-button
purchase row if it isn't.

**About (the print shop).** The story of the press as a long confession:
who, where (the actual hall), the machine (a duotone photograph of the
real drum if the client has one — never a stock riso), the inks, the
jam stories. This page carries the build's credited flaw if the home
page doesn't (§1: one flaw per site, credited in the colophon either
way).

**Contact / order (the order sheet).** The confession form (§6.16) as
the whole page: one sheet, the form, the colophon footer directly
beneath. Checkout equivalents (per-copy purchase) hand payment to the
processor's page from the confirmation — this theme does not dress a
card form; the order sheet collects the order, the processor collects
the money, and the confirmation stamp (§6.16 success) is what the
visitor brings back.

**Article (a single confession).** Reading column 62–68ch, drop cap set
as a historiated initial in pink (the one display initial the theme
allows mid-text), pull-quotes as pasted slips (small rotated −0.4°
sheets, §4 rotation rule — decorative sheets only, and a pull-quote is
one), section joins with §6.10 ornaments, end mark: a small drawn
staple + "END OF CONFESSION" apparatus line.

**404 (the misprint).** A sheet printed wrong on purpose, once: headline
"THIS SHEET WAS MISPRINTED" (shout), the two passes deliberately at
double offset (6px) for this page only — the one licensed exaggeration
— a plain explanation, and the way back (home + contents links). The
misprint page must still work perfectly: every link live, contrast
intact, the joke purely in the registration.

## 8. Worked examples (v2: hero, mid-page, conversion — end-to-end)

### Example A — The hero: "ISSUE 07 — WE LIED ABOUT THE FIRST PRESSING"

A fictional indie label, *Hall Noise Records*, reissuing a sold-out
cassette. The confession: the first pressing was 300 copies, not the 500
the original cover claimed. The hero must carry that admission, the
reissue data, and the buy path — in one cover.

**Build.** Feed strip: "SECOND PRESSING — 300 COPIES — THE FIRST RUN WAS
300 TOO, NOT 500 —" (§6.18). Masthead: wordmark "HALL NOISE", links
Releases / Confessions / The Press / Order. Cover sheet (§6.14): issue
line "ISSUE 07 — PRINTED AT ST. BRIDE'S HALL — SATURDAY"; H1 shout:
"WE LIED ABOUT THE FIRST PRESSING" (shout word: **LIED**, §6.7); lead:
"The first run was 300 copies. We printed 500 on the cover because 500
sounded like a real label. This second pressing is 300 too — here they
are." Cover image: duotone of the cassette stack (§6.9). Cover lines:
"The full confession — sheet 2 · What the reissue costs and why —
sheet 3 · Hear the B-side — sheet 4". Edition data: "PRESSED 300 ·
LEFT" + counter. CTA: "GET A COPY — £9" stamp button.

**Scroll/load timeline (visitor's experience, from navigation).**
- t=0 — Wipe exit (§6.12) reveals the cover already readable: black
  headline, lead, data labels.
- t=150–950 — Ink copies spring in behind the headline; the tear
  completes across the same window.
- t=700 — LIED shakes once, 700ms, and stills. The confession's key
  word carries the machine's tremor.
- t=400–1050 — Cassette image settles, edges pooling teal.
- t=800–1700 — Counters run: PRESSED settles at 300, LEFT counts down-
  style to its real 212 (it counts *up* to 212 — counters count up,
  always; the number is a stock figure, not a countdown gimmick).
- Scrolling on — The cover aligns if hovered (§6.3), the drum in the
  rail has begun its first turn, "% inked" ~8%.

**Why it works.** Every number is checkable against the confession;
the loudest word is the admission; the buy button is on the cover
because a zine sells off its cover. Nothing on the sheet is decoration.

### Example B — Mid-page: the back-catalogue grid sheet

Same label, home page, third sheet: six back-catalogue cassettes, two
sold out, one print-on-demand.

**Build.** One catalogue sheet (§7 listing logic at home scale): H2
"THE BACK CATALOGUE, HONESTLY" (torn reveal on print), six §6.15 cards
in a 3-up grid. Card data (real, per §12 voice): "SPLIT TAPE WITH
FERN SIGNAL — £7 — 38 LEFT"; "LIVE AT THE HALL, RAIN LEAK AND ALL —
£8 — 0 LEFT" (sold out: teal-only print, ALL COPIES GONE stamp, CTA
"JOIN THE REPRINT LIST"); "FIELD RECORDINGS OF THE 38 BUS — PRINTED
ON DEMAND — £10" (data row reads PRINTED ON DEMAND, no number).

**Scroll timeline.**
- Sheet 20% visible — Sheet prints: pink pass over the whole grid
  (300ms), beat, teal pass (420ms). The grid prints as one sheet —
  six cards do NOT stagger-print individually (a fair table is printed
  in one pull; per-card ceremonies here would be confetti, §9).
- Headline tears in at +350 (§6.6).
- Images settle in IO order as the grid crosses the viewport, staggered
  90ms apart by the §6.9 concurrency rule — a wave of drying ink down
  the grid, not six simultaneous blurs.
- Hovering the sold-out card: nothing aligns, nothing lifts; the stamp
  stays. Hovering a live card: lift, tilt, align, shadow swaps to teal.
- Tapping the sold-out card's CTA scrolls to the confession form
  (§6.16) pre-addressed ("REPRINT LIST — LIVE AT THE HALL") — the
  form's lead line names the edition, because the form is a page of
  the same zine.

**Why it works.** The grid's honesty is structural: sold-out items keep
their seats, print-on-demand says so, and the only numbers on the sheet
are stock the label actually holds.

### Example C — Conversion: the reprint-list form sheet

The final light sheet of the home page (§6.16), headed "JOIN THE
REPRINT LIST".

**Build.** H2 (torn on print): "WHEN IT'S GONE, IT'S GONE — UNTIL
ENOUGH OF YOU ASK". Lead: "We reprint when 100 names are on the list.
No sooner, no 'limited drop' games. The list is at 63." (The count is a
real number from the backend, set in Archivo Black inline.) Fields:
Name (required), Email (required), Which edition? (select listing the
two sold-out editions + "Any of them"), One line for the confession
wall (optional textarea — printed confessions are moderated and the
label says so). Submit: "PUT MY NAME DOWN" stamp button.

**Interaction timeline.**
- Sheet prints on entry (§6.1); the form is usable from first paint —
  fields are native inputs under the ceremony.
- Focusing Email — Teal line draws (300ms), pink staple stamps beside
  the label (120ms).
- Submitting with a malformed email — Summary prints at top in two
  passes: "ONE LINE NEEDS ANOTHER LOOK —" focus moves to it; the email
  field's line goes pink with its splat; message in operator voice:
  "That email won't survive the post — it has no @. Your other words
  are safe on the sheet; fix this line and feed it again." Nothing the
  visitor typed is cleared.
- Submitting clean — Button stamps, reads "PRINTING…"; the press pulse
  runs 600ms; success: interior swaps, the stamp lands — "NAME DOWN —
  № 064" (the real new list count) — with the line "You are name 64 of
  100. When the list fills, the drum rolls and you get one email. One."
- The drum in the rail, at the page's foot, reads ~97% inked; the
  footer (§6.17) completes it.

**Why it works.** The conversion mechanic (100 names or no reprint) is
stated on the form itself, the count is real, the error keeps the
visitor's words, and the success is numbered into the same print run
the whole page has been counting.

## 9. Anti-slop — how THIS theme goes cheap, and the cure

| Failure | Why it happens | Cure |
|---|---|---|
| Pink body text | Fluoro pink is exciting; someone sets a paragraph in it | Pink on paper is 2.6:1 — it is physically unreadable. Pink is ink for graphics and display only (§2 hard rule). Lint: no `color: var(--pink)` below 20px. |
| Misregistration on body text | The offset is the brand, so it gets applied to everything | Body text is single-pass black, always (§1). Offsets live on chromatic layers and display copies only. Doubled 17px text is not a theme, it's a defect. |
| Grain so heavy the page looks dirty | Grain opacity creeps up "for texture" | Caps are specced (§6.8): 0.5 paper / 0.35 sheets / 0.3 dark, and worst-case text contrast ≥9:1 measured, not vibes. |
| Everything rotated a little | Rotation is charming, so every sheet gets 1–2° | §4: decorative sheets only, ±0.4° max, text sheets at 0°. A page where the form leans is a page nobody fills in. |
| A third ink sneaks in | A blue link here, a green success there | Links are teal-pass underlined; success is the teal stamp (§6.16). The palette table is closed: 4 anchors + labelled mixes. Any other hex in the CSS fails §10. |
| Stock "staple" clip-art or emoji fasteners | Quicker than drawing the SVG | Staples and tape are drawn paths (§6.5, §6.10) in the theme's own stroke. A photographed staple is a different material world and reads instantly as clip-art. |
| Perfect registration everywhere | A builder "fixes" the offsets as bugs | The 3px is the theme (§2 tokens). If everything aligns, you've built a flat pastel site with grain — the honesty is the product. |
| Re-shaking the shout word on hover | It was delightful once, so it gets wired to hover | §6.7: once, on print, never again. Repeated shake = screensaver. |
| Invented scarcity | "ONLY 3 LEFT!!" copied from e-commerce habit | Numbers are real or absent (§12). Print-on-demand says so; sold out says so. Fake urgency in a confessional theme is a lie in the brand's own voice. |
| Glossy gradients and soft shadows | Default web styling leaks in | Hard offset shadows only; gradients exist solely as ink pooling (§6.9) and shimmer (§6.8). A blurred drop shadow fails review on sight. |
| Bounce easing on everything | One "fun" cubic-bezier reused globally | Easings are the named press vocabulary (§5). `--ease-spring` is licensed for exactly two elements (§6.2, §6.15). |
| The upside-down gag repeated | It got a laugh, so three more blocks rotate | One leaf, in the colophon, credited (§6.17). A second rotated block is a bug the visitor reports. |
| Counters in a rounded sans | Archivo Black "looked heavy" for numbers | Counters are Archivo Black (§3) with width reservation. Data set in a friendly rounded face turns the print-run ledger into a fintech widget. |
| Per-card print ceremonies in grids | Every element spec applied to every instance | A grid prints as one sheet (§8 Example B). Ceremony is rationed by sheet, not by element count. |

## 10. Quality gate

All items are blocking unless marked (advisory). The theme may not ship
with a blocking item failed.

1. **Palette closure** — CSS contains only the 4 anchor hexes + mixes
   derived from them via `color-mix`. Any other hex fails.
2. **Pink discipline** — No pink text below 20px; no pink as the sole
   carrier of any meaning; black-on-pink ≥ AA verified (5.2:1).
3. **Single-pass text** — Body text (≤19px) has no offset duplicate, no
   blur, no fade anywhere in its lifecycle. Verified by disabling JS:
   the page reads perfectly.
4. **No-JS completeness** — With JS off: all content visible, all layers
   at rest/final states, counters at final values, nav fully usable,
   form submittable.
5. **900ms promise** — On a throttled mid-tier device, no above-the-fold
   element remains doubled, blurred, clipped, or hidden past 900ms
   from first paint.
6. **Print permanence** — Scroll up/down repeatedly: nothing un-prints,
   nothing replays except parallax/ambient; shout word shakes exactly
   once per page load.
7. **Staple stillness** — The staple's computed transform is `none` at
   every scroll position, breakpoint, and state. Any exception fails.
8. **Focus visibility** — Every interactive element shows the theme
   focus spec (teal ring on light, pink on dark) at 200% zoom; focus is
   never carried by a moving layer.
9. **Contrast audit** — Measured, not assumed: black/paper 13.7:1,
   teal text ≥14px only, grain's worst-case text contrast ≥9:1, dark-
   sheet secondary text ≥7:1.
10. **Reduced motion** — With `prefers-reduced-motion`: aligned static
    passes, still grain, no shake/tilt/wipe; every content item
    reachable and identical in substance.
11. **Upside-down leaf** — Exactly one; rotated via transform only;
    selects and copies correctly; un-rotated in print; credited in the
    colophon text.
12. **Numbers audit** — Every number on the page (copies, prices,
    counts, №s) traces to real data or is removed. "% inked" is
    computed, never hardcoded.
13. **Performance** — §14 budget met on the reference device; one rAF
    loop only (grep the JS: a second `requestAnimationFrame` driver
    fails); no layout-thrash in the scroll handler (reads cached at
    resize, writes are transform/opacity only).
14. **Faces survive duotone** — Any photograph containing faces passes
    the §6.9 mid-tone rule at arm's-length review. (Advisory for
    non-face imagery.)
15. **Voice pass** — All microcopy read against §12: no invented
    urgency, no corporate filler, errors in operator voice, numbers
    specific.

## 11. Component inventory (v2)

Every component a real site needs, in this theme's dress. Treatments
assume the §6 elements where they exist.

- **Buttons.** Primary: the stamp button — `--pink` fill, `--ink`
  Archivo Black 20px uppercase text, hard shadow 6px teal, §6.11 stamp
  on press, shadow compresses to 2px while stamped. Secondary: paper
  button, 2px `--ink` border, Space Grotesk 700, shadow pink; hover
  draws the teal underline pass inside its bottom edge. Ghost/text
  button: apparatus label with teal-pass underline draw (200ms).
  Disabled: `--ink-soft` border and text, no shadow — an unstamped
  sheet; label states why where it matters ("DRUM EMPTY — REPRINT
  PENDING" is a state, not a style).
- **Inputs / textarea.** §6.16 ruled lines. Textarea gets 3 ruled lines
  (repeating-linear-gradient at the body line-height) so writing stays
  on the lines.
- **Select.** A ruled line with a drawn chevron (staple-leg path);
  open menu is a small sheet with hard shadow, options as apparatus
  rows, selected option carrying the pink staple glyph.
- **Checkbox / radio.** Ink-boxes: 20px squares, 2px `--ink` border;
  checked = a pink tick drawn in (stroke draw, 200ms) slightly
  overshooting the box — a hand tick, not a glyph. Radio: circle with
  a teal centre blob that stamps in (§6.11 at 60% scale). Focus ring
  per §6.13.
- **Toggle.** The duplex switch: a sliding sheet tab labelled "ONE
  SIDE / BOTH SIDES" — the track is a paper strip, the thumb a small
  sheet that feeds 24px with `--ease-feed`. Used for real either/or
  settings (single/duplex printing, email/plain-text editions).
- **Badges.** Edition chips: `--pink` fill, `--ink` Archivo Black 12px
  ("2ND PRINTING"), slight −1° rotation (badges are stickers — the one
  component allowed its own rotation, §4 exception logged here), hard
  3px black shadow. Teal variant for "BACK IN STOCK".
- **Alerts.** Drum-jam alerts: a sheet strip with pink left bar (6px)
  and operator-voice text (§12) for errors; teal bar for success/
  information; black bar for neutral notices. Dismiss = a small drawn
  staple that "unstaples" (rotates −20° and fades, 200ms) — the note
  is unpinned, not closed.
- **Tables.** The ledger: full-width rules (1px `--ink` at 30%, header
  rule 2px), apparatus column heads, numbers in Archivo Black
  right-aligned with width reservation, total row on `--teal-wash`
  with the total in teal-deep. Row hover: pink-wash swipe. A table is
  a printed ledger — no zebra striping (ledgers rule lines, they
  don't shade alternate rows; the total row is the one shaded row).
- **Pagination.** Folios: "SHEET 2 OF 5" apparatus text with prev/next
  as drawn arrows (staple-leg paths); numbered folios as pasted slips,
  current folio carrying the pink swipe (§6.13 marker logic).
- **Modal.** A fresh sheet over the stack: scrim is `--ink` at 55%
  with grain (§6.8 tile at 0.2) — the table under a held-up sheet;
  the modal sheet feeds in from the top (300ms `--ease-feed`) with its
  own compressed two-pass; the immovable staple is covered (§6.5
  z-order) because new paper covers the binding. Esc/backdrop closes
  by feeding the sheet back up. Focus trapped inside; return focus to
  the invoker.
- **Toast.** Slips: small paper slips pinned at bottom-left, beside
  the staple's column, each with a drawn staple; they feed up 200ms,
  stack with 8px gaps, and are pulled off (translateX −110%, 250ms)
  on dismiss/timeout (6s, paused on hover). Toasts announce via
  polite live region; max 2 visible — a third waits, because a wall
  of slips is a mess, not a notification system.
- **Tabs.** Issue tabs: folder-style tabs along a sheet's top edge,
  the active tab's sheet in front (border-bottom merged), labels in
  apparatus; switching cuts instantly (sheets don't animate between
  siblings — the tab you pick is already printed; its colour layers
  run the compressed print, 200ms/280ms, if it has never been shown).
- **Accordion.** Folded sheets: headers with a drawn fold arrow
  (chevron from the staple path); opening unfolds — height animation
  is banned (§5), so panels reveal via clip-path inset (300ms
  `--ease-feed`, the §6.6 mechanism without the torn profile — a
  clean fold line). One open at a time in apparatus contexts (FAQ,
  tracklists); multi-open allowed in catalogue filters.
- **Breadcrumb.** The running head: "ISSUE 07 / RELEASES / SPLIT TAPE"
  in apparatus style with staple-glyph separators, at a sheet's top —
  it is the book's running head, not a UI chrome import.
- **Tooltip.** A tape label: `--pink` at 90% fill, `--ink` 12px text,
  torn short ends, appears above its target after 400ms hover/focus,
  drawn in with the §6.10 tape motion at half duration. Never the
  only carrier of essential information.
- **Search.** A ruled-line input (§6.16) with a drawn magnifier
  (circle + staple-leg handle); results print as a fresh sheet below
  (compressed two-pass), result rows as ledger rows (§11 table)
  with the matched term carrying the pink-wash swipe.
- **Pricing.** Per-copy pricing block: three pasted slips (1 COPY /
  3 COPIES / THE WHOLE RUN) with Archivo Black prices, the middle
  slip carrying the pink badge ("MOST POSTED"); features as ledger
  lines with drawn ticks. Prices are per physical copy — this theme
  sells objects.
- **Author / credit chip.** Duotone circular portrait (§6.9 treatment
  at 40px) + name in Space Grotesk 700 + role in apparatus; the
  circle's pink pass offset is 2px at this size (offsets scale with
  the artefact — a §2 exception for ≤48px elements: `--misreg` halves).
- **Progress steps (order/booking).** Print passes as steps: "SHEET
  FED → PINK DOWN → TEAL DOWN → STAPLED" — the checkout's stages
  named for the press, current step's label in Archivo Black, done
  steps carrying drawn ticks.
- **Empty states.** A blank sheet, printed frame, one apparatus line
  and the voice line (§12): the sheet exists, nothing is on it yet,
  and the copy says what would go there. Never an illustration of a
  mascot.
- **404.** §7's misprint page.

## 12. Content & copywriting voice (v2)

The voice is the person who runs the press, confessing. First person
plural ("we printed", "we lied"), past tense for what happened, present
tense for what is on the sheet, numbers always exact.

**Headlines.** Shouted admissions or announcements, Archivo Black,
never a marketing abstraction. Pattern: a concrete claim a person
could be challenged on.
- ✓ "WE LIED ABOUT THE FIRST PRESSING"
- ✓ "300 COPIES. 212 LEFT. THAT'S THE WHOLE STORY."
- ✗ "EXPERIENCE THE MAGIC OF INDEPENDENT MUSIC" (unconfessable mush)
- ✗ "LIMITED EDITION — ACT FAST!!" (invented urgency; also the theme
  never uses exclamation marks in headlines — the type is already
  shouting)

**Labels & apparatus.** Factual, specific, dated where relevant:
"ISSUE 07 — ST. BRIDE'S HALL — SATURDAY", "PRINTED IN TWO INKS ON
RECYCLED STOCK". A label that could sit on any website ("LEARN MORE",
"OUR SERVICES") is rewritten until it could only sit on this one
("WHAT THE GRANT ACTUALLY BOUGHT", "SHEET 3 — THE JAM STORY").

**Buttons.** Verbs from the press room: "GET A COPY", "PUT MY NAME
DOWN", "FEED IT AGAIN" (retry), "REWIND THE DRUM" (back to top). Never
"SUBMIT", never "CLICK HERE".

**Error voice.** The operator, not the system: what happened, in press
terms; what is safe; what to do. Never blame the visitor, never say
"invalid".
- Email: "That email won't survive the post — it has no @. Your other
  words are safe on the sheet; fix this line and feed it again."
- Network: "THE DRUM JAMMED. Nothing was printed and nothing was
  lost — your words are still on the sheet. Feed it again when ready."
- Empty required field: "This line is still blank, and the press
  can't print a blank. A name will do — it doesn't have to be fancy."

**Empty-state voice.** A blank sheet, honestly labelled: "NOTHING
CONFESSED YET. The page is blank and the drum is warm — when the
first story lands, it prints here." Search with no results: "NO
SHEET MATCHES. The press printed everything it has; try fewer words,
or a different confession."

**Success voice.** Numbered and final: "NAME DOWN — № 064. You are
name 64 of 100. When the list fills, the drum rolls and you get one
email. One." Success copy always states what happens next and what
will NOT happen (no spam promise, in voice).

**Progress voice.** The "% inked" figure is data, not copy — but its
two authored states are: at 100%, "100% INKED — END OF SHEET" (§6.4);
during long loads, "THE DRUM IS WARM. STILL PRINTING…" (§6.12). No
other loading phrases exist in this theme.

## 13. Full-page scroll choreography map (v2)

The home page, top to bottom, as the visitor experiences it. (Other
page types reuse the same beats per §7.)

1. **Arrival (0%, t=0).** Wipe exit or first paint. Staple already
   still in the corner. Feed strip feeding. The cover is readable in
   black; ink copies are mid-flight.
2. **The cover completes (0–5%, t≈1700ms).** Copies settled at the
   honest 3px; LIED has shaken its one beat; counters landed on real
   numbers; drum at ~15°, band a pink stub, "% inked" in single
   figures. The visitor's takeaway is complete even if they go no
   further — the cover did its job.
3. **First join (~8%).** The staple-and-tape ornament draws (§6.10).
   Small, quick — the page's first proof that scrolling manufactures
   the document.
4. **Confession sheet (10–35%).** Prints two-pass on entry; its
   headline tears; pull-quote slip sits at its −0.4°. Drum turning
   through its first full rotation across this stretch; parallax
   spread breathes ±2px on the sheet's image pass.
5. **Catalogue sheet (35–60%).** The grid prints as one pull (§8B).
   Images dry in a 90ms-staggered wave. At 50% exactly, the drum's
   ink-window flips pink→teal and the band's teal segment begins —
   the page's midpoint is marked by the machine changing drums, a
   beat most visitors will feel without naming.
6. **The night sheet (60–78%).** The dark sheet prints; shimmer
   starts its 9s drift 200ms later; grain goes soft-light. The
   pace of the page deliberately slows here — one long story, no
   cards, no counters. Contrast of mood is a choreography tool.
7. **The form sheet (78–95%).** Prints; the visitor who acts meets
   §8C's timeline. The drum is at ~650°; "% inked" in the 90s.
8. **The colophon (95–100%).** Final join ornament; footer sheet
   prints on dark; the figure lands on "100% INKED — END OF SHEET";
   somewhere in the small print, a leaf is upside down, saying
   nothing. The last feeling of the page is a finished object, bound
   by the same staple that was there at the top — which never moved.

## 14. Whole-page performance budget (v2)

Reference device: Moto G4-class Android, 4G throttled (1.6Mbps,
150ms RTT), 4× CPU slowdown for lab checks.

| Budget | Limit |
|---|---|
| Initial HTML + CSS | ≤ 120KB (CSS ≤ 85KB, no framework) |
| JS (all, gzipped) | ≤ 45KB — one IO manager, one rAF loop, form/print handlers; no library |
| Fonts | ≤ 130KB total (Archivo Black latin subset ~55KB; Space Grotesk 400/500/700 subset ~75KB), `font-display: swap`, preloaded display face only |
| Grain tile | ≤ 8KB WebP, one tile for the whole site |
| Images | Duotone WebP; hero ≤ 120KB (eager, LCP), all others ≤ 100KB each and lazy |
| Total initial route weight | ≤ 700KB |
| LCP | ≤ 2.0s on reference device (the hero's black headline is the LCP candidate by design — text paints before its ink copies, which is why the copies are decorative) |
| Frame budget (scroll) | Shared rAF loop ≤ 4ms script per frame; composited transforms/opacity only; zero layout reads inside the loop (geometry cached on resize) |
| Long tasks | None > 50ms after load; counter/IO callbacks ≤ 2ms each |
| INP | ≤ 200ms (stamp feedback is transform-only and starts on pointerdown) |

**Cut order when the budget breaks** (in this order, logged in the
build's DECISIONS note): 1) fluoro shimmer (dark sheets go matte);
2) parallax registration drift (layers lock at rest offsets); 3) grain
crawl freezes to a static frame; 4) card tilt (lift + align remain);
5) torn reveals become hard cuts. The two-pass print, the drum, the
staple, and every fallback are never cut — they are the theme.

## 15. Build-order checklist (v2)

1. Tokens first: the 4 anchors, derived mixes, `--misreg` pair,
   duration/easing tokens (§2, §5). Palette-closure lint (§10.1)
   wired into CI from this step.
2. Static sheets: layout grid, rail, sheet component, type scale —
   the complete page with JS disabled. This state must already pass
   §10 items 3, 4, and 9. (Build the fallback first; enhance into
   it.)
3. Chrome: staple (§6.5), masthead (§6.13), feed strip (§6.18),
   colophon with its leaf (§6.17).
4. The print engine: IO manager + two-pass layers (§6.1) + catch-up
   compression + watchdogs (§5 laws).
5. The shared rAF loop: drum/band/figure (§6.4), parallax (§5).
6. Grain + shimmer (§6.8) with their pause/freeze signals.
7. Hero composition (§6.14) with §6.2, §6.6, §6.7, counters.
8. Images: duotone pipeline + ink-pool settle (§6.9).
9. Interactive layer: hover-to-align (§6.3), stamp click (§6.11),
   cards (§6.15).
10. Forms (§6.16) incl. error/success ceremonies and the no-JS path.
11. Transitions (§6.12) — last, because they decorate navigation that
    must already work without them.
12. Reduced-motion pass: every element's variant implemented and
    diffed against §6 specs (not a global `* { animation: none }` —
    that kills the aligned static states' *styling*, which must
    remain).
13. Accessibility audit against §10 items 2, 3, 8, 9, 11 — measured,
    with the contrast figures recorded.
14. Performance pass against §14 on the reference device; apply the
    cut order if needed, in order, logged.
15. Voice pass (§10.15): every string on the page read aloud against
    §12. If a string could belong to another site, it is rewritten
    or the build is not done.
