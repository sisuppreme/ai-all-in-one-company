# 68. Cryo Lab Monograph — Expanded (v1 + v2)

A cryogenics laboratory's specimen monograph, expanded to the 50x
standard. Identity preserved exactly from the original entry: content
is preserved in frost; sections are samples in cold storage; you thaw
them by reading, and frost creeps back when you leave. Palette anchors
unchanged — freezer white `#EEF3F4`, frost blue `#A8C8D8`,
specimen-label buff `#E4DCC3`, warning orange `#E4572E`, steel
`#6E7B82`. Type unchanged — Archivo for display, IBM Plex Mono for
specimen codes, temperatures and labels. All ten original signature
elements are deepened, never redesigned: the breath-melt hero, the
sliding cold-store drawers, the thaw/re-frost cycle, the header
thermometer, the specimen-code labels, the condensation droplets, the
frost dendrite dividers, the warm-spot hover, the seal-break click,
and the freezer-door transition.

**The theme's one law: *nothing thaws that is not being read, and
nothing is counted that is not in the store.*** Every figure on the
page — specimen counts, tray counts, serial ranges, temperatures,
storage days — traces to one declared record, the Collection Record
(§6.17), and reconciles across every printing of it. Frost is an
overlay on complete, printed content, never a container for it: the
DOM ships thawed and readable, and every frozen state is armed by
script only, behind a named watchdog. A specimen that cannot be
thawed by the reader's own attention does not exist in this theme.

---

## 1. Concept & world

The site is the published monograph of a cryogenics laboratory's
cold store — part catalogue, part lab notebook, part handling
protocol. The laboratory keeps physical specimens at −80 °C:
ice cores, tissue vials, seed duplicates, microbial mats, sediment
traps, reference standards. The monograph is the store's public
face, and it behaves like the store. Content is not *displayed*;
it is *kept*. Sections live in cold-storage drawers that slide open
on a rail. Samples sit in frosted trays. Reading is a controlled
thaw: while you attend to a sample, its frost clears from the edges
inward; when you leave, the frost creeps back, because in the real
store an unattended sample on the bench is a sample being ruined.
The page's progress instrument is not a bar but the header storage
thermometer, which falls one degree for every tray you thaw, from
the door-side −12 °C toward the −80 °C setpoint — the more of the
archive you have personally brought up to reading temperature, the
colder and safer the store reads.

The mood is quiet, exact, and slightly melancholic: a bright room
that is cold in a way the visitor can feel. Nothing sparkles.
Frost is matte, steel is brushed, labels are buff paper typed on a
machine that only prints capitals and hyphens. The single warm
thing in the world is the reader — breath on the hero glass, a warm
spot under the pointer — and the theme spends that warmth carefully:
every thaw is temporary, logged, and reversed.

**Best-fit sites and audiences.** Research institutes and specimen
archives publishing a collection; biorepositories and seed vaults;
glaciology and polar-science programmes with core libraries;
museum stores and conservation labs showing holdings that are
physically kept cold; a journal or laboratory whose authority comes
from *custody* — we hold this, at this temperature, since this
date — rather than from novelty. The audience is patient and
literate: researchers checking a holding, journalists verifying a
claim of preservation, funders reading a stewardship report.

**When NOT to use it.** Never for anything that must feel fast,
hot, or abundant: e-commerce, entertainment, food delivery, event
promotion. Never where the user must act in under a minute — the
theme's whole grammar is dwell and return. Never as a generic
"clean scientific" skin for a SaaS product: stripped of a real
collection record, the drawers are theatre and the thermometer is
a lie, and §10's gate fails the build on exactly that. And never
for content with no stable inventory — if the numbers cannot be
declared once, in §6.17, and left alone, this is the wrong theme.

**The world in one paragraph, for builders.** A specimen has a
code (collection–year–serial), a drawer, a tray, a temperature, and
a number of days in store. A reader has warmth, attention, and a
limited right to thaw. The lab has rules: seals break loudly and
are logged in orange; frost always wins eventually; the store is
colder than any sample's story is warm. Every design decision in
this document is one of those sentences made visible.

## 2. Palette

Five anchors from the original entry, held exactly. Derived tokens
are darkened or lightened *from the anchors only* — no new hues
enter the store.

| Token | Hex | Role | Usage ratio | Pairing / contrast |
|---|---|---|---|---|
| `--freezer` | `#EEF3F4` | Page ground, drawer interiors, tray glass base | ~55% | Ground for `--ink` (11.6:1) and `--steel-dark` (7.1:1) |
| `--frost` | `#A8C8D8` | Frost layer, thaw edges, drawer shadows, divider plates | ~18% | Decorative over `--freezer`; never text (1.6:1) |
| `--buff` | `#E4DCC3` | Specimen labels, table header band, form ledger paper | ~10% | `--ink` on buff 10.4:1; the only paper in the theme |
| `--steel` | `#6E7B82` | Shelving lines, drawer fronts' frames, rules, inactive instruments | ~12% | On `--freezer` 4.0:1 — rules and large marks only, never body text |
| `--orange` | `#E4572E` | Warning only: seal-break crack, seal dot, over-temperature tick | <1% | 3.4:1 on `--freezer` — never carries text at any size |
| `--ink` | `#26333A` | All body text, codes, temperatures (steel darkened to text grade) | — | 11.6:1 on `--freezer`, 10.4:1 on `--buff` |
| `--steel-dark` | `#47535A` | Secondary text, captions, table figures' labels | — | 7.1:1 on `--freezer` |
| `--frost-deep` | `#5E93AC` | Thaw-edge highlight, focus ring, link underline in thawed state | — | 3.1:1 — graphical accents and focus only |
| `--ice-line` | `#C9DCE4` | Hairlines inside drawers, tray cell borders | — | Decorative; always doubled by spacing, never sole structure |
| `--buff-deep` | `#CBBFA0` | Label shadow edge, table band rule | — | Decorative |
| `--orange-deep` | `#B23A1B` | The word "orange" never prints; this is the seal tag's border at small sizes where the anchor reads muddy | <1% | Still never text; border and dot only |

**Usage laws.** (1) *Frost is a value, not a colour effect:* the
frost layer is `--frost` at 82% opacity over `--freezer`, with a
noise texture — never a gradient wash, never blue-tinted glass
"glassmorphism". (2) *Orange census:* `--orange` may appear in
exactly three places — a seal-break crack (§6.9), the 6px seal dot
on a broken-seal label (§6.5), and the thermometer's over-temperature
tick (§6.4). §10 greps for it. Orange never fills a button, never
colours a heading, never means "brand". (3) *Buff is rationed to
things that are labels in the world:* specimen labels, the table's
header band, the form's ledger block. A buff card that is not a
label is slop (§9). (4) *Steel is structure, ink is voice:* if a
visitor reads it, it is `--ink`; if it holds something up, it is
`--steel`. (5) **Dark-mode behaviour:** there is no dark mode. A
cold store is lit like a laboratory at all hours; the theme refuses
the inversion and §11's inventory says so. A visitor's OS dark
preference is honoured only in form controls' native rendering,
never in the palette.

## 3. Typography

Two families, as specified in the original entry. Archivo is the
tight grotesque of drawer fronts and headlines; IBM Plex Mono is
the lab's hand — every code, temperature, count and label is set in
it, because in the store anything measured is typed, not typeset.

| Role | Font | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Display (hero headline) | Archivo, 700 | clamp(2.75rem, 6.5vw, 4.75rem) / 1.02 | −0.02em | Tight grotesque, uppercase never; the headline is a specimen name, not a shout |
| Drawer-front title | Archivo, 600 | 1.5rem / 1.15 | −0.01em | Pairs with its code in mono on the same baseline row |
| Heading (in-drawer) | Archivo, 600 | 1.25rem / 1.25 | −0.01em | Sentence case |
| Body | Archivo, 400 | 1.0625rem / 1.65 | 0 | Measure 62ch inside trays; the monograph is read, not scanned |
| Caption / handling note | Archivo, 400 italic | 0.875rem / 1.5 | 0 | Italics are the lab's pencil: asides, caveats, care instructions |
| Specimen code | IBM Plex Mono, 500 | 0.8125rem / 1.4 | 0.04em | Always `COLLECTION-YEAR-SERIAL`, always 4-digit serial, never truncated |
| Temperature / data | IBM Plex Mono, 500 | 1rem / 1.4 | 0.02em | Minus sign is U+2212; degrees always `°C`; tabular figures |
| Label micro-type | IBM Plex Mono, 400 | 0.6875rem / 1.35 | 0.08em, uppercase | The typewriter register: `STORED`, `THAWED`, `SEAL BROKEN — LOGGED` |

**Type laws.** (1) *Numerals are always mono* — a temperature, a
count, a serial, a day total set in Archivo is a §10 failure; the
eye must be able to tell a measurement from a sentence at a glance.
(2) *Codes are never styled* — no bold, no colour, no size change
for a specimen code anywhere; a code's authority is its format.
(3) *The dead band:* no text between 1.25rem and 2.75rem except
drawer-front titles at exactly 1.5rem — the page is either
monograph text or a drawer front, nothing in between. (4) *Minus
temperatures are set with the true minus* and never hyphenated;
`−80 °C` is a single unbreakable unit (`white-space: nowrap`).
(5) *Archivo never sets a number that matters:* prices of
attention — counts in headlines are re-set in mono inline, even
mid-sentence.

## 4. Layout language

The page is a cold-store wall. A fixed header (the store's door
frame) carries the monograph title, the rail navigation (§6.11),
and the storage thermometer (§6.4). Below it, the wall: eight
drawers (§6.2), stacked vertically, each a full-width horizontal
drawer whose front is a brushed-steel band and whose interior,
when open, is a tray field on `--freezer`.

**Grid and rhythm.** Content column max 1200px, centred; inside a
drawer, a 12-column grid with 24px gutters; tray cards (§6.12)
occupy 3 columns each on desktop. The vertical rhythm is the
*shelf pitch*: drawer fronts are 96px tall, separated by 16px
shelving shadow gaps; an open drawer's interior pads 40px top and
48px bottom — the drawer is deeper than its front, and the layout
says so. Section spacing is never arbitrary margin: it is always
a shelving line (a 2px `--steel` rule with a 1px `--ice-line`
under-rule) or a divider plate (§6.7).

**Density rules.** One open drawer is the reading unit. At most
one drawer is pinned open at a time (§6.2); two drawers may be
transitionally open during a slide, never three. Inside a tray,
density is laboratory density: figures are close, air is in the
margins, nothing floats. Whitespace in this theme is *cold air* —
it appears as the gap between trays (24px), the bench space above
a form (64px), and the empty cold field of the 404 (§6.18) — and
it is always bounded by steel, so it reads as storage volume, not
as minimalism.

**The rail line.** Drawers trigger at the *cold-store rail line*,
38% of viewport height — the height of the store's worktop rail,
where a real drawer would meet the technician's hands. All
scroll-driven thaw measurements (§6.3) are taken against the same
line, so the page has one physics, not per-element triggers.

**Print.** The monograph prints as a monograph: drawers print
open, frost absent, labels in mono, the ledger table (§6.13)
complete. `@media print` forces the thawed state — paper is the
final fallback and §10 checks it.

**Anatomy of an open drawer, top to bottom.** (1) The front,
resting at the drawer's head — it does not scroll away with its
interior; a reader inside Drawer 3 can always see whose drawer
they are in, its range and its mean. (2) The bench strip: a 24px
`--ice-line` band carrying the drawer's handling note in italic
Archivo (the lab's pencil — "Trays thaw while read. Frost returns
when you leave. Seals are logged."). Every drawer has exactly one
handling note, written for its material: the seed drawer's note
speaks of viability, the tissue drawer's of minutes at room
temperature. (3) The tray field (§6.12's grid). (4) The drawer's
foot rule: a steel hairline with the drawer's closing figure in
mono — `DRAWER 3 · 196 SPECIMENS · MEAN −79.8 °C` — the front's
figures restated at the exit, so a drawer is bracketed by its own
record. The anatomy never varies; only the facts do. A builder who
finds themselves designing a special drawer interior has
misunderstood the store: drawers differ in what they hold, never
in how they open.

## 5. Full motion system

Motion in the cold store is thermal: things thaw, frost, slide
under weight, and crack under violation. Nothing bounces. Nothing
spins. The store has exactly one heartbeat — the shared loop — and
exactly two licensed ambient loops (condensation on the hero
glass, frost-noise crawl), each specified where it lives.

**Named easings** (the store's own, used everywhere; no others):
`--ease-drawer` cubic-bezier(0.22, 1.0, 0.36, 1) with a heavy tail
— drawer slides, door transitions; `--ease-thaw`
cubic-bezier(0.4, 0.0, 0.2, 1) — frost clearing; `--ease-frost`
cubic-bezier(0.7, 0.0, 0.84, 0) — frost returning, always slower
than the thaw that preceded it; `--ease-exhale`
cubic-bezier(0.16, 1.0, 0.3, 1) — the hero de-fog; `--ease-crack`
cubic-bezier(0.85, 0.0, 0.15, 1) — the seal crack, the only fast
thing in the store; `--ease-tick` steps(1) — thermometer digits,
which change like instruments, not like animations.

**The shared loop.** One `requestAnimationFrame` loop drives every
scroll- and pointer-coupled value: drawer slide positions, thaw
progress, warm-spot mask position, thermometer display, droplet
slides. Scroll position is lerped at `--loop-lerp` 0.09 — the
heavy, damped feel of pushing a loaded freezer drawer — and all
scrubbed values read from the single lerped progress per section.
Raw scroll events never touch the DOM. If the loop dies, every
watchdog in §6 fires its element to the thawed, printed state.

**Motion-term translation table** (the standard's full vocabulary,
in this theme's language — or refused, in-world):

| Term | In Cryo Lab Monograph |
|---|---|
| Scroll-triggered reveals | Drawer slides (§6.2) at the rail line; labels stagger in cold-store order (§6.5) |
| Scroll-driven / scrub animation | Thaw progress scrubbed to dwell time in view (§6.3); thermometer fall (§6.4) |
| Parallax | Three storage depths only: shelving lines 1.0×, tray contents 0.97×, frost layer 0.94× — the frost lags because it is on the glass |
| Pinned sections | One drawer pins open while its trays are read (§6.2); the ledger table's header band pins inside its drawer (§6.13) |
| Smooth scrolling | The loop's 0.09 lerp; native scroll, damped rendering |
| Progress indicator | The header thermometer (§6.4) — progress as temperature |
| Staggered reveals | Labels and trays in cold-store order: drawer order, then serial order (§6.5, §6.12) |
| Masked reveals | Frost masks: radial warm-spot mask (§6.8), edge-inward thaw mask (§6.3) — masks here are weather, not wipes |
| Kinetic typography | Refused. Type in a lab does not perform; the thermometer's ticking digits are the only moving type |
| Marquee | Refused. Nothing in a cold store scrolls sideways to get attention |
| Counters | Temperature, specimen counts, storage days count in mono (§6.4, §6.12) — instruments, not celebrations |
| SVG line-draw | Frost dendrites grow across divider plates (§6.7); the seal crack draws (§6.9) |
| Image scale-in-frame | Specimen images scale 1.04 → 1.0 inside frosted tray frames as they thaw (§6.12) |
| Hover / tilt micro-interactions | Warm-spot hover (§6.8); trays tilt max 3° toward the light (§6.12) |
| Custom cursor | Refused — standing rule, and in-world: the pointer is a warm hand, shown by the frost it melts, never by a costume |
| Skeleton loading | Frosted silhouettes that thaw as content loads (§6.15) |
| Page transitions | Freezer-door slide (§6.10) |
| Reduced motion | §12's lights-on store: everything thawed, drawers print open, no frost, no slide |

**Ambient loops — exactly two.** (1) Condensation droplets on the
hero glass (§6.6), running only while the hero is in view. (2) The
frost-noise texture crawl — a background-position drift of the
frost layer's noise at 1px per 4s, almost imperceptible, like cold
air moving; it is cut first under any performance pressure (§14).
No third loop may be added; §10 counts them.

**The watchdog registry.** Every armed pre-state in the theme is
registered, at arm time, in one watchdog table owned by the loop —
the store's night watchman, and the mechanical form of the law
that no specimen stays frozen shut. The registry, complete: hero
de-fog 3,000ms (§6.1) → frost layer removed; drawer slide 2,000ms
per drawer (§6.2) → snap open; tray thaw stall 4,000ms (§6.3) →
force reading-clear; thermometer calibration 4,000ms (§6.4) →
snap to live; label settle 1,500ms (§6.5) → snap to rest;
dendrite growth 2,500ms (§6.7) → snap grown; seal crack 800ms
(§6.9) → complete the break; door transition 2,200ms (§6.10) →
force incoming page visible; form submission 4,000ms (§6.14) →
restore with values intact; skeleton ceiling 1,500ms (§6.15) →
print regardless. A watchdog that fires is logged to the console
with the element's specimen code or drawer number — in
development. In production it fires silently, because the reader
is not the technician. §10's drill kills the loop and reads this
table back, deadline by deadline.


## 6. Signature elements

Eighteen elements: the ten originals (§6.1–§6.10), seven
page-family elements (§6.11–§6.16, §6.18), and the Collection
Record itself (§6.17), the one data object every figure obeys.

### 6.1 Breath-melt hero

- **What & why.** The monograph's title plate, shipped under a
  full frost layer. On load, a warm radial breath-gradient melts a
  clear window that travels slowly across the headline, letters
  clearing one by one, and one slow de-fog exhale clears the whole
  plate. It belongs because breath is the reader's first act in a
  cold room — you breathe on the glass to read the label — and the
  hero performs it on the monograph's own name before any content
  is asked for.
- **Structure.** A `<header>` plate: the headline and standfirst
  as real DOM text on `--freezer`, overlaid by a frost layer (a
  `div[aria-hidden]` carrying the `--frost` fill + noise texture)
  whose clearing is a radial-gradient mask. The mask is a CSS
  custom property pair (`--breath-x`, `--breath-y`) updated by the
  shared loop; the window radius is 200px at full melt. The hero
  specimen's label (§6.5) — `CRYO-2019-0482`, the deep core of
  Drawer 3 — sits on the plate's lower edge as the first label in
  the store, buff on the steel rail.
- **Motion spec.** Trigger: load, after fonts settle or at the
  900ms font deadline, whichever is first. The window opens at the
  headline's first word (0 → 200px radius over 600ms
  `--ease-exhale`), travels the headline's reading path over
  1,800ms, letters clearing as the window's leading edge passes
  them; then the full de-fog exhale: mask radius expands to cover
  the plate over 1,200ms `--ease-exhale`. The frost layer then
  thins to its resting 30% edge-presence (frost holds the plate's
  corners only) over 800ms `--ease-thaw`.
- **States.** Frosted (pre-arm only; never the shipped state) /
  breathing (window travelling) / de-fogging / thawed-with-edge-
  frost (resting state) / re-frosting (hero scrolled far past —
  corners only, the headline never re-covers).
- **Content merge.** The window travels the headline's own reading
  path and the first label thawed is the hero specimen's — the
  gesture teaches the page's rule (attention thaws) on the title
  itself, and the specimen it names is a real record entry (§6.17)
  whose drawer the reader will meet at §6.2's third drawer.
- **Failure fallback.** Watchdog at 3,000ms from arm: if the
  de-fog has not completed, the frost layer is removed outright —
  opacity 0, `pointer-events: none` — and the plate stands thawed.
  No-JS: the frost layer is never inserted; the plate ships clear.
  The script inserts the frost and arms the watchdog in the same
  frame, so no ordering of failures can strand the headline.
- **Reduced-motion variant.** No frost layer, no breath. The plate
  ships clear with the corner frost printed as a static texture.
- **Performance budget & mobile variant.** One mask update per
  frame from the loop; ≤0.2ms/frame. Mobile (<768px): the window
  radius is 140px, the travel path shortens to the headline's two
  lines, de-fog 900ms — the ceremony is identical, the glass is
  smaller.
- **Choreography timeline (v2).** t=0 fonts settled → t=0–600ms
  window opens at first word → t=600–2,400ms window travels the
  reading path, letters clearing at its edge → t=2,400–3,600ms
  full de-fog exhale → t=3,600–4,400ms frost settles to corners →
  watchdog deadline t=3,000ms from arm passes unused (it precedes
  the de-fog's end deliberately: at 3,000ms the layer is already
  80% clear, and the watchdog only fires if the loop is dead, in
  which case clearing is instant and total).
- **State matrix (v2).** *Rest:* thawed, corner frost only.
  *Hover:* the warm spot (§6.8) applies to the plate's glass —
  a faint re-melt sheen follows the pointer over the corners.
  *Focus:* the hero's label link focuses clear (its corner frost
  lifts) with the standard focus ring. *Active:* n/a.
  *Scrolled-past:* corner frost deepens 10%; headline stays clear
  forever. *Disabled:* n/a. *Touch:* no hover sheen; the ceremony
  is time-driven and identical.
- **Breakpoints (v2).** ≥1200px: window 200px, full path.
  768–1199px: window 170px. <768px: window 140px, path over two
  lines, de-fog 900ms, label moves below the headline.
- **Edge cases & failure modes (v2).** *Slow fonts:* the ceremony
  waits for the 900ms deadline, then runs regardless — a late font
  swap mid-de-fog is acceptable because the mask is on the frost
  layer, not the text. *Reader scrolls during the breath:* the
  ceremony completes off-screen; the hero is thawed on return,
  latched. *Very tall headline (long monograph title):* the path
  is computed from the headline's actual line boxes at arm time.
- **Accessibility spec (v2).** Headline and standfirst are plain
  DOM text, readable by assistive technology from t=0 — the frost
  is a visual overlay only, `aria-hidden`, never a mask on the
  accessibility tree. Contrast in the thawed state: `--ink` on
  `--freezer` 11.6:1. During the breath, transient contrast is
  lower by design for at most 3.6s and the watchdog guarantees the
  end state; the reduced-motion variant removes the transient
  entirely.
- **Tokens consumed (v2).** `--freezer`, `--frost`, `--ink`,
  `--buff`, `--ease-exhale`, `--ease-thaw`, `--loop-lerp` (0.09),
  `--breath-radius` (200px), `--dur-defog` (1200ms).

### 6.2 Sliding cold-store drawers

- **What & why.** Every section is a cold-storage drawer: a
  brushed-steel front carrying the drawer's title and its specimen
  code range, which slides open horizontally as it reaches the
  rail line, revealing the trays inside. It belongs because the
  monograph's chapters *are* stored samples — opening a section is
  pulling the drawer that holds the material the text describes,
  and the slide's weight is the archive's physical truth.
- **Structure.** A `<section>` per drawer: the front is a 96px
  steel band (a real heading + the code range in mono + the
  drawer's logged mean temperature), the interior a tray field
  whose width is clipped by a wrapper as the drawer translates.
  The slide is a `transform: translateX` on the interior wrapper
  driven by the shared loop from the section's lerped progress —
  the front stays, the drawer body rolls out from behind it, like
  a drawer on rails viewed from above the worktop. Eight drawers,
  in the Record's order (§6.17), never re-sorted by the page.
- **Motion spec.** Trigger: the drawer's top crosses the rail
  line (38% viewport height). Slide: 700ms `--ease-drawer`, the
  interior travelling from −64px offset and 0.92 opacity of its
  frost veil to rest. One drawer — the third, Deep Cores, holding
  the hero specimen — *pins* open: while its trays are read, the
  section holds position for its tray field's height (the pin is
  the original's "one drawer pins open horizontally while its
  contents are read"), then releases. Closing: a drawer never
  visibly closes on scroll-past; its frost returns (§6.3) but the
  drawer stays open — a store does not slam drawers at readers.
- **States.** Closed-frosted (pre-arm only) / sliding / open /
  pinned (Drawer 3) / open-frosted (scrolled past, §6.3's frost
  returned, geometry unchanged).
- **Content merge.** The front carries the drawer's real code
  range and mean temperature from the Record; the interior's
  first tray is the drawer's lowest serial. Remove the drawer and
  1/8 of the collection is gone — the slide is the catalogue's
  structure, not a reveal effect applied to generic sections.
- **Failure fallback.** Watchdog per drawer at 2,000ms from arm:
  an un-slid drawer snaps open (transform none, veil removed).
  No-JS: drawers ship open; the script sets the initial offset
  only when it arms, in the same frame as the watchdog. A drawer
  can therefore never be found shut by a reader.
- **Reduced-motion variant.** Drawers ship open; crossing the rail
  line changes nothing geometric. The front's temperature readout
  still ticks (§6.4 is an instrument, not a reveal).
- **Performance budget & mobile variant.** One transform update
  per animating drawer per frame; at most two drawers animate
  concurrently (the loop queues by rail-line order); ≤0.4ms/frame.
  Mobile (<768px): the slide becomes a 40px vertical settle
  (drawers on a phone are pulled toward the reader, not across),
  500ms, pin disabled — Drawer 3 simply opens first in its group.
- **Choreography timeline (v2).** Drawer top crosses rail line →
  t=0 front's code range ticks once (the label registering) →
  t=0–700ms interior slides `--ease-drawer`, frost veil thinning
  → t=500ms first tray's label staggers in (§6.5) → t=700ms rest,
  thaw cycle (§6.3) takes over → (Drawer 3) pin engages at full
  open and holds for the tray field's scroll length → watchdog
  deadline t=2,000ms passes unused.
- **State matrix (v2).** *Rest:* open, frost state per §6.3.
  *Hover:* the front's steel brightens 6% — a hand resting on the
  handle; the drawer does not move. *Focus:* a drawer's heading
  link focuses with ring; keyboard-open is instant (no slide —
  focus goes straight to the first tray). *Active:* n/a.
  *Scrolled-past:* open, re-frosted. *Disabled:* a drawer whose
  holdings are withdrawn (a real catalogue state) prints its
  front with the range struck through in mono and does not open —
  the store admits an empty drawer. *Touch:* identical slide,
  time-driven.
- **Breakpoints (v2).** ≥1200px: slide −64px, pin on Drawer 3.
  768–1199px: slide −48px, pin on. <768px: vertical settle 40px,
  pin off, front height 80px.
- **Edge cases & failure modes (v2).** *Jump-scroll to page
  bottom:* all passed drawers snap open via their watchdogs; the
  reader never meets a shut drawer below the fold. *A drawer with
  one tray (short content):* the slide distance halves — the
  drawer is shallow and the motion says so. *Drawer content
  longer than expected (a ninth tray added in a CMS):* the pin
  length recomputes from the DOM at arm time; nothing is
  hard-coded to eight trays' heights.
- **Accessibility spec (v2).** Each drawer is a `<section>` with
  an `aria-labelledby` heading; the slide is visual only — content
  is in the accessibility tree, in order, from t=0. Focus order
  follows the catalogue (front link, then trays in serial order).
  The front's temperature is text, not a graphic. Touch targets:
  the front's open-control is the full 96px band.
- **Tokens consumed (v2).** `--steel`, `--freezer`, `--ice-line`,
  `--ink`, `--ease-drawer`, `--loop-lerp` (0.09), `--rail-line`
  (38%), `--dur-drawer` (700ms), `--shelf-pitch` (96px).

### 6.3 Thaw / re-frost cycle

- **What & why.** Inside an open drawer, each tray's frost thaws
  from the edges inward, scrubbed to how long the tray sits in
  view; scroll away, and frost creeps back over ~2s. It belongs
  because it is the lab's handling rule made into the page's
  physics: a sample is only clear while attended. Reading is
  thawing; leaving is re-freezing; the cycle is the theme's
  central verb and every other element borrows from it.
- **Structure.** Each tray (§6.12) carries a frost overlay (the
  `--frost` layer + noise, `aria-hidden`) whose clearing is an
  inset mask: the mask's clear region grows from the tray's edges
  toward its centre as the tray's *thaw value* rises. Thaw value
  is computed by the shared loop from dwell: while ≥60% of the
  tray is inside the viewport band, thaw accrues at 1/6 per
  second (full thaw = 6s of attention); outside, frost accrues at
  1/2 per second (full re-frost = 2s). The asymmetry is the
  point: frost is faster than care.
- **Motion spec.** Thaw: mask edges advance under `--ease-thaw`,
  continuous scrub (no keyframes — the value is dwell, not time
  since trigger). At thaw ≥0.85 the tray is *reading-clear*: its
  image finishes its scale (§6.12), its label's `THAWED` stamp
  fades in (200ms), and the thermometer (§6.4) registers the tray
  — once, latched per session. Re-frost: from the moment the tray
  leaves the band, edges creep back under `--ease-frost`; the
  `THAWED` stamp withdraws at frost ≥0.5, but the thermometer
  never un-registers — the store remembers you thawed it.
- **States.** Frosted (thaw 0) / thawing / reading-clear (≥0.85)
  / re-frosting / frosted-again. A tray mid-cycle holds its value
  when the tab loses focus — dwell is visibility, and a hidden
  tab accrues neither thaw nor frost.
- **Content merge.** The thaw is measured on the tray's own
  content: the specimen image clears first at its edges, the
  label clears last (labels sit under the thickest frost, as on
  real trays where the label is under the lid's rim). The cycle
  is not an overlay effect on a card; it is the state of the
  sample.
- **Failure fallback.** The shipped DOM has no frost overlay; the
  script adds overlays only to trays it can also watch. Watchdog:
  any tray whose thaw value has not moved in 4,000ms while in the
  band is forced reading-clear (a stuck sample is thawed by the
  technician, i.e. the fallback). No-JS: no overlays, all trays
  clear — the monograph reads as its print edition.
- **Reduced-motion variant.** No frost overlays at all. Trays are
  clear; the `THAWED` stamp is replaced by a printed line in the
  tray's label, "in store since" (§6.5), so the information the
  cycle carried — what has been attended — is simply not tracked.
- **Performance budget & mobile variant.** Mask updates are one
  style write per in-band tray per frame, ≤0.5ms/frame total for
  the ≤4 trays that can be in band at once. Mobile (<768px): full
  thaw at 4s dwell (smaller glass, faster melt — stated, not
  silent), re-frost 2s unchanged.
- **Choreography timeline (v2).** Tray enters band → t=0 dwell
  begins accruing → edges clear progressively (0–6s) → thaw 0.5:
  image scale completes → thaw 0.85: `THAWED` stamp in (200ms),
  thermometer registers → tray leaves band → frost creeps from
  edges (0–2s) → stamp withdraws at frost 0.5 → tray frosted,
  thermometer unchanged.
- **State matrix (v2).** *Rest (in band):* thawing or clear.
  *Hover:* the warm spot (§6.8) adds a local clear radius on top
  of the dwell thaw — the two systems compose, neither overrides.
  *Focus:* a focused tray accrues thaw at double rate (keyboard
  attention is attention). *Active:* seal-break (§6.9) forces
  instant full clear, permanently for that tray. *Scrolled-past:*
  re-frosting. *Disabled:* a withdrawn specimen's tray (§6.12)
  never thaws — its frost is printed, static, and its label says
  why. *Touch:* dwell only; no warm spot.
- **Breakpoints (v2).** ≥1200px: thaw 6s, band = viewport.
  768–1199px: thaw 5s. <768px: thaw 4s, band requires ≥75% of the
  tray visible (a phone screen shows fewer, larger trays).
- **Edge cases & failure modes (v2).** *Reader scrolls slowly
  back and forth over one tray:* thaw and frost accrue honestly;
  the tray breathes at the band's edge — correct behaviour, the
  sample is half-attended. *A tray taller than the viewport:*
  the band test uses the tray's visible fraction, capped so a
  tall tray can still reach reading-clear. *Loop throttled in a
  background tab:* dwell pauses (visibility-gated), no tray thaws
  unseen — the lab rule, enforced by the platform.
- **Accessibility spec (v2).** Frost is never announced; thaw
  state is decorative except the `THAWED` stamp, which is real
  text appearing in the label (screen readers encounter it in
  reading order, not via live region — a stamp is a fact on the
  label, not an event). All tray text is fully legible in the DOM
  regardless of frost; visual contrast at reading-clear is the
  §2 standard (11.6:1 body). During partial thaw, text contrast
  is transiently reduced for sighted readers only, and the
  watchdog + 6s cap bound it.
- **Tokens consumed (v2).** `--frost`, `--freezer`, `--ease-thaw`,
  `--ease-frost`, `--loop-lerp` (0.09), `--dur-thaw-full` (6s),
  `--dur-refrost` (2s), `--thaw-clear` (0.85).

### 6.4 Header thermometer — the progress instrument

- **What & why.** The header carries a live storage thermometer.
  It opens at −12 °C (the door-side sensor, warm from the room),
  performs a calibration sweep down to the −80 °C setpoint on
  load, returns to the live reading, and then falls one degree for
  every tray the reader thaws, settling at exactly −80 °C when
  all 68 trays have been thawed. It belongs because progress in
  this world is preservation: the more of the archive you have
  read, the colder and safer the store reads. It is the theme's
  progress indicator with the bar refused (§5).
- **Structure.** A mono readout in the header's right cell:
  `STORE −47 °C` in IBM Plex Mono with a thin vertical mercury
  rule (a 2px track, fill height = (display + 12) / 68 of the
  scale from −12 to −80). The number is real text, updated by the
  loop with `--ease-tick` stepping — digits change discretely,
  like an instrument, never roll. Beside it, the over-temperature
  tick: a 6px `--orange` mark that exists in the DOM only as the
  scale's −10 °C warning notch — one of the orange census's three
  licensed sites (§2).
- **Motion spec.** Load: calibration sweep −12 → −80 at 40ms per
  degree (68 steps, 2,720ms), labelled `CAL` in the readout's
  margin; at −80 the `CAL` tag clears and the readout returns to
  the live value over 400ms `--ease-thaw` — the sweep proves the
  instrument's range, then the instrument tells the truth. Reading:
  each tray reaching reading-clear (§6.3) decrements the target by
  exactly 1; the display ticks toward the target at 120ms per
  degree. Final state: 68 trays → −80 °C, where the readout gains
  the fixed string `AT SETPOINT` (§12) and the mercury rests full.
- **States.** Calibrating / live (falling) / at setpoint (all 68
  thawed) / returning-visitor (a repeat visit in the same session
  starts at the session's thawed count — the store remembers the
  technician's round; a new session starts at −12).
- **Content merge.** The thermometer's arithmetic *is* the
  catalogue's: 68 trays (§6.17) ↔ 68 degrees between −12 and −80.
  The number cannot be faked by scrolling — it counts trays
  thawed (§6.3's dwell), not distance travelled. A reader who
  jump-scrolls to the footer has thawed nothing and the store is
  still warm: the instrument reports attention, not position.
- **Failure fallback.** No-JS: the readout prints `STORE −80 °C ·
  SETPOINT` — the store at rest, fully preserved, which is the
  truthful no-script state of a monograph. Loop failure: the
  readout freezes at its last value; nothing is hidden by it (it
  is a header instrument, not a gate). Watchdog: if calibration
  has not finished by 4,000ms, the readout snaps to live.
- **Reduced-motion variant.** No sweep. The readout prints the
  live value and updates it discretely as trays are read (thaw
  tracking itself is §6.3's reduced variant — off — so the
  readout prints `STORE −80 °C · SETPOINT` statically: with no
  frost, everything is already at temperature).
- **Performance budget & mobile variant.** One text write per
  tick, ≤0.05ms. Mobile (<768px): the mercury rule is dropped;
  the readout is the number alone, right-aligned in the header —
  the instrument survives, its glass does not.
- **Choreography timeline (v2).** t=0 header prints at −12 →
  t=300ms `CAL` appears, sweep begins → 68 ticks × 40ms →
  t≈3,020ms −80 reached, `CAL` clears → t=3,020–3,420ms return to
  live −12 → first tray reading-clear: target −13, tick 120ms →
  … → 68th tray: −80, `AT SETPOINT` prints → watchdog deadline
  t=4,000ms passes unused.
- **State matrix (v2).** *Rest:* live value. *Hover:* the readout
  is not interactive; hovering the header cell shows the fixed
  string `1 °C PER TRAY THAWED` as a printed caption beneath —
  the instrument explains itself in the lab's voice. *Focus:* the
  readout is not focusable. *Active:* n/a. *Scrolled-past:* the
  header is sticky; the instrument is always live. *Disabled:*
  n/a. *Touch:* caption on tap of the header cell.
- **Breakpoints (v2).** ≥1200px: readout + mercury + caption.
  768–1199px: readout + mercury. <768px: readout only.
- **Edge cases & failure modes (v2).** *Reader thaws trays in two
  drawers simultaneously (two in band):* decrements queue; the
  display ticks through them in order, never jumps. *Session
  restore mid-page:* thawed latches restore from sessionStorage;
  the thermometer opens at the restored count after calibration.
  *The count and the catalogue disagree (a tray removed in a
  CMS):* the denominator is read from the DOM's tray count at arm
  time, and §6.17's record is the editorial source — if they
  differ, §10's gate fails the build, not the reader.
- **Accessibility spec (v2).** The readout is text; its changes
  are *not* live-announced (68 announcements would be abuse). It
  carries an `aria-label` summary updated at most once per drawer
  ("Store temperature −47 degrees; 35 of 68 trays thawed"). The
  mercury rule is `aria-hidden` decoration beside the number it
  duplicates.
- **Tokens consumed (v2).** `--ink`, `--steel`, `--orange`,
  `--ease-tick`, `--ease-thaw`, `--temp-start` (−12),
  `--temp-setpoint` (−80), `--dur-cal-tick` (40ms).

### 6.5 Specimen-code labels

- **What & why.** Every drawer front, tray, card and table row
  carries a buff specimen label typed in mono with a real taxonomy
  code — collection–year–serial, e.g. `CRYO-2019-0482` — and the
  serials run in true catalogue order across the page, incrementing
  drawer by drawer exactly as the Record declares (§6.17). Labels
  belong because in the store the label *is* the specimen's name;
  the monograph's content is catalogued, not titled.
- **Structure.** A `<span class="label">` (or the label block in
  §6.12's cards): buff ground, `--ink` mono at label size, the
  code, a hairline rule, and the label's state line — `STORED`,
  `THAWED`, `SEAL BROKEN — LOGGED`, or `WITHDRAWN` — in micro-type.
  Labels are DOM text in reading order; the stagger is a transform
  on the label's tray, never a delay on the text's existence.
- **Motion spec.** Trigger: the label's tray or drawer reaches the
  rail line. Labels stagger in cold-store order — drawer order,
  then serial order within the drawer — at 70ms per label,
  each rising 8px and settling over 300ms `--ease-thaw`. A label
  whose specimen's seal is broken (§6.9) gains the orange seal
  dot (6px, the census's second licensed site) at the moment of
  the break, with the state line changing in the same frame.
- **States.** Stored (default) / thawed (state line per §6.3) /
  seal broken (dot + state line, permanent for the session) /
  withdrawn (code struck through, state `WITHDRAWN`, the label
  stays — the store does not pretend a specimen never existed).
- **Content merge.** The label's code is the specimen's key
  everywhere: the same string appears in the tray card (§6.12),
  the ledger table (§6.13), and the Record (§6.17). A reader can
  find any specimen by its code in any representation — the label
  system is the monograph's indexing, performed as typography.
- **Failure fallback.** Labels are static text; the stagger is
  enhancement. Watchdog: any label not settled by 1,500ms from
  its tray's arm snaps to rest. No-JS: labels print in place —
  they are the content's names, and names are never animated into
  existence.
- **Reduced-motion variant.** No stagger, no rise. Labels print;
  state lines still update (a state change is information, set
  discretely).
- **Performance budget & mobile variant.** Transform-only stagger,
  ≤8 labels animating at once, ≤0.2ms/frame. Mobile: stagger
  interval 50ms, rise 6px.
- **Choreography timeline (v2).** Tray crosses rail line → t=0
  first label rises → +70ms per serial → last label settles
  t≈(n×70)+300ms → state line updates thereafter are discrete
  events (thaw, break, withdraw) → watchdog t=1,500ms passes
  unused.
- **State matrix (v2).** *Rest:* stored line. *Hover:* the label
  is part of its tray — warm spot (§6.8) applies to the tray, the
  label's buff warms 4% (a colour change, not motion). *Focus:*
  labels inside links carry the tray's focus ring. *Active:*
  seal-break updates the label (§6.9). *Scrolled-past:* state
  persists. *Disabled:* withdrawn labels are not links.
  *Touch:* identical, minus the buff warming.
- **Breakpoints (v2).** ≥1200px: full label (code + rule + state).
  768–1199px: full label. <768px: code + state on one line, rule
  dropped — the code is never the thing cut.
- **Edge cases & failure modes (v2).** *A serial range with a gap
  (a specimen on loan):* the label sequence skips the serial and
  the tray prints `ON LOAN` in the state line — gaps are
  catalogued, never silently renumbered, because renumbering
  would break every cross-reference in §6.13. *Long collection
  names:* the code format is fixed-width by construction
  (4+4+4); a longer collection code wraps the label, never
  truncates the serial.
- **Accessibility spec (v2).** Codes are text; screen readers read
  them as written (`CRYO-2019-0482` is set with
  `aria-label="Specimen C R Y O 2019 0482"` only where the code
  stands alone as a link's name). Contrast: `--ink` on `--buff`
  10.4:1 at all states; the orange dot is never the sole carrier
  of the broken state — the state line prints it in words.
- **Tokens consumed (v2).** `--buff`, `--buff-deep`, `--ink`,
  `--orange`, `--ease-thaw`, `--dur-label-stagger` (70ms).


### 6.6 Condensation droplets

- **What & why.** On the hero glass, droplets form at random
  points, grow, and slide downward, leaving a clear trail in the
  frost that re-frosts behind them. It belongs because the glass
  sweats for a physical reason the whole theme is built on: the
  room beyond the glass is warm, the store is not. The droplets
  are the temperature difference, visible — atmosphere generated
  by the lab's one fact.
- **Structure.** A canvas-free DOM layer over the hero plate
  (§6.1): at most 14 droplet elements (radial-gradient discs with
  a clear-trail mask on the frost layer beneath), spawned,
  grown and slid by the shared loop. Each droplet: a seed point
  in the plate's upper two-thirds, a growth phase, a slide path
  (vertical, with ≤6px lateral wander), and a trail — a thinning
  clear streak in the frost mask that re-frosts over 3s after the
  droplet passes.
- **Motion spec.** Loop, hero in view only. A droplet forms
  (scale 0 → 1 over 900ms `--ease-thaw`), grows in place for
  2–5s (seeded per droplet), then slides at 30–55px/s (heavier
  droplets faster), trail clearing behind it; at the plate's
  lower edge it merges into the rail and is removed. Spawn rate:
  one new droplet per 1.6s up to the 14 cap; the field is seeded
  deterministically per session so §10 can audit it.
- **States.** Forming / growing / sliding / merged. Paused
  entirely when the hero leaves the viewport (the loop skips the
  layer) and when the tab is hidden.
- **Content merge.** Droplets form on the *glass over the hero
  plate* — the one surface in the theme that is explicitly glass
  over print. Their trails clear the frost over the headline's
  plate, so the ambience literally re-reads the title; they never
  cross labels or body text elsewhere on the page.
- **Failure fallback.** The layer is pure enhancement: if the loop
  is dead, no droplets exist and nothing is missing — the hero's
  own ceremony (§6.1) is independent. No watchdog is needed
  because the fallback state (no droplets) is the shipped state.
- **Reduced-motion variant.** No droplets. The hero plate's frost
  corners carry a static printed droplet texture — the suggestion
  of condensation, frozen, which is the honest reduced form of
  weather.
- **Performance budget & mobile variant.** ≤14 small elements,
  transform + opacity only, ≤0.3ms/frame; the layer is the first
  ambient cut under pressure (§14). Mobile (<768px): cap 8
  droplets, slide speed capped at 40px/s.
- **Choreography timeline (v2).** Hero in view → t=0 first seeds
  form (900ms each, staggered by spawn) → steady state: form →
  grow 2–5s → slide (plate height ÷ speed ≈ 8–14s) → merge →
  trail re-frosts over 3s → spawn cycle continues at 1.6s
  intervals to cap.
- **State matrix (v2).** *Rest:* steady-state field. *Hover:* a
  droplet under the warm spot (§6.8) evaporates — shrinks over
  400ms and is removed; warmth kills condensation, the physics
  holds even here. *Focus:* n/a. *Active:* n/a. *Scrolled-past:*
  layer paused, droplets hold mid-slide and resume on return.
  *Disabled:* n/a. *Touch:* no evaporation (no hover); the field
  runs identically.
- **Breakpoints (v2).** ≥1200px: cap 14. 768–1199px: cap 10.
  <768px: cap 8, trails narrower (3px).
- **Edge cases & failure modes (v2).** *Hero plate resized
  mid-visit (rotation):* droplet positions are stored as plate
  fractions, not pixels, and re-project on resize. *A droplet's
  trail over the hero label:* trails clear frost only; the label
  is buff paper above the glass layer and is never masked.
  *Long-idle page:* the cap and spawn rate are constant — the
  field never densifies into rain; a cold store sweats slowly.
- **Accessibility spec (v2).** The layer is `aria-hidden`,
  `pointer-events: none`, and carries no information; nothing is
  announced, nothing is focusable. It never overlays text at
  reading sizes — droplets are ≤10px and their trails are
  transparency changes in a decorative layer.
- **Tokens consumed (v2).** `--frost`, `--freezer`, `--ease-thaw`,
  `--loop-lerp` (0.09), `--droplet-cap` (14), `--dur-trail`
  (3000ms).

### 6.7 Frost dendrite dividers

- **What & why.** Between drawers, divider plates — steel bands
  carrying the storage fact that separates the two holdings —
  grow a branching frost dendrite across their width: an SVG
  line-work crystal that branches as it centres. It belongs
  because even the punctuation between chapters in this store is
  frost; the divider is a cold plate in the same wall, and the
  fact printed on it ("Drawer 4 begins below −79.6 °C mean") is
  the reason the crystal grows there and not elsewhere.
- **Structure.** An inline SVG per divider (7 dividers, between
  the 8 drawers): a seeded branching path — a main stem with
  60° branches at three depths, generated from the divider's
  index so each plate's crystal is distinct and stable — drawn
  via `stroke-dashoffset` from the shared loop, over the steel
  band, with the divider's fact set in mono at the band's left,
  clear of the growth field.
- **Motion spec.** Trigger: the divider centres in the viewport
  band. Growth: 1,400ms total — stem draws over 500ms
  `--ease-thaw`, first-order branches 500ms, second-order 400ms,
  tips fading in as they extend. Growth is scrubbed to the
  divider's passage (it grows while centred, holds when passed),
  and it is one-directional: scrolling back up does not ungrow a
  crystal — frost that has formed stays until §6.3's rules, not
  the scroll's, remove it. In fact it never removes: a grown
  dendrite is permanent for the session, like frost on the inside
  of a real store's plate.
- **States.** Ungrown (stem only, printed faint) / growing /
  grown (resting). The ungrown state still shows the divider's
  fact in full — the crystal is ornament on a working plate.
- **Content merge.** Each dendrite's branch count is derived from
  the divider's fact: branches = the tens digit of the drawer
  below's specimen count (Drawer 7's 208 specimens → a fuller
  crystal field than Drawer 4's 121) — the growth's density is
  the holding's size, drawn. §10's audit re-derives one divider.
- **Failure fallback.** No-JS / loop dead: dendrites ship in the
  grown state (dashoffset 0); the script rewinds them only when
  arming, with a 2,500ms watchdog per divider that snaps any
  ungrown crystal to grown. A divider can never be found blank.
- **Reduced-motion variant.** Dendrites ship grown. The fact on
  the plate is unchanged.
- **Performance budget & mobile variant.** One dashoffset write
  per growing divider per frame; ≤2 grow concurrently;
  ≤0.2ms/frame. Mobile (<768px): branch depth 2 (the third order
  is cut), growth 1,000ms.
- **Choreography timeline (v2).** Divider enters band → t=0 stem
  draws (500ms) → t=400ms first branches (500ms, overlapping the
  stem's end) → t=800ms second order (400ms) → t=1,400ms grown,
  latched → watchdog t=2,500ms passes unused.
- **State matrix (v2).** *Rest:* grown (after first pass) or
  faint stem. *Hover:* nothing — plates are not interactive.
  *Focus:* n/a. *Active:* n/a. *Scrolled-past:* grown, permanent.
  *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: depth 3, full width. 768–1199px:
  depth 3, growth field 70% of band width. <768px: depth 2,
  1,000ms.
- **Edge cases & failure modes (v2).** *Divider never centred
  (very tall viewport, short page):* the band test uses entry
  into the middle third, and the watchdog covers the rest. *Two
  dividers in band at once:* they grow in catalogue order, the
  loop serialises. *SVG unsupported (legacy):* the band prints
  its fact on plain steel — the plate works, the crystal is
  absent, nothing is hidden.
- **Accessibility spec (v2).** Dendrites are `aria-hidden`. The
  divider's fact is real text in a `<p>`, in reading order,
  `--ink` on steel-band ground at label contrast (the band's text
  sits on a `--freezer` inset chip, 11.6:1 — text never sits
  directly on brushed steel).
- **Tokens consumed (v2).** `--steel`, `--frost`, `--freezer`,
  `--ink`, `--ease-thaw`, `--dur-dendrite` (1400ms).

### 6.8 Warm-spot hover

- **What & why.** Hovering a tray melts a ~90px radius of its
  frost: a radial mask follows the pointer, lerped, clearing the
  specimen beneath; leaving re-frosts over ~1.5s. It belongs
  because inspection warms the sample — the visitor's attention
  is a heat source applied to the specimen itself, the smallest
  and most intimate form of the theme's law.
- **Structure.** Per tray (§6.12), the frost overlay (§6.3) gains
  a second mask layer: a radial-gradient clear disc whose centre
  is a custom-property pair updated by the loop from lerped
  pointer coordinates relative to the tray. The disc composes
  with the dwell thaw mask (union — either system can clear any
  point). Pointer events are read on the tray, throttled by the
  loop; no per-event DOM writes.
- **Motion spec.** The disc follows at the loop's lerp (0.09) —
  a deliberate thermal lag, ~120ms behind a fast pointer, so the
  melt feels like heat soaking through glass, not a spotlight.
  Radius: 90px at full presence, growing 0 → 90px over 250ms
  `--ease-thaw` on entry, shrinking on leave as the re-frost
  (§6.3, 1.5s for the spot's area) closes it. The disc's edge is
  soft: clear at centre, frost at rim, a 30px falloff.
- **States.** Absent / warming (entering) / present (following) /
  re-frosting (leaving). On touch devices the spot does not exist
  — dwell (§6.3) does the work alone, and §6.3's mobile thaw is
  faster for exactly this reason.
- **Content merge.** The spot clears the tray's own frost over
  the tray's own specimen — hovering the label warms the label,
  hovering the image warms the image. It is the same frost the
  dwell system manages, so the two attentions (lingering, and
  pointing) read as one physics.
- **Failure fallback.** If the loop is dead, no spot — and no
  frost either (§6.3's fallback removes overlays), so nothing is
  lost. If pointer tracking fails mid-hover, the spot fades at
  its last position over 1.5s rather than freezing lit.
- **Reduced-motion variant.** No spot, no frost (§6.3). Hover
  still warms the label's buff by 4% (§6.5) — a colour response
  with no mask and no motion.
- **Performance budget & mobile variant.** One custom-property
  write per hovered tray per frame, ≤0.1ms. Mobile: not shipped
  (touch has no hover); the budget is spent on faster dwell thaw
  instead.
- **Choreography timeline (v2).** Pointer enters tray → t=0–250ms
  disc grows to 90px → follows at 120ms thermal lag → pointer
  leaves → disc holds 100ms (heat lingers) → re-frost closes the
  area over 1,500ms → tray returns to its dwell-thaw state.
- **State matrix (v2).** *Rest:* absent. *Hover:* present.
  *Focus:* keyboard focus on a tray applies a centred spot at
  fixed 90px — focus is a warm hand placed deliberately, and the
  focused tray's frost clears at its centre. *Active:* during
  seal-break (§6.9) the spot is superseded by the full clear.
  *Scrolled-past:* spot removed instantly (the hand is gone).
  *Disabled:* withdrawn trays take no spot — their frost is
  printed (§6.3). *Touch:* absent by design.
- **Breakpoints (v2).** ≥1200px: radius 90px. 768–1199px: radius
  80px. <768px: not shipped.
- **Edge cases & failure modes (v2).** *Fast pointer crossing
  many trays:* the lag means the spot trails honestly and dies in
  the tray it last rested in; spots never stack across trays.
  *Pointer leaves the window mid-hover:* the leave path runs from
  the last coordinates. *Spot over a seal-broken tray:* the tray
  is already clear (§6.9); the spot is a no-op and is not drawn.
- **Accessibility spec (v2).** The spot is visual only; it never
  reveals content that is absent from the DOM (the frost is an
  overlay, §6.3), so no information depends on it. Keyboard users
  get the focus variant above plus §6.3's double-rate focus thaw
  — attention parity between pointer and keyboard is specified,
  not hoped for.
- **Tokens consumed (v2).** `--frost`, `--ease-thaw`,
  `--loop-lerp` (0.09), `--spot-radius` (90px), `--dur-refrost-
  spot` (1500ms).

### 6.9 Seal-break click

- **What & why.** Clicking a tray breaks its seal: a fine crack
  line runs across the frost (~350ms), the tray clears fully and
  permanently, and an orange-tagged line appears on its label —
  `SEAL BROKEN — LOGGED`. It belongs because opening a sample in
  the real store is a protocol event: irreversible, witnessed,
  and written down in the warning colour. The click performs the
  protocol on the record, not a generic "expand".
- **Structure.** Per tray: an SVG crack path (a seeded jagged
  polyline across the tray's diagonal, unique per tray index),
  drawn by dashoffset; on completion the frost overlay is removed
  for that tray, the label's state line (§6.5) switches and gains
  the orange seal dot, and the event is written to the session's
  break log, which the footer (§6.16) reports as a count. The
  tray's control is a real `<button>` wrapping the tray's header
  row — "Break seal" is its accessible name until broken, then
  "Seal broken" and disabled.
- **Motion spec.** Trigger: click / Enter / Space on the tray's
  seal control. Crack: 350ms `--ease-crack`, the only fast motion
  in the theme — a violation should feel quick. At the crack's
  end: frost clears over 300ms `--ease-thaw` (the cold rushes
  out, then the sample is simply open), the tag prints on the
  label in the same frame, and the thermometer (§6.4) registers
  the tray instantly if it had not already (a broken seal is a
  completed thaw, by force).
- **States.** Sealed (resting) / cracking (350ms) / broken
  (permanent for the session; on a fresh session the seal is
  intact again — the store re-seals overnight, and §12's voice
  says so). A broken tray no longer re-frosts (§6.3 yields) and
  takes no warm spot (§6.8).
- **Content merge.** The crack runs across the tray's own frost
  over the tray's own specimen, and the log it writes is the
  footer's real count and the form's context (§6.14 notes prior
  breaks when requesting a thaw). The interaction is the lab's
  chain-of-custody, not a card flip.
- **Failure fallback.** If the crack animation fails (loop dead),
  the click still breaks the seal: frost removed, tag printed —
  the protocol is state, not animation; the animation is its
  witness. Watchdog at 800ms: a tray stuck mid-crack completes
  instantly.
- **Reduced-motion variant.** No crack line. The click clears the
  frost instantly and the tag prints — the log entry matters, the
  fracture is theatre that reduced motion honestly drops.
- **Performance budget & mobile variant.** One dashoffset
  animation per break, ≤0.1ms/frame, never concurrent with
  another break (clicks queue at the loop). Mobile: identical;
  the crack path is shorter (tray width), 300ms.
- **Choreography timeline (v2).** Click → t=0 crack strikes
  (350ms `--ease-crack`) → t=350ms tag + dot print on label,
  thermometer registers → t=350–650ms frost clears → tray open,
  control disabled, footer count +1 → watchdog t=800ms passes
  unused.
- **State matrix (v2).** *Rest:* sealed, control enabled.
  *Hover:* the seal control's label line underlines in
  `--frost-deep`; the crack does not preview. *Focus:* ring on
  the control; the tray's frost centre-clears (§6.8 focus rule).
  *Active:* cracking. *Scrolled-past:* broken state persists.
  *Disabled:* after breaking, the control is disabled with its
  name changed — a seal cannot break twice. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: crack across full diagonal.
  768–1199px: full diagonal. <768px: crack across the tray's
  width, 300ms.
- **Edge cases & failure modes (v2).** *Double-click:* the second
  click lands on a disabled control — nothing happens, correctly.
  *Break during the drawer's slide:* the loop queues the crack
  until the slide completes (≤700ms), so the fracture is drawn on
  a still tray. *All 68 seals broken:* permitted; the footer's
  log line reports 68 and §12's voice notes the store will have
  words — the theme does not punish curiosity, it records it.
- **Accessibility spec (v2).** The control is a button with a
  changing accessible name and `aria-pressed`-equivalent state via
  its disabled state + label text; the break is announced once by
  a polite live region ("Seal broken on CRYO-2019-0482. Logged.")
  — an irreversible logged act is worth one announcement, unlike
  ambient thawing (§6.3). The orange dot is never the sole signal:
  the state line prints the words (§6.5). Target: the full tray
  header row, ≥48px tall.
- **Tokens consumed (v2).** `--orange`, `--frost`, `--ink`,
  `--ease-crack`, `--ease-thaw`, `--dur-crack` (350ms).

### 6.10 Freezer-door page transition

- **What & why.** On navigation, the old page frosts over
  completely (600ms), slides away like a freezer door on its rail,
  and the new page de-fogs from its headline outward. It belongs
  because moving between pages in this world is moving between
  cold stores — you close one door before the next room's cold
  reaches you — and the transition is the one moment the whole
  viewport is allowed to be weather.
- **Structure.** A full-viewport frost layer (the §6.1 layer at
  full opacity + noise) and a door transform on the outgoing
  page's main wrapper: the wrapper translates X by 100vw under
  `--ease-drawer` behind the frost, the incoming page is already
  rendered beneath (server-rendered or pre-fetched), and its hero
  runs its de-fog (§6.1's exhale, shortened). In a classic MPA the
  transition degrades to: frost-over on unload is skipped, and
  the incoming page's de-fog carries the whole effect.
- **Motion spec.** Trigger: internal navigation. Frost-over:
  600ms `--ease-frost` to full cover. Door slide: 700ms
  `--ease-drawer`, beginning at 400ms (overlap 200ms — the door
  starts moving while the last frost forms, as a real door's seal
  breaks before it travels). Incoming de-fog: 900ms
  `--ease-exhale` from the headline outward. Total perceived
  interruption ≤1,900ms, watchdogged at 2,200ms.
- **States.** Idle / frosting / sliding / de-fogging / idle. A
  second navigation mid-transition cancels to the newest target —
  doors do not queue.
- **Content merge.** The frost that covers the old page is the
  same layer, texture and colour as every tray's frost; the new
  page's de-fog is its hero's own ceremony (§6.1) at 0.75×
  duration. The transition is made of the pages' own weather, not
  a branded wipe laid over them.
- **Failure fallback.** Watchdog at 2,200ms: any stuck transition
  forces the incoming page fully visible, frost layer removed.
  No-JS / MPA without pre-render: plain navigation; the incoming
  de-fog still runs (it is §6.1's own arm). A transition may never
  strand a reader between stores.
- **Reduced-motion variant.** No frost-over, no slide. Plain
  navigation; the new page arrives thawed (§6.1's variant).
- **Performance budget & mobile variant.** The frost layer is one
  composited element; the slide is one transform; ≤0.6ms/frame.
  Mobile (<768px): the door slides 100vw identically (a small
  store's door is the same door), frost-over shortens to 450ms.
- **Choreography timeline (v2).** Click → t=0–600ms frost-over →
  t=400ms door slide begins → t=1,100ms slide completes, incoming
  page exposed → t=1,100–2,000ms de-fog from headline → page live
  → watchdog t=2,200ms passes unused.
- **State matrix (v2).** *Rest:* idle. *Hover:* n/a. *Focus:*
  focus is moved to the incoming page's heading at de-fog start
  (not at click) — announced once, correctly placed. *Active:*
  mid-transition states above. *Scrolled-past:* n/a. *Disabled:*
  external links never trigger the door (they leave the store;
  the browser's own chrome is the corridor). *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full sequence. 768–1199px: full
  sequence. <768px: frost-over 450ms, slide 600ms, de-fog 800ms.
- **Edge cases & failure modes (v2).** *Back button:* the restored
  page arrives thawed at its restored scroll position — the door
  does not replay for history navigation (the technician re-enters
  a room they were just in). *Slow incoming page:* the frost holds
  at full cover with the store's name printed on it (§6.15's
  loader language) — never a blank white door. *Prefetch failure:*
  degrade to MPA behaviour above.
- **Accessibility spec (v2).** During transition the outgoing page
  is `aria-hidden` once the slide begins; the incoming heading
  receives focus and is announced by the browser's normal page
  semantics. The frost layer is decorative. No content is ever
  *only* available mid-transition.
- **Tokens consumed (v2).** `--frost`, `--freezer`, `--ease-frost`,
  `--ease-drawer`, `--ease-exhale`, `--dur-door` (700ms),
  `--dur-watchdog-door` (2200ms).


### 6.11 Cold-store masthead & rail navigation

- **What & why.** The header is the store's door frame: monograph
  title at left, the rail navigation — links named for the
  drawers and the store's services (Drawers, Ledger, Request a
  Thaw, the Record) — and the thermometer (§6.4) at right. It
  belongs because navigation in a store is signage on the door
  you entered by; the current drawer's link carries a frost tick —
  a 2px `--frost-deep` underline that forms like frost on a rail —
  so orientation is given in the building's material.
- **Structure.** A sticky `<header>` with a real `<nav>`: title
  (Archivo 600, 1.25rem), nav links in mono uppercase micro-type,
  thermometer cell. The current-section tick is a scaleX transform
  on the active link's underline, driven by a scrollspy reading
  the same rail-line boundaries as §6.2 — one source of "where am
  I" for drawers and nav alike. Ground: `--freezer` at 96% with
  the shelving under-rule (2px `--steel` + 1px `--ice-line`).
- **Motion spec.** On load, the tick forms under the first link
  over 400ms `--ease-thaw` after the hero's de-fog begins. On
  section change: the old tick thins (200ms `--ease-frost`), the
  new tick forms (400ms `--ease-thaw`) — frost leaves faster than
  it forms only here, because a rail you are holding is warm.
  Header never hides on scroll: a store's door frame does not
  duck.
- **States.** Rest: current tick formed. Hover: a link's buff
  warms 4% and its label gains the §6.5 underline. Focus: standard
  ring + tick previews the focused link at 50%. Active (current
  drawer): tick full, link in `--ink`. Disabled: a nav item for
  an unpublished drawer prints in `--steel` with no link — an
  empty slot in the rail, admitted.
- **Content merge.** The nav's drawer links are the drawers'
  names and jump to the drawers themselves; the scrollspy's
  boundaries are §6.2's. Navigation, drawers and thermometer are
  three readings of one position in the store.
- **Failure fallback.** Scrollspy failure (observer dead): the
  first tick stays — the reader is somewhere in the store and the
  door is never wrong about existing. No-JS: no tick; all links
  printed and working.
- **Reduced-motion variant.** Ticks swap instantly. Header
  identical otherwise.
- **Performance budget & mobile variant.** Scrollspy via
  IntersectionObserver; zero per-frame cost. Mobile (<768px): the
  nav folds to a single "Drawers" disclosure that opens a
  full-width cold panel (`--freezer`, shelving rule) listing the
  links at 48px targets; thermometer stays visible (§6.4's mobile
  form).
- **Choreography timeline (v2).** Load → hero de-fog begins →
  tick forms 400ms under Drawers → section boundary crossed → old
  tick thins 200ms → new tick forms 400ms → footer reached:
  Record link ticked.
- **State matrix (v2).** *Rest:* current ticked. *Hover:* buff
  warm + underline. *Focus:* ring + 50% tick preview. *Active:*
  current drawer. *Scrolled-past:* n/a (sticky). *Disabled:*
  unlinked steel item. *Touch:* ticks on scrollspy only.
- **Breakpoints (v2).** ≥1200px: full bar. 768–1199px: full bar,
  title shortens to the collection code + "Monograph". <768px:
  disclosure panel; thermometer number only.
- **Edge cases & failure modes (v2).** *A drawer added in a CMS:*
  the nav and the boundary table are built from the DOM's actual
  sections — nav, drawers and spy cannot disagree with the page
  that exists. *Long drawer names:* links abbreviate to the
  drawer's material name (Deep Cores), never the code — the code
  lives on the drawer front.
- **Accessibility spec (v2).** `<header>` + `<nav
  aria-label="Cold store">`; `aria-current="location"` on the
  active link; the tick is `aria-hidden`. Skip link is the
  header's first element, printed on focus. Link contrast:
  `--ink` 11.6:1; steel disabled items are not links and are
  labelled "(not yet stored)".
- **Tokens consumed (v2).** `--freezer`, `--steel`, `--ice-line`,
  `--ink`, `--frost-deep`, `--ease-thaw`, `--ease-frost`,
  `--dur-tick-form` (400ms).

### 6.12 Specimen tray cards

- **What & why.** Inside each drawer, specimens are tray cards:
  the specimen's image in a frosted tray frame, its buff label
  (§6.5) with code and state, its material facts in mono (depth or
  origin, storage days, the drawer's mean temperature), and one
  line of monograph text. The card belongs because a tray is the
  unit a specimen is handled in — the card is not a summary of the
  specimen, it is the specimen, in its tray, on the page.
- **Structure.** A `<ul>` grid of `<li>` cards per drawer, counts
  per the Record (Drawer 3 shows all 10 of its trays' featured
  specimens as cards; other drawers show their featured trays —
  the Record's featured counts are §6.17's table). Each card: a
  `<figure>` with a real `<img>` in the frosted frame (the §6.3
  overlay lives here), the label block, a fact list (`<dl>`), and
  the seal control (§6.9) in the card's header row. Featured
  specimen of the whole monograph: `CRYO-2019-0482`, first card of
  Drawer 3 — an ice-core section, depth 1,842.6 m, in store 2,557
  days.
- **Motion spec.** Cards print in as their drawer opens,
  staggered in serial order at 70ms (with §6.5's labels), rising
  10px over 350ms `--ease-thaw`. Image: scale 1.04 → 1.0 as the
  tray's thaw passes 0.5 (§6.3), scrubbed by the loop — the image
  settles into its frame as the frost leaves it. Tilt: on hover,
  the tray tilts toward the light, max 3°, computed from lerped
  pointer position in the loop (never raw events), settling back
  over 600ms `--ease-drawer` with no overshoot — a tray is heavy
  and does not bounce.
- **States.** Frosted / thawing / reading-clear (§6.3) / seal
  broken (§6.9) / withdrawn (image replaced by the printed line
  "Withdrawn from the store — see the Record", label struck,
  no tilt, no thaw — the tray is empty and says so).
- **Content merge.** Every field on the card is a Record field:
  code, drawer, tray, depth, days, temperature. Every card's
  days-in-store figure is computed from the Record's
  accession date (14 March 2019) to the Record's stated as-of date
  (14 March 2026) = 2,557 days for original-accession specimens;
  later accessions carry their own dates in the Record and their
  own day counts, printed, never rounded to the collection's.
- **Failure fallback.** Cards are complete DOM; frost and tilt are
  loop enhancements with §6.3's watchdogs behind them. Image
  failure: the frame holds the label and the printed line "Image
  not developed" in mono — a missing photograph is an undeveloped
  plate, recorded, never a broken icon.
- **Reduced-motion variant.** No tilt, no stagger, no frost. Cards
  print as a block per drawer; images at scale 1.0.
- **Performance budget & mobile variant.** Tilt math: two lerped
  values on the single hovered card. Images ≤120KB each, WebP,
  lazy below the first drawer. Grid: 4 columns ≥1200px, 2 at
  768–1199px, 1 below 768px; tilt off on touch, stagger kept
  (it is order, not decoration).
- **Choreography timeline (v2).** Drawer opens (§6.2) → cards
  rise in serial order (70ms stagger) → dwell accrues (§6.3) →
  thaw 0.5: image settles → thaw 0.85: label stamps `THAWED`,
  thermometer registers → hover: tilt lerps to ≤3°, warm spot
  (§6.8) → leave: tilt settles 600ms, frost returns per §6.3.
- **State matrix (v2).** *Rest:* per §6.3 frost state. *Hover:*
  tilt ≤3° + warm spot + image +4% brightness (the specimen
  toward the light). *Focus:* tilt none; focus thaw (§6.3) +
  ring on the card's link. *Active:* seal control per §6.9.
  *Scrolled-past:* re-frosted, flat. *Disabled:* withdrawn cards
  — no link, no tilt, printed reason. *Touch:* no tilt; tap =
  navigate (cards link to the specimen's detail page, §7).
- **Breakpoints (v2).** ≥1200px: 4-col, tilt 3°. 768–1199px:
  2-col, tilt 2.5°. <768px: 1-col, tilt off, image aspect fixed
  4:3 to prevent layout shift.
- **Edge cases & failure modes (v2).** *A drawer with 40 featured
  specimens (a grown collection):* the drawer paginates (§11) at
  12 cards; serial order is global, pagination never renumbers.
  *Specimen with no image:* the "not developed" plate is the
  design, not an error state. *Two accessions same day:* day
  counts tie — printed identically, correctly.
- **Accessibility spec (v2).** The card's link has one accessible
  name ("CRYO-2019-0482 — ice core section, 1,842.6 metres, in
  store 2,557 days"); facts are a real `<dl>`. Alt text is a
  specimen description, not "image of specimen". Contrast: facts
  in `--ink` 11.6:1; captions `--steel-dark` 7.1:1.
- **Tokens consumed (v2).** `--freezer`, `--frost`, `--buff`,
  `--ink`, `--steel-dark`, `--ease-thaw`, `--ease-drawer`,
  `--tilt-max` (3deg), `--dur-card-rise` (350ms).

### 6.13 The storage ledger table

- **What & why.** The monograph's plain-truth page element: a
  true data table of the store — one row per drawer, with its
  code range, tray count, specimen count, logged mean temperature
  and storage band — totals row at the foot carrying the Record's
  1,284 specimens and 68 trays. It belongs because a monograph
  that cannot be read as a ledger is a mood; the table is the
  theme's honesty made structural, and §1's when-NOT clause sends
  hurried readers here.
- **Structure.** A semantic `<table>` in its own drawer (the
  Ledger drawer, following Drawer 8): `<caption>` "The store, by
  drawer — Collection Record, §6.17" (in build terms: "The store,
  by drawer"), `<th scope="col">` headers on the buff header band,
  `<th scope="row">` drawer names, tabular mono numerals
  throughout. The header band pins inside the drawer while the
  rows scroll (the theme's second pin, §5). The totals row is
  separated by a steel double rule; its figures are set in
  `--ink` at 500 weight — totals in this store are stated, not
  decorated.
- **Motion spec.** The table does not perform. Rows print with
  their drawer (§6.2). Row hover: the row's ground lifts to
  `--ice-line` at 40% over 200ms `--ease-thaw`, and that drawer's
  mean temperature cell ticks once (re-prints) — the ledger
  acknowledges the hand on it, nothing more. The restraint is the
  spec.
- **States.** Rest: printed. Hover (row): lift + tick. Focus:
  cells are not focusable; a row's drawer link focuses with the
  standard ring and the lift. Provisional: a drawer whose audit
  is pending prints its temperature in `--steel-dark` with the
  state word `PROVISIONAL` in its label cell — the ledger admits
  the state of its own evidence.
- **Content merge.** The table *is* the Record's drawer half
  (§6.17) in reading flow — same ranges, same counts, same means,
  same totals — and its rows link to the drawers (§6.2) whose
  fronts print the same figures a third time. §10's audit checks
  all three printings agree.
- **Failure fallback.** None required: static HTML, CSS hover.
  This table is the fallback's fallback — if every loop and
  overlay fails, the store is still fully legible here.
- **Reduced-motion variant.** Identical, minus the hover
  transition (instant lift) and the tick.
- **Performance budget & mobile variant.** Zero JS. Mobile
  (<768px): the table becomes a stacked ledger — each drawer a
  block with its figures in definition-list layout, same order,
  same totals; horizontal scrolling is never permitted (a ledger
  you must pan is a ledger lost).
- **Choreography timeline (v2).** Ledger drawer opens → table
  printed → header band pins at the drawer's top as rows pass →
  row hover: lift 200ms, temperature ticks → totals row reached:
  nothing happens — totals do not celebrate.
- **State matrix (v2).** *Rest:* printed. *Hover:* row lift +
  tick. *Focus:* drawer link ring + lift. *Active:* n/a.
  *Scrolled-past:* printed. *Disabled:* provisional rows as
  above. *Touch:* tap on a row lifts it for 600ms.
- **Breakpoints (v2).** ≥1200px: full 6-column table.
  768–1199px: 5 columns (storage band folds into the drawer
  cell). <768px: stacked ledger blocks.
- **Edge cases & failure modes (v2).** *A drawer with zero
  specimens (emptied):* the row prints 0 and "none in store" in
  full `--ink` — a zero is data, printed, not dimmed.
  *Means that drift between audits:* the table prints the
  Record's audited means; a live sensor figure never overwrites
  the ledger — the monograph is an edition, not a dashboard.
- **Accessibility spec (v2).** Full table semantics: caption,
  scoped headers, totals in `<tfoot>` with `scope="row"`.
  Contrast: `--ink` on `--freezer` 11.6:1; on the buff band
  10.4:1. Screen readers receive the store in its most native
  form.
- **Tokens consumed (v2).** `--freezer`, `--buff`, `--ice-line`,
  `--ink`, `--steel-dark`, `--steel`, `--ease-thaw`.

### 6.14 Request-a-thaw form & its logged confirmation

- **What & why.** The monograph's conversion: a researcher
  requests a thaw — a specimen brought to reading temperature for
  examination. The form is a ledger block on buff: fields for the
  requester's name and institution, the specimen code (a select
  of the Record's featured specimens plus a free code field), the
  examination date, and the reason. On submit, the confirmation
  is a ledger entry — "Entered as thaw request № 47" — and the
  requested specimen's tray, if on the page, clears its frost in
  answer. It belongs because it is the one place the visitor asks
  the store for warmth, and the store answers in its own protocol:
  numbered, logged, and rationed.
- **Structure.** A real `<form>` with native validation, enhanced
  never replaced: labelled inputs on `--freezer` insets in the
  buff block, mono for the code field. The preamble prints the
  Record's line: "Thaw requests logged: 46. Yours will be № 47."
  — the derivation shown before the visitor writes a word. The
  ration is printed too: "The cold room admits 4 thaws a day.
  Today: 3 taken." On success the form region swaps to the
  confirmation entry; without JS the form posts and the
  confirmation is a server-rendered page with the same entry and
  number.
- **Motion spec.** Field focus: the field's frost edge (a 1px
  `--frost` inner border the form carries as its glass rim) thaws
  — border to `--frost-deep` over 250ms `--ease-thaw` — plus the
  standard focus ring. Submit: the form's block cools (buff
  desaturates 8% over 300ms) while the request is written — the
  "recording" state uses §6.15's unlit-cluster pulse on the submit
  button, never a spinner. Success: the confirmation entry prints
  in with a 400ms rise `--ease-thaw`; at t=200ms the requested
  specimen's tray (if present on the page) begins a full clear
  (§6.3 at 4× rate — the store thaws it for you, once). Error:
  the offending field's label gains the correction mark — a
  steel caret and the printed word "correct this" beside it;
  orange is not spent on errors (§2 census); the error line
  prints beneath in `--ink`.
- **States.** Rest: ledger printed, № 47 promised, 3 of 4 slots
  taken. Focus: rim thaw + ring. Submitting: cooled block, pulse
  on the button, fields disabled. Success: confirmation entry +
  the answering thaw. Error: field marked, line printed, focus to
  first error, values preserved. Store closed (endpoint down):
  the block prints "The ledger is closed today; requests resume
  tomorrow" and holds the entries, unsent and unlost.
- **Content merge.** The form's specimen select *is* the Record's
  featured list; its request number is the Record's count + 1;
  its daily ration (4, with 3 taken) is the Record's handling
  rule, so the confirmation's "slot 4 of 4 today" is derived, not
  invented. The conversion is transacted inside the theme's
  physics — the requested tray actually thaws.
- **Failure fallback.** Submission watchdog at 4,000ms: no
  response → the block warms back, prints "the entry could not be
  written — your words are still here", values intact, submit
  token idempotent per form instance (no double entry). No-JS:
  native post, server confirmation. 
- **Reduced-motion variant.** Confirmation prints instantly; the
  answering tray is already clear (no frost in the variant); the
  recording state is a printed word, "Writing…", in the button.
- **Performance budget & mobile variant.** Form JS ≤5KB gz,
  deferred; the answering thaw reuses §6.3's loop. Mobile
  (<768px): single column, the ration line moves above the fields
  (a phone reader should meet the limit before the form, not
  after), submit full-width ≥48px.
- **Choreography timeline (v2).** Focus → rim thaws 250ms →
  submit → block cools 300ms, pulse → response → entry rises
  400ms → t=200ms requested tray clears at 4× → confirmation at
  rest, focus moved to its heading → watchdog 4,000ms passes
  unused.
- **State matrix (v2).** *Rest:* printed ledger. *Hover:* field
  rim warms (border lightens 10%). *Focus:* rim thaw + ring.
  *Active:* submitting state. *Scrolled-past:* an in-flight
  submission completes regardless. *Disabled:* store-closed
  state. *Touch:* identical; targets ≥48px.
- **Breakpoints (v2).** ≥1200px: two-column ledger (name +
  institution side by side), measure 44rem. 768–1199px: single
  column, 38rem. <768px: single column full measure, ration line
  first.
- **Edge cases & failure modes (v2).** *A code not in the store:*
  the free field accepts it and the entry prints "code not in
  this store — the request is logged as an enquiry": the ledger
  records the ask honestly instead of rejecting the asker.
  *A fifth request today (ration spent):* the form accepts and
  the confirmation reads "№ 47 — held for tomorrow, first in the
  queue": the ration queues, never refuses. *Duplicate request
  (same code, same date):* the entry prints "second request for
  this thaw — corroboration, not duplication", the store's voice
  (§12) treating agreement as evidence.
- **Accessibility spec (v2).** Visible labels, `--ink` on buff
  10.4:1; errors via `aria-describedby` + a polite summary in the
  ledger's words; confirmation is an `aria-live` region announced
  once ("Entered as thaw request number 47"); focus management:
  first error on failure, confirmation heading on success. The
  correction mark is never colour-alone — it is paired with the
  printed word.
- **Tokens consumed (v2).** `--buff`, `--freezer`, `--ink`,
  `--frost`, `--frost-deep`, `--steel`, `--ease-thaw`,
  `--dur-watchdog-form` (4000ms).

### 6.15 Frosted-silhouette loader & skeleton

- **What & why.** Loading in the cold store is a frosted
  silhouette: a region still arriving shows the shape of its
  coming content under full frost — a tray-shaped frost block, a
  label-shaped buff strip under ice — and as the content lands,
  the silhouette thaws (§6.3's physics at load speed) and the
  content prints in. It belongs because a spinner would be a
  machine from another building; a frosted silhouette is the
  store in its dormant state — the same specimen, not yet thawed
  for you.
- **Structure.** Skeleton regions are DOM elements with
  `data-frosted` styling: the `--frost` layer + noise over a
  buff label strip and `--ice-line` cell rules, shaped by the
  region's own box (a card silhouette is card-shaped; a table
  silhouette carries its band). The real content is server-printed
  or injected complete beneath; thawing is a class swap that runs
  the §6.3 mask to clear over 450ms.
- **Motion spec.** Silhouette frost breathes at 6% ±2% opacity on
  a 3.2s sine (opacity only — dormant, not eager). On data: thaw
  450ms `--ease-thaw`, content rising 300ms beneath it. Hard
  ceiling: any region still frosted at 1,500ms prints its content
  anyway — the store does not hold a reader hostage to a slow
  delivery. Transition use: §6.10's door holds this language at
  full cover when an incoming page is slow.
- **States.** Frosted (breathing) / thawing / printed (rest).
  Error (a region's data fails): the silhouette's label strip
  prints "Not delivered — [retry]" in mono with a real retry
  control; the frost stays, honestly — an undelivered specimen is
  still in transit, and the silhouette says so instead of spinning
  forever.
- **Content merge.** The silhouette is shaped like the content it
  precedes and frosted with the content's own weather; a reader
  learns the page's layout from its frozen shapes, so arrival is
  recognition, not surprise.
- **Failure fallback.** Watchdog per region at 1,500ms (print
  regardless). No-JS: no silhouettes exist; content is
  server-printed complete.
- **Reduced-motion variant.** No breathing; silhouettes are static
  frost blocks that swap to print instantly on data.
- **Performance budget & mobile variant.** Silhouettes are CSS
  gradients + the shared noise texture — zero raster, zero
  per-frame JS except the breathing opacity (compositor).
  Mobile: breathing cut (static frost), ceiling 1,200ms (a phone
  reader's patience is a budget too, and the spec spends it
  openly).
- **Choreography timeline (v2).** Region requested → silhouette
  prints with layout → data lands → thaw 450ms, print rises
  300ms → rest. Ceiling 1,500ms forces print. Error → label strip
  prints the retry line.
- **State matrix (v2).** *Rest:* printed content. *Hover:* n/a.
  *Focus:* silhouettes are `aria-hidden`, unfocusable.
  *Active:* the form's submitting button uses this pulse (§6.14).
  *Scrolled-past:* below-fold regions thaw on arrival regardless
  of visibility. *Disabled / no-JS:* server print. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: full treatment. 768–1199px:
  breathing period 3.6s. <768px: static silhouettes, 1,200ms
  ceiling.
- **Edge cases & failure modes (v2).** *Data faster than the
  silhouette's first paint:* the region prints directly — a
  silhouette that never appears is the best kind. *Partial
  delivery (5 of 8 cards):* landed cards print; the rest hold
  frost to their own ceiling, then print their retry lines
  individually — the drawer opens with gaps admitted.
- **Accessibility spec (v2).** Containers carry `aria-busy="true"`
  while frosted and are removed from the tree until printed; one
  polite announcement ("Drawer loaded") fires per drawer, not per
  card. The retry control is a real button, ≥44px.
- **Tokens consumed (v2).** `--frost`, `--buff`, `--ice-line`,
  `--ink`, `--ease-thaw`, `--dur-frost-ceiling` (1500ms).

### 6.16 Handover footer — the shift log

- **What & why.** The footer is the store's handover note: the
  outgoing technician's log for the shift — the collection's
  totals in mono (1,284 specimens · 68 trays · 8 drawers · in
  store since 14 March 2019), the session's seal-break count from
  §6.9's log ("Seals broken this visit: n — the store re-seals
  overnight"), the setpoint line, and the way back to the surface
  (top, the Ledger, the Record). It belongs because a monograph
  ends the way a shift ends: with the store accounted for and
  handed over, not with a marketing sitemap.
- **Structure.** A steel-banded `<footer>`: the log block in mono
  (three lines, tabular), the totals as a `<dl>`, nav links in
  the §6.11 register, and the colophon line in italic Archivo —
  the lab's pencil: "Set in Archivo and IBM Plex Mono. Kept at
  −80 °C." The seal-break count is a live text node written by
  §6.9's log; at zero it prints the fixed string "Seals intact."
- **Motion spec.** The footer does not animate on entry beyond
  the page's print rise. One behaviour: as the footer centres,
  the drawers above complete their re-frost (§6.3) — the store
  tidies itself behind the departing reader, visible if they
  scroll back. The totals never count up here; the footer states
  them, having been counted elsewhere (§6.12, §6.13).
- **States.** Rest: printed log. Session with breaks: the count
  line updates in place (discrete text change, no motion).
- **Content merge.** The footer's totals are the Record's totals
  in their third printing (§6.13 is the second, §6.17 the first)
  — §10 audits the three. The seal count is the session's real
  §6.9 log. Nothing in the footer is decorative copy.
- **Failure fallback.** Static HTML. The seal count without JS
  prints "Seals intact." — true of a visit that broke none.
- **Reduced-motion variant.** Identical.
- **Performance budget & mobile variant.** Zero JS beyond the
  count's text write. Mobile: the log stacks; totals in two
  columns.
- **Choreography timeline (v2).** Footer enters → print rise
  300ms → (above) re-frost completes → seal line reflects the
  session's final count → rest.
- **State matrix (v2).** *Rest:* printed. *Hover:* links per
  §6.11. *Focus:* standard rings. *Active:* n/a.
  *Scrolled-past:* n/a (it is the past). *Disabled:* n/a.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: log and totals side by side.
  768–1199px: stacked, totals 3-col. <768px: stacked, totals
  2-col.
- **Edge cases & failure modes (v2).** *A session with 68 breaks:*
  the line prints 68 and adds the fixed string "— a full audit
  will follow." (§12) — the store's dry voice, written in advance.
  *Record totals change between editions:* the footer reads the
  same Record object as §6.13/§6.17 at build time; editions are
  versioned in the colophon.
- **Accessibility spec (v2).** `<footer>` landmark; totals as a
  `<dl>`; contrast `--ink` on the steel band's `--freezer` inset
  chips 11.6:1 (text never sits on brushed steel, §6.7's rule).
- **Tokens consumed (v2).** `--steel`, `--freezer`, `--ink`,
  `--ease-thaw`.

### 6.17 The Collection Record — the one source of every figure

- **What & why.** The declared record from which every figure on
  the page derives: the collection is the
  **Meridian Cold Store Collection**, accessioned under code
  `CRYO`, first accession 14 March 2019. The monograph's as-of
  date is 14 March 2026. This section is the record itself,
  printed in the monograph as its final drawer — a site built in
  this theme declares its own record in the same shape, and §10's
  gate audits the page against it.
- **Structure.** The record as data (a table + a machine-readable
  JSON block in the build): eight drawers, each with name, code
  range, tray count, specimen count, logged mean temperature;
  the collection totals; the handling rules (thaw ration, seal
  protocol); the accession and as-of dates.
- **Motion spec.** None. The record is the still point the page's
  weather moves around. Its drawer prints like any other (§6.2)
  and that is all.
- **States.** Printed. A record under audit prints the edition
  line "Edition under audit — figures provisional" (§6.13's
  provisional rule applies here first).
- **Content merge.** Total — this *is* the content every other
  element merges with:

| Drawer | Name | Code range | Trays | Specimens | Logged mean |
|---|---|---|---|---|---|
| 1 | Surface Snow & Firn | CRYO-2019-0001 – 0172 | 9 | 172 | −79.6 °C |
| 2 | Shallow Cores | CRYO-2019-0173 – 0320 | 8 | 148 | −80.4 °C |
| 3 | Deep Cores | CRYO-2019-0321 – 0516 | 10 | 196 | −79.8 °C |
| 4 | Tissue Vials | CRYO-2019-0517 – 0637 | 7 | 121 | −80.1 °C |
| 5 | Seed Duplicates | CRYO-2019-0638 – 0801 | 9 | 164 | −79.9 °C |
| 6 | Microbial Mats | CRYO-2019-0802 – 0938 | 8 | 137 | −80.3 °C |
| 7 | Sediment Traps | CRYO-2019-0939 – 1146 | 11 | 208 | −79.7 °C |
| 8 | Reference Standards | CRYO-2019-1147 – 1284 | 6 | 138 | −80.2 °C |
| **Total** | | | **68** | **1,284** | **−80.0 °C (mean of means)** |

  The arithmetic, checkable by any reader: trays 9+8+10+7+9+8+11+6
  = 68 — which is why the thermometer (§6.4) falls exactly 68
  degrees from −12 to −80, one per tray. Specimens
  172+148+196+121+164+137+208+138 = 1,284, and the serial ranges
  are contiguous and exhaustive: each drawer's first serial is the
  previous drawer's last + 1, ending at 1284. The means sum to
  −640.0, so the collection's mean of means is exactly −80.0 °C —
  the setpoint is the collection's average truth, not a hope.
  Featured specimen: `CRYO-2019-0482` (Drawer 3's range, 0321–0516
  ✓), ice-core section, depth 1,842.6 m; deepest specimen
  `CRYO-2019-0516` at 2,803.4 m. Days in store for original
  accessions: 14 Mar 2019 → 14 Mar 2026 = 2,557 days (7 × 365 + 2
  leap days, 2020 and 2024). Handling rules: 4 thaws admitted per
  day; 3 taken today; thaw requests logged 46 (§6.14's № 47
  derives). Seal protocol: breaks are logged, never hidden (§6.9,
  §6.16).
  Featured trays — the specimens given cards (§6.12) on the home
  wall: Drawer 1: 4, Drawer 2: 4, Drawer 3: 10 (all of its trays —
  the deep cores are the collection's reason to exist), Drawer 4:
  3, Drawer 5: 4, Drawer 6: 3, Drawer 7: 5, Drawer 8: 3 — total
  36 featured cards, each a real serial inside its drawer's range,
  listed in the build's record object in serial order. The other
  1,248 specimens are present as the drawers' counts, the ledger's
  rows and their ranges: a specimen does not need a photograph to
  be in the store, and the monograph never implies the featured 36
  are the collection. On a drawer page (§7) every specimen in the
  range gets a card, paginated — the home wall is the storefront,
  not the store.
- **Failure fallback.** The record is static text and a build-time
  data object; if the two disagree, §10 fails the build. On the
  page it cannot fail — it is print.
- **Reduced-motion variant.** Identical.
- **Performance budget & mobile variant.** Zero. Mobile: the
  record table stacks like §6.13's.
- **Choreography timeline (v2).** None — stated so a builder does
  not invent one.
- **State matrix (v2).** *Rest:* printed. *Hover:* rows per
  §6.13. *Focus:* n/a. *Active:* n/a. *Scrolled-past:* printed.
  *Disabled:* provisional edition state as above. *Touch:*
  identical.
- **Breakpoints (v2).** As §6.13's table at all three bands.
- **Edge cases & failure modes (v2).** *A specimen withdrawn:*
  counts do not change — withdrawn specimens remain in the store's
  count with their state printed (§6.5); the record counts what
  the store holds, including its losses. *A new accession year:*
  a new collection code block (CRYO-2027-…) appends; ranges never
  rewrite history.
- **Accessibility spec (v2).** As §6.13: full table semantics;
  the derivation paragraph is plain text following the table.
- **Tokens consumed (v2).** `--buff`, `--ink`, `--steel`.

### 6.18 Unthawed water — the empty state & 404

- **What & why.** Where the store finds nothing — a search with
  no specimen, a code that does not exist, a page not in the
  monograph — the answer is an empty drawer: a drawer front,
  opened, holding one frosted empty tray and the lab's plain
  statement. The 404 is the full-page form: "This code is not in
  the store." It belongs because absence in an archive is a
  finding, not an error: the store has checked its drawers and
  reports the shelf empty, with the way back printed as real
  links (the Drawers, the Ledger, Request a Thaw — a code from
  another store is a plausible reason to be here).
- **Structure.** The empty drawer (§6.2's geometry, opened,
  static) containing one empty tray outline in `--ice-line`, the
  statement in Archivo, the searched code (if any) in mono on a
  buff label stamped `NOT IN STORE`, and the exits. The frost on
  the empty tray never thaws — there is nothing under it, and the
  theme does not pretend otherwise.
- **Motion spec.** The drawer is already open when found (no
  slide — an empty drawer is not a reveal). The one motion: the
  `NOT IN STORE` stamp settles onto the label over 300ms
  `--ease-drawer` as the page centres. Nothing else moves; an
  empty shelf is still.
- **States.** Rest: printed absence. Search-empty and 404 share
  the element; the search form variant keeps the query in its
  field above the drawer.
- **Content merge.** The empty drawer is a real drawer in the
  wall's geometry, at the position the missing thing would have
  occupied in reading order — absence takes up its true space in
  the store, neither hidden nor inflated.
- **Failure fallback.** Static HTML; the element *is* a fallback
  state for other systems and needs none of its own.
- **Reduced-motion variant.** Identical (the stamp prints).
- **Performance budget & mobile variant.** Zero JS. Mobile: the
  drawer stacks identically; exits full-width.
- **Choreography timeline (v2).** Page centres → stamp settles
  300ms → rest. That is the whole timeline, deliberately.
- **State matrix (v2).** *Rest:* printed. *Hover:* exits per
  §6.11. *Focus:* the first exit receives the page's initial
  focus path after the heading. *Active:* n/a.
  *Scrolled-past:* n/a. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** All bands: same drawer, exits stack
  below 768px.
- **Edge cases & failure modes (v2).** *A code that exists but is
  withdrawn:* not this element — the specimen's own tray (§6.12)
  answers, with its reason. The 404 is only for what was never in
  the store. *A mistyped code one digit off a real one:* the
  statement adds the fixed line "Nearest in store: CRYO-2019-0482"
  when a unique near match exists — the lab helps, in mono,
  without guessing aloud.
- **Accessibility spec (v2).** The heading is the statement
  itself; the searched code is text; exits are links with real
  names. Contrast standard throughout (11.6:1).
- **Tokens consumed (v2).** `--ice-line`, `--buff`, `--ink`,
  `--steel`, `--ease-drawer`.


## 7. Page application map

| Page type | How the theme plays |
|---|---|
| **Home (the monograph)** | The full wall: breath-melt hero (§6.1), eight drawers (§6.2) with tray cards (§6.12), dendrite dividers (§6.7), the Ledger drawer (§6.13), the Record drawer (§6.17), handover footer (§6.16). The thermometer's full journey lives here. |
| **Drawer / listing page** (one drawer, all its specimens) | The drawer opens without the wall: its front becomes the page header, trays paginate at 12 (§11), the drawer's mean temperature replaces the store thermometer as the header instrument (same mechanics, the drawer's own band). Seal-break and thaw rules unchanged. |
| **Specimen detail** | One tray, full width: the specimen's image large in its frosted frame, its label at reading size, its full fact record as a ledger block, its handling history (accession, thaws logged, seals) in mono. The warm spot (§6.8) is at its most intimate here; the page's single drawer is this specimen's. |
| **About / the laboratory** | Told as the store's own record: the building, the setpoint, the staff as the Record's custodians. Photographs sit in frosted frames (§6.12's treatment); the prose is monograph prose, no drawers — the about page is the one room that is not cold storage, and it is styled as the office by the door: same palette, no frost. |
| **Request / contact** | §6.14's form is the page. No other conversion furniture exists in this theme — no chat widget, no callback pop-up; you write in the ledger or you do not write. |
| **Search results** | A temporary drawer (§6.18's geometry, populated): results as tray cards in serial order regardless of match rank — the store does not reorder its shelves for a query; the match line on each label states why it was pulled. Empty search → §6.18. |
| **404** | §6.18, full page. |
| **Checkout / commerce** | Refused. A cold store does not sell from the shelf; institutions request thaws (§6.14) and custody transfers happen off-page, in writing. A build that needs checkout needs another theme for those pages, and §10 fails a monograph that bolts a cart onto a drawer. |

## 8. Worked examples

### 8.1 The hero — breath on the glass (worked example 1)

The visitor arrives. The header prints: title, rail nav, and the
thermometer at `STORE −12 °C` with its `CAL` tag lit. The hero
plate is clear in the DOM — headline "The Meridian Cold Store
Collection", standfirst, and the buff label of `CRYO-2019-0482` on
the steel rail — and in the same frame the script lays the frost
layer over it and arms the 3,000ms watchdog. At t≈300ms the
calibration sweep begins in the header: −13, −14, … one tick per
40ms, the mercury rule sinking. On the plate, the breath window
opens at the headline's first word (600ms), then travels the
reading path over 1,800ms; letters clear as its leading edge
passes, and the visitor understands — before reading a word of
explanation — that attention is what thaws things here. At
t≈2,400ms the full de-fog exhale runs (1,200ms); the frost
retreats to the plate's corners. In the header the sweep reaches
−80 at t≈3,020ms, `CAL` clears, and the readout returns over
400ms to the live −12 °C: the instrument has proved its range and
now tells the truth. The hero specimen's label is the first
`STORED` label the visitor has seen; below the fold, Drawer 1's
front waits with its range `CRYO-2019-0001 – 0172` and its mean,
−79.6 °C. Total ceremony: ≈4.4s, every millisecond of it
skippable by scrolling — the hero is thawed and latched whenever
the visitor returns to it.

### 8.2 Mid-page — Drawer 3, the deep cores (worked example 2)

The visitor has thawed trays in Drawers 1 and 2; the thermometer
reads −29 °C (17 trays: 9 + 8 ✓). The dendrite divider above
Drawer 3 grows as it centres — a fuller crystal than Drawer 2's,
because its branch count derives from the 196 specimens below it.
Drawer 3's front crosses the rail line: its code range ticks once,
the interior slides open over 700ms `--ease-drawer`, and because
this is the pinned drawer, the section holds while its tray field
is read. The first card is `CRYO-2019-0482` — the hero's label,
met again in its tray. The visitor dwells: frost clears from the
core photograph's edges inward over 6s; at thaw 0.5 the image
settles into its frame; at 0.85 the label stamps `THAWED` and the
header ticks to −30 °C. They hover the next tray — a warm spot
blooms under the pointer, lagging 120ms like heat through glass —
then click a third tray's seal: the crack strikes in 350ms, the
label prints `SEAL BROKEN — LOGGED` with its orange dot, the
footer's count silently becomes 1, and the tray stays clear when
they scroll on — while its merely-thawed neighbours re-frost
behind them over 2s. One drawer has taught the whole protocol:
dwell, warmth, and the one irreversible act.

### 8.3 Conversion — requesting a thaw (worked example 3)

Below the Ledger drawer sits the buff ledger block. Its preamble
has already made two promises in mono: "Thaw requests logged: 46.
Yours will be № 47." and "The cold room admits 4 thaws a day.
Today: 3 taken." The researcher selects `CRYO-2019-0482` from the
specimen list — the same core they broke the seal on in §8.2; the
store remembers, and the form's note line says so: "Seal broken
this visit — the thaw will be supervised." They type their
institution, pick a date, write one sentence of reason. On submit
the block cools, the button pulses its unlit frost cluster
(§6.15) — no spinner — and at response the confirmation entry
rises: "Entered as thaw request № 47 — CRYO-2019-0482 — slot 4 of
4 today." Above, in Drawer 3, the specimen's tray clears its
frost at 4× rate in answer: the request has physically reached
into the store. Focus sits on the confirmation heading; the live
region has announced the number once. Had the endpoint failed,
the 4,000ms watchdog would have warmed the block back with their
words intact and the line "the entry could not be written — your
words are still here". Had they asked for a fifth thaw, the entry
would read "held for tomorrow, first in the queue" — the ration
queues; it never refuses.

## 9. Anti-slop — what makes THIS theme look cheap

1. **Blue glassmorphism frost.** Frost rendered as a translucent
   blue blur panel is a UI kit, not weather. *Cure:* frost is
   `--frost` at 82% over `--freezer` with the noise texture and a
   mask — matte, granular, never a backdrop-blur.
2. **Frost that hides content from the DOM.** A reveal that ships
   text at opacity 0 "under frost" breaks the law and the reader.
   *Cure:* content prints complete; frost is an inserted overlay
   with a watchdog (§6.3). §10 tests with JS disabled.
3. **Random specimen codes.** Codes invented per component
   (`CRYO-X92`, serials out of order) dissolve the catalogue.
   *Cure:* every code from §6.17's ranges, in order; §10 greps
   for out-of-range serials.
4. **A thermometer that counts scroll.** Progress-by-distance is
   a progress bar in a lab coat. *Cure:* the thermometer counts
   trays thawed by dwell (§6.3/§6.4) — jump-scrollers stay warm.
5. **Orange as brand colour.** A CTA in warning orange teaches
   visitors that alarms are marketing. *Cure:* the census (§2) —
   orange exists three times, all of them warnings or logs.
6. **Bouncy drawers.** A drawer that overshoots reads as a toy
   kitchen. *Cure:* `--ease-drawer` only, lerp 0.09, no spring
   anywhere in the theme.
7. **Snowfall particles.** Falling snow is a screensaver and a lie
   (it does not snow inside a −80 °C store; frost forms still).
   *Cure:* the only ambient motions are droplets forming on glass
   and frost-noise crawl (§5) — both are stillness-adjacent.
8. **Generic card grids.** Tray cards restyled as SaaS cards
   (shadow, radius, icon) break the store. *Cure:* trays are
   flat, steel-ruled, label-first (§6.12); radius is 0 everywhere
   except droplet discs.
9. **Thermometer in the hero as decoration.** A big temperature
   that means nothing is data-slop. *Cure:* the only temperatures
   are the header instrument (live) and Record figures (audited).
10. **"Ice" gradients and aurora washes.** Decorative cold-colour
    gradients belong to a spa brand. *Cure:* flat tokens only;
    the palette table (§2) is exhaustive.
11. **Labels as badges.** Buff pills with icons are not labels.
    *Cure:* §6.5's format — mono, ruled, state line — or it is
    not a label and may not wear buff.
12. **A loader spinner.** *Cure:* §6.15's frosted silhouettes.
    Anything that spins in this theme fails review on sight.

## 10. Quality gate

Blocking checks — the theme may not ship in a build until all
pass, verified by a non-builder:

1. **Figure audit.** Every number on the page traces to §6.17:
   trays sum to 68, specimens to 1,284, ranges contiguous, means'
   mean exactly −80.0, days 2,557, request count 46 → № 47,
   ration 4 with 3 taken. Any orphan figure fails.
2. **Three-printings agreement.** Drawer fronts (§6.2), the
   ledger table (§6.13) and the Record (§6.17) print identical
   ranges, counts and means.
3. **No-JS read.** With JavaScript disabled the entire monograph
   reads, drawers open, frost absent, form submittable.
4. **Watchdog drill.** Loop killed mid-visit: every armed element
   reaches its thawed/printed state within its watchdog deadline
   (hero 3,000ms, drawers 2,000ms, trays 4,000ms, door 2,200ms).
5. **Orange census.** `grep` for `#E4572E` uses: crack paths, seal
   dots, thermometer tick — and nothing else. Orange text: zero.
6. **Code census.** Every specimen code on the page falls inside
   §6.17's ranges and appears in serial order within its drawer.
7. **Thermometer honesty.** Jump-scroll test: footer reached with
   zero trays thawed → readout still −12 °C (or session-restored
   value). Dwell test: 68 trays → exactly −80 °C + `AT SETPOINT`.
8. **Reduced-motion pass.** With `prefers-reduced-motion`: no
   frost, no slide, no crack, no droplets; all content printed;
   the form and ledger fully usable.
9. **Cursor rule.** No custom cursor, no `cursor: none`, no
   cursor follower anywhere in the build.
10. **Loop census.** Exactly one rAF loop; exactly two ambient
    loops (§5); no CSS keyframe animation outside §6.6's droplet
    opacity and §6.15's breathing.
11. **Contrast audit.** Body 11.6:1, captions 7.1:1, labels
    10.4:1 measured on the shipped tokens; frost states never
    carry text that exists only under frost.
12. **Print pass.** The print stylesheet shows the monograph
    thawed and complete, ledger and record included.


## 11. Component inventory

Every component a real monograph site needs, with its themed
treatment — and the refusals, which are part of the theme:

| Component | Treatment in this theme |
|---|---|
| Primary button | Flat steel-ruled rectangle, `--ink` text on `--freezer`, 2px `--steel` border; hover warms the border to `--frost-deep`; active presses 1px. No fill, no radius, no orange — the store's buttons are labels you can press |
| Secondary button | Borderless mono uppercase with the §6.5 underline; the label register |
| Seal control | §6.9's tray-header button; its own component, never reused for anything but breaking a seal |
| Text input | `--freezer` inset in the buff block, 1px steel rule, mono for codes / Archivo for prose; focus = rim thaw (§6.14) + 2px ring |
| Select | Native select, styled ground only; the specimen select lists featured codes in serial order |
| Checkbox / radio | Square, steel-ruled, filled with `--frost-deep` when checked — a frost tick, not a checkmark glyph |
| Table | §6.13's ledger; the only table style in the theme |
| Badge / tag | Refused as a component class. State is carried by label state lines (§6.5) and the one seal tag (§6.9). A generic badge is slop here |
| Alert | A ledger note: a buff block with a steel caret and the fact in mono, inline where it belongs. Never a banner, never orange |
| Toast | Refused. The store does not interrupt; outcomes print where the act happened (§6.14's entry, §6.16's log) |
| Modal | Refused. There is no room inside the room; specimen detail is a page (§7), not an overlay |
| Tabs | Refused. Drawers are the theme's one sectional device (§6.2) |
| Accordion | Refused, same reason — a drawer that is not a drawer is a lie |
| Pagination | Mono page line under a drawer listing: "Trays 1–12 of 196 · next" — serial ranges, not numbered pills |
| Breadcrumbs | A mono custody line: `STORE / DRAWER 3 / CRYO-2019-0482` — chain of custody, not site hierarchy |
| Search input | Header-adjacent, mono, placeholder "Specimen code or material"; results per §7, absence per §6.18 |
| Progress | §6.4's thermometer. No bar component exists |
| Loader | §6.15's frosted silhouettes. No spinner component exists |
| Tooltip | Refused. Instruments explain themselves in printed captions (§6.4's hover line) |
| Card | §6.12's tray. No other card exists |
| Form errors | §6.14's caret + printed line. No red, no shake |
| Empty state | §6.18's empty drawer |
| Dark mode toggle | Refused — §2: the store is lit like a laboratory at all hours |

## 12. Content & copywriting voice

Two registers, never mixed. **The Instrument** (IBM Plex Mono,
uppercase micro-type or tabular statements) reports: temperatures,
counts, states, log lines. **The Monograph** (Archivo, sentence
case) explains: what a specimen is, why it is kept, how to handle
it. A sentence that measures is set by the Instrument; a sentence
that means is set by the Monograph.

**Headline style.** A specimen or a holding, named plainly: "The
Meridian Cold Store Collection", "Deep Cores", "Drawer 3 — Deep
Cores". Never a promise, never a verb phrase, never "Discover the
frozen world of…". ✓ "Surface Snow & Firn" ✗ "Explore our icy
treasures!"

**Label style.** Fixed strings, verbatim, everywhere:
`STORED` · `THAWED` · `SEAL BROKEN — LOGGED` · `WITHDRAWN` ·
`ON LOAN` · `NOT IN STORE` · `AT SETPOINT` · `1 °C PER TRAY
THAWED`. New state strings require a Record amendment (§6.17),
not a copywriter's afternoon.

**Error voice.** The ledger corrects without scolding, in the
Instrument register, stating the fact and the remedy: ✓ "Code not
in this store — check the serial and write again." ✗ "Oops! That
specimen doesn't exist." The word "oops" is banned from the
building, along with "just", "simply", and every exclamation mark
outside a specimen's historical name.

**Empty-state voice.** A finding, stated: "This code is not in
the store." + the nearest holding when one exists (§6.18). Never
"Nothing here yet!" — the store is not embarrassed by an empty
drawer.

**Numbers voice.** Figures are printed with their units and their
provenance nearby: a temperature is `−79.8 °C (logged mean,
Drawer 3)` at first use on a page, bare thereafter. Counts are
never rounded in the Instrument register: 1,284, not "1.2k+" —
a store that rounds its holdings does not know them.

**The reduced-motion store, in voice.** Where the standard
requires the variant to be described (§5, §6), the monograph's own
pages describe it as "the lights-on store": everything thawed,
everything printed — the voice treats reduced motion as a
different lighting condition of the same building, never as a
lesser edition.

## 13. Full-page scroll choreography map

The home page, top to footer, in order — every beat the visitor
meets, and what carries it:

1. **Arrival.** Header prints; thermometer calibrates (−12 → −80,
   `CAL`) and returns to live −12 (§6.4). Hero frost armed.
2. **The breath.** Window travels the headline; de-fog exhale;
   frost to corners (§6.1). Droplets begin forming on the glass
   (§6.6).
3. **Divider into Drawer 1** — dendrite grows (stem, branches,
   tips) as it centres (§6.7).
4. **Drawer 1 opens** at the rail line (700ms slide); labels
   stagger in serial order (§6.2, §6.5). Dwell thaw begins on the
   first trays (§6.3); the thermometer's first tick falls when
   the first tray stamps `THAWED`.
5. **Drawers 2–8 repeat the grammar** with their own facts: each
   front's range and mean, each divider's dendrite density from
   the drawer below's count, each tray's thaw on dwell. Warm
   spots under the pointer throughout (§6.8); a seal-break
   whenever the visitor chooses (§6.9) — the map does not schedule
   violations.
6. **Drawer 3 pins** while its ten trays are read (§6.2); the
   hero specimen's card is the map's centre of gravity.
7. **The Ledger drawer** opens on the table (§6.13); its buff
   band pins inside the drawer while rows pass; totals state
   68 / 1,284 without ceremony.
8. **The form's bench space** — 64px of cold air — then the buff
   ledger block (§6.14) with its two promises printed before its
   fields.
9. **The Record drawer** (§6.17): the table again, as the source,
   with the derivation paragraph — the visitor who reads to here
   can check every number they have seen.
10. **The handover footer** (§6.16): totals a third time, the
    session's seal count, the colophon. Above it, the drawers
    complete their re-frost; the store is tidy behind the
    departing reader.

**Reverse pass.** Scrolling up: drawers stay open, dendrites stay
grown, broken seals stay broken, thawed trays re-frost and may
re-thaw — the only beats that reverse are thermal ones (§6.3),
because cold is the only thing here that comes back. **Jump
scroll:** watchdogs snap every passed drawer open and every
divider grown; the thermometer reports thawed trays only — a
jumped-to footer is honest about the unread drawers above it.

**The returning visit.** A second visit in a new session replays
the map with two differences, both stated in the open: the hero's
breath ceremony runs at 0.6× duration (the visitor has breathed on
this glass before), and seals are intact again — the store
re-sealed overnight, and the footer's line (§6.16) says so rather
than letting the visitor wonder whether their break was forgotten.
Within a session, the map is stateful as specified: thawed counts
persist, broken seals persist, the thermometer opens where the
round left it. Nothing else about the choreography changes —
a store does not rearrange its drawers for a familiar face.

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Total page weight (home, first load) | ≤640KB (HTML/CSS/JS + above-fold media) |
| JavaScript | ≤38KB gz total: the shared loop + thaw/dwell engine ≤18KB, transition/form ≤12KB, scrollspy/misc ≤8KB |
| CSS | ≤30KB gz |
| Fonts | Archivo (2 weights) + IBM Plex Mono (2 weights), subset, ≤90KB total, `font-display: swap` with the 900ms ceremony deadline (§6.1) |
| Images | ≤120KB per specimen image, WebP/AVIF, responsive sizes; ≤6 images decoded above the fold |
| Animation frame budget | ≤1.2ms of JS per frame at steady state (loop + ≤4 in-band trays + ≤2 animating drawers/dividers); compositor-only transforms/opacity/masks beyond that |
| Long tasks | None >50ms after load; dwell computation is O(in-band trays) |
| Ambient cost | Droplets ≤0.3ms/frame; frost-noise crawl is a background-position drift, compositor-only |

**Cut order when the budget is exceeded** (in this order, and
§10 re-checks after cuts): (1) frost-noise crawl; (2) droplet
cap 14 → 8; (3) dendrite third-order branches; (4) tray tilt;
(5) image count per drawer (featured trays only). **Never cut:**
the watchdogs, the no-JS completeness, the thermometer's honesty,
the Record's figures, reduced-motion variants. A build that meets
budget by cutting a fallback has not met the budget.

**Low-power / constrained devices.** When the loop measures
sustained frame times >24ms, it sheds in the cut order above,
automatically, and the page remains the same monograph with less
weather. Battery-saver and `prefers-reduced-motion` converge on
the lights-on store (§12). Shedding is announced nowhere on the
page — a visitor on a weak device is owed the same monograph, not
an apology — but it is recorded in the build's telemetry as the
cut level reached, so a store whose visitors all read at cut
level 4 has a performance finding, not a design preference.

## 15. Build-order checklist

1. **The Record first.** Encode §6.17 as the build's single data
   object; generate ranges, counts and the thermometer's
   denominator from it. Nothing is designed before the store
   knows what it holds.
2. **Static monograph.** Build the full page thawed and complete —
   every drawer open, every figure printed — with no script.
   This is the print edition and the permanent fallback.
3. **Palette and type tokens** per §2/§3, including the dead band
   and the mono-numerals rule, enforced in the design-token lint.
4. **Layout:** header/door frame, shelf pitch, rail line, tray
   grid, bench spaces (§4).
5. **The ledger table and Record drawer** from the data object;
   verify the three printings agree (§10.2) before any motion
   exists.
6. **Labels** (§6.5) with state lines driven by a per-tray state
   machine (stored / thawed / broken / withdrawn / on loan).
7. **The shared loop** with lerp 0.09 and the watchdog registry;
   every later element registers its watchdog before its
   animation.
8. **Drawers** (§6.2): arm offsets, slides, Drawer 3's pin,
   snap-open watchdogs.
9. **Thaw engine** (§6.3): dwell accrual, masks, stamps,
   thermometer feed (§6.4) with calibration sweep.
10. **Micro-systems:** warm spot (§6.8), droplets (§6.6),
    dendrites (§6.7) — in that order of importance.
11. **Seal-break** (§6.9) with the session log and the footer's
    count (§6.16).
12. **Form** (§6.14) with idempotent submit, the 4,000ms watchdog
    and the answering thaw.
13. **Loader language** (§6.15) and **door transition** (§6.10),
    with the back-button exemption.
14. **Empty state / 404** (§6.18) and search drawer (§7).
15. **Gate.** Run §10's twelve checks, signed by a non-builder;
    then reduced-motion and print passes; then ship.

