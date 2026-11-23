# 76. Ice Core Archive — Expanded (v1 + v2)

> Eight hundred thousand years in a tube of ice. The page is a
> drilled core and scrolling is drilling: each stratum is an era,
> the deeper the reader goes the older and stranger the world
> gets, and every number on the page — depth, age, CO₂ — is read
> off the ice by one published function, never typed in by hand.
> Built for a fictional Dome C deep-drilling programme, the
> Concordia Deep Core Programme, drilling at 3,233 m on the East
> Antarctic plateau.

**The theme's one law: the core is the record — every figure is
drilled, not written.** Depth is the only input. Age is computed
from depth by the one declared function (`age = 800,000 × p^2.8`,
where `p` is depth ÷ 3,270 m); CO₂ is interpolated between the
anchor points printed in the core record (§6.15); era boundaries,
ash layers and sample tags all sit at the depths that function
puts them. A figure that cannot be re-derived from the record by
a visitor with a calculator does not belong on the page. And the
descent is an overlay, never a hiding place: the page ships fully
lit at surface white with every word readable, and the deepening
blue is a tint the script lays over finished content — each band
carries its own declared text pairing, so nothing ever darkens
into illegibility on the way down.

Reference implementation: demos/ice-core-archive.html

---

## 1. Concept & world

A ice core is the only archive on Earth that stores the air
itself. Snow falls on the plateau, compacts to firn, seals to ice,
and traps bubbles of the atmosphere of its year — so a 3,270 m
tube drilled at Dome C holds 800,000 years of weather, ash from
eruptions nobody witnessed, and the CO₂ curve of eight ice ages,
in order, oldest at the bottom. This theme takes that object
literally as a page structure. The page *is* the core: a fixed
rail core runs down the left edge ruled every 100 m, a pinned
mono readout reports DEPTH / AGE / CO₂ beside it, and scrolling
drills — the fill front descends, the background tint deepens from
core white to ancient blue, and the age readout accelerates
through the real non-linear maths of ice flow, crawling through
the Holocene and crossing millennia per centimetre near the bed.

The emotional register is cold, quiet and exact. Nothing on the
page is in a hurry — drilling advances metres per day, and the
theme's motion is priced accordingly: scrubs are heavy (lerp
0.09), reveals settle rather than snap, and the only fast thing
on the page is the red stamp, because a stamp is a hand coming
down. Warmth exists but it is rationed and human: Fraunces'
old-style serif against the cold, a field camp with tents and a
flag, two polar bears who live on the surface the core came from.
The page's drama is stratigraphic: ash layers appear where the
eruptions actually put them — Campanian Ignimbrite (≈39,000 BP,
1,112 m) above the Toba super-eruption layer (≈74,000 BP,
1,397 m) — and the page says so, in print, because a core that
lies about its layers is a poster, not an archive.

**Best-fit sites and audiences.**

- **Climate-science programmes, ice-core projects and polar
  institutes** publishing a flagship long-form feature: the page
  structure is their data structure, and the readout teaches the
  age–depth relationship by making the visitor's thumb perform
  it.
- **Museum and science-press features** on deep time, where the
  audience must *feel* 800,000 years rather than read the number —
  the non-linear scrub does what no paragraph can: the last 10%
  of the scroll is older than everything above it combined.
- **Research consortia and drilling campaigns** reporting a
  season: the core tray is a table of contents, the sample form
  is a real collaboration instrument, and the honesty note is the
  credibility signal funders actually read.
- **Data-storytelling teams** with a genuine depth series —
  sediment cores, boreholes, ocean transects, tree-ring and
  speleothem archives — any record where position *is* time.

**When NOT to use it.**

- **Anything that is not a depth record.** If the content has no
  honest vertical axis — no quantity that deepens monotonically
  and means more as it goes — the rail becomes a costume and the
  readout a random-number generator. The theme exposes invented
  data faster than any other in this library, because every
  figure invites recomputation.
- **Fast transactional flows.** Checkout, booking and dashboards
  need the visitor at the surface, acting now. The one conversion
  surface this theme licenses is the sample request (§6.14), and
  even that is a logbook entry, not a funnel.
- **Warm, fast or loud brands.** The palette tops out at glacial
  blue and the loudest event is a red stamp. A product launch in
  core white will read as a refrigeration manual.
- **Short content.** The descent needs strata to descend through:
  fewer than five substantial sections and the drill reaches the
  bed before the reader has felt the Holocene end. Below that,
  use a shallower theme.

**The bears are residents, not mascots.** The patrolling bear
(§6.10) and the camp bears (§6.12) are flat silhouettes with real
walk cycles and real camp facts beside them; they are never
named, never speech-bubbled, never rendered cute. They mark the
surface — 0 yr BP, the present day — which is the one stratum the
reader is standing in. The moment a bear winks, the archive
becomes a children's poster and the data stops being believed.

---

## 2. Palette

Five anchors from the original entry, unchanged, plus six derived
tokens. Every contrast figure below was **computed from the hex
values for this expansion** (WCAG relative luminance), not
estimated. The palette's discipline: white and glacial do the
surface work, ancient blue is *earned* by depth, ash grey is a
material (a layer in the ice) before it is a text colour, and
marker red is a stamp — it appears only where a human hand would
have put it: stamps, the drill line, sample tags.

| Token | Hex | Role | Usage ratio | Pairing / contrast ruling |
|---|---|---|---|---|
| `--core-white` | `#EDF2F2` | Core white — the page ground, the ice surface, un-drilled strata | ~48% of surface | Ground for `--ink-frost` text: **12.88:1** — the page's reading pair |
| `--glacial` | `#7FB0C4` | Glacial blue — young-ice tint, tray segments, band mid-tones | ~20% | On `--core-white` **2.09:1 — never text, never a text ground for white**; `--ink-frost` on it is 6.18:1 (the mid-depth reading pair) |
| `--ancient` | `#2E5F74` | Deep ancient ice — the filled rail core, deep strata bands | ~16% | `--core-white` on it **6.18:1** — the deep reading pair; `--glacial` on it 2.96:1, graphic only |
| `--ash` | `#6B6F72` | Ash-layer grey — volcanic layers, captions, secondary stamps | ~5% | On `--core-white` **4.49:1 — labels and captions ≥14px only, never body copy**; it is a material first |
| `--marker` | `#C0392B` | Marker red — stamps, drill line, sample tags ONLY | ≤2% | On `--core-white` **4.81:1** (stamp text legal); on `--ancient` **1.28:1 — forbidden pairing**: the drill bit rides on a core-white collar (§6.3), never bare on the fill |
| `--ink-frost` | `#1C2B33` | Deep-ice ink — body and display text on light grounds | text | On `--core-white` 12.88:1; on `--glacial` 6.18:1; never used on `--ancient` (white takes over below the declared threshold, §4) |
| `--core-pale` | `#F8FBFB` | Raised ice — tray segments, cards, the form sheet | raised surfaces | A surface, not a text colour; `--ink-frost` on it ≈12.9:1 |
| `--frost-line` | `#C9D8DC` | Frost line — rail ticks, hairlines, band rules on white | lines only | Never text; exists to be ruled, not read |
| `--glacial-deep` | `#4E86A0` | Mid-strata blue — the transition band between glacial and ancient | band ground | `--core-white` on it **3.55:1 — display text ≥24px only**; body in this band sits on `--core-pale` insets |
| `--ancient-deep` | `#1E4256` | Bedrock approach — the deepest band and the footer ground | ~6% | `--core-white` on it **9.44:1** — the footer reading pair; `--glacial` on it 4.53:1 (labels legal); `--marker` on it 1.96:1 — forbidden, stamps in the footer are white |
| `--bubble-sheen` | `#FFFFFF` | Bubble glint — a gradient stop inside the hero core only | inside §6.1 only | Never a surface, never text; exists at 12–40% opacity inside ice |

**Dark behaviour — there is no dark-mode inversion; there is a
depth behaviour.** The page's light-to-dark journey is the scroll
itself, driven by content position, not by the visitor's OS. A
`prefers-color-scheme: dark` visitor gets the identical descent;
the theme refuses to start a science archive at the bed.
`prefers-reduced-data` and print both resolve to the **surface
state**: the whole page rendered as it ships — core white ground,
ink-frost text, rail core printed with its fill at the visitor's
current depth as a static band, readout values printed as final
figures. Print stylesheet = surface state exactly: an archive is
meant to be filed.

**Rationing rules (enforced by the quality gate, §10).**

- Marker red appears only as: the drill line (§6.2), the drill
  bit's collar tag (§6.3), SAMPLE CUT stamps (§6.5, §6.14), the
  camp flag (§6.12) and sample tags in the record (§6.15). A
  page-wide red census above 10 instances fails the gate. Red is
  never a link colour, a button fill or an error colour — errors
  in this archive are ash-grey notes (§6.14).
- The background tint may only deepen through the declared band
  sequence (white → glacial wash → glacial-deep → ancient →
  ancient-deep) at the depth thresholds in §4. No band may be
  skipped, and no band may carry text in a pairing this table has
  not licensed.
- Ash grey is drawn as *layers* (2–6px bands in the core, §6.6)
  far more often than it is set as type. A page where ash is
  mostly text has mistaken the material for a colour.

---

## 3. Typography

Three faces, three jobs. **Fraunces** is the warmth — an old-style
serif with soft, slightly bookish forms, used for display and era
headings; it is the voice of the scientists writing about the ice.
**Archivo** is the working body face — neutral, sturdy, set in
long strata of text. **JetBrains Mono** is the instrument — every
depth, age, CO₂ figure, stamp and readout, because a number that
must be audited is set in a face whose digits cannot shift.

| Role | Face / weight | Size | Line-height | Tracking | Rules |
|---|---|---|---|---|---|
| Display (hero) | Fraunces 560, optical sizing on | `clamp(2.6rem, 5.8vw, 4.5rem)` | 1.04 | −0.01em | Sentence case; revealed stratum by stratum (§6.2); never set in `--ancient` on white below 6.18:1 pairings |
| Era heading | Fraunces 600 | `clamp(1.7rem, 3.2vw, 2.4rem)` | 1.12 | 0 | Prefixed by its depth range in mono (`723–1,636 M —`) |
| Sub-head / segment title | Archivo 600 | 1.125rem | 1.3 | 0 | Tray segment names, card titles, camp facts' labels |
| Body | Archivo 400 | 1.0625rem (17px) | 1.6 | 0 | Max measure 64ch; body never sits directly on `--glacial-deep` or deeper — it moves to `--core-pale` insets (§4) |
| Caption / honesty note | Archivo 400 italic | 0.9375rem | 1.5 | 0 | The archive's conscience voice (§6.6); italic is reserved for it and for Latin binomials |
| Data / readout | JetBrains Mono 500 | 0.875rem | 1.4 | 0 | Tabular by nature; readouts at `clamp(1.05rem, 1.6vw, 1.3rem)`; figures never wrap mid-number |
| Stamp lettering | JetBrains Mono 700 | 0.8125rem | 1 | 0.14em, uppercase | SAMPLE CUT / depth tags — the only all-caps text on the page |
| Depth scale (rail) | JetBrains Mono 500 | 0.6875rem | 1 | 0.05em | Tick labels every 100 m down the rail (§6.3) |

**Type laws.**

1. **Numerals are mono, always.** A depth set in Fraunces is a
   rounding waiting to happen; mono digits confess every change
   as the readout runs (§6.4).
2. **Ages are printed with their unit and their era** — "74,000 YR
   BP", never a bare 74000 — because the page's whole argument is
   that these numbers are durations, not scores.
3. **Fraunces never sets a figure, and mono never sets a
   sentence.** The instrument reads; the voice explains; the two
   do not swap jobs.
4. **Stamps are the only uppercase.** Headlines in caps would
   shout over ice that took 800,000 years to accumulate; the
   archive does not shout.
5. **The honesty note is always italic Archivo, always ash or
   ink, always on the surface pairing** — a caveat set in red
   would read as an alarm; set in small mono it would read as
   fine print. It is neither (§6.6).

---

## 4. Layout language

The page is a **core laid vertically beside its own reading**.
A fixed left rail, 96px wide on desktop, carries the core column
itself (64px of ice, §6.3) and its tick scale; immediately right
of the rail, a pinned readout block (§6.4) reports the drill's
position. All content lives right of the rail in wide, quiet
strata bands. The right margin carries snow: the paw-print trail
(§6.11) descends it on wide screens. The hero inverts the scale
once — the core there is 180px wide and the subject of the page
(§6.1) — before the rail takes over at instrument size.

**Grid and rhythm.**

- Rail: fixed, full viewport height, 96px (≥1200px), 72px
  (768–1199px), and a 56px top bar under 768px (§6.3's breakpoint
  ruling). The rail never scrolls; the drill front moves inside
  it.
- Content column: max 1160px, starting after rail + 48px gutter.
  Readout block pins at the rail's right edge, top-aligned with
  the hero's base, and stays for the whole descent.
- Baseline rhythm: 8px grid. Strata bands are separated not by
  rules but by **tint steps** — the background lerps continuously
  with lerped progress and *quantises its text pairing* at five
  declared thresholds (p = 0.18 / 0.38 / 0.58 / 0.78 / 0.92):
  below each threshold the band's text colour, inset colour and
  caption colour switch as a set, so the page is always in a
  licensed pairing from §2 even mid-lerp.
- Era sections are **strata**: full-bleed bands with 96–160px of
  vertical air, an era heading prefixed by its mono depth range,
  and the margin stratigraphy column (§6.7) drawn at the band's
  left inset. Density is deliberately low — one idea per stratum,
  like one climate per layer — against the readout's dense mono
  cluster at the rail. The contrast between sparse strata and a
  busy instrument is the theme's central spatial fact.

**The tray.** The core tray (§6.5) is the page's one horizontal
object: five segments lying in a shallow tray, presented
left-to-right in depth order, each segment a miniature of the
section it names. It sits at the surface (before the descent
deepens) so the visitor handles the whole 800,000 years at arm's
length before drilling into it.

**Whitespace.** Whitespace here is *undrilled ice*: pale, faintly
grained, never pure flat white, and never filled with decorative
objects that are not in the record. A snowfield with a bear on it
(§6.10) is a stratum (the surface); an empty band with a floating
icon is a lie about the archive's contents. If a band has nothing
to say, it is not padded — the descent simply passes through it
faster, and the readout shows the reader why.

---

## 5. Full motion system

Motion in this theme is **drilling: slow, weighted, and
irreversible in one direction**. The drill descends; it does not
bounce back up the hole. Every scrubbed value — the rail fill,
the readout figures, the background tint, the paw prints, the
strata highlights — is computed from **one shared rAF loop**
reading a single lerped progress value (`--loop-lerp: 0.09`, the
heaviest lerp in this library, because ice resists). Raw
`scrollY` is never written to the DOM by any handler; the loop
owns all descent values, and each element below registers with
the loop rather than running its own scroll listener.

**The published functions (the page's physics, printed in
§6.15).**

- `p` = lerped scroll progress through the descent, 0–1.
- `depth(p) = 3,270 × p` metres.
- `age(p) = 800,000 × p^2.8` years BP — the age–depth curve. Near
  the surface 1% of scroll ≈ 60 years; at p = 0.9 the same 1% ≈
  19,000 years. This asymmetry is the theme's thesis and is never
  "corrected" into linearity.
- `co2(p)` = linear interpolation between the record's anchor
  points (§6.15): (0 BP, 280) · (11,700, 265) · (20,000, 190) ·
  (39,000, 205) · (74,000, 200) · (123,000, 280) · (400,000, 265)
  · (800,000, 195) ppm, evaluated at `age(p)`.

**Named easings (the only ones the theme uses).**

| Token | Curve | Used by |
|---|---|---|
| `--ease-drill` | `cubic-bezier(0.6, 0.05, 0.3, 1)` | Scrubbed descent character — counter easing, tint steps, strata highlights; a bit biting, then carrying |
| `--ease-settle` | `cubic-bezier(0.25, 0.6, 0.3, 1)` | Reveals, band changes, the thaw — everything unhurried |
| `--ease-stamp` | `cubic-bezier(0.2, 1.25, 0.4, 1)` | The SAMPLE CUT stamp and cut receipt — the system's one overshoot, a hand coming down |
| `--ease-grow` | `cubic-bezier(0.3, 0.8, 0.3, 1)` | Frost crystal growth, paw-print press, bubble glints |
| `--ease-lift` | `cubic-bezier(0.25, 0.8, 0.35, 1)` | Tray segment lift, card rises — a section lifted from its tray, no bounce |

**The motion terms, in this theme's language.**

- **Scroll-triggered reveals** — strata *surface* as the drill
  reaches them: a band's content rises 12px and settles over
  700ms `--ease-settle` as its heading crosses 72% of the
  viewport, with the band's ash layers and frost (§6.8) arriving
  on their own beats. Content is fully visible before, during
  and after; the reveal is a change of emphasis, never of
  existence.
- **Scroll-driven / scrubbed animation** — the descent itself:
  rail fill (§6.3), readout (§6.4), tint, paw prints (§6.11) and
  strata highlights all read the loop's `p`. Scrubbing back up
  *raises the drill*: fill, figures and tint reverse exactly,
  because re-reading shallower ice is legitimate — but stamps
  (§6.5) and the tray's cut tags never un-stamp; what a visitor
  has sampled stays sampled.
- **Parallax** — two depths only, both inside ice: the hero
  core's bubble layer (§6.1) at 0.94× and the snow ridge at the
  hero's foot at 1.03×. The rail and the strata never parallax —
  an instrument that drifts is an instrument that lies.
- **Pinned sections** — the rail core and readout pin for the
  entire page (they are the instrument panel, not a section);
  the core tray pins for 120vh while its five segments present
  in sequence (§6.5); the camp scene's fact counters pin beside
  the scene while it plays (§6.12).
- **Masked line reveals** — the hero headline un-clips stratum
  by stratum behind the descending drill line (§6.2), each line
  a clip-path inset released as the line passes its baseline.
  Text is in the DOM and readable from first paint; the mask is
  JS-armed only, with a hard 4.5s fallback.
- **Blur-to-sharp** — given its ice form, once: photographs of
  core sections enter as *frosted* (a 6px backdrop blur on a
  surface glaze, never on the image's data) and the glaze clears
  over 900ms as the section centres — frost wiping off a cold
  store window. Body text is never blurred at any point.
- **Kinetic typography** — *refused, with a reason:* type in an
  archive does not perform. The only moving letterforms are the
  readout's digits (§6.4), which move because the *quantity*
  moves, and stamp lettering, which arrives with the stamp.
- **Marquee** — *refused:* nothing at Dome C moves sideways at
  reading speed except the wind, and the wind is drawn as streaks
  in the camp scene (§6.12), not as text. There is no ticker in
  the archive.
- **Counters** — §6.4's readout (continuous, scrubbed) and
  §6.12's camp facts (count-up on entry, 1400ms `--ease-drill`,
  landing exactly on the printed figure, which is in the DOM
  from first paint). Counters never count to a rounded value.
- **SVG line-draw** — the margin stratigraphy column (§6.7)
  strokes in band by band as each era arrives; the drill line
  (§6.2) is a dashed stroke whose dashoffset is the descent
  made visible.
- **Image scale-in-frame** — core-section photographs scale
  1.07→1.0 inside their tray frames over 1100ms `--ease-settle`
  as they centre; the frame is a tray slot and never moves.
- **Hover / magnetic / tilt micro-interactions** — magnetic is
  refused (instruments are not attracted to hands); tilt is
  licensed exactly once, as physics: tray segments tilt up like
  a section lifted from its tray (§6.5), rotating on their long
  axis by 4° with the far edge rising. The hero core's hover is
  a lamp, not a lean (§6.9). Buttons get a 140ms frost-line
  underline draw.
- **Custom cursor** — *refused, standing rule.* The visitor's
  pointer is a hand at a field site, not an exhibit.
- **Skeleton loading** — the un-drilled core (§6.16): content
  areas print as blank core-white sections in an outlined tube,
  ruled with faint ticks, with a printed "CORE NOT YET RAISED"
  note; hard ceiling 2000ms before the watchdog raises the
  content regardless.
- **Page transitions** — the thaw (§6.16): a 320ms frost glaze
  sweeps the viewport edge-to-edge as pages change, content
  swapped at the glaze's peak; aborted at 1400ms by watchdog.
- **Ambient loops** — exactly three are licensed: the hero
  bubbles (§6.1, continuous physics), the patrolling bear
  (§6.10, a ~48s round with pauses), and the camp's wind and
  flag (§6.12, while the scene is on screen). All pause when
  their section is off-screen or the tab is hidden; none runs
  merely because the page is open.
- **Progress indicator** — the rail core itself (§6.3): fill,
  bit and depth scale are the progress, the scale and the
  readout in one object. There is no separate progress bar
  anywhere in the theme.
- **Reduced motion** — §10's global ruling: the descent becomes
  a printed core — rail fill drawn at final depth as a static
  band, readout values printed at the figures for the section
  in view, bubbles drawn once as a still field, bear standing
  at the ridge's centre, tray flat with all tags printed, tint
  stepped (not lerped) at band thresholds. The reduced page is
  the *filed* archive, not a stripped one.

---

## 6. Signature elements

### 6.1 Hero ice-core cylinder with trapped air bubbles

- **What & why.** The hero is a single object: a 180px-wide,
  full-hero-height core of ice, drawn with frosted cylindrical
  shading (a horizontal linear gradient, `--core-pale` →
  `--glacial` → `--ancient` at the shaded edge, plus an inner
  shadow at the tube's rim), banded with the same strata the page
  below will drill through — Holocene white at the top, the two
  ash layers as thin grey lines at their true fractional depths
  (1,112 m and 1,397 m of 3,270 m: 34.0% and 42.7% down the tube),
  deepening to ancient blue at the base. Inside it, a canvas
  holds 46 air bubbles that rise, wobble and glint endlessly.
  It belongs because the core is the site's subject, evidence
  and logo in one object; a hero photograph of Antarctica would
  be scenery, but this is the artefact itself.
- **Structure.** A DOM cylinder (three stacked gradient layers +
  rim highlights, all CSS) with one `<canvas>` absolutely
  positioned inside the tube's inner width (132px), clipped to
  the tube by `border-radius` and `overflow: hidden`. Strata
  bands are DOM divs whose heights are computed from the record
  (§6.15) at build time and printed as data attributes
  (`data-depth-from`, `data-depth-to`). Bubbles are canvas-drawn
  circles (radius 1–3.5px, `--bubble-sheen` at 12–40% opacity)
  with a 1px glint arc. The headline and standfirst sit right of
  the cylinder on desktop, below it on mobile. No WebGL; if
  canvas is unavailable the cylinder renders with a static SVG
  bubble field baked at build time.
- **Motion spec.** Trigger: time, from load, ambient. Bubbles
  integrate with real dt (clamped to 33ms per frame): rise speed
  6–14 px/s scaled by radius (smaller bubbles are older air and
  rise slower), horizontal wobble = sin(phase + y·0.02) × 2px,
  glint opacity oscillates on a 3–7s per-bubble period. A bubble
  reaching the top fades over 600ms and respawns at the base —
  the air in this ice is 800,000 years old and is in no hurry,
  so nothing pops. The whole field runs only while the hero is
  ≥10% visible (IntersectionObserver) and the tab is visible.
- **States.** Rest (bubbles rising) / lit (§6.9's core-light
  active: nearby bubbles cluster) / stilled (reduced motion or
  data-saver: one static frame) / past (hero scrolled away:
  loop unregistered, zero cost).
- **Content merge.** The cylinder's bands are labelled with the
  same era names and depth ranges as the tray (§6.5) and the
  strata below — it is the table of contents rendered as the
  object itself. Strip the labels and the hero is decoration;
  with them, a visitor can read the whole archive off the hero
  before scrolling.
- **Failure fallback.** Watchdog at 3000ms: if the canvas has
  not painted two consecutive frames (blocked script, starved
  budget), the canvas is removed and the baked SVG bubble field
  is shown. No-JS: the SVG field ships in the DOM and the canvas
  is JS-inserted over it. The cylinder, bands and labels are
  pure DOM/CSS and can never fail to appear.
- **Reduced-motion variant.** The SVG still field, printed:
  bubbles at fixed positions, no rise, no glint cycle. The
  cylinder and its labelled bands are unchanged — stillness is
  this ice's natural state, so the variant loses nothing.
- **Performance budget & mobile variant.** One canvas ≤132×900
  device px, 46 particles, dt physics with no allocation in the
  loop; budget ≤0.5ms/frame. Mobile (<768px): cylinder 120px
  wide, 28 bubbles, glint cycle off (static glint per bubble),
  canvas height capped at 60vh.
- **Choreography timeline (v2).** t=0 first paint (cylinder,
  bands, labels and SVG bubble field all printed) → JS arms →
  canvas fades in over the SVG over 500ms as its first frame
  paints → bubbles begin rising from their printed positions
  (no teleporting: canvas seeds from the SVG's coordinates) →
  first respawn cycle completes ≈t=40s → watchdog deadline
  t=3000ms passes unused.
- **State matrix (v2).** *Rest:* rising. *Hover:* §6.9's lamp
  (desktop, pointer fine only). *Focus:* the cylinder is not
  focusable; its band labels are text, not controls. *Active:*
  n/a. *Scrolled-past:* loop unregistered. *Disabled:* n/a.
  *Touch:* no hover state; a tap on the cylinder does nothing —
  the hero core is looked at, not operated (the tray, §6.5, is
  the operable miniature).
- **Breakpoints (v2).** ≥1200px: 180px cylinder, 46 bubbles,
  headline right. 768–1199px: 148px cylinder, 38 bubbles,
  headline right with narrower measure. <768px: 120px cylinder
  centred above the headline, 28 bubbles, bands keep labels but
  at mono 0.6875rem.
- **Edge cases & failure modes (v2).** *No canvas:* SVG field
  (above). *Low-power device:* `hardwareConcurrency` ≤2 or a
  save-data signal caps bubbles at 20 and disables the glint
  cycle. *Very tall hero (>120vh):* canvas height caps at
  120vh and the cylinder's lower bands repeat the tint, never
  stretch the strata — band heights are data, not decoration.
  *Tab hidden mid-rise:* dt clamp means bubbles resume within
  33ms of their printed physics — no jump on return.
- **Accessibility spec (v2).** The canvas is `aria-hidden`; the
  cylinder's information content (era bands with depth ranges)
  is real DOM text beside it, in reading order. The hero's
  heading order is headline → standfirst → band list. No
  information exists only inside the canvas. Contrast: band
  labels sit on `--core-pale` chips, `--ink-frost` at 12.88:1,
  never directly on the gradient.
- **Tokens consumed (v2).** `--core-white`, `--core-pale`,
  `--glacial`, `--ancient`, `--ash`, `--bubble-sheen`,
  `--ink-frost`, `--ease-grow`, `--loop-lerp`.

### 6.2 Descending drill line + stratum-by-stratum headline reveal

- **What & why.** On load, a dashed marker-red line descends
  the hero core over ~1.8s, and the headline — set in three
  lines, one per "stratum" — un-clips line by line as the line
  passes each baseline, finishing with a rotated red age stamp
  printing last ("800,000 YEARS IN ONE TUBE" is the stamp's
  text in the reference build). It belongs because the reveal
  performs the theme's premise instead of decorating it: you
  read the headline by drilling to it, at drilling's pace.
- **Structure.** The line is an SVG path (2px, dashed 6/5,
  `--marker`) overlaid on the hero core (§6.1), drawn by
  stroke-dashoffset. Headline lines are block spans with
  `clip-path: inset(0 0 100% 0)` in their JS-armed pre-state;
  the stamp is a bordered mono element, rotated −6°, initially
  scale 1.6 / opacity 0 in its armed state. All pre-states are
  applied by a `.js` gate class on `<html>`; without it, the
  headline prints whole and the stamp sits at rest.
- **Motion spec.** Trigger: page load, once. Line draws
  0→100% over 1800ms `--ease-drill`. Line 1 un-clips over
  500ms as the line crosses 22% (t≈400ms); line 2 at 48%
  (t≈860ms); line 3 at 74% (t≈1330ms); each `--ease-settle`.
  Stamp lands at t≈1950ms: scale 1.6→1 + opacity 0→1 over
  240ms `--ease-stamp`, with a 1-frame 1px settle. The sequence
  is skippable: first scroll or any keypress completes it
  instantly to final state.
- **States.** Pre-state (JS-armed, <100ms) / drilling (line
  descending, lines releasing) / printed (final, permanent) /
  skipped (jumped to printed). There is no replay: a drilled
  headline stays drilled.
- **Content merge.** The headline's three lines are the site's
  actual title and claim, and the stamp prints the archive's
  actual span — the animation's beats are the sentence's own
  strata. Remove the drill and the lines still read perfectly;
  the line adds the *act* of reaching them.
- **Failure fallback.** Hard fallback at 4500ms: a watchdog
  removes all clip-paths and prints the stamp at rest, whatever
  state the sequence is in. No-JS: no pre-state exists (the
  gate class is absent), so the headline and stamp ship
  printed. A blocked animation frame can delay the drill; it
  cannot bury the headline.
- **Reduced-motion variant.** No descent, no un-clip, no stamp
  impact: headline printed whole, stamp at rest at −6°. The
  page opens as a filed front page.
- **Performance budget & mobile variant.** One SVG stroke +
  three clip-path animations, transform/opacity/clip only;
  budget ≤0.2ms/frame for 2s. Mobile (<768px): the line
  descends the 120px cylinder in 1400ms; the stamp rotates
  −4° (less travel on a narrow measure) and lands at t≈1600ms.
- **Choreography timeline (v2).** t=0 paint (headline whole if
  no JS; armed pre-state if JS, applied before first paint via
  the gate class) → t=100ms line starts → 400ms line 1 →
  860ms line 2 → 1330ms line 3 → 1800ms line complete, fades
  to 40% (it stays as the hero's drill scar) → 1950ms stamp →
  2190ms printed, sequence deregisters → watchdog deadline
  t=4500ms passes unused.
- **State matrix (v2).** *Rest:* printed (after the one run).
  *Hover:* none — the headline is not a control. *Focus:* if
  focus enters the hero during the run, the sequence completes
  instantly (a keyboard visitor never waits for a reveal).
  *Active:* n/a. *Scrolled-past:* completed instantly at first
  scroll. *Disabled:* n/a. *Touch:* first touch-scroll skips,
  as scroll does.
- **Breakpoints (v2).** ≥1200px: as specified. 768–1199px:
  line duration 1600ms, crossings at 24/50/76%. <768px: 1400ms,
  two-line headline variant (the title's short form, declared
  in the record), stamp −4°.
- **Edge cases & failure modes (v2).** *Slow font load:*
  Fraunces swapping mid-reveal shifts baselines; the clip
  releases are keyed to the line's progress, not to line
  boxes, so a font swap can change which glyphs show but
  never re-buries a released line (clip only ever opens).
  *Return visit:* the sequence runs once per session
  (sessionStorage flag); later loads print instantly.
  *Headline longer than three lines:* the record caps the
  title at three strata; a fourth line is an editorial error
  the gate (§10) rejects, not a layout case.
- **Accessibility spec (v2).** The headline is one `<h1>` with
  three visual lines (spans, not separate headings); AT reads
  it whole from first paint — clip-path does not remove it
  from the accessibility tree, and the armed pre-state is
  never `visibility: hidden`. The stamp is `aria-hidden`
  decoration around a real text span (the span is in the h1's
  following paragraph for AT). Focus never waits on the
  animation (see state matrix).
- **Tokens consumed (v2).** `--marker`, `--ink-frost`,
  `--ease-drill`, `--ease-settle`, `--ease-stamp`.

### 6.3 Scroll-scrubbed rail core with drill bit

- **What & why.** The page's spine: a 64px-wide core column
  fixed in the left rail for the entire page, ruled with ticks
  every 100 m (33 ticks over 3,270 m, labelled every 500 m).
  As the visitor scrolls, glacial fill grows down the tube and
  a marker-red drill-bit marker rides the fill front. It is
  the progress indicator, the depth scale and the theme's
  thesis in one instrument: your position on the page *is* a
  depth, and the rail never lets you forget which one.
- **Structure.** Fixed rail (`position: fixed`, left, full
  height) containing: the tube (64px, `--core-white` ground,
  1px `--frost-line` edges), the fill (a child div, glacial →
  ancient vertical gradient, transformed by `scaleY` with
  `transform-origin: top` — never layout height), the tick
  scale (an SVG ruled at build time from the record, ticks at
  exact 100 m fractions), and the bit: a 26px marker-red
  triangle-and-collar marker whose collar is a 14px
  `--core-white` chip (the §2 ruling: red on ancient is
  1.28:1 and forbidden, so the bit always rides on white).
  Fill and bit are written only by the shared rAF loop from
  the lerped `p`.
- **Motion spec.** Trigger: scroll, continuous. Fill scaleY =
  p; bit translateY = p × (rail height − 26px); both from the
  loop's lerped p (lerp 0.09), so the drill lags the scroll by
  a weighted beat and settles like a heavy instrument. The
  tick nearest the front brightens (opacity 0.45→1) as the
  front passes it. Scrolling up reverses everything exactly —
  the drill can be raised; only stamps (§6.5) are permanent.
- **States.** At surface (p=0, bit at top, fill empty) /
  drilling (0<p<1) / at the bed (p=1: bit rests on the
  ancient-deep base, a mono "BEDROCK — 3,270 M" label prints
  under the rail) / stepped (reduced motion: fill jumps
  between band thresholds, no lerp).
- **Content merge.** The rail's scale is the page's own
  contents list: era boundaries from the record are marked on
  the tube as named ticks (HOLOCENE BASE 723 M, TOBA 1,397 M…),
  so the progress bar is simultaneously the archive's index.
  A generic progress bar could sit on any site; this one can
  only sit on a page whose sections are strata.
- **Failure fallback.** No-JS: the tube prints with its strata
  bands at their true fractional heights (a static, complete
  core diagram) and the tick scale fully labelled — the rail
  degrades into the archive's frontispiece. Watchdog: if the
  loop stalls >2000ms, the fill snaps to raw scroll progress
  (unsmoothed but correct) rather than freezing at a wrong
  depth.
- **Reduced-motion variant.** Fill steps at the five band
  thresholds (§4) instead of lerping; bit moves in 100 m
  increments as sections change; the depth is always right,
  it simply arrives in strata rather than as a glide.
- **Performance budget & mobile variant.** Two transforms per
  frame from the shared loop; budget ≤0.15ms/frame. Mobile
  (<768px): the rail becomes a 56px top bar — the tube turns
  horizontal (fill scaleX, bit translateX, ticks every 500 m
  only), pinned above the readout strip (§6.4); the descent
  grammar is unchanged, only its axis rotates.
- **Choreography timeline (v2).** t=0: tube printed, fill at
  p=0, bit at surface → first scroll: loop lerps p toward
  target (0.09/frame) → fill front and bit track ~180ms
  behind the visitor's raw position, settling within 300ms
  of scroll stop → era tick brightens as the front crosses
  its fraction → p=1: bedrock label prints, bit parks →
  scroll up: exact reverse, stamps elsewhere unaffected.
- **State matrix (v2).** *Rest:* at current depth, settled.
  *Hover:* hovering the rail shows the depth at the pointer's
  height as a mono ghost label (a reading, not a control).
  *Focus:* the rail is not focusable; its era ticks are
  mirrored by real links in §6.13's navigation. *Active:*
  n/a. *Scrolled-past:* the rail has no past — it is fixed.
  *Disabled:* n/a. *Touch:* no hover ghost; the readout
  (§6.4) carries the number instead.
- **Breakpoints (v2).** ≥1200px: 96px rail, 64px tube, ticks
  every 100 m, labels every 500 m. 768–1199px: 72px rail,
  48px tube, labels every 1,000 m. <768px: horizontal top
  bar (above), 500 m ticks, era ticks become dots with the
  current era named in the readout.
- **Edge cases & failure modes (v2).** *Short page:* if the
  document's descent is shorter than 300vh, p still maps
  0–1 across it — the maths is positional, not absolute —
  but §1's ruling applies: this theme should not be built
  that short. *Overscroll/bounce:* p clamps 0–1; the bit
  never leaves the tube. *Resize mid-scroll:* rail height
  recomputed in the loop; bit position is a fraction, never
  a stored pixel, so nothing jumps. *Print:* surface state
  (§2) — fill printed at final p as a static band.
- **Accessibility spec (v2).** The rail is `aria-hidden` as a
  visual instrument; its information is duplicated accessibly
  in §6.4's readout, which is a live region in polite mode
  updated at most once per second with the current era name
  and depth (never a per-frame announcement). Era navigation
  for AT and keyboard is §6.13's list, not the rail.
- **Tokens consumed (v2).** `--core-white`, `--glacial`,
  `--ancient`, `--ancient-deep`, `--frost-line`, `--marker`,
  `--ink-frost`, `--loop-lerp`, `--ease-drill`.


### 6.4 Non-linear DEPTH / AGE / CO₂ readout

- **What & why.** A pinned mono block beside the rail printing
  three live figures — DEPTH in metres, AGE in years BP, CO₂
  in ppm — all computed from the loop's lerped `p` by §5's
  published functions. It is the theme's beating heart: the
  visitor *feels* the age–depth curve here, watching AGE crawl
  through centuries near the surface and then tear through
  millennia near the bed, while CO₂ breathes between glacial
  ~190 and interglacial ~280 ppm. The numbers are the article's
  data, updating as you descend through the eras they describe.
- **Structure.** A definition list in JetBrains Mono, pinned
  at the rail's right edge: three label/value rows (DEPTH /
  AGE / CO₂) plus a fourth line naming the current stratum
  ("STRATUM — LAST GLACIAL MAXIMUM") resolved from the record
  at the current depth. Values are text nodes updated by the
  shared loop **only when the rendered string changes**
  (repaint-on-change; at 60fps the depth string changes most
  frames, the CO₂ string rarely). The printed initial values
  in the DOM are the surface figures (0 M / 0 YR BP / 280 PPM).
- **Motion spec.** Trigger: scroll (via the loop). Figures
  follow `depth(p)`, `age(p)`, `co2(p)` exactly — no easing is
  applied to the values themselves beyond the loop's lerp on
  `p`, so the readout's acceleration *is* the p^2.8 curve and
  nothing else. Formatting is fixed: depth as integer metres
  with thousands separators (1,397 M), age as integer years
  (74,000 YR BP), CO₂ as integer ppm. The stratum line changes
  with a 200ms `--ease-settle` fade when a boundary is crossed.
- **States.** Surface (0 / 0 / 280) / descending (values
  running) / settled (scroll stopped: values land on the exact
  figures for the resting p — the lerp always completes, the
  readout never freezes mid-number) / at the bed (3,270 M /
  800,000 YR BP / 195 PPM, stratum line reads "BEDROCK —
  BELOW THIS, NO ICE") / printed (reduced motion / no-JS:
  per-section static values, see below).
- **Content merge.** The readout is not chrome around the
  content; it is the content's instrument. Every era section
  opens with the figures the readout will show at its depth,
  and the tray (§6.5) prints the same figures — the three
  printings (readout, tray, record §6.15) must agree, and the
  gate (§10) checks that they do.
- **Failure fallback.** No-JS: each era section carries its
  own static readout line printed at its head (depth range,
  age range, CO₂ range from the record), so the data survives
  with no loop at all; the pinned block prints surface values
  and is labelled as the surface reading. Loop-stall watchdog
  (§6.3) snaps values to raw progress — unsmoothed, never
  wrong.
- **Reduced-motion variant.** The pinned block updates in
  steps at band thresholds, and each era section's static
  readout line (the no-JS fallback) is shown as well — the
  visitor reads the figures stratum by stratum, as a filed
  table.
- **Performance budget & mobile variant.** Three text writes
  per frame worst case, guarded by repaint-on-change; budget
  ≤0.1ms/frame. Mobile (<768px): the block becomes a one-line
  strip under the horizontal rail (§6.3): "1,397 M · 74,000 YR
  BP · 200 PPM · TOBA ASH", same functions, same figures,
  smaller type (0.75rem mono).
- **Choreography timeline (v2).** t=0: surface figures
  printed → first scroll: depth moves within one frame of
  the lerp → age visibly lags depth's *rate* (the curve, not
  a delay) → boundary crossings fire the stratum line's
  200ms fade and §6.6's ash highlights at 1,112 m and 1,397 m
  → p=1: bed figures land and hold → scroll up: exact
  reverse, figures retracing the curve.
- **State matrix (v2).** *Rest:* settled on exact figures.
  *Hover:* hovering a value underlines it with the frost
  line and shows the function's name in a caption ("AGE =
  800,000 × p^2.8 — §6.15") — the readout cites its own
  maths. *Focus:* values are not focusable; the stratum line
  is mirrored in §6.13's nav for keyboard visitors. *Active:*
  n/a. *Scrolled-past:* n/a (pinned). *Disabled:* n/a.
  *Touch:* no hover caption; the caption text is printed
  permanently under the mobile strip.
- **Breakpoints (v2).** ≥1200px: full three-row block +
  stratum line, values at 1.3rem. 768–1199px: same block,
  values at 1.1rem, stratum line wraps to two lines.
  <768px: the one-line strip (above).
- **Edge cases & failure modes (v2).** *Rounding:* values are
  floored to integers from the exact float; the record's
  printed figures use the same floor, so printings agree to
  the unit. *The 800,000 cap:* p clamps at 1 — AGE can never
  print 800,001. *CO₂ anchors:* interpolation is over age,
  not depth; between anchors the value is a declared model,
  and §6.15 prints the anchors so the model is auditable.
  *Long pages:* none — p is positional.
- **Accessibility spec (v2).** The block is a `<dl>` with real
  terms; a visually-hidden polite live region announces era
  changes only ("Now entering: Toba Ash, 74,000 years BP"),
  throttled to boundary crossings — never per-frame values.
  Contrast: values sit on `--core-pale` chips at every depth
  (the pinned block carries its own ground, so the deepening
  page tint never touches its pairing): `--ink-frost` 12.88:1
  at all depths.
- **Tokens consumed (v2).** `--core-pale`, `--ink-frost`,
  `--frost-line`, `--marker` (bedrock line only), `--ease-
  settle`, `--loop-lerp`.

### 6.5 Core-tray era segments

- **What & why.** Five core segments lying in a shallow
  horizontal tray — Holocene, Last Glacial Maximum, Toba Ash,
  Eemian, Deep Ancient Blue — each a physical miniature of the
  section below it: correct relative length is impossible
  (Toba is a 4 cm band), so each segment instead carries its
  true depth and age range as a printed label, and Toba's
  segment is honestly drawn thin and labelled "A LAYER, NOT
  AN ERA". On hover a segment tilts up like a section lifted
  from its tray; on click, a rotated red SAMPLE CUT tag stamps
  onto it with its depth range. The tray is the page's table
  of contents you can handle.
- **Structure.** A `<nav>` list of five segment cards lying in
  a tray (a `--core-pale` recessed band with a 1px
  `--frost-line` rim and end stops). Each segment is a button
  containing: a mini core graphic (CSS gradient bands at the
  era's own colours, ash line included where true), the era
  name (Fraunces), and its mono label (depth range · age
  range, from the record). Clicking also navigates: the stamp
  lands, then the page smooth-scrolls to the era's stratum
  (the tray is a contents list first, a toy second). The tray
  section pins for 120vh while segments present (below).
- **Motion spec.** Triggers: scroll (presentation), hover
  (lift), click (stamp + go). Presentation: while the tray is
  pinned, segments lift in sequence as scroll crosses the pin
  range — each rises 10px and tilts 4° on its long axis over
  600ms `--ease-lift`, in depth order, 120ms apart in scroll
  progress (scrubbed by the loop, reversible). Hover: the
  same lift, 250ms `--ease-lift`, plus the segment's stratum
  below is named in a caption line. Click: the SAMPLE CUT tag
  (mono, `--marker` border and text on `--core-pale`, rotated
  −5°) stamps in over 240ms `--ease-stamp`, printing
  "SAMPLE CUT — 1,397 M"; the tag persists for the session.
  Then a 900ms smooth scroll to the stratum.
- **States.** Resting (in tray) / presented (lifted by the
  pin sequence) / hovered (lifted + captioned) / sampled
  (tag stamped, permanent for the session) / current (the
  segment whose stratum the reader is inside carries a
  frost-line underline — the tray tracks the descent) /
  disabled: none — all five always work.
- **Content merge.** Each segment *is* its section in
  miniature: same name, same figures, same ash honesty. The
  stamp's depth is the section's depth. A visitor who only
  ever uses the tray has still read the archive's structure
  correctly — that is the test the element sets itself.
- **Failure fallback.** No-JS: segments are plain anchor
  links in a list; no lift, no stamp, full navigation. The
  pin is JS-armed (`position: sticky` enhancement); without
  it the tray is a static band. Watchdog: if the loop stalls,
  segments rest flat and remain clickable — the stamp is a
  class toggle, not a loop citizen, so it can never be
  starved.
- **Reduced-motion variant.** No pin sequence, no tilt: the
  tray is a flat contents band; sampled tags print at rest
  (no stamp impact); navigation is an instant jump.
- **Performance budget & mobile variant.** Five transforms in
  the pin range, from the shared loop; budget ≤0.2ms/frame.
  Mobile (<768px): the tray turns vertical — segments stack
  as five full-width rows (mini core as a left stripe), no
  pin, lift becomes a 4px rise, stamp rotation −3°.
- **Choreography timeline (v2).** Tray enters → pin engages
  → scroll 0–120vh: segments lift in depth order (Holocene
  first — the visitor meets time in the order the drill
  will) → pin releases with all five at rest → hover/click
  grammar takes over → when the reader later descends into
  an era, its segment gains the current underline (the tray,
  if revisited, remembers where you are).
- **State matrix (v2).** *Rest:* flat in tray. *Hover:*
  lift + caption (pointer fine). *Focus:* identical to hover
  (lift + caption), with a 2px `--ink-frost` outline — a
  keyboard visitor gets the same showing. *Active:* stamp
  lands on press, navigation follows on release.
  *Scrolled-past:* if the pin sequence was skipped by a fast
  scroll, segments rest flat (the sequence never plays
  catch-up). *Disabled:* n/a. *Touch:* tap = stamp + go;
  the lift is skipped (no hover to hold it).
- **Breakpoints (v2).** ≥1200px: horizontal tray, segments
  ~200px each, pin 120vh. 768–1199px: horizontal tray,
  segments ~150px, pin 80vh, mono labels at 0.75rem.
  <768px: vertical stack (above), no pin.
- **Edge cases & failure modes (v2).** *Sampled then
  revisited:* tags persist per session only; a fresh visit
  starts with a clean tray (the archive does not keep your
  samples without an account — §6.14 is where a request
  becomes real). *Era renamed in the record:* tray, strata
  and rail ticks all read the record, so one edit renames
  everywhere. *Very long era name:* segment titles clamp to
  two lines with the mono label always fully visible — the
  figures are never the thing truncated.
- **Accessibility spec (v2).** Segments are real `<button>`s
  inside a labelled `<nav>` ("Eras of the core"); each
  button's accessible name includes its figures ("Toba Ash,
  1,397 metres, 74,000 years BP — go to section, stamp a
  sample tag"). The stamp is `aria-hidden`; a polite live
  region announces "Sample cut stamped: Toba Ash, 1,397
  metres." Touch targets: full segment, ≥64px tall on
  mobile rows.
- **Tokens consumed (v2).** `--core-pale`, `--core-white`,
  `--glacial`, `--ancient`, `--ash`, `--marker`, `--ink-
  frost`, `--frost-line`, `--ease-lift`, `--ease-stamp`,
  `--loop-lerp`.

### 6.6 Honest ash layers

- **What & why.** Two volcanic ash layers drawn at their true
  relative depths everywhere the core appears — Campanian
  Ignimbrite (≈39,000 BP) at 1,112 m, above the Toba
  super-eruption layer (≈74,000 BP) at 1,397 m — in the hero
  cylinder (§6.1), the rail (§6.3), the tray (§6.5) and the
  margin column (§6.7), with an on-page honesty note in italic
  Archivo beside the tray: *"Campanian Ignimbrite (≈39,000 BP)
  lies above Toba (≈74,000 BP), because it fell later. The
  core is drawn to the record; the ash is where the ash is."*
  It belongs because it is the theme's credibility made
  visible: the one detail a knowledgeable reader will check,
  gotten right, and signed.
- **Structure.** Ash layers are 3px (hero: 4px) `--ash` bands
  positioned by percentage from the record (1,112/3,270 =
  34.0%; 1,397/3,270 = 42.7%), each with a mono side label
  ("CI ASH — 1,112 M", "TOBA ASH — 1,397 M") on wide screens.
  The honesty note is a real paragraph in the tray section.
  When the drill front (§6.3/§6.4) crosses an ash depth, the
  layer's label and band pulse once (below).
- **Motion spec.** Trigger: scroll — when lerped depth
  crosses 1,112 m or 1,397 m (in either direction, once per
  crossing), the band brightens (`--ash` → `--ink-frost` at
  60% mix) and its label underlines over 400ms `--ease-
  settle`, holding 1200ms before relaxing. That is all. Ash
  does not sparkle, erupt or animate decoratively; a
  74,000-year-old layer is not a celebration.
- **States.** Dormant (drawn, unlabelled emphasis) / crossed
  (the 1600ms highlight) / labelled (≥1200px, labels always
  printed) / printed (reduced motion: labels printed at all
  widths, no highlight pulse — the crossing is announced by
  §6.4's live region instead).
- **Content merge.** The ash layers are data in every object
  that claims to be the core; their highlight is wired to
  the readout's own depth, so the page notices them exactly
  when the visitor's drill arrives. The honesty note turns
  a drawing decision into a stated editorial policy.
- **Failure fallback.** The layers and note are static DOM;
  the highlight is the only scripted part and its absence
  loses nothing. No-JS: layers drawn, labels printed,
  note present.
- **Reduced-motion variant.** No pulse; labels always
  printed; the stratum line in §6.4 names the ash as the
  drill passes.
- **Performance budget & mobile variant.** Two opacity/colour
  transitions on crossing frames only; budget ≈0ms/frame
  steady-state. Mobile: side labels move into §6.4's strip
  (the stratum line names the ash); bands stay at true
  percentages in the horizontal rail.
- **Choreography timeline (v2).** Descent → depth crosses
  1,112 m → CI band + label highlight (400ms in, 1200ms
  hold) → relax → 285 m of ice → depth crosses 1,397 m →
  Toba highlight, same beat → the reader has been shown the
  ordering by the drill itself, in order, once each way.
- **State matrix (v2).** *Rest:* dormant. *Hover:* hovering
  a band (hero/rail) shows its full label as a caption —
  name, depth, age, source eruption. *Focus:* bands are not
  focusable; their data is in the adjacent text and §6.15.
  *Active:* n/a. *Scrolled-past:* dormant again; crossings
  re-arm. *Disabled:* n/a. *Touch:* no hover caption; the
  stratum line carries the name.
- **Breakpoints (v2).** ≥1200px: printed side labels.
  768–1199px: labels on the hero cylinder only; rail bands
  unlabelled (readout names them). <768px: bands in the top
  bar at true percentages; names via §6.4's strip.
- **Edge cases & failure modes (v2).** *A third ash layer
  added to the record:* it draws everywhere automatically —
  positions are record-driven, never hand-placed; the gate
  (§10) fails a build where any core rendering disagrees
  with the record's layer list. *Layers closer than 8px at
  render size:* labels stack with leader lines rather than
  overlapping (does not occur with the declared pair: 285 m
  apart).
- **Accessibility spec (v2).** Bands are `aria-hidden`
  graphics; their full data (name, depth, age, eruption) is
  in the honesty note's section as real text and in §6.15's
  table. The crossing announcement comes through §6.4's
  live region ("Passing Toba Ash, 1,397 metres").
- **Tokens consumed (v2).** `--ash`, `--ink-frost`,
  `--core-pale`, `--ease-settle`, `--loop-lerp`.


### 6.7 Margin stratigraphy column that draws itself

- **What & why.** In the left inset of each era band, an SVG
  column — 56px wide, the era's own height in miniature —
  strokes itself in band by band as the section arrives: the
  era's sub-layers, its ash line if it has one, its boundary
  ticks, drawn with stroke-dashoffset over ~1.2s per section.
  It is a drawn abstract of the text beside it: a visitor
  skimming the page reads the columns and gets the archive's
  shape without reading a word.
- **Structure.** One inline SVG per era section, generated at
  build time from the record: rects for sub-bands (fill =
  band colour at 18% over the section ground), a path outline
  stroked in `--ancient` (or `--core-white` on deep bands),
  ash lines in `--ash` at true in-era fractions, and a mono
  depth label at the column's foot. The draw is driven by an
  IntersectionObserver per column arming a CSS transition on
  stroke-dashoffset; it is not a loop citizen (it plays once,
  forward only).
- **Motion spec.** Trigger: section enters at 30% viewport.
  Bands stroke in top-to-bottom (oldest last — the column
  draws in drilling order), each band's outline over 300ms,
  staggered 120ms, total ≈1.2s `--ease-settle`; fills fade in
  behind their outlines at 40% of each band's stroke. Scroll
  back up: the column stays drawn. It is a summary that has
  been written, not a state that toggles.
- **States.** Undrawn (JS-armed pre-state: outlines at full
  dashoffset, fills at 0 — content around it fully visible) /
  drawing (≈1.2s) / drawn (permanent) / printed (no-JS or
  reduced motion: fully drawn from first paint).
- **Content merge.** The column is generated from the same
  record rows the section's text cites — sub-layer names in
  the drawing match the text's terms, and clicking a column
  band (it is a button on desktop) scrolls to the paragraph
  that discusses that sub-layer. A decorative squiggle could
  not do that; this is an index that happens to be drawn.
- **Failure fallback.** Force-reveal fallback at 4000ms after
  the section first enters: if the transition never ran
  (observer failure, background tab), a watchdog sets the
  column to its drawn state. No-JS: no pre-state is applied —
  columns ship drawn.
- **Reduced-motion variant.** Columns ship drawn; no stroke
  animation. The summary is present, the performance is not.
- **Performance budget & mobile variant.** One transition per
  section, ≤8 path strokes each; budget ≈0ms/frame
  steady-state. Mobile (<768px): the column turns horizontal
  — a 100% × 28px strip above the era heading, same drawing,
  same order.
- **Choreography timeline (v2).** Section crosses 30% →
  band 1 outline (300ms) → fills trail at 40% → bands 2–5
  stagger at 120ms → foot label prints last (200ms fade) →
  drawn; if the section is §6.6's ash-bearing era, its ash
  line draws in `--ash` at its true fraction, mid-sequence.
- **State matrix (v2).** *Rest:* drawn (after first play).
  *Hover:* a band highlights (fill 18%→30%) and names its
  sub-layer in a caption. *Focus:* bands are buttons on
  ≥768px; focus draws a 2px outline in the band's pairing
  colour and shows the same caption. *Active:* press
  scrolls to the sub-layer's paragraph (600ms smooth).
  *Scrolled-past:* drawn. *Disabled:* n/a. *Touch:* bands
  are not buttons <768px (targets too small); the strip is
  a picture there, and the text carries the index.
- **Breakpoints (v2).** ≥1200px: 56px column, labels at
  foot. 768–1199px: 44px column, foot label only (no band
  captions on hover — caption moves under the column).
  <768px: horizontal strip (above), undrawn pre-state
  applies horizontally.
- **Edge cases & failure modes (v2).** *Era with many
  sub-layers (>6):* the column draws the six most
  significant (record's `column: true` flag) and prints
  "+N MORE IN THE RECORD" at its foot — the summary admits
  it is a summary. *Era with none:* the column is a single
  undivided band and says so ("UNIFORM ICE — NO SUB-LAYERS
  LOGGED"). *Section revisited:* never redraws.
- **Accessibility spec (v2).** Each SVG has
  `role="img"` and a `<title>` summarising the era's layers
  in words ("Last Glacial Maximum: five sub-layers, Toba
  ash at its base"). Buttons (≥768px) have accessible names
  per band. The drawing animation is invisible to AT by
  design — the data is in the title and the text.
- **Tokens consumed (v2).** `--ancient`, `--core-white`,
  `--glacial`, `--ash`, `--ink-frost`, `--ease-settle`.

### 6.8 Frost crystals growing at section edges

- **What & why.** Small SVG crystal clusters — six-armed
  dendrites in fine `--frost-line` strokes with
  `--bubble-sheen` fills — that grow at the corners of era
  sections as they enter view, branching over ~2.4s and then
  holding, still, for the rest of the visit. Frost is the
  theme's punctuation: it marks a boundary the way frost
  marks a cold-store door frame, at corners only, never over
  text, never in the reading measure.
- **Structure.** Three pre-drawn SVG cluster variants (6, 9
  and 14 branches), inlined per section corner with a
  per-section rotation from a small declared set (0/90/180/
  270° ± 6°). Growth is a stroke-dashoffset + scale
  transition on branch paths, armed by the same
  IntersectionObserver pattern as §6.7, with the §6.7-style
  4s force-reveal fallback. Clusters are `aria-hidden`,
  `pointer-events: none`, positioned in the band's corner
  padding — outside the content box by construction.
- **Motion spec.** Trigger: section enters at 30%. Primary
  arms stroke in over 900ms; secondary branches stagger at
  150ms intervals `--ease-grow`; tertiary tips fade in last;
  total ≈2.4s, then still forever (no shimmer, no loop —
  frost that twinkles is glitter, and §9 names it). Growth
  is one-shot per section per session.
- **States.** Ungrown (armed pre-state: opacity 0, only
  under the `.js` gate) / growing (≈2.4s) / grown (still) /
  printed (reduced motion / no-JS: fully grown at paint).
- **Content merge.** Crystals grow only where a stratum
  boundary actually is — section edges, tray corners, the
  form sheet's corner (§6.14) — so their placement is the
  page's structure made visible in its own material. They
  carry no data, and the theme is honest about that: they
  are the one purely atmospheric element, rationed to
  corners and capped in size (≤72px) precisely because they
  earn their place by restraint.
- **Failure fallback.** The 4s force-reveal sets grown state
  if the observer or transition fails. No-JS: printed grown.
  A crystal can never cover content: it lives in padding,
  behind the content's stacking context.
- **Reduced-motion variant.** Printed grown, still. (Not
  removed — the variant is the same page with the
  performance removed, and a bare corner would read as a
  printing error.)
- **Performance budget & mobile variant.** ≤14 paths per
  cluster, one transition per section; budget ≈0ms/frame.
  Mobile (<768px): one cluster per section (top-left
  corner), 6-branch variant, ≤48px.
- **Choreography timeline (v2).** Section crosses 30% →
  §6.7's column begins (t=0) → crystals start at t=300ms
  (after the column has established the section) → arms
  900ms → branches stagger to ≈2.1s → tips fade → still by
  ≈2.7s, as the reader's eye reaches the text.
- **State matrix (v2).** *Rest:* grown, still. *Hover:*
  none — crystals are not interactive and do not react
  (reacting frost would be a toy). *Focus:* n/a (not
  focusable). *Active:* n/a. *Scrolled-past:* grown.
  *Disabled:* n/a. *Touch:* identical; no tap behaviour.
- **Breakpoints (v2).** ≥1200px: two clusters per section
  (top-left, bottom-right), ≤72px. 768–1199px: one cluster,
  ≤56px. <768px: one 6-branch cluster, ≤48px.
- **Edge cases & failure modes (v2).** *Short sections:*
  if a band is under 40vh, its crystals shrink to the
  6-branch variant rather than crowding the text.
  *Deep bands:* on `--ancient` grounds the strokes switch
  to `--glacial` at 60% (the pairing is declared, not
  improvised). *Many sections:* clusters reuse the three
  variants in rotation; two adjacent sections never share
  a variant + rotation pair.
- **Accessibility spec (v2).** Fully decorative and marked
  so (`aria-hidden="true"`, no title). No information,
  focus or contrast obligation attaches; on deep bands the
  stroke colour keeps ≥3:1 against its ground as a graphic,
  per §2's graphic ruling.
- **Tokens consumed (v2).** `--frost-line`, `--bubble-
  sheen`, `--glacial`, `--ease-grow`.

### 6.9 Core-light hover with bubble clustering

- **What & why.** Hovering the hero core (§6.1) lights a
  soft glow inside the ice at the pointer's height — a
  radial pool, warm only in brightness (this ice has no
  warm colour; the light is `--bubble-sheen` at low alpha)
  — and the bubbles nearest the light drift toward it and
  slow, the way a scientist holds a core section up to the
  lamp and the trapped air seems to gather. It invites
  inspection of the hero's bands: as the light moves, the
  band under it is named in a caption beside the cylinder.
- **Structure.** A radial-gradient div inside the cylinder,
  clipped to the tube, translated by the shared loop toward
  the pointer's y (x is fixed at the tube's centre — the
  lamp moves along the core, not around it). The canvas
  bubble sim (§6.1) receives the light's y and radius
  (90px): bubbles within it gain a gentle attraction term
  (≤4 px/s²) and a 20% speed cut. The band caption is a DOM
  element reading the record at the light's depth fraction.
- **Motion spec.** Trigger: pointer hover (fine pointers
  only). Light fades in over 300ms `--ease-settle`; follows
  pointer y lerped at 0.18 (snappier than the descent lerp —
  a hand is quicker than a drill); fades out 400ms after
  the pointer leaves. Caption updates on band change only.
  Clustering is physics inside §6.1's existing sim — no new
  loop, no new canvas.
- **States.** Unlit (no hover) / lit (light tracking) /
  clustering (bubbles gathered — a consequence, not a
  separate mode) / off (touch, reduced motion, hero
  off-screen).
- **Content merge.** The light's caption names real bands
  with real depths — hovering the Toba level reads "TOBA
  ASH — 1,397 M · 74,000 YR BP". The interaction teaches the
  cylinder's scale; it is a reading lamp, not a spotlight
  effect, and it works only because the bands are data.
- **Failure fallback.** Pure enhancement: no hover, no
  light, nothing lost — bands are labelled statically
  (§6.1) regardless. If the canvas is absent (SVG fallback),
  the light still works and the static bubbles simply do
  not cluster; the caption still names bands.
- **Reduced-motion variant.** No light, no clustering. The
  band caption is printed as a static list beside the
  cylinder (it already is, in the no-JS state).
- **Performance budget & mobile variant.** One gradient
  transform + a bounded force term on ≤46 bubbles; budget
  ≤0.15ms/frame while hovering. Mobile/touch: element is
  absent — tapping the cylinder does nothing, by design
  (§6.1's state matrix); the tray is the touch instrument.
- **Choreography timeline (v2).** Pointer enters → light
  fades in at pointer height (300ms) → bubbles within 90px
  begin drifting in over ~1s → caption names the band →
  pointer moves: light tracks at lerp 0.18, cluster
  reforms at the new height → pointer leaves: cluster
  disperses into the ambient rise over ~2s, light fades
  (400ms).
- **State matrix (v2).** *Rest:* unlit. *Hover:* lit, as
  specified. *Focus:* keyboard focus on the cylinder's
  band list (§6.1) lights the focused band at its height
  — keyboard visitors get the lamp too. *Active:* n/a.
  *Scrolled-past:* hero logic unregisters the hover.
  *Disabled:* n/a. *Touch:* absent (above).
- **Breakpoints (v2).** ≥1200px: full effect, radius 90px.
  768–1199px: radius 70px, caption below the cylinder.
  <768px: absent (touch-first layout; coarse pointers
  never arm it at any width).
- **Edge cases & failure modes (v2).** *Pointer races up
  and down:* the lerp caps the light's speed; bubbles
  never teleport (forces are bounded). *Pointer leaves
  mid-cluster:* dispersal is the ambient sim resuming —
  no state to clean up. *prefers-reduced-data:* light
  works, clustering off (fewer physics terms, same lamp).
- **Accessibility spec (v2).** The light is `aria-hidden`;
  the caption it drives is a real text element whose
  content (band names + depths) duplicates the static band
  labels. Focus behaviour (above) keeps the feature
  available without a pointer. No contrast obligation:
  the light never sits under body text.
- **Tokens consumed (v2).** `--bubble-sheen`, `--glacial`,
  `--ink-frost`, `--core-pale`, `--ease-settle`,
  `--loop-lerp`.


### 6.10 Patrolling polar bear on the surface ridge

- **What & why.** At the foot of the hero, a snow ridge runs
  the width of the page, and a flat-silhouette polar bear
  ambles across it on a real walk cycle — diagonal leg pairs,
  body bob, head nod — pausing twice per crossing to raise
  its head and sniff the wind. A mono caption under the ridge
  reads, verbatim: "THE SURFACE · 0 YR BP · PATROLLED
  DAILY". The bear belongs because it lives on the one
  stratum the reader is standing in: the present day, the
  top of the core, the surface the drill left from. It is
  the page's only living thing, and it is alive at 0 metres.
- **Structure.** One inline SVG bear (body, four legs as two
  diagonal pairs, head group), ~180px long on desktop,
  filled `--core-pale` with a `--glacial` shadow side —
  against the hero's white ridge it reads as a white animal
  on snow, outlined by a 1px `--frost-line` contour. The
  walk is keyframed transforms on the leg groups (rotate
  ±14° at the shoulder/hip pivots) plus a body bob
  (translateY 0→2px) and head nod, all CSS keyframes on a
  1.6s gait cycle; the crossing itself is a transform on
  the bear group driven by the shared loop over a ~48s
  round (walk 20s → sniff pause 4s → walk 16s → sniff 4s →
  turn and return). The ridge is a DOM snow band with a
  soft top edge (SVG path).
- **Motion spec.** Trigger: time, ambient, hero visible
  only. Gait: legs swing at 1.6s/cycle, bob synced at half
  period, head nod at quarter. Sniff: head raises 8° over
  600ms `--ease-settle`, holds 3.4s with two small nostril-
  height twitches, lowers over 600ms. Turn at the ridge's
  end: the bear flips (scaleX −1) over 400ms with a planted
  paw beat — no sliding. Speed: ~9px/s. It never hurries,
  never runs, and never acknowledges the visitor.
- **States.** Walking / sniffing / turning / standing
  (reduced motion: mid-ridge, head up, still) / absent
  (hero off-screen: the round pauses mid-stride and resumes
  in phase — the bear does not teleport).
- **Content merge.** The caption is data: the surface, 0 yr
  BP, is the core's top boundary in the record (§6.15), and
  the bear patrols exactly that boundary across the hero's
  foot — the same line the rail's bit starts from. Remove
  the record and the caption is a joke; with it, the bear
  is a scale marker with a heartbeat.
- **Failure fallback.** Pure enhancement over a printed
  ridge and caption: no-JS shows the bear standing at the
  ridge's centre (its reduced-motion pose) with the caption
  beneath. A stalled loop leaves a standing bear, never a
  broken one.
- **Reduced-motion variant.** Standing at centre, head up
  (the sniff pose, held). The caption prints unchanged.
- **Performance budget & mobile variant.** CSS keyframes on
  one SVG group + one loop transform; budget ≤0.1ms/frame.
  Mobile (<768px): bear at 120px, round shortened to ~36s,
  one sniff pause instead of two (screen width is the
  territory; the bear patrols what exists).
- **Choreography timeline (v2).** Hero paints → bear
  standing at left third → t=800ms: first stride → walk
  20s (gait 1.6s × 12.5 cycles) → sniff (0.6s up, 3.4s
  hold, 0.6s down) → walk 16s → sniff → ridge end: turn
  (400ms) → return leg mirrors the round → loop. The first
  sniff lands at ≈t=21s — after §6.2's drill has finished,
  so the hero's two performances never compete.
- **State matrix (v2).** *Rest:* mid-round phase. *Hover:*
  none — the bear ignores the pointer entirely (a bear
  that reacts to a cursor is a pet, §9). *Focus:* not
  focusable. *Active:* n/a. *Scrolled-past:* round paused
  in phase. *Disabled:* n/a. *Touch:* identical; no tap
  behaviour.
- **Breakpoints (v2).** ≥1200px: 180px bear, full round.
  768–1199px: 150px bear, round ~44s. <768px: 120px bear,
  ~36s round, one sniff.
- **Edge cases & failure modes (v2).** *Narrow ridge
  (<500px):* the round compresses proportionally; gait
  cycle never speeds up (a small territory is patrolled
  more often, not faster). *Tab hidden mid-sniff:* CSS
  animations pause with the document; the loop's crossing
  transform is phase-based, so the bear resumes mid-pose.
  *Hero very wide (>1600px):* crossing caps at 1600px of
  travel centred on the ridge; the bear does not patrol
  empty margin.
- **Accessibility spec (v2).** The bear is `aria-hidden`;
  the caption is real text and carries the meaning (the
  surface stratum, patrolled). No information is in the
  animation. The ridge area keeps text contrast by keeping
  text off it — the caption sits below on the page ground.
- **Tokens consumed (v2).** `--core-pale`, `--glacial`,
  `--frost-line`, `--ink-frost`, `--ease-settle`,
  `--loop-lerp`.

### 6.11 Paw-print trail down the margin

- **What & why.** Twelve bear paw prints — one main pad,
  four toe pads, the theme's smallest drawn object — run
  down the right snow margin in a walking alternation (left,
  right, offset by half a stride). Each print presses in
  (scale 1.15→1 + opacity, like a pad settling into snow)
  as the smoothed drill depth passes the print's declared
  depth, and lifts again if the visitor scrolls back up.
  The trail is a second, quieter progress track: the
  instrument (§6.3) tells you the depth; the trail tells
  you something alive has been descending with you.
- **Structure.** Twelve inline SVG prints positioned
  absolutely in the right margin at declared fractions of
  the descent (print n at p = n/13, so the twelfth presses
  at p ≈ 0.923, just above the bed). Each print is a group
  of five ellipses filled `--glacial` at 55% on the surface,
  deepening toward `--ancient` at 70% as the page's own tint
  deepens (the prints are in the margin snow, and the snow
  darkens with the page — §4's thresholds restyle them).
  Press state is a class toggled by the shared loop when
  lerped p crosses the print's fraction.
- **Motion spec.** Trigger: scroll, via the loop. Press:
  500ms `--ease-grow`, scale 1.15→1.0, opacity 0.25→1,
  with a 60ms stagger between the toe pads and the main
  pad (toes land first, as they do). Lift (scroll up past
  the fraction): reverse over 400ms. Prints never animate
  in sequence on load — they respond only to the drill.
- **States.** Unpressed (faint, 0.25 opacity — a print in
  old snow) / pressing (500ms) / pressed (full) / lifting
  (reverse) / printed (reduced motion: all prints below
  the current band threshold shown pressed, stepped).
- **Content merge.** The trail's prints are spaced by the
  descent itself (n/13 of the whole core), so the margin
  is a second scale — a visitor can estimate depth from
  the prints alone to within ~270 m, and the estimate
  agrees with the readout because both read the same p.
  Playful, yes; arbitrary, no.
- **Failure fallback.** No-JS: all twelve prints print at
  0.55 opacity — a complete trail down a static page, the
  way a field guide would draw it. Loop stall: prints hold
  their last correct states (they are threshold classes,
  recomputed whenever the loop runs).
- **Reduced-motion variant.** Prints step between pressed
  and unpressed at band thresholds with no press
  animation; the trail still tracks depth.
- **Performance budget & mobile variant.** Twelve class
  toggles + short transitions; budget ≈0ms/frame
  steady-state. Mobile (<768px): the margin does not
  exist — the trail is **cut entirely** rather than shrunk
  (a 20px margin print is a smudge). The readout carries
  progress alone on small screens, and §14 lists the trail
  as the mobile build's declared omission.
- **Choreography timeline (v2).** Descent: p crosses 1/13
  → print 1 presses (toes t=0, pad t=60ms, settled
  t=500ms) → … → p crosses 12/13 → print 12 presses → the
  bed: the trail ends one print short of the bottom — the
  bear does not go below the ice, and the missing
  thirteenth print is the surface's signature on the
  design. Ascent: prints lift in reverse order.
- **State matrix (v2).** *Rest:* pressed set = all prints
  above current depth. *Hover:* hovering a print shows its
  depth as a mono caption ("PRINT 7 — ≈1,760 M") — the
  trail answers when asked. *Focus:* prints are not
  focusable (the caption data duplicates §6.4). *Active:*
  n/a. *Scrolled-past:* prints above stay pressed — the
  trail records where the drill has been *this visit's
  current position*, lifting only when the drill rises
  above them. *Disabled:* n/a. *Touch:* no hover caption.
- **Breakpoints (v2).** ≥1200px: full trail, prints 34px.
  768–1199px: trail in a narrowed margin, prints 26px,
  captions off (margin too narrow to hold them).
  <768px: cut (above).
- **Edge cases & failure modes (v2).** *Fast scroll to the
  bed:* prints press in a rapid cascade (each still gets
  its 500ms, overlapping) — the loop toggles classes by
  threshold, so a jump-scroll settles all twelve correctly
  within one frame plus transitions. *Content shorter
  than expected:* fractions are of the descent, not of
  pixels, so the trail compresses with the page and still
  ends at 12/13.
- **Accessibility spec (v2).** `aria-hidden` as a set; the
  trail's information (current depth) is §6.4's job,
  announced properly there. Print contrast against the
  margin ground is graphic-level (≥3:1 at pressed state
  in every band, via the band restyling above).
- **Tokens consumed (v2).** `--glacial`, `--ancient`,
  `--core-white`, `--ease-grow`, `--loop-lerp`.

### 6.12 Field-camp scene with mother bear and cub

- **What & why.** Between the tray and the deep strata, a
  full-width drawn scene: the field camp on the surface —
  two tents, fuel drums, the drill tower with a fluttering
  marker-red flag, katabatic wind streaks sliding downhill,
  and at the ridge behind camp, a mother bear standing
  watch while her cub periodically rears up over the ridge
  line, looks, and drops back. Beside the scene, real camp
  facts count up as it enters: altitude 3,233 m; polar
  night 100 days; winterover crew 16; mean annual
  temperature −54.5 °C. It is the page's human stratum: the
  section about the people who drill, drawn at the surface
  they live on, with the bears sharing their world rather
  than decorating it.
- **Structure.** One inline SVG scene (~1100×340 viewBox):
  ridge path, camp group (tents as triangles with guy-line
  strokes, drums as rounded rects, tower as a lattice of
  lines with the flag as a small `--marker` path), wind
  streaks (six dashed paths), mother bear silhouette
  standing at the ridge (static pose, head group on a slow
  sway), cub group behind the ridge line, translated down
  (hidden) except during its rear-up. Facts are a DOM list
  beside the scene with mono values; the count-up is run
  by the shared loop's one-shot registry (not a per-element
  timer).
- **Motion spec.** Triggers: scroll into view (facts +
  scene start) + ambient while visible. Facts count up
  over 1400ms `--ease-drill`, staggered 150ms, landing
  exactly on the printed figures (which are in the DOM
  from first paint). Flag flutters: rotate/skew keyframes
  on a 0.9s cycle with irregular amplitude (two nested
  keyframe sets, 0.9s and 1.7s, beating against each other
  — a flag in gusty wind, not a metronome). Wind streaks
  dash-offset slide at 60–90px/s, staggered, fading at the
  ridge's foot. Cub: every ~14s (phase-offset per load by
  the record's seed, so it is not a metronome either), the
  cub rears: translateY −34px over 700ms `--ease-grow`,
  holds 2.2s with a head tilt, drops over 500ms.
  Mother's head sways ±2° on a 7s cycle. All of it pauses
  when the scene is off-screen.
- **States.** Approaching (facts uncounted, scene still) /
  alive (facts counted, flag/wind/cub cycling) / past
  (scrolled beyond: animations pause, facts stay at their
  figures) / printed (reduced motion: scene drawn complete,
  cub up, facts at final figures).
- **Content merge.** Every drawn object is in the section's
  text: the tower is the drill that made the core, the
  drums are the fuel the text prices, the flag is the
  camp's marker the logistics paragraph describes. The
  facts list is the section's data table wearing the scene
  as its illustration — remove the text and the scene is a
  poster; with it, the scene is a figure in a paper.
- **Failure fallback.** No-JS: the complete scene prints
  (cub up, flag at rest angle), facts at final figures.
  Loop stall: facts have a 2500ms watchdog that prints
  final values; the scene's CSS keyframes (flag) are
  independent of the loop and cannot be starved.
- **Reduced-motion variant.** Scene printed complete and
  still: cub up over the ridge, flag at a fixed angle,
  no wind streaks (drawn at rest opacity 0.18), facts
  printed. The section loses motion, not content.
- **Performance budget & mobile variant.** One SVG (~40
  paths), CSS keyframes, one count-up registry entry;
  budget ≤0.3ms/frame while visible. Mobile (<768px):
  the scene crops to its centre 60% (camp + mother,
  viewBox reframed), the cub is cut (its ridge is outside
  the crop — §14's declared mobile omission, stated
  here), facts stack above the scene in two columns.
- **Choreography timeline (v2).** Section crosses 30% →
  fact 1 counts (1400ms) → facts 2–4 stagger at 150ms →
  flag and wind already alive from 10% visibility → cub's
  first rear-up at ≈t=6s after entry (never during the
  count-ups — the scene introduces its actors in order:
  place, facts, wildlife) → cycle continues while visible.
- **State matrix (v2).** *Rest:* alive cycle (when
  visible). *Hover:* hovering the tower highlights the
  logistics paragraph's first line (a frost-line underline
  draws, 300ms) — scene and text point at each other.
  *Focus:* the scene is not focusable; facts are text.
  *Active:* n/a. *Scrolled-past:* paused, facts final.
  *Disabled:* n/a. *Touch:* no hover link; identical
  ambient cycle.
- **Breakpoints (v2).** ≥1200px: full scene + facts at
  right. 768–1199px: scene full width, facts in a row of
  four beneath it. <768px: centre crop, facts 2×2 above,
  cub cut.
- **Edge cases & failure modes (v2).** *Facts edited in
  the record:* scene labels and count-up targets both
  read the record — one edit updates the drawing's
  caption data and the list. *Scene revisited:* facts
  never recount (counted is a permanent state, like a
  stamp). *Very slow device:* wind streaks are the first
  cut (§14's order applies inside the element too).
- **Accessibility spec (v2).** The SVG is `role="img"`
  with a `<title>` and `<desc>` naming the camp's contents
  and the bears ("Field camp: two tents, fuel drums, drill
  tower with a red flag; a mother polar bear and cub at
  the ridge"). Facts are a real `<dl>`. The cub's motion
  is ambient and unannounced.
- **Tokens consumed (v2).** `--core-pale`, `--glacial`,
  `--ancient`, `--ash`, `--marker`, `--ink-frost`,
  `--frost-line`, `--ease-drill`, `--ease-grow`,
  `--loop-lerp`.


### 6.13 Rail masthead & era navigation

- **What & why.** The site's navigation lives where an
  expedition keeps its manifest: at the surface. A masthead
  at the page top carries the programme name in Fraunces
  ("CONCORDIA DEEP CORE PROGRAMME" in the reference build),
  and beneath it the era navigation — a horizontal list of
  the five strata plus Camp, Record and Sample — each item
  labelled with its depth ("TRAY · SURFACE", "HOLOCENE ·
  0–723 M", "RECORD · ALL DEPTHS"). As the visitor descends,
  the nav item for the current stratum gains a frost-line
  underline and its depth range; the nav itself scrolls away
  after the hero (the surface is behind you now) and is
  replaced in the rail head by a compact "SURFACE ↑" return
  link beside the readout. Navigation that knows your depth
  is the theme's wayfinding; a generic top bar would not.
- **Structure.** A `<header>` with the wordmark and a
  `<nav>` list of anchor links to section IDs; current-state
  is driven by the loop's stratum resolution (§6.4's record
  lookup), toggling `aria-current` and the underline class.
  The rail-head return link is a fixed element that fades in
  once p > 0.04. All links are plain anchors — navigation
  works with no script; the script only adds the *knowing*.
- **Motion spec.** Trigger: scroll (stratum changes).
  Underline draws over 300ms `--ease-settle` (scaleX 0→1,
  origin left). Return link fades in 400ms when the surface
  is left, out when regained. Anchor jumps use the theme's
  smooth scroll (900ms, §6.5's go behaviour) with the loop's
  lerp following — the drill travels, it does not teleport,
  unless reduced motion or the visitor's own find-in-page
  says otherwise.
- **States.** At surface (nav visible, no current item —
  or "SURFACE" current) / descending (current item tracks
  strata) / deep (nav long gone; return link present) /
  returning (jump in flight).
- **Content merge.** Nav labels carry depths from the
  record, so the menu is a miniature of the archive's
  structure — a visitor who reads only the nav has the
  era order and depths right. The current-item tracking
  makes the menu a second readout, in words.
- **Failure fallback.** No-JS: a plain, complete nav; no
  current-state (nothing claims to know your depth without
  the instrument running), return link printed from the
  start. Loop stall: current-state freezes at the last
  true stratum — wrong by at most one boundary, and the
  §6.3 watchdog's snap corrects it.
- **Reduced-motion variant.** Jumps are instant; underline
  appears without drawing; return link appears without
  fading.
- **Performance budget & mobile variant.** Class toggles on
  boundary crossings only; ≈0ms/frame. Mobile (<768px):
  the nav becomes a horizontally scrollable strip under
  the masthead (depth labels kept — they are the point),
  and the rail-head return link sits in §6.4's strip.
- **Choreography timeline (v2).** Load: masthead printed,
  drill line (§6.2) runs beneath it → first scroll: nav
  scrolls off with the page, return link fades in at
  p=0.04 → each boundary: underline leaves the old item
  (150ms) and draws under the new (300ms) in the same beat
  as §6.4's stratum line → jump from tray/nav: drill
  travels, current item settles on arrival.
- **State matrix (v2).** *Rest:* current item = current
  stratum. *Hover:* item's depth label brightens
  (`--ash` → `--ink-frost`). *Focus:* 2px `--ink-frost`
  outline (light bands) / `--core-white` outline (deep
  bands) — the header sits on the page ground, which
  deepens, so the focus pairing follows §4's thresholds.
  *Active:* press begins the smooth travel. *Scrolled-
  past:* n/a (the header is the past). *Disabled:* n/a.
  *Touch:* tap = travel; no hover brightening.
- **Breakpoints (v2).** ≥1200px: full labels with depths.
  768–1199px: era names + depths at 0.75rem mono.
  <768px: scrollable strip, names only on the current
  item, depths on all (depths are never the thing cut).
- **Edge cases & failure modes (v2).** *More than five
  strata (a longer archive):* nav items wrap to a second
  row at the surface; the strip scrolls on mobile. The
  theme caps declared strata at eight — beyond that the
  tray (§6.5) becomes the primary index and the nav lists
  sections, not strata. *Section renamed:* record-driven,
  renames propagate.
- **Accessibility spec (v2).** Real `<nav>` with an
  aria-label ("Strata of the core"); `aria-current="true"`
  on the current item, updated on boundary crossings only.
  Focus order is DOM order. The return link's text is
  "Back to the surface" (visually "SURFACE ↑").
- **Tokens consumed (v2).** `--ink-frost`, `--core-white`,
  `--ash`, `--frost-line`, `--ease-settle`, `--loop-lerp`.

### 6.14 Sample-request form & its stamped cut receipt

- **What & why.** The theme's one conversion surface: a
  researcher requests a physical section of the core. The
  form is a sheet from the cold-store logbook — fields for
  name, institution, the requested depth interval (two mono
  number fields, FROM / TO, in metres), and purpose — set
  on `--core-pale` at the depth where the page's descent
  ends, because you ask for ice after you have seen what
  the ice holds. On submit, the form does not show a toast:
  a SAMPLE CUT tag stamps onto the sheet (§6.5's stamp,
  grown up) reading "CUT REQUEST № 97 — LOGGED", the
  number derived from the season's printed cut count (96
  cuts logged, §6.15), and a logbook line is added beneath
  the form in mono: the interval, the requester, the
  station season. Asking for a piece of 74,000-year-old ice
  should feel like an entry in a book that outlives you,
  because it is.
- **Structure.** A real `<form>` (posts to the site's
  endpoint; fully functional without JS) with labelled
  inputs styled as logbook lines (borderless on a printed
  `--frost-line` rule; focus = double rule). Depth fields
  are `inputmode="numeric"` mono. Validation is in the
  archive's voice (§12): errors print as ash-grey notes
  under the field — never red (§2's ruling). On JS submit,
  the stamp element and logbook line are inserted; the
  form's fields freeze (disabled) with values intact —
  the entry is written, not cleared.
- **Motion spec.** Trigger: submit. Stamp: scale 1.6→1,
  opacity 0→1, rotate −5°, 240ms `--ease-stamp`, landing
  across the sheet's corner. Logbook line types in as a
  fade + 8px rise, 500ms `--ease-settle`, at t=300ms.
  Field errors (validation) print with the same rise,
  300ms. Nothing else moves; a logbook does not celebrate.
- **States.** Blank (printed sheet, cut count shown: "96
  CUTS LOGGED THIS SEASON") / filling (focus rules double)
  / invalid (ash notes under fields, values kept) /
  logged (stamped, frozen, receipt line printed) /
  submitting (button text becomes "LOGGING…" for the
  request's duration — the one place the theme permits an
  ellipsis).
- **Content merge.** The form's depth fields validate
  against the record itself: intervals must lie within
  0–3,270 m, FROM above TO (shallower first — the form
  teaches the archive's direction), and requesting an ash
  interval (within ±2 m of 1,112 or 1,397 m) prints a
  note, not an error: "This interval contains the Toba
  ash layer. The curators will write to you." The form
  knows the core because it reads the same record.
- **Failure fallback.** No-JS: the form posts normally and
  the server returns the logged page with the receipt
  printed (same words, same number logic server-side).
  JS submit failure (network): an ash note — "The request
  did not reach the logbook. Nothing was logged; try
  again." — and the fields stay live. A request is never
  shown as logged when it was not.
- **Reduced-motion variant.** Stamp prints at rest (no
  impact), receipt line appears without rising. The
  *fact* of the stamp is the content; its landing is the
  performance.
- **Performance budget & mobile variant.** One stamp
  transition + one line insertion on submit only;
  ≈0ms/frame. Mobile (<768px): the sheet goes full-width,
  depth fields stack, stamp rotates −3° and scales to fit
  the sheet's corner without covering the receipt line.
- **Choreography timeline (v2).** Submit pressed → fields
  validate (ash notes if needed, no stamp) → request sent,
  button "LOGGING…" → success: stamp lands (240ms) →
  receipt line rises (t=300ms, 500ms) → fields freeze →
  the page's cut count, wherever printed (§6.15's record
  display, the footer §6.17), now reads 97 — one number,
  updated everywhere, because it was always one record.
- **State matrix (v2).** *Rest:* blank sheet. *Hover:*
  submit button's frost-line underline draws (140ms).
  *Focus:* double rule on the field + its label bolds;
  focus order = visual order. *Active:* button presses
  1px. *Scrolled-past:* n/a. *Disabled:* after logging,
  fields disable with values visible (a written entry is
  read-only). *Touch:* identical; targets ≥48px.
- **Breakpoints (v2).** ≥1200px: two-column sheet (fields
  left, the season's cut log right). 768–1199px: single
  column, cut log below. <768px: stacked (above).
- **Edge cases & failure modes (v2).** *Interval across
  an era boundary:* legal and unremarked — cores are cut
  where science needs them. *Interval already requested
  this session:* the receipt notes "SECOND REQUEST THIS
  SESSION — LOGGED AS № 98" — the logbook counts honestly
  rather than deduplicating silently. *Depths entered as
  ages:* the fields are labelled in metres twice (label +
  unit inside the rule) and an out-of-range value gets
  the ash note "Depths here are in metres, 0–3,270."
- **Accessibility spec (v2).** Every field has a real
  `<label>`; errors are linked with `aria-describedby`
  and announced via a polite live region on submit; the
  stamp is `aria-hidden`, the receipt line is the
  accessible confirmation ("Cut request number 97 logged:
  1,390 to 1,405 metres."). Focus moves to the receipt
  line's heading after logging.
- **Tokens consumed (v2).** `--core-pale`, `--core-white`,
  `--ink-frost`, `--ash`, `--marker`, `--frost-line`,
  `--ease-stamp`, `--ease-settle`.

### 6.15 The core record — the one declared data source

- **What & why.** Not a visual element but the element
  every other element obeys: a single declared record —
  in the build, one JSON block (or data table) in the
  page's source and printed in full on the Record page —
  holding the total depth (3,270 m), the total span
  (800,000 yr), the age function, the CO₂ anchors, the
  five strata with their depth/age ranges, the two ash
  layers, the camp facts, the cut count (96) and the
  fixed strings. The theme's law (§0) is enforceable only
  because this record exists: every figure in §§6.1–6.14
  cites it, and §10's gate recomputes the page from it.
  On the Record page it is presented as the archive's own
  table: strata, layers, anchors, facts — the page behind
  the page, published.
- **Structure.** Build-time: one `core-record.json`
  consumed by the templates that render the hero bands,
  rail ticks, tray, strata, column SVGs and readouts — no
  figure is hand-typed in markup. Runtime: the loop reads
  the same record (inlined, ≤4KB) for stratum resolution
  and CO₂ interpolation. The Record page renders it as
  mono tables with Fraunces headings.
- **Motion spec.** None of its own — the record does not
  move; everything else moves *by* it. (Its one dynamic
  behaviour: the cut count increments on §6.14's logging,
  propagated from the single runtime copy.)
- **States.** Declared (build) / published (Record page) /
  incremented (cut count after a request) — no other
  states exist; a record with moods is not a record.
- **Content merge.** Total: the record *is* the content,
  and the theme's entire claim to honesty rests on there
  being exactly one of it. Two spreadsheets, one for the
  tray and one for the readout, would be the theme's
  original sin (§9).
- **Failure fallback.** If the runtime copy fails to load,
  the static build-time renderings (which are complete)
  stand, the loop degrades to the §6.3 watchdog behaviour,
  and the readout prints per-section static values (§6.4's
  fallback). The page never invents a figure to fill a
  gap; it prints the last true one or the section's range.
- **Reduced-motion variant.** Identical — the record is
  beneath the motion layer entirely.
- **Performance budget & mobile variant.** ≤4KB inlined;
  parsing is build-time. Mobile: identical record; only
  its presentations shrink.
- **Choreography timeline (v2).** Build: record → all
  renderings → gate recomputation (§10) → ship. Runtime:
  load → loop registers record → every beat in §13 reads
  from it → a §6.14 logging increments the count → all
  printings of the count agree from that frame onward.
- **State matrix (v2).** *Rest:* declared. *Hover / focus
  / active:* n/a (it is data, not a control); on the
  Record page its tables are ordinary text. *Scrolled-
  past:* n/a. *Disabled:* n/a. *Touch:* n/a.
- **Breakpoints (v2).** The record is breakpoint-invariant;
  the Record page's tables scroll horizontally under
  768px rather than truncating a figure.
- **Edge cases & failure modes (v2).** *A stratum added:*
  tray, rail, nav, columns and readout all gain it from
  the one edit; the gate recounts. *An anchor changed:*
  CO₂ printings change everywhere at once — the gate's
  three-printings check (§10) exists precisely to catch a
  build where they did not. *Record missing a field:* the
  build fails loudly at build time; a half-record never
  ships.
- **Accessibility spec (v2).** On the Record page, tables
  use real `<th>` scope, figures are text, and the age
  function is printed in words as well as symbols ("age
  equals 800,000 times the depth fraction raised to the
  power 2.8").
- **Tokens consumed (v2).** None directly; it *declares*
  the values other elements' tokens frame. (Listed for
  completeness: its printings use `--ink-frost`,
  `--core-pale`, `--frost-line`.)


### 6.16 Un-drilled skeleton & the thaw page transition

- **What & why.** Loading, in this theme, is ice not yet
  raised: while a page or a heavy section (the camp scene's
  SVG, the Record tables) is fetched, its area prints as an
  un-drilled core — a `--core-white` tube outline ruled
  with faint 100 m ticks, empty strata bands in
  `--core-pale`, and a mono note: "CORE NOT YET RAISED".
  Page changes are a thaw: a frost glaze (a `--bubble-
  sheen` gradient at 22% with a `--frost-line` edge) sweeps
  down the viewport like a breath fogging and clearing on
  cold glass, the content swaps at the glaze's peak, and
  the new page settles clear. Both are the theme's honesty
  about waiting: the archive does not shimmer; it states
  what has not arrived yet.
- **Structure.** Skeleton: static DOM shells with reserved
  heights (the real sections' heights, so CLS stays at
  zero), tick rules drawn in CSS gradients. Transition: a
  fixed full-viewport glaze div, `pointer-events: none`,
  translated from −100% to 100% on the y axis; the swap is
  timed to its 50% point. Both are enhancements over a
  server-rendered page — the skeleton appears only for
  client-fetched fragments, never as a gate on first
  paint.
- **Motion spec.** Skeleton: no animation at all (a still
  tube; motion would claim drilling that is not
  happening). A hard ceiling of 2000ms: a watchdog swaps
  in whatever content has arrived, or an ash note ("THIS
  SECTION IS STILL ON THE SURFACE — RELOAD TO RAISE IT")
  if none has. Thaw: sweep 320ms `--ease-settle` (160ms
  down-fog, swap, 160ms clear), aborted at 1400ms by
  watchdog — if the new content is not ready at the
  glaze's peak, the glaze clears anyway and the skeleton
  grammar takes over in place.
- **States.** Skeleton: waiting / raised (content swapped
  in with a 300ms `--ease-settle` settle) / failed (ash
  note, ceiling reached). Transition: idle / fogging /
  swapping / clearing / aborted (watchdog).
- **Content merge.** The skeleton is shaped like the thing
  it stands for — tube, bands, ticks at true scale — so a
  waiting visitor is still looking at the archive's
  structure, and the thaw's glaze is the cold-store door's
  glass, the one surface in the theme's world that fogs.
- **Failure fallback.** The skeleton *is* the fallback
  system; its own failure mode (content never arrives) is
  covered by the ceiling + ash note. No-JS: no skeleton
  and no transition — pages load as pages.
- **Reduced-motion variant.** No sweep: an instant swap
  with a 120ms opacity settle. Skeleton identical (it
  never moved).
- **Performance budget & mobile variant.** One gradient
  div + static shells; ≤0.1ms/frame during the 320ms
  sweep. Mobile: identical, sweep shortens to 260ms.
- **Choreography timeline (v2).** Navigation → glaze
  starts (t=0) → peak fog at t=160ms, content swaps →
  clear by t=320ms → new page's §6.2-equivalent entrance
  (if any) begins only after the glaze has fully cleared
  — two performances never overlap.
- **State matrix (v2).** *Rest:* idle, glaze off-screen.
  *Hover / focus / active:* n/a — but focus is never moved
  by the transition until the swap completes, and then it
  goes to the new page's heading (a route change is
  announced, §below). *Scrolled-past:* n/a. *Disabled:*
  n/a. *Touch:* identical.
- **Breakpoints (v2).** Invariant across breakpoints
  except the sweep duration (320/300/260ms). Skeleton
  shells follow their sections' own breakpoint heights.
- **Edge cases & failure modes (v2).** *Back/forward
  cache restore:* no transition plays (the page was never
  gone). *Slow fragment >2000ms:* ceiling behaviour
  (above). *Rapid double navigation:* the second
  navigation cancels the first glaze mid-sweep and starts
  from the current fog level — the glaze never stacks.
- **Accessibility spec (v2).** Skeleton regions carry
  `aria-busy="true"` until raised; the ash-note failure
  is a real message, not an icon. Transitions: the route
  change is announced by moving focus to the new `<h1>`
  with `tabindex="-1"` after the swap; the glaze is
  `aria-hidden`.
- **Tokens consumed (v2).** `--core-white`, `--core-pale`,
  `--frost-line`, `--ash`, `--bubble-sheen`,
  `--ease-settle`.

### 6.17 Surface footer — the drill-site colophon

- **What & why.** The descent ends at the bed, and the
  footer is where the drill comes back up: a
  `--ancient-deep` band (the deepest ground, §2) that
  prints the archive's totals for the third and final
  time — 3,270 M DRILLED · 800,000 YEARS · 96 CUTS LOGGED
  (97 after §6.14 logs one) — the programme's colophon
  (site credits in the logbook's voice), the surface
  links (Programme, Record, Camp, Sample), and one drawn
  element: the full core, horizontal, 100% wide and 28px
  tall, every stratum and both ash layers at their true
  fractions, as the footer's top edge. It is the whole
  archive in one line, at the bottom of the page that
  drilled it — the third printing of every figure, in the
  place a reader checks a book's claims.
- **Structure.** A `<footer>` on `--ancient-deep`:
  the horizontal core strip (build-time SVG from the
  record, strata rects + ash lines + depth ticks at
  0 / 1,000 / 2,000 / 3,270 m), a totals row in mono
  (`--core-white`, 9.44:1), colophon text in Archivo
  (`--glacial` labels at 4.53:1, white body), and the
  link list. As the footer enters, the strip's fill wipes
  in left-to-right (below) — the core, laid down at last.
- **Motion spec.** Trigger: footer enters at 40%. The
  strip's strata wipe in over 1200ms `--ease-drill`
  (clip-path inset animating 100%→0 from the left — the
  core laid in its tray one last time), ash lines fade in
  at their fractions as the wipe passes them (34.0% at
  ≈410ms, 42.7% at ≈510ms). Totals are printed from first
  paint; nothing counts here — the footer states, it does
  not perform.
- **States.** Approaching (strip unfilled outline) /
  laid (wipe complete) / printed (reduced motion / no-JS:
  strip complete at paint).
- **Content merge.** The strip is the record (§6.15)
  drawn whole — the only place the entire core appears at
  once at reading size — and the totals are the same
  figures as the hero stamp and the readout's bed state.
  A footer that merely repeated the nav would waste the
  one moment the visitor has the whole descent behind
  them.
- **Failure fallback.** Static DOM/SVG: the strip ships
  complete; the wipe is a clip enhancement with a 3000ms
  force-complete watchdog. No-JS: printed whole.
- **Reduced-motion variant.** Strip printed complete;
  no wipe.
- **Performance budget & mobile variant.** One clip
  animation, 1200ms, once; ≈0ms/frame otherwise. Mobile:
  the strip stays full-width (it is the footer's reason
  to exist) at 22px; totals wrap to two lines; ticks at
  0 / 3,270 m only.
- **Choreography timeline (v2).** Last stratum (Deep
  Ancient Blue) settles → footer crosses 40% → wipe
  begins → CI ash fades at ≈410ms → Toba at ≈510ms →
  wipe completes 1200ms at the bedrock tick → the drill's
  work is done; §6.3's bit is parked at the bed above, in
  the rail, agreeing with the strip's right edge.
- **State matrix (v2).** *Rest:* laid. *Hover:* hovering
  a stratum in the strip names it + its range in a
  caption above the strip (the record, one last time).
  *Focus:* strip strata are not focusable (the links
  below are the footer's controls); the caption data is
  in the totals row's text. *Active:* n/a. *Scrolled-
  past:* laid. *Disabled:* n/a. *Touch:* no hover
  caption.
- **Breakpoints (v2).** ≥1200px: 28px strip, four ticks.
  768–1199px: 24px strip, three ticks. <768px: 22px,
  two ticks (above).
- **Edge cases & failure modes (v2).** *Cut count
  incremented this session:* the footer's total reads 97
  — the third printing updates with the record, and the
  gate (§10) checks footer against form. *Footer reached
  by jump (anchor):* the wipe plays from the jump's
  landing, or is already complete if the watchdog fired.
- **Accessibility spec (v2).** The strip SVG is
  `role="img"` titled "The whole core: five strata, ash
  layers at 1,112 and 1,397 metres". Footer links are a
  real list; totals are text. Contrast per §2's footer
  pairings (white 9.44:1, glacial labels 4.53:1).
- **Tokens consumed (v2).** `--ancient-deep`, `--core-
  white`, `--glacial`, `--ancient`, `--ash`, `--marker`
  (never in the footer — §2 forbids red here; listed to
  record the refusal), `--ease-drill`.

### 6.18 Below bedrock — the 404

- **What & why.** A missing page in this archive is a
  depth below the bottom of the core: the 404 is a short
  page on `--ancient-deep` whose entire content is a mono
  readout in the §6.4 format — "DEPTH — 3,270 M + / AGE —
  OLDER THAN THE ICE / CO₂ — NONE TRAPPED" — one line of
  Archivo ("There is no ice below the ice. The page you
  drilled for is not in this archive."), and two ways
  back: the surface (home) and the Record page. Its
  choreography is specified as *nearly none*, on purpose:
  below bedrock there is nothing to animate, and a playful
  bouncing 404 would break the archive's register at the
  exact moment it should be most itself.
- **Structure.** A single centred block: the readout
  (real `<dl>`, values printed, not computed — there is
  no p below the bed), the line, the two links styled as
  §11's primary/secondary buttons in their deep-band
  pairing (white outline, white text). The rail (§6.3)
  shows its bed state: bit parked, "BEDROCK" label
  printed.
- **Motion spec.** Trigger: none. One permitted motion:
  the return links' underline draw on hover/focus
  (140ms, §6.13's grammar). Everything else is still —
  specified stillness, tested by the gate (§10) so a
  well-meaning builder does not "enliven" it later.
- **States.** Only one: printed. (The absence of states
  is the design.)
- **Content merge.** The 404's joke is the record's own
  limit, stated in the record's own units — it works
  only because the whole site has taught the visitor
  what 3,270 m means. It is the archive's driest page
  and its most on-theme.
- **Failure fallback.** It is a static page; its fallback
  is itself. No-JS: identical.
- **Reduced-motion variant.** Identical (nothing moves).
- **Performance budget & mobile variant.** ≈0 everything.
  Mobile: the readout wraps to three lines; links stack
  full-width.
- **Choreography timeline (v2).** Specified as *none*:
  paint → read → leave by a link. The timeline's
  emptiness is the deliverable.
- **State matrix (v2).** *Rest:* printed. *Hover:* link
  underline only. *Focus:* 2px `--core-white` outline on
  links. *Active:* 1px press. *Scrolled-past:* the page
  does not scroll. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px / 768–1199px: centred
  block, max 560px. <768px: block full-width padded,
  readout stacked.
- **Edge cases & failure modes (v2).** *A genuinely deep
  link to a removed stratum:* the 404's Record link
  lands the visitor on the current record — the archive
  answers an old citation with its present state, and
  the Record page's strata table is where they will find
  what replaced it.
- **Accessibility spec (v2).** A real `<h1>` ("Below
  bedrock"), the readout as `<dl>`, links with plain
  text ("Back to the surface", "Read the core record").
  Contrast: white on `--ancient-deep` 9.44:1 throughout.
- **Tokens consumed (v2).** `--ancient-deep`, `--core-
  white`, `--glacial`, `--frost-line`.

---

## 7. Page application map

| Page | How the theme plays out |
|---|---|
| **Home (the descent)** | The full instrument: hero core (§6.1) + drill-line headline (§6.2), rail + readout (§§6.3–6.4) live throughout, tray (§6.5), honesty note (§6.6), camp (§6.12), five strata with columns (§6.7) and frost (§6.8), paw trail (§6.11), sample form (§6.14) at the bed, footer (§6.17). The reference build's shape; §13 maps its beats. |
| **Stratum detail (one era, deep-dive)** | Opens *at depth*: the rail loads with p preset to the era's start fraction and the page's own scroll spans only the era's range — the readout's age runs within the era's bounds, the margin column (§6.7) becomes full-height, and the tray is replaced by the era's sub-layer index. The visitor drills a single stratum the way the home page drills the whole core. |
| **The Record page** | §6.15 published: strata table, ash table, CO₂ anchors, the age function in symbols and words, camp facts, cut log. Minimal motion (reveals only); this is the page other pages cite, and it behaves like a reference work — dense, mono-led, printable at surface state. |
| **Camp / about page** | The surface, held: no descent (p stays 0; the rail prints its static frontispiece). §6.12's scene grammar at full width, crew and logistics as strata of *text* (each section a "layer" of the season), the bear (§6.10) patrolling the header ridge. Proves the theme can rest at the surface without drilling. |
| **Sample / contact (conversion)** | §6.14 as a whole page: the logbook sheet centred, the season's cut log beside it, the record's constraints (ash intervals, depth range) printed as the form's instructions. Arriving here directly (not via the descent) is fine — the sheet carries its own context. |
| **404** | §6.18: below bedrock. Specified stillness. |
| **Search / index of sections** | Refused as a separate page type: the tray (§6.5) + nav (§6.13) + Record (§6.15) are the index, at three scales. A fourth index would be a second record (§9). |

---

## 8. Worked examples

### 8.1 The hero — drilling the headline (worked example 1)

The home page's opening, end to end. **Content:** the
programme wordmark (§6.13); the hero core (§6.1) at 180px
with its five labelled bands and both ash lines at 34.0%
and 42.7%; the headline in three strata — "Eight hundred
thousand years," / "fell as snow" / "and kept the air." —
and a standfirst citing the record: "One core, 3,270
metres, drilled at Dome C (3,233 m, 75°S). Every figure on
this page is read off the ice." The age stamp (§6.2)
prints "800,000 YEARS IN ONE TUBE". The bear (§6.10)
stands at the ridge's left third, caption beneath.

**Scroll/timing timeline.** t=0: everything printed (no-JS
state is already the complete hero). JS arms: headline
lines clip, stamp lifts. t=100ms: the red drill line
begins its 1800ms descent of the core. t≈400/860/1330ms:
headline lines release as the line crosses 22/48/74%.
t=1800ms: line completes, fades to its 40% scar. t=1950ms:
the stamp lands (240ms, `--ease-stamp`). ≈t=2.7s: bubbles
(§6.1) are in steady rise, seeded from the printed SVG
positions. ≈t=21s: the bear's first sniff — long after the
drill's performance, by §6.10's choreography rule. First
scroll at any point: the drill sequence completes
instantly if still running; the rail (§6.3) takes over the
story. **What the visitor feels:** they did not watch an
intro; they watched the archive's first metre being
drilled, and the title was *in* the ice.

### 8.2 Mid-page — the tray and the ash (worked example 2)

The tray section, at the surface, before the deep descent.
**Content:** §6.5's five segments with their record
figures — Holocene (0–723 M · 0–11,700 YR BP), Last
Glacial Maximum (860–968 M · 19,000–26,500 YR BP), Toba
Ash (1,397 M · 74,000 YR BP — "A LAYER, NOT AN ERA"),
Eemian (1,636–1,709 M · 115,000–130,000 YR BP), Deep
Ancient Blue (2,900–3,270 M · 571,572–800,000 YR BP) —
and §6.6's honesty note beside them.

**Scroll timeline.** The tray enters → pins for 120vh →
segments lift in depth order as the pin's progress runs
(Holocene at pin-p 0.1, LGM 0.3, Toba 0.5, Eemian 0.7,
Deep Ancient Blue 0.9), each 600ms `--ease-lift` → pin
releases. The visitor hovers Toba: it lifts, and the
caption names its stratum. They click: the SAMPLE CUT tag
stamps "SAMPLE CUT — 1,397 M" (240ms), a live region
announces it, and the page begins its 900ms travel down —
past the camp (§6.12), into the glacial strata — while
the rail's bit descends and the readout (§6.4) runs:
crossing 1,112 m, the CI ash highlights for 1600ms
(§6.6); crossing 1,397 m, Toba highlights, and the
readout's stratum line settles on "TOBA ASH". The visitor
arrives at the Toba section having been shown the layer
twice — once in their hand, once by the drill. **What the
visitor feels:** the contents list and the archive are
the same object, and the page's honesty note was not a
boast — they watched the ordering happen.

### 8.3 Conversion — requesting a cut (worked example 3)

§6.14's form, at the bed of the home page (and standalone
as the Sample page). **Content:** the logbook sheet; the
printed line "96 CUTS LOGGED THIS SEASON"; fields for
name, institution, FROM / TO depths, purpose. **The
worked submission:** a researcher enters FROM 1,390 /
TO 1,405 — an interval containing the Toba ash at 1,397 m.

**Timeline.** Fields fill; focus doubles each rule in
turn. On submit: validation reads the record — the
interval is legal (within 0–3,270, FROM shallower than
TO) and triggers the ash note, printed in ash-grey
Archivo under the depth fields: "This interval contains
the Toba ash layer (1,397 M). The curators will write to
you." — information, not obstruction. The request sends;
the button reads "LOGGING…". Success: the stamp lands
across the sheet's corner — "CUT REQUEST № 97 — LOGGED"
(240ms `--ease-stamp`; 97 because the printed count was
96, §6.15) — and at t=300ms the logbook line rises
beneath the form: "№ 97 · 1,390–1,405 M · TOBA ASH
INTERVAL · LOGGED THIS SEASON". Fields freeze with values
intact. The footer's total (§6.17), when reached, reads
97 CUTS LOGGED. Focus moves to the receipt heading; the
live region speaks the same sentence. **What the visitor
feels:** they have not "converted"; they have written in
a book, in ink, at a numbered line — and the book's other
pages already agree with what they wrote.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **The lying core.** Ash layers in the wrong order,
   era boundaries at decorative depths, a readout whose
   age is linear "because it felt better". This is the
   theme's capital sin: the whole design is a claim that
   position is data. *Cure:* §6.15's single record +
   §10's recomputation gate. A builder who hand-places a
   band has failed the theme, however pretty the band is.
2. **Generic snow.** Falling-snow particle overlays,
   snowflake clip-art, winter-sale iconography. Snow at
   Dome C is not weather decoration; it is the archive's
   raw material, and it appears as strata and ridge, not
   as confetti. *Cure:* no precipitation effects, ever;
   the only falling thing on the page is the drill.
3. **The mascot bear.** A named, waving, speech-bubbled
   bear — or worse, a cartoon bear "guide" who explains
   sections. *Cure:* §1's ruling: flat silhouettes, real
   gait, no name, no reactions to the visitor.
4. **Blue-gradient soup.** Every section a different
   blue gradient with glassmorphism cards floating on
   it — the generic "climate tech" look. *Cure:* the
   tint is one continuous function of depth (§4), bands
  are flat tints with declared pairings, and cards are
   core-pale *objects in trays*, not frosted glass.
5. **Red as a colour.** Red buttons, red links, red
   "error" states, a red logo. Red here is a hand with a
   stamp; the moment it is a brand colour the stamps
   stop meaning anything. *Cure:* §2's census (≤10,
   licensed uses only).
6. **Numbers as vibes.** "800K years!" in a hero, "over
   3,000 metres" in a stat row, CO₂ given as "low/high".
   *Cure:* type law 2 + §6.4: exact figures, units
   always, derived never typed.
7. **The drill as decoration.** A cute animated drill
   cartoon beside an unrelated article; a progress bar
   skinned as a core that does not correspond to the
   sections. *Cure:* the rail's ticks are the sections
   (§6.3); if the correspondence is not exact, ship a
   plain page instead.
8. **Twinkling frost.** Crystals that shimmer, pulse or
   regrow on hover — glitter in a lab coat. *Cure:*
   §6.8: grow once, hold still, corners only, ≤72px.
9. **Two records.** Tray figures updated, readout figures
   stale; the footer disagreeing with the form. Nothing
   kills an archive's credibility faster. *Cure:* one
   record (§6.15), three-printings check (§10).
10. **Speed.** Snappy 200ms everything, springy
    overshoots on scroll, a readout that *zips* to the
    bed on a fast flick. The ice took 800,000 years; a
    theme that feels like a fintech launch has missed
    its subject. *Cure:* lerp 0.09, the named easings,
    and §5's refusal list (no marquee, no kinetic type).
11. **Covering the ice.** Overlays, modals or sticky
    banners that hide the rail or the core mid-descent.
    *Cure:* the theme has no modals (§11); the rail is
    never covered by anything, including cookie notices —
    those print at the surface, above the hero, as part
    of the page.
12. **Warmth cosplay.** Wood textures, cabin imagery,
    "cosy winter" styling creeping in around the camp.
    The camp is a workplace at −54.5 °C, drawn flat.
    *Cure:* §6.12's figure-in-a-paper rule: the scene
    illustrates facts, in the palette, or it is cut.

---

## 10. Quality gate

The theme may not ship in a build unless every line
passes. Blocking checks, in order:

1. **Recomputation.** A script (or a patient human)
   recomputes every printed figure from §6.15's record:
   era ranges, ash depths (1,112 / 1,397 m), CO₂ anchors,
   camp facts, cut count. Any hand-typed figure that
   disagrees fails the build.
2. **Three printings agree.** Readout bed state, tray
   labels and footer totals print the same totals
   (3,270 M · 800,000 YR · cut count). After a test
   §6.14 submission, all printings of the count move
   together (96 → 97).
3. **Age-curve honesty.** Scrubbing to p = 0.5 shows an
   age within ±1% of 800,000 × 0.5^2.8 ≈ 114,900 YR BP —
   not 400,000. A linear readout fails, however smooth.
4. **Ash order.** In every core rendering (hero, rail,
   tray, columns, footer strip), CI (1,112 m) sits above
   Toba (1,397 m), and the honesty note is present
   verbatim beside the tray.
5. **No-strand drill.** JS disabled: headline whole,
   stamp printed, tray navigable, readout data present
   per section, form submittable. Then JS on with the
   loop artificially stalled: every watchdog (4.5s
   headline, 3s hero, 2s skeleton, 2.5s camp facts,
   3s footer) fires and settles its element.
6. **Red census.** ≤10 marker-red instances on the home
   page, each from §2's licensed list; zero red text on
   `--ancient` or `--ancient-deep` grounds.
7. **Pairing audit.** Every text element's pairing
   appears in §2's table with its ratio; specifically:
   no white text on `--glacial`, no body text on
   `--glacial-deep`, no ash-grey body copy, focus
   outlines correct per band.
8. **Reduced-motion pass.** With `prefers-reduced-
   motion`: no lerp, no gait, no growth, no wipe —
   and the page is *complete*: bear standing, crystals
   grown, columns drawn, figures stepped but exact.
9. **Loop discipline.** One rAF loop; disabling any
   single element's registration never breaks another's
   values; frame cost of the loop with everything live
   ≤1.6ms on a mid-tier laptop; zero long tasks >50ms.
10. **Ambient census.** Exactly three ambient loops
    (bubbles, bear, camp) and each pauses off-screen and
    on tab-hide — verified by scrolling past each and
    watching the frame cost fall to the readout's alone.
11. **404 stillness.** The 404 contains no animation
    beyond link underlines. (A gate line for a negative
    — because someone will try.)
12. **Mobile omissions are the declared ones.** Under
    768px: paw trail cut, cub cut, rail horizontal —
    and nothing else missing. An undeclared omission
    fails; a declared one is design.

---

## 11. Component inventory

Every component a real site in this theme needs, with its
themed treatment — or its refusal, with the in-theme
replacement.

| Component | Treatment in this theme |
|---|---|
| Primary button | A stamped tag in waiting: `--core-pale` sheet, 1.5px `--ink-frost` border, Archivo 600 label ("LOG THIS REQUEST"); on press it takes the §6.14 stamp behaviour — actions in this archive leave a mark |
| Secondary button | Underlined Archivo text; hover draws the frost-line underline (140ms) |
| Text input | A logbook line: borderless field on a printed `--frost-line` rule; focus = double rule (§6.14) |
| Number input (depths) | Mono, with the unit printed inside the rule ("M"); range validated against the record |
| Select / picker | Refused as a styled dropdown; era/depth picking is done on the tray (§6.5) or the Record's tables — you point at the ice, you do not open a menu of it |
| Checkbox | A sample box: an outlined square that takes a miniature SAMPLE CUT stamp when ticked — used in the cut log filters |
| Radio group | Stratum rows: one row per option with its depth range; the chosen row carries the frost-line underline |
| Tabs | Refused. Strata are not tabs; a page is descended, not switched. Section switching on the Record page is a contents list of anchor links |
| Accordion | Refused on the descent (a stratum does not fold). On the Record page only, long tables may collapse under their headings — a reference work may shelve |
| Modal / dialog | Refused entirely. Nothing may cover the rail or the core (§9.11). Confirmations are receipts printed in place (§6.14) |
| Toast | Refused. Outcomes are stamped or logged in place; nothing floats over ice and vanishes |
| Alert / banner | The ash note (§6.14): ash-grey Archivo italic on the surface pairing, in place, permanent until resolved |
| Badge / chip | The sample tag: mono, `--marker` border on `--core-pale`, rotated −3 to −5°, used for SAMPLE CUT and logged states only |
| Pagination | Depth folios: "STRATUM 3 OF 5 · 1,636–1,709 M" in mono with prev/next named by era — used on stratum detail pages |
| Table | The Record pattern (§6.15): mono figures, Fraunces headings, frost-line rules, no zebra (zebra is not stratigraphy — bands in tables are *data rows*, shaded only when the row is a layer) |
| Card | A tray segment (§6.5) or a core-pale inset sheet on deep bands (§4) — cards are physical sections or logbook sheets, never floating glass |
| Progress bar | Refused; replaced by the rail core (§6.3) |
| Spinner | Refused; replaced by the un-drilled skeleton (§6.16) |
| Skeleton | §6.16 — blank ruled tube + "CORE NOT YET RAISED", 2000ms ceiling |
| Tooltip | A mono caption that prints beside the item on hover/focus (§6.9's band caption pattern) — positioned text, never a floating dark box |
| Breadcrumbs | A depth line: "SURFACE › TRAY › TOBA ASH · 1,397 M" in mono at the stratum's head |
| Search | Refused as a page; the Record (§6.15) is the findable thing, and the tray is the browse. A site this size that needs search has grown a second record |
| Empty state | §6.18's grammar at small scale: "NO ICE LOGGED AT THIS DEPTH" + the record line + a way back |
| Error state | Ash notes in place (§6.14) for fields; §6.18 for pages |
| Form validation | Record-checked (§6.14): ranges, direction, ash intervals — errors in ash, information in ink |
| Footer | §6.17 — the horizontal core + third printing of totals |
| 404 | §6.18 — below bedrock, still by specification |

---

## 12. Content & copywriting voice

Two registers, kept apart by law. **The log** (Archivo) is
the programme's written voice: plain, complete sentences,
past-tense factual, no exclamation marks anywhere on the
page. **The instrument** (JetBrains Mono) is labels, stamps
and readouts: terse, uppercase only where §3 licenses it,
always with units. Fraunces speaks only in headings — the
scientists' titles, sentence case, with the number in them
where the number is the news.

- **Headlines**: a statement of fact with its scale in it.
  ✓ "Eight hundred thousand years, in one tube."
  ✗ "Journey to the Centre of the Ice Age!!" — exclamation,
  and a journey the page does not take.
- **Labels** (mono): literal, with units. ✓ "DEPTH — 1,397 M"
  / "CO₂ — 200 PPM". ✗ "How deep are we?" / "Air quality".
- **The log's sentences**: ✓ "The Toba layer fell in a
  single season, 74,000 years ago. The ice above it is
  younger than the ice below it, and both are younger than
  the eruption." ✗ "Nature's most epic eruption dropped
  some serious ash!" — the log does not do epic.
- **Error messages** (form): an ash note saying what would
  do. ✓ "Depths here are in metres, 0–3,270. The TO depth
  must be the deeper one." ✗ "Invalid range!!".
- **Empty states**: ✓ "No ice logged at this depth."
  ✗ "Nothing here… yet 👀" — no emoji anywhere in the
  theme, ever.
- **Numbers**: exact, unit-bearing, derived. ✓ "571,572 YR
  BP". ✗ "Over half a million years!" / "≈570K BP".
- **Fixed strings (verbatim, never paraphrased):** the
  surface caption "THE SURFACE · 0 YR BP · PATROLLED
  DAILY"; the honesty note (§6.6, quoted there in full);
  the stamp texts "SAMPLE CUT" and "CUT REQUEST № N —
  LOGGED"; the skeleton note "CORE NOT YET RAISED"; the
  404 line "There is no ice below the ice."; the bedrock
  readout "BEDROCK — BELOW THIS, NO ICE".
- **Dates and seasons** are station seasons, not calendar
  marketing: "the 2026–27 season", "winterover" as a noun
  for the crew. The archive's clock is depth; its calendar
  is the drilling season, and the copy says which.

---

## 13. Full-page scroll choreography map

The home page, surface to bed, in the order the visitor
lives it. One shared rAF loop (lerp 0.09) drives every
scrubbed value; beats are listed at their trigger points.

1. **First paint.** The complete surface: hero core printed
   with its SVG bubble field, headline whole (or armed),
   stamp at rest, bear standing, rail at p=0, readout at
   surface figures. *Feels like:* arriving at a drill site
   where the core is already on the table.
2. **t≈100–2200ms.** §6.2's drill: line descends, headline
   releases stratum by stratum, stamp lands. The one
   entrance the page performs unprompted.
3. **Ambient settles.** Bubbles in steady rise (≈t=2.7s);
   the bear begins its round (first sniff ≈t=21s, after
   the drill, §6.10). The hero is alive but unhurried.
4. **First scroll.** The rail takes over: fill and bit
   descend at lerp 0.09, readout figures begin their
   crawl through the Holocene — depth moving, age barely
   (the curve's first lesson, taught by the thumb).
   Paw print 1 presses at p=1/13.
5. **The tray.** Pins for 120vh; five segments lift in
   depth order; the honesty note is read (it sits beside
   the tray, at the exact moment the visitor handles the
   layers it describes). A click stamps and sends the
   drill travelling (§8.2).
6. **The camp.** Facts count up (1400ms, staggered) as the
   scene enters; flag, wind and cub cycle while visible;
   the descent pauses narratively at the surface's human
   layer before going under.
7. **The glacial strata.** Bands deepen through §4's
   thresholds; text pairings switch as sets; margin
   columns draw (§6.7); frost grows at corners (§6.8).
   The readout's age starts to run — centuries per
   centimetre becoming millennia.
8. **The ash crossings.** At 1,112 m the CI layer
   highlights and the live region names it; at 1,397 m,
   Toba. Two quiet beats, 285 m apart, that the whole
   theme has been promising since the hero.
9. **The Eemian.** A warm stratum in the data (CO₂ back
   to ~280 ppm) inside deepening blue — the readout
   tells a returning visitor's favourite story: it has
   been warm before, and the ice remembers.
10. **Deep Ancient Blue.** The last stratum: sparse text
    on core-pale insets, age tearing past 571,572 toward
    800,000, paw print 12 pressing at p=12/13 — the trail
    ends one print above the bed.
11. **The bed + the form.** p reaches 1: bedrock label
    prints under the rail; §6.14's logbook sheet waits on
    core-pale. The visitor may write in the book (§8.3)
    or simply stand at the bottom of 800,000 years.
12. **The footer.** §6.17's horizontal core wipes in —
    the whole descent, seen at once, level — ash lines
    fading up as the wipe passes their fractions. Totals
    for the third time. *Feels like:* the core laid in
    its tray in the cold store, labelled, done.
13. **Reverse pass.** Scrolling back up: fill, tint and
    figures retrace exactly (the drill can be raised);
    stamps stay stamped, columns stay drawn, facts stay
    counted, the tray's tags persist. The ascent is
    faster in the hand but the ice does not care: nothing
    un-happens in an archive; only position changes.

---

## 14. Whole-page performance budget

| Budget line | Limit | Notes |
|---|---|---|
| Total page weight (home) | ≤ 780KB | Fonts are the floor: three families, subset, ≤ 190KB total |
| Core-section photography | ≤ 110KB each, ≤ 4 on home | WebP, tray-framed sizes, lazy below the fold |
| JS (theme system) | ≤ 42KB gz | One loop, one record, no framework for the theme layer |
| CSS | ≤ 32KB gz | Gradients and rules do the material work; no image textures |
| Inline SVG (scene, columns, bears, footer strip) | ≤ 60KB total | Build-time generated from the record; paths simplified |
| Frame budget (shared loop) | ≤ 1.6ms/frame | Fill/bit transforms, readout repaint-on-change, tint lerp, paw thresholds, bubble physics share the one loop |
| Long tasks | none > 50ms | The record parses at build time; runtime never re-derives strata |
| Layout shift | CLS ≤ 0.02 | Skeleton shells reserve real heights; images carry aspect ratios; stamp landings are transform-only over printed space |
| Time to readable | first paint, JS or not | The page is content-complete in HTML; JS adds the descent, the drill and the bubbles — never content |

**Cut order when the budget is exceeded** (cut in this
order, never skip ahead): 1) core-section photographs
(4 → 2); 2) wind streaks in the camp scene (§6.12's own
first cut); 3) hero bubbles (46 → 28, the mobile count);
4) frost cluster variant count (3 → 1); 5) the footer's
wipe (print the strip). **Never cut:** the record's
completeness, the watchdogs, the ash layers in any
rendering, the exact figures, the reduced-motion
variants, the honesty note. A shallower page is legal; a
dishonest or stranding one is not.

**Declared mobile omissions** (design, not failure —
§10 check 12): paw-print trail (§6.11), the camp cub
(§6.12), vertical rail → horizontal bar (§6.3).

---

## 15. Build-order checklist

1. **The record first.** Author `core-record.json`:
   totals (3,270 m / 800,000 yr), the age function, CO₂
   anchors, five strata with ranges, two ash layers,
   camp facts, cut count, fixed strings. Validate it:
   ranges contiguous or honestly gapped, ash order true,
   every figure in this spec derivable. No design work
   precedes the data — the page is the record's printout.
2. **Static surface page.** Build the complete page with
   no JS: hero printed with SVG bubble field, headline
   whole, stamp at rest, tray as links, per-section
   static readouts, camp facts at final figures, form
   functional, footer strip complete. This is the
   fallback state and it must already be good.
3. **Typography and bands.** Load the three faces
   subset; set the type laws (§3); implement §4's five
   tint thresholds with their text-pairing switches.
4. **The rail and readout.** Tube, ticks and era marks
   from the record; readout block with surface figures;
   the bedrock label.
5. **The shared loop.** rAF + lerp 0.09 + the record;
   register fill, bit, readout, tint, paw thresholds;
   add the global stall watchdog (snap-to-raw at
   2000ms).
6. **The hero performances.** Canvas bubbles seeded
   from the SVG field; §6.2's drill line and stamp with
   their 4.5s fallback; §6.9's lamp; §6.10's bear round.
7. **The tray and the ash.** Pin sequence, lifts,
   stamps, smooth travel; §6.6's crossing highlights
   wired to the loop's depth; the honesty note placed
   and proofread against the record.
8. **Strata dressing.** Margin columns generated per
   era; frost clusters placed at corners; per-section
   static readout lines (the no-JS layer) verified
   against the loop's values at the same depths.
9. **The camp.** Scene SVG, count-up registry, flag /
   wind / cub cycles with off-screen pausing; the
   2500ms facts watchdog.
10. **The form.** Logbook sheet, record-driven
    validation (range, direction, ash intervals),
    server-side receipt with the same number logic;
    JS enhancement: stamp + receipt line + count
    propagation to §6.17.
11. **Skeleton and thaw.** §6.16 shells with reserved
    heights, the 2000ms ceiling, the glaze transition
    with its 1400ms abort.
12. **Footer and 404.** §6.17's strip generated from
    the record, wipe + watchdog; §6.18 built and then
    *checked for stillness* (§10 check 11).
13. **Reduced-motion pass.** Every element's variant
    implemented and walked: stepped readout, standing
    bear, grown frost, drawn columns, printed stamps,
    instant jumps.
14. **The gate.** Run §10's twelve checks, including
    the recomputation script and the three-printings
    test with a live form submission. Sign-off by
    someone who did not build the page — an archive is
    audited, not self-certified.
15. **Ship the surface first.** If anything must launch
    before the loop is ready, launch step 2's static
    page. It is complete. The descent is an enhancement
    the archive can receive later — like a deeper core,
    it is worth waiting for and never worth faking.
