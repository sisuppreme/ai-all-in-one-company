# 66. The Data Cartographer's Atlas — Expanded (v1 + v2)

> A dataset treated as an unmapped continent and published as a
> printed atlas: charts, soundings, marginalia and one honestly
> hatched blank where the data runs out. The site is not a
> dashboard wearing a costume. It is a bound volume of plates —
> a coastline that inks itself as you arrive, a brass expedition
> marker that travels the survey route as you scroll, depth
> soundings that are counted at the moment the survey passes
> them, and a Terra Incognita plate that itemises, in the
> atlas's own hand, everything the data does not cover.

**The theme's one law: the chart is printed before it is inked,
and the blank is surveyed too.** Every figure printed anywhere
on the page traces to one declared survey record (§6.17) and is
never printed without its station — a sounding belongs to a
place, a distance to a leg, a total to the record that sums it.
Inking, travelling, counting and turning are enhancements armed
over a finished, fully printed atlas: the DOM ships as the
complete volume, every pre-state is set by script in the same
frame that registers its watchdog, and no plate may ever be
left blank by a failed animation. The unsurveyed interior is
not a gap in the design — it is a plate, bounded, hatched and
labelled with what is missing. Gold leaf is spent in exactly
three places (the cartouche glint, the compass rose's north
point, the plate numerals) and hazard magenta on exactly six
marks (§6.17) — never a seventh. A build that prints a number
without its station, fills the blank to look complete, spends
the gold a fourth time, or strands a plate un-inked has broken
the law four ways.

---

## 1. Concept & world

Most data sites behave like instruments: dials, feeds, live
tiles. This theme behaves like a **survey**. The dataset —
whatever it truly is: a decade of coastal measurements, a
product's usage history, a research corpus, a city's records —
is treated as a continent that an expedition has crossed once,
carefully, and published as an atlas. The visitor does not
query the continent; they *travel* it. The home page is the
atlas opened at its chart: a coastline drawn from the data's
real edge, a route line joining nine surveyed stations, and a
facing page of marginal notes that change as the brass marker
reaches each station. Reading is travelling. Depth of scroll is
distance surveyed — the margin inks the route and counts the
miles as they pass under the reader's hand.

The world has four materials and no fifth: **paper** (the atlas
paper ground, deckled at the plate edges, ruled by fold lines),
**ink** (sepia for everything drawn or printed — coastlines,
contours, text), **teal** (the surveyed water: the coastline
itself, the route, everything the expedition has actually
reached), and two rationed luxuries — **gold leaf**, spent
three times only, and **hazard magenta**, spent six times only,
on the six marks where the data can wreck you. Nothing else is
permitted a saturated colour. The discipline is the luxury: a
real atlas is expensive because every plate was drawn by hand
and every colour cost a separate pass through the press.

The emotional register is *earned confidence*. A chart that
shows its soundings, names its surveyor, dates its survey and
hatched its blanks is making a stronger claim than any
dashboard: *we went there, we measured, and here is exactly
where our knowledge stops.* Premium here is not gloss; it is
the visible apparatus of trust — plate numbers, a register, a
colophon, an errata slip — applied to data. Every design
decision is tested against one question: *would a cartographer
sign this plate?*

**Best-fit sites and audiences.** Data-rich organisations whose
asset is a corpus and whose problem is trust: open-data
publishers, research institutes and observatories, archives and
digital libraries, climate/environmental monitoring bodies,
genealogy and records services, annual-report microsites for
data companies, and "state of the field" publications. The
audience is patient and literate — researchers, journalists,
analysts, funders, the professionally curious. They will check
the figures against the table (§6.13). The figures must
therefore reconcile, everywhere, to the one record (§6.17).

**When NOT to use it.** Not for anything live: a trading floor,
a status page, a feed — the atlas is a *published* survey, fixed
at its edition date, and pretending otherwise breaks the law.
Not for conversion-first marketing pages that must sell in the
first screen; the atlas converts at the commission form
(§6.14), after the continent has been travelled. Not for small
datasets — a continent needs a coastline; below roughly fifty
data points the survey apparatus becomes costume. Not for
audiences who need the answer in five seconds: the atlas's
honesty is slow by design, and §1's own escape hatch is the
sounding table (§6.13), which hurried readers are routed to.
And never for a client who wants the Terra Incognita filled in
"so it looks finished" — the blank is the theme's most valuable
plate, and a client who will not protect it should be sold a
different theme.

---

## 2. Palette

Five anchors from the original entry, unchanged. Derived tokens
are shades and tints of the anchors only — no new hues enter
the volume.

| Token | Hex | Role | Usage |
|---|---|---|---|
| `--paper` | `#EDE4CE` | Atlas paper — the page ground, plate faces | ~78% of every screen |
| `--paper-shade` | `#E2D5B4` | Paper in shadow: fold lines, plate-mark recesses, the facing page at rest | ~6% |
| `--ink` | `#4A3826` | Ink sepia — text, coastline under-drawing, rules, contour lines | ~10% |
| `--ink-soft` | `#7A6650` | Marginalia ink, captions, secondary print | ~3% |
| `--pencil` | `#9A8B74` | Pencil under-drawing (loader states only), hairlines | <1% |
| `--teal` | `#2F6F6A` | Coastline teal — the surveyed water: coast, route, soundings, links | ~2.5% |
| `--teal-deep` | `#1E4A46` | Teal at full survey: route already travelled, active states | <1% |
| `--magenta` | `#B23A6D` | Hazard magenta — the six hazard marks ONLY (§6.17 census) | <0.1% |
| `--gold` | `#C9A227` | Gold leaf — cartouche glint, rose north point, plate numerals ONLY | <0.1% |
| `--binding` | `#3A2C1E` | The binding — footer ground, the volume's spine and boards | footer only |

**Contrast, computed for this expansion** (against `--paper`
unless stated): `--ink` 9.6:1 (all text, all sizes); `--ink-soft`
5.4:1 (marginalia and captions at ≥13px only, never body copy);
`--teal` 5.1:1 (links, soundings, route labels — soundings are
figures, set at ≥11px tabular, and always paired with their
station name in `--ink`, so no figure depends on teal alone);
`--magenta` 4.7:1 (hazard labels at ≥12px, always paired with
the ✕ hatch glyph, never colour-alone); `--gold` 2.3:1 —
**ruled never-text**: gold is leaf, not ink; it appears only as
the cartouche glint, the rose's north point and plate numerals
set in Fraunces small caps at ≥14px where the numeral is
redundantly printed in `--ink` in the plate's caption line.
`--paper` on `--binding` 8.9:1 (footer text).

**Pairing rules.** Ink prints on paper; teal touches paper only
as line, figure or link — never as a filled panel (the water is
drawn, not poured). Magenta never sits beside gold on the same
plate. The binding appears once per page, in the footer
(§6.16): the volume closes at the bottom of every page, so the
footer is the back board, not a design surface.

**Dark-mode behaviour.** An atlas has no dark mode and this
theme refuses to invent one: the paper *is* the light source,
as a printed page is lit by the room. An OS dark preference is
answered with the identical printed volume, framed by a
`--binding` margin of 24px (the boards showing around the page)
— the book on a dark table. Any build that inverts the plates
to a "dark atlas" has broken the law: sepia on black is a
different, cheaper theme.

**The two censuses.** Gold: exactly three uses — §6.4's
cartouche glint, §6.2's compass-rose north point, plate numerals
(§6.9). Magenta: exactly six marks — the hazards named in
§6.17. Both censuses are grep-audited at the quality gate
(§10): a fourth gold or a seventh magenta fails the build.

---

## 3. Typography

Two families, exactly as the original entry declares.
**Fraunces** — display, cartouches, plate titles, all figures
(its old-style figures are the atlas's numerals; its optical
sizes let a plate title carry engraved weight). **Newsreader**
— body, marginalia, captions, the surveyor's hand (its italic
is a written hand, not a slanted print). No third family enters
the volume: soundings and coordinates, which a lesser build
would set in a mono, are set in Fraunces with tabular lining
figures engaged (`font-variant-numeric: tabular-nums`) — the
original entry's "small mono numbers" are satisfied by tabular
figures that align in columns like a printed sounding table,
without breaking the two-family law.

| Role | Font | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Cartouche title | Fraunces 72pt optical, 560 | clamp(2.6rem, 6vw, 4.4rem) / 1.02 | −0.01em | Inside §6.4 only; old-style figures |
| Plate title | Fraunces, 520 | 2rem / 1.1 | 0 | Opens every plate |
| Section head | Fraunces, 500 | 1.45rem / 1.2 | 0.005em | The facing page's voice |
| Body | Newsreader, 400 | 1.0625rem / 1.62 | 0 | Measure ≤62ch |
| Marginalia | Newsreader italic, 400 | 0.9375rem / 1.5 | 0 | `--ink-soft`; the surveyor's hand |
| Sounding / figure | Fraunces, tabular | 0.6875–0.8125rem / 1.3 | 0.02em | `--teal`; always with a station name |
| Coordinates | Fraunces, tabular | 0.8125rem / 1.4 | 0.03em | Degrees + minutes, never decimal-only |
| Plate numeral | Fraunces small caps, 600 | 0.875rem | 0.14em | `--gold` leaf over `--ink` caption (§2) |
| Register / form label | Newsreader, 500 | 0.8125rem / 1.4 | 0.06em, uppercase | The office's print, not the hand |

**Five type laws.** (1) *No naked numbers:* a figure never
prints without its station, leg or plate attached — "412 fm at
Deepwater Anchorage", never "412". (2) *Numerals are tabular
everywhere figures align* — sounding columns, the table (§6.13),
the register count — and old-style everywhere they flow in
prose. (3) *The hand annotates, the print carries:* marginalia
may comment, doubt and correct, but a fact lives in print
(Fraunces/Newsreader roman) or it does not live on the page.
(4) *Coordinates are spelled, not pasted:* "41°07′N 073°56′W"
with minutes, in the record's own datum line — never a raw
lat/long string from a database. (5) *Hazard labels are set in
print, not in the hand* — a warning is the office speaking, in
roman Newsreader with the ✕ glyph, never an italic aside.

---

## 4. Layout language

The page is a **bound spread**. The grid is 12 columns on a
1280px plate width, but the governing unit is the **plate mark**
— the engraved double-rule frame (§6.9) that bounds every chart
and image, inset 24px from the spread edge, with its plate
numeral at the lower right. Everything on a page is either
*inside a plate* (the chart, the surveyed water) or *on the
facing page* (the print that reads it: heads, body, marginalia).
The two never mix their materials: no body text crosses a plate
mark, no chart escapes one.

**Spread choreography.** The signature arrangement is §6.2's:
the chart plate pins centred in the left seven columns while
the facing page (right five columns) swaps its marginal notes
as the expedition marker reaches each station. Below the pinned
spread, the volume returns to single-column plates, one per
viewport, in survey order: sounding table, plates, the Terra
Incognita, the register form, the colophon. A **fold line** — a
1px `--paper-shade` rule with a 12px soft shadow — runs down the
centre of every spread-width section: the binding's crease,
felt rather than seen.

**Spacing rhythm.** Base unit 8px; plate padding 40px (the
plate mark's margin is the chart's neatline); section gaps are
one full "leaf" of 96–128px of unbroken paper — whitespace in
this theme is *uninked paper*, a material with a cost, never
leftover space. Marginalia sit in a dedicated 5-column rail or,
in single-column plates, in a right-hand margin column of
≤34ch width, keyed to the text by station numerals.

**Density rules.** One plate per viewport, never two charts
competing. Soundings on any plate: the record's own count, no
decorative extras (§6.5). Contour density is capped at the
record's three states (§6.3). The Terra Incognita (§6.6) is the
only plate allowed to be mostly empty — its emptiness is its
content, itemised in its margin.

**Deckle and grain.** Plate edges carry a deckled edge (an SVG
feTurbulence mask on the plate-mark frame, static, pre-rendered
— §14 budgets it once per plate, never per frame) and the paper
carries a faint laid-line texture (a repeating gradient at 3%
ink). Both are print, present with JS off, identical in the
reduced-motion variant: the paper is the paper in every state
of the build.

**Scale bar & rhumb lines.** Every chart plate carries its
scale bar in the plate mark's lower-left — a divided bar in
ink, "0 — 50 — 100 miles", its divisions computed from the
record's own coast so the bar and the route can never disagree
— and a rhumb-line network radiating faintly from the compass
rose (§6.2) at 8% ink: the straight-line bearings between
stations, drawn because a chart without bearings is a picture
of a coast, not an instrument for one. Both are print: static,
present with JS off, unchanged at every breakpoint except that
below 768px the bar re-divides to 25-mile units (a smaller
chart, a finer bar — the divisions follow the plate, as a real
engraver would re-cut them).

**Breakpoints in the layout language.** ≥1200px: true spreads,
pinned plate + facing page. 768–1199px: the spread stacks —
plate above, facing page below, the pin released (the marker
still travels, §6.2). <768px: single column, plate marks inset
12px, marginalia move below the passage they annotate, keyed by
the same station numerals.

---

## 5. Full motion system

One shared `requestAnimationFrame` loop drives every
scroll-scrubbed value on the page — marker position, contour
density crossfade, route inking, sounding counts, plate scale —
from a single lerped scroll progress (`--loop-lerp: 0.12`). The
loupe (§6.7) smooths its pointer follow at the original entry's
0.15 lerp on the same loop. Nothing animates off-loop except
the three licensed one-shot sequences (coastline inking,
cartouche engraving, page turn), each CSS/JS-timed, each
watchdogged, each armed over a fully printed DOM.

**Named easings — the surveyor's kit.** `--ease-ink`:
cubic-bezier(0.6, 0.05, 0.2, 1) — a nib's draw, fast wet start,
long dry finish (all stroke inking). `--ease-survey`: linear —
the marker travels at survey pace; easing a journey would lie
about distance. `--ease-settle`: cubic-bezier(0.2, 0.9, 0.25,
1.2) with a 2% overshoot — a brass instrument set down (marker
pauses, pin drops). `--ease-page`: cubic-bezier(0.7, 0, 0.3, 1)
— heavy paper turning (page transitions, note crossfades).
`--ease-bloom`: cubic-bezier(0.3, 0.7, 0.4, 1) — ink blooming
into sized paper (sounding pop-ins, note inking).

**Every motion term, translated or refused.** *Scroll-triggered
reveals:* plates ink as the marker's survey reaches them —
reveal is arrival, never a fade-up. *Scroll-driven/scrub:*
the route, the marker, the contour refinement (§6.3) and the
margin mile-counter are one scrub system. *Parallax:* paper,
hatching and marginalia drift at 0.94× / 0.97× / 1.0× — loose
plates in a bound volume, three rates only, never more (a
fourth rate is a screen effect, not a book). *Pinned sections:*
the survey spread (§6.2) only — one pin per page; a second pin
would make the volume feel like a website. *Masked reveals:*
the coastline inks inside its plate mark; the cartouche
engraves inside its frame — masks here are plate marks, not
clip-path tricks. *Blur-to-sharp:* refused for charts (a chart
is never out of focus; the loupe sharpens locally instead,
§6.7) and used once, for the pencil under-drawing resolving to
ink (§6.15). *Kinetic typography:* refused — print does not
move; the atlas's letters are set once, by the compositor.
*Marquee:* refused — atlases do not scroll sideways; the
plate index (§6.11) is a printed list. *Counters:* soundings
and surveyed miles count to their record values and stop
(§6.5) — a counter that overshoots its sounding has falsified
a measurement. *SVG line-draw:* the coastline, route, contours
and cartouche — the theme's native stroke. *Image scale-in-
frame:* plates settle 1.04 → 1.0 inside their plate marks
(§6.9). *Hover micro-interactions:* the loupe, the 2° page-lift
tilt on plates, the pin's hover shadow — instruments, not
sparkles. *Magnetic buttons:* refused — brass does not attract
the hand; buttons are printed register entries. *Custom
cursor:* refused absolutely (standing rule) — the system
cursor is the reader's own hand on the page. *Skeleton
loading:* pencil under-drawings that ink in (§6.15). *Page
transitions:* the page-turn (§6.10). *Ambient loops:* exactly
two licensed — the compass rose's slow drift (one rotation per
240s, §6.2) and the contour breathing at the deepest density
(§6.3); a third ambient loop fails the gate. *Reduced motion:*
the atlas lies open, fully inked (§6, per element).

**The watchdog law.** Every armed animation registers a named
watchdog (per element, 1200–3000ms) that forces the printed
final state if the sequence has not completed. The DOM ships
printed; scripts *rewind* to pre-states only in the same frame
they register the watchdog. A plate can therefore never be
stranded blank, half-inked or mid-turn — the failure mode of
this theme is a printed atlas, which is to say, no failure the
reader can see.

---

## 6. Signature elements

Eighteen elements: the original entry's ten, deepened, plus
eight page-family elements (navigation, station cards, the
sounding table, the commission form, the loader, the colophon
footer, the survey record itself, and the uncharted 404). Every
element carries the v1 build spec and the v2 layers. Every
figure named in any element traces to §6.17.

### 6.1 The self-inking coastline

- **What & why.** The hero chart's coastline draws itself in
  sepia ink over ~2.2s, with a slight hand wobble in the stroke,
  and the depth soundings pop in along it in survey order as the
  line passes them. It belongs because the atlas's first claim
  is that this shore was *surveyed*: the visitor watches the
  survey happen, once, at arrival — the map of the data is drawn
  by the act of reaching it.
- **Structure.** One inline SVG in the hero plate mark: the
  coastline as a single path (the record's shore, §6.17) drawn
  with `stroke-dasharray` driven from the shared loop; a
  duplicate path beneath at 0.5px offset and 18% ink supplies
  the hand wobble (two passes of the same nib, pre-rendered —
  the wobble is in the path data, never a per-frame filter).
  Soundings are real DOM text positioned on the plate, printed
  from the start; the inking script arms their pop-in only when
  it arms the stroke.
- **Motion spec.** Trigger: load, after the plate mark settles.
  Coastline: 2200ms `--ease-ink`, dashoffset scrubbed by the
  loop so a throttled tab still completes in order. Soundings:
  each pops at the moment the stroke's head passes its station —
  scale 0.6 → 1.0 with an ink-bloom (a 6px radial `--teal` wash
  fading over 380ms `--ease-bloom`), staggered by survey order,
  not by DOM order. The whole sequence runs once; revisits in
  the same session arrive at the printed chart (§6.15's rule).
- **States.** Un-inked (script-armed only, ≤1 frame) / inking /
  inked (rest) / re-entered (always inked — the survey is not
  re-run for a returning reader).
- **Content merge.** The coastline is the dataset's actual edge
  from the record; the soundings are the record's soundings at
  the record's stations. Remove the data and there is no shore
  to draw — the element cannot be pasted onto another site,
  because its path *is* the content.
- **Failure fallback.** Watchdog at 3000ms from arm: stroke
  snaps to fully drawn, all soundings printed. No-JS: the SVG
  ships fully drawn and the soundings printed — the script
  rewinds dashoffset only in the frame it registers the
  watchdog.
- **Reduced-motion variant.** The chart arrives printed: full
  coastline, all soundings, no draw, no bloom. The survey is
  presented as its published result.
- **Performance budget & mobile variant.** One path attribute
  update per frame; ≤0.25ms/frame. The wobble path is static.
  Mobile (<768px): the coastline path is the same data,
  simplified at build to 60% of its points (a smaller-scale
  chart is honestly less detailed, as real charts are); the
  draw shortens to 1600ms; sounding pop-ins become a single
  200ms fade of the whole set.
- **Choreography timeline (v2).** t=0 plate mark settles →
  t=120ms nib touches at Port Meridian → t=120–2320ms stroke
  draws under `--ease-ink`, soundings pop as the head passes
  (first at t≈300ms, last at t≈2260ms) → t=2400ms cartouche
  begins (§6.4) → watchdog deadline t=3000ms passes unused.
- **State matrix (v2).** *Rest:* inked chart. *Hover:* the
  loupe (§6.7) over the plate. *Focus:* the plate is a figure
  with a text alternative; not focusable itself. *Active:* a
  click drops a survey pin (§6.8). *Scrolled-past:* inked;
  never re-draws on re-entry. *Disabled:* n/a. *Touch:* tap =
  pin drop; no pop-in replay.
- **Breakpoints (v2).** ≥1200px: full path, soundings at 13px.
  768–1199px: full path, soundings 12px, the two most crowded
  roadsteads labelled by leader line. <768px: simplified path,
  soundings 11px, minor soundings (under 10 fm) printed only in
  the table (§6.13).
- **Edge cases & failure modes (v2).** *Slow network:* the SVG
  is inline — the survey starts before any image arrives.
  *Tab throttled mid-draw:* the loop's clamped delta completes
  the stroke in survey order, never out of order. *A dataset
  whose edge changes between editions:* the path is regenerated
  from the record at build; the edition line (§6.16) dates it —
  a redrawn coast is a new edition, announced as one.
- **Accessibility spec (v2).** `role="img"` with `aria-label`
  summarising the chart ("Chart of Veralia: 1,284 miles of
  coastline, nine stations, deepest sounding 412 fathoms at
  Deepwater Anchorage"). Soundings are real text, readable by
  assistive technology at all times — the pop-in is visual
  only. The draw is not announced; the chart's *content* is the
  plate's printed caption.
- **Tokens consumed (v2).** `--ink`, `--teal`, `--paper`,
  `--ease-ink`, `--ease-bloom`, `--loop-lerp` (0.12),
  `--dur-coast-draw` (2200ms), `--dur-watchdog-chart` (3000ms).

### 6.2 The expedition marker & the facing page

- **What & why.** A brass expedition marker travels the survey
  route across the pinned chart as the reader scrolls; at each
  of the nine stations it pauses with a small settle, and the
  facing page's marginal notes crossfade to that station's
  notes. It belongs because it makes the reader's position in
  the data a *place*: the notes belong to locations, and you
  travel to read them. It is the theme's central mechanism —
  scroll becomes survey.
- **Structure.** The spread (§4): chart plate pinned in the
  left seven columns (position: sticky inside a 340vh track),
  facing page in the right five. The marker is an SVG group (a
  brass disc, 14px, with a needle tail) positioned on the route
  path via `getPointAtLength` from the shared loop; the route
  itself inks in `--teal-deep` behind the marker as travelled
  distance (§5's progress). The facing page holds nine note
  blocks, all in the DOM, stacked in one margin frame; the
  active station's block is at full ink, the rest held at 0%
  only when script arms the swap. A compass rose (SVG, 32
  points) sits at the plate's lower-left corner; its north
  point is the build's second gold spend (§2 census).
- **Motion spec.** Trigger: scroll scrub across the spread's
  track. Marker travel: `--ease-survey` (linear) against the
  lerped progress — distance is honest. At each station
  (progress thresholds from the record's leg miles ÷ 1,284):
  the marker settles 260ms `--ease-settle`, a ring pulses once
  from the station point (scale 1 → 2.2, opacity 0.5 → 0,
  600ms), and the facing page crossfades 420ms `--ease-page` to
  that station's notes. Route inking: the travelled portion
  draws in `--teal-deep` at the marker's exact pace; the margin
  mile-counter (§6.5's sibling readout in this spread) counts
  the surveyed miles to the current leg's figure.
- **States.** Travelling / settled at a station (notes live) /
  at the terminus (Saltmarsh Reach: the marker rests, the
  facing page shows the survey's closing note) / scrolled past
  the spread (marker parked at the terminus; the plate unpins
  complete).
- **Content merge.** The notes are the stations' own records —
  what was found, measured and doubted at each place (§6.17).
  The marker does not decorate the chart; it *reads* it, and
  the facing page is the chart's own margin, printed by the
  surveyor at the place it describes.
- **Failure fallback.** Watchdog per station swap at 1500ms:
  if a crossfade has not completed, the incoming notes snap to
  full ink. No-JS: all nine note blocks print in sequence down
  the facing page (a longer page, a complete atlas) and the
  marker rests at Port Meridian with the route fully inked.
- **Reduced-motion variant.** No pin, no travel: the spread
  unstacks, the route prints fully inked, the marker is printed
  at each station as a small brass dot beside its notes — nine
  short spreads, all notes visible, nothing swapped.
- **Performance budget & mobile variant.** One
  `getPointAtLength` + one transform per frame; ≤0.3ms/frame.
  768–1199px: the pin releases; plate above, notes below, the
  marker still scrubs through the plate's own scroll passage.
  <768px: the spread becomes a single column — chart, then the
  nine note blocks in survey order with the marker printed at
  each; scrub travel is cut entirely (the second cut in §14's
  order) and the route ships inked.
- **Choreography timeline (v2).** Spread enters → plate pins →
  progress 0–1 across the track: marker departs Port Meridian →
  at each leg threshold, settle 260ms + ring 600ms + notes
  crossfade 420ms (overlapping, in that order) → terminus:
  marker settles for good, closing note inks → track ends,
  plate unpins with the survey complete.
- **State matrix (v2).** *Rest (before spread):* marker at Port
  Meridian, first notes printed. *Hover:* loupe over the plate
  (§6.7); the marker ignores the pointer — it answers the
  scroll, not the hand. *Focus:* the note blocks are readable
  in DOM order regardless of the visual swap; a "stations" list
  in the plate caption gives keyboard readers the same journey
  as links (§6.11). *Active:* clicking a station point jumps
  the scroll to that leg (the one licensed jump — travel by
  index). *Scrolled-past:* terminus state persists.
  *Disabled:* n/a. *Touch:* identical scrub; no hover ring.
- **Breakpoints (v2).** ≥1200px: pinned spread as specified.
  768–1199px: unpinned stack, scrub retained within the plate.
  <768px: printed column, scrub cut, all notes visible.
- **Edge cases & failure modes (v2).** *Reader scrolls back
  up:* the marker retraces the route in reverse and the notes
  swap back — the survey is re-walkable; travelled ink stays
  inked (ink does not unwrite), only the marker moves.
  *Jump-scroll (keyboard End, scrollbar drag):* the loop's
  lerp carries the marker to the true position within ~600ms;
  intermediate stations' notes never flash — only the landing
  station's notes ink. *A station with no notes in the record:*
  the facing page prints the surveyor's honest line — "No note
  was entered at this station" — a blank in the margin, admitted
  (never filled with generated colour).
- **Accessibility spec (v2).** The visual swap never gates
  content: all note blocks are in the accessibility tree in
  survey order (visually-hidden-when-inactive is forbidden —
  inactive blocks are `visibility`-swapped only after the
  active block is announced, and a no-JS/reduced-motion reader
  gets all nine in sequence). The marker and rose are
  `aria-hidden`; the plate caption lists the nine stations with
  their soundings as text. Focus order follows the DOM: chart
  caption, then notes in survey order.
- **Tokens consumed (v2).** `--teal`, `--teal-deep`, `--gold`
  (rose north point — census № 2), `--ink`, `--ink-soft`,
  `--paper-shade`, `--ease-survey`, `--ease-settle`,
  `--ease-page`, `--loop-lerp` (0.12), `--dur-station-settle`
  (260ms), `--dur-note-swap` (420ms), `--dur-watchdog-notes`
  (1500ms).

### 6.3 Refining contours

- **What & why.** The chart's interior contour lines redraw at
  finer intervals the deeper the reader scrolls — three density
  states crossfaded — as if the survey improves under attention.
  It belongs because it is the theme's epistemology drawn:
  knowledge here is not binary; the longer you study the
  continent, the better surveyed it becomes, and the chart says
  so in its own line-work.
- **Structure.** Three SVG contour sets for the hero plate's
  interior, generated at build from the record's elevation
  model: coarse (40m interval), surveyed (20m), fine (10m).
  All three are inline paths grouped by state; the loop
  crossfades opacity between adjacent states across the scroll
  band. Contours are `--ink` at 22% — hatching-weight, never
  competing with the coastline's full ink.
- **Motion spec.** Trigger: scroll depth across the hero
  spread. State boundaries at 33% and 66% of the spread's
  track; each crossfade spans 12% of the track on either side,
  driven by the lerped progress — no thresholds pop. At the
  fine state only, the licensed ambient breath: contour opacity
  oscillates 20% ↔ 24% on a 9s sine — the paper settling, not
  the land moving.
- **States.** Coarse (arrival) / surveyed (mid-spread) / fine
  (deep) / reversed (scrolling up re-coarsens symmetrically —
  attention withdrawn is survey withdrawn, the one element
  whose scrub is fully reversible).
- **Content merge.** The contours are the record's interior
  relief; their three densities are the record's three survey
  passes (§6.17 names them: the 1st, 2nd and 3rd surveys). The
  refinement is not a zoom effect — the margin note at the fine
  state changes to cite the third survey by name and date.
- **Failure fallback.** Watchdog at 2000ms after the spread is
  entered: if the loop has not run, the surveyed (middle) state
  prints at full opacity — the published chart's own density.
  No-JS: the middle state only, printed. A chart at its
  published density is never a failure.
- **Reduced-motion variant.** The middle state, static, at all
  depths. The margin note cites the second survey. No breath.
- **Performance budget & mobile variant.** Three pre-rendered
  path groups; per-frame cost is two opacity writes, ≤0.1ms.
  Mobile (<768px): two states only (coarse → surveyed); the
  fine set is not shipped (the third cut in §14's order) — a
  small chart is honestly a coarser chart.
- **Choreography timeline (v2).** Spread progress 0.27 →
  coarse begins fading → 0.33 surveyed at full → 0.60 fine
  begins → 0.66 fine at full, margin note swaps to the third
  survey → deepest band: breath begins (9s sine) → reverse
  scroll mirrors the sequence exactly.
- **State matrix (v2).** *Rest:* state follows depth. *Hover:*
  inside the loupe (§6.7) contours resolve one state finer
  than the page's current state — the instrument out-surveys
  the eye. *Focus:* n/a (decorative layer over a labelled
  figure). *Active:* n/a. *Scrolled-past:* the last state
  holds; the breath stops off-screen (the loop skips
  off-viewport plates). *Disabled:* n/a. *Touch:* identical
  scrub.
- **Breakpoints (v2).** ≥1200px: three states. 768–1199px:
  three states, crossfade bands widened to 16%. <768px: two
  states, no breath.
- **Edge cases & failure modes (v2).** *A record with only one
  survey pass:* the element collapses honestly — one density,
  no refinement, and the margin note says the interior "awaits
  its second survey" (which also feeds §6.6's itemisation).
  *Very tall hero plate:* state bands are computed from the
  spread track, not the plate, so density follows reading
  depth, not geometry. *Print:* the middle state prints (§14's
  print rule) — paper gets the published chart.
- **Accessibility spec (v2).** The contour groups are
  `aria-hidden` decoration over the labelled chart figure; the
  survey state is conveyed in text by the margin note ("Interior
  shown at the third survey, 10-metre intervals"), which updates
  in the DOM at each state change — a screen-reader user is
  told the density, not shown the lines.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--ease-ink`,
  `--loop-lerp` (0.12), `--contour-coarse` (40m),
  `--contour-surveyed` (20m), `--contour-fine` (10m),
  `--dur-watchdog-contours` (2000ms).

---

### 6.4 The engraving cartouche

- **What & why.** The atlas's title lives inside an engraved
  cartouche — a scrollwork frame that strokes itself in last,
  after the coastline, its corners finishing with a single
  gold-leaf glint. It belongs because an atlas's title is not a
  headline dropped on a chart; it is part of the plate,
  engraved by the same hand, and the order of the entrance —
  shore first, soundings second, title last — is the survey's
  own order of work.
- **Structure.** An SVG frame (four corner scrolls, two side
  cartouches, a title ribbon) drawn as stroked paths around a
  DOM title in Fraunces. The gold glint is a single 26px leaf
  segment on the ribbon's crest — the build's first gold spend
  (§2 census). The title text is real DOM text from first paint;
  only the frame is armed for drawing.
- **Motion spec.** Trigger: the coastline (§6.1) completing, or
  t=2400ms, whichever is first. Frame strokes in over 800ms
  `--ease-ink`, corners in reading order (top-left, top-right,
  bottom-right, bottom-left — the engraver's circuit); at
  t≈760ms the glint passes once across the crest leaf (a
  gradient sweep, 240ms) and the gold then rests — leaf does
  not twinkle.
- **States.** Printed (rest — frame fully engraved) / engraving
  (the one entrance) / revisited (printed; the engraving is
  never re-run in-session).
- **Content merge.** The cartouche carries the atlas's actual
  title and edition line ("Sheet I · Survey of Veralia · the
  Meridian Coast Survey") — the plate's imprint, not a logo
  lockup. On inner pages the cartouche shrinks to a printed
  running head (§6.11); the full engraving belongs to the
  opening plate alone.
- **Failure fallback.** Watchdog at 3200ms from load: frame
  snaps to fully drawn. No-JS: frame ships drawn.
- **Reduced-motion variant.** Frame printed, glint static — the
  leaf is simply there, as leaf is on paper.
- **Performance budget & mobile variant.** Four path draws on
  one loop pass, entrance only; zero steady-state cost. Mobile:
  the side cartouches simplify to plain rules at build (a
  small plate carries a plainer frame); the circuit and glint
  are unchanged.
- **Choreography timeline (v2).** Coastline completes (or
  t=2400ms) → t+0 corners begin → t+800ms frame complete →
  within it, t+760–1000ms the glint sweeps the crest once →
  rest. Watchdog deadline t=3200ms passes unused.
- **State matrix (v2).** *Rest:* engraved. *Hover:* none — a
  title frame is not an instrument. *Focus:* the title is the
  page's `<h1>`; the frame is `aria-hidden`. *Active:* n/a.
  *Scrolled-past:* engraved. *Disabled:* n/a. *Touch:* as rest.
- **Breakpoints (v2).** ≥1200px: full scrollwork. 768–1199px:
  full scrollwork, frame narrows with the plate. <768px:
  simplified side rules, corners retained (the corners are the
  signature; the sides are the ornament).
- **Edge cases & failure modes (v2).** *A long title (a
  translated edition):* the ribbon is sized by the title's
  measure at build; the frame paths are generated per edition,
  never stretched — a stretched cartouche is a broken plate.
  *The coastline watchdog firing first:* the cartouche still
  engraves on its own trigger; the two sequences are
  independent by design, so one failure cannot cascade.
- **Accessibility spec (v2).** The `<h1>` is plain DOM text,
  first in the reading order; the SVG frame is decorative and
  hidden from assistive technology. The edition line is text,
  not part of the engraving.
- **Tokens consumed (v2).** `--ink`, `--gold` (crest leaf —
  census № 1), `--ease-ink`, `--dur-cartouche` (800ms),
  `--dur-glint` (240ms), `--dur-watchdog-cartouche` (3200ms).

### 6.5 Counting soundings & the surveyed-mile readout

- **What & why.** Sounding numbers count up to their true
  depths as the survey passes them, and the margin readout
  counts the surveyed miles as the marker travels — every
  counter in the atlas is a measurement being taken at the
  moment of passing, and it stops dead at the record's figure.
  It belongs because counting is this theme's data verb: a
  number that arrives by counting was *measured*; a number that
  fades in was merely displayed.
- **Structure.** Sounding figures are DOM text with tabular
  Fraunces figures (§3); the count is a text update from the
  shared loop, interpolating 0 → the record value across the
  survey's passage of that station, staggered 60ms per sounding
  along the coast (the original entry's stagger, preserved).
  The mile readout is a fixed margin instrument in the survey
  spread: "Surveyed: NNN of 1,284 miles", the denominator
  always printed — a count without its total is a naked number
  and breaks §3's first law.
- **Motion spec.** Trigger: the marker (§6.2) or the inking
  head (§6.1) passing the sounding's station. Duration: 700ms
  per sounding, linear count (a lead line pays out evenly —
  easing a depth would falsify it), the final value held with a
  120ms ink-settle (weight shift via a brief `--teal-deep`
  pass). Miles: continuous with the marker, integer miles,
  updating at most every 80ms (a readout that flickers tenths
  is an instrument pretending to precision it does not have).
- **States.** Uncounted (printed at true value until armed —
  the DOM value is always the record value; the count is armed
  by zeroing the *display* only) / counting / held (rest, the
  overwhelming majority of the read) / re-passed (never
  recounts — a sounding once taken is taken).
- **Content merge.** The counts are the record's soundings and
  the record's leg miles (§6.17), taken at the record's
  stations. The counter is the lead line; remove the survey and
  there is nothing to count.
- **Failure fallback.** Watchdog per sounding at 1600ms from
  arm: display snaps to the record value. No-JS: all values
  printed at their record figures — the count is enhancement
  over print, by the law.
- **Reduced-motion variant.** No counts: values print at their
  record figures as the station enters, miles readout updates
  in whole-leg steps (nine updates, one per station) instead of
  continuously.
- **Performance budget & mobile variant.** Text writes only for
  soundings in their 700ms window (≤9 concurrent worst case);
  ≤0.15ms/frame. Mobile: the mile readout moves from the margin
  into the plate's caption line; soundings count identically.
- **Choreography timeline (v2).** Survey head reaches a station
  → its soundings begin, staggered 60ms apart in survey order →
  each counts 700ms linear → final figure settles 120ms in
  `--teal-deep` → held. Mile readout: continuous across the
  spread, arriving at each leg's cumulative figure exactly as
  the marker settles at its station (the two instruments agree
  — §10 audits it).
- **State matrix (v2).** *Rest:* held at record value. *Hover:*
  a held sounding under the loupe shows its station's full
  entry (name, depth, plate) in the margin (§6.7). *Focus:*
  soundings are text; the readout is a `role="status"` updated
  at station granularity only (never per-mile — a live region
  that chatters is a broken instrument). *Active:* n/a.
  *Scrolled-past:* held. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: margin readout. 768–1199px:
  readout in the plate caption. <768px: readout in the caption;
  soundings under 10 fm do not count (they print) — a small
  chart takes fewer soundings aloud.
- **Edge cases & failure modes (v2).** *Fast scroll through
  the spread:* soundings whose stations are jumped over snap
  to held via their watchdogs — the survey is complete behind
  the reader even if unwatched. *A record value of 0* (a dry
  station, a becalmed leg): the counter prints 0 and holds —
  zero is a measurement, set in full ink, never dimmed.
  *Rounding:* counts land on the record's exact printed figure
  (412, never 411.6 mid-count shown to a reader — intermediate
  values are integers only).
- **Accessibility spec (v2).** Counting is visual only: the
  DOM/AT value of every sounding is its record figure from
  first paint (the visual count is a `aria-hidden` overlay
  clone where implementation requires one, or the live region
  is suppressed during counting). The mile readout announces
  at stations only: "Station 5, The Narrows. 620 of 1,284
  miles surveyed."
- **Tokens consumed (v2).** `--teal`, `--teal-deep`, `--ink`,
  `--dur-sounding-count` (700ms), `--dur-sounding-stagger`
  (60ms), `--dur-watchdog-sounding` (1600ms), `--loop-lerp`
  (0.12).

### 6.6 The Terra Incognita plate

- **What & why.** One plate in the volume is a hatched, empty
  region: the part of the continent the data does not cover.
  Entering it, the hatching draws itself in and the label inks
  — *Terra Incognita* — beside a marginal itemisation of exactly
  what is missing and why. It belongs because it is the theme's
  law made visible: the atlas's honesty is a place you visit,
  bounded and surveyed like any other plate, not a footnote
  apology.
- **Structure.** A full plate inside its plate mark: the
  continent's outline with the interior region bounded by a
  dashed survey line (the boundary of knowledge is itself
  surveyed), filled with engraved hatching (two SVG pattern
  densities, coast-ward finer). The margin carries the
  itemisation as a printed list — in the worked record: the
  interior's elevation model, all records after the survey's
  closing year, and the Saltmarsh Reach's upper waters, each
  with its reason (§6.17). The area figure prints with the
  plate: "36,632 of 96,400 square miles — 38 per cent — not
  surveyed."
- **Motion spec.** Trigger: scroll into view. The boundary
  dashes draw in 900ms `--ease-ink`; the hatching fades in as
  two passes (coarse 600ms, fine 600ms delayed 200ms — the
  engraver's two plates); the label inks last, 380ms
  `--ease-bloom`. Nothing inside the region ever moves again:
  the blank does not perform.
- **States.** Printed (rest) / hatching (entrance only) /
  revisited (printed). There is no hover state inside the
  region — the loupe (§6.7) over Terra Incognita shows the
  hatching at the same density: there is nothing finer to
  resolve, and the instrument says so.
- **Content merge.** The plate's content *is* the dataset's
  documented absence — its boundary from the record's coverage
  map, its itemisation from the record's own exclusions list
  (§6.17). It cannot be decorated into fullness without
  breaking the law; §9 lists a filled blank as the theme's
  first anti-slop failure.
- **Failure fallback.** Watchdog at 2200ms: hatching and label
  snap to printed. No-JS: the plate ships hatched and labelled.
- **Reduced-motion variant.** The plate arrives printed —
  boundary, both hatch densities, label, itemisation. Identical
  information, no drawing.
- **Performance budget & mobile variant.** Two pattern fills
  and one path draw, entrance only; zero steady-state cost.
  Mobile: the itemisation moves below the plate (as all
  marginalia do <768px, §4); the hatching's fine pass is cut —
  a small blank is a coarser blank.
- **Choreography timeline (v2).** Plate enters → t=0 boundary
  begins → t=900ms boundary closed → t=200–800ms coarse hatch →
  t=800–1400ms fine hatch → t=1400–1780ms label inks →
  itemisation prints with the section rise → rest, permanently.
  Watchdog deadline t=2200ms passes unused.
- **State matrix (v2).** *Rest:* hatched, labelled, itemised.
  *Hover:* none inside the region; the itemisation's entries
  hover as ordinary text links to the record (§6.17) where a
  fuller exclusion note exists. *Focus:* the plate's caption
  and the itemisation are the focusable content, in that order.
  *Active:* n/a. *Scrolled-past:* printed. *Disabled:* n/a.
  *Touch:* as rest.
- **Breakpoints (v2).** ≥1200px: plate + margin itemisation.
  768–1199px: plate full width, itemisation beneath in two
  columns. <768px: itemisation beneath, single column, fine
  hatch cut.
- **Edge cases & failure modes (v2).** *A dataset with no
  documented gaps:* the plate may not be faked — if the record
  declares no exclusions, the plate is omitted and §6.17 states
  "no exclusions declared" in the record itself (an absence of
  honesty-apparatus is itself printed). *A gap that closes in a
  later edition:* the new edition re-surveys the plate, and the
  colophon (§6.16) notes the change — blanks close by edition,
  never silently.
- **Accessibility spec (v2).** The plate is `role="img"` labelled
  with its full claim ("Terra Incognita: 36,632 square miles,
  38 per cent of the continent, not surveyed; the margin lists
  what is missing"). The itemisation is ordinary text, first
  class — a screen-reader user gets the honesty in words, not
  in hatching.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--pencil`,
  `--paper`, `--ease-ink`, `--ease-bloom`, `--dur-hatch`
  (1400ms), `--dur-watchdog-incognita` (2200ms).

---

### 6.7 The loupe

- **What & why.** Hovering a chart plate sharpens and enlarges
  the chart beneath the pointer by ~12% inside a soft circular
  loupe, and the contour lines inside it resolve one density
  state finer than the page's (§6.3). It belongs because
  inspection is the cartographer's instrument: the chart rewards
  the loupe the way paper rewards a real one — by having more
  in it than the naked eye was given.
- **Structure.** A circular lens (220px desktop) clipped over a
  duplicate render of the plate's SVG at 1.12× scale, registered
  to the base plate; the lens carries a thin `--ink` rim and a
  brass handle tick at its lower right — drawn, not skeuomorphic
  chrome. The fine contour set inside the lens is the record's
  own next density (§6.3), pre-rendered; the loupe reveals
  survey that exists, never invents detail.
- **Motion spec.** Trigger: pointer over a plate. The lens
  follows the pointer on the shared loop at the original
  entry's 0.15 lerp — a hand's weight, not a cursor's snap.
  Lens fades/scales in 180ms `--ease-settle` on entry, out in
  140ms on exit. Inside the lens, the finer contours crossfade
  in over 240ms.
- **States.** Absent (rest) / entering / inspecting / leaving.
  Over Terra Incognita (§6.6): the lens appears but resolves
  nothing finer — same hatching, slightly larger: the honest
  loupe.
- **Content merge.** The loupe magnifies the plate it is over —
  chart, soundings, plate-mark frames (§6.9) — and nothing else
  on the page; over body text it does not appear (print is read,
  charts are inspected). What it shows is the record's finer
  survey, so the merge is literal: attention reveals data.
- **Failure fallback.** The lens is pure enhancement: if the
  duplicate render fails, no lens appears and the plate is
  untouched. No watchdog is needed because nothing is ever
  hidden by its absence — the base plate is complete. No-JS:
  no loupe; the fine contour state is reachable by scroll
  (§6.3) instead.
- **Reduced-motion variant.** No loupe. The fine contour state
  and full sounding labels are printed at the plate's deepest
  scroll state (§6.3's variant), so the information the loupe
  would have shown is on the page without the instrument.
- **Performance budget & mobile variant.** The duplicate plate
  is one extra SVG render, composited by transform only;
  ≤0.4ms/frame while active, zero at rest. Touch / <768px: no
  loupe (a finger is not a lens) — a tap on the plate toggles
  the plate's fine state in place, with the same 240ms
  crossfade.
- **Choreography timeline (v2).** Pointer enters plate →
  t=180ms lens settled at pointer → follow at 0.15 lerp →
  t≈240ms fine contours resolved inside → pointer leaves →
  t=140ms lens gone. No other beats: an instrument has no
  ceremony.
- **State matrix (v2).** *Rest:* absent. *Hover:* inspecting.
  *Focus:* keyboard focus on a plate's caption link offers the
  same fine state as a page-level toggle ("Show the third
  survey") — the loupe's content is never pointer-exclusive.
  *Active:* a click through the lens drops a pin (§6.8) at the
  lens's centre point. *Scrolled-past:* lens dismissed.
  *Disabled:* n/a. *Touch:* tap-toggle fine state, as above.
- **Breakpoints (v2).** ≥1200px: lens 220px, 1.12×. 768–1199px:
  lens 180px, 1.10×. <768px: no lens; tap-toggle.
- **Edge cases & failure modes (v2).** *Pointer at the plate's
  edge:* the lens clamps inside the plate mark — a loupe does
  not hang off the chart. *Two plates on screen (listing
  pages):* one lens, bound to the plate under the pointer;
  crossing plates re-registers the duplicate render.
  *High-DPI:* the duplicate renders from the same vector data —
  the magnification is real resolution, never upscaled blur.
- **Accessibility spec (v2).** The lens is `aria-hidden`; its
  revealed content (fine contours, full sounding labels) is
  available to assistive technology in the plate's caption and
  the table (§6.13) at all times. The keyboard toggle is a real
  button with `aria-pressed`, labelled per plate. Magnification
  never carries information that exists nowhere else — §10
  audits this.
- **Tokens consumed (v2).** `--ink`, `--teal`, `--ease-settle`,
  `--loupe-lerp` (0.15), `--loupe-scale` (1.12),
  `--loupe-size` (220px), `--dur-loupe-in` (180ms).

### 6.8 The survey-pin click

- **What & why.** Clicking the chart drops a brass survey pin
  at the point — a 300ms drop with a tiny bounce — and inks a
  marginal note beside it recording the coordinates and the
  figure found there. It belongs because it lets the reader
  *join the survey*: their findings are entered in the atlas's
  margin, on the plate itself, in the surveyor's own format.
- **Structure.** A pin (SVG brass marker, the marker of §6.2
  at rest) placed in plate coordinates; the note is a real
  marginalia block appended to the plate's margin rail, set in
  the hand (Newsreader italic, §3) with the print's figures:
  coordinates spelled per §3's fourth law, the nearest
  station's sounding, the leg it falls on. Pins persist for the
  session in a list the reader can clear ("Strike the pins" —
  a printed control, §6.11's register style).
- **Motion spec.** Trigger: click/tap on a chart plate (not
  through an interactive child). Pin drop: 300ms
  `--ease-settle` with a 2px bounce at contact and a single
  ring pulse (as §6.2's station ring, 500ms). The note inks in
  over 420ms `--ease-bloom`, letter by letter in effect but as
  one opacity pass — handwriting that types itself
  character-by-character is a screen effect, refused.
- **States.** No pins (rest) / dropping / entered (pin + note
  held) / struck (cleared: pins lift in 160ms, notes stay in
  the margin struck through with a single ink rule — the atlas
  corrects, it does not erase, §3's third law).
- **Content merge.** The note's figures are computed from the
  record at the pin's position — interpolated depth between the
  leg's two stations, labelled as an estimate ("by dead
  reckoning between The Narrows and Cape Verity") — the pin
  produces *data about the data*, in the record's own terms,
  never a generic tooltip.
- **Failure fallback.** The pin is an annotation layer over a
  complete chart: if scripting fails, no pins, and the chart
  loses nothing. The estimate computation is client-side from
  the printed record; a failed computation prints the nearest
  station's sounding alone, labelled as such.
- **Reduced-motion variant.** The pin appears placed (no drop,
  no bounce, no ring); the note prints in one step.
- **Performance budget & mobile variant.** Pins are DOM nodes,
  capped at 12 per plate (the thirteenth strikes the first —
  a margin can hold only so many entries, and the cap is
  printed in the plate caption). Mobile: tap drops the pin; the
  note appears beneath the plate with the other marginalia.
- **Choreography timeline (v2).** Click → t=0 pin begins drop →
  t=300ms contact, bounce, ring starts → t=300–720ms note inks
  in the margin → pin at rest, note held. Strike: pins lift
  160ms, notes ruled through in 240ms.
- **State matrix (v2).** *Rest:* no pins. *Hover:* a placed pin
  shows its note's first line in the margin (highlighting the
  entry, 160ms). *Focus:* pins are focusable in placement
  order; focus shows the note as hover does; Delete strikes
  the focused pin. *Active:* the dropping state. *Scrolled-
  past:* pins persist on their plate. *Disabled:* pinning is
  disabled on the Terra Incognita plate — you cannot survey
  what the atlas has declared unsurveyed; the plate's caption
  says so. *Touch:* tap = drop; long-press on a pin strikes it.
- **Breakpoints (v2).** ≥1200px: notes in the margin rail.
  768–1199px: notes in the margin rail, rail narrows to 30ch.
  <768px: notes beneath the plate, in drop order.
- **Edge cases & failure modes (v2).** *Pin dropped in the
  water vs the interior:* both are legal — a water pin reports
  a sounding estimate, an interior pin reports "ashore: no
  sounding taken — the survey was a coast survey", an honest
  non-figure instead of an invented one. *Pin at a hazard
  mark:* the note prints the hazard's warning first, in print
  (§3's fifth law), before its figures. *Session restore:*
  pins are session-only by design — an atlas's pencil marks do
  not survive the closing of the book, and the caption says so.
- **Accessibility spec (v2).** Each pin is a button with an
  accessible name ("Survey pin 3: 41°07′N 073°56′W, estimated
  87 fathoms by dead reckoning"); its note is a list item in
  the margin's pin list, associated by `aria-describedby`.
  Dropping a pin announces once via a polite live region.
  Keyboard: with a plate focused, arrow keys move a crosshair
  in 1′ steps and Enter drops the pin — the survey is fully
  operable without a pointer.
- **Tokens consumed (v2).** `--gold` is NOT used (pins are
  brass-toned `--ink`/`--teal-deep`, never leaf — the census
  holds), `--teal-deep`, `--ink-soft`, `--ease-settle`,
  `--ease-bloom`, `--dur-pin-drop` (300ms), `--dur-note-ink`
  (420ms), `--pin-cap` (12).

### 6.9 Plate-mark image frames

- **What & why.** Every image in the volume sits inside an
  engraved plate mark — a fine double-rule border with a plate
  number at its lower right — and settles from 1.04 to 1.0 as
  the plate mark finishes engraving on entry. It belongs
  because in an atlas a figure is not an illustration pasted
  into text; it is a numbered plate, cited by number in the
  text that refers to it, and the frame is the citation made
  visible.
- **Structure.** A `<figure>` wrapped in the plate-mark frame
  (two nested rules, 1px and 3px apart, `--ink` at 60% and
  100%), the plate numeral in gold small caps at the lower
  right — the build's third gold spend (§2 census) — and a
  caption in print: "Plate IV. The Narrows, from the third
  survey." The image itself is a real `<img>` with full `alt`,
  printed dimensions, and the record's subject. In-text
  references cite the numeral ("…the lee shore at the Verity
  (Plate V)"), so frame and text are one apparatus.
- **Motion spec.** Trigger: scroll into view. The frame's outer
  rule strokes in over 500ms `--ease-ink` while the image
  settles 1.04 → 1.0 over 700ms `--ease-settle`, the two
  overlapping so the plate is *mounted* as it arrives. The
  numeral inks last (120ms). Once mounted, a plate never
  re-mounts.
- **States.** Unmounted (armed only) / mounting / mounted
  (rest). Hover: the page-lift — the plate tilts ≤2° toward
  the pointer's side (the original entry's page lifting at the
  corner), transform from the shared loop, settling back over
  500ms on exit.
- **Content merge.** The plate's subject is a record subject —
  a station's view, the survey's instrument, the coast at a
  named point — captioned with its plate number, station and
  survey. A stock photograph in a plate mark is the theme's
  most detectable lie (§9): if the record has no image for a
  subject, the plate is an engraved chart detail instead, or
  there is no plate.
- **Failure fallback.** Watchdog at 1800ms: frame snaps drawn,
  image at 1.0. No-JS: frames printed, images at rest scale.
  Image failed to load: the plate mark holds the caption and an
  engraved hatch panel with the plate's subject line printed —
  a plate whose impression failed is still a cited plate, never
  a broken-image icon.
- **Reduced-motion variant.** Plates arrive mounted: frame
  printed, image at 1.0, no tilt on hover.
- **Performance budget & mobile variant.** Entrance cost is one
  stroke draw + one transform per plate; images lazy-load below
  the fold with reserved aspect boxes (no layout shift — a
  shifting plate is a misbound page). Mobile: the double rule
  becomes a single 1px rule (a small plate is more plainly
  bound); tilt is cut (touch has no hover); settle retained at
  1.02 → 1.0.
- **Choreography timeline (v2).** Plate enters → t=0 outer rule
  begins → t=0–700ms image settles → t=500ms rule closes →
  t=500–620ms numeral inks → mounted. Watchdog deadline
  t=1800ms passes unused.
- **State matrix (v2).** *Rest:* mounted. *Hover:* ≤2° lift.
  *Focus:* a plate linked to its detail page (§7) shows the
  lift plus a `--teal` outer rule — focus is a state of the
  frame, not an outline pasted on it. *Active:* pressed plates
  flatten (0°) in 90ms before navigation — the page is set down
  before it is turned (§6.10). *Scrolled-past:* mounted.
  *Disabled:* n/a. *Touch:* no tilt; tap follows the link.
- **Breakpoints (v2).** ≥1200px: double rule, full treatment.
  768–1199px: double rule, tilt ≤1.5°. <768px: single rule, no
  tilt, settle 1.02 → 1.0.
- **Edge cases & failure modes (v2).** *Portrait plates:* the
  mark sizes to the image's true aspect from the record — a
  cropped-to-fit plate is a trimmed plate, and trimming is
  falsification in this world. *A plate cited before it appears
  (text on an earlier page):* the citation stands; atlases cite
  plates the reader has not yet reached, and the plate index
  (§6.11) resolves it.
- **Accessibility spec (v2).** Real `alt` written as a plate
  description ("Plate V — Cape Verity and its lee shore, looking
  north; the hazard ✕ at the point"). The frame and numeral are
  decorative (`aria-hidden`); the caption is the figure's
  accessible name and carries the numeral in text.
- **Tokens consumed (v2).** `--ink`, `--gold` (plate numeral —
  census № 3), `--paper`, `--ease-ink`, `--ease-settle`,
  `--dur-plate-mount` (700ms), `--dur-watchdog-plate` (1800ms),
  `--tilt-max` (2deg).

---

### 6.10 The page-turn transition

- **What & why.** Moving between pages is turning the atlas's
  page: a fold shadow crosses the spread — a moving gradient
  with a soft crease highlight — over ~600ms as one plate gives
  way to the next. It belongs because the binding is the
  navigation in this world; a reader who has travelled a
  continent should feel the leaf turn when they leave it, not
  watch a screen wipe.
- **Structure.** A full-spread overlay: a linear gradient band
  (paper-shade → transparent) with a 2px crease highlight at its
  leading edge, sweeping right-to-left for forward navigation,
  left-to-right for back — the turn has a direction, like a
  real leaf. The destination page is rendered beneath from its
  printed state (§6.15's rule: destinations arrive printed; only
  their hero survey may arm, and only after the turn completes).
- **Motion spec.** Trigger: an internal navigation click.
  t=0–600ms `--ease-page`: the band crosses; at the crossing's
  midpoint (t≈300ms, the leaf vertical) the route swaps beneath
  it. Total perceived interruption ≤600ms, watchdogged at
  900ms: a turn that has not completed forces the destination
  fully printed and the overlay removed.
- **States.** Closed (rest — no overlay) / turning / turned.
  Browser back/forward: the turn plays in the matching
  direction; a history jump of more than one leaf plays a
  double-width band (two leaves at once) at the same 600ms —
  the gesture scales, the duration does not.
- **Content merge.** The turn is made of the volume's own paper
  — the band is `--paper-shade` deepening to the fold shadow of
  §4 — and it turns *between plates*: navigation points in this
  theme are plates and stations (§6.11), so the metaphor never
  has to stretch over a settings screen or a checkout.
- **Failure fallback.** Watchdog at 900ms as above. No-JS:
  plain navigation, complete pages — the turn is the one
  element whose absence costs the theme nothing structural.
  A failed route (404) turns onto §6.18's uncharted plate,
  which is printed complete: the turn never strands a reader
  between leaves.
- **Reduced-motion variant.** No turn: plain navigation. The
  destination's plate arrives printed. The binding is honoured
  by the colophon's edition line instead of by a gesture.
- **Performance budget & mobile variant.** One composited
  gradient transform; ≤0.2ms/frame for 600ms. Mobile: the band
  narrows (a smaller leaf) and the duration shortens to 450ms;
  on low-power devices (§14's detection) the turn is cut first.
- **Choreography timeline (v2).** Click → t=0 band enters at
  the fore-edge → t≈300ms leaf vertical, route swaps →
  t=600ms band exits at the binding → destination at rest,
  its hero survey free to arm. Watchdog ceiling t=900ms.
- **State matrix (v2).** *Rest:* closed. *Hover:* n/a. *Focus:*
  focus moves to the destination's `<h1>` at the swap — never
  left on a turned-away page. *Active:* turning. *Scrolled-
  past:* n/a. *Disabled:* during the 600ms the outgoing page's
  controls are inert (a turning leaf cannot be written on).
  *Touch:* identical; swipe-back gestures keep the browser's
  own behaviour — the theme does not hijack platform gestures.
- **Breakpoints (v2).** ≥1200px: full-spread band. 768–1199px:
  band at 70% width. <768px: 450ms, band at 55% width.
- **Edge cases & failure modes (v2).** *Rapid double
  navigation:* the second click during a turn is queued to the
  destination (the leaf finishes its turn; atlases are not
  riffled). *External links:* no turn — leaving the volume is
  closing the book, marked instead by the colophon's imprint
  (§6.16). *Anchor links within a page:* no turn; the marker
  (§6.2) is the within-page traveller.
- **Accessibility spec (v2).** The overlay is `aria-hidden`; the
  route change is announced by the destination's heading and
  the document title ("Plate IV — The Narrows · The Data
  Cartographer's Atlas"). Focus management as in the state
  matrix. The turn is never the sole signal of navigation.
- **Tokens consumed (v2).** `--paper-shade`, `--paper`,
  `--binding`, `--ease-page`, `--dur-page-turn` (600ms),
  `--dur-watchdog-turn` (900ms).

### 6.11 Atlas masthead & plate-index navigation

- **What & why.** The volume's furniture: a slim masthead
  carrying the atlas's title as a printed running head, the
  edition line, and the plate index — the list of plates and
  stations by which the whole continent is navigated. It
  belongs because an atlas is navigated by its index, not by a
  menu: the reader looks up a place and turns to it.
- **Structure.** A `<header>` with a real `<nav>`: left, the
  running head (small cartouche, §6.4's frame at print size,
  no engraving animation — furniture is printed, not performed);
  centre/right, the index entries — Plates, Stations, Soundings
  (§6.13), Terra Incognita (§6.6), Commission (§6.14), Colophon
  — set as a printed list with plate numerals. Below 1200px the
  surveyed-mile readout (§6.5) joins the masthead's right edge
  (the margin cannot hold it). A compass mark (the rose at 24px,
  north point in gold — the same census № 2 spend, at furniture
  size) orients the head.
- **Motion spec.** Entrance: none — the masthead is printed
  from first paint (furniture precedes ceremony; the coastline
  inks beneath it). Scroll: the masthead is sticky with a paper
  ground that gains its fold shadow after 40px of scroll
  (200ms `--ease-page`); it never hides on scroll — an atlas's
  running head is on every page, including while you read it.
  The current plate's index entry gains a `--teal` rule as the
  reader's survey reaches it (scrollspy reading the same
  progress as §6.2's marker — one source of "where am I").
- **States.** Rest: all entries printed, current entry ruled.
  Hover: an entry's numeral inks to full `--ink` (from
  `--ink-soft`) over 160ms. Focus: as hover plus the standard
  2px `--ink` focus outline. Active (current plate): teal rule
  + `aria-current="page"`. Disabled: an unpublished plate's
  entry prints in `--pencil` with no link — "Plate VIII, in
  preparation" — an honest furniture entry for a leaf not yet
  bound.
- **Content merge.** The index entries *are* the volume's
  contents — plates, stations, the table, the blank, the
  register — named as the colophon (§6.16) names them. Nothing
  decorative is indexed; nothing indexed is decorative.
- **Failure fallback.** The masthead is static HTML and CSS:
  it cannot fail into invisibility. No-JS: identical, minus the
  scrollspy rule (current-ness is lost, navigation is not).
- **Reduced-motion variant.** Identical, minus the fold-shadow
  transition (the shadow is simply present after 40px).
- **Performance budget & mobile variant.** Zero per-frame cost
  (scrollspy via IntersectionObserver). Mobile (<768px): the
  index moves behind a printed "Index" toggle opening a
  full-width paper panel (the index leaf) with the same entries
  at reading size; the mile readout stays visible in the
  masthead — instruments outrank furniture.
- **Choreography timeline (v2).** Load → masthead printed →
  scroll 40px: fold shadow settles 200ms → plate boundary
  crossed: old rule fades 300ms as the new rule inks → footer
  reached: the Colophon entry rules itself.
- **State matrix (v2).** *Rest:* printed, current ruled.
  *Hover:* numeral inks. *Focus:* as hover + outline. *Active:*
  current plate — teal rule, `aria-current`. *Scrolled-past:*
  n/a (sticky). *Disabled:* pencil entry, no link. *Touch:*
  entries ≥44px targets; the index leaf opens on tap.
- **Breakpoints (v2).** ≥1200px: full head, index inline.
  768–1199px: index inline, edition line drops to the footer
  only. <768px: Index toggle + leaf panel; mile readout in the
  head.
- **Edge cases & failure modes (v2).** *A volume that grows
  past nine plates:* the index paginates as a printed list with
  its own leaf (§11's pagination) rather than shrinking type —
  an index that cannot be read is a binding error. *Deep link
  to a station:* the scrollspy rules the station's plate on
  arrival; the marker (§6.2) is placed at that station, so
  furniture and instrument agree.
- **Accessibility spec (v2).** Landmarks: `<header>`, `<nav
  aria-label="Plate index">`; `aria-current` on the active
  entry; the Index toggle is a button with `aria-expanded`.
  Skip link printed as the masthead's first element, visible on
  focus, `--ink` on `--paper` (9.6:1).
- **Tokens consumed (v2).** `--paper`, `--paper-shade`, `--ink`,
  `--ink-soft`, `--pencil`, `--teal`, `--gold` (rose mark —
  census № 2, shared with §6.2), `--ease-page`,
  `--dur-rule-ink` (300ms).

### 6.12 Station entry cards

- **What & why.** The nine stations as a printed index of entry
  cards — one per station: its name in Fraunces, its sounding,
  its leg's miles and days, its plate numeral, and the first
  line of its marginal note. It belongs because the atlas needs
  its finding apparatus in card form for listing pages (§7):
  the stations are the dataset's entries, and a reader browsing
  them is reading the survey's table of contents with the
  figures attached.
- **Structure.** A `<ul>` of `<li>` cards on `--paper` with a
  single-rule frame (the plate mark's plainer sibling, §6.9);
  each card is one link to the station's detail (§7). The card's
  sounding is set as §6.5's figure style; hazard stations
  (Breaker Shoal, and any station whose note carries a warning)
  print the ✕ glyph and the hazard's name in `--magenta` —
  magenta on a card is a *mark reference*, counted in §6.17's
  census only where the mark itself appears on the chart; the
  card cites the mark, it does not re-spend it (§10 audits the
  distinction).
- **Motion spec.** Cards print in with the section rise (400ms,
  staggered 60ms in survey order — the index is read in the
  order the coast was travelled). Hover: the card lifts its
  page corner ≤2° (as §6.9) and its sounding inks to
  `--teal-deep` over 200ms. No count animation on cards: the
  index states figures, the survey (§6.5) takes them.
- **States.** Rest: printed. Hover: lift + sounding deepens.
  Focus: the card's link shows lift + a `--teal` frame rule.
  Active: flatten 90ms, then the page turn (§6.10).
  Scrolled-past: printed. Disabled: a station whose detail page
  is unpublished renders linkless, its note's first line
  replaced by "The entry for this station is in preparation" —
  the index admits its stubs.
- **Content merge.** Every field is a record field (§6.17):
  name, sounding, leg miles, leg days, plate, note's first
  line. The nine cards' leg miles sum to the record's 1,284 in
  the index's footer line, printed: "Nine stations · eight legs
  · 1,284 miles" — the index adds itself up, in public.
- **Failure fallback.** Cards are static print with a CSS
  hover; the rise is loop-armed with a 1200ms watchdog per
  section. No-JS: printed, no rise.
- **Reduced-motion variant.** No rise, no stagger, no lift —
  the index lies printed; hover deepens the sounding only.
- **Performance budget & mobile variant.** Grid: 3 columns
  ≥1200px, 2 at 768–1199px, 1 below 768px. Tilt math is the
  shared loop's, one hovered card at a time. Mobile: cards full
  measure; the note's first line is cut to the name + figures
  (a small index is a denser index, honestly).
- **Choreography timeline (v2).** Section enters → cards rise
  in 60ms survey-order stagger → rest → hover: sounding deepens
  200ms, corner lifts → leave: settle 500ms → press: flatten
  90ms → turn (§6.10).
- **State matrix (v2).** *Rest:* printed. *Hover:* lift +
  deepen. *Focus:* lift + teal rule. *Active:* flatten, turn.
  *Scrolled-past:* printed. *Disabled:* linkless, stub line.
  *Touch:* no lift; tap follows.
- **Breakpoints (v2).** ≥1200px: 3-col, note line shown.
  768–1199px: 2-col, note line shown. <768px: 1-col, figures
  only.
- **Edge cases & failure modes (v2).** *A tenth station added
  in a new edition:* the index's footer line is computed from
  the record at build — it can never disagree with the cards
  above it (§10's two-printings audit covers cards vs table
  vs record). *A station with a tied sounding:* ties print as
  measured; the index does not rank stations — an atlas is not
  a league table.
- **Accessibility spec (v2).** Each card is one link with one
  accessible name ("Station 7, Breaker Shoal — sounding 3
  fathoms — hazard: the shoal — Plate V"). The ✕ and magenta
  are redundant with the printed word "hazard" — never
  colour-alone. Contrast: `--ink` on `--paper` 9.6:1;
  `--ink-soft` note lines 5.4:1 at ≥14px.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--ink-soft`,
  `--teal`, `--teal-deep`, `--magenta` (citation only — see
  census note), `--ease-settle`, `--dur-card-rise` (400ms),
  `--dur-watchdog-cards` (1200ms), `--tilt-max` (2deg).

---

### 6.13 The sounding table

- **What & why.** For the reader who needs the survey plain: a
  true data table of the nine stations — leg miles, sailing
  days, the station's sounding, its plate — with a totals row
  carrying the record's 1,284 miles and 86 sailing days. It
  belongs because an atlas that cannot be read as a table is a
  picture book; the table is the theme's honesty in its most
  checkable form, and §1 routes hurried readers here.
- **Structure.** A semantic `<table>` with `<caption>` ("The
  nine stations of the Meridian Coast Survey — Sheet I"),
  `<th scope="col">` heads, station names as `<th scope="row">`,
  tabular Fraunces numerals throughout (§3). The totals row is
  a `<tfoot>` separated by a double rule. The sounding column
  carries **no total** — depths are point measurements and are
  not summed; the table's footnote prints why, with the
  survey's own count: "Depths are point soundings and are not
  summed. The survey took 214 soundings in all (§6.17)." The
  footnote is the element's signature: the table refuses a
  false total in public.
- **Motion spec.** The table does not animate — no rise beyond
  the section's print entrance. Row hover: the row's ground
  lifts to `--paper-shade` over 180ms and a brass margin tick
  appears at the row's station (the marker's furniture form).
  That is all. The restraint is the spec: the one element a
  hurried reader uses is the one element that never performs.
- **States.** Rest: printed. Hover (row): lift + tick. Focus:
  a row's station link shows the tick plus the standard
  outline. Active: n/a. Scrolled-past: printed. Disabled: a
  provisional station (a build mid-edition) prints its figures
  in `--ink-soft` with the word "provisional" in its note cell
  — the table admits the state of its evidence rather than
  hiding the row.
- **Content merge.** The table *is* §6.17's station half in
  reading order — same figures, same order, same totals — and
  §10's audit re-adds its columns against the record and the
  cards (§6.12). Table, cards and chart are three printings of
  one survey.
- **Failure fallback.** None required: static HTML, CSS hover.
  No-JS: identical. This element is the fallback's fallback —
  if every instrument on the page failed, the survey would
  still be fully readable here.
- **Reduced-motion variant.** Identical, minus the row-lift
  transition (instant) — the table was already the stillest
  element on the page.
- **Performance budget & mobile variant.** Zero JS. Mobile
  (<768px): the table becomes a stacked station list — each
  station a block with its figures in definition-list layout,
  same order, same totals, same footnote; no horizontal scroll
  is ever permitted (a table you must pan is a table lost at
  sea).
- **Choreography timeline (v2).** Section print entrance →
  table at rest → row hover: lift 180ms, tick inks → leave:
  lift releases 240ms. Nothing else, ever.
- **State matrix (v2).** *Rest:* printed. *Hover:* lift + tick.
  *Focus:* cell link tick + outline. *Active:* n/a.
  *Scrolled-past:* printed. *Disabled:* provisional rows
  softened and labelled. *Touch:* tap on a row holds the lift
  for 600ms (a finger's reading pause), no tick.
- **Breakpoints (v2).** ≥1200px: full 5-column table.
  768–1199px: 4 columns (plate folds into the station cell as
  a sub-line). <768px: stacked station list.
- **Edge cases & failure modes (v2).** *A zero in the table*
  (a leg of 0 days — a station surveyed from the anchorage):
  prints 0 in full ink; absence of travel is still a figure.
  *Print:* the table is the print stylesheet's centrepiece —
  full grid, totals, footnote, on white; the atlas is a printed
  thing and prints like one (§14).
- **Accessibility spec (v2).** Real table semantics with
  caption and scoped headers; the totals row is a `<tfoot>`
  with `scope="row"`. Screen readers receive the survey in its
  most native form. Contrast: `--ink` on `--paper` 9.6:1, on
  the lifted `--paper-shade` rows 8.7:1.
- **Tokens consumed (v2).** `--paper`, `--paper-shade`, `--ink`,
  `--ink-soft`, `--teal`, `--ease-page`, `--dur-row-lift`
  (180ms).

### 6.14 The commission form & its register entry

- **What & why.** The atlas's conversion: a reader with a
  dataset of their own commissions a chart — the Atlas Office
  will survey it and bind it as a plate. The form is styled as
  a page of the Survey Register: fields for the commissioner's
  name, the dataset's "coast" (what it measures), its extent
  (records, years), and the sheet desired. On submit, the
  confirmation is a register entry — "Entered as Commission
  № 313" — and the register's printed count, shown in the
  preamble before the reader writes a word, was 312: the
  number is a kept promise, derived from the record (§6.17),
  never a surprise.
- **Structure.** A real `<form>` with native validation
  semantics, enhanced never replaced: labelled ruled inputs
  (the register's ruled lines — a bottom rule in `--ink` at
  40%, focusing to full ink with a `--teal` station tick at the
  label). The preamble prints the register line: "The Register
  holds 312 commissions. Yours will be № 313." On success
  (JS-intercepted, or a server-rendered page without JS) the
  form region is replaced by the entry: a ruled register block
  with the commission's number, its coast and extent as
  entered, and the office's line — "The Office will write
  within seven days with the survey's terms."
- **Motion spec.** Field focus: rule inks to full over 200ms,
  label's tick appears. Submit: the form dims to 65% over
  250ms while the entry is written — the "entering" state shows
  the pencil under-drawing shimmer (§6.15) on the button, never
  a spinner. Success: the entry prints in with a 450ms rise
  `--ease-page`; a fresh rule draws beneath the entry number
  (300ms `--ease-ink`) — the clerk underlining the new line.
  Error: the offending field's rule goes `--magenta`? — **no:**
  magenta is hazards only (§2 census). Errors print in the
  office's voice beneath the field in `--ink`, with a ✳ mark
  in `--ink` — the register corrects in ink, and the error is
  a sentence, not a colour.
- **States.** Rest: register page printed, № 313 promised.
  Focus: per-field inking. Active (entering): form at 65%,
  fields disabled, button shimmering. Success: the entry,
  ruled and held. Error: fields marked ✳ with printed reasons,
  focus moved to the first error, values preserved.
  Scrolled-past: an in-flight entry completes regardless of
  scroll. Disabled (office closed — endpoint down): the form
  prints the register's note, "The Register is closed today;
  commissions resume tomorrow", and holds the reader's entries
  in the fields — unsubmitted, unsent, unlost.
- **Content merge.** The form's extent field is the record's
  own unit language (records as soundings, years as surveys);
  its sheet choices are the atlas's plate types; its
  confirmation number is the record's register count + 1; and
  on success the masthead's register count (§6.11) and the
  colophon (§6.16) both read 313 — one figure, three printings,
  audited (§10).
- **Failure fallback.** Watchdog at 4000ms on submission: if no
  response, the form restores from its 65% state and prints
  "The entry could not be written — your words are still here",
  values intact, submission token idempotent so nothing is
  entered twice. No-JS: native post, server-rendered entry,
  same number derivation.
- **Reduced-motion variant.** The entry prints instantly; no
  dim, no shimmer, no rule draw — the register simply gains a
  line. Errors print without transition.
- **Performance budget & mobile variant.** The form's JS is
  ≤5KB gz, deferred, the page's only non-loop script besides
  §6.15's. Mobile (<768px): single column, ruled inputs full
  measure, the submit control fixed at the form's foot within
  its own box; the preamble's promise stays above the first
  field — a promise scrolled away from is a promise weakened.
- **Choreography timeline (v2).** Focus field → rule inks
  200ms → submit → form dims 250ms → entering shimmer →
  response → entry rises 450ms → rule draws beneath № 313,
  300ms → register counts (§6.11, §6.16) now read 313 →
  rest. Watchdog ceiling 4000ms.
- **State matrix (v2).** *Rest:* register printed, № 313
  promised. *Hover:* field rule at 70%. *Focus:* rule full +
  tick + outline. *Active:* entering state. *Scrolled-past:*
  waits; entry completes. *Disabled:* register-closed note,
  values held. *Touch:* identical; fields ≥48px.
- **Breakpoints (v2).** ≥1200px: two-column register (coast +
  extent side by side), measure 44rem. 768–1199px: single
  column, 38rem. <768px: full measure, submit at the form's
  foot.
- **Edge cases & failure modes (v2).** *An extent of zero or
  absurd (a joker enters 10⁹ records):* the office's voice
  corrects without scolding — "A coast of one record is still
  a coast; enter what you hold" — and extents beyond the
  register's largest printed commission are accepted but
  entered as "extent as stated, unverified": the register
  records claims as claims. *Duplicate commission (same coast,
  same extent):* the entry prints with a marginal note —
  "A second commission on this coast — corroboration, not
  duplication." *A name left blank:* the register enters the
  commission as "Commissioner unnamed" rather than refusing —
  registers record what happened.
- **Accessibility spec (v2).** Native labels, visible, `--ink`
  (9.6:1); errors via `aria-describedby` plus an
  `aria-live="polite"` summary in the office's words; the
  success entry is an `aria-live` region announcing "Entered
  as Commission № 313" once. Focus management: first error on
  failure, entry heading on success. The ✳ is paired with the
  printed word "Correct this" — never mark-alone.
- **Tokens consumed (v2).** `--paper`, `--paper-shade`, `--ink`,
  `--ink-soft`, `--teal`, `--ease-page`, `--ease-ink`,
  `--dur-watchdog-form` (4000ms), `--register-next` (313).

### 6.15 Pencil under-drawings — loader & skeleton

- **What & why.** Loading in the atlas is the draughtsman's
  first pass: regions still arriving show their pencil
  under-drawing — the plate's coast, frames and text blocks as
  faint `--pencil` construction lines — and as each region's
  content lands, the pencil inks in (§6.1's language at region
  scale). It belongs because a spinner would be a machine in a
  print shop; an under-drawing is the atlas in its own dormant
  state — the same drawing, not yet inked.
- **Structure.** Skeleton regions are DOM elements styled with
  the plate's own geometry: a chart-shaped pencil coastline for
  a chart region, ruled pencil lines at the text's own measure
  for a text region — never grey rectangles. The real content
  is in the DOM (server-printed) wherever the architecture
  allows; the under-drawing covers only genuinely deferred
  regions (below-fold plates, the register count). Inking is a
  class swap animating pencil → ink over 450ms `--ease-ink`
  with a brief 2px blur-to-sharp on the region's strokes — the
  one licensed blur in the theme (§5).
- **Motion spec.** Under-drawing state: static — pencil does
  not pulse; a breathing skeleton is a screen habit, refused.
  Ink-in: 450ms `--ease-ink` as data lands, region by region in
  survey order. Hard ceiling: any region still pencilled at
  1500ms inks its content anyway — the atlas does not hold a
  reader hostage to a slow plate. Error (a region's data
  fails): the pencil stays and the region prints its office
  note — "This plate has not reached the Office — [re-send
  for it]" with a real retry control.
- **States.** Pencilled → inking → inked (rest). Error:
  pencilled + printed note + retry. Scrolled-past: regions
  below the fold ink on arrival regardless of visibility — by
  the time the reader travels to them, they are print.
  Disabled: JS off → no under-drawings exist; content is
  server-printed complete.
- **Content merge.** The under-drawing is drawn from the
  region's own geometry — the chart's actual coastline in
  pencil — so the loading state is already the content in its
  first state, and the ink-in is the survey arriving, region by
  region, exactly as §6.1 performs it for the hero.
- **Failure fallback.** Watchdog per region at 1500ms (ink
  regardless) — the same law as §5, applied per region. A retry
  that fails twice prints the office note permanently for the
  session with the region's caption and whatever partial print
  exists: a plate admitted missing is better than a plate
  forever pencilled.
- **Reduced-motion variant.** No pencil state visible:
  deferred regions print a plain "Plate in preparation" line
  and swap to full print instantly on arrival.
- **Performance budget & mobile variant.** Pencil regions are
  CSS/SVG line-work — zero raster, zero per-frame cost. Mobile:
  identical; the under-drawing's coastline simplifies with the
  chart's (§6.1).
- **Choreography timeline (v2).** Region requested → pencil
  drawing present with layout → data lands → ink-in 450ms →
  region at rest. Ceiling 1500ms forces ink. Nothing pulses;
  the only motion is the inking itself.
- **State matrix (v2).** *Rest:* printed content. *Hover:* n/a.
  *Focus:* pencilled regions are `aria-hidden` and unfocusable
  until inked. *Active:* the form's entering state (§6.14)
  borrows this shimmer. *Scrolled-past:* pre-inked print.
  *Disabled / no-JS:* server print, no pencils. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: full under-drawings.
  768–1199px: full. <768px: simplified coast pencil, ruled
  lines unchanged.
- **Edge cases & failure modes (v2).** *Data arrives before
  the pencil paints (fast cache):* the region prints directly —
  an under-drawing that never appears is the best kind.
  *Partial arrival (a plate's chart lands, its marginalia
  still travelling):* the chart inks; the margin stays
  pencilled under its own watchdog — the atlas opens with a
  gap admitted, not with the page held shut.
- **Accessibility spec (v2).** Pencilled containers carry
  `aria-busy="true"` and are removed from the accessibility
  tree until inked; one polite announcement ("The atlas is
  printed") fires when the last above-fold region inks — not
  one per region. The error note's contrast: `--ink` on
  `--paper`, 9.6:1.
- **Tokens consumed (v2).** `--pencil`, `--ink`, `--paper`,
  `--ease-ink`, `--dur-pencil-ceiling` (1500ms),
  `--dur-ink-in` (450ms).

---

### 6.16 The colophon footer

- **What & why.** The volume closes with its colophon, set on
  the `--binding` ground: who surveyed, from what data, in
  which edition, with what instruments — and the totals,
  printed a third time (chart, table, colophon: the survey's
  figures agree in three printings or the build fails, §10).
  It belongs because an atlas's authority lives in its
  colophon; a footer of marketing links would close the book
  with someone else's voice.
- **Structure.** A `<footer>` on `--binding`, `--paper` text:
  three columns — the imprint (Atlas Office, edition line,
  "Sheet I · First edition"), the survey's totals (1,284 miles,
  nine stations, 214 soundings, deepest 412 fm at Deepwater
  Anchorage), and the register line ("The Register holds 313
  commissions", live from §6.14's record). Beneath, the errata
  slip: a ruled strip listing the edition's known corrections —
  in the worked record, one: "Plate II: Gull Roads was printed
  72 fm in the prospectus; the survey's figure is 27 fm — a
  transposed digit, corrected." An atlas that prints its errata
  in its footer is practising its law at the last line of the
  page.
- **Motion spec.** None, beyond the page's print entrance. The
  colophon is the stillest element after the table (§6.13):
  the book ends, it does not animate its ending. The register
  count, when §6.14 increments it during the visit, updates as
  a plain text change — print correcting itself, without
  ceremony.
- **States.** Rest: printed. Hover: its links (the Office's
  other sheets, the errata's full sheet) underline in `--paper`
  over 160ms. Focus: 2px `--paper` outline. Active: n/a.
  Scrolled-past: n/a — the footer is the terminus. Disabled:
  an unpublished sheet's entry prints in `--paper` at 55% with
  no link ("Sheet II — in survey"). *Touch:* identical.
- **Content merge.** Every line is the record (§6.17) or the
  imprint of the volume itself; the totals' third printing is
  the merge — the footer is where the survey signs.
- **Failure fallback.** Static HTML; cannot fail. No-JS:
  identical (the register line prints the record's count as of
  the build; a same-visit increment is the only JS touch).
- **Reduced-motion variant.** Identical in every particular.
- **Performance budget & mobile variant.** Zero cost. Mobile:
  the three columns stack — imprint, totals, register, errata —
  in that order (the signing order is preserved at every size).
- **Choreography timeline (v2).** The page's last beat: the
  final plate settles → the binding ground begins → the
  colophon stands printed. If §6.14 fired during the visit:
  register line already reads 313 when the reader arrives —
  the book they close is the book they wrote in.
- **State matrix (v2).** *Rest:* printed. *Hover:* link
  underlines. *Focus:* outline. *Active:* n/a. *Scrolled-past:*
  n/a. *Disabled:* unpublished sheets dimmed, unlinked.
  *Touch:* targets ≥44px.
- **Breakpoints (v2).** ≥1200px: three columns. 768–1199px:
  two columns (register under imprint). <768px: stacked, in
  signing order.
- **Edge cases & failure modes (v2).** *An edition with no
  errata:* the slip prints "No errata are recorded against
  this edition" — the slip exists even when empty, because its
  absence would read as concealment. *A second edition:* the
  colophon's edition line changes and the first edition's
  colophon is archived at its own URL — colophons are never
  rewritten, only superseded.
- **Accessibility spec (v2).** `<footer>` landmark with
  `aria-label="Colophon"`; contrast `--paper` on `--binding`
  8.9:1; the dimmed unpublished entries are text-labelled
  "in survey", never dimming-alone.
- **Tokens consumed (v2).** `--binding`, `--paper`, `--gold`
  NOT used (the colophon is print, not leaf — the census
  holds), `--ease-page`, `--register-count` (313).

### 6.17 The survey record — the one source of every figure

- **What & why.** The theme's single declared data object:
  the Survey of Veralia, Sheet I, from which the coastline,
  route, soundings, table, cards, counters, form numbers and
  colophon all derive. It is specified as an element because
  in this theme the record *is* a design surface: every other
  element is a printing of it, and §10's gate is an audit of
  printings against it. A build substitutes the client's real
  dataset into the same fields; the fields, and the discipline,
  are the theme.
- **Structure.** The record, as printed in the atlas's own
  sheet (and held in the build as one data object): **The
  continent:** Veralia. **The survey:** the Meridian Coast
  Survey, Sheet I, one expedition of 96 days (86 sailing, 10
  ashore surveying), crew of 14, all returned. **The coast:**
  1,284 miles, nine stations joined by eight legs — Port
  Meridian → Cape Alder 162 mi / 9 d; → Gull Roads 148 / 11;
  → Port Sorrow 171 / 8; → The Narrows 139 / 13; → Cape Verity
  155 / 10; → Breaker Shoal 184 / 12; → Deepwater Anchorage
  166 / 9; → Saltmarsh Reach 159 / 14. (Legs sum: 1,284 miles;
  sailing days sum: 86; 86 + 10 ashore = 96.) **Station
  soundings:** Port Meridian 22 fm (Plate I), Cape Alder 12
  (I), Gull Roads 27 (II), Port Sorrow 8 (III), The Narrows 64
  (IV), Cape Verity 118 (V), Breaker Shoal 3 (V), Deepwater
  Anchorage 412 (VI), Saltmarsh Reach 19 (VII). Deepest 412 fm
  at Deepwater Anchorage; shoalest 3 fm at Breaker Shoal.
  **Soundings in all:** 214, by plate — I: 38, II: 34, III: 29,
  IV: 41, V: 27, VI: 25, VII: 20 (sum 214). **Survey passes
  over the interior:** three (§6.3's densities: 40m, 20m, 10m
  intervals). **Area:** the continent 96,400 sq mi; charted
  59,768 (62%); Terra Incognita 36,632 (38%). **The six hazard
  marks (the magenta census):** Breaker Shoal; Widow's Reef;
  the Sorrow Flats; Gull Rock; the Verity Lee Shore; the
  Saltmarsh Bar. **The exclusions (Terra Incognita's
  itemisation, §6.6):** the interior's elevation model beyond
  the third survey's lines; all records after the survey's
  closing year; the upper waters of the Saltmarsh Reach,
  unsounded. **The register:** 312 commissions entered before
  this edition; the form (§6.14) issues № 313.
- **Motion spec.** None — the record does not move. Its
  printings move (§6.1–§6.16); the record is what they answer
  to. Any element found animating a figure *away* from the
  record's value (an overshooting counter, a rounded total)
  is a defect under §9, not a style.
- **States.** One state: declared. An edition change is a new
  record, versioned and dated in the colophon (§6.16) — the
  record is never edited in place beneath its printings.
- **Content merge.** Total: there is no content on the page
  that is not a printing, a citation or a consequence of this
  record. The worked examples (§8) are walks across its
  printings.
- **Failure fallback.** If a data source behind the record is
  unavailable at build or runtime, the affected printing shows
  the record's last declared figure with its edition date —
  print cites its edition rather than failing blank.
- **Reduced-motion variant.** Identical — the record has no
  motion to reduce.
- **Performance budget & mobile variant.** The record ships as
  one JSON object ≤8KB and as the DOM's printed figures; every
  printing reads from it, so the page carries each figure's
  *source* once and its printings as text.
- **Choreography timeline (v2).** Build time: record declared
  → printings generated → §10's audit re-adds every column,
  route and count against it → the edition is dated. Runtime:
  the only mutation the record permits is the register's
  increment (312 → 313) on §6.14's success, propagated to its
  three printings.
- **State matrix (v2).** *Rest:* declared. *Hover / focus /
  active:* n/a. *Scrolled-past:* n/a. *Disabled:* a field the
  source cannot supply is declared as an exclusion (feeding
  §6.6), never silently dropped. *Touch:* n/a.
- **Breakpoints (v2).** The record is size-invariant; its
  printings carry the breakpoint behaviour.
- **Edge cases & failure modes (v2).** *A client dataset that
  does not divide into legs and stations:* the mapping is the
  design work — a time series becomes a coast (time as
  distance, events as stations, gaps as Terra Incognita); if
  no honest mapping exists, the theme is wrong for the data
  and §1's when-NOT applies. *Two sources disagreeing on a
  figure:* the disagreement prints — the record carries both
  with their sources, as §6.6's sibling theme-neighbour
  discipline demands; a silently averaged figure is a
  falsified one.
- **Accessibility spec (v2).** The record's own sheet (the
  "Survey Sheet" page, §7) presents it as the table (§6.13)
  plus this declaration in text — the source itself is
  readable, not locked in a script file.
- **Tokens consumed (v2).** None — the record consumes no
  tokens; it issues figures. Its constants: `--coast-miles`
  (1284), `--stations` (9), `--soundings-total` (214),
  `--deepest` (412 fm), `--register-next` (313).

### 6.18 Uncharted waters — the 404 & empty states

- **What & why.** Where the atlas has no plate — a wrong URL,
  a search with no station, an index filter with no entries —
  the reader is shown uncharted water: a plate mark holding
  open paper, one pencil coastline that stops mid-draw at the
  edge of the known, and the office's plain statement of where
  they are and how to return to charted water. It belongs
  because in this world a missing page is not an error state;
  it is a place the survey has not reached, and the atlas —
  true to §6.6's law — prints its blanks rather than dressing
  them as content.
- **Structure.** A plate inside its mark (§6.9): the known
  coast enters from the left in full ink and ends — cleanly,
  at a surveyed boundary line — where the record ends; beyond
  it, paper and one pencilled, dashed continuation marked
  "not surveyed". The print block: the heading in Fraunces
  ("Uncharted water"), the statement in Newsreader ("This
  sheet is not in the atlas. The address answers to no plate
  in Sheet I."), and the exits as real links — to the chart
  (Plate I), the plate index (§6.11), and the commission form
  (§6.14: an uncharted coast is a plausible reason to commission
  one). Search/filter empty states reuse the plate at region
  scale, with the statement naming the empty result.
- **Motion spec.** Entrance: the known coast is already inked;
  the pencil continuation draws itself once, slowly, 1200ms
  `--ease-ink`, and stops — visibly, deliberately — at the
  boundary, its last dash fading to `--pencil` at 40%. It does
  not complete. That incompletion is the entire animation, and
  it runs once.
- **States.** Printed (rest). There is no hover, no retry
  loop, no suggestion engine: uncharted water does not
  recommend other water. The exits are the whole interaction.
- **Content merge.** The coast that *is* drawn is the record's
  own first leg (Port Meridian → Cape Alder, §6.17) — the
  reader is shown the edge of the real chart, not a generic
  wave doodle; and the statement's "Sheet I" is the edition's
  actual name, from the colophon (§6.16).
- **Failure fallback.** The 404 is itself a fallback and ships
  fully printed; its one animation is armed with a 2000ms
  watchdog that leaves the pencil line at its final, stopped
  state. No-JS: the pencil line prints at its stopped state.
- **Reduced-motion variant.** The plate arrives as printed:
  inked coast, stopped pencil line, statement, exits. No draw.
- **Performance budget & mobile variant.** One small SVG, one
  draw, once. Mobile: the plate narrows, the statement and
  exits stack beneath the coast; nothing is cut — a lost reader
  on a small screen is owed the whole plate.
- **Choreography timeline (v2).** Page lands (via §6.10's turn
  or directly) → coast already inked → t=200ms pencil begins →
  t=1400ms pencil stops at the boundary, final dash fades →
  rest, permanently. Watchdog deadline t=2000ms.
- **State matrix (v2).** *Rest:* printed, pencil stopped.
  *Hover:* exit links underline (as §6.16). *Focus:* exits in
  DOM order — chart, index, commission. *Active:* n/a.
  *Scrolled-past:* n/a (single plate). *Disabled:* n/a.
  *Touch:* exits ≥44px.
- **Breakpoints (v2).** ≥1200px: plate + statement side by
  side. 768–1199px: plate above, statement beneath. <768px:
  stacked, exits full-width.
- **Edge cases & failure modes (v2).** *A URL that names a
  real station but a wrong plate:* the statement says so —
  "Cape Verity is charted on Plate V" with the link — the
  atlas corrects a mis-shelved request precisely, because its
  index (§6.11) can. *A search with results in the record but
  none in the edition:* the empty state names the distinction
  ("charted in the survey, not printed in this edition") —
  two kinds of absence, two sentences, never one vague
  "no results".
- **Accessibility spec (v2).** The plate is `role="img"`
  labelled "The charted coast ends; beyond it, unsurveyed
  water". The statement and exits are plain text and links,
  first-class. The HTTP status is a real 404 — the honesty is
  protocol-deep, not cosmetic.
- **Tokens consumed (v2).** `--ink`, `--pencil`, `--paper`,
  `--paper-shade`, `--ease-ink`, `--dur-pencil-stop` (1200ms),
  `--dur-watchdog-404` (2000ms).

---

## 7. Page application map

**Home — the atlas opened.** The full ceremony: §6.15's
under-drawings ink to the hero plate; §6.1's coastline draws;
§6.4's cartouche engraves; the §6.2 spread carries the reader
down the coast through all nine stations; then §6.13's table,
§6.12's index, §6.6's blank, §6.14's register, §6.16's
colophon. The home page is the whole volume in one leaf.

**Listing — the plate index.** §6.12's cards at full grid,
§6.11's index as the page's own head, plates cited by numeral.
Filters are index refinements (by plate, by survey, by hazard)
printed as register lines, never as chip-clouds; an empty
filter result is §6.18 at region scale.

**Detail — one station, one plate.** The station's plate at
full size with §6.7's loupe and §6.8's pins live; its marginal
note complete; its leg's figures in a ruled record block; the
prev/next navigation is the coast itself — "Westward: Gull
Roads, 148 miles" — travel, not pagination arrows. A station's
hazards print first among its facts (§3's fifth law).

**About — the expedition.** The survey's story as a log: the
crew of 14, the 96 days, the instruments, told in the margin's
hand against the print's dates. §6.9 plates carry the
expedition's views. The page ends at the colophon it describes.

**Commission — the register.** §6.14 at full-page scale: the
register's recent entries printed above the form (coasts
commissioned, sheets issued — from the record), the form, the
entry. This is the volume's only conversion page, and it
converts in the office's voice.

**The Survey Sheet — the record itself.** §6.17 presented as a
page: §6.13's table, the declaration, the censuses, the
exclusions. The atlas's sources are a page of the atlas.

**404 — uncharted water.** §6.18, reached by §6.10's turn,
printed complete.

**Checkout / account / settings:** refused the theme (§1).
Commerce, if any, happens off-volume, linked plainly from the
colophon — the atlas does not pretend a till is a plate.

---

## 8. Worked examples

### 8.1 The hero — the coast inks itself (worked example 1)

The reader lands. The masthead (§6.11) is already printed —
furniture precedes ceremony. The hero plate stands in its plate
mark with the coastline's SVG shipped drawn and the soundings
printed; in the first frame, the script rewinds the stroke,
registers the 3000ms watchdog (§6.1), and the survey begins.
t=120ms: the nib touches at Port Meridian. The stroke draws
under `--ease-ink` — fast and wet at the harbour, slowing as
the coast complicates — and at t≈300ms the first sounding pops:
22 fm at Port Meridian, blooming teal for 380ms and settling in
`--teal-deep`. The reader's eye is pulled along the shore by
the drawing itself; no headline competes, because the title is
still unframed. Soundings pop in survey order — 12 at Cape
Alder, 27 at Gull Roads — each a measurement taken as the line
passes. At t≈2260ms the last sounding (19 fm, Saltmarsh Reach)
settles; at t=2400ms the cartouche begins its circuit (§6.4),
corners in engraver's order, and at t≈3160ms the gold glint
crosses the crest once and rests. The plate is complete:
coast, soundings, title, edition line. Scroll begins, and
§6.2's spread takes over — the marker is waiting at Port
Meridian. *Reduced motion / no-JS:* the same plate, printed,
in the same order of reading. The ceremony cost the reader
nothing and its absence costs them nothing: that is the law,
working.

### 8.2 Mid-page — the blank, admitted (worked example 2)

Deep in the home leaf, after the sounding table has given the
survey plain, the reader reaches the Terra Incognita plate
(§6.6). Its boundary dashes draw in over 900ms — the reader
watches the edge of knowledge get surveyed like any other
line — then the hatching in two passes, coarse then fine, and
the label inks last: *Terra Incognita*. In the margin, the
itemisation, in the hand: the interior's elevation model
beyond the third survey's lines; all records after the closing
year; the Saltmarsh's upper waters, unsounded — each with its
reason, and the figure in print: "36,632 of 96,400 square
miles — 38 per cent — not surveyed." The reader has just been
told, by the most beautiful plate on the page, exactly what
this atlas does not know. §6.8's pins refuse to drop here; the
loupe resolves nothing finer. The plate's restraint is the
worked example's point: every other theme in the library fills
its showcase section; this one *bounds* it, and the bounding is
the premium gesture — the moment the visitor decides the
numbers elsewhere on the page can be trusted.

### 8.3 Conversion — a coast enters the register (worked example 3)

The reader, having travelled the continent, reaches the
commission form (§6.14). The preamble has already made its
promise in print: "The Register holds 312 commissions. Yours
will be № 313." They enter a name; a coast — "forty years of
tide-gauge records, three stations, one harbour silting up";
an extent — "14,600 records". The extent is beyond nothing
and within the register's printed range, so no marginal note
is needed. Submit: the form dims to 65%, the button shimmers
in pencil, and at the response the form region is replaced by
the entry — ruled, risen over 450ms, its number underlined by
a fresh 300ms rule: **Commission № 313** — the coast and extent
as entered, and the office's line: "The Office will write
within seven days with the survey's terms." Simultaneously the
masthead's register line and the colophon's (§6.16) now read
313 — the reader scrolls down later and finds the book they
close is the book they wrote in. The conversion did not leave
the world for a checkout; it was *entered in the register*,
and the number it issued was promised before the first field
was touched. That is conversion in this theme's grammar: not a
funnel, an entry.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **The filled blank.** Terra Incognita quietly populated
   with decorative texture, stock imagery or "coming soon"
   sparkle to make the page feel complete. The blank is the
   theme's thesis; filling it is falsifying the survey. Cure:
   §6.6's plate, hatched, bounded, itemised — or, if the record
   declares no exclusions, no plate and a printed declaration.
2. **Naked numbers.** A figure printed without its station,
   leg or plate — "412" floating in a hero. Cure: §3's first
   law; §10 greps for unattached figures in copy.
3. **Gold creep.** Gold leaf spreading to buttons, links,
   headings, "premium" accents. The census is three spends
   (§2); a fourth is costume jewellery on a chart. Cure: the
   §10 census grep; buttons are printed register entries in ink.
4. **Magenta as an accent colour.** Hazard magenta used for a
   sale badge or an error state. Six marks, all hazards (§6.17);
   errors are corrected in ink (§6.14). Cure: census audit.
5. **The fake hand.** Marginalia in a script font, or
   handwriting that types itself letter by letter. The hand is
   Newsreader italic (§3) and inks as one pass (§6.8). A script
   font turns the surveyor into a greeting card.
6. **Stock plates.** A generic ocean photograph inside a plate
   mark. The frame makes the lie worse — it cites the image as
   evidence. Cure: §6.9's rule — record subjects only, else an
   engraved chart detail, else no plate.
7. **Counters that perform.** Overshoot, bounce, decimal
   flicker, a sounding that lands on 411.6 before settling at
   412. A measurement does not wobble. Cure: §6.5's linear
   counts, integer intermediates, dead stop at the record.
8. **Pirate cosplay.** Sepia-washed everything, torn-edge
   clip art, a compass rose as a logo watermark on every
   section. The atlas is a *working instrument*, crisply
   printed; age is in its apparatus (plate numbers, register,
   errata), not in distress filters. Cure: paper stays clean
   `#EDE4CE`; the rose appears at §6.2 and §6.11 only.
9. **The dashboard relapse.** Live-updating tiles, sparklines,
   a "real-time" badge. The atlas is an edition, dated in its
   colophon. Cure: §1's when-NOT; new data is a new edition.
10. **Pins as confetti.** Pin drops that produce tooltips with
    marketing copy. A pin produces a survey note with figures
    from the record, or — ashore — an honest non-figure (§6.8).
11. **Two pins on one page.** The §6.2 spread plus a second
    pinned "story" section. One pin per page (§5); a second
    turns a bound volume into a landing page.
12. **The silent average.** Two sources disagree and the page
    prints a compromise figure. Cure: §6.17's rule — the
    disagreement prints, with sources.

---

## 10. Quality gate

Blocking checks — the build does not ship until every one
passes, signed by a non-builder:

1. **Figure audit.** Every figure on every page re-derived
   from §6.17: legs sum to 1,284; sailing days to 86; 86 + 10
   = 96; plate soundings sum to 214; charted + incognita =
   96,400; the register reads 312 in the preamble and issues
   313. Any mismatch, anywhere, blocks.
2. **Three-printings agreement.** The totals agree in the
   chart apparatus, the table (§6.13) and the colophon (§6.16);
   the station figures agree across chart, cards (§6.12) and
   table.
3. **Gold census.** `grep` the build for the gold token: its
   uses are exactly the cartouche crest (§6.4), the rose north
   point (§6.2/§6.11 — one component), and plate numerals
   (§6.9). A fourth use blocks.
4. **Magenta census.** Exactly six hazard marks, the six named
   in §6.17, each with its ✕ and its printed label; magenta in
   any CSS outside the hazard marks blocks (card citations are
   audited as citations of chart marks, not new marks, §6.12).
5. **Watchdog drill.** With the animation loop disabled, every
   plate reaches its printed final state within its watchdog
   deadline; with JS disabled entirely, the volume is complete
   and readable, in order, with all figures.
6. **No-naked-numbers pass.** Copy review against §3's first
   law: every figure in prose carries its station, leg, plate
   or total.
7. **Instrument agreement.** At each station settle (§6.2), the
   marker, the mile readout (§6.5) and the facing notes name
   the same station and the same cumulative miles.
8. **Loupe honesty.** The loupe's fine state exists in the
   record (a real next density) and its content is available
   without the loupe (caption/table/keyboard toggle) — §6.7.
9. **Blank integrity.** Terra Incognita's boundary and
   itemisation match §6.17's exclusions exactly; pin and loupe
   refusal states work on the plate.
10. **Reduced-motion walk.** With `prefers-reduced-motion`,
    the entire volume is traversed with zero animation and
    zero missing content; the register form completes; the 404
    reads complete.
11. **Contrast sign-off.** The §2 ratios verified in the built
    CSS at every state (including hover/focus deepening), gold
    never text, magenta never colour-alone.
12. **Print check.** The volume prints as an atlas: plates at
    their marks, table complete with footnote, colophon last —
    on paper, in ink.

---

## 11. Component inventory

Every component a real site in this theme needs, with its
treatment. Refusals are components too — each names its
in-theme replacement.

- **Buttons.** Printed register entries: ink rule beneath,
  Newsreader 500 uppercase; primary = the register's submit
  style (double rule). No fills, no pills, no shadows.
- **Links.** `--teal`, underlined as a surveyed line (solid
  in text, dashed in marginalia — the hand cites loosely).
- **Inputs.** Ruled lines (§6.14): bottom rule, station tick
  on focus, labels in the office's print.
- **Selects.** A printed list that unfolds — the register's
  sheet choices as radio entries, not a dropdown menu; a
  select in an atlas is a list of plates.
- **Tables.** §6.13 is the pattern: caption, scoped heads,
  double-rule totals, honest footnotes.
- **Cards.** §6.12's station entries; no other card style
  exists in the volume.
- **Badges.** Refused. A status is a marginal note or a
  register line; the atlas does not pin labels on its data.
- **Alerts.** The office's note: a ruled block in print, ✳
  where correction is needed (§6.14); hazards alone use ✕ +
  magenta. No banners, no dismiss buttons — a note in a
  register is struck through when resolved, not closed.
- **Toasts.** Refused. Confirmations are entries (§6.14) or
  marginal notes (§6.8) — things written in the book, not
  notifications over it.
- **Modals.** Refused. The atlas has no overlays; a plate that
  needs room gets its own page (§7's detail). The index leaf
  (§6.11, mobile) is a page, not a modal.
- **Tabs.** Refused. The volume's organisation is plates and
  an index; tabbed content is a drawer of unbound sheets.
- **Accordions.** The exclusions list (§6.6) and the errata
  may fold as printed sub-entries with a rule and a "continued"
  line — folding in the atlas is a leaf turned, marked as such.
- **Pagination.** Travel: "Westward / Eastward" with the leg's
  miles (§7 detail pages); index pagination is a printed list
  of leaves (§6.11).
- **Breadcrumbs.** The survey path: Atlas › Plate V › Cape
  Verity — positions in the volume, set as a running head line.
- **Progress indicators.** The route itself (§6.2) and the
  mile readout (§6.5). No bars, no spinners, anywhere.
- **Search.** An index lookup: results are station entries
  (§6.12) or the uncharted statement (§6.18) — searching an
  atlas is consulting its index.
- **Tooltips.** Refused. Explanation lives in marginalia,
  attached to its station, in the hand.
- **Avatars / people.** The survey's crew are named in print
  (the log, §7's about) — an atlas credits its surveyors in
  the colophon, not in circles.
- **Chips / tags.** Refused; classification is by plate and
  survey, printed in the entry.
- **Dividers.** Fold lines and plate rules (§4) — the volume's
  own seams, never decorative hairlines between "sections".
- **Icons.** Four only, drawn as engravings: the compass rose,
  the station ring, the ✕ hazard mark, the ✳ correction mark.
  An icon set would be a fifth material.
- **Empty states.** §6.18 at region scale.
- **404.** §6.18 at page scale.

---

## 12. Content & copywriting voice

Two registers, as the type laws (§3) decree. **The Print** —
the office and the compositor: Fraunces and Newsreader roman,
declarative, figured, dated; it states what was measured and
signs it. **The Hand** — the surveyor's margin: Newsreader
italic, first person plural ("we"), present at the place it
describes; it may doubt, correct and confess, but it never
carries a fact alone.

**Headline style.** Plate titles name places and acts, not
benefits: "The Narrows, sounded at slack water" — never
"Unlock powerful insights". A headline that could sell software
is rewritten until it could only head a chart.

**Label style.** Register labels are nouns of the office:
"Commissioner's name", "The coast (what it measures)", "Extent,
in records". Buttons complete the register's sentence: "Enter
the commission", never "Submit" or "Get started".

**Error voice.** The office corrects in complete sentences,
in ink, without blame: ✓ "The extent is entered as words;
give it as a figure — 14,600, not fourteen thousand." ✗
"Invalid input!!" ✗ "Oops — something went wrong." The atlas
has no "oops"; it has errata.

**Empty-state voice.** ✓ "This sheet is not in the atlas. The
address answers to no plate in Sheet I." (§6.18.) ✗ "404 —
lost at sea lol." The blank is admitted in the same voice that
prints the soundings.

**Verbatim fixed strings** (never paraphrased in any build):
the preamble — "The Register holds 312 commissions. Yours will
be № 313."; the table's footnote — "Depths are point soundings
and are not summed. The survey took 214 soundings in all.";
Terra Incognita's figure line — "36,632 of 96,400 square miles
— 38 per cent — not surveyed."; the office's promise — "The
Office will write within seven days with the survey's terms.";
the unsurveyed pin note — "Ashore: no sounding taken — the
survey was a coast survey."; the empty errata slip — "No errata
are recorded against this edition."

**Numbers in copy.** Always with their station (§3); always
the record's figure, spelled as the record spells it (1,284
with its comma; fathoms as "fm" after the first full use on a
page); percentages only where the record prints both parts
("38 per cent" travels with 36,632 of 96,400).

---

## 13. Full-page scroll choreography map

The home leaf, top to footer — every beat in order:

1. **Arrival.** Masthead printed; hero under-drawing inks
   (§6.15); the plate stands in its mark.
2. **The survey.** Coastline draws 2.2s (§6.1); soundings pop
   in survey order; cartouche engraves and glints (§6.4). The
   reader has watched the chart being made.
3. **The descent into the spread.** The fold shadow deepens in
   the masthead; the spread's plate pins; the marker waits at
   Port Meridian; the mile readout stands at "0 of 1,284".
4. **The journey.** Nine settles: ring, notes swap, miles
   counting — Cape Alder (162), Gull Roads (310), Port Sorrow
   (481), The Narrows (620), Cape Verity (775), Breaker Shoal
   (959 — the hazard note prints first in its margin), Deepwater
   Anchorage (1,125 — the 412 fm sounding counts longest),
   Saltmarsh Reach (1,284). Contours refine coarse → surveyed →
   fine across the same scroll (§6.3). The compass rose drifts,
   almost imperceptibly, throughout.
5. **The plain survey.** The table (§6.13) — stillness after
   travel; the reader checks the journey against the figures.
6. **The index.** Station cards rise in survey order (§6.12);
   the index adds itself up in its footer line.
7. **The plates.** §6.9 plates mount one per viewport; the
   loupe is live; pins may be dropped.
8. **The blank.** Terra Incognita hatches in (§6.6) — the
   page's quietest beat, placed after its fullest, on purpose.
9. **The register.** The form (§6.14) under its printed
   promise; a submission here writes № 313 into the book.
10. **The closing.** The binding ground rises; the colophon
    (§6.16) signs the volume — totals a third time, register
    count as the reader left it, the errata slip last.

Reverse scroll retraces honestly: the marker walks back, notes
swap back, contours re-coarsen; ink, pins and the register
entry do not unwrite.

---

## 14. Whole-page performance budget

- **Total page weight:** ≤640KB (home leaf, all plates) —
  HTML/CSS/JS ≤180KB gz; the two font families subset to the
  edition's character set ≤90KB; images (plates) ≤340KB, WebP/
  AVIF with reserved aspect boxes; the record (§6.17) ≤8KB.
- **Frame budget:** the shared loop's per-frame cost ≤0.6ms on
  a mid-tier device — one path update (§6.1), one
  `getPointAtLength` (§6.2), two opacity writes (§6.3), text
  writes only inside count windows (§6.5). No per-frame
  filters, shadows or blurs anywhere; the deckle mask and paper
  grain are static, pre-rendered.
- **Long tasks:** none over 50ms after first paint; the
  coastline path is inline so the survey never waits on the
  network.
- **Licensed loops:** one rAF loop; two ambient motions (rose
  drift, contour breath) ride it and pause off-screen.
- **Cut order when the budget is exceeded:** (1) the page turn
  (§6.10) on low-power devices; (2) the marker's scrub travel
  on <768px (already cut, §6.2); (3) the fine contour set on
  mobile (§6.3); (4) the loupe's duplicate render below 768px
  (already a toggle, §6.7); (5) plate tilt (§6.9).
- **Never cut:** any watchdog; the printed DOM; the table
  (§6.13); Terra Incognita (§6.6); the reduced-motion variants;
  the record (§6.17). A build that ships the ceremony and cuts
  the honesty has inverted the theme.
- **Print budget:** the print stylesheet is part of the theme,
  not an afterthought — plates, table and colophon print
  complete (§10, check 12).

---

## 15. Build-order checklist

1. **Declare the record (§6.17) first** — map the client's
   dataset into legs, stations, soundings, exclusions; if no
   honest mapping exists, stop and re-theme (§1).
2. **Print the static volume** — the full DOM, all figures,
   all plates, no script: the atlas complete as a book.
3. **Set the paper** — palette tokens (§2), type (§3), plate
   marks, fold lines, deckle and grain (§4).
4. **Build the table (§6.13) and the record sheet (§7)** — the
   honesty apparatus before any ceremony.
5. **Build the masthead and index (§6.11)** — furniture before
   performance.
6. **Build the cards (§6.12)** from the record; verify the
   index's footer sum against the record by hand.
7. **Build Terra Incognita (§6.6)** — boundary and itemisation
   from the record's exclusions, exactly.
8. **Build the register form (§6.14)** — preamble promise,
   entry, watchdog, the register increment propagated to
   §6.11 and §6.16.
9. **Build the colophon (§6.16)** — totals' third printing;
   run the figure audit (§10, checks 1–2) on the static build.
10. **Arm the shared loop** — scroll progress, lerp 0.12;
    wire §6.2's marker, §6.3's contours, §6.5's counters, each
    with its watchdog registered in the same frame as its
    rewind.
11. **Arm the entrance ceremonies** — §6.1's coastline, §6.4's
    cartouche, §6.15's ink-ins, §6.9's plate mounts.
12. **Add the instruments** — loupe (§6.7) with its keyboard
    toggle; pins (§6.8) with their caps and refusals.
13. **Add the turn (§6.10)** and the 404 (§6.18).
14. **Write the reduced-motion variants** element by element
    (§6) and walk the volume with motion off (§10, check 10).
15. **Run the full quality gate (§10)** — censuses grepped,
    watchdog drill, instrument agreement, print check — signed
    by a non-builder. Only then is the atlas an edition.

---
