# 56. Frost Fern — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened not redesigned).**
Window frost growing in real time: fern-like crystals spread from the
screen's corners as you linger, and the page is a pane of glass between
the reader and a warm room beyond. Palette anchors: Frost `#EDF1F2`,
ice fern `#C7D5DA`, cold glass `#7E97A3`, winter dusk `#3E5A66`,
lamplight beyond `#E8A24B`. Type: Spectral (display), Inter (body).
All ten original signature elements are kept and deepened — corner
frost growth, the wiped-clear headline patch, idle growth / scroll
melt, amber interior glow, margin fern progress, hover thumbprint
melt, breath-fog click, science fern draw, frosted image frames, the
CTA thumbprint — and eight page-family elements are added to reach
eighteen full build specs.

## 1. Concept & world

The visitor is outside, in the cold, looking in. Every page built in
this theme is a single pane of glass: on the far side of it a warm,
lamplit room holds the site's real content — cabins, menus, booking
forms, photographs of firesides — and on the near side, the visitor's
side, frost is growing. The frost is not a background image and it is
not a loading ornament. It is the page's clock and its weather: it
advances while the reader stays still, retreats while the reader
moves, thins over warm content and thickens over cold margins, and it
is grown, melted, wiped and breathed on by the reader's own behaviour.
The site's inhabitant — the host, the keeper, the person inside the
warm room — has wiped two clearings in the frost before the visitor
arrived: one around the headline, so the house can introduce itself,
and one around the call to action, so the door can always be knocked
on. Everything else the visitor must earn by moving, hovering and
touching, exactly as a real visitor at a real frozen window earns a
clearer view by leaning closer and wiping with a warm hand.

**The theme's one law: the frost frames the glass; it never takes
it.** Frost coverage is capped at a declared maximum (38% of the
viewport's area, §2's `--frost-cap`), measured as rendered coverage,
not as a hope; and the two clearings — the headline patch (§6.2) and
the CTA thumbprint (§6.10) — are exclusion zones written into the
frost layer's mask geometry, so no growth step, no idle advance, no
transition and no bug in the growth engine can ever freeze over the
site's name or its door. A build in which frost can cover the
headline or the CTA has not implemented this theme; it has
implemented a screensaver with a website trapped behind it. The
second, supporting law: **frost is behaviour, not decoration** —
every change in coverage traces to a declared cause in §5's growth
model (idle time, scroll velocity, pointer warmth, section warmth,
a click of breath). Frost that thickens on a timer unrelated to the
reader is a gate failure (§10).

**Best-fit sites.** Winter hospitality above all: mountain cabins,
ski lodges, ice hotels, sauna-and-cold-plunge retreats, winter
wedding venues, Christmas markets and seasonal pop-ups, a
glögg or winter-menu restaurant, a Northern Lights tour operator.
Second circle: anything whose product is warmth behind cold —
heating and insulation firms with a sense of humour, a winter
clothing maker's seasonal campaign, a cold-water swimming club, a
glacier or polar science outreach site (the science fern, §6.8, was
born there), a winter festival. The audience is a visitor who is
being invited *in*: the theme's whole rhetoric is threshold —
outside/inside, cold/warm, frost/clearing — so it fits any offer
structured as "come in from the cold".

**When NOT to use it.** Not for content that must be scanned at
speed: dashboards, documentation, news, comparison tables, checkout
funnels with more than one decision per screen (the frost's idle
growth punishes exactly the pausing that dense content demands —
see §6.3's reading-pause exemption, which mitigates but does not
abolish this). Not for sites whose brand is summer, speed, or
clinical sterility. Not where the primary audience is on very
low-powered devices with no reliable rAF (the fallback is honest —
static frost frame — but the theme without its behaviour is a
picture frame, and a plainer theme serves better). Not for pages
longer than ~9 sections: the growth model's drama is calibrated to
a single sitting at one window; a 40-section page exhausts the
metaphor and the coverage budget alike.

**The emotional register.** Quiet, held, slightly lonely at the
edges and warm at the centre. Nothing in this theme bounces, pops
or shouts; the fastest motion on the page is a breath clearing
(§6.7). If a build feels playful, it has drifted; if it feels like
a horror film's frozen window, it has drifted further — the room
beyond is always lit, always inhabited, always glad the visitor
came.

## 2. Palette

Five anchors, inherited unchanged, plus a closed derived list. The
palette's logic is thermal: three cold tones build the glass, one
warm tone is the entire interior, and one deep tone is the night
the glass is set into. Lamplight is the only warm colour on the
page — the Verdigris-style rationing of §9 failure 4 applies: the
moment amber appears anywhere except *through* the glass, on
genuinely warm content, the metaphor collapses into decoration.

| Token | Hex | Role | Usage ratio | Pairing & contrast |
|---|---|---|---|---|
| `--frost` | `#EDF1F2` | The crystal field itself; page ground at the margins | ~34% of viewport at rest | On `--dusk` 6.46:1 — the only cold tone licensed for text, and only on dusk |
| `--fern` | `#C7D5DA` | Ice-fern crystal strokes, fern frond, rims | ~8% | On `--frost` 1.42:1 — graphical only, by design: crystals are read by shape, not contrast |
| `--glass` | `#7E97A3` | Cold glass mid-tone: frames, rules, the pane's unlit areas | ~14% | On `--frost` 2.70:1 — never text; on `--dusk` 2.39:1 — never text |
| `--dusk` | `#3E5A66` | Winter dusk: the night ground behind the glass, footer field, nav field | ~30% | `--frost` on it 6.46:1 (body text ✓); `--lamp` on it 3.40:1 (display ≥24px only) |
| `--lamp` | `#E8A24B` | Lamplight beyond: interior glow, warm content's light, the CTA's warmth | ~9%, always *behind* glass | On `--dusk` 3.40:1 (display only); on `--frost` 1.90:1 — never text on frost, ever |

**Derived tokens (closed list — no others may be coined).**
`--ink` `#243A43` (dusk deepened for body text on clear glass and
frost: on `--frost` 10.51:1, the page's workhorse text colour);
`--ink-warm` `#4A3220` (body text inside warm interior panels, on
`--room` 8.94:1); `--room` `#F5E7CE` (the warm interior's lit wall —
the ground of content panels seen through clearings, never a page
background in its own right); `--frost-deep` `#D9E4E8` (frost at
double density, used at rims and corners where crystals stack);
`--bead` `#B9CCD4` (melt droplets on rims and thumbprint edges);
`--lamp-deep` `#C47E27` (lamplight at the wick — focus rings on warm
elements, the CTA's pressed state; on `--dusk` 4.62:1, the only
lamp tone licensed at small sizes).

**Contrast rulings (measured for this expansion, blocking at §10).**
Body text is exactly two pairings: `--ink` on `--frost`/clear glass
(10.51:1) and `--ink-warm` on `--room` (8.94:1), plus `--frost` on
`--dusk` (6.46:1) for the night fields. `--lamp` never carries text
below 24px. `--glass` and `--fern` never carry text at any size —
they are the window, not the words. Crystal strokes at 1.42:1
against their ground are licensed because they are pure ornament
with a coverage cap and two guaranteed clearings; the instant a
crystal is asked to *mean* something (the fern progress, §6.5), it
is drawn in `--glass`-on-`--dusk` margin housing or paired with a
text equivalent (§6.5's accessibility spec).

**Dark-mode ruling: the page is already the night.** There is no
light scheme to invert to and no dark scheme to deepen into; a
Frost Fern page at `prefers-color-scheme: dark` is identical, and
at `light` is identical — the visitor is outside at dusk either
way. Print is the exception: the print stylesheet drops the frost
layer entirely and prints the warm room alone, ink on room, because
paper is not glass.

## 3. Typography

**Faces.** Spectral (display, 300/400/600 with italics) — a serif
with frost-feathered stroke endings at display sizes, chosen
because its light weight reads as breath-thin without going
fragile; Inter (body, 400/500/600) for everything the visitor must
actually use. No third face. Numerals for data (§6.16) are Inter
tabular.

**Scale (desktop ≥1200px; root 16px).** Display 56px/1.04 Spectral
300, tracking −0.01em — the headline in its wiped patch (§6.2).
H2 34px/1.12 Spectral 400. H3 22px/1.25 Spectral 600. Body 17px/1.62
Inter 400. Small 14px/1.55. Caption/label 12px/1.4 Inter 600,
uppercase, tracking 0.14em — labels are the keeper's handwriting on
the glass: sparing, spaced, never a headline's costume. Data figures
28px Inter 500 tabular.

**Five type laws.**
1. **Type never sits under frost.** Any text node's region is either
   inside a clearing (headline patch, thumbprint, hover melt), on a
   night field (`--dusk`), or in the frost-free reading column the
   coverage model guarantees (§4). A build that lets body copy drift
   beneath the crystal field has broken the law in §1, whatever its
   coverage percentage says.
2. **Spectral is the room's voice; Inter is the glass's.** Headings,
   standfirsts, pull-quotes and the keeper's notes are Spectral —
   they come from inside. Labels, figures, form furniture and
   navigation are Inter — they are written on the window.
3. **Cold text is quiet text.** Display weight never exceeds 600
   and body never bolds for emphasis; emphasis inside cold copy is
   italic Spectral or a move to `--lamp-deep` at display size. The
   page whispers because the visitor is close to the glass.
4. **Line-height loosens as warmth rises.** Body at 1.62 in cold
   sections, 1.7 inside warm interior panels (§6.4) — warm air
   expands; the leading is the room breathing. This is set per
   section, never animated.
5. **Figures are temperatures, not statistics.** Every number the
   theme prints is a temperature, a snowfall, a distance through
   snow or a count of nights — §6.16's counters refuse any figure
   that could not be read off a thermometer, a ruler in the snow or
   a booking ledger.

## 4. Layout language

**The pane.** The page is one fixed pane: a `position: fixed`
frost layer (`inset: 0`, `pointer-events: none`, z-index above
content, below nothing interactive — it must never intercept a
click, and its `pointer-events: none` is a §10 gate, tested, not
assumed) floats over the scrolling room. The room scrolls; the
glass does not. This single decision generates the theme's whole
layout grammar: content is *behind* something, so every section is
composed as a view through a window — centred, framed by cold
margins, with its warmest element placed where the frost is
thinnest.

**The reading column and the cold margins.** Content column max
68ch, centred ≥1200px. The margins outside it are the frost's home
territory: crystals own the outer 18% of the viewport width on each
side and may advance to the column's edge but never into it — the
coverage model's geometry (§5) is expressed in these zones.
Sections alternate **cold passages** (copy on `--frost` ground,
frost at full local density around them) and **warm rooms**
(§6.4: content on `--room` panels, glow scrubbed, frost locally
thinned to ≤40% of its margin density). A page is a walk past a
lit house: cold glass, warm window, cold glass, warm window.

**Spacing rhythm.** Base unit 8px; section padding 120px desktop,
72px tablet, 48px mobile — winter pages are spacious because the
frost needs room to be frost in. The fern margin (§6.5) lives in
the left cold margin ≥1200px (a 72px-wide housing on `--dusk`);
below that it retires to a compact form (§6.5 breakpoints).

**Density law.** At most one warm room per viewport; at most one
pinned scene per page (the cabin interior pin, §5); the CTA
thumbprint (§6.10) appears at most twice on a page (hero-adjacent
conversion block and footer approach) and the two instances share
one re-bead clock so the page never pulses in two places at once.

**The clearings are layout, not effects.** The headline patch
(§6.2) and thumbprint (§6.10) are reserved geometry in the grid:
the hero reserves the patch's ellipse before any frost is drawn,
and conversion blocks reserve the thumbprint's oval. Frost is drawn
*around* reservations — exclusion by construction, not by cleanup.

## 5. Full motion system

Five named easings, each a temperature of movement:
`--ease-grow` `cubic-bezier(0.22, 0.61, 0.21, 1)` — crystal growth:
a slow committed start, branching acceleration, a hard stop (ice
does not overshoot); `--ease-melt` `cubic-bezier(0.33, 1, 0.68, 1)`
— melting: quick to start weeping, long tail of drips;
`--ease-wipe` `cubic-bezier(0.65, 0, 0.35, 1)` — a hand passing:
symmetric, deliberate; `--ease-thaw` `cubic-bezier(0.16, 1, 0.3, 1)`
— thawing reveals: long soft arrival; `--ease-glow`
`cubic-bezier(0.45, 0, 0.55, 1)` — lamplight breathing: near-linear,
barely a curve at all.

**The growth model (the theme's engine, declared once, used by
§6.1/§6.3/§6.4).** State is a single number, coverage `C`
(0–`--frost-cap` 0.38), plus a per-corner growth front. One shared
rAF loop (lerp 0.12 for scrubbed values, §14) integrates: **idle**
(no scroll input for 3000ms) → `C` rises one growth step per
2500ms, each step +0.008 coverage, drawn as corner crystals
advancing ~14px along their fronts; **scroll velocity above
400px/s** → `C` falls at 0.02 per 100px travelled beyond the
threshold, drawn as edge melt; **velocity below 400px/s** → `C`
holds (reading is not melting; §6.3's exemption). Warm rooms
(§6.4) multiply local density by a scrubbed warmth factor
1→0.4 as they centre. Jump scrolls, keyboard paging and scrollbar
drags are inputs like any other: velocity is computed from
position deltas in the loop, never from wheel events, so every
input method melts and freezes identically.

**Term by term.** *Scroll-triggered reveals:* interior elements
stagger in glowing (§6.12's hero; §6.4's rooms) — lamps lit one by
one, 90ms stagger, `--ease-glow`. *Scroll-driven/scrub animation:*
coverage, warmth, image-rim retreat (§6.9), the sun-disc — no,
this theme has no sun; the scrubbed quantities are coverage,
warmth factor, rim retreat and fern growth (§6.5), all from the
one loop. *Parallax:* the frost layer translates at 0.92× against
the room (it is nearer the visitor than the room is), warm glows
at 1.06×; both clamp to ±14px and re-converge at section
boundaries so the pane never drifts off its frame. *Pinned
sections:* exactly one — the cabin interior (§6.12 map) pins
behind nearly-clear glass for 160vh while frost creeps only at
the corners; the pin is the theme's held breath. *Masked reveals:*
the headline's centre-out clearing (§6.2) and the science fern's
growth-order draw (§6.8). *Blur-to-sharp:* refused — frost is not
blur; crystals are drawn geometry, and blurring text is §9 failure
2. The single licensed blur is the breath-fog's own softness
(§6.7), applied to the fog, never to content. *Kinetic
typography:* refused — letters do not move in the cold; the
headline's frost-edging (§6.2) is a mask change, not motion of
type. *Marquee:* refused — nothing parades past a winter window.
*Counters:* §6.16, counting only thermometer-and-ledger figures.
*Progress indicator:* the margin fern (§6.5). *Hover/magnetic/
tilt:* thumbprint melt (§6.6), pane-lean card tilt ≤3° (§6.13);
magnetic pull refused — glass does not attract. *Custom cursor:*
refused, standing rule; the system cursor is the visitor's own
hand, and §6.6 gives it warmth to work with. *Skeleton loading:*
§6.15. *Page transitions:* §6.15's frost-over and hand-wipe.
*Reduced motion:* §6 per element; globally, coverage rests at a
fixed decorative frame (C = 0.18, corners only), clearings open,
glow steady — the finished still pane.

**Durations ledger (extract).** Corner growth on load 2000ms;
idle step 2500ms cadence; headline edge-frost 600ms, clearing
900ms; fern branch unfurl 400ms; thumbprint follow lerp 0.15,
re-freeze 1200ms; breath bloom 300ms, clear 900ms; fern draw
2000ms; rim retreat scrubbed; thumbprint re-bead 6000ms cycle,
pulse 800ms; glow stagger 90ms; transition frost-over 700ms,
wipe 800ms.

## 6. Signature elements

### 6.1 Corner frost growth

- **What & why.** On load, dendritic fern crystals branch inward
  from all four frame corners across ~2000ms and settle into the
  page's resting frame. It belongs because it is the theme's first
  sentence: before a word is read, the visitor learns they are
  outside looking in, and the glass is alive. The growth is drawn,
  not faded — crystals *branch*, in the order ice actually forms:
  a primary stem, then sub-branches at ~40° in the dendritic
  habit, then needle side-shoots.
- **Structure.** Four inline SVG groups pinned to the corners of
  the fixed frost layer (§4), each an authored set of stroked
  paths in `--fern` over a soft `--frost-deep` underlay shape.
  Branching is authored per site (a crystal is a drawing, not a
  particle system — §9 failure 6), with per-path `pathLength`
  normalised so growth is a `stroke-dashoffset` scrub. The four
  groups share one growth variable from §5's model; each path's
  draw window is its authored distance from its corner, so the
  front advances geometrically, not path by path. Hard geometric
  stop: no path's endpoint comes within 120px of the headline
  patch's ellipse (§6.2) or within the reading column (§4) —
  enforced by the authored coordinates and audited at §10.
- **Motion spec.** Trigger: load, gated on first paint (not fonts —
  crystals are geometry, they need no face). Growth runs 2000ms
  `--ease-grow`, the four corners starting together, fronts
  advancing at authored rates (top corners 1.0×, bottom corners
  0.85× — frost climbs a pane unevenly). At completion the layer
  hands control to §6.3's idle/melt model at C = 0.18. Repeats:
  never on the same page view; `sessionStorage` visitors returning
  to the page find the frame already grown (growth is a first
  meeting only).
- **States.** Ungrown (JS-armed only, dashoffset full) → growing →
  resting frame (rest). Hover/focus/active: none — the frame is
  not a control. Scrolled-past: the frame is fixed; it does not
  scroll away, it *is* the window.
- **Content merge.** The crystals frame the actual page — they grow
  on the glass the reader is looking through, around the real
  content, and their authored stop-lines are drawn from the real
  hero's geometry. Remove the content and the frame is meaningless;
  that is the test it passes.
- **Failure fallback.** Watchdog at 2600ms: if growth has not
  completed (rAF stalled, tab backgrounded), dashoffsets snap to
  final. No JS: the SVGs ship fully drawn — the frame is printed,
  the page complete. Slow network changes nothing; the layer is
  inline.
- **Reduced-motion variant.** The frame ships grown. No growth
  ceremony; the pane simply has its winter frame, as a printed
  winter scene does.
- **Performance budget & mobile variant.** Four SVG groups ≤18KB
  inline total; animation touches `stroke-dashoffset` only.
  Mobile (<768px): two corners only (top-left, bottom-right — the
  diagonal the eye travels), paths thinned by authored omission
  (the mobile groups are separate, smaller drawings, not scaled
  desktop ones), growth 1600ms.
- **Choreography timeline (v2).** t=0 first paint → t=0–2000
  fronts advance, sub-branches firing as their stem positions are
  passed (a branch begins when the front reaches its root, +0ms)
  → t=2000 rest at C = 0.18 → t=3000 idle clock starts (§6.3 may
  begin advancing the same fronts).
- **State matrix (v2).** *Rest:* grown frame, C = 0.18. *Hover:*
  none. *Focus:* none — the layer is `aria-hidden` and unfocusable.
  *Active:* n/a. *Scrolled-past:* n/a (fixed layer). *Disabled /
  no-JS:* fully drawn at first paint. *Touch:* identical; growth
  does not wait for a first touch.
- **Breakpoints (v2).** ≥1200px: four corners, full drawings,
  2000ms. 768–1199px: four corners, sub-branch density −30%
  (authored), 1800ms. <768px: two corners, 1600ms, stop-line
  distance to patch 72px (the patch itself shrinks, §6.2).
- **Edge cases & failure modes (v2).** *Very tall hero:* stop-lines
  are measured from the patch, not the viewport, so a tall hero
  never lets a front cross the column. *Resize mid-growth:* fronts
  are drawn in SVG user units against a `preserveAspectRatio=
  "none"`-free, corner-anchored viewBox per corner group — resize
  rescales the corner drawing, growth fraction is unitless and
  survives. *Second page in session:* printed frame (see Motion
  spec). *WebGL/canvas absent:* irrelevant — the layer is SVG.
- **Accessibility spec (v2).** The whole frost layer is
  `aria-hidden="true"`, `pointer-events: none`, absent from the
  accessibility tree and the tab order. It carries no information:
  everything it frames is in the room beneath, fully readable —
  contrast of content is measured with the layer removed (§10),
  because the layer may never be load-bearing.
- **Tokens consumed (v2).** `--frost`, `--frost-deep`, `--fern`,
  `--ease-grow`, `--dur-grow-load` (2000ms), `--frost-cap` (0.38),
  `--coverage-rest` (0.18).

### 6.2 The wiped-clear headline patch

- **What & why.** The hero headline sits in an irregular clear
  patch in the frost — a radial clearing with a hand-smudged edge,
  as if the keeper inside wiped the glass with a warm palm so the
  house could speak. On entry the headline's letters frost at
  their edges, then clear from the centre outward. It belongs
  because it is the theme's thesis in one gesture: communication
  across the cold is an act of warmth, performed by someone
  inside. It is also the law's (§1) first exclusion zone — the
  patch can never freeze over.
- **Structure.** The hero reserves an elliptical region (§4) sized
  to the headline + standfirst + 48px of smudge margin. The frost
  layer's mask carries this ellipse as a permanent hole with a
  feathered, irregular edge (an authored SVG mask path — a wobbly
  ellipse with three palm-drag lobes, never a clean CSS radial
  gradient, §9 failure 3). The headline is a real `<h1>` in the
  room beneath. Its frost-edging is a duplicate text layer
  (`aria-hidden`) clipped to the glyph edges via an SVG mask,
  filled with a `--fern`-to-transparent gradient, armed by JS.
- **Motion spec.** Trigger: load, after §6.1's fronts pass the
  patch's latitude (~t=900ms). Edge-frost fades in over 600ms
  `--ease-grow`; hold 250ms (the visitor sees the name *through*
  a breath of frost); clearing runs 900ms `--ease-wipe`, the clear
  mask's radius scrubbing 0→full from the headline's optical
  centre — centre-outward, the way a palm's heat spreads. Total
  ceremony ≤2000ms. Runs once; returning session visitors get the
  patch already clear, letters clean.
- **States.** Frost-edged (JS-armed only) → clearing → clear
  (rest). Hover: none. Focus: focus entering the hero completes
  the clearing instantly — a keyboard visitor is never asked to
  wait for weather before reading the name. Scrolled-past
  mid-ceremony: the ceremony completes on its own clock; the patch
  is fixed in the hero, scrolling away leaves it clear for the
  return.
- **Content merge.** The headline is the site's name and subject;
  the patch is not a vignette around it but the reason it can be
  read at all — the clearing *is* the introduction, and the
  standfirst beneath is set inside the same clearing, in the
  keeper's Spectral voice (§3 law 2).
- **Failure fallback.** Watchdog at 2400ms from load: edge layer
  removed, patch at full clear. No JS: no edge layer exists, the
  patch is a static mask hole, the headline printed and readable
  at first paint. The mask hole is CSS/SVG, not JS — the clearing
  cannot be lost to a script failure.
- **Reduced-motion variant.** No edging, no clearing. The patch is
  simply clear, the headline clean — the information (this name
  was wiped clear for you) survives as the patch's visible smudged
  edge in the resting frost.
- **Performance budget & mobile variant.** One mask path + one
  duplicate text layer; the clearing animates a mask radius via
  `clip-path` on the edge layer only — the real `<h1>` is never
  repainted. Mobile: patch sized to the stacked hero (headline,
  then standfirst below), edge-frost omitted (letters at 34px have
  no edges worth frosting — the ceremony becomes a simple 600ms
  clear), smudge margin 28px.
- **Choreography timeline (v2).** t≈900 fronts pass → t=900–1500
  edges frost → t=1500–1750 hold → t=1750–2650 clearing
  centre-out → t=2650 rest; watchdog 2400 measured from load
  forces rest if the sequence is interrupted (tab switch) —
  the hold is the only beat that may be skipped, and skipping it
  is what the watchdog does.
- **State matrix (v2).** *Rest:* clear patch, clean letters.
  *Hover:* none. *Focus:* instant clear (above). *Active:* n/a.
  *Scrolled-past:* clear. *Disabled/no-JS:* clear, printed.
  *Touch:* identical; first tap anywhere completes a running
  clearing.
- **Breakpoints (v2).** ≥1200px: full ceremony, patch ellipse
  ~min(880px, 86vw) wide. 768–1199px: ceremony kept, hold cut to
  150ms. <768px: simplified clear (above), patch = full-width band
  with smudged top/bottom edges.
- **Edge cases & failure modes (v2).** *Long headline (3+ lines):*
  the patch is sized from the rendered headline box + margin at
  build/layout time, never a fixed ellipse — a wrapped name gets
  a taller clearing, and §10 checks the smudge edge clears the
  last line's descenders by ≥24px. *CMS-edited headline:* patch
  geometry is computed from the live box on load (one
  `getBoundingClientRect` before first frost draw), so an edited
  name re-reserves its clearing. *Font swap:* the edge layer is
  armed only after `document.fonts.ready`; a swap after arming
  disarms it (letters would misalign with their frost).
- **Accessibility spec (v2).** The `<h1>` is complete in the tree
  from first paint; edge layer `aria-hidden`. Contrast inside the
  patch is the room's own: `--ink` on `--frost` 10.51:1, unaltered
  by the ceremony at every frame because the readable layer is
  beneath the effect layer, whole.
- **Tokens consumed (v2).** `--frost`, `--fern`, `--ink`,
  `--ease-grow`, `--ease-wipe`, `--dur-edge-frost` (600ms),
  `--dur-clear` (900ms), `--dur-fallback-hero` (2400ms).

### 6.3 Idle growth / scroll melt

- **What & why.** The pane's living behaviour: after 3s without
  scrolling, corner crystals advance one growth step every ~2.5s,
  up to the coverage cap; scrolling faster than ~400px/s melts
  growth back from the edges at the same rate. It belongs because
  it makes the reader's own conduct the weather — lingering
  freezes your view, moving thaws it — and that *is* the winter-
  cabin experience the theme sells. No other element in the theme
  matters if this one is faked with a timer (§5's second law).
- **Structure.** Not a DOM element but the behavioural layer over
  §6.1's SVG fronts, driven by §5's growth model: state `C`,
  per-corner front offsets, an idle clock, and velocity computed
  in the shared rAF loop from scroll-position deltas (never wheel
  events). Growth steps select the next authored sub-branch
  segments on each front (the drawings carry ~26 steps of headroom
  beyond the resting frame, authored as the paths' outer thirds);
  melt reverses the same segments in reverse order — the frost
  retreats along the paths it grew on, never by fading.
- **Motion spec.** Idle threshold 3000ms without scroll input;
  step cadence 2500ms; step size +0.008 coverage (~14px of front
  advance); cap `C ≤ 0.38` — at the cap, growth stops and the
  fern (§6.5) gives one slow pulse (§6.5) to say the glass is as
  frozen as it is allowed to get. Melt: velocity >400px/s removes
  0.02 coverage per 100px travelled, applied to the outermost
  segments first, `--ease-melt` per segment (300ms). Velocity
  <400px/s: hold — **the reading exemption**: slow reading scroll
  neither grows nor melts; growth resumes only after a full 3000ms
  of *no input at all*. Both directions are scrubbed through the
  loop's lerp (0.12), so a fling melts in a smooth retreat, not a
  jump-cut.
- **States.** Resting (C = 0.18, no input <3s) → growing (idle) →
  capped (C = 0.38) → melting (fast scroll) → resting. The model
  has no other states; in particular there is no "growing while
  scrolling slowly" state — that is §9 failure 5.
- **Content merge.** The behaviour is applied to the page's own
  glass over the page's own content; its meaning is the reader's
  relationship to *this* visit's pace. It merges by being the
  medium itself, not an effect on top of it.
- **Failure fallback.** If the loop dies (JS error, rAF throttled
  to nothing in a background tab), coverage freezes at its last
  value — which is always ≤ cap and always leaves both clearings
  open, so the worst case is a static frame: the no-JS state by
  another route. A 5000ms loop-stall watchdog (§14) additionally
  steps C back to the resting 0.18 if the tab was hidden mid-
  growth, so a returning visitor never finds a page that froze
  shut in their absence.
- **Reduced-motion variant.** The model is off. C rests at 0.18
  forever; idle does nothing, fast scroll does nothing. The pane
  is a still winter scene.
- **Performance budget & mobile variant.** The model writes at
  most four `stroke-dashoffset` values per frame and only on step
  boundaries; idle steps are 2500ms apart — the cheapest ambient
  system in the library. Mobile: step size +0.012 (two corners,
  §6.1, reach their fronts sooner), cap unchanged, melt threshold
  350px/s (touch flings are faster and shorter).
- **Choreography timeline (v2).** Continuous: t=last-input+3000
  idle arms → steps at +2500ms intervals → any scroll input
  disarms idle instantly (the current segment finishes its 300ms
  draw, no segment is left half-grown) → velocity >threshold melts
  from the same frame the threshold is crossed.
- **State matrix (v2).** *Rest:* as above. *Hover:* pointer
  movement is not scroll input — moving the mouse does not thaw
  the glass (only §6.6's local melt answers the pointer).
  *Focus:* keyboard scroll (arrows, Page Down, space) is scroll
  input with real velocity — melts and idles identically to wheel
  and touch. *Active:* n/a. *Scrolled-past:* the model is
  viewport-global, not per-section. *Disabled:* model off, frame
  printed. *Touch:* fling = melt; a held, still finger = idle.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: step
  cadence 2800ms (fewer branches to spend). <768px: as mobile
  variant above; growth steps also pause while the on-screen
  keyboard is open (a form being filled is not lingering, §6.14).
- **Edge cases & failure modes (v2).** *Reader reads without
  scrolling for minutes (long article, no input):* growth proceeds
  to the cap and stops; the reading column and clearings are
  geometrically unreachable (§4), so a capped pane is a heavy
  frame around a clear page — atmospheric, never obstructive; the
  first scroll of any speed >400px/s or any §6.6 hover begins
  relief. *Scrollbar drag to the bottom:* velocity is enormous;
  melt floors at C = 0.10 (a fast journey thaws the edges but the
  pane never goes fully clear by speed alone — arrival is not
  entry). *Find-in-page jumps:* treated as jump scrolls; C eases
  to the position's scrubbed value over 600ms, no segment pops.
- **Accessibility spec (v2).** The behaviour changes only the
  `aria-hidden` layer. Nothing it does is announced; nothing it
  covers is information (§6.1's spec). Keyboard and switch users
  get identical physics via position-delta velocity. A user who
  cannot scroll quickly can still clear any card by hover/focus
  (§6.6) and any section by its warmth (§6.4) — melt-by-speed is
  never the only way through the glass.
- **Tokens consumed (v2).** `--frost-cap` (0.38), `--coverage-rest`
  (0.18), `--coverage-floor` (0.10), `--idle-arm` (3000ms),
  `--step-cadence` (2500ms), `--step-size` (0.008), `--melt-line`
  (400px/s), `--ease-grow`, `--ease-melt`, `--lerp-scroll` (0.12).

### 6.4 Amber interior glow

- **What & why.** Warm sections — the cabins, the menu, the
  booking room — glow lamplight-amber *through* the frost, their
  glow radius scrubbed to how centred they are, and the frost over
  them stays thinner. It belongs because it is how the visitor
  navigates the page: warmth is visible before detail is, exactly
  as a walker in snow finds the lit windows of a house before its
  door. The glow is the theme's wayfinding.
- **Structure.** Each warm section is a `.room` panel on `--room`
  ground inside the reading column. Above it, in the frost layer,
  a corresponding glow shape: a radial-gradient disc in `--lamp`
  at low alpha, clipped to the panel's box, whose alpha and radius
  are written by the shared loop from the panel's viewport
  position; and the crystal field over the panel is drawn at the
  warmth factor's density (§5) — implemented as a second, sparser
  crystal group per room whose opacity is the complement of the
  warmth factor, crossfading against the standard-density group.
  The glow disc is `pointer-events: none`, `aria-hidden`, and
  lives entirely inside the frost layer.
- **Motion spec.** Trigger: scroll scrub, continuous. Warmth
  factor `W` = 1 at the panel's centre crossing the viewport's
  50% line, falling to 0 at ±65% viewport height (a declared
  bell, computed in the loop, lerp 0.12). Glow alpha 0→0.34 and
  radius 55%→100% of the panel box as `W` 0→1, `--ease-glow`.
  Frost density over the panel: 1→0.4 × margin density. No
  discrete animation fires; the room *breathes* warmer as it
  centres and cools as it leaves, both directions, symmetric.
- **States.** Cold (out of band, W = 0; panel readable on its own
  `--room` ground, frost at full local density at its edges) →
  warming → centred/warm (rest state while reading the room) →
  cooling. Hover: none of its own (§6.6 answers the pointer).
  Focus: focus inside a room drives `W` to ≥0.7 regardless of
  scroll position — a keyboard visitor's room is always lit.
- **Content merge.** The glow belongs to the rooms the copy is
  about — cabins with fires, a menu served hot, the booking desk
  by the hearth. It is not a highlight effect applied to sections;
  cold sections (§1's cold passages) have no glow shape at all,
  and §10 counts glow shapes against `.room` elements one-to-one.
- **Failure fallback.** Loop dead → glow discs at their CSS
  default (alpha 0.18, radius 80%) and crystal density at the
  mid value: every room looks mildly warm, every panel fully
  readable on `--room`. No JS: same defaults; warmth is a printed
  suggestion, content untouched.
- **Reduced-motion variant.** `W` is computed once from initial
  position and never scrubbed; rooms in view are warm, rooms out
  of view are at default. No breathing.
- **Performance budget & mobile variant.** One gradient disc +
  one opacity crossfade per room; ≤4 rooms per page (§4 density
  law keeps it ≤1 per viewport). Gradients are pre-rendered
  background images, not live `filter: blur` — blur on a fixed
  full-screen layer is §9 failure 2. Mobile: glow radius capped
  at 90% of panel width, alpha cap 0.28 (smaller screens, closer
  glass, less bloom needed).
- **Choreography timeline (v2).** Continuous scrub; the only
  beats are thresholds: W crosses 0.5 → the room's heading glow
  (§6.12's stagger) is eligible; W crosses 0.85 → frost over the
  room reaches its thinnest and the room's figures (§6.16) may
  count if armed.
- **State matrix (v2).** *Rest (centred):* W = 1, full glow, thin
  frost. *Hover:* unchanged. *Focus:* W floored at 0.7 (above).
  *Active:* n/a. *Scrolled-past:* W → 0, room cools behind the
  visitor — scrolling back up re-warms it identically (the scrub
  is symmetric; the house does not hold a grudge). *Disabled:*
  defaults (fallback). *Touch:* identical scrub; no hover
  substitute needed because warmth is positional, not pointeral.
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: bell
  widened (±75% vh) — shorter viewports centre rooms sooner.
  <768px: W computed against a 45% line (rooms centre higher on a
  phone held in one hand), alpha cap per mobile variant.
- **Edge cases & failure modes (v2).** *Two rooms in one tall
  viewport (short rooms, big screen):* each keeps its own W; the
  density law (§4) is a build rule, and if a build breaks it the
  loop still behaves — two mild glows, no error. *Room taller
  than the viewport:* W uses the room's *heading* position, so a
  long menu warms as its title centres and holds while its body
  passes (clamped W ≥0.6 while any part of the room is in view).
  *Glow over photography:* §6.9's frames carry their own warmth;
  the room glow is disabled inside frame boxes to keep the two
  systems from double-warming a picture.
- **Accessibility spec (v2).** Glow and density are decorative
  layers over a panel whose own ground (`--room`) already gives
  `--ink-warm` 8.94:1 with the glow at zero — warmth never carries
  contrast. Nothing is announced; W is not exposed to AT.
- **Tokens consumed (v2).** `--lamp`, `--room`, `--ink-warm`,
  `--ease-glow`, `--lerp-scroll` (0.12), `--glow-alpha-max` (0.34),
  `--warmth-floor-focus` (0.7).

### 6.5 Margin fern progress

- **What & why.** A single fern frond grows in the margin, one
  branch per section read — the page's progress indicator, made
  of the page's own material. It belongs because a progress bar
  would be a plastic strip glued to a winter window; a fern of
  ice *is* the window, keeping time in the theme's own substance.
  It is also the coverage cap's herald: when the glass can freeze
  no further (§6.3), the fern pulses once — progress and weather
  are the same instrument.
- **Structure.** An SVG frond in a 72px-wide `--dusk` housing in
  the left cold margin (§4), fixed with the pane: a central stem
  path plus one branch group per section of the page (authored
  count = the page's real section count, written at build time
  from the page's own outline — a fern with the wrong number of
  branches is §9 failure 7). Branches alternate sides up the stem
  in the fern's habit; each is a small dendrite cluster in
  `--fern` with a `--frost` tip. Beside the housing, in the room
  layer, a visually-hidden-then-shown text equivalent: "Section
  3 of 7" in label style (§3), updated at the same beats — the
  fern is never the only carrier of progress.
- **Motion spec.** Trigger: a section's heading crossing the 55%
  viewport line (read = arrived, not merely glimpsed). The next
  branch unfurls over 400ms: a curl — the branch's paths draw
  while rotating from a 38° furled angle to rest, `--ease-grow`,
  tip last. Branches fire in order, at most one per 400ms (a fling
  to the bottom queues them at 120ms intervals — the fern hurries
  but does not skip). Scrolling back up does **not** un-grow
  branches: progress is a record of reading, and frost that has
  grown on the margin stays grown (contrast §6.3's field, which
  melts — the margin is the pane's edge, where frost is permanent
  first and last; the asymmetry is authored, stated here so two
  builders build the same fern).
- **States.** Ungrown branches (JS-armed only) → unfurling →
  grown (rest). At C = cap (§6.3): one slow pulse — all grown
  branches' tips brighten to `--frost` over 800ms `--ease-glow`
  and settle; once per cap-arrival. Hover on the housing: the
  current branch's section title appears as a label beside it
  (the fern explains itself). Focus: the housing is not focusable;
  its text equivalent is in the room's tab order as a status.
- **Content merge.** The fern's branch count is the page's section
  count and its growth is the reader's own journey down *this*
  page — it is the table of contents, crystallised. It merges by
  being generated from the content's structure.
- **Failure fallback.** Watchdog per branch: an unfurl interrupted
  (tab hidden) completes instantly on return. No JS: all branches
  ship grown and the text reads "Section — of 7" as a static
  "7 sections" label; progress as a *live* signal is the only
  casualty, and it is an honest one.
- **Reduced-motion variant.** Branches appear (opacity, 1 frame)
  as sections are read; no curl, no pulse. The text equivalent
  still updates.
- **Performance budget & mobile variant.** One SVG ≤6KB; unfurls
  animate `stroke-dashoffset` + a ≤38° rotate on a small group.
  Mobile (<768px) and tablet: the margin housing does not exist;
  the fern retires to a horizontal mini-frond in the header bar
  (§6.11) — stem along the bar, branches as ticks, same beats,
  24px tall; below 400px viewport width it is the text equivalent
  alone.
- **Choreography timeline (v2).** Section heading crosses 55% →
  t=0 branch begins (if queue empty) → t=0–400 curl unfurl, tip
  lands t=400 → text equivalent updates t=400 (after the motion,
  so AT never announces a half-grown state) → next queued branch
  t=+120ms if fling-queued.
- **State matrix (v2).** *Rest:* grown branches for sections read.
  *Hover:* current branch labels itself (above). *Focus:* n/a
  (status text carries focus semantics). *Active:* n/a.
  *Scrolled-past (up):* branches stay grown. *Disabled/no-JS:*
  fully grown, static label. *Touch:* no hover label; a tap on
  the housing (it is `pointer-events: none` as part of the frost
  layer — so instead the *header* mini-frond's tap target in the
  room layer) shows the same label.
- **Breakpoints (v2).** ≥1200px: margin fern as specced.
  768–1199px: header mini-frond. <768px: header mini-frond;
  <400px: text only.
- **Edge cases & failure modes (v2).** *Page with 2 sections:*
  a two-branch fern looks sparse — licensed; the housing shortens
  to fit (the stem is drawn to the last branch, never a long bare
  stem). *Page with 12+ sections:* branches compress (stem
  segments shorten, authored minimum 26px per branch) — beyond 14
  sections the theme itself is out of scope (§1). *Anchor jump to
  section 6:* all branches up to 6 grow in the 120ms queue — the
  fern records arrival, honestly labelled by the text equivalent
  jumping straight to "Section 6 of 7".
- **Accessibility spec (v2).** The SVG is `aria-hidden`; the text
  equivalent is a `role="status"` with `aria-live="off"` (updates
  are read on demand, never pushed — a fern that announces itself
  every section is a cuckoo clock). Contrast of the text
  equivalent: `--frost` on `--dusk` 6.46:1.
- **Tokens consumed (v2).** `--fern`, `--frost`, `--dusk`,
  `--ease-grow`, `--ease-glow`, `--dur-unfurl` (400ms),
  `--fern-branch-min` (26px).

### 6.6 Hover thumbprint melt

- **What & why.** Hovering a card melts a ~110px radial clear
  patch in its frost veil, its edge beaded with droplets; the
  patch follows the pointer and re-freezes when the pointer
  leaves. It belongs because inspection on a frozen window *is*
  touch: you warm the exact spot you want to see with your
  fingertip. It turns "hover state" — the web's deadest convention
  — into the theme's central physical act.
- **Structure.** Each card (§6.13) carries a frost veil: a
  `--frost-deep` layer at 55% opacity over its face, masked by a
  radial hole whose centre and radius are CSS custom properties
  written by the shared loop. The melt edge is an SVG ring of
  droplet circles (`--bead`) positioned on the hole's rim,
  scaling with the hole's radius. The veil is `pointer-events:
  none`; the card beneath is fully rendered at all times — the
  veil thins the view, it never gates the content (a card's text
  is legible through its veil at rest: veil alpha is capped so
  card text contrast stays ≥4.5:1 against its ground, §10).
- **Motion spec.** Trigger: pointerenter/move on a card (fine
  pointers only). The hole's centre follows the pointer with the
  loop's melt lerp (0.15 — a fingertip's heat lags a fingertip);
  radius grows 0→55px over 350ms `--ease-melt` on entry. Droplets
  on the rim scale 0.6→1.0 staggered by angle as the rim passes
  them. On leave: the hole holds 200ms (a fingertip's warmth
  lingers), then re-freezes over 1200ms `--ease-grow` — radius
  shrinking, rim droplets flattening back into the veil. Focus
  (keyboard) melts a centred patch of the same size over 350ms;
  blur re-freezes identically.
- **States.** Veiled (rest) → melting → clear-at-pointer →
  holding → re-freezing → veiled. *Active* (press): hands over to
  §6.7's breath. *Scrolled-past:* a card scrolled out mid-melt
  completes its re-freeze off-screen; state is per-card and cheap.
  *Disabled (touch):* no veil melt on tap (tap is §6.7's); touch
  cards rest at a lighter veil (35%) so nothing needs melting to
  be read.
- **Content merge.** The melt happens on the card being inspected,
  centred where the visitor is actually looking — the effect's
  position is the content's position. A melt that followed the
  pointer over chrome or margins would be decoration; confined to
  cards, it is reading.
- **Failure fallback.** Loop dead → veils at their CSS default
  with a static centred clearing per card (the print of a
  thumbprint, pre-melted). No JS: same. The card never depends on
  the melt to be used: links and buttons inside are live under
  the veil at all times (the veil intercepts nothing).
- **Reduced-motion variant.** No following, no re-freeze
  animation: hover/focus swaps the veil instantly to its melted
  state (centred clearing), leave swaps back. The information —
  this card is the one you're touching — survives without the
  physics.
- **Performance budget & mobile variant.** Per card: two custom
  properties + one droplet ring (≤14 circles) per frame, only
  while that card is hovered/focused. No mobile variant — touch
  uses the lighter static veil (above); this is a designed
  absence, stated so it is not "fixed" later.
- **Choreography timeline (v2).** t=0 pointerenter → t=0–350 hole
  opens at pointer → continuous: centre lerps behind pointer at
  0.15 → t=leave → t=+200 hold → t=+200–1400 re-freeze → rest.
  Focus path: t=0 focus → t=0–350 centred hole → blur → same
  hold/re-freeze.
- **State matrix (v2).** *Rest:* veiled 55%. *Hover:* as specced.
  *Focus:* centred melt. *Active:* §6.7 takes the card.
  *Scrolled-past:* re-freeze completes off-screen. *Disabled:*
  static clearing. *Touch:* 35% veil, no melt.
- **Breakpoints (v2).** ≥1200px: hole Ø110px. 768–1199px: Ø96px
  (cards are narrower). <768px: touch rules dominate; on a
  fine-pointer small screen (rare) Ø88px.
- **Edge cases & failure modes (v2).** *Pointer races across six
  cards:* each card runs its own state; two cards may be mid-
  re-freeze while a third melts — capped at 3 concurrent rim
  rings animating, further cards melt without droplet animation
  (radius still animates). *Pointer leaves the window mid-melt:*
  treated as leave; hold + re-freeze. *Card contains a video or
  form field:* the veil never covers interactive children at
  >35% — cards with controls use the touch-weight veil at all
  pointers, so a control is never seen through thick frost
  (§6.14's fields are never veiled at all).
- **Accessibility spec (v2).** Veil and melt are `aria-hidden`
  decoration over live content; focus melt gives keyboard users
  the identical clearing sighted pointer users get. Card text
  contrast is audited *through the resting veil* (§10), not
  beneath it.
- **Tokens consumed (v2).** `--frost-deep`, `--bead`, `--ease-melt`
  , `--ease-grow`, `--lerp-melt` (0.15), `--melt-radius` (55px),
  `--dur-refreeze` (1200ms), `--veil-rest` (0.55).

### 6.7 Breath-fog click

- **What & why.** Clicking a card breathes on it: a soft fog
  patch blooms from the click point, then clears from the centre
  outward, leaving the card momentarily clearer than its
  neighbours. It belongs because a click on glass, in winter, is
  breath — the visitor leans in, exhales, and for a moment the
  view is both fogged and then *clearer than before*, which is
  exactly what activation feedback should feel like: contact,
  then confirmation.
- **Structure.** A fog layer per card (a radial-gradient disc in
  `--frost` at 0.85 alpha, edges feathered by the gradient itself
  — the theme's one licensed blur-like softness, and it is a
  gradient, not a `filter`, §6.4), centred on the click point via
  custom properties, scaling from the loop. After clearing, the
  card's veil (§6.6) rests at 30% instead of 55% for 4000ms —
  the "clearer than its neighbours" residue — then drifts back
  to 55% over 2000ms. All layers `pointer-events: none`.
- **Motion spec.** Trigger: click/activation on a card (pointer
  or keyboard Enter/Space — keyboard breath centres on the card).
  Bloom: scale 0→1 (Ø ~180px) over 300ms `--ease-glow` (breath is
  soft, not springy). Hold at full fog 120ms. Clear: an inner
  clear radius scrubs 0→full over 900ms `--ease-wipe`,
  centre-outward — the middle of your breath clears first, the
  edges last. Total 1320ms. A second click mid-clear restarts
  the bloom from the current fog value (no snap).
- **States.** Clear (rest, under §6.6's veil) → blooming → fogged
  → clearing → afterglow (veil 30%, 4000ms) → rest. *Disabled:*
  a disabled card does not breathe — breath on a card that cannot
  answer would be a lie; it gets §6.6's melt only, and its veil
  stays at 55%.
- **Content merge.** The fog blooms on the element acted upon,
  from the point of contact, and its residue is a clearer view of
  *that card's* content. It is the activation receipt, printed in
  the theme's material, on the thing itself.
- **Failure fallback.** JS dead: no fog, no residue — clicks
  simply work, as they must. The fog is feedback, never a gate:
  the card's action fires on the click event itself, at t=0, not
  after any animation (§10 tests this with the loop disabled).
- **Reduced-motion variant.** No bloom, no clear: the card's veil
  steps directly to 30% for 4000ms, then back. The residue — the
  information — survives; the weather rests.
- **Performance budget & mobile variant.** One gradient disc per
  active card; concurrent breaths capped at 2 (a third click's
  card gets the residue without the bloom). Mobile: identical —
  tap *is* breath here (contrast §6.6, where touch abstains);
  bloom Ø150px.
- **Choreography timeline (v2).** t=0 click (action fires) →
  t=0–300 bloom → t=300–420 full fog → t=420–1320 centre-out
  clear → t=1320 afterglow begins → t=5320 veil drift-back starts
  → t=7320 rest.
- **State matrix (v2).** *Rest:* §6.6 veil. *Hover:* §6.6 melt
  (breath does not pre-fire on hover). *Focus:* no fog; focus
  melt only. *Active:* the breath itself. *Scrolled-past:*
  afterglow timers are wall-clock; a card scrolled away finishes
  its residue unseen and rests at 55% on return. *Disabled:*
  no breath (above). *Touch:* tap = full breath.
- **Breakpoints (v2).** ≥1200px: Ø180px bloom. 768–1199px:
  Ø165px. <768px: Ø150px; afterglow 3000ms (shorter attention,
  smaller glass).
- **Edge cases & failure modes (v2).** *Click lands on a link
  inside the card:* the breath still blooms (the visitor did
  breathe on the card) and navigation proceeds — the fog layer is
  in the *origin* card and is abandoned with the page; on
  same-page anchor jumps the fog completes in the origin card,
  unseen, harmless. *Rapid repeat clicks (a stepper control):*
  breaths throttle to one per 1400ms per card; the control's own
  feedback is primary. *Card is mid §6.6 re-freeze:* the bloom
  overrides the veil state; on clear, veil goes to afterglow,
  not back to the interrupted re-freeze.
- **Accessibility spec (v2).** Fog is `aria-hidden`; the card's
  own `:active`/focus styles and any `aria-live` result of the
  action are the accessible feedback — breath is never the only
  signal that something happened. Contrast during full fog is
  irrelevant by construction: the fog lasts 120ms at peak and the
  content beneath is not being read mid-click; §10 verifies the
  *afterglow* state's contrast, which is the state a reader
  actually reads in.
- **Tokens consumed (v2).** `--frost`, `--ease-glow`, `--ease-wipe`
  , `--dur-bloom` (300ms), `--dur-breath-clear` (900ms),
  `--veil-afterglow` (0.30), `--afterglow-hold` (4000ms).

### 6.8 Science fern draw

- **What & why.** In the science section, one large dendrite —
  central stem, five branch pairs — strokes itself in true growth
  order over ~2s, each branch labelled with its formation fact as
  it completes. It belongs because it is the theme teaching its
  own physics: the diagram grows the way the crystal it explains
  grows, so form and content are the same event. On a site with
  no science section, this element migrates: it becomes the
  "how frost works" fern in whatever explainer block the site
  does have — it is never dropped and replaced with a stock
  illustration (§9 failure 8).
- **Structure.** One inline SVG (~340×420px desktop) on a
  `--dusk` panel inside the reading column: stem path, five
  branch-pair paths with sub-branchlets, drawn in `--fern` with
  `--frost` tips. Six label slots (stem + five pairs) sit beside
  the drawing in the room layer, each a figure + caption in
  Spectral italic / Inter small (§3): e.g. pair 3's label states
  the branching angle and the humidity it implies. Labels are
  real DOM text, present from first paint; the drawing is
  `aria-hidden` with the labels carrying the information.
  Growth is `stroke-dashoffset` per path, windows sequenced by
  the growth order (stem 0–35%, pairs basal→apical).
- **Motion spec.** Trigger: the panel's centre crossing 60%
  viewport height, once. Total 2000ms `--ease-grow`. Stem draws
  0–700ms; pair *n* begins at 600 + n×220ms, draws 420ms,
  sub-branchlets in its final 40%; each label's figure brightens
  from `--glass` to `--frost` over 300ms as its branch completes
  (labels are printed throughout — brightening is emphasis, not
  revelation). Scrolled away mid-draw: the draw completes
  off-screen (growth does not pause for an absent audience; ice
  is indifferent) — returning visitors find it grown and labelled.
- **States.** Ungrown (JS-armed only) → growing → grown (rest).
  Hover on a label: its branch re-brightens (stroke to `--frost`,
  200ms) — the diagram answers questions. Focus: labels are
  focusable (`tabindex="0"` with a described-by pointing at the
  SVG's title) and focus brightens identically. Scrolled-past:
  grown.
- **Content merge.** The drawing is the section's figure and its
  labels are the section's facts; remove either and the other is
  orphaned. The growth order is the formation order the text
  describes — the animation is the argument.
- **Failure fallback.** Watchdog at 2600ms from trigger: all
  paths snap drawn. No JS: fully drawn, labels at full bright —
  a printed plate in a book of winter science.
- **Reduced-motion variant.** Drawn from the start; label
  brightening is instant on hover/focus.
- **Performance budget & mobile variant.** One SVG ≤9KB, six
  dashoffset animations in a 2s window, once per page. Mobile:
  the panel stacks (drawing above labels), drawing 280px wide,
  draw duration 1600ms, sub-branchlets omitted from the *drawing*
  (the labels still describe them — the mobile plate is a smaller
  drawing of the same crystal, authored, not scaled).
- **Choreography timeline (v2).** t=0 trigger → 0–700 stem →
  600/820/1040/1260/1480 pairs begin, each 420ms → labels
  brighten at 1020/1240/1460/1680/1900 → t=2000 rest.
- **State matrix (v2).** *Rest:* grown, labels at rest bright.
  *Hover:* branch brightens (above). *Focus:* same, plus the
  label's full fact is the focus's `aria-describedby` target.
  *Active:* n/a. *Scrolled-past:* grown. *Disabled/no-JS:*
  printed plate. *Touch:* tap on a label brightens its branch
  for 1200ms (no hover on touch; the tap is the question).
- **Breakpoints (v2).** ≥1200px: side-by-side, 340px drawing.
  768–1199px: side-by-side, 300px, labels narrowed. <768px:
  stacked, per mobile variant.
- **Edge cases & failure modes (v2).** *Section is the page's
  last and never centres (short final viewport):* trigger falls
  back to an IntersectionObserver at 40% visibility if the 60%
  centre line is unreachable — the fern must grow even on a page
  that ends abruptly. *Labels longer than slots (a wordy
  translation):* labels are flowing text beside the drawing, not
  fixed slots; the brighten beat keys to branch completion, not
  label height, so long labels cannot desync the draw.
- **Accessibility spec (v2).** Information lives in the labels
  (real text, correct reading order: stem fact first, pairs in
  growth order — the DOM order *is* the growth order). The SVG
  carries `role="img"` and a `<title>` ("A frost fern: one stem,
  five branch pairs") for contexts that surface it, but the
  labels are the canonical carrier.
- **Tokens consumed (v2).** `--dusk`, `--fern`, `--frost`,
  `--glass`, `--ease-grow`, `--dur-fern-draw` (2000ms).

### 6.9 Frosted image frames

- **What & why.** Photographs sit behind frost rims — pictures
  are windows in the window, deeper glass over the warm interior
  the photo shows. As each photo centres, its rim retreats ~30%
  and the image scales 1.06→1.0 while lamplight warmth rises in
  its shadows. It belongs because a photograph of a fireside, seen
  through frost, is the theme's whole promise in one frame: the
  warmth is real, and it is on the other side of glass.
- **Structure.** A `<figure>` with the `<img>` in the room layer
  and a rim layer above it (in the frost layer's stacking context,
  `pointer-events: none`): an authored frame of crystal paths
  (`--fern` on `--frost-deep`) inset from the figure's edges,
  thickness ~9% of the frame's width per side. The rim's inner
  edge is a mask whose inset is a custom property scrubbed by the
  loop. Warmth in the shadows is a `--lamp` multiply overlay at
  ≤0.18 alpha, scrubbed with the same value — no `filter` on the
  image itself (§9 failure 2).
- **Motion spec.** Trigger: scroll scrub. Retreat value `R` = 0
  when the figure's centre is beyond ±70% vh, 1 at centre (same
  bell as §6.4, lerp 0.12). Rim inset grows by 30% of its rest
  thickness × R; image scale 1.06 − 0.06R; shadow warmth alpha
  0→0.18 × R. Fully reversible: scrolling back re-rims the
  picture — a photo you have passed is a window you have left,
  and it frosts over behind you. That reversibility is authored,
  not an accident of scrubbing: the theme's glass has no memory
  for pictures, only for reading (§6.5's asymmetry, again).
- **States.** Rimmed (rest, out of band) → retreating → centred/
  clear-rimmed → re-rimming. Hover: the rim retreats an extra
  10% (stacked on R, capped at 40% total) over 300ms — leaning
  closer. Focus: same via focus-within. 
- **Content merge.** The rim is drawn *on the photograph's own
  frame*, sized from its box; the warmth that rises is in the
  photograph's shadows, i.e. in the depicted room's light. The
  effect has no existence apart from the image it frames.
- **Failure fallback.** Loop dead / no JS: rims at their mid
  state (15% retreat), images at 1.03 — every photograph fully
  visible and handsome; the scrub is a refinement, never a gate.
- **Reduced-motion variant.** Static mid state (as fallback);
  hover/focus retreat is instant.
- **Performance budget & mobile variant.** Per figure: one mask
  inset + one transform + one overlay alpha per frame while in
  the scrub band; ≤2 figures in band at once by layout. Mobile:
  rim thickness 7%, retreat 25%, warmth cap 0.14.
- **Choreography timeline (v2).** Continuous scrub; thresholds:
  R crosses 0.8 → the figure's caption (in the room layer) gets
  its one permitted emphasis — Spectral italic brightens from
  `--glass`-toned to full `--ink` — the picture is "arrived"
  when its caption is fully lit.
- **State matrix (v2).** *Rest:* rimmed at band value. *Hover:*
  +10% retreat (above). *Focus:* same. *Active:* n/a.
  *Scrolled-past:* re-rimmed to rest. *Disabled:* mid state.
  *Touch:* scrub only; no hover addition; a tap does nothing
  (pictures are looked at, not breathed on — §6.7 is for cards).
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: rim 8%,
  retreat 28%. <768px: per mobile variant; figures full-column
  width, so the bell uses the 45% line (§6.4's mobile ruling).
- **Edge cases & failure modes (v2).** *Very tall image (a
  portrait of the lodge):* R keys to the figure's *focal band*
  (its middle third), declared per figure via a data attribute
  at build; default is the centre. *Image fails to load:* the
  figure's `--room` ground and its alt text stand; the rim still
  frames the empty window — frost on an empty frame is honest:
  the room is there, the view is not, and the alt says so.
  *Caption longer than the frame:* captions live below the rim,
  never under it (type law 1).
- **Accessibility spec (v2).** Rim and warmth are `aria-hidden`;
  the `<img>`'s alt is untouched by any state. Nothing about the
  scrub is announced. Focus retreat gives keyboard users the
  lean-closer view pointer users get.
- **Tokens consumed (v2).** `--fern`, `--frost-deep`, `--lamp`,
  `--ink`, `--ease-melt`, `--lerp-scroll` (0.12), `--rim-rest`
  (9%), `--rim-retreat` (30%).

### 6.10 The CTA thumbprint

- **What & why.** The booking CTA permanently sits inside a
  melted thumbprint: a clear oval in the frost with a beaded melt
  rim that subtly re-beads every ~6s. It is the theme's second
  exclusion zone and its moral centre — the one action on the
  page is kept warm and touchable by an unseen hand, because the
  invitation is literally kept clear for you. If §6.2 is the house
  saying its name, this is the house holding its door.
- **Structure.** The conversion block reserves an oval clearing
  (§4) in the frost layer's mask — same construction as §6.2's
  patch, smaller and rounder, with a rim ring of `--bead`
  droplets (an SVG ellipse of ~22 droplet circles, authored
  sizes 2–5px, denser at the bottom where meltwater gathers).
  Inside, in the room layer: the CTA button on `--lamp` ground
  with `--ink-warm` text (the only solid lamp surface on the
  page — rationed by §2), its label, and one line of keeper's
  copy. The mask hole is CSS/SVG, not JS: the clearing exists
  before any script runs and cannot be revoked by one failing.
- **Motion spec.** Persistent, plus a time loop: every 6000ms the
  rim re-beads — droplets scale 1→1.35→1 over 800ms `--ease-glow`,
  staggered by 26ms around the ellipse starting at the top (a
  fresh sheen of melt travelling around the rim). The pulse is
  the page's quietest possible "still here". Hover/focus on the
  button: droplets at the nearest rim point scale to 1.5 and the
  button's ground warms `--lamp` → `--lamp-deep` at its edges
  over 250ms (a gradient shift, not a colour swap). Pressed: the
  button depresses 1px and one droplet at the bottom of the rim
  detaches and falls 10px, fading — once per press, the
  thumbprint's receipt.
- **States.** Clear-and-beaded (rest) → re-beading (6s cycle) →
  rest. *Hover/focus:* warmed (above). *Active:* pressed +
  droplet fall. *Disabled:* a disabled CTA keeps its clearing
  (the door is still the door) but the rim stops re-beading and
  droplets rest at 0.7 scale — a cold thumbprint for a door that
  cannot open today; the copy beside it must say why (§12).
  *Scrolled-past:* the cycle continues only while the block is
  within 1.5 viewports; off-screen, the clock pauses (no pulses
  are spent on an empty room).
- **Content merge.** The thumbprint exists only around the real
  conversion action; its copy is the offer itself. A build that
  puts a thumbprint around a newsletter link or a decorative
  button has broken the ration (§4: at most two per page, both
  around *the* conversion) and §10 greps for it.
- **Failure fallback.** No JS: the clearing and rim are static,
  the button fully live. The re-bead is the only casualty.
- **Reduced-motion variant.** Static rim, no cycle, no droplet
  fall; hover warmth is instant.
- **Performance budget & mobile variant.** One SVG rim ≤3KB, one
  800ms staggered scale pass every 6s while near view — the
  cheapest loop on the page. Mobile: oval hugs the full-width
  button; droplets 16; cycle 7000ms (a phone's glass is smaller,
  its keeper slower).
- **Choreography timeline (v2).** Cycle: t=0 top droplet pulses →
  stagger 26ms × 22 → t≈1370 full rim has pulsed → rest until
  t=6000. Press: t=0 depress → t=80 droplet detaches → t=80–480
  falls 10px fading → rim re-forms the gap by t=900 (a new bead
  scales in at the vacancy).
- **State matrix (v2).** *Rest:* clear, cycling. *Hover:* warmed
  edges, near droplets 1.5. *Focus:* identical to hover (keyboard
  visitors get the same warm door). *Active:* press + fall.
  *Scrolled-past:* clock paused (above). *Disabled:* cold rim,
  no cycle. *Touch:* no hover; the cycle and press states carry
  the life; tap = press.
- **Breakpoints (v2).** ≥1200px: oval ~340×150px around a
  standard button. 768–1199px: oval ~300×140px. <768px:
  full-width button, oval = button box + 18px, per mobile variant.
- **Edge cases & failure modes (v2).** *Two CTAs on the page*
  (§4's licensed pair): they share one re-bead clock, phase-
  offset by 3000ms so the page never pulses twice at once.
  *Long button label (a translated "Reserve your winter cabin"):*
  the oval is sized from the rendered button box + fixed margin,
  computed like §6.2's patch — never a fixed ellipse that a long
  word could outgrow into the frost. *CTA is a form submit
  (§6.14):* the thumbprint wraps the submit only, never the whole
  form — fields are work, the submit is the door.
- **Accessibility spec (v2).** The button is a real `<button>`/
  link in the room layer, focusable, with a visible focus ring in
  `--lamp-deep` drawn *inside* the clearing (2px, offset 3px) —
  focus is never indicated by the rim alone. The rim and cycle
  are `aria-hidden`. Button contrast: `--ink-warm` on `--lamp`
  5.87:1 — the page's one warm surface is audited like any other.
- **Tokens consumed (v2).** `--lamp`, `--lamp-deep`, `--bead`,
  `--ink-warm`, `--ease-glow`, `--ease-melt`, `--rebead-cycle`
  (6000ms), `--dur-rebead` (800ms).

### 6.11 Glass-pane navigation

- **What & why.** The site's header is a band of the pane itself:
  a `--dusk` night field across the top of the glass, the house
  name in Spectral at its left in a small wiped clearing, and nav
  links as labels written on the glass — each link's text sits in
  its own thumbnail-sized clearing so it can be read, with frost
  feathering the spaces between. It belongs because even the
  furniture of a website must obey the window: you do not bolt a
  plastic menu bar onto a winter pane.
- **Structure.** A sticky header in the room layer (it scrolls
  with the room's frame, not the room's content — the pane's top
  frame). Ground `--dusk`; name clearing = a static mask hole in
  a header-height frost strip (a second, shallow instance of the
  frost layer, clipped to the header, sharing §5's coverage at
  0.5× density); link clearings are radial masks per link,
  feathered 10px. On mobile the fern mini-frond (§6.5) lives at
  the header's right, and below 400px the text equivalent alone.
  The current page's link carries a `--lamp-deep` underline drawn
  as a melt line — a slightly wobbling 2px stroke, authored, not
  a border.
- **Motion spec.** On load: the header's frost strip grows in
  with §6.1 (it is part of the frame; 2000ms, same fronts,
  arriving from the top corners). On scroll past 140px: the
  header compresses 72→56px over 300ms `--ease-wipe` and its
  frost density rises one step (the frame thickens as you
  descend into the page — you are further from the door).
  Hover/focus on a link: its clearing widens 6px over 200ms
  `--ease-melt` (a fingertip approaching warms its label).
  Nothing else moves; navigation is furniture, not theatre.
- **States.** Full (top) → compressed (scrolled). *Current link:*
  melt-line underline, persistent. *Hover/focus:* clearing
  widens. *Active:* the underline brightens to `--lamp` for the
  press. *Disabled:* a link to a closed season's page sits at
  60% with no clearing-widening (frost does not warm for a door
  that is shut — but its text stays readable, §3 law 1).
- **Content merge.** The nav's clearings are sized from the real
  link labels; the name clearing from the real name. It is the
  page's actual wayfinding, wearing the window.
- **Failure fallback.** No JS: header at full height, clearings
  static, all links live. The compression is the only loss.
- **Reduced-motion variant.** No compression animation (height
  steps), no clearing widening (instant), frost strip static.
- **Performance budget & mobile variant.** The header frost strip
  reuses the main layer's SVG defs (no duplicate paths; a `<use>`
  per corner). Mobile: name + fern + a menu button whose panel
  (§11) opens as a full-pane sheet with its own large clearings;
  links stack in Spectral 22px.
- **Choreography timeline (v2).** t=0–2000 strip grows with the
  frame → scroll 140px crossing → 300ms compress → link hover →
  200ms widen. No other beats exist; any build that adds one has
  decorated the furniture.
- **State matrix (v2).** *Rest:* as specced per scroll position.
  *Hover:* widen. *Focus:* widen + a `--frost` focus ring inside
  the clearing. *Active:* underline brightens. *Scrolled-past:*
  n/a (sticky). *Disabled:* per above. *Touch:* no widening; tap
  targets ≥44px with clearings sized to the target, not the text.
- **Breakpoints (v2).** ≥1200px: full row, fern in margin (§6.5)
  so header carries no fern. 768–1199px: full row + header
  mini-frond. <768px: name + mini-frond + menu button.
- **Edge cases & failure modes (v2).** *Many links (7+):*
  clearings may not merge into one long slot — if labels +
  feathering would bridge two clearings, the header drops to the
  mobile pattern at that width regardless of breakpoint (the
  pane refuses a slushy header). *Very long site name:* the name
  clearing computes from the rendered name (§6.2's rule); at
  <400px the name truncates with an ellipsis *inside* its
  clearing — the frost never eats the last visible letter.
- **Accessibility spec (v2).** A real `<nav>` with a list; current
  page via `aria-current="page"` (the melt line is its visual
  twin, never its only signal). Link contrast `--frost` on
  `--dusk` 6.46:1 inside clearings. The frost strip is
  `aria-hidden`, `pointer-events: none`.
- **Tokens consumed (v2).** `--dusk`, `--frost`, `--lamp`,
  `--lamp-deep`, `--ease-wipe`, `--ease-melt`, `--dur-compress`
  (300ms).

### 6.12 The warm-room hero composition

- **What & why.** The first screen assembled: the pane grown
  (§6.1), the name wiped clear (§6.2), and below the patch the
  room's first furniture arriving as lamps are lit one by one —
  standfirst, a frosted photograph of the cabin (§6.9), the
  keeper's one-line welcome, and the scroll cue written on the
  glass. It belongs because a hero in this theme is not a banner
  but a *threshold*: the composition's order is the order of
  arriving at a winter house — you see the name, then the lit
  window, then the person.
- **Structure.** The hero is a 100vh (min 640px) section in the
  room: headline patch zone (top 38%), then a two-column
  composition ≥1200px — standfirst + welcome left, the §6.9
  figure right, its rim at rest — and at the hero's foot the
  scroll cue: a small fern glyph + "The room is below" in label
  style, on the glass line between hero and first cold passage.
  The cabin-interior pin (§5's one pin) is *not* the hero; it
  waits mid-page. Hero content is real DOM in reading order:
  name, standfirst, figure+caption, welcome, cue.
- **Motion spec.** Trigger: load, sequenced after §6.2's clearing
  completes (t≈2650 worst case, earlier if the watchdog fires).
  Furniture staggers in glowing: each element's `--lamp` glow
  underlay (a soft disc behind it, as §6.4's in miniature) rises
  0→0.22 alpha while the element fades/rises 12px over 600ms
  `--ease-glow`, stagger 90ms, in reading order. The figure's rim
  starts at rest; its scrub (§6.9) owns it thereafter. The scroll
  cue's fern glyph pulses once at t=+1200 after the stagger (a
  single `--ease-glow` breath, 1200ms) — once, ever.
- **States.** Unlit (JS-armed only, elements at rest opacity —
  the stagger is a glow-and-rise of *fully rendered* elements,
  never a reveal from nothing; §1's law) → lighting → lit (rest).
  Scrolled-past: lit; the hero does not re-light on return.
- **Content merge.** Every element is the site's real opening
  content in its real order; the composition *is* the page's
  first section, staged as an arrival. There is no separate
  "intro" to skip.
- **Failure fallback.** Watchdog at 3200ms: all glow underlays to
  rest, all elements at final position. No JS: the hero stands
  lit and complete; the lamps were always on.
- **Reduced-motion variant.** Lit from first paint; no stagger,
  no cue pulse.
- **Performance budget & mobile variant.** Glow underlays are
  pre-rendered gradients (as §6.4). Mobile: single column —
  name, standfirst, figure (full width), welcome, cue; stagger
  70ms; hero min-height auto (a phone's window is the size it is).
- **Choreography timeline (v2).** t=0 §6.1 growth → t≈900 §6.2
  edging → t≈1750–2650 clearing → clearing complete → +0
  standfirst lights (600ms) → +90 figure → +180 welcome → +270
  cue → +1470 cue fern's single pulse → rest.
- **State matrix (v2).** *Rest:* lit. *Hover:* elements keep
  their own (§6.9's figure lean). *Focus:* focus into the hero
  completes the stagger instantly. *Active:* n/a. *Scrolled-past:*
  lit. *Disabled/no-JS:* lit, printed. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: two-column as specced.
  768–1199px: two-column narrowed (figure 40%). <768px: stacked
  per mobile variant.
- **Edge cases & failure modes (v2).** *Short viewport (landscape
  phone):* hero min-height yields; the composition flows past
  100vh rather than compressing — a window taller than the screen
  is fine, a squashed one is not. *No photograph available:* the
  figure slot is omitted at build (never an empty frosted frame
  in the hero — §6.9's empty-frame honesty applies to galleries,
  not to the threshold) and the welcome moves up.
- **Accessibility spec (v2).** Reading order = visual order =
  lighting order. The cue is real text, not an icon alone. Glow
  underlays `aria-hidden`; content contrast is the room's own at
  every frame (elements are never below 85% opacity — the stagger
  brightens, it does not fade from invisible, §1).
- **Tokens consumed (v2).** `--lamp`, `--room`, `--ink`,
  `--ease-glow`, `--dur-light` (600ms), `--stagger-lamp` (90ms).

### 6.13 Cabin cards

- **What & why.** The listing unit of the theme — a cabin, a room,
  a table, a tour — presented as a small pane leaned against the
  wall: a photograph under a frost veil (§6.6), its name wiped
  readable, its facts (sleeps, price per night, distance through
  the snow) in Inter beneath, and a lean of at most 3°. It belongs
  because a listing in a warm-room site is a row of little windows
  along a corridor wall, each fogged, each warmable by a fingertip.
- **Structure.** `<article>` cards in a grid (3 columns ≥1200px,
  2 at tablet, 1 mobile): figure (with §6.9's rim at card scale)
  under the §6.6 veil; name in Spectral 22px in a static mini-
  clearing at the figure's foot (the name is *always* readable —
  veils thin, they never hide names, §3 law 1); facts row; one
  link ("Look inside") whose whole card is the hit area via a
  stretched-link pattern. The lean: cards rest at authored tilts
  (−1.2° to +1.2°, alternating by index — panes leaned, not
  aligned) and straighten to 0° under hover/focus.
- **Motion spec.** Entry: cards rise 16px + glow (§6.4's stagger
  grammar, 90ms, `--ease-thaw` 500ms) as their row centres. Lean
  physics: hover/focus straightens over 350ms `--ease-wipe`;
  leaving returns the lean over 600ms `--ease-grow` (a pane
  settles back slowly). Pointer tilt beyond the lean: none —
  the card is glass against a wall, it does not follow your hand;
  §6.6's melt does the following. §6.7 owns clicks.
- **States.** Veiled-and-leaned (rest) → lit (entered) →
  straightened + melting (hover/focus) → breathing (active,
  §6.7). *Unavailable card* (booked out): veil at 70%, no melt,
  no breath, a "In other hands until March" line in the facts —
  frost does not warm for what cannot be had (§6.11's rule,
  applied to stock). Its link is absent, not disabled-looking.
- **Content merge.** The card's frost, name clearing and facts are
  the listing itself; the photograph is the cabin's own. Nothing
  on the card exists that is not the cabin's data.
- **Failure fallback.** No JS: cards upright (lean is a transform
  applied by CSS class at build — the no-JS lean is fine and
  static, so it ships leaned; transforms need no script), veils at
  static clearing, all links live.
- **Reduced-motion variant.** No entry rise, no straighten/settle
  animation (states swap instantly); lean itself is retained —
  it is posture, not motion.
- **Performance budget & mobile variant.** Per card costs are
  §6.6's + §6.9's; grid caps concurrent animations as there.
  Mobile: single column, lean ±0.8°, veil 35% (touch ruling,
  §6.6), entry rise 10px.
- **Choreography timeline (v2).** Row centres → t=0 first card
  rises → stagger 90ms across the row → hover: t=0–350
  straighten, melt per §6.6 → leave: t=0–600 re-lean → click:
  §6.7's timeline takes the card.
- **State matrix (v2).** *Rest:* leaned, veiled. *Hover:*
  straight + melt. *Focus:* same, melt centred (§6.6). *Active:*
  §6.7. *Scrolled-past:* entered state persists (lamps stay lit).
  *Disabled:* the unavailable state (above). *Touch:* tap =
  §6.7 breath; no straighten (nothing hovers) — the lean simply
  rests.
- **Breakpoints (v2).** ≥1200px: 3 columns, lean ±1.2°.
  768–1199px: 2 columns, lean ±1°. <768px: 1 column, ±0.8°,
  facts wrap under the name.
- **Edge cases & failure modes (v2).** *Odd card out (a row of
  one):* it leans at the row's authored angle; no placeholder
  cards are ever rendered to complete a grid — an empty slot is
  cold margin, honestly. *Very long cabin name:* two lines
  maximum in the clearing; the clearing grows downward, never
  sideways into the veil's thick field. *Price missing (a cabin
  not yet priced):* the facts row prints "Price at the door"
  instead of a gap or a zero — the theme never invents a figure
  (§3 law 5).
- **Accessibility spec (v2).** One link per card with a complete
  accessible name ("Look inside Fern Cabin — sleeps four");
  facts are text, not veil-dependent; unavailable state is text,
  not opacity alone. Focus ring inside the card's clearing,
  `--lamp-deep` 2px.
- **Tokens consumed (v2).** `--room`, `--frost-deep`, `--lamp-deep`
  , `--ease-thaw`, `--ease-wipe`, `--ease-grow`, `--dur-card-in`
  (500ms), `--lean-max` (1.2°).

### 6.14 The booking form — writing on the glass

- **What & why.** The conversion form: dates, guests, a name, a
  note for the keeper. Its fields are small clearings in a frosted
  panel — you write on the glass, in the clear, where the keeper
  wiped space for your hand. The submit sits in §6.10's
  thumbprint. It belongs because a form is the moment the visitor
  stops looking through the window and starts speaking through
  it; the theme makes that literal without making it harder —
  every field is clearer than the page around it, never less
  usable than a plain form (§10's form-keeping rehearsal).
- **Structure.** A `--dusk` panel (the night side of the glass —
  you write from outside) with fields as `--frost`-ground
  clearings: label above in label style (`--frost` on `--dusk`),
  input in `--ink` on `--frost` (10.51:1), 48px tall, radius 3px
  (the theme's one licensed radius family: wiped edges are not
  pill-shaped). Focus: the clearing's feathered edge sharpens
  (mask inset −4px) and a `--lamp-deep` rule underlines the field
  — the keeper is attending. Errors: the rule turns `--lamp-deep`
  to a doubled line and the error text appears *inside* the
  clearing beneath the field, in the keeper's voice (§12) — errors
  are never exiled to a summary box at the top; you correct them
  where you wrote them.
- **Motion spec.** Panel entry: the panel's frost thins as it
  centres (§6.4's warmth, panel is a `.room` inverted — a dusk
  room). Field focus transitions 200ms `--ease-melt`. Submit:
  §6.10's press. On successful submit: the whole panel *wipes
  clear* over 800ms `--ease-wipe` — every clearing expands until
  the panel is one clear pane — and the confirmation stands in
  the cleared glass: the booking's facts, the keeper's reply line
  (§12's fixed string), and a reference derived from the booking
  itself (dates + a sequence counted from the page's own ledger
  element, §6.17 — never a random number dressed as a reference).
  The wipe is the receipt: you wrote on frost; the answer comes
  back on clear glass.
- **States.** Rest (fields clear, panel frosted at edges) →
  field focus (attended) → error (kept, doubled rule, copy in
  place, input preserved — always) → submitting (submit's
  droplet falls, §6.10; fields inert but readable) → confirmed
  (wiped panel, facts, reply). No state ever clears the visitor's
  typing.
- **Content merge.** The form is the site's real booking act; its
  clearings are sized from the real fields; the confirmation's
  facts are the visitor's own entries read back. Nothing is
  decoration: the panel's frost is thinnest exactly where the
  work is.
- **Failure fallback.** No JS: a plain, fully working form on the
  dusk panel (native validation off, server errors return as
  printed error text in the same slots). The wipe is a JS
  ceremony over a form that never needed it.
- **Reduced-motion variant.** No wipe: confirmation replaces the
  form in one step, panel statically clear. Focus transitions
  instant.
- **Performance budget & mobile variant.** The wipe animates one
  mask over one panel, once. Mobile: panel full-width, fields
  stack, idle growth pauses while the form holds focus (§6.3's
  keyboard ruling), submit thumbprint per §6.10's mobile variant.
- **Choreography timeline (v2).** Focus field → t=0–200 edge
  sharpens, rule draws → submit → t=0 droplet falls (§6.10) →
  server/native round trip (apparatus line "Writing to the
  keeper…" appears at t=1200 if unanswered) → success → t=0–800
  panel wipe → facts + reply stand at t=800 → fern (§6.5) does
  not grow for a form — forms are not sections; the confirmation
  is outside the reading journey, and the fern's honesty (§6.5)
  forbids the branch.
- **State matrix (v2).** *Rest:* as above. *Hover:* field
  clearings brighten 4% (a hand nearing). *Focus:* attended
  state. *Active:* submit press. *Scrolled-past:* a half-filled
  form scrolled away keeps its values and its panel state.
  *Disabled:* submit disabled only with its reason printed beside
  it in the clearing (§12) — a cold thumbprint (§6.10) plus words.
  *Touch:* fields ≥48px, focus states on tap, no hover brighten.
- **Breakpoints (v2).** ≥1200px: two-column field pairs (dates,
  guests) over full-width note. 768–1199px: pairs kept, narrower
  panel. <768px: single column, panel edge-to-edge.
- **Edge cases & failure modes (v2).** *Date in the past:* the
  keeper's error, in place: the field keeps the date, the note
  explains, focus returns to the field. *Double submit:* the
  second press is absorbed (submit inert from first press); the
  droplet falls once. *Session expires mid-form:* values persist
  in the DOM; the error slot carries the keeper's apology and the
  form re-arms — nothing the visitor wrote is lost to weather.
- **Accessibility spec (v2).** Real `<label>`s, `aria-describedby`
  wiring for errors, `aria-invalid` on error, focus moved to the
  first error field on failed submit, confirmation in a
  `role="status"` region. All contrasts are the panel's audited
  pairings at rest *and* mid-wipe (§10 samples the wipe at 50%).
- **Tokens consumed (v2).** `--dusk`, `--frost`, `--ink`,
  `--lamp-deep`, `--ease-melt`, `--ease-wipe`, `--dur-wipe-form`
  (800ms), `--field-h` (48px).

### 6.15 Frosted skeleton & the hand-wipe transition

- **What & why.** Loading and page change, in the theme's two
  weathers. Loading: a fully frosted skeleton — the page's shape
  present but frozen over, thawing in patches as real content
  arrives. Transition: frost grows across the whole pane, and
  then a hand wipes it clear onto the new page. It belongs
  because in a house of glass, waiting *is* weather: you do not
  show a spinner to a visitor at a window; you show them the
  window, frosting and clearing.
- **Structure.** Skeleton: the incoming page's layout in
  `--frost-deep` blocks (headline bar at true measure, text bars,
  a figure block) under a crystal field at C = 0.30, each block
  carrying a thaw patch (a radial clearing, as §6.2's in
  miniature) that opens when that block's real content is ready
  to swap in. Transition: an overlay pane (a transition-only
  instance of the frost layer) whose coverage animates 0.18 →
  cap → wipe: at full frost the route swaps beneath it; then a
  wipe mask — an authored hand-smudge shape, the same family as
  §6.2's patch edge — sweeps once across, clearing to the new
  page's resting frame.
- **Motion spec.** Skeleton thaw: per block, patch opens over
  600ms `--ease-thaw` when its content lands; blocks thaw in
  readiness order, not layout order (the headline usually first,
  a gallery last — the room assembles as it can). Hard cap: any
  block still frozen at 4000ms thaws regardless (its content, if
  still absent, is the §6.18 state, shown honestly). Transition:
  frost-over 700ms `--ease-grow` → swap at full cover → wipe
  800ms `--ease-wipe`, hand shape travelling left→right (or
  right→left on back-navigation — the hand wipes toward where
  you came from). Latest-wins: a second navigation mid-transition
  completes the wipe instantly and starts from the new page.
- **States.** Skeleton: frozen → thawing per block → live.
  Transition: clear → frosting → covered (swap) → wiping →
  clear. Neither state ever shows a blank: the skeleton is a
  *page-shaped* frost, and the transition's covered beat still
  shows frost, frame and fern — the window, never a void.
- **Content merge.** The skeleton's blocks are the real page's
  real boxes at real sizes (built from the same layout), and its
  thaw order is the content's true arrival order. The transition
  wipes onto the actual destination, whose own frame (§6.1,
  session-printed) is what the wipe reveals.
- **Failure fallback.** If content fails, blocks thaw onto
  §6.18's honest states at the 4000ms cap. If the transition's
  JS fails mid-route, the overlay is removed by a 1600ms watchdog
  and the new page stands in its printed frame — a wipe that
  never finishes is a §10 failure, rehearsed there.
- **Reduced-motion variant.** Skeleton: blocks appear as content
  lands, no thaw patches. Transition: a 200ms crossfade through
  `--frost` — through the *colour* of frost, not its growth.
- **Performance budget & mobile variant.** Skeleton reuses the
  frost layer's SVG defs. The transition overlay is one mask
  animation; it is forbidden on pages where the route change is
  same-page anchor travel (anchors are journeys *within* the
  room — §6.11's links never frost the pane). Mobile: frost-over
  550ms, wipe 650ms, skeleton identical.
- **Choreography timeline (v2).** Navigation → t=0–700 frost-over
  (fern and header last to freeze — the frame outlasts the view)
  → t=700 swap → t=700–1500 wipe → t=1500 destination at rest.
  Skeleton: t=0 frozen page-shape → per-block thaws on readiness
  → all live or capped by t=4000.
- **State matrix (v2).** *Rest:* n/a (transient element).
  *Hover/focus:* during a transition, focus is held on the
  destination's heading at swap (focus custody: the wipe never
  strands focus on a removed page). *Active:* n/a. *Scrolled-
  past:* n/a. *Disabled/no-JS:* no skeleton (content renders
  directly), no transition (plain navigation — the honest web).
  *Touch:* identical beats.
- **Breakpoints (v2).** ≥1200px / 768–1199px: as specced.
  <768px: per mobile timings; skeleton figure block stacks above
  text bars as the layout does.
- **Edge cases & failure modes (v2).** *Instant content (cached
  page):* if all blocks are ready within 250ms, the skeleton
  never shows — a flash of frost on a fast load is worse than
  none; the skeleton has a minimum-show of 0ms and a
  show-threshold of 250ms. *Back/forward cache restore:* the
  page returns in its resting frame, no transition (the browser
  is the hand here). *Prefetch hover:* no pre-frosting on hover —
  the pane does not weather for a maybe.
- **Accessibility spec (v2).** Skeleton blocks are `aria-hidden`
  with a single `aria-busy` region announcing "The room is being
  made ready" once; the transition moves focus per the custody
  rule and the destination's title is the announcement. Neither
  element traps focus or blocks interaction beyond its beats.
- **Tokens consumed (v2).** `--frost-deep`, `--frost`, `--fern`,
  `--ease-grow`, `--ease-wipe`, `--ease-thaw`, `--dur-frost-over`
  (700ms), `--dur-wipe-page` (800ms), `--thaw-cap` (4000ms).

### 6.16 Counters — the thermometer & the ledger

- **What & why.** The theme's figures — tonight's low, the week's
  snowfall, the nights the cabin has stood empty — count to their
  values as their section centres. It belongs because data in a
  winter house is read off instruments: a thermometer does not
  spin through numbers for show; it *settles*. These counters
  settle — and they refuse, by §3 law 5, any figure that is not a
  temperature, a snowfall, a distance or a ledger count.
- **Structure.** Figure blocks inside cold passages and warm
  rooms: a value in Inter 28px tabular, a label in label style,
  and a source line in small text ("from the porch thermometer,
  read at dusk") — every figure carries its instrument with it;
  a figure without a source line does not ship (§10). Values are
  printed in the DOM at their true final value; JS re-zeros and
  counts only for the ceremony.
- **Motion spec.** Trigger: the figure's block centring (the
  §6.4 bell at W ≥0.85 for rooms; the 55% line for cold figures).
  Count: 1200ms `--ease-thaw`, integers stepping at their natural
  grain (temperatures in whole degrees, snowfall in cm with one
  decimal in the final step only — a thermometer does not do
  hundredths), negatives counting *down* through zero to −11°
  with the minus sign present from the first frame (a temperature
  below zero is not a surprise reveal). Counts once per page
  view; scrolling back does not recount (instruments do not
  re-settle for an audience).
- **States.** Printed (rest, no-JS and after counting) → counting
  → settled. Hover/focus: none. 
- **Content merge.** The figures are the site's real winter data
  with their real sources; the count is how the instrument
  arrives at the reading the copy already states in its sentence
  nearby (figure and prose agree to the digit — §10's three-
  printings audit applies: prose, figure and §6.17's footer
  record are one dataset).
- **Failure fallback.** No JS: printed values, which are the
  truth anyway. Loop dead mid-count: a 1600ms watchdog snaps to
  final.
- **Reduced-motion variant.** Printed values; no count.
- **Performance budget & mobile variant.** Text updates at most
  every 50ms per figure (20 steps), ≤3 figures concurrent.
  Mobile: identical; figure size 24px.
- **Choreography timeline (v2).** Centre → t=0 count begins →
  steps at grain → t=1200 settled → source line, printed
  throughout, gets its one emphasis: an underline in `--glass`
  draws 300ms as the count lands (the instrument signs its
  reading).
- **State matrix (v2).** *Rest:* printed/settled. *Hover:* none.
  *Focus:* a figure in a focusable block counts if armed,
  regardless of scroll (focus = arrival, §6.4's rule). *Active:*
  n/a. *Scrolled-past:* settled. *Disabled:* printed. *Touch:*
  identical.
- **Breakpoints (v2).** All: as specced; figures wrap in pairs
  on mobile rather than shrinking below 24px.
- **Edge cases & failure modes (v2).** *Figure is zero (no snow
  this week):* prints "0 cm" with its source line and does not
  count (zero is a reading, not a ceremony). *Live data changes
  the value between visits:* the DOM value is the value; the
  count targets whatever the page printed — the instrument
  settles to the truth it was given.
- **Accessibility spec (v2).** The printed value is the accessible
  value at all times (the counting layer is a visual overlay on
  the same text node — implemented by animating the node's text
  only after copying the final value into a visually-hidden
  sibling that AT reads; §10 checks the tree mid-count). Source
  lines are plain text, never `aria-hidden`.
- **Tokens consumed (v2).** `--ink`, `--glass`, `--ease-thaw`,
  `--dur-count` (1200ms).

### 6.17 The hearth footer

- **What & why.** The foot of the pane is the hearth: a `--dusk`
  field where the frost is thinnest of all (the room's warmth
  rises and gathers at the base of the glass), carrying the
  colophon, the house's plain legal lines, repeat navigation, and
  the winter record — the season's figures from §6.16, printed
  again as the footer's ledger. It belongs because every winter
  house is judged by its hearth, and a footer that went cold and
  corporate would betray the whole visit at the last step.
- **Structure.** Full-width `--dusk` footer: three columns ≥1200px
  (the house: name + one Spectral line; the way back: nav repeated
  as text links with small clearings, §6.11's grammar at rest; the
  record: §6.16's figures in small tabular rows with their source
  lines shortened but present). Below, the legal line in small
  `--frost` at 6.46:1, plain and complete. The frost layer over
  the footer is capped at C = 0.08 locally (a footer-local density
  multiplier in §5's model) — the frame's bottom corners still
  grow (§6.1), but the field between them stays nearly clear.
- **Motion spec.** Entry: the footer's columns light in §6.12's
  stagger grammar (90ms, `--ease-glow`) as the footer centres —
  the last lamps of the page. The record's figures do not recount
  (§6.16's rule); they stand printed. One ambient beat: every
  9000ms, a single droplet at the footer's top edge (where the
  cold field meets the hearth) swells and falls 14px, fading —
  meltwater off the frame, the page's slowest punctuation. Pauses
  off-screen and under reduced motion (where it never runs).
- **States.** Unlit (JS-armed) → lit (rest). The droplet: resting
  → falling → resting, on its 9s clock, only in view.
- **Content merge.** The record is §6.16's dataset's second
  printing; the nav is the site's real nav; the legal line is the
  house's real legal line. The hearth burns the house's own wood.
- **Failure fallback.** No JS: lit, printed, droplet absent.
- **Reduced-motion variant.** Lit from the start; no droplet.
- **Performance budget & mobile variant.** One droplet animation
  per 9s; columns stack on mobile with the record last (you read
  the house, then the way back, then the winter).
- **Choreography timeline (v2).** Footer centres → columns light
  stagger 90ms → droplet clock starts on first full view → falls
  at +9000, +18000… while in view.
- **State matrix (v2).** *Rest:* lit. *Hover:* links take §6.11's
  widening clearings. *Focus:* same + ring. *Active:* n/a.
  *Scrolled-past:* lit; droplet clock pauses off-screen.
  *Disabled/no-JS:* printed. *Touch:* no widening; targets ≥44px.
- **Breakpoints (v2).** ≥1200px: three columns. 768–1199px: two
  columns (house + record; nav as a row above). <768px: stacked
  per mobile variant.
- **Edge cases & failure modes (v2).** *No record data (a site
  with no §6.16 figures):* the record column is omitted, never
  filled with invented weather — the footer is two columns and
  the hearth is smaller, honestly. *Very long legal line:* it
  wraps inside its clearing-free field (legal text never sits
  under frost, §3 law 1 — the footers' local cap exists precisely
  so this line is always on clear dusk).
- **Accessibility spec (v2).** A real `<footer>` with labelled
  nav (`aria-label="Footer"`); figures as text rows; droplet
  `aria-hidden`. Contrast: `--frost` on `--dusk` 6.46:1
  throughout, including the legal small print.
- **Tokens consumed (v2).** `--dusk`, `--frost`, `--lamp`,
  `--ease-glow`, `--stagger-lamp` (90ms), `--footer-cap` (0.08),
  `--dur-droplet` (9000ms cycle).

### 6.18 The wiped pane — the missing page

- **What & why.** The 404: a pane someone has wiped almost
  entirely clear, looking for a page that is not in the room.
  One handprint-wiped area (larger than §6.2's patch, a little
  desperate at the edges), through it an empty chair by the fire,
  and the keeper's note. It belongs because even the theme's
  failure state is a scene in its world — a missing page is a
  room you cannot find, and the wipe says someone already looked
  for you.
- **Structure.** A short page: the pane at C = 0.10 with one large
  wiped region (the §6.2 mask construction at 1.6× scale, edges
  more feathered — this wipe was hurried). Inside the clearing:
  the plain fact first ("This page is not in the house."), then
  the keeper's line in Spectral, then two real links (the door —
  home; the corridor — the section index) as §6.11-style cleared
  labels. A §6.9 figure of an empty chair is optional and, if
  used, is a real photograph with real alt ("The chair by the
  fire, empty"), never a clip-art ghost.
- **Motion spec.** On load: the wipe *finishes* — the clearing's
  last 15% clears over 700ms `--ease-wipe` as if the hand has
  just passed (the visitor arrives a moment after the keeper
  looked). Then stillness: this page has no idle growth (§6.3 is
  suspended — a wiped pane held clear by attention), no counters,
  no fern beyond the branches of pages actually read to get here
  (in practice: the fern renders with zero new branches; §6.5's
  honesty forbids growing one for a page that is not a section).
- **States.** Wiping (700ms) → clear-and-still (rest). Links
  behave as §6.11's.
- **Content merge.** The scene is the error: the clearing, the
  empty room, the note and the way back are one composition whose
  subject is the missing page itself.
- **Failure fallback.** No JS: the wipe is complete in the static
  mask; the page stands clear and still. Nothing to fall back
  from.
- **Reduced-motion variant.** Fully wiped from first paint.
- **Performance budget & mobile variant.** The cheapest page on
  the site: one mask, no loops at all — the stillness is also a
  performance statement. Mobile: clearing full-width, links stack.
- **Choreography timeline (v2).** t=0–700 final wipe → rest.
  No further beats exist on this page; §10 verifies the absence
  of loops (a restless 404 is a §9 failure).
- **State matrix (v2).** *Rest:* clear, still. *Hover/focus:*
  link clearings widen (§6.11). *Active:* n/a. *Scrolled-past:*
  the page is shorter than a scroll. *Disabled:* printed.
  *Touch:* tap targets ≥44px.
- **Breakpoints (v2).** ≥1200px: clearing 1.6× §6.2's patch.
  768–1199px: 1.4×. <768px: full-width band.
- **Edge cases & failure modes (v2).** *The missing URL is a
  mistyped section that exists under another name:* the keeper's
  note gains a third link — the nearest real page, computed by
  the server, printed as a fact ("The nearest room is the
  Cabins.") — never a search box dressed as help. *Soft 404s*
  (empty listing results) reuse this composition at 1.0× scale
  inside the listing page (§7), with the same stillness.
- **Accessibility spec (v2).** The fact is the `<h1>`; the
  keeper's line is a paragraph, not a heading; links are
  descriptive ("Back to the door — home"). Status is conveyed by
  the server's real 404, never by the scene.
- **Tokens consumed (v2).** `--frost`, `--ink`, `--ease-wipe`,
  `--dur-wipe-404` (700ms), `--coverage-404` (0.10).

## 7. Page application map

- **Home.** The full grammar: §6.12 hero, cold passage (the
  house's story), warm rooms (cabins §6.13, menu), the science
  fern (§6.8) if the house keeps one, the pin (cabin interior,
  160vh) before the final cold passage, booking form (§6.14) as
  the closing room, hearth footer (§6.17). Fern branches = the
  home page's true section count.
- **Listing (all cabins).** A colder page: hero reduced to the
  name patch over a cold passage, the card grid (§6.13) as the
  body, one warm room only (the keeper's pick, §6.4) to keep the
  corridor from becoming a showroom. Filters, if any, are §11's
  cleared-label controls on the dusk band — never a sidebar of
  plastic chips on glass.
- **Detail (one cabin).** A warm page: §6.9 figures large, the
  room's facts as §6.16 figures with their instruments ("sleeps
  four, counted in beds"), the booking form (§6.14) in the final
  third, and the page's one licensed afternoon exception — none;
  this theme has no time-of-day, and a detail page simply runs
  warmer: base warmth floor 0.3 so the room never fully cools
  while its facts are read.
- **About (the keepers).** Portraits as §6.9 frames with the
  sitters' names in clearings; the science fern (§6.8) often
  lives here on non-science sites, as the keepers' explanation
  of their own window. Cold passages dominate; warmth is in the
  faces.
- **Contact / booking.** §6.14 nearly whole: a short cold
  approach, the form's dusk panel, the thumbprint submit, the
  wipe confirmation. No cards, no pin — a page for speaking
  through the glass should not make the visitor tour the house
  first.
- **The missing page.** §6.18, and empty states everywhere take
  its stillness at smaller scale.

## 8. Worked examples

### 8.1 The hero — "Fern Cabin, above the tree line" (home)

The site is a three-cabin winter lodge. The page loads: §6.1's
fronts grow from four corners over 2000ms `--ease-grow`, bottom
corners at 0.85×, stopping 120px clear of the reserved patch.
At t≈900 the fronts pass the patch's latitude; the headline —
"Fern Cabin" in Spectral 300 at 56px, with the standfirst "Three
cabins, one fire, and the snow kept outside" — frosts at its
letter edges over 600ms, holds 250ms, then clears centre-outward
over 900ms `--ease-wipe`. Beneath the patch, the furniture lights
in order (§6.12): standfirst's glow underlay at clearing-complete
+0ms, the photograph of the cabin's fireside (§6.9, rim at rest,
warmth 0) at +90ms, the keeper's line — "Marta keeps the kettle
on." — at +180ms, the scroll cue at +270ms; the cue's fern takes
its single pulse at +1470ms. Scroll timeline from there: the
first 300px of scroll is pure §6.3 — velocity stays under the
melt line, C holds at 0.18, the frost layer parallaxes 0.92×
(±14px clamp); the hero's photograph enters its scrub band and
its rim begins its 30% retreat; at the first cold passage's
heading crossing the 55% line, the fern (§6.5) unfurls branch one
over 400ms and the status text steps to "Section 1 of 6". If the
visitor instead sits still on the hero for 30 seconds: idle arms
at 3s, eleven growth steps land by ~30s (C ≈ 0.27), the corners
thicken visibly, the patch and the room do not change — the law
holds at every frame, and §10's cap audit samples exactly this
scenario.

### 8.2 Mid-page — the science fern in "How frost thinks" (home, section 4)

The cold passage turns to explanation. A `--dusk` panel enters;
its centre crossing 60% vh triggers §6.8: the stem draws 0–700ms,
the five pairs begin at 600/820/1040/1260/1480ms, each drawing
420ms with branchlets in its last 40%, and the labels — printed
from first paint — brighten pair by pair at 1020/1240/1460/1680/
1900ms: "The stem grows toward the coldest glass." / "Each pair
leaves at forty degrees — the angle water chooses." / … The
visitor hovers the third label: pair three's strokes lift from
`--fern` to `--frost` over 200ms; the fact they are reading is
the branch they are touching. Meanwhile §6.3 idles: the visitor
has not scrolled for 9 seconds (they are reading), so two growth
steps land on the corner fronts — the panel, being a cold
passage, takes no warmth exemption, and the frost around the
science is honestly thicker than the frost around the cabins.
Scrolling on at reading pace (<400px/s) holds C; a flick to the
booking form melts 0.02 per 100px, and the fern unfurls branch
four in its 120ms hurried queue as sections pass. The worked
point: three systems (draw, idle growth, fern) run concurrently
from one loop, none covering the panel's text at any frame —
§13's map shows their beats interleaved.

### 8.3 Conversion — booking Fern Cabin's small room (detail → form)

From the cabin's detail page (warmth floor 0.3, §7), the visitor
reaches §6.14's dusk panel: dates, two guests, a name, and a note
— "We arrive by the late train; please leave the lamp." Each
field is a clearing; focus on the date field sharpens its edge
over 200ms and draws the `--lamp-deep` rule. The visitor first
picks a leaving date before the arriving one: on submit, the
error stands inside that field's clearing in the keeper's voice
— "The leaving day is before the arriving one. Even the snow
waits to fall before it melts." — input preserved, focus returned
to the field, nothing exiled to a banner. Corrected, the second
submit presses the thumbprint (§6.10): the button depresses, one
droplet falls from the rim, the apparatus line "Writing to the
keeper…" appears at 1200ms; the answer returns at ~1600ms and the
panel wipes clear over 800ms `--ease-wipe`. In the cleared glass:
the facts read back (dates, guests, the note's first line), the
keeper's fixed reply (§12), and the reference "Fern Cabin — the
14th to the 21st, entered as № 7 in the winter book", the number
counted from §6.17's ledger element on the page, not generated.
The fern grows no branch for this; the hearth, when reached,
already holds the booking in its record column's count of nights
— one dataset, three printings (§6.16).

## 9. Anti-slop — what makes THIS theme look cheap

1. **Frost as a stock photo overlay.** A PNG of frost pasted over
   the page, static, identical on every page. *Cure:* the frost
   is drawn SVG geometry grown by §5's model from the page's own
   layout; if it does not respond to idle, scroll and warmth, it
   is not this theme.
2. **Blur standing in for frost.** `backdrop-filter: blur()` over
   content, called "frosted glass". *Cure:* crystals are strokes,
   not blur; the only softness licensed is §6.7's gradient fog,
   applied to the fog itself. Blurred text is an automatic fail.
3. **A clean CSS radial-gradient "wipe".** A perfect ellipse with
   a gradient edge reads as a spotlight, not a hand. *Cure:*
   authored smudge masks with palm-drag lobes (§6.2/§6.10); if
   the clearing's edge is a perfect curve, redraw it.
4. **Amber everywhere.** Lamplight buttons, amber links, a warm
   gradient hero — the ration spent, the metaphor dead. *Cure:*
   `--lamp` appears only through glass, on warm content, plus
   the one solid CTA surface (§6.10). §10 greps lamp usage
   against the room/CTA whitelist.
5. **Frost that grows while you read-scroll.** Growth triggered
   by a naive timer that fires during slow reading scroll, so the
   page freezes while being read. *Cure:* §5's velocity model —
   growth requires 3000ms of *no input*; slow scroll holds.
6. **Random particle frost.** A canvas of drifting snow dots
   labelled frost. *Cure:* authored dendrites with the fern
   habit (stem, 40° pairs, needle shoots); snowfall is weather
   outside a different window and appears nowhere in this theme.
7. **A fern with the wrong number of branches.** Progress
   furniture copied from another page, counting sections that
   are not this page's. *Cure:* branch count is generated from
   the page's outline at build (§6.5); §10 diffs them.
8. **The science fern replaced by an illustration.** A stock
   crystal image in the science section. *Cure:* §6.8's draw is
   the section's figure; its labels are the facts. No substitute
   ships.
9. **Clearings that can freeze.** Any code path — a growth bug,
   a transition, a resize — that lets frost cross the patch or
   the thumbprint. *Cure:* exclusion by mask construction (§4),
   plus §10's scripted siege: idle 10 minutes, fling, resize,
   transition-spam — the clearings are audited after each.
10. **A spinner in winter.** Generic loading UI inside the pane.
    *Cure:* §6.15's frosted skeleton and hand-wipe; waiting is
    weather here.
11. **Hover states that lift cards like app tiles.** Shadows,
    scales, glows borrowed from SaaS. *Cure:* cards lean and
    straighten like panes (§6.13); warmth, not elevation, is the
    hover language.
12. **Exclamation-point copy in a whispering theme.** "Book NOW
    before the snow melts!!" *Cure:* §12's voice; the keeper
    does not shout through glass.

## 10. Quality gate

Blocking — all must pass before a Frost Fern page may ship:

1. **Law audit.** Rendered frost coverage ≤ 0.38 at every sampled
   frame (load, idle 60s, cap arrival, mid-transition); headline
   patch and CTA thumbprint pixel-tested clear at every sample.
2. **Siege test.** Scripted: 10-minute idle, fast flings, slow
   reading scroll, resize storm, transition spam, tab hide/show —
   after each, both clearings are clear, C ≤ cap, no segment is
   left half-grown.
3. **No-JS pass.** JavaScript disabled: every page complete and
   readable, frost a static frame, forms submittable, counters
   printed, fern grown, skeleton absent.
4. **Reduced-motion pass.** The finished still pane: coverage
   resting, clearings open, no loops running (verified by
   sampling `requestAnimationFrame` callbacks over 10s — only
   the shared loop's idle tick may exist, writing nothing).
5. **Contrast audit.** Content measured with the frost layer
   *removed* and with card veils at rest: `--ink`/`--frost`
   10.51, `--ink-warm`/`--room` 8.94, `--frost`/`--dusk` 6.46,
   CTA 5.87, card text through veil ≥4.5.
6. **Lamp ration audit.** `--lamp` occurrences in the built CSS
   resolve only to §6.4 glow shapes, §6.9 shadow warmth, §6.12
   underlays and §6.10's button; `--lamp` text below 24px: zero.
7. **Fern truth audit.** Branch count = section count per page;
   text equivalent present; growth order matches DOM order.
8. **Figure audit.** Every §6.16 figure has a source line; prose,
   figure and footer record agree to the digit; no figure exists
   that is not a temperature, snowfall, distance or ledger count.
9. **Form-keeping rehearsal.** Submit §6.14 with each error
   class: input preserved, error in place in the keeper's voice,
   focus correct, confirmation reference traceable to the page's
   ledger; action fires at click with animations disabled.
10. **Pointer-events proof.** Automated click-through at 40
    random viewport points: every click lands on room content,
    never on the frost layer.
11. **Performance pass.** §14's budgets measured on the reference
    mid-tier phone: frame budget, layer weight, no long task
    >50ms during growth, melt and wipe.
12. **One-pin & two-thumbprint census.** Exactly one pinned scene
    per page; thumbprints ≤2, both around the conversion;
    glow shapes = `.room` count, one-to-one.

## 11. Component inventory

Every component a real Frost Fern site needs, with its themed
treatment. Refusals are part of the inventory: a component the
theme refuses is listed with its in-world replacement, so a
builder never imports the generic version by default.

- **Buttons (primary).** Only inside §6.10's thumbprint: `--lamp`
  ground, `--ink-warm` text, 48px, radius 3px. There is no
  secondary primary.
- **Buttons (secondary).** Cleared-label buttons: text in a small
  static clearing on `--dusk` or on cold ground, `--ink` text,
  hairline `--glass` rule beneath that melts (widens its clearing)
  on hover/focus (§6.11's grammar).
- **Links (inline).** `--ink` with a `--glass` underline; on warm
  panels `--ink-warm` with a `--lamp-deep` underline. Never amber
  text (§9.4).
- **Inputs / selects / textareas.** §6.14's clearings, without
  exception — a form anywhere on the site uses the glass-writing
  treatment. Selects open their list *below* the glass line: the
  list is a `--dusk` sheet with cleared rows.
- **Date fields.** Two clearings and a printed dash between them
  (the register's dash, borrowed from §6.14's worked grammar);
  no calendar popover — a calendar is a plastic widget on glass;
  the keeper's voice corrects impossible dates instead.
- **Cards.** §6.13, the only card.
- **Tables.** A winter ledger table: rows on alternating `--frost`
  / `--room` (cold row, warm row), figures tabular Inter, the
  header row on `--dusk` in `--frost`. Tables never sit under
  moving frost — they live in warm rooms or below the coverage
  floor.
- **Badges / tags.** Refused. A badge is a sticker on the window.
  Replacement: a line of label-style text in a clearing ("The
  keeper's pick" written on the glass beside the card).
- **Alerts.** A note from the keeper: a `--dusk` strip across the
  column with the message in `--frost` and one cleared action
  label. Never a coloured toast; weather is the only thing that
  arrives uninvited on this pane.
- **Toasts.** Refused — replaced by the alert strip, or by
  in-place state (the form's confirmation, the card's afterglow).
- **Modal dialogs.** Refused as overlays. Replacement: a full-pane
  sheet (§6.11's mobile menu pattern at any size) — the visitor
  steps to another part of the glass; focus custody per §6.15.
- **Tabs.** Refused. Replacement: sections in sequence with the
  fern (§6.5) as the map — winter pages are walked, not tabbed.
- **Accordion.** A row of small panes: each item a §6.13-leaned
  strip that straightens and clears (its veil thins to 20%) when
  open; one open at a time; answers fully in the DOM (closed
  state is JS-armed only).
- **Pagination.** "Further into winter" / "Back toward the door"
  cleared-label links with the count as a ledger line ("Cabins
  1–6 of 9, counted at the door"). Numbered page chips refused.
- **Search.** A single clearing in the header band (§6.11) with
  the keeper's empty state (§6.18's stillness at small scale).
- **Breadcrumbs.** Refused — replaced by the fern + the header's
  current melt-line (§6.11); a trail of crumbs on glass is litter.
- **Progress bar.** Refused — the fern (§6.5) is the progress.
- **Spinner.** Refused — §6.15's frosted skeleton is the loading.
- **Tooltip.** Refused. Replacement: the label itself lengthens
  (§6.5's hover label pattern) — explanations are written on the
  glass, not floated over it.
- **Toggle / switch.** A wiper switch: a small clearing with a
  thumbprint that slides 24px over 250ms `--ease-wipe` between
  two printed states ("Lamps lit" / "Lamps out"). The state words
  are always visible; the switch never carries meaning by
  position alone.
- **Slider.** Refused (a slider is a machine control; the pane
  has none). Replacement: stepped cleared-label choices.
- **Image gallery.** §6.9 frames in a row; selecting one centres
  it (scroll) rather than opening a lightbox — lightboxes refused.
- **Video.** A §6.9 frame whose rim retreats fully on play and
  returns on pause; the poster's warmth is the video's own first
  frame. No autoplay, ever — nothing moves in the room unasked.
- **Price / figure display.** §6.16's grammar: value, label,
  source line.
- **Divider.** A frost line: a 1px `--glass` rule with a small
  fern glyph at its centre, drawn (not grown) at section
  boundaries inside the column.
- **Footer.** §6.17, the only footer.
- **404 / empty state.** §6.18, the only pattern.

## 12. Content & copywriting voice

Two registers, per §3 law 2. **The Keeper** (Spectral) speaks
from inside the room: warm, brief, unhurried, first person
plural or the house's name; sentences end; nothing is urged.
**The Glass** (Inter labels) is written on the window: terse,
factual, instrumental — labels, figures, furniture.

- **Headlines (Keeper).** A statement of the room, not a promise:
  ✓ "Three cabins, one fire, and the snow kept outside."
  ✗ "Your dream winter escape awaits!!" (§9.12).
- **Labels (Glass).** Instrument readings: ✓ "TONIGHT, FROM THE
  PORCH THERMOMETER". ✗ "Check out tonight's amazing temps!".
- **Buttons.** The door's words: ✓ "Ask for the small cabin".
  ✗ "BOOK NOW". The CTA names the act as a request to a person,
  because it is one.
- **Error messages (Keeper, in place, §6.14).** The keeper
  corrects as one adult to another, with the weather as the only
  metaphor allowed: ✓ "The leaving day is before the arriving
  one. Even the snow waits to fall before it melts."
  ✗ "Invalid date range." / ✗ "Oops! Something went wrong."
- **Empty states (Keeper, §6.18).** ✓ "This page is not in the
  house." then one plain line of fact, then the way back.
  ✗ "404 — looks like you're lost in a blizzard!"
- **Confirmation (Keeper, fixed frame).** "Entered in the winter
  book." + the facts read back + the reference (§8.3). The frame
  is verbatim across the site; only the facts change.
- **Banned words.** *Blizzard* (unless the weather is one, with a
  figure and a source), *cosy* more than once per page (the room
  proves it; the word needn't insist), *escape*, *dream*,
  *magical*, any exclamation mark in Keeper copy, and percentages
  for warmth or welcome ("100% cosy" is §9 slop in a sentence).
- **Owned words.** *Kept* (the kettle is kept on; the invitation
  is kept clear), *the door*, *the book* (the winter book = the
  ledger), *beyond the glass*, *at the door* for prices held
  back (§6.13).
- **Figures in copy** obey §3 law 5 and §6.16: every number in a
  sentence could be read off the porch thermometer, a ruler in
  the snow, or the winter book — and if it is in a sentence, the
  same number stands in the figure block and the footer record.

## 13. Full-page scroll choreography map

The home page (§7's assembly), top to bottom. Every beat names
its system so the map doubles as the build's integration test.

1. **Arrival (no scroll).** §6.1 growth (2000ms) → §6.2 edging
   and clearing (t≈900–2650) → §6.12 lighting stagger → the pane
   rests at C = 0.18. The visitor has been *let in visually*
   before touching anything.
2. **First scroll (0–600px).** §6.3 holds (velocity < melt line);
   frost parallax 0.92×, hero figure's rim begins retreating
   (§6.9); §6.11 header compresses at 140px.
3. **Cold passage 1 — the house's story.** Full local frost
   density at the margins; §6.16's first figure (tonight's low)
   counts as it centres; fern branch 1 unfurls at the passage's
   heading.
4. **Warm room 1 — the cabins.** §6.4 warmth bell: glow rises,
   frost over the room thins to 0.4×; §6.13 cards light in their
   90ms stagger; a hovered card melts (§6.6), a clicked one
   breathes (§6.7). Fern branch 2.
5. **The pin — inside the cabin (160vh).** The room pins behind
   nearly-clear glass: coverage over the pin's field is forced
   to its local floor while §6.3's idle growth creeps *only at
   the corners* — the visitor is inside now, and the weather is
   at the window's edges, where it belongs. Fern branch 3 at the
   pin's midpoint.
6. **Cold passage 2 — how frost thinks.** §6.8's fern draws
   (2000ms) as the panel centres; idle steps accumulate honestly
   around the cold copy; the week's snowfall figure (§6.16)
   counts down through its cm. Fern branch 4.
7. **Warm room 2 — the menu / the table.** Warmth bell again;
   §6.9 figures of the food warm in their shadows; the room's
   glow is the page's second and last full warm beat (§4's
   density law made visible as rhythm). Fern branch 5.
8. **The booking room.** §6.14's dusk panel thins as it centres;
   §6.10's thumbprint re-beads on its 6s clock as the panel
   enters (its one near-view start); form beats per §8.3. Fern
   branch 6 unfurls as the panel's heading crosses — the form
   *is* a section here (contrast §6.14's timeline note: the
   branch belongs to the room's heading, never to the submit).
9. **The hearth.** §6.17 lights in stagger; the record stands
   printed; the droplet clock starts. Scroll ends with the glass
   nearly clear at the foot and the corners grown — the page's
   last image is a warm base and a cold frame: the house, held.
10. **Reverse pass.** Scrolling up: §6.9 rims re-form, §6.4
    rooms cool and re-warm symmetrically, §6.3 melts nothing
    (up-scroll is still scroll — velocity rules apply identically),
    the fern does not un-grow, lamps do not re-light (they never
    went out). The asymmetry is the theme's memory: *weather is
    reversible; reading is not.*
11. **Jump scroll (anchor / find / scrollbar).** Coverage eases
    to the destination's scrubbed values over 600ms; fern
    branches queue at 120ms; §6.8, if jumped past, is found grown.

## 14. Whole-page performance budget

- **Total page weight ≤ 780KB** (HTML/CSS/JS/images at the
  reference build, fonts subsetted: Spectral 300/400/600 + italic,
  Inter 400/500/600 — ≤120KB of font in total; photographs are
  the budget's bulk and are sized to their frames, never larger).
- **Frost layer ≤ 30KB** inline SVG across all groups (§6.1 18KB,
  §6.5 6KB, §6.10 3KB, header strip reuses defs) — the theme's
  signature material is also its cheapest asset.
- **Frame budget.** The shared loop writes, per frame, at most:
  4 dashoffsets (growth fronts), 1 coverage-derived mask value,
  per-in-band-room 2 values (glow alpha, density crossfade),
  per-in-band-figure 3 values, 1 melt centre/radius pair for the
  single hovered card, fern/parallax transforms — a ceiling of
  ~20 style writes/frame, all transform/opacity/mask properties;
  **no layout, no paint of text layers, ever**. Target ≤1.2ms of
  main-thread work per frame on the reference mid-tier phone;
  long tasks >50ms: zero during growth, melt, wipe and count.
- **The loop sleeps.** When nothing is scrubbing, melting,
  growing or breathing, the rAF loop unregisters itself and is
  re-armed by the next input/observer event; idle growth steps
  are timer-scheduled (2500ms), not loop-polled. A resting Frost
  Fern page consumes no more battery than a printed one.
- **Cut order** (when the budget is exceeded, cut in this order,
  never out of it): 1) §6.17's droplet; 2) §6.9's shadow-warmth
  overlay (rims stay); 3) §6.4's density crossfade (glow stays,
  frost over rooms at fixed 0.7×); 4) §6.12's glow underlays
  (stagger becomes a plain rise); 5) §6.6's droplet rims (melt
  stays, beads go); 6) §6.1's sub-branch density (fronts stay).
  **Never cut:** the two clearings' mask integrity, §6.3's model
  itself, §6.5's text equivalent, any fallback or watchdog, the
  form's in-place errors.

## 15. Build-order checklist

1. **The room first.** Build the complete page with no frost:
   content, forms, figures printed, nav, footer. It must pass
   §10's no-JS pass in this state — because this state *is* the
   fallback.
2. **Reserve the clearings.** Lay out §6.2's patch and §6.10's
   thumbprint geometry from the rendered boxes; build the frost
   layer's mask with both holes. Verify the law (§1) with the
   layer at forced full coverage before any crystal is drawn.
3. **Author the crystals.** Draw §6.1's four corner groups (and
   the mobile pair) with stop-lines measured from step 2's
   geometry; author ~26 growth steps of headroom per front.
4. **The growth model.** Implement §5's single loop + §6.3's
   state machine; wire velocity from position deltas; rehearse
   the siege (§10.2) before any other element is added.
5. **The fern.** Generate branch count from the page outline;
   build §6.5 + its text equivalent; verify the count diff.
6. **Warmth.** Mark `.room` sections; build §6.4's glow/density
   pair per room; audit glow shapes = rooms (§10.12).
7. **Cards and veils.** §6.13 with §6.6 melt and §6.7 breath;
   audit card text contrast through resting veils (§10.5).
8. **Figures and frames.** §6.9 rims; §6.16 counters with source
   lines; run the three-printings figure audit (§10.8).
9. **The science fern** (§6.8) with labels in growth order in the
   DOM.
10. **Header and hearth.** §6.11 (with the clearing-merge rule),
    §6.17 (with the footer-local cap wired into the model).
11. **The form.** §6.14 on the §11 inventory's rules; keeper-
    voice errors (§12) written before any are triggered;
    form-keeping rehearsal (§10.9).
12. **Loading and leaving.** §6.15 skeleton + transition with
    focus custody; §6.18 last — the still page, verified loop-free.
13. **Reduced-motion and print.** The still pane end-to-end;
    print stylesheet (room only).
14. **Gate.** Run §10 in full, signed by someone who did not
    build the page. The gate's signature line is part of the
    deliverable: a Frost Fern page that has not been sieged has
    not been built.
