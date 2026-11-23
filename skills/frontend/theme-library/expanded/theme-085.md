# 85. Transit Photometry — Expanded (v1 + v2)

## 1. Concept & world

The site is an exoplanet hunter's light curve, and it hangs on
one graph: a star's brightness measured over time, plotted as
thousands of points that sit on a flat line — except where
something crossed. The story of the page is never told in
headlines first; it is told in the dips. The visitor scrolls
through one observation run, section by section, and each section
is one transit: the dip in the pinned strip at the top of the
page deepens as its text arrives, the transits fold on top of
each other into a single sharp profile, and the error bars on
every printed figure shrink as the fold accumulates. Certainty
is the narrative arc. A page in this theme does not *describe*
a detection — it performs one, at instrument pace, with the
uncertainty left in.

**The theme's one law: the curve never lies, and no planet is
claimed before it is folded.** Every number printed anywhere on
the page — depth, period, duration, SNR, every error bar, every
counter — traces to one declared observation record (§6.17): the
run's star, cadence, baseline, and the five transit epochs with
their measured depths. Error bars are drawn to the scale of the
axis they sit on, never as decoration. A dip shown in the strip
is the same dip, at the same epoch and the same depth, as the
section below it and the row in the log table. If a figure
cannot be derived from the record, it does not appear; if the
record changes, every printing of the figure must change with
it, and the quality gate (§10) greps for the stale ones.

The worked record used throughout this spec (every site
substitutes its own real record, in the same shape): survey
target **K-85**, a K-dwarf in Field 7; run window **BJD −2459000
= 124.000 → 144.250** (20.25 days); cadence **15 minutes**;
**1,944 points** in the run; five complete transits, epochs
**127.900, 131.420, 134.940, 138.460, 141.980**, spacing exactly
**P = 3.52 d**; transit duration **T14 = 2.1 h**; measured depths
**288, 312, 295, 307, 301 ppm**, folded depth **300 ppm**; the
next epoch, **145.500**, falls after the run ends and is printed
as a prediction, never drawn as data.

**Best fit.** Astronomy institutes publishing a detection;
citizen-science platforms (the reader's click genuinely is the
vetting gesture); space-data companies whose product is a
catalogue of measured things; mission and survey microsites;
any organisation whose credibility rests on showing its
uncertainty honestly. The theme flatters data that improves as
you watch it accumulate.

**When NOT to use it.** When there is no time series — the strip
is the page's sky and a fake one is instantly visible. When the
client wants a claim stated up front ("we found a planet!") —
this theme's whole grammar is that the claim is *earned* at the
fold, near the end. When figures are marketing numbers with no
uncertainty (a conversion rate has no honest ± here; forcing one
is the theme's cardinal sin, §9). When the audience needs the
answer in ten seconds: the run takes the run's time, compressed,
and a visitor in a hurry should be given a different theme.

**The visitor's role.** Not an audience — a member of the survey
team on their first night. They watch the run, they read each
transit as it centres, they may mark transits themselves (§6.7),
and by the fold they have seen exactly the evidence the
announcement rests on. The page trusts them with the noise.

---

## 2. Palette

Five anchors from the original entry, unchanged, plus seven
derived tokens. Every contrast figure below was **computed from
the hex values for this expansion** (WCAG relative luminance),
not estimated. The palette's discipline: paper and ink do the
reading; indigo is the data's colour and appears only where data
is; red is rationed to annotation — the human hand on the chart;
grey is uncertainty itself, drawn, never typed.

| Token | Hex | Role | Usage ratio | Pairing / contrast ruling |
|---|---|---|---|---|
| `--paper` | `#F2F1EC` | Observatory white — the chart paper, page ground | ~70% of surface | Ground for `--ink` text: **13.7:1** — the page's reading pair |
| `--ink` | `#1F2430` | Photometry ink — scatter points, body text, axis rules | ~18% | On `--paper` 13.7:1; `--grey` labels on it 5.9:1 (mono captions only) |
| `--indigo` | `#3C4A6B` | Dip indigo — dip fills, the folded profile, marked transits | ~6% | On `--paper` **7.8:1** (text legal); on `--ink` **1.8:1 — forbidden pairing** |
| `--red` | `#B03A2E` | Annotation red — the human hand: marks, confirmations, margin notes | ≤2% | On `--paper` **5.3:1** (annotation text ≥13px mono only); on `--ink` **2.6:1 — forbidden as text** |
| `--grey` | `#9AA0A6` | Error-bar grey — error bars, scatter noise, residuals | ~4% | On `--paper` **2.3:1 — never text, never a rule that carries meaning alone**; it is drawn uncertainty, always paired with a mono figure |
| `--paper-deep` | `#E7E5DC` | Plate shading — alternate section grounds, card faces | bands | `--ink` on it 12.4:1; sections alternate paper/paper-deep by transit parity |
| `--grid` | `#D8D5C9` | Graph grid, minor — the 8px scientific grid | background | Never a border on an interactive element; sits behind everything |
| `--grid-major` | `#C2BFB2` | Graph grid, major — the 40px lines and axis frames | background | The only grid tone allowed to frame a chart |
| `--ink-soft` | `#4A5064` | Secondary ink — captions, table row labels, footnotes | small areas | On `--paper` **7.1:1** — body-legal; the softest tone permitted for prose |
| `--baseline` | `#B9B6A9` | The fitted baseline — the model's flat line through the scatter | one line per chart | A drawn model, never text; always labelled "BASELINE FIT" in mono where it appears |
| `--plate` | `#171B24` | The reduction plate — the folded-profile panel (§6.12) and the strip's fold zone | one panel + strip end | `--paper` text on it **15.2:1**; `--grey` residuals on it 6.5:1; `--red` on it **2.9:1 — glyphs and strokes only, never text** |
| `--indigo-fill` | `rgba(60,74,107,0.14)` | Dip fill — the soft body of a deepened dip | inside dips only | A gradient stop, not a surface; text never sits on it |

**Dark behaviour — there is no dark-mode inversion.** The theme
is a printed chart from a white-walled observatory; the single
dark surface is the reduction plate, which is dark because
reduced data is presented on the plate, not because the room
lights went out. `prefers-color-scheme: dark` changes nothing.
The print stylesheet is the theme's own fallback state (§6.2):
the full light curve printed once, at full width, with every
figure beside its section — a light curve is meant to be pinned
to the wall and argued over.

**Rationing rules (enforced by the quality gate, §10).**

- Red appears only as annotation: reader marks (§6.7), the
  confirmation strings, and margin notes. A page-wide red census
  above 12 instances fails the gate. Red is never a button fill,
  a link colour, or an error colour — errors are ink text with a
  red margin tick (§11), because on a chart, red already means
  "a person marked this."
- Indigo appears only where data deepens: dip fills, the folded
  profile, marked-state dips. Navigation, buttons and headings
  are ink. If indigo is carrying decoration, the theme has
  already failed.
- Grey never carries meaning alone: every error bar is paired
  with its ± figure in mono within the same figure block, so the
  uncertainty survives a greyscale photocopy and a screen reader.

---

## 3. Typography

Two faces, two jobs, no third voice. **Spectral** is the prose
of the observatory — display lines and body text, a serif cut
for scientific publishing. **IBM Plex Mono** is the instrument:
every measurement, every axis label, every epoch, every figure
with a unit. The split is absolute and is the theme's most
recognisable discipline: if it was measured, it is mono; if it
was written, it is Spectral.

**Type scale.**

| Role | Face | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Display (the dip headline) | Spectral 300 | 44px / 1.08 (≥1200px); 34px (768–1199); 27px (<768) | −0.01em | Set inside the hero dip (§6.1); never more than two lines |
| Section heading | Spectral 400 | 30px / 1.15 | −0.005em | One per transit section; names the event, not the marketing |
| Body | Spectral 400 | 17px / 1.55 | 0 | Measure 62ch max; the reading column (§4) |
| Lead / standfirst | Spectral 300 italic | 20px / 1.45 | 0 | One per page, under the hero |
| Data figure (hero class) | IBM Plex Mono 500 | 28px / 1.2 | 0 | Depth, period, SNR in the counters rail (§6.15) |
| Data figure (inline) | IBM Plex Mono 400 | 15px / 1.5 | 0 | Always with unit: `300 ppm`, `3.52 d`, `±9 ppm` |
| Axis / strip labels | IBM Plex Mono 400 | 10.5px / 1.3 | 0.04em | Hour ruler, flux ticks; uppercase |
| Annotation | IBM Plex Mono 500 | 12.5px / 1.4 | 0.06em | `--red`, uppercase: `T3 — CONFIRMED` |
| Caption / footnote | Spectral 400 | 13.5px / 1.5 | 0 | `--ink-soft`; states the figure's provenance |

**Five type laws.**

1. **A number is never set in Spectral.** If it has a unit, an
   epoch, or a ±, it is mono. A serif numeral anywhere on the
   page fails the gate — it means prose and measurement have
   been mixed, which is how charts start lying.
2. **Mono figures are tabular and never round silently.**
   Depths print as integers of ppm (`300 ppm`), periods to two
   decimals (`3.52 d`), uncertainties always with their ± and
   never dropped for tidiness. Where a figure is a prediction it
   says so in words beside it (`PREDICTED`), in the same line.
3. **The headline lives in the dip.** The one display line of
   the hero is set inside the U of the transit (§6.1) at a size
   the dip's width can hold; if the copy does not fit the dip,
   the copy is shortened — the dip is never widened to fit the
   words. The data outranks the headline.
4. **Annotations are uppercase mono, red, and dated.** Every
   human mark carries its epoch or its transit ID (`T3 —
   CONFIRMED`, `MARKED 138.460`). An undated annotation is an
   opinion; the chart does not print opinions.
5. **Spectral never shouts.** No bold display, no all-caps
   Spectral anywhere. Emphasis in prose is italic; emphasis in
   data is a deeper dip. The only uppercase on the page is mono
   — labels and annotations — because on a real chart the
   uppercase is the instrument's and the annotator's, never the
   author's.

---

## 4. Layout language

**The strip is the sky.** A fixed light-curve strip, 90px tall,
pins across the top of the viewport for the entire page (§6.2):
the full run's scatter, its five dips, the hour ruler along its
foot, and at its right end the fold zone where transits stack
(§6.4). Everything below the strip is read *under* the star's
ongoing record. The strip never hides, never collapses, and
never carries navigation chrome inside the plot area — its right
rail, outside the plot, holds the run's clock (current epoch
under the scroll position) and nothing else.

**Sections are transits.** The reading column below is divided
into sections that correspond one-to-one with the strip's dips:
five transit sections (T1–T5), preceded by the hero (the whole
run, §6.1) and followed by the fold (§6.12), the log (§6.13),
and the joining (§6.14). A section's vertical extent is
proportional to nothing decorative — each transit section is one
reading unit of 90–110vh so that exactly one dip is "current" in
the strip at any scroll position. Sections alternate `--paper` /
`--paper-deep` by transit parity, the way ruled paper alternates
nothing but the eye needs the seam: the seam *is* the transit
boundary, and the boundary is labelled in the margin with its
epoch in mono.

**Graph paper everywhere.** The ground carries a scientific
grid: minor lines every 8px (`--grid`), major every 40px
(`--grid-major`), drawn as background, never as borders. Charts
align their axes to the major grid; the reading column's left
edge sits on a major line; figure blocks snap to the 40px
module. The grid is the theme's whitespace discipline: space is
not empty, it is *ruled* — measured room to plot in.

**Density rules.** One chart or figure block per section, one
idea per figure. Data figures never sit closer than 24px to
prose they do not describe. The counters rail (§6.15) is the
only place figures from different transits share a band, because
the rail's job is accumulation. Cards (§6.11) run at most three
across at ≥1200px — a survey page is an instrument bench, not a
marketplace grid.

**The margin is the annotator's.** A 200px right margin at
≥1200px (collapsing into the column below 1200px) carries the
red annotations, the figure provenance captions, and the
reader's marks. Nothing in the margin is decoration; if a margin
note exists, a person (or the reader, §6.7) put it there, and it
is dated per §3 law 4.

---

## 5. Full motion system

One shared `requestAnimationFrame` loop drives every
scroll-scrubbed value on the page — strip deepening, fold
progress, counter interpolation, bracket drawing — with a single
lerp factor, `--loop-lerp: 0.12`, so all scrubbed motion settles
with the same instrument damping. Time-based loops are limited
to exactly two: new points arriving at the strip's edge (§6.2)
and the noise field's jitter (§6.8), both paused off-screen and
when the tab is hidden. Nothing else on the page moves on its
own. An observatory is a quiet room.

**Named easings (the theme's five).**

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-arrive` | `cubic-bezier(0.22, 1, 0.36, 1)` | A point lands on the curve and stays | Scatter draw-in, point arrivals |
| `--ease-dip` | `cubic-bezier(0.65, 0, 0.35, 1)` | Symmetric, unhurried — the U is traced, not dropped | Dip drawing, deepening |
| `--ease-fold` | `cubic-bezier(0.77, 0, 0.18, 1)` | Long slide, firm stop — epochs aligning | Phase-fold stacking, fold transition |
| `--ease-ink` | `cubic-bezier(0.33, 1, 0.68, 1)` | A pen stroke: quick start, decisive end | Annotations, brackets, error-bar draws |
| `--ease-settle` | `cubic-bezier(0.25, 1, 0.5, 1)` | Figures coming to rest | Counters, hovers, UI state changes |

**Every motion term, in this theme's language — applied or
refused with its reason.**

- **Scroll-triggered reveals** — the dip-deepening (§6.3): a
  section's arrival deepens its dip in the strip. Reveals are
  data changes, not entrances; prose itself never animates in —
  text on a chart is printed, and printed things do not fade up.
- **Scroll-driven / scrubbed animation** — the fold (§6.4) is
  the page's one great scrub: scroll position drives dip
  alignment continuously through the shared loop.
- **Parallax** — refused between layers of the same chart (a
  chart's layers must stay registered to its axes — parallax on
  data is a lie about position). The only permitted offset is
  the strip's scatter grain sitting 0.3× behind the strip's axis
  frame on scroll, inside the strip only, never moving a point
  relative to its epoch.
- **Pinned sections** — the strip itself is the pin (the whole
  page is its pinned scene); §6.12's folded profile pins for
  160vh while its residuals assemble. No other pins.
- **Smooth scrolling** — native, unmodified. The loop lerps the
  *values*, never the scroll position; the reader's hand stays
  on the page.
- **Progress indicator** — the strip's hour ruler fills with
  elapsed epochs (§6.2) and the fold counter counts transits
  folded. There is no progress bar; the observation *is* the
  progress.
- **Staggered reveals** — the scatter's time-ordered draw
  (§6.1): stagger with a physical meaning (time), 1,944 points
  in 2500ms. No other staggering anywhere.
- **Masked line reveals** — refused for prose (see above);
  permitted only for the baseline fit line drawing across a
  chart, left to right, once, as a model being fitted.
- **Blur-to-sharp** — refused. Photometry does not defocus; an
  unresolved dip is drawn *shallower with larger error bars*,
  which is the honest version of the same idea.
- **Kinetic typography** — refused except the hero headline
  settling into the dip (§6.1), where the type's position is the
  meaning. Letters never move elsewhere.
- **Marquee** — refused. A light curve does not loop; a looping
  chart would claim the star repeats for our convenience.
- **Counters** — §6.15: depth, period, SNR and transits-folded
  count as the fold accumulates, interpolating through the
  shared loop and stopping dead at the record's figures.
- **SVG line-draw** — error bars (§6.5), measurement brackets
  (§6.6), annotations' leader lines, the splice of the fold —
  all stroke-drawn with `--ease-ink` at stated durations.
- **Image scale-in-frame** — photographs (telescope, team,
  instrument) sit in figure frames ruled like chart plates and
  scale 1.04→1 on centre, the way a plate is examined; each is
  captioned with its epoch or its instrument, never bare.
- **Hover / magnetic / tilt micro-interactions** — hover is the
  measurement bracket (§6.6). Magnetic pull and tilt are
  refused: instruments do not lean toward the hand.
- **Custom cursor** — refused; the system cursor everywhere,
  with the OS-native `crosshair` on chart surfaces only (an
  unmodified system cursor, not a drawn one). The measurement
  bracket is drawn on the chart, never attached to the pointer
  as chrome.
- **Skeleton loading** — §6.16: an empty ruled chart with points
  arriving — the skeleton is the observation starting.
- **Page transitions** — the fold transition (§6.9).
- **Reduced motion** — every element carries its variant (§6);
  the global ruling: the full curve printed once, the fold shown
  already folded, every figure beside its section.

**Master timing table.**

| Beat | Duration | Easing | Driven by |
|---|---|---|---|
| Hero scatter draw (1,944 pts) | 2500ms | `--ease-arrive` | load, once |
| Hero dip trace | 900ms | `--ease-dip` | load, at 55% of draw |
| Dip deepening (per section) | 700ms | `--ease-dip` | shared loop, scrubbed |
| Fold slide (per transit) | 1100ms | `--ease-fold` | shared loop, scrubbed |
| Error-bar draw | 300ms | `--ease-ink` | hover / section centre |
| Annotation ink-in | 240ms | `--ease-ink` | mark / confirm |
| Counter settle | 600ms | `--ease-settle` | shared loop |
| Point arrival at strip edge | 1 per 900ms | `--ease-arrive` | time (instrument pace) |

---

## 6. Signature elements

### 6.1 The scatter that dips (hero)

- **What & why.** The hero is the whole run drawn as data: 1,944
  brightness points plot across a full-width chart in time
  order, and midway through the draw the points descend into one
  clean U — a transit, 300 ppm deep — and the page's single
  display headline fades in *inside the dip*: "SOMETHING PASSED
  IN FRONT OF THE STAR." It belongs because the headline is
  discovered the way the planet was: the reveal is the
  detection, and the copy sits in the only place the chart has
  room for it — the hole the planet made.
- **Structure.** One `<canvas>` (the scatter layer) over an SVG
  frame (axes, hour ruler, flux ticks, the baseline fit in
  `--baseline`). Points are drawn from the record's generated
  series (§6.17): epoch on x (124.000 → 144.250), relative flux
  on y (range +600 → −600 ppm over the hero's ~420px plot, so
  the 300 ppm dip is ~105px deep). The headline is a real DOM
  heading positioned inside the dip's x-range, below the
  baseline — HTML text, never canvas text, so it is selectable,
  searchable, and read by AT. The hero dip is T3 (epoch 134.940,
  the run's central transit) at its measured 295 ppm; the
  headline's fade is an opacity change on the DOM node only.
- **Motion spec.** Trigger: load, once. Points draw in time
  order over 2500ms under `--ease-arrive` (≈778 points/second,
  batched per frame by the shared loop — the draw is a
  progression of the plotted frontier, not 1,944 individual
  animations). At 55% of the draw (≈t=1375ms) the frontier
  reaches T3 and the dip traces over 900ms under `--ease-dip`;
  the headline fades in over 600ms beginning at t≈1900ms, as the
  dip completes. After the draw, the frontier hands over to
  §6.2's strip, which is already pinned above. Replays: never —
  a run is observed once; on revisit within the session the hero
  renders complete.
- **States.** Rest (complete run drawn, headline in the dip) /
  drawing (frontier advancing) / revisited (rendered complete,
  no draw) / reduced (printed complete, §below). The chart has
  no hover state of its own; figures inside it inherit §6.6.
- **Content merge.** The hero *is* the dataset the whole page
  annotates: same epochs, same depths, same point count as
  §6.17's record and §6.13's log. Remove the record and there is
  no hero — the element cannot be pasted onto another site,
  because its picture is this survey's evidence.
- **Failure fallback.** Watchdog at 4000ms: if the draw has not
  completed (blocked script, starved frames), the canvas is
  painted complete in one pass and the headline shown. No-JS:
  the server renders the full curve as a static SVG in the same
  frame, headline in the dip — the hero ships as a finished
  chart, and the draw is an enhancement layered over it. No
  point of the run can be stranded mid-air.
- **Reduced-motion variant.** No draw, no fade: the complete
  curve printed once, headline in place. The detection is
  presented as a result, which is what a printed paper does.
- **Performance budget & mobile variant.** One canvas, ≤1,944
  point fills total, DPR capped at 2; the draw writes only
  during its 2500ms and only while the hero is on-screen.
  Budget: ≤0.8ms/frame during the draw, 0 at rest. Mobile
  (<768px): plot height 260px, flux range widened to ±900 ppm
  (dip ~43px — shallower on paper, same ppm; the axis says so),
  point count unchanged (the record is not thinned for small
  screens; points are 1px and cheap), headline 27px set inside
  the dip in two lines.
- **Choreography timeline (v2).** t=0 first paint (frame, axes,
  ruler, empty plot, headline present but at rest opacity 0 —
  JS-armed only; no-JS and watchdog states show it) → t=120ms
  draw begins → t≈1375ms frontier reaches T3, dip traces (900ms)
  → t≈1900ms headline fades (600ms) → t=2500ms draw completes,
  final points land past T5 → t=4000ms watchdog deadline passes
  unused.
- **State matrix (v2).** *Rest:* complete curve, headline in
  dip. *Hover:* n/a on the field; §6.6 brackets apply to figure
  blocks below. *Focus:* the chart figure carries a mono caption
  link ("RUN LOG — TABLE", §6.13) as its focusable companion;
  the canvas itself is `role="img"` with a full text
  description. *Active:* n/a. *Scrolled-past:* canvas static,
  zero cost; the strip (§6.2) has taken over. *Disabled:* n/a.
  *Touch:* no draw change; the chart scrolls with the page.
- **Breakpoints (v2).** ≥1200px: plot 420px tall, dip ~105px,
  headline 44px one or two lines. 768–1199px: plot 340px,
  headline 34px. <768px: plot 260px, flux ±900 ppm, headline
  27px, the hour ruler shows every 2nd day tick (labels thinned,
  data never).
- **Edge cases & failure modes (v2).** *Slow network:* the
  series is generated client-side from the record's seed
  (§6.17) — no data fetch gates the hero; fonts lagging means
  the headline reflows once inside the dip's fixed box (the box
  is sized for the fallback font's wider measure; law §3.3 —
  copy fits the dip, not vice versa). *No canvas:* the static
  SVG fallback renders instead. *Very long headline from a
  client:* rejected at build time by the §10 gate's dip-fit
  check. *User scrolls during the draw:* the draw continues
  off-screen only until its 2500ms end (it is short), then the
  canvas is static; no work is queued behind scroll.
- **Accessibility spec (v2).** The figure is `role="img"` with
  `aria-label` summarising the record ("Light curve of K-85,
  1,944 points over 20.25 days; five transits of depth about
  300 parts per million, period 3.52 days"). The headline is the
  page's `<h1>`. The full data is one click away in §6.13's
  table — the chart is never the only carrier of its numbers.
  Contrast: points `--ink` on `--paper` 13.7:1; the dip fill is
  decorative over data already stated in text.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--indigo`,
  `--indigo-fill`, `--baseline`, `--grid`, `--grid-major`,
  `--ease-arrive`, `--ease-dip`, `--loop-lerp`, `--dur-draw`
  (2500ms), `--dur-dip` (900ms).

### 6.2 The pinned observation strip

- **What & why.** The light curve does not end at the hero: a
  90px strip carrying the entire run pins across the top of the
  viewport for the whole page, and scrolling *extends* the
  observation — new points keep arriving at its right edge at
  instrument pace while the strip's window compresses to hold
  the full run. It belongs because the graph is the page's sky:
  every section below is read under the star's ongoing record,
  and the reader always knows which transit they are inside.
- **Structure.** A fixed header-height band: `<canvas>` scatter
  layer (the full 1,944 points, redrawn on the shared loop only
  when a scrubbed value changes), an SVG overlay for the five
  dip profiles, fills, annotations and the fold zone at the
  right end (§6.4), and a DOM hour ruler along the foot (mono
  10.5px, epoch ticks every 1.0 d, labels every 2 d). Flux range
  in the strip: +1500 → −1500 ppm over 64px of plot, so a 300
  ppm dip is ~6.4px deep — small, honest, and exactly why the
  deepening (§6.3) and the fold (§6.4) exist. The right rail
  outside the plot (112px) shows the run clock: `EPOCH 138.460`
  — the epoch at the reading position — and the folded count.
- **Motion spec.** Trigger: scroll + time, for the page's whole
  length. New points arrive at the right edge one per 900ms
  under `--ease-arrive`, appended beyond epoch 144.250 and
  labelled by the ruler as the run extending — they are the
  star's honest noise continuing (drawn from the same seeded
  distribution, §6.8), never new transits. The reading-position
  epoch in the rail updates through the shared loop (lerp 0.12).
  Dip deepening and folding are §6.3/§6.4's, drawn on this
  strip's SVG overlay.
- **States.** Rest (run complete, arrivals continuing) /
  deepening (a section centred, §6.3) / folding (§6.4 active) /
  folded (profile assembled at the right end) / parked (tab
  hidden or page at footer: arrivals pause, strip holds). The
  strip is never in a hidden state.
- **Content merge.** The strip is not a progress decoration: it
  is the same record as the hero and the log, kept in view
  because the sections below are meaningless without their
  position in the run. Its dips are the sections' titles in data
  form (§6.3 locks them 1:1).
- **Failure fallback.** Watchdog at 3000ms: if the loop stalls,
  arrivals stop and the strip renders the run exactly as printed
  at load — complete, static, correct. No-JS: the strip ships as
  a static SVG of the full run with all five dips at full
  profile and the fold shown assembled in the fold zone. Print:
  the strip un-pins and prints once at the page head (§2).
- **Reduced-motion variant.** No arrivals, no deepening motion:
  the strip prints the full run with all dips at full profile
  and the folded profile assembled; the rail clock prints the
  section's epoch as the reader scrolls (a text change, not a
  motion).
- **Performance budget & mobile variant.** One canvas redraw
  only on scrub-change (not per frame at rest); arrivals add
  ≤2 points/second. Budget: ≤0.5ms/frame while scrolling, 0 at
  rest. Mobile (<768px): strip height 72px, plot 48px (dip
  ~4.8px — the deepening fill and annotation carry the signal,
  and the axis prints the scale so the smallness is honest), the
  rail clock moves under the ruler as a single mono line, ruler
  labels every 4 d.
- **Choreography timeline (v2).** Page load: strip present from
  first paint (it is the header) → hero draws beneath it (§6.1)
  → first scroll: rail clock begins tracking → T1 section
  centres: §6.3 deepening on this strip → each section end:
  §6.4 fold step at the strip's right end → footer reached:
  arrivals park, fold zone holds the finished profile.
- **State matrix (v2).** *Rest:* as above. *Hover:* hovering a
  dip in the strip brackets it (§6.6 applies here too) and the
  rail prints that transit's epoch and depth. *Focus:* each dip
  is a focusable link to its section ("T3 — epoch 134.940, depth
  295 ppm"); focus draws the same bracket. *Active:* activating
  a dip link scrolls to its section (native anchor; the loop
  settles the deepening on arrival). *Scrolled-past:* n/a — the
  strip is the fixed frame. *Disabled:* a dip whose section does
  not exist on the page is not rendered as a link (the record
  and the page are built from the same source, §6.17).
  *Touch:* tap on a dip = the link; arrivals and clock unchanged.
- **Breakpoints (v2).** ≥1200px: 90px strip, full ruler, rail
  clock at right. 768–1199px: 84px strip, ruler labels every
  2 d, rail clock retained. <768px: 72px strip as above; the
  fold zone keeps its width (the fold is the point of the page)
  and the plot compresses instead.
- **Edge cases & failure modes (v2).** *Long pages / many
  transits:* the strip window always shows the full run; beyond
  12 transits the dips would crowd — the theme caps a page at
  one run (§1); a second run is a second page (§6.9). *Tab
  hidden:* arrivals pause (visibilitychange) and resume without
  a catch-up burst — the instrument does not fabricate the
  missed points; the ruler marks the gap with a 4px paper break
  if the hidden interval exceeds 60s. *Reader jumps to the
  footer (End key):* the loop settles all scrubbed values to
  their final state within one frame of the jump landing — the
  fold appears assembled, never mid-slide (§13 jump rules).
- **Accessibility spec (v2).** The strip is a `banner`-adjacent
  figure with `role="img"` and a live text twin: a
  visually-hidden line, updated per section (not per frame),
  reads "Now reading transit 3 of 5, epoch 134.940." Dip links
  are real anchors with 40px-tall hit areas spanning the strip.
  The rail clock is `aria-hidden` (its information is in the
  twin). Flux scale is printed at the strip's left in mono —
  the chart's size claims are checkable by eye.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--indigo`,
  `--indigo-fill`, `--grey`, `--red`, `--grid-major`,
  `--ease-arrive`, `--loop-lerp`, `--dur-arrive` (900ms cadence).

### 6.3 Dip-deepening sections

- **What & why.** Each content section corresponds to one
  transit, and as the section centres in the viewport its dip in
  the pinned strip deepens from the strip's shallow ~6px trace
  to its full profile with a soft indigo fill — the chart
  equivalent of the room going quiet as the event is described.
  It belongs because text and data are locked 1:1: the reader
  always knows which transit they are reading about, and the
  strip always knows which section is being read.
- **Structure.** Each transit section carries `data-transit="T3"`
  and `data-epoch="134.940"`; the strip's SVG overlay holds one
  dip group per transit (path + fill). Deepening is a scrubbed
  value per transit, `d ∈ [0,1]`, computed in the shared loop
  from the section's distance to viewport centre; the dip path
  interpolates between its strip profile and its full profile
  (same epoch width, depth scaled from the strip's 3000 ppm
  range to a 900 ppm inset range drawn as an expanded callout
  profile within the strip — the strip grows a magnified inset
  of the current dip at its left end, axes labelled, rather than
  pretending the 90px strip can show 300 ppm at reading size).
  The section itself is plain printed prose and figures (§6.11's
  card, §6.5's error bars) — the motion lives in the strip.
- **Motion spec.** Trigger: scroll, scrubbed. `d` targets 1 as
  the section's centre crosses the viewport's middle band
  (40–60% of viewport height) and returns to 0 as it leaves;
  lerp 0.12 in the shared loop; the inset profile draws under
  `--ease-dip` character (the scrub supplies the timing; the
  easing shapes the path interpolation). Full deepen ≈700ms of
  scroll travel. Only one dip is deepened at a time — the loop
  enforces it arithmetically (sections are 90–110vh apart, §4).
- **States.** Rest (section off-centre, dip at strip profile) /
  deepening (0<d<1) / deepened (d=1, inset open, fill at full
  14%) / marked (the reader has marked this transit, §6.7 — the
  dip keeps a red annotation at any d) / scrolled-past (d→0, the
  dip remains at its folded state if §6.4 has taken it).
- **Content merge.** The deepening is not emphasis chrome: the
  inset it opens is the section's own chart at reading scale,
  carrying the section's figures (depth, epoch, duration). The
  section's first figure block and the inset print the same
  numbers from the same record — a reader who never looks up
  still gets every figure in the text.
- **Failure fallback.** Watchdog per section at 2000ms after
  first centre-crossing: if `d` has not reached 1 (loop
  starved), the inset is rendered open statically for the
  centred section. No-JS: every section prints its own static
  inset chart inline (the strip cannot deepen without the loop,
  so the charts move into the sections — no figure depends on
  the strip to exist).
- **Reduced-motion variant.** No scrub: when a section is the
  current one (per the scroll twin, §6.2), its inset is simply
  present — open or not, a state change with no transition. The
  strip marks the current dip with its fill at full opacity.
- **Performance budget & mobile variant.** One SVG path
  interpolation + one inset group per transit; only the active
  transit's values change per frame. Budget: ≤0.3ms/frame while
  scrolling. Mobile (<768px): the inset opens *below* the strip
  as a 120px chart band (the strip is too short to hold it);
  deepening still scrubs, figures identical.
- **Choreography timeline (v2).** Section approaches → its dip
  begins deepening as the section's top crosses 75% viewport
  height → d=1 as its centre crosses the middle band → inset
  fully open, fill settled → section end approaches: §6.4's fold
  step triggers for this transit → d hands over to the fold
  value; the dip's next state is "folded", not "rest".
- **State matrix (v2).** *Rest / deepening / deepened:* as
  above. *Hover:* hovering the section's figure block brackets
  the figures (§6.6) and raises the dip's fill to 20% — the two
  ends of the lock acknowledge each other. *Focus:* focus
  entering the section (heading link from the strip, §6.2)
  deepens its dip immediately (d set to 1 via the loop's fast
  path, 300ms). *Active:* n/a. *Scrolled-past:* d→0 or folded.
  *Disabled:* n/a. *Touch:* identical scrub; no hover raise.
- **Breakpoints (v2).** ≥1200px: inset inside the strip's left
  end, 260px wide. 768–1199px: inset 220px, strip plot
  compresses. <768px: inset as the under-strip band (above);
  sections shorten to 80–100vh so the lock still reads.
- **Edge cases & failure modes (v2).** *Reader scrolls fast:*
  d values chase through the loop and settle; a transit flashed
  past in <300ms never fully deepens — correct behaviour (it was
  not read), and its fold step (§6.4) still fires from the
  section-end threshold, so the fold cannot be skipped by speed.
  *Two sections near centre at a short viewport:* the loop picks
  the nearer centre; the other waits — the 1:1 lock is never
  ambiguous. *Section content much longer than 110vh:* the
  deepening holds at d=1 for the section's whole middle, defined
  by its centre's passage, not its edges.
- **Accessibility spec (v2).** The deepening is presentational;
  the section's heading announces the transit ("Transit 3 —
  epoch 134.940") as a real `<h2>`, and the visually-hidden twin
  (§6.2) names the current transit. The inset chart is
  `role="img"` labelled with its three figures. Nothing about
  the section's meaning waits for the strip.
- **Tokens consumed (v2).** `--indigo`, `--indigo-fill`,
  `--paper`, `--ink`, `--red`, `--ease-dip`, `--loop-lerp`,
  `--dur-deepen` (700ms).

### 6.4 Phase-fold stacking

- **What & why.** At each section's end, the strip performs the
  actual analysis: the transits so far slide horizontally —
  each dip travelling from its epoch position to the fold zone
  at the strip's right end — and stack into one sharp, deep
  profile, while the period readout assembles beside it:
  "P = 3.52 d". It belongs because certainty visibly
  accumulating *is* the story of a transit survey; the page does
  not announce the planet, it folds the evidence until the
  profile is undeniable, and the reader watched every transit
  that went into the stack.
- **Structure.** The fold zone is the strip's rightmost 300px,
  backed by `--plate` (the reduction plate intruding into the
  strip — reduced data is presented on the plate, §2). Each
  transit has a fold ghost: an SVG path copy of its dip that,
  under scrub, translates from its epoch x to the fold centre
  while its opacity steps 0.25 → 1 as it joins the stack; the
  stacked profile is the pointwise mean of the folded transits,
  redrawn per step — with one transit it is shallow and wide
  with ±48 ppm error shading; with five it is the record's sharp
  300 ppm profile with ±21 ppm shading; the final state (§6.12)
  adds the archive fold at ±9. The period readout is DOM mono
  text assembling digit-group by digit-group: `P = 3.5` after
  two transits (the spacing is measurable), `P = 3.52 d` from
  the third (the record's precision is earned at three epochs —
  stated in the caption, not hidden).
- **Motion spec.** Trigger: scroll thresholds at each section's
  end, scrubbed through the shared loop (fold progress `f ∈
  [0,1]` per transit, driven by the 30vh of scroll after the
  section's centre passes). Each transit's slide takes the
  scroll-equivalent of 1100ms under `--ease-fold` character.
  Folding is reversible: scrolling back up un-stacks the transit
  and returns its dip to its epoch — the analysis can be
  unwatched, and the profile shallows honestly as it loses
  members. The final (fifth) fold, at the fold section (§6.12),
  additionally draws the model fit and the SNR counter's run to
  33.3 (§6.15).
- **States.** Rest (no transits folded; zone shows the plate and
  the words `AWAITING TRANSITS` in mono) / folding (a ghost in
  transit) / stacked-n (profile of n members, error shading at
  48/√n ppm) / complete (five folded; the archive fold and
  confirmation live in §6.12) / reversed (scrolling up: members
  leave in reverse order).
- **Content merge.** The fold is the page's thesis rendered as
  its own chart: every member of the stack is a section the
  reader has read, at the depth the record measured. The period
  readout is not a stat callout — it is computed on the page
  from the epochs the reader passed. Remove any section and the
  profile visibly loses a member.
- **Failure fallback.** Watchdog at 2500ms after a fold
  threshold is crossed: if `f` has not settled, the ghost snaps
  to its stacked position (state correct, motion skipped).
  No-JS: the fold zone prints the finished five-transit profile
  with the period readout complete — the result without the
  performance. No state of the fold can leave a dip stranded
  between its epoch and the stack: the watchdog and the jump
  rules (§13) both settle to a member-or-not binary.
- **Reduced-motion variant.** No slides: at each section end the
  stacked profile simply gains its member (a state change), the
  error shading steps to its new width, and the readout updates.
  The accumulation — the meaning — is fully preserved.
- **Performance budget & mobile variant.** ≤5 ghost paths + 1
  profile path + shading on the strip's SVG; redrawn only while
  `f` changes. Budget: ≤0.4ms/frame during folds. Mobile
  (<768px): the fold zone keeps 300px by compressing the strip's
  plot (the run's early epochs clip behind a paper-edge fade
  with the ruler intact — the epochs are still labelled; the
  fold outranks the early baseline on a small screen, and §6.13's
  table carries the full run regardless).
- **Choreography timeline (v2).** Section end threshold →
  ghost detaches (opacity 0.25) → slides 1100ms-equivalent along
  the strip, passing the later epochs → arrives at fold centre,
  opacity 1 → profile redraws deeper/sharper, error shading
  narrows → readout updates (`P = …`, `n = 3 TRANSITS`) →
  next section begins with the stack one member stronger.
- **State matrix (v2).** *Rest / folding / stacked / complete:*
  as above. *Hover:* hovering the profile brackets its depth
  figure (§6.6) and prints `300 ± 21 ppm · n = 5`. *Focus:* the
  fold zone is reachable as a figure with a caption link to
  §6.12's full plate. *Active:* n/a. *Scrolled-past:* the stack
  persists (it is cumulative state, not a per-section effect) —
  the one scrubbed value on the page that does not reset by
  position alone, only by scrolling back above a fold threshold.
  *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: fold zone 300px on `--plate`.
  768–1199px: 260px, readout wraps under the profile.
  <768px: 300px retained (above); the strip's plot yields.
- **Edge cases & failure modes (v2).** *Reader jumps to the
  fold section directly:* all five folds settle assembled in one
  frame (§13) — the profile is correct, the performance is
  skipped, and §6.12's caption says the fold can be watched by
  scrolling the run. *A transit was never centred (jumped
  past):* its fold still fires from its section-end threshold
  during the jump settle — membership is by record, not by
  whether the reader lingered. *Record with a rejected transit:*
  a transit the survey rejected (systematic, not a planet) is
  never folded: its ghost is struck through in red at its epoch
  and the caption says why — the fold's honesty includes its
  exclusions.
- **Accessibility spec (v2).** The fold zone's text twin updates
  per fold step: "Three transits folded. Period 3.52 days.
  Depth 298 plus or minus 28 parts per million." The profile is
  `role="img"`; all its figures are printed in §6.12 and §6.13
  in text. No information exists only as the stack's shape.
- **Tokens consumed (v2).** `--plate`, `--paper`, `--indigo`,
  `--indigo-fill`, `--grey`, `--red`, `--ease-fold`,
  `--loop-lerp`, `--dur-fold` (1100ms).

### 6.5 Honestly shrinking error bars

- **What & why.** Every figure on the page carries its error
  bars, drawn to the scale of the axis they sit on — and as the
  fold accumulates, the bars shrink: the folded depth prints
  ±48 ppm after T1, ±34 after T2, ±28 after T3, ±24 after T4,
  ±21 after T5, and ±9 in the final archive fold. It belongs
  because this is the theme's anti-slop detail made structural:
  precision is not asserted, it is *earned*, visibly, at the rate
  statistics actually earns it — σ falls as 48/√n, and the page
  prints the n beside every bar so the reader can check the
  arithmetic.
- **Structure.** Each figure block (in §6.11's cards, §6.15's
  rail, §6.12's plate, §6.13's table) renders its value as DOM
  mono text (`298 ± 28 ppm`) plus an SVG bar: a horizontal rule
  centred on the value's position within a printed scale track,
  capped with 6px end ticks, in `--grey`, its half-width exactly
  σ at the track's stated ppm-per-pixel. The scale track itself
  is printed (0 / 150 / 300 / 450 ppm ticks) — a bar without a
  scale is decoration and is forbidden. The folded-figure blocks
  update their σ as folds land (§6.4); per-transit figures keep
  their own transit's σ (48 each — a single transit's depth is
  always ±48 in this record, and the spec forbids quietly
  lending the fold's precision to a single event).
- **Motion spec.** Trigger: per section / per fold. When a
  folded figure's σ steps down, the bar's half-width animates
  from the old σ to the new over 450ms under `--ease-ink` (a
  redraw, like an annotator correcting a bar), and the mono
  figure crossfades to the new value at the animation's midpoint.
  On first appearance in a section, bars draw in over 300ms
  under `--ease-ink` as the section centres (with §6.3's
  deepening). Bars never animate on hover — hover brackets
  (§6.6); the bar is data, not feedback.
- **States.** Rest (bar at current σ) / stepping (a fold landed,
  bar redrawing to smaller σ) / single-transit (bar at ±48,
  labelled `SINGLE TRANSIT`) / final (archive fold, ±9, labelled
  `n = 28, INCL. 23 ARCHIVED`). A bar's state is always labelled
  with its n — an unlabelled bar fails §10.
- **Content merge.** The bars are the figures' honesty made
  visible; the page's argument ("certainty is earned") is
  literally drawn by them. They cannot be removed without the
  page losing its thesis, and they cannot be pasted onto a page
  whose numbers have no n.
- **Failure fallback.** Watchdog at 1500ms: a stepping bar that
  has not settled snaps to the new σ (the value text updates
  with it — text and bar can never disagree; they are written in
  the same frame). No-JS: bars print at their section's σ as
  static SVG. The figure text always carries the ± in words, so
  a bar that never draws loses nothing but the picture.
- **Reduced-motion variant.** No draw-in, no stepping animation:
  bars appear at their σ; when a fold lands, the bar and figure
  change state instantly at the section boundary.
- **Performance budget & mobile variant.** Pure SVG geometry,
  ≤12 bars live per page view; redraw only on fold events.
  Budget: ≤0.1ms/frame, event-driven. Mobile (<768px): the scale
  track compresses to 0 / 300 ppm end ticks only (mid ticks
  dropped, σ unchanged — the scale prints its compression);
  bars remain full-width in the figure block.
- **Choreography timeline (v2).** Section centres → its folded
  figure's bar draws in (300ms) at the σ for the transits so far
  → section end: fold lands (§6.4) → the *next* section's figure
  will print the smaller σ; the rail's bar (§6.15) steps down
  live (450ms) as the ghost docks → final fold: bar steps to
  ±9 and the `n = 28` label inks in.
- **State matrix (v2).** *Rest / stepping:* as above. *Hover:*
  the bar's figure gets §6.6's bracket; the bar itself does not
  move. *Focus:* figure blocks are not focusable; their values
  are text. *Active:* n/a. *Scrolled-past:* bars hold their σ —
  precision, once earned on the page, is not un-earned by
  scrolling (the fold's ratchet is §6.4's reverse rule: bars
  step back up only if the reader scrolls back above the fold
  threshold that earned them). *Disabled:* n/a. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: full scale track with four
  ticks. 768–1199px: track narrows, ticks at 0 / 150 / 300 / 450
  retained. <768px: two end ticks (above); bar geometry
  unchanged.
- **Edge cases & failure modes (v2).** *A figure whose σ exceeds
  the track:* the track's range is a build-time property of the
  record (max σ = the single-transit 48, track to 450 ppm
  value + 60 ppm headroom); a record that overflows fails the
  §10 figure audit at build, not at runtime. *Rounding:* σ
  prints as the record's rounded integers (48, 34, 28, 24, 21,
  9) and the bar is drawn from the same rounded value — bar and
  text can never disagree by a rounding residue. *The archive
  step (21 → 9) is the largest on the page* and is always
  captioned with its reason (`INCL. 23 ARCHIVED TRANSITS`) — a
  big precision jump without a stated cause is exactly the lie
  this element exists to prevent.
- **Accessibility spec (v2).** Every bar's value is in the DOM
  text (`298 ± 28 ppm`); the SVG is `aria-hidden`. The n label
  is text. A greyscale print keeps bar and scale legible (grey
  on paper is drawn, and its meaning is duplicated in the ±
  figure — §2's ruling).
- **Tokens consumed (v2).** `--grey`, `--ink`, `--grid-major`,
  `--ease-ink`, `--dur-bar` (300ms), `--dur-step` (450ms).

### 6.6 Measurement-bracket hover

- **What & why.** Hovering any figure on the page — a depth, a
  period, an epoch — brackets it with a measurement cursor: two
  corner ticks close around the figure and its error bars draw
  in, the chart's own notation for "this is being measured." It
  belongs because inspection in this theme uses the science's
  grammar: to look closely at a number is to bracket it and show
  its uncertainty, not to underline it in a brand colour.
- **Structure.** A figure block is a `<span class="fig">` or
  figure element carrying `data-value`, `data-sigma`, `data-n`.
  The bracket is an SVG overlay pair (⌐ ¬ corners) positioned to
  the figure's box, stroke `--ink` 1.5px; beneath it, the
  figure's error bar (§6.5's component, miniaturised to the
  figure's own scale strip if not already present) draws in.
  The bracket is drawn, never a background or border — borders
  would move layout; ink must not.
- **Motion spec.** Trigger: hover (pointer) or focus. Corners
  stroke-draw over 300ms under `--ease-ink`, error bar with
  them; on leave, both fade over 180ms under `--ease-settle`
  (ink dries slower than it lifts — no, it lifts faster: the
  measurement ends, the chart returns). One bracket at a time
  per page; moving between figures hands the bracket over
  without a gap frame.
- **States.** Rest (no bracket) / bracketing (drawing in) /
  bracketed (figure + bars shown; a mono readout beside the
  figure prints `σ = 28 ppm · n = 3` if not already adjacent) /
  leaving (fading). Figures inside the strip (§6.2) and the fold
  (§6.4) bracket identically.
- **Content merge.** The bracket reveals the figure's own
  uncertainty — content that belongs to the figure, hidden only
  until asked. It decorates nothing: a figure without a σ in the
  record (a label, a date) does not bracket.
- **Failure fallback.** Watchdog at 1200ms: a bracket stuck
  mid-draw (pointer events lost) fades out. No-JS / no-hover:
  every figure's σ is already printed beside it in the figure
  blocks (§6.5's ruling) — the bracket is an emphasis, never the
  only carrier. Touch: tap = bracket until tap elsewhere.
- **Reduced-motion variant.** The bracket appears and disappears
  as a state change (opacity step, no draw). The error bar is
  already printed (per §6.5's variant).
- **Performance budget & mobile variant.** Two SVG paths + one
  bar per bracket; transform/opacity only. Budget: negligible,
  event-driven. Mobile (<768px): brackets trigger on tap only;
  corner size grows to 10px so the bracket reads at small
  scales; the σ readout moves below the figure (no room beside).
- **Choreography timeline (v2).** Pointer enters figure →
  corners begin drawing (300ms) → error bar completes with them
  → readout prints at t=300ms → hold while hovered → pointer
  leaves → 180ms fade → chart clean.
- **State matrix (v2).** *Rest / bracketed:* as above. *Hover:*
  the trigger. *Focus:* keyboard focus on a figure's companion
  link (§6.11 cards, §6.13 rows) brackets the same figure —
  keyboard readers get the measurement too. *Active:* n/a (click
  belongs to §6.7 on transit charts). *Scrolled-past:* a bracket
  on a figure that scrolls off is released. *Disabled:* figures
  from a rejected transit (§6.4) bracket in red — the bracket
  itself carries the rejection. *Touch:* tap toggles.
- **Breakpoints (v2).** ≥1200px: readout beside the figure.
  768–1199px: readout beside, smaller (11px). <768px: readout
  below (above).
- **Edge cases & failure modes (v2).** *Figure wraps two lines:*
  the bracket boxes the figure's full box, corners at the outer
  corners — a bracket around half a number would misstate what
  is measured. *Rapid pointer sweeping across a table:* bracket
  hand-over is debounced 60ms so a sweep does not strobe the
  chart. *Print:* brackets never print; the σ text does.
- **Accessibility spec (v2).** The bracket is `aria-hidden`
  emphasis; the σ and n it reveals are present in the DOM for
  every figure regardless (visually adjacent in figure blocks,
  or in the figure's `aria-label` for inline figures: "depth
  298 parts per million, plus or minus 28, from 3 transits").
  Focus-visible figures get a 2px `--indigo` outline in addition
  to the bracket (the bracket alone is too quiet for focus).
  Touch target: the figure's hit area is its full line box,
  ≥40px tall in cards and tables.
- **Tokens consumed (v2).** `--ink`, `--grey`, `--indigo`,
  `--red`, `--ease-ink`, `--ease-settle`, `--dur-bracket`
  (300ms).

### 6.7 Click-to-mark a transit

- **What & why.** Clicking a section's chart marks its transit:
  the strip's dip deepens, holds its fill, and an annotation
  inks in beside it in red — "T3 — CONFIRMED". It belongs
  because marking transits by eye is the actual work of a
  citizen-science survey; the reader is not consuming the
  detection, they are *vetting* it, and the page keeps their
  marks the way a chart keeps an annotator's pencil — visibly,
  in red, dated with the epoch.
- **Structure.** Each transit section's inset chart (§6.3)
  carries a real `<button class="mark">` styled as a mono
  annotation-in-waiting: `MARK THIS TRANSIT`. On mark: the
  strip's dip for that transit gains a persistent state
  (fill locked at 20%, a red tick at its epoch on the ruler),
  and the annotation text `T3 — CONFIRMED` inks in beside the
  dip in the strip and beside the section's heading in the
  margin (§4). Marks persist in `sessionStorage` for the visit
  (the annotator's pencil survives a page transition, §6.9, but
  is not stored beyond the session — a mark is a working note,
  not an account). The marked count feeds §6.15's rail
  (`MARKED 2 / 5`).
- **Motion spec.** Trigger: click/tap/Enter on the mark button.
  The annotation inks in over 240ms under `--ease-ink`
  (stroke-drawn tick + text fade, pen-paced); the strip dip's
  fill rises to its locked value over 450ms under `--ease-dip`.
  Unmarking (second click) reverses at the same durations and
  the annotation fades — a struck mark remains faintly visible
  at 30% for the rest of the visit (pencil erased is still a
  smudge; the chart remembers that a judgement was made and
  withdrawn — §9 forbids silently clean reversals).
- **States.** Unmarked (button offered) / marking (ink-in) /
  marked (annotation printed, dip locked, button now reads
  `UNMARK T3`) / unmarked-after (smudge state, button offered
  again) / pre-marked (a transit the survey itself has confirmed
  in the record — in the worked record, none: confirmation is
  the fold's, §6.4; a record may pre-mark, and then the button
  is absent and the annotation is printed, not drawn).
- **Content merge.** The mark acts on the data itself — the dip
  in the strip changes state — and the annotation joins the
  chart's margin record. It is the one interaction on the page
  and it is the survey's real gesture; nothing about it is a
  like button in costume.
- **Failure fallback.** Watchdog at 1500ms: a mark whose strip
  update has not landed applies the strip state instantly (the
  section's annotation is the primary record of the mark; the
  strip follows). No-JS: the button is absent and the sections
  print the survey's own vetting status from the record
  (`VETTED — SURVEY TEAM`) where the record carries one. A mark
  can never be lost between the click and the chart: the button's
  own label flips in the same frame as the click.
- **Reduced-motion variant.** No ink-in: the annotation appears,
  the fill steps to locked. The smudge rule still applies.
- **Performance budget & mobile variant.** One text node + one
  SVG group per mark; ≤5 marks. Budget: negligible. Mobile
  (<768px): the mark button is full-width under the section's
  chart (44px tall), the annotation inks in the under-strip
  band's inset (§6.3's mobile position) as well as the margin.
- **Choreography timeline (v2).** Click → button label flips
  (same frame) → red tick draws at the epoch (240ms) →
  annotation text inks in beside the dip → dip fill rises
  (450ms) → rail's marked count steps (§6.15) → the fold, when
  this transit's turn comes, folds a marked dip with its tick
  riding (§6.4 — the reader's judgement enters the stack
  visibly).
- **State matrix (v2).** *Rest (unmarked) / marked / smudged:*
  as above. *Hover:* the button underlines in red over 120ms —
  the pencil hovers. *Focus:* 2px `--red` outline, offset 2px
  (red is correct here: focus is on the annotator's tool).
  *Active:* pressed state = tick half-drawn. *Scrolled-past:*
  marks persist in the strip regardless of section position.
  *Disabled:* a rejected transit (§6.4) cannot be marked; its
  button is replaced by the printed rejection note.
  *Touch:* tap = click; no hover underline.
- **Breakpoints (v2).** ≥1200px: annotation in the right margin
  beside the heading. 768–1199px: margin collapses; annotation
  inks in under the heading. <768px: full-width button (above);
  annotation under the heading.
- **Edge cases & failure modes (v2).** *Reader marks all five:*
  the rail prints `MARKED 5 / 5` and the fold section's caption
  acknowledges the completed vetting — but the page never
  upgrades the reader's marks into the survey's confirmation;
  the fold's SNR does that, and §12's copy rules keep the two
  words apart (`CONFIRMED` the event, never `PLANET CONFIRMED`
  before §6.12). *Session storage unavailable:* marks live in
  memory for the page view and are lost on navigation — the
  §6.9 transition warns of nothing; the loss is acceptable
  because a mark is a working note (§above), and the button
  states re-derive from memory only. *Double-click:* the second
  click is the unmark — intended, and the smudge records it.
- **Accessibility spec (v2).** The button's accessible name
  carries the transit and epoch ("Mark transit 3, epoch
  134.940"). Marking announces via a live region: "Transit 3
  marked confirmed." The strip annotation is `aria-hidden` (the
  announcement and the section's printed status carry it). The
  marked state is never colour-only: the word CONFIRMED is
  printed.
- **Tokens consumed (v2).** `--red`, `--indigo-fill`, `--ink`,
  `--ease-ink`, `--ease-dip`, `--dur-ink` (240ms),
  `--dur-lock` (450ms).

### 6.8 Noise-honest scatter field

- **What & why.** The page's background texture is scatter —
  but it twinkles only at measurement-noise amplitude: each
  point jitters vertically by at most ±1σ of the record's noise
  (a few ppm rendered as sub-pixel to ~1.5px), generated from a
  seeded distribution so it is visibly random and never
  sparkly. It belongs because even the wallpaper in this theme
  refuses to lie about what noise looks like: real photometry
  noise is small, grey, and boring, and a page that makes its
  noise beautiful has misunderstood its subject.
- **Structure.** A `<canvas>` fixed behind the reading column's
  figure areas (never behind body text — text sits on clean
  paper, §4), holding ~600 points placed on the graph grid's
  major intersections in the margins and figure gutters. Points
  are 1.5px `--grey` at 60% opacity. Jitter is computed from the
  record's seed (§6.17): a mulberry32 stream, each point's
  offset a gaussian sample clamped to ±1σ, re-sampled on a slow
  cycle. The hero and strip have their own data scatter (§6.1,
  §6.2); this field is only the margins' texture, and it is
  labelled nowhere because it claims nothing.
- **Motion spec.** Trigger: time. Each point re-jitters on a
  1400ms cycle, offset per point by its seed so the field never
  pulses in unison; the move itself is a 300ms `--ease-settle`
  glide of ≤1.5px. The field pauses off-screen (it is behind
  everything; an IntersectionObserver on the figure areas gates
  it) and when the tab is hidden. Amplitude is a hard cap in
  code, not a style choice: `min(σ_px, 1.5px)`.
- **States.** Rest (jittering at noise amplitude) / paused
  (off-screen, hidden tab, reduced motion) / printed (print and
  no-JS: points static at their seeded positions — the texture
  survives as a still).
- **Content merge.** The field is the record's noise floor made
  ambient: same seed, same σ as the data scatter. It is the one
  decorative element the theme permits itself, and it is
  permitted only because it is *the data's own texture* at the
  data's own amplitude — remove the record and the field has no
  distribution to draw from.
- **Failure fallback.** Watchdog at 3000ms: if the jitter loop
  has not run, the canvas stays at its first static paint —
  indistinguishable from the intended still. No-JS: the field is
  a static SVG scatter printed in the gutters. There is no state
  in which the field's failure hides or corrupts content: it is
  behind figure areas only, at 60% grey.
- **Reduced-motion variant.** Fully static: points at seeded
  positions, no jitter. (This is the variant where the theme's
  discipline is most visible — the still field and the moving
  field differ by ≤1.5px.)
- **Performance budget & mobile variant.** One canvas, ~600
  points, redrawn at most every 1400ms in small batches.
  Budget: ≤0.2ms/frame amortised. Mobile (<768px): the field is
  cut entirely (gutters are too narrow to hold it honestly) —
  margins print clean paper; this is the budget's first cut
  (§14) at every size if frames run long.
- **Choreography timeline (v2).** First paint: static seeded
  field → JS arms → jitter cycles begin per point (staggered by
  seed) → continuous, ≤1.5px, forever, until paused by state.
- **State matrix (v2).** *Rest / paused / printed:* as above.
  *Hover / focus / active:* none — the field is inert and
  `pointer-events: none`. *Scrolled-past:* gutters scroll with
  the page (the field is in-flow behind figure areas, not
  fixed); off-screen areas pause. *Disabled:* n/a. *Touch:* no
  interaction.
- **Breakpoints (v2).** ≥1200px: full field in margins and
  gutters. 768–1199px: field only in figure gutters (margins
  have collapsed). <768px: cut (above).
- **Edge cases & failure modes (v2).** *A point drifting over
  text:* impossible by construction — the canvas is clipped to
  gutter regions, and jitter is vertical ≤1.5px within them.
  *Seed collision with the data scatter:* the field uses the
  record's seed + a fixed salt, so its randomness is related to
  but never identical to the hero's series (a visitor must not
  "recognise" margin noise in the data). *Low-power device:*
  `hardwareConcurrency ≤ 2` or a save-data hint renders the
  field static from the start.
- **Accessibility spec (v2).** `aria-hidden`, no role, no text.
  The jitter's amplitude and slowness keep it outside
  photosensitivity concern (≤1.5px, no luminance flash, no
  periodicity above 1 cycle/1.4s per point); it still honours
  reduced-motion by stopping entirely.
- **Tokens consumed (v2).** `--grey`, `--grid-major`,
  `--ease-settle`, `--dur-jitter` (1400ms cycle).

### 6.9 Fold transition (page transition)

- **What & why.** Moving between pages phase-shifts: the strip
  folds — the current page's transits slide into the fold zone —
  the content crossfades at the fold, and the next page's run
  unfolds from its strip. It belongs because navigation in this
  theme should use the method's own gesture: you do not "go to"
  another observation, you fold this one and open the next.
- **Structure.** A client-side transition layer over the strip
  (§6.2) and the reading column: on navigation, the strip's SVG
  runs a compressed fold (all unfolded transits ghost to the
  fold zone over 500ms), the column crossfades (opacity, 240ms)
  at the fold's midpoint, and the incoming page renders with its
  strip already assembled to that page's scroll state (top of
  page: unfolded, hero drawing per §6.1). Marks (§6.7) persist
  across the transition via session state. Full reloads (no
  client router) skip the transition entirely — the fold is an
  enhancement of navigation, never a requirement of it.
- **Motion spec.** Trigger: navigation (in-app links). Total
  740ms: fold 500ms under `--ease-fold`, crossfade centred at
  t=370ms over 240ms under `--ease-settle`, unfold of the new
  strip's state 0ms (it arrives assembled — unfolding is the
  hero draw's job, §6.1). The browser's own navigation is never
  delayed beyond the 740ms; a slow incoming page holds at the
  folded state with §6.16's skeleton below the strip.
- **States.** Idle / folding / held (incoming page not ready;
  skeleton shows) / unfolding (new page painting) / aborted
  (navigation cancelled or failed — the fold reverses, 300ms,
  and the current page is untouched; a failed navigation must
  never leave the reader between runs).
- **Content merge.** The transition is performed by the strip —
  the page's own instrument — on the page's own data. It cannot
  be reused on a site without a fold, which is the point.
- **Failure fallback.** Watchdog at 2000ms: any transition state
  older than 2000ms forces completion (new page shown) or abort
  (old page restored) — the reader is never held on a folded
  strip. No-JS: plain navigation, full loads, zero loss.
- **Reduced-motion variant.** No fold, no crossfade: navigation
  is instant; the new page's strip arrives assembled.
- **Performance budget & mobile variant.** Reuses the strip's
  SVG and one opacity on the column. Budget: ≤0.3ms/frame during
  its 740ms. Mobile (<768px): identical (the strip is the
  header at every size); the crossfade shortens to 180ms.
- **Choreography timeline (v2).** Link activated → fold begins
  (transits ghost right, 500ms) → t=370ms column crossfades →
  new page's strip present, hero begins (§6.1) → transition
  layer releases at t=740ms → watchdog deadline t=2000ms passes
  unused.
- **State matrix (v2).** *Rest (idle) / folding / held /
  aborted:* as above. *Hover / focus:* links behave normally;
  focus is moved to the new page's `<h1>` on completion (and
  announced, below). *Active:* the activated link prints its
  destination's run name in the strip's rail during the fold —
  the reader sees which run they are opening. *Scrolled-past:*
  n/a. *Disabled:* external links and downloads never fold —
  they leave the observatory by the door, not the fold.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px / 768–1199px / <768px: as above;
  only the crossfade duration changes at <768px.
- **Edge cases & failure modes (v2).** *Back button during a
  fold:* the transition aborts to whichever page history
  settles on; state is derived from the page, never from the
  transition. *Two rapid navigations:* the second supersedes;
  the fold restarts from the current strip state — folds never
  queue. *Prefetch:* in-app links may prefetch, but the fold
  still runs its 740ms — the gesture is the brand, not a
  loading screen, and it never pretends to be waiting for data
  it already has (if prefetched, the held state is skipped).
- **Accessibility spec (v2).** During the fold, the outgoing
  page is `aria-hidden` at the crossfade point and the incoming
  page's title is announced ("Observation run — K-85, continued:
  the fold"). Focus lands on the new `<h1>`. Reduced-motion and
  screen-reader users get plain navigation semantics — the
  transition is decorative state over a normal route change.
- **Tokens consumed (v2).** `--plate`, `--indigo`,
  `--ease-fold`, `--ease-settle`, `--dur-transition` (740ms).

### 6.10 Masthead & run navigation

- **What & why.** Above the strip sits a slim masthead — the
  survey's name in Spectral, the run's identity in mono
  (`K-85 · FIELD 7 · RUN 124.000–144.250`) — and the navigation
  is the strip itself: the five dips are the five section links,
  supplemented by a mono text row (RUN / TRANSITS / THE FOLD /
  LOG / JOIN) for the page's non-transit destinations. It
  belongs because in this theme the table of contents *is* the
  dataset: you navigate the page by epoch, the way you would
  navigate the run itself.
- **Structure.** Masthead: 48px band, `--paper`, bottom rule in
  `--grid-major`; left, the survey wordmark (Spectral 20px);
  right, the run identity (mono 11px, `--ink-soft`). Below it,
  the strip (§6.2) with its dip links. Below the strip, the mono
  nav row (13px, uppercase, 0.06em tracking) with the current
  destination underlined by a drawn rule. On non-run pages
  (about, method), the strip persists with the run it belongs
  to — the observatory's sky does not change because you walked
  into the office — and the nav row marks the current page.
- **Motion spec.** Trigger: scroll / navigation. The nav row's
  underline draws to the current item over 240ms under
  `--ease-ink` as sections change (scrollspy driven by the same
  centre-band test as §6.3). Masthead itself: no motion, ever —
  the nameplate does not perform.
- **States.** Rest / current (a nav item underlined; a dip
  deepened per §6.3) / marked (a dip carrying §6.7's red tick —
  navigation shows the reader's own annotations) / folded (dips
  taken by §6.4 render at the fold, and their strip positions
  show a small mono `FOLDED` tick on the ruler).
- **Content merge.** The navigation's primary items are data
  (epochs with depths in their labels, §6.2's dip links); a
  visitor learns the run's shape from the menu alone. The text
  row exists because not every destination is a transit — and
  it is deliberately secondary, in the chart's label type.
- **Failure fallback.** Watchdog: the scrollspy underline is
  decorative state; if the loop stalls it freezes on the last
  item — navigation itself is plain anchors and cannot fail.
  No-JS: no underline animation; the current page's item is
  server-marked with `aria-current` and a printed underline.
- **Reduced-motion variant.** The underline steps between items
  without drawing. Dip links behave identically.
- **Performance budget & mobile variant.** One SVG line + text.
  Budget: negligible. Mobile (<768px): the masthead's run
  identity truncates to `K-85 · RUN 20.25 D` (the full window is
  one tap away in §6.13); the nav row scrolls horizontally as a
  snap row; the strip remains the primary nav.
- **Choreography timeline (v2).** Page load: masthead and strip
  present at first paint → first scroll: scrollspy arms →
  section changes: underline draws (240ms) in step with §6.3's
  deepening → fold events add `FOLDED` ticks as they land
  (§6.4).
- **State matrix (v2).** *Rest / current:* as above. *Hover:* a
  nav item's label brackets lightly (corners only, §6.6's
  grammar at half weight). *Focus:* 2px `--indigo` outline on
  the item; focusing a dip link deepens its dip (§6.2).
  *Active:* pressed item inks its underline instantly.
  *Scrolled-past:* n/a (fixed). *Disabled:* a destination not in
  this build is not rendered — the nav is generated from the
  site's page list, never hand-maintained. *Touch:* tap targets
  44px tall on the row.
- **Breakpoints (v2).** ≥1200px: full masthead + row. 768–1199px:
  run identity shortens (`K-85 · FIELD 7`). <768px: as above.
- **Edge cases & failure modes (v2).** *Long survey names:* the
  wordmark truncates with an ellipsis at 40vw — the run identity
  never truncates first (the data outranks the brand, §3 law 3's
  cousin). *Pages outside the run (about):* scrollspy idles; the
  row underlines the page; the strip still folds nothing.
- **Accessibility spec (v2).** `<nav>` with an aria-label
  ("Observation run"); dip links named with transit, epoch and
  depth (§6.2); `aria-current` on the active item; the masthead
  identity is plain text. Skip-link lands below the strip — the
  strip is 90px of the reader's time and the skip link respects
  it.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--ink-soft`,
  `--indigo`, `--red`, `--grid-major`, `--ease-ink`,
  `--dur-spy` (240ms).

### 6.11 Transit record cards

- **What & why.** Each transit also exists as a card — a ruled
  figure plate carrying its epoch, measured depth with error
  bar, duration, single-transit SNR, and vetting status — used
  in the transit sections and in the candidates listing (§7).
  It belongs because a survey's findings must be *fileable*:
  the card is the chart's data cut into a record a reader can
  scan, compare, and cite, with the uncertainty printed on its
  face, not in a footnote.
- **Structure.** A DOM card on `--paper` (or `--paper-deep` by
  section parity), framed by `--grid-major` rules, header row in
  mono (`T3 · EPOCH 134.940`), a mini light-curve SVG (the
  transit's own 2.1 h window: ±3 h of baseline either side, 49
  points at cadence, the dip at measured depth, flux range
  ±600 ppm printed), then the figure rows: `DEPTH 295 ± 48 ppm`
  with §6.5's bar, `DURATION 2.1 h`, `SNR (SINGLE) 6.1`, and the
  status line — `UNMARKED` / `CONFIRMED — READER` (§6.7) /
  `FOLDED n = 3` as states accrue. Cards are generated from
  §6.17's record; a card for a transit not in the record cannot
  be built.
- **Motion spec.** Trigger: scroll into view. The mini-curve's
  points arrive over 600ms under `--ease-arrive` in time order
  (a pocket §6.1), the dip traces at its end over 300ms under
  `--ease-dip`; the error bar draws with §6.5's 300ms. Cards in
  a listing stagger by transit order — which is time order; the
  stagger is the chronology, never a cascade for its own sake.
- **States.** Rest (printed, mini-curve complete) / arriving
  (first view) / marked (§6.7 state mirrored: red status) /
  folded (status line updates as §6.4 takes the transit) /
  rejected (record-flagged: the mini-curve's dip is struck in
  red and the status reads `REJECTED — SYSTEMATIC`, §6.4).
- **Content merge.** The card is a window into the same record
  as the strip: its mini-curve's dip is the strip's dip at the
  same epoch and depth, drawn at reading scale. A reader who
  only reads cards has still read the data — every figure on the
  card is in the strip and the log.
- **Failure fallback.** Watchdog at 2000ms: a card whose
  mini-curve has not drawn renders it complete. No-JS: static
  SVG mini-curve, all figures printed. The card's text never
  waits for its chart.
- **Reduced-motion variant.** Mini-curve printed complete; no
  arrival. Status changes are state changes.
- **Performance budget & mobile variant.** ≤5 cards per page
  (one run), each one small SVG (~49 points). Budget: ≤0.2ms/
  frame during arrivals. Mobile (<768px): cards stack single-
  column; the mini-curve keeps its full width (it is the card's
  evidence; the figure rows wrap instead).
- **Choreography timeline (v2).** Card enters viewport → points
  arrive (600ms) → dip traces (300ms) → error bar draws (300ms,
  overlapping the trace's second half) → status line prints →
  card at rest, identical in content to its no-JS form.
- **State matrix (v2).** *Rest / arriving / marked / folded /
  rejected:* as above. *Hover:* the card's depth figure brackets
  (§6.6); the mini-curve's dip fills to 20%. *Focus:* the card's
  heading is a link to its section; focus brackets the depth.
  *Active:* n/a. *Scrolled-past:* static. *Disabled:* n/a.
  *Touch:* tap on the figure = bracket; the heading link is the
  card's only navigation.
- **Breakpoints (v2).** ≥1200px: cards in sections full-column
  width (max 720px); in listings, ≤3 across (§4). 768–1199px:
  listings 2 across. <768px: 1 across, figure rows stack.
- **Edge cases & failure modes (v2).** *A transit with a
  shallower depth (a grazing candidate in another record):* the
  mini-curve's flux range is per-record fixed (§6.5's build
  rule), so a 90 ppm dip draws honestly small — the card never
  rescales one transit to look like another. *Missing duration
  in a record:* the row prints `DURATION — NOT MEASURED` (a
  dash and words, never an invented figure).
- **Accessibility spec (v2).** Card figures are text; the
  mini-curve is `role="img"` labelled ("Transit 3, epoch
  134.940: dip of 295 parts per million lasting 2.1 hours").
  Status is words, not colour. The heading link's name includes
  the transit ID.
- **Tokens consumed (v2).** `--paper`, `--paper-deep`, `--ink`,
  `--indigo`, `--indigo-fill`, `--grey`, `--red`,
  `--grid-major`, `--ease-arrive`, `--ease-dip`, `--dur-card`
  (600ms).

### 6.12 The folded profile plate (detail / confirmation)

- **What & why.** After the run's sections, the page arrives at
  the reduction plate: a full-width dark panel where the folded
  profile stands at reading scale — all five transits stacked,
  the model fit drawn through them, the residuals plotted
  beneath, and the final figures printed with the archive fold's
  ±9 ppm. This is the page's confirmation scene: the planet is
  claimed here, and only here, because here is where the
  evidence is complete. It belongs because a detection deserves
  a plate, not a banner — the claim and its proof in one frame,
  at the size an astronomer would print it.
- **Structure.** A `--plate` panel, pinned for 160vh (§5) while
  its layers assemble. Inside: the phase-folded chart (x: phase
  −0.06 → +0.06 of period; y: flux +400 → −500 ppm), the stacked
  points in `--paper` at 70%, the mean profile in `--paper`, the
  trapezoid model fit in `--baseline`, residuals below in
  `--grey` with their own ±30 ppm axis, and the figure block:
  `DEPTH 300 ± 9 ppm`, `P = 3.52 d`, `T14 = 2.1 h`, `SNR 33.3`,
  each with §6.5 bars at plate scale, and the caption: `FOLDED
  FROM 5 TRANSITS ON THIS PAGE + 23 ARCHIVED · n = 28`. The
  announcement prose sits *below* the plate, in Spectral —
  the claim follows the evidence in the layout as in the logic.
- **Motion spec.** Trigger: scroll, pinned scrub. As the pin
  travels: the five fold ghosts arrive from the strip (§6.4's
  final step, 1100ms-equivalent under `--ease-fold`), the points
  settle, the model fit draws left-to-right over 800ms under
  `--ease-ink` (the one masked line reveal the theme permits,
  §5 — a model being fitted), residuals fade in per bin over
  600ms, and the figure block's bars step to their final σ
  (§6.5). Scrolling back above the pin reverses the assembly to
  the five-transit state — the archive fold is presented as
  this panel's act, and leaving it un-presents it.
- **States.** Assembling (pin travelling) / assembled (all
  layers in, figures final) / held (pin released, panel static
  at the page's flow) / print (static, all layers). The panel
  never shows a partial figure: each figure's text updates only
  when its layer completes (text and chart in the same frame,
  §6.5's rule).
- **Content merge.** The plate is the destination of every
  earlier element: the strip's fold zone (§6.4) is this panel in
  miniature; the counters (§6.15) end at its figures; the log
  (§6.13) tabulates its inputs. It is the least removable
  element on the page.
- **Failure fallback.** Watchdog at 3000ms after the pin starts:
  the panel renders assembled. No-JS: the panel prints assembled
  with all figures — a reader without the performance loses
  nothing but the performance. The announcement prose never
  depends on the panel's state.
- **Reduced-motion variant.** The panel is not pinned; it prints
  assembled in flow. The confirmation loses its ceremony and
  keeps its evidence.
- **Performance budget & mobile variant.** One chart, ~28 binned
  profile points + residuals (the plate plots the *binned*
  profile — 1,944 raw points would be ink, not information, at
  this scale; the binning is stated in the caption: `BINNED TO
  4 MIN PHASE`). Budget: ≤0.5ms/frame during the pin. Mobile
  (<768px): pin shortens to 120vh; the chart keeps its aspect
  (phase axis compresses its labels, not its range); figure
  block stacks two-by-two.
- **Choreography timeline (v2).** Pin engages → ghosts arrive
  from the strip (1100ms-equiv) → profile settles → model fit
  draws (800ms) → residuals fade (600ms) → figure bars step to
  ±9, SNR counter completes its run to 33.3 (§6.15) → pin
  releases → announcement prose below.
- **State matrix (v2).** *Rest (assembled/held):* as above.
  *Hover:* figures bracket (§6.6, in plate colours — corners
  `--paper`, bar `--grey` at plate contrast 6.5:1). *Focus:* the
  panel's caption link ("FULL RUN LOG") is its focusable
  companion. *Active:* n/a. *Scrolled-past:* panel static,
  assembled. *Disabled:* n/a. *Touch:* scrub by scroll
  identical; no hover brackets.
- **Breakpoints (v2).** ≥1200px: plate full-bleed, chart 380px
  tall. 768–1199px: chart 320px. <768px: chart 260px, pin 120vh
  (above); axis labels thin to every 0.04 phase.
- **Edge cases & failure modes (v2).** *A record whose archive
  fold does not exist (first run of a new target):* the plate
  folds only the page's transits, σ stays at ±21, and the
  caption says `NO ARCHIVED TRANSITS — FIRST RUN`; the SNR
  prints its true 14.3 and the announcement copy must match
  (§12: the words "candidate" until the record's SNR crosses
  the survey's stated threshold — the plate never inflates).
  *Residuals showing structure (a bad fit):* if the record's
  residuals carry a stated systematic, the panel prints it —
  the plate shows the fit's quality, not just the fit.
- **Accessibility spec (v2).** The panel's figures are DOM text
  on `--plate` at 15.2:1. The chart is `role="img"` with a full
  label including the residuals' verdict ("residuals scatter
  within plus or minus 30 parts per million, no structure").
  Annotations on the plate are `--paper` text; `--red` is
  glyph-only here (§2's ruling) — a red *word* never appears on
  the plate.
- **Tokens consumed (v2).** `--plate`, `--paper`, `--grey`,
  `--baseline`, `--indigo`, `--ease-fold`, `--ease-ink`,
  `--loop-lerp`, `--dur-fit` (800ms).

### 6.13 The observation log table

- **What & why.** The run, tabulated: every transit's epoch,
  measured depth, duration, folded depth and σ as of that
  transit, SNR, and status — plus the run's own metadata
  (cadence, points, window, the predicted next epoch). It
  belongs because a chart persuades the eye but a table is what
  gets cited; the log is the page's evidence in its most
  portable form, and the place where the theme's arithmetic can
  be checked line by line.
- **Structure.** A real `<table>`: Spectral row labels, mono
  figures, rules in `--grid-major`, no zebra (zebra is not a
  measurement). Columns: `TRANSIT / EPOCH (BJD−2459000) / DEPTH
  (ppm) / T14 (h) / FOLDED DEPTH ± σ (ppm) / SNR / STATUS`.
  Rows T1–T5 from the record, a totals row (`FOLDED, n = 5`:
  300 ± 21, SNR 14.3), and a final archive row (`+ ARCHIVE,
  n = 28`: 300 ± 9, SNR 33.3) set on `--paper-deep`. Below the
  table, the prediction line: `T6 PREDICTED — EPOCH 145.500,
  AFTER THE RUN ENDS` — printed, never drawn as a dip (§1).
  Every figure in the table is the same figure as in the strip,
  cards and plate (one record, §6.17; §10 greps them).
- **Motion spec.** Trigger: scroll into view. Rows do not
  animate in (a table is printed, §5). The one motion: when a
  fold lands (§6.4) while the table is on screen, the affected
  row's STATUS cell updates (`FOLDED n = 3` inks in, 240ms,
  `--ease-ink`) and its folded-σ figure steps with §6.5's bar
  rule. Sorting: none — the log is chronological; a sortable
  log would let a reader disorder the evidence.
- **States.** Rest (printed) / updating (a fold lands while
  visible) / marked (rows mirror §6.7 marks in their STATUS
  cells: `CONFIRMED — READER`) / print (the table is the print
  stylesheet's centrepiece, §2).
- **Content merge.** The log is the record in tabular form —
  the same numbers, the third printing (strip, cards, table).
  Its existence is what makes the charts honest: anything the
  eye thinks it saw in a dip can be checked against a row.
- **Failure fallback.** Watchdog: none needed — the table is
  static DOM; its fold-driven updates are enhancements with the
  final state server-rendered per the record (a no-JS reader
  sees the completed log). If JS state and record disagree, the
  record wins on reload — the table re-renders from §6.17.
- **Reduced-motion variant.** Status updates are instant state
  changes. Otherwise identical — the table was already the
  reduced-motion citizen of the page.
- **Performance budget & mobile variant.** Static DOM, ~8 rows.
  Budget: zero at rest. Mobile (<768px): the table scrolls
  horizontally inside a ruled frame with the TRANSIT column
  sticky — columns are never dropped (a dropped σ column is a
  lie by omission); the frame's edge fades with a mono note
  `TABLE CONTINUES →`.
- **Choreography timeline (v2).** Table enters view: printed,
  complete → folds landing while visible update their rows
  (240ms ink) → the archive row is present from first paint (it
  is part of the record, not a reveal).
- **State matrix (v2).** *Rest / updating / marked:* as above.
  *Hover:* a row's figures bracket (§6.6) — the table is
  figure-dense and the bracket is its inspection tool. *Focus:*
  rows are not focusable; the table's caption link to the data
  file (where the record offers one) is. *Active:* n/a.
  *Scrolled-past:* static. *Disabled:* n/a. *Touch:* tap a
  figure = bracket.
- **Breakpoints (v2).** ≥1200px: full table in the reading
  column. 768–1199px: full table, figures at 13.5px. <768px:
  horizontal scroll frame (above).
- **Edge cases & failure modes (v2).** *A run with 12 transits:*
  the table grows rows; the page's sections (§4) cap at one run
  — a 12-transit run's table is long and that is correct; it
  paginates only in the §7 listing context, never mid-run.
  *A rejected transit:* its row prints with the dip struck in
  the status (`REJECTED — SYSTEMATIC`) and its depth in
  parentheses — present in the log, excluded from the fold, the
  difference stated in the row itself.
- **Accessibility spec (v2).** Proper `<th scope>` headers, a
  `<caption>` naming the run and its n, figures as text. The
  table is the chart system's accessible twin — a screen-reader
  user loses nothing that the sighted reader gets from the
  strip. Status words, never colour-only.
- **Tokens consumed (v2).** `--paper`, `--paper-deep`, `--ink`,
  `--ink-soft`, `--grey`, `--red`, `--grid-major`, `--ease-ink`,
  `--dur-ink` (240ms).

### 6.14 Join-the-survey form (conversion)

- **What & why.** The conversion section is an observer's
  enrolment: name, email, and the shift the volunteer is
  offering (which nights, which field) — submitted not to a
  database abstraction but *into the log*: the confirmation is
  an observer entry, numbered from the printed observer count,
  with the new observer's first assignment stated as an epoch
  ("Your first window: T6, epoch 145.500 — the transit this page
  predicted"). It belongs because joining a survey is joining a
  roster of people who watch; the form's receipt should read
  like the log it joins.
- **Structure.** A ruled form plate on `--paper-deep`: fields as
  ledger lines (borderless inputs on `--grid-major` rules,
  labels in mono uppercase), three fields only (name, email,
  availability as a checklist of printed windows — the upcoming
  predicted epochs from the record, T6 first). Submit button:
  ink-filled, Spectral, `TAKE THE NEXT TRANSIT`. On success the
  form plate is replaced by the log entry (§6.13's table style):
  `OBSERVER № 1,208 — [NAME] — FIRST WINDOW T6 · 145.500`,
  where 1,208 = the printed roster count (1,207) + 1 — the
  number is derived from a figure printed on the page before
  the form (§10's figure audit covers it), never invented at
  submit time.
- **Motion spec.** Trigger: submit. Validation is instant and
  in place (below). On submit: the button's label sets to
  `LOGGING…` (the theme has no spinner — §11), the plate holds
  400ms under `--ease-settle` while the entry is written, then
  the form crossfades (240ms) to the log entry, whose observer
  number counts from 1,207 to 1,208 over 600ms under
  `--ease-settle` — a counter with exactly one step to take,
  taken at reading pace.
- **States.** Rest (fields empty, rules light) / focused (the
  field's rule doubles and its label inks to `--ink`) / error
  (rule stays single, a red margin tick + a mono note in the
  annotator's voice, §12: `THAT ADDRESS WILL NOT SURVIVE THE
  NIGHT — CHECK IT`) / submitting / logged (the entry) /
  already-logged (returning session: the entry prints with
  `ALREADY ON THE ROSTER`).
- **Content merge.** The form's choices are the record's own
  predictions (T6's epoch is §6.13's printed prediction), and
  its receipt is a row in the page's own log format. The
  conversion is continuous with the science: you do not sign up
  for a newsletter, you take a transit.
- **Failure fallback.** Watchdog at 3000ms on submit: if the
  request has not resolved, the plate prints `THE LOG IS
  SLOW TONIGHT — YOUR ENTRY IS HELD, NOT LOST` and retries in
  place; a hard failure prints the observatory's email as a
  mono line (a person can be written to — the form never strands
  a volunteer on a dead end). No-JS: the form posts to a real
  endpoint and the confirmation is a server-rendered page in
  the same log format.
- **Reduced-motion variant.** No crossfade or count: the entry
  replaces the form as a state change, number printed final.
- **Performance budget & mobile variant.** DOM form, one request.
  Budget: negligible. Mobile (<768px): fields stack; the
  availability checklist rows are 48px tall; the submit button
  is full-width, 52px.
- **Choreography timeline (v2).** Focus: rule doubles (120ms) →
  submit: label sets → 400ms hold → crossfade (240ms) → entry
  prints, number steps 1,207 → 1,208 (600ms) → the strip's rail
  (§6.2) gains a mono tick: `OBSERVERS 1,208` → done.
- **State matrix (v2).** *Rest / focused / error / submitting /
  logged:* as above. *Hover:* the submit button deepens to
  `--indigo` over 150ms (the one place a button may wear the
  data colour — it submits you to the data). *Focus:* 2px
  `--indigo` outline on fields and button. *Active:* button
  translates 1px. *Scrolled-past:* n/a. *Disabled:* the submit
  is disabled only while submitting; the roster-closed state
  (a record may close enrolment) replaces the form with the
  printed note `THE ROSTER IS FULL FOR THIS RUN` and the next
  run's date — never a greyed-out form. *Touch:* 48px targets.
- **Breakpoints (v2).** ≥1200px: form plate 640px in the column,
  availability in two columns. 768–1199px: one column checklist.
  <768px: full-width plate, as above.
- **Edge cases & failure modes (v2).** *Duplicate email:* the
  entry prints `ALREADY ON THE ROSTER — № 1,143` with the
  original number (derived from the response, stated as such) —
  never a scolding error for a person who volunteered twice.
  *The predicted T6 epoch passes while the page is live:* the
  record is build-time; the form's first window is the record's
  printed prediction and the caption dates it (`AS OF RUN
  124.000`) — the page does not silently recompute its record.
- **Accessibility spec (v2).** Real `<label>`s (the mono labels
  are the labels, not placeholders); errors are text linked via
  `aria-describedby`, summarised in a live region on submit;
  the confirmation entry is a heading + text, announced. Focus
  order follows the reading order; the log entry takes focus on
  appearance.
- **Tokens consumed (v2).** `--paper-deep`, `--paper`, `--ink`,
  `--ink-soft`, `--indigo`, `--red`, `--grid-major`,
  `--ease-settle`, `--dur-log` (600ms).

### 6.15 The counters rail (accumulating figures)

- **What & why.** A band of the survey's headline figures —
  DEPTH, PERIOD, SNR, TRANSITS FOLDED, MARKED — that starts the
  page nearly empty (`DEPTH — NOT YET MEASURED`) and fills as
  the reader's scroll earns each figure: depth after the first
  fold, period after the third transit, SNR climbing with every
  fold to its final 33.3 at the plate. It belongs because the
  rail is the page's abstract written in the instrument's hand:
  a summary that refuses to exist before the evidence does.
- **Structure.** A ruled band (in flow, after the hero; a
  condensed twin lives in the strip's rail, §6.2) of five figure
  blocks in mono: label (11px uppercase), value (28px, §3), and
  beneath each, its §6.5 error bar or its n (`n = 3`). Values
  are DOM text driven by the shared loop from fold state
  (§6.4): DEPTH prints the folded depth ± σ as of the deepest
  fold reached; SNR likewise (6.0 → 8.8 → 10.6 → 12.5 → 14.3 →
  33.3 at the plate's archive step, captioned there); PERIOD
  prints `—` until two transits fix the spacing, `3.5 d` at two,
  `3.52 d` from three (§6.4's precision rule); FOLDED counts
  0–5; MARKED counts §6.7's reader marks. One arithmetic
  convention governs the whole page: SNR always prints as the
  *printed* folded depth ÷ the *printed* folded σ (288/48 =
  6.0; 300/34 = 8.8; 298/28 = 10.6; 301/24 = 12.5; 301/21 =
  14.3; 300/9 = 33.3), so a reader's pocket check reproduces
  every figure exactly — no hidden unrounded intermediates.
- **Motion spec.** Trigger: fold and mark events, via the shared
  loop. Values interpolate numerically over 600ms under
  `--ease-settle` and stop dead at the record's figures (a
  counter that overshoots its measurement is a small lie and is
  forbidden — interpolation is monotonic and clamped). The σ bar
  under DEPTH steps per §6.5. Scrolling back above a fold
  reverses the affected counters (§6.4's rule) — the rail
  reports the fold as it stands, not as it once stood.
- **States.** Empty (page top: labels printed, values as
  em-dashes with `NOT YET MEASURED` captions) / accumulating /
  complete (at the plate: final figures, caption `AS OF THE
  ARCHIVE FOLD`) / reversed (reader scrolled up: values back at
  the earlier fold's figures).
- **Content merge.** Every value on the rail is a figure the
  reader has watched being earned in the strip; the rail is an
  index of the page's own events. It advertises nothing that is
  not derived, on this page, from the record.
- **Failure fallback.** Watchdog at 2000ms: a counter mid-
  interpolation when the loop stalls snaps to the current fold
  state's figure. No-JS: the rail prints the final figures with
  the caption `FINAL — SEE THE LOG` (the summary of a finished
  run is a legitimate thing to print; the *performance* of
  earning them is the enhancement).
- **Reduced-motion variant.** Values change as state at fold
  boundaries; no interpolation.
- **Performance budget & mobile variant.** Five text nodes + one
  bar. Budget: ≤0.1ms/frame during interpolations. Mobile
  (<768px): the rail wraps to two rows (DEPTH, SNR / PERIOD,
  FOLDED, MARKED); values at 22px.
- **Choreography timeline (v2).** Hero completes: rail prints
  labels, dashes → T1 fold: DEPTH 288 ± 48, SNR 6.0, FOLDED 1 →
  T2 fold: DEPTH 300 ± 34, PERIOD `3.5 d` → T3 fold: PERIOD
  `3.52 d`, SNR 10.6 → T4, T5 folds step likewise → plate:
  DEPTH ± 9, SNR 33.3, caption switches to the archive line.
- **State matrix (v2).** *Rest (empty/accumulating/complete):*
  as above. *Hover:* a figure brackets (§6.6) with its n.
  *Focus:* figures are text; the rail's companion link is §6.13.
  *Active:* n/a. *Scrolled-past:* the rail is in flow; its strip
  twin (§6.2) keeps the current figures in view. *Disabled:*
  n/a. *Touch:* tap = bracket.
- **Breakpoints (v2).** ≥1200px: five across. 768–1199px: five
  across at 22px values. <768px: two rows (above).
- **Edge cases & failure modes (v2).** *Reader jumps straight
  to the plate:* counters settle to final in one frame (§13) —
  correct figures, unearned performance, and the caption's
  `AS OF THE ARCHIVE FOLD` remains true. *A record with one
  transit only:* PERIOD never prints (a single transit has no
  period — the rail prints `PERIOD — NEEDS A SECOND TRANSIT`,
  the theme's honesty at its most characteristic).
- **Accessibility spec (v2).** The rail is a list of labelled
  figures in text; updates are *not* live-announced per step
  (the §6.2 twin announces per section instead — one voice, not
  five). Em-dash states are read as their captions
  ("depth: not yet measured").
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--grey`,
  `--grid-major`, `--ease-settle`, `--loop-lerp`, `--dur-count`
  (600ms).

### 6.16 Arrival skeleton & unfolding loader

- **What & why.** While a page or a heavy figure loads, the
  theme does not shimmer: it shows an empty ruled chart — axes,
  grid, hour ruler — with points beginning to arrive at
  instrument pace, exactly as an observation starts. It belongs
  because waiting in an observatory is watching the first points
  come in; the skeleton is the run beginning, not a grey
  apology for it.
- **Structure.** The strip (§6.2) renders immediately in its
  skeleton state: frame and ruler printed, plot empty, and a
  mono line in the rail: `OBSERVING…`. Below, section skeletons
  are ruled plates with their headings printed (headings are
  content, not chrome — they render with the HTML) and figure
  blocks as empty scale tracks (§6.5's tracks without bars).
  Points arrive on the strip's plot from the record's first
  epochs at 1 per 120ms (faster than §6.2's live pace — this is
  the backlog arriving) until real content paints, when the
  skeleton hands over to §6.1/§6.2's states without a flash:
  the skeleton's strip *is* the strip.
- **Motion spec.** Trigger: load / navigation hold (§6.9).
  Arrival cadence 120ms per point under `--ease-arrive`; the
  `OBSERVING…` ellipsis is a 1200ms three-step cycle (steps, not
  a fade — instruments blink, they do not breathe). Hard ceiling:
  at 4000ms the skeleton resolves to the static fallback
  (below) regardless of load state.
- **States.** Observing (points arriving) / resolved (real
  content painted; skeleton gone without trace) / timed-out
  (4000ms: the full static curve prints in the strip and a mono
  note `SLOW NIGHT — THE PRINTED CURVE IS BELOW` points to the
  in-flow static chart every page carries for no-JS).
- **Content merge.** The skeleton is built from the page's own
  record (its ruler spans the real window; its arriving points
  are the run's real first points) — a slow load shows the
  actual observation starting, not a generic placeholder shaped
  like one.
- **Failure fallback.** The 4000ms ceiling *is* the fallback,
  and it falls back to print, not to a spinner: watchdog at
  4000ms forces the timed-out state. No-JS: no skeleton at all —
  content is server-rendered; skeletons exist only where JS
  will replace them.
- **Reduced-motion variant.** No arrivals: the strip prints its
  full static curve immediately (the timed-out state, without
  the wait or the note).
- **Performance budget & mobile variant.** One canvas, ≤200
  skeleton points. Budget: ≤0.2ms/frame. Mobile (<768px):
  identical; section skeletons shorten to heading + one track.
- **Choreography timeline (v2).** Navigation/load → strip frame
  and ruler paint (first frame) → points begin arriving (120ms
  cadence) → content ready: hand-over, hero draw (§6.1) takes
  the narrative → or t=4000ms: static curve + note.
- **State matrix (v2).** *Rest:* resolved (the skeleton's rest
  is absence). *Hover / focus / active:* the skeleton contains
  no interactive elements; focus is never placed inside it.
  *Scrolled-past:* n/a. *Disabled:* n/a. *Touch:* no
  interaction.
- **Breakpoints (v2).** ≥1200px / 768–1199px / <768px: the strip
  skeleton matches §6.2's heights at each size.
- **Edge cases & failure modes (v2).** *Content arrives in
  pieces:* the strip resolves when the hero's data is ready;
  below-fold skeletons resolve independently as their sections'
  content lands — a page may be half-observed, like a real run
  interrupted by cloud, and the printed headings keep it
  navigable throughout. *Repeat navigation:* cached pages skip
  the skeleton entirely (§6.9's prefetch rule).
- **Accessibility spec (v2).** The skeleton region is
  `aria-busy="true"` with a visually-hidden "Loading the
  observation run" — announced once, not per point. The
  `OBSERVING…` text is `aria-hidden`. Focus never enters a
  skeleton.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--grey`,
  `--grid`, `--grid-major`, `--ease-arrive`, `--dur-observe`
  (120ms cadence), `--dur-ceiling` (4000ms).

### 6.17 The observation record (the declared source)

- **What & why.** The record is an element, not a backstage
  file: a printed block — set in the page's colophon area above
  the footer, and mirrored in the build as a single JSON source
  — declaring everything every figure on the page derives from:
  target, window, cadence, point count, the five epochs with
  measured depths, duration, the archive count, the roster
  count, and the noise seed. It belongs because the theme's law
  (§1) is enforceable only if the record is public: printing it
  on the page lets any reader re-derive any figure, which is
  the difference between a chart and a claim.
- **Structure.** A ruled mono block, two columns at ≥1200px:
  `TARGET K-85 · FIELD 7 / WINDOW 124.000–144.250 (20.25 d) /
  CADENCE 15 min / POINTS 1,944 / T1 127.900 · 288 ppm / T2
  131.420 · 312 ppm / T3 134.940 · 295 ppm / T4 138.460 · 307
  ppm / T5 141.980 · 301 ppm / T14 2.1 h / P 3.52 d / ARCHIVE 23
  TRANSITS / ROSTER 1,207 OBSERVERS / NOISE σ 48 ppm PER
  TRANSIT / SEED 85-124`. The scatter series for §6.1/§6.2/§6.8
  are generated from this seed by a stated generator (mulberry32
  + gaussian clamp), so the printed record and the drawn curve
  are the same data, reproducibly. Every element in §6 cites
  this section for its figures; a figure found anywhere that is
  not derivable here fails §10.
- **Motion spec.** None. The record is printed. (Its one dynamic
  property: §6.7's marks and §6.14's roster step are *visitor*
  state, kept out of the record block — the record is the
  survey's, the annotations are the reader's, and the page never
  mixes the two inks in this block.)
- **States.** Printed. (A record under revision between runs is
  a new page, §6.9 — records are versioned by run, never edited
  in place: the block carries `RUN OF 124.000` as its version.)
- **Content merge.** The record is the content's source and its
  citation in one. It merges by definition: there is no figure
  on the page that is not either in this block or derived from
  it by a stated rule (fold means, σ = 48/√n, SNR = depth/σ).
- **Failure fallback.** The block is static HTML; it cannot
  fail. If the generated series and the printed record ever
  disagreed (a build error), §10's figure audit catches it
  before ship — the audit regenerates the series from the seed
  and compares epochs and depths.
- **Reduced-motion variant.** Identical (no motion to reduce).
- **Performance budget & mobile variant.** One text block.
  Budget: zero. Mobile (<768px): one column; the transit rows
  keep their epoch·depth pairing per line (never split a transit
  across lines — a row is a measurement).
- **Choreography timeline (v2).** Printed at first paint, above
  the footer, after §6.12's plate and §6.13's log — the page's
  last word is its source.
- **State matrix (v2).** *Rest:* printed. *Hover:* individual
  values bracket (§6.6) — even the record submits to
  measurement. *Focus:* values are text; the block's heading is
  a normal heading. *Active / scrolled-past / disabled:* n/a.
  *Touch:* tap = bracket.
- **Breakpoints (v2).** ≥1200px: two columns. 768–1199px: two
  columns, tighter. <768px: one column (above).
- **Edge cases & failure modes (v2).** *A client record with
  proprietary data:* the block prints the record the page
  actually used, at the precision the page claims — if a figure
  on the page cannot be printed here, it cannot be printed
  anywhere (§9: the unpublished source). *Rounding:* the record
  prints the rounded values the whole page uses (§6.5's rule),
  so re-derivation matches to the printed digit.
- **Accessibility spec (v2).** A `<section>` with heading "The
  observation record"; the block is a definition list in DOM
  order (term: the label; definition: the value), so AT reads
  label–value pairs, not a visual grid.
- **Tokens consumed (v2).** `--paper-deep`, `--ink`, `--ink-soft`,
  `--grid-major`.

### 6.18 The flat-field 404 (out-of-field page)

- **What & why.** The 404 is a flat field: a chart with axes, a
  full run of points sitting dead on the baseline, no dips
  anywhere, and the line `NO TRANSIT IN THIS WINDOW — THE PAGE
  YOU ASKED FOR WAS NOT IN THE FIELD.` It belongs because an
  observatory's honest failure is an empty observation, not a
  mascot with a telescope: the page reports what the instrument
  saw, which is nothing, and says where the real fields are.
- **Structure.** The strip (§6.2) prints a flat run (points on
  the baseline, σ jitter only, §6.8's amplitude). Below: the
  Spectral line above, then the log-style list of real
  destinations (§6.13's table typography: `FIELD 7 — THE K-85
  RUN`, `THE FOLD`, `THE LOG`, `JOIN THE SURVEY`), each with its
  "epoch" — the link's plain path in mono. No search box
  dressed as an instrument; if the site has search it appears
  as itself (§11).
- **Motion spec.** Trigger: load. The flat points arrive over
  1200ms under `--ease-arrive` — and pointedly do not dip. That
  is the whole choreography; its restraint is the joke the
  theme permits itself, and it is a quiet one. The strip's rail
  reads `EPOCH — NOT OBSERVED`.
- **States.** Printed (the flat field, complete) — the page has
  one state; a 404 with states is a lobby, not an observation.
- **Content merge.** The flat field is drawn from a null record
  (the same generator, depth 0) — the 404 is the theme's own
  instrument reporting zero, in its own units.
- **Failure fallback.** The page *is* a fallback; its own
  fallback is that every link on it is a plain anchor. No-JS:
  identical, minus the arrival.
- **Reduced-motion variant.** Points printed, no arrival.
- **Performance budget & mobile variant.** One small canvas.
  Budget: ≤0.2ms/frame for 1200ms. Mobile (<768px): the
  destination list stacks; the flat strip is unchanged.
- **Choreography timeline (v2).** Load → strip frame prints →
  points arrive flat (1200ms) → the line and the list are
  already readable beneath (they never waited for the chart).
- **State matrix (v2).** *Rest:* printed. *Hover:* destination
  rows bracket their paths (§6.6 grammar). *Focus:* standard
  link focus, `--indigo` outline. *Active / scrolled-past /
  disabled:* n/a. *Touch:* 44px rows.
- **Breakpoints (v2).** ≥1200px / 768–1199px / <768px: strip per
  §6.2; list one column below 1200px.
- **Edge cases & failure modes (v2).** *A 404 reached from a
  marked-transit state:* session marks (§6.7) are not shown
  here — the flat field belongs to no run. *Server misconfig
  serving the 404 with a 200:* the page still reads correctly;
  its honesty does not depend on its status code, though the
  build checklist (§15) verifies the status too.
- **Accessibility spec (v2).** The heading is the Spectral line
  as `<h1>`; the flat chart is `role="img"` labelled "A light
  curve with no transits". Links are descriptive ("The K-85
  observation run"), never "click here".
- **Tokens consumed (v2).** `--paper`, `--ink`, `--ink-soft`,
  `--grey`, `--grid-major`, `--ease-arrive`, `--dur-flat`
  (1200ms).

---

## 7. Page application map

| Page type | How the theme plays out |
|---|---|
| **Home (the run)** | The full performance: hero (§6.1), strip (§6.2), five transit sections (§6.3 + §6.11 + §6.5), fold (§6.4), plate (§6.12), log (§6.13), record (§6.17), join (§6.14). One run per home page — the theme's unit is the run. |
| **Candidates listing** | A table of candidate targets (§6.13's typography) with §6.11 cards for the vetted few; each row's figures carry their σ and n; unvetted candidates print `AWAITING FOLD` instead of a depth — the listing never lends folded precision to unfolded candidates. The strip shows the survey's current run (context, not the listing's data). |
| **Candidate detail** | That target's own run page: same structure as home, with its own record (§6.17). A candidate with a single transit gets the honest rail (`PERIOD — NEEDS A SECOND TRANSIT`, §6.15) and no fold section — §6.12 is replaced by a printed note of what the next run must observe. |
| **About / method** | Prose pages under the strip: the method explained with small printed charts (static, §6.11's mini-curves at larger scale); the fold demonstrated once, on the worked record, labelled as the worked example. Method pages carry no live fold of their own. |
| **Join / contact** | §6.14's form as the page; contact is a mono block of real addresses in the log's typography — an observatory is written to, not "reached out" to. |
| **404** | §6.18's flat field. |
| **Print** | The run printed once (§2): strip unpinned at the head, fold assembled, log and record complete. Print is a first-class page type in this theme — light curves live on walls. |

---

## 8. Worked examples

### 8.1 The hero — "the run begins" (home, top)

**Build.** Masthead (§6.10) over the strip (§6.2, skeleton
state §6.16 for the first frames) over the hero figure (§6.1):
canvas scatter, SVG frame, the `<h1>` waiting in T3's dip.
Beneath, the standfirst in Spectral italic: "For twenty nights
the telescope watched one star. Five times, something crossed
it." — with "twenty nights" corrected by the record to the
run's true span in the caption beneath: `RUN 124.000–144.250 ·
20.25 d · 1,944 POINTS`.

**Scroll/load timeline.** t=0: masthead, strip frame, hero
frame paint; headings readable. t=120ms: the scatter draw
begins, frontier sweeping left to right at ~778 points/s.
t≈1375ms: the frontier reaches epoch 134.940 and T3's dip
traces (900ms, `--ease-dip`) to 295 ppm. t≈1900ms: the headline
fades in inside the dip — "SOMETHING PASSED IN FRONT OF THE
STAR." t=2500ms: the draw completes past T5; the strip above is
now the live one, its first new point arriving at t≈3400ms.
The visitor scrolls: the rail clock starts tracking epochs.

**What the visitor understands.** Before reading a word of
prose: a star was watched, points accumulated, something
crossed, and the crossing is where the headline lives. Every
later section is a footnote to this chart.

### 8.2 Mid-page — the T3 section and its fold

**Build.** Section T3 (paper-deep parity): `<h2>` "Transit 3 —
the one in the headline", epoch in the margin; two paragraphs
of Spectral prose (what made T3 clean: no systematics, full
ingress and egress inside the window); §6.11's card (depth
295 ± 48 single-transit, duration 2.1 h, SNR 6.1); the folded
figure block (after three transits: `298 ± 28 ppm`, §6.5 bar at
the 28 width, `n = 3`); the mark button (§6.7).

**Scroll timeline.** Section top crosses 75% viewport: its dip
in the strip begins deepening (§6.3). Centre: d=1, the inset
opens showing T3 at reading scale; the card's mini-curve has
already drawn on entry. The reader marks it: red tick at
134.940, `T3 — CONFIRMED` in the margin, rail MARKED steps to
1. Section end + 30vh: the fold fires (§6.4) — T3's ghost
slides right along the strip, docks on the two-member stack;
the profile sharpens; the rail's DEPTH steps 300 ± 34 → 298 ±
28; PERIOD completes `3.52 d`. The next section (T4) begins
under a strip whose fold is visibly stronger.

**What the visitor understands.** Their mark is in the stack.
The period became exact at the transit they just read. The
arithmetic (48/√3 ≈ 28) is printed beside the bar for checking.

### 8.3 Conversion — taking the next transit (join)

**Build.** After the plate (§6.12) and the log (§6.13): the
join plate (§6.14) on paper-deep. The prose above it is one
Spectral paragraph: the survey runs on volunteers' nights; the
next transit of K-85 falls at epoch 145.500, after this run's
end, and somebody has to be watching. The form's availability
checklist is that prediction and the two after it (145.500,
149.020, 152.540 — the record's arithmetic, 3.52 d spacing,
printed as predictions).

**Submit timeline.** The volunteer ticks T6, enters name and
email, submits: label sets to `LOGGING…`, 400ms hold, crossfade
to the entry: `OBSERVER № 1,208 — FIRST WINDOW T6 · 145.500`.
The strip's rail gains `OBSERVERS 1,208`. Below the entry, one
mono line: `THE LOG WILL CALL THIS TRANSIT BY YOUR NAME.` —
§12 permits exactly this much warmth, in mono, because it is a
statement about the log.

**What the visitor understands.** They have not subscribed to
anything. They have taken a shift, at an epoch, in a log that
now contains their number — derived from a count they saw
printed before they acted.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **Sparkle noise.** Scatter that twinkles decoratively, at
   amplitudes no instrument would produce. *Cure:* §6.8's hard
   cap — ±1σ, seeded, ≤1.5px; if the texture is pretty, it is
   wrong.
2. **Error bars as garnish.** Bars all the same length, or drawn
   without a scale, or omitted where the number is embarrassing.
   *Cure:* §6.5 — every bar to scale on a printed track, every
   σ labelled with its n, the sequence 48/34/28/24/21/9 derived
   from 48/√n and printed so it can be checked.
3. **The dip that matches nothing.** A hero dip at an epoch no
   section discusses, or sections whose order differs from the
   strip's. *Cure:* §6.3's 1:1 lock, generated from one record
   (§6.17); §10's correspondence audit compares them.
4. **Precision theatre.** `SNR 33.3` in the hero, before any
   fold; a period printed before two transits exist. *Cure:*
   §6.15's earned rail and §6.4's precision rule — figures
   appear when the page has earned them, at the precision it
   has earned.
5. **The rounded record.** "Over 2,000 points", "about
   300 ppm". *Cure:* §3 law 2 and §6.17 — 1,944 points,
   300 ± 9 ppm, exact or admitted, never rounded for rhythm.
6. **A fold that invents depth.** Stacked profile deeper than
   the transits that compose it. *Cure:* the profile is the
   pointwise mean (§6.4); its depth is the record's folded depth
   and §10's figure audit recomputes it.
7. **Fake live data.** Points arriving that imply an observation
   happening now, on a page about a finished run. *Cure:* §6.2 —
   arrivals are labelled as the run extending at instrument
   pace from the record's distribution, and the rail always
   prints the epoch under the reader, never a fake "LIVE".
8. **Serf numerals.** A depth set in Spectral because it looked
   nicer in the headline. *Cure:* §3 law 1; the gate greps
   figure blocks for the mono class.
9. **Red as branding.** Red buttons, red links, a red logo —
   until red means nothing when the annotator uses it. *Cure:*
   §2's rationing; red census ≤12 per page, annotation only.
10. **The hidden record.** Figures sourced from a spreadsheet
    the reader cannot see. *Cure:* §6.17 prints the record on
    the page; a figure not derivable from it fails the audit.
11. **Confirmation drift.** Copy that says "planet confirmed" in
    the hero and "candidate" in the log. *Cure:* §12's word
    discipline — the event is confirmed by marks, the planet by
    the fold's SNR against the survey's printed threshold, and
    the words are never swapped.
12. **Charts that apologise.** A dip drawn shallower "so it
    looks cleaner", axes rescaled per section so every transit
    looks the same size. *Cure:* per-record fixed scales (§6.5,
    §6.11); a 90 ppm transit looks small because it is small.

---

## 10. Quality gate

Blocking checks — all must pass before this theme ships in a
build. The gate is signed by someone who did not build the page
(§15).

1. **Figure audit.** Every depth, epoch, period, σ, SNR and
   count on the page is regenerated from §6.17's record by
   script and compared to the DOM. Zero mismatches.
2. **Correspondence audit.** Strip dips, sections, cards and
   log rows are the same transits in the same order at the same
   epochs. Zero orphans in either direction.
3. **Error-scale audit.** Each bar's pixel half-width equals
   its printed σ at its track's printed scale, ±1px.
4. **σ sequence audit.** Folded σ values follow 48/√n with the
   page's printed rounding; the archive step carries its
   `INCL. 23 ARCHIVED` caption.
5. **Red census.** ≤12 red instances per page, all annotation
   class. No red buttons, links, or logos.
6. **Mono audit.** No numeral with a unit set outside the mono
   class; no Spectral numerals in figure blocks.
7. **Watchdog drill.** With the rAF loop artificially stalled:
   hero complete by 4000ms, strip static-correct by 3000ms,
   every fold settled, every bar at its final σ. Nothing
   stranded, anywhere.
8. **No-JS pass.** The full curve printed, the fold assembled,
   the log and record complete, the form posting to its
   endpoint. The page loses motion and nothing else.
9. **Reduced-motion pass.** Printed curve, assembled fold,
   instant counters; the plate unpinned and complete.
10. **Dip-fit check.** The hero headline fits inside the dip at
    all three breakpoints without widening the dip (§3 law 3).
11. **Threshold wording check.** "Confirmed" language matches
    §12's discipline at every occurrence; the planet is claimed
    only at/after §6.12 and only if the record's SNR crosses the
    printed threshold.
12. **Performance pass.** §14's budgets met on the reference
    device; the noise field is the first thing cut and its
    absence changes nothing else.

---

## 11. Component inventory

Every component a real site in this theme needs, with its
themed treatment — or its refusal, with the in-theme
replacement.

| Component | Treatment in this theme |
|---|---|
| Primary button | Ink-filled plate, Spectral label (`TAKE THE NEXT TRANSIT`); hover deepens to `--indigo` only on the submit (§6.14) |
| Secondary button | Mono uppercase text with a 120ms `--ease-ink` underline draw |
| Text input | A ledger line: borderless field on a `--grid-major` rule; focus doubles the rule (§6.14) |
| Select / picker | A printed list of windows (radio rows styled as log lines) — no dropdown chrome on a chart |
| Checkbox | A small ruled square that takes a red tick when checked — the annotator's mark, reused honestly |
| Radio group | Log-line rows; the chosen row's epoch inks in beside it |
| Tabs | Refused. A run is read in time order; tabbing a light curve disorders the evidence. Page destinations are §6.10's nav |
| Accordion | Refused for data (a folded-away figure is an unpublished figure); permitted for method prose on §7's about page only, styled as ruled plates |
| Modal / dialog | Refused. Detail opens as a plate in flow (§6.12) or a card expansion; nothing floats over the curve |
| Toast | Refused. Outcomes are logged (§6.14's entry) or annotated in place; nothing vanishes from a chart |
| Alert / banner | A mono line in the margin with a red tick for warnings; system failures print as log lines (§6.14's held-entry pattern) |
| Badge / chip | Refused as pills. Status is a mono word in a ruled cell (`FOLDED n = 3`) — chips are not a unit of evidence |
| Pagination | Run folios in mono: `RUN 124.000 · PAGE 2 OF 4`, prev/next as log entries; listings paginate by run, never mid-run |
| Table | §6.13 — the theme's second native component |
| Card | §6.11 — the theme's atom |
| Progress bar | Refused; replaced by the strip's hour ruler and the fold count (§6.2, §6.15) |
| Spinner | Refused; replaced by §6.16's observing skeleton |
| Skeleton | §6.16 — ruled charts with points arriving |
| Tooltip | A mono note printed beside the figure on focus/hover (§6.6's readout) — never a floating grey box |
| Breadcrumbs | An epoch path in mono: `FIELD 7 › K-85 › T3 · 134.940` at the section head |
| Search | A mono input over the log's index (§6.13 pattern): results are log rows, ranked by epoch — the observatory's catalogue is searched like a log, not a shop |
| Empty state | §6.18's flat field, in miniature: `NO TRANSIT IN THIS WINDOW` |
| Error state | Ink text with a red margin tick and the annotator's voice (§12); the recovery action stated in the same line |
| Avatar / identity | Refused. Observers are numbers in the log (§6.14); the survey's identity is its record |
| Toggle / switch | Refused. States on a chart are printed or annotated; there is nothing to toggle in an observation |
| Chart (generic) | The theme's first-class citizen: axes printed, scale stated, source = §6.17; a chart without a stated scale may not ship (§10.3) |

---

## 12. Content & copywriting voice

Two registers, kept apart by law. **The instrument** (IBM Plex
Mono) states measurements and labels: literal, uppercase,
unit-bearing, without adjectives. **The observatory** (Spectral)
writes the prose: measured, plain, one claim per sentence, and
it never uses a number the instrument has not printed first.

- **Headlines** (observatory): a statement of what the data
  did. ✓ "Something passed in front of the star." ✗ "We found
  a new world!!" — the exclamation and the claim both outrun
  the fold.
- **Labels** (instrument): ✓ `DEPTH 300 ± 9 ppm` / `EPOCH
  134.940` / `AWAITING TRANSITS`. ✗ "Amazing depth!" /
  "When it happened".
- **Annotations** (the annotator's hand, red mono): ✓ `T3 —
  CONFIRMED` / `MARKED 138.460` / `REJECTED — SYSTEMATIC`.
  ✗ "Looks good to me!" — a mark is a verdict with an epoch,
  not an impression.
- **Error messages** (form): in the annotator's voice, saying
  what would do. ✓ `THAT ADDRESS WILL NOT SURVIVE THE NIGHT —
  CHECK IT`. ✗ "Invalid input".
- **Empty states**: ✓ `NO TRANSIT IN THIS WINDOW`. ✗ "Nothing
  here… yet 👀" — no emoji anywhere in the theme, ever.
- **The confirmation discipline (binding):** a transit *event*
  may be called CONFIRMED when marked/vetted; the *planet* is
  called confirmed only after the fold, only where the record's
  SNR crosses the survey's printed threshold (the worked
  record: SNR 33.3 against a printed threshold of 10), and the
  word used before that is CANDIDATE. Copy that upgrades early
  fails §10.11.
- **Numbers**: exact or admitted. ✓ `1,944 points` / `300 ± 9
  ppm` / `PERIOD — NEEDS A SECOND TRANSIT`. ✗ "2,000+ points!"
  / "≈300 ppm".
- **Fixed strings (verbatim, never paraphrased):** the hero
  headline "SOMETHING PASSED IN FRONT OF THE STAR."; `P = 3.52
  d` (assembled per §6.4's precision rule); `T3 — CONFIRMED`
  (and its siblings per transit); `NO TRANSIT IN THIS WINDOW`;
  `AWAITING TRANSITS`; `THE LOG WILL CALL THIS TRANSIT BY YOUR
  NAME.`
- **Dates and epochs** are always BJD with the offset printed
  (`BJD −2459000`), never converted to calendar dates in figure
  contexts — the chart's clock is the chart's.

---

## 13. Full-page scroll choreography map

The home page, top to footer, every beat in order. Reverse-pass
and jump rules follow the beats.

| # | Scroll position | Beat | What the visitor sees / feels |
|---|---|---|---|
| 1 | Load | §6.16 skeleton → §6.1 draw | The run plots itself in time order; the headline is discovered inside T3's dip |
| 2 | Hero → T1 | Strip takes over | The strip is live; the rail clock starts tracking epochs; arrivals begin at the edge |
| 3 | T1 centres | §6.3 deepening | T1's dip deepens; inset opens; card drawn; folded figure `288 ± 48` |
| 4 | T1 end | §6.4 fold 1 | T1's ghost docks; profile = one member; rail FOLDED 1, SNR 6.0 |
| 5 | T2 centres → end | Deepen → fold 2 | PERIOD appears as `3.5 d`; σ steps to ±34 |
| 6 | T3 centres | Deepen; §6.7 available | The headline's own transit, at reading scale; a mark here inks `T3 — CONFIRMED` |
| 7 | T3 end | Fold 3 | PERIOD completes: `P = 3.52 d`; σ ±28; the stack is now visibly a profile |
| 8 | T4, T5 | Deepen → folds 4, 5 | σ ±24, ±21; SNR 12.5, 14.3; the strip's fold zone is full |
| 9 | The plate | §6.12 pin (160vh) | Ghosts arrive, model fits, residuals settle; σ steps to ±9 with its archive caption; SNR completes 33.3 |
| 10 | Announcement | Prose below the plate | The claim, in Spectral, after its evidence |
| 11 | The log | §6.13 | The whole run as a table; the T6 prediction line at its foot |
| 12 | Join | §6.14 | The roster, the windows, the form; submitting writes a log entry |
| 13 | Record + footer | §6.17, then the footer | The source, printed; the footer is a log line: survey, run, `END OF RUN — NEXT EPOCH 145.500` |

**Reverse-pass rules.** Scrolling up un-folds transits in
reverse order (§6.4), counters step back (§6.15), deepening
releases (§6.3) — with two ratchets that never reverse: the
reader's marks (§6.7, including their smudges) and the join
entry (§6.14, once logged). The page's evidence is reversible;
the reader's acts are not.

**Jump rules.** Any discontinuous jump (End key, anchor to the
plate, restored scroll position) settles every scrubbed value
to its target state within one frame of landing: folds
assembled or not per position, counters at the position's
figures, the plate assembled if landed past it. Nothing may be
caught mid-slide by a jump (§6.4's watchdog is the backstop).

---

## 14. Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight (home) | ≤700KB gz | Fonts subset (Spectral 300/400 + italic, Plex Mono 400/500) ≈180KB; data is generated from the seed — the 1,944-point series costs the record's ~1KB, not a payload |
| Animation frame budget | ≤1.6ms/frame, all elements summed | Shared loop (§5); per-element budgets in §6 sum to ≈1.5ms worst case (hero draw + fold + deepening simultaneously is prevented by layout — they cannot co-occur) |
| Long tasks | None >50ms after first paint | Series generation is ~1,944 points: <5ms; profile recomputation per fold step is 5 paths |
| Canvas count | ≤3 live (hero, strip, noise field) | DPR capped at 2; strip redraws only on scrub change |
| Ambient loops | Exactly 2 (arrivals, noise jitter) | Both pause off-screen / hidden tab |

**Cut order when the budget is exceeded** (first → last):
1. §6.8's noise field (texture; nothing depends on it).
2. §6.2's point arrivals (the strip holds the printed run).
3. §6.1's draw → the hero prints complete.
4. §6.4's slide → folds become state changes.
5. §6.12's pin → the plate prints assembled in flow.

**Never cut:** the printed figures and their ± values; §6.13's
log; §6.17's record; any watchdog; the reduced-motion variants;
the strip itself. A page that keeps its evidence and loses its
motion is still this theme; the reverse is not.

---

## 15. Build-order checklist

1. **The record first.** §6.17's block and its JSON source;
   every figure in the build derives from it. No record, no
   build.
2. **The printed page.** Full static site: strip as static SVG,
   fold assembled, all figures and bars printed, log and record
   complete, form posting. This version must pass §10's no-JS
   and figure audits before any motion exists.
3. **Type and grid.** §3's scale and laws; §4's graph grid and
   section rhythm; the mono audit (§10.6) runs here.
4. **The strip.** §6.2 static → live (rail clock, arrivals),
   with its watchdog.
5. **Sections and cards.** §6.11 cards from the record; §6.5's
   bars with printed scales; §6.3's deepening on the shared
   loop.
6. **The fold.** §6.4 ghosts, profile, readout precision rule;
   §6.15's rail wired to fold state.
7. **Marks.** §6.7 with session persistence and the smudge
   rule; §6.6's brackets across all figure classes.
8. **The plate.** §6.12's pin and assembly; the archive step
   and its caption.
9. **The form.** §6.14 with its derived observer number,
   held-entry failure state, and no-JS endpoint.
10. **Texture and transitions.** §6.8's field (seeded, capped),
    §6.9's fold transition, §6.16's skeleton.
11. **The flat field.** §6.18, including its status-code check.
12. **Reduced-motion pass.** Every element's variant verified
    against §6, one by one.
13. **Watchdog drill.** §10.7 executed with the loop stalled at
    each element in turn.
14. **Audits.** §10.1–10.6, 10.10, 10.11 by script and eye.
15. **Gate sign-off.** §10 signed by a non-builder; the sign-off
    line joins the record block's page (`GATE — [NAME], [DATE]`)
    because in this theme, even the approval is logged.
