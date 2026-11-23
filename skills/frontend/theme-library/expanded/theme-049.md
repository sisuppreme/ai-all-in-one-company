# 49. Pearl Diver's Breath — Expanded (v1 + v2)

> Identity preserved exactly from the original entry: the ama diver's
> single-breath concept; the same five palette anchors — Surface foam
> `#EAF3F1`, Shallow `#8FC1BC`, Mid-water `#2E6E6A`, Seabed `#0E3236`,
> Pearl `#E9D8C8`; Cormorant Garamond + Karla; all 9 original signature
> elements deepened, not redesigned (dive line drop, foam surfacing,
> depth gauge, thinning light rays, seabed pin, flaw highlight, nacre
> diagram draw, bubble release click, surface break), plus 9
> page-family elements to reach 18. Original ~950 words → this file.

## 1. Concept & world

The page is one dive on one breath. The ama — Japan's free-diving
women who harvest oysters without air tanks, some into their eighties —
go down on a single lungful, work the seabed briefly and deliberately,
and come back up before the breath runs out. This theme takes that
discipline literally as a page structure: the visitor's scroll *is*
the breath. The page opens at the bright surface (foam sections, the
atelier's name, the day's catch), descends through deepening water
(mid-water catalogue, the craft of nacre), arrives at a pinned dark
seabed where the one featured pearl is held in view while its story
surfaces beside it, and then — because a dive that does not come back
up is a drowning, not a theme — ascends through brightening sections
to a foam-white footer. The visitor surfaces at the end of the page.
That return is not optional decoration: roughly the final third of
every Pearl Diver's Breath page is ascent, and any build that spends
the whole scroll descending and then simply *stops* at the footer has
failed the theme's central promise.

**The one law: the breath is one, and no depth is invented.** Every
depth printed anywhere on the page — the margin gauge's readout, the
animated depth counter, each section's depth stamp, the footer's dive
record — is read from a single value, `--depth-now`, computed once per
frame by the shared loop from the visitor's actual scroll position
inside the declared dive track (§4). No depth figure may be typed by
hand into copy, hard-coded into a second script, or rounded
differently in two places: the gauge, the counter, the stamps and the
record are four printings of one number, and a page where the gauge
says −19 m while a section stamp says −22 m has broken the law even
if every animation is beautiful. The corollary is the honesty rule:
the page may never claim more depth than the visitor has scrolled.
The maximum is −28 m, reached only inside the seabed pin; a build
whose gauge reaches −28 m in the catalogue section has lied about the
dive, and lying about the dive is a blocking quality-gate failure
(§10).

**Best fit.** Single-product and small-catalogue luxury with a true
harvest story: a pearl atelier or ama cooperative selling a handful of
pieces per season; a free-diving school or breathwork retreat whose
whole method is descent and return; a marine conservation appeal that
takes the visitor down to the reef it is asking them to protect; a
perfume or tea presented as something gathered from depth. The theme
needs a product that rewards slowness and a story that genuinely has
a bottom — something found, harvested or earned at the deepest point.

**When NOT to use it.** Dense catalogues (a hundred products cannot
each sit at a depth); anything the visitor must scan fast (comparison
tables, documentation, dashboards — the dive forbids skimming by
design); sites whose content is mostly forms; any brand that cannot
commit to the ascent — a page that ends dark because the designer ran
out of sections is the theme's most common failure. Also refuse it
for medical, safety or emergency content: a page about actual diving
safety must never make breath-holding feel like a game mechanic.

**Mood in one line.** Bright, held, quiet — the hush of being under
water with work to do, and the relief of the surface at the end.

**Grounding facts the design answers to.** The ama dive with a
rope tied at the waist running up to the boat — the rope is §6.1's
line and §6.3's spine, not a decorative vertical. They work a
bottom measured in tens of metres, not hundreds — hence the
theme's −28 m ceiling, deep enough to be earned, shallow enough
to be true. They surface to a floating tub or the boat and rest
between dives — hence the page's insistence that surfacing is a
*place* (the foam footer, §6.14) and not merely the absence of
depth. And the harvest is seasonal and limited by the
cooperative's own rules — hence the catalogue's small counts
(§6.12's 61 dives, 214 oysters) and the refusal of infinite
inventory patterns in §11. A build that gets these facts wrong —
a 200-metre gauge, an endless catalogue, a footer that is just a
darker section — has decorated the theme instead of building it,
however pretty the water looks.

## 2. Palette

Five anchors, inherited unchanged. The derived list is **closed**:
builders may not invent intermediate water colours; depth is expressed
by moving between the declared stops, never by tinting ad hoc.

| Token | Hex | Role | Usage ratio | Pairing / contrast (measured for this expansion) |
|---|---|---|---|---|
| `--foam` | `#EAF3F1` | Surface: hero, ascent, footer, all text ground above −6 m | ~30% | Ground for `--ink-deep` (12.2:1) and `--mid` (5.2:1) |
| `--shallow` | `#8FC1BC` | Shallow water band, ray colour, gauge fill, card water | ~18% | On `--foam` 1.75:1 — **never text**; on `--seabed` 7.0:1 — licensed for deep-band labels |
| `--mid` | `#2E6E6A` | Mid-water band ground, links and rules in the surface band | ~22% | On `--foam` 5.2:1 — the only anchor that carries text in the surface band; on `--seabed` 2.4:1 — never text in the deep band |
| `--seabed` | `#0E3236` | Deep band ground, pinned seabed, footer-of-the-deep | ~24% | Ground for `--pearl` (10.0:1) and `--shallow` (7.0:1) |
| `--pearl` | `#E9D8C8` | The pearl itself, deep-band text, nacre highlights, the gauge marker | ~6% | On `--seabed` 10.0:1 — deep-band body text; on `--foam` 1.2:1 — never text at the surface |

Derived tokens (the complete list):

| Token | Value | Role |
|---|---|---|
| `--ink-deep` | `#0E3236` (= `--seabed`) | Body text in foam and shallow bands — the seabed colour is the ink; there is no black on this page |
| `--ink-pale` | `#E9D8C8` (= `--pearl`) | Body text in the deep band |
| `--mid-deep` | `#1E4A47` | Hover/pressed state of `--mid` links and buttons; 7.4:1 on `--foam` |
| `--foam-dim` | `#D9E8E4` | Card ground and skeleton water inside the surface band |
| `--nacre-1 / --nacre-2 / --nacre-3` | `#E9D8C8 / #D9C6E4 / #BFE0DA` | The three nacre gradient stops (§6.16); hue travel is confined to the triangle these three points make — warm pearl, faint violet, faint sea-green, never beyond |
| `--ray` | `#FFFFFF` at 0.35 alpha max | Light rays (§6.4); alpha is a hard cap, not a default |

**Contrast law (blocking).** Darkening is achieved by *section
backgrounds changing at declared depth bands* (§4), never by an
overlay that progressively dims text. Any scrim used for imagery is
capped at 0.35 alpha and may never sit behind body text. Text colour
switches by band, not by gradient: foam band text is `--ink-deep`,
deep band text is `--ink-pale`, and the mid band (background `--mid`)
carries `--foam` text at 5.2:1. A screenshot taken at any scroll
position must pass WCAG AA for every visible text element; §10
audits three depths.

**Dark mode.** There is no inverted dark mode; the page already
contains its own darkness, earned by depth. Under
`prefers-color-scheme: dark`, the *surface* band deepens one step —
hero and footer grounds become `--mid` with `--foam` text — so a
dark-mode visitor starts at dusk on the water rather than at noon.
The deep band is unchanged (it is already the bottom). The dive
structure, gauge and law are untouched.

## 3. Typography

Two families, inherited: **Cormorant Garamond** for display and
**Karla** for everything that must be read, counted or tapped.

| Role | Face / weight | Size (≥1200px) | Line-height | Tracking | Rules |
|---|---|---|---|---|---|
| Display (hero headline) | Cormorant Garamond 500 | 76px | 0.98 | −0.01em | Italic permitted for exactly one word — the word that names the pearl |
| Section headline | Cormorant Garamond 500 | 44px | 1.05 | −0.005em | Never uppercase; the water does not shout |
| Standfirst / lead | Karla 400 | 20px | 1.55 | 0 | Max 34ch in the surface band, 46ch in the deep band (the eye slows at depth) |
| Body | Karla 400 | 17px | 1.65 | 0 | Measure 58–66ch at the surface, narrowing to 48–54ch at the seabed (§4) |
| Depth stamp / data | Karla 700 | 13px | 1.2 | 0.14em, uppercase | Always tabular figures; always read from `--depth-now` or the section's declared depth (§6.17) — never typed |
| Caption (incl. the flaw caption) | Karla 400 italic | 14px | 1.5 | 0 | The flaw caption is set in the same size as every other caption — pride is not emphasis (§9) |
| Button / label | Karla 700 | 14px | 1 | 0.12em, uppercase | Sentence rhythm inside: "Go down to her" not "DOWNLOAD" |

**Five type laws.**
1. **Figures are tabular, always.** Depth, metres, millimetres and
   counts use Karla's tabular figures at every size; a gauge whose
   digits change width as they count makes the needle appear to
   tremble, and the needle never trembles.
2. **Depth is written with the minus sign and the unit, every time:**
   `−28 m`, never `28` alone, never `28m deep!`. The gauge, stamps,
   counters and record all use the identical string format, produced
   by one formatter function.
3. **Cormorant never carries data.** If a number matters, it is Karla.
   Cormorant is for names, titles and the one italic word.
4. **No headline may promise a depth the page does not reach.** A
   standfirst saying "twenty-eight metres down" is a contract; §10
   checks the dive actually reaches −28 m.
5. **Line-height loosens with depth** (1.55 surface → 1.75 seabed):
   reading slows as the light goes, and the leading admits it.

## 4. Layout language

**The dive track.** The page body is one `<main class="dive-track">`.
Its height is the dive. Scroll progress `p` through the track maps to
depth by the declared function, implemented once in the shared loop:

- `p` 0 → 0.55 (descent): depth = −28 × (p / 0.55)
- `p` 0.55 → 0.68 (the seabed hold, containing the §6.5 pin): depth = −28
- `p` 0.68 → 1.00 (ascent): depth = −28 × (1 − (p − 0.68) / 0.32)

The function lives in exactly one place in the codebase; the gauge
(§6.3), counter (§6.12), stamps (§6.17) and footer record (§6.14) all
subscribe to its output. Jump-scroll (a visitor dragging the scrollbar
to the middle) lands the page at the correct depth instantly — the
function is positional, not cumulative, so there is nothing to catch
up and nothing to fake.

**Depth bands.** Sections declare their band by the depth at their
midpoint: *surface band* 0 to −6 m (ground `--foam`), *shallow band*
−6 to −14 m (ground `--foam` with `--shallow` water shapes, or
`--foam-dim` cards), *mid band* −14 to −22 m (ground `--mid`, text
`--foam`), *deep band* −22 to −28 m (ground `--seabed`, text
`--ink-pale`). Band boundaries are authored, not interpolated: a
section is one band, wholly, so text contrast is always at a tested
value and never at an untested blend.

**Grid and measure.** 12-column grid ≥1200px, content measure
narrowing with depth: surface sections span 10 columns, mid-band 8,
the seabed story 6 — the page literally narrows as it deepens, like
the diver's field of vision. The **gauge margin** is a fixed 72px
left rail (≥1200px) holding the dive line (§6.1), gauge (§6.3) and
depth stamps; content never enters it. Between 768–1199px the rail
becomes a 48px mini-gauge; below 768px it collapses to a top depth
bar (§6.3 breakpoints).

**Density.** Density falls with depth. Surface sections are airy and
commercial (cards, figures, the day's catch); the mid band holds one
idea per section; the deep band holds exactly one object — the
featured pearl — plus its story. A build that puts a card grid on the
seabed has not understood the theme: at −28 m there is room for one
thing, held carefully.

**The dive data object.** One build-time data object — call it
`DIVE` — is the single source every depth-bearing element reads:
`DIVE.maxDepth` (28), `DIVE.track` (the §4 breakpoints 0.55 /
0.68), `DIVE.pearl` (name, measure, flaw, price, dive date, diver),
`DIVE.harvest` (dives, oysters, per-pearl depths for §6.11),
`DIVE.bands` (each section's declared band and midpoint depth).
The gauge's maximum, the stamps' values, the counters' targets,
the form's options and the footer's record are all rendered from
`DIVE` or computed from scroll by the §4 function — there is no
second place in the codebase where a depth, a price or a pearl
name is written down. Changing the featured pearl for a new season
is a one-object edit; §10's audits exist to catch any build where
that stopped being true.

**Bands at a glance.**

| Band | Depth | Ground | Text | What lives there |
|---|---|---|---|---|
| Surface | 0 to −6 m | `--foam` | `--ink-deep` | Hero, invitation, footer |
| Shallow | −6 to −14 m | `--foam` / `--foam-dim` | `--ink-deep` | Catalogue (§6.11), rays (§6.4) |
| Mid | −14 to −22 m | `--mid` | `--foam` | Craft (§6.7), figures (§6.12) |
| Deep | −22 to −28 m | `--seabed` | `--ink-pale` | The pin (§6.5), the drowned page (§6.18) |

**Whitespace is water.** Gaps between sections are not empty; they
are the water the visitor swims through, coloured by the band they
belong to. Section padding is therefore generous (120px surface,
160px mid, 200px around the seabed) and never collapses below 64px at
any breakpoint — compressing the water to fit more content is the
theme's cardinal layout sin.


## 5. Full motion system

Five named easings, used by every element and nothing else:

| Token | Curve | Character |
|---|---|---|
| `--ease-sink` | `cubic-bezier(0.55, 0.06, 0.68, 0.19)` | Descent: slow commitment, gathering fall |
| `--ease-rise` | `cubic-bezier(0.16, 1, 0.3, 1)` | Buoyancy: quick lift, long settle at the surface |
| `--ease-sway` | `cubic-bezier(0.45, 0, 0.55, 1)` | Symmetric water movement: rays, bobbing, grain |
| `--ease-draw` | `cubic-bezier(0.65, 0, 0.35, 1)` | Line work: dive line, nacre diagram, underlines |
| `--ease-pop` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | The bubble's pop only — the theme's single overshoot, rationed to §6.8 |

**One loop.** A single `requestAnimationFrame` loop with lerp factor
**0.10** for depth-bearing values (gauge, depth, ray thinning, band
parallax) and 0.14 for lights (flaw highlight position, nacre grain)
drives every scrubbed value on the page. No element runs its own
scroll handler or its own loop. The 0.10 factor is the held breath:
deliberately slower than the library's typical 0.12–0.14, so the
page always feels like it is moving through a medium denser than air.
Scroll itself is never hijacked — no smooth-scroll library, no
scroll-jacking; the *resistance* is in the lerp, not in the wheel.

**Every motion term, translated or refused:**
- *Scroll-triggered reveals* — things surface: elements rise 24px and
  fade in over 700ms `--ease-rise` as they cross 78% viewport height,
  as if floating up to meet the visitor (§6.10, §6.11).
- *Scroll-driven / scrubbed animation* — the dive itself: depth,
  gauge, rays and band parallax are pure functions of scroll
  position, fully reversible until the seabed, then mirrored on the
  ascent.
- *Parallax* — three water speeds: surface shimmer layer 1.06×,
  mid-water shapes 0.96×, seabed layer 1.00× (still — at the bottom,
  nothing drifts). Amplitudes capped at ±18px so layers never uncover
  a section edge.
- *Pinned sections* — exactly one pin: the seabed (§6.5), 120vh.
  One pin per dive; a second pin would be a second breath.
- *Smooth scrolling* — native, unmodified. The theme's smoothness is
  the lerp loop's, applied to *values*, never to the scrollbar.
- *Progress indicator* — the depth gauge (§6.3). Progress is depth;
  there is no separate progress bar anywhere on the page.
- *Staggered reveals* — surface elements stagger 90ms apart like
  things floating up (§6.2, §6.11); deep-band content never staggers
  — at the bottom, things arrive one at a time or not at all.
- *Masked reveals* — the foam-edge mask wipe of the headline
  (§6.2) and the surface break (§6.9): irregular foam borders, never
  straight clip edges.
- *Kinetic typography* — the headline's letters rising like bubbles,
  last word to first (§6.2). This is the theme's only kinetic type;
  body copy never moves letter by letter.
- *Marquee* — **refused.** Nothing on a held breath scrolls sideways
  forever. The footer's dive record is a still table (§6.14).
- *Counters* — depth counter and pearl-grade figures count once, to
  true values, when their section first surfaces (§6.12).
- *SVG line-draw* — the dive line (§6.1) and the nacre diagram
  (§6.7), drawn in the order the real things are made: rope first,
  layers in growth order.
- *Image scale-in-frame* — pearl photography scales 1.06 → 1 over
  900ms `--ease-rise` inside its frame as it surfaces; the frame
  never moves.
- *Hover / micro-interactions* — the flaw highlight (§6.6), card
  water deepening one band-step on hover (§6.11), links drawing a
  dive-line underline (§6.10).
- *Custom cursor* — **refused.** Normal system cursor everywhere;
  the theme's own standing rule and the library's.
- *Page transitions* — the line-pass (§6.15): leaving a page is
  hauling up the dive line.
- *Ambient loops* — exactly two: ray sway (§6.4) in the shallow band
  only, and nacre grain drift (§6.16). Both pause off-screen and
  under `document.hidden`. No ambient motion exists below −14 m:
  deep water is still.
- *Reduced motion* — the whole dive rests as a static depth chart:
  bands printed in order, gauge drawn at −28 m beside the seabed and
  0 m at the footer, no bobbing, rays, pins or draws (§10 gate).

**Durations ledger (the complete list — no other durations may
appear in a build).** Load ceremonies: line drop 1400ms (§6.1),
foam wipe 1200ms (§6.2), letter rise 500ms at 45ms stagger (§6.2).
Scroll-scrubbed: depth/gauge/rays/break — continuous, lerp 0.10;
grain — continuous, lerp 0.14. Pins and thresholds: seabed story
lines 600ms each at pin progress 0.15/0.32/0.49/0.66/0.83 (§6.5),
nacre sheen crossing 1600ms at 0.50. Draws: nacre layers 700ms at
220ms stagger (§6.7), drowned line 1200ms (§6.18), link underlines
300ms (§6.10). Interactions: flaw cross 600ms + 400ms exit (§6.6),
bubble rise 140px/s + pop 160ms (§6.8), card surface 700ms at
90ms stagger (§6.11), card deepen 300ms (§6.11), counters 900ms
(§6.12), form break 600ms (§6.13), pass sheets 450ms each way
(§6.15). Ambient periods: ray sway 9000ms (§6.4), skeleton wash
1800ms (§6.15). Watchdogs: 2200 / 2600 / 1000 / 4000 / 1400 /
2500 / 3000ms as declared per element. A duration found in code
that is not in this ledger is a review finding, full stop.

## 6. Signature elements

### 6.1 The dive line drop

- **What & why.** On load, an SVG line drops from beneath the hero
  headline down the gauge margin to the bottom of the hero — the
  ama's rope, thrown before the dive begins. It then stays for the
  whole page as the gauge's spine (§6.3). It belongs because the dive
  must be *prepared* in view of the visitor: the rope is how the
  diver finds her way back, and the page's progress instrument is
  meaningless until the rope exists.
- **Structure.** An inline SVG in the 72px gauge rail, one vertical
  path with a slight authored slack curve (never a ruler-straight
  line — a rope in water), plus a small weight circle at its lower
  end. `pathLength` normalised to 100; drawn via
  `stroke-dashoffset`. The SVG is decorative (`aria-hidden`); the
  depth information it carries is duplicated by the gauge's text
  readout (§6.3).
- **Motion spec.** Trigger: load, gated on `document.fonts.ready`
  raced against a 700ms timer. Draw 1400ms `--ease-draw`, top to
  bottom; the weight settles with a 120ms sway overshoot of 3px
  (`--ease-sway`, not `--ease-pop` — rope does not bounce). Runs once
  per session; a returning visitor finds the rope already down.
- **States.** Undrawn (JS-armed only, pre-load) → drawing → resting
  as the gauge spine for the remainder of the page. It never
  redraws, including on resize — a resize re-fits the path geometry
  instantly, without replaying the draw.
- **Content merge.** The line is the gauge's spine and the headline's
  anchor: its top terminates in a knot ring drawn around the
  headline's final full stop, so the title is visibly tied to the
    depth the visitor is about to descend. Remove it and §6.3 has no
  spine; it is structure, not illustration.
- **Failure fallback.** Watchdog: if the draw has not completed by
  2200ms after trigger, the line is set fully drawn instantly. No JS:
  the line ships drawn in the HTML (dashoffset 0) and JS arms the
  undrawn state only after first paint confirms the loop is alive.
- **Reduced-motion variant.** The line stands drawn from first paint;
  a caption in the rail reads "THE LINE IS DOWN." The fact is kept,
  the drop is not performed.
- **Performance budget & mobile variant.** One SVG path, one dash
  animation; <1 KB. Mobile (<768px): the rail is gone, so the line
  drops instead along the top depth bar's left edge as a 40px
  horizontal segment — the rope is shorter on a phone, and the spec
  admits it rather than squeezing the margin.
- **Choreography timeline (v2).** t=0 fonts ready (or 700ms race
  lost) → t=0–1400 line draws downward → t=1400 weight reaches hero
  bottom → t=1400–1520 weight sway settles (±3px → 0) → t=1520 line
  at rest; the headline's foam surfacing (§6.2) begins at t=900,
  overlapping the draw's second half — the title surfaces while the
  rope is still going down, as a diver's catch comes up before the
  rope is hauled.
- **State matrix (v2).** *Rest:* fully drawn, acting as gauge spine.
  *Hover:* none — not a control. *Focus:* none. *Active:* n/a.
  *Scrolled-past:* drawn; becomes the spine the gauge marker travels.
  *Disabled / no-JS:* drawn at first paint. *Touch:* identical;
  no touch behaviour of its own.
- **Breakpoints (v2).** ≥1200px: full rail drop, 72px margin.
  768–1199px: rail narrows to 48px, line drops the same path scaled,
  draw 1200ms. <768px: horizontal 40px segment in the top bar, draw
  800ms.
- **Edge cases & failure modes (v2).** *Slow fonts:* the 700ms race
  governs. *Tab hidden during draw:* rAF pauses; on return, if
  elapsed wall time > 2200ms the watchdog completes it. *Hero
  shorter than expected:* the drop length is the hero's rendered
  height, measured at trigger time, never hard-coded. *Session
  return:* `sessionStorage` marks the drop done; line paints drawn.
- **Accessibility spec (v2).** `aria-hidden="true"`; the line conveys
  no information that the gauge's text readout (§6.3) does not. It
  never receives focus. Its contrast against every band ground is
  graphical-only by design (1.9:1 against `--foam`) and it is never
  the sole carrier of meaning.
- **Tokens consumed (v2).** `--shallow`, `--pearl`, `--ease-draw`,
  `--dur-line-drop` (1400ms), `--dur-fallback-line` (2200ms),
  `--rail-w` (72px).

### 6.2 Foam surfacing — the headline

- **What & why.** The hero headline surfaces through foam: an
  irregular foam-edge mask sweeps upward across it over 1200ms while
  its letters rise one by one like bubbles — last word to first, as
  the original specifies, because a diver's catch is hauled from the
  end of the line. It belongs because the title is the first thing
  brought up from the water; the hero's entrance is a small surfacing
  that teaches the visitor the page's whole grammar in two seconds.
- **Structure.** The `<h1>` in final DOM position, fully typeset.
  Letters are wrapped in spans by JS only (the unwrapped headline is
  the no-JS state). The foam mask is an SVG turbulence-edged mask on
  a wrapper, animated via mask-position; the mask layer is
  `pointer-events: none` and sits above the text visually only during
  the wipe.
- **Motion spec.** Trigger: t=900ms of the §6.1 timeline (or
  standalone 300ms after load if §6.1 already ran this session).
  Mask wipe 1200ms `--ease-rise`. Letters: each rises 14px and fades
  in over 500ms `--ease-rise`, staggered 45ms per letter, ordered
  last word → first word, left-to-right within each word. Total
  ceremony ≈2.3s. First scroll, click or keypress completes it
  instantly.
- **States.** Submerged (JS-armed only: mask closed, letters at
  +14px / opacity 0) → surfacing → rested, fully legible. Scrolled-
  past mid-ceremony: completed instantly.
- **Content merge.** The headline is the page's real `<h1>` — the
  atelier's name and the dive's promise ("Nine metres of water,
  twenty-eight of depth" style copy per §12) — not a decorative
  title card. The foam it surfaces through is the same foam token
  family as the surface band it sits in.
- **Failure fallback.** Watchdog at 2600ms: mask removed, letters at
  rest. No JS: the headline stands printed and legible at first
  paint; the letter-wrapping never happens.
- **Reduced-motion variant.** No wipe, no letter rise. The headline
  stands printed; beneath it the apparatus line "SURFACED." is not
  printed either — reduced motion keeps the fact (the headline is
  here) without annotating the theatre that was skipped.
- **Performance budget & mobile variant.** One mask animation + up to
  40 letter spans; transform/opacity only. Mobile: letter stagger
  shortens to 30ms and the rise to 10px; headlines longer than 40
  letters wrap by word instead (whole words rise, 120ms stagger) so
  the ceremony never exceeds 2.3s on a small screen.
- **Choreography timeline (v2).** t=0 trigger → t=0–1200 foam mask
  sweeps up → letters begin at t=150, last word first, 45ms stagger
  → final (first-word) letter lands ≈ t=150 + 45×(n−1) + 500,
  capped by the word-wrap fallback → t=2300 ceremony over; §6.4 rays
  begin their sway only after t=2300, so the surface is still while
  the title comes up.
- **State matrix (v2).** *Rest:* printed headline. *Hover:* none.
  *Focus:* focus entering the hero completes the ceremony instantly
  (a keyboard visitor never waits for foam). *Active:* n/a.
  *Scrolled-past:* completed instantly. *Disabled / no-JS:* printed
  at first paint. *Touch:* first touch completes it.
- **Breakpoints (v2).** ≥1200px: 76px display, full letter ceremony.
  768–1199px: 56px, letter ceremony kept, stagger 40ms. <768px:
  42px, word-wise rise (see budget), mask wipe 1000ms.
- **Edge cases & failure modes (v2).** *Very long headline:* the
  40-letter cap switches to word mode automatically. *Font swap
  mid-ceremony:* letter spans are measured after `fonts.ready`;
  the 700ms race applies as in §6.1. *Interrupt by navigation:*
  the ceremony is session-flagged only on completion; an interrupted
  load simply replays next visit — acceptable, because the headline
  is legible in every frame of the replay.
- **Accessibility spec (v2).** The `<h1>` text is in the
  accessibility tree whole and unwrapped at all times (spans are
  `aria-hidden` duplicates are NOT used; the real letters are the
  spans, with the heading's text content intact for AT). The mask
  never removes the heading from the tree. Contrast at rest 12.2:1
  (`--ink-deep` on `--foam`); during the wipe, any partially masked
  letter is a transient state under 1200ms and the full headline is
  available to AT throughout.
- **Tokens consumed (v2).** `--foam`, `--ink-deep`, `--ease-rise`,
  `--dur-foam-wipe` (1200ms), `--dur-letter-rise` (500ms),
  `--dur-fallback-headline` (2600ms).

### 6.3 The depth gauge

- **What & why.** The page's progress instrument is a depth gauge in
  the margin rail: a fixed pearl marker sits at the rail's vertical
  centre while metre marks (0, −7, −14, −21, −28) scroll past it,
  driven by `--depth-now`, with a Karla tabular readout (`−13.5 m`)
  beneath the marker. It belongs because progress on this page is not
  "how much have I read" but "how deep am I" — the visitor's breath
  is the scroll, and the gauge is where the breath is measured.
- **Structure.** A fixed-position rail component (≥1200px) containing
  the §6.1 line as its spine, an SVG/div strip of metre ticks
  translated by the loop, the pearl marker (a 10px pearl disc with a
  hairline), and the text readout in an `<output>` element. The
  readout is the accessible source of truth; the moving strip is
  `aria-hidden`.
- **Motion spec.** Trigger: scroll, scrubbed. The tick strip's
  translation is a pure function of `--depth-now` (0 → −28 m maps to
  0 → 560px of strip travel, 20px per metre), lerped at 0.10 by the
  shared loop. The readout updates at most every 100ms and always
  lands on the true value when scroll rests. On the ascent the strip
  climbs back — the gauge is honest in both directions.
- **States.** *At surface:* readout `−0.0 m`, 0-tick at the marker.
  *Descending:* strip falling, readout deepening. *At seabed:*
  `−28.0 m` held through the pin; the marker's hairline turns
  `--pearl`-bright (the only state change — no alarm, no pulse; the
  bottom is a place, not an alert). *Ascending:* strip rising.
  *Scrolled-past / at footer:* `−0.0 m` again — the record of the
  dive moves to §6.14.
- **Content merge.** The gauge is generated from the same dive-track
  function as the section depth stamps (§6.17): the stamp printed at
  a section's head is the depth the gauge reads when that section is
  centred. They cannot disagree because they are the same number
  printed twice.
- **Failure fallback.** No JS: the gauge renders as a static depth
  chart — the full tick strip printed beside the sections it
  describes, with the seabed strip segment marked `−28 m`. Watchdog:
  if the loop stalls >1000ms, the readout snaps to the true
  positional value (the function is positional, §4, so truth is
  always recoverable instantly).
- **Reduced-motion variant.** The gauge becomes the static chart:
  ticks printed in the rail at their sections' positions, no moving
  strip, readout replaced by per-section stamps only.
- **Performance budget & mobile variant.** One transformed strip +
  one text update ≤10/s; negligible. Mobile (<768px): the rail
  collapses to a 28px top bar — a horizontal pearl marker travelling
  a 0 → −28 track with the readout at its right end; 768–1199px
  keeps a 48px rail with ticks at 0/−14/−28 only.
- **Choreography timeline (v2).** Continuous: each frame, loop
  computes target depth from scroll → lerps strip and readout toward
  it (0.10) → at rest (<0.05 m delta for 300ms) the readout snaps to
  the exact formatted value. On entering the pin (depth reaches
  −28.0): marker hairline brightens over 300ms `--ease-sway`. On
  leaving upward: dims over 300ms.
- **State matrix (v2).** *Rest (surface):* `−0.0 m`. *Hover:* the
  rail is not interactive; hovering the readout shows nothing extra.
  *Focus:* the readout is focusable (`tabindex="0"`) so AT users can
  query current depth; focus does not alter the strip. *Active:*
  n/a. *Scrolled-past:* continues to report true depth — it never
  freezes at −28 after the ascent begins. *Disabled / no-JS:*
  static chart. *Touch:* top-bar variant; no touch gestures of its
  own.
- **Breakpoints (v2).** ≥1200px: 72px rail, 5 labelled ticks,
  20px/m. 768–1199px: 48px rail, 3 labelled ticks, strip travel
  420px. <768px: top bar, horizontal travel = bar width − 64px,
  readout 12px.
- **Edge cases & failure modes (v2).** *Jump-scroll to footer:*
  depth function returns 0 at the track's end — gauge reads
  `−0.0 m` instantly; correct, because the visitor *is* at the
  surface. *Overscroll / rubber-banding:* depth clamps to
  [−28, 0]; the strip never travels past either stop. *Content
  longer than designed:* the mapping is by track proportion (§4),
  so added sections deepen their band's share, not the maximum —
  −28 m is a constant of the theme. *Resize:* strip geometry
  re-measured, position re-derived from scroll in the same frame.
- **Accessibility spec (v2).** The `<output>` readout has
  `aria-live="off"` (a live region announcing every 0.1 m would be
  unusable) but is focusable and labelled "Current depth"; AT users
  stepping through the page meet each section's stamp (§6.17) in
  reading order. Tick labels are real text in the static variant.
  Marker contrast: pearl on seabed 10.0:1, pearl on foam uses an
  `--ink-deep` hairline ring so the marker is visible in both bands.
- **Tokens consumed (v2).** `--pearl`, `--shallow`, `--ink-deep`,
  `--ink-pale`, `--ease-sway`, `--rail-w` (72px), `--gauge-px-per-m`
  (20px), `--dur-readout-snap` (100ms).

### 6.4 Thinning light rays

- **What & why.** In the shallow band, three diagonal light rays fall
  across the section background, swaying slowly like sun through
  water. As the visitor descends, the rays thin — width and alpha
  shrink scrubbed to depth — and by −14 m they are gone. They belong
  because light is the resource the dive spends: the rays make depth
  *felt* in the background of the content rather than announced by a
  widget, and their disappearance is how the visitor knows the deep
  band is near before the seabed arrives.
- **Structure.** An absolutely-positioned layer inside shallow-band
  sections: three skewed linear-gradient bars (`--ray`, alpha capped
  0.35) on a `pointer-events: none` wrapper, clipped to the section.
  Rays are background of the section they fall across — they pass
  *behind* text and cards, never over them.
- **Motion spec.** Two motions, both from the shared loop. Sway:
  rotation ±1.2° and x-drift ±8px on a 9000ms `--ease-sway` sine,
  phase-offset per ray (0 / 0.33 / 0.66). Thinning: scrubbed to
  `--depth-now` — at 0 m, full width (90px) and alpha 0.35; at
  −14 m, width 0 and alpha 0, interpolated linearly, lerped at 0.10.
  On the ascent they return by the same function — light comes back
  exactly as it left.
- **States.** *Surface/shallow:* full, swaying. *Mid band:* absent
  (width 0 — the layer is not rendered, not merely transparent).
  *Deep band:* absent. *Scrolled-past (ascent):* re-form scrubbed.
  *Hover/focus:* none — rays ignore the visitor entirely, as light
  does.
- **Content merge.** The rays belong to the sections they cross: each
  shallow section's rays are angled to fall from its own top-left
  (the surface is always up-page), and the catalogue section's rays
  fall across the water behind the pearl cards (§6.11), so the
  products are lit by the same light the visitor is descending
  through. They are the section's weather, not a page overlay.
- **Failure fallback.** No JS: rays are printed at their shallow-band
  rest state (fixed width 60px, alpha 0.25, no sway) in shallow
  sections and absent elsewhere — a still, truthful picture of where
  light reaches. If the loop stalls, rays freeze mid-sway; content
  is never behind them, so nothing is hidden.
- **Reduced-motion variant.** Rays printed static at rest state in
  shallow sections only; no sway, no scrubbed thinning (band
  membership alone decides presence).
- **Performance budget & mobile variant.** Three gradient bars,
  transform + opacity only; the layer is `content-visibility`
  managed and unrendered below −14 m. Mobile: two rays, sway drift
  ±5px, width cap 60px — shallower water on a smaller screen.
- **Choreography timeline (v2).** Continuous: sway phase advances
  with wall time while the section is in view; thinning follows the
  depth lerp each frame. On section exit upward (ascent), rays
  re-form over the same scrub range — no separate entrance
  choreography exists, deliberately: light has no entrance, only a
  depth.
- **State matrix (v2).** *Rest (in band):* swaying at authored
  width/alpha. *Hover:* none. *Focus:* none; the layer is never
  focusable. *Active:* n/a. *Scrolled-past:* per depth function —
  gone below −14 m, restored on ascent. *Disabled / no-JS:* static
  print in shallow band. *Touch:* identical; no touch response.
- **Breakpoints (v2).** ≥1200px: 3 rays, 90px cap. 768–1199px:
  3 rays, 70px cap. <768px: 2 rays, 60px cap, sway period 11000ms
  (slower on small screens reads as calmer, not laggier).
- **Edge cases & failure modes (v2).** *Section taller than
  designed:* rays are clipped to the section; a 300vh section gets
  rays only in its top 100vh (authored wrapper height) so light
  never appears to originate mid-water. *Dark mode:* ray alpha cap
  drops to 0.22 — dusk light is weaker (§2). *Low-power device:*
  sway is the first thing cut (§14); thinning (a scroll value)
  remains.
- **Accessibility spec (v2).** Purely decorative: `aria-hidden`,
  behind all content, alpha-capped so even where a ray crosses a
  card edge the underlying contrast is unchanged (rays never sit
  behind text — the wrapper's z-order is below the content layer,
  verified in §10). No information is carried by the rays that the
  gauge and stamps do not carry in text.
- **Tokens consumed (v2).** `--ray`, `--ease-sway`, `--dur-ray-sway`
  (9000ms), `--ray-alpha-max` (0.35), `--ray-vanish-depth` (−14 m).

### 6.5 The seabed pin — the featured pearl

- **What & why.** At the bottom of the dive, the featured pearl pins
  for 120vh on the dark seabed while its story surfaces beside it,
  line by line. It is the dive's purpose: everything above was
  descent toward this one object, and the pin is the held moment at
  the bottom — the diver does not rush the find. It belongs because
  a theme built on a single breath must have a single still centre,
  and the product is it.
- **Structure.** A deep-band section (`--seabed` ground) of 220vh
  total: a sticky stage (100vh) holding the pearl — a large
  photograph or rendered sphere with its dimple (§6.6) — on the
  left 5 columns, and the story column on the right 6, whose lines
  (name, harvest, measure, price, the flaw caption) are revealed in
  sequence as the pin progresses. The pearl's name is the section's
  `<h2>`.
- **Motion spec.** Trigger: scroll. Pin duration 120vh of scroll.
  The pearl itself does not move, scale or rotate during the pin —
  stillness is the spec. Story lines surface one by one: each rises
  18px and fades in over 600ms `--ease-rise` at pin progress
  thresholds 0.15 / 0.32 / 0.49 / 0.66 / 0.83 (five lines). A faint
  nacre sheen (§6.16) crosses the pearl once, at progress 0.5, over
  1600ms. Pin progress is lerped at 0.10 like all depth values.
- **States.** *Approaching:* pearl visible at the stage's top,
  story empty. *Pinned:* pearl still, lines surfacing per progress.
  *Complete:* all five lines printed; the pearl's purchase action
  (§6.13's ascent form is separate — here a single "Reserve her"
  anchor) becomes available only at progress ≥0.83, because a
  visitor may not buy the pearl before her story has surfaced.
  *Scrolled-past:* stage releases; the section scrolls away as an
  ordinary printed section with all lines visible.
- **Content merge.** The pinned object *is* the product and the
  surfacing lines are its actual commerce data — name, the dive she
  came from (date, diver, depth −28 m, read from the dive record
  data, §6.14), her measure (9.4 mm), her flaw caption, her price.
  The pin does not decorate the product page; on a single-product
  build, this section *is* the product page.
- **Failure fallback.** No JS / no sticky support: the section is a
  static deep-band spread, pearl and all five lines printed in
  order. Watchdog: if pin progress cannot be computed (loop dead),
  all lines are set visible instantly — the story may never be held
  hostage by the pin.
- **Reduced-motion variant.** No pin. A static seabed spread:
  pearl, then the five lines in reading order, then the action.
  The depth stamp still reads −28 m (§6.17) — the fact of the
  bottom is kept; the holding is not performed.
- **Performance budget & mobile variant.** Sticky positioning only;
  the pearl image is the page's LCP-class asset and is budgeted in
  §14 (≤180 KB, preloaded). Mobile (<768px): **the pin is cut** —
  pearl and story stack and scroll naturally, lines pre-printed
  after the pearl; a 120vh pin on a phone traps the thumb, and the
  theme admits the bottom is reached by swimming on mobile, not by
  being held.
- **Choreography timeline (v2).** Pin progress 0: stage sticks,
  depth locks at −28.0 m (§6.3 hairline brightens). 0.15: line 1
  (name) surfaces. 0.32: line 2 (harvest). 0.49: line 3 (measure).
  0.50: nacre sheen crosses the pearl (1600ms). 0.66: line 4 (the
  flaw caption). 0.83: line 5 (price) + reserve action enabled.
  1.00: stage releases; ascent sections begin.
- **State matrix (v2).** *Rest (before pin):* pearl printed, story
  lines armed (JS only). *Hover:* the pearl's flaw answers hover
  per §6.6; the stage itself has no hover state. *Focus:* focus
  entering the story column surfaces all lines instantly up to the
  focused one — a keyboard visitor reads the story in order without
  scrolling the pin. *Active:* n/a. *Scrolled-past:* all lines
  printed. *Disabled / no-JS:* static spread. *Touch:* pin kept on
  ≥768px touch (scroll is scroll); cut <768px per budget.
- **Breakpoints (v2).** ≥1200px: 120vh pin, pearl left / story
  right, measure 48–54ch. 768–1199px: pin shortened to 90vh, pearl
  above story in the sticky stage, thresholds compressed to
  0.12/0.30/0.48/0.66/0.84. <768px: no pin (see budget).
- **Edge cases & failure modes (v2).** *Story longer than five
  lines:* the spec caps the story at five lines; a sixth line joins
  line 5's threshold group rather than extending the pin. *Pearl
  image fails to load:* the stage shows the pearl's nacre-gradient
  placeholder (§6.16 stops) with her name and measure — the story
  still surfaces on schedule; a broken-image icon at the bottom of
  the sea is a gate failure (§9). *Visitor scrolls up mid-pin:*
  progress reverses; lines that surfaced stay surfaced (a thing
  brought up is not thrown back) — only the sheen may re-run.
  *Browser without `position: sticky`:* fallback spread, detected
  by feature test at build, not at runtime.
- **Accessibility spec (v2).** The story lines are in the DOM in
  reading order at all times; surfacing is visual only (opacity /
  transform on already-present text). The reserve action's
  availability at 0.83 is visual emphasis only — the link is
  focusable and activatable from page load, so AT users are never
  gated by pin progress. Pearl image alt text names her and her
  flaw: "The Dimpled One, baroque pearl, 9.4 millimetres, a small
  dimple on her left shoulder." Contrast: `--ink-pale` on
  `--seabed` 10.0:1 at every line.
- **Tokens consumed (v2).** `--seabed`, `--ink-pale`, `--pearl`,
  `--ease-rise`, `--dur-line-surface` (600ms), `--pin-seabed`
  (120vh), `--nacre-1/2/3`.

### 6.6 The flaw highlight

- **What & why.** The hero pearl — and the featured pearl (§6.5) —
  carries one visible flaw: a small dimple, described proudly in her
  caption ("imperfect, therefore real"). Hovering the pearl makes
  the dimple catch light: a highlight travels across the dimple over
  600ms. It belongs because the theme's anti-slop law (§9) says the
  imperfection is the proof of reality, and attention is what makes
  it shine — the interaction teaches the visitor to look *at* the
  flaw, not past it.
- **Structure.** The pearl image with an SVG overlay aligned to the
  dimple's authored position (per-pearl `data-dimple="x%,y%,r%"`).
  The highlight is a radial gradient disc clipped to the dimple's
  circle, translated across it. Overlay is `pointer-events: none`;
  hover is detected on the pearl figure itself.
- **Motion spec.** Trigger: hover (pointer-fine) or focus-within.
  Highlight enters from the dimple's upper-left, crosses to
  lower-right over 600ms `--ease-sway`, holds 200ms, exits over
  400ms. It may run once per hover entry; re-entry replays it.
  Driven by the shared loop's light channel (lerp 0.14).
- **States.** *Rest:* dimple visible, unlit — a matte crescent in
  the pearl image itself. *Hover/focus:* highlight travels (above).
  *Active (press):* highlight snaps to the dimple's centre and
  holds while pressed — the visitor is holding the pearl to the
  light. *Scrolled-past:* no behaviour. *Disabled:* if the overlay
  fails, the dimple in the base image remains — the flaw never
  depends on its highlight.
- **Content merge.** The dimple is on the product photograph, at the
  position the caption describes ("a small dimple on her left
  shoulder"), and the same `data-dimple` coordinates drive §6.5's
  sheen stop point. The caption, the image and the interaction are
  three printings of one fact about one pearl.
- **Failure fallback.** No JS: the dimple is simply visible in the
  image; the caption carries the meaning alone, as it does in print.
  Overlay misalignment (image swapped without updating
  `data-dimple`) is a build error caught by §10's flaw audit, not a
  runtime state.
- **Reduced-motion variant.** No travelling highlight. On hover, the
  dimple's circle outline fades in statically (opacity 200ms) — the
  flaw is indicated, not performed.
- **Performance budget & mobile variant.** One gradient disc,
  transform-only. Mobile / touch: no hover exists, so the highlight
  runs once automatically when the pearl first reaches 60% viewport
  height — the flaw introduces itself, once, and never repeats on
  scroll-back.
- **Choreography timeline (v2).** Hover in → t=0–600 highlight
  crosses → t=600–800 hold → t=800–1200 exit fade. Press during
  hold: exit is cancelled, highlight centres (150ms) and holds
  until release, then exits over 400ms. Touch auto-run: same
  timeline, triggered by the 60% viewport crossing, once per page
  load.
- **State matrix (v2).** *Rest:* unlit dimple. *Hover:* travel +
  hold + exit. *Focus:* identical to hover (keyboard parity).
  *Active:* centred hold. *Scrolled-past:* none. *Disabled /
  no-JS:* dimple in image only. *Touch:* one auto-run at 60%
  visibility; taps belong to §6.8, not to the flaw.
- **Breakpoints (v2).** ≥1200px and 768–1199px: identical behaviour;
  dimple coordinates are percentage-based so they scale with the
  image. <768px: touch auto-run variant (above); pointer-fine
  tablets keep hover.
- **Edge cases & failure modes (v2).** *Pearl without a flaw:* not
  permitted — §9 requires exactly one flawed pearl in the hero and
  the featured pearl is the same individual; a flawless build fails
  the gate. *Two pearls with dimples on one page:* forbidden by the
  ration — the highlight exists once per page (hero and seabed are
  the same pearl at two depths). *Image zoom / responsive crops:*
  `data-dimple` is relative to the image's intrinsic frame and the
  overlay is inside the same `object-fit` box, so crops move both
  together.
- **Accessibility spec (v2).** The interaction is decorative
  emphasis: the flaw's existence and position are fully conveyed by
  the caption text and the image's alt (§6.5). The overlay is
  `aria-hidden`. Focus parity is required (above) so keyboard
  visitors get the same indication. No contrast state depends on
  the highlight.
- **Tokens consumed (v2).** `--pearl`, `--nacre-1`, `--ease-sway`,
  `--dur-flaw-cross` (600ms), `--dur-flaw-exit` (400ms).

### 6.7 The nacre diagram draw

- **What & why.** In the craft section (mid band), a cross-section
  diagram of a pearl — concentric nacre layers around the nucleus —
  draws itself layer by layer as the visitor reads. It belongs
  because it is the theme's one piece of teaching, and it is built
  the way the pearl was: in layers, in growth order, under the
  reader's eye. A diagram that fades in whole would contradict the
  craft it explains.
- **Structure.** Inline SVG: 6 concentric layer paths (nucleus +
  5 nacre layers), each a closed path drawn via `stroke-dashoffset`,
  with a thin fill that fades in only after its stroke completes.
  Layer labels sit in the margin beside leader lines (real HTML
  text, not SVG text, so they are selectable and translatable):
  "nucleus — a grain of sand", "first nacre — one winter", and so
  on, each label naming a true layer fact from the section's copy.
- **Motion spec.** Trigger: scroll — the diagram's section crossing
  65% viewport height starts the draw; layers draw inside-out
  (growth order), each stroke 700ms `--ease-draw`, staggered 220ms,
  fill fade 300ms after each stroke. Total ≈2.6s. Scrolling away
  and back does not redraw; the finished diagram is the resting
  state (a pearl does not un-grow).
- **States.** *Undrawn* (JS-armed only) → *drawing* (layers in
  sequence) → *drawn* (rest). *Scrolled-past quickly:* if the
  section is flung past in under 600ms, the diagram completes
  instantly rather than drawing to an empty viewport. *Hover:* a
  layer under the pointer brightens its fill by one nacre step and
  its label bolds — the diagram answers questions.
- **Content merge.** The labels are the section's actual teaching
  copy, and the layer count (6) is the count the copy states ("six
  winters of nacre"). The diagram is the craft section's body, not
  an illustration beside it: on narrow screens the text wraps
  *around* the drawing's sequence, paragraph per layer.
- **Failure fallback.** No JS: diagram ships fully drawn with fills
  at rest. Watchdog: 4000ms after trigger, any undrawn layer is set
  drawn instantly.
- **Reduced-motion variant.** Diagram printed drawn; labels listed
  in order. Hover brightening remains (it is a state, not a motion).
- **Performance budget & mobile variant.** One SVG, 6 paths; trivial.
  Mobile: diagram scales to full column width; labels stack beneath
  in growth order with numbered markers matching the layers; draw
  stagger shortens to 150ms (total ≈2.1s) — a smaller pearl, grown
  slightly faster, admitted in the spec.
- **Choreography timeline (v2).** Trigger (65% crossing) → t=0
  nucleus stroke (700ms) → t=220 layer 2 → t=440 layer 3 → t=660
  layer 4 → t=880 layer 5 → t=1100 layer 6 → fills trail each stroke
  by +300ms → t≈2400 all fills settled → t=2600 diagram at rest;
  labels fade in with their layer's fill, never before it.
- **State matrix (v2).** *Rest:* drawn, fills at authored opacity.
  *Hover:* per-layer brighten + label bold (pointer-fine).
  *Focus:* each layer group is focusable in growth order
  (`tabindex="0"`, role `img` with per-layer label) and focus
  brightens exactly as hover does. *Active:* n/a. *Scrolled-past:*
  drawn. *Disabled / no-JS:* drawn at first paint. *Touch:* tap on
  a layer brightens it and shows its label first (labels are
  visible by default on touch layouts, so tap is emphasis only).
- **Breakpoints (v2).** ≥1200px: diagram 420px, labels in margin.
  768–1199px: 340px, labels right of diagram. <768px: full-width,
  labels stacked beneath, numbered.
- **Edge cases & failure modes (v2).** *Copy changes layer count:*
  the SVG is generated from the same data list as the labels, so a
  seventh winter adds a seventh path and label together — they
  cannot drift apart. *Long labels:* margin labels wrap to two
  lines max; leader lines are drawn to the wrapped block, not to a
  fixed point. *Print:* drawn state is the print state.
- **Accessibility spec (v2).** The SVG carries `role="img"` and an
  `aria-label` summarising the whole ("Cross-section of a pearl:
  a sand-grain nucleus wrapped in five layers of nacre"); per-layer
  focus stops expose the same facts as the visible labels. Label
  text contrast: `--foam` on `--mid` 5.2:1. The draw animation is
  never the only way the information arrives — labels are in the
  DOM from first paint.
- **Tokens consumed (v2).** `--mid`, `--foam`, `--nacre-1/2/3`,
  `--pearl`, `--ease-draw`, `--dur-layer-draw` (700ms),
  `--dur-layer-stagger` (220ms), `--dur-fallback-diagram` (4000ms).

### 6.8 Bubble release click

- **What & why.** Clicking a pearl card (§6.11) releases one bubble
  from the click point: it rises inside the card, wobbling slightly,
  and pops at the card's top edge. It belongs because feedback on
  this page is air — the visitor's touch exhales into the water the
  card sits in. It is also the theme's only overshoot (`--ease-pop`
  at the pop) and its only playful element, rationed to one bubble
  per click so the water stays quiet.
- **Structure.** A bubble element (24px circle, pearl-gradient
  border, transparent centre) spawned inside the card's
  `overflow: hidden` layer at the click coordinates, animated by the
  shared loop's light channel. The card's content layer is a sibling
  above it; the bubble never covers text (it rises in the card's
  water margin and image area, and its path is clipped to the card).
- **Motion spec.** Trigger: click / tap / Enter-Space activation on
  the card. Rise: from click point to the card's top edge at
  140px/s, wobble ±3px on a 700ms `--ease-sway` sine, growing 24px →
  30px as it rises (pressure drops, bubble expands — the physics is
  the spec). Pop: at the top edge, scale 1 → 1.35 with opacity
  1 → 0 over 160ms `--ease-pop`, plus a 6px ripple ring fading over
  300ms. One bubble per click; a second click while one rises spawns
  a second only if the first is above the card's midline (max 2
  concurrent per card).
- **States.** *Rest:* no bubble. *Rising:* per above. *Popping:*
  160ms + ripple. *Card pressed state:* the card itself answers the
  click per §11 (water deepens one step for 200ms) — the bubble is
  *additional*, never the only feedback. *Disabled card:* no bubble;
  a disabled card is out of the water.
- **Content merge.** The bubble is released from the card the
  visitor touched, rises through that card's own water (its band
  colour), and pops at its edge — it is the card's response, not a
  page-level confetti. Cards in the deep band do not bubble (§6.5's
  pearl is not a card); bubbles belong to the catalogue's shallows,
  where air still exists.
- **Failure fallback.** If the loop is dead, clicks still register
  the card's pressed state and navigation; the bubble is an
  enhancement layered on a working control. No JS: cards are plain
  links; no bubble layer exists.
- **Reduced-motion variant.** No bubble. The card's pressed state
  (deepen 200ms) is the whole feedback.
- **Performance budget & mobile variant.** ≤2 bubble nodes per card,
  transform/opacity only, nodes removed on pop. Mobile: identical —
  the tap *is* the click point; bubble size starts 28px (a thumb's
  bubble is bigger, admitted).
- **Choreography timeline (v2).** t=0 click → bubble spawns at
  point, card deepens → rise at 140px/s (a 220px card ≈ 1.6s) with
  wobble and growth → top edge: pop 160ms → ripple to t≈+460ms
  after arrival → node removed. Keyboard activation: bubble spawns
  from the card's centre-bottom (the focus point is the card, not a
  coordinate).
- **State matrix (v2).** *Rest:* none. *Hover:* no bubble (hover is
  §6.6 / §6.11's domain). *Focus:* no bubble until activation.
  *Active:* bubble on activation (above). *Scrolled-past:* bubbles
  in flight complete even if the card leaves the viewport — air
  does not freeze because the visitor looked away; nodes are
  cleaned on completion regardless. *Disabled:* none. *Touch:*
  tap = click, coordinates from the tap.
- **Breakpoints (v2).** Identical at all breakpoints; rise speed is
  constant, so taller desktop cards simply bubble longer — the
  variance is the physics, not a bug.
- **Edge cases & failure modes (v2).** *Click near the top edge:*
  minimum rise distance 40px enforced by spawning the bubble 40px
  below the click if needed — a pop with no rise reads as a glitch.
  *Rapid clicking:* the 2-concurrent cap; further clicks still
  register their card action. *Card navigates on click:* the bubble
  is skipped if the click triggers immediate navigation (the
  line-pass transition, §6.15, owns the departure) — bubbles are
  for cards that stay on the page (quick-view / select patterns).
- **Accessibility spec (v2).** Purely decorative: `aria-hidden`,
  spawned in a presentational layer. The card's action and state
  are conveyed by the card itself (§6.11). Keyboard activation
  produces the bubble for sighted keyboard users at parity with
  pointer users. Nothing is communicated by the bubble alone.
- **Tokens consumed (v2).** `--pearl`, `--nacre-3`, `--ease-sway`,
  `--ease-pop`, `--dur-bubble-pop` (160ms), `--bubble-rise-rate`
  (140px/s).

### 6.9 The surface break

- **What & why.** The ascent's final section brightens into a
  foam-white transition: a foam edge sweeps up across the last
  mid-band section, light floods back over 900ms, and the visitor
  arrives in the foam-white footer (§6.14). It belongs because
  finishing the page is surfacing, and surfacing must be *felt* —
  the moment the head breaks water is the dive's second-most
  important beat, after the find.
- **Structure.** The final ascent section carries a foam-edge layer
  (SVG turbulence edge, same family as §6.2's mask) over its top
  boundary, and its background is a declared gradient from the last
  mid-band ground to `--foam`, scrubbed to the ascent's final 15%.
  The footer itself is plain `--foam` — by the time the visitor
  arrives, the water is entirely behind them.
- **Motion spec.** Trigger: scroll, scrubbed. Across the section's
  entry (its top crossing 100% → 40% viewport), the foam edge sweeps
  upward 900ms-equivalent of scroll (scrubbed, lerped 0.10, not
  timed — the visitor controls the surfacing speed with their
  scroll, as a diver does), background brightening in step. Light
  rays (§6.4) re-form in this section at full shallow strength by
  its end — the only place rays appear outside the descent's shallow
  band, because this *is* shallow water again.
- **States.** *Before:* section at mid-band ground, foam edge
  parked below its top. *Breaking:* scrubbed sweep + brighten.
  *Surfaced:* section fully foam, rays swaying, footer continuous
  with it — no visible seam between section and footer ground.
  *Scrolled back down:* the break reverses scrubbed — the visitor
  may duck back under, and the page lets them.
- **Content merge.** The section the break happens across is the
  ascent's real closing content — typically the atelier's invitation
  ("Come up and see her in the light") and the path to §6.13's form.
  The brightening is that content's own water clearing, not a
  transition overlay between pages.
- **Failure fallback.** No JS: the section prints at a fixed
  mid-to-foam split (top third mid ground, lower two-thirds foam)
  with the foam edge drawn statically — a still picture of a
  surface, truthful about where the water ends. Loop stall: the
  scrub freezes; all text sits on whichever ground its band
  declares, contrast intact (§2 law — brightening never carries
  text contrast; band text colours switch at the section's declared
  midpoint, not with the gradient).
- **Reduced-motion variant.** Static split as in the no-JS state;
  rays printed still. The footer is reached by ordinary scrolling.
- **Performance budget & mobile variant.** One scrubbed gradient +
  one mask layer; negligible. Mobile: the sweep distance shortens
  (section is shorter); rays are the 2-ray mobile variant (§6.4).
- **Choreography timeline (v2).** Section top at viewport bottom →
  foam edge begins → across 60vh of scroll: edge sweeps, ground
  brightens in 3 declared steps (mid → shallow-tint → foam; steps,
  not a continuous blend, so text contrast is always at a tested
  value) → rays re-form at the second step → section top passes
  40% viewport: fully surfaced; footer seam invisible.
- **State matrix (v2).** *Rest (below the section):* mid ground.
  *Hover:* none. *Focus:* focus entering the section does not force
  the break; the content is legible at every step (see fallback).
  *Active:* n/a. *Scrolled-past:* surfaced state. *Disabled /
  no-JS:* static split. *Touch:* identical scrub.
- **Breakpoints (v2).** ≥1200px: sweep across 60vh of scroll.
  768–1199px: 50vh. <768px: 40vh, 2 steps instead of 3 (mid → foam)
  — a phone's surfacing is quicker, admitted.
- **Edge cases & failure modes (v2).** *Visitor jumps straight to
  the footer (End key):* the section renders surfaced — positional
  function, no catch-up animation. *Section content taller than
  designed:* the break is tied to the section's first 60vh only;
  extra content sits on foam, already surfaced. *Dark mode:* the
  break lands on the dark-mode surface ground (`--mid`, §2) — the
  visitor surfaces at dusk; the steps are re-declared for that
  scheme, not improvised.
- **Accessibility spec (v2).** The foam layer is `aria-hidden` and
  behind content. Text colour steps are declared per step with
  measured pairs (foam text on mid 5.2:1; ink-deep on foam 12.2:1;
  the intermediate step uses ink-deep on the shallow-tint at
  7.6:1). No text changes colour continuously — only at steps,
  so no frame of the scrub puts text at an untested contrast.
- **Tokens consumed (v2).** `--mid`, `--foam`, `--shallow`,
  `--ink-deep`, `--ease-sway`, `--dur-surface-break` (900ms
  scrub-equivalent), `--ray`.

### Page-family elements

### 6.10 Buoy navigation (page family: navigation)

- **What & why.** The site's navigation floats at the surface: a
  foam-white bar pinned to the top of the viewport, carrying the
  atelier name and section links named as dive stages ("The
  Surface", "The Descent", "The Bottom", "Coming Up"). It belongs
  because a buoy is what a diver navigates by — it stays at the
  surface while she is below, and this bar does the same: it never
  descends, never darkens, at any depth.
- **Structure.** A `<header>` fixed at top, `--foam` ground at 92%
  opacity with a 12px backdrop blur, one row: wordmark (Cormorant),
  nav links (Karla), and the current-stage label at the right,
  which is the section name — not the depth (depth is §6.3's job;
  the buoy names *where*, the gauge measures *how deep*).
- **Motion spec.** Stage label crossfades 250ms `--ease-sway` when
  the centred section changes. Links underline with a dive-line
  draw (a 2px `--mid` rule growing left→right, 300ms
  `--ease-draw`) on hover/focus. The bar itself never moves, hides
  or shrinks — a buoy that ducks is a failed buoy; hide-on-scroll
  patterns are explicitly refused.
- **States.** *Rest:* full bar. *Hover (link):* underline draws.
  *Focus:* underline drawn + 2px `--mid-deep` outline offset 2px.
  *Active/current:* the current stage's link carries a permanent
  pearl dot beneath it (6px, `--pearl` with `--ink-deep` ring).
  *Scrolled-past:* the bar is depth-invariant — identical at −28 m
  and at the surface. *Disabled:* n/a.
- **Content merge.** The stage names are the page's real section
  names, taken from the sections' headings — renaming a section
  renames its link. The bar's right-hand stage label and §6.17's
  stamps agree by construction (same section registry).
- **Failure fallback.** No JS: the bar is a static header (not
  fixed) with all links; the stage label shows the first stage.
  Backdrop blur unsupported: opacity rises to 100% — declared in
  CSS via `@supports`, not detected in JS.
- **Reduced-motion variant.** Stage label swaps instantly; link
  underlines appear instantly. The bar's stillness is unchanged.
- **Performance budget & mobile variant.** One fixed bar; blur is
  the only cost and is cut on low-power devices (§14). Mobile:
  the nav collapses to wordmark + stage label + a "Stages" button
  opening a full-foam sheet listing the four stages as large
  links (44px targets); the bar stays fixed and shallow (52px).
- **Choreography timeline (v2).** Section change (centred section
  crosses) → t=0–250 label crossfade; pearl dot slides to the new
  link over 300ms `--ease-draw`. Nothing else in the bar ever
  animates.
- **State matrix (v2).** *Rest:* as above. *Hover:* underline draw
  (pointer-fine). *Focus:* underline + outline. *Active:* pearl
  dot on current stage. *Scrolled-past:* invariant. *Disabled /
  no-JS:* static header. *Touch:* no hover; taps navigate; the
  Stages sheet opens with a 250ms foam fade (§6.15 grammar).
- **Breakpoints (v2).** ≥1200px: full row, 64px tall. 768–1199px:
  links shrink to the four stages only (secondary links move to
  the footer). <768px: 52px, Stages sheet pattern.
- **Edge cases & failure modes (v2).** *Long stage names /
  translations:* links may wrap to a second row ≥768px rather than
  truncating a stage name — a truncated stage is a wrong direction.
  *Anchor jump to the seabed:* the stage label lands on "The
  Bottom" instantly (positional, no crossfade queue).
- **Accessibility spec (v2).** Landmark `header` + `nav` with
  `aria-label="Dive stages"`; current link carries
  `aria-current="true"` (the pearl dot is its visual twin).
  Contrast: `--ink-deep` on `--foam` 12.2:1 in every state; the
  92% opacity is over page grounds that are themselves light at
  the top — where the bar overlays the deep band during scroll,
  the blur + a declared 0.9 `--foam` backing keeps text at ≥7:1,
  audited in §10. Focus order: wordmark, stages, label is not
  focusable.
- **Tokens consumed (v2).** `--foam`, `--ink-deep`, `--mid`,
  `--mid-deep`, `--pearl`, `--ease-draw`, `--ease-sway`,
  `--dur-stage-fade` (250ms).

### 6.11 Pearl cards (page family: cards / listing)

- **What & why.** The catalogue lives in the shallow and mid bands:
  cards for the season's other pearls, each card a small volume of
  water holding one pearl's photograph, name, measure and price.
  They belong because the theme still has to sell the catch that is
  not the featured pearl — and it sells them *in* the water they
  came from, at the depth their section declares, not on a white
  e-commerce grid lowered into the sea.
- **Structure.** A `<ul>` of cards; each card is one link wrapping a
  figure (photograph in a nacre-edged frame), name (Cormorant
  24px), measure + grade line (Karla tabular), price. Card ground
  is its band's water: `--foam-dim` in the shallow band, `--mid` at
  12% over `--foam` in the mid band — cards never carry their own
  white background.
- **Motion spec.** Surfacing: cards rise 24px + fade over 700ms
  `--ease-rise`, staggered 90ms per card in reading order, when the
  grid crosses 78% viewport. Hover (pointer-fine): the card's water
  deepens one declared step (`--foam-dim` → `--shallow` at 35%)
  over 300ms `--ease-sway` and the photograph scales 1 → 1.03
  inside its frame over 600ms; no lift, no shadow — things under
  water do not cast drop shadows, and the theme forbids the
  catalogue-card levitation reflex. Click: §6.8's bubble.
- **States.** *Rest:* printed card. *Hover:* deepen + image scale
  (above). *Focus:* deepen + 2px outline `--mid-deep` — focus gets
  the hover's water plus a visible ring. *Active:* deepen holds
  200ms deeper (one more step) while pressed. *Scrolled-past:*
  printed; surfacing never replays on scroll-back. *Disabled
  (sold pearl):* the card remains, its water stills (no hover
  deepen), a "TAKEN UP" stamp line replaces the price — a sold
  pearl is surfaced permanently and says so.
- **Content merge.** Each card's band is the depth that pearl was
  actually gathered at, and the card prints it ("from −19 m,
  Tuesday's dive") from the same harvest data as §6.14's record.
  The grid is ordered by depth, shallowest first — the catalogue's
  sort order *is* the dive.
- **Failure fallback.** No JS: cards printed in order, fully linked.
  Images missing: the nacre-gradient placeholder with the pearl's
  name and measure (§6.5's rule, repeated deliberately).
- **Reduced-motion variant.** No surfacing rise; cards printed.
  Hover deepen becomes instant. Bubble off (§6.8).
- **Performance budget & mobile variant.** Images ≤60 KB each,
  `loading="lazy"` below the first row; transforms on the figure
  only. Mobile: single column, stagger cut (cards print in pairs),
  hover states absent, tap = §6.8 bubble + navigation per card
  pattern.
- **Choreography timeline (v2).** Grid crosses 78% → cards surface
  at 90ms stagger, 700ms each → rest. Hover in: deepen 300ms,
  image scale 600ms (they deliberately finish at different times —
  water first, then the pearl settles). Hover out: reverse at
  250ms / 400ms.
- **State matrix (v2).** *Rest:* printed. *Hover:* deepen + scale.
  *Focus:* deepen + outline. *Active:* deeper hold + §6.8 bubble
  where the card pattern stays on-page. *Scrolled-past:* printed.
  *Disabled (sold):* stilled water, stamp line, link removed
  (`aria-disabled`, not a dead link). *Touch:* no hover; first tap
  on a staying card bubbles; navigation cards navigate.
- **Breakpoints (v2).** ≥1200px: 3 columns, measure narrows per §4.
  768–1199px: 2 columns. <768px: 1 column, cards full-measure,
  stagger 0ms (pairs print together).
- **Edge cases & failure modes (v2).** *Odd pearl counts:* the grid
  never balances itself with filler cards; an empty final cell
  shows the water and one line — "The rest of Tuesday's catch is
  still being graded." — an honest empty state in the theme's
  voice (§12). *Very long names:* Cormorant clamps at 2 lines with
  the full name in the link's accessible name. *Price changes:*
  price is data, printed from the same source as §6.13's form
  options; a mismatch is a §10 failure.
- **Accessibility spec (v2).** One link per card with a composed
  accessible name ("The Pale Sister, 8.1 millimetres, from
  nineteen metres, £420"). Sold cards are not links. Image alt:
  the pearl's name + measure. Text contrast per band (§2 pairs);
  the hover deepen never reduces text contrast below the rest
  state's pair.
- **Tokens consumed (v2).** `--foam-dim`, `--shallow`, `--mid`,
  `--mid-deep`, `--ink-deep`, `--ease-rise`, `--ease-sway`,
  `--dur-card-surface` (700ms), `--dur-card-deepen` (300ms).

### 6.12 Pearl-grade figures (page family: data / counters)

- **What & why.** The figures a visitor should remember — the dive's
  depth (−28 m), the featured pearl's measure (9.4 mm), the season's
  dives (61), the oysters opened (214) — count up once, to their
  true values, when their section surfaces. They belong because a
  dive is measured, and the counting is the sound of the gauge
  settling; but the theme's law binds them hardest: every figure
  here is read from the same data object as the copy that surrounds
  it, so a counter can never arrive at a number the text contradicts.
- **Structure.** A figures row per relevant section: value (Karla
  700, tabular, 40px) + label (13px stamp style). The depth figure
  in the hero is *live* — it is §6.3's readout restated large — while
  harvest figures are counted-once statistics. Both kinds are
  rendered by one formatter (§3 law 2).
- **Motion spec.** Counted figures: animate from 62% of value to
  value over 900ms `--ease-rise` when the row crosses 70% viewport,
  once per page load, landing exactly (no overshoot, no decimals
  beyond the value's own precision — 9.4 counts in tenths, 214 in
  ones). The live depth figure updates with §6.3's 100ms cadence.
  Counting is a visual treatment of a value already in the DOM.
- **States.** *Pre-count* (JS-armed only): value shown at 62%.
  *Counting:* 900ms. *Rest:* true value. *Scrolled-past:* true
  value; never recounts. *Disabled / no-JS:* true value printed.
- **Content merge.** Each figure sits inside the sentence it proves:
  the depth figure inside the hero's promise (§3 law 4), 214 inside
  the harvest paragraph, 61 beside the divers' names. A figures
  *dashboard* — numbers without sentences — is refused (§9).
- **Failure fallback.** Watchdog 1400ms after trigger: value snaps
  to true. No JS: true values in HTML. The DOM ships with true
  values; JS arms the 62% start only after first paint.
- **Reduced-motion variant.** True values, no counting. The live
  depth figure still updates (it is information, not decoration)
  but at 250ms cadence.
- **Performance budget & mobile variant.** Text updates only;
  trivial. Mobile: figures stack 2×2, size 32px; counting kept
  (it is cheap) but shortened to 700ms.
- **Choreography timeline (v2).** Row crosses 70% → t=0 values at
  62% → t=0–900 count with `--ease-rise` → t=900 exact landing,
  formatter-verified string → rest. Multiple figures in a row
  count simultaneously (they are one fact set, not a sequence).
- **State matrix (v2).** *Rest:* true value. *Hover:* none.
  *Focus:* none — figures are not controls; the live depth figure
  is duplicated in focusable form by §6.3's readout. *Active:* n/a.
  *Scrolled-past:* true value. *Disabled / no-JS:* true value.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: 40px values, row of up to 4.
  768–1199px: 34px, row of 3 + wrap. <768px: 32px, 2×2 grid.
- **Edge cases & failure modes (v2).** *Value is zero or one:* a
  count from 62% of 1 is theatre; values < 4 print statically
  (declared rule). *Locale:* the formatter localises separators
  but never the minus sign or unit position of depth strings (§3
  law 2 is format-fixed across locales — the gauge must read the
  same everywhere). *Data updates between builds:* figures are
  generated from the harvest data object at build time; a
  hand-edited figure in HTML is a §10 audit failure.
- **Accessibility spec (v2).** Values are plain text in reading
  order; counting never uses `aria-live`. Screen readers receive
  the true value from first paint (the 62% start is a visual
  transform of the rendered glyphs' *displayed* string only for
  counted figures — to keep this honest, counted figures render
  their true value in a visually-hidden span and the animated
  number is `aria-hidden`; AT never hears a wrong number).
- **Tokens consumed (v2).** `--ink-deep`, `--ink-pale`, `--pearl`,
  `--ease-rise`, `--dur-count` (900ms), `--dur-fallback-count`
  (1400ms).

### 6.13 The reserve form — coming up to buy (page family: forms / conversion)

- **What & why.** The conversion section sits on the ascent, in
  brightening water: a short form to reserve the featured pearl or
  book a viewing at the atelier. Its placement is the spec — nobody
  is asked for anything at the bottom of the sea; the ask happens
  while coming up, in returning light, after the story has surfaced.
  It belongs because the theme's commercial grammar is the dive's
  grammar: descend, find, *then* surface and speak.
- **Structure.** A `<form>` on a `--foam` panel in the first ascent
  section: pearl selector (the featured pearl preselected; other
  options are §6.11's available cards, generated from the same
  data), name, email, one-line message ("Tell her diver anything"),
  submit "Reserve her". Success replaces the form with a surfaced
  confirmation: the pearl's name, the reservation reference
  (generated server-side; the client never invents one), and the
  line "She will be kept above water until Friday."
- **Motion spec.** Fields: focus draws a dive-line underline (300ms
  `--ease-draw`, §6.10's grammar) and the field's water deepens one
  step. Submit: the button's label sinks (translateY 2px, 150ms)
  then the whole panel performs a small surface break — a foam edge
  sweeps the panel's top over 600ms `--ease-rise` — as the
  confirmation replaces the form (crossfade 300ms). Errors: the
  field's margin note (§12 voice) fades in 200ms; no shaking —
  water does not shake.
- **States.** *Rest:* printed form. *Focus:* underline + deepen.
  *Invalid:* margin note in `--mid-deep`, field outline 2px; the
  entered text is kept, always (form-keeping is rehearsed in §10).
  *Submitting:* button disabled, label "Holding…" — the one place
  the theme's breath metaphor names a wait. *Success:* confirmation
  state (above). *Disabled (pearl sold):* the selector removes her
  and the form's head line says who took her up, in §12's voice.
- **Content merge.** The form sells the exact pearls the page dived
  for: options, prices and availability are generated from the
  catalogue data (§6.11), and reserving the featured pearl is only
  offered after her section — the form does not exist in the DOM
  before the ascent on single-product builds; it is the dive's
  final act, not a sidebar.
- **Failure fallback.** The form is a real form: no JS, it submits
  natively and the server returns a confirmation page in the
  theme's static dress. JS enhancement failure leaves a working
  form, never a dead panel.
- **Reduced-motion variant.** No foam sweep; confirmation replaces
  the form with an instant swap + focus move to its heading.
  Underlines appear instantly on focus.
- **Performance budget & mobile variant.** No libraries; the form
  is ~2 KB of HTML. Mobile: single column, 48px field height,
  the foam sweep cut (confirmation swap only) — surfacing on a
  phone is a tap, not a ceremony.
- **Choreography timeline (v2).** Submit → t=0 button sinks,
  label "Holding…" → server response → t=0–600 foam edge sweeps
  panel top → t=300–600 confirmation crossfades in → focus moves
  to confirmation heading at t=600 → the pearl's card (§6.11), if
  on the page, stamps itself TAKEN UP in the same beat.
- **State matrix (v2).** *Rest:* as above. *Hover (button):*
  water deepens one step (300ms). *Focus:* underline + outline
  (fields), outline (button). *Active:* sink 150ms. *Scrolled-
  past:* n/a — the form is a destination, not a reveal.
  *Disabled:* sold-pearl state (above); submit disabled only
  during submission. *Touch:* 48px targets, no hover states,
  focus grammar identical.
- **Breakpoints (v2).** ≥1200px: panel 7 columns, two fields per
  row where paired (name/email). 768–1199px: 8 columns, stacked.
  <768px: full measure, stacked, 48px fields.
- **Edge cases & failure modes (v2).** *Double submit:* disabled
  at first activation; the reference is requested once.
  *Validation failure after submit:* focus moves to the first
  error's field, note announced (`role="alert"` on the note),
  all entries preserved. *Pearl sold while the form is open:*
  on submit the server declines and the form re-renders in its
  disabled state with the reason — never a silent success.
  *Long names / addresses:* fields are single-line with no
  truncation of stored values; display may scroll, data may not
  be cut.
- **Accessibility spec (v2).** Every field has a visible `<label>`
  (no placeholder-only fields); errors are text, linked via
  `aria-describedby`, in `--mid-deep` on `--foam` at 7.4:1.
  Required fields are marked in text ("needed"), not by colour
  alone. The confirmation heading receives focus on success
  (`tabindex="-1"`). Touch targets ≥44px (48px mobile).
- **Tokens consumed (v2).** `--foam`, `--foam-dim`, `--mid`,
  `--mid-deep`, `--ink-deep`, `--pearl`, `--ease-draw`,
  `--ease-rise`, `--dur-field-line` (300ms), `--dur-form-break`
  (600ms).

### 6.14 Foam footer & the dive record (page family: footer)

- **What & why.** The footer is above water: flat `--foam`, bright,
  ordinary — and it carries the dive record, a small still table of
  the dive the page just made: deepest point −28 m, the featured
  pearl's name and measure, the date of her dive, her diver's name.
  It belongs because a real dive ends with a log entry; the footer
  is where this page logs itself, and the record is the fourth
  printing of the dive's facts (§1 law).
- **Structure.** `<footer>` on `--foam`: the dive record as a real
  `<table>` (term/value rows), the atelier's ordinary footer matter
  (address, hours, links), and the colophon line. No animation
  layer exists in the footer except the §6.4 rays printed still in
  its top edge — the visitor has surfaced; the water is calm.
- **Motion spec.** None scrubbed. On first arrival, the record's
  rows fade in together over 400ms `--ease-rise` (no stagger — a
  log is written in one hand). The "deepest point" value is not
  typed in the HTML: it is written by the loop from the maximum of
  the dive function (−28 m) at build/render, and §10 audits that
  the rendered string matches the function's maximum.
- **States.** *Rest:* printed footer. *Hover:* links per §6.10
  grammar. *Focus:* standard outlines. *Scrolled-past:* n/a — it
  is the end. *Disabled / no-JS:* the record prints with its values
  server-rendered (the no-JS page still logs the dive honestly;
  the values come from the same data object at build time).
- **Content merge.** The record's facts are the page's facts —
  pearl name from §6.5, depth from §4's function, diver and date
  from the harvest data (§6.11). A footer that logs a different
  pearl than the one pinned is the law's clearest failure, and
  §10 names it.
- **Failure fallback.** The footer has no failure mode beyond the
  page's: it is static HTML. If the loop never ran, the record's
  build-time values stand — correct, because they were generated
  from the same data.
- **Reduced-motion variant.** Identical, minus the 400ms fade.
- **Performance budget & mobile variant.** Zero animation cost.
  Mobile: record stacks as term-over-value rows; footer links
  stack at 44px targets.
- **Choreography timeline (v2).** Footer crosses 60% viewport →
  rows fade 400ms once → rest. Nothing else ever moves in the
  footer, on any visit, at any scroll speed.
- **State matrix (v2).** *Rest:* printed. *Hover:* link underline
  draw (§6.10). *Focus:* outline. *Active:* n/a. *Scrolled-past:*
  n/a. *Disabled / no-JS:* printed with build-time values.
  *Touch:* links at 44px.
- **Breakpoints (v2).** ≥1200px: record left (5 cols), matter
  right (6 cols). 768–1199px: stacked, record first. <768px:
  stacked, record first, colophon last.
- **Edge cases & failure modes (v2).** *Multi-pearl builds:* the
  record logs the featured pearl only — the dive has one purpose;
  other pearls' facts live on their cards. *Season change:* the
  record is regenerated from the new season's data object; a
  footer naming last season's pearl is a stale-data gate failure.
- **Accessibility spec (v2).** The record is a real table with
  `<th scope="row">` terms. Footer landmarks and link text are
  ordinary and descriptive ("The atelier in Mie", not "click
  here"). Contrast `--ink-deep` on `--foam` 12.2:1 throughout.
- **Tokens consumed (v2).** `--foam`, `--ink-deep`, `--mid`,
  `--ease-rise`, `--dur-footer-fade` (400ms).

### 6.15 Surface skeleton & the line-pass transition (page family: loader / transition)

- **What & why.** Two linked pieces. The loader: while the page's
  surface assembles, shallow sections show a water skeleton —
  `--foam-dim` blocks with a slow `--shallow` wash — never a
  spinner (a diver does not spin). The transition: leaving the
  page hauls up the dive line — a `--foam` sheet rises from the
  bottom of the viewport over the old page as the new page's line
  drops (§6.1). Together they keep the visitor in the water
  between states instead of dropping them into a blank browser
  void.
- **Structure.** Skeleton: the real section layout with content
  blocks replaced by same-size water blocks (the DOM ships real
  content; skeletons are a JS-applied pre-paint treatment only on
  slow loads, per the watchdog rule). Transition: a fixed
  `--foam` layer with a foam edge (§6.2's mask family) and a
  centred dive-line segment, animated by the loop.
- **Motion spec.** Skeleton wash: a `--shallow` gradient sweeps
  each block left→right over 1800ms `--ease-sway`, looping until
  content lands; hard cap — any block still skeleton at 3000ms is
  replaced by whatever content exists (the watchdog law: a
  skeleton may never become the content). Transition out: sheet
  rises 450ms `--ease-rise` covering the viewport → navigation →
  new page's sheet lifts 450ms as its §6.1 line drops. Total
  ≤900ms + load.
- **States.** *Skeleton:* washing blocks. *Resolving:* blocks swap
  to content one by one in DOM order, each with a 200ms fade —
  things surface individually, not in a page-wide flash.
  *Transition:* covering → covered (line segment centred, stage
  name of the destination printed beneath it) → revealing.
  *Interrupted transition* (navigation cancelled): sheet lowers
  back 300ms; the visitor is returned to the surface they left.
- **Content merge.** Skeleton blocks are the sections' own shapes
  (a card-shaped block where a card will be) — the visitor reads
  the page's anatomy before its words. The transition's printed
  stage name is the destination's real first stage (§6.10), so
  the pass itself carries orientation information.
- **Failure fallback.** No JS: no skeleton (content streams in
  naturally), no transition (ordinary navigation). Transition
  watchdog: if the new page has not signalled readiness in
  2500ms, the sheet lifts anyway — the visitor is never held
  under a foam sheet.
- **Reduced-motion variant.** No skeleton wash (static water
  blocks), no sheet transition — instant navigation, with the
  destination's stage name briefly shown as a plain foam page
  only if load exceeds 800ms.
- **Performance budget & mobile variant.** Skeleton: CSS gradients
  only. Transition layer: one fixed div + mask. Mobile: identical
  grammar, sweep 350ms each way (a phone's surface is closer).
- **Choreography timeline (v2).** Load: t=0 skeleton arms only if
  first content paint has not occurred by 400ms → blocks wash →
  each content arrival swaps its block (200ms fade) → last block
  + 300ms: skeleton layer removed. Exit click → sheet rises
  450ms → covered beat (line + stage name) until ready or 2500ms
  watchdog → sheet lifts 450ms while §6.1 drops on the new page.
- **State matrix (v2).** *Rest:* no layer. *Hover:* n/a.
  *Focus:* during the covered beat, focus is held on the sheet's
  stage-name heading (`tabindex="-1"`) and restored to the new
  page's heading on reveal — focus is never dropped to `<body>`
  mid-pass. *Active:* n/a. *Scrolled-past:* n/a. *Disabled /
  no-JS:* absent entirely. *Touch:* identical timings minus
  100ms (above).
- **Breakpoints (v2).** Identical grammar at all sizes; skeleton
  blocks follow the section layouts' own breakpoints (§6.11).
- **Edge cases & failure modes (v2).** *Back/forward cache:* a
  bfcache restore shows the page surfaced (no skeleton, no
  transition replay) — the dive resumes where it was, depth
  re-derived positionally. *Slow image inside a resolved section:*
  the image's own placeholder (§6.11) governs; the skeleton does
  not return for one late photograph. *Two rapid navigations:*
  latest wins; the sheet never double-covers.
- **Accessibility spec (v2).** Skeleton blocks are `aria-hidden`;
  the underlying content region carries `aria-busy="true"` until
  resolved. The transition sheet's stage name is a heading that
  AT can read during the covered beat. Neither layer ever traps
  focus or blocks the browser's own loading announcements.
- **Tokens consumed (v2).** `--foam`, `--foam-dim`, `--shallow`,
  `--ink-deep`, `--ease-sway`, `--ease-rise`,
  `--dur-skeleton-wash` (1800ms), `--dur-pass` (450ms),
  `--dur-fallback-pass` (2500ms).

### 6.16 Nacre grain (page family: ambient layer)

- **What & why.** Pearl surfaces on the page — the featured pearl's
  sheen, card frames, the gauge marker — carry a mother-of-pearl
  grain: a soft gradient among the three nacre stops (§2) whose
  hue rotates a few degrees with scroll. It belongs because nacre
  is the theme's material truth: the grain is what makes a pearl a
  pearl rather than a white ball, and tying its shift to scroll
  means the light changes as the visitor moves through the water —
  the same pearl, seen from descending angles.
- **Structure.** A CSS gradient layer (`background: linear-gradient`
  among `--nacre-1/2/3`) applied to declared pearl surfaces only,
  with its angle driven by a `--nacre-turn` custom property the
  loop updates. Surfaces opt in via one class; nothing else on the
  page may use the nacre stops (§2's closed list).
- **Motion spec.** `--nacre-turn` travels 0 → 24deg across the full
  dive (descent) and back on the ascent, scrubbed, lerped at 0.14
  (the light channel). 24 degrees is the whole budget: warm pearl →
  faint violet → faint sea-green and back. The gradient never
  animates on a timer — no scroll, no shift.
- **States.** *At surface:* turn 0deg (warm pearl dominant).
  *At seabed:* 24deg (sea-green edge at the pearl's lower rim).
  *Ascending:* returns by the same function. *Hover:* §6.6's
  highlight is separate; the grain does not respond to hover.
  *Disabled / no-JS:* turn fixed at 8deg (a mid-dive light) on all
  pearl surfaces.
- **Content merge.** The grain lives only on things that are
  pearl or shell in the page's world: the pearls themselves, their
  frames, the gauge's marker, the §6.7 diagram's fills. A nacre
  button or nacre heading would be slop (§9) — the material is
  rationed to what it is.
- **Failure fallback.** If custom-property animation fails, the
  gradient stands static at 8deg — indistinguishable from a
  deliberate still. No content depends on the grain.
- **Reduced-motion variant.** Static at 8deg, as the no-JS state.
- **Performance budget & mobile variant.** Custom-property updates
  on one property, repaint confined to pearl surfaces (small
  areas). Mobile: identical; the surfaces are smaller, the cost
  lower.
- **Choreography timeline (v2).** Continuous with scroll: turn =
  24 × (current depth fraction of the descent, mirrored on
  ascent), lerped 0.14 per frame. At rest, the grain rests —
  there is no idle drift to choreograph.
- **State matrix (v2).** *Rest:* per depth. *Hover:* none.
  *Focus:* none. *Active:* none. *Scrolled-past:* per depth
  function (positional). *Disabled / no-JS:* 8deg static.
  *Touch:* identical scrub.
- **Breakpoints (v2).** Identical at all breakpoints.
- **Edge cases & failure modes (v2).** *Forced-colors mode:* the
  gradient is removed by the UA; pearl surfaces fall back to
  `--pearl` flat — declared in CSS so the fallback is authored,
  not accidental. *Gradient banding on low-end displays:* the
  stops are close in luminance by design; a 2% noise overlay on
  pearl images (part of the image asset, not a runtime layer)
  breaks banding without runtime cost.
- **Accessibility spec (v2).** The grain is never behind text
  (pearl surfaces carry labels *beside*, not on, the gradient —
  the one exception, the gauge marker, has no text). Hue travel
  stays inside the §2 triangle, so no state change can alter any
  text contrast pair.
- **Tokens consumed (v2).** `--nacre-1`, `--nacre-2`, `--nacre-3`,
  `--nacre-turn` (0–24deg), `--pearl`.

### 6.17 Depth stamps (page family: section furniture)

- **What & why.** Every section head carries a small stamp: the
  section's depth range in the §3 data format (`−14 m — THE CRAFT`)
  set in Karla 700 caps beside the section's Cormorant headline.
  They belong because they are the dive's chapter marks — the
  visitor always knows how deep the content they are reading was
  brought from — and because they are the law's most visible
  enforcement: a stamp is generated from the dive-track function,
  so it cannot drift from the gauge.
- **Structure.** A `<p class="depth-stamp">` generated at build
  time from the section's declared band (§4) and rendered in the
  section head; the value is the depth at the section's midpoint,
  formatted by the §3 formatter. On multi-pearl builds the stamp
  also carries the section's stage name (§6.10's registry).
- **Motion spec.** The stamp surfaces with its headline (rise
  18px, 500ms `--ease-rise`, 100ms before the headline so the
  depth is read first — orientation before content). No other
  motion: stamps do not tick, pulse or count; they are print.
- **States.** *Rest:* printed. *Hover:* none. *Focus:* none (not
  interactive). *Scrolled-past:* printed. *Disabled / no-JS:*
  printed — stamps are build-time HTML, present in the no-JS
  page in full.
- **Content merge.** The stamp's depth is the section's own: the
  craft section's stamp says −19 m because the craft section sits
  at −19 m in the track, and §6.7's diagram labels inherit the
  same figure when they cite the depth the pearl grew at.
- **Failure fallback.** None needed — static text. A build error
  (hand-typed stamp) is caught by §10's three-printings audit
  comparing stamps against the function.
- **Reduced-motion variant.** Printed; no rise.
- **Performance budget & mobile variant.** Zero runtime cost.
  Mobile: stamp moves above the headline (stacked) at 12px.
- **Choreography timeline (v2).** Section head crosses 78% →
  stamp rises (500ms) → headline rises at +100ms → body follows
  per §6.11/§6.7 grammar. Scroll-back: no replay.
- **State matrix (v2).** *Rest:* printed. *Hover:* none. *Focus:*
  none. *Active:* n/a. *Scrolled-past:* printed. *Disabled /
  no-JS:* printed. *Touch:* printed.
- **Breakpoints (v2).** ≥1200px: stamp left of headline in the
  margin column. 768–1199px: stamp above headline. <768px: above,
  12px.
- **Edge cases & failure modes (v2).** *Sections added in
  redesign:* stamps regenerate from band declarations; a section
  without a declared band fails the build (the stamp is not
  optional furniture). *Sections spanning a band boundary:* the
  midpoint rule (§4) decides; the stamp prints one depth, never a
  range — a section is at a depth, as a diver is.
- **Accessibility spec (v2).** The stamp is real text in reading
  order, before the headline it belongs to. Its minus sign and
  unit are text, not icons. Contrast per band pairs (§2): on
  `--mid`, `--foam` at 5.2:1; on `--seabed`, `--ink-pale` 10.0:1.
- **Tokens consumed (v2).** `--ink-deep`, `--foam`, `--ink-pale`,
  `--ease-rise`, `--dur-stamp-rise` (500ms).

### 6.18 The drowned page (page family: 404 / empty state)

- **What & why.** The 404 is a page that sank: a deep-band page —
  the only page besides the seabed that lives at the bottom —
  stating plainly that what was sought is below where this site
  goes, with the dive line leading back up to the surface (home)
  and to the stages (§6.10). It belongs because even the site's
  failure is inside the dive's world, and because it enforces the
  law one last time: the drowned page claims no depth figure —
  its stamp reads "BELOW −28 m" as words, not a number the
  function never produced.
- **Structure.** A deep-band page (`--seabed` ground): stamp,
  Cormorant headline ("This one went down without us."), two
  lines in §12's voice, and two real links styled as §6.10's
  stages: "The Surface" (home) and "The Bottom" (the featured
  pearl). A faint dive line rises from the headline toward the
  top of the viewport — drawn, static.
- **Motion spec.** On load, the line draws upward (bottom→top,
  reverse of §6.1) over 1200ms `--ease-draw` — the way back is
  shown, once. Nothing else moves; a lost page is quiet.
- **States.** *Rest:* printed page, line drawn. *Hover/focus
  (links):* §6.10 grammar. *Scrolled:* the page is one viewport;
  no scroll behaviours. *Disabled / no-JS:* line printed drawn.
- **Content merge.** The links are the site's real stages; the
  copy names what likely happened in the theme's voice without
  inventing a cause ("The address may have been copied from a
  shell — they fade."). No fake depth, no fake sitemap.
- **Failure fallback.** The 404 must work with everything broken:
  no JS required, no webfont required (system serif fallback
  declared), no image. It is the most robust page on the site by
  spec.
- **Reduced-motion variant.** Line printed; no draw.
- **Performance budget & mobile variant.** <15 KB total, no
  images. Mobile: identical, stacked.
- **Choreography timeline (v2).** t=0 page printed → t=0–1200
  line draws upward → rest. Links are usable from t=0; the draw
  never gates navigation.
- **State matrix (v2).** *Rest:* printed. *Hover:* link underline
  draw. *Focus:* outline + underline. *Active:* n/a.
  *Scrolled-past:* n/a. *Disabled / no-JS:* printed, line drawn.
  *Touch:* links at 48px.
- **Breakpoints (v2).** ≥1200px: measure 54ch centred in the deep
  band. <1200px: full measure with margins. <768px: stacked,
  headline 36px.
- **Edge cases & failure modes (v2).** *Soft 404s (empty search /
  sold-out season):* reuse this page's dress with honest copy —
  an empty catch page says "The boats came back light." and
  links to the stages; it never borrows the 404's headline.
  *Server error (500):* same dress, plainer copy, no line draw
  (the way back is the browser's, and the page says so).
- **Accessibility spec (v2).** The page is a single heading +
  text + two links; focus order is the reading order. Contrast
  `--ink-pale` on `--seabed` 10.0:1. The HTTP status is correct
  (404) — the theme never trades the status code for the joke.
- **Tokens consumed (v2).** `--seabed`, `--ink-pale`, `--pearl`,
  `--shallow`, `--ease-draw`, `--dur-line-up` (1200ms).

## 7. Page application map

- **Home (the dive itself).** The full structure: surface hero
  (§6.1, §6.2) → shallow catalogue (§6.11) → mid-band craft (§6.7)
  → seabed pin (§6.5) → ascent invitation → reserve form (§6.13) →
  surface break (§6.9) → foam footer + dive record (§6.14). One
  dive per page; the home page is the only page that must contain
  all four stages.
- **Listing / season page.** A shallower dive: max depth −14 m.
  The track function is re-declared for the page (the §1 law
  binds the *page's* maximum, printed in its own footer record —
  a listing page's record honestly logs −14 m). Cards (§6.11) in
  depth order; no seabed pin; the ascent is short and the form is
  a viewing-request variant of §6.13.
- **Detail (a single pearl).** The pearl gets her own dive: hero
  at the surface with her portrait, descent through her harvest
  story and the nacre teaching (§6.7), her own seabed moment
  (static, unpinned — the pin is rationed to the home dive; a
  second pin would be a second breath), ascent to §6.13 with her
  preselected.
- **About / the divers.** Surface-heavy: portraits and names in
  foam and shallow bands, one mid-band section on the cooperative's
  rules (no tanks, no winter diving, the catch limits), and a
  short ascent. The divers' page never goes below −18 m — the
  women are not exhibits at the bottom of their own sea.
- **Journal / story page.** Reading dive: depth accrues slowly
  (track stretched; max −22 m), stamps mark chapters (§6.17), no
  catalogue, no form — the ascent ends in the footer record
  logging the story's deepest chapter.
- **Contact / visit.** No dive: a surface page, foam throughout,
  gauge absent (a page that does not descend does not carry a
  depth instrument — printing one would break the law). Form per
  §6.13's grammar, footer without a dive record (a record of no
  dive is a lie).

- **Checkout (after §6.13's reservation).** Payment, where a
  build takes it online, happens entirely at the surface: a
  dedicated foam page, no gauge, no bands, the pearl's name and
  price restated from `DIVE` (§4) at the top — the visitor is out
  of the water and doing paperwork in daylight, and the theme
  respects the difference between reserving a pearl (part of the
  dive's story) and paying for one (not). The confirmation of
  payment returns the visitor to the surface page, where §6.14's
  record pattern logs the purchase beside the dive that found
  her. A checkout styled as deep water — dark, immersive,
  "experience" — is the one application of this theme that is
  refused outright: nobody should enter card details at −28 m.

## 8. Worked examples

### 8.1 The hero — the title surfaces, the rope goes down

*Build: home page of the Hama Pearl Atelier (fictional but
plausible: an ama cooperative in Mie selling one season's pearls).*
t=0: the foam hero stands printed — Cormorant headline "Brought up
by hand." (the italic word is *hand*), standfirst naming the
cooperative and the season, the depth figure (§6.12) reading
−0.0 m, §6.10's buoy bar above. JS arms §6.1: the dive line drops
from the headline's full stop (1400ms) while, from t=900, §6.2's
foam mask sweeps the headline and its letters rise last-word-first.
By t≈2.3s the surface is still: rope down, title surfaced, rays
(§6.4) beginning their 9s sway at the hero's lower edge where the
shallow band starts. Scroll timeline: the first 400px of scroll
deepen the gauge to ≈−2 m and thin nothing yet; the hero's pearl
portrait (the featured pearl, at the surface for her introduction)
answers the pointer with §6.6's flaw highlight. The visitor has
been taught — rope, depth, light, flaw — before reading a word of
sales copy.

### 8.2 Mid-page — the bottom of the sea

*Build: the seabed pin (§6.5) on the same page.* The descent has
passed the catalogue (cards at −9 to −14 m) and the craft section
(§6.7's diagram drawn at −19 m, its stamp agreeing with the gauge
to the tenth of a metre). At p=0.55 the stage sticks: depth locks
at −28.0 m, the gauge's hairline brightens, and over 120vh the
story surfaces — name ("The Dimpled One"), harvest ("Tuesday's
dive, the third of the morning, from the rope's end"), measure
(9.4 mm), the flaw caption set in the same 14px italic as every
caption on the page ("A small dimple on her left shoulder —
imperfect, therefore real."), and finally price + the reserve
anchor, enabled as the fifth line lands. The nacre sheen crosses
her once at the pin's midpoint. Scroll-back: lines stay surfaced;
the visitor who rises and returns finds her story told, not
reset — the page remembers what it brought up.

### 8.3 Conversion — reserving her on the way up

*Build: §6.13 on the ascent.* The first ascent section brightens
in three declared steps as it enters; on its foam panel the form
stands with "The Dimpled One" preselected — generated from the
same catalogue data as her card and her pin, so name, measure and
price on the form are character-identical to §8.2's. The visitor
adds a name and email; a mistyped email earns the margin note in
the desk voice (§12): "That direction will not carry — check the
address." Entries are kept. On submit, the button reads "Holding…"
for the server's beat, the panel's foam edge sweeps, and the
confirmation surfaces: her name, the server-issued reference, and
"She will be kept above water until Friday." Her card, far above
in the catalogue, stamps itself TAKEN UP in the same beat. The
visitor continues up through §6.9's surface break into §6.14's
footer, where the dive record logs the dive they actually made —
deepest point −28 m — beside the pearl they have just reserved.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The aquarium screensaver.** Clip-art bubbles drifting up the
   whole page on a timer, fish silhouettes, wave SVGs lapping at
   section tops. *Cure:* bubbles exist only as §6.8's click-born
   air; waves exist only as foam edges on §6.2/§6.9; nothing
   swims. If it would work on a dentist's waiting-room screen, it
   is banned.
2. **The gradient dive.** A single blue gradient sprayed down the
   page with white text throughout, contrast dying by degrees.
   *Cure:* §4's authored bands + §2's contrast law — four tested
   grounds, text colour switching by band, audited at three
   depths.
3. **Depths typed by hand.** A "−30 m" in a headline, "40 metres"
   in a caption, gauge disagreeing with both. *Cure:* the §1 law —
   one function, four printings, §10's audit greps every depth
   string in the build against the formatter.
4. **The flawless pearl.** Stock-photo perfect spheres, airbrushed.
   *Cure:* exactly one flawed pearl, the featured one, her dimple
   in the photograph, her caption, her alt text and §6.6's
   coordinates — four printings of the flaw, audited.
5. **Drop shadows underwater.** Cards levitating with soft shadows
   on hover. *Cure:* §6.11 — hover deepens water and scales the
   image; nothing lifts, nothing casts.
6. **A second pin.** Pinning the craft section "for engagement"
   too. *Cure:* one pin per dive (§5). A second held breath is a
   different, lesser theme.
7. **Neon nacre.** Iridescent rainbow gradients on buttons and
   headings. *Cure:* §2's closed nacre triangle and §6.16's
   ration — grain only on pearl surfaces, travel capped at 24°.
8. **The drowning footer.** A page that descends and simply ends
   dark. *Cure:* the ascent is ~⅓ of the track by construction
   (§4's function); §10 measures it.
9. **Progress-bar relapse.** A thin "reading progress" bar added
   by habit above the header. *Cure:* progress is depth (§6.3);
   the bar is removed in review, every time.
10. **Breath gamification.** "You held your breath for 0:42!"
    timers, lung-capacity widgets, streaks. *Cure:* refused
    outright — the breath is a metaphor for attention, never a
    score (§1's when-not-to-use).
11. **Instant darkness.** Sections that fade to black as a "deep"
    effect over text. *Cure:* scrims capped at 0.35 and never
    behind text (§2 law); depth is a background you author, not a
    dimmer you drag.
12. **Generic sea copy.** "Dive into our collection!" puns.
    *Cure:* §12's voice — the sea is where these women work; the
    copy is a work log, not a holiday brochure.

## 10. Quality gate

Blocking — all must pass before the theme ships:

1. **Law audit (three printings + record).** At five scroll
   positions, the gauge readout, the centred section's stamp and
   the live depth figure agree to 0.1 m; the footer's record
   maximum equals the dive function's maximum (−28 m home build).
2. **Depth-string grep.** Every depth string in the shipped HTML
   matches the §3 formatter's output pattern; any hand-typed depth
   fails the build.
3. **Contrast audit.** Screenshots at −3 m, −16 m, −27 m: every
   visible text element meets WCAG AA against its actual ground.
4. **Ascent measurement.** The ascent occupies ≥30% of the dive
   track; the footer ground is `--foam` (or the dark-mode surface,
   §2).
5. **Flaw audit.** The featured pearl's dimple coordinates
   (`data-dimple`) land on the visible dimple in the shipped
   image at two breakpoints; caption and alt text name the flaw.
6. **One-pin audit.** Exactly one pinned section in the build.
7. **No-JS dive.** With JavaScript disabled, the full page reads
   top to bottom: headline printed, diagram drawn, story lines
   present, gauge chart static, form submittable.
8. **Form-keeping rehearsal.** Submit §6.13 with a bad email:
   entries preserved, error in §12 voice, focus moved to the
   field, note announced.
9. **Reduced-motion pass.** With `prefers-reduced-motion`, the
   page is the static depth chart: no pin, sway, draws or counts;
   all content present in order.
10. **Watchdog pass.** Loop killed mid-dive: gauge snaps to true
    depth, pin lines print, diagram completes, headline rests —
    nothing stranded anywhere.

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components not listed do not get invented ad hoc; if a build needs
one, it is added here first.

- **Buttons.** Primary: `--mid` ground, `--foam` text, Karla 700
  caps; hover deepens to `--mid-deep` (300ms); active sinks 2px
  (§6.13's grammar); focus 2px outline `--mid-deep` offset 2px.
  On the deep band: `--pearl` ground, `--ink-deep` text. Buttons
  never use nacre (§6.16 ration) and never cast shadows.
- **Links (body).** `--mid` with the §6.10 dive-line underline;
  deep band: `--shallow` (7.0:1 on `--seabed`).
- **Inputs / textarea / select.** Foam ground, 1px `--shallow`
  rule beneath, focus draws the dive-line underline + deepens one
  step (§6.13); labels always visible above; errors per §12.
- **Cards.** §6.11, verbatim. No other card style exists.
- **Badges / stamps.** Text-only stamp lines in the §3 data style
  ("TAKEN UP", "FROM −19 M") — never pill-shaped, never coloured
  chips; a badge on this page is a log entry.
- **Tables.** The dive record (§6.14) is the pattern: row rules in
  `--shallow` at 40%, terms Karla 700, values tabular; no zebra
  striping (the water bands are the striping).
- **Pagination.** Refused as numbered pages; a season archive is a
  shallower dive (§7 listing) linked as a stage. "Older seasons"
  is a surface link, not a pager.
- **Modal / dialog.** One pattern: the quick-view of a card pearl,
  presented as a *shallows panel* — a foam sheet rising from the
  viewport's bottom edge (400ms `--ease-rise`), holding her
  photograph, measure, depth and reserve action. It never darkens
  the page below 0.35 scrim (§2 law) and closes by sinking.
- **Toast.** Refused. Confirmations surface in place (§6.13) or
  not at all; nothing on a dive pops up from nowhere.
- **Tabs.** Refused. Stages (§6.10) are navigation, not tabs; a
  page's bands are travelled by scroll, not switched.
- **Accordion.** The journal page's chapter list only: chapter
  rows open downward like a held breath released (height 350ms
  `--ease-rise`), one open at a time, stamps (§6.17) on every row.
- **Alerts.** In-band margin notes in §12's voice, `--mid-deep`
  text + dive-line rule; never red — there is no red in this
  palette, and an error is a direction that will not carry, not
  an alarm.
- **Loader.** §6.15's water skeleton. Spinners are banned.
- **Tooltip.** Refused. Anything worth saying is printed (the
  flaw caption is the model: say it in the open).
- **Breadcrumb.** Refused; the stage label (§6.10) + stamp
  (§6.17) already answer "where am I" in the theme's own terms.
- **Price / measure display.** Karla tabular, unit always present
  (mm, m, £), formatted by the §3 formatter family.
- **Image frame.** Nacre-edged (1px gradient border from §6.16's
  stops) on pearl photography only; other photography takes a
  plain 1px `--shallow` rule. Frames never have shadows.

## 12. Content & copywriting voice

Two registers. **The Diver** speaks for the work: short, factual,
unadorned — a woman reporting a dive. **The Desk** speaks for the
atelier: warm, plain, commercial without pressure. Neither register
ever uses sea puns, exclamation marks, or the word "luxury".

- **Headlines (Diver).** Statements of fact with one image allowed:
  ✓ "Brought up by hand." / ✓ "Six winters of nacre." /
  ✗ "Dive into luxury!" / ✗ "Pearls like you've never seen!!!"
- **Labels & buttons (Desk).** Verbs from the work: "Reserve her",
  "See the season", "Come up" (for returning to the top — never
  "Back to top ↑"). ✗ "Buy now", "Grab yours".
- **Depth & data (formatter only).** "−19 m", "9.4 mm", "214
  oysters" — §3 law 2. Copy never rounds a depth for rhythm.
- **The flaw caption (fixed pattern).** "[The flaw], — imperfect,
  therefore real." ✓ "A small dimple on her left shoulder —
  imperfect, therefore real." The pattern is used once, for the
  one flawed pearl; applying it to everything makes it a slogan
  (§9.4).
- **Error voice (Desk, margin notes).** The direction metaphor,
  used consistently: ✓ "That direction will not carry — check
  the address." / ✓ "She needs a name to be kept for." /
  ✗ "Invalid input!" / ✗ "Oops! Something went wrong."
- **Empty states (Diver).** ✓ "The boats came back light."
  (empty catch) / ✓ "Nothing was brought up from that depth."
  (empty search) / ✗ "No results found."
- **Success (Desk).** ✓ "She will be kept above water until
  Friday." — a concrete keeping, with a day in it. ✗ "Success!
  Your order has been placed."
- **Banned words.** dive in/into (as a verb of invitation), pearl
  of wisdom, hidden gem, treasure, breathtaking (the one word
  this theme may never use about itself), luxury, exclusive.
- **Owned words.** brought up, kept, the rope, the season, her
  diver, above water, the bottom — used sparingly, always
  literally before figuratively.

## 13. Full-page scroll choreography map

The home dive, top to bottom (progress = dive-track `p`, §4):

1. **p 0.00 — the surface.** Buoy bar (§6.10) in place; dive line
   drops (§6.1); headline surfaces through foam (§6.2); depth
   figure reads −0.0 m. *Feels like:* standing on the boat.
2. **p 0.02–0.10 — first metres.** Hero pearl answers hover with
   the flaw highlight (§6.6); rays (§6.4) at full strength; gauge
   begins its fall. *Feels like:* slipping under, light everywhere.
3. **p 0.10–0.28 — the shallows.** Catalogue cards surface in
   stagger (§6.11) at −6 to −14 m; clicks release bubbles (§6.8);
   rays thin measurably. *Feels like:* browsing the reef shelf.
4. **p 0.28–0.50 — the mid band.** Ground becomes `--mid`; the
   nacre diagram draws layer by layer (§6.7); figures count
   (§6.12); rays reach zero at −14 m and are gone. *Feels like:*
   the quiet middle, one idea at a time.
5. **p 0.50–0.55 — the deepening.** Ground steps to `--seabed`;
   measure narrows; the featured pearl appears at the stage's
   top. *Feels like:* the light going, deliberately.
6. **p 0.55–0.68 — the bottom.** The pin (§6.5): depth locked at
   −28.0 m, five story lines surface, sheen crosses at the
   midpoint, reserve anchor enables at 0.83 of the pin. *Feels
   like:* held stillness — the point of the whole page.
7. **p 0.68–0.80 — the turn.** Stage releases; first ascent
   section brightens step one; the form (§6.13) appears in
   returning light. *Feels like:* the kick upward.
8. **p 0.80–0.93 — the shallows again.** Ground steps back through
   shallow tints; rays re-form ahead (§6.9); invitation copy.
   *Feels like:* light flooding back.
9. **p 0.93–1.00 — the surface break & the log.** Foam sweeps
   (§6.9); footer (§6.14) continuous with the section; the dive
   record prints the dive just made; gauge rests at −0.0 m.
   *Feels like:* head out of the water, logbook open.

**Reverse pass.** Scrolling up replays the map in mirror: every
scrubbed value (depth, rays, grain, break) retraces exactly;
every *completed* event (surfaced lines, drawn diagram, counted
figures) stays completed. The page remembers what it brought up.
**Jump scroll.** Any jump lands positionally correct in one frame
(§4); completed-event elements between the old and new positions
resolve to their completed states instantly, without playing.

**A note on what is not choreographed.** The map above assigns
every motion a beat, but it deliberately assigns the visitor no
feelings to perform: there is no moment where the page asks to
be admired, no "wow" beat, no reveal staged for its own gasp.
The two beats that carry emotion — the find (§6.5) and the
surface (§6.9) — earn it structurally: the first by stillness
after a long descent, the second by light returning after a long
dark. If a build review finds a third emotional beat, it is
almost certainly a piece of decoration that crept in (§9.1) and
it comes out. The theme's restraint is not a lack of ambition;
it is the discipline the whole concept is borrowed from — an
ama does not perform the dive, she works it.

**Timing contract.** At a natural reading pace the full dive
takes 2½–4 minutes: roughly 60–80 seconds of descent, 30–45
seconds held at the bottom (the pin's 120vh at reading speed),
and 60–90 seconds of ascent including the form. A build whose
track is so short that the bottom arrives in under 20 seconds of
scrolling has made the pearl too easy to reach — depth must cost
time, or the gauge is lying about effort even when its numbers
are honest. Conversely, a descent over ~4,500 words of body copy
before the pin tests the breath past the theme's welcome: cut
copy or move a section to the ascent before lengthening the
track. These are editorial measurements, taken with a stopwatch
on the real build during the §15 voice pass — not aspirations.

## 14. Whole-page performance budget

- **Total page weight:** ≤900 KB (home dive), of which the
  featured pearl image ≤180 KB (preloaded — it is the dive's
  purpose), card images ≤60 KB each and lazy below the first row,
  fonts ≤110 KB (Cormorant Garamond 500 + italic subset; Karla
  400/700), JS ≤45 KB, CSS ≤38 KB. No other imagery ships without
  a budget line here.
- **Frame budget:** the single loop does ≤1.2ms of work per frame
  (one depth computation, one lerp pass over ≤14 subscribed
  values, style writes batched); no layout reads inside the loop
  (track geometry is measured on resize only). Long tasks: none
  over 50ms after load; the §6.2 letter-wrapping is the largest
  single task and is capped by the 40-letter rule.
- **Paint discipline:** scrubbed layers are transform/opacity
  only; the nacre grain (§6.16) repaints only pearl surfaces;
  rays (§6.4) are unrendered below −14 m rather than transparent.
- **Cut order when over budget:** (1) ray sway (keep scrubbed
  thinning); (2) nacre grain travel (fix at 8deg); (3) card
  surfacing stagger (print in pairs); (4) skeleton wash animation
  (static blocks); (5) §6.15 transition (instant navigation).
- **Never cut:** the depth function's single source (§1 law), the
  watchdogs, the no-JS completeness, the flaw and its caption,
  the ascent's share of the track. A build that ships without
  these is not a cheaper version of the theme; it is a different
  page wearing the palette.

- **Measurement method (named, so two builders get the same
  numbers).** Frame cost is measured on the loop's own
  instrumentation: the loop records its per-frame execution time
  into a ring buffer, and a debug build reports the 95th
  percentile over a full descent + ascent on a mid-tier Android
  device (the library's reference handset class), throttled to
  4× CPU slowdown in devtools as a cross-check. Page weight is
  measured as transferred bytes on a cold cache, fonts included,
  from the production build — not from the dev server. A budget
  dispute is settled by these two measurements and no others;
  "it feels smooth on my machine" is not evidence at the gate.

## 15. Build-order checklist

1. **Static surface first.** Build the whole page as the no-JS
   depth chart: bands, stamps, drawn diagram, printed story,
   static gauge chart, working form. Gate §10.7 passes here,
   before any motion exists.
2. **The dive function.** Implement §4's mapping + formatter;
   wire gauge, stamps, figures, record to it. Gate §10.1/10.2.
3. **The loop.** One rAF loop, lerp 0.10 / 0.14 channels,
   subscription list; kill-switch test for §10.10.
4. **Bands & contrast.** Author the four grounds and text pairs;
   screenshot audit at three depths (§10.3).
5. **The line & the headline.** §6.1 drop, §6.2 surfacing, with
   watchdogs and session flags.
6. **Rays & grain.** §6.4 scrub + sway; §6.16 grain ration.
7. **Cards & bubbles.** §6.11 surfacing and hover grammar;
   §6.8 bubble caps.
8. **The diagram.** §6.7 generated from its data list (SVG +
   labels together).
9. **The pin.** §6.5 with thresholds, focus rule and the
   mobile cut. Gate §10.6.
10. **Figures.** §6.12 counting with the AT-honesty pattern
    (hidden true value, animated aria-hidden twin).
11. **The ascent.** §6.13 form (data-generated options),
    §6.9 break steps, §6.14 record generation. Gate §10.8.
12. **Furniture.** §6.10 buoy, §6.15 skeleton/transition,
    §6.18 drowned page.
13. **Reduced-motion build.** The static depth-chart variant as
    a first-class render, not a media-query afterthought.
    Gate §10.9.
14. **Voice pass.** Every string checked against §12; banned
    words grepped; flaw caption verified word-for-word.
15. **Full gate.** §10 all ten items, signed by someone who did
    not build the page.
16. **Surface.** Only when all ten gate items pass does the
    build come up for release — and the release note, like the
    footer (§6.14), logs the dive the page makes: its maximum
    depth, its featured pearl, and the name of the non-builder
    who signed the gate. A release without that log line is
    treated as a dive nobody recorded, and it does not ship.
