# Theme 71 — The Bioluminescent Census (50x expansion)

A midnight census of glowing organisms, expanded to the full v1 + v2
standard. Identity preserved exactly from the original entry: the page
is black water, every data point is a living light, statistics behave
like a plankton bloom — an ecosystem, not a chart library. Palette
anchors unchanged (midnight water `#04141C`, plankton cyan `#4FD8C8`,
dinoflagellate gold `#E9C46A`, predator red `#D64541` rare, bone text
`#DCE9E4`); type unchanged (Fraunces display, Space Grotesk body); all
10 original signature elements deepened, not redesigned, plus 8
page-family elements — 18 in total, each with a full build spec.

**The theme's one law: nothing glows that is not counted.** Every
light on the page is an organism in the census record (§6.17) or a
value derived from it by a function printed in this spec. The printed
figure in bone text is always the authority; the bloom is its
portrait. If a glow cannot be traced to the sheet, it is cut.

## 1. Concept & world

The visitor is a naturalist descending at midnight with a lantern and
a tally sheet. The site hangs in black water. Its statistics are not
drawn as bars or pies; they are *performed* by the population they
count — a flocking swarm of 160 simulated organisms schools in the
margins, parts around the text it lives beside, aggregates into the
shapes of the section's key figures, and settles along the sea floor
at the foot of the page. Depth is the page's geography: the reader
does not scroll down, they sink, and a sounding line in the margin
reports their depth in fathoms from the surface (0 fm) to the floor
(550 fm).

The world has rules a visitor can learn in one screen. Cyan light is
the plankton majority. Gold light is the dinoflagellates — rarer,
warmer, reserved for the species the census most wants noticed. Red
appears exactly once at a time and never as text: it is the predator,
and the swarm's fear of it is the page's only moment of danger. Bone
is the printed record — the naturalist's ink — and it never moves,
never glows, and never waits for the light-play to finish before it
can be read.

**Best fit.** Marine and environmental data stories; aquarium,
oceanographic-institute and research-expedition sites; annual reports
for conservation organisations whose numbers deserve ceremony;
night-sky and deep-sea exhibition microsites; any data publication
whose subject is a living population counted in the dark. The theme
is at its best when the data genuinely is a census — counts of
organisms, sightings, stations, samples — because the swarm's
behaviour is then literally the subject behaving.

**When NOT to use it.** Never for data that must be compared at a
glance under time pressure (operations dashboards, trading, clinical
monitoring): aggregation takes 1.2 s to form a figure, by design, and
a reader in a hurry is owed a table, not a bloom — §6.13's sounding
table exists for them, but if the table is the whole job, use a
plainer theme. Never for a light, daytime brand: there is no light
scheme (§2). Never where red is the brand colour — red is spent here,
rationed to one predator, and a red-heavy brand would bankrupt the
ration. Never for content with no counts in it; a page of pure prose
gives the swarm nothing to be, and it degenerates into wallpaper,
which §9 names as this theme's first failure.

**The census the worked examples count.** One declared record,
printed in full as §6.17 and summarised here so every number in this
spec can be audited against it: **61,408 organisms** counted over
**38 nights** at **96 stations**, from **1,142 samples**. By stratum:
the Shallows (0–30 fm) 31,204; the Twilight Shelf (30–110 fm) 19,876;
the Midnight Shelf (110–550 fm) 10,328 — summing to the total. By
species: *Noctiluca scintillans* 24,917 (gold); *Pyrocystis
fusiformis* 13,208; *Lingulodinium polyedra* 9,864; *Ceratium
horridum* 6,402; *Pyrodinium bahamense* 4,517 (gold); unclassified
lights 2,500 — summing to the total. Predator passes logged: 3.
Sighting reports on file: 412 — so the next report entered is № 413
(§6.14). Any build substitutes its own sheet; the rule is that there
is exactly one, and everything traces to it.

## 2. Palette

Five anchors from the original entry, four derived tokens added by
this expansion. Contrast ratios below were measured for this
expansion from the hex values (WCAG relative luminance), not
estimated.

| Token | Hex | Role | Measured contrast |
|---|---|---|---|
| `--midnight` | `#04141C` | The water itself; page ground | — |
| `--midnight-deep` | `#020A0F` | The floor and the deepest stratum; page edges, footer ground | bone on it 15.97:1 |
| `--water-2` | `#07212C` | Section water; ledger cards, table body | bone on it 13.32:1 |
| `--water-3` | `#0B2E3D` | Raised frames, inputs, the pinned figure stage's rim | cyan on it 8.14:1 |
| `--bone` | `#DCE9E4` | All printed text; the record's ink | on midnight 14.99:1 |
| `--bone-dim` | `#A8BDB4` | Captions, labels, secondary print | on midnight 9.45:1 |
| `--cyan` | `#4FD8C8` | Plankton light; links, primary data light, focus | on midnight 10.69:1 |
| `--cyan-dim` | `#2F8C80` | Unlit organisms; printed dim states, skeleton clusters | on midnight 4.62:1 |
| `--gold` | `#E9C46A` | Dinoflagellate light; the honoured species, seals, totals | on midnight 11.20:1 |
| `--gold-deep` | `#A8823C` | Error markers, hairline rules under gold | on midnight 5.28:1 |
| `--predator` | `#D64541` | The predator only. Signal, never text, never UI chrome | on midnight 4.27:1 |

**Usage ratio across a typical page:** midnight 78%, water-2 12%,
water-3 4%, bone 3%, cyan 2%, gold 0.8%, predator under 0.2% — and
predator's share is measured in *time*, not area: at most one red
light on screen, at most one pass per 45 s (§6.10).

**Pairing rules.** Bone and bone-dim are the only text colours on
midnight and water-2. Cyan may set links and short data labels
(10.69:1) but never body copy — light is data, not prose (§3 law 2).
Gold sets totals and the honoured species' figures (11.20:1), never
running text. Cyan-dim at 4.62:1 is ruled graphics-and-large-labels
only: unlit organism dots, skeleton clusters, axis print at ≥14 px —
never a sentence. Predator red is forbidden as text, as a button, as
an error colour and as a link colour, on any ground; on water-2 it
falls to 3.79:1 and is forbidden there entirely — the predator crosses
only open midnight. Error states use gold-deep markers plus bone text
(§6.14): in this census, red means something alive and dangerous, and
a form error is neither. The primary button is a cyan fill with
midnight text (10.69:1); the honoured action (submitting a sighting)
is a gold fill with midnight text (11.20:1).

**Dark-mode behaviour.** There is none, by ruling: the census is
taken at midnight, and a light scheme would be a different body of
water. `color-scheme: dark` is declared so form controls and
scrollbars render in their dark forms. The *print* stylesheet is the
one inversion: bone paper, midnight text, organisms printed as their
recorded figures and a static dot census in cyan-dim — a printed
sheet a naturalist could pin above a desk.

## 3. Typography

Two families, as in the original entry. **Fraunces** (display — the
naturalist's journal serif, optical sizing on, `SOFT` axis at 40 for
display sizes) carries headlines, species names and the standfirst.
**Space Grotesk** carries body, data, labels and UI; its numerals are
used with `font-variant-numeric: tabular-nums` everywhere a figure
can change, so a counting total never changes width as it climbs.

| Role | Font | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Display 1 (hero) | Fraunces 560 | clamp(2.75rem, 6vw, 4.5rem) / 1.04 | −0.01em | Never set in cyan or gold |
| Display 2 (section) | Fraunces 560 | 2.25rem / 1.12 | −0.005em | One per stratum |
| Display 3 (card/species) | Fraunces 520 | 1.5rem / 1.2 | 0 | Species names |
| Figure (pinned) | Space Grotesk 600 | clamp(3rem, 9vw, 6.5rem) / 1 | 0 | The printed twin of §6.3's bloom |
| Figure (inline) | Space Grotesk 600 | 1.75rem / 1.2 | 0 | Totals, table figures |
| Body | Space Grotesk 400 | 1.0625rem / 1.65 | 0 | Measure 34–38rem |
| Data label | Space Grotesk 500 | 0.8125rem / 1.4 | 0.08em, uppercase | Bone-dim or cyan |
| Caption | Space Grotesk 400 | 0.8125rem / 1.5 | 0.01em | Bone-dim |
| Depth readout | Space Grotesk 600 | 0.9375rem / 1 | 0.04em | Tabular; "128 fm" |

**Five type laws.** (1) *Fraunces never carries a number.* Figures
are Space Grotesk, always — the journal voice narrates, the ledger
voice counts, and they never swap. (2) *Light is never prose.* Cyan
and gold set labels, links and figures; a paragraph in either is a
defect (§9). (3) *The printed figure sits directly beneath its
bloom.* Every aggregated number (§6.3) and the counting total (§6.4)
is twinned with the same figure printed in bone within 24 px below
the light-figure — the bloom is the portrait, the print is the
record, and neither appears without the other. (4) *Red never sets a
glyph.* No character on the page is ever predator-coloured. (5)
*Italic is reserved for Latin.* Fraunces italic is used only for
binomial names (*Noctiluca scintillans*); emphasis in prose is
weight, never italic, so a Latin name reads as a different species of
text on sight.

## 4. Layout language

The page is a single column of print sunk in a full-viewport canvas
of water. The canvas (`position: fixed`, behind everything, `z-index:
0`) carries the swarm, the motes and the glow fields; the content
column (`max-width: 72rem`, print measure 34–38rem for prose) floats
above it at `z-index: 1`. The margins are not empty space — they are
the water the swarm schools in, and the layout is designed
margin-first: at ≥1200 px the left margin (13rem) holds the depth
line (§6.5) and the right margin (7rem) holds the current line
(§6.6); the swarm's schooling density is highest in the margins and
at section edges, thinnest behind the text measure, because organisms
part around print (§6.2).

**Strata are the section rhythm.** Sections are grouped under the
three census strata, and the water darkens as the reader sinks: the
Shallows sections sit on `--midnight`, the Twilight Shelf on a ground
lerped 40% toward `--midnight-deep`, the Midnight Shelf on
`--midnight-deep` itself — the background transition is scrubbed by
the shared loop (§5) across each stratum boundary's 40vh of travel,
so sinking is something the reader's eyes adjust to gradually, the
way a diver's do. Stratum headers are full-width bands: the stratum
name in Fraunces, its depth range in the data voice, and its count —
the pinned figure stage (§6.3) belongs to these bands.

**Density rules.** At most one pinned figure stage per viewport
height × 2.5 — aggregation is ceremony and rations itself. At most
one volumetric image (§6.9) per section. Glow fields (radial
gradients behind figures and frames) never overlap each other; two
glows in one viewport must be separated by at least 30vh of plain
water. The print itself is calm: sections breathe at 18vh gaps in the
Shallows, 22vh in the Midnight Shelf — the deeper the water, the
slower the page.

**The stage.** The pinned figure stage is a centre-screen field
100vh tall in which the section's key figure aggregates (§6.3). It
contains no text block of its own besides the figure, its printed
twin and one caption line: the stage is the census's lectern, and
nothing else is allowed to stand on it.

## 5. Full motion system

One requestAnimationFrame loop runs everything: the boid simulation,
the scroll lerp, the depth and current lines, the ripples. There is
no second loop and no CSS-driven scroll effect; if it moves with
scroll, it reads the loop's lerped progress.

**Named easings.**
- `--ease-bloom`: cubic-bezier(0.17, 0.89, 0.32, 1.28) — a flare's
  attack: fast rise, slight overshoot, slow decay. All brightness
  changes.
- `--ease-drift`: cubic-bezier(0.25, 0.46, 0.45, 0.94) — water
  gliding to rest. Hovers, gathers, card returns.
- `--ease-sink`: cubic-bezier(0.55, 0.06, 0.68, 0.19) — accelerating
  descent. Dispersals, the transition's sink.
- `--ease-surge`: cubic-bezier(0.65, 0, 0.35, 1) — a current's push:
  slow, strong, slow. The current pulse, stratum darkening.
- `--ease-settle`: cubic-bezier(0.22, 1, 0.36, 1) — buoyant settle;
  the character of the scroll lerp itself.

**Scroll model.** Native scroll is never hijacked. The loop keeps a
target (real scroll position) and a lerped value at factor **0.08**
per frame at 60 Hz — deliberately heavy, so the water feels viscous
and every scrubbed value (depth, darkening, parting, aggregation)
trails the reader's hand by ~180 ms and settles without a bounce.
Scrubbed values read the lerped progress; discrete triggers (pin
enter/exit, reveals) read the real scroll position so nothing fires
late. Scroll velocity (px/s, from the lerped value) is published by
the loop and consumed by the depth comet's brightness (§6.5) and by
the swarm's turbulence: at velocity above 1,800 px/s the motes
streak and the swarm's cohesion weight drops 30% — fast sinking
stirs the water.

**Parallax — three true rates.** Far motes drift at 0.94×, mid-water
particulate at 0.98×, content at 1.0×. The organisms themselves do
not parallax — they are simulated, not layered; their apparent depth
comes from size (1–3 px) and baseline brightness (0.35–1.0). Glow
fields behind volumetric frames translate at 0.97×.

**Motion terms, translated or refused.** Scroll-triggered reveals:
sections print in with a 400 ms `--ease-drift` rise of 12 px as the
swim descends past them — print first, light second; the swarm's
parting (§6.2) is the reveal's visible half. Masked line reveals:
refused for headlines — the headline resolves in clustered lights
(§6.1), which is this theme's masked reveal performed by organisms.
Blur-to-sharp: refused — light does not focus; images surface by
scale and glow (§6.9). Animated counters: the census total (§6.4),
counted by the counted. Progress indicator: the depth line (§6.5).
Marquee: refused — the current line (§6.6) is the only looping
travel on the page, and it carries the eye downward, not sideways.
Kinetic typography: refused for prose; the one kinetic type event is
the counting total's digits forming and dissolving (§6.4). Magnetic
hover: refused — water has no magnets; attention is a bloom (§6.7).
Tilt: licensed only on ledger cards, max 3°, as a specimen tray
tilting in water (§6.12). Custom cursor: refused — the system cursor
stands; the pointer's presence in the water is shown by the swarm
fleeing it ~60 px (§6.2), which is feedback, not a cursor. Page
transitions: dispersal and re-bloom (§6.15). Skeleton loading: unlit
clusters (§6.15). Ambient loops: exactly three are licensed — the
swarm (§6.2), the current pulse (§6.6), mote drift. The predator
pass (§6.10) is an event on a randomised schedule, not a loop.

**Simulation parameters (the swarm, §6.2).** 160 organisms at
≥1200 px, 110 at 768–1199 px, 64 below 768 px. Perception radius
46 px; separation radius 22 px; weights — separation 1.6, alignment
1.0, cohesion 0.8; maximum speed 54 px/s; pointer flee radius 60 px
at strength 2.2; content-parting: registered content blocks act as
soft obstacles with a 24 px margin, steering force 1.4. Simulation
step is dt-clamped at 33 ms so a stalled frame cannot teleport the
school. Brightness per organism: baseline 0.35–1.0 by individual,
breathing ±12% on a 3.2 s sine offset per organism — no two
organisms pulse together.

## 6. Signature elements

### 6.1 The bloom-wave hero

- **What & why.** The page opens in darkness — true `--midnight`,
  print not yet risen. A disturbance ripple expands from screen
  centre and hundreds of lights flare in a wavefront as the ring
  passes, brightness peaking at the ring and decaying over ~1.5 s;
  in the ring's wake the headline stands revealed, written in
  clustered lights that hold and breathe faintly, its printed twin
  beneath it in bone. It belongs because it is the census's method
  performed before a word is read: disturb the water and the water
  answers with light. The hero does not introduce the data; the data
  introduces itself by behaving.
- **Structure.** A real `<h1>` in the DOM at full bone contrast from
  first paint, inside a 100vh hero section. The canvas (§6.2) is
  fixed behind the whole page; the hero's bloom is a mode of that
  canvas, not a second one. The headline's light-form is rendered by
  the swarm itself: target points are sampled from the headline's
  glyphs (offscreen canvas, Fraunces at computed size, 6 px sampling
  grid, alpha > 128), capped at 110 targets; the remaining organisms
  keep schooling so the hero never empties the water. A printed
  standfirst and the census total (§6.4) complete the hero's print.
- **Motion spec.** Trigger: load, once per session
  (`sessionStorage` — a returning visitor finds the hero already
  bloomed and lit, no ceremony repeated). Gated on
  `document.fonts.ready` raced against 900 ms: glyph sampling in a
  fallback face would misplace the lights, so if fonts lose the
  race the hero ships lit and printed, ceremony skipped. t=0:
  ripple ring expands from centre at 420 px/s; organisms flare as
  the front passes (brightness to 2.4× baseline, `--ease-bloom`,
  decay 1,500 ms). Headline targets ignite as the ring crosses them
  (t≈400–900 ms); cluster holds, breathing ±8%. Print rises last:
  standfirst and total fade-rise 400 ms `--ease-drift` at t=900.
  Total ceremony ≤2,400 ms.
- **States.** Dark (JS-armed only, pre-load) → blooming → lit
  (rest). Hover/focus: none of its own — the hero is not a control;
  pointer presence is answered by the swarm's flee (§6.2). Focus
  entering the hero (keyboard) cancels the ceremony to the lit
  state instantly. Scrolled away mid-bloom: the bloom completes off
  screen; returning shows the lit hero.
- **Content merge.** The lights that form the headline are census
  organisms on loan from the swarm, and the headline they write is
  the census's name — the title is a bloom of the data it titles.
  When the visitor scrolls, the headline cluster disperses back into
  general schooling over 800 ms: the title literally rejoins the
  population it announced.
- **Failure fallback.** Watchdog at 2,800 ms: if the bloom has not
  completed (fonts stalled, canvas slow), the hero snaps to lit —
  headline cluster formed, print at full contrast. No JS: no dark
  state is ever applied; the hero ships printed and the canvas
  never exists. Canvas failure after load: the bloom-fallback
  (§6.2) renders the headline cluster as a static CSS glow field
  behind the printed `<h1>`.
- **Reduced-motion variant.** The lit hero, still: headline printed,
  a static printed dot-field (cyan-dim) behind it standing in for
  the cluster, no ripple, no breathing. The census total is printed,
  not counted (§6.4).
- **Performance budget & mobile variant.** Glyph sampling ≤8 ms
  once, offscreen 1024×256 canvas, freed after sampling. Hero adds
  no assets beyond the shared canvas. Mobile (<768 px): 64
  organisms page-wide, headline targets capped at 64, ripple speed
  300 px/s, ceremony ≤1,800 ms.
- **Choreography timeline (v2).** t=0 fonts ready (or 900 ms race
  lost → lit state, ceremony skipped) → t=0–1,100 ripple expands →
  t≈400–900 headline targets ignite as the ring crosses → t=900
  print rises → t=1,500 last flare decays → t=2,400 hero at rest,
  cluster breathing. Watchdog ceiling 2,800 ms.
- **State matrix (v2).** *Rest (return visit):* lit, cluster
  breathing, print up. *Hover:* none (swarm flee only). *Focus:*
  focus within cancels ceremony to lit. *Active:* n/a.
  *Scrolled-past:* cluster dispersed into schooling; returning
  re-forms it in 600 ms `--ease-drift` without the ripple.
  *Disabled / no-JS:* printed lit hero at first paint. *Touch:*
  identical; first touch-drag is a scroll and disperses the cluster
  as on desktop.
- **Breakpoints (v2).** ≥1200 px: 110 headline targets, ripple
  420 px/s. 768–1199 px: 88 targets, ripple 360 px/s.
  <768 px: 64 targets, ripple 300 px/s, hero 92vh so the first
  stratum header shows its edge — the descent is advertised.
- **Edge cases & failure modes (v2).** *Very long headline (CMS
  edit):* sampling caps targets at the cap and reduces sampling
  density to 8 px rather than borrowing more organisms — the water
  never empties for a title. *Tab hidden mid-bloom:* rAF pauses;
  on return, wall-clock beyond 2,800 ms fires the watchdog.
  *Headline in a language with complex glyphs:* sampling is
  alpha-based and script-agnostic; if sampled points < 40% of cap,
  the cluster falls back to a halo formation behind the print.
- **Accessibility spec (v2).** The `<h1>` is complete in the
  accessibility tree from first paint at 14.99:1; the canvas is
  `aria-hidden` and the bloom is never announced. The ceremony is
  not focusable and steals no focus. Brightness peaks stay under
  the photosensitivity ceiling in §10 (no more than 3 flashes per
  second anywhere; the bloom is one wave, not a strobe).
- **Tokens consumed (v2).** `--midnight`, `--bone`, `--cyan`,
  `--gold`, `--cyan-dim`, `--ease-bloom`, `--ease-drift`,
  `--dur-bloom` (2400 ms), `--dur-watchdog-hero` (2800 ms),
  `--swarm-hero-targets` (110).

### 6.2 The flocking swarm

- **What & why.** The page's resident population: 160 simulated
  organisms running continuous flocking — separation, alignment,
  cohesion — in the water around the real content. They school in
  the margins, part around text blocks as the reader sinks past
  them, flee the pointer by ~60 px and regroup. It belongs because
  it is the census's subject, alive on the page: the document and
  the ecosystem are one system, and the swarm's behaviour is shaped
  by the content's layout, so the light-play can never be mistaken
  for decoration pasted over the print.
- **Structure.** One fixed full-viewport `<canvas>` at `z-index: 0`,
  devicePixelRatio capped at 1.5. Organisms are pre-rendered sprites
  (radial-gradient dots in cyan, gold, cyan-dim and predator tints,
  3 sizes, drawn once to offscreen canvases) composited with
  `globalCompositeOperation: 'lighter'` — no per-frame gradient
  allocation. Content blocks register their rectangles (with 24 px
  margin) into an obstacle list on layout and on resize; the
  simulation steers around them. Species tint is assigned by the
  census sheet's proportions (§6.17): of 160 organisms, 65 gold
  *Noctiluca scintillans*, 34 cyan *Pyrocystis fusiformis*, 26
  cyan *Lingulodinium polyedra*, 17 cyan *Ceratium horridum*, 12
  gold *Pyrodinium bahamense*, 6 cyan-dim unclassified — the
  sheet's shares × 160, rounded, with the unclassified taking the
  remainder so the school sums exactly (§6.17).
- **Motion spec.** Continuous simulation on the shared rAF loop
  (§5): perception radius 46 px, separation radius 22 px, weights
  separation 1.6 / alignment 1.0 / cohesion 0.8, max speed 54 px/s,
  dt clamped at 33 ms. Pointer flee: radius 60 px, strength 2.2,
  organisms return to schooling as the pointer leaves. Content
  parting: obstacle steering force 1.4, so a text block entering
  the viewport pushes a slow bow-wave of organisms ahead of it
  rather than being swum through. Baseline brightness 0.35–1.0 per
  organism, breathing ±12% on individual 3.2 s sines. Turbulence:
  scroll velocity >1,800 px/s drops cohesion to 0.56 and streaks
  motes (§5).
- **States.** Schooling (rest) → parting (content passing) →
  fleeing (pointer near) → gathering (hover bloom §6.7, aggregation
  §6.3) → settling (footer floor, §6.18). Disabled state: if the
  canvas context fails or the device reports
  `hardwareConcurrency ≤ 2` with a low-memory flag, the swarm does
  not start and the static fallback stands. Scrolled-past is not a
  state the swarm has — it is viewport-bound, always present tense.
- **Content merge.** The swarm is routed by the content: obstacle
  rectangles are the text itself, margins are its habitat, and its
  members are on constant loan to the content's figures (§6.3),
  totals (§6.4) and hovers (§6.7). Remove the content and the
  choreography has nothing to school around — the test §10 applies.
- **Failure fallback.** Watchdog at 1,200 ms after load: if the
  first frame has not rendered, the canvas is removed and a static
  printed dot-field (CSS radial-gradient pattern, cyan-dim at 18%
  brightness, positioned in the margins only) stands in — the
  census still printed as dots, the page fully readable. No JS:
  the dot-field is the shipped state and the canvas is only ever
  added by script. Context lost mid-session (`webglcontextlost`'s
  2D equivalent — context restore failure): same snap to the
  dot-field, figures unaffected because print is authoritative.
- **Reduced-motion variant.** No simulation. The static dot-field
  stands in the margins at rest brightness; figures print; the page
  is a still, fully lit census — the original entry's reduced-motion
  ruling, kept verbatim in spirit.
- **Performance budget & mobile variant.** Simulation + render
  ≤4 ms per frame at 160 organisms on a mid-range laptop; sprite
  compositing only, no shadowBlur (banned — it is the classic
  canvas budget-killer). Mobile (<768 px): 64 organisms, DPR cap
  1.25, obstacle list limited to blocks in/near the viewport,
  budget ≤3 ms per frame. Battery saver / `prefers-reduced-data`:
  swarm runs at 30 Hz (every other frame) with speeds halved.
- **Choreography timeline (v2).** Load → t=0 dot-field visible
  (printed state) → t≤1,200 first simulated frame replaces it
  seamlessly (organisms spawn at dot-field positions, so the water
  "wakes" rather than pops) → continuous schooling → on scroll,
  parting waves lead content by ~200 ms of travel → on pin stages,
  loans depart (§6.3) and return on dispersal.
- **State matrix (v2).** *Rest:* schooling in margins. *Hover:*
  local members lent to §6.7's bloom. *Focus:* keyboard focus on
  an element triggers the same local gather as hover, at the
  element's edge. *Active:* click lends members to §6.8's ripple.
  *Scrolled-past:* n/a (viewport-bound). *Disabled:* dot-field.
  *Touch:* no pointer flee (no pointer); touch-drag turbulence
  applies through scroll velocity instead.
- **Breakpoints (v2).** ≥1200 px: 160 organisms, full margins as
  habitat. 768–1199 px: 110 organisms, margins narrow — schooling
  shifts to section edges and the stage field. <768 px: 64
  organisms, habitat is above/below content blocks only (the single
  column leaves no side margins); parting margin 16 px.
- **Edge cases & failure modes (v2).** *Content taller than
  expected (long article):* obstacle list is windowed to ±1
  viewport around the current scroll position and rebuilt on
  scroll settle — memory stays flat on a 50-section page. *Resize
  / rotation:* obstacles re-registered, organisms clamped inside
  the new viewport, no organism may be left outside the water.
  *Very fast scroll to the footer:* turbulence state, then the
  floor settling (§6.18) takes over within 600 ms. *Two fingers /
  pointer leaves window:* flee force decays to zero over 300 ms —
  no permanent dent in the school.
- **Accessibility spec (v2).** Canvas is `aria-hidden`, pointer
  events none; it is never the sole carrier of any information —
  every figure it forms is printed in bone (§3 law 3). Motion
  sensitivity: the reduced-motion variant removes the simulation
  entirely, and §10's gate includes a vestibular check — organism
  speed (54 px/s max) is below the threshold where peripheral
  motion dominates the page.
- **Tokens consumed (v2).** `--midnight`, `--cyan`, `--gold`,
  `--cyan-dim`, `--predator`, `--swarm-count` (160), `--swarm-perception`
  (46 px), `--swarm-flee-radius` (60 px), `--ease-drift`,
  `--loop-lerp` (0.08).

### 6.3 Digit-aggregation numbers

- **What & why.** Each stratum's key figure gets a pinned
  centre-screen stage (§4): as the stage pins, organisms stream in
  and aggregate into the shapes of the figure's digits — target
  points sampled from the numeral glyphs — hold ~1.2 s while the
  reader reads a number made of the population it counts, then
  disperse back into the swarm as the stage exits. It belongs
  because it is the theme's thesis in one gesture: the statistic is
  *composed of* the counted. A bar chart describes a census; this
  figure is one.
- **Structure.** A stage section of 220vh scroll length with a
  sticky 100vh inner stage. The figure's printed twin (§3 law 3) is
  real text in the sticky stage from first paint — Space Grotesk
  600 at the Figure size, bone, centred, with its caption ("counted
  in the Shallows, 0–30 fm"). The light-figure forms on the shared
  canvas directly over the printed twin's position: digit target
  points are sampled from an offscreen rendering of the same figure
  string in Space Grotesk 600 (7 px grid, alpha > 128), so the
  bloom and the print are the same glyphs in two media. Up to 140
  of the swarm's organisms are reserved for the formation; at least
  20 always remain schooling — the water never empties for a number.
- **Motion spec.** Trigger: stage pin (sticky engagement, read from
  real scroll). Aggregation: reserved organisms receive targets and
  steer to them over 900–1,400 ms (nearer organisms arrive first —
  arrival is staggered by distance, not choreographed by index),
  brightness rising to 1.6× as each locks (`--ease-bloom`). Hold:
  1,200 ms at full formation, breathing ±6%. Dispersal: on pin
  exit, targets release over 800 ms `--ease-sink`, organisms
  rejoin schooling. Re-entry (scroll back up): re-aggregation is
  faster — 700 ms — the census remembers being counted. The whole
  cycle is scrubbed by nothing; it is triggered, held and released
  by the pin, because a number half-formed by scrub would be a
  number mis-stated.
- **States.** Printed (rest — twin visible, no formation) →
  aggregating → held → dispersing → printed. Hover: none — the
  stage is not a control. Focus: focus entering the stage (a
  keyboard reader reaching the figure) forms the figure instantly
  at held state — no one waits 1.4 s for a number. Scrolled-past:
  printed; the formation does not chase the reader. Disabled:
  canvas absent → printed only, which is complete.
- **Content merge.** The figure is the section's own key statistic
  from the census sheet (§6.17) — 31,204 in the Shallows, 19,876 on
  the Twilight Shelf, 10,328 on the Midnight Shelf — and the
  caption names the stratum and its depths. The organisms forming
  it are tinted by the stratum's species mix (§6.2), so the
  Shallows figure is mostly cyan with its gold minority visible in
  the digits themselves.
- **Failure fallback.** Watchdog per stage at 2,000 ms from pin: if
  the formation has not reached held state (canvas stalled, tab
  throttled), targets release and the printed twin stands alone —
  it was never hidden, so nothing is lost. No JS: no pin, no
  formation; the stage is a static centred figure with its caption,
  fully legible. Slow device: if frame budget is exceeded twice
  (§14), the formation's reserve drops to 90 organisms and the
  sampling grid coarsens to 9 px — the digits read slightly
  softer, the number identical.
- **Reduced-motion variant.** No pin, no aggregation. The figure
  prints at stage centre with a static cyan-dim dot halo behind it
  (the dot-field treatment), held for exactly as long as the reader
  stays — which is the honest still version of the same census.
- **Performance budget & mobile variant.** Sampling ≤6 ms per
  figure, once, cached per figure string. Formation adds no
  per-frame cost beyond §6.2's simulation (targets are steering
  goals, not new objects). Mobile (<768 px): stage 160vh, reserve
  56 of 64 organisms, grid 9 px, hold 1,200 ms unchanged — the
  ceremony is not shortened on small screens, only softened.
- **Choreography timeline (v2).** Pin engages → t=0 reserve
  organisms peel from schooling → t=0–1,400 arrivals stagger by
  distance, locking brightness rising → t=1,400 formation complete
  → hold 1,200 ms → pin exit → t=0–800 dispersal `--ease-sink` →
  organisms rejoin schooling. Watchdog ceiling 2,000 ms from pin.
- **State matrix (v2).** *Rest:* printed twin, swarm schooling
  past. *Hover:* none. *Focus:* instant held formation. *Active:*
  n/a. *Scrolled-past:* printed; re-entry re-forms in 700 ms.
  *Disabled / no-JS:* printed figure and caption only. *Touch:*
  identical; the pin is scroll-driven, not gesture-driven.
- **Breakpoints (v2).** ≥1200 px: 220vh stage, reserve 140, grid
  7 px. 768–1199 px: 200vh stage, reserve 96, grid 8 px. <768 px:
  160vh stage, reserve 56, grid 9 px, figure size steps down one
  scale stop so a 6-digit figure fits the measure.
- **Edge cases & failure modes (v2).** *Figure with more digits
  than the reserve can draw (a build counting millions):*
  sampling density coarsens automatically (grid grows until
  targets ≤ reserve); if still over, the formation draws the
  figure at a smaller size — the number is never truncated or
  rounded to fit the light. *Two stages adjacent:* stages are
  separated by ≥250vh of ordinary sections (§4 density rule), so
  reserves never compete. *Reader parks on the pin:* hold extends
  indefinitely at breathing ±6% — a held figure is a feature, not
  a timeout.
- **Accessibility spec (v2).** The printed twin is the accessible
  figure: a real text node, in the reading order at the stage's
  position, announced once as text ("31,204 — counted in the
  Shallows"). The canvas formation is `aria-hidden`. Contrast is
  the print's (14.99:1) at all times, including mid-formation —
  the bloom adds light around a figure that is already legible.
- **Tokens consumed (v2).** `--bone`, `--cyan`, `--gold`,
  `--cyan-dim`, `--water-3`, `--ease-bloom`, `--ease-sink`,
  `--dur-aggregate` (1400 ms), `--dur-hold` (1200 ms),
  `--dur-disperse` (800 ms), `--swarm-reserve` (140),
  `--dur-watchdog-stage` (2000 ms).

### 6.4 The counting census total

- **What & why.** In the hero, beneath the headline, the census
  total counts up organism by organism: the light-figure's digits
  form, dissolve and reform as the count climbs through
  intermediate values, settling at the true total — 61,408 — where
  the printed twin has stood all along. It belongs because counting
  is this census's core act, and the total should be *performed by
  the counted*: the number accumulates the way a bloom accumulates,
  one organism at a time, instead of spinning like a slot machine.
- **Structure.** The printed total is a real text node (Space
  Grotesk 600, inline-figure size, bone) with its label ("organisms
  counted, 38 nights, 96 stations"). Above it, on the shared
  canvas, a light-figure field ~0.9× the printed figure's width
  renders the climbing value: at each step, the current value's
  glyphs are sampled (same sampler as §6.3, 8 px grid, cap 90
  targets) and a subset of hero organisms holds the formation for
  one beat before the value advances. Intermediate values are not
  random: they are the count itself at sampling beats — the value
  at beat *k* is round(61,408 × easeOutCubic(k/26)) — so the climb
  decelerates as it approaches the truth, like a tally nearing its
  end.
- **Motion spec.** Trigger: hero bloom completing (§6.1), or scroll
  into view on a return visit. 26 beats over 2,340 ms (90 ms per
  beat): at each beat the light-figure dissolves (brightness to
  30% over 40 ms) and reforms at the new value (to 1.5×,
  `--ease-bloom`). Final beat: the formation holds 600 ms at 1.6×,
  then releases its organisms back to schooling over 800 ms,
  leaving the printed total alone in the hero — the count ends, the
  record remains. Runs once per session; a return visit shows the
  settled total.
- **States.** Printed (rest, before and after) → counting → settled
  (printed, organisms released). Hover on the total: the printed
  figure does not move; organisms nearby bloom locally (§6.7) —
  the total is print, and print is still. Focus: focus on the
  total's region skips the count to settled. Scrolled-past
  mid-count: the count completes off-screen by watchdog rather
  than freezing half-climbed.
- **Content merge.** The number counted is the census sheet's
  total (§6.17), and its label carries the sheet's effort figures
  (38 nights, 96 stations) — the hero's three numbers are the
  sheet's first three lines. The organisms performing the count are
  the hero cluster's members (§6.1), borrowed from the headline
  formation as it disperses — the title's lights become the
  total's.
- **Failure fallback.** Watchdog at 3,200 ms from trigger: if the
  count has not settled, the light-figure clears and the printed
  total stands — it was complete from first paint, so the failure
  is invisible. No JS: the printed total only. Canvas failure: as
  §6.2's dot-field fallback; the count simply never performs.
- **Reduced-motion variant.** The printed total, settled, with the
  static dot halo. No counting — a reduced-motion reader is given
  the record, not the performance.
- **Performance budget & mobile variant.** Sampling per beat ≤2 ms
  (values cached after first computation — the 26 values are
  deterministic, sampled once). Mobile (<768 px): 18 beats over
  1,800 ms, target cap 56, other parameters unchanged.
- **Choreography timeline (v2).** Hero bloom completes → t=0 beat
  1 (value ≈ 2,300) forms → beats every 90 ms, dissolve/reform →
  t=2,340 final value 61,408 forms → hold 600 ms at 1.6× →
  t=2,940–3,740 organisms release to schooling → printed total
  alone. Watchdog ceiling 3,200 ms.
- **State matrix (v2).** *Rest (return visit):* settled print.
  *Hover:* local bloom only (§6.7). *Focus:* skip to settled.
  *Active:* n/a. *Scrolled-past:* watchdog completes the count.
  *Disabled / no-JS:* printed total. *Touch:* identical.
- **Breakpoints (v2).** ≥1200 px: 26 beats, cap 90 targets.
  768–1199 px: 22 beats over 2,200 ms, cap 72. <768 px: 18 beats
  over 1,800 ms, cap 56.
- **Edge cases & failure modes (v2).** *A build whose total is
  small (a pond census of 212):* beats scale down — one beat per
  ~8% of the total, minimum 8 beats — so the ceremony fits the
  number and never counts past it. *Total edited in a CMS:* the
  count reads the printed node's value at runtime; the light
  climbs to whatever the print says — print leads, light follows,
  they cannot disagree. *Reader with a screen reader:* the count
  is silent; the settled value is the only one in the tree.
- **Accessibility spec (v2).** The printed total is a single text
  node with its final value from first paint — assistive tech
  never encounters an intermediate value, because the light-figure
  is canvas (`aria-hidden`) and the print never changes. No
  `aria-live` — a counting total must not chatter.
- **Tokens consumed (v2).** `--bone`, `--cyan`, `--gold`,
  `--ease-bloom`, `--ease-drift`, `--dur-count` (2340 ms),
  `--count-beats` (26), `--dur-watchdog-count` (3200 ms).

### 6.5 Depth-line progress

- **What & why.** In the left margin, a sounding line descends the
  page: a hairline of cyan-dim with a short comet of full cyan
  light (~80 px) trailing the reader's position, and at the rail's
  foot a printed readout of current depth in fathoms — 0 fm at the
  surface, 550 fm at the floor. It belongs because progress in this
  census is not a percentage consumed but a depth attained: the
  reader is sinking into the data, and the line is the
  naturalist's plumb line paying out beside them, in the census's
  own unit.
- **Structure.** A fixed left rail (≥1200 px: 13rem margin, rail at
  its inner edge) containing an SVG line (2 px, cyan-dim at 40%)
  drawn to the page's full height fraction, the comet as a second
  SVG segment with a gradient mask, and the readout as a real text
  node updated by the loop (throttled to changes of ≥1 fm). The
  line's drawn fraction is the lerped read fraction (§5); the
  readout value is `round(550 × readFraction)`, computed from the
  real scroll position so the number is never wrong, only the
  comet is smoothed. Stratum boundaries are marked on the rail at
  their scroll positions with small bone-dim ticks and labels
  ("30 fm — Twilight Shelf").
- **Motion spec.** Continuous, scrubbed by the shared loop (lerp
  0.08). The comet's brightness pulses with scroll velocity:
  brightness = 0.7 + 0.6 × clamp(velocity / 2,400 px/s), so a fast
  descent makes the sinking light flare and a resting reader's
  comet breathes at 0.7. At stratum boundaries the comet pauses
  its pulse for 300 ms and the boundary label lights from bone-dim
  to bone — crossing into deeper water is a small event. No other
  animation: the line is an instrument, and instruments are steady.
- **States.** Rest (velocity 0): comet at 0.7 brightness, readout
  current. Scrolling: comet flares with velocity. Focus: keyboard
  scrolling moves the line identically — it reads scroll position,
  not input type. Scrolled-past / at floor: readout 550 fm, comet
  rests at the line's foot and dims to 0.5 — the descent is
  complete. Disabled / no-JS: the rail prints as a static stratum
  index (the three stratum labels with their depth ranges, no
  live readout) — still useful, still true.
- **Content merge.** The readout's 550 fm ceiling is the census
  sheet's deepest stratum boundary (§6.17), the ticks are the
  strata the reader is passing through, and the foot of the line
  is the footer (§6.18) where the swarm settles on the floor — the
  progress indicator, the page geography and the data's depth
  structure are one drawing.
- **Failure fallback.** Watchdog: the readout is a text node
  updated from a scroll listener independent of the canvas loop —
  if the rAF loop dies, the line freezes but the readout keeps
  updating on scroll events (degraded, still true). No JS: static
  stratum index as above. Canvas failure does not touch this
  element at all — it is SVG and text, deliberately independent of
  the swarm, so the reader's depth survives the ecosystem.
- **Reduced-motion variant.** The line and readout remain — they
  are information, not ornament — but the comet's velocity pulse
  is removed (fixed 0.85 brightness) and boundary lighting is
  instant rather than eased.
- **Performance budget & mobile variant.** One SVG segment update
  and at most one text update per frame; ≤0.1 ms. Mobile
  (<1200 px): the left rail does not exist — the depth readout
  moves into the navigation bar (§6.11) as a compact "128 fm"
  readout beside the wordmark, and the line itself is cut (the
  descent is reported, not drawn). §14's cut order protects this
  element last among margin features.
- **Choreography timeline (v2).** Page load → rail prints, readout
  0 fm → first scroll → comet ignites at the line's head → descent:
  comet trails lerped position, flaring with velocity → stratum
  tick reached → 300 ms pulse pause, label lights → floor: readout
  550 fm, comet dims to rest.
- **State matrix (v2).** *Rest:* comet 0.7, readout current.
  *Hover:* none — the rail is not interactive. *Focus:* follows
  keyboard scroll identically. *Active:* n/a. *Scrolled-past*
  (returning up): the line rewinds with the same lerp — depth is
  reversible and the readout falls as the reader rises.
  *Disabled / no-JS:* static stratum index. *Touch:* identical;
  momentum scrolling reads through the same lerp.
- **Breakpoints (v2).** ≥1200 px: full rail, line, comet, ticks,
  readout. 768–1199 px: readout in the nav (§6.11), line cut, a
  2 px depth hairline under the nav shows fraction only.
  <768 px: readout in nav only.
- **Edge cases & failure modes (v2).** *Page shorter than two
  viewports:* the line still spans it; stratum ticks cluster —
  below a 150vh page the ticks print without labels to avoid
  collision. *Reader jumps to the floor (End key):* the readout
  snaps (it reads real scroll), the comet travels at most 600 ms
  to catch up — instruments may hurry, they may not lie.
  *Horizontal content overflow:* the rail is fixed and outside the
  content flow; overflow never pushes it.
- **Accessibility spec (v2).** The readout is exposed as a
  `progressbar`-equivalent only in its static form: an offscreen
  text "Reading depth: N of 550 fathoms" updated at stratum
  boundaries (not per fathom — no chatter). The SVG is
  `aria-hidden`. Contrast: readout bone on midnight 14.99:1;
  boundary labels reach bone (14.99:1) when lit, bone-dim
  (9.45:1) at rest — both pass for their sizes.
- **Tokens consumed (v2).** `--cyan`, `--cyan-dim`, `--bone`,
  `--bone-dim`, `--midnight`, `--ease-surge`, `--depth-max`
  (550 fm), `--loop-lerp` (0.08).

### 6.6 The current line

- **What & why.** An SVG current threads the right margin from
  surface to floor — a gently meandering path, mostly dark, along
  which a bright segment of light ~80 px long travels in a ~6 s
  loop: the water's movement made visible, carrying the eye down
  the page the way the current carries the organisms. It belongs
  because the margin's decoration is the water's own motion — the
  one licensed ambient travel on the page (§5 refuses the marquee
  in its favour), and because a census of drifting organisms needs
  the drift itself on the record.
- **Structure.** One inline SVG in the right margin (≥1200 px),
  path authored as a smooth vertical meander with three bends
  keyed to the page's strata. The path is stroked cyan-dim at 25%;
  the travelling pulse is the same path stroked cyan with a
  dasharray window (80 px lit, remainder transparent) and a soft
  glow filter, its dashoffset animated by the shared loop from
  wall-clock time (not scroll) — the current flows whether or not
  the reader moves. Where the path passes a section edge, two or
  three mote sprites drift along it on the canvas (§6.2's motes),
  so the line reads as the current's visible lane.
- **Motion spec.** Pulse travel: full path length in 6,000 ms,
  linear within each stratum, easing `--ease-surge` across stratum
  boundaries (the current quickens slightly in deep water: 6,400 ms
  in the Shallows, 5,600 ms on the Midnight Shelf — the loop period
  is stratum-dependent, read from the reader's current stratum).
  Pulse brightness 1.4× baseline, head brighter than tail (gradient
  along the 80 px). The loop is seamless: the pulse exits at the
  floor and re-enters at the surface during the footer (§6.18),
  where its re-entry is hidden by the floor's glow field.
- **States.** Flowing (rest and always). Hover: none. Focus: none.
  Scrolled-past: n/a — it is margin, present at every depth, its
  phase independent of scroll. Disabled: script absent → the path
  prints at cyan-dim 25% with no pulse — a charted current on a
  still chart, still true to the geography.
- **Content merge.** The current's bends are keyed to the strata,
  its lane carries real motes, and its direction teaches the
  page's reading direction — down, deeper. It is the only element
  allowed to be purely atmospheric, and it earns the licence by
  being the ecosystem's transport system, drawn where the
  ecosystem lives: the margin.
- **Failure fallback.** Watchdog: none needed beyond §6.2's — the
  pulse is a dashoffset on an SVG path; if the loop dies the pulse
  freezes mid-path as a lit segment, legible as a marked reach of
  current, not an error. No JS: static charted path as above.
- **Reduced-motion variant.** The pulse does not travel. The path
  prints with three fixed lit segments, one per stratum — the
  current charted at rest, its reaches marked.
- **Performance budget & mobile variant.** One dashoffset update
  per frame, ≤0.05 ms; the glow filter is applied to the short
  pulse segment only, never the full path. Mobile (<1200 px): cut
  entirely — the margins it threads do not exist; its pulse's role
  (a living margin) is inherited by the depth readout in the nav
  (§6.11). This is the first margin element in §14's cut order.
- **Choreography timeline (v2).** Load → path prints → pulse
  enters at surface → 6 s loop per stratum period → boundary
  crossings ease `--ease-surge` → at floor, pulse exits into the
  footer's glow and re-enters at the surface.
- **State matrix (v2).** *Rest:* flowing. *Hover:* none. *Focus:*
  none. *Active:* n/a. *Scrolled-past:* n/a. *Disabled / no-JS:*
  static charted path. *Touch:* identical (time-driven, not
  input-driven).
- **Breakpoints (v2).** ≥1200 px: full line and pulse.
  768–1199 px: cut (margin too narrow to thread honestly).
  <768 px: cut.
- **Edge cases & failure modes (v2).** *Very long page:* the path
  is generated per stratum segment and tiled — path length scales
  without authored SVG growing; the pulse period stays per-stratum,
  not per-page. *Reader at the floor for a long read:* the pulse
  keeps its loop beside the footer — acceptable, it is the water —
  but its brightness drops 20% while the footer is in view, so the
  colophon is read in calmer water.
- **Accessibility spec (v2).** Purely decorative and
  `aria-hidden`; it carries no information not printed elsewhere
  (strata are labelled on the depth rail, §6.5). Its motion is
  slow (one 80 px segment per 6 s) and removed entirely under
  reduced motion.
- **Tokens consumed (v2).** `--cyan`, `--cyan-dim`, `--ease-surge`,
  `--dur-current` (6000 ms), `--current-pulse` (80 px).

### 6.7 Local bloom hover

- **What & why.** Hovering — or focusing — any element disturbs
  the water around it: organisms within ~180 px flare to 2.2×
  brightness and gather toward the element's edge over ~600 ms,
  dimming back on leave. It belongs because bioluminescence *is*
  this ecosystem's response to attention — real dinoflagellates
  flash when the water around them is disturbed — so the hover
  state is produced by the element's own neighbourhood, in the
  medium's physics, instead of a colour swap invented by a style
  guide.
- **Structure.** A behaviour of the shared swarm (§6.2), not a DOM
  effect: interactive and hoverable elements register a bloom
  anchor (their bounding rect's nearest edge point). On
  pointerenter/focus, organisms within 180 px of the anchor
  receive a gather target on a ring 12 px outside the element's
  edge and a brightness multiplier ramping to 2.2; on leave, both
  release. The element itself also gets its print response — links
  brighten bone-dim → bone, cards lift their glow (§6.12) — but the
  bloom is the primary signal. Pointer and keyboard focus share
  the code path exactly.
- **Motion spec.** Gather: 600 ms `--ease-drift`, organisms
  arriving staggered by distance (nearest first, ~40 ms spread).
  Flare: brightness ramps to 2.2× over 250 ms `--ease-bloom` —
  faster than the gather, so the flash precedes the crowd, as in
  the water. Hold: while hovered, the ring holds with breathing
  ±10%; the flare settles to 1.7× after 900 ms so a long hover
  calms. Release: 500 ms `--ease-drift`, brightness first, then
  positions. Rapid re-hover of a neighbouring element: targets
  retarget without a brightness reset — the bloom slides along the
  page like a hand trailing in water.
- **States.** Rest (no bloom) → flaring → gathered → releasing.
  Focus state is identical to hover, triggered by `:focus-visible`
  as well as programmatic focus. Active (pressed): the bloom
  tightens — ring radius −6 px, brightness 2.4× for 120 ms — a
  small squeeze of light on the press. Disabled elements: no bloom;
  organisms treat a disabled control's edge as ordinary water —
  the absence of response is itself the disabled signal, backed by
  the print's dimming. Scrolled-past: an element scrolled out
  mid-hover releases immediately.
- **Content merge.** The bloom gathers at the attended thing's own
  edge and is made of its neighbouring organisms — attention is
  shown by the content's ecosystem, not by a halo graphic. On
  ledger cards (§6.12) the bloom is the card's hover state; on
  table rows (§6.13) it gathers along the row's margin edge; on
  the form (§6.14) it follows field focus — one behaviour, every
  surface, always the element's own water.
- **Failure fallback.** Watchdog: the bloom is a steering overlay
  on §6.2; if the canvas is absent or has fallen back, hover falls
  back to print-only responses (link colour, card glow, focus
  ring) which are fully specified per component in §11 — no
  interactive element depends on the canvas to show its state.
  No JS: print responses only, via CSS `:hover`/`:focus-visible`.
- **Reduced-motion variant.** No gather, no flare travel: organisms
  near a hovered element simply brighten in place to 1.5× (a
  colour-value change, not a motion), and print responses carry
  the state. Under the static dot-field fallback, hover is
  print-only.
- **Performance budget & mobile variant.** The gather touches at
  most the ~30 organisms within 180 px; steering targets only,
  ≤0.3 ms per frame during a bloom. Mobile / touch: no hover —
  the bloom fires on tap-focus (first tap gathers, second tap
  activates, on cards and rows only; links and buttons activate
  immediately and bloom briefly at the tap point instead, via
  §6.8's ripple at small radius).
- **Choreography timeline (v2).** Pointerenter/focus → t=0 flare
  begins (to 2.2× by 250 ms) → t=0–600 gather arrives, nearest
  first → t=900 flare settles to 1.7× → hold, breathing →
  leave/blur → brightness releases 250 ms → positions release by
  500 ms → rest.
- **State matrix (v2).** *Rest:* no bloom. *Hover:* flare +
  gather as above. *Focus:* identical to hover. *Active:*
  tighten + 2.4× for 120 ms. *Scrolled-past:* immediate release.
  *Disabled:* no bloom, print dimmed. *Touch:* tap behaviour as
  in the budget line above.
- **Breakpoints (v2).** ≥1200 px: radius 180 px, full gather.
  768–1199 px: radius 150 px. <768 px: radius 120 px, tap-fired
  only; gather ring follows the element's top edge (the column
  has no side water to gather from).
- **Edge cases & failure modes (v2).** *Element larger than the
  radius (a full-width table):* anchors multiply — one per 300 px
  of edge — so the bloom gathers along the edge nearest the
  pointer, not at a single point. *Pointer moving fast across a
  nav:* blooms retarget with the 40 ms stagger suppressed — a
  skimmed menu shows a travelling brightening, not six competing
  gathers. *Hover during a digit aggregation (§6.3):* the stage's
  reserved organisms are exempt — a hover near the stage blooms
  only from the unreserved school.
- **Accessibility spec (v2).** The bloom never carries state
  alone: every hoverable element's state is also printed (colour,
  underline, ring per §11), and the visible focus indicator is a
  2 px bone outline at 3 px offset — present with or without the
  canvas. Bloom brightness changes are not announced. Touch
  targets ≥44 px; the 180 px bloom radius is visual only and
  extends no target.
- **Tokens consumed (v2).** `--cyan`, `--gold`, `--bone`,
  `--ease-bloom`, `--ease-drift`, `--dur-bloom-gather` (600 ms),
  `--bloom-radius` (180 px), `--bloom-flare` (2.2).

### 6.8 Disturbance-ripple click

- **What & why.** Clicking anywhere on the water sends a ripple
  through the swarm: a wavefront of flaring light radiates from
  the click point at ~300 px/s, organisms flaring as the front
  passes and settling behind it. It belongs because touch is this
  medium's primary verb — a naturalist trails a hand and the
  plankton answer — and because click feedback in the ecosystem's
  physics confirms the page felt the touch, on the page itself,
  not in a button's colour alone.
- **Structure.** A ripple is an entry in the canvas's ripple list:
  origin (viewport coords), birth time, radius growing at
  300 px/s to a maximum of 520 px, front width 26 px. Organisms
  whose distance from the origin falls inside the front band get
  a brightness impulse to 2.6× decaying over 700 ms behind the
  front, plus a small outward velocity nudge (8 px/s) — the water
  is displaced, not just lit. Interactive elements keep their own
  click behaviour untouched; the ripple is a parallel canvas
  response to the same event (a delegated pointerdown listener on
  the document, canvas coordinates).
- **Motion spec.** Expansion 300 px/s linear (a wave, not an
  easing — its *decay* eases, `--ease-bloom`, 700 ms per
  organism). Front brightness peaks at 2.6× at the front's centre,
  falling to baseline at both edges of the 26 px band. Maximum 3
  concurrent ripples; a fourth click replaces the oldest. Ripples
  die at 520 px radius or at the viewport edge, whichever first.
  On buttons and links the ripple still fires — the activation is
  the element's, the ripple is the water's receipt for it.
- **States.** Idle → expanding → decayed (removed). Hover: none —
  ripples are click-born. Focus: keyboard activation (Enter/Space
  on a focused element) fires a ripple from the element's centre
  at half radius (260 px) — keyboard touch disturbs the water
  too, more gently. Scrolled-past: ripples are viewport events;
  scrolling does not carry them. Disabled elements: a click on a
  disabled control fires no ripple — still water over a dead
  control, consistent with §6.7's disabled ruling.
- **Content merge.** The ripple radiates through the actual swarm
  around the actual click point — clicking a species card lights
  the water that card floats in; clicking the form's submit
  (§6.14) sends the confirmation's first signal through the
  organisms before the ledger entry prints. Feedback is located
  where the act happened.
- **Failure fallback.** Watchdog: none of its own — a ripple is
  fire-and-forget on the shared loop; if the canvas has fallen
  back, clicks simply produce no ripple and every control's own
  feedback (§11) is unaffected. No JS: no ripples; controls work.
- **Reduced-motion variant.** No travelling front. A click
  brightens the organisms within 120 px of the point in place to
  1.6×, decaying over 500 ms — a local glow answering the touch,
  without propagation.
- **Performance budget & mobile variant.** Ripple evaluation is a
  distance check folded into §6.2's existing per-organism loop —
  no extra pass; ≤0.2 ms per frame with 3 ripples live. Mobile:
  radius cap 360 px, front speed 260 px/s, max 2 concurrent.
- **Choreography timeline (v2).** Pointerdown → t=0 front born at
  origin → front expands 300 px/s, organisms flare and settle in
  its wake (700 ms decay each) → t≈1,730 front reaches 520 px cap
  and dissolves → last wake settles by t≈2,430.
- **State matrix (v2).** *Rest:* no ripple. *Hover:* none.
  *Focus:* keyboard activation → half-radius ripple from element
  centre. *Active:* full ripple from pointer point.
  *Scrolled-past:* n/a. *Disabled:* no ripple from disabled
  controls. *Touch:* tap = pointerdown, identical.
- **Breakpoints (v2).** ≥1200 px: cap 520 px, 3 concurrent.
  768–1199 px: cap 440 px, 3 concurrent. <768 px: cap 360 px,
  2 concurrent, speed 260 px/s.
- **Edge cases & failure modes (v2).** *Click storms (a reader
  tapping repeatedly):* the 3-ripple cap with oldest-replacement
  keeps the water legible; beyond 6 clicks in 2 s, new ripples
  are suppressed for 1 s — the census does not reward panic.
  *Click during aggregation (§6.3):* reserved organisms flare
  with the front but do not leave their targets — the figure
  shivers with light, it does not break. *Click on the pinned
  stage:* the front passes through the formation as above.
- **Accessibility spec (v2).** The ripple is never the sole
  feedback for any action — every control's activation has its
  printed result (§11). It is `aria-hidden` canvas behaviour,
  unannounced. Brightness impulse 2.6× on individual dots stays
  under §10's flash ceiling (dots are ≤3 px; no large-area flash
  is possible from this element).
- **Tokens consumed (v2).** `--cyan`, `--gold`, `--ease-bloom`,
  `--ripple-speed` (300 px/s), `--ripple-max` (520 px),
  `--ripple-front` (26 px).

### 6.9 Volumetric image frames

- **What & why.** Photographs in the census — a bloom photographed
  from the boat, a jellyfish at the surface, the expedition's
  night deck — glow inside soft volumetric frames: a radial falloff
  of light around the image, tinted cyan or gold by the species
  pictured, the image scaling 0.96 → 1.0 as it centres, like a
  creature approaching the light. It belongs because in black water
  a photograph cannot sit in a rectangle with a border; it must
  *surface*. The frame is the water brightening around something
  rising into the lantern's range.
- **Structure.** A `<figure>` with a real `<img>` (complete `alt`,
  real dimensions, lazy-loaded below the fold) wrapped in a frame
  div carrying two glow layers: a `::before` radial-gradient
  (species tint at 22% centre → transparent at 70%) translating at
  0.97× parallax, and the image itself with a soft inner shadow
  vignette so its edges dissolve into the water rather than ending
  at a crop line. The caption prints beneath in bone-dim with the
  species name in Fraunces italic and the station number in the
  data voice — every photograph is a census record, captioned like
  one. `data-tint="cyan|gold"` on the figure selects the glow.
- **Motion spec.** Trigger: scroll scrub across the figure's
  passage through the viewport centre band. Scale 0.96 → 1.0 and
  glow opacity 0.35 → 1.0, both read from the lerped progress
  (§5) across the figure's central 60vh of travel; the glow leads
  the scale by 10% of the range — the water brightens before the
  creature arrives. As the figure exits upward, the treatment
  reverses symmetrically: it recedes into the dark it rose from.
  Hover: the glow brightens 15% and the local bloom (§6.7)
  gathers at the frame's edge. No Ken Burns, no pan — the creature
  approaches, it does not perform.
- **States.** Submerged (below centre band: scale 0.96, glow
  0.35) → surfacing → surfaced (centred: scale 1.0, glow 1.0) →
  receding. Focus: a figure is not focusable; its caption link, if
  any, blooms per §6.7. Scrolled-past: receded state, symmetric.
  Disabled: image failed to load → the frame holds the printed
  caption and a cyan-dim dot cluster in the image's place with the
  alt text printed as the caption's first line — a missing
  photograph is an empty frame on the record, never a broken icon.
- **Content merge.** The tint is the pictured species' own colour
  from the sheet (§6.17) — *Noctiluca* photographs glow gold,
  *Pyrocystis* cyan — and the caption's station number ties the
  image to the census's geography. The organisms of the swarm
  gather slightly toward a surfaced frame (a weak attraction
  well, strength 0.3, radius 240 px): the photographed bloom draws
  the living one.
- **Failure fallback.** Watchdog: the treatment is scrub-driven
  from the shared loop; if the loop dies, figures freeze at
  whatever scale they hold — so the shipped default is the
  *surfaced* state (scale 1.0, glow 0.85) and the loop only ever
  *dims and shrinks toward* submerged from that default as it
  computes position. A dead loop therefore leaves every image
  fully visible at near-full glow — the fallback is the design's
  resting face, not an error state. No JS: surfaced state, static.
- **Reduced-motion variant.** Surfaced state at all positions: no
  scale change, glow fixed at 0.85, no parallax on the glow layer.
  The photograph is simply there, lit — a specimen under a lamp.
- **Performance budget & mobile variant.** Glow layers are CSS
  gradients (compositor-only opacity/transform); the image itself
  is the only raster cost, budgeted in §14 (≤180 KB per image,
  responsive sizes, WebP/AVIF). Per-frame cost: two style updates
  per in-band figure, ≤0.1 ms. Mobile (<768 px): scale range
  narrows to 0.98 → 1.0, glow fixed 0.7 (parallax off), attraction
  well off.
- **Choreography timeline (v2).** Figure enters centre band →
  glow rises 0.35 → 1.0 leading → scale follows 0.96 → 1.0 →
  centred: full surface, swarm attraction on → exit: symmetric
  recession → figure leaves at submerged values.
- **State matrix (v2).** *Rest (centred):* surfaced. *Hover:*
  glow +15%, edge bloom. *Focus:* n/a (caption link per §6.7).
  *Active:* n/a. *Scrolled-past:* receded, symmetric with entry.
  *Disabled (image failed):* printed alt + dot cluster + caption.
  *Touch:* identical scrub; no hover brightening.
- **Breakpoints (v2).** ≥1200 px: full treatment, glow radius
  70% of frame width. 768–1199 px: scale 0.97 → 1.0, glow 0.5 →
  1.0. <768 px: scale 0.98 → 1.0, glow fixed 0.7, attraction off.
- **Edge cases & failure modes (v2).** *Two figures in one
  viewport:* §4's density rule forbids it (one per section); if a
  CMS build violates it, the second figure's glow caps at 0.5 —
  the water cannot hold two suns. *Very tall image (portrait
  specimen):* the centre band is computed on the image's middle
  third, so a tall frame surfaces progressively rather than
  waiting for its centre. *Gold-tinted image under the depth
  rail:* glow is clipped by the content column — light never
  bleeds over the instruments (§6.5).
- **Accessibility spec (v2).** Real `alt` on every image, written
  as a census caption ("Bioluminescent bloom of *Noctiluca
  scintillans* at the surface, Station 41, night 12"). The glow
  and scale are decorative (`aria-hidden` layers); the image is
  fully legible in its shipped state with no motion required.
  Caption contrast: bone-dim on midnight 9.45:1.
- **Tokens consumed (v2).** `--cyan`, `--gold`, `--bone-dim`,
  `--water-3`, `--ease-drift`, `--ease-settle`, `--loop-lerp`
  (0.08), `--frame-glow` (0.85).

### 6.10 Predator pass

- **What & why.** Rarely — on a randomised schedule of every
  45–70 s — a single red point crosses the deep margin, and the
  swarm near its path scatters in a clean cone before regrouping.
  It belongs because an ecosystem without stakes is an aquarium:
  the census includes its predator (3 passes logged on the sheet,
  §6.17), and for four seconds the page's light rearranges itself
  around fear. It is the theme's only red, its only danger, and
  its most remembered moment precisely because it is rationed.
- **Structure.** One special organism in the swarm's roster,
  flagged predator, rendered from the red sprite at 3 px, resident
  *offscreen* (parked beyond the right margin, invisible) until a
  pass is scheduled. The schedule is seeded per session
  (`sessionStorage` seed) so passes are deterministic per visit
  and auditable in testing: first pass no earlier than 40 s after
  load, subsequent intervals drawn from 45–70 s. During a pass the
  predator crosses the right margin lane at 90 px/s on a slight
  diagonal; swarm organisms within 140 px of its path receive a
  cone-shaped flee force (strength 3.0, cone axis along the
  predator's velocity, half-angle 40°) — the scatter opens ahead
  of it and closes behind.
- **Motion spec.** Pass duration ~4–6 s depending on viewport
  height. Scatter: organisms reach the cone's edge within 300 ms
  (`--ease-bloom` brightness to 1.8× as they flee — frightened
  plankton flash). Regroup: 2,500 ms `--ease-drift` after the
  predator exits; the school closes the wound slowly, not
  instantly — the water remembers. The predator itself never
  flares, never pulses: one steady red point. It never crosses
  the content column — its lane is the right margin and, below
  1200 px where no margin exists, the pass is postponed until the
  layout has one (§14 cut order removes it on small screens
  entirely).
- **States.** Parked (invisible, the overwhelming majority of the
  time) → crossing → gone. Hover/focus: none; the predator
  ignores the pointer, and the pointer's flee (§6.2) does not
  apply to it. During a digit aggregation (§6.3): a scheduled pass
  is postponed until dispersal + 5 s — the predator never breaks a
  forming figure; the census's ceremony outranks its danger.
  During the hero bloom (§6.1): postponed likewise. Scrolled-past:
  n/a — passes are time events in the current viewport's margin.
- **Content merge.** The pass is logged: the footer (§6.18) prints
  "predator passes logged this season: 3" from the sheet, and if a
  pass occurs during the visit, nothing on the page claims it was
  a fourth — the session's passes are the sheet's passes
  re-enacted, not new data. The scatter rearranges the swarm
  around real content edges, so the fear is legible against the
  print it briefly abandons.
- **Failure fallback.** Watchdog: if a pass has not completed
  within 8 s (tab throttled mid-crossing), the predator is parked
  instantly offscreen and the school regroups — no red point may
  ever be left standing on the page. No JS: no predator, and the
  printed log line in the footer carries its existence. Canvas
  fallback (dot-field): no passes.
- **Reduced-motion variant.** No passes, ever. The predator exists
  only as its printed log line — a reduced-motion reader's water
  is safe water, and the census says so in §12's voice rules.
- **Performance budget & mobile variant.** One extra organism and
  a cone check inside the existing simulation pass; ≤0.1 ms per
  frame during a pass, zero when parked. Mobile (<1200 px): cut —
  no margin lane exists, and a predator crossing the text column
  would violate its own law. This is §14's second cut.
- **Choreography timeline (v2).** Schedule fires (≥40 s after
  load, then every 45–70 s) → predator enters right margin →
  scatter cone opens 300 ms ahead of its path → crossing 4–6 s →
  exit → regroup over 2,500 ms → water at rest. Watchdog ceiling
  8 s per pass.
- **State matrix (v2).** *Rest:* parked, invisible. *Hover:* none.
  *Focus:* none. *Active:* n/a. *Scrolled-past:* n/a.
  *Disabled / no-JS:* printed log line only. *Touch:* passes
  occur identically (time-driven) at ≥1200 px; cut below.
- **Breakpoints (v2).** ≥1200 px: full passes in the right margin
  lane. 768–1199 px: cut (no lane). <768 px: cut.
- **Edge cases & failure modes (v2).** *Reader opens the page and
  leaves it in a background tab for an hour:* rAF is throttled,
  the schedule reads wall-clock — on return, at most one pass is
  owed (missed passes are forgiven, never queued). *Pass
  scheduled while the reader is in the form (§6.14):* passes are
  postponed while any form field holds focus — the census does
  not frighten a visitor mid-signature. *Two passes could
  overlap after a throttled tab wakes:* the scheduler is a single
  timer; overlap is structurally impossible.
- **Accessibility spec (v2).** The pass is `aria-hidden` canvas
  behaviour, never announced — a screen reader's census has no
  predator event, only the printed log. The single red point
  (3 px, steady, no flashing) is far below photosensitivity
  thresholds; §10's red census audits that exactly one red light
  exists and only during a pass.
- **Tokens consumed (v2).** `--predator`, `--cyan`, `--ease-bloom`,
  `--ease-drift`, `--predator-interval` (45–70 s),
  `--predator-lane` (right margin), `--dur-watchdog-pass`
  (8000 ms).

### 6.11 Lantern-line navigation

- **What & why.** The site's navigation is a line of lanterns
  hung at the surface: a slim top bar carrying the wordmark in
  Fraunces, the section links in the data voice, each link with a
  small unlit dot above it that blooms cyan when its section is
  the reader's current depth and flares gently on hover — and, at
  the bar's right edge on narrower screens, the depth readout
  (§6.5) that the margin rail cannot hold. It belongs because
  navigation in this world is surface equipment: the naturalist
  orients by the lanterns on the boat while the census happens
  below, and the lit dot tells you which water you are in without
  a word of chrome.
- **Structure.** A `<header>` with a real `<nav>`, `position:
  sticky; top: 0`, ground a vertical gradient from `--midnight`
  to transparent over 72 px so the bar dissolves into the water
  rather than ending at a rule. The current-section dot is a CSS
  element (not canvas) lit by a scrollspy reading the same section
  boundaries as the depth rail (§6.5) — one source of "where am
  I" for both instruments. Links are bone-dim, bone on hover and
  for the current section. The compact depth readout (<1200 px)
  is the §6.5 text node relocated, not duplicated — the DOM node
  moves via CSS order into the bar, its update path unchanged.
- **Motion spec.** Bar entrance: at load, after the hero bloom,
  the lanterns light in sequence — dots flare one by one,
  90 ms stagger, 300 ms `--ease-bloom` each, wordmark printed
  from the start. Scrollspy changes: the old dot dims over
  400 ms `--ease-drift`, the new dot flares to full cyan and
  settles at 0.85. On scroll the bar's gradient deepens (ground
  opacity to 92%) so print over moving water stays legible; on
  scroll-stop it relaxes over 600 ms. No hide-on-scroll — the
  lanterns stay lit; a census does not hide its boat.
- **States.** Rest: current dot lit at 0.85, others unlit
  (cyan-dim at 30%). Hover: dot flares to 1.4×, link to bone.
  Focus: dot flares as hover, plus the standard 2 px bone focus
  outline on the link. Active (current section): dot lit, link
  bone, `aria-current="location"`. Scrolled-past: the bar is
  sticky; its state is the current section's, always. Disabled:
  a nav item pointing to an unpublished section is printed
  bone-dim at 50% with no dot and no link — an unlit lantern for
  water not yet surveyed.
- **Content merge.** The dots are the strata and sections
  themselves — the nav's items are the census's geography (The
  Shallows, Species Ledger, Soundings, Report a Sighting), and
  the current dot agrees with the depth rail's ticks (§6.5) and
  the stratum the reader is sinking through, because all three
  read one boundary table.
- **Failure fallback.** Watchdog: the scrollspy is a scroll
  listener with an IntersectionObserver — if neither fires within
  1,000 ms of load, the first dot lights by default (the reader
  is at the surface; that is never wrong). No JS: all dots unlit,
  all links printed and working; current-section indication is
  lost, navigation is not. Canvas failure: irrelevant — the bar
  is DOM and CSS by design.
- **Reduced-motion variant.** Dots change state instantly (no
  flare, no stagger); the entrance sequence is a single printed
  bar. The gradient no longer breathes with scroll.
- **Performance budget & mobile variant.** Scrollspy via
  IntersectionObserver, zero per-frame cost; bar paint is
  compositor-only. Mobile (<768 px): the bar holds wordmark,
  depth readout and a menu button; links move into a full-width
  surface panel (a "lantern drawer") that opens over the water
  with the same dot language, 250 ms `--ease-drift`; the panel's
  ground is `--water-2` at 98% so the census behind it rests.
- **Choreography timeline (v2).** Load → wordmark printed →
  hero bloom completes → dots light in sequence (90 ms stagger)
  → first scroll: gradient deepens → section boundary crossed:
  old dot dims 400 ms as new dot flares → floor reached: last
  dot lit, readout 550 fm.
- **State matrix (v2).** *Rest:* current dot 0.85. *Hover:* dot
  1.4×, link bone. *Focus:* as hover + outline. *Active:*
  current section — dot lit, link bone, `aria-current`.
  *Scrolled-past:* n/a (sticky). *Disabled:* dotless dim item.
  *Touch:* dots light on scrollspy only; tap targets ≥44 px.
- **Breakpoints (v2).** ≥1200 px: full bar, dots + labels, depth
  readout stays in the margin rail. 768–1199 px: full bar, depth
  readout in the bar. <768 px: wordmark + readout + menu button;
  links in the lantern drawer.
- **Edge cases & failure modes (v2).** *Many sections (a
  12-section census):* dots stay one per link; below 9 px dot
  spacing the labels abbreviate to stratum names only — the
  drawer carries full names. *A section removed in a CMS:* the
  boundary table is built from the DOM's actual sections at
  load, so scrollspy, rail and dots can never disagree with the
  page that exists. *Sticky bar over the pinned stage (§6.3):*
  the stage's figure centres in the viewport below the bar's
  72 px — the stage's sticky math reserves the bar's height.
- **Accessibility spec (v2).** Landmark `<header>` + `<nav
  aria-label="Census">`; `aria-current` on the active link; dots
  are decorative (`aria-hidden`) — current-ness is in the link's
  semantics, not only in light. Skip link is the bar's first
  element, printed bone on `--water-3`, visible on focus. Link
  contrast: bone-dim 9.45:1 at rest, bone 14.99:1 lit.
- **Tokens consumed (v2).** `--midnight`, `--water-2`,
  `--water-3`, `--bone`, `--bone-dim`, `--cyan`, `--cyan-dim`,
  `--ease-bloom`, `--ease-drift`, `--dur-nav-stagger` (90 ms).

### 6.12 Species ledger cards

- **What & why.** The species index is a ledger of specimen
  cards, one per species on the sheet: name in Fraunces, binomial
  in italic, count printed in the data voice, depth range, and a
  small glow portrait — a radial field in the species' tint with
  its dot density proportional to its share of the census. On
  hover the card tilts like a specimen tray tilting in water
  (max 3°) and the swarm blooms at its edge (§6.7). It belongs
  because the ledger is the census's working document — the cards
  are records you can handle, and handling one disturbs its water
  exactly as lifting a tray disturbs a tank.
- **Structure.** A `<ul>` of `<li>` cards on `--water-2`, each
  card an `<article>` with a link to the species' detail page
  (§7). The glow portrait is a CSS radial-gradient field (species
  tint) with a printed dot pattern whose density is set by an
  inline custom property `--share` from the sheet (40.6% for
  *Noctiluca* down to 4.1% for the unclassified) — the portrait's
  crowdedness *is* the data, legible before a number is read.
  Tilt is a transform on the card driven by pointer position
  (rotateX/rotateY, max 3°, computed in the shared loop from
  lerped pointer values — never raw pointer events).
- **Motion spec.** Tilt: follows the pointer with the loop's
  lerp (0.08), so the tray feels suspended in water, not glued
  to the cursor; on leave it settles back over 600 ms
  `--ease-settle` with no overshoot past 0.3°. Glow portrait:
  brightness +18% on hover over 300 ms `--ease-bloom`. Cards
  print in on scroll with the section reveal (§5: 400 ms rise),
  staggered 70 ms per card in reading order — a ledger being
  opened page by page. The count on the card never animates; it
  is print.
- **States.** Rest: flat, portrait at rest brightness. Hover:
  tilt ≤3°, portrait +18%, edge bloom (§6.7). Focus: the card's
  link focus flares the portrait and blooms the edge; tilt does
  not follow keyboard focus (a tray does not tilt for a voice).
  Active (pressed): tilt flattens to 0° in 100 ms — the tray is
  set down firmly — then the link follows. Scrolled-past:
  printed, flat. Disabled: a species with no detail page renders
  as a card without a link, portrait dimmed 30%, labelled
  "record only" — the ledger admits which entries are stubs.
- **Content merge.** Every field on the card is a sheet field
  (§6.17): count, share (as portrait density), depth range,
  tint. The six cards' counts sum to the census total, and §10's
  gate re-adds them. The card is the sheet, handled one species
  at a time.
- **Failure fallback.** Watchdog: tilt and bloom are loop-driven;
  if the loop is dead the cards stand flat and printed with
  portraits at rest brightness — complete. No JS: identical,
  with CSS-only hover brightening. Images: cards use no `<img>`
  (portraits are gradients), so there is nothing to break.
- **Reduced-motion variant.** No tilt, no stagger — cards print
  in as a block with the section; hover brightens the portrait
  only. The tray stays level for every reader who asks.
- **Performance budget & mobile variant.** Tilt math is two
  lerped values per hovered card (only one card can be hovered);
  portraits are gradients, zero raster cost. Grid: 3 columns
  ≥1200 px, 2 at 768–1199 px, 1 below 768 px. Mobile: tilt off
  (no pointer), tap fires the edge bloom at the tap point
  (§6.7's touch ruling) and the portrait brightens on the first
  tap only if the card's link needs a second tap — links here
  navigate on first tap, so the bloom is a 300 ms farewell flash
  as the page transition (§6.15) begins.
- **Choreography timeline (v2).** Section enters → cards rise in
  70 ms stagger → rest → pointer enters a card → portrait flares
  300 ms, tilt lerps to pointer angle, edge bloom gathers
  600 ms (§6.7) → pointer leaves → bloom releases, tray settles
  600 ms `--ease-settle`.
- **State matrix (v2).** *Rest:* flat, portrait rest. *Hover:*
  tilt ≤3°, portrait +18%, bloom. *Focus:* portrait flare +
  bloom, no tilt. *Active:* flatten 100 ms, then navigate.
  *Scrolled-past:* flat print. *Disabled:* linkless, dimmed,
  "record only". *Touch:* no tilt; tap bloom + transition.
- **Breakpoints (v2).** ≥1200 px: 3-col grid, tilt on.
  768–1199 px: 2-col grid, tilt on (max 2.5°). <768 px: 1-col,
  tilt off, portrait height 96 px.
- **Edge cases & failure modes (v2).** *A census with 40
  species:* the ledger paginates (§11) rather than growing —
  cards per page 12, and the swarm's loans are unaffected.
  *A species renamed in the CMS:* card and sheet read the same
  record; the detail page's title is the card's name — one
  source. *Share below 2%:* portrait density floors at a visible
  minimum of 6 dots — a rare species is sparse, never invisible.
- **Accessibility spec (v2).** The whole card is one link with a
  single accessible name ("*Noctiluca scintillans* — 24,917
  counted — Shallows to Twilight Shelf"); the portrait is
  `aria-hidden` (its density is data, but the same data is
  printed as the count and share). Focus outline 2 px bone at
  3 px offset on the card. Text contrast: bone on water-2
  13.32:1; bone-dim captions 8.4:1 on water-2 (measured against
  the card ground).
- **Tokens consumed (v2).** `--water-2`, `--bone`, `--bone-dim`,
  `--cyan`, `--gold`, `--cyan-dim`, `--ease-bloom`,
  `--ease-settle`, `--tilt-max` (3deg), `--loop-lerp` (0.08).

### 6.13 The depth-sounding table

- **What & why.** For the reader who needs the census plain: a
  true data table of the soundings — one row per stratum, with
  its depth range, organism count, share of the census, dominant
  species and station count — printed in the data voice, totals
  row at the foot carrying the sheet's 61,408. It belongs because
  a census that cannot be read as a table is a light show; the
  table is the theme's honesty made structural, and §1's when-NOT
  clause sends hurried readers here. Its one piece of theatre:
  hovering a row gathers the swarm's bloom along the row's margin
  edge (§6.7), so even the table floats in the water it tabulates.
- **Structure.** A semantic `<table>` with `<caption>` ("Soundings
  by stratum — Census Sheet, §6.17" in build terms: "Soundings by
  stratum"), `<th scope="col">` headers, `<th scope="row">`
  stratum names, tabular numerals throughout. Rows sit on
  alternating `--midnight` / `--water-2` at 40% — a sounding
  line's striping, subtle enough that print contrast is computed
  against the darker ground. The totals row is separated by a
  gold-deep hairline and its figure is set in gold (§3: gold sets
  totals). Shares print to one decimal with the sheet's rounding
  note (§6.17): "shares are rounded; the counts govern."
- **Motion spec.** The table itself does not animate — no reveal
  beyond the section's print rise (§5). Row hover: background
  lifts to `--water-3` over 200 ms `--ease-drift` and the margin
  bloom gathers (§6.7). That is all. The restraint is the spec:
  the one element a hurried reader uses is the one element that
  never performs.
- **States.** Rest: printed, striped. Hover (row): lift + bloom.
  Focus: a row is not focusable; focusable cells (a stratum's
  detail link) bloom per §6.7. Active: n/a. Scrolled-past:
  printed. Disabled: if a stratum's data is provisional (a build
  mid-season), its row prints with counts in bone-dim and a
  "provisional" label — the table admits the state of its own
  evidence rather than hiding the row.
- **Content merge.** The table *is* the census sheet's stratum
  half (§6.17) presented in the reading flow — same numbers, same
  order, same totals — and its rows' depth ranges are the depth
  rail's ticks (§6.5) and the strata the reader has been sinking
  through. Table, rail and swarm are three readings of one record.
- **Failure fallback.** Watchdog: none required — the table is
  static HTML with a CSS hover; it cannot fail into invisibility.
  No JS: identical, minus the margin bloom. This element is the
  fallback's fallback: §10's canvas-failure drill ends here, with
  the census still fully readable.
- **Reduced-motion variant.** Identical, minus the row-hover
  transition (instant lift) and the bloom (print response only).
- **Performance budget & mobile variant.** Zero JS cost beyond
  §6.7's shared bloom. Mobile (<768 px): the table becomes a
  stacked sounding list — each stratum a block with its figures
  in definition-list layout, same order, same totals; no
  horizontal scroll is ever permitted (a sounding you must pan
  is a sounding lost). The transformation is CSS + semantic
  markup chosen at build, not a JS re-render.
- **Choreography timeline (v2).** Section print rise 400 ms →
  table at rest → row hover: lift 200 ms, bloom gathers 600 ms
  (§6.7) → leave: release 500 ms. Nothing else, ever.
- **State matrix (v2).** *Rest:* printed stripes. *Hover:* row
  lift + margin bloom. *Focus:* cell link bloom. *Active:* n/a.
  *Scrolled-past:* printed. *Disabled:* provisional rows dimmed
  and labelled. *Touch:* tap on a row lifts it for 600 ms (no
  bloom gather; §6.7's touch ruling).
- **Breakpoints (v2).** ≥1200 px: full 6-column table.
  768–1199 px: 5 columns (station count folds into the stratum
  cell as a sub-line). <768 px: stacked sounding list.
- **Edge cases & failure modes (v2).** *A stratum with zero
  counted (a dry season):* the row prints 0 and "none sighted" —
  a zero is data, and the table prints it in full bone, not
  dimmed: absence counted is not absence hidden. *Counts with 7+
  digits:* tabular numerals and right alignment hold; the totals
  row never wraps (white-space: nowrap on figure cells, measure
  permitting). *Print:* the table is the print stylesheet's
  centrepiece — full grid, no striping, midnight on bone.
- **Accessibility spec (v2).** Real table semantics with caption
  and scoped headers; the totals row is a `<tfoot>` with
  `scope="row"`. Screen readers get the census in its most
  native form. Contrast: bone on midnight 14.99:1, bone on the
  striped water-2 rows 13.32:1, gold totals on midnight 11.20:1.
  The margin bloom is `aria-hidden` decoration on a table that
  needs nothing from it.
- **Tokens consumed (v2).** `--midnight`, `--water-2`,
  `--water-3`, `--bone`, `--bone-dim`, `--gold`, `--gold-deep`,
  `--ease-drift`.

### 6.14 Report-a-sighting form

- **What & why.** The census's conversion: a visitor who has seen
  a bloom — on a night beach, from a pier — files a sighting
  report, and the report becomes a record in the census. The form
  is styled as a ledger page on `--water-2`: fields for the
  reporter's name, the place, the species (a select of the
  sheet's six entries plus "unclassified light"), an estimated
  count, and the night of the sighting. On submit, the
  confirmation is a ledger entry — "Entered as record № 413" —
  and one gold organism detaches from the swarm, blooms at the
  form's edge, and swims off into the margin to join the school:
  your sighting, entering the census, performed by the census. It
  belongs because it is the only element where the visitor adds a
  light to the water, and the theme's law (§1) is honoured: the
  new light is counted — it has a record number, derived from the
  sheet.
- **Structure.** A real `<form>` with native validation semantics
  enhanced, never replaced: labelled inputs on `--water-3`,
  bone text, 2 px focus outline in bone plus the field's edge
  bloom (§6.7). The preamble prints the sheet's line: "412
  reports on file. Yours will be № 413." — the derivation is
  shown before the visitor writes a word, so the confirmation
  number is a kept promise, not a surprise. On submit (JS
  intercepts, posts, and on success swaps the form region for
  the confirmation ledger entry); without JS the form posts to
  its endpoint and the confirmation is a server-rendered page
  with the same entry and the next number.
- **Motion spec.** Field focus: edge bloom gathers 600 ms
  (§6.7); the field's ground lifts water-3 → a 6% cyan tint over
  250 ms. Submit: the button's ripple (§6.8) fires; the form
  dims to 60% over 300 ms while the entry is written (a
  "recording" state with the unlit-cluster pulse on the button,
  §6.15 — never a spinner). Success: confirmation entry prints
  in with a 500 ms rise `--ease-drift`; at t=300 the gold
  organism detaches from the nearest schooling group, blooms to
  2.2× at the entry's edge, and swims a curved path into the
  right margin over 1,800 ms `--ease-surge`, joining the school.
  Error: the offending field's marker draws in gold-deep
  (an asterisk-star, the ledger's correction mark) and its error
  line prints beneath in bone — no shake, no red, ever (§2).
- **States.** Rest: printed ledger, preamble showing № 413.
  Focus: per-field bloom + lift. Active (submitting): form at
  60%, button pulsing unlit clusters, fields disabled.
  Success: confirmation entry + the departing organism.
  Error: field marked, error line printed, focus moved to the
  first error, values preserved. Scrolled-past: the form waits;
  an in-flight submission completes regardless of scroll.
  Disabled (endpoint down): the form prints a ledger note —
  "The ledger is closed tonight; reports resume at dusk" — and
  holds the visitor's entries in the fields, unsubmitted, unsent,
  unlost.
- **Content merge.** The form's species select *is* the sheet's
  species list; its preamble number is the sheet's report count;
  its confirmation number is that count + 1; and the organism
  that departs is gold because the honoured action (§2) is gold.
  The conversion is not decorated with the theme — it is
  transacted inside it.
- **Failure fallback.** Watchdog at 4,000 ms on submission: if no
  response, the form restores from its 60% state and prints the
  ledger note "the entry could not be written — your words are
  still here" with values intact; nothing is silently lost and
  nothing is double-submitted (the submit token is idempotent
  per form instance). No JS: native post, server confirmation,
  as above. Canvas absent: the confirmation prints without the
  departing organism — the number is the record; the swim is its
  portrait.
- **Reduced-motion variant.** Confirmation prints instantly; no
  organism swims — a gold dot appears at the entry's edge at rest
  brightness, printed as part of the entry's seal. Errors print
  without transition.
- **Performance budget & mobile variant.** The form's JS is the
  page's only non-canvas script beyond the loop: ≤6 KB gz,
  deferred. The departing organism is one steering target in the
  existing simulation — zero extra per-frame cost after its
  1,800 ms swim. Mobile (<768 px): single column, fields full
  measure, the organism swims to the *top* margin (the column has
  no right margin) and the confirmation's seal dot sits at the
  entry's head.
- **Choreography timeline (v2).** Focus field → bloom 600 ms →
  submit → ripple fires, form dims 300 ms → recording pulse →
  response → entry rises 500 ms → t=300 organism blooms at edge
  → swims 1,800 ms `--ease-surge` → joins school → confirmation
  at rest. Watchdog ceiling 4,000 ms on the submission.
- **State matrix (v2).** *Rest:* ledger printed, № 413 promised.
  *Hover:* field edge blooms (§6.7). *Focus:* bloom + ground
  lift + outline. *Active:* submitting state as above.
  *Scrolled-past:* waits; submission completes. *Disabled:*
  ledger-closed note, values held. *Touch:* identical; targets
  ≥48 px on fields, submit full-width.
- **Breakpoints (v2).** ≥1200 px: two-column ledger (place +
  night side by side), form measure 44rem. 768–1199 px:
  single column, measure 38rem. <768 px: single column full
  measure, submit sticky at the form's foot within the form's
  own box.
- **Edge cases & failure modes (v2).** *Estimated count of 0 or
  absurd (a joker files 10⁹):* the ledger voice corrects without
  scolding — "a bloom of one is still a bloom; enter what you
  saw" — and values above the sheet's total are accepted but
  flagged "unverified estimate" in the entry: the census records
  claims as claims. *Duplicate report (same night, place,
  species):* the entry prints with a marginal note, "second
  report of this bloom — corroboration, not duplication": the
  ledger treats agreement as evidence. *Species "unclassified":*
  the departing organism is cyan-dim, not gold — the swim
  honours the classification honestly.
- **Accessibility spec (v2).** Native labels on every field
  (visible, bone, 14.99:1); errors use `aria-describedby` and an
  `aria-live="polite"` summary that reads the ledger's own
  words; the confirmation entry is an `aria-live` region
  announcing "Entered as record № 413" once. Focus management:
  on error, focus to the first invalid field; on success, focus
  to the confirmation heading. The departing organism is
  `aria-hidden`. Error markers are never colour-alone: the
  gold-deep mark is paired with the printed word "correct this".
- **Tokens consumed (v2).** `--water-2`, `--water-3`, `--bone`,
  `--bone-dim`, `--cyan`, `--gold`, `--gold-deep`,
  `--ease-bloom`, `--ease-drift`, `--ease-surge`,
  `--dur-watchdog-form` (4000 ms).

### 6.15 Unlit clusters — loader & page transition

- **What & why.** Loading in this census is unlit water: content
  regions that are still arriving show dim clusters of unlit
  organisms — cyan-dim dots at 18% brightness, printed in the
  shape of the coming content (a figure's block, a card's field) —
  and as each region's data lands, its cluster flares to full
  light and the content prints in. The page transition uses the
  same physics at full scale: leaving a page, the swarm disperses
  into darkness over 600 ms; arriving, it re-blooms around the new
  headline (§6.1's ceremony, shortened). It belongs because a
  spinner would be a machine in the water; unlit organisms are
  the census in its dormant state — the same population, not yet
  shining — and because the original entry specifies exactly this
  loading language.
- **Structure.** Skeleton regions are DOM elements with a
  `data-unlit` attribute, styled with layered radial-gradient dot
  fields (cyan-dim) shaped by the region's own box — no grey
  boxes: an unlit figure region is a wide dim cluster, an unlit
  card is a card-shaped one. The flare is a class swap
  (`.is-lit`) animating the dot field's opacity/brightness while
  the real content, already in the DOM or injected complete,
  prints in beneath it. The transition is a mode of the shared
  canvas: dispersal raises every organism's separation weight and
  fades global brightness to 0 over 600 ms `--ease-sink`; arrival
  runs §6.1's ripple at 60% duration from the new headline.
- **Motion spec.** Unlit pulse: skeleton clusters breathe at
  12% ±4% on a 2.8 s sine — barely alive, clearly dormant; the
  pulse is opacity only, no movement. Flare on data: 450 ms
  `--ease-bloom` to full brightness, content print rising
  simultaneously (300 ms), cluster field fading out over the
  same 450 ms — light hands over to print. Hard ceiling: any
  region still unlit at 1,500 ms prints its content anyway, lit
  or not — the census does not hold a reader hostage to a slow
  jar. Transition: dispersal 600 ms, navigation, arrival bloom
  ≤1,400 ms; total perceived interruption ≤2,000 ms, watchdogged.
- **States.** Unlit (dormant pulse) → flaring → lit/printed
  (rest). Error (a region's data fails): the cluster dims to 8%
  and the region prints its ledger note ("this jar did not reach
  the boat — [retry]") in bone with a real retry control; the
  skeleton never spins forever. Focus: a skeleton region is not
  focusable and is `aria-hidden` until printed. Scrolled-past:
  regions below the fold flare on arrival regardless of
  visibility — by the time the reader sinks to them, they are
  print. Disabled: JS off → no skeletons exist; content is
  server-printed complete.
- **Content merge.** The skeleton is shaped like the content it
  precedes and made of the content's own organisms' unlit state;
  the transition's dispersal is the same swarm the reader has
  been swimming with, leaving — continuity of population across
  pages is the theme's answer to the page boundary: it is one
  body of water, sounded page by page.
- **Failure fallback.** Watchdog per region at 1,500 ms (print
  regardless) and on the transition at 2,000 ms (the destination
  page forces its lit state — a transition may never strand a
  reader in dark water between pages). No JS: no loader, no
  transition; plain navigation, complete pages.
- **Reduced-motion variant.** No pulse, no dispersal: skeletons
  are static dim fields that swap to print instantly on data;
  transitions are plain navigations with the destination's hero
  in its lit state.
- **Performance budget & mobile variant.** Skeleton fields are
  CSS gradients — zero raster, zero JS per frame. The transition
  reuses the simulation; its cost is §6.2's. Mobile (<768 px):
  dispersal shortens to 400 ms and the arrival bloom is the
  hero's mobile variant (§6.1); skeleton pulse is cut (static
  dim fields) to save battery.
- **Choreography timeline (v2).** Region requested → unlit field
  prints with the layout → data lands → flare 450 ms, print
  rises 300 ms → region at rest. Ceiling 1,500 ms forces print.
  Transition: click → dispersal 600 ms → navigate → arrival
  bloom ≤1,400 ms → lit page. Watchdog ceiling 2,000 ms.
- **State matrix (v2).** *Rest:* printed content. *Hover:* n/a.
  *Focus:* skeletons unfocusable, `aria-hidden`. *Active:*
  submitting regions show the unlit pulse (§6.14). *Scrolled-past:*
  pre-flared print. *Disabled / no-JS:* server print, no
  skeletons. *Touch:* identical.
- **Breakpoints (v2).** ≥1200 px: full treatment. 768–1199 px:
  full, pulse period 3.2 s. <768 px: static skeletons, 400 ms
  dispersal.
- **Edge cases & failure modes (v2).** *Data arrives before the
  skeleton paints (fast cache):* the region prints directly —
  a skeleton that never appears is the best kind. *Partial
  failure (3 of 6 cards land):* landed cards print; unlanded
  regions hold unlit until their own retry or the ceiling,
  then print their ledger notes individually — the ledger
  opens with gaps admitted, not with the page held shut.
  *Reader navigates mid-transition:* the watchdog belongs to
  the destination page, so a double navigation still lands lit.
- **Accessibility spec (v2).** Skeleton regions carry
  `aria-busy="true"` on their container and are removed from
  the accessibility tree until printed; a single polite
  announcement ("Census loaded") fires when the last
  above-fold region prints — not one per region. The
  transition is never announced. Contrast of the ledger error
  note: bone on midnight 14.99:1.
- **Tokens consumed (v2).** `--cyan-dim`, `--bone`, `--midnight`,
  `--water-2`, `--ease-bloom`, `--ease-sink`,
  `--dur-unlit-ceiling` (1500 ms), `--dur-disperse` (600 ms),
  `--dur-watchdog-transition` (2000 ms).

### 6.16 Unlit water — empty state & 404

- **What & why.** Where the census finds nothing — a search with
  no species, a filter with no stations, a page that does not
  exist — the water is unlit: a region the swarm will not enter,
  printed with the ledger's plain statement of absence and one
  small static cluster of cyan-dim dots, unlit, at its centre.
  It belongs because absence is a census result: a night with no
  bloom is recorded, not errored. The 404 is the full-page form —
  "this water is not on the chart" — with the way back to the
  surface printed as real links. The emptiness is designed, not
  defaulted: organisms actively avoid the region, so the visitor
  *sees* the nothing the text reports.
- **Structure.** The empty region registers as a repel zone in
  the swarm's obstacle list (§6.2) with a stronger force (2.0)
  and no parting bow-wave — organisms curve away early, leaving
  a visibly empty ellipse of water. At its centre, a static
  printed dot cluster (CSS, cyan-dim at 18%) — the unlit cluster
  of §6.15, here permanent: these organisms are not coming. The
  print block carries the heading in Fraunces, the statement in
  body text, and the exits (back to surface / open the ledger /
  file a sighting, §6.14 — an uncharted bloom is a plausible
  reason to be lost).
- **Motion spec.** Almost none, by design: the repel field is
  steady; the centre cluster does not pulse (§6.15's pulse
  would imply something is coming). One licensed motion: on
  arrival at the 404, the swarm's general brightness dips 15%
  for the first 2 s — the water itself is quieter here — then
  restores. The empty state's choreography is specified as
  *absence*, and §10's gate checks that no animation has crept
  in.
- **States.** Rest: unlit, still, printed. Hover: the exit
  links bloom per §6.7 — the only light the region permits is
  at its doors. Focus: same. Active: n/a. Scrolled-past: the
  repel zone deregisters when the region leaves the viewport;
  the water refills behind the reader. Disabled / no-JS: the
  print and exits stand; the repel zone and dip simply do not
  occur — the statement of absence remains complete.
- **Content merge.** The emptiness is *caused* by the content's
  state (no results, no page) and enacted by the ecosystem's
  avoidance — the swarm's behaviour and the ledger's statement
  are the same fact in the theme's two media. The 404's exits
  are the census's real doors, including the sighting form: a
  visitor who arrived looking for an unlisted bloom is routed
  to the one page that can list it.
- **Failure fallback.** Watchdog: none needed — the element is
  print plus a steering force; if the canvas has fallen back,
  the static cluster and print remain and the absence is still
  stated. No JS: identical print.
- **Reduced-motion variant.** Identical, minus the arrival dip.
  This is the one element whose reduced variant is nearly the
  element itself — stillness was already its language.
- **Performance budget & mobile variant.** The repel zone is one
  entry in the existing obstacle pass; ≤0.05 ms per frame.
  Mobile (<768 px): the ellipse becomes a full-width band of
  unlit water above the print block (the column has no sides to
  empty); the centre cluster centres over the band.
- **Choreography timeline (v2).** Region enters → repel field
  active, water empties over ~800 ms as organisms curve away →
  (404 only) brightness dip 15% for 2 s → rest: still, unlit,
  printed. Exit: field deregisters, water refills 600 ms.
- **State matrix (v2).** *Rest:* unlit stillness. *Hover:*
  exit-link blooms only. *Focus:* same. *Active:* n/a.
  *Scrolled-past:* field deregistered, water refilled.
  *Disabled / no-JS:* print + static cluster. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200 px: elliptical repel field in the
  column's water. 768–1199 px: field narrows with the column.
  <768 px: unlit band treatment, as above.
- **Edge cases & failure modes (v2).** *Empty state inside a
  small component (a filtered card grid):* the repel field
  scales to the component and the centre cluster shrinks to 7
  dots — absence at tray scale. *A search that returns results
  after showing empty (debounced re-query):* the field
  deregisters and the results print with §6.15's flare — the
  water lights because the census found something; the
  transition between the two states is itself reported by the
  print ("3 species match"). *The 404 reached from a deep
  link mid-census:* the depth readout (§6.5) prints "uncharted"
  in place of a fathom count — the one place the instrument
  admits it has no sounding.
- **Accessibility spec (v2).** The statement of absence is the
  first printed content of the region, a real heading; search
  empties are announced via `aria-live="polite"` ("No species
  match that name"). The repel field and cluster are
  `aria-hidden`. Exit links are ordinary links at full contrast
  (bone 14.99:1) with §11's standard focus treatment.
- **Tokens consumed (v2).** `--midnight`, `--cyan-dim`,
  `--bone`, `--bone-dim`, `--ease-drift`, `--repel-force`
  (2.0).

### 6.17 The census sheet — the declared record

- **What & why.** Near the foot of the page, before the floor,
  the census prints its sheet: the single declared record from
  which every light, figure and percentage on the page derives —
  the total, the effort (nights, stations, samples), the strata
  table, the species table, the predator log and the report
  count. It belongs because the theme's law (§1: nothing glows
  that is not counted) needs an auditable home: a visitor — or a
  builder, or §10's gate — can stand at the sheet and re-derive
  every number the blooms performed. The sheet is not a summary
  of the page; the page is a performance of the sheet.
- **Structure.** A section on `--water-2` styled as the ledger's
  master page: two tables (strata, species) in §6.13's table
  language, a definition list for the effort figures and the
  logs, and the rounding note printed as a marginal line:
  "Shares are rounded to one decimal and may sum to 100.1; the
  counts govern." Species tints are printed as a 10 px dot
  beside each row — the sheet is the one place tint is assigned,
  and §6.2's swarm proportions are computed from this table at
  build: of 160 organisms — *Noctiluca* 65, *Pyrocystis* 34,
  *Lingulodinium* 26, *Ceratium* 17, *Pyrodinium* 12,
  unclassified 6 — the sheet's shares × 160, each rounded to the
  nearest organism, the unclassified taking the remainder so the
  school sums to exactly 160. The allocation is printed here,
  on the sheet, because the school is a derived figure like any
  other and is audited like one (§10).
- **Motion spec.** None of its own. The sheet is print; it
  receives the section print rise (§5) and nothing else. The
  swarm above it schools at slightly lower brightness (the
  reader is meant to read, and the water calms over the record —
  a 20% dim within the sheet's viewport passage, driven by the
  loop, the only concession).
- **States.** Rest: printed. Hover: table rows lift per §6.13.
  Focus: links (method note, data download) bloom per §6.7.
  Active: n/a. Scrolled-past: printed. Disabled: n/a — the
  sheet has no JS-dependent state; it is the element every
  fallback falls back *to*.
- **Content merge.** Total identity: the hero's counted total
  (§6.4) is the sheet's total; the stages' figures (§6.3) are
  its strata rows; the cards (§6.12) are its species rows; the
  form's preamble (§6.14) is its report count; the footer's log
  (§6.18) is its predator line. §10's figure-truth audit is a
  mechanical comparison of the page against this section.
- **Failure fallback.** Watchdog: not applicable — static print.
  If every other system on the page fails, the sheet remains,
  and the census is still published. That is its job.
- **Reduced-motion variant.** Identical. The sheet was always
  still.
- **Performance budget & mobile variant.** Two tables and a
  definition list; zero script. Mobile (<768 px): both tables
  take §6.13's stacked sounding-list form; the definition list
  stacks; the rounding note prints in full — small screens get
  the whole record, never an abridgement.
- **Choreography timeline (v2).** Section print rise 400 ms →
  swarm dims 20% across the sheet's passage → print, read,
  audited → brightness restores over 600 ms after exit. Nothing
  else, by law.
- **State matrix (v2).** *Rest:* printed. *Hover:* row lift.
  *Focus:* link blooms. *Active:* n/a. *Scrolled-past:*
  printed. *Disabled / no-JS:* printed — its native state.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200 px: two tables side by side in
  the ledger spread. 768–1199 px: tables stacked, full width.
  <768 px: stacked sounding lists.
- **Edge cases & failure modes (v2).** *A build whose census
  updates mid-season:* the sheet is versioned in print ("Sheet
  3 of the season — supersedes Sheet 2, 14 March") and every
  derived figure on the page must be regenerated from the new
  sheet in the same deploy — §10's audit fails a page whose
  hero total and sheet total differ by even one organism.
  *Rounding:* shares may sum to 100.1; the note says so; the
  counts govern. *A species struck from the sheet:* its card,
  its swarm tint proportion and its form option (§6.14) all
  derive from the sheet, so one edit propagates everywhere —
  by design, there is no second place to forget.
- **Accessibility spec (v2).** Full table semantics as §6.13;
  the definition list uses real `<dl>` structure. The sheet is
  the page's most accessible element by intent: a screen-reader
  user who reads only this section has the entire census.
  Contrast: bone on water-2 13.32:1 throughout.
- **Tokens consumed (v2).** `--water-2`, `--bone`, `--bone-dim`,
  `--gold`, `--gold-deep`, `--cyan`, `--cyan-dim`,
  `--ease-drift`.

### 6.18 The deep-floor footer

- **What & why.** The page ends at the sea floor, 550 fm down:
  the footer is a band of `--midnight-deep` where the depth
  readout (§6.5) comes to rest at its maximum, the census totals
  print for the third and final time, the predator log line
  stands ("predator passes logged this season: 3"), and the
  swarm — its last behaviour — settles: as the footer enters,
  organisms sink toward the bottom edge, slow, and dim to 40%,
  coming to rest along the floor like a population settling for
  the day. It belongs because a descent must land. The footer is
  not the page's small print; it is the bottom of the water,
  where the census is filed.
- **Structure.** A `<footer>` on `--midnight-deep`: three
  columns at desktop (the census colophon — who counted, where,
  the sheet's version; the totals block — total, nights,
  stations, samples, predator log, in the data voice; the
  surface links — back to top, the ledger, report a sighting),
  and a floor line: a hairline of cyan-dim with the settled
  organisms' glow field behind it (a CSS gradient in the shipped
  state; the canvas settling is the enhancement). "Surface ↑"
  link returns with the depth line rewinding (§6.5).
- **Motion spec.** Settling: as the footer's top crosses the
  viewport's lower third, the loop raises the swarm's floor
  bias — a gentle downward attractor along the bottom 12% of
  the viewport, strength ramping 0 → 0.9 over the footer's
  60vh of entry, max speed falling to 18 px/s, brightness
  lerping to 40% (`--ease-settle` character). At rest the
  school hangs almost still above the floor line, breathing
  only. Scrolling back up releases the bias symmetrically — the
  population rises again. The current pulse (§6.6) exits into
  the footer's glow field and re-enters at the surface, closing
  its loop here.
- **States.** Rest (footer in view): swarm settled, totals
  printed. Hover: footer links bloom per §6.7 — the settled
  organisms near a hovered link brighten to 1.3× but do not
  rise; even attention does not fully wake the floor. Focus:
  same. Active: n/a. Scrolled-past: the footer is the end;
  scrolling up releases the settling as above. Disabled /
  no-JS: the printed footer with its static glow field —
  complete.
- **Content merge.** The totals block is the sheet's third
  printing (§6.17), agreeing to the organism; the predator log
  line is the sheet's; the depth readout's rest at 550 fm is
  the sheet's deepest boundary. The settling swarm is the
  population the whole page counted, coming to rest over its
  own record — the census ends with the counted asleep above
  their tally.
- **Failure fallback.** Watchdog: the settling is a bias in the
  shared simulation; if the loop or canvas has failed, the
  footer's shipped CSS glow field stands and the print is
  complete. No JS: identical print, static glow.
- **Reduced-motion variant.** No settling behaviour: the
  dot-field stands in the margins as elsewhere, the footer's
  glow field is static at 40%, print identical.
- **Performance budget & mobile variant.** The floor bias is
  one attractor term in the existing simulation; ≤0.1 ms per
  frame. Mobile (<768 px): columns stack (totals first — the
  record before the colophon), settling range narrows to the
  bottom 8%, brightness floor 50% (small screens keep their
  light a little longer).
- **Choreography timeline (v2).** Footer enters lower third →
  floor bias ramps over 60vh of travel → speeds fall to
  18 px/s, brightness to 40% → school at rest above the floor
  line → current pulse exits into the glow → reader scrolls up:
  bias releases symmetrically, school rises.
- **State matrix (v2).** *Rest:* settled swarm, printed totals.
  *Hover:* link bloom at 1.3×, no rising. *Focus:* same.
  *Active:* n/a. *Scrolled-past:* (scrolling up) bias released.
  *Disabled / no-JS:* print + static glow. *Touch:* identical.
- **Breakpoints (v2).** ≥1200 px: three columns, full settling.
  768–1199 px: two columns (totals + links), colophon below.
  <768 px: stacked, totals first.
- **Edge cases & failure modes (v2).** *A short page (a single
  species detail, §7):* the footer arrives quickly; the bias
  ramps over the available travel and the school settles less
  deeply (brightness floor scales to 55%) — a shallow dive
  settles shallow. *Reader parks at the floor:* the school
  hangs indefinitely at breathing ±6% — rest is a state, not a
  timeout. *Back-to-top via the surface link:* the depth line
  rewinds (§6.5) and the school rises through its strata in
  reverse — the ascent is the descent's mirror, never a jump
  cut, unless reduced motion makes it one.
- **Accessibility spec (v2).** `<footer>` landmark; the totals
  block is a definition list; the predator log is plain text.
  The settling is `aria-hidden`. Contrast on midnight-deep is
  the palette's best: bone 15.97:1 — the floor is where the
  smallest print lives, and it is the most legible ground on
  the page, deliberately.
- **Tokens consumed (v2).** `--midnight-deep`, `--bone`,
  `--bone-dim`, `--cyan-dim`, `--gold`, `--ease-settle`,
  `--ease-surge`, `--depth-max` (550 fm), `--loop-lerp`
  (0.08).

## 7. Page application map

- **Home (the census itself).** The full descent as choreographed
  in §13: hero bloom (§6.1), counting total (§6.4), the three
  strata with their pinned figures (§6.3), the species ledger
  (§6.12), sounding table (§6.13), volumetric frames (§6.9), the
  sighting form (§6.14), the sheet (§6.17), the floor (§6.18).
  Every element appears; the home page is the theme's reference
  build.
- **Species index (listing).** The ledger (§6.12) at full size —
  12 cards per page with pagination (§11) — over a shallower
  descent: depth ceiling for the page is printed as its own
  sounding (the index is surface work; the depth line's maximum
  is the page's, computed from its length against the 550 fm
  scale, so a short page reads shallow honestly). No pinned
  stages; the index's key figure (the total) prints without
  aggregation — listings are for finding, not ceremony.
- **Species detail.** One species, sounded deep: a hero with the
  species' own count aggregated once (§6.3, the page's single
  stage), its glow portrait enlarged as a volumetric frame
  (§6.9) with the species' tint, its rows from the sheet, its
  depth range drawn as a band on the depth rail (the rail gains
  a gold or cyan range marker showing where this species lives).
  The form (§6.14) appears pre-set to this species.
- **Expedition / about.** The naturalists' page: prose-led, the
  swarm calmer (cohesion +20%, speeds −20% — older water),
  volumetric frames of the boat and the night deck, the effort
  figures (nights, stations, samples) as inline figures without
  stages. The census sheet (§6.17) appears in its method form:
  how the counting is done, in the ledger voice.
- **Report / contact.** The form (§6.14) is the page; the descent
  is short (one stratum), the water bright, the preamble's №
  prominent. Contact details print as a ledger block — no map:
  a map would be another theme's furniture; the census gives
  coordinates in the data voice (lat/long as figures, which is
  how a naturalist is found).
- **Checkout / commerce.** Refused. A census does not sell from
  the water; a build with a shop keeps the shop in a plainer
  theme and links out from the surface nav. (A donation page for
  the institute is permitted in the form's clothing — §6.14 with
  amounts as figures — because a donation is a report of support,
  transacted in the ledger.)
- **404 / empty.** §6.16, full-page form.

## 8. Worked examples

### 8.1 The hero — "The Census at Midnight" (home, top)

The visitor arrives at midnight. The print is already there — a
real `<h1>`, "The Census at Midnight", in Fraunces at the Display
1 size, bone on midnight, with its standfirst ("Sixty-one thousand
four hundred and eight organisms, counted by hand over thirty-eight
nights — and every one of them shining.") and the printed total
beneath — but the water is dark and the eye goes to the light.
t=0 (fonts ready): the ripple leaves the centre at 420 px/s. As
the ring crosses the headline's glyphs, the sampled targets ignite
— the title is suddenly written twice, once in ink and once in
animals. The ring reaches the margins; the school, disturbed,
brightens in its wake and settles. At t=900 the standfirst rises
its 12 px. Then the count begins (§6.4): below the headline the
light-figure forms "≈ 2,300", dissolves, reforms — 26 beats, each
value the true count's eased fraction, the digits made of the same
organisms that wrote the title — and at t=2,340 it forms 61,408
and holds, breathing, while beneath it the printed twin has said
61,408 all along. The visitor scrolls: the headline cluster lets
go, organism by organism, back into the school; the depth readout
leaves 0 fm; the Shallows header rises. Total elapsed ceremony:
under 4 seconds, none of it blocking a word of print. A returning
visitor sees none of it — the hero stands lit, the total settled,
the water schooling: the census remembers being visited.

### 8.2 Mid-page — the Twilight Shelf stage and its soundings

Halfway down, the water has darkened 40% toward the floor's black.
The stratum band prints: "The Twilight Shelf — 30 to 110 fathoms"
and the section's prose — what lives here, why it glows deeper.
Then the stage: 220vh of water with nothing in it but the figure.
As it pins, the school thins — 140 organisms peel away and stream
toward the centre, arriving nearest-first, and the number 19,876
assembles itself out of *Lingulodinium* and *Pyrocystis* light,
cyan with its gold minority glinting inside the digits. It holds
for 1.2 s — long enough to read a number and understand what it is
made of — while beneath it, printed all along, the same figure
stands in bone with its caption. The reader scrolls on; the digits
dissolve back into the school behind them. Immediately below, the
mood changes on purpose: the sounding table (§6.13), strip-plain,
every stratum's figures in a row, the gold total at its foot. The
ceremony and the audit sit one screen apart, and the page trusts
the reader with both. A keyboard reader meets the same figure as
instant print with the formation formed at once; a reduced-motion
reader meets the print and the still halo; a reader on a dead
canvas meets the print alone — and all four have read the same
number, which is the point of the census.

### 8.3 Conversion — filing a sighting (record № 413)

Below the Midnight Shelf, in the darkest water, the ledger page
rises on `--water-2`: "Report a sighting." The preamble keeps the
sheet's promise in print: "412 reports on file. Yours will be
№ 413." A visitor who watched a beach ignite last Tuesday fills
the fields — name, place ("Marina Beach, north end"), species
(they choose "unclassified light", honestly unsure), estimate
(300), night (Tuesday's date). Each focused field gathers its
small bloom at its edge; the water attends to the writing. They
submit: a ripple leaves the button, the ledger dims to 60%, the
button pulses with unlit clusters — no spinner turns in this
water. The entry returns: a ledger block, printed in the form's
place — "Entered as record № 413 — unclassified light, Marina
Beach, night of Tuesday — estimate 300, unverified." And at the
entry's edge one cyan-dim organism brightens, because an
unclassified sighting swims in the unclassified tint (§6.14's
ruling), and curves away into the margin over 1.8 s to join the
school — one more light in the census, numbered, admitted as an
estimate, and shining. The visitor scrolls to the sheet (§6.17)
and finds the report count now reads 413 in their session's
printing — the census they leave is one light larger than the
one they found.

## 9. Anti-slop — what makes THIS theme look cheap

1. **Wallpaper swarm.** Organisms drifting in a uniform field
   behind everything, parting for nothing, schooling around
   nothing. *Cure:* the obstacle test — delete a text block and
   the parting field must visibly change (§6.2). If the swarm's
   behaviour is identical with the content removed, it was
   decoration, and it is cut or fixed.
2. **Chart-library cosplay.** A bar chart, pie or line graph
   dropped in with a glow filter on it. *Cure:* figures in this
   theme are either aggregated from organisms (§6.3) or printed
   plainly as a table (§6.13). There is no third, glowing-chart
   option.
3. **Neon aquarium.** Cyan at 40% of the page, everything
   glowing, saturation standing in for "ocean". *Cure:* the §2
   usage ratios are audited — cyan light is 2% of a page. Black
   water is the theme; light is its exception.
4. **The lying bloom.** A light-figure that shows a different
   number than its printed twin — rounded for beauty, sampled
   from a different total, left stale after a data edit. *Cure:*
   §10's figure-truth audit, and §6.4's rule that the count reads
   the printed node's value at runtime.
5. **Red confetti.** Predator red reused for errors, badges,
   sale tags, required-field asterisks — until red means
   "chrome" and the one real pass means nothing. *Cure:* the red
   census (§10): one red light, only during a pass, never a
   glyph. Errors are gold-deep (§6.14).
6. **Slot-machine counter.** The total spinning through random
   digits with a casino ease. *Cure:* §6.4's beats are the
   count's own eased fractions — every intermediate value is a
   true partial tally of the climb, and the deceleration is a
   tally nearing its end, not a wheel stopping.
7. **Glow prose.** Body copy set in cyan or gold because it
   "looks oceanic". *Cure:* §3 law 2 — light sets labels, links
   and figures; prose is bone. A paragraph you must squint at
   through its own glow is a defect, not a mood.
8. **The empty stage.** A pinned 220vh stage whose figure is a
   round marketing number ("10,000+ happy customers") with no
   stratum, no caption, no sheet row. *Cure:* a stage figure
   must be a stratum count from the sheet, captioned with its
   depths (§6.3) — ceremony is rationed to real soundings.
9. **Cursor plankton.** A pet organism glued to the pointer, a
   trailing sparkle cursor, a light that follows the mouse like
   a pet. *Cure:* refused in §5 — the pointer *disturbs* the
   water (the school flees it); it never acquires a follower.
   The cursor stays the system cursor.
10. **Strobe bloom.** Flares chained so fast the page flashes —
    hover storms, ripples on every scroll tick, aggregation
    strobing. *Cure:* §10's photosensitivity ceiling: no area of
    the page flashes more than 3 times per second; flares are
    waves with decays, never strobes.
11. **Skeleton theatre.** Unlit clusters pulsing beautifully
    while content waits behind a slow API, regions held past
    their data "for the effect". *Cure:* §6.15's 1,500 ms hard
    ceiling — print regardless. A loader that performs is a
    loader that lies about the wait.
12. **Aquarium screensaver.** The build where the swarm *is* the
    page and the print is a caption under it — gorgeous in a
    demo, useless as a census. *Cure:* the no-JS read (§10):
    with script off, the page must read as a complete, ordered
    document. If it does not, the light was the content, and
    the build fails.

## 10. Quality gate

All twelve checks are blocking. The gate is signed by someone
other than the builder (§15, step 15).

1. **Figure-truth audit.** Every figure performed by light —
   hero total (§6.4), three stage figures (§6.3), the form's
   № (§6.14) — equals its printed twin and its sheet row (§6.17)
   exactly. One organism of difference fails the gate.
2. **Sheet-sum audit.** Strata counts sum to the total; species
   counts sum to the total; the six ledger cards (§6.12) sum to
   the total; the footer's third printing (§6.18) agrees. The
   swarm allocation sums to the organism count for the
   breakpoint.
3. **Canvas-failure drill.** Canvas context killed at load and
   mid-session: the dot-field stands within §6.2's 1,200 ms, all
   figures printed, no dark or empty regions anywhere.
4. **No-JS read.** Script disabled: the whole page reads in
   order, the nav works, the form posts natively, the sheet is
   complete. (§9, failure 12.)
5. **Watchdog drill.** Fonts stalled, loop stalled, submission
   stalled, transition stalled, predator throttled mid-pass:
   each ceiling fires — hero 2,800 ms, stage 2,000 ms, count
   3,200 ms, unlit regions 1,500 ms, transition 2,000 ms, form
   4,000 ms, pass 8,000 ms — and every state lands printed.
6. **Red census.** Sampled across a 10-minute session including
   three passes: at most one red light at any instant, red only
   inside a pass, zero red glyphs, zero red UI elements.
7. **Reduced-motion pass.** With `prefers-reduced-motion`: no
   simulation, no counting, no passes, no ripples — and every
   figure, table and form still complete and usable. The still
   census is a full census.
8. **Photosensitivity check.** No region flashes more than 3
   times per second under worst-case interaction (hover storms,
   click storms, aggregation + ripple simultaneously).
9. **Print-first check.** At first paint, before any script:
   every figure on the page is legible at full contrast. The
   light may only ever add to a legible page.
10. **Performance sign-off.** §14's budgets measured on the
    reference mid-range device: simulation + render ≤4 ms per
    frame at full organism count, no long task >50 ms during
    the hero ceremony, page weight within budget.
11. **Depth agreement.** At five sampled scroll positions, the
    rail readout (§6.5), the nav's current dot (§6.11) and the
    stratum ground-darkening (§4) agree about which stratum the
    reader is in.
12. **Parting test.** With content blocks hidden one at a time,
    the swarm's parting field changes for each — proof the
    ecosystem is routed by the document (§9, failure 1).

## 11. Component inventory

Every component a real census site needs, with its treatment in
this theme. Refusals carry their in-theme replacement.

- **Primary button.** Cyan fill, midnight text (10.69:1), data
  voice label, sentence case. Press fires §6.8's ripple from the
  button's centre.
- **Honoured button** (the sighting submit, donations). Gold
  fill, midnight text (11.20:1). One per page at most — gold is
  rationed like the species it honours.
- **Quiet button / link-button.** Bone outline at 40%, bone text;
  hover fills the outline's water (water-3) and blooms the edge
  (§6.7).
- **Text link.** Cyan, underlined with a cyan-dim rule that
  brightens on hover; visited links shift to bone-dim with the
  underline kept — a sounded depth stays marked.
- **Inputs (text, number, date).** `--water-3` ground, bone text,
  bone-dim label above in the data voice; focus = 2 px bone
  outline + edge bloom (§6.14). Placeholder text is a ledger
  example ("e.g. Marina Beach, north end"), never a label
  substitute.
- **Select.** Native select restyled to the input treatment; its
  options are the sheet's species (§6.14) — the list is data,
  not chrome.
- **Textarea.** As inputs, with a ledger ruling (faint water-3
  lines every 1.65rem) — the report is written on ruled water.
- **Checkbox / radio.** A small unlit circle that blooms cyan
  when chosen (radio) or a tally mark drawn in cyan (checkbox):
  the ledger ticks its boxes by hand, in light.
- **Toggle.** A lantern switch: a pill of water-3 with an unlit
  dot that slides and lights cyan when on; label always printed
  beside it — the dot never carries the state alone.
- **Data table.** §6.13 is the pattern: scoped headers, tabular
  numerals, gold totals row, provisional rows dimmed and
  labelled.
- **Badge / chip.** Stratum chips: water-3 pill, bone-dim text,
  a 6 px dot in the stratum's dominant tint. Filter chips add a
  printed × and light their dot when active.
- **Alert / notice.** A ledger note: water-2 block, gold-deep
  correction mark (✳ in the ledger's hand) at its head, bone
  text. There is no red alert in this theme (§2); urgency is
  carried by placement and wording, not colour.
- **Pagination.** Sounding pages: "Soundings 1–12 of 61,408" in
  the data voice with prev/next lantern links (§6.11's dots at
  small size). Numbered pages print as fathom marks.
- **Modal.** The specimen jar: a `--water-3` dialog lifted to
  the lantern — outside it, the swarm dims 40% and stills its
  schooling near the jar; inside, print is still and complete.
  One modal at a time; Esc returns the jar to the water.
- **Toast.** Refused. A toast is a shout across the water;
  instead, confirmations are ledger lines appended where the
  act happened (§6.14's entry) or, for page-level events, a
  note line printed at the foot of the current section that
  remains until dismissed.
- **Tabs.** Stratum tabs on the sheet and species pages: the
  tab list is a row of lantern dots with printed labels; the
  active tab's dot is lit and its panel prints below.
- **Accordion.** The station log: each station a row that opens
  its nights beneath it, the row's dot lighting as it opens;
  opening is a print reveal (300 ms rise), not a bloom.
- **Tooltip.** A sounding note: a small water-3 card appearing
  above its term with the definition in caption text ("fathom —
  1.83 m, the depth of a naturalist's outstretched arms").
  Hover and focus both summon it; it never holds essential
  content alone.
- **Progress.** §6.5's depth line is the theme's progress
  component; in-component progress (an upload, a long form) is
  a sounding line in miniature: a hairline filling cyan with
  its figure printed at its end.
- **Skeleton.** §6.15's unlit clusters, shaped to the coming
  content, ceilinged at 1,500 ms.
- **Empty state.** §6.16's unlit water, at component or page
  scale.
- **Search.** An input in the lantern bar's drawer form: as the
  visitor types, matching species print beneath as ledger rows;
  no match prints §6.16 at small scale with the query in the
  ledger's words ("No species answers to that name tonight").
- **Breadcrumbs.** A surface trail: "Surface / Species Ledger /
  *Noctiluca scintillans*" in bone-dim with cyan-dim
  separators — the path back up the water column.
- **Avatar.** Refused as photographs; naturalists are initials
  in a tally circle (water-3 disc, bone initials) — the census
  records people the way it records stations, by mark.
- **Range slider.** A sounding slider for depth filters: the
  track is a vertical-feeling hairline (horizontal in layout),
  the thumb a lit dot, its value printed in fathoms at the
  track's end and updated live.
- **File upload.** Sample photographs for a sighting (§6.14's
  optional evidence): a dashed water-3 frame labelled in the
  ledger voice; a chosen file prints as a thumbnail in a
  volumetric frame (§6.9) at small size.
- **Divider.** A current hairline: a 1 px cyan-dim rule with a
  brighter 80 px reach at its centre — the current line's
  signature, borrowed at component scale (§6.6).
- **Blockquote.** A field note: Fraunces italic is forbidden
  here (§3 law 5 reserves italic for Latin) — field notes set
  in Fraunces roman, indented into the margin's water, with the
  note-taker's initials and night number as its citation.

## 12. Content & copywriting voice

Two registers, never blended in one sentence. **The Naturalist**
(Fraunces, prose): unhurried, exact, sensory without gushing —
the voice of someone who has actually stood in the water at
night. **The Ledger** (Space Grotesk, data and UI): terse,
numbered, admits the state of its evidence — provisional,
unverified, not sighted. Headlines are the Naturalist's;
labels, buttons, errors and totals are the Ledger's.

**Headline style.** A place, a depth, a count — in some order.
"The Twilight Shelf" alone is a label; "The Twilight Shelf —
19,876 lights between thirty and a hundred and ten fathoms" is
a headline. ✓ "Counted in the Shallows, where the water is
knee-deep and the light is thickest." ✗ "Dive into our amazing
data story!!" — the census does not exclaim; it has seen the
thing itself.

**Label style.** Data voice, uppercase, tracked (§3): "ORGANISMS
COUNTED", "DEPTH — FATHOMS", "RECORD №". Labels name the thing
counted, never the chart type: ✗ "BAR CHART 1" is impossible
here (§9, failure 2); ✓ "SOUNDINGS BY STRATUM".

**Error voice.** The Ledger corrects like a clerk who respects
the writer: it says what is missing, where, and what to write —
never blame, never red. ✓ "The night is missing — a sighting
needs its night. Enter the date you saw the bloom." ✗ "Invalid
input." ✓ (absurd value) "A bloom of one is still a bloom;
enter what you saw." (§6.14.)

**Empty-state voice.** Absence reported as a result. ✓ "No
species answers to that name tonight. The water is unlit, not
empty of everything — try the ledger." ✗ "Oops! Nothing
found." The word "oops" does not exist in this census.

**Fixed strings (verbatim, do not paraphrase).**
- The law, printed on the sheet: "Nothing glows that is not
  counted."
- The rounding note: "Shares are rounded; the counts govern."
- The 404 heading: "This water is not on the chart."
- The ledger-closed line: "The ledger is closed tonight;
  reports resume at dusk."
- The form's promise: "Reports on file: 412. Yours will be
  № 413." (numbers from the build's sheet.)

**Numbers in prose.** The Naturalist spells a count out when it
is the sentence's subject ("Sixty-one thousand four hundred and
eight organisms…") and uses figures everywhere else; the Ledger
always uses figures, always tabular, always with their unit or
their stratum attached — a bare number is a number out of its
water.

## 13. Full-page scroll choreography map

The home page, surface to floor. Every beat names what the
visitor sees and what the water does.

1. **Surface (0 fm).** The bloom wave (§6.1): darkness, ripple,
   the headline igniting in clustered light, print rising last.
2. **The count.** The total climbs its 26 beats (§6.4) and
   settles; the school takes the headline's lights back as the
   visitor begins to sink.
3. **First descent.** Prose of the Shallows; the swarm parts
   ahead of the text (§6.2); the depth comet ignites (§6.5);
   the current pulse is already travelling the right margin
   (§6.6).
4. **31,204.** The Shallows stage (§6.3): the figure aggregates,
   holds 1.2 s, disperses behind the reader.
5. **The ledger.** Species cards (§6.12) rise in their stagger;
   trays tilt under the pointer; the gold *Noctiluca* card leads
   — 24,917, the honoured species, met at tray scale before its
   stage.
6. **The Twilight Shelf (30 fm tick).** The rail's boundary
   pause; the ground darkens its 40%; the stratum band prints.
7. **19,876.** The Twilight stage, then — one screen later — the
   sounding table (§6.13): ceremony, then audit, by design.
8. **Surfacing photographs.** Volumetric frames (§6.9) rise
   through their centre band; the photographed bloom draws the
   living one toward it.
9. **The Midnight Shelf (110 fm tick).** The darkest water;
   10,328 aggregates in the page's last stage; the prose slows
   (22vh gaps, §4).
10. **The ledger page.** The sighting form (§6.14) in the dark,
    its № 413 promise lit by field blooms; the conversion
    happens at depth, where only the committed reader remains.
11. **The sheet.** §6.17: the water calms 20%; the whole census
    stands in print to be audited against everything above it.
12. **The floor (550 fm).** The footer (§6.18): totals a third
    time, the predator log, the school settling to rest above
    the floor line.

**Reverse pass.** Rising is the descent mirrored, not rewound:
figures do not un-form (they disperse ahead of the rising
reader and may re-form faster, 700 ms, §6.3); the depth readout
falls; stratum grounds lighten across the same 40vh boundaries;
the settled school lifts off the floor symmetrically. Nothing
plays backwards — water does not run in reverse; it settles
differently.

**Jump scroll.** A reader who jumps (End key, scrollbar drag,
anchor link) is owed the destination, not the journey: any
stage passed in under 300 ms of pin time does not aggregate;
the destination renders in its printed, lit state; the depth
comet hurries (≤600 ms, §6.5) but the readout never lies during
the hurry.

## 14. Whole-page performance budget

**Page weight (home, first load):** ≤840 KB total. Fonts
≤130 KB (Fraunces variable subset + Space Grotesk subset, latin
+ figures, `font-display: swap` with the §6.1 race rule). CSS
≤34 KB gz. JavaScript: the shared loop + simulation + all canvas
behaviours ≤42 KB gz; the form module ≤6 KB gz, deferred;
scrollspy and rail are inside the loop's budget, not separate
scripts. Images: ≤180 KB each (responsive WebP/AVIF), at most
one above the fold, the rest lazy. The canvas itself is code,
not an asset — the water costs no download beyond the engine.

**Frame budget.** At the full organism count (160), simulation +
render ≤4 ms per frame on the reference device (a mid-range
2021 laptop, DPR 1.5); all other per-frame work (rail, comet,
ripples, tilts) ≤1 ms combined; total theme cost ≤5 ms of the
16.7 ms frame, leaving the browser its majority. Long tasks:
none over 50 ms after load; glyph sampling (§6.1, §6.3, §6.4)
runs off the critical path and is cached per string.

**When the budget is exceeded, cut in this order** (each cut is
a configuration, not a redesign): (1) the current line (§6.6);
(2) the predator pass (§6.10); (3) the far mote layer; (4)
ripples (§6.8) beyond one concurrent; (5) aggregation reserve
140 → 90 with the coarser grid; (6) organism count 160 → 110 →
72. **Never cut:** the printed figures and their twins, the
depth readout, the census sheet, any watchdog or fallback, the
reduced-motion variants, the sounding table. The budget protects
the record first and the weather last — a poorer sea, never a
falser census.

**Runtime degradation.** Frame cost is measured on a rolling
2 s window; if simulation exceeds 5 ms sustained, the build
steps down the cut order automatically one rung per 5 s until
inside budget, and reports the rung in a `data-perf-rung`
attribute for §10's sign-off. Battery-saver and reduced-data
signals start the page at rung 3.

## 15. Build-order checklist

1. **The sheet first.** Author the census record (§6.17) as the
   build's single data source; every later step reads it.
2. **The printed page.** Complete static HTML — every figure,
   table, form and caption — readable and navigable with no CSS
   or JS beyond typography. This is the fallback; build it like
   the product, because for some readers it is.
3. **Tokens and type.** Palette (§2) as custom properties, the
   type scale and five laws (§3), `color-scheme: dark`, the
   print stylesheet.
4. **Layout and strata.** The column, margins, stratum grounds
   and darkening, the stage geometry (§4).
5. **Instruments.** Depth rail and readout (§6.5), nav and
   scrollspy (§6.11) — one boundary table feeding both.
6. **The static water.** The dot-field fallback in place and
   verified (§6.2) before any canvas exists.
7. **The swarm.** Canvas, sprites, simulation, obstacle
   parting, pointer flee (§6.2) on the single shared loop (§5).
8. **The hero.** Bloom wave and counting total (§6.1, §6.4),
   with their watchdogs.
9. **The stages.** Digit aggregation (§6.3) for each stratum,
   figure-truth checked against step 2's print.
10. **Attention behaviours.** Bloom hover (§6.7), ripple (§6.8),
    card tilt (§6.12), volumetric frames (§6.9).
11. **The predator.** Schedule, lane, cone, watchdog (§6.10) —
    built late, rationed from birth.
12. **The form.** §6.14 with native-post fallback working
    before the JS enhancement is attached.
13. **Loading and edges.** Unlit clusters and transitions
    (§6.15), empty states and the 404 (§6.16).
14. **Sheet and floor.** §6.17 wired to the same record as
    step 1; footer settling (§6.18); the current line (§6.6)
    last of the elements — it is the first cut if budgets bite.
15. **The gate.** §10's twelve checks, run and signed by a
    non-builder, including the failure drills with the canvas
    killed and the network throttled. No signature, no ship.
