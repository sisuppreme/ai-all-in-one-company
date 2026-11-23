# 48. Sun-Fired Clay — Expanded (v1 + v2)

> Expansion of theme #48 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same two typefaces, the same nine signature elements —
> deepened, never redesigned — plus nine page-family elements.

## 1. Concept & world

A clay tile spends its life under one sun. It is dug as mud, shaped,
dried on a rooftop in the heat it will later shed, fired, laid — and
then it sits on the roof for a hundred years doing nothing but
mediating between the sun and the room below: taking the noon blow,
holding the afternoon, giving the heat back slowly after dark. This
theme builds a website out of that working day. The page is a
**rooftop at noon** when it loads — flat, bright, hard-shadowed — and
scrolling is the afternoon passing over it. Every shadow on the page
lengthens on one shared clock (§6.2). The light warms, the air stops
shimmering, the pace itself slows for the siesta (§5), and the last
stretch of the page is read **by lamplight**: dark violet ground,
warm pools of glow gathered around the final content (§6.8), lamps
the visitor lights with their own hand (§6.9). The footer is 19:40.
The day is over; the roof gives back its heat; the record of the day
is printed in the colophon (§6.17).

The world is the **tile works and its roof**, treated as a complete
interface vocabulary. The page has a **ridge** (the curved tile ridge
that caps every section, §4 — sections emerge from beneath their own
roofline, §6.5), **courses** (the rows of the roof grid: content is
laid in rows like tiles, §6.4, and a card *is* a tile, §6.12), **walls**
(the lime-wash grounds the content sits on beneath the ridges), **the
sundial** (the corner instrument that tells the page's time, §6.3 —
progress is not a bar here, it is a dial), **the day book** (the
works' ledger — batches fired, tiles laid, hours of sun — from which
every printed figure on the page is drawn, §6.16), and **the lamps**
(the evening's furniture: pools of light in the finale, lit by the
visitor, counted honestly in the colophon). Nothing on the page is
Mediterranean decoration. The terracotta is the product, the sun is
the clock, and the shadows are the mechanism.

**The theme's one law: there is one sun, and it keeps one time.**
Every time-bearing value on the page — every shadow's length and
bearing (§6.2), the sundial's gnomon (§6.3), the printed clock
reading, the temperature (§6.14), the hours of light remaining
(§6.14) — is a printing of a single declared function, `dayTime(t)`,
of the page's scroll progress (§5). They cannot disagree, because
they are not five instruments; they are one instrument read five
ways. A build whose card shadows point at a different hour than its
sundial, whose temperature peaks at a scroll position its own
formula forbids, or whose footer claims lamps no hand lit (§6.9), has
not bent the theme — it has hung five clocks in a house with one sun,
and the quality gate (§10) fails it on sight. Everything else in this
theme is craft. That one is the roofer's honesty.

**Time is the interaction model.** The visitor does not operate this
page so much as spend its day. Their scroll is the sun's path: they
lay the roof by arriving at it (§6.4), they draw sections out from
under their ridges (§6.5), their hover is a passing cloud that shades
the tile it crosses (§6.7), and at dusk their click is a hand lighting
a lamp (§6.9) — the one moment the visitor gives light instead of
receiving it. The site does not have users consuming content before a
deadline; it has guests on a roof, and the content is paced the way
the place is paced: brisk in the morning, slow at siesta, gathered
close around the lamps at night. That is why the theme fits work
whose value is literally made by sun and time — fired clay, terracotta,
tile and pottery, olive oil and harvest produce, solar craft, slow
building — and why it curdles around anything instant, nocturnal or
air-conditioned.

**Best-fit sites and audiences.**

- Terracotta tile works, potteries and clay studios: the theme *is*
  the product's working conditions; the hero's shadows fall on the
  tiles being sold, at the hours the yard actually works.
- Mediterranean food and harvest producers (olive oil, wine, sun-dried
  goods): the day is the production method — ripening, drying and
  curing are clocked in hours of sun, and the day book (§6.16) is the
  harvest ledger the maker already keeps.
- Rooftop terraces, agriturismo and slow hospitality: the page sells
  an afternoon; the lamplight finale is the evening the guest is
  booking, and the order form (§6.13) takes the booking at dusk, in
  lamplight, because that is when evenings are decided.
- Solar and passive-building crafts: shading, thermal mass, orientation
  — the lengthening shadow (§6.2) is the product's physics demonstrated
  on the page's own objects.
- Heritage building and restoration yards: lime wash, clay, timber —
  materials specified by course and batch, recorded in a day book.

**When NOT to use it.**

- For products with no sun story. If nothing in the catalogue was
  dried, fired, ripened or shaded, the day is a costume and `dayTime`
  is fiction — §1's law cannot be kept, so the theme cannot be used.
- For content that must be read at speed. The siesta band (§5) slows
  the page's own instruments to lerp 0.07; a reference document or a
  checkout that must complete in one impatient minute should not ask
  its visitors to live through an afternoon.
- For night-first brands. The page *begins* at noon, flat and harsh;
  a brand whose identity is darkness gets seven hours of daylight
  before its own mood arrives, and the violet is locked to the finale
  (§2) — it may not be promoted up the page to fix that.
- For audiences who will not reach the footer. The theme's argument
  completes at 19:40 — the lamps, the colophon, the day's totals. A
  page whose visitors reliably leave at the hero shows them a bright
  roof and nothing else; half the theme is unloaded.
- Where shadows are content. Data-dense interfaces (tables, charts,
  CAD-like tools) cannot have their objects' shadows re-aimed by a
  decorative clock without lying about the data's own emphasis. In
  this theme the shadow belongs to the sun, not to the state.

## 2. Palette

Five anchors, inherited unchanged. The palette is a day in five
materials: fired clay, its own shadow, the bleach the sun leaves,
the olive that survives the heat, and the violet that arrives only
when the day ends. Nothing else is admitted; every other colour on
the page is one of these five, tinted, shaded, or set at an opacity
over its own ground.

**The day's bands (the palette's grammar).** The page's scroll is
divided into five declared bands. Bands are *states of light with
locked rules*, not moods a builder may blend at whim. Text pairings
never change with the band (§3, law 2) — only shadows, warmth and
ambient life do — which is what keeps a page whose light moves all
day AA-safe at every hour.

| Band | Scroll t | Clock (from `dayTime`) | Light rules |
|---|---|---|---|
| Noon | 0–0.16 | 12:00–13:14 | Shadows 2–6px, blur 0; heat shimmer at full strength (§6.6); page at its brightest and flattest |
| Afternoon | 0.16–0.45 | 13:14–15:27 | Warmth rising to its peak; shadows 6–15px; shimmer thinning |
| Siesta | 0.45–0.65 | 15:27–16:59 | Lerp at its slowest (§5); shimmer gone by t=0.55; nothing new starts moving in this band |
| Golden hour | 0.65–0.85 | 16:59–18:31 | Longest warm shadows (to 26px); warmth falling; first lamp pools kindle in the finale's approach |
| Dusk | 0.85–1.00 | 18:31–19:40 | Finale only: violet grounds, lamplight pools (§6.8), lamp clicks live (§6.9). The violet never appears above this band |

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--terra` | `#C96F4A` | Terracotta: the tiles themselves — ridges, card bodies, the sundial's face, fired surfaces everywhere | ~26% of pixels | On lime it measures **2.98:1** — never text, never an indicator on pale grounds; it is a material, not an ink. Lime text on it is equally 2.98:1 and equally refused: nothing is lettered on a tile. |
| `--fired` | `#A44A2A` | Fired shadow: terracotta in shade — links, apparatus, the shadow side of every ridge, hover states on pale grounds | ~14% of pixels | On lime **4.86:1** (AA) — the pale grounds' working red: links, labels, the sundial's figures. On sun-bleached it falls to 3.12:1 — apparatus only there, never body. |
| `--bleached` | `#E4B48C` | Sun-bleached: the sun's own tint — warm highlights, the lamp-glow's outer halo, secondary text on dusk grounds | ~10% of pixels | On dusk violet **7.25:1** (AAA) — the dusk grounds' secondary voice. On lime it is 1.35:1 — a tint, never a letter. |
| `--olive` | `#707A4A` | Olive: the one green — shutters, doors, the works' yard planting; rationed to real objects, never a wash | ~4% of pixels | On lime **3.82:1** — graphical and large-apparatus only; its text form is `--olive-deep` (below). On dusk it is 2.96:1 — refused there; nothing green is read at night. |
| `--dusk` | `#2E2A4A` | Dusk violet: the finale and footer ground ONLY (§1's band law) | ~12% of pixels, all below t=0.85 | Lime on it **11.29:1** (AAA); sun-bleached on it 7.25:1 (AAA); lamp glow on it 8.75:1. The most legible ground on the page — evening is when the reading gets close. |

**Derived tokens (closed list — no others may be introduced).**

| Token | Hex / value | Derivation & use |
|---|---|---|
| `--lime` | `#F4E9D4` | Lime-wash: sun-bleached mixed 62% toward white. The page's wall — the default ground of every section above the finale. Ink on it **10.17:1** (AAA). |
| `--lime-deep` | `#EBD9BC` | Lime in shade: sun-bleached mixed 30% toward white. Alternating wall ground, the underside of ridges, card wells. Ink on it **8.84:1** (AAA). |
| `--ink` | `#542A12` | Fired shadow deepened 32%: all body text on lime grounds. On lime **10.17:1**, on lime-deep 8.84:1, on sun-bleached 6.53:1 (AA). The day's ink is kiln-brown, never black — black is a colour this yard does not fire. |
| `--olive-deep` | `#5C6639` | Olive deepened 18%: olive's only text form on lime — **5.11:1** (AA). Used for the yard's own labels (varieties, grove names) where olive must be read, not just seen. |
| `--terra-deep` | `#A8542F` | Terracotta deepened 20%: display headings on lime at ≥24px only (**4.39:1** — large-text AA, refused below 24px). The hero's second line and section titles in the afternoon bands. |
| `--lamp` | `#F5C97B` | Sun-bleached warmed toward gold: lamplight itself — pool cores, the lit lamp's halo centre, the colophon's figures. On dusk **8.75:1**, on dusk-deep **10.42:1** (both AAA). Never used above the dusk band; a lamp colour at noon is a gate failure. |
| `--dusk-deep` | `#211D38` | Dusk violet deepened 22%: the footer's ground and the pools' outer falloff. Lime on it 13.45:1; lamp on it 10.42:1. |
| `--shadow-ink` | fired shadow at 38% over lime (≈`#B98A6B` effective at noon) | The shadow colour itself: every cast shadow on the page is fired shadow at 38% opacity, warming to 46% and cooling toward dusk-violet at 30% across the day (§6.2) — shadows are the clay's own colour, thinned by light. |

**Dark-mode behaviour: the theme does not invert — the walls are
read after sunset.** The page *is* a passage from noon to dusk;
there is no light scheme to flip to. Under `prefers-color-scheme:
dark`, only the pale walls change: lime grounds are read as
**lime-wash by lamplight** — `--lime-night` (`#E9DCC0`, lime mixed
12% toward sun-bleached) replaces `--lime`, and ink holds at
**9.01:1** (AAA). The tiles, ridges, sundial and dusk finale are
unchanged (fired clay does not care about the room's light), the
shadow system runs exactly as declared, and text on dusk grounds
stays lime at full value — lamplight deepens the walls' warmth,
never the violet. A build that inverts the page or darkens the
terracotta has misunderstood the yard: after sunset you read the
wall by a lamp, you do not repaint the roof.

**Pairing law.** Text is `--ink` on lime, lime-deep and sun-bleached
grounds; `--fired` for links and apparatus on lime only; lime on
dusk and dusk-deep; sun-bleached as secondary on dusk grounds only;
`--lamp` for figures and lit states in the dusk band only.
Terracotta carries no text at any hour. Olive is read only as
`--olive-deep`. Any other pairing is a build error, not a variation.

## 3. Typography

Two typefaces, inherited unchanged. **Marcellus** is the fired voice
— a Roman inscriptional face with flared stems, cut like lettering
on a kiln-yard sign — and sets display, headings, tile names and the
sundial's hour figures. It exists in one weight (400) and the theme
treats that as a discipline, not a lack: hierarchy on this page is
built from size, case and shadow, never from a bold that does not
exist. **Alegreya** is the wall voice — a warm book serif — and sets
body text, captions, the day book and all prose. Data (temperatures,
clock readings, tile counts, hours) is set in Alegreya with
`font-variant-numeric: tabular-nums`, never in Marcellus: the yard's
figures are tallied in the book hand, not carved. There is no third
typeface. Emphasis inside Marcellus is size and letterspacing;
emphasis inside Alegreya is weight (400→700) or italic — Alegreya's
italic is the voice of the day book's marginal notes (§12) and leans
like handwriting in a ledger margin, rationed to it.

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Display / hero headline | Marcellus 400 | 54–88px / 1.02, `clamp(3.375rem, 7.5vw, 5.5rem)` | +0.015em | Stamped at noon (§6.1); its shadow is part of its typesetting (law 1). Never more than 2 lines; uppercase first line permitted, never the whole headline. |
| Section title | Marcellus 400 | 36–54px / 1.06, `clamp(2.25rem, 4.8vw, 3.375rem)` | +0.015em | Emerges from beneath its ridge with the section (§6.5); set in `--ink`, or `--terra-deep` at ≥36px in afternoon bands. |
| Tile / product name | Marcellus 400 | 22–28px / 1.16 | +0.01em | Name only; the batch and firing ride beneath it in apparatus, never inside the name (law 3). |
| Heading (in-section) | Marcellus 400 | 24–30px / 1.14 | +0.01em | One per wall region; a heading never crosses a ridge — it is lettered on one wall. |
| Body | Alegreya 400 | 16.5–18px / 1.68 | 0 | Measure 56–64ch. On dusk grounds 17px minimum — the pools are read close (§6.8). |
| Caption / day book | Alegreya 400 | 14–15px / 1.55 | 0 | The ledger's voice (§6.16): what the batch is, how many tiles, which firing, whose hands. |
| Apparatus (clock, temperature, counts) | Alegreya 700 | 11–13px, uppercase | +0.16em | The sundial's reading ("17:52"), temperatures ("34°"), course counts. Uppercase is rationed to apparatus only. |
| Price | Marcellus 400 | 28–38px / 1.05 | +0.01em | Lettered on the card's wall strip, never floated on a badge — a price is painted on the tile's own tag. |
| The colophon line | Alegreya 500 | 15–17px / 1.6 | 0 | The footer's closing sentence (§6.17) — the day's totals in the book voice, sentence case, unhurried. |

**Type laws.**

1. **The headline's shadow is typesetting.** The hero headline is set
   with its noon shadow (§6.1) as a designed part of the line — 2px,
   hard, fired — and that shadow is §6.2's first citizen: it lengthens
   with every other shadow on the page. A build that gives the
   headline a private, prettier shadow has hung a second sun (§1).
2. **Type never changes colour with the hour.** Text colour is a
   property of the ground (§2's pairing law) and does not warm, cool
   or fade as the bands pass. The light moves; the letters hold.
   A heading that "glows" at golden hour is a build error.
3. **The count rides with the name.** Every tile, batch and section
   title that has a record carries it in apparatus directly beneath
   the name — name, then count, then prose. A title that praises a
   tile before stating its firing has skipped the kiln.
4. **Figures are tallies.** Any number the page asserts (degrees,
   minutes, tiles, metres) is set tabular and is subject to the one
   law (§1): printed from `dayTime(t)` or traceable to the day book
   (§6.16). Percentages are banned from the theme — a roof is counted
   in tiles and hours, not proportioned.
5. **Marcellus never shouts.** Display is sentence case or title case;
   full-uppercase display is refused — inscriptional capitals at 80px
   are a monument, and this is a working yard. Uppercase belongs to
   apparatus (≤13px) where it is carved small, like the sundial's
   numerals.

## 4. Layout language

**The section is a room under its own roofline.** Every section is
capped by a **ridge**: a curved tile ridge — a repeating barrel-tile
arc, drawn once as an SVG pattern and reused at every section head —
and the section's content sits on its **wall** (lime or lime-deep)
beneath it. The ridge is not a divider decoration: it is the
section's own roof, it parallaxes against its wall (§5), and the
section's content emerges from beneath it (§6.5). A page in this
theme reads as a street of small houses, each with its roof, its
wall, and its hour of shade.

**The course grid.** Content inside a wall is laid in **courses** —
rows aligned to a 148px tile module (the laid width of one coppo
with its overlap, declared in the day book, §6.16). Cards are sized
in whole tiles: a standard tile card is 2 modules wide × 2 courses
tall (296×296px at desktop); a wide card is 3×2; nothing is 2.5 tiles
wide, ever — a card that breaks the module is a tile cut wrong, and
the grid shows it. Vertical rhythm is the course height: sections
pad in whole courses (148px desktop, 118px tablet, 96px mobile —
the module shrinks, the wholeness doesn't).

**The sundial's corner.** The sundial (§6.3) lives in the hero's
top-right corner at desktop — a 168px semicircular dial set into the
hero wall like a courtyard dial — and, once the hero is past, retires
to a 44px margin chip (§6.10's navigation carries its reading) rather
than following the visitor down the page like a widget. Instruments
in this theme are *placed*, the way a real dial is placed on the
wall that gets the sun; they are not floating UI.

**Density falls with the day.** Noon is full and flat: the hero and
the first courses are dense with tiles. The siesta band is the
emptiest stretch of the page by design — one wall, long measure,
nothing competing (§2's band law: nothing new starts moving there).
Golden hour re-gathers: figures and the day book. Dusk is the
closest density of all — the finale's content drawn into pools, each
pool one block, generously ringed by dark. A page that is uniformly
dense from noon to dusk has not understood the afternoon.

**Whitespace is shade.** The lime margins between courses are not
empty space; they are the wall in shadow-side rest, and they widen
as the day cools (section gaps grow one course-step between the
siesta band and the finale — the street empties as it darkens).
Alignment is to the ridge above: every wall's content hangs from its
ridge's baseline, so a section's first line always sits the same
distance under its roofline — the eye learns the street's rhythm in
two sections and is never surprised again.

## 5. Full motion system

Five named easings, used by every element and no others:

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-stamp` | `cubic-bezier(.2,.85,.3,1)` | The press: a fast fall and a dead stop — fired clay does not bounce | Noon stamp (§6.1), lamp press (§6.9), form submit (§6.13) |
| `--ease-lay` | `cubic-bezier(.35,.65,.3,1)` | A tile settling onto its course: weight arriving, one small adjustment, rest | Roof-laying stagger (§6.4), cards (§6.12), skeleton resolve (§6.15) |
| `--ease-ridge` | `cubic-bezier(.45,.05,.25,1)` | The slide out from under the roofline: slow to clear the ridge, then free | Ridge reveals (§6.5), ridge-pass transition (§6.15) |
| `--ease-cloud` | `cubic-bezier(.4,0,.6,1)` | Weather: an even, unhurried drift with soft edges on both ends | Cloud-shade hover (§6.7), shimmer fade (§6.6), warmth ramps |
| `--ease-lamp` | `cubic-bezier(.3,.55,.35,1)` | A lamp catching: a small hesitation, then a warm bloom that settles | Lamplight pools (§6.8), lamp click (§6.9), colophon kindle (§6.17) |

**The one sun: `dayTime(t)` (the theme's master clock).** Every
time-bearing value derives from scroll progress `t` (0 at the hero's
top, 1 at the footer's foot) through one declared function, printed
here so any builder — and the gate (§10) — can audit it:

- **Clock:** `clock(t) = 12:00 + 460·t minutes` — the day runs
  12:00 → 19:40. At t=0.5 the page's time is 15:50, everywhere, in
  every instrument, without exception.
- **Shadow vector:** x-offset `sx(t) = 2 + 24t px` (2px at noon, 26px
  at 19:40), y-offset `sy(t) = 2 + 9t px`, blur `0 + 6t px`; the
  vector's bearing swings ≈22° across the day (45° below the
  horizontal at noon, ≈23° at 19:40 — long and low). Shadow colour is
  `--shadow-ink`, its opacity warming 38% → 46% by t=0.65 then
  cooling toward dusk-violet 30% in the finale.
- **Sundial:** the gnomon shadow's hour angle is `115·t degrees`
  from the noon line — the sun's true rate, 15° per hour, across
  7h40m. The dial's printed reading is `clock(t)` in apparatus.
- **Temperature:** declared in two legs — warming leg t∈[0, 0.45]:
  `T = 33 + 3·(t/0.45)` (33° → 36°); cooling leg t∈(0.45, 1]:
  `T = 36 − 12·((t−0.45)/0.55)` (36° → 24°). Peak 36° at 15:27,
  the siesta's start: the hottest hour is the stillest, by design.
- **Light remaining:** `460·(1−t)` minutes, printed as hours and
  minutes ("3 H 12 M OF LIGHT") — the same 460, read backwards.
- **Warmth:** a sun-bleached overlay whose opacity is
  `0.14·sin(π·t)` — nothing at noon's flat glare, fullest at golden
  hour's heart, gone at dusk, where the lamps (§6.8) take over the
  job of warmth.

**Every motion term, translated into the yard's language:**

- **Scroll-triggered reveals** are ridge reveals: sections slide out
  from behind the ridge above them (§6.5). Nothing fades up out of
  nowhere; on this page rooms emerge from under their own rooflines.
- **Scroll scrub** is the day itself: shadows (§6.2), the sundial
  (§6.3), temperature and light-remaining (§6.14) are pure functions
  of `t`, driven by the shared loop. Scrubbing back up is the day
  rewinding — every scrubbed value retraces exactly (§13).
- **Parallax** is the roof against the wall: exactly one parallax
  pair per section — its ridge drifts at 0.92× against its wall —
  plus the hero's sundial corner (§6.11). Nothing else pretends to
  be at two depths; a roof has two layers, not five.
- **Pinned scenes:** exactly one — the lamplight finale (§6.8). A
  day has one evening; pinning a second scene is refused.
- **Masked reveals** are the ridge's own curve: the reveal mask is
  the ridge arc (§6.5), so content is uncovered by its roofline, not
  by a generic wipe.
- **Blur-to-sharp is refused**, except inside the heat shimmer's
  distortion (§6.6) where the blur is the air's, never the content's.
  Fired clay is hard-edged at every hour; a soft-focus tile is a
  melting one.
- **Kinetic typography is refused.** Letters do not perform here;
  the headline is stamped once (§6.1) and then only its shadow moves.
  Type holds still so the light can be seen moving.
- **Counters** are the day figures (§6.14): temperature, light
  remaining, tiles laid — tabular, stepped like chalk marks on the
  day book, every figure from `dayTime` or the book.
- **Progress** is the sundial (§6.3): a gnomon shadow and a printed
  reading. There is no progress bar; there is a dial in the corner.
- **Marquee is refused.** A roof does not run sideways. The day book's
  totals (§6.16) are printed standing still, like entries.
- **Ambient loops:** exactly two, both rationed — the heat shimmer
  (§6.6, noon bands only, dead by siesta) and the dust motes inside
  lit lamp pools (§6.8, dusk only). They never coexist: the day's
  air shimmers *or* its lamplight holds dust, and the handover at
  dusk is the theme's ambient signature. A third loop is a gate
  failure.
- **Micro-interactions:** the cloud shade (§6.7), the lamp click
  (§6.9), the stamp press (§6.13's submit). Every interaction is
  weather or lamplight.
- **Hover physics:** no magnetic pull, no tilt stages. A tile under
  a hand is shaded (§6.7); clay does not lean toward the visitor.
- **Page transitions** are a ridge pass (§6.15): the current
  section's ridge sweeps down as the new page's first ridge rises —
  the street continues; you walk under a roofline into the next room.
- **Smooth scrolling — the siesta rule.** Native scroll is never
  hijacked; the theme smooths its *instruments*, and the smoothing
  itself keeps the day's hours: the shared loop's lerp is **0.16 in
  the morning bands** (brisk, t<0.3), **0.07 through the siesta**
  (t 0.45–0.65 — the page's own gauges move slowly at the slow hour),
  and **0.12 in the evening**. A builder who flattens this to one
  lerp has air-conditioned the siesta out of the theme.
- **The shared loop law.** One `requestAnimationFrame` loop owns
  every scrubbed value (shadow vector, sundial angle, temperature,
  warmth, ridge parallax, pool gather). It writes only `transform`,
  `opacity` and custom properties (`--sx`, `--sy`, `--sun-angle`,
  `--warmth`), recomputes `dayTime` once per frame from the lerped
  `t`, and stops writing a value when it settles within 0.1% of
  target. All cast shadows on the page read the same two custom
  properties — that is the mechanical guarantee of §1's law: there
  is one `--sx` because there is one sun.

**Watchdog law.** Every time-bearing instrument has a timer: if the
loop or an observer fails, shadows snap to the band-correct vector,
the sundial prints its reading for the last known `t`, and counters
print their true figures by 1200ms after the trigger (§6.2, §6.3,
§6.14). The DOM ships at **noon rest** — flat, bright, fully
legible, sundial reading 12:00, temperature printed at 33° — and JS
arms the day's passage from there. No-JS is not a degraded mode: it
is the yard at noon with the day held, every word readable, every
tile priced.

## 6. Signature elements

### 6.1 The noon stamp

- **What & why.** On load, the hero headline is stamped onto the hero
  wall — arriving in one hard press, flat and bright, with a short
  2px fired shadow — and the instant it lands, its shadow begins
  lengthening into §6.2's system. It belongs because noon is the
  page's first fact and the stamp is how noon feels: no fade, no
  rise, a kiln-yard sign pressed into fresh lime. The stamp is also
  the clock starting: the headline's shadow is the first shadow the
  day moves, so the title is not above the theme's physics — it is
  the first object the sun touches.
- **Structure.** The `<h1>` in the hero wall (§6.11), set in
  Marcellus at the display clamp (§3). It ships at rest — fully
  lettered, shadow at the noon vector (2px/2px, blur 0) — and JS
  arms the pre-stamp state (translateY −6px, opacity 0) only after
  first paint confirms the loop is alive. The shadow is a real
  `text-shadow` reading the shared `--sx`/`--sy` custom properties,
  so from the stamp's first frame the headline is wired into the
  one sun.
- **Motion spec.** Trigger: load, gated on `document.fonts.ready`
  raced against a 600ms timer — the stamp must not wait for a slow
  font; noon does not wait. The press runs 240ms `--ease-stamp`:
  translateY −6px → 0 with no overshoot (fired clay does not bounce)
  and the shadow snapping from 0 to the full noon vector in the same
  beat — the shadow is *struck*, not grown. From t≈260ms the shadow
  hands over to §6.2's scrub: it is already lengthening as the
  visitor starts to read. Runs once per session; a returning visitor
  finds the headline standing in whatever light their scroll
  position declares.
- **States.** Pre-stamp (JS-armed only, ≤600ms) → stamped at noon →
  under the day (shadow scrubbed by §6.2 for the rest of the page).
  Scrolled during the press: the press completes regardless — it is
  240ms and owes nothing to the viewport.
- **Content merge.** The headline is the site's name and claim,
  lettered on the hero wall; the stamp is its hanging. Remove the
  animation and the hero loses only the press; keep it and the
  title has a provenance — it was put up at noon, and its shadow
  has been keeping time ever since.
- **Failure fallback.** Watchdog: if the headline has not stamped by
  900ms after the trigger, it is set to rest instantly. No JS: the
  headline stands lettered at first paint, shadow at the noon
  vector, indistinguishable from a stamped one at rest.
- **Reduced-motion variant.** No press. The headline stands at rest
  with the noon vector, and one apparatus line beneath the
  standfirst records the hour the stamp would have struck: "SET UP
  AT NOON — THE SHADOW KEEPS THE DAY." The fact is kept; only the
  blow rests.
- **Performance budget & mobile variant.** One transformed element +
  one text-shadow; no images, no canvas. Mobile (<768px): the press
  shortens to 180ms and the travel to −4px — a smaller wall takes a
  smaller stamp.
- **Choreography timeline (v2).** t=0 fonts ready (or 600ms race
  lost) → t=0–240 the press: headline falls 6px, shadow strikes to
  (2px, 2px, 0) → t=240 headline at rest → t=260 §6.2's scrub takes
  the shadow → the hero's hour lines (§6.3) finish drawing by
  t≈1100, beneath a headline already standing.
- **State matrix (v2).** *Rest:* lettered, noon vector. *Hover:*
  none — the headline is not a control. *Focus:* none (not
  focusable). *Active:* n/a. *Scrolled-past:* the press has
  completed; the shadow reads the current `t`. *Disabled / no-JS:*
  rest at first paint. *Touch:* identical; the first touch does not
  re-stamp.
- **Breakpoints (v2).** ≥1200px: full 240ms press, −6px travel.
  768–1199px: 220ms, −5px. <768px: 180ms, −4px.
- **Edge cases & failure modes (v2).** *Slow fonts:* the 600ms race
  governs; the stamp fires in a fallback face and the fixed hero
  height absorbs letterfit shift. *Tab hidden during load:* on
  return, elapsed wall-time > 900ms rests the headline — no visitor
  resumes a half-struck sign. *Session return:* `sessionStorage`
  marks the stamp done; the headline paints at rest.
- **Accessibility spec (v2).** The headline is the page's `<h1>` from
  first paint and is never removed from the accessibility tree; the
  press is visual only and never announced. Contrast at every frame:
  ink on lime 10.17:1 (§2); the shadow is decorative and excluded
  from contrast. Focus is never moved by the stamp.
- **Tokens consumed (v2).** `--lime`, `--ink`, `--shadow-ink`,
  `--sx`, `--sy`, `--ease-stamp`, `--dur-stamp` (240ms),
  `--dur-stamp-race` (600ms), `--dur-stamp-watchdog` (900ms).

### 6.2 Lengthening shadows

- **What & why.** Every cast shadow on the page — cards, tiles,
  type, ridges, the sundial's own furniture — lengthens and swings
  scrubbed to scroll, from the 2px noon vector to 26px at 19:40.
  It belongs because it is the theme's thesis made mechanical: the
  afternoon is not described, it is *applied to the objects*. A
  visitor who reads nothing still feels the day pass, because the
  tile they are looking at casts a longer shadow than the tile
  above it did. This is the one system every other element borrows
  its time from, and the mechanical heart of §1's law.
- **Structure.** No DOM of its own: a pair of custom properties,
  `--sx` and `--sy` (plus `--shadow-blur` and `--shadow-tint`), set
  on `:root` by the shared loop from `dayTime(t)` (§5). Every
  shadowed element declares `box-shadow: var(--sx) var(--sy)
  var(--shadow-blur) var(--shadow-ink)` (or the `text-shadow`
  equivalent for §6.1 and §6.11's display lines). Builders may not
  hand-write a shadow value anywhere in the theme; a literal
  `box-shadow` in the stylesheet outside the token definitions is
  a gate failure (§10).
- **Motion spec.** Trigger: scroll, continuous. The loop lerps `t`
  (§5's daypart lerps: 0.16 / 0.07 / 0.12) and writes the vector per
  frame: `sx = 2 + 24t`, `sy = 2 + 9t`, blur `6t`, tint opacity
  warming 38% → 46% by t=0.65 then cooling to dusk-violet at 30%
  across the finale. Fully reversible: scrolling up shortens every
  shadow along the same path, at the same values — the day rewinds
  exactly, with no hysteresis, because the function has none.
- **States.** Noon vector (t=0, the shipped default) → lengthening
  (any t>0) → evening vector (t=1: 26px/11px/6px). Hover/focus do
  not exempt an element: a hovered card's shadow is still the sun's
  (§6.7 adds shade *over* the card; it never touches the shadow
  *under* it).
- **Content merge.** The shadows belong to the content's own
  objects — they are the tiles' and letters' shadows, not a light
  effect laid over the page. Remove the system and the page is a
  flat noon forever; the content loses its clock, not a garnish.
- **Failure fallback.** Watchdog: if the loop stalls (no frame for
  1200ms while scroll is changing), the vector snaps to the value
  for the current scroll position computed directly from
  `scrollY` — a stepped shadow at the right hour beats a smooth
  shadow at the wrong one. No JS: every shadow stands at the noon
  vector; the page reads as permanent noon, complete and legible.
- **Reduced-motion variant.** Shadows rest at one gentle
  late-afternoon vector — 14px/6.5px, blur 3px, tint 44% (t≈0.5,
  15:50) — for the whole page, unmoving. The apparatus line §6.1
  adds in this mode names the hour the page rests at.
- **Performance budget & mobile variant.** Two custom-property
  writes per frame on `:root`; shadows are compositor-cheap at
  these offsets but repaint-bound on some mobile GPUs, so the
  mobile variant quantises the vector to 0.5px steps and caps blur
  at 4px — the day still passes, in slightly larger minutes.
  Budget: ≤0.4ms/frame of the shared loop's 1.6ms (§14).
- **Choreography timeline (v2).** Continuous: each frame, lerp `t`
  toward the scroll target at the daypart rate → recompute the
  vector → write `--sx`, `--sy`, `--shadow-blur`, `--shadow-tint`
  → settle-check (stop writing when within 0.1% of target). Band
  crossings (t=0.16/0.45/0.65/0.85) change nothing in this element
  except the lerp rate and tint path declared in §5.
- **State matrix (v2).** *Rest (no scroll):* vector holds at the
  current `t`. *Hover:* unchanged (see §6.7). *Focus:* unchanged —
  focus rings are drawn in `--fired` outlines, never shadows, so
  the sun cannot swallow a focus indicator. *Active:* unchanged.
  *Scrolled-past:* n/a — the system is global. *Disabled:* n/a.
  *Touch:* identical; quantised on small screens per above.
- **Breakpoints (v2).** ≥1200px: full vector range, blur to 6px.
  768–1199px: range to 22px/10px, blur to 5px. <768px: range to
  18px/8px, blur to 4px, 0.5px quantisation — a phone's roof is
  smaller and its evening shadows are shorter; the *hours* are
  identical, only the wall is nearer.
- **Edge cases & failure modes (v2).** *Jump scroll / anchor
  leap:* the lerp catches up at the daypart rate; a leap across
  the siesta lands within ~600ms — the day visibly hurries, which
  is honest: the visitor hurried. *Very long pages:* `t` is
  normalised to the page's full scroll, so the day always ends at
  the footer regardless of page length (§7's page types declare
  their own lengths; the clock stretches, the hours don't change).
  *Print:* shadows print at the noon vector (the stylesheet's
  default), so a printed page is a noon page.
- **Accessibility spec (v2).** Shadows are decorative and excluded
  from all contrast claims; text contrast is a property of the
  grounds (§2) and is invariant across the vector's whole range —
  verified at t=0, 0.5 and 1 in the gate (§10). No information is
  carried by shadow alone: the hour is always also printed (§6.3,
  §6.14).
- **Tokens consumed (v2).** `--sx`, `--sy`, `--shadow-blur`,
  `--shadow-tint`, `--shadow-ink`, `--fired`, `--dusk`, `--lerp-am`
  (0.16), `--lerp-siesta` (0.07), `--lerp-pm` (0.12).

### 6.3 The sundial progress

- **What & why.** A semicircular sundial set into the hero wall's
  corner: its hour lines draw themselves on entrance, and its
  gnomon shadow rotates scrubbed to scroll from the noon line to
  the 19:40 mark, with the current time printed beneath it in
  apparatus. It belongs because progress in this theme is not an
  abstract percentage — it is the hour, told by the instrument
  the yard actually uses, sitting in the corner where a courtyard
  dial sits. It is also §1's law made visible: the dial and the
  shadows (§6.2) are the same function, and a visitor can check
  one against the other all day.
- **Structure.** An inline SVG (168px desktop) in the hero's
  top-right corner (§6.11): a semicircle face in `--terra` with
  hour lines for 12, 13, …, 19 and a longer line at 19:40, a
  triangular gnomon, and a shadow wedge (a rotated path in
  `--shadow-ink`) whose rotation the loop writes as
  `--sun-angle`. Beneath the dial, an `<output>` prints
  `clock(t)` ("17:52") and the band name ("GOLDEN HOUR"). The DOM
  ships with the wedge on the noon line and the reading "12:00 —
  NOON".
- **Motion spec.** Entrance: the hour lines draw (stroke-offset)
  over 900ms `--ease-lay`, staggered 60ms per line from the noon
  line outward, gated on fonts-ready raced at 600ms; the wedge is
  live from the first frame. Scrub: the wedge rotates
  `115·t degrees` — the sun's true 15°/hour across the 7h40m day
  (§5) — on the shared loop's lerped `t`, so the dial's shadow
  sweeps with the same slight lag as every cast shadow (§6.2).
  The printed reading updates when the minute changes (≤ every
  ~26px of scroll on a typical page), tabular, never animated —
  figures step like a dial's, they do not roll.
- **States.** Undrawn (pre-entrance, JS-armed only) → drawn, wedge
  at noon → sweeping (any t>0) → at rest on the 19:40 line in the
  footer zone (the dial itself has retired to the margin chip by
  then, §6.10; the hero dial's last seen state is wherever the
  visitor left it). Hover: the wedge deepens 8% and the reading
  gains its seconds-free precision note ("BY THE SUN") — the dial
  acknowledges being read. Focus (the dial is a link to the day
  book, §6.16): the fired focus ring, wedge unchanged.
- **Content merge.** The dial measures the reading itself: its
  wedge is the visitor's scroll drawn as an hour. It sits in the
  hero because the hero is where the day starts; remove it and
  the page still passes its afternoon, but nothing on the page
  *says* what time it is — the instrument is the page's clock
  face, not a progress widget wearing a costume.
- **Failure fallback.** Watchdog: lines not drawn by 1600ms are
  set drawn; wedge angle written directly from `scrollY` if the
  loop stalls (§6.2's rule). No JS: the dial stands drawn at noon
  reading 12:00 — a true statement about a held day.
- **Reduced-motion variant.** The dial stands drawn, the wedge
  rests at the late-afternoon angle matching §6.2's resting
  vector (t≈0.5), and the reading prints "15:50 — AFTERNOON, AT
  REST". No sweep, no draw.
- **Performance budget & mobile variant.** One SVG rotation + one
  text update per minute-change; ≤0.1ms/frame. Mobile (<768px):
  the dial shrinks to a 96px corner instrument, hour lines for
  12/15/19:40 only (the day in three marks), reading unchanged —
  a small wall gets a small dial, telling the same time.
- **Choreography timeline (v2).** t=0 hero enters → t=0–900 hour
  lines draw, 60ms stagger → wedge live throughout → on scroll,
  per frame: wedge angle = 115·(lerped t) → on minute change:
  reading steps → at hero exit: the dial hands its reading to
  §6.10's margin chip (the chip's first value is the dial's last,
  from the same `t` — the handover cannot drift).
- **State matrix (v2).** *Rest:* wedge at current `t`, reading
  current. *Hover:* wedge tint +8%, precision note shown.
  *Focus:* fired ring on the dial link; reading unchanged.
  *Active:* navigates to the day book (§6.16). *Scrolled-past:*
  retired to the chip (§6.10); its state is the chip's state.
  *Disabled:* n/a. *Touch:* tap = the link; no hover deepening
  (a tap is a visit, not a reading).
- **Breakpoints (v2).** ≥1200px: 168px dial, all hour lines,
  band name printed. 768–1199px: 132px dial, all hour lines,
  band name cut. <768px: 96px dial, three hour lines, reading
  kept (the reading is never cut — it is the dial's voice).
- **Edge cases & failure modes (v2).** *Minute-boundary flicker:*
  the reading updates on the lerped value crossing a minute
  boundary, never on raw scroll, so it cannot oscillate. *Very
  short page:* if the page cannot scroll, `t` stays 0 and the
  dial honestly reads noon all day — a one-room house has one
  hour. *Hero revisited at dusk:* scrolling back to the top
  rewinds the wedge to the morning — the dial obeys `t`, not
  memory.
- **Accessibility spec (v2).** The dial is an image with a text
  twin: the `<output>` reading is the accessible instrument,
  updated politely (`aria-live="off"`; the reading is available
  on demand, not announced per minute — a clock that announces
  every minute is a nuisance, not an aid). The SVG is
  `aria-hidden`. The dial link's label: "The day book — the
  yard's record". Touch target ≥44px (the whole dial).
- **Tokens consumed (v2).** `--terra`, `--fired`, `--shadow-ink`,
  `--sun-angle`, `--ink`, `--ease-lay`, `--dur-dial-draw` (900ms),
  `--stagger-dial` (60ms).

### 6.4 The roof-laying stagger

- **What & why.** Tile cards enter row by row — a full course at a
  time, 120ms per row — each card settling with a small shadow
  snap, like a roof being laid by a crew working across it. It
  belongs because the product grid *is* the roof (§4's course
  grid): its assembly is the trade the brand practices, performed
  at the moment the visitor arrives at the stock. A grid that
  fades in item by item is inventory appearing; a grid that lays
  itself course by course is a roof being built in front of the
  buyer.
- **Structure.** The card grid (§6.12) as a `<ul>` of tile cards in
  course rows. Cards ship laid — visible, priced, at rest — and JS
  arms the unlaid pre-state (translateY 18px, opacity 0) per row
  only when the grid's approach is observed. The shadow snap is
  §6.2's vector applied in two beats: the card lands with its
  shadow at 60% of the current vector, then the vector's full
  value arrives 90ms later — the small *settle* of a tile finding
  its bed.
- **Motion spec.** Trigger: the grid's top crossing 78% of the
  viewport. Rows fire in course order, 120ms apart; each row's
  cards rise 18px → 0 over 460ms `--ease-lay`, simultaneous within
  the row (a course is laid by a crew, not one tile at a time).
  Shadow snap at land +0ms (60% vector) → +90ms (full vector).
  A row that enters during a fast fling is laid instantly — the
  crew does not perform for a visitor who has already passed the
  roof. Once laid, a row never un-lays; scrolling back shows the
  finished roof.
- **States.** Unlaid (JS-armed only) → laying (its 460ms) → laid
  (rest, permanent for the session). Hover/focus per §6.12/§6.7.
  Scrolled-past mid-stagger: remaining rows lay instantly.
- **Content merge.** The cards are the products — tiles with names,
  batches and prices (§6.12). The stagger is not an entrance
  effect applied to a grid; it is the grid's own construction,
  and the row order is the course order a roofer would follow.
- **Failure fallback.** Watchdog per row: any row not laid by
  trigger +1400ms is set laid. No JS: the roof stands built at
  first paint.
- **Reduced-motion variant.** The roof stands built. One apparatus
  line at the grid's head records the fact: "LAID COURSE BY
  COURSE — 120 MS A ROW." (§12's voice: the record states the
  making instead of performing it.)
- **Performance budget & mobile variant.** Transform + opacity
  only; ≤12 cards animating at once (two rows). Mobile: rows are
  single cards; the stagger becomes 90ms per card and the travel
  12px — a small roof is laid by a smaller crew, faster.
- **Choreography timeline (v2).** t=0 grid top crosses 78% →
  row 1 rises t=0–460 → row 2 at t=120 → row n at t=(n−1)·120 →
  each row's shadow snap at its land +90ms → the grid's head
  apparatus (§6.14's counts, if present) starts counting only
  after the last row lands.
- **State matrix (v2).** *Rest:* laid. *Hover:* §6.7's cloud shade
  (never a lift — laid tiles do not rise). *Focus:* fired outline;
  the row does not re-lay. *Active:* the card's own link. 
  *Scrolled-past:* laid, instantly if skipped. *Disabled:* n/a.
  *Touch:* identical; no hover shade on first tap (tap = visit).
- **Breakpoints (v2).** ≥1200px: rows of 3–4 cards, 120ms course
  stagger. 768–1199px: rows of 2, 110ms. <768px: single column,
  90ms per card, travel 12px.
- **Edge cases & failure modes (v2).** *One-card row:* a short
  final course lays alone — honest, like a roof's last course.
  *Content longer than expected (many rows):* the stagger caps
  at 8 rows; rows beyond arrive laid — a big roof's far courses
  are already on when you arrive. *Reflow mid-lay (resize):* rows
  re-form; laid state is per-card, so nothing re-lays.
- **Accessibility spec (v2).** Cards are list items with real
  links; the stagger never reorders or hides them from the
  accessibility tree (pre-state is visual only, applied after
  first paint, removed on the watchdog). Focus entering the grid
  lays all rows instantly — a keyboard visitor is never asked to
  wait for a roof. Touch targets: the whole card, ≥96px tall.
- **Tokens consumed (v2).** `--ease-lay`, `--dur-lay` (460ms),
  `--stagger-course` (120ms), `--sx`, `--sy`, `--shadow-ink`,
  `--lime`, `--lime-deep`.

### 6.5 Ridge reveals

- **What & why.** Each section slides into view from behind the
  curved tile ridge that caps it — the ridge's arc is the reveal
  mask — over 800ms as the section enters. It belongs because the
  architecture is the reveal: a room emerges from under its own
  roofline, so the page's structure and its motion are the same
  fact stated twice. It is also the theme's discipline against the
  generic fade-up: nothing on this page *appears*; everything is
  *uncovered by its roof*.
- **Structure.** Each `<section>` carries its ridge as an SVG arc
  strip (§4) at its head, and its wall content in a wrapper whose
  `clip-path` follows the ridge curve (an inset clip whose top
  edge is the arc, approximated by a 24-segment path). The content
  ships uncovered — clip at full — and JS arms the covered
  pre-state (clip raised to the ridge line, content translated
  24px up behind it) on approach.
- **Motion spec.** Trigger: the section's ridge crossing 82% of
  the viewport. The clip's arc edge sweeps down over 800ms
  `--ease-ridge` while the content settles 24px → 0 on the same
  curve; the ridge itself parallaxes at 0.92× against the wall
  throughout (§5). The reveal is scrub-independent — it plays
  once, on arrival — but a section flung past mid-reveal completes
  instantly: the room is open when you get there, however fast
  you travelled. Reveals never replay; a section scrolled back to
  stands open under its ridge.
- **States.** Covered (JS-armed only) → revealing (800ms) → open
  (rest, permanent). Hover/focus: none at section level.
  Scrolled-past unrevealed (jump): open, instantly.
- **Content merge.** The ridge is the section's own head — the
  mask is the architecture, not an overlay. Remove the motion and
  the section loses its emergence but keeps its roof; the ridge
  remains as the section's cap in the static page.
- **Failure fallback.** Watchdog: any section not open by trigger
  +1600ms is set open (clip removed). No JS: all sections stand
  open at first paint — the street is built.
- **Reduced-motion variant.** Sections stand open. The ridge
  remains, static, as each section's cap; the parallax pair is
  stilled (ridge and wall scroll together).
- **Performance budget & mobile variant.** `clip-path` animation
  is repaint-bound; one section reveals at a time (queued by the
  observer), ≤1.2ms/frame during a reveal. Mobile: the arc flattens
  (fewer segments), travel 16px, duration 650ms — a smaller
  roofline, a quicker uncovering.
- **Choreography timeline (v2).** t=0 ridge crosses 82% →
  t=0–800 clip sweeps, content settles → t=800 section open; its
  first instrument (counter, §6.4 row, §6.14 figure) starts only
  after t=800 — nothing inside a room performs before the room is
  open.
- **State matrix (v2).** *Rest:* open. *Hover:* none. *Focus:*
  focus entering a covered section opens it instantly (keyboard
  visitors walk into open rooms). *Active:* n/a. *Scrolled-past:*
  open. *Disabled / no-JS:* open at first paint. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: full arc, 800ms, 24px travel.
  768–1199px: arc at 70% depth, 720ms, 20px. <768px: flattened
  arc, 650ms, 16px.
- **Edge cases & failure modes (v2).** *Short sections* (shorter
  than the reveal travel): the clip still sweeps the ridge line
  only — content shorter than 24px of travel settles by fade of
  the clip alone, never clipped mid-line. *Nested interactive
  content:* the clip wrapper is `pointer-events: none` until
  open, so nothing can be clicked through a half-open roof.
  *Print:* all sections print open (the shipped state).
- **Accessibility spec (v2).** Content is in the accessibility
  tree at all times; the covered pre-state is visual only and is
  never applied before first paint. The reveal is not announced.
  Focus order follows the DOM, not the reveal order.
- **Tokens consumed (v2).** `--ease-ridge`, `--dur-ridge` (800ms),
  `--terra`, `--fired`, `--lime`, `--lime-deep`.

### 6.6 Heat shimmer

- **What & why.** Above the noon sections, the air trembles: a
  low-amplitude distortion layer shimmers over the top of the
  section, fading as the page cools and gone by the siesta. It
  belongs because it is the one ambient effect that is *about the
  content's temperature* — the air over hot tiles behaves like
  noon air, and its absence later in the page is the proof of
  cooling that no copy has to claim. When the shimmer stops, the
  visitor *feels* the afternoon turn.
- **Structure.** A `::before` layer on sections in the noon and
  afternoon bands (declared per section in the survey, §15), an
  SVG-turbulence displacement over a transparent gradient strip
  occupying the section's top 18%, `pointer-events: none`,
  composited above the wall but *below* the section's first line
  of text (z-order law: shimmer crosses the ridge and the wall's
  empty head, never a glyph). Amplitude is a custom property,
  `--shimmer`, written by the shared loop from `dayTime`:
  full (1.0) at t≤0.16, falling linearly to 0 at t=0.55.
- **Motion spec.** Ambient loop: the turbulence base frequency
  oscillates 0.012 ↔ 0.02 over a 2.6s cycle `--ease-cloud`,
  displacement scale 4px × `--shimmer`. Gated twice: by band
  (amplitude is 0 past t=0.55 regardless of section) and by
  visibility (paused when the section is off-screen or the tab
  hidden). It never starts on a section the visitor arrives at
  after t=0.55 — late arrivals get still air, which is the truth
  of the hour.
- **States.** Shimmering (noon/afternoon, amplitude by `t`) →
  thinning (0.35<t<0.55) → still (t≥0.55, permanent for the
  session — air does not reheat on this page, even if the
  visitor scrolls back to noon: the *shadows* rewind, the air
  remembers. This asymmetry is declared, not accidental: §13's
  reverse-pass rule). Hover/focus: none.
- **Content merge.** The shimmer lives over the section's own
  ridge and head-space — it is the air of that section's hour.
  It carries no content and covers none; its whole job is to be
  the temperature of the room the content sits in.
- **Failure fallback.** No SVG-filter support: the layer is
  simply absent — still air at noon, a lesser page but a complete
  one. Watchdog: if the filter costs >0.5ms/frame sustained, the
  loop sets `--shimmer: 0` and the day proceeds unshimmered (§14's
  cut order, applied live).
- **Reduced-motion variant.** Absent entirely. The noon sections
  stand in still air; §6.1's apparatus line in this mode carries
  the temperature as a figure instead ("33° AT NOON — THE AIR
  STOOD STILL OVER THE TILES" is §6.14's job; the shimmer adds
  no line of its own).
- **Performance budget & mobile variant.** SVG filter on a
  clipped strip only; ≤0.5ms/frame, first in §14's cut order.
  Mobile: **cut entirely** — phone GPUs pay the most for filters
  and the noon sections read perfectly in still air; the mobile
  day is told by shadows and figures alone.
- **Choreography timeline (v2).** Continuous while live: 2.6s
  oscillation cycle; amplitude follows `dayTime` per frame;
  t=0.55 crossing begins a 900ms `--ease-cloud` fade of the
  residual amplitude to 0 (the air settles, it does not switch
  off) → still for the rest of the page.
- **State matrix (v2).** *Rest:* shimmering at band amplitude.
  *Hover:* none. *Focus:* none (never on focusable content — the
  strip is above the wall's head, clear of controls). *Active:*
  n/a. *Scrolled-past:* amplitude follows `t`; off after the
  siesta crossing. *Disabled:* layer absent. *Touch:* n/a
  (mobile cuts the layer).
- **Breakpoints (v2).** ≥1200px: full layer, 18% strip.
  768–1199px: strip 14%, displacement 3px. <768px: cut (above).
- **Edge cases & failure modes (v2).** *Low-power device:*
  `hardwareConcurrency` ≤2 or a sustained frame cost breach
  stills the air from load. *Section re-entering after dusk:*
  stays still (the declared asymmetry). *Filter unsupported in
  the browser:* absent, silently — no fallback shimmer is faked
  with opacity tricks; fake heat is worse than still air.
- **Accessibility spec (v2).** Purely decorative, `aria-hidden`,
  outside the accessibility tree, never over text (z-order law),
  and it stops under `prefers-reduced-motion` and on request of
  the performance watchdog. It carries no information: the
  temperature is always also a figure (§6.14).
- **Tokens consumed (v2).** `--shimmer`, `--ease-cloud`,
  `--dur-shimmer-cycle` (2600ms), `--bleached`, `--terra`.

### 6.7 Cloud-shade hover

- **What & why.** Hovering a tile card slides a soft, tile-shaped
  shadow over it — a passing cloud — cooling the card's colours
  slightly as it crosses. It belongs because shade is the
  visitor's first physical act on this page: their hand over the
  tile, relief performed on the product itself. Where other themes
  lift a card toward the visitor, this one *shades* it — the
  correct Mediterranean response to attention at noon is not more
  sun but less.
- **Structure.** A shade layer inside the card (§6.12): a
  rounded-rect gradient in `--shadow-ink` at 0% → 22% opacity,
  shaped as a barrel-tile silhouette (the card's own proportions,
  softened 12px), translating across the card on a custom property
  the shared loop lerps. Beneath it, the card's terracotta cools:
  a `--bleached`-to-`--terra` mix shift on the card's fired
  surfaces, driven by the same property, so shade and cooling are
  one event, not two.
- **Motion spec.** Trigger: hover (pointer-fine) or focus-within.
  The shade slides in from the card's left over 400ms
  `--ease-cloud`, crossing to cover 88% of the card, and holds
  while hovered. On leave it continues across and out the right
  side over 500ms — a cloud does not reverse; it passes. The
  cooling ramp is 300ms in, 600ms out (clay cools slower than it
  shades: the asymmetry is the material's). Keyboard focus gets
  the shade at rest position (centred, no travel) applied in
  120ms — a keyboard visitor's cloud arrives already overhead.
- **States.** Unshaded (rest) → shading (400ms) → shaded (held;
  colours cooled ~8% toward bleached) → passing (500ms out) →
  unshaded. Active (pressed): the shade deepens to 28% for the
  press — a hand pressing is a hand shading harder.
  Scrolled-past: n/a. Disabled card: no shade; a sold tile takes
  no cloud (§6.12's sold state).
- **Content merge.** The shade falls on the card's own tile body;
  the card's name, batch and price sit on its wall strip (§6.12),
  which the shade never covers — the product is shaded, its tag
  stays in the sun and readable. That split is the element's
  merge: weather on the clay, legibility on the paper.
- **Failure fallback.** No JS / no hover capability: cards rest
  unshaded; focus still shows the fired outline. The shade is an
  enhancement of a complete card, never a gate to its content.
- **Reduced-motion variant.** No travel: hover applies the cooled
  colour mix instantly at 60% strength, removed instantly on
  leave. Shade as a state, not a journey.
- **Performance budget & mobile variant.** One gradient layer +
  one colour mix per hovered card; ≤0.2ms/frame, one card at a
  time (a second hover ends the first's pass instantly). Touch:
  no hover shade — first tap is the card's link (§6.4's rule);
  long-press is not hijacked.
- **Choreography timeline (v2).** t=0 pointer enters → t=0–400
  shade crosses to 88% cover → t=100–400 cooling ramps in →
  held while hovered → on leave: t=0–500 shade exits right →
  t=0–600 cooling releases → rest.
- **State matrix (v2).** *Rest:* unshaded, full colour. *Hover:*
  as spec. *Focus:* centred shade in 120ms + fired outline.
  *Active:* shade 28%. *Scrolled-past:* n/a. *Disabled:* no
  shade, card at sold rest (§6.12). *Touch:* no shade; tap
  navigates.
- **Breakpoints (v2).** ≥1200px: full travel, 88% cover.
  768–1199px: cover 80%, travel 350ms. <768px: no hover (touch
  rules); focus shade still applies for switch/keyboard users.
- **Edge cases & failure modes (v2).** *Pointer skims a row:*
  each card's pass is independent and a skim shades each briefly
  — a cloud street; passes cap at 3 concurrent, further cards
  cool without travel. *Hover during §6.4's laying:* the shade
  waits until the card lands — you cannot shade a tile still in
  the roofer's hands. *Leave mid-entry:* the pass continues out
  from its current position (never snaps back).
- **Accessibility spec (v2).** The shade never covers the card's
  text strip (z-order law), so contrast is unchanged in every
  state — verified in the gate (§10). Focus shade + outline
  together meet the visible-focus requirement; the shade alone
  would not, and is never the only indicator.
- **Tokens consumed (v2).** `--shadow-ink`, `--terra`,
  `--bleached`, `--fired`, `--ease-cloud`, `--dur-shade-in`
  (400ms), `--dur-shade-out` (500ms).

### 6.8 Lamplight pools

- **What & why.** The finale pins on the dusk-violet ground while
  warm pools of lamplight gather around the last content blocks,
  brightening as each block centres — evening content is *lit*,
  not just recoloured. It belongs because it is the day's reward
  and the theme's closing argument: after seven hours of the sun
  doing the lighting, the page ends with light at human scale,
  placed around the words being read. The pin is the street at
  nightfall — you stop walking and gather where the lamps are.
- **Structure.** A pinned region (160vh of scroll) containing the
  finale's blocks (the closing claim, the day book's totals
  excerpt, the order form's dusk appearance per §7) on `--dusk`
  ground. Each block carries a pool: a radial gradient layer
  (`--lamp` core → transparent at 62%) sized 140% of the block,
  centred on it, opacity written by the shared loop as a function
  of the block's distance from the viewport centre. Dust motes
  (§5's second ambient loop) drift only inside pools whose
  opacity exceeds 0.5 — 14 motes per pool, canvas-free, as
  transformed dots.
- **Motion spec.** Trigger: the finale's approach (t≥0.85, §2's
  dusk band). The pin engages; across the pinned scroll each
  block's pool gathers 0 → full over the block's centre-crossing,
  `--ease-lamp` on the loop's evening lerp (0.12) — a pool is
  full (opacity 0.9, core `--lamp` at 34%) when its block is
  centred, and dims to 0.35 as the block leaves centre: you read
  by the lamp you are under. The ground's own violet deepens
  `--dusk` → `--dusk-deep` across the pin's first third, so the
  pools gather against a darkening street.
- **States.** Ungathered (before the band) → gathering (pool
  ramping) → lit (block centred) → dimming (block leaving) →
  the last block stays lit at the pin's end — the page ends
  under a lit lamp, never in the dark. Hover on a block: its
  pool warms +6% (a lamp leans toward a reader). Focus within a
  block: its pool goes full instantly — a keyboard reader's lamp
  is lit on arrival, not on centring.
- **Content merge.** The pools are centred on the content blocks
  themselves and sized to them; the light exists because the
  block is there. Remove a block and its pool is removed — the
  lamps light the reading, not the street in general.
- **Failure fallback.** No JS / no pin support: the finale stands
  unpinned on `--dusk`, pools printed at their lit state (0.9)
  around every block — a lamplit street, static. Text contrast
  never depends on a pool: lime on dusk is 11.29:1 unlit (§2);
  pools only add warmth.
- **Reduced-motion variant.** No pin. Blocks stack on dusk-deep,
  each pool printed lit, motes absent. One apparatus line at the
  finale's head: "READ BY LAMPLIGHT — THE POOLS WERE ALREADY
  LIT." The evening is kept; the gathering rests.
- **Performance budget & mobile variant.** ≤3 pools animating
  (opacity only) + ≤42 mote transforms; ≤0.8ms/frame. Mobile:
  the pin shortens to 120vh, pools size 120%, motes cut to 8 per
  pool and cut entirely under the performance watchdog — a
  phone's evening is lamplit but still.
- **Choreography timeline (v2).** t=0.85 band crossing: ground
  begins deepening → pin engages → block 1's pool gathers as it
  centres (≈pin 20%) → block 2 gathers as block 1 dims to 0.35
  (≈pin 55%) → final block gathers (≈pin 85%) and holds → pin
  releases into the colophon (§6.17) already lamplit.
- **State matrix (v2).** *Rest (block centred):* pool full.
  *Hover:* pool +6% warmth. *Focus:* pool full instantly.
  *Active:* n/a. *Scrolled-past (block above centre):* pool at
  0.35, still warm. *Disabled:* n/a. *Touch:* identical scrub;
  no hover warmth (no hover), focus rule applies on tap-focus.
- **Breakpoints (v2).** ≥1200px: pin 160vh, pools 140%.
  768–1199px: pin 140vh, pools 130%. <768px: pin 120vh, pools
  120%, motes 8/pool.
- **Edge cases & failure modes (v2).** *Finale with one block:*
  its pool gathers and holds; the pin shortens to 110vh (a
  one-lamp street is a short stop). *Finale with many blocks
  (>4):* pools cap at 3 concurrent ramps; later blocks print
  lit when centred if the queue is full — no block is ever left
  dark at centre. *Jump into the finale:* pools print at the
  state for the landing position; the last block lit if the
  footer is reached.
- **Accessibility spec (v2).** The pin never traps focus: content
  order is DOM order, and the pinned visual is a transform of
  the natural layout. Contrast is pool-independent (§2 law).
  Motes are `aria-hidden` and pause off-screen. The finale's
  heading is a real heading; the evening is announced by
  structure, not by darkness.
- **Tokens consumed (v2).** `--dusk`, `--dusk-deep`, `--lamp`,
  `--bleached`, `--lime`, `--ease-lamp`, `--lerp-pm` (0.12).

### 6.9 The lamp click

- **What & why.** In the dusk sections, clicking a content block
  lights a small lamp at the click point — a warm glow that
  kindles there and stays lit for the session. It belongs because
  it completes the day's exchange: all page long the sun lit the
  visitor; at dusk, the visitor lights the page, point by point,
  on the content they touch. It is also §1's second honesty: the
  colophon's lamp count (§6.17) is exactly the number of lamps
  lit here — a lamp is lit by a hand, or it is not counted.
- **Structure.** Each dusk block (§6.8's finale and any §7 dusk
  region) carries a lamp layer: a radial glow (`--lamp` core,
  120px radius desktop) centred on a stored click point, plus a
  6px lamp dot at its heart. Lit lamps persist in a session map
  (`sessionStorage`: block id + relative click coordinates), so
  the street a visitor lit is the street they find on return.
  Unlit blocks carry no layer in the DOM until first lit.
- **Motion spec.** Trigger: click/tap on a dusk block (not on a
  link or control inside it — those keep their own jobs). The
  lamp kindles over 650ms `--ease-lamp`: dot first (120ms), then
  the glow blooming 0 → 26% opacity with a 40ms hesitation at
  30% bloom (a lamp catching), settling at rest. A second click
  on a lit block does not extinguish it — lamps, once lit, stay
  lit for the evening (the session); the click instead warms the
  glow +4% for 900ms, an acknowledgment. There is no un-lighting:
  the theme has no switch-off gesture, because an evening is not
  undone.
- **States.** Unlit (no layer) → kindling (650ms) → lit (rest,
  glow 26%, dot full `--lamp`) → warmed (transient +4% on
  re-click). Focus: keyboard users light the focused block's
  lamp with the `L` key or the block's lamp button (§11) — the
  lamp is a control, not a mouse treat; the button sits in the
  block's apparatus line ("LIGHT THE LAMP"). Scrolled-past:
  lamps stay lit behind the visitor.
- **Content merge.** The lamp lights at the point the visitor
  touched, on the block they touched — the glow is centred on
  their reading, not on a decorative fixture. The count it feeds
  (§6.17) is the colophon's closing fact: how much of this
  evening the visitor made themselves.
- **Failure fallback.** No JS: no lamps, and the colophon prints
  its fallback wording ("THE LAMPS WERE LIT FOR YOU" — pools at
  their printed state, §6.8). Storage unavailable: lamps light
  for the page view and the colophon counts the live DOM, not
  the map — the count stays true either way.
- **Reduced-motion variant.** The lamp appears at rest instantly
  (no kindle, no hesitation). The lighting still happens — it is
  an act, not an animation — only the bloom rests.
- **Performance budget & mobile variant.** One radial layer per
  lit block, opacity-only after kindling; ≤0.1ms/frame. Mobile:
  glow radius 84px; tap targets are the blocks themselves (≥64px
  tall in the finale by §4's density law).
- **Choreography timeline (v2).** t=0 click → t=0–120 dot
  kindles → t=120–160 hesitation → t=160–650 glow blooms to
  26% → rest lit; the session map writes at t=650 (a lamp is
  counted when it has caught, not when it was struck).
- **State matrix (v2).** *Rest (unlit):* no layer, block at pool
  light (§6.8). *Hover:* a 6% pre-glow at the pointer's block
  position on pointer-fine — the promise of a lamp, gone on
  leave. *Focus:* the lamp button shows its fired outline.
  *Active:* the kindle. *Scrolled-past:* lit state persists.
  *Disabled:* n/a. *Touch:* tap on the block lights it; tap on
  a link navigates (target discrimination by event target).
- **Breakpoints (v2).** ≥1200px: glow radius 120px. 768–1199px:
  100px. <768px: 84px, dot 5px.
- **Edge cases & failure modes (v2).** *Click near a block's
  edge:* the glow centres on the click but clamps 24px inside
  the block — a lamp is lit on the wall, not half off it.
  *Many lamps:* no cap — a visitor who lights the whole street
  gets the whole street lit, and the colophon says so.
  *Session return:* lamps restore at rest instantly, no
  re-kindling ceremony.
- **Accessibility spec (v2).** The lamp button is a real
  `<button>` with `aria-pressed` and the label "Light the lamp
  by this block" / "Lamp lit". Mouse clicks on the block are a
  shortcut to the same action, never the only path. Lighting is
  confirmed visually and by the button's state, not by sound or
  announcement spam (the colophon's count is the record).
- **Tokens consumed (v2).** `--lamp`, `--dusk`, `--ease-lamp`,
  `--dur-kindle` (650ms), `--ease-stamp`.

### 6.10 The ridge-line navigation (page family: navigation)

- **What & why.** The site's navigation is a roofline: a fixed
  bar whose underside is a shallow tile ridge, its links lettered
  on the wall strip beneath it, and — at its right end — the
  sundial's margin chip carrying the live reading (§6.3's
  handover). It belongs because the visitor should always be
  under the site's roof: the nav is the street's continuous
  roofline, and its chip is the courtyard dial retired to the
  margin, still telling the same time from the same function.
- **Structure.** A `<header>` bar, `--lime` ground, with an SVG
  ridge strip (the §4 arc at 40% depth) along its bottom edge.
  Links in Alegreya 500, current section marked by a fired rule
  beneath the word and `aria-current`. The chip: a 44px pill in
  `--terra` with the reading in apparatus (`--lime` text at
  11.29:1 against the chip's dusk edge — the chip is dusk-ground
  from noon on: the instrument that reports the day is already
  shaded, like a real dial's face). The bar ships fully lettered;
  JS adds only the chip's live updates and the current-section
  tracking.
- **Motion spec.** The bar is sticky; on scroll down past 240px
  it compresses (ridge strip flattens, bar 64px → 48px) over
  300ms `--ease-lay` — the roofline lowers as you commit to the
  street — and restores on scroll up. The current-section rule
  migrates between links over 260ms `--ease-ridge` as sections
  pass the reading line. The chip's reading steps on minute
  changes only (§6.3's rule, same `t`).
- **States.** Full (top) → compressed (scrolled) → full (return
  to top). Hover on a link: its word warms to `--fired`.
  Focus: fired outline. Active section: rule + word in `--ink`.
  The chip never animates except its figures stepping.
- **Content merge.** The nav is the roof of every room; its chip
  is the page's clock in the margin. It carries the site's real
  sections and the real time — furniture, not decoration.
- **Failure fallback.** No JS: full bar, all links, chip printed
  "12:00" (the held day's truth). The bar never hides content:
  compression is disabled if it would overlap a focused link.
- **Reduced-motion variant.** Bar fixed at 56px, no compression;
  the rule jumps between sections; chip reading still steps
  (figures are information, not motion).
- **Performance budget & mobile variant.** Sticky + one transform;
  negligible. Mobile: the ridge strip stays (it is the brand),
  links collapse to a "ROOFLINE" toggle opening a wall panel of
  the same links; the chip remains visible at 40px — the time is
  never menu-hidden.
- **Choreography timeline (v2).** Scroll past 240px: compress
  300ms → section crossings: rule migrates 260ms → minute
  changes: chip steps → hero re-entry: the chip hands the
  reading back to §6.3's dial (same value, same frame).
- **State matrix (v2).** *Rest:* full at top, compressed below.
  *Hover:* link warms. *Focus:* outline; bar un-compresses if
  the focused link is inside it. *Active:* current rule.
  *Scrolled-past:* n/a. *Disabled:* n/a. *Touch:* toggle panel;
  chip tappable to the day book (§6.16).
- **Breakpoints (v2).** ≥1200px: full links + chip. 768–1199px:
  links at 15px, chip kept. <768px: toggle panel + chip.
- **Edge cases & failure modes (v2).** *Long section names:*
  links truncate never — the bar wraps its wall strip to two
  lines before it shrinks a word. *Chip vs dial disagreement:*
  impossible by construction (one `t`); the gate tests it
  anyway (§10).
- **Accessibility spec (v2).** Real `<nav>` with labelled links;
  `aria-current="location"` migrates with the rule. The chip is
  an `<output>` twin of §6.3's reading, `aria-live="off"`.
  Toggle is a real button with `aria-expanded`. Targets ≥44px.
- **Tokens consumed (v2).** `--lime`, `--terra`, `--fired`,
  `--ink`, `--dusk`, `--ease-lay`, `--ease-ridge`.

### 6.11 The noon hero composition (page family: hero)

- **What & why.** The first screen is a courtyard wall at noon:
  the works' name stamped across it (§6.1), the sundial in its
  corner (§6.3), a first course of tiles along its foot, and
  nothing else competing. It belongs because the hero must state
  the theme's whole contract in one glance — a wall, a sun, an
  instrument, a product — at the hour the day begins. A hero that
  opens at golden hour has spent the theme's arc before the
  visitor has read a word.
- **Structure.** A `<section>` on `--lime`, one viewport tall
  (min 92vh): headline (§6.1) upper-left on the wall, standfirst
  beneath it, the primary action ("SEE THE COURSES" → §6.12's
  grid; "THE DAY BOOK" → §6.16) as two wall-lettered links; the
  sundial (§6.3) top-right; along the foot, a single course of
  three tile cards (§6.12) half-laid — the roof beginning. The
  DOM ships complete: headline lettered, dial drawn at noon,
  course laid.
- **Motion spec.** On load: §6.1's stamp (240ms), §6.3's hour
  lines drawing (900ms), the foot course laying (§6.4's grammar,
  two rows of stagger compressed to one: 120ms). The hero's own
  parallax: as the hero leaves, its wall scrolls at 1.0× and its
  ridge cap at 0.92× (§5's pair) — the roof lifts away slower
  than the wall, the day's first depth cue. Nothing else moves;
  noon is still.
- **States.** Composing (load, ≤1100ms of staggered arrivals) →
  standing at noon → leaving (parallax) → past (the dial retired
  to §6.10's chip). Hover/focus: per §6.3/§6.12.
- **Content merge.** Every hero element is a working instrument
  or product: the name, the dial, the first tiles. There is no
  hero *image* — the wall is the image, and it is load-bearing.
- **Failure fallback.** No JS: the composed noon stands at first
  paint — headline, dial at 12:00, course laid, actions linked.
- **Reduced-motion variant.** The composed noon, static, with
  §6.1's apparatus line under the standfirst naming the resting
  hour.
- **Performance budget & mobile variant.** The hero is type, one
  SVG dial and three cards: ≤120KB total, no raster image.
  Mobile: dial 96px in the corner (§6.3), headline clamp floor,
  the foot course becomes one card wide and two courses tall —
  the roof begins smaller, the wall is the same wall.
- **Choreography timeline (v2).** t=0 paint (composed) → stamp
  at fonts-ready → dial lines t=0–900 → foot course lays
  t=200–800 → stillness → first scroll: parallax pair separates,
  §6.2's shadows begin to lengthen.
- **State matrix (v2).** *Rest:* standing at noon. *Hover:* per
  children. *Focus:* first focusable is the primary action;
  focus into the hero never triggers a re-stamp. *Active:* n/a.
  *Scrolled-past:* parallax complete, dial handed over.
  *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full composition, 168px dial.
  768–1199px: dial 132px, foot course 2 cards. <768px: dial
  96px, course 1×2, headline at clamp floor, min-height 88vh.
- **Edge cases & failure modes (v2).** *Very tall viewport:*
  the hero caps at 1080px of wall; extra height goes to the
  street below, not to a vaster noon. *Headline longer than two
  lines:* refused at build (law: the name fits its wall) —
  shorten the name's line, never shrink below the clamp floor.
- **Accessibility spec (v2).** Landmark order: h1 → standfirst →
  actions → dial (as §6.3's labelled link) → course list. The
  hero's contrast is the palette's best (10.17:1); nothing in
  the hero is conveyed by shadow alone.
- **Tokens consumed (v2).** `--lime`, `--ink`, `--terra`,
  `--fired`, `--ease-stamp`, `--ease-lay`.

### 6.12 Tile cards (page family: cards / listing)

- **What & why.** A product is a tile: a card whose body is the
  tile itself — terracotta face with its batch variation, ridge
  curve along its top — and whose name, firing record and price
  are lettered on a lime wall strip at its foot, the way a tile's
  tag hangs in the yard. It belongs because the card does not
  *represent* the product; at card scale it *is* the product,
  laid in the course grid (§4) and laid by §6.4's crew.
- **Structure.** An `<article>` in the course grid: the tile face
  (a CSS/SVG barrel-tile rendering or the product photograph
  clipped to the tile's curve — photographs are clipped to the
  tile shape, never shown as rectangles: §9, item 6), a variation
  note in the face's corner apparatus ("BATCH 214 — FIRED 9 DAYS"),
  and the wall strip: name (Marcellus), record line (apparatus:
  clay, firing, count in stock), price (Marcellus, §3). The whole
  card is one link to the tile's detail (§7). Sold tiles stay in
  the course, their strip stamped "LAID — [ROOF NAME]" in fired:
  a sold tile is a roof somewhere, and the grid keeps its place.
- **Motion spec.** Entrance: §6.4's laying. Hover: §6.7's cloud
  shade over the face only. The face's own life: a slow sheen —
  the tile's fired glaze catching the hour — a gradient whose
  angle follows `--sun-angle` (§6.3's property), so a card's
  glaze brightens on the side the sun has reached. That is the
  card's only independent motion, and it is borrowed from the
  one sun like everything else.
- **States.** Unlaid → laid (§6.4) → shaded (§6.7 hover) →
  sold (stamped strip, no shade, link becomes the roof's story
  in the day book). Focus: fired outline + centred shade (§6.7).
  Scrolled-past: laid, sheen at the current angle.
- **Content merge.** Face, record and price are the product's own
  facts; the sheen is the day's light on its glaze. Nothing on
  the card is decoration: remove the photograph and the tile
  face still carries the batch variation as a colour fact.
- **Failure fallback.** No JS: cards stand laid, priced, linked.
  Photograph failure: the face falls back to its batch colour
  (a declared per-batch tint) with the variation note intact —
  a tile is still a tile without its portrait.
- **Reduced-motion variant.** Cards stand laid; the sheen rests
  at the late-afternoon angle; shade is §6.7's instant variant.
- **Performance budget & mobile variant.** Faces are CSS/SVG or
  one photograph ≤40KB each, lazy below the second course.
  Mobile: cards are 2 modules wide still (§4) in a single
  column of courses; the sheen angle still tracks the sun.
- **Choreography timeline (v2).** Per §6.4 for laying; sheen
  continuous with `t`; shade per §6.7; sold stamp is a state,
  not an animation (it prints, 160ms `--ease-stamp`, when the
  day book's record changes — §6.16).
- **State matrix (v2).** *Rest:* laid, sheen at hour. *Hover:*
  shade over face. *Focus:* outline + shade. *Active:* press
  deepens shade (§6.7). *Scrolled-past:* laid. *Disabled
  (sold):* stamped, unshaded, still linked to its record.
  *Touch:* tap navigates; no shade.
- **Breakpoints (v2).** ≥1200px: 2×2-module cards, 3–4 per
  course. 768–1199px: 2 per course. <768px: 1 per course,
  face height 148px (one module), strip unchanged.
- **Edge cases & failure modes (v2).** *Long tile names:* the
  strip allows two lines and the course height absorbs them —
  courses align by their tallest card, like a roof course
  levelled by its thickest tile. *No photograph:* batch tint
  (above). *Price changes:* the strip re-letters instantly; a
  price never animates — figures step (§5).
- **Accessibility spec (v2).** One link per card with the full
  name + record as its label text; the face image is decorative
  (`alt=""`) when the strip carries the name, or labelled when
  it is the detail page's main portrait (§7). Sold state is
  text, not colour alone. Target: the whole card, ≥148px.
- **Tokens consumed (v2).** `--terra`, `--fired`, `--lime`,
  `--ink`, `--sun-angle`, `--ease-lay`, `--ease-cloud`,
  `--ease-stamp`.

### 6.13 The terrace order form — order by the hour (page family: forms / conversion)

- **What & why.** The conversion form is taken at dusk, on the
  terrace: the visitor states what they need in the yard's own
  units — tiles by the course, an area in square metres, a
  firing week — and the form does the yard's arithmetic aloud:
  tiles required = area × 16 per m² + 8% for breakage, both
  figures declared on the form itself, computed live from the
  visitor's own entries. It belongs because an order for clay is
  specified the way clay is specified — by count, coverage and
  firing — and a form that hides its arithmetic is a merchant's
  trick this yard does not play.
- **Structure.** A `<form>` on a lime wall (or in the finale's
  lamplight per §7's home map, where its fields sit in a pool,
  §6.8): inscription-line fields (§11) — name, direction (email),
  the tile (a seam list of the catalogue's tiles, §11's radio
  grammar), area in m² (number), firing week (a seam list of the
  day book's real upcoming firings, §6.16) — and the reckoning
  line: an `<output>` that recomputes on every keystroke: "214
  TILES — 198 TO LAY, 16 FOR BREAKAGE — BATCH 215, FIRED IN THE
  WEEK OF THE 14TH." The submit is a stamp press: "PRESS THE
  ORDER".
- **Motion spec.** Fields ink their rules on focus (200ms
  `--ease-lay`). The reckoning line re-letters instantly on
  change (figures step; §5) with a 120ms fired flash on the
  changed figure only. Choosing a firing week stamps that
  week's line (160ms `--ease-stamp`). Submit: the button presses
  2px (120ms `--ease-stamp`), and on success the form is
  replaced by a pressed order slip — the visitor's own figures
  lettered on a lime-deep slip with the order's day-book number
  ("ORDER No. 88 — ENTERED IN THE DAY BOOK") — which is also
  written to §6.16's record excerpt if the page shows one: the
  form and the book agree because they are the same entry.
- **States.** Empty (reckoning shows the formula, uncomputed:
  "— TILES — TELL US THE AREA") → reckoning (figures live) →
  error (a field's rule holds fired, the book's note beneath it
  in §12's voice) → pressing → entered (the slip). A failed
  submit keeps every field, the tile, the week and the reckoning
  exactly as left (gate §10, item 7).
- **Content merge.** The form's units, weeks and arithmetic are
  the yard's real ones, drawn from the day book (§6.16) and the
  catalogue (§6.12) — the same tile names, the same batch
  numbers, the same 16-per-m² the yard quotes on its wall.
- **Failure fallback.** No JS: the form posts natively; the
  reckoning line prints the formula and the yard computes on
  receipt (stated on the form: "WITHOUT THE RECKONING, WE COUNT
  BY HAND AND CONFIRM BY RETURN"). Nothing about the order
  depends on the animation layer.
- **Reduced-motion variant.** Rules ink instantly; the slip
  replaces the form without the press. The reckoning still
  computes — arithmetic is not motion.
- **Performance budget & mobile variant.** No animation beyond
  rules and the press; the reckoning is one listener. Mobile:
  fields stack, the reckoning line pins above the submit (a
  sticky wall strip) so the figures are visible at the moment
  of pressing — the count is checked before the stamp falls.
- **Choreography timeline (v2).** Focus: rule inks 200ms →
  typing: reckoning steps per keystroke → week chosen: stamp
  160ms → submit: press 120ms → success: slip replaces form
  (300ms `--ease-lay`) with the order number lettered → the
  day-book excerpt (§6.16), if present, gains the row.
- **State matrix (v2).** *Rest:* fields ruled pale. *Hover:*
  rule warms. *Focus:* rule inks + label lifts to apparatus.
  *Active:* press. *Scrolled-past:* n/a. *Disabled (submitting):*
  fields locked, button reads "PRESSING…". *Touch:* identical;
  number field uses the numeric keypad.
- **Breakpoints (v2).** ≥1200px: two-column fields, reckoning
  at the form's foot. 768–1199px: two columns narrow, reckoning
  full-width. <768px: single column, sticky reckoning strip.
- **Edge cases & failure modes (v2).** *Absurd area (0 or
  10,000 m²):* the reckoning answers in the book's voice —
  "NO ROOF" for 0, and for the vast: the true figure, plus
  "A ROOF OF THIS SIZE IS A VILLAGE — WRITE TO THE YARD
  DIRECTLY" with the form still submittable. *Tile sold out:*
  its seam line is struck through with its reason ("BATCH 214
  IS LAID OUT — NEXT FIRING THE WEEK OF THE 21ST") and cannot
  be chosen. *Network failure:* §8.3's rehearsal — words kept,
  note printed, nothing cleared.
- **Accessibility spec (v2).** Real labels, `aria-describedby`
  for the book's notes, errors announced via a polite live
  region *and* printed at the field (never only announced).
  The reckoning output is `aria-live="off"` (it changes per
  keystroke) but is focusable and labelled "The reckoning".
  Targets ≥44px; the press is a real submit button.
- **Tokens consumed (v2).** `--lime`, `--lime-deep`, `--ink`,
  `--fired`, `--lamp`, `--ease-lay`, `--ease-stamp`.

### 6.14 Day figures — temperature & light (page family: data)

- **What & why.** A band of the yard's figures, counted in the
  open: the current temperature (from `dayTime`, §5), the hours
  of light remaining (the same function read backwards), the
  tiles laid today and the batch in the kiln (both from the day
  book, §6.16). It belongs because the theme's numbers are its
  honesty on display — a visitor who trusts the 36° because it
  agrees with the sundial will trust the stock count because it
  agrees with the book. Figures here are instruments, not
  marketing statistics.
- **Structure.** A row of figure blocks on a lime-deep wall:
  each is an apparatus label ("TEMPERATURE", "LIGHT REMAINING",
  "LAID TODAY", "IN THE KILN"), a tabular Alegreya figure, and
  a source line in caption ("BY THE SUN", "FROM THE DAY BOOK —
  BATCH 214"). Temperature and light update from the loop;
  book figures are printed from the record object at build and
  re-letter only when the record changes (§6.13's orders).
- **Motion spec.** On the band's reveal (§6.5), book figures
  count up once from 88% of value to value over 900ms
  `--ease-lay`, stepped in whole tiles (a tally being chalked —
  the count arrives like a count, not like a slot machine).
  Temperature and light do not count up: they step to the true
  current value instantly and thereafter step per minute-change
  of `clock(t)` (§6.3's rule). Nothing in the band animates
  continuously; figures are read, not watched.
- **States.** Uncounted (pre-reveal) → counting (900ms, book
  figures only) → standing (all figures at truth, sun figures
  stepping with the day). Hover: a figure's source line warms —
  the band invites audit. Focus: figures are focusable as a
  group with the source lines as their description.
- **Content merge.** Every figure names its source on its face;
  the band is the day book's and the sun's public reading. A
  figure without a source line may not be printed (gate §10).
- **Failure fallback.** No JS: all figures print at their noon /
  record values — temperature 33°, light 7 H 40 M, book figures
  as entered. Loop stall: sun figures snap per §6.2's watchdog.
- **Reduced-motion variant.** All figures print at truth; no
  count-up. The band is identical, stiller.
- **Performance budget & mobile variant.** ≤4 figure updates per
  minute-change; negligible. Mobile: the band wraps 2×2; source
  lines keep (they are the point).
- **Choreography timeline (v2).** Section opens (§6.5) → book
  figures count 900ms → standing → per minute-change of the
  day: temperature/light step → on a §6.13 order: "LAID TODAY"
  does not change (orders are not layings — the book distinguishes,
  §6.16) but the kiln figure may gain the order's batch note.
- **State matrix (v2).** *Rest:* standing at truth. *Hover:*
  source warms. *Focus:* group outline + sources described.
  *Active:* n/a. *Scrolled-past:* standing; sun figures keep
  stepping (they are live instruments, read on return).
  *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: one row of 4. 768–1199px: one
  row, tighter. <768px: 2×2 grid.
- **Edge cases & failure modes (v2).** *Temperature at band
  boundaries:* the figure is `round(T(t))` — the formula is
  printed in §5, so a visitor can check the rounding at the
  peak (36° at t=0.45 exactly). *Book figure disputed:* the
  source line names the batch; the day book (§6.16) is the
  appeal. *Midnight race (real clock):* none — the page's day
  is scroll's, not the wall clock's; the figures never read the
  visitor's actual time.
- **Accessibility spec (v2).** Figures are text, tabular, with
  their labels and sources in reading order; the live sun
  figures are `aria-live="off"` with the current reading
  available in §6.3's output — one clock voice per page, not
  three announcing.
- **Tokens consumed (v2).** `--lime-deep`, `--ink`, `--fired`,
  `--ease-lay`, `--dur-count` (900ms).

### 6.15 Lime-wash skeleton + ridge-pass transition (page family: loader / transition)

- **What & why.** Loading in this theme is a wall being
  lime-washed: placeholder blocks stand as pale wash shapes —
  the wall's rectangles without their lettering — and resolve
  into content as it arrives, course by course. Leaving a page
  is a ridge pass: the current section's ridge sweeps down over
  the viewport as the new page's first ridge rises beneath it.
  Both belong because the yard has no spinners and no fades-to-
  white: a wall is washed before it is lettered, and you leave
  a room by passing under its roofline.
- **Structure.** Skeleton: the real layout (ridge, wall, course
  grid) with content blocks as `--lime-deep` wash rectangles at
  the true sizes of the incoming content — the skeleton is the
  page's own geometry, unpainted. Transition: a full-viewport
  ridge strip (the §4 arc, full depth) that sweeps down 520ms,
  holds 80ms while the route changes beneath it, and rises
  520ms to reveal the new page's head already composed.
- **Motion spec.** Skeleton resolve: as each block's content
  arrives it is lettered in over 300ms `--ease-lay`, in course
  order (top course first — a wall is read from its ridge
  down); a block unresolved at 4000ms shows the book's note
  ("THIS COURSE IS STILL IN THE KILN") with a retry — never a
  permanent wash ghost. Transition: on internal navigation,
  sweep down 520ms `--ease-ridge`, swap, rise 520ms; the new
  page's `t` is its own (each page keeps its own day from its
  own scroll — the transition does not carry the hour across;
  §7's pages each start at their own noon or declared hour).
- **States.** Washing → resolving (per block) → lettered.
  Transition: standing → passing (down) → held (80ms) →
  rising → standing on the new page. A second navigation during
  a pass queues after the rise; rapid double-navigation cancels
  to an instant swap (the street does not perform for a visitor
  running through it).
- **Content merge.** The skeleton *is* the page's layout; the
  ridge that passes is the section's own ridge, enlarged. Both
  are the architecture doing double duty, not loading theatre
  pasted over it.
- **Failure fallback.** JS-off or transition failure: instant
  navigation, pages composed at rest (the shipped state).
  Skeleton data failure: the kiln note + retry, per block —
  one failed course never blanks a wall.
- **Reduced-motion variant.** No pass: instant navigation. No
  wash: content blocks appear as they arrive, unanimated.
- **Performance budget & mobile variant.** The pass is one
  transformed strip, ≤1.0ms/frame, and is cut second in §14's
  order. Mobile: pass shortens to 380ms each way; skeleton
  identical (geometry is geometry).
- **Choreography timeline (v2).** Load: wash stands → blocks
  resolve in course order, 300ms each, staggered by arrival →
  page lettered. Navigation: click → ridge descends 520ms →
  80ms hold (route swap) → ridge rises 520ms → new page at
  rest, its instruments live.
- **State matrix (v2).** *Rest:* lettered / standing. *Hover:*
  n/a. *Focus:* focus is placed at the new page's heading after
  a pass (announced by the heading itself). *Active:* the pass.
  *Scrolled-past:* n/a. *Disabled:* retry button states per
  §11. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: pass 520ms, full-depth ridge.
  768–1199px: 460ms. <768px: 380ms, ridge at 70% depth.
- **Edge cases & failure modes (v2).** *Slow route (>1200ms
  under the ridge):* the held ridge gains the book's line
  ("UNDER THE RIDGE — THE NEXT ROOM IS BEING LAID") at 1200ms;
  a pass never holds silently past that. *Back/forward:* the
  pass does not run on history navigation (the browser's own
  gesture wins). *Prefetch:* prefetched pages skip the wash.
- **Accessibility spec (v2).** The skeleton uses `aria-busy` on
  the wall region with content announced once when lettered;
  wash shapes are `aria-hidden`. The pass never moves focus
  except to the new heading, per SPA practice, and is skipped
  entirely under reduced motion.
- **Tokens consumed (v2).** `--lime-deep`, `--terra`, `--fired`,
  `--ink`, `--ease-ridge`, `--ease-lay`, `--dur-pass` (520ms).

### 6.16 The day book (page family: trust / record)

- **What & why.** The works' ledger, printed on the page: the
  current batch's firing (number, clay, days in the kiln, tiles
  out), the tiles laid and the roofs they went to, the hours of
  sun the yard has worked — every figure §6.14 prints and every
  week §6.13 offers, drawn from this one record. It belongs
  because a yard that asks to be trusted with a roof shows its
  book; and mechanically, the book is the single data object
  the figures, form weeks and footer totals all render from —
  the three-printings guarantee (§10) is a data decision
  before it is a design one.
- **Structure.** A ledger section on lime: a head rule that
  draws on entry (a steady 600ms draw on `--ease-lay`),
  ruled rows (batch / clay / firing days / tiles out / state),
  a totals line, and the marginal notes in Alegreya italic (§3)
  — the bookkeeper's hand: "Batch 213 came out dark at the
  edges; those tiles are seconds and are priced as seconds, in
  the course below." Seconds are *in* the book, priced in the
  grid (§6.12) as seconds: the record does not hide the kiln's
  bad days.
- **Motion spec.** Entry: the head rule draws 600ms; rows are
  printed standing (a ledger is not performed). On a §6.13
  order, the book gains the order's row at the totals line —
  lettered in over 300ms `--ease-lay` with its number — so a
  visitor who orders sees the book take their entry before
  they leave. Nothing else moves; the book's stillness is its
  authority.
- **States.** Standing (rest) → gaining a row (on order) →
  standing. Hover on a row: its rule warms. The marginal notes
  never animate.
- **Content merge.** The book is not a trust badge near the
  content; it is the content's source, printed. §6.14's figures
  cite it, §6.13's weeks come from it, §6.17's totals close it.
- **Failure fallback.** No JS: the book stands printed from the
  build's record object — the same object the static figures
  use, so no-JS and JS pages show the same book.
- **Reduced-motion variant.** Identical, minus the head rule's
  draw (printed drawn).
- **Performance budget & mobile variant.** Static text; the
  rule draw is one stroke. Mobile: rows stack as ledger entries
  (label above figure), marginal notes keep — a small book is
  still a book.
- **Choreography timeline (v2).** Section opens (§6.5) → head
  rule draws 600ms → rows read → (on order) new row letters in
  300ms at the totals → the colophon's totals (§6.17) already
  include it, being the same object.
- **State matrix (v2).** *Rest:* standing. *Hover:* row rule
  warms. *Focus:* rows are not focusable; the book's one link
  (to the full record page, §7) takes the fired outline.
  *Active:* n/a. *Scrolled-past:* standing. *Disabled:* n/a.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: ruled table rows. 768–1199px:
  same, tighter measure. <768px: stacked entries.
- **Edge cases & failure modes (v2).** *A batch with no tiles
  out yet:* its row reads "IN THE KILN — OPENS [DAY]" — the
  book prints the kiln's present tense honestly rather than a
  zero dressed as a count. *Disputed figure:* the book is the
  appeal (§6.14); its rows carry dates so a figure can be
  checked against a day.
- **Accessibility spec (v2).** A real `<table>` with a caption
  ("The day book — batches and layings") and scoped headers;
  marginal notes are table-adjacent paragraphs, associated by
  order. Figures tabular (§3, law 4).
- **Tokens consumed (v2).** `--lime`, `--ink`, `--fired`,
  `--ease-lay`, `--dur-book-rule` (600ms).

### 6.17 The lamplight colophon (page family: footer)

- **What & why.** The footer is the day closed: dusk-deep
  ground, the sundial's final reading printed as a fact —
  "19:40 — THE DAY IS DONE" — the day book's totals (tiles
  fired, tiles laid, hours of sun), the lamps the visitor lit
  (§6.9) counted in the closing sentence, and the yard's
  imprint. It belongs because a theme that runs a whole day
  owes the visitor its closing entry; the colophon is the day
  book's last page, written at the hour the book shuts.
- **Structure.** A `<footer>` on `--dusk-deep`: the closing
  sentence (Alegreya 500, §3) — "The yard fired 1,180 tiles
  this week and laid three roofs. You lit 2 lamps." — the
  totals row (apparatus, `--lamp` figures), the imprint and
  links in lime, and one lamp glyph lit in the corner for each
  lamp the session lit, up to the count — the glyphs are the
  sentence drawn. The DOM ships with the fallback sentence
  ("THE LAMPS WERE LIT FOR YOU") and zero glyphs; JS amends
  both from the live count (§6.9's map / DOM).
- **Motion spec.** Entry: the footer's first pool (§6.8) is
  already lit from the pin's release; the totals' figures step
  to truth on entry (no count-up — the day is over; its figures
  are read, not performed). The lamp glyphs kindle in sequence,
  120ms apart `--ease-lamp`, as the colophon centres — the
  visitor's own lamps, lit again in miniature at the day's
  close. Nothing else moves in the footer, ever.
- **States.** Unread (below) → closing (centred: totals true,
  glyphs kindled) → closed (rest). Hover on links: warm to
  `--lamp`. Focus: lamp outline.
- **Content merge.** The colophon's numbers are the day's own:
  book totals from §6.16's object, lamp count from §6.9's real
  acts, the final hour from §5's function at t=1. It is a
  summary of facts the page has already established — the one
  place the theme permits itself a summary, because a day may
  be summed at its end.
- **Failure fallback.** No JS: fallback sentence, book totals
  printed from the record object, hour printed "19:40". The
  footer is complete without a single lit lamp.
- **Reduced-motion variant.** Glyphs printed lit; sentence and
  totals identical.
- **Performance budget & mobile variant.** Static; glyph
  kindling is ≤ the lamp count of opacity ramps. Mobile:
  totals wrap 2×2, glyphs keep (they are the record).
- **Choreography timeline (v2).** Pin releases (§6.8) → footer
  enters lamplit → centre: totals step, glyphs kindle 120ms
  apart → the closing sentence read → rest. The page ends
  standing in lamplight.
- **State matrix (v2).** *Rest:* closed. *Hover:* links warm.
  *Focus:* lamp outline. *Active:* n/a. *Scrolled-past:* n/a —
  there is nothing past the day. *Disabled:* n/a. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: totals in one row. 768–1199px:
  one row, tighter. <768px: 2×2, glyphs above the sentence.
- **Edge cases & failure modes (v2).** *Zero lamps lit:* the
  sentence takes its honest zero form — "You lit no lamps;
  the pools were lit for you." — and no glyphs appear. A
  colophon that claims a lamp nobody lit fails §10 outright.
  *Many lamps (>12):* glyphs cap at 12 with "+ n MORE" in
  apparatus; the sentence's count stays exact.
- **Accessibility spec (v2).** Footer landmark; totals are text
  with labels; glyphs are `aria-hidden` (the sentence carries
  the count). Contrast: lime on dusk-deep 13.45:1, lamp figures
  10.42:1 (§2).
- **Tokens consumed (v2).** `--dusk-deep`, `--dusk`, `--lamp`,
  `--lime`, `--bleached`, `--ease-lamp`.

### 6.18 The shuttered page (page family: 404 / empty state)

- **What & why.** The missing page is a house shuttered for the
  siesta: a lime wall, its shutters closed (olive, the theme's
  one green, used as an object at last), the sundial printed
  still at 15:00, and the book's plain statement that this room
  is not on the street — with the street's real directions back
  to the courses, the day book and the terrace. It belongs
  because even the theme's absence keeps the day's manners: a
  missing page is not an error void, it is a closed house at
  the quiet hour, and its stillness is specified, not defaulted.
- **Structure.** A single wall section: shutter pair (two olive
  panels, closed, with the house number in Marcellus), the
  statement ("THIS HOUSE IS SHUTTERED — THE PAGE YOU ASKED FOR
  IS NOT ON THIS STREET"), the still dial (SVG, wedge printed
  at the siesta angle, reading "15:00 — SIESTA, AT REST"), and
  three direction links lettered as wall signs. Search results'
  empty state reuses the wall at section scale ("NO TILES UNDER
  THIS RIDGE — THE COURSE IS EMPTY") with the nearest courses
  linked.
- **Motion spec.** None, declared: the shuttered page's
  choreography is stillness. The dial does not sweep (there is
  no day to keep on a page that is not on the street — its
  `t` is fixed at the siesta, 0.55, and printed as such). One
  licensed exception: the shutters' slat shadows stand at the
  siesta vector from §5's function at t=0.55 — computed, not
  decorative.
- **States.** Shuttered (only state). Hover/focus on the
  direction links: fired warmth / outline, per §11.
- **Content merge.** The directions are the site's real sections;
  the house number is the requested path lettered in apparatus
  beneath the statement ("/tiles/batch-999 — NOT A COURSE WE
  LAY") — the 404 names what was asked for, like a book that
  records a request it cannot fill.
- **Failure fallback.** The page *is* the fallback; it must
  render with no JS and no images (shutters are CSS/SVG).
- **Reduced-motion variant.** Identical (there is nothing to
  reduce — the ruling is the point).
- **Performance budget & mobile variant.** ≤30KB, no loop runs
  (the shared loop is not started; the siesta vector is a
  static property set). Mobile: shutters narrow, dial 72px,
  directions stack.
- **Choreography timeline (v2).** None — declared stillness.
  The absence of a timeline is this element's timeline, and
  the gate (§10) checks that no animation is registered on
  the page.
- **State matrix (v2).** *Rest:* shuttered. *Hover:* link
  warmth only. *Focus:* fired outline. *Active:* navigation.
  *Scrolled-past:* n/a. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full wall + dial 132px.
  768–1199px: dial 110px. <768px: dial 72px, shutters at 60%
  width.
- **Edge cases & failure modes (v2).** *Soft 404 (empty
  search):* the section-scale variant keeps the page's own
  day running around it — only the empty course is shuttered,
  not the street. *Server error (500):* the same wall, the
  statement in the book's voice ("THE KILN HAS CRACKED — THE
  YARD KNOWS; TRY THE STREET AGAIN SHORTLY") — one wall for
  every absence, worded per cause.
- **Accessibility spec (v2).** The statement is the `<h1>`;
  the dial is `aria-hidden` with its reading in the statement's
  apparatus line as text. Directions are a real list of links.
  HTTP status is correct (404/500) — the theme never soft-404s.
- **Tokens consumed (v2).** `--lime`, `--olive`, `--ink`,
  `--fired`, `--shadow-ink`.

## 7. Page application map

**Home — the full day.** Noon hero (§6.11) with the stamp
(§6.1) and sundial (§6.3); the courses (§6.12) laid by §6.4;
a craft wall (the firing, told under its ridge, §6.5); the day
figures (§6.14); the day book (§6.16); the lamplight finale
(§6.8) holding the closing claim and the order form (§6.13) in
its pools; the colophon (§6.17). The home page is the only page
that runs the complete 12:00 → 19:40 arc and the only one with
the pin — the full day is the home page's privilege.

**Listing — one street of courses.** A category page is courses
all the way: its own head apparatus stating the street's count
and clay ("TWELVE TILES — COPPO, FIRED IN BATCHES 209–214"),
§6.4 laying each course as it arrives, §6.7 shading on hover.
Filters, if the catalogue honestly needs them, are shutter
toggles on the street's head (§11) — never a sidebar of facets,
which is a warehouse's furniture on a roof. The listing's day
runs shorter: its `t` spans its own scroll, and its finale is a
single lamplit wall with the order form — no pin (the pin is
home-only, §5).

**Detail — one tile, at its record.** The tile at full size:
its face in the ridge frame at the day's current light, its
name and full firing record, its day-book
row excerpted from §6.16, its price, and the order form
(§6.13) pre-set to the tile and its batch. Its neighbours in
the course close the page ("ALSO IN THIS COURSE"). A detail
page's hero is a single wall at its declared hour — tile pages
open at afternoon (t starts at 0.2, printed in the sundial chip:
a visitor arriving at a tile arrives mid-day, the yard already
working) — the one licensed exception to a noon start, declared
here so no builder improvises another.

**About — the yard itself.** The makers and the method under
their ridges: who throws, who fires, how a batch is judged, the
kiln's biography (a real kiln is rebuilt brick by brick across
years, and its age is a figure §6.14 may print with its
source). This is where §1's law is stated in long form — the
about page is the theme's ethics, placed where a committed
visitor digs for it. Its day runs noon to golden hour only;
the yard's own page does not perform the evening it sells.

**Contact / order — the form's own page.** §6.13 alone on a
lime wall, reached from anywhere; a direct arrival lands at
noon (the form at its plainest), while arrival from the home
finale keeps the lamplight appearance (§6.8's pools printed
lit) — the form remembers the hour it was decided at, and
says so in its head line ("DECIDED AT DUSK") when it does.

**The shuttered page (404).** §6.18, everywhere, unchanged.

**Interior pages and the sundial.** Only the home hero carries
the full dial (§6.3); every interior page carries §6.10's chip
from its first screen — the instrument is placed once, then
reported. Interior heroes are a single wall with the page's
title under a ridge: the street's houses have one roofline
each.

## 8. Worked examples

### 8.1 The hero — a wall at noon

*The commission: "Casa Tegola", a family terracotta works
selling roof tiles and terrace ware; the home page runs hero →
courses → the firing → figures → day book → finale (claim +
order form in the pools) → colophon. Declared survey: courses
of coppo and canale tiles, batches 209–215, the kiln's ninth
year.*

- **The composition (§6.11).** First screen: lime wall, the
  headline upper-left — "Tiles that keep the noon off." —
  standfirst beneath ("Coppo and canale, fired in our own kiln
  since the yard's ninth year…"), the actions "SEE THE COURSES"
  and "THE DAY BOOK", the sundial (§6.3) in the top-right
  corner, and along the foot the first course: three tile cards
  (§6.12) half-laid.
- **The ceremony (§6.1, §6.3, §6.4).** Fonts ready at t≈120ms:
  the headline stamps (240ms, shadow struck at 2px), the
  dial's hour lines draw outward from noon (900ms), the foot
  course lays at t=200–800. By one second the wall stands
  complete in flat noon light — and its shadows have already
  begun, almost imperceptibly, to lengthen. A visitor who
  never scrolls has still received the contract: a wall, a
  sun, a dial, a product — and time already passing over all
  four.
- **Scroll timeline.** 0–120px: the ridge cap parallaxes at
  0.92× against the wall; the dial hands its reading to the
  nav chip (§6.10) as the hero's top leaves. The first section's
  ridge crosses 82%: §6.5 opens the first room, and the day —
  and the reading — begins in earnest.

### 8.2 Mid-page — the courses at siesta

*The same page, mid-descent: the course grid (§6.12) and the
day figures (§6.14), straddling the siesta band (t 0.45–0.65).*

- **Entry.** The grid's head apparatus: "TWELVE TILES — COPPO
  AND CANALE, BATCHES 209–214". The first courses laid on
  arrival in the afternoon band (§6.4); the visitor shades a
  canale with their hover (§6.7) — the cloud crosses, the clay
  cools — and reads its record: "BATCH 211 — FIRED 6 DAYS —
  340 IN THE YARD."
- **The siesta beat.** Scrolling into the figures band, the
  page's own gauges slow: the loop's lerp drops to 0.07 (§5),
  the shadows' lengthening becomes a creep, the shimmer —
  already thin — settles to still air at t=0.55 (§6.6). The
  figures band itself is the emptiest wall on the page: four
  figures, long measure, nothing else moving. Temperature
  stands at its 36° peak, printed, checkable against §5's
  formula and the dial's 15:27.
- **What the visitor feels.** The page has slowed down *with*
  them, at the hour when the yard itself stops. Nothing asked
  for attention; the stillness is the content of the hour, and
  the figures gain authority from being read in it.

### 8.3 Conversion — the order, pressed at dusk

*The same page's end: the order form (§6.13) inside the
finale's second pool (§6.8), reached after the day book
(§6.16). The visitor shaded three tiles and read two batches
on the way down.*

- **Arrival.** The pin has gathered the finale; the form sits
  in its pool, lit. Its head line: "THE TERRACE ORDER — BY THE
  TILE AND THE FIRING." The tile seam list shows the catalogue
  with Batch 214 struck through and its reason printed
  ("LAID OUT — NEXT FIRING THE WEEK OF THE 21ST"); the visitor
  chooses Batch 215's coppo.
- **The reckoning.** They enter 42 m²: the reckoning line
  steps — "726 TILES — 672 TO LAY, 54 FOR BREAKAGE — BATCH
  215, FIRED IN THE WEEK OF THE 14TH" — 42 × 16 = 672, +8%
  breakage rounded up = 54, total 726, the arithmetic printed on the form for
  checking. They mistype the direction (no @): on blur the
  rule holds fired and the book notes beneath, in Alegreya:
  "That direction will not carry — check the address before
  we press it into the book." (§12's error voice: a fact about
  addresses, not a scolding.) They correct it; the note
  clears. They press PRESS THE ORDER: the button stamps down,
  and the form becomes the pressed slip — "ORDER No. 88 —
  726 TILES OF BATCH 215 — ENTERED IN THE DAY BOOK" — while
  the colophon below (§6.17) will close the day with their
  lamp count added to the yard's totals.
- **Failure rehearsed.** If the post fails, nothing they
  wrote is cleared; the note above the form reads "NOT
  PRESSED — THE YARD COULD NOT BE REACHED. YOUR WORDS ARE
  KEPT ABOVE." and the reckoning keeps their figures. A
  visitor who spent a whole day on the roof to reach this
  form is never sent back to noon by a network blink (§10,
  blocking gate 7).

## 9. Anti-slop — what makes THIS theme look cheap

1. **The travel-poster page.** Stock terracotta textures,
   lavender sprigs, "Mediterranean vibes" copy over ordinary
   web content. *Cure:* §1's law and §6.16 — the clay is the
   product with a batch record, or the theme is not in use.
2. **Five clocks.** Card shadows at one angle, headline shadow
   at another, a decorative sun icon spinning on its own
   schedule. *Cure:* §5's single `--sx`/`--sy` and the gate's
   shadow audit — one sun, mechanically enforced.
3. **Violet creep.** Dusk violet promoted into buttons, links
   and mid-page bands because it "looks premium". *Cure:* §2's
   band law — the violet exists below t=0.85 only; a violet
   button at noon fails the gate on sight.
4. **The fade-up grid.** Cards fading in one by one with a
   generic stagger. *Cure:* §6.4 — courses lay by the row, with
   the shadow snap; the crew's rhythm, not the library default.
5. **Hover lift.** Cards rising toward the visitor with a
   drop-shadow bloom. *Cure:* §6.7 — attention shades a tile;
   nothing on a roof lifts.
6. **Rectangle photographs.** Product shots pasted as clean
   rectangles onto tile cards. *Cure:* §6.12 — photographs are
   clipped to the tile's curve or not shown.
7. **Invented figures.** "10,000 happy roofs", a temperature
   typed as decoration, a sundial that doesn't agree with the
   shadows. *Cure:* §6.14's source lines and §10's
   three-printings audit — every figure from `dayTime` or the
   book, or not printed.
8. **Perpetual shimmer.** Heat distortion running the whole
   page, all day, because it looked good in the hero. *Cure:*
   §6.6 — the shimmer dies at the siesta and never returns;
   an effect that cannot end cannot tell time.
9. **The bouncing stamp.** A hero headline arriving with
   spring/overshoot easing. *Cure:* §5's `--ease-stamp` —
   fired clay does not bounce; the press falls and stops.
10. **Lamps everywhere.** Warm glows sprinkled up the page as
    ambience. *Cure:* §6.8/§6.9 — lamplight exists in the dusk
    band, in pools, around content, lit by acts; a glow at
    noon is a gate failure.
11. **A progress bar.** Any linear bar, however styled, doing
    the sundial's job. *Cure:* §6.3 — progress is a dial and a
    printed reading; the bar is refused in §11.
12. **Siesta deleted.** One lerp for the whole page because
    variable smoothing "felt inconsistent". *Cure:* §5's
    siesta rule — the slowdown *is* the consistency; the page
    keeps the yard's hours.

## 10. Quality gate

**Blocking (any failure stops the build):**

1. **One-sun audit.** Sampled at t = 0, 0.25, 0.5, 0.75, 1:
   every cast shadow on the page reads the shared `--sx`/`--sy`
   for that `t`; the sundial's wedge angle equals 115·t; the
   printed reading equals `clock(t)`; the temperature equals
   §5's formula (rounded as §6.14 declares). Any disagreement,
   anywhere, fails.
2. **Three-printings agreement.** A tile's batch, firing and
   stock agree across its card (§6.12), its detail page (§7)
   and its day-book row (§6.16) at every point in a scripted
   session, including after a §6.13 order adds its row.
3. **Band law.** No `--dusk`, `--dusk-deep` or `--lamp` pixel
   renders above the dusk band (t<0.85) on any page; no
   `--terra` surface carries text; olive is read only as
   `--olive-deep`. Grep + visual audit.
4. **No stranded content.** With JS disabled, the whole page
   reads at noon rest: headline lettered, dial at 12:00,
   courses laid, figures printed, form working, footer in its
   fallback wording. With JS on and the loop killed, every
   watchdog (§6.2's 1200ms, §6.4's 1400ms, §6.5's 1600ms)
   fires and settles its surface.
5. **Lamp honesty.** In a scripted session with a known number
   of lamp clicks, the colophon's sentence and glyph count
   (§6.17) equal the clicks exactly; with zero clicks, the
   honest zero wording prints and no glyph appears.
6. **Shade clearance.** §6.7's shade never covers a card's wall
   strip at any breakpoint — checked with the catalogue's
   longest real names at their longest.
7. **Form-keeping.** A failed submit (simulated network error)
   leaves every field, the chosen tile and week, and the
   reckoning exactly as the visitor left them, with §12's
   failure note. Any build that clears the form on error fails.
8. **Reckoning audit.** The form's arithmetic (§6.13) is
   recomputed by hand for three areas (including 0 and an
   absurd value) and matches the printed formula — 16 per m²,
   +8% breakage, rounded up — exactly.

**Standard (must pass, fixable in review):**

9. Density falls with the day (§4): noon full, siesta emptiest,
   dusk closest. Exactly one pin (§6.8); ambient loops exactly
   two and never coexisting (§6.6, §6.8).
10. §5's refusal list honoured: no marquee, no blur reveals
    outside the shimmer, no kinetic type, no parallax beyond
    the ridge/wall pairs and the hero corner.
11. The siesta lerp (0.07) is measurably in force between
    t=0.45 and t=0.65 — instrument the loop and read it; a
    flattened lerp fails here even if it passed review.
12. The stamp runs once per session; a returning visitor's hero
    paints at rest, and §6.1's apparatus line is present under
    reduced motion.
13. Every interactive element is ≥44px; focus shows §11's ring;
    focus never triggers a shade pass or a lamp on its own
    (the lamp button is the keyboard's path, §6.9).
14. Mobile: shimmer cut (§6.6), pin 120vh (§6.8), dial 96px
    (§6.3), reckoning strip sticky (§6.13).

## 11. Component inventory

Every component a real Sun-Fired Clay site needs, with its
themed treatment. Components the theme refuses are listed with
their in-theme replacement — a refusal without a replacement
is a gap, not a stance.

| Component | Themed treatment |
|---|---|
| Primary button | Stamp press: the ground's locked pairing, 2px fired rule beneath the label; presses 2px on `--ease-stamp`. On lime, fired ground with lime label; in the dusk band, lamp ground with dusk label. |
| Secondary button | Wall-lettered link-button: transparent, 2px bottom rule in the ground's text colour; hover shades the rule's tile (§6.7's grammar at line scale). |
| Lamp button | §6.9's control: apparatus label "LIGHT THE LAMP", `aria-pressed`, lamp-dot indicator. A component in its own right — no other button may imitate its dot. |
| Text input | Inscription line (§6.13): apparatus label above, 2px rule below, no box; focus inks the rule fired. |
| Textarea | Ruled wall: lines every 29.6px (the body line unit ×1.75), Alegreya 17px. |
| Select | Refused. Choices are seam lists: ruled radio lines (§6.13's tile and week lists generalised) — a yard lays its tiles out; it does not hide them in a dropdown. |
| Checkbox | Tile tick: an unfired square outline in fired; filled = a small terracotta square, stamped. |
| Radio | Seam line (§6.13): the chosen line's left edge stamps a fired bar; the dot is a gnomon tick. |
| Toggle / switch | Refused. The yard has shutters, not switches; use two seam lines (Shutters open / Shutters closed) as radios. |
| Card | Tile card (§6.12): curved face, batch apparatus, wall strip with name/record/price. |
| Table | The day book (§6.16): ruled ledger rows, scoped headers, italic marginal notes. |
| Badge / chip | The sundial chip (§6.10) is the only chip admitted: dusk ground, apparatus reading. Stock and batch facts ride in card apparatus, never as floating badges. |
| Alert | A book note: lime-deep wall strip, fired left bar, §12's voice ("NOT PRESSED — …"). Never a coloured toast; the yard writes its warnings in the book. |
| Toast | Refused. Confirmations are pressed slips (§6.13) and book rows (§6.16) — records, not ephemera. |
| Modal | Refused. A dialogue is a shuttered room (§6.18's wall at overlay scale): full-wall panel under a ridge, opened by a ridge pass (§6.15). |
| Tabs | Course tabs: ridge-capped strips; the current course's ridge is fired, others lime-deep; panels are walls beneath. |
| Accordion | Shutters: each item a shutter pair that opens downward on `--ease-lay`; only one pair open per wall (the siesta rule — a wall rests between openings, 120ms). |
| Pagination | Course steps: "COURSE 2 OF 5" in apparatus with ridge links; never numbered page pills. |
| Progress bar | Refused. Progress is the sundial (§6.3) and its chip (§6.10). |
| Spinner | Refused. Loading is the lime-wash (§6.15); waiting figures print "STILL IN THE KILN". |
| Tooltip | Refused. Instruments explain themselves in apparatus lines on the wall (§6.14's source lines); nothing hides behind a hover. |
| Breadcrumbs | The street line: "THE STREET / THE COURSES / BATCH 215" in apparatus, fired separators as ridge ticks. |
| Search | A wall opening: full-width inscription line under the nav ridge; results are courses (§6.12) with §6.18's empty wall when none. |
| Price / figure display | §6.14's grammar: tabular figure + source line, always. |
| Footer | The lamplight colophon (§6.17). |
| 404 / empty | The shuttered wall (§6.18). |

## 12. Content & copywriting voice

Two registers, and the page never mixes them inside one block.

**The Roofer** — the working voice: headlines, section titles,
actions. Short, declarative, present tense, addressed to the
work: the tile, the hour, the hand. Sentence case in Marcellus;
never more than nine words a headline.

- ✓ "Tiles that keep the noon off."
- ✓ "Laid course by course."
- ✗ "Discover our stunning range of premium roofing solutions!"
- ✗ "Handcrafted Mediterranean elegance for your dream home."

**The Day Book** — the record voice: captions, apparatus, errors,
the colophon. Facts with their sources, past tense for what is
done, no adjectives that cannot be checked against the book.

- ✓ "BATCH 211 — FIRED 6 DAYS — 340 IN THE YARD."
- ✓ "Order No. 88 — entered in the day book."
- ✗ "Tons of tiles in stock now!"
- ✗ "Oops! Something went wrong."

**Error voice** (the Book, speaking plainly): an error is a fact
about the world, stated once, with the remedy in the same breath
— never a scolding, never a joke at the visitor's expense.

- ✓ "That direction will not carry — check the address before
  we press it into the book."
- ✓ "NOT PRESSED — THE YARD COULD NOT BE REACHED. YOUR WORDS
  ARE KEPT ABOVE."
- ✗ "Invalid email!!"
- ✗ "Uh oh — our bad!"

**Empty-state voice:** the shuttered house (§6.18): "THIS HOUSE
IS SHUTTERED — THE PAGE YOU ASKED FOR IS NOT ON THIS STREET."
Absence is stated as a fact of the street, with directions.

**Fixed strings (verbatim, do not paraphrase):** the reckoning
formula line "16 TILES TO THE SQUARE METRE — 8 IN EVERY 100
MORE FOR BREAKAGE"; the stamp's apparatus "SET UP AT NOON —
THE SHADOW KEEPS THE DAY."; the colophon's hour "19:40 — THE
DAY IS DONE"; the zero-lamp sentence "You lit no lamps; the
pools were lit for you."

**Banned words:** "vibes", "stunning", "premium", "solutions",
"dream home", "oops", exclamation marks in the Book's register
(the Roofer may use one per page, in a headline only — the yard
is not excitable). **Owned words:** course, batch, fired, laid,
shade, the hours by name (noon, siesta, golden hour, dusk),
"by the sun", "in the book".

**Numbers:** always tabular, always sourced (§3, law 4);
times in 24-hour apparatus ("15:27"); temperatures whole
degrees with the degree mark and no space ("36°").

## 13. Full-page scroll choreography map

The home day, top to bottom. Every beat in order; instruments
run continuously beneath the beats (shadows §6.2 lengthening,
sundial §6.3 sweeping, chip §6.10 reporting).

| Beat | Scroll zone | What happens | What the visitor feels |
|---|---|---|---|
| 1 | Load | The stamp (§6.1), dial lines draw (§6.3), foot course lays (§6.4) | Noon, struck |
| 2 | 0–120px | Ridge/wall parallax separates; dial hands over to the chip (§6.10) | The roof lifts; the day starts |
| 3 | First ridge | First section opens from under its ridge (§6.5) | A room, uncovered |
| 4 | Courses in view | Rows lay (§6.4); shade and sheen live (§6.7, §6.12) | The stock, inspected |
| 5 | Afternoon | Warmth overlay rises (§5); shimmer thins (§6.6) | The day warming |
| 6 | Siesta band | Lerp drops to 0.07; shimmer dies at t=0.55; figures stand in the emptiest wall (§6.14) | The yard at rest |
| 7 | Day book | Head rule draws; the record stands (§6.16) | The workings, shown |
| 8 | Golden hour | Longest shadows; warmth falling; finale's ground begins to deepen | Evening approaching |
| 9 | Dusk band | Pin engages; pools gather block by block (§6.8) | Gathering at the lamps |
| 10 | Finale | The claim read by lamplight; the form reckons and presses (§6.13); lamps light at the visitor's hand (§6.9) | The ask, at dusk, by lamplight |
| 11 | Colophon | Totals step to truth; the visitor's lamp glyphs kindle (§6.17) | The day, closed |

**Reverse pass.** Scrolling up: scrubbed values retrace exactly
(shadows shorten, the dial rewinds, warmth falls and rises on
its curve) — with two declared exceptions that do not rewind:
the air does not reheat (§6.6's shimmer stays dead once the
siesta has passed) and lamps stay lit (§6.9). The page going up
is the same day remembered, not the same day relived: the light
reverses, the acts persist. §6.6 and §6.9 state it in their own
sections so no builder harmonises it away.

**Jump-scroll catch-up.** Anchor jumps and flings: sections
passed stand open (§6.5), courses passed stand laid (§6.4),
the sundial and shadows land on the true `t` within the lerp's
catch-up (~600ms across a full-day leap), pools print at the
landing position's state (§6.8). No ceremony is owed to a
teleport; the instruments simply tell the landing hour's truth.

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Total page weight (home) | ≤ 720KB, of which images ≤ 380KB |
| Fonts | Marcellus (1 weight) + Alegreya (3 weights) ≤ 120KB, `font-display: swap` |
| JS | ≤ 65KB gzipped (one loop, two observers, lamp map, form reckoning) |
| Shared-loop cost | ≤ 1.6ms/frame average; writes only transform / opacity / custom properties |
| Long tasks | None > 50ms after load; the stamp and dial draw are timer-sliced |
| Shadow repaint | Vector quantised to 0.5px steps on <768px (§6.2); blur capped 6px / 4px mobile |
| Active pool ramps | ≤ 3 concurrent (§6.8); lamp glows opacity-only after kindling |
| Shimmer | ≤ 0.5ms/frame, desktop ≥768px only (§6.6) |

**Cut order when the budget is exceeded** (cut in this order,
record each cut in the build notes):

1. Heat shimmer (§6.6) — stilled entirely; the day is told by
   shadows and figures.
2. Dust motes (§6.8) — pools stay, the air in them stills.
3. Ridge/wall parallax (§5) — ridges scroll with their walls.
4. The ridge-pass transition (§6.15) — navigation becomes
   instant with a chip flash (§6.10).
5. Cloud-shade travel (§6.7) — shade applies at rest position
   (the reduced-motion treatment) for all visitors.
6. Pool gathering (§6.8) — pools print lit as blocks centre;
   the pin and the dusk stay.

**Never cut:** the one-sun watchdogs, the locked pairings, the
sundial and its reading, the day book, the reckoning's
arithmetic, the colophon's true lamp count, any reduced-motion
variant. A build that cuts the honesty to keep the ambience
has painted the wall and called it a day.

## 15. Build-order checklist

1. Survey first: fix the sections and their ridges, each
   section's band membership (where the shimmer lives, §6.6),
   the catalogue with real batches/firings/stock, the day
   book's data object, and the form's real firing weeks.
   Write the survey; everything else is generated from it.
2. Build the static noon: all sections open under their
   ridges, courses laid, figures printed, dial at 12:00, form
   working, footer in fallback wording — with no JS. This is
   the site; the rest is the day passing over it.
3. Set the palette tokens and the pairing law (§2); audit
   contrast on every ground, including dusk, before any
   motion exists.
4. Set the type scale (§3) and the five type laws; verify the
   headline fits its wall in two lines at every breakpoint.
5. Build the course grid and ridge geometry (§4): the module,
   the arc pattern drawn once, the sundial's corner.
6. Implement `dayTime(t)` (§5) as the single source: clock,
   shadow vector, temperature, light remaining, warmth —
   unit-tested against §5's printed values at t = 0, 0.45,
   0.5, 1 before any element consumes it.
7. Build the instruments from the survey's object: sundial
   (§6.3), day figures (§6.14), day book (§6.16), colophon
   (§6.17) with fallback wording. Verify the three-printings
   agreement by reading all of them against the object.
8. Add the shared loop; wire shadows (§6.2) and the dial's
   wedge to the same lerped `t`; verify the one-sun audit
   (§10, gate 1) at the five sample points.
9. Add the entrances: stamp (§6.1), dial draw (§6.3),
   roof-laying (§6.4), ridge reveals (§6.5) — each with its
   watchdog and its focus rule.
10. Add the weather: shimmer (§6.6) with its band gating and
    live cut, cloud shade (§6.7) with strip clearance checked
    against the longest real names.
11. Add the evening: finale pin and pools (§6.8), lamp click
    (§6.9) writing to the one session map, colophon kindling
    (§6.17) reading the same map.
12. Build the order form (§6.13) with its reckoning from the
    printed formula and error-keeping rehearsed against a
    simulated network failure.
13. Add the skeleton and ridge pass (§6.15), the shuttered
    page (§6.18) with its no-animation audit.
14. Run the full gate (§10), including the lamp-honesty
    scripted session and the one-sun sampling; sign-off by a
    non-builder — the roofer who judges the day is never the
    hand that laid the roof.
