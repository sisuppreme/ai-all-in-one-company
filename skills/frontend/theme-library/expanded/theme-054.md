# 54. Beeswax & Comb — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never
redesigned).** Not cute honey branding — the material science of
wax: warmth, drips, translucency, and a page structured like comb
cells that get filled as you explore. Palette anchors: pale wax
`#F7E7C3`, honey `#E9B44C`, deep comb `#B97A1E`, propolis brown
`#6B4423`, hive dark `#2A1D10`. Type: Fraunces (display) + Work
Sans (body). Hexagonal cells are used structurally — section
grids, the shop grid and the side progress comb are all real comb
geometry, never clip-art; layered semi-opaque wax panels give the
page its translucency; the pricing section hangs wax drips from
its top edge; candle burn times are listed in evenings, not hours.

## 1. Concept & world

Beeswax & Comb is the website of a material that is worked warm
and stored in geometry. Beeswax is not poured and forgotten: it is
melted, dipped, rolled, cooled, and finally capped — sealed under
a thin wax lid the bees lay over a full cell to keep what is
inside. The page holds both halves of that life at once. Its
structure is the comb: hexagonal cells that share walls, each one
a container with a job — a product, a price, a section of the
reader's progress — and its behaviour is the wax: things warm,
soften, settle a few pixels, drip under gravity, and cool back to
stillness. Nothing on the page is rectangular by default, because
nothing in a hive is. Nothing glows without a heat source, because
in a candleworks light is a physical event with a wick under it.

The world the page performs is the candleworks at the hour the
lamps are lit. The hero is a sheet of pale wax warming from its
centre, the headline settling into it letter by letter the way
type settles into warm wax under a stamp. As the visitor reads,
they do the bees' work without being told a story about it: the
comb fixed at the side of the page fills cell by cell with honey
colour as each section is completed — progress you can see stored,
not a bar that evaporates. In the shop, candlelight itself drifts
across the grid on a slow loop and gathers under the visitor's
pointer, warming each product's wax frame as it passes; a frame
warms in tone as its product nears the centre of the screen,
because proximity is warmth. Over the pricing section, wax drips
hang from the top edge and lengthen as the section approaches —
the candles' own wax melting over the offers it belongs to. In
the making section the page pins, and one drip forms at a wick
point, stretches to three times its length, necks, and falls,
exactly as the adjacent copy narrates the pour. When the visitor
chooses a product they do not tick a box: they cap its cell, a wax
seal dot fills in the card's corner, and the product is stored in
"your comb" — the visitor stores goods the way bees store honey,
in the comb itself.

**The theme's one law: the comb fills only with what was actually
gathered.** Every fill, count, percentage and tally on the page is
computed from one completion record — the set of sections the
visitor has genuinely read to their end — and that record is
printed three ways that must never disagree: the side comb's
filled cells (§6.2), the assistive-technology percentage the same
element carries (§6.2 accessibility), and the footer's stored
tally (§6.17). A comb that arrives pre-filled for looks, a
percentage rounded up for encouragement, a "cells" figure typed
into copy — each is a gate failure, because in this world a filled
cell is a claim that something was gathered, and the page does not
lie about its stores. The corollary is the warmth law: **warmth
is attention made visible, and nothing warms that the reader is
not actually looking at.** Frames warm as they centre (§6.9),
light pools brighten only products inside the viewport (§6.6),
the pointer gathers the pool only over the grid it is actually
touching (§6.6). A warm glow painted onto an off-screen product, a
hero that stays lit after the reader has left it — decoration
warmth — is the same lie in a softer colour. The second corollary
is the unit law, inherited from the original entry's anti-slop
detail and promoted to a gate: **burn time is stated in evenings,
never hours** — one evening is one burning session at a table,
defined once in the science section (§6.7's neighbour copy) as
roughly three hours, and every candle on the site is measured in
that unit, because evenings are how people actually spend candles.

**Best-fit sites and audiences.** Beeswax candle makers and
chandlers first of all; beekeepers and honey farms selling comb,
sections and raw wax; wax suppliers and candle-making schools
(workshops are quite literally evenings); natural-skincare makers
whose balms are wax-based and whose register is material rather
than cosmetic; encaustic artists; a meadery with patience; any
small maker whose product is warm, slow, stored, and sold in
small numbers to people who read labels. The audience it suits is
unhurried and tactile: people who buy by material and method, who
will notice that the progress indicator is a comb and that it is
honest, who light a candle most evenings and think in evenings.
Conversion in this world is an order, a workshop booking, or a
subscription to a candle club — considered, repeatable acts.

**When NOT to use it.** Not for anything cold, fast, or
industrial: electronics, logistics, discount retail, anything
whose promise is speed or volume — the wax would be a costume.
Not for data-dense tools: hex geometry is a container for goods
and stories, not for scanning tables, and §11 refuses the dense
data grid rather than bend cells around it. Not for children's
brands, despite the bee association — this theme's whole point is
that it is *not* cute; there is no mascot, no cartoon bee, no
rounded honey-yellow wash (see §9). Not where the client sells
nothing warm, stored, or made: a comb with nothing to store is
clip-art, which §9 failure 1 names. And not where the content
cannot supply real figures — real burn evenings, real cell
counts, real section records — because the law audits them; a
site that must invent its numbers should choose a theme whose law
it can keep.

## 2. Palette

Five anchors, inherited exactly. Derived tokens are a closed
list; a colour not in this table does not appear on the page.
Contrast figures below are measured (WCAG ratio, computed for
this expansion), not estimated.

| Token | Hex | Role | Usage | Pairing / contrast |
|---|---|---|---|---|
| `--wax` | `#F7E7C3` | Pale wax — the page's ground, panel faces, cell interiors at rest | ~55% of surface | Ground for `--hive` text at 13.38:1 |
| `--honey` | `#E9B44C` | Honey — fills, glows, the warm accent; stored progress; light pools | ~12%, never a ground | On `--wax` 1.55:1 — **never text, never a label ground**; on `--hive` 8.66:1 — licensed for large labels on dark only |
| `--comb` | `#B97A1E` | Deep comb — cell walls, drip bodies, diagram strokes, seal dots | ~10% | On `--wax` 2.93:1 — graphical and display only, **never body text** |
| `--propolis` | `#6B4423` | Propolis brown — secondary text, captions, rules, footer ground band | ~13% | On `--wax` 6.93:1 — the licensed secondary-text voice; on `--honey` 4.48:1 — large text only (≥18px) |
| `--hive` | `#2A1D10` | Hive dark — primary text, dark panels, the pinned making section's ground | ~10% | On `--wax` 13.38:1 — the text anchor |

Derived tokens (closed list):

- `--wax-pale #FBF3DC` — the palest sheet: card faces lifted off
  the ground, the skeleton's shimmer base, form fields at rest.
  `--hive` on it: 14.78:1.
- `--comb-deep #8F5E12` — the only text form of deep comb: links,
  small labels, prices' unit words. On `--wax` 4.54:1. Any text
  the design wants in "deep comb" uses this token; `--comb`
  itself never sets text below display size.
- `--wax-shadow #E3C98F` — the cool side of wax: cell-wall shading,
  panel under-edges, the drip's shadow edge. Graphical only.
- `--glow rgba(233,180,76,.38)` — the light pool's colour, always
  an alpha over a real surface, never a fill: a pool is light
  *on* wax, not a yellow shape.
- `--seal #B97A1E` — the wax-seal dot (aliases `--comb`; named
  separately so the gate can grep seal usage independently).
- `--err #8C3B12` — error text and rules on `--wax`: 5.9:1
  (computed against `--wax-pale` fields at 6.4:1). Errors never
  borrow honey; honey is good news only.

**Dark behaviour — lamplight, not inversion.** Under
`prefers-color-scheme: dark` the page does not invert; the
candleworks simply works after sunset. Grounds go `--hive`;
translucent wax panels keep their material — a wax panel over a
dark room is still pale wax, lit from within, so panel faces stay
`--wax`/`--wax-pale` at 88% opacity over the dark ground and text
on them stays `--hive`. Text that sits directly on the dark
ground is `--wax` (13.38:1). Honey's role grows slightly (fills
and glows read stronger at night — usage ~15%) and `--glow`
alpha rises to .46, because a pool of lamplight in a dark room is
brighter relative to its surround; the pool's radius and speed do
not change. The one thing dark mode must never do is turn the wax
dark: a black panel with yellow text is a different theme wearing
this one's name (§9 failure 11).

**Usage discipline.** Honey is rationed the way the law rations
warmth: it appears as fill (stored progress), as glow (light on a
surface), and as the single warm accent in a composition — never
as a background wash, a button fill behind small text, or a
section tint. A page where honey exceeds its ~12% is a page that
has started shouting (§9 failure 2).

## 3. Typography

**Faces.** Fraunces (display — its soft, wonky serif is the only
display face whose letterforms look poured rather than cut; use
the `opsz` axis, softness `SOFT` 100, wonk on for headlines) and
Work Sans (body, data, labels — a grotesque with warm proportions
that does not fight the wax). No third face. Handwriting is
refused: a chandler's hand appears as the seal and the drip, not
as a script font (§9 failure 9).

**Scale** (1.25 ratio on a 17px body, tightened at display sizes
because Fraunces swells):

| Role | Size / line-height | Face, weight | Tracking |
|---|---|---|---|
| Display (hero headline) | 54px / 1.04 (≥1200), 42px (768–1199), 33px (<768) | Fraunces 72pt optical, 560 | −0.01em |
| H2 (section title) | 34px / 1.12 | Fraunces, 560 | −0.005em |
| H3 (cell title) | 21px / 1.25 | Fraunces, 600 | 0 |
| Body | 17px / 1.62 | Work Sans, 400 | 0 |
| Standfirst | 20px / 1.5 | Work Sans, 350 | 0 |
| Caption / record | 13.5px / 1.45 | Work Sans, 450 | +0.01em |
| Data (figures, evenings) | 15px / 1.4, tabular | Work Sans, 550, `tnum` | 0 |
| Cell label (nav, comb) | 12px / 1.2, uppercase | Work Sans, 600 | +0.14em |

**Type laws.**
1. **Fraunces is poured, Work Sans is measured.** Display type
   may melt, settle and drip (§6.1); data type never animates
   except counting between two true values (§6.15). A figure set
   in Fraunces is a category error — figures are records.
2. **The evening is the unit.** Every duration of use is set in
   evenings in data type: "about 14 evenings". The word "hours"
   does not appear in product copy anywhere on the site (§10 gate
   2 greps it); the science section's single defining sentence is
   the only place the conversion is stated.
3. **Warm words, plain grammar.** Headlines are short declarative
   fragments about material and use ("Poured on Tuesdays.",
   "Fourteen evenings, give or take one."), never exclamations;
   the theme bans the exclamation mark in display copy (§12).
4. **Uppercase is for cell labels only** — the comb's small
   stamped labels. Headlines and buttons are sentence case; a
   shout does not belong in a warm room.
5. **Line-height loosens as wax warms.** Body copy inside a
   translucent panel sits at 1.66 (the panel register); body copy
   on the flat ground at 1.62. The 0.04 is subliminal and
   deliberate: text inside wax breathes slightly more.

## 4. Layout language

**The comb grid.** The page's structural unit is the flat-top
hexagon cell, sized in three registers: the **comb cell** (side
progress comb, §6.2) at 34px across flats; the **grid cell** (shop
and section grids) at a 12-column layout whose cards sit inside
hex-clipped wax frames with a shared-wall gap of 10px; and the
**panel cell** (hero and section panels) — large translucent wax
sheets whose corners are cut at the comb angle (30° chamfers,
`clip-path` polygon), so even a rectangular panel declares its
geometry. Cells share walls: in the shop grid, adjacent frames
are separated by exactly one wall's width (10px ground showing),
never double-walled with margins on both sides — the eye must
read one comb, not a pile of hexagons (§9 failure 5).

**Translucency.** Panels are layered semi-opaque wax: `--wax` at
82–92% opacity over the ground or over a `--hive` photograph
plate, so underlying colour warms the panel the way light through
a wax sheet warms. Two panel depths exist — sheet (92%, body
content) and veil (82%, captions and overlays) — and a third
layer is refused: translucency stacked three deep turns to mud
(§9 failure 6). Panels parallax at comb-over-comb depths (§5):
the ground at 0.94×, sheets at 1.0×, veils at 1.05×, a maximum
differential travel of 18px across a section, re-converging at
section boundaries so text columns never shear apart.

**Spacing rhythm.** Vertical rhythm is the pour: sections are
separated by 96px (≥1200), 72px (768–1199), 56px (<768) of ground
— cooling space between pours. Within a section, the title sits
28px above its first cell. The pricing section is the one
exception to top spacing: its top edge carries the drips (§6.3),
which occupy the first 64px of the section's box, and its title
clears them by a further 24px.

**Density rules.** Density falls as the page warms: the hero is
one panel, one headline, one standfirst, two actions — nothing
else above the fold. The shop grid is the densest surface (3
cells across ≥1200, 2 at 768–1199, 1 below) and is immediately
followed by the science section's single diagram (§6.7) at rest
density. The making section (§6.4) is pinned and sparse: one drip,
one column of copy, 120vh of time. No section may contain two
competing spectacles; where the original entry gives a section
both a diagram and a mask reveal, they are sequenced, never
simultaneous (§13).

**The margin comb.** At ≥1200px the left margin holds the filling
comb (§6.2): a fixed rail 64px wide, vertically centred, holding
18 cells in a 2-column honeycomb offset. The rail is furniture,
not content: it never overlaps the measure (the layout reserves
its 64px + 24px gutter at all times, so content never slides
under it), and it is the only fixed element on the page besides
the reduced top strip that replaces it below 1200px (§6.2
breakpoints).

**Whitespace is cooling.** The ground between cells is not empty;
it is where wax cools. Sections end with a deliberate 40px of
unadorned ground before the next pour — no rules, no dividers,
no "next section" teasers. The page trusts the comb at the side
to say where the reader is.

## 5. Full motion system

Five named easings, used by every element and named in every
spec; no element invents a sixth.

- `--ease-melt: cubic-bezier(.2,.9,.3,1.2)` — the wax ease from
  the original entry: a soft overshoot, for things settling into
  warmth (headline letters, melt-ins). Overshoot is capped by the
  distances it serves (≤4px), so the bounce reads as softness,
  not springiness.
- `--ease-pour: cubic-bezier(.25,.8,.3,1)` — liquid rises and
  fills: comb cells, seal dots, skeleton shimmer fills. Fast
  start, long settle — a pour fills quickly then levels.
- `--ease-drip: cubic-bezier(.6,.05,.8,.4)` — gravity's curve:
  slow necking, fast stretch. Drips elongate, the pinned droplet
  falls, the curtain drops.
- `--ease-settle: cubic-bezier(.2,.7,.3,1)` — the general landing:
  panels, cards, images scaling in-frame. No overshoot; cooled
  wax does not bounce.
- `--ease-draw: cubic-bezier(.45,0,.2,1)` — strokes and walls:
  the comb diagram's walls, leader lines, the footer's rule.

**The shared loop.** One `requestAnimationFrame` loop drives
every scrubbed value on the page — drip lengths, parallax,
warmth, the light pool's drift, the pinned drip's phase — with
lerp factor **0.12** for position and **0.10** for warmth (warmth
lags position slightly, the way real wax lags a flame). No scroll
handler writes styles; scroll handlers update targets only. The
loop sleeps when the tab is hidden and when every registered
value is within 0.1% of target for 30 consecutive frames.

**Motion vocabulary, translated or refused.** Scroll-triggered
reveals: sections melt in (§5 below). Parallax: comb-over-comb
depths (§4). Pinned scenes: exactly one — the making drip
(§6.4); a second pin is refused, pins are expensive attention.
Masked reveals: hex-cell masks over images (§6.5). Blur-to-sharp:
**refused** — wax does not blur, it warms; images resolve by
scale and tone (§6.9), never by focus. Animated counters: between
two true values only (§6.15). Progress: the filling comb (§6.2)
— the theme has no progress bar, and §11 refuses one.
Marquee: **refused** — nothing in a hive hurries sideways.
Ambient loops: exactly two — the hero's inner glow (§6.12) and
the migrating light pools (§6.6), and the second runs only while
the shop grid is in view. Kinetic type: refused beyond §6.1's
single dripping letter. Page transitions: the drip curtain
(§6.10), route changes only. Hover physics: tilt ≤4° (§6.13),
pool gathering (§6.6), seal press (§6.8).

**Melt-ins.** Every section's content melts in on first entry:
opacity is never touched (content is visible from first paint —
the melt is a *settle*, not a reveal): elements translate Y +4px
→ 0 over 550ms `--ease-melt`, staggered 60ms per cell in honey
order (centre-out in grids, top-down in columns), and their panel
tone warms by 4% over the same beat. Trigger: IntersectionObserver
at 20% visibility, once per section per session. Content that has
melted in never melts again; scrolling back up is met with the
settled page. The 4px cap and the no-opacity rule are the
original entry's safety clause kept verbatim in spirit: a melt-in
can fail in any way it likes and the content is still simply
*there*.

**Durations ledger.** Glow warm-up 1000ms; letter settle 380ms
at 50ms stagger; drip-letter elongate 600ms; cell fill 400ms;
drip scrub — continuous, no duration; pinned drip — 120vh of
scroll; hex-mask ring 60ms per ring; pool drift 9000ms loop;
pool gather 700ms; diagram draw 1600ms; seal fill 450ms; frame
warm — scrubbed; curtain 700ms; counter count 900ms; skeleton
shimmer 1200ms loop until resolved. Nothing on the page animates
longer than 1600ms except the two ambient loops and scrubbed
values; a duration not in this ledger does not ship (§15 step 12
checks it).


## 6. Signature elements

### 6.1 The melting headline

- **What & why.** The hero headline is set in the material the
  site sells. On load, a radial candle-glow warms the hero panel's
  centre; the headline's letters then settle downward a few pixels
  each, as type pressed into warming wax, and the final word's
  last letter elongates like a drip and snaps back. It belongs
  because the first thing the visitor learns is not the brand's
  name but its physics: here, warmth makes things settle, and type
  is wax. Every later melt, drip and fill is a rhyme the visitor
  already knows how to read.
- **Structure.** A real `<h1>` in Fraunces carrying the full
  headline text in the DOM from first paint, its letters wrapped
  in `<span class="ltr">` by JS only (the unwrapped headline is
  the no-JS state). Behind it, inside the hero panel, a
  `--glow` radial layer (420px diameter at ≥1200px) centred on
  the headline's optical centre, `pointer-events: none`,
  `aria-hidden`. The final letter carries a dedicated transform
  origin at its top centre so its elongation hangs downward like
  wax, not a stretch from the baseline.
- **Motion spec.** Trigger: load, gated on `document.fonts.ready`
  raced against an 800ms timer (settling letters in a fallback
  face would land at wrong offsets; if fonts lose, the headline
  ships printed — see fallback). t=0: the glow warms 0 → full
  over 1000ms `--ease-settle`. Letters begin at t=250ms: each
  translates Y −4px → 0 over 380ms `--ease-melt`, staggered 50ms
  in reading order; a 14-letter headline completes its settle at
  250 + 13×50 + 380 = 1280ms. At the final letter's landing
  +120ms, that letter elongates scaleY 1 → 1.12 over 600ms
  `--ease-drip`, holds 90ms at full stretch, and snaps back over
  140ms `--ease-melt` — the snap is the only fast motion in the
  hero. The ceremony caps at 1800ms; headlines longer than 22
  letters compress their stagger to fit (letters are refused
  beyond 30 at build time — §12 headline law).
- **States.** Cold (JS-armed only, glow at 0, letters at −4px) →
  warming (glow rising) → settling (letters landing in order) →
  dripping (final letter) → warm rest (glow at full, letters
  home; the glow hands off to §6.12's ambient pulse). Hover/focus:
  none — the headline is not a control and never re-melts.
  Scrolled-past mid-ceremony: the ceremony completes on its own
  timeline; it is load-locked, not scroll-locked.
- **Content merge.** The headline is the hero's `<h1>` and its
  subject; the glow is centred on the headline, not the panel —
  the light source is the words themselves warming. The
  standfirst (§6.12) waits for the drip-snap before its own
  melt-in, so the hero reads as one pour, not two effects.
- **Failure fallback.** Watchdog at 1600ms: any letter not home
  snaps to rest and the glow to full; the watchdog is the
  original entry's safety rule in this theme's form — a melt is a
  transform over complete content, and interrupted warmth can
  never leave a letter floating. No JS: headline printed, glow
  present statically at full (it is a background layer, harmless
  without motion).
- **Reduced-motion variant.** No settle, no drip. The headline
  stands printed and the glow stands at full from first paint —
  the information (this panel is warm at its centre) survives;
  only the performance rests.
- **Performance budget & mobile variant.** Letters animate
  `transform` only; the glow is one radial-gradient layer,
  compositor-only. Budget: ≤0.4ms/frame during the ceremony.
  Mobile (<768px): glow diameter 300px, letter travel 3px,
  stagger 40ms, drip elongation 10% — the same beats at a
  smaller scale, none cut.
- **Choreography timeline (v2).** t=0 fonts ready (or race lost
  → printed) → t=0–1000 glow warms → t=250 first letter starts →
  50ms stagger per letter → final letter lands → +120ms elongate
  600ms → hold 90ms → snap 140ms → t≤1800 ceremony complete →
  standfirst melt-in begins (§6.12) → glow hands to ambient
  pulse at t=+2000.
- **State matrix (v2).** *Rest:* warm, printed, glow pulsing via
  §6.12. *Hover:* none. *Focus:* focus entering the hero
  completes a running ceremony instantly — a keyboard visitor
  never waits for wax. *Active:* n/a. *Scrolled-past:*
  completed. *Disabled / no-JS:* printed, glow static.
  *Touch:* identical; first touch completes a running ceremony.
- **Breakpoints (v2).** ≥1200px: 54px type, 420px glow, 4px
  travel. 768–1199px: 42px, 360px glow, 4px travel. <768px:
  33px, 300px glow, 3px travel, 40ms stagger, cap 1500ms.
- **Edge cases & failure modes (v2).** *Font swap after arming:*
  spans are wrapped only after fonts resolve; a late swap
  unwraps (spans removed, headline prints). *Tab hidden
  mid-ceremony:* rAF pauses; on return, wall-clock past 1600ms
  fires the watchdog. *CMS-edited headline:* letter spans are
  generated at runtime from the DOM text, so any edit re-wraps
  correctly — but the drip letter is always the final letter of
  the final word; an edit ending in punctuation makes the last
  *letter* drip, punctuation excluded by the wrapper.
  *Very long headline:* build-time refusal at 30 letters (§12).
- **Accessibility spec (v2).** The `<h1>` text is whole in the
  accessibility tree from first paint; letter spans are
  `aria-hidden` duplicates are *not* used — the spans wrap the
  real text and the heading's accessible name is the full string
  (spans carry no semantics). The glow layer is decorative and
  hidden from AT. Contrast never changes during the ceremony:
  `--hive` on `--wax` 13.38:1 at every frame, because the settle
  moves glyphs without fading them.
- **Tokens consumed (v2).** `--wax`, `--hive`, `--glow`,
  `--ease-melt`, `--ease-drip`, `--ease-settle`,
  `--dur-glow-warm` (1000ms), `--dur-letter-settle` (380ms),
  `--dur-letter-stagger` (50ms), `--dur-drip-letter` (600ms).

### 6.2 The filling comb (progress)

- **What & why.** A fixed side structure of 18 hexagonal cells
  fills with honey colour, cell by cell, as the visitor completes
  sections — progress stored as honey in a comb. It belongs
  because it is the theme's law made visible: the reader fills
  the comb by exploring, exactly as bees do, and a filled cell is
  a kept promise that something was gathered. It replaces the
  progress bar, which this theme refuses (§11): a bar measures
  distance; a comb stores goods.
- **Structure.** A `<nav aria-label="Your comb">` rail fixed at
  the left margin (≥1200px), holding 18 hex cells (34px across
  flats, flat-top, 2-column offset honeycomb, shared-wall gap
  3px) generated from the page's section registry — the same
  registry that builds §6.11's navigation, so cell *n* is section
  *n* by construction. Each cell is a link to its section. Fill
  is an inner hex layer (`--honey`) whose height animates 0 →
  100% inside the cell's clip; a capped cell (current section)
  gains a `--comb` lid line across its top flat. The element
  carries `role="progressbar"` semantics on a visually hidden
  companion: `aria-valuenow` is the percentage computed from the
  completion record — the second printing of the law (§1).
- **Motion spec.** Trigger: a section's completion — defined
  exactly: the section's end marker crosses the 55% viewport line
  going down, once per section per session; the record (§1) is a
  `Set` of section ids, the single source. On completion, the
  cell's fill rises over 400ms `--ease-pour` (a liquid rise: fast
  to 80%, levelling to 100%), and the *next* cell in reading
  order pulses its wall colour `--comb` → `--honey` → `--comb`
  over 600ms to say "this one is being gathered now". Scrolling
  back up never un-fills a cell: stores are not un-stored. A
  section completed while the comb is off-screen still fills;
  the fill is state, not spectacle.
- **States.** Empty (wall only, `--wax-shadow` interior) →
  gathering (next-cell pulse) → filling (400ms rise) → filled
  (honey to the brim, resting) → capped (the reader's current
  section wears the lid line; the lid moves as they move, the
  fill does not). Hover on a cell: wall deepens to `--comb-deep`,
  tooltip refused — the cell's section title appears as a stamped
  label (§3 cell label) to the rail's right. Focus: 2px
  `--comb-deep` outline offset 2px. Disabled state: none — every
  cell is always a working link.
- **Content merge.** The comb is the page's table of contents
  wearing the theme's material: its cells are the sections, its
  fills are the reader's own history, its lid is their present
  position. Remove the fiction and it is still a complete,
  working navigation instrument — that is the test every element
  here must pass.
- **Failure fallback.** No JS: all cells render filled to the
  *printed* state the original entry specifies — the comb rests
  filled to the reader's section is unknowable without JS, so the
  no-JS comb renders all cells as filled links (a complete index,
  honestly static) and the percentage companion is absent, not
  faked. Observer failure: a 3s sweep checks scroll position
  against section offsets and reconciles the record.
- **Reduced-motion variant.** Fills apply instantly (no rise);
  the next-cell pulse is replaced by a steady `--comb` wall on
  the gathering cell. The comb's information is identical; only
  the pouring rests.
- **Performance budget & mobile variant.** 18 small clipped
  layers; fills animate `transform: scaleY` on the inner layer
  (compositor-only), ≤0.2ms/frame. Below 1200px the rail is cut
  (§6.2 breakpoints) and replaced by the top strip — the mobile
  variant is a different instrument, not a shrunken rail.
- **Choreography timeline (v2).** Section end crosses 55% line →
  t=0 record adds the id → t=0–400 fill rises → t=100 the AT
  percentage updates (batched, never per-frame) → t=400 fill
  rests → t=450 next cell's wall pulse begins (600ms) → lid
  moves to the new current cell at the moment its section's
  start crosses the 45% line.
- **State matrix (v2).** *Rest:* fills as per record, lid on
  current. *Hover:* wall deepens, label stamps in. *Focus:*
  outline; focus does not fill — only reading fills. *Active:*
  link follows to the section; on arrival the lid moves, the
  fill waits for genuine completion (jumping to a section does
  not complete it — its start crossing is not its end crossing).
  *Scrolled-past:* fills persist. *Disabled:* none. *Touch:*
  cells are 44px targets via an expanded hit area (visual cell
  34px, hit area 44px, walls drawn inside the hit hex).
- **Breakpoints (v2).** ≥1200px: fixed left rail, 18 cells,
  2-column honeycomb. 768–1199px: a horizontal comb strip under
  the masthead — 18 cells in one row at 22px, fills identical,
  labels omitted (title attribute + AT only). <768px: the strip
  persists at 18px cells, sticky with the masthead, and the
  percentage companion becomes visible text ("6 of 18 cells") in
  the strip's right end — small screens get the number the rail
  keeps visual.
- **Edge cases & failure modes (v2).** *Reader jumps to the
  footer via §6.11 nav:* sections passed at speed complete only
  if their end markers genuinely crossed during the scroll —
  a programmatic jump to the bottom completes nothing except the
  final section when its end crosses; the comb honestly shows a
  sparse fill, and §6.17's tally prints the same sparse truth.
  *Short page (< 18 sections):* the registry builds exactly as
  many cells as sections; the 18 figure is this site's registry,
  not a constant — a 9-section page has a 9-cell comb. *Print:*
  the rail is hidden; the percentage prints in the footer.
- **Accessibility spec (v2).** The rail is a `<nav>` of real
  links with section-title accessible names ("The shop — 6
  cells, 2 filled" pattern per cell state via `aria-label`).
  The progressbar companion updates at most once per completion
  (never per scroll frame) and is `aria-live="off"` — progress
  is available on request, never announced uninvited. Filled vs
  empty is never colour-only: filled cells carry the lid-flat
  top edge geometry and a 2px inner wall weight difference.
  Contrast: `--hive` labels on `--wax` 13.38:1; the honey fill
  itself carries no text, ever (§2).
- **Tokens consumed (v2).** `--wax`, `--wax-shadow`, `--honey`,
  `--comb`, `--comb-deep`, `--ease-pour`, `--dur-cell-fill`
  (400ms), `--cell-size` (34px), `--rail-width` (64px).

### 6.3 Pricing drips

- **What & why.** Five to seven wax drips hang from the pricing
  section's top edge, lengthening as the section approaches —
  the candles' own wax melting over the offers it belongs to. It
  belongs because pricing in a candleworks is where the product's
  cost becomes literal: every candle sold is wax that will drip,
  and the section's decoration is its merchandise behaving. The
  drips are not a border; they are the stock, overhead.
- **Structure.** An SVG strip spanning the pricing section's top
  edge, 64px tall, holding 5–7 drip paths (one per pricing card
  column position — drips are anchored to cards, not scattered:
  each drip hangs centred over a card's left third). Each drip is
  a single path (rounded stem, bulb tip) filled `--wax` with a
  `--wax-shadow` right edge, `transform-origin` at its top anchor,
  elongated by `scaleY`. The strip is `aria-hidden`,
  `pointer-events: none`, and sits in the section's reserved top
  band (§4) so it can never overlap the title.
- **Motion spec.** Scrubbed, continuous: each drip's scaleY runs
  0.3 → 1.0 across the scroll span from the section's top being
  90% of a viewport below the fold to its top reaching 30% of the
  viewport — the approach, not the reading. Drips differ by phase:
  drip *i* begins its span offset by *i* × 6% of the total span
  and its full length differs (0.82–1.0 of the 64px band, authored
  per drip in the SVG), so the row never moves in lockstep.
  Values are driven by the shared loop (lerp 0.12); scrolling
  back up shortens the drips symmetrically — wax re-forms, the
  one reversible melt on the page, because nothing has been
  spent yet: the offers are still overhead, unlit.
- **States.** Rest (section far below): scaleY 0.3, stubby.
  Approaching: elongating per the scrub. Arrived (section top
  above the 30% line): full authored length, resting; the drips
  then hold for the whole section — they do not keep growing
  while prices are read. Scrolled-past: hold. Hover/focus: none.
- **Content merge.** Each drip is anchored to a pricing card and
  shares its column; the longest drip hangs over the
  best-value card (authored, and §12 requires the copy to know
  why: the club candle burns longest). The drips' wax is the
  section's own material arriving from the section above — the
  making section's candles, conceptually, melt into pricing.
- **Failure fallback.** No JS / loop failure: drips render at
  scaleY 0.65 statically — mid-length, decorative-plausible, and
  the section reads identically. The strip is pure ornament with
  zero content, so its failure mode is allowed to be merely
  static; nothing else on the page may use this excuse (§10
  gate 6 checks the strip is the only purely decorative
  animated element besides §6.12's glow).
- **Reduced-motion variant.** Drips render at full authored
  length, static. The information (wax hangs over these offers)
  is spatial, not temporal, and survives whole.
- **Performance budget & mobile variant.** 5–7 SVG paths,
  `transform` only, ≤0.15ms/frame. Mobile (<768px): 4 drips (one
  per visible card column pair), band height 48px, same scrub
  span compressed to the section's approach on a short screen.
- **Choreography timeline (v2).** Continuous scrub, no discrete
  beats: section top at 90% vh below fold → all drips 0.3 →
  per-drip phase offsets engage → section top at 30% vh → drips
  at authored lengths → hold through the section → (reverse on
  scroll-up, symmetric).
- **State matrix (v2).** *Rest:* 0.3 or full per scroll position.
  *Hover/focus:* none (non-interactive). *Active:* n/a.
  *Scrolled-past:* full length, held. *Disabled / no-JS:* 0.65
  static. *Touch:* identical scrub; no touch-specific behaviour.
- **Breakpoints (v2).** ≥1200px: 7 drips, 64px band. 768–1199px:
  5 drips, 56px band. <768px: 4 drips, 48px band, phase offset
  8% (shorter screens need the stagger spread wider to read).
- **Edge cases & failure modes (v2).** *Pricing section is the
  first section (landing-page variant):* the scrub span has no
  approach; drips ship at full length and the element degrades
  to a static fringe — §7's landing map states this ruling.
  *Very fast scroll:* the lerp smooths; drips may lag the span
  by up to ~200ms of travel and settle — acceptable, wax lags.
  *Cards reflow (filter/sort):* drip anchors are column
  positions, not card ids; a re-sorted grid keeps its drips.
- **Accessibility spec (v2).** Fully decorative: `aria-hidden`,
  no text, no state conveyed. It must never be the only signal
  of the section's identity — the section title does that work.
  Motion is scrub-bound (no autonomous movement), so vestibular
  risk is limited to the reader's own scroll speed.
- **Tokens consumed (v2).** `--wax`, `--wax-shadow`, `--hive`
  (section ground edge), `--drip-band` (64px), `--scrub-lerp`
  (0.12).


### 6.4 The pinned drip

- **What & why.** In the candle-making section, the page pins for
  ~120vh while one drip forms at a wick point, stretches to three
  times its length, necks, and falls as a droplet that splashes
  into a small wax pool — the making process performed in scrub
  time beside the copy that narrates it. It belongs because this
  is the theme's one pinned scene (§5 rations pins to one) and it
  spends that ration on the site's central act: a candle is made
  by exactly this, wax leaving a height and landing as a pool.
  The visitor's scroll is the pour; their pace is the drip's
  physics.
- **Structure.** A pinned stage (200vh of scroll room, 120vh of
  pinned travel at ≥1200px) on a `--hive` ground — the making
  room is the page's dark room, lit by the work. Left: the copy
  column (three short paragraphs, one per phase, crossfading by
  phase). Right: the drip stage — an SVG scene 480px tall: a
  candle silhouette at top with a wick point, the drip path
  beneath it, and the pool ellipse at the base on a `--propolis`
  bench line. The drip is one path whose `d` is interpolated
  between four authored keyframes (form / stretch / neck / fall)
  by the shared loop; the droplet is a separate small path shown
  only in the fall phase; the splash is three short stroke arcs
  in the pool, drawn at landing.
- **Motion spec.** Pure scrub, phase-mapped to pinned progress
  *p* (lerp 0.12): *p* 0–0.3 **form** — a bead swells at the wick
  point, scale 0 → 1, copy paragraph 1 rules. *p* 0.3–0.65
  **stretch** — the drip elongates to 3× its formed length,
  width narrowing 15% as it stretches (volume is conserved on
  screen as in wax), `--ease-drip` shaping within the scrub.
  *p* 0.65–0.8 **neck** — the stem thins to 30% width at the
  neck point, the bulb below swelling 8%. *p* 0.8–0.9 **fall** —
  the droplet detaches and drops the remaining distance in the
  scrub's fastest 10% (gravity does not do slow). *p* 0.9–1.0
  **splash & rest** — splash arcs draw (120ms `--ease-draw` at
  the moment *p* crosses 0.9, the section's only time-based
  beat), the pool ellipse widens 12%, copy paragraph 3 lands.
  Scrolling back up reverses every phase symmetrically — the
  visitor can un-pour, because the candle is not yet lit; this
  reversibility is stated in §12's voice as a feature ("scroll
  back: the wax climbs home").
- **States.** Before pin: scene at *p*=0, bead unformed, first
  paragraph lit. In pin: phases as above; the copy column's
  active paragraph is full `--wax`, the others at 45% — on the
  dark ground, dimming is opacity of the *inactive* copy only,
  and the active paragraph is never below 13.38:1's source
  colour. After pin: the pool rests with its splash, scene
  printed complete. Hover/focus: none. The pin releases exactly
  at *p*=1; there is no skip button — the exit is 120vh of
  scroll, signposted by §6.2's lid resting on the making cell.
- **Content merge.** The three paragraphs are the process steps
  (warm / pour / set) and each phase *is* its paragraph's claim
  performed: when the copy says the wax necks before it falls,
  the neck is on screen at that scroll position. Remove the
  animation and the section is a static three-step explanation
  with a printed drip scene (fallback) — remove the copy and the
  scene is a screensaver; the element is the two together.
- **Failure fallback.** No JS / no pin support: the stage renders
  unpinned as a tall scene with the drip at its stretched
  keyframe and all three paragraphs at full contrast in order —
  the explanation complete, the performance absent. Loop stall:
  a watchdog compares pinned progress to scroll position every
  500ms during the pin and snaps the keyframe interpolation to
  the true *p* if they diverge by >0.05.
- **Reduced-motion variant.** No pin. The scene prints at the
  stretch keyframe between the three paragraphs in normal flow —
  the original entry's safety rule (reduced motion: no drips in
  motion) applied to the theme's biggest drip: it may be *shown*,
  it may not *fall*.
- **Performance budget & mobile variant.** One path interpolation
  (4 keyframes, ≤40 path points) + opacity crossfades, ≤0.5ms/
  frame — the page's most expensive element, and §14's cut order
  protects it last among scrubbed elements because it is the
  theme's signature. Mobile (<768px): pin travel 80vh, scene
  360px tall, copy stacked above the stage (paragraphs become
  captions under the scene, crossfading in place).
- **Choreography timeline (v2).** Pin engages → *p* 0–0.3 bead
  forms, ¶1 lit → 0.3 ¶2 begins crossfade (200ms of scroll-travel
  equivalent) → 0.3–0.65 stretch to 3× → 0.65–0.8 neck to 30% →
  0.8 ¶3 crossfade → 0.8–0.9 droplet falls → 0.9 splash draws
  120ms, pool +12% → 0.9–1.0 rest → pin releases.
- **State matrix (v2).** *Rest (pre-pin):* unformed, ¶1 lit.
  *Hover/focus:* none; keyboard focus entering the section moves
  to the copy column and the pin behaves identically (scroll is
  scroll). *Active:* n/a. *Scrolled-past:* completed scene,
  pool printed. *Disabled / no-JS:* static stretch scene, all
  copy full contrast. *Touch:* identical scrub; touch scroll
  through 120vh is the intended gesture, and the phase mapping
  is velocity-independent (position, not momentum).
- **Breakpoints (v2).** ≥1200px: 120vh pin travel, side-by-side
  copy/stage. 768–1199px: 100vh pin, stage 420px, copy column
  narrows to 38%. <768px: 80vh pin, stacked layout, scene 360px.
- **Edge cases & failure modes (v2).** *Reader flings through:*
  phases compress in time but never skip — the fall still takes
  its 10% of travel, so a fast reader sees a fast drip, not a
  teleport. *Reader stops mid-neck for a minute:* the scene
  holds, perfectly still — a held drip is physically true and
  the theme would rather be still than idle-animate (§9 failure
  8). *Resize mid-pin:* keyframes are in viewBox units; the
  interpolation is resolution-independent and survives resize
  without a jump. *Browser without sticky:* fallback engages
  (static scene).
- **Accessibility spec (v2).** The scene is `role="img"` with an
  `aria-label` that names the whole process once ("A drip of wax
  forms at the wick, stretches, necks and falls into a pool as
  you scroll") — AT users get the three paragraphs, which carry
  the full content in text; the scene adds nothing the text
  lacks. Inactive-paragraph dimming never applies to the
  paragraph currently being read by a screen reader: dimming is
  visual only, all three paragraphs are full DOM text.
  Focus order: copy column links (if any) in DOM order; the pin
  traps nothing.
- **Tokens consumed (v2).** `--hive`, `--wax`, `--propolis`,
  `--honey` (pool highlight), `--ease-drip`, `--ease-draw`,
  `--pin-travel` (120vh), `--scrub-lerp` (0.12).

### 6.5 Hex-mask image reveals

- **What & why.** Section images are revealed by a hexagonal cell
  mask that expands cell by cell — centre-out, ring by ring — as
  the image enters: photographs are stored in comb, and the image
  literally occupies cells of the hive as it arrives. It belongs
  because it makes the layout signature (§4) do the revealing:
  the mask is not an effect laid over the image, it is the grid
  the whole page is built from, claiming the photograph cell by
  cell.
- **Structure.** Each masked image sits in a hex-grid mask layer:
  an SVG `<clipPath>` (or CSS `clip-path` composite on the
  wrapper) tiled with the grid-cell hexagon at the section's
  register size, cells grouped into concentric rings from the
  image's focal cell (authored per image via `data-focal="x,y"`
  in cell coordinates — the photograph's subject decides the
  centre, not the geometry's). Beneath the mask, the image at its
  final scale from first paint. Ring count is computed from the
  tile: a 3×2 grid-cell image carries 3 rings.
- **Motion spec.** Trigger: image enters at 25% visibility. Rings
  open outward at 60ms per ring, each ring's cells fading their
  clip in over 120ms `--ease-settle` (cells within a ring are
  simultaneous — the ring is the beat). A 3-ring image completes
  in ~300ms; the largest licensed image (5 rings) in ~420ms.
  Once only per image per session. The reveal is a mask
  expansion over a fully rendered image — at no frame is any
  part of the photograph *absent*, it is only ever *covered by
  wax-toned cells* that match the ground, so a stalled reveal
  reads as a partly-stored photograph, never a broken one.
- **States.** Stored (all cells closed; image covered by
  ground-coloured cells — the image's own `<img>` is loaded and
  present beneath) → opening (rings expanding) → stored-open
  (mask fully open, mask layer retired from the compositor).
  Hover/focus: none. Scrolled-past unopened (fling): opens
  instantly on the next frame the image is ≥25% visible.
- **Content merge.** The mask's cells are the same geometry, at
  the same size, as the shop grid's frames (§6.13) and the
  diagram's cells (§6.7): the visitor learns one comb and meets
  it everywhere. Alt text and captions are unaffected — the
  caption sits outside the mask and melts in with the section.
- **Failure fallback.** Watchdog at 900ms from trigger: mask
  snaps fully open. No JS: no mask is applied at all (the mask
  layer is JS-inserted; the shipped DOM is a plain framed
  photograph). Image fails to load: the mask never arms, and the
  frame shows its `--wax-shadow` interior with the alt text as a
  caption — an empty cell, honestly labelled (§6.18's grammar).
- **Reduced-motion variant.** No expansion. Images are simply
  present, framed. The comb claim is carried by the frame
  geometry alone.
- **Performance budget & mobile variant.** Clip-path composites
  on one wrapper per image, ≤4 masked images per page (budget,
  §14); ≤0.4ms/frame during a reveal. Mobile: ring size grows
  (fewer, larger cells — 2 rings typical), 70ms per ring; total
  beat unchanged in feel, cheaper in layers.
- **Choreography timeline (v2).** Image at 25% visibility →
  t=0 focal ring opens (120ms) → +60ms ring 2 → +60ms per ring →
  final ring → mask layer retired at +200ms → caption melt-in
  (already running with the section, §5) completes independently.
- **State matrix (v2).** *Rest:* open (post-reveal) or stored
  (pre-trigger). *Hover/focus:* focus on a link wrapping the
  image opens the mask instantly if unopened — a keyboard
  visitor is never shown a covered photograph. *Active:* n/a.
  *Scrolled-past:* open. *Disabled / no-JS:* no mask, image
  present. *Touch:* identical triggers.
- **Breakpoints (v2).** ≥1200px: grid-cell rings as authored.
  768–1199px: same geometry, images narrower so rings reduce
  naturally. <768px: ring cell size ×1.4, 70ms/ring.
- **Edge cases & failure modes (v2).** *Image taller than the
  viewport:* trigger threshold switches to "top edge crosses
  60% line" so the reveal isn't withheld from a long photograph.
  *Lazy-loaded image arrives after trigger:* the reveal waits
  for the `load` event, raced at 1200ms — after which the mask
  opens anyway over whatever is there (frame + alt), never
  holding a frame hostage to a slow network. *Focal cell
  outside the tile (bad data):* clamped to the nearest in-tile
  cell at build.
- **Accessibility spec (v2).** The mask is presentational; the
  `<img>` and its alt are untouched in the accessibility tree
  from first paint. No information is gated on the reveal.
  Covered cells are ground-coloured, so low-vision users see a
  photograph arriving, never flashing or strobing (cell fades
  are 120ms opacity, no luminance jumps above the WCAG flash
  thresholds).
- **Tokens consumed (v2).** `--wax-shadow`, `--ease-settle`,
  `--dur-ring` (60ms), `--grid-cell` (section register size),
  `--mask-max` (4 per page).

### 6.6 Migrating light pools

- **What & why.** In the shop grid, a soft warm radial glow —
  candlelight, ~260px across — drifts slowly between products on
  a 9-second loop, brightening each product's wax frame as it
  passes; when the visitor's pointer enters the grid, the pool
  gathers under it. It belongs because it is the warmth law (§1)
  as an ambient system: light in a candleworks moves because
  flames are carried, and the pool warms only what it touches —
  products in view, under a real pointer. It is one of the
  page's two licensed ambient loops (§5), and it earns the
  licence by being *about* the merchandise.
- **Structure.** One `--glow` radial layer (260px, blur-free —
  a radial gradient with a 60% falloff) absolutely positioned
  inside the shop grid's wrapper, `pointer-events: none`,
  `aria-hidden`, z-order below card frames but above the ground,
  so it reads as light *on the ground between frames* that rims
  each frame it nears. Its drift path is authored as anchor
  points at product-frame corners (derived from the grid's DOM
  at build: the pool visits frames, it does not wander free).
  Frame brightening is a per-frame `--warm` custom property the
  pool's proximity writes through the shared loop, consumed by
  §6.9's frame tint.
- **Motion spec.** Drift: the pool's target anchor advances every
  9000ms (one full visit cycle per product in grids of ≤6; in
  larger grids the cycle is 9000ms per *leg* and the path is a
  closed loop through all anchors). Movement between anchors is
  lerped in the shared loop at 0.10 (warmth's lag) — a leg takes
  ~2.5s of visible travel, then the pool rests at the anchor,
  breathing ±4% alpha on a 4s sine. Gather: on pointerenter of
  the grid, the pool's target becomes the pointer (tracked at
  pointermove, throttled to the loop's frames); on pointerleave
  it returns to its interrupted anchor and resumes the cycle —
  the flame is borrowed, then given back. The pool runs only
  while the grid is ≥30% in view (IntersectionObserver gates the
  loop's registration); off-screen, it freezes mid-leg.
- **States.** Drifting (autonomous loop) → gathered (pointer
  present) → returning (pointer left, travelling back to anchor)
  → resting-at-anchor (breathing). Hover on a single card: the
  pool is the grid's, not the card's — card hover states (§6.13)
  do not summon it; only grid-level pointer presence does, so
  the light never feels like a cursor spotlight (§9 failure 7).
  Focus: keyboard focus entering the grid parks the pool at the
  focused card's anchor — focus is a form of presence, and the
  warmth law honours it.
- **Content merge.** The pool's path is the product list; its
  brightening is §6.9's frame warmth driven by proximity instead
  of scroll. A visitor watching the grid learns the range in the
  pool's order — the drift sequence is the merchandising order,
  authored, not random.
- **Failure fallback.** Loop or observer failure: the pool parks
  at the first anchor at 60% alpha — a static warm patch over
  the first product, plausible and harmless. No JS: no pool
  element exists; frames rest at their printed tone (§6.9's
  fallback), and nothing is missing because the pool carries no
  content.
- **Reduced-motion variant.** No drift, no gather. The pool is
  absent entirely — reduced motion in this theme means the
  candle is not carried; frames keep §6.9's scroll warmth, which
  is reader-driven. (A static pool was considered and refused:
  unmoving light with no source reads as a stain.)
- **Performance budget & mobile variant.** One gradient layer +
  per-frame custom-property writes for ≤12 frames, ≤0.3ms/frame.
  Mobile (<768px): the pool is cut — a 260px glow on a 360px
  screen is a floodlight, and touch has no hover to gather it.
  The cut is §14's first ambient sacrifice and is stated here so
  no builder "optimises" it back in.
- **Choreography timeline (v2).** Grid ≥30% visible → pool fades
  in 600ms at its first anchor → leg travel ~2.5s → rest +
  breathe (4s sine) → next anchor at 9000ms cycle → (pointer
  enters) target switches within one frame, gather travel per
  distance at lerp 0.10 → (pointer leaves) return leg → cycle
  resumes from the interrupted anchor, not the start.
- **State matrix (v2).** *Rest:* drifting or parked per view.
  *Hover (grid):* gathered. *Focus:* parked at focused card.
  *Active:* pointerdown does not change the pool (it is light,
  not a control). *Scrolled-past:* frozen off-screen, resumes on
  return. *Disabled / no-JS:* absent. *Touch:* no pool (cut).
- **Breakpoints (v2).** ≥1200px: 260px pool, full drift + gather.
  768–1199px: 220px pool, drift only (gather disabled — pointer
  precision on tablets is a maybe, and a hesitant pool is worse
  than a steady one). <768px: cut.
- **Edge cases & failure modes (v2).** *Grid filtered to fewer
  products:* anchors rebuild from the live DOM; the pool's path
  never targets a removed frame. *Pointer races across the
  grid:* the lerp caps the pool's speed — it trails behind a
  fast pointer like carried light, never teleporting; if the
  pointer exits mid-chase, the return leg starts from wherever
  the pool actually is. *Two grids on one page:* each grid gets
  its own pool only if §14's budget allows; the second grid
  ships pool-less rather than halving the frame budget.
- **Accessibility spec (v2).** Purely decorative and hidden from
  AT; it conveys no state (a product is not "selected" by being
  lit — §6.8's seal does selection, accessibly). Alpha and
  radius are capped so the pool never reduces text contrast
  below the printed ratios: it renders *below* frames and text,
  and §6.9's warmth tint is checked against the same ratios.
- **Tokens consumed (v2).** `--glow`, `--honey`, `--warm-lerp`
  (0.10), `--pool-size` (260px), `--dur-pool-cycle` (9000ms).


### 6.7 The comb diagram

- **What & why.** In the science-of-wax section, an SVG
  cross-section of comb — cell walls, capped and uncapped cells,
  a honey gradient at the base — strokes its walls in over ~1.6s
  as it arrives: the labelled anatomy the adjacent text explains,
  drawn wall by wall. It belongs because the science section's
  claim is structural (why hexagons, why capping, what an evening
  of burn is), and a diagram that assembles itself teaches the
  structure in the order the text teaches it: walls first, then
  stores, then the cap.
- **Structure.** One inline SVG (~520×360 viewBox at desktop): a
  7×4 cell field in cross-section, wall paths as a single stroked
  path group in `--comb`, three capped cells whose caps are
  filled paths in `--wax-shadow`, two open cells showing a
  `--honey` gradient fill (bottom-third), and four leader lines
  (`--ease-draw` strokes) to labels in Work Sans data type set in
  HTML beside the SVG (labels are text, never SVG text — they
  must wrap, translate and be read by AT). The wall group is
  drawn by `stroke-dashoffset`; caps and fills fade-settle after
  their walls.
- **Motion spec.** Trigger: diagram at 35% visibility, once per
  session. Walls draw over 1600ms `--ease-draw`, sequenced as
  three sub-beats: outer frame walls (0–500ms), inner cell walls
  in reading order (300–1300ms, overlapping the frame's tail),
  then caps settle (1200–1500ms, `--ease-pour` opacity + 2px
  drop) and honey fills rise in the two open cells (1300–1600ms,
  `--ease-pour`). Leader lines draw with their labels' melt-in
  as each label's referent completes. The draw is the section's
  spectacle and is sequenced *before* the section's hex-masked
  photograph (§6.5) if both are present — diagram first, photo
  after, per §4's one-spectacle rule; the photo's trigger waits
  for the draw's completion + 200ms.
- **States.** Undrawn (JS-armed only: dashoffset at full length,
  caps/fills at 0) → drawing (sub-beats above) → drawn (rest;
  dash retired). Hover on a label: its leader line thickens 1px
  → 1.75px and its cell wall group warms to `--comb-deep` —
  the diagram answers questions. Focus on a label (labels are
  list items, focusable as a group via the section's "anatomy"
  list): same response. Scrolled-past mid-draw: the draw
  completes on its own clock (it is 1.6s; the reader who flung
  past returns to a drawn diagram).
- **Content merge.** Every label names a part the adjacent
  paragraphs discuss, in the paragraphs' order; the paragraph
  about capping sits beside the capped cells. The diagram is the
  section's second author, not its illustration: §12 requires
  the science copy to reference the diagram's parts by name
  ("the cap, top right, is the lid §6.2 wears").
- **Failure fallback.** No JS: the SVG ships fully drawn (dash
  offsets are JS-armed; the printed state is the drawn state).
  Watchdog at 2200ms from trigger snaps any remaining dash to
  drawn and caps/fills to full. A browser without SVG stroke
  animation support still receives the static drawn diagram —
  the technique degrades to the fallback by construction.
- **Reduced-motion variant.** The diagram stands drawn. Labels
  and leaders printed. Nothing about the science is temporal.
- **Performance budget & mobile variant.** One SVG, dash
  animation on ≤6 path groups, ≤0.3ms/frame during the draw.
  Mobile: the field reduces to 5×3 cells (the two outer columns
  are the same lesson at lower resolution — the SVG ships both
  fields and CSS selects), draw compresses to 1200ms, labels
  stack beneath as a numbered list matching leader numbers.
- **Choreography timeline (v2).** 35% visible → t=0 frame walls
  → t=300 inner walls begin → t=1200 caps settle → t=1300 fills
  rise → t=1600 drawn → t=1800 §6.5 photograph (if present) may
  trigger → labels' leaders complete with their referents
  throughout.
- **State matrix (v2).** *Rest:* drawn. *Hover (label):* leader
  thickens, wall warms. *Focus:* same as hover. *Active:* n/a.
  *Scrolled-past:* drawn. *Disabled / no-JS:* drawn at first
  paint. *Touch:* tap on a label gives the hover response for
  1200ms (touch has no hover; the diagram still answers).
- **Breakpoints (v2).** ≥1200px: 7×4 field, side labels.
  768–1199px: 7×4 field, labels beneath in two columns.
  <768px: 5×3 field, numbered leaders, labels as a list.
- **Edge cases & failure modes (v2).** *Section revisited in a
  later session:* `sessionStorage` marks the draw done; the
  diagram stands drawn — science does not re-teach itself.
  *Print:* drawn state prints (the print stylesheet forces the
  fallback). *Label text edited longer:* HTML labels wrap
  freely; leader endpoints are anchored to cell coordinates,
  not label boxes, so copy edits never misalign the diagram.
- **Accessibility spec (v2).** The SVG is `role="img"` with a
  full `aria-label` describing the cross-section in one sentence
  plus the four labelled parts; the HTML label list is the
  accessible primary — each label is a real list item with its
  explanation, so the diagram's entire content exists as text.
  Contrast: walls `--comb` on `--wax` are graphical (2.93:1,
  licensed for diagram strokes ≥2px effective weight at drawn
  size — stated here because §2 forbids `--comb` text, not
  strokes); label text is `--hive`/`--propolis` at full ratios.
- **Tokens consumed (v2).** `--comb`, `--comb-deep`,
  `--wax-shadow`, `--honey`, `--ease-draw`, `--ease-pour`,
  `--dur-diagram` (1600ms).

### 6.8 The wax-seal click (capping a cell)

- **What & why.** Clicking a product card caps its cell: a small
  hex seal dot fills in the card's corner with deep-comb colour
  under a thin "SEALED" ring, and the product joins the "your
  comb" list in the shop section's header. Selection as capping —
  the visitor stores products the way bees store honey, in the
  comb itself. It belongs because it is the shop's one committing
  gesture, and the theme gives commitment a material: a capped
  cell is closed, kept, and counted.
- **Structure.** Each product card (§6.13) carries a real
  `<button class="cap-toggle" aria-pressed="false">` occupying
  the card's corner cell — a 44px hex hit area containing the
  visual seal: an SVG hex (22px) whose interior is a `--seal`
  fill layer (scaleY rise inside the hex clip) and whose ring is
  a stroked hex that completes as the fill lands. The button's
  accessible name is "Cap the [product] cell" / "Uncap…". The
  "your comb" list is a live region in the section header: a row
  of mini hex cells (one per capped product, in capping order)
  plus a text tally ("Your comb: 3 cells capped") — the shop's
  printing of the same stored-state the footer (§6.17) totals.
- **Motion spec.** Trigger: click/tap/Enter/Space on the corner
  button. The fill rises over 450ms `--ease-pour`; at t=300ms
  the ring stroke draws its final sixth and the seal gives a 2px
  settle (`--ease-melt`, the press of a thumb); at t=450ms the
  mini cell appears in the header list with its own 300ms fill,
  and the tally increments. Uncapping reverses: fill drains over
  300ms `--ease-settle` (wax is scraped off faster than it was
  laid), ring breaks at its top flat, mini cell empties and is
  removed after its drain. Capping is capped: the comb holds at
  most 12 products (a frame of comb, stated in copy); the 13th
  cap attempt shakes nothing — the button explains itself via
  the tally line's text change ("Your comb is full — 12 cells")
  for 3s.
- **States.** Uncapped (empty hex, wall `--wax-shadow`) → capping
  (450ms) → capped (filled, ring closed, `aria-pressed="true"`)
  → uncapping (300ms) → uncapped. Hover on the button: the empty
  hex warms `--wax-shadow` → `--honey` at 40% (a promise, not a
  fill). Focus: 2px `--comb-deep` outline on the hex. Disabled:
  only in the comb-full state for *uncapped* cards, and disabled
  here means `aria-disabled` with the reason in the tally — the
  button stays focusable so the reason is reachable.
- **Content merge.** The seal sits in the card's own corner cell —
  the card is a cell of the shop comb (§6.13), and capping marks
  the cell, not a cart icon in a distant header. The header list
  is inside the shop section, so the visitor's comb grows where
  they are standing. §6.14's order form reads this same stored
  list as its starting contents: cap three candles here, and the
  form below opens with those three lines already entered.
- **Failure fallback.** No JS: the button is a plain toggle that
  submits as a checkbox-equivalent in the order form's fieldset
  (the cards and form share a `<form>` in the no-JS build path —
  selection degrades to ordinary form semantics, never to
  nothing). State persists in `sessionStorage` only; a storage
  failure leaves the session's caps in memory and the tally
  honest for the visit.
- **Reduced-motion variant.** Fill and drain apply instantly;
  the settle press is cut. `aria-pressed` and the tally carry
  the state identically.
- **Performance budget & mobile variant.** Per-card: one clipped
  fill + one stroke, ≤0.15ms/frame during a cap. Mobile: the
  corner hit area grows to 48px and the visual seal to 26px —
  thumbs cap cells too. The header mini-cell row wraps to two
  rows maximum, then scrolls horizontally inside the header —
  it never pushes the grid down mid-shop.
- **Choreography timeline (v2).** Click → t=0 fill begins →
  t=300 ring closes + 2px press → t=450 fill rests → t=450
  header mini cell starts its 300ms fill → t=750 tally text
  updates (after the visual, so eyes and numbers agree) →
  §6.14's form lines sync silently in the background.
- **State matrix (v2).** *Rest:* capped or uncapped as stored.
  *Hover:* empty hex warms 40%. *Focus:* outline; focus never
  caps. *Active:* the press beat (t=300). *Scrolled-past:*
  state persists off-screen. *Disabled:* comb-full state as
  above. *Touch:* tap caps; no hover promise state.
- **Breakpoints (v2).** ≥1200px: 44px hit / 22px seal, header
  list right-aligned in the section header. 768–1199px: same
  sizes, header list wraps under the section title. <768px:
  48px hit / 26px seal, header list is a sticky mini-comb strip
  at the grid's top while the shop section is in view.
- **Edge cases & failure modes (v2).** *Product sold out:* its
  card (§6.13) shows the empty-cell state and its cap button is
  removed from the DOM — you cannot cap a cell with nothing in
  it; the tally never counts intentions. *Rapid toggling:* the
  fill/drain animations are interruptible and reverse from
  their current value (no queue); `aria-pressed` flips at click,
  not at animation end — state is instant, only wax is slow.
  *Comb-full then uncap:* the disabled reason clears on the
  uncap's drain completion.
- **Accessibility spec (v2).** A real button with `aria-pressed`
  and a product-naming label; the tally is `aria-live="polite"`
  but updates are batched to the t=750 beat so rapid capping
  announces once. The seal is never colour-only: capped cells
  carry the closed ring geometry and the header list names each
  capped product as text. Hit area 44px (48px mobile) meets
  target minimums inside a hex, measured on the inscribed
  circle.
- **Tokens consumed (v2).** `--seal`, `--comb`, `--comb-deep`,
  `--wax-shadow`, `--honey`, `--ease-pour`, `--ease-melt`,
  `--ease-settle`, `--dur-seal` (450ms), `--comb-max` (12).

### 6.9 Warming image frames

- **What & why.** Product images sit in translucent wax frames;
  as each image centres in the viewport, its frame's colour
  temperature warms — pale wax toward honey tint — and the image
  scales 1.05 → 1.0, settling as it arrives at the reader's
  attention. It belongs because it is the warmth law at the level
  of a single photograph: proximity is warmth, and the frame —
  candle wax around the product — is the thing that would
  actually warm. It is also the theme's image treatment (§5):
  images resolve by tone and scale, never by blur.
- **Structure.** Each framed image: a wrapper with the hex-cut
  wax frame (a `--wax` panel border, 10–14px, with a `--glow`
  tint layer whose alpha is the frame's `--warm` property), the
  `<img>` inside at scale 1.05 (transform-origin centre), and the
  caption beneath in the panel register (§3 law 5). `--warm` is
  written by the shared loop from the image's distance to the
  viewport centre; the tint is a `color-mix` of `--wax` toward
  `--honey` at `--warm × 22%` — a tint, never a wash: at maximum
  warmth the frame is still 78% wax.
- **Motion spec.** Pure scrub. `--warm` runs 0 → 1 across the
  span where the image's centre travels from 75% viewport height
  to 50% (the reading centre), holds 1 while the centre is
  between 50% and 40%, and returns to 0 by 25% — warmth is a
  visit, not a medal; an image scrolled past cools. Image scale
  maps to the same value: 1.05 at `--warm` 0 → 1.0 at 1, so the
  photograph settles exactly as its frame warms — one gesture,
  two materials. §6.6's pool adds its proximity to the same
  `--warm` (pool contribution capped at +0.3, and the two
  contributions sum-clamp at 1): a product can be warmed by
  being read *or* by the light passing, and the frame cannot
  tell the difference, which is the point.
- **States.** Cool (frame `--wax`, image 1.05) → warming
  (scrub) → warm (frame tinted, image settled at 1.0) → cooling
  (scroll-past, symmetric). Hover: no additional warmth — hover
  is §6.13's tilt and §6.8's promise; stacking a third response
  on one card is §9 failure 10. Focus-within (card focused): the
  frame warms to a steady 0.6 regardless of scroll position —
  keyboard attention is attention, and the law honours it.
- **Content merge.** The frame is the product's packaging in the
  fiction — candles ship in waxed paper — and its warming is the
  shop's lighting responding to the reader. The caption's data
  (name, evenings, price) is outside the tint layer and never
  tinted: records don't warm (§3 law 1).
- **Failure fallback.** No JS: frames rest at `--warm` 0.35
  printed (a gentle permanent tint, mid-visit) and images at
  scale 1.0 — the printed page looks like a photograph of the
  shop at mid-afternoon, which is exactly the intent. Loop
  failure mid-scroll: frames freeze at their last `--warm` —
  always a plausible state, never a broken one.
- **Reduced-motion variant.** Frames rest at the printed 0.35
  tint; images at 1.0. Scroll-driven tone change is motion, and
  it rests.
- **Performance budget & mobile variant.** `--warm` writes are
  one custom property per visible frame (≤6 concurrently),
  compositor-friendly tint via a pre-rendered gradient layer's
  opacity (not a live `color-mix` repaint — the mix is baked
  into the tint layer, opacity carries the value). ≤0.25ms/
  frame. Mobile: warmth span compresses (centre band 65%→45%),
  scale range 1.03 → 1.0 — smaller screens, smaller gestures.
- **Choreography timeline (v2).** Continuous scrub, no discrete
  beats: image centre at 75% vh → `--warm` 0 → 50% vh → 1.0,
  scale 1.0 → holds through the 50–40% band → 25% vh → back to
  0. Pool proximity adds ≤+0.3 on its own timeline (§6.6).
- **State matrix (v2).** *Rest:* per scroll position. *Hover:*
  none (deliberately). *Focus:* steady 0.6. *Active:* n/a.
  *Scrolled-past:* cooled to 0. *Disabled / no-JS:* printed
  0.35. *Touch:* identical scrub.
- **Breakpoints (v2).** ≥1200px: spans as specified, frame
  14px. 768–1199px: frame 12px. <768px: frame 10px, compressed
  span, scale 1.03.
- **Edge cases & failure modes (v2).** *Image fails to load:*
  the frame still warms (the frame is real even when its
  photograph is not) around the alt-text cell — warmth does not
  pretend the photo arrived. *Very tall image:* `--warm` maps
  to the image's *visible centre*, computed from the visible
  rect, not the element box. *Dark mode:* the tint layer's
  alpha rises 1.25× (lamplight warms more visibly, §2) but the
  22% mix cap is unchanged.
- **Accessibility spec (v2).** Presentational: warmth conveys no
  state, no price, no availability. The tint layer never
  overlays the image's pixels or the caption, so no contrast
  ratio in the card ever changes — the frame's own tint has no
  text on it. Alt text unaffected.
- **Tokens consumed (v2).** `--wax`, `--honey`, `--glow`,
  `--warm` (per-frame property), `--warm-lerp` (0.10),
  `--frame-width` (14px).


### 6.10 The drip-curtain transition

- **What & why.** On navigation, nine wax drips elongate from the
  top edge at staggered rates, meet, and wipe the page to the
  next in ~700ms: leaving is a wax event, not a UI fade. It
  belongs because a site made of wax should change pages the way
  wax moves — downward, under gravity, all at once and never
  quite evenly. It is also rationed to the point of severity:
  route changes only, never in-page anchors, never on filter or
  sort — a curtain that falls ten times a visit is a tic, not a
  material (§9 failure 12).
- **Structure.** A fixed overlay (top of the z-order,
  `pointer-events: none` except during its 700ms when it blocks
  input deliberately) holding an SVG of 9 drip paths across the
  viewport width, each anchored at the top edge with authored
  lengths and phases, filled `--wax` over a `--wax-shadow`
  underlayer 6px deeper (the curtain has a shadow edge — it is
  wax in front of light). Beneath the drips' meeting line, the
  overlay is a solid `--wax` sheet: when the drips meet, the
  page is fully covered by the sheet.
- **Motion spec.** Trigger: an intercepted same-origin route
  change (link click that the router owns). t=0: drips begin
  elongating `--ease-drip`, staggered 30ms per drip left to
  right with per-drip rates (0.85–1.15× authored), reaching the
  viewport bottom between t=380–520ms; the sheet follows the
  slowest drip's tip. t≈520ms: fully covered; the route swap
  happens beneath the sheet. t=520–700ms: the covered page is
  held for one beat (the swap is instant; the hold is the
  curtain's dignity) — then the whole overlay lifts as one sheet
  over 180ms `--ease-settle` on the new page, whose own content
  is already printed beneath (the new page never melts in under
  a curtain — §5's melt-ins are for first entries, and a
  curtain-arrival counts as entered). Total: ~700ms to cover,
  ~880ms to revealed new page.
- **States.** Idle (overlay absent from the DOM) → falling
  (drips elongating) → covered (swap beneath) → lifting (sheet
  rises) → idle. A second navigation during a curtain is queued
  to the covered beat, never stacked. Browser back/forward: the
  curtain does not run (history navigation is the browser's
  ceremony, not the site's).
- **Content merge.** The curtain is the site's material poured
  over itself: the drips are §6.3's drips grown to full length —
  the visitor has seen this wax behave at 64px all page, and the
  transition is the same behaviour at viewport scale. Continuity
  of material is the merge.
- **Failure fallback.** Any failure — router error, swap timeout
  at 1200ms, JS error mid-curtain — lifts the sheet immediately
  and completes the navigation plainly. The curtain is a
  courtesy over a working router; it can delay a navigation by
  at most 1200ms in the worst failure, and the watchdog is
  load-bearing code, reviewed as such (§15 step 13). No JS: no
  curtain, ordinary navigation.
- **Reduced-motion variant.** No curtain. Navigation is instant.
  Reduced motion is a complete exemption from ceremony here —
  a 700ms full-screen wipe is precisely the class of motion the
  preference exists to refuse.
- **Performance budget & mobile variant.** 9 paths + 1 sheet,
  transform/opacity only, ≤0.4ms/frame for <1s per navigation.
  Mobile: 6 drips (viewport is narrower; 9 would stripe), same
  timings — the curtain's beat is tempo, not size.
- **Choreography timeline (v2).** Click (router-owned) → t=0
  drips start, 30ms stagger → t=380–520 tips reach bottom,
  sheet closes → t=520 swap → t=520–700 covered beat → t=700
  sheet lifts 180ms → t=880 new page revealed, overlay removed
  from DOM.
- **State matrix (v2).** *Rest:* absent. *Hover/focus:* n/a —
  links behave normally until the click that owns them.
  *Active:* the click that triggers is acknowledged by the
  curtain's first drip within one frame (no dead click).
  *Scrolled-past:* n/a. *Disabled:* in-page anchors, external
  links, and modified clicks (cmd/ctrl/middle) bypass the
  curtain entirely — the browser's intent outranks the theme's.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: 9 drips. 768–1199px: 7 drips.
  <768px: 6 drips. Timings identical at all sizes.
- **Edge cases & failure modes (v2).** *Slow route fetch:*
  the covered beat extends to a 1200ms cap with the sheet
  static (a held curtain, no looping drips — wax waits), then
  lifts regardless and lets the destination's own loading
  (§6.16) speak. *Same-page link (href to current route):*
  ignored by the interceptor. *Form submission navigations:*
  excluded — a submitted order (§6.14) resolves in place, never
  behind a curtain.
- **Accessibility spec (v2).** The overlay is `aria-hidden` and
  the navigation's accessibility is the router's (focus moves
  to the new page's heading at the covered beat, announced by
  the route change itself, not by the curtain). During the
  700ms the overlay blocks pointer input but never keyboard
  focus order — focus is already moving with the route.
  Vestibular: full-screen vertical motion is the risk; the
  reduced-motion exemption above is therefore absolute, and the
  curtain additionally does not run when the OS reports a
  reduced-data/reduced-motion media state at the browser level
  beyond the standard query.
- **Tokens consumed (v2).** `--wax`, `--wax-shadow`,
  `--ease-drip`, `--ease-settle`, `--dur-curtain` (700ms),
  `--curtain-drips` (9).

### 6.11 Hive navigation

- **What & why.** The masthead navigation is a row of comb cells:
  each destination is a hex cell in a shared-wall strip, the
  current destination's cell is capped (filled, with the lid
  line), and the strip's last cell is "Your comb" with its live
  count. It belongs because the site's wayfinding should be made
  of the site's structure — the visitor learns in the first
  screen that cells are containers with states, and §6.2 and
  §6.8 then speak a language already taught.
- **Structure.** A `<header>` on the ground (not a bar — the
  masthead sits on `--wax` with a `--propolis` hairline beneath,
  1px, the only straight line on the page) holding: the wordmark
  (Fraunces, sentence case, §3), the nav strip (4–6 cells,
  flat-top hexagons 44px tall sharing walls, each a real link
  with its label centred), and the your-comb cell (a link to
  §6.14's form / the shop's comb list, showing the capped count
  as data type: "Your comb · 3"). The current page's cell
  carries `--honey` fill at 30% plus the `--comb` lid line —
  capped, but translucently: you are *in* this cell, it is not
  yet stored.
- **Motion spec.** Mostly still — navigation is furniture.
  Two motions only: on page load, the current cell's fill pours
  in over 400ms `--ease-pour` (it rhymes with §6.2's fills and
  teaches them); on hover/focus of another cell, its wall warms
  `--wax-shadow` → `--comb` over 180ms `--ease-settle` and cools
  over 300ms on leave (warming is faster than cooling — wax
  remembers heat briefly). The your-comb count, when it changes
  (§6.8), ticks with a single 300ms `--ease-pour` fill pulse on
  its cell — never a badge bounce.
- **States.** Rest: current capped-translucent, others walled.
  Hover/focus: wall warms as above; focus adds the 2px
  `--comb-deep` outline inside the hex. Active (press): cell
  scales 0.97 for 120ms `--ease-melt` (a wax press). Current
  cell is `aria-current="page"` and is not a link to itself.
  Disabled: none.
- **Content merge.** The nav cells and the side comb's cells are
  the same component at two scales — pages across the top,
  sections down the side — so the site's whole information
  architecture is one comb read two ways.
- **Failure fallback.** No JS: the strip is a plain list of
  links in hex dress; the current cell ships pre-filled (server
  / build marks it). Nothing about navigation depends on motion.
- **Reduced-motion variant.** Current cell ships filled; wall
  warms apply instantly. 
- **Performance budget & mobile variant.** Negligible (≤6 small
  layers). Mobile (<768px): the strip becomes a two-row comb
  under the wordmark (cells 40px), never a hamburger — a
  candleworks has few rooms and shows them all; if a site
  outgrows 6 destinations, §7's map requires splitting the site,
  not hiding the nav.
- **Choreography timeline (v2).** Load → t=0 current cell fill
  begins → t=400 rests → (the hero's glow, §6.1, starts at the
  same t=0 below — masthead and hero warm together, one room
  lighting). Hover beats are event-local as specified.
- **State matrix (v2).** *Rest:* as above. *Hover:* wall warms
  180ms in / 300ms out. *Focus:* warm + outline. *Active:* 0.97
  press. *Scrolled-past:* the masthead is not sticky at ≥1200px
  (the side comb is the persistent instrument; a sticky masthead
  would double it) — at <1200px it *is* sticky, because the rail
  is gone and something must persist (§6.2 breakpoints).
  *Disabled:* none. *Touch:* tap = navigation; no hover warm.
- **Breakpoints (v2).** ≥1200px: single row, non-sticky.
  768–1199px: single row, sticky, comb strip (§6.2) rides
  beneath it. <768px: two-row comb, sticky, strip integrated
  as the second row's right end.
- **Edge cases & failure modes (v2).** *Long destination
  names:* cell labels are capped at 12 characters at build
  (§12); a longer name gets a wider cell (the comb tolerates
  one wide cell per strip — bees build irregular cells at
  edges, and so does this grid) rather than smaller type.
  *Count desync:* the your-comb count reads the same stored
  list as §6.8/§6.17 — one source, three printings, again.
- **Accessibility spec (v2).** Real `<nav>` with a list of
  links; hex shapes are CSS on the list items and carry no
  semantics. Hit targets 44px tall, full cell width. Current
  state is never colour-only: the lid line geometry + 
  `aria-current`. Labels `--hive` on `--wax` 13.38:1; the
  translucent honey fill sits *behind* the current label and
  the label's contrast is computed against the filled cell
  (hive on honey-at-30%-over-wax ≈ 9.8:1, stated and checked).
- **Tokens consumed (v2).** `--wax`, `--honey`, `--comb`,
  `--comb-deep`, `--wax-shadow`, `--propolis`, `--ease-pour`,
  `--ease-settle`, `--dur-nav-fill` (400ms).

### 6.12 First-cell hero composition

- **What & why.** The hero is one translucent wax panel — the
  first cell — holding the warming headline (§6.1), the
  standfirst, two actions, and a strip of three small cells at
  its foot that state the house's facts (poured weekly / burns
  in evenings / capped by hand). It is specified separately from
  §6.1 because the headline is an event and the hero is a room:
  its composition, its glow discipline, and its ambient pulse
  (the page's second licensed ambient loop, §5) live here.
- **Structure.** A panel cell (§4 panel register: chamfered
  corners, sheet translucency 92%) spanning the measure, on the
  ground with a `--hive` photograph plate behind its top third
  (the workshop, warming the panel through the wax). Inside:
  kicker (cell label, §3), the `<h1>` (§6.1), standfirst, action
  row (primary: a filled comb-cell button "Shop the candles";
  secondary: a walled cell link "How a candle is made" → §6.4),
  and the fact strip: three mini cells with data-type facts.
  The hero's glow (§6.1's layer) is centred on the headline and
  owned by this panel.
- **Motion spec.** Load ceremony: §6.1 runs (glow 1000ms,
  letters, drip). After the ceremony (+2000ms), the glow hands
  to the **ambient pulse**: alpha breathing ±5% on a 5s sine,
  the hero's inner glow the original entry licenses — alive,
  but at the edge of notice; it pauses when the hero is
  off-screen and never resumes mid-breath (it restarts at sine
  0). Panel parallax: the photograph plate drifts at 0.94×
  (§4) against the panel's 1.0×, ≤14px across the hero's exit.
  The fact cells melt in last, staggered 80ms, after the
  standfirst.
- **States.** Ceremony (§6.1) → ambient rest (pulse on, plate
  drifting with scroll) → scrolled-past (pulse off, panel
  settled; the hero does not perform for an empty room).
  Hover: none at panel level (actions have their own, §11).
  Focus entering the hero: ceremony completes instantly (§6.1).
- **Content merge.** The fact strip's three facts are the site's
  three promises, and each is checkable deeper in the page
  (pour day in §6.4's copy, evenings in §6.7's science, capping
  in §6.8) — the hero is the comb's first cell and it contains
  the whole argument in miniature, which is what first cells
  are for.
- **Failure fallback.** No JS: the panel ships printed — glow
  static at full, headline set, facts present. The photograph
  plate failing leaves the panel on plain ground, warmer for
  the loss of nothing.
- **Reduced-motion variant.** No pulse, no parallax, no
  ceremony (§6.1). The glow stands at full — a lit panel,
  resting.
- **Performance budget & mobile variant.** One gradient layer +
  one parallax layer, ≤0.3ms/frame. Mobile: the plate becomes a
  band above the panel (translucency over a photo on a small
  screen muddies text; the panel sits on ground instead), fact
  cells stack 1×3, pulse retained (it is alpha-only and cheap).
- **Choreography timeline (v2).** t=0 §6.11's nav fill + glow
  warm begin together → §6.1 ceremony (to ~1800ms) → standfirst
  melt-in → fact cells stagger in (80ms) → t≈2000 pulse handoff
  → scroll: plate parallax until the hero exits → pulse off.
- **State matrix (v2).** *Rest:* printed or pulsing per above.
  *Hover:* none. *Focus:* ceremony completes. *Active:* n/a.
  *Scrolled-past:* settled, pulse off. *Disabled / no-JS:*
  printed, glow static. *Touch:* identical; no hover states
  anywhere in the hero.
- **Breakpoints (v2).** ≥1200px: panel 92% sheet, plate behind
  top third. 768–1199px: plate band above panel. <768px: plate
  band, facts stacked, actions full-width cells stacked.
- **Edge cases & failure modes (v2).** *No photograph supplied:*
  the plate is omitted and the panel warms from its glow alone
  — the hero must work as pure wax (a client without photography
  is common in this trade; §9 failure 6 covers the muddy
  alternative). *Long standfirst:* capped at 34 words at build
  (§12); the panel grows downward, never truncates.
- **Accessibility spec (v2).** Landmark order: kicker is
  presentational; the `<h1>` is the hero's first content in the
  accessibility tree. The glow and plate are decorative
  (`aria-hidden`, empty alt). Text on the translucent panel is
  computed against the *panel-over-plate* composite at its
  darkest authored point: `--hive` on the composite ≥7:1
  (checked at build against the supplied photograph's darkest
  region behind text — §15 step 4 makes this a build task, not
  a hope).
- **Tokens consumed (v2).** `--wax`, `--wax-pale`, `--hive`,
  `--glow`, `--ease-settle`, `--dur-pulse` (5000ms),
  `--sheet-opacity` (.92).


### 6.13 Comb-cell product cards

- **What & why.** The shop grid's product cards: each product
  lives in a cell of the grid comb — hex-framed photograph
  (§6.9), name, burn evenings, price, and the cap corner (§6.8).
  The card is specified as its own element because it is where
  five other elements meet (frame warmth, pool light, tilt, cap,
  counter data), and a card that is merely a box with things
  happening to it becomes §9 failure 10. Here the card *is* a
  cell: its geometry, its tilt (it lifts like a comb frame
  prised from the hive), and its data discipline are one design.
- **Structure.** An `<article>` per product inside the grid
  comb's shared-wall layout (§4): hex-clipped frame with the
  photograph, a body block beneath the frame (cards are cells
  with a label shelf — the hex holds the image, the shelf holds
  the record), name in Fraunces H3, the evenings line in data
  type ("about 14 evenings · beeswax, cotton wick"), price in
  data type with the unit word in `--comb-deep`, and the cap
  button (§6.8) at the frame's top-right corner cell. A sold-out
  product's cell is *empty*: frame shows the `--wax-shadow`
  interior, shelf reads "This cell is empty — next pour Tuesday"
  (§6.18's grammar at card scale), no cap button.
- **Motion spec.** Tilt: on pointer over the card (pointer-fine
  only), the card lifts as a frame from comb — rotateX/rotateY
  toward the pointer, max 4° on the long axis, with a 3px rise
  and its ground shadow deepening `--wax-shadow` → `--propolis`
  at 30%; driven by the shared loop at lerp 0.14 so the lift has
  wax's slight lag; on leave it settles over 450ms `--ease-melt`
  (it does not snap flat — a frame settles back into comb).
  Melt-in with the section (§5). Frame warmth and pool are
  §6.9/§6.6 writing to this card's properties. Nothing else
  moves: the shelf's text never tilts (the tilt pivots the frame
  only — records stay level, §3 law 1 applied to geometry).
- **States.** Rest (in comb) → lifted (pointer over, frame
  tilted ≤4°, shelf level) → capped (§6.8's seal in the corner,
  independent of tilt) → empty (sold out, no tilt — an empty
  cell is not lifted for inspection). Focus-within: the frame
  lifts 2° toward centre (a courtesy tilt, §6.6's focus rule
  applied locally) and the cap button takes focus outline.
  Disabled: the empty state only.
- **Content merge.** The card's data is the product's record and
  its order is fixed — image, name, evenings, price, cap —
  because a cell's contents settle in one order. The evenings
  line is the card's second line, never a badge or a corner
  ribbon: in this theme the burn time is the headline fact after
  the name, and §12's card copy law keeps it there.
- **Failure fallback.** No JS: cards print flat in the comb,
  frames at §6.9's printed tint, cap buttons as form toggles
  (§6.8 fallback). Images missing: the empty-cell grammar.
  Tilt unsupported (no pointer): nothing is lost — tilt is the
  only purely kinesthetic element on the card.
- **Reduced-motion variant.** No tilt, no melt-in travel; cards
  print in place. Cap and warmth (§6.9's reduced ruling) follow
  their own variants.
- **Performance budget & mobile variant.** Tilt transforms on
  the frame layer only, ≤8 cards concurrently in view typical,
  ≤0.3ms/frame. Mobile: tilt is cut (touch has no hover, and a
  tap-tilt that fights the tap is a defect); cards stack 1-across
  below 560px, 2-across 560–767px; the cap corner grows per
  §6.8.
- **Choreography timeline (v2).** Section melt-in (§5) → cards
  settled → pointer enter → tilt rises over ~300ms of loop time
  to pointer angle → pointer move → tilt follows at lerp 0.14 →
  pointer leave → 450ms settle → cap events (§6.8) run
  independently at any tilt angle (capping a lifted frame is
  allowed and encouraged — the seal presses at t=300 of §6.8
  while the frame holds its tilt).
- **State matrix (v2).** *Rest:* in comb, cool or warm per
  §6.9. *Hover:* frame tilt ≤4°, shelf level. *Focus:* 2°
  courtesy tilt, outlines per §6.8. *Active:* cap press (§6.8).
  *Scrolled-past:* cooled (§6.9), flat. *Disabled:* empty-cell
  state. *Touch:* no tilt; tap on the frame follows the card's
  link (product page), tap on the corner caps — the two targets
  are geometrically separate (frame vs corner cell) so a thumb
  cannot confuse them.
- **Breakpoints (v2).** ≥1200px: 3-across comb, tilt full.
  768–1199px: 2-across, tilt ≤3°. <768px: 1–2 across, no tilt.
- **Edge cases & failure modes (v2).** *Long product names:*
  the shelf grows; the frame never shrinks (cells in a comb are
  uniform — the shelf is not a cell and may vary). *Price
  changes / sale:* a struck price is set in `--propolis` with
  the new price in `--hive` — honey never marks a discount
  (§9 failure 3); there are no percentage badges in this theme,
  ever (§12). *Grid filtered:* cards that leave take their caps
  with them in the stored list (§6.8) — filtering hides, it does
  not uncap.
- **Accessibility spec (v2).** The card is an `<article>` with
  the name as its heading; the photograph's alt names the
  product and its vessel ("Alderwick No. 4 candle in a glass
  vessel"). Tilt is decorative and never moves the cap button's
  hit area (the button is on the untilted shelf layer — a moving
  target is an accessibility failure, and this is why the shelf
  stays level). All text ratios per §2 against the untilted
  shelf ground `--wax-pale`.
- **Tokens consumed (v2).** `--wax`, `--wax-pale`,
  `--wax-shadow`, `--propolis`, `--comb-deep`, `--hive`,
  `--ease-melt`, `--tilt-max` (4deg), `--warm` (from §6.9).

### 6.14 The candle-order form (conversion)

- **What & why.** The order form is a sheet of ruled wax paper
  inside a panel cell: your capped products (§6.8) arrive as its
  first lines, quantities are set in evenings of burn, and
  submitting seals the order — the confirmation is a capped cell
  bearing the order's record. It belongs as a specified element
  because conversion in this theme is the visitor's comb being
  carried to the till: the form must feel like the same material
  behaving the same way, or the shop's fiction collapses at the
  exact moment money appears (§9 failure 4).
- **Structure.** A `<form>` in a sheet panel (§4): line items
  (one row per capped product — name, evenings each, quantity
  stepper as two walled cells − / +, line total), an uncapped
  "add from the shelf" select (§11's cell-radio pattern in a
  disclosure), delivery fields (name, direction/email, address)
  as ruled-line inputs (bottom rule only, `--propolis` at rest,
  inking to `--comb-deep` on focus over 260ms), a burn-total
  line that sums the order in evenings ("This order burns for
  about 61 evenings, lit one at a time") computed live from the
  rows, and the submit cell: a filled comb-cell button, "Seal
  the order". Success replaces the form with the confirmation
  cell (§6.8's seal at 3× size, the order number in data type,
  and the day-book line "Entered — [date], order № …").
- **Motion spec.** Field focus: the rule inks 260ms `--ease-draw`
  left to right; a filled field's rule rests at 60% ink.
  Quantity steps: the row's evenings total re-counts (§6.15's
  count, 300ms here — form counts are quicker than display
  counts) and the burn-total line re-counts with it. Submit:
  the button presses (scaleY 0.96, 120ms `--ease-melt`), the
  form's panel warms +6% over 400ms (the wax softening to take
  the seal), then the confirmation cell's seal fills over
  600ms `--ease-pour` with the §6.8 ring closing at t=450 — the
  same gesture as capping, at ceremony scale. Errors: the
  field's rule turns `--err` and the margin note appears in the
  chandler's voice (§12) with a 300ms melt-in; nothing shakes.
- **States.** Empty (no caps carried in: the form opens with the
  shelf disclosure expanded and a line in the empty voice,
  "Your comb is empty — the shelf is above.") → filled → 
  submitting (button pressed, fields inert, panel warming) →
  sealed (confirmation). Error state per field, keeping the
  visitor's input (§10 gate 7 rehearses it). The form never
  disables its submit to punish incompleteness — it submits,
  and errors are kept and explained (the theme's form law,
  shared with §6.8's disabled ruling).
- **Content merge.** The form's first content is the visitor's
  own comb carried down the page — §6.8's stored list *is* the
  form's initial state, so the conversion section begins already
  half-filled by the shop's play. The burn-total line converts
  the order into the theme's unit: you are not buying objects,
  you are buying evenings, and the form says so in arithmetic.
- **Failure fallback.** No JS: a plain form with the same fields
  (caps arrive as pre-checked toggles per §6.8's fallback),
  native validation off, server errors rendered in the same
  margin-note positions. Submission failure (network): the
  panel's warmth fades, a day-book error line appears above the
  submit cell ("The order didn't reach the book — nothing was
  charged. Try once more."), input fully preserved.
- **Reduced-motion variant.** All transitions instant; the
  confirmation seal appears filled. The panel warm-up is cut.
- **Performance budget & mobile variant.** Trivial layers; the
  counts are text writes batched per step. Mobile: rows stack
  (name / stepper / total on two lines), ruled fields full
  width, submit cell full width at 52px tall.
- **Choreography timeline (v2).** Arrive with caps → lines
  print with quantities at 1 → steps re-count (300ms) →
  focus inks rules (260ms) → submit press (120ms) → panel warms
  (400ms) → seal fills (600ms, ring at 450) → confirmation cell
  replaces form → §6.17's footer tally gains the order's line
  on next view (same record, §1).
- **State matrix (v2).** *Rest:* as stored. *Hover:* submit
  cell wall warms (§6.11's rule). *Focus:* rule inks; focus is
  never taken by an error — errors are notes, focus moves only
  on submit to the first error field with its note read by AT.
  *Active:* press beat. *Scrolled-past:* state persists.
  *Disabled:* submit never disabled. *Touch:* steppers are
  48px cells; ruled fields 52px tall.
- **Breakpoints (v2).** ≥1200px: form panel at 8 columns of the
  measure, summary rail at right (burn total + seal preview).
  768–1199px: single column, summary rail becomes a sticky foot
  line inside the panel. <768px: single column, summary in
  flow above the submit.
- **Edge cases & failure modes (v2).** *Zero-quantity row:*
  stepping to 0 uncaps the product (§6.8 syncs) and the row
  drains out over 300ms — it does not linger as a ghost line.
  *Evenings arithmetic:* line evenings = product evenings ×
  quantity, from the product data object — the same object the
  card printed from, so form and card can never disagree
  (§10 gate 3). *Guest with no caps and no selection:* submit
  yields the empty-voice error at the shelf disclosure, in
  voice, not a red asterisk.
- **Accessibility spec (v2).** Real labels on ruled fields (the
  rule is decoration; the label is text above the field, never
  placeholder-only). Errors are `aria-describedby` margin notes
  + a summary at the submit that names the fields in the
  chandler's voice. The burn-total is `aria-live="off"` (it is
  available, not announced per step). Confirmation replaces the
  form with `role="status"` content including the order number
  as text.
- **Tokens consumed (v2).** `--wax-pale`, `--wax`, `--hive`,
  `--propolis`, `--comb-deep`, `--err`, `--seal`, `--ease-pour`,
  `--ease-melt`, `--ease-draw`, `--dur-rule-ink` (260ms).

### 6.15 Comb counters (figures that count)

- **What & why.** The site's numbers — burn evenings on cards,
  cell counts in the science section, jars capped this season in
  the footer record — count up when they arrive. The element is
  specified separately because counting is where themes lie:
  here, every counter runs between two true values (the printed
  figure's own neighbours in the data record) and lands exactly
  on the figure the data object holds, which is the same figure
  the no-JS page prints. A counter that starts at 0 is claiming
  the workshop once had nothing; a counter that overshoots is
  theatre. These counters *arrive*, the way a chandler reads a
  tally aloud.
- **Structure.** A `<span class="count" data-count="[true
  value]">` in data type (§3), with the true value as its text
  content in the shipped DOM. JS replaces the text during the
  count with a visually-hidden sibling holding the true value
  for AT at all times. Counters are registered centrally (one
  observer, one loop) — a page carries ≤6 (budget, §14).
- **Motion spec.** Trigger: the figure's line enters at 40%
  visibility, once per session. The count runs from
  `max(0, value − 12%)` (rounded to the figure's own precision —
  evenings count in whole evenings, from value−2 at small values)
  to the true value over 900ms `--ease-pour` timing (the pour
  curve: fast gather, long settle on the exact figure), digits
  tabular so the line never jitters. The final frame holds the
  true value for 200ms before the registration retires — the
  eye must catch the landing. §6.14's form counts reuse the
  mechanism at 300ms and from the *previous* value (a step from
  14 to 28 evenings counts 14 → 28, never from a floor — inside
  a form, counts are arithmetic, not arrival).
- **States.** Printed (rest, true value) → counting (900ms) →
  printed. Hover/focus: none. Scrolled-past uncounted: prints
  (a flung-past figure does not count for nobody).
- **Content merge.** Every counter is a figure in a sentence —
  "about 14 evenings", "312 cells in a frame", "1,140 jars
  capped this season" — and the sentence is the content; the
  count is the chandler reading it. §12's figure law: a number
  that cannot appear in a sentence does not appear on the page.
- **Failure fallback.** No JS: the printed true value, which was
  always the text content. Observer failure: figures print.
  There is no state in which a wrong number is displayed except
  mid-count transients that are *between* two true values by
  construction.
- **Reduced-motion variant.** No count. Figures print. (A count
  is motion; the number is the content.)
- **Performance budget & mobile variant.** Text writes ≤1 per
  frame per counter, ≤6 counters, negligible. Mobile identical.
- **Choreography timeline (v2).** Line at 40% → t=0 count starts
  at value−12% → pour curve → t=900 true value lands → t=1100
  registration retires. Form variant: step event → 300ms count
  from previous to new.
- **State matrix (v2).** *Rest:* true value. *Hover/focus:*
  none. *Active:* n/a. *Scrolled-past:* true value.
  *Disabled / no-JS:* true value. *Touch:* identical.
- **Breakpoints (v2).** Identical at all sizes; figures are type,
  and type does not change its honesty by viewport.
- **Edge cases & failure modes (v2).** *Value edited in a CMS:*
  `data-count` and text content are generated from the same
  data field at build; a hand-edit that desyncs them is caught
  by §10 gate 3's agreement audit (the count lands on
  `data-count`; the audit greps that text == data-count in the
  shipped HTML). *Huge values:* counts above 10,000 abbreviate
  the transient (count in hundreds) but land on the exact
  figure with its grouping commas. *Zero is a true value:* a
  product with 0 evenings does not exist; a season count of 0
  prints "none yet" (§12's zero wording) instead of counting
  to 0.
- **Accessibility spec (v2).** The visually-hidden true value is
  the accessible one throughout; the animated text is
  `aria-hidden`. A screen reader never hears a number mid-count.
  Tabular figures keep line lengths stable for low-vision
  tracking.
- **Tokens consumed (v2).** `--ease-pour`, `--dur-count`
  (900ms), `--count-max` (6 per page).


### 6.16 Empty-comb skeleton + section pass

- **What & why.** Loading in this theme is an empty comb: skeleton
  cells — hex outlines in `--wax-shadow` — that fill with a pale
  wax shimmer as content loads, cell by cell, until the real
  section pours in. It belongs because a visitor waiting at a
  candleworks should see the comb before the honey: the skeleton
  is the page's structure honestly empty, and its fill order
  (centre-out, honey order) previews how the real grid will
  arrive. It also carries the in-page "section pass" — when a
  nav jump (§6.11) crosses more than two sections, the skeleton
  flashes for the duration of the scroll-settle, so long jumps
  feel like passing comb, not teleporting.
- **Structure.** A skeleton is the target section's own grid
  geometry (same cell count and register as the content it
  stands for — a shop skeleton has the shop's cells, a text
  section's skeleton is one panel cell with three ruled lines):
  hex outlines with an inner shimmer layer (`--wax-pale` →
  `--wax` gradient translating across the cell on a 1200ms loop).
  Skeletons are JS-inserted only, into a reserved box of the
  section's exact dimensions — the layout never shifts when
  content replaces them (the box is the contract).
- **Motion spec.** On insert: cells fill in honey order
  (centre-out), each cell's shimmer starting at a 40ms stagger.
  Resolution: when the section's content is ready, cells fill
  solid `--wax` over 300ms `--ease-pour` in the same order, and
  the real content melts in (§5) as the last cell fills — the
  handoff is one beat, never a flash of empty ground. Hard cap:
  a skeleton lives at most 2500ms; past that, it resolves to
  whatever content exists or to the empty-cell state (§6.18)
  with a day-book line ("This section is still pouring — the
  shelf above is open.") — a skeleton that outlives 2.5s is a
  broken promise, and the theme names it rather than spinning.
- **States.** Absent → shimmering (loading) → filling (handoff)
  → absent (content in). The section-pass variant: appears only
  during >2-section nav jumps, shimmer only, resolves on
  scroll-settle + 150ms. Hover/focus: none; a focused element
  inside a loading section forces immediate resolution attempt
  (focus is never left standing on a skeleton).
- **Content merge.** The skeleton *is* the section's geometry —
  it teaches the grid while it waits, and its cell count is the
  real cell count (a shop of 9 products skeletons 9 cells; the
  count is data, not wallpaper).
- **Failure fallback.** No JS: no skeletons exist; content is
  simply the page. Slow content: the 2500ms cap and empty-state
  line above. A skeleton must never be the last thing a section
  shows.
- **Reduced-motion variant.** Skeletons render as static empty
  cells (no shimmer) and resolve instantly when content lands.
  The section pass does not run.
- **Performance budget & mobile variant.** Shimmer is one
  gradient translation per cell, ≤12 cells concurrent, ≤0.3ms/
  frame. Mobile: identical, cell register per §6.5's mobile
  sizing.
- **Choreography timeline (v2).** Section requested → t=0
  skeleton inserted into reserved box → cells shimmer in
  (40ms stagger) → content ready → solid fill 300ms honey
  order → content melt-in overlaps the final 150ms → skeleton
  removed at melt-in completion.
- **State matrix (v2).** *Rest:* absent. *Hover/focus:* focus
  forces resolution attempt. *Active:* n/a. *Scrolled-past:*
  a skeleton scrolled past unresolved resolves silently in the
  background (its content will be printed when returned to).
  *Disabled / no-JS:* absent. *Touch:* identical.
- **Breakpoints (v2).** Geometry follows the target section at
  every size; shimmer loop identical.
- **Edge cases & failure modes (v2).** *Content arrives before
  the skeleton's first frame (cache-fast):* the skeleton is
  skipped entirely — a loader that flashes for 80ms is worse
  than none; insertion is raced against a 120ms timer.
  *Repeated nav jumps:* skeletons never stack; one pass at a
  time, and a new jump re-targets it.
- **Accessibility spec (v2).** The skeleton region carries
  `aria-busy="true"` on the section and a visually-hidden
  status ("Loading the shop") that resolves to silence when
  content lands — announced once, never per cell. Shimmer cells
  are `aria-hidden`.
- **Tokens consumed (v2).** `--wax-shadow`, `--wax-pale`,
  `--wax`, `--ease-pour`, `--dur-shimmer` (1200ms),
  `--skeleton-cap` (2500ms).

### 6.17 The hive footer (the day-book)

- **What & why.** The footer is the candleworks' day-book: the
  shop's record lines (address, pour days, the season's tally),
  the visitor's own stored tally ("Your comb this visit: 3 cells
  capped · 1 order sealed"), repeat navigation, and the closing
  line. It belongs as a specified element because it is the
  law's third printing (§1): the footer's tally must agree with
  the side comb (§6.2) and the shop header (§6.8) because all
  three read one record — and a footer that prints the visit's
  truth is the theme's final argument that its numbers are real.
- **Structure.** A `--propolis` ground band (the page's one dark
  band besides the making section) with `--wax` text: three
  columns — the house record (name, address, pour days, in the
  Record register §12), your visit (the tally lines, data type,
  updated from the record), and the index (repeat nav as a
  vertical cell strip, §6.11's cells at label size) — over a
  closing rule drawn in `--honey` hairline with the fixed line
  (§12) and the year, computed (§6.15's discipline: the year is
  `new Date().getFullYear()` in JS, printed statically correct
  at build).
- **Motion spec.** Nearly still. The closing rule draws
  (`--ease-draw`, 600ms) when the footer enters — the day-book
  is underlined as it is reached. The tally lines, if the record
  changed since the footer was last seen, update with §6.15's
  count at 600ms on entry. Nothing else moves; a footer is a
  record, and records do not perform.
- **States.** Rest. Hover/focus on index cells: §6.11's wall
  warm. The your-visit column with an empty record prints the
  honest zero lines ("Your comb this visit: nothing capped
  yet.") — zero is printed as words, never as a shame number.
- **Content merge.** The footer's house record is the shop's
  real facts and its visit tally is the reader's real session —
  the page ends by accounting for itself and for the visitor in
  the same ledger, which is what day-books are for.
- **Failure fallback.** No JS: the visit column prints the
  static line "Your comb is kept in the shop, above." (a true
  pointer, not a fake tally); house record and index complete.
- **Reduced-motion variant.** The rule stands drawn; tallies
  print.
- **Performance budget & mobile variant.** Negligible. Mobile:
  columns stack — visit first (the reader's own record leads on
  a small screen), house second, index as a two-row comb.
- **Choreography timeline (v2).** Footer at 30% → rule draws
  600ms → tally counts (if changed) 600ms → rest.
- **State matrix (v2).** *Rest:* printed record. *Hover/focus:*
  index warms. *Active:* n/a. *Scrolled-past:* n/a (it is the
  bottom). *Disabled / no-JS:* static pointer line. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: three columns. 768–1199px:
  two columns (visit + house), index as a row beneath.
  <768px: stacked as above.
- **Edge cases & failure modes (v2).** *Record in another tab:*
  `sessionStorage` is per-tab; the footer prints this tab's
  truth and says "this visit" — the wording is the honesty.
  *Order sealed (§6.14):* the tally gains its line from the
  same record object the form wrote; a disagreement between
  form confirmation and footer tally is a §10 gate-3 failure
  by definition.
- **Accessibility spec (v2).** A real `<footer>` with labelled
  columns; the tally is text, not a chart. Contrast: `--wax` on
  `--propolis` 6.93:1 for body, `--honey` on `--propolis` for
  the rule only (graphical). The year and tallies are plain
  text in the accessibility tree.
- **Tokens consumed (v2).** `--propolis`, `--wax`, `--honey`,
  `--ease-draw`, `--dur-rule-draw` (600ms).

### 6.18 The unfilled cell (404 / empty state)

- **What & why.** The page that does not exist is an unfilled
  cell: a large empty hex cell in a field of faint comb, the
  sought direction printed in its label shelf, the chandler's
  plain line, and the nearest real cells offered as links. It
  belongs because every comb has empty cells, and an empty cell
  is not an error in a hive — it is a place nothing has been
  stored yet. The 404 in this theme refuses alarm: no broken
  jar, no spilt honey, just an honest empty.
- **Structure.** The standard page frame (§6.11 masthead, §6.17
  footer) around a centred composition: one large cell (280px
  across flats ≥1200px) outlined in `--comb` over a field of
  `--wax-shadow` ghost cells at 30%, its interior empty `--wax`,
  beneath it the label shelf: "This cell is empty." in Fraunces,
  then the sought path in data type (struck through in
  `--propolis`, never in honey — honey is good news, §2), then
  two lines in the chandler's voice and three real suggestion
  cells (the shop, the making, the science — the site's three
  fullest combs).
- **Motion spec.** One beat only: on entry, the ghost field's
  cells fill faintly in honey order (200ms stagger across the
  field, `--ease-pour`, to 30% and no further — the field warms
  but never fills; filling it would lie). The central cell does
  not fill, pulse, or glow. Its stillness is the message, held
  against the field's faint warmth. Nothing loops.
- **States.** Rest (after the field's one warm pass). Hover on
  suggestion cells: §6.11's wall warm. Focus: outlines per
  §6.11. No other states — an empty cell has no behaviour, and
  inventing one (a bouncing bee, a "go home" button that
  pulses) is §9 failure 1 in its purest form.
- **Content merge.** The sought path is printed and struck — the
  page names what was asked for, as the register grammar
  requires — and the suggestions are the site's real fullest
  sections, not a sitemap dump.
- **Failure fallback.** The 404 is the fallback; it ships fully
  static-capable (the field's warm pass is JS-armed; without JS
  the field prints at 30% and the page is complete).
- **Reduced-motion variant.** Field prints at 30%; no warm pass.
- **Performance budget & mobile variant.** One staggered fade
  across ≤24 ghost cells, once. Mobile: central cell 200px,
  ghost field cropped to the viewport width, suggestions stack.
- **Choreography timeline (v2).** Load → t=0 ghost field begins
  its warm pass (honey order, 200ms total stagger) → t≈600
  field rests at 30% → stillness. The central cell never moves.
- **State matrix (v2).** *Rest:* empty, still. *Hover/focus:*
  suggestions only. *Active:* n/a. *Scrolled-past:* n/a.
  *Disabled / no-JS:* printed field. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: 280px cell, full field.
  768–1199px: 240px cell. <768px: 200px cell, field cropped.
- **Edge cases & failure modes (v2).** *A sought path that
  exists but errored (500):* the same page serves with the
  day-book line changed to the failure's honest wording
  ("This cell is full, but the lid is stuck — the shop has
  been told.") — the grammar stretches to server errors
  without changing its voice. *Search empties (no results):*
  the same composition at section scale inside the shop: one
  empty cell, "Nothing is stored under that name." and the
  nearest categories as cells.
- **Accessibility spec (v2).** The heading is the plain fact
  ("This cell is empty."); the struck path is read as text
  with a visually-hidden "(the page you asked for)" prefix so
  AT users get the sentence, not a riddle. HTTP status is a
  real 404 — the theme never soft-404s behind a pretty cell.
- **Tokens consumed (v2).** `--comb`, `--wax-shadow`, `--wax`,
  `--propolis`, `--hive`, `--ease-pour`.

## 7. Page application map

- **Home.** The full choreography (§13): hero cell (§6.12),
  shop comb (§6.13/§6.6/§6.9), science (§6.7 + §6.5), making pin
  (§6.4), pricing (§6.3), order (§6.14), day-book (§6.17). The
  side comb's registry is the home page's sections.
- **Shop / listing.** The comb grid at full density; the side
  comb's registry becomes the category list (each category a
  cell-row); §6.6's pool runs; §6.16 skeletons serve filtered
  re-renders; the pricing drips do not appear (they belong to
  the home page's pricing section — one house per element).
- **Product detail.** The hero becomes a single large cell: the
  product's frame (§6.9) at panel scale, its evenings and record
  on the shelf, the cap button (§6.8) as the page's primary
  action. The making pin is refused here — a product page is a
  shelf, not a workshop tour; in its place, the product's own
  pour is told in a §6.5-masked photograph sequence.
- **Science / journal (article pages).** The diagram grammar
  (§6.7) generalises: one diagram per article, drawn on entry;
  the side comb's registry is the article's headings; pull-quotes
  sit in veil panels (§4). Counters (§6.15) carry the article's
  figures.
- **Workshops / booking.** The order form's grammar (§6.14) with
  evenings as the booked unit — a workshop *is* an evening, and
  the form's burn-total line becomes the booking's plain total
  ("Two evenings, four places"). The confirmation seal is the
  booking's ticket.
- **About / the apiary.** Panel cells and §6.5 photographs; the
  comb diagram is replaced by the apiary's own frame diagram
  (same draw grammar, different anatomy — the element is a
  grammar, not a picture).
- **404 / empty.** §6.18, at page scale and at section scale
  (search empties, sold-out cells §6.13).

## 8. Worked examples

### 8.1 The hero — Alderwick Candleworks, first screen

The visitor arrives at the candleworks of Alderwick — a
two-person chandlery selling poured beeswax candles. t=0: the
page prints complete (headline set, glow at full, facts
present) — then JS arms the ceremony and, fonts having
resolved inside the race, replays warmth: the masthead's
current cell ("Candles") pours its fill (§6.11, 400ms) as the
hero panel's glow warms from 0 (1000ms, §6.1). The headline —
"Poured on Tuesdays, lit all winter." (34 letters; the build
compresses its stagger to 38ms to hold the 1800ms cap) —
settles letter by letter from t=250, each glyph dropping 4px
into the wax with the soft overshoot of `--ease-melt`; the
final letter of "winter." elongates 12% over 600ms, holds 90ms,
snaps home. The standfirst melts in ("Beeswax candles from two
hives and one very patient man. Burn time counted in evenings,
the way you'll spend them."), then the fact cells stagger in:
POURED EVERY TUESDAY / ABOUT 14 EVENINGS A CANDLE / CAPPED BY
HAND. The actions sit beneath: "Shop the candles" (filled
cell) and "How a candle is made" (walled cell). Behind the
panel's top third, the workshop photograph warms the sheet
through its translucency. Scroll timeline: the plate parallaxes
0.94× as the hero exits; the side comb's first cell is already
gathering (its wall pulses) because the hero counts as the
registry's first section; at the hero's end-marker crossing,
cell 1 fills (§6.2) — the visitor has stored their first honey
before reaching the shop.

### 8.2 Mid-page — the science of wax

Three sections down, the reader reaches "Why a hexagon" — the
science section. Its spectacle order is legislated (§6.7): the
diagram first. At 35% visibility the comb cross-section draws:
frame walls, then inner walls in reading order, caps settling,
honey rising in the two open cells — 1600ms — while the four
labels melt in beside their referents ("The wall — shared, so
no wax is wasted", "The cap — the lid §6.2 wears", "The store
— honey at a third", "The evening — about three hours at a
table", this last being the unit law's defining sentence,
placed in the diagram's own mouth). The copy beside it runs in
the Record register (§12): cell counts as counters ("A frame
holds 312 cells, give or take the corners" — the counter
arrives at 312, §6.15, from 274). Only when the draw completes
+200ms may the section's photograph (a macro of real comb)
trigger its hex-mask reveal (§6.5), focal cell on the capped
corner the text is discussing. The reader scrolling back up
meets both finished: drawn diagram, stored photograph, and the
comb at the side filling this section's cell as its end-marker
crossed on the way down.

### 8.3 Conversion — sealing an order

In the shop above, the visitor capped three cells: No. 4
(14 evenings), No. 9 (22 evenings), and the tapers (9 evenings).
The order section (§6.14) opens with those three lines already
entered — the comb carried down. The burn-total line reads
"This order burns for about 45 evenings, lit one at a time"
(14+22+9, computed from the same product objects the cards
printed). The visitor steps the tapers to 2: the line re-counts
45 → 54 over 300ms (§6.15's form variant). They fill the ruled
fields; the email lacks its @, and on submit the field's rule
turns `--err` with the chandler's note in the margin: "That
direction won't carry — the @ is missing, looks like." Input
kept, focus moved to the field, nothing else disturbed. Fixed
and resubmitted: the button presses, the panel warms 6%, and
the confirmation cell's seal pours full over 600ms — order №
in data type, "Entered in the day-book", and the line the
whole theme exists to make ordinary: "We'll pour on Tuesday.
Your first evening is on us if it rains." (The last clause is
the house's real policy, printed in §12's fixed strings — the
form never invents policy.) The footer's tally, when reached,
shows the order among the visit's record: three printings, one
truth.


## 9. Anti-slop — what makes THIS theme look cheap

1. **The cartoon bee.** A mascot, a striped icon set, a smiling
   insect anywhere. *Cure:* there is no bee in this theme. The
   makers are bees; the page is the works. Any bee imagery is a
   build-time rejection.
2. **Honey-yellow wash.** Whole sections tinted honey, honey
   buttons with white text, a "warm" gradient background.
   *Cure:* §2's ration — honey is fill, glow, or one accent,
   ~12% of surface; text on honey is forbidden outright.
3. **Drips as wallpaper.** Wax drips fringing every section,
   dripping logos, drip dividers between paragraphs. *Cure:*
   drips exist exactly twice — over pricing (§6.3, anchored to
   cards) and in the making pin (§6.4) — plus the curtain
   (§6.10) that is made of them. A third drip location fails
   the build.
4. **The checkout that forgot the fiction.** A generic cart,
   a blue PayPal-shaped button, "Add to cart" language.
   *Cure:* §6.14's grammar end-to-end; the words are "cap",
   "your comb", "seal the order" — and the form's data must
   actually arrive from §6.8's list, not a parallel cart state.
5. **Hexagon clip-art.** Hexagonal badges, hex bullet points,
   hex social icons — geometry as confetti. *Cure:* every
   hexagon on the page is a container with a state (a cell that
   fills, a frame that warms, a seal that caps, a nav room).
   A hexagon containing nothing and meaning nothing is cut.
6. **Mud translucency.** Panels stacked three deep, photos
   behind text at veil opacity, "frosted" everything. *Cure:*
   §4's two depths only, and §6.12's build check: text
   composites are measured against the darkest point behind
   them, at build, with the real photograph.
7. **The cursor spotlight.** The light pool rebuilt as a
   pointer-following glow across the whole page. *Cure:* §6.6's
   pool lives inside the shop grid only, is grid-owned (the
   pointer borrows it), and never follows the pointer elsewhere.
   The cursor itself is the system cursor, always.
8. **Idle wax.** Drips that drip forever, a flame flicker loop
   on every candle photo, shimmer that never resolves. *Cure:*
   the page's ambient budget is two loops (§5); everything else
   is scrubbed, triggered, or still. A held drip (§6.4) is
   *still*, proudly.
9. **Script-font "handmade".** A handwriting font for "authentic"
   labels. *Cure:* §3 — the hand appears as seal, drip and pour,
   never as letterforms. Fraunces and Work Sans, no third face.
10. **Everything responds.** Cards that tilt, glow, warm, bounce
    and badge on one hover. *Cure:* one response per element per
    cause, as specified (§6.13's tilt, §6.9's warmth-by-scroll,
    §6.6's light-by-proximity are three different causes and
    never stack into a fourth).
11. **Inverted dark mode.** Black panels, yellow text, "dark
    honey" rebrands. *Cure:* §2's lamplight ruling — the wax
    stays wax after dark; only the room darkens.
12. **Curtain abuse.** The drip curtain on anchor jumps, filter
    changes, tab switches. *Cure:* §6.10's ration — route
    changes only, with the 1200ms failure cap rehearsed.

## 10. Quality gate

Blocking items — all must pass before the theme ships on a
build; the gate is signed by someone who did not build the page
(§15 step 15).

1. **Fill-law audit.** At five scripted scroll positions, the
   side comb's filled count, the ARIA percentage, and (at page
   end) the footer's tally agree exactly with the completion
   record computed independently from section offsets. Any
   disagreement fails the build.
2. **Evenings audit.** `grep` the shipped copy for "hour" in
   product contexts: zero hits outside the science section's
   one defining sentence. Every candle's burn figure is in
   evenings and matches its product data object.
3. **Three-printings agreement.** Pick three figures at random
   (a card's evenings, a form line total, a footer tally): all
   trace to one data object / one record. Hand-typed duplicates
   fail.
4. **Drip-function audit.** §6.3's drip scaleY values at three
   sampled scroll positions match the declared span function
   within lerp tolerance; §6.4's phase at three sampled pin
   positions matches the phase map. A drip whose length was
   chosen "to look right" fails.
5. **Warmth audit.** With the shop grid scrolled off-screen,
   no frame's `--warm` exceeds its scroll value (pool frozen);
   with the pointer outside the grid, no pool gather. Warmth
   without attention fails.
6. **No-strand test.** JS disabled, and separately JS killed
   mid-ceremony at five random moments: the page is complete
   and readable in every case — headline whole, comb a full
   index, diagram drawn, form submittable.
7. **Form-keeping rehearsal.** Submit §6.14 with (a) a bad
   email, (b) a zeroed row, (c) a killed network: input is
   preserved, errors are in the chandler's voice (§12), and no
   charge/order state is claimed that did not happen.
8. **Hexagon census.** Count hexagons in the shipped DOM:
   every one maps to a §6 element with a state. Ornament
   hexagons: zero. Drip locations: exactly §6.3 + §6.4
   (+ §6.10's curtain). Ambient loops running off-screen:
   zero.

## 11. Component inventory

Every component a real candleworks site needs, with its themed
treatment. Refusals name their replacement; a refused component
that appears anyway is a gate failure under §10's census
spirit.

- **Primary button** — a filled comb cell (`--honey` fill,
  `--hive` label — the one licensed text-on-honey pairing, at
  8.66:1 against the filled cell's darkened print treatment;
  where the fill is bright, the label sits on the cell's
  `--comb` base band instead). Press: §6.11's 0.97 wax press.
- **Secondary button** — a walled cell: transparent interior,
  `--comb` wall, `--comb-deep` label. Hover warms the wall.
- **Text link** — `--comb-deep`, underlined with a 1px rule that
  inks on hover (`--ease-draw` 200ms). Never honey.
- **Text input** — §6.14's ruled line: label above, bottom rule,
  focus inks the rule. No boxes; paper has lines, not borders.
- **Textarea** — ruled sheet: repeating-linear-gradient rules at
  the body line-height, text sitting on the lines.
- **Select** — *refused.* Replaced by the cell-radio row: options
  as walled cells in a strip, the chosen one capped (§6.8's
  grammar at form scale).
- **Radio / checkbox** — small cap toggles (§6.8's button at
  18px visual / 44px hit).
- **Stepper (quantity)** — two walled cells (− / +) flanking the
  figure in data type; the figure counts (§6.15 form variant).
- **Tabs** — *refused.* Replaced by the comb strip (§6.11):
  rooms of the site are cells, and a page's sections are the
  side comb (§6.2). A third tab system would be a third comb —
  the site has two, by design.
- **Accordion** — cell drawers: FAQ rows as long cells whose
  lower wall drops (clip) over 400ms `--ease-pour`; one open at
  a time; answers are printed open without JS.
- **Modal** — *refused.* Replaced by the capped panel: an
  in-flow sheet panel that pours in over the section it belongs
  to (quick-view of a product is §6.13's card expanded in
  place). Nothing floats above the page; wax does not hover.
- **Toast** — *refused.* Replaced by the day-book line: a record
  line that appears in the relevant section header (§6.8's
  tally) or the footer (§6.17) — news in this house is written
  in the book, not floated.
- **Tooltip** — *refused.* Replaced by the stamped label (§6.2's
  cell labels) and by captions; if a thing needs explaining,
  it gets a sentence (§12), not a hover secret.
- **Badge** — a cap dot (§6.8's seal at label size) with its
  word beside it in cell-label type. Percentage badges are
  banned absolutely (§12).
- **Alert / notice** — a propolis band: `--propolis` ground,
  `--wax` text, a `--honey` hairline at its top flat. Errors
  inside forms use §6.14's margin notes instead.
- **Pagination** — *refused* for the shop (the comb is long;
  filters narrow it). For the journal: a two-cell "older pour /
  newer pour" pair — pours are dated, pages are not numbered
  into infinity.
- **Data table** — the ledger: ruled rows on `--wax-pale`,
  figures right-aligned in data type, the header row capped
  (a `--wax-shadow` fill). Dense data grids are refused (§1).
- **Card** — §6.13's comb-cell card. No other card exists.
- **Progress bar** — *refused.* §6.2's comb is the progress.
- **Spinner** — *refused.* §6.16's empty comb is the loading.
- **Skeleton** — §6.16.
- **Breadcrumb** — *refused.* A candleworks is small; the comb
  strip (§6.11) and the side comb (§6.2) locate the visitor.
  Deep sites split (§6.11) rather than breadcrumb.
- **Search** — a ruled input in the shop header; results filter
  the comb live; empties resolve to §6.18 at section scale.
- **Price display** — data type, unit word in `--comb-deep`;
  struck prices in `--propolis` (§6.13). Currency is a record
  and never wears honey.
- **Image frame** — §6.9's wax frame / §6.5's mask. No other
  image treatment exists on the site.
- **Divider** — cooling space (§4): 40px of ground. Rules and
  hairlines are refused between sections; the comb at the side
  is the only continuous structure.

## 12. Content & copywriting voice

Two registers, kept apart the way §3 keeps the faces apart.

**The Chandler** — the maker's voice: warm, plain, first-person
plural, material before metaphor. Headlines, standfirsts, empty
states, errors, confirmations. Sentences are short; claims are
checkable; the exclamation mark is banned (warmth is not volume).

**The Record** — the day-book's voice: figures, dates, counts,
prices, tallies. No adjectives. If a line contains a number, the
Record wrote it, and §10 gate 3 can audit it.

**Headline law.** ≤30 letters for the melting headline (§6.1);
section headlines ≤6 words; every headline is a declarative
fragment about material or use. ✓ "Poured on Tuesdays, lit all
winter." ✓ "Why a hexagon." ✗ "Indulge in nature's golden glow!"
✗ "Our amazing handcrafted luxury candles" (three adjectives,
no facts, one banned mark).

**Label law.** Cell labels are stamped, short, and literal:
SHOP THE CANDLES, THE MAKING, YOUR COMB. Buttons say what
happens: "Seal the order", "Cap this cell". ✗ "Submit", ✗
"Click here", ✗ "Add to cart" (the cart does not exist here).

**Figure law.** Numbers live in sentences and in evenings:
✓ "about 14 evenings" ✓ "312 cells in a frame, give or take
the corners" ✗ "burns 50 hours!" ✗ "10,000+ happy customers"
(unowned, unauditable). Approximation is honest and verbal
("about", "give or take") — never a rounded-up integer wearing
a plus sign.

**Error voice (the Chandler, apologising like a person).**
✓ "That direction won't carry — the @ is missing, looks like."
✓ "The wax can't set without a name." ✗ "Invalid input."
✗ "Oops! Something went wrong :(" — the theme has no "oops";
things in a workshop are stated plainly and fixed.

**Empty voice.** ✓ "This cell is empty." ✓ "Your comb is
empty — the shelf is above." ✓ "Nothing is stored under that
name." ✗ "No results found." ✗ any sentence with a bee pun.
**Bee puns are banned absolutely** — "bee happy", "buzz",
"hive five" — the fastest route to §9 failure 1 is a pun.

**Fixed strings (verbatim, do not paraphrase).** The science
section's unit sentence: "An evening is one burning, about
three hours at a table." The seal confirmation: "Capped. It's
in your comb." The order confirmation's closing: "We'll pour
on Tuesday." The footer's closing line: "Poured, capped and
kept — the Alderwick day-book." (the house name is the site's
own; the structure is fixed). The 404's first line: "This cell
is empty."

**Banned words.** amazing, indulgent, luxury (as an adjective),
glow-up, buzz, bee-happy, artisanal (say who made it instead),
"hours" in product copy (§1 unit law). **Owned words.** pour,
cap, cell, comb, evening, settle, warm, store, day-book, shelf.

## 13. Full-page scroll choreography map

The home page, top to bottom. Every beat names its element and
its trigger; anything not on this map does not move (§15 step
12 audits the build against the map).

1. **Arrival (t=0).** Page printed whole. Masthead's current
   cell pours (§6.11) as the hero glow warms (§6.12/§6.1).
2. **The melt (t≈250–1800ms).** Headline letters settle; the
   last letter drips and snaps (§6.1). Standfirst melts in;
   fact cells stagger (§6.12).
3. **Hero exit.** Photograph plate parallaxes 0.94×; the pulse
   hands over at 2000ms and dies as the hero leaves (§6.12).
   Side-comb cell 1 fills as the hero's end-marker crosses
   (§6.2) — the first stored honey.
4. **The shop.** Section melt-in (§5). The pool fades in at its
   first anchor as the grid reaches 30% (§6.6); frames begin
   warming as they approach the centre (§6.9). The reader caps
   cells (§6.8); the header comb grows.
5. **The science.** Diagram draws (§6.7, 1600ms); counters
   arrive (§6.15); only then the photograph's hex-mask opens
   (§6.5). Comb cell for the section fills at its end.
6. **The making (the pin).** The room darkens to `--hive`. Over
   120vh: bead, stretch, neck, fall, splash (§6.4), the three
   paragraphs ruling in turn. The visitor's scroll is the pour.
7. **The pricing approach.** Drips over the section lengthen
   from 0.3 to full as the section approaches (§6.3) — the
   candles of §6.4 melt, conceptually, into their prices.
8. **Pricing read.** Drips hold. Cards here are walled cells
   with the club terms in the Record register; the longest drip
   hangs over the longest candle.
9. **The order.** Carried caps arrive as lines (§6.14); the
   burn-total counts the order into evenings; sealing pours
   the big seal.
10. **The day-book.** The footer's rule draws; the visit tally
    prints the same numbers the comb has been showing (§6.17).
    The page ends in agreement with itself.
11. **Reverse pass.** Scrolling up: drips shorten (§6.3), the
    pinned drip un-pours (§6.4), frames cool (§6.9) — but fills
    stay filled, caps stay capped, counts stay counted. What
    was gathered is kept; only the weather reverses. This
    asymmetry is the theme's physics and §10 gate 1 samples it.

## 14. Whole-page performance budget

- **Total page weight:** ≤780KB (home), of which images ≤520KB
  (wax frames forgive compression; photographs are warm-toned
  and compress kindly — use it), inline SVG (diagram, drips,
  seals) ≤48KB total, fonts ≤120KB (Fraunces variable subset +
  Work Sans, `woff2`, display subset excludes unused axes).
- **Frame budget:** the shared loop's total work ≤1.6ms/frame
  on a mid-tier phone; per-element budgets are stated in §6 and
  sum to ≤1.4ms with all systems live (pool + warmth + drips +
  pin) — the remaining 0.2ms is headroom the gate measures, not
  spends.
- **Long tasks:** none >50ms after load; the ceremony (§6.1)
  splits its letter-wrapping across two frames if the headline
  exceeds 20 letters.
- **Counts:** ≤4 hex-masked images, ≤6 counters, ≤12 warmth
  frames, 1 pool, 1 pin, 18 comb cells — the §6 budgets are the
  page budget, enforced by §10's census.
- **Cut order** (when the budget is exceeded, cut in this order,
  never improvise): (1) the light pool on the second grid, then
  the first (§6.6); (2) hero plate parallax (§6.12); (3) hex-mask
  rings reduce (larger cells, §6.5); (4) card tilt (§6.13);
  (5) comb diagram's label-hover response (§6.7); (6) the pinned
  drip's splash arcs (§6.4 — the fall itself is never cut).
  **Never cut:** the comb's fill truth (§6.2), any fallback or
  watchdog, the counters' landing accuracy (§6.15), the form's
  error-keeping (§6.14). A build that cuts a never-cut to save a
  cut-list item has failed the gate regardless of its frame rate.

## 15. Build-order checklist

1. Print the static page first: full content, drawn diagram,
   filled-to-index comb, printed figures, submittable form —
   the no-JS state is the foundation, not a fallback.
2. Lay the comb geometry: grid registers, shared walls, the
   rail's reserved margin; census the hexagons (§10 gate 8).
3. Build the data objects: product records (evenings, prices),
   the section registry, the completion record — one source
   each, before any element reads them.
4. Measure the hero composite contrast with the real photograph
   (§6.12) and adjust the plate, never the text.
5. Masthead (§6.11) and footer (§6.17) — the two still rooms.
6. Hero panel and the melting headline (§6.12, §6.1) with its
   watchdog; rehearse the font-race loss.
7. The filling comb (§6.2) against the registry; script the
   gate-1 audit now, while the record is young.
8. Shop grid: cards (§6.13), frames (§6.9), cap (§6.8), pool
   (§6.6) — in that order, each on the previous one's hooks.
9. Science: diagram (§6.7), counters (§6.15), mask reveal
   (§6.5) with its sequencing gate.
10. The making pin (§6.4) and pricing drips (§6.3); sample the
    drip-function audit (§10 gate 4).
11. The order form (§6.14) wired to §6.8's stored list; rehearse
    gate 7's three failures.
12. Skeleton (§6.16), curtain (§6.10), 404 (§6.18). Audit every
    moving thing against §13's map and §5's durations ledger —
    an unlisted motion is removed, not documented.
13. Rehearse the curtain's failure paths (swap timeout, router
    error) — its watchdog is load-bearing (§6.10).
14. Reduced-motion pass: every element's variant, verified one
    by one against §6 — not a global "disable animations"
    switch.
15. Run §10's gate end-to-end; a non-builder signs. Then, and
    only then, light the candles.
