# 95. The Cartographer's Table — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never
redesigned).** The visitor's journey across the site is a voyage
being charted live on a hand-drawn map — the page literally draws
its own coastline as you travel through it. Palette anchors:
vellum `#EFE6D0`, sepia ink `#43382A`, madder red `#8C4A2F` (the
route), sea-wash teal `#476C6B`, compass brass `#C2A15C`. Type:
IM Fell English (display — 17th-century print), IM Fell English
SC (labels), Libre Franklin (small modern annotations). One great
vellum map underlies the page; sections are "landfalls" at points
along the madder-red route line; a map panel pins for a zoom
sequence mid-page; compass roses, depth soundings and hatched
coastlines throughout; grain deepens over surveyed regions. For
travel storytellers, tour operators, expedition and logistics
brands, geography education. The original entry's anti-slop
detail is kept verbatim as §6.10: the map is hand-lettered
*"Here be delays"* over the section everyone usually skips.

## 1. Concept & world

The Cartographer's Table is the website of a survey still in
progress. On the great age-of-sail charts this theme descends
from, a coastline was not a fact the cartographer looked up; it
was a record the voyage earned — drawn league by league as the
ship made its landfalls, hatched where the survey boats had
sounded, left blank where no one had yet been. This page works
the same way on its own content. The visitor does not *view* the
site; they *sail* it, and the chart beneath the page is the log
of their sailing: the coastline sketches in as the first scroll
begins, the madder route draws itself from landfall to landfall
in exact scroll sync, place-names are engrossed — lettered by a
slow hand — only when the route reaches them, and the vellum
grain deepens over every region the reader has surveyed, so the
map at the foot of the page is visibly more worked, more known,
than the map at its head. The page is not illustrated by a map.
The page *is* the chart, and reading it is the act that draws it.

The world the page performs is a chart table in a harbour office:
vellum under a brass straightedge, a compass rose that actually
points somewhere, soundings pricked along the coast in a
surveyor's small numerals, and — in the margin, where the honest
cartographer always worked — the admissions: a shoal marked, a
coast left blank, and over the one dull stretch, in the same
hand as everything else, *"Here be delays."* Nothing here is
pirate fancy-dress. There are no skulls, no "ahoy", no treasure
crosses. The romance of this theme is the romance of *accuracy
being earned*: a name exists because someone arrived there; a
depth exists because someone lowered a line; a region is dark
with hatching because someone did the work.

**The theme's one law: the chart records only where the reader
has been.** Three clauses, all audited by the gate (§10).
(1) *Nothing is drawn ahead of the journey.* Coastline, route,
names, soundings and hatching exist on screen only as far as
the reader has travelled. Territory below the reader's position
is honestly unworked — blank vellum, or fog (§6.5) where the
theme wants mystery with a promise — never pre-drawn and merely
dimmed, because a chart that shows the whole coast on load and
calls the dimming "animation" is wallpaper, not a survey.
(2) *Ink is permanent.* Once a stretch of coast is charted it
stays charted. Scrolling back up never un-draws the route, never
un-letters a name, never lightens hatching: the ratchet is the
theme's honesty about records — a log that erases itself is a
lie about the voyage. (The single licensed exception is the
needle, §6.6, which is an instrument, not a record, and may
swing as instruments do.) (3) *The finished chart underlies
everything.* Every drawn element is a complete, finished SVG
wearing a dash mask or a clip; the draw-on is a performance
laid over a finished artefact, never the artefact's only form.
With JavaScript dead, a stalled loop, or a flung scroll, what
remains is the whole chart, fully drawn — never a blank sea.
Clause 3 is the original entry's reliability rule, kept
verbatim in spirit: route and labels exist as finished SVG
beneath the dash-offset draw-on.

**Best-fit sites and audiences.** First, the original entry's
own list, which is exact: travel storytellers (a journey
narrated as it is charted — the form *is* the story), tour
operators and expedition outfitters whose product is a route
with stages, logistics and shipping brands whose truth is a
line across water or land with named stops, and geography
education, where the drawing of the map is the lesson. Then,
by the law's logic, any business whose offer is a *progression
the customer travels*: a relocation firm charting a family's
move city by city; a genealogy service charting a family's
coast backwards; a winery whose vintages are ports along one
river; a pilgrimage or long-distance trail organisation; a
restoration studio publishing a building's survey as it
proceeds. The audience it suits is going somewhere and enjoys
the going: readers who will watch a name letter itself in
because the lettering *is* the brand's argument — we have been
there, slowly, and we wrote it down. Conversion on such sites
is a berth booked, a tour joined, a passage entered in the
logbook (§6.13) — acts taken at a landfall, in the chart's own
grammar.

**When NOT to use it.** Not for any site the visitor enters
with a destination already fixed and a clock running: support
desks, account dashboards, checkout-first commerce, emergency
or reference information. The chart makes the visitor sail;
a visitor who needs the harbour master's phone number in two
clicks must not be made to round three headlands for it. Not
for catalogues or feeds — forty products are not forty
landfalls, and a route drawn through a grid of SKUs is a lie
about both. Not for dense data: one table of soundings (§6.14)
is the theme's licensed instrument panel; a second table wants
another theme. Not where the client cannot supply a real
journey — real legs, real distances, real depths (§6.7's
voyage object): a chart drawn over invented leagues is a
forgery with good typography. And not for brands whose register
is speed: this theme's fastest event is a wax seal's thud, and
a brand that sells urgency will suffocate under vellum.

## 2. Palette

Five anchors, inherited exactly. Derived tokens form a closed
list: a token not in this table does not exist in the theme,
and the gate greps built CSS for undeclared hex values.
Contrast figures below are measured, not estimated.

| Token | Hex | Role | Usage ratio | Pairing & contrast (measured) |
|---|---|---|---|---|
| `--vellum` | `#EFE6D0` | Vellum — the page's ground, the chart sheet itself | ~52% of viewport area | Carries `--ink` at **9.20:1**, `--ink-deep` at 12.12:1, `--sepia-soft` at 5.27:1, `--madder` at 5.39:1, `--teal` at 4.66:1. The ground is a material, not a background colour: grain (§4) lives on it. |
| `--ink` | `#43382A` | Sepia ink — body text, coastline strokes, hatching | ~14% | On vellum 9.20:1 — the reading colour. On `--vellum-deep` 7.72:1. Ink is what the hand draws with; it is never a surface. |
| `--madder` | `#8C4A2F` | Madder red — the route line, the wax seal, the one warm accent | ≤3% (rationed, §5) | On vellum 5.39:1 — licensed for the route (a line, read as a path, not text), ≥18px display text, and the seal. Small text in the madder register uses `--madder-deep`. On `--night` 2.49:1 — **forbidden**: the route never sails the night ground without its vellum underlay (§6.17). |
| `--teal` | `#476C6B` | Sea-wash teal — the sea itself: wash fields, water ornament, chart furniture | ~16% | On vellum 4.66:1 — large text, labels ≥14px and graphics only; body text in the teal register is `--teal-deep` (6.95:1). On `--night` 2.88:1 — forbidden for text; sea-wash on night is a fill at ≤40% strength, never lettering. |
| `--brass` | `#C2A15C` | Compass brass — the instruments: roses, needle, scale bars, rules | ~6% | On vellum **1.98:1** — graphical only, at any size, without exception: brass is a metal, not an ink, and never sets text on vellum (§3 law 5). On `--night` **6.78:1** — the one ground where brass may letter (footer imprint, §6.17). |
| `--ink-deep` (derived) | `#2E2519` | Fresh ink — display headings, the engrossed names' final state | — | On vellum 12.12:1; on `--parchment` 13.01:1. Names finish in this tone (§6.3): a name still in `--ink` is a name still being written. |
| `--parchment` (derived) | `#F5EEDC` | The fair sheet — raised panels the copy sits on (§4's fair-sheet rule), card stock, the logbook's leaves | — | Carries `--ink` at 9.87:1, `--sepia-soft` at 5.66:1, `--teal-deep` at 7.47:1, `--madder-deep` at 8.27:1. Slightly lighter than the chart ground so a panel reads as a sheet laid on the table. |
| `--vellum-deep` (derived) | `#E2D3B2` | Worked vellum — inset chart panels, the soundings table's ground, un-scrubbed skeleton tone | — | Carries `--ink` at 7.72:1. The tone of vellum that has been handled: insets and instruments sit on it. |
| `--sepia-soft` (derived) | `#6B5B45` | Pencil sepia — captions, marginalia, chart apparatus, source lines | — | On vellum 5.27:1, on parchment 5.66:1. The annotator's hand (§12): everything that explains the chart rather than being it. |
| `--madder-deep` (derived) | `#6E3520` | Dried madder — small text in the accent register: seal captions, form errors, the delays line's apparatus | — | On vellum 7.71:1, on parchment 8.27:1. Fresh marks (route, seal face) render in `--madder`; their printed captions use the deep tone. |
| `--teal-deep` (derived) | `#33514F` | Deep water — teal-register body text, the sea's labels at reading size | — | On vellum 6.95:1, on parchment 7.47:1. Carries `--vellum` at 6.95:1 when it is the ground (the one licensed teal surface: the soundings table's head row, §6.14). |
| `--brass-deep` (derived) | `#8A6D2F` | Tarnished brass — brass-register display lettering on vellum where lettering is unavoidable (chart titles ≥24px) | — | On vellum 3.92:1 — display only, ≥24px, never body, never labels. A concession with a fence around it; §9 failure 6 is the builder who moves the fence. |
| `--night` (derived) | `#241D13` | The chart room after dark — footer ground (§6.17), the 404's ground (§7) | — | Carries `--vellum` at 13.41:1, `--parchment` at 14.40:1, `--brass` at 6.78:1. The only dark ground in the theme; it is a room in the building, not a mode. |
| `--fog` (derived) | `rgba(239,230,208,.88)` | Chart fog — the unvisited territory's weather (§6.5) | — | A layer, never a colour: vellum-toned, so fogged coast reads as the same sheet under weather, not as a different page. Its opacity is a scrubbed value (§5), never a static design choice. |

**Usage discipline.** A page is roughly half vellum, a sixth
sea-wash, a seventh ink (most of it line-work, not text),
brass as instrument glints, and madder as a single red thread
with a seal at the end of it. The ratio is audited in the gate
(§10): madder pixels above 4% of any viewport means the route
has become a colour scheme; brass *text-shaped* pixels on
vellum at any count fail outright (§3 law 5).

**Dark behaviour — the page does not invert; the chart is read
by lamplight.** The Cartographer's Table is a light theme by
material: vellum is pale because paper is pale. Under
`prefers-color-scheme: dark` the chart grounds stay vellum —
a chart does not turn black at night; it is carried into a
dark room. What changes: the page's outer margins and the
footer deepen to `--night`, sea-wash fields render at 70%
strength (lamplight flattens water first), the fog layer's
strength rises to .92 (night fog sits heavier), and brass
brightens in role — rules and roses unchanged in hex, but the
needle's specular (§6.6) gains its second licensed highlight.
Every text pairing in the table is unchanged in class, because
no text ground changes. A build that "adds dark mode" by
inverting vellum to charcoal has burned the chart to keep the
room lit, and fails §9.

## 3. Typography

**Faces.** IM Fell English — the display face and the
cartographer's hand: a 17th-century print face with the slight
irregularity of type struck from Fell's own punches, which is
why the engrossed names (§6.3) can swell thick-thin inside it
without fancy dress. IM Fell English SC — the label face:
small caps for chart furniture (landfall labels, scale-bar
apparatus, the cartouche's index), the voice of the chart's
printed frame. Libre Franklin — the modern annotator: a clean
grotesque reserved for everything the *site* (as opposed to the
chart) must say plainly — body copy, form apparatus, table
data, source lines. The division is constitutional: **the
chart speaks Fell; the annotations speak Franklin; the two
never swap jobs.** A headline in Franklin is a spreadsheet on
the chart table; body copy in Fell is a novel pretending to be
a website.

**The scale** (desktop; §6 breakpoint tables carry the smaller
sizes):

| Role | Face | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Hero display | IM Fell English 400 | 68px / 1.04 | −0.01em | The departure headline (§6.1); max 8 words (§12) |
| Landfall display | IM Fell English 400 | 44px / 1.1 | −0.005em | One per landfall, at the route's arrival point (§4) |
| Place-name | IM Fell English 400 | 30px / 1.15 | 0 | The engrossed names (§6.3); never below 24px anywhere (§3 law 1) |
| Chart label | IM Fell English SC 400 | 15px / 1.3 | +0.04em | Landfall labels, rose apparatus, scale bars |
| Body | Libre Franklin 400 | 17px / 1.6 | 0 | Measure 58–66ch (§4) |
| Body small | Libre Franklin 400 | 15px / 1.55 | 0 | Card body, logbook entries |
| Annotation / apparatus | Libre Franklin 500 | 13px / 1.45 | +0.01em | `--sepia-soft`; source lines, marginalia, form notes |
| Sounding numerals | IM Fell English 400 | 15px / 1.2 | 0 | Depths along the coast (§6.7) — marginalia, so the chart's hand |
| Table data | Libre Franklin 500 | 14px / 1.5 | 0, tabular lining | The soundings table (§6.14) — an instrument read comparatively, so the modern hand |
| Leagues counter | IM Fell English 400 | 40px / 1.1 | 0 | The voyage's odometer (§6.7) |

**Five type laws.**
1. **Names are engrossed, never set small.** A place-name is
   IM Fell English at ≥24px wherever it appears as a name —
   on the chart, in a card, in the index. Below 24px a place
   is demoted honestly to a *label* in IM Fell English SC;
   the theme never shrinks a name into caption size and calls
   it a name.
2. **The modern hand annotates, never announces.** Libre
   Franklin sets body copy and apparatus only. It never sets
   a headline, a place-name, or the seal's legend. If a
   builder reaches for Franklin to make a heading "cleaner",
   they have brought a spreadsheet to the chart table (§9,
   failure 11).
3. **Type never moves while it letters.** Engrossing (§6.3)
   animates a stroke mask over finished letterforms; layout
   at the first letter is pixel-identical to layout at the
   last — zero CLS is a law, not a metric. The same holds for
   every reveal: fog lifts *off* type (§6.5); type itself
   never fades, rises, or scales into place.
4. **Madder is a line before it is a colour.** Madder sets
   text only at ≥18px (5.39:1) — the seal's legend, a
   landfall's "visited" mark. Below 18px the madder register
   writes in `--madder-deep` (7.71:1). The route itself is
   exempt by kind: a 2.5px path is read as a path, and its
   contrast is audited as a graphic (§10), not as text.
5. **Brass never inks.** At 1.98:1 on vellum, brass sets no
   text on a light ground at any size, in any state, ever.
   Brass lettering exists only on `--night` (6.78:1, §6.17's
   imprint) or, at ≥24px display only, as `--brass-deep`
   (3.92:1) for a chart's title line. A brass caption on
   vellum is the theme's most common forgery and its gate's
   easiest catch (§10).


## 4. Layout language

**One great chart.** The page's foundation is a single SVG
chart layer spanning the full document height, absolutely
positioned beneath the content, drawn at the page's natural
width and never responsive-scaled into illegibility (§6
breakpoints govern its simplifications instead). On it: the
coastline of the site's territory, the master route (§6.2),
the hatching fields (§6.8), the soundings (§6.7), two compass
roses (one in the hero's field, one at the chart's foot — a
chart is signed at both ends), and the sea-wash fields that
give the water its body. Content sections are **landfalls**:
each sits at a point on the route, its text column offset to
the side the route's local course leaves clear — text to
starboard of a northbound leg, to port of a southbound one —
so the composition of every section is decided by the
geography, not by a template's alternation toggle.

**The fair-sheet rule.** Body copy never sits directly on
worked chart. Wherever text is read, it rests on a *fair
sheet* — a `--parchment` panel with the chart's grain showing
at its edges, as if a clean leaf had been laid on the table
over the survey. The chart works around the sheets: hatching
stops at a sheet's edge, the route passes *beside* text,
never beneath it, and soundings keep a 24px clearance from
any sheet. A build that sets paragraphs over coastline has
confused the chart with wallpaper (§9, failure 1's cousin).

**The landfall fractions.** The route's geometry is declared
once, in a route object every element reads: each landfall's
fraction of the route's total length, its leg's length in
leagues, and its leg's bearing. For the worked site (§8) the
object is:

| Landfall | Route fraction | Leg leagues (cumulative) | Leg bearing |
|---|---|---|---|
| Port Aveline (departure) | 0.00 | — (0) | — |
| The Gull Shoals | 0.18 | 38 (38) | 042° |
| St. Cwyll's Harbour | 0.36 | 39 (77) | 078° |
| The Long Reach | 0.55 | 41 (118) | 031° |
| Fog Anchorage | 0.74 | 40 (158) | 105° |
| Cape Meridian (final) | 1.00 | 56 (214) | 063° |

Total voyage: **214 leagues**. Every figure the page prints —
the leagues counter (§6.7), the needle's bearings (§6.6), the
soundings table's leg column (§6.14), the footer imprint's
summary (§6.17) — is a printing of this object, and §10
recomputes it. A league that cannot be traced here is an
invented league, and invented leagues are this theme's
counter-from-nowhere (§9, failure 7).

**Grid and measure.** Content columns run 58–66ch on the fair
sheets. At ≥1200px a 240px **chart margin** stands on the
route's outer side, holding the compass (§6.6), the leagues
counter (§6.7) and the marginalia — the instruments live in
the margin the way they do on a real chart, never inside the
measure. Between 768–1199px the margin narrows to 120px and
holds the compass alone; below 768px the margin dissolves,
the compass moves to the cartouche (§6.11), and the chart
layer simplifies (§6 breakpoints). Vertical rhythm is
nautical, not typographic: landfalls are spaced by the route's
own legs, so section gaps vary with the geography (a long leg
is a long scroll — the page's pacing *is* the voyage's), with
a floor of 120px and a ceiling of 60vh between landfall heads.

**Grain and depth.** The vellum grain is one SVG turbulence
texture at 4% opacity over the whole sheet, plus a second,
identical grain layer masked to *surveyed* territory only, at
9% — the deepening of §6.8. Three parallax depths ride on the
chart layer (original entry, verbatim in structure): sea-wash
fields at 0.92× scroll speed, hatching and coastline at
0.97×, grain and fair sheets at 1.0× — the paper does not
move; the water on it lags; the ink lags least. Parallax
travel is capped at ±18px and clamped to authored overflow so
no layer's edge can open a gap at a section boundary.

**Density law.** Chart furniture is rationed by the fair-sheet
rule's complement: at any scroll position, worked chart
(hatching, soundings, roses, wash) may underlie at most 30%
of the viewport, and *zero* percent of any text column. Fog
(§6.5) may cover at most 25% of the viewport at any moment,
and never the reading line (§5). A page that needs more chart
than the ration has too many landfalls above the fold; the
cure is editorial — fewer, longer legs — not technical.

**The reading line.** The theme's master measurement: a
horizontal line at 55% of viewport height. Arrivals, fog
lifts, sounding pops, counter firings and needle swings are
all keyed to landfalls crossing it (§5). It is not drawn. A
build that draws it has confused the instrument with the
furniture; the route itself is the only progress the visitor
is shown.

## 5. Full motion system

Five named easings, defined once, used everywhere; an element
that invents a sixth fails the gate's grep.

| Easing token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-pen` | `cubic-bezier(.42,.04,.28,1)` | The engrossing hand — even pressure, slight build, no bounce | Coastline sketch (§6.1), engrossed names (§6.3), hatching sketch (§6.8), diagram strokes |
| `--ease-sail` | `cubic-bezier(.3,.55,.25,1)` | A ship under steady sail — smooth gather, gentle arrival | Fog lifts (§6.5), wash breathing (§6.1), cartouche index glide (§6.11) |
| `--ease-swell` | `cubic-bezier(.25,1.35,.35,1)` | A needle answering — one overshoot, damped to rest | Compass needle (§6.6), seal's legend settle (§6.9), accordion bearing (§6.16) |
| `--ease-thud` | `cubic-bezier(.6,.02,.9,.5)` | Weight arriving — reluctant, then all at once | Wax seal (§6.9), sounding pops (§6.7), logbook confirmation stamp (§6.13) |
| `--ease-glide` | `cubic-bezier(.35,.6,.3,1)` | The chart sliding under a lens — long, level travel | Pinned zoom (§6.4), unrolling transition (§6.18), footer sail-back (§6.17) |

**Durations ledger** (the theme's complete vocabulary; an
element may combine but not invent): coastline sketch 2400ms
(scrubbed by first scroll, §6.1); compass rose bloom 900ms;
hero headline settle 600ms; route draw — scrubbed, no fixed
duration (the scroll is the clock); place-name engrossing
110ms per letter, min 700ms, max 2200ms per name; hatching
sketch 1200ms per region; fog lift 1400ms sweep; needle swing
1100ms `--ease-swell`, tremble ±1.5° at 7s period; sounding
pop 260ms `--ease-thud`; leagues count 1200ms per leg, latched;
zoom pin 160vh of travel, scale 1→2.4; seal thud 380ms + 120ms
splat settle; ship-circle (§6.10) 24s per circuit; wash
breathing 10s cycle; unrolling 700ms; watchdogs 3000ms (hero
charting), 1500ms (route, names, hatching), 1200ms (fog
lifts), 4000ms (zoom pin), 2000ms (unrolling).

**Every motion term, translated or refused.**
- *Scroll-triggered reveals* — fog lifts (§6.5): regions
  reveal as the fog of the unvisited lifts off them. Nothing
  fades up from below; the weather leaves, the coast was
  always there.
- *Scroll-scrubbed animation* — the route draw (§6.2),
  hatching deepening (§6.8), grain deepening (§4), the zoom
  (§6.4): all scrubbed from the one shared loop (below).
- *Parallax* — three depths (§4): wash 0.92×, ink-work 0.97×,
  paper 1.0×. Capped ±18px; the route itself never parallaxes
  (a course line that drifts from its coast is a wreck).
- *Pinned sections* — exactly one: the map zoom (§6.4),
  160vh. A second pin is refused; a voyage gets one strait
  where the chart leans close.
- *Masked reveals* — the fog lift's parchment-gradient mask
  (§6.5) and the engrossing stroke mask (§6.3). Masks always
  sit over complete content (§1 clause 3 is the theme's
  constitution: the finished chart is beneath, whole).
- *Blur-to-sharp* — **refused** as a filter on content. The
  theme's softness is fog — a vellum-toned layer *above* the
  coast that lifts (§6.5) — never a blur applied to the coast
  itself. Blurred coastline is out-of-focus cartography, and
  the survey's whole claim is focus.
- *Kinetic typography* — the engrossed place-names (§6.3) and
  nothing else. Letters on a chart are written by a hand, at
  a hand's speed; they do not bounce, stagger-rise or split.
- *Marquee* — **refused.** A chart does not scroll sideways
  forever. The sea-wash breathing at the map's edges (§6.1)
  is the page's only ambient travel, and it breathes rather
  than loops a message.
- *Animated counters* — leagues and soundings (§6.7): counted
  once per leg, latched, in engraved numerals. A counter that
  re-runs on scroll-back is a log being rewritten (§1 clause
  2 forbids it).
- *Progress indicators* — the route itself (§6.2) and the
  needle (§6.6). Percentages are banned from progress
  contexts (§12): the drawn fraction of the route *is* the
  fraction, in ink.
- *Micro-interactions* — hover hatching shade (§6.12), the
  seal thud (§6.9), the needle's tremble (§6.6), the logbook's
  ruling ink (§6.13).
- *Ambient loops* — three licensed, no more: wash breathing
  (10s), needle tremble (7s), the delays ship's circle (24s,
  §6.10). All pause off-screen and on hidden tabs. A fourth
  loop is a menagerie, not a chart (§9, failure 9).
- *Page transitions* — the unrolling (§6.18): the chart rolls
  away and the next sheet unrolls, route first.
- *Reduced motion* — every element's variant, stated per
  element in §6; the global rule is the original entry's,
  verbatim: **the complete map shown fully drawn, needle
  still.**

**The shared loop.** One `requestAnimationFrame` loop drives
every scrubbed value — route fraction, hatching depth, grain
mask, zoom scale, wash phase, needle angle — with a lerp
factor of **0.09** for scroll-scrubbed values: the original
entry's "scroll glides like a ship under steady sail"
implemented as physics. A ship answers its helm a beat late
and never jerks; the chart answers scroll the same way, so
the ink lags the reader's hand by at most a breath while the
*content* — fair sheets, text, controls — is always exactly
where the reader put it. Native scroll is never intercepted.
The loop sleeps when every scrubbed value is within 0.1% of
target and when the tab is hidden. Time-based acts (blooms,
engrossing, seals, counts) run on CSS transitions/animations
or one-shot rAF timers, never on the shared loop.

**The route function.** One function serves every
route-reading element, so two builders — or two elements —
can never disagree about where the voyage has got to. Page
progress `p` (scroll fraction of the document, 0–1) maps to
drawn route fraction `r = p` exactly — the route is the
page's own length, surveyed: a builder who eases, offsets or
"improves" this mapping has falsified the survey. Landfall
`i` is *arrived* when the lerped `r` crosses its declared
fraction (§4); arrival is latched (clause 2), and the latch —
not the live value — is what names, counters, hatching and
the index read. The function and the fractions are printed
here because the gate tests them (§10): sample three
landfalls and the rendered drawn length must match `r × L`
to the pixel.

**Madder ration.** The route is spent like a surveyor's one
red pencil: per page, at most the route line (§6.2), the
seals (§6.9, §6.13), the delays line (§6.10), and error text
in `--madder-deep`. A page rendering more madder than that
has made a livery out of a course line and fails §10's pixel
audit.


## 6. Signature elements

### 6.1 Blank vellum that charts itself

- **What & why.** The hero opens as a sheet of blank vellum
  carrying only a compass rose and the departure headline.
  On load the rose blooms; as the first scroll begins, the
  coastline of the site's territory sketches in stroke by
  stroke around the hero's field, and the first leg of the
  route draws out of the departure point. It belongs because
  it is the theme's thesis performed before a word of body
  copy is read: this territory does not exist until it is
  travelled, and the visitor's own hand on the scroll is the
  surveyor's hand on the pen.
- **Structure.** A real `<h1>` on a fair sheet (§4), complete
  in the DOM at full contrast from first paint. The hero's
  chart field is one inline SVG (coastline paths, the rose,
  the first route leg), every path finished and wearing a
  `stroke-dasharray` mask whose offset is the only animated
  property. The rose is a separate SVG group (two 8-point
  stars, a brass ring, cardinal letters in IM Fell English SC)
  so it can bloom independently. The wash field beneath is a
  teal gradient div at 0.92× parallax (§4). No canvas: the
  chart must remain inspectable, printable SVG (§1 clause 3).
- **Motion spec.** Trigger: load, once per session
  (`sessionStorage`; a returning visitor finds the hero
  already charted to their furthest point, §6.2's memory).
  Gated on `document.fonts.ready` raced against 900ms —
  sketching in a fallback face would misalign the rose's
  letters, so if fonts lose the race the hero ships drawn.
  t=0: rose blooms — ring draws 500ms `--ease-pen`, star
  points scale from centre 900ms `--ease-swell`, cardinal
  letters fade-print in the last 200ms. Headline settles
  (opacity/translate, 600ms `--ease-sail`) at t=300. Coastline
  sketch arms at first scroll: scrubbed by the shared loop
  across the hero's first 60vh of travel, total stroke time
  ≈2400ms at reading pace, `--ease-pen` character. The first
  route leg (§6.2) begins drawing from the departure point as
  the coastline completes.
- **States.** Uncharted (JS-armed only) → charting → charted
  (rest). Hover/focus: none — the hero chart is not a control.
  Scrolled away mid-sketch: the sketch is scrubbed, so it
  simply waits; returning resumes it. Focus entering the hero
  completes the sketch instantly — a keyboard visitor is
  never asked to wait for cartography.
- **Content merge.** The sketch draws the *site's actual
  territory* — the coastline the route (§6.2) will sail, the
  landfalls the page will visit — not a decorative squiggle.
  The headline it frames is the voyage's name and the page's
  subject; the hero is the chart's title block, not an intro
  screen in front of one.
- **Failure fallback.** Watchdog at 3000ms: if the sketch has
  not completed, all dash offsets snap to drawn and the hero
  stands charted. No JS: masks are never applied; the chart
  ships finished (§1 clause 3). Slow network: the hero is
  HTML-first; the charting script is deferred and the
  watchdog runs from DOMContentLoaded.
- **Reduced-motion variant.** The complete hero chart, fully
  drawn, rose bloomed, needle still (§6.6) — the original
  entry's global rule applied at the first screen.
- **Performance budget & mobile variant.** Hero SVG ≤14KB;
  one turbulence texture shared with §4. Mobile (<768px):
  coastline path simplified at build (a second, coarser path
  set — surveyors drew small charts coarser too), sketch
  ≈1800ms, rose at 96px, wash parallax off (the sheet is
  small; depth is spent on the draw instead).
- **Choreography timeline (v2).** t=0 fonts ready (or 900ms
  race lost → drawn state, ceremony skipped) → t=0–500 rose
  ring draws → t=200–1100 star points bloom → t=300 headline
  settles → t=900–1100 cardinal letters print → first scroll:
  coastline strokes scrub 0→100% across 60vh → coastline
  complete → first route leg arms (§6.2). Watchdog ceiling
  3000ms cancels everything past the rose if the sketch
  stalls.
- **State matrix (v2).** *Rest (first visit, pre-scroll):*
  rose bloomed, coast unsketched, headline printed. *Hover:*
  none. *Focus:* focus within hero completes a running
  sketch. *Active:* n/a. *Scrolled-past:* charted, latched;
  returning shows the drawn coast. *Disabled / no-JS:*
  printed drawn at first paint. *Touch:* identical; the
  first touch-drag is the first scroll and arms the sketch.
- **Breakpoints (v2).** ≥1200px: full coastline set, rose
  144px, sketch across 60vh. 768–1199px: rose 120px, sketch
  across 50vh, wash parallax 0.94×. <768px: coarse path set,
  rose 96px, sketch across 40vh, parallax off.
- **Edge cases & failure modes (v2).** *Territory edited in
  a CMS:* the coastline is one authored path set per site,
  versioned with the route object (§4); an edit that changes
  landfalls without re-surveying the paths fails §10's
  arrival audit — by design. *Tab hidden mid-sketch:* rAF
  pauses; on return, wall-clock past 3000ms fires the
  watchdog. *Very tall hero content:* the sketch is keyed to
  scroll travel, not hero height, so a long standfirst cannot
  strand the coast half-drawn above the fold.
- **Accessibility spec (v2).** The `<h1>` is complete in the
  accessibility tree from first paint; the chart SVG is
  `aria-hidden` (its information — the landfall names and
  order — is carried accessibly by the cartouche index,
  §6.11). The sketch is never announced. Contrast is the
  printed layer's at all times: ink on vellum 9.20:1.
- **Tokens consumed (v2).** `--vellum`, `--parchment`,
  `--ink`, `--ink-deep`, `--teal`, `--brass`, `--madder`,
  `--ease-pen`, `--ease-sail`, `--ease-swell`, `--dur-sketch`
  (2400ms), `--dur-rose` (900ms), `--dur-watchdog-hero`
  (3000ms).

### 6.2 The master route line

- **What & why.** A madder-red SVG path winds through the
  whole page's geography, from the departure landfall at the
  head to the final landfall at the foot, and draws itself in
  exact sync with scroll: the drawn fraction of the route is
  the read fraction of the page (§5's route function). It
  belongs because it makes progress *geographical* — the
  reader does not consume the page, they sail it, and the red
  line behind them is the proof of passage. It is the theme's
  spine: arrivals (§6.3), soundings (§6.7), hatching (§6.8)
  and the index (§6.11) all read their state from it.
- **Structure.** One SVG `<path>` in the page chart layer
  (§4), authored to pass beside every landfall's fair sheet
  with 24px clearance, wearing a dash mask driven by the
  shared loop. Waypoint dots (4px, `--madder-deep`) are
  printed at each landfall fraction from the start — the
  *destinations* are charted; it is the *sailing* that is
  earned. A 6px vellum halo underlay (a slightly wider
  `--vellum` stroke beneath the madder) keeps the line legible
  where it crosses hatching or wash.
- **Motion spec.** Trigger: scroll, scrubbed — drawn length
  = lerped `r × L` (§5), lerp 0.09, so the line's head trails
  the reader's true position by at most a breath and settles
  onto it when scrolling stops. No fixed duration: the scroll
  is the clock. When the drawn head crosses a landfall
  fraction, the arrival latch fires (§6.3, §6.6, §6.7) —
  arrivals are events on this line, not intersection
  observations, so they cannot be skipped by a fast scroll:
  a fling fires every latch it passes, in order, compressed.
- **States.** Drawing (underway) → arrived segments latched
  permanently (clause 2: the line never un-draws). Hover:
  none on the line itself. Scrolled-past: fully drawn to the
  furthest point ever reached — the loop's target is the
  *maximum* progress, not the current one, so scrolling up
  leaves the wake intact. Session memory: the maximum is
  stored; a returning visitor's route starts drawn to their
  furthest landfall (§6.1).
- **Content merge.** The route is not a progress bar wearing
  a costume: its geography is the page's structure. It passes
  each landfall because the landfall is *there*; sections
  exist where the route goes. A builder who draws the route
  down the page's centre margin regardless of content has
  drawn a progress bar (§9, failure 3).
- **Failure fallback.** No JS: the path ships undashed —
  fully drawn. Loop stalled: watchdog at 1500ms snaps the
  drawn length to the true scroll fraction. Print: the route
  prints fully drawn (print stylesheet removes all masks —
  a printed chart is a finished chart).
- **Reduced-motion variant.** The route fully drawn from
  first paint; the lerp is bypassed; arrivals fire as state,
  not ceremony (names print complete, §6.3).
- **Performance budget & mobile variant.** One path, one
  dash-offset write per frame from the shared loop — the
  cheapest element on the page and the one everything else
  hangs from. Mobile: the path is re-authored at build for
  the narrow sheet (fewer meanders, same fractions — the
  fractions are the survey; the meanders are the drawing).
- **Choreography timeline (v2).** Continuous: scroll input →
  loop lerps drawn fraction at 0.09 → head settles within
  ~300ms of scroll stop → crossing a fraction fires, in
  order: waypoint dot fills (120ms), name engrossing arms
  (§6.3), needle swings (§6.6), leg counter arms (§6.7),
  index marker advances (§6.11). Reverse scroll: no beats —
  the wake holds.
- **State matrix (v2).** *Rest:* drawn to furthest point.
  *Hover:* none. *Focus:* keyboard traversal fires arrivals
  as landfalls are reached by focus-scroll, identically.
  *Active:* n/a. *Scrolled-past:* latched drawn. *Disabled /
  no-JS:* fully drawn. *Touch:* identical; flings fire
  compressed arrival sequences (each latch still fires; the
  ceremonies queue at max 2 concurrent, §6.3).
- **Breakpoints (v2).** ≥1200px: full meander set, line
  2.5px, halo 6px. 768–1199px: line 2.5px, meanders reduced
  ~30%. <768px: re-authored path, line 2px, halo 5px,
  fractions unchanged.
- **Edge cases & failure modes (v2).** *Content grows (CMS
  adds a section):* the route object (§4) is the contract —
  a new landfall must be surveyed into it (fraction, leg,
  bearing) or §10 fails the build; the path is re-authored,
  never auto-routed. *Reader jumps to foot (anchor):*
  jump-scroll rule (§13) — all latches fire in order, route
  snaps drawn to target, ceremonies are skipped, not queued.
  *Reader never scrolls:* the route waits at the departure
  dot; nothing downstream pretends to have happened.
- **Accessibility spec (v2).** The route is decorative record
  (`aria-hidden`); progress is conveyed accessibly by the
  cartouche index's `aria-current` (§6.11), not by the line.
  The line's contrast is audited as a graphic: madder on
  vellum 5.39:1, halo guaranteeing separation from hatching
  at all crossings.
- **Tokens consumed (v2).** `--madder`, `--madder-deep`,
  `--vellum`, `--route-w` (2.5px), `--route-halo` (6px),
  `--lerp-route` (0.09), `--dur-watchdog-route` (1500ms).

### 6.3 Engrossed place-names

- **What & why.** At each landfall, as the route arrives, the
  place-name letters itself in at pen speed — each letter's
  stroke swelling thick-thin as a broad nib would lay it —
  until the name stands complete in fresh ink. It belongs
  because on a real chart a name is not metadata; it is an
  act of possession performed by arrival. Geography is named
  by being reached, so the naming is the reward the route
  pays at every stop.
- **Structure.** The name is real text in IM Fell English,
  complete in the DOM, each letter wrapped (build-time, not
  JS-split at runtime — the DOM ships lettered) in a span
  carrying an SVG-free stroke illusion: a per-letter clip
  mask that wipes left-to-right while the letter's
  `font-variation` weight — Fell is not variable, so the
  swell is faked honestly: a duplicate letter in `--ink-deep`
  clips in over the `--ink` base, its clip edge soft, giving
  the thick-thin swell as the nib's pressure. The base layer
  is the finished name (§1 clause 3); the performance is the
  top layer's mask.
- **Motion spec.** Trigger: the landfall's arrival latch
  (§6.2). Letters letter at 110ms per letter, `--ease-pen`,
  staggered left to right, min total 700ms, max 2200ms (a
  20+ letter name compresses to 90ms/letter rather than
  outstaying its welcome). The swell peaks at each letter's
  60% point. On completion the name's colour settles from
  `--ink` to `--ink-deep` over 300ms — fresh ink drying
  darker. Once per landfall, ever: the latch is permanent.
- **States.** Unwritten (masked, JS-armed only) → lettering →
  engrossed (rest, `--ink-deep`). Hover on an engrossed name:
  its hatching shades (§6.12's rule when the name is a link).
  Focus: a name that is a link shows the §11 focus ring; if
  focused before arrival (keyboard racing the route), the
  name completes instantly — focus never waits for penmanship.
  Scrolled-past: engrossed, latched.
- **Content merge.** The name being lettered is the section's
  actual heading — the landfall's `<h2>` — not a caption
  beside it. The section's content is the place; its heading
  is the place's name; the chart and the document are the
  same object at this point, which is the theme in miniature.
- **Failure fallback.** Watchdog at 1500ms from arming: masks
  removed, name stands printed in `--ink-deep`. No JS: names
  ship complete — the unwritten state is JS-armed only.
  Fonts race lost (§6.1): names print statically; lettering
  in a fallback face would swell the wrong letterforms.
- **Reduced-motion variant.** Names print complete in
  `--ink-deep` at arrival (or from load, per §5's global
  rule); no lettering, no swell.
- **Performance budget & mobile variant.** Per name: two text
  layers, masks on spans — no canvas, no per-letter layout
  (law 3: the lettered and unlettered layouts are identical).
  Mobile: letter rate 90ms, swell amplitude reduced (the
  duplicate layer clips at 70% strength) — the gesture reads
  at arm's length or it is cut, and at 90ms it reads.
- **Choreography timeline (v2).** Arrival latch fires →
  t=0 first letter's mask opens → letters at 110ms intervals,
  swell peaking at each letter's 60% → final letter +0ms:
  drying settle begins (300ms) → name at rest in `--ink-deep`
  → landfall label (SC) prints beneath at +150ms. Total for
  a 10-letter name: ≈1400ms + settle.
- **State matrix (v2).** *Rest:* engrossed, `--ink-deep`.
  *Hover:* hatching shade if linked; the name itself does
  not move. *Focus:* instant completion if mid-lettering;
  ring per §11. *Active (link):* §6.9's seal is the active
  ceremony, not the name. *Scrolled-past:* engrossed.
  *Disabled / no-JS:* printed complete. *Touch:* identical;
  no hover swell is faked on tap.
- **Breakpoints (v2).** ≥1200px: 30px names, 110ms/letter.
  768–1199px: 27px, 100ms/letter. <768px: 24px (law 1's
  floor), 90ms/letter, swell at 70%.
- **Edge cases & failure modes (v2).** *Very long names
  (20+ letters):* rate compresses to 90ms, total capped
  2200ms; a name over 34 characters is refused at build
  (§12) — a chart name is a name, not a sentence. *Two
  arrivals in one fling:* ceremonies queue, max 2 concurrent,
  later names print complete if the queue would exceed
  3000ms (§13's jump rule). *Name edited in CMS:* lettering
  is per-letter spans generated at build from the heading
  text — an edit regenerates; runtime JS never splits text.
- **Accessibility spec (v2).** The heading is one text node
  to assistive technology (spans are presentational,
  `aria-hidden` duplicates; the accessible name is the full
  string from first paint). Lettering is never announced.
  Contrast: `--ink-deep` on vellum 12.12:1 at completion;
  during lettering the base layer is `--ink` at 9.20:1 —
  the name is legible at every frame, only its *finish*
  animates.
- **Tokens consumed (v2).** `--ink`, `--ink-deep`, `--vellum`,
  `--ease-pen`, `--dur-letter` (110ms), `--dur-dry` (300ms),
  `--dur-watchdog-name` (1500ms).

### 6.4 Pinned map zoom

- **What & why.** Mid-page, at the voyage's most intricate
  coast (the worked site puts it at The Long Reach, §8.2),
  the chart panel pins and the chart glides closer — scale
  1→2.4 centred on the current region — while the region's
  place-names letter in around the reader at their enlarged
  size. It belongs because every survey has one stretch where
  the small chart is not enough: the chart leans closer at
  the interesting coast, and attention becomes magnification.
  It is the page's single pin (§5) and its centre of gravity.
- **Structure.** A sticky stage (200vh of travel, 160vh of
  it the zoom) containing a clipped viewport onto the page
  chart's regional inset — a dedicated, more detailed SVG of
  the one region (finer coastline, its own soundings, two
  inset roses), authored at zoom resolution so the scale
  transform reveals *drawn detail*, not enlarged pixels:
  stroke widths are counter-scaled (vector-effect) so lines
  stay survey-weight at 2.4×. The region's names are HTML
  text (§6.3's structure) positioned over the inset, so they
  letter in as text, not as scaled graphics.
- **Motion spec.** Trigger: scroll through the pinned range,
  scrubbed by the shared loop (`--ease-glide` character via
  lerp 0.09). Scale 1→2.4 across the first 70% of the range,
  centred on the region's principal landfall; pan follows a
  declared two-point path (enter wide on the region's west
  cape, settle on its harbour). At scale ≥1.8 the region's
  names arm their engrossing (§6.3 rates). Final 30%: hold —
  the chart rests close while the section's copy is read —
  then the pin releases and the page sails on at full-chart
  scale. Watchdog 4000ms: a stalled loop releases the pin
  with the inset at rest scale.
- **States.** Unpinned (approach) → zooming (scrubbed) →
  held close → released (the inset remains, at rest, as a
  detail chart in the flow). Scrolled back up: the zoom
  reverses scrubbed (the one licensed un-performance — it is
  a lens, not a record; §1 clause 2 protects *ink*, and the
  zoom lays no ink). Names lettered during the zoom stay
  lettered (they are ink).
- **Content merge.** The zoom's subject is the section's
  subject: the copy beside the stage is *about* this coast —
  its shoals are the soundings visible at 2.4×, its harbour
  is the name that letters in largest. A zoom into a region
  the text never mentions is a magnifying glass over someone
  else's chart (§9, failure 4).
- **Failure fallback.** No JS / loop dead: the inset renders
  at rest scale in flow, names printed, copy complete — the
  section loses a lens, not its content. Pin unsupported
  (old browser): the stage degrades to the same in-flow
  inset. The watchdog guarantees the reader can never be
  trapped in a held pin.
- **Reduced-motion variant.** No pin, no zoom: the detailed
  inset stands in flow at 1.4× rest scale (large enough to
  read its soundings), names printed complete.
- **Performance budget & mobile variant.** Inset SVG ≤18KB;
  transform-only animation (scale/translate on one layer);
  the stage is the page's only `will-change` citizen.
  Mobile (<768px): **pin abolished** — the inset stands in
  flow at full width with a horizontal glide (translateX
  scrubbed ≤120px) as the reader passes; a pinned zoom on a
  phone is a trap with a view.
- **Choreography timeline (v2).** Stage top reaches reading
  line → pin engages → travel 0–70%: scale 1→2.4, pan west
  cape → harbour → scale crosses 1.8: names arm, letter at
  §6.3 rates → travel 70–100%: hold, copy read → pin
  releases → inset rests in flow, its soundings now legible
  at rest scale. Watchdog 4000ms oversees the whole range.
- **State matrix (v2).** *Rest (before):* inset at 1× in
  flow position. *Hover:* none (the stage is not a control).
  *Focus:* focus entering the stage's copy releases any
  mid-zoom to the held state instantly — reading outranks
  lens-work. *Active:* n/a. *Scrolled-past:* inset rests in
  flow, names lettered. *Disabled / no-JS:* in-flow inset.
  *Touch:* scrubbed identically; no pinch handling is
  intercepted — the browser's own zoom is never fought.
- **Breakpoints (v2).** ≥1200px: pin 200vh stage, scale to
  2.4, inset 720px wide. 768–1199px: pin 170vh, scale to
  2.0, inset full column. <768px: no pin; in-flow inset +
  ≤120px glide.
- **Edge cases & failure modes (v2).** *Short viewport
  (<400px tall):* pin drops (stage becomes in-flow) — a
  strait needs headroom. *Reader flings through:* scale
  snaps to the held state, names print, pin releases —
  the jump rule (§13). *Inset detail insufficient:* the
  inset is authored at zoom resolution by §15's checklist;
  a build that scales the small chart instead fails §10's
  zoom audit (stroke weights must stay survey-weight).
- **Accessibility spec (v2).** The stage's copy is in normal
  document flow (never inside the transformed layer), so
  reading order and focus order are the document's own. The
  inset SVG is `aria-hidden` with its data repeated in the
  soundings table (§6.14). Focus is never moved by the pin.
- **Tokens consumed (v2).** `--vellum-deep`, `--ink`,
  `--teal`, `--brass`, `--ease-glide`, `--zoom-max` (2.4),
  `--dur-watchdog-pin` (4000ms), `--lerp-route` (0.09).

### 6.5 Fog-lifting reveals

- **What & why.** Regions the route has not yet reached are
  not hidden — they are *fogged*: a vellum-toned fog layer
  lies over the unvisited coast, and as a landfall approaches
  the reading line the fog lifts off it in a soft parchment
  gradient sweep, leaving the coast charted and clear. It
  belongs because it is the emotional complement of §1
  clause 1: unknown places are not absent, they are
  weathered-in, and the reveal is the survey arriving. A fade
  says "content loading"; a fog lift says "landfall ahead."
- **Structure.** Each landfall section carries a fog layer
  (a div, `aria-hidden`, `pointer-events: none`) filled with
  `--fog` and a linear-gradient mask whose clear edge is a
  CSS custom property (`--lift`, 0→100%) driven by the
  shared loop. Beneath it, the section complete: fair sheet,
  text, chart work — printed and legible to any technology
  that ignores the layer (§1 clause 3). Fog never covers the
  section's heading zone at rest in the DOM order — the
  layer is inserted by JS only.
- **Motion spec.** Trigger: the landfall's approach — when
  its head crosses 85% viewport height, `--lift` scrubs
  0→100% as the head travels to the reading line (55%), a
  1400ms-equivalent sweep at reading pace, `--ease-sail`.
  The gradient's soft edge is 18vh tall: fog thins before it
  clears, coast ghosting through at 60% lift. At 100% the
  layer is removed from the DOM (a lingering fog layer is a
  compositing cost and a lie). One direction only: lifted
  fog never returns (clause 2).
- **States.** Fogged (JS-armed only) → lifting → clear
  (rest; layer absent). Hover/focus: focus entering a fogged
  section lifts its fog instantly — the keyboard visitor
  surveys by arriving, same as anyone. Scrolled-past:
  clear, latched. The fog state is presentational only; the
  section is in the accessibility tree, complete, throughout.
- **Content merge.** The fog covers the *chart work and the
  section's opening view* — the territory — while the
  section's text sits on its fair sheet, which the fog layer
  also covers visually but never structurally: the merge is
  that fog is weather *over the place the copy describes*,
  lifting as the copy arrives to be read. Fog over unrelated
  decoration is weather in the wrong county (§9, failure 8).
- **Failure fallback.** Watchdog at 1200ms per section: fog
  not lifted on schedule is removed. No JS: fog is never
  inserted; sections stand clear. Scroll-end snap: when
  scrolling stops with a section mid-lift, the lift completes
  in 400ms `--ease-sail` — no section is ever left half-weathered
  at rest.
- **Reduced-motion variant.** No fog layers at all. Sections
  stand charted and clear; the unvisited are distinguished
  only by their un-drawn route (§6.2's variant) — the
  original entry's rule: unknown is shown by absence of ink,
  not by weather.
- **Performance budget & mobile variant.** One layer per
  section, removed on completion; at most 2 fog layers live
  at once (the lifting one and the next section's). Mask
  animates a registered custom property (compositor-driven).
  Mobile: gradient edge 12vh, sweep 1100ms-equivalent, fog
  strength .92 (night ruling, §2 — small sheets weather
  heavier).
- **Choreography timeline (v2).** Section head crosses 85%
  line → lift arms → head travels 85%→55%: `--lift` 0→100%,
  coast ghosts at ~60% → head at reading line: layer removed
  → arrival latch (§6.2) fires its ceremonies on clear
  ground. Scroll stop mid-lift → 400ms completion glide.
  Watchdog ceiling 1200ms from arming.
- **State matrix (v2).** *Rest (unvisited):* fogged
  (visual only). *Hover:* none. *Focus:* instant lift.
  *Active:* n/a. *Scrolled-past:* clear, layer absent.
  *Disabled / no-JS:* never fogged. *Touch:* identical;
  flings lift in passing order, compressed (§13).
- **Breakpoints (v2).** ≥1200px: edge 18vh, strength .88.
  768–1199px: edge 15vh. <768px: edge 12vh, strength .92,
  sweep shortened (1100ms-equivalent).
- **Edge cases & failure modes (v2).** *Two sections in one
  viewport (short sections):* lifts sequence by head
  position; the density law (§4) caps live fog at 25% of
  viewport — if both would exceed it, the lower section's
  fog waits at 40% lift (ghosting) until the upper clears.
  *Back-scroll into a lifted section:* stays clear (clause
  2). *Fog over interactive content:* controls in a fogged
  section are focusable and lift on focus (above) — a
  control is never left usable-but-invisible.
- **Accessibility spec (v2).** Fog is `aria-hidden` and never
  the only carrier of state: unvisited sections are
  announced by the index (§6.11) as not-yet-reached, not by
  their weather. Text contrast is the printed layer's
  (9.20:1) — fog is a visual layer over a complete page,
  and screen readers read the page, not the weather.
- **Tokens consumed (v2).** `--fog`, `--vellum`, `--ease-sail`,
  `--lift` (custom property), `--dur-watchdog-fog` (1200ms),
  `--dur-lift-snap` (400ms).

### 6.6 Swinging compass needle

- **What & why.** In the chart margin stands the compass: a
  brass rose, and on it a needle that swings — with one
  damped overshoot — to point along the bearing of the leg
  currently being sailed, trembling faintly as instruments
  do, and re-swinging at every arrival to the next leg's
  bearing. It belongs because it is the page's orientation
  made instrumental: the reader always knows the way onward,
  not from a progress percentage but from a needle that
  knows the coast. The bearings it points along are the
  route object's own (§4) — the needle never invents a
  direction.
- **Structure.** An inline SVG rose (shared drawing with
  §6.1's, at margin size: 120px) — ring, 8-point star,
  cardinal letters — with the needle as a separate two-tone
  group (madder north half, ink south half, brass pivot)
  rotating about the centre via a CSS custom property
  (`--needle`, degrees) written by the shared loop. A small
  SC label beneath prints the current leg: *"LEG III —
  BEARING 031°"* — the needle's claim, in text, from the
  same object.
- **Motion spec.** Trigger: arrival latches (§6.2). On a new
  leg, the needle swings to the leg's bearing over 1100ms
  `--ease-swell` — one overshoot of ≤6°, damped to rest.
  Tremble: a continuous ±1.5° sway, 7s period, `--ease-sail`
  character, amplitude scaled by scroll velocity (a ship
  under way trembles more than a ship at anchor; at rest the
  tremble settles to ±0.4°). The label crossfades at the
  swing's midpoint. The needle points *along the page's
  geography*: bearing 031° means the next landfall lies
  up-page-right as charted — the rose is oriented to the
  chart, not to true north, and says so in its apparatus
  ("bearings are chart bearings").
- **States.** At rest: pointing along the current leg,
  trembling. Between landfalls: unchanged (the leg is the
  leg until the next arrival). At the final landfall: the
  needle settles to the rose's north and the label prints
  *"VOYAGE COMPLETE — 214 LEAGUES"* (the object's total,
  §4). Hover: the rose warms (brass ring brightens 150ms) —
  an instrument acknowledging a hand nearby, nothing more.
  Focus: the compass is not a control; it takes no focus.
- **Content merge.** The needle's bearings are the route's
  bearings; its label names the actual next landfall. It is
  the route (§6.2) read as an instrument. A needle pointing
  at decorative angles — or worse, following the pointer —
  is a toy compass in a gift shop (§9, failure 5).
- **Failure fallback.** No JS: needle printed pointing along
  leg I, label printed for leg I, and the full leg table
  (§6.14) carries the bearings accessibly. Loop stalled:
  watchdog 1500ms sets the needle to the current leg's
  bearing without ceremony.
- **Reduced-motion variant.** Needle still (the original
  entry's words), set to the current leg's bearing, updated
  by instant jumps at arrivals; no tremble, no overshoot.
- **Performance budget & mobile variant.** One SVG ≤4KB, one
  transform write per frame from the shared loop. Mobile:
  the compass leaves the margin and docks in the cartouche
  (§6.11) at 56px, label abbreviated to the bearing only —
  the instrument survives the small sheet, miniaturised,
  not deleted.
- **Choreography timeline (v2).** Arrival latch → t=0 needle
  releases → t=0–1100 swing `--ease-swell`, overshoot ≤6° at
  ~700ms → t=550 label crossfades to the new leg → t=1100
  needle at bearing, tremble resumes at anchor amplitude →
  under way: tremble scales with scroll velocity. Final
  arrival: swing to north, label prints the completion line.
- **State matrix (v2).** *Rest:* on bearing, trembling ±0.4°.
  *Hover:* ring warms 150ms. *Focus:* none (not a control).
  *Active:* n/a. *Scrolled-past:* on the current leg's
  bearing — scrolling back does not swing it back (the leg
  is read from the latch, §5). *Disabled / no-JS:* leg I
  static. *Touch:* identical; no pointer-following, ever.
- **Breakpoints (v2).** ≥1200px: 120px rose in the chart
  margin, full label. 768–1199px: 96px, full label. <768px:
  56px in the cartouche, bearing-only label.
- **Edge cases & failure modes (v2).** *Adjacent legs with
  near bearings (031° after 078°):* the swing takes the
  short way round, always — a needle that spins 340° to
  move 20° is showing off. *Velocity spikes (fling):*
  tremble amplitude caps at ±1.5°; swings queue behind the
  latch order, max one swing in flight, later bearings
  supersede (the needle serves the current leg, not the
  history). *Bearing edited in the route object:* needle,
  label and table read the same object — §10 recomputes all
  three from it.
- **Accessibility spec (v2).** The compass is `aria-hidden`
  as a graphic; its information is the label text, which is
  real text in the margin (and duplicated in the index,
  §6.11). The completion state is announced by the label's
  text change, not by the needle. Brass on vellum is
  graphical-only here (1.98:1) — lawful because the needle
  is an instrument, and its reading is always also printed
  in ink (§3 law 5 is not breached: the *text* is ink).
- **Tokens consumed (v2).** `--brass`, `--madder`, `--ink`,
  `--sepia-soft`, `--needle` (custom property),
  `--ease-swell`, `--ease-sail`, `--dur-swing` (1100ms),
  `--dur-watchdog-route` (1500ms).


### 6.7 Soundings and leagues counters

- **What & why.** Two instruments of accumulation. *Soundings:*
  small depth numerals in fathoms, pricked along the coast in
  the chart layer, which pop in as the route passes their
  position — the survey's measurements, taken where the ship
  actually went. *Leagues:* a counter in the chart margin, in
  engraved Fell numerals, that counts up the current leg's
  leagues as the route draws them and latches at each
  landfall's cumulative total (§4). They belong together
  because they are how a real chart accumulates knowledge:
  depths where you sounded, distance where you sailed — data
  as marginalia, earned by passage, never as decoration.
- **Structure.** Soundings are SVG `<text>` elements in the
  chart layer, positioned from a declared sounding set in the
  route object (each: route fraction, fathoms, side of coast),
  printed in the DOM at full opacity — their pop is a scale
  settle on a duplicate highlight ring, not the numeral's
  existence. The leagues counter is HTML in the margin: label
  in SC ("LEAGUES SAILED"), numeral in IM Fell English 40px,
  and beneath it the leg's source line ("Leg III — 41 leagues
  of 214", §12's provenance rule).
- **Motion spec.** Sounding pop: when the drawn route head
  passes a sounding's fraction, its ring settles 260ms
  `--ease-thud` (a lead line hitting bottom) and the numeral
  deepens `--ink` → `--ink-deep` 200ms. Leagues: scrubbed,
  not timed — the numeral is `round(r × 214)` read from the
  route function (§5), so the count *is* the drawing; at each
  arrival it ticks the final league with a 120ms settle.
  Both latch permanently (clause 2): scrolling back leaves
  every sounding sounded and every league counted.
- **States.** Unsounded (numeral printed, ring unsettled,
  tone `--ink`) → sounded (ring settled, tone `--ink-deep`).
  Counter: underway (live value) → at landfall (latched
  cumulative, settle tick) → complete (214, with the
  completion line, §6.6). Hover on a sounding: its ring warms
  — a measurement acknowledging inspection. Neither is a
  control; no focus state.
- **Content merge.** The soundings are the coast's real
  declared depths — the same set the soundings table (§6.14)
  prints in full, the same depths the zoom inset (§6.4)
  shows enlarged. The leagues are the route object's legs.
  A sounding placed for visual rhythm, at a depth nobody
  declared, is a forged measurement (§9, failure 7) and
  §10's audit recomputes the set.
- **Failure fallback.** No JS: all soundings printed sounded
  (rings settled in the static render), counter printed at
  the voyage total with its source line — a finished chart
  shows its full survey. Loop stalled: watchdog 1500ms
  settles every sounding the true progress has passed and
  sets the counter to the true figure.
- **Reduced-motion variant.** Soundings appear sounded as
  their fractions are passed (state change, no pop); the
  counter updates in whole leagues at arrivals only — the
  record without the ceremony.
- **Performance budget & mobile variant.** Soundings are
  text in an existing SVG — near-zero cost; cap 24 soundings
  per page (a coast more densely sounded than that is a
  harbour plan, not a chart). Mobile: sounding numerals
  13px, the counter leaves the margin and rides in the
  cartouche (§6.11) at 24px beside the needle.
- **Choreography timeline (v2).** Route head crosses a
  sounding's fraction → t=0 ring settle begins (260ms) →
  t=100 numeral deepens → sounded, latched. Leg in progress:
  counter tracks `round(r × 214)` per frame → arrival: final
  league ticks (120ms), source line updates to the next leg,
  needle swings (§6.6) concurrently — instruments agreeing.
- **State matrix (v2).** *Rest:* sounded set = all fractions
  behind the latch; counter at latched cumulative when at a
  landfall, live value under way. *Hover:* sounding ring
  warms 150ms. *Focus:* none (not controls). *Active:* n/a.
  *Scrolled-past:* all latched; nothing un-sounds.
  *Disabled / no-JS:* full set printed, counter at total.
  *Touch:* identical; no tap targets (44px rule does not
  apply — they are not controls, and making them buttons
  would be a lie about what a sounding is).
- **Breakpoints (v2).** ≥1200px: soundings 15px, counter
  40px in margin. 768–1199px: soundings 14px, counter 32px
  in the narrowed margin. <768px: soundings 13px, counter
  24px in the cartouche; sounding set thins to every second
  sounding (the survey object is unchanged — the small chart
  prints a selection, labelled as such in §6.14).
- **Edge cases & failure modes (v2).** *Two soundings at
  near fractions:* pops sequence 80ms apart in route order,
  never simultaneously — measurements are taken one at a
  time. *Counter during a fling:* the numeral tracks the
  lerped value, so it sweeps honestly rather than teleporting;
  latches still fire in order. *Depths in the copy vs the
  chart:* any depth quoted in prose must exist in the
  sounding set — §10 greps prose figures against the object.
- **Accessibility spec (v2).** Soundings in the SVG are
  `aria-hidden`; the full set is available as data in §6.14's
  table (the accessible form of the survey). The counter is
  real text, updated without announcement (`aria-live` off —
  a number changing per frame must never be narrated); its
  latched landfall values are what the index (§6.11) states.
- **Tokens consumed (v2).** `--ink`, `--ink-deep`,
  `--sepia-soft`, `--madder-deep`, `--ease-thud`,
  `--dur-pop` (260ms), `--dur-tick` (120ms),
  `--dur-watchdog-route` (1500ms).

### 6.8 Hatching that deepens over surveyed land

- **What & why.** As each region is charted, its coastline
  hachures — the short engraved strokes that shade a chart's
  landward edge — sketch in along the coast, and the vellum
  grain over the region deepens (§4's second grain layer).
  The map visibly shows where it has been worked: surveyed
  land is darker, denser, more *known* than the blank coast
  ahead. It belongs because it is the theme's memory made
  visible at the level of texture — clause 2 (ink is
  permanent) you can see from across the room.
- **Structure.** Hachures are SVG path groups per region in
  the chart layer, each stroke finished, wearing dash masks
  driven per-region by the shared loop. The grain deepening
  is the second turbulence layer (§4) revealed by a mask
  whose edge follows the drawn route's progress through the
  region. Regions are declared in the route object (a region
  per leg, bounded by its landfalls) — hatching exists only
  where a region is declared.
- **Motion spec.** Trigger: the region's first landfall
  arrival begins its hatching; the sketch scrubs with route
  progress across the leg, ≈1200ms of stroke time per region
  at reading pace, `--ease-pen`, strokes in survey order
  (from the arrived landfall along the coast). Grain mask
  follows the same progress, lagging the hatching by ~10% —
  the work first, the patina after. Both latch at region
  completion; neither ever lightens.
- **States.** Unworked (no hatching, base grain) → working
  (sketching) → surveyed (full hatching, deep grain; rest).
  Hover on a surveyed region (when it carries a card or link,
  §6.12): hatching shades one tone deeper over 200ms — the
  original entry's hover, kept. Scrolled-past: surveyed,
  permanent.
- **Content merge.** Hatching shades the *coast of the
  section the reader has just read* — the deepening is the
  receipt for the reading. It never shades regions ahead,
  never shades the sea (hachures are landward, by definition
  of the craft), and stops at every fair sheet's edge (§4).
- **Failure fallback.** No JS: all regions print surveyed —
  a finished chart is a worked chart. Loop stalled:
  watchdog 1500ms completes the current region's hatching to
  the true progress. Print: fully hatched.
- **Reduced-motion variant.** Regions take their surveyed
  state at arrival (hatching printed, grain deep) with no
  sketching — the patina without the pen-work.
- **Performance budget & mobile variant.** Hachure paths are
  the chart layer's largest cost: cap ≤30KB for all regions,
  strokes as single paths per region (not per-stroke
  elements). Mobile: hachure density halves at build (a
  coarser survey for a smaller sheet — same regions, same
  fractions), grain deepening kept (it is one masked layer).
- **Choreography timeline (v2).** Arrival at region's first
  landfall → hatching arms → scrubbed across the leg:
  strokes sketch in survey order → grain mask follows at
  −10% → next arrival: region latches surveyed → next region
  arms. Reverse scroll: no beats — worked land stays worked.
- **State matrix (v2).** *Rest:* surveyed behind the latch,
  unworked ahead. *Hover:* +1 tone over 200ms where linked.
  *Focus:* a focused card's region shades identically to
  hover (focus is inspection too). *Active:* n/a.
  *Scrolled-past:* surveyed, latched. *Disabled / no-JS:*
  all surveyed. *Touch:* no hover shade; surveyed state is
  the touch feedback.
- **Breakpoints (v2).** ≥1200px: full hachure set, grain 9%.
  768–1199px: full set, grain 8%. <768px: half-density
  hachures, grain 9% (the small sheet leans on grain to
  carry the patina the strokes no longer can).
- **Edge cases & failure modes (v2).** *Region with no
  coastline (an inland landfall):* its hatching rings its
  declared boundary (a surveyed parish is hatched round, not
  along) — the region object declares which. *Overlapping
  parallax:* hatching rides the 0.97× layer (§4) while its
  grain mask rides at 1.0×; the ±18px cap keeps the two from
  visibly separating at region edges. *Reader idles
  mid-region:* scrubbed values hold; nothing completes
  itself out of politeness.
- **Accessibility spec (v2).** Purely presentational
  (`aria-hidden`); surveyed state is conveyed in text by the
  index's visited marks (§6.11) and the seal (§6.9). Hatching
  never carries information a reader must have — it is the
  chart's complexion, not its data.
- **Tokens consumed (v2).** `--ink`, `--ink-deep`, `--ease-pen`,
  `--grain-deep` (9%), `--dur-hatch` (1200ms per region),
  `--dur-watchdog-route` (1500ms).

### 6.9 Wax-seal click

- **What & why.** Clicking a landfall — its name, its card,
  its index entry — thuds a wax seal onto the chart beside it:
  a madder disc that drops, splats a breath wider as it lands,
  and settles, marking the landfall *visited* in the margin
  index. It belongs because it is the reader's one act of
  authorship on the chart: the surveyor drew the coast, but
  the sponsor stamps it. Possession by seal — the expedition
  is *theirs* now — and the index keeps the count.
- **Structure.** The seal is an inline SVG: an irregular disc
  (a path with hand-varied radius — a perfect circle is a
  sticker, §9 failure 8), an inner ring, and the landfall's
  initial lettered in IM Fell English at its centre, printed
  complete beneath a scale/opacity performance layer. Seal
  state persists per landfall in `localStorage` — a returning
  visitor finds their seals where they left them, because a
  stamped chart is not un-stamped by closing the book.
- **Motion spec.** Trigger: click/tap/Enter on the landfall's
  control. The seal drops from 8px above its mark over 380ms
  `--ease-thud`, scaling 1.15→1.0; on landing it splats —
  scaleX 1.0→1.06→1.0 over 120ms `--ease-swell` — and its
  legend settles. A soft shadow (one consistent light source,
  §4) grounds it at the landing frame only. Second click:
  the seal is *not* removed (ink is permanent applies to wax
  too) — instead it warms 200ms and the index pulses the
  entry: already yours. Unsealing exists only as an explicit
  index action ("lift the seal"), which fades it over 400ms
  and strikes the index entry — a deliberate un-stamping,
  never an accidental toggle.
- **States.** Unsealed (no mark; the control invites) →
  sealing (380ms) → sealed (rest; index entry marked with a
  madder dot and "visited"). Hover on an unsealed landfall:
  a ghost seal at 18% opacity previews the mark's position —
  the reader sees where their stamp will fall. Focus: ghost
  at 30% + §11 ring on the control. Disabled state: a
  landfall not yet arrived cannot be sealed — its control is
  `aria-disabled`, and attempting it swings the needle
  (§6.6) toward it instead: *not yet — the way is charted,
  sail there first.*
- **Content merge.** The seal lands on the chart *at the
  landfall it seals*, and the index entry it marks is the
  landfall's own entry. The count it feeds ("3 of 6 landfalls
  visited") is printed from the real seal states. A seal
  used as a generic "like" button on unrelated content is a
  stamp on someone else's letter (§9, failure 8).
- **Failure fallback.** No JS: landfalls carry a printed
  "visited" checkbox state in the index (the seal is the
  ceremony; the record is a list) — the function survives
  the performance. Storage unavailable: seals last the
  session and the index says so ("seals keep for this
  sitting") — honesty about persistence, §12.
- **Reduced-motion variant.** The seal appears at rest scale
  with a 120ms opacity settle — stamped, not dropped. The
  ghost preview is unchanged (it is a state, not a motion).
- **Performance budget & mobile variant.** One SVG ≤2KB,
  reused per landfall with its letter swapped. Mobile: seal
  44px (also its touch target's visual), drop distance 6px,
  splat kept — the thud is the element; scale it, never cut
  it.
- **Choreography timeline (v2).** Click → t=0 seal releases
  at +8px, scale 1.15 → t=380 lands, shadow grounds →
  t=380–500 splat settle → t=450 index entry marks (dot
  prints, "visited" appends) → t=500 count line updates.
  Ghost preview precedes all of it at hover/focus.
- **State matrix (v2).** *Rest:* sealed (disc at mark, index
  marked) or unsealed (no disc). *Hover:* ghost 18%.
  *Focus:* ghost 30% + ring. *Active:* the drop itself.
  *Scrolled-past:* unchanged — seals are state, not scroll
  events. *Disabled:* un-arrived landfall — needle swing
  instead of a seal. *Touch:* tap = click; ghost shows on
  first tap's press-and-hold is refused (a held press is
  not a preview gesture on this chart; the tap seals).
- **Breakpoints (v2).** ≥1200px: seal 56px on the chart,
  index marks in the margin. 768–1199px: 48px. <768px: 44px,
  seals land on the landfall card (§6.12) instead of the
  chart layer (the small sheet's chart is too fine to stamp
  honestly), index in the cartouche (§6.11).
- **Edge cases & failure modes (v2).** *Sealing during the
  zoom (§6.4):* the seal waits for the pin's held state —
  stamping a moving chart smears the wax; the click queues
  and fires at hold, with the ghost shown meanwhile.
  *Rapid repeat clicks:* latched after the first; repeats
  only warm. *All six sealed:* the index prints the
  completion line and the needle (§6.6) settles north — the
  voyage is the reader's, whole.
- **Accessibility spec (v2).** The control is a real
  `<button>` per landfall ("Seal St. Cwyll's Harbour as
  visited"), `aria-pressed` carrying state; the seal graphic
  is `aria-hidden`. The index's visited marks are text, not
  colour alone. Touch target ≥44px at every breakpoint.
- **Tokens consumed (v2).** `--madder`, `--madder-deep`,
  `--ink-deep`, `--ease-thud`, `--ease-swell`, `--dur-seal`
  (380ms), `--dur-splat` (120ms), `--seal-size` (56px).

### 6.10 "Here be delays"

- **What & why.** Over the section everyone usually skips —
  the terms, the logistics, the long practical read — the
  chart is hand-lettered, in the cartographer's own hand,
  *"Here be delays."* And if the reader lingers there, a tiny
  ship doodle in the margin weighs anchor and sails a small
  slow circle, waiting, until they move on. It is the
  original entry's anti-slop detail promoted to an element,
  and it belongs because it is the theme's honesty with a
  face: the map admits its territory's dull strait instead
  of disguising it, and the admission is placed exactly where
  the data says people stall.
- **Structure.** The lettering is an SVG path-text in the
  chart margin beside the designated section — IM Fell
  English italic letterforms as drawn paths (hand-lettered
  means drawn, not typeset at an angle), in `--sepia-soft`
  with a surveyor's underline flourish. The ship is a 28px
  SVG doodle (hull, one sail, a wake arc) on a circular
  margin path. The designated section is declared in the
  route object with its analytics reason ("the section with
  the highest measured abandonment") — the joke has a source.
- **Motion spec.** The lettering is static (it was always on
  the chart; the reader's arriving is the event). The ship:
  after the reader dwells in the section for 20s (scroll
  position within it, page visible), the ship fades-print in
  over 600ms and begins its circle — 24s per circuit,
  `--ease-sail`, wake arc drawing behind it and fading. When
  the reader scrolls on, the ship completes its current
  circuit and anchors (it does not vanish mid-sail — even
  the joke keeps the theme's manners). Once per session; a
  reader who returns to the section finds the ship at anchor,
  wake gone.
- **States.** Absent (not yet lingered) → sailing (dwelling)
  → anchored (reader departed or session-spent; rest).
  Hover: the ship does not react — it is waiting, not
  performing. No focus, no control: it is marginalia.
- **Content merge.** The merge is the point: the lettering
  comments on *this site's actual dull section*, chosen from
  measured behaviour and re-chosen when the data changes.
  Lettering it over a section nobody skips — or worse, over
  the pricing — is a joke at the reader's expense and fails
  §10's placement audit.
- **Failure fallback.** No JS: the lettering prints (it is
  part of the finished chart); the ship simply never sails —
  the margin holds an anchored doodle. Timers throttled in a
  background tab: dwell accrues only while the page is
  visible (`visibilitychange`-gated).
- **Reduced-motion variant.** The lettering prints; the ship
  is drawn at anchor from the section's first arrival — the
  wit without the wait, and without the sailing.
- **Performance budget & mobile variant.** Lettering ≤3KB
  SVG, ship ≤1KB, one small rotation on the shared loop's
  timer class. Mobile: the lettering moves into the section's
  head margin (the small sheet has no side margin to doodle
  in) at 15px equivalent; the ship sails its circle at 20px —
  miniaturised, not cut: the theme's honesty is not a
  desktop luxury.
- **Choreography timeline (v2).** Reader enters the section
  → dwell timer starts (visible time only) → t=20s ship
  prints in (600ms) → circuits at 24s, wake drawing/fading
  → reader leaves: current circuit completes → ship anchors,
  wake fades 800ms → session flag set.
- **State matrix (v2).** *Rest:* lettering present, ship
  absent or anchored. *Hover:* none. *Focus:* none (not a
  control). *Active:* n/a. *Scrolled-past:* anchored if it
  sailed. *Disabled / no-JS:* lettering + anchored doodle
  printed. *Touch:* identical; dwell is dwell.
- **Breakpoints (v2).** ≥1200px: margin placement, ship 28px.
  768–1199px: margin placement, ship 24px. <768px: head-margin
  placement, ship 20px, circuit 18s (a smaller circle).
- **Edge cases & failure modes (v2).** *The dull section is
  removed or split:* the route object's designation must
  move with it — §10 checks the lettering's target exists.
  *Reader dwells with the page idle but section off-screen:*
  dwell requires the section at the reading line, not mere
  page idleness. *A second dull section emerges in the data:*
  the chart holds one delays line, ever — the data picks the
  worse strait; two jokes is a comedy club (§9, failure 10).
- **Accessibility spec (v2).** The lettering is `aria-hidden`
  decoration; the section it marks carries its real heading
  as usual. The ship is `aria-hidden`. Nothing about the
  reader's obligations is communicated by the joke — the
  section's content stands on its own, which is why the joke
  is kind rather than cruel.
- **Tokens consumed (v2).** `--sepia-soft`, `--ink`,
  `--ease-sail`, `--dur-dwell` (20s), `--dur-circuit` (24s),
  `--ship-size` (28px).

### 6.11 The cartouche navigation

- **What & why.** The site's navigation is the chart's
  cartouche — the ornamental title block a real chart carries
  in its corner: the voyage's name, the chart's scale line,
  and the index of landfalls, each entry with its leagues and
  its state (charted, visited, ahead). It belongs because a
  chart's furniture is how a chart is used: the reader
  navigates the site the way a navigator uses the cartouche —
  to know where they are on the sheet, what remains, and what
  it costs in leagues to get there.
- **Structure.** A header block on `--parchment` with a brass
  rule frame (double rule, the chart's own border grammar):
  left, the site name engrossed small (§6.3's face at 24px,
  static); centre/right, the landfall index as a horizontal
  list on desktop — each entry: SC label, leagues from
  departure, a state dot (hollow = ahead, ink = charted,
  madder = sealed/visited, §6.9). Below, a 2px mini-route: a
  hairline with the drawn fraction in madder — the route
  (§6.2) in miniature, reading the same latch. On mobile the
  index collapses behind a "The Chart" disclosure, with the
  compass (§6.6) and leagues counter (§6.7) docked in the bar.
- **Motion spec.** The cartouche is fixed; on scroll past
  140px it compresses (padding halves, the scale line hides)
  over 300ms `--ease-sail` — a chart folding to its working
  size. The index's state dots update at arrival latches
  (dot fills 200ms); the mini-route's madder fraction is
  written by the shared loop. The current landfall's entry
  takes an ink underline that glides between entries
  (400ms `--ease-glide`) as arrivals change it.
- **States.** Expanded (top) → compressed (underway). Index
  entries: ahead (hollow dot, `--sepia-soft` label) → current
  (ink label, underline) → charted (ink dot) → visited
  (madder dot, "visited" appended for AT). Hover on an entry:
  its region's hatching previews one tone deeper on the chart
  (§6.8) — the index and the coast answer each other. Focus:
  §11 ring; the preview applies identically.
- **Content merge.** The index entries are the page's real
  sections with their real leagues — navigation as the
  chart's own table of contents, not a menu wearing a frame.
  Entries link by anchor to their landfalls; following one is
  a jump (§13's jump rule applies: the chart completes in
  order, no theatre owed).
- **Failure fallback.** No JS: the cartouche prints expanded,
  all dots ink (a finished chart's index), links work as
  anchors. Compression is JS-armed; without it the block
  simply stays its full, handsome size.
- **Reduced-motion variant.** No compression glide (the block
  takes its compressed size instantly past 140px), no dot
  transitions, the underline jumps. All state still updates.
- **Performance budget & mobile variant.** The cartouche is
  DOM + one hairline write per frame. Mobile: bar with name,
  needle, counter and the disclosure; the index lists
  vertically in the opened sheet with 44px rows.
- **Choreography timeline (v2).** Load: expanded, index at
  departure state → scroll 140px: compress 300ms → each
  arrival: dot fills (200ms), underline glides (400ms),
  mini-route fraction continuous → final arrival: index
  prints all-visited state when seals complete (§6.9).
- **State matrix (v2).** *Rest:* as above. *Hover:* entry →
  chart preview shade. *Focus:* ring + same preview.
  *Active:* anchor jump fires §13. *Scrolled-past:* n/a
  (fixed). *Disabled / no-JS:* static expanded. *Touch:*
  disclosure opens the index sheet; taps are 44px rows.
- **Breakpoints (v2).** ≥1200px: full horizontal index,
  scale line shown. 768–1199px: index wraps to two rows,
  scale line hidden. <768px: bar + disclosure sheet; compass
  and counter docked.
- **Edge cases & failure modes (v2).** *Many landfalls
  (8+):* the index scrolls horizontally within the cartouche
  with the current entry scrolled into view — a long chart's
  index is a strip, not a paragraph. *Long names:* entries
  use the SC label form (law 1's demotion) — the full name
  lives at the landfall. *Sticky offset:* landfall anchors
  land below the compressed cartouche (`scroll-margin-top`
  set from the same token the compression uses).
- **Accessibility spec (v2).** A real `<nav>` with a list;
  the current entry carries `aria-current="location"`;
  state dots are supplemented by text ("visited", "ahead")
  for AT — never colour alone. The disclosure is a
  `<button>` with `aria-expanded`. Focus order: name, index
  entries in voyage order, disclosure on mobile.
- **Tokens consumed (v2).** `--parchment`, `--brass`,
  `--ink`, `--sepia-soft`, `--madder`, `--ease-sail`,
  `--ease-glide`, `--dur-compress` (300ms),
  `--cartouche-h` (compressed height token).

### 6.12 Landfall cards

- **What & why.** Where the site must offer its voyages,
  ports or stops as a set — the listing grammar — each is a
  landfall card: a small surveyed inset of that place's own
  coast, its name, its leagues from departure, its sounding
  summary, and its seal state. It belongs because a
  Cartographer's Table site sells *places on a route*, and
  the card is the chart's way of holding one place up for
  inspection without leaving the table: an inset, not a
  poster.
- **Structure.** A card on `--parchment`: head, the place's
  inset chart (a small SVG excerpt of its coast with its
  hatching state, §6.8); body, the name (§6.3's face, static
  here — cards do not letter; lettering is earned at the
  landfall itself), two or three lines of copy, a data row
  (leagues, principal sounding, season) in Franklin tabular;
  foot, the seal control (§6.9) and the "Chart this
  landfall" link to its page. The whole card is not a link —
  the link and the seal are separate acts.
- **Motion spec.** Cards enter with their section's fog lift
  (§6.5) — no separate entrance. Hover: the inset's hatching
  shades one tone deeper (200ms) and the card lifts 2px with
  its shadow deepening from the one light source — a sheet
  picked up off the table, not a tile scaling. The seal
  control behaves per §6.9. Cards never stagger, never flip:
  charts are laid side by side, not dealt.
- **States.** Rest → hover (shade + lift) → focus-within
  (same, with ring on the focused control). Visited state:
  the seal printed on the inset's corner and the data row
  appends "— visited". A card for a place not yet surveyed
  (a future voyage) prints its inset as blank vellum with
  its name as a label and "Unsurveyed — the season is not
  yet charted": an honest empty berth in the set, never a
  fake coast.
- **Content merge.** The inset is the place's actual coast
  from the site chart; the data row is the route object's
  figures for that place. A card whose inset is a stock
  squiggle and whose leagues are invented is a brochure in
  the chart's clothing (§9, failure 7's retail form).
- **Failure fallback.** No JS: cards print complete, seals
  as their index checkboxes (§6.9's fallback), insets fully
  hatched. Fog never armed: cards stand clear.
- **Reduced-motion variant.** No lift on hover (the hatching
  shade remains — it is a state change, readable without
  motion); seals per §6.9's variant.
- **Performance budget & mobile variant.** Inset SVGs ≤6KB
  each, cap 6 cards per page (a chart table holds six insets
  before it is a catalogue, §1). Mobile: cards stack; the
  inset goes full-width at the card's head (the small sheet
  gives the coast the whole width — it is the point of the
  card); seal at 44px.
- **Choreography timeline (v2).** Section fog lifts (§6.5) →
  cards clear with it → hover: shade 200ms, lift concurrent
  → seal click: §6.9's timeline, landing on the inset →
  visited line appends at t=500 of the seal's clock.
- **State matrix (v2).** *Rest:* printed, unvisited or
  visited per state. *Hover:* shade + 2px lift. *Focus:*
  ring on the control; card shades as hover. *Active:*
  link follows §13's jump rule; seal per §6.9.
  *Scrolled-past:* unchanged. *Disabled / no-JS:* complete
  static set. *Touch:* no lift; first tap on the link
  navigates (no hover theatre is faked).
- **Breakpoints (v2).** ≥1200px: 3 per row, inset 16:10.
  768–1199px: 2 per row. <768px: 1 per row, inset full-width
  16:9, data row wraps to two lines.
- **Edge cases & failure modes (v2).** *A place with no
  coast (inland):* its inset is its hatched boundary (§6.8's
  ruling) — the grammar holds. *Long names:* the name wraps
  to two lines at 24px floor (law 1) and the card grows —
  cards in a row match the tallest, sheets aligned at the
  foot. *Missing data (no sounding declared):* the data row
  omits the field — a blank in the row is honest; a
  plausible number is a forgery.
- **Accessibility spec (v2).** Card heading is the place
  name (`<h3>`); the inset is `aria-hidden` (its data is the
  data row, in text). Seal button labelled per §6.9. Reading
  order: name, copy, data, actions — the DOM order, at every
  breakpoint.
- **Tokens consumed (v2).** `--parchment`, `--ink`,
  `--ink-deep`, `--teal-deep`, `--madder`, `--ease-sail`,
  `--dur-shade` (200ms), `--card-lift` (2px).


### 6.13 The logbook form

- **What & why.** The conversion form — booking a berth,
  joining the voyage, writing to the harbour office — is a
  page of the ship's logbook: ruled leaves on `--parchment`,
  fields as log lines, and a confirmation that is entered as
  the log's next numbered entry and stamped with the seal.
  It belongs because on this site a booking is not a
  transaction in a funnel; it is an entry in a record the
  visitor has watched being kept all the way down the page.
  The form inherits the chart's credibility because it is
  kept in the chart's grammar.
- **Structure.** A `<form>` on a parchment leaf with a brass
  head rule and the log's running head ("THE LOGBOOK — ENTRY
  № —", the number blank until success). Fields: label in
  IM Fell English SC, input on a ruled line (1px `--sepia-soft`
  baseline, no box — log entries are written on lines), ink
  `--ink`. The voyage choice is a radio set drawn as the
  chart's landfall list (dot + name + leagues), not a select.
  Submit is the theme's one madder button (§11): *"Set it
  down in the log."* (§12 verbatim). Errors print beneath
  their field in `--madder-deep`, in the Log's voice (§12).
- **Motion spec.** Focus: the field's rule inks from
  `--sepia-soft` to `--ink` left-to-right over 260ms
  `--ease-pen` — a line being ruled for writing. Filled and
  blurred: the rule rests at `--ink` 60%. Choice radios: the
  chosen landfall's dot fills madder 200ms and its leagues
  print beside the total line ("Your passage: 118 leagues to
  St. Cwyll's" — from the route object). Submit: the button
  presses 1px; past 600ms it reads "Entering…"; on success
  the form is replaced by the entered entry (below). No
  shake, no fog, no spinner (§11).
- **States.** Rest (rules at 40%) → focus (inking) → filled
  (rule at 60%, ink text) → error (rule `--madder-deep`, the
  Log's line beneath, the visitor's writing untouched) →
  submitting (button state) → entered (the confirmation
  entry, §below). The entered entry: the running head takes
  its number — the printed log count + 1, from the record —
  the visitor's own details set as a log entry in Fell
  italic, and the seal (§6.9's drawing) thuds onto it at
  t=300. The entry is the confirmation; there is no separate
  "success screen."
- **Content merge.** The form's choices are the site's real
  landfalls with their real leagues; its entry number is the
  real log count + 1; its confirmation promises only what
  the operator actually does ("The office writes within two
  days" — if that is true). A logbook form over a generic
  CRM with invented entry numbers is a forged log (§9,
  failure 7 applied to conversion).
- **Failure fallback.** The form is a working form without
  JS: native validation off, server validates, errors return
  as a re-rendered leaf with the Log's lines printed and the
  visitor's entries intact. The seal and the entry ceremony
  are progressive layers over a submittable form, never the
  submission mechanism.
- **Reduced-motion variant.** Rules change colour without
  the inking sweep; the seal appears per §6.9's variant; the
  entry replaces the form without ceremony. All text and
  state identical.
- **Performance budget & mobile variant.** The form is DOM
  and rules — no library. Mobile: the leaf goes full-width,
  radio landfalls stack at 44px rows, the submit is
  full-width madder (the small sheet spends its one red
  button whole).
- **Choreography timeline (v2).** Focus: rule inks 260ms →
  choice made: dot fills 200ms, passage line updates →
  submit: press, 600ms "Entering…" → success: form fades to
  the leaf's blank (200ms) → entry sets (Fell italic lines,
  no stagger — a log entry is written, not performed) →
  t=300 seal thuds (§6.9's 380ms) → entry at rest, numbered.
  Error path: no timeline — errors print immediately; a
  delayed error is a withheld correction.
- **State matrix (v2).** *Rest:* rules 40%, labels SC.
  *Hover:* field rules warm to 55% (a line inviting a hand).
  *Focus:* inking sweep + §11 focus ring on the input (the
  ring is accessibility's, the ink is the theme's; both
  show). *Active:* button press 1px. *Scrolled-past:* n/a.
  *Disabled:* submit disabled while a required line is
  empty only if the Log can say why beside it ("The log
  wants a name for the entry") — a mute disabled button is
  refused. *Touch:* 44px radio rows, 16px input text (no
  focus zoom).
- **Breakpoints (v2).** ≥1200px: leaf 640px in the measure,
  two-column name/passage rows. 768–1199px: leaf full
  column, rows stack at the passage choice. <768px: leaf
  full-width, single column, submit full-width.
- **Edge cases & failure modes (v2).** *Long voyages (many
  landfalls):* the radio list caps at the route's landfalls;
  a "further ports" entry links to the listing (§7) rather
  than growing the log's page. *Server error (500):* the
  Log admits (§12): "The log could not be written to — the
  office has been told. Your entry is kept above; try the
  stamp again." — and the entry *is* kept, in the form.
  *Double submit:* the button latches at first press; a
  second entry with the same number is a forgery the client
  must never mint.
- **Accessibility spec (v2).** Real `<label>` per field,
  errors linked by `aria-describedby`, error summary at the
  leaf's head on return ("Two lines want attention") with
  anchors to the fields. Focus moves to the first error
  field on failed submit, to the entry's heading on success.
  Contrast: labels `--ink` 9.20:1; error text
  `--madder-deep` 7.71:1 — errors are never madder-bright
  small text (law 4).
- **Tokens consumed (v2).** `--parchment`, `--ink`,
  `--sepia-soft`, `--madder`, `--madder-deep`, `--brass`,
  `--ease-pen`, `--ease-thud`, `--dur-ink` (260ms),
  `--dur-seal` (380ms).

### 6.14 The table of soundings

- **What & why.** The theme's one data table: the full survey
  printed as a table — every sounding by leg, with its depth
  in fathoms, its position, and the leg's leagues and
  bearing. It belongs because a chart's marginalia (§6.7)
  needs its audit surface: the table is where the chart's
  numbers can be read comparatively, checked, and believed.
  Claim (the coast), instrument (the needle), record (this
  table) — §7's order for the survey page.
- **Structure.** A `<table>` on `--vellum-deep`: head row in
  `--teal-deep` with vellum text (the one licensed teal
  surface, §2), columns in IM Fell English SC; body rows in
  Franklin tabular 14px — Leg, Landfall, Sounding (fathoms),
  Bearing, Leagues. Leg subtotal rows rule in brass; the
  totals row rules double in ink and prints the voyage
  object whole: 214 leagues, the sounding count, the deepest
  and shoalest water. The table is generated from the route
  object at build — it cannot drift from the chart because
  it is printed from the same survey.
- **Motion spec.** Almost none, by design: the table is the
  record, and records do not perform. Rows take their state
  from the latch — a leg's rows deepen from `--sepia-soft`
  to `--ink` as that leg is sailed (state, scrubbed by
  arrival, 300ms). The totals row's leagues figure counts
  once, when the table first centres, from the latched value
  to the total over 900ms `--ease-pen` — the one count the
  table is allowed, because it is the audit completing
  itself. No row hovers with a colour wash; a hovered row
  rules a 2px ink left border (a finger down the page of
  the log).
- **States.** Unsounded legs (apparatus tone) → sounded
  (ink) as latched. Sortable columns are refused (§11) — a
  survey is read in voyage order; the one interaction is the
  leg rows' expansion on small screens (below).
- **Content merge.** The table *is* §6.7's data in full and
  §4's object in print. Its totals are §10's audit surface.
  A table of anything else (prices, specs) wearing this
  grammar is borrowed authority (§9, failure 12).
- **Failure fallback.** No JS: all rows print in ink at full
  state — the record complete. The table is fully usable
  with every script dead; it is the page's most static
  citizen by intention.
- **Reduced-motion variant.** Rows take ink state instantly
  at arrivals; the totals figure prints at total, uncounted.
- **Performance budget & mobile variant.** A table is text:
  ≤4KB for a 6-leg survey. Mobile: the table keeps all five
  columns at 12.5px Franklin (a survey is not reflowed into
  cards — comparability is its function) with horizontal
  scroll inside a brass-ruled frame and the Leg column
  sticky — the frame admits the sheet is wide, honestly.
- **Choreography timeline (v2).** Arrivals during the page:
  leg rows ink at their latch (300ms) → table centres first
  time: totals count 900ms to 214 → final arrival: totals
  row's state completes; the shoalest sounding's cell takes
  its madder-deep mark (the survey's warning, printed).
- **State matrix (v2).** *Rest:* rows at latch state.
  *Hover:* 2px ink row rule. *Focus:* rows are not focusable;
  the table's links (landfall names) take §11 rings.
  *Active:* n/a. *Scrolled-past:* all legs ink.
  *Disabled / no-JS:* complete ink record. *Touch:* scroll
  frame pans natively; no tap states are faked.
- **Breakpoints (v2).** ≥1200px: full table in the measure.
  768–1199px: full table, Sounding column narrows (positions
  abbreviate to fractions). <768px: framed horizontal scroll,
  sticky Leg column, 12.5px data.
- **Edge cases & failure modes (v2).** *A leg with no
  soundings (an overland portage):* its rows print the
  portage line — "No water — the boats were carried" — in
  the sounding column: the record admits the gap in the
  survey's own grammar. *Very long surveys (12+ legs):* the
  table paginates by leg groups behind the §11 bank-index
  pattern ("Earlier legs"), never by arbitrary row counts.
- **Accessibility spec (v2).** Real `<th>` scope, a
  `<caption>` naming the survey ("Soundings of the Salt
  Road, by leg"), totals in a `<tfoot>`. State (sounded /
  ahead) is a text column state, not colour alone — the Leg
  cell appends "(ahead)" until latched. Contrast: head
  vellum on teal-deep 6.95:1; body ink on vellum-deep
  7.72:1.
- **Tokens consumed (v2).** `--vellum-deep`, `--teal-deep`,
  `--vellum`, `--ink`, `--sepia-soft`, `--brass`,
  `--madder-deep`, `--ease-pen`, `--dur-ink` (260ms).

### 6.15 Logbook entries

- **What & why.** Testimonials and field reports are kept as
  logbook entries: dated, positioned, and signed — each a
  ruled entry on parchment with the writer's landfall, the
  date they sailed, their words set as a log-keeper's fair
  copy, and their initial sealed small beside it. It belongs
  because praise on a chart site must carry the chart's
  evidence discipline: who, where on the route, when — or it
  is weather-talk. An entry without a position is a rumour
  with good typography.
- **Structure.** Entries stack as leaves in a bordered log
  column: head line (SC): *"ENTRY — 14 MAY — ST. CWYLL'S
  HARBOUR, 77 LEAGUES"*; body in Libre Franklin 15px (the
  fair copy — the writer's words, edited only for length,
  and the entry says if it was shortened); foot: the
  writer's name in Fell italic and a 28px seal (§6.9's
  drawing, their initial) printed — not clickable: this seal
  is a signature, not the reader's stamp.
- **Motion spec.** Entries arrive with their section's fog
  lift (§6.5) and nothing else — a log does not animate its
  past. The one licensed motion: as the route passes the
  entry's own landfall fraction, the entry's head line
  deepens `--sepia-soft` → `--ink` (300ms) and its seal
  takes its full madder — the chart and the log agreeing
  about where the reader has got to.
- **States.** Unreached (apparatus tone head) → reached
  (ink head, full seal). Hover: none — entries are read, not
  handled. The set is capped at five per page (§4's density
  in prose form: a log page of forty entries is a guestbook,
  not a survey).
- **Content merge.** Every entry's position is a real
  landfall of the site's route, its leagues the object's;
  entries are selected for the legs they evidence (one per
  leg is the honest spread). An entry praising a place the
  route never visits is struck by §10's audit.
- **Failure fallback.** No JS: entries print complete, heads
  in ink. Nothing about an entry depends on a script — a
  record's whole virtue is that it persists.
- **Reduced-motion variant.** Identical, minus nothing — the
  element was already still; its state change is instant.
- **Performance budget & mobile variant.** Text and one
  small SVG per entry. Mobile: entries full-width, the head
  line wraps (position before date — where before when, the
  chart's priority), seal 24px.
- **Choreography timeline (v2).** Section fog lift (§6.5)
  reveals the stack → route passes an entry's fraction: head
  inks (300ms), seal fills → rest. No entrance beats of its
  own, ever.
- **State matrix (v2).** *Rest:* at latch state. *Hover:*
  none. *Focus:* entries contain no controls (a quoted link
  in a writer's words is edited out at selection — the log
  does not carry other people's links). *Active:* n/a.
  *Scrolled-past:* reached state. *Disabled / no-JS:*
  complete. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: log column 62ch with the
  margin rail beside. 768–1199px: full column. <768px:
  full-width leaves, head wraps, seal 24px.
- **Edge cases & failure modes (v2).** *A writer withdraws
  consent:* the entry is struck from the log with a ruled
  line and a note ("Entry struck at the writer's request —
  the log keeps the striking, not the words") — the theme's
  honesty applied to its own records. *No entries yet (a
  new voyage):* the log prints its empty state in §12's
  voice — "The log opens with the spring sailing. Nothing is
  entered yet, and nothing is invented for the space."
- **Accessibility spec (v2).** Entries are `<article>`s with
  the head as their heading; the seal is `aria-hidden`; the
  date is a real `<time>` element. Contrast: head ink on
  parchment 9.87:1 at reached state; unreached heads are
  `--sepia-soft` 5.66:1 — apparatus, still above AA for its
  size class.
- **Tokens consumed (v2).** `--parchment`, `--ink`,
  `--sepia-soft`, `--madder`, `--brass`, `--dur-ink` (260ms).

### 6.16 The bearings accordion

- **What & why.** The FAQ grammar: questions of navigation,
  each with its bearing number, unfolding like a chart fold
  when opened — the answer's leaf swings down from its head
  rule, and the bearing rotates to point down the opened
  leaf. It belongs because a chart site's questions are
  practical seamanship (what to bring, where to board, what
  the weather does to the sailing), and the chart's own
  furniture — bearings, folds, ruled leaves — answers them
  without importing a foreign component's manners.
- **Structure.** A stack of ruled entries on `--parchment`:
  head row (a real `<button>`): bearing chip ("BRG 042°" —
  the question's number in the voyage's grammar, assigned in
  route order, not by importance), the question in Fell SC
  17px, a small brass chevron drawn as a compass point. The
  answer leaf: Franklin body, max 62ch, with any figure it
  quotes carrying its source line (§12).
- **Motion spec.** Open: the leaf unfolds over 550ms
  `--ease-pen` — a `grid-template-rows` 0fr→1fr transition
  with the head rule as the fold's hinge, the compass point
  rotating 90° over 300ms `--ease-swell` to point down the
  leaf. Close: 400ms, the fold reversing. One leaf open at a
  time in the stack (a chart fold covers its neighbour —
  the physical truth of the metaphor), unless the stack is
  on the dedicated questions page (§7), where two may rest
  open.
- **States.** Closed (head only) → unfolding → open (rest;
  bearing points down-leaf) → folding. Hover on a head: its
  rule warms to `--ink`. Focus: §11 ring on the button.
  The deep-linked question (URL fragment) opens at load,
  instantly, no fold — a reader sent to an answer is not
  made to watch it unfold.
- **Content merge.** The bearings are the questions' real
  order on the voyage (boarding before weather before
  return), and answers quote the route object's figures
  where figures are the answer. An accordion of marketing
  questions ("Why are we the best?") in bearings clothing
  fails §12's voice audit.
- **Failure fallback.** No JS: all leaves print open — a
  chart unfolded on the table shows everything. The button
  degrades to a heading. Nothing is ever locked inside a
  closed leaf without script.
- **Reduced-motion variant.** Leaves open/close instantly;
  the compass point jumps. State and content identical.
- **Performance budget & mobile variant.** CSS grid-rows
  transition — no height measuring, no JS animation. Mobile:
  heads wrap to two lines (bearing chip keeps its line),
  leaves full-width, 44px head rows minimum.
- **Choreography timeline (v2).** Click → t=0 fold begins,
  compass point rotates (300ms) → t=550 leaf at full, its
  last line clear of the fold → previously open leaf folds
  concurrently (400ms) — the stack's total height breathes
  once, never twice.
- **State matrix (v2).** *Rest:* closed or open per state.
  *Hover:* rule warms. *Focus:* ring; no auto-open (focus
  is not a request to read). *Active:* the fold.
  *Scrolled-past:* state persists. *Disabled / no-JS:* all
  open. *Touch:* tap = click; heads ≥44px.
- **Breakpoints (v2).** ≥1200px: stack in the measure,
  bearing chips left. 768–1199px: full column. <768px:
  full-width, chip above the question line.
- **Edge cases & failure modes (v2).** *Long answers (300+
  words):* the leaf caps at 60vh with its own scroll — a
  fold that unrolls the whole page has mistaken itself for
  a section; better, the question is promoted to a landfall
  (§15's editorial rule). *Print:* all leaves print open.
  *Many questions (10+):* the stack moves to its own page
  (§7); the home chart carries at most five bearings.
- **Accessibility spec (v2).** `aria-expanded` on the
  button, `aria-controls` to the leaf region, the leaf a
  `role="region"` with `aria-labelledby`. Keyboard: standard
  button behaviour; arrow-key travel between heads is
  offered (roving) but never required. Contrast: question
  ink on parchment 9.87:1; chip text `--madder-deep`
  8.27:1.
- **Tokens consumed (v2).** `--parchment`, `--ink`,
  `--sepia-soft`, `--brass`, `--madder-deep`, `--ease-pen`,
  `--ease-swell`, `--dur-fold` (550ms).

### 6.17 The chart-room footer

- **What & why.** The footer is the chart's imprint block,
  set in the chart room after dark: a `--night` ground
  carrying the survey's colophon — who charted it, when, the
  voyage's totals — the scale bar, the credit line, and the
  one brass-lettered passage in the theme (§2: brass may
  letter on night). It belongs because a real chart ends
  with its imprint: the authority for everything above it,
  printed where the sheet ends. The page's last act is the
  chart signing itself.
- **Structure.** A night panel: top, a brass double rule (the
  cartouche's grammar, closing the frame §6.11 opened);
  columns: the imprint (site name, "Charted by —" line, the
  survey's date), the voyage summary (the route object's
  totals printed as the log speaks them: landfalls, leagues,
  soundings counted), the scale bar (a brass rule with its
  leagues marked — drawn to the chart's declared scale, a
  working scale, not a decoration), and the return link:
  *"Back to the departure"* — which sails the reader home
  (§below). The credit line (§12 verbatim) closes the panel
  in Fell italic, vellum on night.
- **Motion spec.** The panel enters plainly (it is the
  sheet's end; ends do not perform). The return link, on
  activation: the page glides to the top over 1200ms
  `--ease-glide` with the route un-drawing **refused** — the
  chart stays charted (clause 2); instead the needle (§6.6)
  swings to the departure bearing during the glide and the
  cartouche's index re-marks the current entry as the reader
  passes each landfall upward. Arriving at the top, the
  reader finds their whole voyage drawn behind them — the
  footer has sent them home over a completed chart.
- **States.** Rest. The summary's figures are state-aware:
  leagues *sailed by this reader* (the latch) printed beside
  the voyage's total ("You have charted 158 of 214 leagues")
  — the imprint personalises from the record, never from a
  profile. Hover on the return link: its brass rule draws
  220ms. Focus: vellum ring on night (§11).
- **Content merge.** Every figure in the imprint is the
  route object's or the reader's latch — the footer's
  summary is the third printing of the survey (§10 audits
  all three: chart, table, imprint). The scale bar is drawn
  from the chart's declared scale token, so it is true of
  the sheet it closes.
- **Failure fallback.** No JS: the summary prints the
  voyage's totals without the personal line (no latch to
  read), the return link is a plain anchor to the top.
  Nothing in the imprint requires a script to be true.
- **Reduced-motion variant.** The return link jumps (native
  anchor behaviour); the needle sets instantly. The panel
  is otherwise identical — it never moved.
- **Performance budget & mobile variant.** A static panel;
  the glide is one scroll animation. Mobile: columns stack
  (imprint, summary, scale, return), the scale bar keeps its
  true length relative to the small sheet's declared scale —
  a scale bar that lies about scale to fit a phone is §9,
  failure 12 in miniature.
- **Choreography timeline (v2).** Footer arrives: nothing
  performs → return activated: needle swings (1100ms,
  concurrent) → glide 1200ms, index re-marking upward →
  top: cartouche expanded state, chart fully drawn, needle
  at departure bearing → rest.
- **State matrix (v2).** *Rest:* printed imprint. *Hover:*
  link rule draws. *Focus:* vellum ring. *Active:* the
  sail-home. *Scrolled-past:* n/a (it is the end).
  *Disabled / no-JS:* static imprint + anchor. *Touch:*
  identical; the return row is 44px.
- **Breakpoints (v2).** ≥1200px: four columns. 768–1199px:
  two columns (imprint + summary; scale + return).
  <768px: stacked, scale bar full-width.
- **Edge cases & failure modes (v2).** *Reader arrives by
  jump (§13):* the personal line reads the latch honestly
  ("You have charted 214 of 214 leagues — by the chart's
  reckoning; the sailing was swift") — the log notes the
  manner of arrival without scolding. *No sailing at all
  (footer reached by keyboard):* the line prints "The chart
  is drawn; the sailing is yours to make" — the record
  admits the route not taken.
- **Accessibility spec (v2).** A `<footer>` with the imprint
  as its heading structure; brass lettering on night is
  6.78:1 (labels and the credit at ≥15px); body text vellum
  on night 13.41:1. The return link's purpose is its text —
  no icon-only navigation at the sheet's end.
- **Tokens consumed (v2).** `--night`, `--vellum`,
  `--parchment`, `--brass`, `--ink-deep`, `--ease-glide`,
  `--dur-sail-home` (1200ms), `--dur-swing` (1100ms).

### 6.18 The unrolling (loader & page transition)

- **What & why.** Moving between pages of the site, the old
  chart rolls away from one edge and the new sheet unrolls
  across the table — vellum over vellum, the new page's route
  already drawing its first leg as the sheet settles. And
  while a page's own content loads, its unbuilt regions show
  as *uncharted sheet*: blank vellum panels ruled with the
  chart's border, marked in SC — *"UNCHARTED — THE SURVEY IS
  UNDER WAY"* — never grey boxes. It belongs because the
  theme's material has a honest way to be absent: a chart
  that has not been drawn yet is blank paper with a border,
  and a site that travels between charts should roll them
  like charts.
- **Structure.** Transition: a fixed vellum layer with the
  chart border grammar, its leading edge a rolled shadow
  (a gradient cylinder illusion, one light source), animated
  by a clip-path inset from the navigation's side. The new
  page loads beneath it; the layer unrolls off as the new
  sheet's hero arms (§6.1). Skeleton: unbuilt sections render
  their true layout in `--vellum-deep` panels with the SC
  uncharted line and a faint rose outline — the layout is
  real (CLS 0), only the survey is pending.
- **Motion spec.** Transition total 700ms `--ease-glide`:
  roll-away 300ms (old page covered by the sheet's back),
  swap at full cover, unroll 400ms onto the new page. Hard
  ceiling: if the new page is not ready at 2000ms, the sheet
  lifts plainly (a fade of the layer only) — a reader is
  never held behind rolled vellum. Skeleton: panels persist
  until their content arrives, then the content's own
  element rules apply (fog §6.5 if unvisited, print if
  charted) — the uncharted panel never cross-fades into
  content; it is *replaced*, the way a survey replaces a
  blank.
- **States.** Idle (layer absent) → rolling → covered (swap)
  → unrolling → idle. Skeleton: uncharted → replaced.
  Browser back/forward: the transition is skipped (the
  browser's own travel is not the site's to choreograph) —
  pages arrive plainly, charts drawn to the latch.
- **Content merge.** The unrolling is the site's travel
  grammar: it happens between *charts* (pages of this site),
  never inside a page, never over the logbook's submission
  (§6.13's entry must not be interrupted by weather or
  rolling — a record being written is sacred). External
  links never trigger it.
- **Failure fallback.** No JS: plain navigation, no layer,
  skeletons render as the sections' final layout with the
  uncharted line as a printed note until content exists
  server-side. A failed page load under the sheet: the
  ceiling lifts it and the browser's own error stands — the
  theme does not wallpaper over a wreck.
- **Reduced-motion variant.** No rolling: navigation is
  instant, pages arrive with their charts at latch state.
  Skeletons are unchanged (they are layout, not motion).
- **Performance budget & mobile variant.** The layer is one
  div + gradient; the transition script is part of the
  ≤34KB chart script (§14). Mobile: the roll becomes a plain
  sheet slide from the bottom edge (a small chart is lifted,
  not rolled — the physics of small paper), 500ms, same
  ceiling.
- **Choreography timeline (v2).** Internal link activated →
  t=0 roll-away begins → t=300 full cover, navigation swaps
  → new page's hero arms beneath → t=300–700 unroll → new
  sheet at rest, its first leg drawing (§6.1). Ceiling
  2000ms oversees the whole act.
- **State matrix (v2).** *Rest:* layer absent. *Hover:*
  none. *Focus:* focus is never held by the layer; on
  arrival it lands on the new page's heading (the swap
  moves focus deliberately, once, announced by the
  heading). *Active:* the roll. *Scrolled-past:* n/a.
  *Disabled / no-JS:* plain navigation. *Touch:* identical;
  swipe-back gestures are the browser's, untouched.
- **Breakpoints (v2).** ≥1200px: side roll, 700ms.
  768–1199px: side roll, 600ms. <768px: bottom sheet slide,
  500ms.
- **Edge cases & failure modes (v2).** *Slow page (3G):*
  the ceiling rules — the sheet shows the uncharted line
  and a plain "still charting…" apparatus note after
  1200ms, and lifts at 2000ms regardless. *Same-page
  anchors:* never trigger the roll (they are §13 jumps).
  *Form submission in flight:* the roll is suppressed until
  the logbook's entry resolves (§6.13) — travel never
  interrupts a record.
- **Accessibility spec (v2).** The layer is `aria-hidden`;
  during the covered beat the old page is inert. Arrival
  focus lands on the new `<h1>` with `tabindex="-1"` — the
  one licensed focus move, because the alternative (focus
  lost to the body) strands keyboard sailors. The skeleton's
  status text ("The survey is under way") is the visually
  hidden `aria-live` polite note, once per page.
- **Tokens consumed (v2).** `--vellum`, `--vellum-deep`,
  `--ink`, `--sepia-soft`, `--brass`, `--ease-glide`,
  `--dur-roll` (700ms), `--dur-ceiling` (2000ms).


## 7. Page application map

**Home.** The full voyage: charting hero (§6.1), the master
route (§6.2) through all six landfalls, names engrossing
(§6.3), the one pinned zoom (§6.4) at the fourth landfall,
fog on every unvisited region (§6.5), needle and counters
live (§6.6, §6.7), hatching deepening (§6.8), seals offered
(§6.9), the delays line over the practical section (§6.10),
cartouche (§6.11) and the chart-room footer (§6.17). The
home page is the only page licensed to run every element;
it is also the page §4's density ration is audited on.

**Listing (the voyages / the ports).** A chart index, not a
catalogue: landfall cards (§6.12) capped at six, over a
resting chart drawn in full — a listing is a reference sheet,
consulted, not sailed, so its chart prints complete and its
route is the index's mini-route only. No pin, no fog: a
reader comparing voyages must see all the coasts at once.
Cards carry their seal state from the reader's latch.

**Detail (one voyage / one port).** The detail page *is* a
landfall enlarged: its hero is that place's inset chart at
zoom rest scale (§6.4's inset grammar, unpinned), its own
short route (three to four stops within the place — a harbour
chart inside the voyage chart, fractions declared in a local
route object), its soundings table (§6.14) scoped to its
legs, and the logbook form (§6.13) at its foot in the booking
variant. Names letter on arrival exactly as on the home
chart — a detail page is still a place being reached.

**About (the surveyors).** The chart at rest: fully drawn,
grain deep everywhere — this is the office, where the work
is already done. The crew are kept as logbook entries (§6.15)
with their surveying grounds as positions; the methods
section carries the bearings accordion (§6.16) for its
practical questions. No route is sailed on the about page;
the cartouche's index links home to begin one.

**Survey / the record (data page).** Claim, instrument,
record, in that order: the coast described, the needle and
counters (§6.6, §6.7) as instruments, the table of soundings
(§6.14) complete. This page is §10's audit surface — the
gate's three-printings check is performed against it — so
it carries the least weather of any page: fog only on its
one unvisited appendix, no pin, no cards.

**Booking / contact (conversion).** The logbook form (§6.13)
as the page's centre, on a chart drawn complete — a page
someone visits to *do* something is a surveyed page; nobody
signs a log in fog. The practical facts (boarding point,
what the weather does to sailings) sit beside it as bearings
(§6.16). The seal the confirmation takes is the reader's
first — the conversion *is* a sealing, and the page knows it.

**The uncharted page (404).** On `--night`: a blank vellum
sheet in a brass frame, one engrossed line — *"Terra
incognita."* — the Log's admission beneath ("This coast is
not on the chart. The chart's harbours are below."), and the
index of landfalls as plain links. No route is drawn to it
and none leaves it except the reader's choice. Stillness and
a fact: the theme's model error page, kin to every honest
blank on every real chart.

## 8. Worked examples

The site in all three: **Aveline & Cross, Charted Voyages** —
a small operator sailing one surveyed route, **The Salt
Road**: 214 leagues down a working coast, six landfalls
(Port Aveline, The Gull Shoals, St. Cwyll's Harbour, The Long
Reach, Fog Anchorage, Cape Meridian), in nine days, twelve
berths. The route object (§4) is the site's single source:
legs of 38 / 39 / 41 / 40 / 56 leagues, bearings 042° / 078°
/ 031° / 105° / 063°, fractions 0.00 / 0.18 / 0.36 / 0.55 /
0.74 / 1.00, and a declared sounding set of fourteen depths
along the coast. The logbook holds 87 entries when the page
is built.

### 8.1 The hero (home)

**Build.** The page opens on blank vellum. At the head, the
cartouche (§6.11) expanded: "Aveline & Cross" engrossed at
24px, the index of six landfalls with their leagues, the
mini-route empty but for the departure dot. In the chart
margin, the compass (§6.6) at rest on leg I's bearing, the
leagues counter (§6.7) at 0 with its source line. The hero
field: the rose (§6.1) at the sheet's heart, and on a fair
sheet the headline — "The coast, charted as you sail it"
(7 words, Fell 68px) — with the standfirst in Franklin:
*"Nine days, six harbours, two hundred and fourteen leagues
— and the chart drawn by the sailing."* The coastline is
present in the DOM, finished, wearing its masks.

**Scroll timeline.** t=0 (load, first visit): fonts race
(900ms cap) → the rose blooms (ring 500ms, points to
1100ms), the headline settles at t=300. The visitor begins
to scroll: the coastline sketches in stroke by stroke across
the first 60vh (`--ease-pen`), the wash breathing beneath at
0.92×. As the sketch completes, the route's first leg draws
out of Port Aveline's dot — and the reader is under way: the
counter begins its scrubbed count toward 38, the needle
trembles on 042°, the cartouche compresses at 140px. By the
first landfall's approach, the fog (§6.5) is already lifting
off The Gull Shoals. The visitor has been handed a blank
sheet, watched a coast exist, and set sail — the site's
entire argument, performed once, inside the first screen
and a half.

### 8.2 Mid-page: the pinned zoom at The Long Reach (home)

**Build.** The fourth landfall, the voyage's intricate
coast: a working estuary with two shoals (soundings 6 and 8
fathoms, the survey's shoalest) and the harbour the whole
voyage turns on. The stage (§6.4): a 200vh pin; the inset —
the estuary drawn at zoom resolution, its own fine coastline,
fourteen soundings of the whole coast's set thickest here,
a small rose — clipped in a brass-ruled frame. Beside the
stage (in flow, never inside the transform), the landfall's
copy: what the estuary asks of a navigator, why the ship
anchors mid-reach on the third night, what the 6-fathom
shoal means at low water. The place-name waits at its
enlarged size, unlettered.

**Scroll timeline.** The stage's top reaches the reading
line; the pin engages. Travel 0–70%: the chart glides closer
(`--ease-glide`, lerp 0.09) — scale 1→2.4, the view travelling
from the estuary's west cape to its harbour; the shoal
soundings grow legible as they enlarge, stroke weights
holding survey-true. Scale crosses 1.8: "The Long Reach"
letters itself in (§6.3) at its enlarged size, 110ms a
letter, while the route — arriving concurrently — latches
the landfall: the needle swings from 078° to 031° (1100ms,
one overshoot), the counter ticks to 118. Travel 70–100%:
the chart holds close while the copy is read — the reader
checks the prose's shoals against the chart's figures with
their own eyes, which is the zoom's whole purpose. The pin
releases; the inset rests in the flow, detailed and drawn,
and the route draws on toward Fog Anchorage. Claim,
instrument, arrival — the survey's order, performed at the
page's centre of gravity.

### 8.3 Conversion: entering the log (booking page)

**Build.** A surveyed page (§7): the chart complete, the
needle at rest, no fog anywhere. Centre: the logbook leaf
(§6.13) — head rule in brass, running head "THE LOGBOOK —
ENTRY № —" with the number honestly blank. The head line
reads: "The log holds 87 entries. The spring sailing is
entered up to the 4th of April." — the count printed from
the record, scarcity stated as a fact of the log with a
date on it (§12), not as pressure. Fields: name, direction
(email), the passage as the chart's own radio list — the
six landfalls with their leagues, "the whole voyage" first
(214 leagues) — and a notes line ruled for one sentence.
Submit, madder, full of the leaf's foot: *"Set it down in
the log."*

**Scroll timeline.** The page's two bearings (§6.16) rest
closed beneath the leaf. The visitor focuses the name
field: its rule inks in 260ms. They choose *the whole
voyage*: the radio dot fills madder, the passage line
prints "Your passage: the whole voyage — 214 leagues,
six landfalls." They mistype the direction without an @:
on submit nothing shakes and nothing fogs; the direction's
rule turns `--madder-deep` and the Log's line appears —
"That direction will not carry — the @ is missing, looks
like." — focus on the field, their writing intact.
Corrected, they submit: the button presses, reads
"Entering…" past 600ms, and then the leaf turns: the entry
stands set — "ENTRY № 88 — [their name], the whole voyage,
entered this day. The office writes to [their direction]
within two days." — and at t=300 the seal thuds onto it
(§6.9), madder on parchment, the initial theirs. The number
is the printed count + 1; the promise is the office's real
one; nothing on the page performed urgency, and everything
on it performed record-keeping — which is why the visitor
believes it.


## 9. Anti-slop — what makes THIS theme look cheap

Each failure is named as it appears in the wild, with its
cause and its cure. The gate (§10) tests for the blocking
ones.

1. **The pre-drawn chart.** The whole map rendered complete
   on load, with a token dash animation on the hero route
   only. *Cause:* the chart treated as a hero illustration
   rather than as the page's record. *Cure:* §1 clause 1 —
   nothing drawn ahead of the journey, anywhere, and §10's
   arrival audit samples unvisited territory for stray ink.
2. **The un-drawing chart.** Scrolling up erases the route,
   un-letters names, lightens hatching — the map "resetting"
   for the next performance. *Cause:* scrub state read live
   instead of latched. *Cure:* §1 clause 2 and §5's latch —
   the loop's target is maximum progress; ink is permanent.
3. **The progress bar in a false beard.** A straight red
   line down the margin, filling with scroll, with a little
   ship icon riding it. *Cause:* the route (§6.2) reduced to
   its progress function and stripped of its geography.
   *Cure:* the route winds through the page's actual
   geography, beside actual fair sheets; the gate checks the
   path passes every landfall with its declared clearance.
4. **Google-Maps cosplay.** Pins dropping, a pulsing blue
   dot, zoom buttons, a "satellite" toggle. *Cause:*
   reaching for the nearest map vocabulary instead of the
   theme's own. *Cure:* the theme's instruments are the rose,
   the needle, the sounding and the seal (§6). A pin is a
   confession that the chart was never surveyed.
5. **The gift-shop compass.** A rose that spins on hover, a
   needle that follows the pointer, bearings that point at
   nothing. *Cause:* the instrument treated as a toy.
   *Cure:* §6.6 — the needle points along the route object's
   bearings, trembles within ±1.5°, and is never the
   pointer's puppet.
6. **Brass lettering on vellum.** Captions, labels, even
   body copy set in `#C2A15C` on the pale ground because it
   "looks classy". *Cause:* 1.98:1 contrast nobody measured.
   *Cure:* §3 law 5 — brass never inks; brass text lives on
   `--night` or as `--brass-deep` display. The gate greps
   for brass-coloured text nodes on light grounds.
7. **Invented leagues.** Counters counting to numbers no
   route object declares; soundings scattered for rhythm;
   a footer total that matches nothing. *Cause:* figures
   authored per-element by different hands. *Cure:* §4's
   route object is the single source; §10 recomputes all
   three printings (chart, table, imprint) from it.
8. **The sticker seal.** A perfect-circle red badge, dropped
   on cards, buttons and banners alike, meaning "new" or
   "sale". *Cause:* the seal (§6.9) read as a shape instead
   of an act. *Cure:* the seal is irregular, initialled, and
   lands only on landfalls at the reader's own click; its
   census is in §10. A seal that sells is a forgery stamp.
9. **The menagerie.** Wash breathing, needle trembling,
   ship circling, roses blooming, names lettering, water
   sloshing, gulls flying — everything moving, all the time.
   *Cause:* ambient loops collected, not licensed. *Cure:*
   §5's three licensed loops; anything else that moves does
   so on a trigger, once, and rests.
10. **Dragon spray.** "Here be dragons" on three sections, a
    sea serpent in every margin, pirate copy throughout.
    *Cause:* the one joke (§6.10) mistaken for the theme.
    *Cure:* the delays line exists once, placed by data,
    in the surveyor's hand; the theme's register is the
    survey, not the tavern (§12).
11. **Franklin headlines.** Clean sans headings "for
    readability" over Fell body copy — the constitution (§3)
    inverted by habit. *Cause:* a builder's default theme
    leaking through. *Cure:* the chart speaks Fell, the
    annotations speak Franklin; the gate samples computed
    font families per role.
12. **Borrowed authority.** Prices, specifications or
    dashboards set in the soundings table's grammar (§6.14)
    or the logbook's (§6.13) to lend them the survey's
    credibility. *Cause:* the theme's instruments are
    handsome, so they get spent. *Cure:* §6.14's and §6.13's
    merges — those grammars belong to the survey and the
    record; other content uses §11's plain treatments or
    another theme.

## 10. Quality gate

Blocking items must all pass before the theme may be used
in a build. The gate is run by someone who did not build the
page (§15), against a production build, on a real device
profile — not the builder's monitor.

**Blocking**
1. **Ratchet test.** Scroll to the foot and back to the head
   at three speeds: the route, names, hatching, soundings
   and counters at the head show the *furthest* state, never
   a rewound one. (§1 clause 2, §5)
2. **Nothing-ahead audit.** At load and at 25% scroll,
   screenshot sampling of unvisited territory: no coastline,
   route, name or hatching ink below the latch (fog and
   blank vellum only). (§1 clause 1)
3. **Dead-JS test.** With JavaScript disabled, the page is
   the complete finished chart: coast drawn, names printed,
   table in ink, form submittable, seals as index checkboxes.
   (§1 clause 3)
4. **Figure-truth audit.** The route object is recomputed:
   legs sum to the printed total (38+39+41+40+56 = 214);
   the counter's landfall values, the table's totals row and
   the imprint's summary all match it; every depth quoted in
   prose exists in the sounding set.
5. **Arrival audit.** At each landfall fraction, the drawn
   route length matches `r × L` to the pixel, and the
   latch's ceremonies (name, needle bearing, counter
   cumulative, index state) agree with the object's row for
   that landfall.
6. **Contrast audit.** Every text pairing measured at rest:
   body 9.20:1, apparatus ≥5.27:1, madder text only ≥18px
   or in `--madder-deep`, teal body only as `--teal-deep`;
   **zero** brass text nodes on light grounds; footer brass
   lettering on night at 6.78:1.
7. **Watchdog drill.** With the shared loop artificially
   stalled, every armed element reaches its printed state
   via its fallback within its stated watchdog (hero 3000ms,
   route/names/hatching 1500ms, fog 1200ms, pin 4000ms,
   roll 2000ms).
8. **Zoom audit.** Through the pin (§6.4): inset strokes
   hold survey weight at full scale (vector-effect
   verified), the names letter only past 1.8×, focus is
   never inside the transformed layer, and the pin releases
   on schedule at all three viewport heights.
9. **Seal census.** Seals exist only at landfalls, minted
   only by the reader's click (plus the logbook's
   confirmation, §6.13); the index count equals the DOM
   seal count equals the stored count.
10. **Reduced-motion pass.** With `prefers-reduced-motion`,
    the page is the finished chart: route drawn, names
    printed, needle still and correct, no pin, no fog, no
    roll — all information present in the same order.

**Advisory**
11. The five-second test: a first-time visitor, shown the
    hero for five seconds, can say what is being charted
    and where the voyage goes.
12. The delays audit: *"Here be delays"* (§6.10) sits over
    the section the site's own data says is skipped, and
    nowhere else; its placement reason is recorded in the
    route object.

## 11. Component inventory

Every component a real Cartographer's Table site needs, with
its themed treatment. Components the theme refuses are listed
with the refusal's reason and the in-theme replacement — a
refusal without a replacement is a gap, and there are no gaps.

| Component | Treatment in this theme |
|---|---|
| Primary button | The seal button: `--madder` rectangle, parchment text, radius 0, press = 1px translate (§6.13). One per view. |
| Secondary button | Parchment ground, 1px `--ink` rule, ink text; hover rule doubles 200ms. |
| Text link | `--teal-deep` with a drawn rule (220ms); in the footer, vellum with a brass draw. |
| Navigation | The cartouche (§6.11). |
| Hero | The charting hero (§6.1) on home; a place's inset chart (§6.4 grammar, unpinned) on detail pages. |
| Cards | Landfall cards (§6.12), max 6 per page. |
| Data table | The table of soundings (§6.14) — the only table pattern; a survey's columns, in voyage order, unsortable by law. |
| Form fields | Log-ruled fields (§6.13): baseline rule inking on focus, SC labels, errors in `--madder-deep` in the Log's voice. |
| Radio / choice | Landfall radios (§6.13): dot + name + leagues from the route object. |
| Checkbox | A small square of chart border with an ink tick — a survey mark, not a box from an OS. Label in the Log's voice. |
| Select | **Refused** — a native dropdown is a machine part on a chart table. Replacement: landfall radio rows (§6.13) for ≤7 options; a listing page (§7) for more. |
| Tabs | **Refused** — a chart is read by travelling it, not by filing it. Replacement: landfalls + the cartouche index's scrollspy state (§6.11). |
| Accordion | The bearings accordion (§6.16) — the one licensed pattern, for questions of navigation. |
| Modal / dialog | **Refused as overlay.** Replacement: the unrolling (§6.18) to a dedicated page, or an in-flow inset chart (§6.4's resting state). The one exception — a legal consent that must interrupt — prints as a plain parchment panel in flow, unsealed and unadorned (§9.12's inverse). |
| Toast | **Refused.** Replacement: a log line — a printed entry at the head of the relevant section in the Log's voice (§12), persistent until dismissed by reading. |
| Tooltip | **Refused.** Replacement: the marginalia note — if a figure needs explaining, its source line prints beside it (§6.7), not on hover. |
| Progress bar | **Refused.** Replacement: the route itself (§6.2) and its miniature in the cartouche (§6.11). |
| Spinner | **Refused.** Replacement: the uncharted sheet (§6.18) with its 2000ms ceiling. |
| Pagination | **Refused** for the log and the table (the record is whole). For long listings: the bank index — a single link row ("Earlier voyages") to whole pages; a survey is not sliced. |
| Badge / tag | The sounding chip: a small `--vellum-deep` lozenge (radius 2px — charts are squared; the chip is a label pasted on, and pasted labels have corners) with the depth or state in Franklin 11px. Used for facts the chart must state ("Shoal — 6 fm"), never for marketing. |
| Alert / notice | A log entry panel: parchment ground, 2px `--madder-deep` left rule, the Log's voice, printed — never fogged, never auto-dismissing. Form errors use §6.13's lines. |
| Breadcrumbs | **Refused** — the needle (§6.6) and the cartouche index (§6.11) carry orientation; a crumb trail on a chart is a second, worse route. |
| Search | A chart index lookup: one log-ruled field (§6.13 pattern) on its own page; results as landfall cards (§6.12), each with its leagues from the reader's position. |
| Image | Inset charts and speckled fair-sheet frames in the chart's own drawing; photography, where a place must be *seen*, sits in a brass-ruled frame captioned as a view ("The Reach from the west cape — from the survey"), never under the route. |
| Footer | The chart-room footer (§6.17). |
| 404 | The uncharted page (§7). |
| Focus ring (cross-cutting) | `--ink` 2px, 2px offset on vellum grounds; `--vellum` 2px on `--night`. Never brass (1.98:1 is not a focus indicator), never madder (the route's colour is not a state). |
| Radius law (cross-cutting) | 0 everywhere — charts are cut square — except the instruments that are round by craft: the rose, the needle's pivot, the seal, the sounding dot. A builder who rounds a card has brought another theme's furniture. |

## 12. Content & copywriting voice

Two registers, kept apart as strictly as the palettes.

**The Cartographer** — the site's voice: the hand that draws
the chart and writes its names. Measured, wry, concrete;
speaks of coasts, weather, leagues and arrivals in sentences
that could be pencilled in a margin. Never sells; surveys.
Headlines are claims about the territory that the page then
verifies ("The coast, charted as you sail it" — verified by
the chart drawing itself, §8.1). Maximum 8 words for a display
line; a headline that needs a ninth word is two headlines
arguing.

**The Log** — the data's voice: soundings, leagues, bearings,
dates, form errors, empty states. Figures with their
provenance attached, always. The Log never rounds silently,
never exclaims, and — the register's signature — *the Log
admits*: a shoal is printed, a delay is lettered (§6.10), a
struck entry keeps its striking (§6.15).

**Headline style.** ✓ "The coast, charted as you sail it."
✓ "Six harbours, and every one of them sounded." ✗ "Embark
on the adventure of a lifetime!" ✗ "Welcome to Aveline &
Cross — award-winning voyages since 1998, book now!"
(a headline is not a brochure's first paragraph).

**Label style.** Labels are chart apparatus: noun + fact.
✓ "Leg III — 41 leagues, bearing 031°". ✓ "St. Cwyll's
Harbour — 77 leagues from departure". ✗ "Amazing stop #3!!"
✗ "You are here-ish" (the chart knows where you are, or it
says nothing).

**Error voice** (the Log, correcting an entry — never the
machine, never the visitor's fault). ✓ "That direction will
not carry — the @ is missing, looks like." ✓ "The log wants
a name for the entry." ✗ "Invalid email format." ✗ "Oops!
Something went wrong." (The Log admits specifics or it says
nothing.)

**Empty-state voice.** ✓ (an unsurveyed card, §6.12)
"Unsurveyed — the season is not yet charted." ✓ (a new
logbook) "The log opens with the spring sailing. Nothing is
entered yet, and nothing is invented for the space."
✗ "No results found." ✗ Any empty state that fills itself
with a decorative coastline and an apology — the uncharted
page (§7) is the model: stillness and a fact.

**Banned words & constructions.** "Adventure awaits",
"hidden gem", "off the beaten path", "bucket list", pirate
register in any form ("ahoy", "matey", "treasure" for
anything but a stated fact), exclamation marks in the Log's
register (the Cartographer may have one per page, and the
worked examples have none), percentages in progress contexts
(the route is the fraction, §6.2), "content" for the site's
own material (it is *the voyage*, *the chart*, *the log*),
and any league, depth or bearing without its source — the
route object — within the same figure's apparatus.

**Owned words.** Landfall, sounding, leagues, charted,
surveyed, the offing, to make (a port), to enter (in the
log), fair sheet, the chart table.

**Verbatim fixed strings** (builders do not paraphrase):
- The delays line: *"Here be delays"* (§6.10)
- The uncharted page's line: *"Terra incognita — this coast
  is not on the chart."* (§7)
- The form's submit: *"Set it down in the log."* (§6.13)
- The skeleton's status (visually hidden): *"The survey is
  under way."* (§6.18)
- The credit's close: *"Charted by hand, and checked against
  the coast."* (§6.17)

## 13. Full-page scroll choreography map

The home page (§8's site), top to bottom, six landfalls.
Every beat names what the visitor sees and what it is *for*;
a beat with no purpose is cut, not kept.

1. **Load.** Cartouche expanded, rose blooming, headline
   printed on blank vellum, counter at 0. *The sheet before
   the voyage: everything promised, nothing yet claimed.*
2. **First scroll — the coast exists (0–60vh).** The
   coastline sketches in; the first route leg draws out of
   the departure dot. *The visitor's hand is the surveyor's;
   the page teaches its physics by being used.*
3. **Leg I — The Gull Shoals (fraction 0.18).** Fog lifts
   ahead of the reading line; the name letters itself in on
   arrival; soundings pop as the route passes them; the
   counter ticks to 38 and the needle swings to 078°.
   *Arrival is a ceremony with instruments, not a fade.*
4. **Leg II — St. Cwyll's Harbour (0.36).** Hatching deepens
   over the first two regions behind the reader; the
   logbook entries (§6.15) for this harbour ink their heads
   as the route passes their fractions. *The record and the
   chart begin agreeing — the page's credibility compounds.*
5. **Leg III — The Long Reach (0.55).** The pin: the chart
   leans to 2.4× over the estuary, the name letters at
   enlarged size, the counter to 118, the needle to 031°.
   *The strait where attention is magnification — the
   page's centre of gravity.*
6. **Leg IV — Fog Anchorage (0.74).** The foggiest landfall:
   its fog lifts latest and slowest (its sweep runs at 1.3×
   the standard duration — the place is named for its
   weather, and the chart is honest about it). The delays
   section follows in this leg's lee; the ship doodle waits
   for dwellers. *Weather and wit, each placed by the data.*
7. **Leg V — Cape Meridian (1.00).** The final leg is the
   longest (56 leagues) and the chart knows it: the scroll
   is the sailing. On arrival the needle settles north, the
   counter latches 214, the cartouche index stands complete.
   *The voyage whole — every instrument agreeing at once.*
8. **The record (survey band).** The table of soundings
   (§6.14) in ink, its totals counted; the bearings (§6.16)
   beneath. *Belief, having been earned, is documented.*
9. **The imprint (footer).** The chart-room footer (§6.17):
   the summary prints the reader's own sailing ("You have
   charted 214 of 214 leagues"), the credit closes the
   sheet. *The chart signs itself, and the signature
   includes the reader.*

**Reverse pass.** Scrolling up: nothing un-draws (clause 2).
The needle stays on the furthest leg's bearing; fog stays
lifted; hatching stays deep. The reader going back up sails
a *known* coast — every name standing, every sounding
sounded — which is correct: they have surveyed it. The only
motion licensed on the reverse pass is the zoom (§6.4)
releasing its lens, and the cartouche re-marking the current
entry as landfalls pass upward.

**Jump scroll.** An anchor jump or a scrollbar drag to the
foot: every latch between here and there fires in order —
names print complete (no lettering queue), soundings settle,
hatching completes, the counter stands at the target
cumulative, the pin is skipped entirely (its inset renders
at rest). The page never makes a jumping visitor watch the
voyage they skipped; the chart simply stands surveyed, and
the footer's line notes the swift arrival (§6.17).

## 14. Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight (home) | ≤ 720KB | Of which photography ≤ 380KB (detail-page views are the spend; the home chart is drawn, not photographed) |
| Chart script | ≤ 34KB gz | The shared loop, route function, latch system and all §6 acts |
| Inline SVG (whole chart layer) | ≤ 60KB total | Coastline + hatching ≤30KB (§6.8), hero ≤14KB (§6.1), inset ≤18KB (§6.4), instruments ≤6KB (§6.6, §6.9) — overlapping budgets audited as one sum |
| Fonts | IM Fell English (400 + italic) + IM Fell English SC + Libre Franklin (400/500), subset, ≤ 110KB | `font-display: swap` with the §6.1 font race as the guard |
| Frame budget | ≤ 1.6ms of JS per frame in the shared loop | The loop computes values; CSS/compositor applies them. At most 3 transform layers live at once (chart depths) + 1 dash-offset write |
| Long tasks | None > 50ms after load | The chart SVG's parse is the risk; it is inline and capped above |
| CLS | 0.00 target, 0.02 ceiling | §3 law 3 (lettering moves no layout) and §6.18 (skeleton = real layout) are the mechanisms |

**Cut order** (when a build exceeds budget, cut in this
order — never improvise):
1. The unrolling transition (§6.18) — navigation goes plain.
2. Wash breathing (§6.1) — the sea stands still.
3. Hachure density (§6.8) halves — the regions keep their
   grain.
4. The delays ship (§6.10) — the lettering stays; the wit
   loses its animation before the survey loses anything.
5. The zoom's pan path (§6.4) — zoom becomes a straight
   scale on the harbour; the pin and the lettering stay.
6. Sounding pop rings (§6.7) — numerals deepen without the
   settle; the measurements stay.

**Never cut:** the printed-DOM guarantee (§1 clause 3), any
watchdog, the latch, the route object and its three
printings, the reduced-motion variants. A build that ships
the draw-on without its finished chart beneath has not saved
weight; it has removed the theme and kept its riskiest
surface.

## 15. Build-order checklist

1. **Static chart first.** The complete site with the chart
   fully drawn: every coast inked, every name printed, table
   in ink, form working, seals as index checkboxes. This is
   the page §10's dead-JS test will grade — build it as a
   deliverable, not as a by-product.
2. **Tokens & type.** §2's closed token list (grep-gated),
   §3's scale and five laws; the forbidden pairings (brass
   text on vellum, madder on night) encoded as lint rules,
   not intentions.
3. **The route object.** One data source for §6.2/§6.6/
   §6.7/§6.14/§6.17 — fractions, legs, bearings, soundings;
   the three-printings audit wired into CI before any
   element that prints a figure is built.
4. **Layout.** The chart layer, fair sheets, the chart
   margin, the reading-line constant shared by every
   trigger (§4).
5. **The shared loop + route function + latch.** §5's
   function implemented once, unit-tested against the
   printed fractions before any element consumes it; the
   latch (max-progress, permanent) proven by the ratchet
   test in miniature.
6. **The route (§6.2) and fog (§6.5)** — the spine and its
   weather; then hatching and grain (§6.8) keyed to them.
7. **Arrivals.** Names (§6.3), needle (§6.6), soundings and
   counters (§6.7) — the latch's ceremonies, in that order,
   each with its watchdog.
8. **The hero charting (§6.1)** — after §6.2, because the
   first leg's draw depends on the route's machinery.
9. **The pin (§6.4)**, its watchdog, its sub-400px and
   mobile abolitions; the inset authored at zoom resolution
   and audited for stroke weight.
10. **Seals (§6.9)** with persistence and the index's marks
    (§6.11); cards (§6.12) reading the same state.
11. **The record chain.** Table (§6.14), logbook entries
    (§6.15), bearings (§6.16) — in §7's order: claim,
    instrument, record.
12. **Form (§6.13)**, footer (§6.17), cartouche compression
    (§6.11) — the frame, last, because it is the part that
    may be cut (§14) and must therefore be the part least
    depended upon.
13. **Unrolling & uncharted sheets (§6.18); the 404 (§7)**
    shipped without the chart script's ceremonies.
14. **Reduced-motion pass** — every element's variant
    verified against §10.10, on a device, not a toggle in
    devtools alone.
15. **The gate (§10)** run by a non-builder; failures return
    to the step that owns them. The theme ships when the
    gate passes, not when the chart looks handsome in the
    builder's browser.
