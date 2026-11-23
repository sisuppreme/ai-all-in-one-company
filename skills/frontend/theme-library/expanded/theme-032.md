# 32. Tidal Ledger — Expanded (v1 + v2)

*Expansion written to `EXPANSION-STANDARD.md` v1 + the v2 deepening pass
(50x standard), ordered 2026-11-23. This file is the complete, buildable
specification of theme #32. The original library entry's identity is
preserved exactly — the harbourmaster's logbook whose whole page keeps
tidal time, the five palette anchors (Chart paper `#F4EFE4`, deep
harbour green `#1E3A3A`, sea glass `#5E7A6B`, brass `#B98A44`, buoy
orange `#D96C4A` used once), Libre Caslon Text display with Source
Serif 4 prose and IBM Plex Mono data, the ruled-ledger layout with the
continuous tide curve in the left margin rail, and all nine original
signature elements — deepened, never redesigned. Where this file and
the short library entry disagree, this file governs.*

**The one law of the theme, stated before everything else:** the page
never invents a tide. Every height, every time, every weight on the
page is either printed in the page's own tide table (§6.13) or computed
from that table by the one declared interpolation — the rule of
twelfths (§5) — and the margin curve, the section stamps, the pinned
hours and the counters are four printings of that single record, so
they can never disagree. A harbourmaster's log is evidence: a figure
written in it was observed, or it was not written. A site in this theme
that animates a plausible-looking 4.7 m it never sourced has not made a
rounding error; it has forged a log entry, and the quality gate (§10)
treats it as one. The second law follows from the first: **the buoy
orange appears exactly once** — on the single booking button (§6.9).
It is the harbour's one buoy. A second orange element anywhere on the
page is a second buoy in a one-buoy harbour, and the gate counts it.

---

## 1. Concept & world

A harbour runs on two clocks: the wall clock on the harbour office and
the tide clock in the water. Ferries sail on the second one, fishermen
launch on it, the harbour bar silts and clears on it, and the
harbourmaster writes both into the same ruled book — arrivals against
the hour, depths against the tide — because in his world an event is
not fully recorded until you know the state of the water when it
happened. The Tidal Ledger takes that book as the interface. The page
is a day's page from the log: a continuous tide curve runs down the
left margin from the first entry to the last, every section is an entry
written at its tide, images sit in brass-rimmed portholes the way the
office's photographs hang in brass frames, and the day closes with the
two tables the harbour actually works by — the tide table and the
harbour hours — printed as the closing ledger page.

The emotional register is *kept time*. Nothing on the page hurries: the
flood takes 900ms because water rising over a page of entries should
feel like water, the bob is a slow sine because moored things move
slowly, and the only fast motions are the harbourmaster's own hand —
the 180ms seal press, the 200ms stamp. The visitor should feel that
the site has a working day, a state of water, and a book that will
still be correct tomorrow.

**Best fits.** Businesses and places whose real rhythm is tidal,
seasonal or scheduled against a natural cycle: ferry and boat-trip
operators, harbour and marina services, seafood restaurants and fish
markets publishing the day's catch, coastal hotels and tide-dependent
attractions (causeways, tidal pools, island visits), sailing schools,
lifeboat and harbour charities, working-port museums. The theme earns
its keep wherever the honest answer to "when?" is "it depends on the
tide" — the site's own content then supplies the real table the law
requires.

**Audiences.** Visitors planning around a schedule they cannot move —
they read the page the way they would read the log: top to bottom, in
order, trusting the figures. The design repays that trust literally:
the stamp on the section they are reading is computed from the same
table printed at the foot of the page (§6.5, §6.13).

**When NOT to use it.** (1) Any site that cannot supply a real,
dated tide table (or an equally real cyclic dataset — a mill's shift
tides, a market's opening cycle) for the curve to plot: without real
data the law cannot be kept and the theme is a costume. (2) Content
that must be scanned out of order — dense reference documentation,
comparison shopping — because the ledger's meaning is sequential; an
entry read before its tide is a line read out of the book. (3)
Anything urgent: an emergency notice must not wait 900ms for a flood.
(4) A page whose single conversion is not bookable in one action — the
buoy law (§6.9) allows exactly one orange button; a site needing three
competing CTAs cannot keep it.

**The world in one sentence.** It is 06:40, the harbourmaster has
ruled the day's page, the tide is making, and everything written below
happened at the height stamped beside it.

---

## 2. Palette

Five anchors, inherited exactly. Four are the harbour office — paper,
green-black water, sea glass, brass fittings — and the fifth is out in
the harbour, seen once.

| Token | Hex | Role | Usage ratio | Pairing / contrast (measured) |
|---|---|---|---|---|
| `--paper` | `#F4EFE4` | Chart paper: page ground, entry stock | ~62% | Ground for `--ink` (13.11:1) and `--harbour` (10.64:1) |
| `--harbour` | `#1E3A3A` | Deep harbour green: display type, rules' ink, footer ground | ~18% | On `--paper` 10.64:1 — text-grade at all sizes; `--paper` on it 10.64:1 |
| `--glass` | `#5E7A6B` | Sea glass: the tide curve's unfilled stroke, porthole glass sheen, secondary data | ~9% | On `--paper` 4.10:1 — **large text and graphics only, never body text**; text uses `--glass-deep` |
| `--brass` | `#B98A44` | Brass: curve fill, porthole rims, seals, stamps' rings, table rules | ~8% | On `--paper` 2.70:1 — **metal, never text**; the text-grade derivative is `--brass-deep` |
| `--buoy` | `#D96C4A` | Buoy orange: the booking button, once (§6.9) | ≤0.5% | Label in `--ink` 4.44:1 at ≥18px bold only; counted by the gate |

**Derived tokens (closed list — no others may be coined):**

| Token | Hex | Derivation / role | Contrast |
|---|---|---|---|
| `--ink` | `#152A2A` | Harbour green blackened: body text, mono data | 13.11:1 on `--paper` |
| `--paper-deep` | `#E9E0C9` | Paper in shadow: the waterline band, skeleton lines, footer-adjacent stock | `--ink` on it 11.44:1 |
| `--glass-deep` | `#3E5C4C` | Sea glass deepened to text grade: secondary text, table captions, the curve's axis labels | 6.45:1 on `--paper` |
| `--brass-deep` | `#856023` | Brass oxidised to text grade: stamp lettering, seal text, entry numbers | 4.96:1 on `--paper` |
| `--buoy-deep` | `#A34A2E` | Buoy orange in shade: the button's pressed state and its focus ring only — the button's face stays `--buoy` | `--paper` on it 5.12:1 |
| `--waterline` | `#5E7A6B` at 14% over `--paper` | The flood mask's visible surface band (§6.3) | n/a — a moving surface, never under text at rest |

**Pairing laws.** (1) Body text is `--ink` on `--paper`, nothing else.
(2) `--brass` and `--glass` are materials, not inks: they may draw,
rim, fill and rule, but any letterform a visitor must read is set in
`--ink`, `--harbour`, `--glass-deep` or `--brass-deep`. (3) `--buoy`
has exactly one rendered instance per page — the booking button —
enforced by counting `background: var(--buoy)` instances in the built
CSS/DOM at the gate (§10); hover and pressed states of that same button
may use `--buoy-deep`, because a buoy in shadow is still the same buoy.
(4) The tide curve is drawn in `--glass` and fills in `--brass`; the
two metals of the theme — water and fitting — never swap roles.

**Dark behaviour — "night watch", not inversion.** After dark the
harbour office works by lamplight over the same book: the page does not
invert. `--paper` deepens to `#22332F` (the green-black of the office
at night), `--ink` lifts to `#EDE6D2` (paper-coloured ink, as if the
entries were chalked), `--harbour` surfaces rise to `#2A4A44`,
`--glass` brightens to `#7E9C8B` for the curve, and `--brass` stays
`#B98A44` — brass is brass by lamplight. The buoy stays `--buoy`; a
buoy shows a light at night, it does not change colour. Ratios are
re-measured in the night scheme at the gate; the pairing laws are
unchanged. The scheme is selected by `prefers-color-scheme` only —
there is no toggle, because the logbook does not offer the reader a
choice of lighting.

---

## 3. Typography

Three families, three jobs, no fourth voice. **Libre Caslon Text** is
the harbourmaster's display hand — the hand the day's heading and the
entry titles are written in. **Source Serif 4** is prose: the entries
themselves, read at length. **IBM Plex Mono** is data: every height,
time, weight, price and count on the page, without exception, because
in a logbook a figure is a figure and is set like one.

| Role | Font | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Day heading (H1) | Libre Caslon Text 400 | 54px / 1.08 (≥1200), 42px tablet, 34px phone | −0.01em | The surfacing headline (§6.1); never bold — Caslon has no bold in the book |
| Entry title (H2) | Libre Caslon Text 400 | 32px / 1.15 | 0 | Carries its tide stamp (§6.5) at its right |
| Sub-entry (H3) | Source Serif 4 600 | 20px / 1.3 | 0 | Inside entries only |
| Prose | Source Serif 4 400 | 18px / 1.62 | 0 | Measure 62ch (§4); the reading voice |
| Data / figures | IBM Plex Mono 400/500 | 15px / 1.5, tabular | 0 | Heights `4.7 m`, times `14:20`, weights `212 kg` — always with unit |
| Apparatus (labels, stamps, index) | IBM Plex Mono 500 | 11.5px / 1.4, uppercase | 0.14em | Entry numbers, stamp lettering, table heads |
| Harbourmaster's hand | Libre Caslon Text italic | 17px / 1.45 | 0 | Stamps' second line, margin notes, error voice (§12) — a person, not a system |

**Type laws.** (1) **No figure out of mono.** A height, time or weight
set in Caslon or Source Serif is a build error the gate greps for: any
digit string followed by `m`, `kg`, `:` (in a time) or a currency mark
must resolve to the mono stack. (2) **Times always carry their tide.**
A sailing time is printed `14:20 · HW 4.7 m`, never bare — in this
book a time without the water's state is half a fact. (3) **Caslon is
never bold and never uppercase** except the day heading's port name,
which is set in Caslon small caps as it would be on the office door.
(4) **The stamp is two lines and two voices**: the fact in mono
(`HW 4.7 m · 14:20`), the harbourmaster's remark beneath in Caslon
italic (`— a fair tide for the crossing`). (5) Tabular figures
everywhere mono is used: `font-variant-numeric: tabular-nums` is set
once on the mono stack and never overridden, so columns of heights in
§6.13 align to the decimal point as ruled columns must.

---

## 4. Layout language

**The ruled page.** The page is one sheet of the log, ruled before it
is written. Three vertical territories run its full height: the
**margin rail** (96px at ≥1200px, 56px at 768–1199px, a 28px edge
strip under 768px) holding the tide curve (§6.2); the **entry column**
(max 680px, prose measure 62ch) holding the day's entries in order;
and the **data margin** (up to 240px at ≥1200px) holding stamps,
figures and porthole frames that belong to the entry beside them. On
tablet the data margin folds under its entry; on phone the entry is
single-column and the rail becomes the strip the curve flattens into.

**Rules and ruling.** Every entry is separated from the next by a
brass hairline (1px `--brass` at 55%) with the entry's number in the
margin (`No. 4 — HW 14:20`). The baseline rhythm is 9px: prose sits on
a 29.16px leading (18px × 1.62) and all vertical spacing is a multiple
of 9px, so the page feels ruled even where no rule is printed. Section
padding is 81px (9 × 9) desktop, 54px tablet, 36px phone — the book
breathes at the top of each entry and nowhere else.

**Density laws.** (1) One entry, one subject: an entry that needs a
second H2 is two entries and gets two tide stamps. (2) The data margin
may hold at most three objects per entry (a stamp, a figure block, a
porthole) — a margin fuller than that is a second column pretending.
(3) Portholes (§6.15) are rationed: at most one per entry, diameter
between 180px and 320px, always in the data margin or centred above
the entry on phone — never floated inside prose, because a photograph
in a logbook is pasted to the page, not poured into the text. (4)
Whitespace is the water between entries: it is left empty on purpose,
and no element may be placed in it to "use the space" — the tide curve
in the rail is the only permanent resident of the margins.

**Section choreography.** The day reads in tidal order, not marketing
order: opening of the log (hero, §6.11) → the day's entries in the
order their tides occur → the pinned harbour hours with the day's
tides scrolling beside them (§6.6) → the closing ledger (tide table,
§6.13) → the booking entry (form, §6.12) → the ledger closed (footer,
§6.14). A build that reorders conversion before the entries has torn
pages out of the book and re-bound them wrong.

---

## 5. Full motion system

Five named easings, each a physical thing in the harbour:

| Token | Curve | Used by |
|---|---|---|
| `--ease-swell` | `cubic-bezier(0.37, 0.00, 0.21, 1.00)` | Floods, the waterline's rise — water arriving, fast at first over the flat, slowing as it deepens |
| `--ease-bob` | `cubic-bezier(0.45, 0.05, 0.55, 0.95)` (≈ sine in-out) | Bob cycles, the buoy's drift — a moored thing's ease |
| `--ease-press` | `cubic-bezier(0.20, 0.90, 0.30, 1.00)` | Seal and stamp presses — the hand comes down fast and sure |
| `--ease-draw` | `cubic-bezier(0.60, 0.00, 0.30, 1.00)` | The tide line's draw, rules, the footer's closing line |
| `--ease-drift` | `cubic-bezier(0.25, 0.10, 0.25, 1.00)` | Parallax settle, wet-ink spread — slow weather |

**The shared loop.** All scroll-scrubbed values — the curve's brass
fill level, the bob phase, the three parallax depths, the pinned-hours
alignment, the buoy's position — are written by **one**
requestAnimationFrame loop with lerp **0.12** toward the true scroll
value. Nothing else in the theme owns a scroll handler. Time-based
loops (the curve's 11s undulation, the buoy's rest bob) run on the
same rAF clock but are suspended when their element is off-screen and
when the tab is hidden.

**The declared interpolation — rule of twelfths.** Between two
consecutive extrema in the printed table (say LW 1.1 m at 08:05 and
HW 4.7 m at 14:20), the height at each intervening hour is computed by
the rule of twelfths: the range (3.6 m) divides into twelfths
(0.3 m), distributed 1, 2, 3, 3, 2, 1 across the six hours of the rise.
The margin curve's path is plotted from these computed points; the
stamp for any scroll position reads the same interpolation at the
page-tide that position declares (§6.5). One function, `tideAt(t)`,
serves curve, stamps, pinned hours and counters; the gate tests it
against three hand-computed points (§10).

**Every motion term, in this theme's language:**

- *Scroll-triggered reveals* — the flood (§6.3): content rises through
  a waterline. Nothing fades in from nothing; things come up out of
  the water the page keeps.
- *Scroll-driven scrub* — the curve fill (§6.2), the bob (§6.4), the
  parallax: three depths — chart lines and rules at 0.96×, prose at
  1.0×, brass data and stamps at 1.04× — the book's layers sliding a
  hair against each other like pages in a loose binding.
- *Pinned scene* — the harbour hours (§6.6): the day's fixed hours pin
  while its moving tides scroll past them; the pin is the office wall,
  the scroll is the water.
- *Masked reveals* — the waterline mask is the theme's only mask.
  Line-by-line masked text reveals are refused: entries are written,
  not unveiled, and §6.3's flood already performs the entry's arrival.
- *Blur-to-sharp* — refused. Water does not defocus a logbook; a wet
  page blurs ink permanently, which is a defect in this world, not an
  effect.
- *Kinetic typography* — refused except the headline's single bob on
  surfacing (§6.1). Letters in a ledger do not perform; the one
  exception is cargo breaking the surface, once.
- *Marquee* — refused, permanently. A logbook has no sideways. The
  harbour's notices are pinned to the office board (the entry index,
  §6.10), not streamed past the reader.
- *Animated counters* — heights and catch weights count to their true
  values (§6.18), always from the table or the day's record, always
  landing exactly on the printed figure.
- *Progress indicator* — the margin curve filling brass (§6.2). No
  bar, no percentage, anywhere: progress in this book is a state of
  water, read off the curve as "the tide is at 3.9 m and making".
- *Ambient loops* — exactly two: the curve's undulation (§6.2) and the
  buoy's rest bob (§6.9). A third ambient loop is a gate failure — a
  harbour is quiet.
- *Page transitions* — the waterline sweep (§6.16): leaving a page,
  the water rises over it and falls on the next; the log's pages turn
  under water because the whole book is kept at the harbour.
- *Micro-interactions* — wet-ink hover (§6.7), seal press (§6.8), the
  buoy's tug (§6.9): attention, approval, and the one invitation.
- *Skeleton / loading* — unruled lines (§6.16): an entry not yet
  written shows its ruling and its entry number, never a spinner.

---

## 6. Signature elements

### 6.1 Headline surfacing

- **What & why.** The day heading does not appear; it *surfaces*. On
  load the tide line draws itself across the hero, and the headline
  rises up through it — clip-path waterline climbing over 1600ms —
  each letter bobbing once, out of phase, ±4px, as it breaks the
  surface, like cargo floated off a barge at the rise of tide. It is
  the theme's thesis in one gesture: on this page, things arrive by
  water, and the headline is the first thing the tide delivers.
- **Structure.** The hero holds an SVG tide line (the first 340px of
  the same curve geometry §6.2 plots, path drawn in `--glass` 2px)
  across the entry column at the headline's midline. The H1 sits in a
  wrapper with `clip-path: inset()` animated from `inset(100% 0 0 0)`
  — no: the waterline reveal works downward-to-up: the clip's *bottom*
  edge is fixed and the *top* inset animates from 100% to 0 as the
  "water" falls away — implemented as a rising reveal: the headline is
  clipped by a mask whose waterline edge (an SVG mask following the
  drawn curve, ±6px amplitude) climbs the headline's height over the
  duration. Letters are wrapped in spans (JS-only enhancement; the DOM
  text is whole) for the bob. Beneath the headline, the standfirst
  prints plainly — prose never surfaces; only the day's title rates
  the ceremony.
- **Motion spec.** t=0 (fonts ready or 300ms, whichever first): the
  tide line draws left→right, 700ms `--ease-draw`. t=500ms: the
  waterline begins its climb, 1600ms `--ease-swell`, from the
  headline's baseline to above its cap height. Each letter, as the
  waterline passes its x-position, bobs once: translateY 0 → −4px →
  +2px → 0 over 620ms `--ease-bob`, staggered 60ms per letter in
  reading order. At t≈2100ms the mask is removed entirely — the
  headline stands dry and un-clipped for the rest of the visit.
- **States.** *Rest (DOM default):* headline fully printed above the
  drawn line — this is the no-JS and post-animation state alike.
  *Surfacing:* as specced. *Revisit within session:* skipped
  (sessionStorage flag); the headline is simply there, because a
  harbourmaster does not re-float the same cargo twice a day.
  *Scrolled-past:* plain headline; the ceremony never replays on
  scroll-back.
- **Content merge.** The line the headline surfaces through is the
  head of the margin curve — the same plotted tide, continued across
  the hero. The headline's own words name the port and the day; the
  tide that floats them is the tide the page will report all day.
- **Failure fallback.** The clip and letter spans are JS-applied only.
  If fonts stall, the draw waits for the 300ms cap, not for the font.
  A 2400ms watchdog removes the mask unconditionally: a headline still
  underwater at 2.4s is a drowned headline, and the watchdog is the
  lifeboat. No-JS: headline and drawn line print statically.
- **Reduced-motion variant.** No draw, no climb, no bob. The tide line
  prints statically beneath the headline and the headline is simply
  read. The information — today's port, today's date — is identical.
- **Performance budget & mobile variant.** One SVG path draw + one
  mask animation + ≤ 34 letter transforms, all compositor-only; ≤
  0.5ms/frame. Mobile: the climb shortens to 1200ms and the bob to
  ±3px; letters beyond 26 are bobbed in word groups, not individually,
  to cap concurrent transforms at 26.

#### 6.1 v2 — Choreography timeline

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Fonts-ready (or 300ms cap): tide line begins drawing across the hero |
| 2 | t₀ + 500ms | Line drawn; waterline mask starts its climb at the headline's baseline |
| 3 | t₀ + 560ms + 60ms × n | Each letter bobs once as the waterline passes it (−4px → +2px → 0, 620ms) |
| 4 | t₀ + 2100ms | Waterline clears the cap height; mask removed; headline stands dry |
| 5 | t₀ + 2400ms | Watchdog deadline: any mask still present is stripped, unconditionally |

#### 6.1 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest (printed) | Headline dry above the drawn line | Same |
| Surfacing | Draw 700ms, climb 1600ms, letters bob ±4px | Climb 1200ms, bob ±3px, word-group stagger past 26 letters |
| Hover | None — the day's title is not a control | n/a |
| Focus | Headline contains no focusable element; a skip-link landing here shows the dry state instantly (mask removed) | Same |
| Scrolled-past | Dry, static | Same |
| Disabled / no-JS | Printed headline, static line | Same |

#### 6.1 v2 — Breakpoint behaviour

≥1200px: full spec, 54px Caslon, bob ±4px. 768–1199px: headline 42px,
climb 1400ms, bob ±3.5px. <768px: headline 34px, climb 1200ms, the
tide line draws at 480ms, and the letter bob applies per word (spans
wrap words, not letters) — a phone's hero must not spend its first
two seconds on ceremony.

#### 6.1 v2 — Edge cases & failure modes

*Very long port name (two-line headline):* the waterline climbs the
full two-line height (duration scales ×1.3); letters bob per line in
reading order. *Fonts fail entirely:* the draw proceeds at the 300ms
cap in the fallback serif; the ceremony is geometry, not typography.
*User scrolls during surfacing:* the climb continues (it is short) but
the bob is cancelled for letters not yet passed — cargo already
shipped does not bob for an empty dock. *Session revisit:* the flag
suppresses the whole sequence including the draw; the line prints.

#### 6.1 v2 — Accessibility spec

The headline is a plain `<h1>` with its full text; letter spans are
`aria-hidden` inside an `aria-label`led heading wrapper so screen
readers meet one title, not 34 letters. The surfacing is never the
only route to the text: DOM order and content are complete at first
paint. Contrast: Caslon `--harbour` on `--paper` 10.64:1, unaffected
by the mask at rest. The bob's ±4px never moves the headline's box —
layout is reserved, CLS 0.

#### 6.1 v2 — Tokens consumed

`--harbour`, `--glass`, `--ease-draw`, `--ease-swell`, `--ease-bob`,
`--dur-surface` (1600ms), `--dur-linedraw` (700ms), `--bob-hero` (4px).

### 6.2 Margin tide curve

- **What & why.** The theme's spine and its progress indicator in one
  object: a continuous SVG curve plotted down the left margin rail for
  the whole page height, undulating slowly, and filling with brass up
  to the reader's current tide height. It is simultaneously the chart
  of the day's water and the measure of the reader's progress through
  it — scroll down and you are later in the day, the tide higher or
  lower as the real table says, the brass fill standing at exactly the
  height the curve has reached *at your entry*. No other progress
  indicator is permitted on the page (§5), because a second one would
  be a second clock in a one-clock office.
- **Structure.** One inline SVG, viewBox width 96 (the rail), height
  equal to the page's entry column, `preserveAspectRatio="none"` on
  the vertical axis only via a path plotted in page coordinates. The
  path is generated at build time (or first paint) from the day's
  printed table (§6.13): extrema joined by rule-of-twelfths points
  (§5), smoothed with a monotone cubic so the curve can never loop or
  overshoot an extremum — a plotted tide that exceeds its own HW is a
  forged figure. Two strokes share the path: the full curve in
  `--glass` 2px (the chart), and a clipped copy in `--brass` 2.5px
  whose clip rect's height is the fill level, written by the shared
  loop. Hour ticks cross the rail at each hour's page position, with
  the hour in mono 10px at every third tick. HW and LW points carry a
  brass dot and their printed height (`4.7`) in mono.
- **Motion spec.** *Undulation:* the plotted path's control offsets
  breathe ±3px horizontally on an 11s sine, phase continuous — the
  chart is alive but the extrema never move: undulation amplitude is
  multiplied by the local slope factor so HW/LW points (slope 0) stay
  pinned to their true heights while the steep mid-tide water moves
  most, exactly as a real curve on a chart table shivers at its
  crossings, not at its marks. *Fill:* the reader's page-tide maps
  linearly to document progress; the brass clip height lerps (shared
  loop, 0.12) to the curve's y at that progress, and the current
  height is interpolated by `tideAt()` and printed in the rail head —
  `TIDE 3.9 m · MAKING` — updated at most every 200ms, textContent
  only when the value changes by ≥ 0.1 m.
- **States.** *Rest (top):* fill at the day's first printed height —
  the tide the log opens at. *Reading:* fill tracks progress both
  directions (scrolling up ebbs the fill — the reader is re-reading an
  earlier hour, and the curve honestly shows it). *Scrolled-past
  (bottom):* fill at the day's last height; the rail head reads
  `TIDE 2.3 m · EBBING` or the day's closing state. *Hover:* none.
  *No-JS:* the curve prints complete in `--glass` with a static brass
  fill to the *current real time's* height if the build can compute
  it, else to mean level; the rail head prints `MEAN LEVEL` — the
  original entry's reduced state, honest about what it is.
- **Content merge.** The curve *is* the data: plotted from the same
  table the page prints at its close (§6.13), ticked with the same
  hours the harbour keeps (§6.6), and read by the stamps (§6.5). It is
  not a decoration beside the content; it is the content's x-axis,
  stood upright.
- **Failure fallback.** If SVG generation fails or the table data is
  absent, the rail prints the static mean-level line and the page
  proceeds without fill — the log opens at mean level and says so. A
  loop stall of 1000ms freezes the fill at its last true value (never
  animates it to a guessed one).
- **Reduced-motion variant.** No undulation; the curve prints as a
  still chart. The fill still tracks scroll (it is information, a
  state, not a performance) but steps instantly to the mapped height
  with no lerp. The rail head text still updates.
- **Performance budget & mobile variant.** One path, one clip rect,
  one text node: ≤ 0.3ms/frame in the shared loop. Undulation is a
  `d` rewrite at 30Hz maximum on the *visible* segment only (the path
  is windowed: segments beyond ±1 viewport are rendered from a
  pre-baked static path). Mobile (<768px): the rail narrows to 28px,
  the curve flattens to a centre-line amplitude of ±8px, hour ticks
  and height labels are dropped (the rail head keeps the live height),
  and undulation amplitude halves to ±1.5px.

#### 6.2 v2 — Choreography timeline

Continuous, so the timeline is a map: page top → fill at the opening
height, rail head printing the opening state → each entry boundary →
the fill passes that entry's stamped height at the moment the entry's
header crosses 55% viewport height (the stamp and the fill agree by
construction, §6.5) → mid-page → the fill crosses HW or LW exactly
where the curve turns, the brass dot at the extremum brightening as
the fill touches it → page foot → fill at the closing height, rail
head printing the closing state. Undulation runs throughout at 11s,
independent of scroll, suspended off-screen.

#### 6.2 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest (top) | Fill at opening height; undulation live | Fill at opening height; undulation ±1.5px |
| Reading | Fill lerps 0.12 to mapped height; head text updates ≤ 5×/s | Same, labels suppressed |
| Hover | None | n/a |
| Focus | The rail is not focusable; the rail head's height is duplicated in §6.13's table for AT | Same |
| Scrolled-past (bottom) | Fill at closing height | Same |
| Disabled / no-JS | Static curve, mean-level fill, `MEAN LEVEL` head | Same |

#### 6.2 v2 — Breakpoint behaviour

≥1200px: 96px rail, full ticks and labels, undulation ±3px.
768–1199px: 56px rail, ticks kept, height labels only at extrema,
undulation ±2px. <768px: 28px strip, curve amplitude ±8px around the
strip centre, no ticks or labels in-rail, undulation ±1.5px, rail head
moves into the masthead (§6.10) as a single mono line.

#### 6.2 v2 — Edge cases & failure modes

*Short page (curve shorter than one tide):* the day's table still
plots; the fill maps across whatever range the table declares, and the
rail head names the partial day (`TO HW ONLY`) rather than implying a
full cycle. *Table with a double HW (a real anomaly in some ports):*
both extrema plot; `tideAt()` interpolates between them across the
stand, and the stamps say `HW STAND` — the theme prints the anomaly,
it does not smooth it away. *Resize / orientation change:* the path
re-plots from the table at the new rail width within one frame; the
fill re-maps proportionally, never animating to the new value.
*Content injected late (a late entry):* the rail lengthens and the
path re-plots; entries already stamped keep their stamps (they were
true when written).

#### 6.2 v2 — Accessibility spec

The SVG is `aria-hidden` — it is a chart of data that exists in full
as §6.13's table, which is the accessible original; the rail head's
live height is *not* a live region (a height announcement every 0.1 m
would be noise), and the same value is reachable in the table and in
each entry's stamp. The curve's brass-on-glass pairing is graphical
(≥ 3:1 against paper is not required of a chart line whose data is
duplicated in text, per the duplication law stated here and audited at
the gate). Focus never enters the rail.

#### 6.2 v2 — Tokens consumed

`--glass`, `--brass`, `--glass-deep`, `--ink`, `--loop-lerp` (0.12),
`--undulate-period` (11s), `--undulate-amp` (3px), `--rail-w` (96px).

### 6.3 Section flooding

- **What & why.** Each entry enters the page the way water enters a
  dry dock: through a rising waterline. As an entry scrolls into view,
  a waterline mask climbs it from bottom to top over 900ms and the
  entry is *flooded in* — revealed not by fading from nothing but by
  the level rising over it, a visible meniscus line at the surface,
  after which the entry stands complete and dry. It belongs because
  the entries are written at successive tides (§1); the flood is the
  entry's timestamp being applied, the moment the day's water reached
  this line of the book.
- **Structure.** Each `.entry` carries a `::after` waterline band
  (height 26px, `--waterline` fill with a 2px `--brass` meniscus rule
  at its top edge) positioned over the entry's lower portion, and the
  entry's content wrapper takes a `clip-path: inset(0 0 X% 0)` whose
  X is driven from 100 → 0 by an IntersectionObserver trigger and a
  CSS transition on a registered custom property, or by the shared
  loop where clip animation is needed in step with the band. Both the
  band and the clip are applied by JS arming (`html.js .entry`); the
  un-armed entry is complete.
- **Motion spec.** Trigger: entry's top crosses 82% viewport height.
  Duration 900ms `--ease-swell`: the waterline rises from the entry's
  foot to its head, the band travelling with the clip edge; at
  completion the band fades over 200ms and the clip is removed
  entirely (not left at inset 0 — a finished flood leaves no
  apparatus). Entries already above the fold on load flood in
  sequence, staggered 120ms in reading order, after §6.1 completes.
  An entry taller than 160vh floods in two stages keyed to its halves,
  so its foot is never held underwater waiting for its head.
- **States.** *Unflooded (armed, below trigger):* clipped, band at
  foot — a state that exists only below the fold or in the first
  paint above it. *Flooding:* 900ms rise. *Flooded (rest):* complete,
  clip removed — the permanent state. *Scrolled-past:* flooded;
  floods never reverse (water that has covered an entry has covered
  it; scrolling up shows the dry, written entry). *Hover/focus:* a
  focus event inside an unflooded entry floods it instantly (keyboard
  readers are never asked to tab through water).
- **Content merge.** The flood reveals the entry's own contents in
  reading order — head first is wrong for water, so the reveal runs
  foot-to-head visually while DOM order stays head-first; the
  meniscus passes the entry's stamp, figures and porthole in the
  order the water would reach them. Remove the entry and there is
  nothing to flood: the animation has no independent existence.
- **Failure fallback.** The original entry's safety law, kept: a
  1000ms observer-timeout — any entry that has been in the viewport
  1000ms without its flood completing is un-clipped by the watchdog,
  band removed. IO unsupported: no arming at all; entries print. JS
  off: entries print. A flood interrupted by tab-hidden completes
  instantly on return (the transition's end state is applied, not
  resumed mid-rise).
- **Reduced-motion variant.** No flood. Entries are simply present,
  separated by their brass rules. The entry's arrival is marked only
  by its stamp (§6.5), which still fires.
- **Performance budget & mobile variant.** One clip + one band per
  flooding entry, concurrency capped at 2 simultaneous floods (a
  third waits for the first to finish — docks fill one at a time);
  compositor-only, ≤ 0.4ms/frame. Mobile: duration 700ms, band height
  18px, concurrency 1.

#### 6.3 v2 — Choreography timeline

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Entry top crosses 82% vh; waterline band appears at the entry's foot, clip at 100% |
| 2 | t₀ + 0–900ms | Waterline rises `--ease-swell`; content revealed foot-to-head as the meniscus passes |
| 3 | t₀ + 900ms | Meniscus clears the entry head; clip reaches 0 |
| 4 | t₀ + 900–1100ms | Band fades out; clip removed from the DOM node |
| 5 | t₀ + 1000ms | Watchdog checkpoint: if beats 3–4 have not completed, they are forced |

#### 6.3 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Unflooded | Clipped, band at foot (below fold or pre-trigger only) | Same |
| Flooding | 900ms rise, ≤ 2 concurrent | 700ms rise, 1 concurrent |
| Flooded (rest) | Complete, no clip, no band | Same |
| Hover | No change | n/a |
| Focus inside | Floods instantly to complete | Same |
| Scrolled-past | Flooded, permanent | Same |
| Disabled / no-JS | Printed entry | Same |

#### 6.3 v2 — Breakpoint behaviour

≥1200px: full spec, 900ms, band 26px. 768–1199px: 800ms, band 22px.
<768px: 700ms, band 18px, and entries taller than 120vh flood in two
stages (the 160vh rule tightens with the smaller viewport).

#### 6.3 v2 — Edge cases & failure modes

*Fast fling past several entries:* entries more than one viewport
above the current position are flooded instantly by the watchdog pass
— the reader must never scroll up into an underwater entry. *Entry
edited live (CMS preview):* a re-armed entry floods once more; the
stamp (§6.5) does not re-fire (the tide at that line has not changed).
*Very short entry (a single line):* the flood still runs but at 500ms
— duration scales with height between 500ms and 900ms, because a
puddle does not take as long to fill as a dock. *Print:* clips and
bands do not print; entries print complete.

#### 6.3 v2 — Accessibility spec

Flooding never changes DOM order, focusability timing beyond the
900ms window, or text availability to AT (the clip is visual only;
the content is in the accessibility tree throughout — `clip-path`
does not remove content from AT, and the build must not pair it with
`visibility: hidden`). Focus entering an unflooded entry completes
its flood instantly (state matrix). The meniscus band is
`aria-hidden`. Contrast of revealed content is the standing palette
contrast; the `--waterline` band at 14% never sits *under* text at
rest, only passes over it in motion.

#### 6.3 v2 — Tokens consumed

`--waterline`, `--brass`, `--ease-swell`, `--dur-flood` (900ms),
`--band-h` (26px), `--watchdog` (1000ms).

---

### 6.4 Sine bob

- **What & why.** Everything that floats in this harbour moves a
  little, and it moves on the visitor's own hand: porthole frames and
  the images in them bob ±5px on a sine whose phase is the *scroll
  position*, scrubbed — scroll and the moored things ride; stop and
  they settle where the water left them. It belongs because the bob
  is not an ambient decoration loop (the theme rations those to two,
  §5) but a property of the water the reader is moving through: the
  same scroll that raises the tide (§6.2) rocks the things floating
  on it.
- **Structure.** Each `.float` element (porthole frames §6.15, the
  buoy §6.9 at rest, figure blocks in the data margin) carries a
  `data-phase` offset assigned in reading order (0, 0.7, 1.4… radians,
  so neighbours are never in step — a harbour where every boat rises
  together is a diorama, not a harbour). The shared loop writes
  `transform: translateY(sin(scrollY × 0.004 + phase) × amp)` per
  visible floater. The transform is on a wrapper, never on the
  element that carries borders or text layout, so the bob cannot
  disturb the ruling of the page.
- **Motion spec.** Amplitude 5px at ≥1200px, wavelength one full cycle
  per 1570px of scroll (0.004 rad/px). Lerped by the shared loop
  (0.12) so a fling does not teleport floaters — they ride through
  the positions between. No autonomous time component: at rest
  scroll, bob is still. This is deliberate and is the element's
  discipline: motion sickness in this theme comes from things moving
  unasked, and nothing here moves unasked except the curve and the
  buoy.
- **States.** *Rest (scroll still):* floater holds its sine value at
  the current scroll position. *Scrolling:* rides the sine. *Hover:*
  the bob continues under the pointer (a boat does not stop for a
  hand) but §6.7's wet-ink and §6.15's sheen proceed unaffected on
  their own layers. *Scrolled-past:* value frozen at exit position;
  loop stops writing off-screen floaters. *Disabled:* transform
  removed below the fold on low-power devices (§14 cut order).
- **Content merge.** The things that bob are the page's own floating
  objects — the photographs in their brass portholes, the day's
  figures in their frames — and they bob *in place*, in the margin
  where they are moored. Text never bobs: prose is written in the
  book, and the book is on the desk, not in the water. That line —
  print still, cargo afloat — is the element's whole grammar.
- **Failure fallback.** No loop, no bob: floaters sit at translateY 0,
  fully laid out. A floater whose wrapper fails keeps its content —
  the wrapper is a plain div in the DOM, transform or none.
- **Reduced-motion variant.** None. Bob is abolished, not reduced:
  the original entry's standing rule ("reduced-motion variant has no
  bob or swell") is kept verbatim.
- **Performance budget & mobile variant.** Transform writes only for
  floaters within ±1 viewport, capped at 8 concurrent; ≤ 0.3ms/frame.
  Mobile: amplitude 3px, cap 5 floaters.

#### 6.4 v2 — Choreography timeline

Scrubbed, so the timeline is spatial: floater enters the viewport at
its phase value → as the reader scrolls one wavelength (1570px) the
floater completes one full ride (+5 → −5 → +5px) → it leaves the
viewport holding its exit value → the loop retires it. Two adjacent
floaters are always ≥ 0.7 rad out of phase, so at any scroll position
the margin reads as separate moorings, never a chorus line.

#### 6.4 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Holds sine value at current scroll | Holds value; amp 3px |
| Scrolling | Rides sine, lerp 0.12 | Same |
| Hover | Bob continues; other layers unaffected | n/a |
| Focus (floater contains a link) | Bob continues — focus outline rides with the wrapper, staying glued to the frame | Same |
| Scrolled-past | Frozen at exit value, writes stopped | Same |
| Disabled / no-JS | translateY 0, static | Same |

#### 6.4 v2 — Breakpoint behaviour

≥1200px: amp 5px, cap 8. 768–1199px: amp 4px, cap 6. <768px: amp 3px,
cap 5, and portholes in the single column bob at half phase density
(phase step 1.1 rad) so a short screen of stacked frames does not
read as a wave machine.

#### 6.4 v2 — Edge cases & failure modes

*Floater taller than the viewport:* its phase is read at its centre;
the ride is gentle enough (±5px) that no edge can expose a gap —
floaters are never clipped by their containers for this reason
(build rule: bobbing wrappers live in unclipped margin space).
*Scroll restoration mid-page:* floaters take their sine values from
the restored position on the first frame — no ride-in. *Layout
shift:* transforms only; the wrapper's box never moves, CLS 0.

#### 6.4 v2 — Accessibility spec

Purely visual; nothing is announced. A focusable element inside a
bobbing wrapper keeps its outline attached (the outline is drawn on
the inner element, which rides with the wrapper's transform — verified
at the gate, because an outline left behind by a moving frame is a
known failure of transform-based motion). Motion is scroll-bound and
ceases when scrolling ceases; vestibular risk is minimal and the
reduced-motion variant removes it entirely.

#### 6.4 v2 — Tokens consumed

`--ease-bob`, `--loop-lerp` (0.12), `--bob-amp` (5px), `--bob-wave`
(0.004 rad/px), `--bob-phase-step` (0.7 rad).

### 6.5 Tide-height stamps

- **What & why.** Every entry header is stamped, as it enters, with
  the tide at that point of the page — `HW 4.7 m · 14:20`, or on the
  ebb `3.9 m · FALLING` — struck at −3° with the harbourmaster's seal
  ring around it. The stamp is the entry's metadata made physical:
  not a date in a byline but the state of the water when this line of
  the book was written, computed by `tideAt()` from the printed table
  at the page-tide the entry's position declares. It is the element
  that makes the law (§1) visible — a reader who doubts a stamp can
  check it against §6.13's table and the rule of twelfths, and it
  will agree, because it was computed from them.
- **Structure.** A `.stamp` element at the entry title's right (data
  margin on desktop, beneath the title on phone): an oval double ring
  (border 1.5px `--brass`, inner ring offset) containing two lines —
  the fact in mono 12px `--brass-deep` (`HW 4.7 m · 14:20`) and, where
  the entry earns one, the harbourmaster's remark in Caslon italic
  13px `--glass-deep`. The stamp's rotation is −3° exactly — a hand
  strikes at a slight angle, and the angle is a constant of the
  office, not a random per-stamp jitter (deterministic: every stamp
  on the page at −3.0°, because it is the same hand and the same
  stamp). The stamp is server-rendered with its computed values
  wherever the build allows; JS re-computation must produce identical
  strings or leave the server's alone.
- **Motion spec.** Trigger: the entry's flood (§6.3) completes, or
  the entry crosses 55% viewport height, whichever is later — the
  stamp is struck on a written entry, not on water. Strike: scale
  1.5 → 1 with `--ease-press` over 200ms, opacity 0 → 1 in the first
  60ms, and a brass fade-in ring (a pseudo-element ring scaling
  1 → 1.18, opacity 0.5 → 0, 380ms) — the shock of the strike
  travelling into the paper. Once struck, a stamp never moves again;
  scroll-back shows it struck.
- **States.** *Unstruck (armed, pre-trigger):* absent (opacity 0,
  scale 1.5) — the only hidden state in the element, and it resolves
  by watchdog, below. *Striking:* 200ms press. *Struck (rest):*
  printed at −3°, permanent. *Hover:* none — a stamp is a record,
  not a control; the cursor passes over it as over ink. *Scrolled-
  past:* struck.
- **Content merge.** The stamp sits on the entry it describes, states
  the tide the entry's own position declares, and its values come
  from the page's own table. It is the entry's colophon, not a badge
  applied by the design system: move the entry earlier in the day and
  its stamp must change, because its tide changed — the gate tests
  exactly this (§10).
- **Failure fallback.** Stamps are printed in the DOM by default; JS
  arming hides only stamps below the trigger line, and a 1000ms
  watchdog strikes any stamp whose entry has been readable for a
  second unstruck. If `tideAt()` data is missing, the stamp prints
  its state without a height (`HW · TIME FROM TABLE`) rather than an
  invented figure — a stamp with a blank where the number belongs is
  honest; a stamp with a guessed number is forgery (§1).
- **Reduced-motion variant.** The stamp appears without the press —
  opacity step at the trigger, no scale, no ring. The record is the
  same.
- **Performance budget & mobile variant.** One transform + one
  pseudo-element per stamp, one-shot; negligible. Mobile: the stamp
  sits beneath the title at −3°, ring diameter shrinks 84px → 68px,
  the italic remark line is dropped below 380px width (the fact
  remains).

#### 6.5 v2 — Choreography timeline

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Entry flooded and past 55% vh: stamp begins its press (scale 1.5, opacity 0) |
| 2 | t₀ + 60ms | Opacity reaches 1 — the ink lands before the stamp has finished travelling |
| 3 | t₀ + 200ms | Scale reaches 1; the stamp is struck |
| 4 | t₀ + 200–580ms | Brass shock ring expands 1 → 1.18 and fades to 0 |
| 5 | t₀ + 1000ms | Watchdog: any stamp readable-but-unstruck is printed without animation |

#### 6.5 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Unstruck | Hidden, below trigger only | Same |
| Striking | 200ms `--ease-press` + ring | Same |
| Struck (rest) | At −3°, permanent | At −3°, beneath title |
| Hover | No change | n/a |
| Focus | Stamp is not focusable; entry focus never waits for it | Same |
| Scrolled-past | Struck | Struck |
| Disabled / no-JS | Printed struck | Printed struck |

#### 6.5 v2 — Breakpoint behaviour

≥1200px: stamp in the data margin, ring 84px, both lines. 768–1199px:
stamp at the title's right within the entry column, ring 76px.
<768px: beneath the title, ring 68px; <380px the italic remark is
omitted (fact line always kept).

#### 6.5 v2 — Edge cases & failure modes

*Entry at the exact extremum:* the stamp reads `HW 4.7 m · 14:20` /
`LW 1.1 m · 08:05` — the extremum's own time from the table, not the
entry's scroll time; within ±20 minutes of an extremum the stamp says
`HW SLACK` / `LW SLACK`, because a harbourmaster writes "slack" when
the water is standing. *Entry between tides on a short page:* stamps
interpolate and round to 0.1 m, always by `tideAt()`. *Duplicate
heights on the stand (double HW):* the stamp prints the first HW and
the remark line carries `— the water stands twice today`. *Remark
absent:* most entries earn no remark; an entry with a remark on every
line is a gate failure (§9) — the harbourmaster is a busy man.

#### 6.5 v2 — Accessibility spec

The stamp is real text in the DOM in reading order after the entry
title, so AT meets `No. 4 — HW 4.7 m · 14:20` as part of the heading's
entry. The rotation is visual only. `--brass-deep` on `--paper` is
4.96:1 — the fact line passes AA at its 12px mono size; the ring
itself is decorative. The strike animation is never announced.

#### 6.5 v2 — Tokens consumed

`--brass`, `--brass-deep`, `--glass-deep`, `--ease-press`,
`--dur-stamp` (200ms), `--stamp-tilt` (−3°), `--stamp-ring` (84px).

### 6.6 Pinned harbour hours

- **What & why.** The harbour keeps two times: the hours the office
  is open, which do not move, and the tides, which do nothing else.
  This element pins them against each other: the harbour-hours table
  pins for one viewport while the day's tide rows scroll beside it,
  each row inking darker as it aligns with its hour — so the visitor
  reads, in one screen, whether the office is open when the water is
  right. It belongs because it is the page's one genuinely functional
  instrument: every harbour business answers "can I come at three?"
  with exactly this join of the two tables.
- **Structure.** A two-column stage (≥1200px): left, the pinned
  harbour-hours table (a real `<table>`: days, open/close, the
  harbourmaster's notes — "Office closes HW−1 on spring tides"); right,
  the day's tide rows as a scrolling list, each row carrying time,
  state (HW/LW), height, and the office state at that tide computed
  from the left table (`OFFICE OPEN`, `OFFICE CLOSED`, `LAST HOUR`).
  The pin is `position: sticky` inside a stage of 200vh; the rows
  column scrolls naturally. Alignment: a row is "aligned" when its
  centre is within 40px of the pinned table's centre row; aligned
  rows take full `--ink`, others rest at 55% ink — inking, not
  highlighting: no background changes, the letters themselves darken,
  as if the row had been gone over twice with the pen.
- **Motion spec.** Scroll-driven throughout, written by the shared
  loop: row ink opacity lerp 0.12 toward its alignment value. The
  pin engages and releases with the stage's own geometry (sticky,
  no JS pinning). At the stage's end the hours table unpins and
  scrolls away with the last rows — the office closes the instrument
  by putting it back in the book. Total stage: 200vh desktop, and on
  mobile the pin is abolished entirely (below).
- **States.** *Approaching:* both columns in flow. *Pinned:* hours
  fixed, rows scrolling and inking. *Released:* both in flow again.
  *Hover (a row):* §6.7's wet-ink spread applies — the rows are
  ledger rows. *Focus:* keyboard focus on a row's link (a row may
  link to the booking entry, pre-filled with that tide) inks it fully
  regardless of alignment.
- **Content merge.** The two tables are the business's real hours and
  the port's real tides, and the computed third column (office state
  at each tide) is information that exists only in their join — the
  element *is* the computation, performed spatially. Print the stage
  statically and it still works as two tables side by side; the pin
  merely keeps the join in view while it is read.
- **Failure fallback.** No sticky support or JS off: the two columns
  print side by side in flow, all rows at full ink, the computed
  column present (it is server-rendered). Nothing about the data
  depends on the pin.
- **Reduced-motion variant.** No pin (a pinned scene is a motion
  commitment), no ink gradation: both tables in flow, all rows full
  ink, the computed column printed. The instrument becomes a table —
  which is what it always was, minus the performance.
- **Performance budget & mobile variant.** Opacity writes on ≤ 12
  rows, in the shared loop; ≤ 0.2ms/frame. Mobile (<768px): pin
  abolished; the hours table prints above the tide rows as a single
  stacked ledger page, rows full ink, computed column kept — a phone
  reader gets the join as a table, not a stage.

#### 6.6 v2 — Choreography timeline

Spatial beats: stage top reaches viewport top → pin engages, hours
table fixed → first tide row aligns (inks to 100% over ~300ms of
scroll) as the reader's eye reaches it → successive rows align and
ink, the previously aligned row settling back to 55% as it passes →
the last row aligns at the stage's final viewport → pin releases,
hours table scrolls away above the closing rows. Reverse scroll
replays the inking symmetrically — alignment is a function of
position, not of history.

#### 6.6 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Approaching | Both columns in flow | Stacked, in flow |
| Pinned | Hours fixed; rows ink 55% → 100% at alignment | n/a — no pin |
| Released | Both in flow | Stacked, in flow |
| Hover (row) | Wet-ink spread (§6.7) | n/a |
| Focus (row link) | Row inks fully | Row inks fully |
| Scrolled-past | In flow, rows at rest ink | Same |
| Disabled / no-JS | Side-by-side tables, full ink | Stacked tables, full ink |

#### 6.6 v2 — Breakpoint behaviour

≥1200px: full stage, 200vh, pin + inking. 768–1199px: stage 160vh,
pin kept, alignment band widens to 56px (a tablet's scroll is
coarser). <768px: no stage, no pin — stacked ledger page, computed
column retained.

#### 6.6 v2 — Edge cases & failure modes

*A day with two tides only (a short table):* the stage shortens to
140vh so the pin does not outstay its data. *Office closed all day
(a Sunday in winter):* every row's computed state reads `OFFICE
CLOSED`, and the hours table's note says why in the harbourmaster's
hand — the instrument reports a closed harbour as plainly as an open
one. *Tide row exactly at closing time:* the computed state reads
`LAST HOUR` — the join's edge case is given its own honest word, not
rounded to open or closed. *Rows taller than the alignment band on
short screens:* alignment reads the row's first line.

#### 6.6 v2 — Accessibility spec

Both tables are real `<table>`s with `<th scope>` headers; the
computed column is a real column, not a visual overlay, so AT reads
the join directly. The ink gradation is presentational — all rows
are in the accessibility tree at all times, and 55% ink rows still
measure `--ink` at 55% over `--paper` ≈ 5.4:1 effective, above AA
for the 15px mono they are set in (verified at the gate; if a build's
paper differs, the rest value rises to 65%). Sticky positioning does
not alter focus order.

#### 6.6 v2 — Tokens consumed

`--ink`, `--paper`, `--brass`, `--glass-deep`, `--loop-lerp` (0.12),
`--stage-h` (200vh), `--align-band` (40px), `--row-rest-ink` (55%).

---

### 6.7 Wet-ink hover

- **What & why.** A ledger row under attention looks *wetter*: hover
  spreads a darker ink wash across the row from the left, the
  gradient's edge travelling over 400ms, as if the line had just been
  written and the ink were still finding the paper. It belongs
  because in a logbook attention is physical — the reader's finger
  travels the line being read, and the wash is that finger, rendered
  as the page's own material. No row changes colour, lifts, or glows;
  its ink simply deepens, left to right, in reading order.
- **Structure.** Rows (`.lrow` — ledger rows in tables, index lines,
  tide rows) carry a background built from two stacked linear
  gradients: the paper, and an ink wash (`--ink` at 7%) whose
  `background-size` animates 0% → 100% width with
  `background-position: left`, transitioned 400ms `--ease-drift`. A
  2px `--brass` left rule is part of the wash layer, so the attended
  row also gains its margin tick — the reader's place, kept in the
  margin as readers have always kept it.
- **Motion spec.** Hover/focus-within: wash spreads 0 → 100% over
  400ms. Leave: the wash recedes over 550ms — slower out than in,
  because ink dries slower than it spreads; the brass tick fades in
  the last 100ms of the spread and out in the first 100ms of the
  recession. The wash never exceeds 7% ink: it is a deepening, not a
  highlight block, and text contrast over the washed ground stays
  ≥ 12:1.
- **States.** *Rest:* paper, no tick. *Attended:* wash full, tick
  present. *Active (row pressed, where the row is a control):* wash
  deepens to 10% for the press duration — the finger presses. *Focus:*
  identical to hover (keyboard attention is attention). *Scrolled-
  past:* rest.
- **Content merge.** The wash acts on the row's own paper and stops at
  the row's own edges; the tick lands in the row's own margin. It
  carries no content and hides none — remove it and the ledger reads
  identically, only drier.
- **Failure fallback.** A plain background transition; unsupported
  gradient sizing degrades to an opacity fade of the same wash. No-JS
  is irrelevant — the element is pure CSS and works in the static
  page.
- **Reduced-motion variant.** The wash appears and disappears
  instantly (0ms) — the state (this row is attended) is information a
  keyboard user needs; only its travel is motion.
- **Performance budget & mobile variant.** One background-size
  transition per attended row; zero JS. Mobile: no hover — the wash
  is focus/active only, and tide rows (§6.6) get the wash on tap-hold
  via `:active`.

#### 6.7 v2 — Choreography timeline

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Pointer/focus enters the row; wash begins spreading from the left rule |
| 2 | t₀ + 300ms | Wash at ~85%; brass margin tick begins fading in |
| 3 | t₀ + 400ms | Wash full at 7% ink; tick solid — the row is attended |
| 4 | Leave + 0ms | Tick fades (100ms); wash begins receding |
| 5 | Leave + 550ms | Row back to dry paper |

#### 6.7 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Dry paper | Dry paper |
| Hover | Wash spreads 400ms, tick in | n/a |
| Focus | Same as hover | Same (external keyboard) |
| Active | Wash deepens to 10% while pressed | Wash on tap-hold |
| Scrolled-past | Rest | Rest |
| Disabled row | No wash; row printed at 55% ink with its reason (§11) | Same |

#### 6.7 v2 — Breakpoint behaviour

All breakpoints: identical mechanism; below 768px the wash applies to
full-width rows only (margin rows are too narrow to read a spread in)
and the tick moves to the row's right edge, since the left margin is
the tide rail there.

#### 6.7 v2 — Edge cases & failure modes

*Very long row (a wrapped two-line entry):* the wash covers both
lines — it is the row's ground, not its first line's. *Pointer
skimming a table:* a 60ms intent delay before the spread starts, so
a diagonal crossing doesn't wet six rows; leaving within the delay
cancels cleanly. *Row inside the pinned hours (§6.6):* the wash and
the alignment inking compose (wash is background, inking is colour)
— verified at the gate, because two attention systems on one row is
exactly where themes usually double-print.

#### 6.7 v2 — Accessibility spec

The wash is decorative emphasis on an already-legible row; the
attended state is conveyed to AT by the row's own semantics (link,
button, or `aria-current` where applicable), never by the wash alone.
Focus-visible rows get the wash *plus* the theme's focus ring (§11) —
the wash supplements the ring, never replaces it. Contrast over the
full wash: `--ink` on 7%-washed paper ≈ 12.3:1.

#### 6.7 v2 — Tokens consumed

`--ink`, `--brass`, `--paper`, `--ease-drift`, `--wash` (7%),
`--dur-wash` (400ms).

### 6.8 Seal stamp click

- **What & why.** Clicking a ledger row stamps it with the
  harbourmaster's seal at its end — the round brass seal, pressed at
  the same −3°, marking the entry *read and approved* in the book's
  own language. It belongs because a logbook's only native
  interaction is the mark of the office: entries are not liked or
  saved, they are *passed*. Where a site needs a read/approved/
  confirmed state per item — applications reviewed, catches logged,
  berths allocated — the seal is that state, struck on the item
  itself.
- **Structure.** The seal is an inline SVG (outer ring, inner ring,
  the port's initials and a fouled anchor in line work, drawn in
  `--brass-deep`) sized 44px, placed in the row's data cell, rendered
  only after the click (before that, the cell holds its ordinary
  content — a dash, a figure — because an unsealed row is not an
  empty row). Rows that can be sealed are real `<button>`s or carry a
  button in the row; the seal's presence is state, persisted per the
  host site's rules (form state, account state) and reflected in
  `aria-pressed`.
- **Motion spec.** Click: the seal presses in — scale 1.5 → 1, 180ms
  `--ease-press`, opacity 0 → 1 in 50ms — with the same brass shock
  ring as §6.5 (scale 1 → 1.18, fade 380ms) and a 1px downward settle
  of the row's baseline text at the press's end (the page takes the
  weight). Un-sealing (second click, where the host allows it): the
  seal fades over 300ms and a hairline strike prints through it
  before it goes — a seal struck through, then removed from the
  copy the visitor sees; the office keeps its own records.
- **States.** *Unsealed:* no seal; the row's cell holds its content.
  *Pressing:* 180ms. *Sealed (rest):* seal printed at −3°, 44px,
  permanent while the state holds. *Hover (unsealed, sealable row):*
  §6.7's wash plus a ghost of the seal at 18% opacity in the cell —
  the visitor sees where the mark will fall before committing it.
  *Disabled row:* not sealable; no ghost, no press.
- **Content merge.** The seal lands on the entry it approves, in the
  entry's own row, at the end of its own line — the mark and the
  marked are one object. A sealed count, where the page shows one
  (§6.14's closing totals), counts the DOM's sealed rows; it is not
  a separate number that could drift.
- **Failure fallback.** The seal state is class + `aria-pressed`;
  without JS the rows render with their server-side state (sealed
  rows print sealed). A click that fails to persist (network) keeps
  the visual seal only if the host confirms — otherwise the seal
  fades at 600ms and the row's note line says, in the harbourmaster's
  hand, `— not entered; try again`. The book never shows a mark the
  office didn't make.
- **Reduced-motion variant.** Seal appears at full size, opacity step,
  no press, no ring, no baseline settle. State identical.
- **Performance budget & mobile variant.** One SVG per sealed row
  (instances share the same `<symbol>`), one-shot transforms;
  negligible. Mobile: seal 38px; the ghost preview is omitted (no
  hover) — the first tap seals, with the row's note confirming.

#### 6.8 v2 — Choreography timeline

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Click lands; seal at scale 1.5, opacity 0, above the cell |
| 2 | t₀ + 50ms | Opacity 1 — ink contact |
| 3 | t₀ + 180ms | Scale 1: the press completes; shock ring begins |
| 4 | t₀ + 190ms | Row's baseline settles 1px and returns over 120ms — the page takes the weight |
| 5 | t₀ + 560ms | Ring faded; the seal rests as print |

#### 6.8 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Unsealed | Cell holds its content | Same |
| Hover (sealable) | Wash + seal ghost at 18% | n/a |
| Focus | Wash + ghost + focus ring | Same |
| Pressing | 180ms press + ring | Same |
| Sealed (rest) | Seal at −3°, 44px | Seal at −3°, 38px |
| Disabled | Not sealable, no ghost | Same |
| Scrolled-past | State persists as print | Same |

#### 6.8 v2 — Breakpoint behaviour

≥1200px and 768–1199px: full spec, seal 44px, ghost preview on hover.
<768px: seal 38px, no ghost, tap seals directly; the strike-through
un-seal animation shortens to a 200ms fade (small screens, small
ceremonies).

#### 6.8 v2 — Edge cases & failure modes

*Row already sealed by the server on load:* prints sealed, no press —
the visitor did not strike it. *Rapid double-click:* the second
click is the un-seal only after the press completes (input locked
180ms) — a stutter must not strike and strike-through in one gesture.
*Seal on a row that is mid-flood (§6.3):* clicks are accepted only
after the flood completes; before that the row is water, and the
office does not seal water. *Many sealed rows (a full day approved):*
each seal is the same −3° and the same SVG — uniformity is the
authenticity; per-seal random rotation is a §9 failure.

#### 6.8 v2 — Accessibility spec

Sealable rows expose the state with `aria-pressed` and a label that
names the act (`Mark entry 4 as passed`) — the seal graphic is
`aria-hidden`, the state is not. The ghost preview never appears for
keyboard focus without the focus ring also showing. Sealed rows
remain fully readable; the seal sits in the data cell, never over
text. Touch target: the row's button is ≥ 44px tall.

#### 6.8 v2 — Tokens consumed

`--brass-deep`, `--brass`, `--ease-press`, `--dur-seal` (180ms),
`--stamp-tilt` (−3°), `--seal-size` (44px).

### 6.9 Buoy button tug

- **What & why.** The page's single conversion — the booking button —
  is the harbour's single buoy: buoy orange, used nowhere else (§2),
  and it *behaves* like a moored buoy. It drifts toward the pointer
  within a 60px radius with a slow elastic lag, and at rest it bobs
  gently on the page's water. It belongs because the theme's one law
  of conversion is that there is one thing to do here and the harbour
  marks it the way harbours mark the safe channel: with the one
  orange object, riding the same tide as everything else, impossible
  to mistake for anything else on the page.
- **Structure.** A real `<button>` or link styled as the buoy: pill
  form (the theme's only fully rounded element — a buoy is round),
  `--buoy` face, label in `--ink` 18px Source Serif 600 with the
  sailing's fact in mono beneath it where the button is large
  (`BOOK THE CROSSING` / `FRI 14:20 · HW 4.7 m`). It sits inside a
  mooring wrapper with 60px of clear water on all sides (layout
  reserves it; the drift never overlaps neighbouring content). The
  drift is transform on the button, driven by the shared loop toward
  a target computed from pointer position; the bob adds §6.4's sine
  at the button's own phase.
- **Motion spec.** *Rest bob:* ±3px on the scroll-scrubbed sine (§6.4
  machinery, the button's phase fixed at 2.1 rad) plus a slow
  time-based sway of ±1.5px at 7s — the buoy is the second of the
  theme's two permitted ambient loops (§5), because a buoy that never
  moves at rest is a painted buoy. *Tug:* pointer within 60px of the
  button's edge → target = pointer direction × up to 14px, lerped at
  0.08 (slower than the loop's 0.12 — a buoy is heavy) with an elastic
  overshoot of 2px on arrival (spring via the lerp's under-damping,
  capped). Pointer leaves → the buoy rides back to its mooring over
  ~900ms of decaying bob. *Press:* scale 0.97 for 120ms `--ease-press`
  and the face darkens to `--buoy-deep` — the buoy dips under the
  hand.
- **States.** *Rest:* bobbing at its mooring. *Approached:* tugging
  toward the pointer, ≤ 14px. *Hover:* at full tug, bob continues
  (superimposed, ±1.5px). *Focus:* tug is *not* applied — a keyboard
  user's button stays where the layout put it; the focus ring is a
  2px `--buoy-deep` outline offset 3px, and the bob pauses while
  focused (a button being read does not move). *Active:* the dip.
  *Disabled:* the buoy is hauled out — printed in `--glass` at 55%
  with its note (`— no sailing; next tide FRI 06:10`), because a
  disabled orange button would still be an orange object competing
  with nothing, and a grey buoy is an honest closed channel.
- **Content merge.** The button's label carries the sailing it books
  — time and tide state (§3 law 2) — and it lives in the booking
  entry (§6.12), moored in that entry's water. It is not a floating
  action button and never follows the reader: a buoy marks a place,
  and the place is the booking entry. One per page, enforced at the
  gate by counting `--buoy` (§2 law 3).
- **Failure fallback.** No JS or no loop: a static orange button in
  its mooring, fully functional — the tug and bob are the buoy's
  behaviour, not its existence. Pointer-coarse devices: no tug (a
  finger is not a tide), bob only.
- **Reduced-motion variant.** No tug, no bob, no sway. A still orange
  button with its label and sailing fact; the press dip becomes a
  colour step to `--buoy-deep`.
- **Performance budget & mobile variant.** One transform in the shared
  loop; the pointer listener is passive and throttled to frame rate.
  Mobile: tug abolished (proximity has no meaning under a thumb),
  rest bob ±2px scroll-scrubbed only, mooring clearance 24px, button
  full-width of the booking entry — the channel marker spans the
  channel.

#### 6.9 v2 — Choreography timeline

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Pointer enters the 60px radius; target set toward pointer, ≤ 14px |
| 2 | t₀ + 0–600ms | Buoy drifts to target at lerp 0.08, overshooting ~2px at arrival |
| 3 | Hover hold | Bob superimposes ±1.5px at 7s; the buoy rides at its tugged position |
| 4 | Pointer leaves | Target returns to mooring; buoy rides back over ~900ms, bob decaying from ±3px to rest ±1.5px sway |
| 5 | Press | 120ms dip: scale 0.97, face to `--buoy-deep`; release restores over 200ms |

#### 6.9 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Bob ±3px scroll sine + ±1.5px 7s sway | Bob ±2px scroll sine only |
| Approached | Tugs ≤ 14px toward pointer, lerp 0.08 | n/a |
| Hover | Full tug + bob | n/a |
| Focus | Moored, bob paused, `--buoy-deep` ring | Same |
| Active | Dip: scale 0.97, face `--buoy-deep` | Same |
| Disabled | Hauled out: `--glass` 55% + note | Same |
| Scrolled-past | Bob continues if in view; tug off-screen never computed | Same |

#### 6.9 v2 — Breakpoint behaviour

≥1200px: full spec, 60px mooring, tug 14px. 768–1199px: mooring 40px,
tug 10px, bob ±2.5px. <768px: no tug, full-width button, mooring 24px,
bob ±2px, label 17px (never below the 18px rule by more than the one
sanctioned step — and the gate re-checks the 4.44:1 pairing at 17px
bold, which passes as large text).

#### 6.9 v2 — Edge cases & failure modes

*Pointer parked at the radius edge:* the target is clamped and
hysteresis of 6px prevents jitter between tug and rest. *Button near
the viewport edge:* the drift is clamped so the button never leaves
its mooring wrapper — a buoy that drags its anchor into the text has
become a hazard, and the wrapper's reserved water is the guarantee.
*Two booking actions on one page (a return sailing):* the theme
forbids it — the return is a second step inside the booking entry
(§6.12), reached after the first click; the page still has one buoy.
*Reduced data / no loop:* static button, per fallback.

#### 6.9 v2 — Accessibility spec

The button is a native control with its full name (`Book the
crossing, Friday 14:20, high water 4.7 metres`) — the visible mono
sub-line is inside the accessible name, not a decoration. Drift never
applies under keyboard focus, and the button's layout box never
moves (transform only), so focus order and hit-testing stay honest.
Label contrast: `--ink` on `--buoy` 4.44:1 at ≥18px bold — large-text
AA, and the gate forbids the label at any smaller size or lighter
weight. Touch target ≥ 48px tall at all breakpoints.

#### 6.9 v2 — Tokens consumed

`--buoy`, `--buoy-deep`, `--ink`, `--glass`, `--ease-press`,
`--ease-bob`, `--loop-lerp-buoy` (0.08), `--tug-radius` (60px),
`--tug-max` (14px).

---

### 6.10 Ledger masthead & entry index (page family: navigation)

- **What & why.** Navigation in this theme is the log's own index:
  the masthead carries the port name and the day, and beneath it the
  entry index — the day's entries listed by number and tide, the way
  the harbourmaster would find anything in his book. It belongs
  because a logbook is not navigated by a menu; it is *consulted*,
  and the index is the consultation. The current entry is marked by
  its tide, not by a highlight pill: the index line for the entry in
  view carries the live height (`YOU ARE HERE · 3.9 m · MAKING`) in
  the margin beside it.
- **Structure.** A masthead block (not a floating bar): port name in
  Caslon small caps, the day and date in mono, and the rail head's
  live tide line (§6.2) repeated as text at the masthead's right. The
  index is a `<nav>` of ledger rows (§6.7 applies): `No. 4 — The
  Morning Catch — HW 14:20`, each a real anchor to its entry. On
  scroll the masthead does not stick; a compact index strip (entry
  numbers only, mono, with the current number in `--brass-deep`)
  takes its place at the viewport top after the masthead passes —
  the office's bookmark ribbon, not a second masthead.
- **Motion spec.** Index rows enter with the page's first flood
  (§6.3 grammar at masthead scale). Current-entry tracking runs on
  the shared IntersectionObserver: the current row's margin note
  crossfades (200ms) as the current entry changes; the compact
  strip's number swaps instantly (paperwork does not animate). The
  strip itself appears by a 240ms `--ease-drift` slide from above
  when the masthead leaves, and leaves the same way on scroll-back.
- **States.** *Rest (top):* full masthead + index visible. *Reading:*
  compact strip, current number marked. *Hover/focus (index row):*
  §6.7 wash + tick. *Scrolled-past (footer reached):* the strip
  retires — at the closing ledger the index's work is done.
- **Content merge.** The index is generated from the page's actual
  entries and their actual stamps: add an entry and the index gains
  a line with that entry's tide, because the index *is* the entries,
  listed. A navigation item that points nowhere in the book cannot
  exist in it.
- **Failure fallback.** Plain masthead and anchor list; the compact
  strip is the only JS behaviour, and its absence leaves the full
  index at the top — the reader scrolls, as readers of books do.
- **Reduced-motion variant.** No strip slide (it appears), no
  crossfades (notes swap instantly). Index and masthead identical.
- **Performance budget & mobile variant.** One observer, one small
  strip; negligible. Mobile: the index collapses to a `CONTENTS OF
  THE DAY` disclosure (a real `<button aria-expanded>`) listing the
  same rows; the compact strip shows `No. n / N` and the live height.

#### 6.10 v2 — Choreography timeline

Load: masthead prints, index floods with the first entry's timing →
scroll past masthead: strip slides in 240ms as the masthead leaves →
each entry boundary: strip number swaps, index margin note crossfades
200ms → footer in view: strip retires 240ms → scroll to top: strip
leaves, masthead restored. No beat animates content the reader is
currently reading.

#### 6.10 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest (top) | Masthead + full index | Masthead + closed disclosure |
| Reading | Compact strip, current No. marked | Strip with `No. n / N` + height |
| Hover (row) | Wash + tick (§6.7) | n/a |
| Focus | Wash + tick + ring | Same |
| Scrolled-past | Strip retired at footer | Same |
| Disabled / no-JS | Masthead + anchor index | Same, disclosure open by default |

#### 6.10 v2 — Breakpoint behaviour

≥1200px: full spec. 768–1199px: index in two columns under the
masthead. <768px: disclosure index; strip carries number + height
only; the port name shortens to its small-caps form without the day
line (the day lives in the hero).

#### 6.10 v2 — Edge cases & failure modes

*More entries than the index holds gracefully (> 9):* the index
lists first-level entries only; sub-entries are found by reading —
a log's index that lists every line is a second book. *An entry
without a tide (the closing ledger itself):* its index line carries
its nature instead (`— THE TABLES`), never a fabricated tide.
*Duplicate entry titles:* numbers disambiguate, as they do in the
book (`No. 4` / `No. 7`).

#### 6.10 v2 — Accessibility spec

Real `<nav aria-label="Entries of the day">`; current row carries
`aria-current="true"`, updated on entry change only. The live-height
margin note is duplicated in §6.13's table and is `aria-hidden` in
the strip (a changing height must not chatter). Disclosure button is
a real button with `aria-expanded`; Esc closes it. Rows ≥ 44px tall
on touch.

#### 6.10 v2 — Tokens consumed

`--harbour`, `--ink`, `--brass-deep`, `--glass-deep`, `--ease-drift`,
`--dur-strip` (240ms).

### 6.11 Opening of the log (page family: hero)

- **What & why.** The hero is the top of the day's page: the ruled
  heading every log opens with — port, day, the state of the water
  at opening — with §6.1's surfacing headline as its title. It
  belongs because the theme's first screen must establish the book,
  the day, and the tide before it asks for anything: a visitor who
  reads only the hero knows where they are, what day the harbour is
  keeping, and what the water is doing — which is precisely what the
  top of a harbourmaster's page tells the office.
- **Structure.** The masthead (§6.10) above; then the opening block:
  the surfacing H1 (port + day), the standfirst in Source Serif
  (the day's one-sentence summary — weather, water, and the day's
  notable sailing), and the opening figures in a ruled mono row:
  `OPENING TIDE LW 1.1 m · 08:05 · WIND NW 12 KT · VIS MODERATE` —
  each figure a real datum from the day's record or the port's
  published conditions, each traceable (§1). The margin curve (§6.2)
  begins at the hero's left, its head at the opening height.
- **Motion spec.** §6.1's surfacing runs the headline; the standfirst
  and figure row flood in (§6.3) as the surfacing completes, staggered
  120ms; the opening stamp (§6.5) strikes at the figure row's right
  when the flood settles. Nothing else moves. The hero does not
  parallax its headline — the book's first page lies flat.
- **States.** *Loading:* the unruled skeleton (§6.16) for at most
  the watchdog window. *Rest:* the printed opening. *Scrolled-past:*
  the compact strip (§6.10) inherits the day. *Focus:* a skip-link
  to the first entry bypasses the ceremony (surfacing completes
  instantly).
- **Content merge.** Every element of the hero is the day's actual
  opening record; the headline's tide line is the curve's head. There
  is no hero image and no decorative layer: the port's name, set
  large in Caslon over ruled paper, is the picture.
- **Failure fallback.** The printed opening, complete, per §6.1 and
  §6.3's fallbacks. A missing figure (no wind data today) omits its
  cell — the row prints three figures, never four with a guess.
- **Reduced-motion variant.** The printed opening, stamps appearing
  by step. Identical content.
- **Performance budget & mobile variant.** Inherits §6.1 + §6.3
  budgets; the figure row wraps to two lines on phone, mono 13px,
  and the standfirst shortens by editorial rule (§12), not by CSS
  truncation.

#### 6.11 v2 — Choreography timeline

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Masthead printed; tide line begins drawing (§6.1) |
| 2 | t₀ + 500–2100ms | Headline surfaces and bobs (§6.1 beats) |
| 3 | t₀ + 1900ms | Standfirst floods in (700ms at hero scale) |
| 4 | t₀ + 2100ms | Figure row floods; opening stamp strikes (§6.5) |
| 5 | t₀ + 2400ms | Watchdog: opening complete or forced complete |

#### 6.11 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Loading | Unruled skeleton ≤ 1000ms | Same |
| Rest | Printed opening, stamp struck | Same, figures wrapped |
| Hover | None (no hero controls except the index) | n/a |
| Focus (skip-link) | Ceremony completes instantly | Same |
| Scrolled-past | Strip inherits | Same |
| Disabled / no-JS | Printed opening | Same |

#### 6.11 v2 — Breakpoint behaviour

≥1200px: full spec, H1 54px. 768–1199px: H1 42px, figure row wraps
at four figures to 2 × 2. <768px: H1 34px, figure row 2 × 2 at 13px,
stamp beneath the row.

#### 6.11 v2 — Edge cases & failure modes

*The day has no notable sailing:* the standfirst says so in the
day's own words (`A quiet day on the water; the office is open.`) —
an honest quiet day, never an invented busy one. *Opening tide is
the day's first extremum exactly:* the stamp reads `HW · AT THE
OPENING`. *Port name very long:* H1 wraps to two lines and §6.1's
two-line rule applies.

#### 6.11 v2 — Accessibility spec

One `<h1>`; the figure row is a `<dl>` in disguise — a real
description list, term and figure paired, so AT reads `Opening tide:
low water 1.1 metres, 08:05`. The hero contains the page's first
focusable element (the index) only after the heading in DOM order.

#### 6.11 v2 — Tokens consumed

`--harbour`, `--ink`, `--glass-deep`, `--ease-swell`, `--dur-surface`
(1600ms), `--watchdog` (1000ms).

### 6.12 The booking entry (page family: conversion form)

- **What & why.** Conversion in a logbook is an entry written by the
  visitor: the booking form is ruled like the page it closes — fields
  as ledger columns (name, party, sailing), its submit the one buoy
  (§6.9), its confirmation a stamped entry with a number. It belongs
  because a booking *is* the day's most consequential entry, and the
  theme treats it with the book's full ceremony: written in, checked
  against the table, sealed by the office.
- **Structure.** A `<form>` ruled as a ledger page: each field a
  column with a brass head rule, label in apparatus mono above, input
  as a ruled writing line (transparent ground, 1.5px `--ink` bottom
  rule, Source Serif 18px input text). The sailing field is a select
  styled as a table excerpt — its options are the day's real sailings
  with their tide states (`14:20 · HW 4.7 m · PLACES OPEN`). The party
  size is a stepper drawn as tally marks. Submit: §6.9's buoy, full
  form width on phone. On success the form is replaced by its
  confirmation entry: entry number, the booking's facts in mono, and
  the harbourmaster's seal (§6.8's SVG at 64px) struck at its foot.
- **Motion spec.** Field focus: the field's rule thickens to 2.5px
  and a `--glass` wash fills the column from its head rule down
  (200ms `--ease-drift`) — the column being written in is the wet
  one. Error: the rule turns `--buoy-deep` (the theme's only other
  use of the buoy family — a warning is a buoy's cousin, and the gate
  counts it as the same single object's family, never a second
  orange element competing for attention; where a build cannot
  accept even this, errors fall back to `--brass-deep` with a double
  rule) and the error note prints beneath in Caslon italic, the
  harbourmaster's hand (§12 voice). Submit press: the buoy dips
  (§6.9); on success the confirmation entry floods in (§6.3, 700ms)
  and the seal strikes at its foot (§6.5 timing).
- **States.** *Rest:* ruled, empty, the buoy moored beneath. *Focus:*
  column wet, rule thick. *Error:* rule in warning colour, note in
  the hand, the visitor's text untouched — a form in this theme
  never eats what was written in it, even on a server 500 (the
  values persist in the DOM and are re-presented). *Submitting:* the
  buoy holds its dip and its label reads `ENTERING…` in mono;
  a submission longer than 3s releases the buoy and prints the note
  `— the office is slow today; your entry is kept above` with the
  values intact. *Success:* the confirmation entry, sealed.
- **Content merge.** The form's sailings are §6.13's tides joined
  with the operator's real departures; its confirmation number is
  the next entry number in the day's book (`No. 214` continues the
  sequence the index began). Nothing in the form is a generic
  checkout pattern wearing a costume.
- **Failure fallback.** A plain working form: labels, inputs, submit
  — the ruling is CSS. No-JS: standard form post. A failed sailing
  option (sold out) prints struck through with `FULL AT THIS TIDE`
  — visible, honest, unselectable.
- **Reduced-motion variant.** No wash travel (column wets instantly),
  no flood on confirmation (it prints), seal by step. All states and
  texts identical.
- **Performance budget & mobile variant.** CSS transitions + one
  flood; negligible. Mobile: single column, fields full width, the
  buoy full width (§6.9), error notes beneath their fields at 16px
  italic (never smaller — an apology you cannot read is not one).

#### 6.12 v2 — Choreography timeline

| Beat | Time | What happens |
|---|---|---|
| 1 | Focus + 0ms | Field rule thickens; wash begins down the column |
| 2 | Focus + 200ms | Column wet; the writing line is the attended line |
| 3 | Submit + 0ms | Buoy dips (§6.9 beat 5); label to `ENTERING…` |
| 4 | Success + 0ms | Form retires; confirmation entry begins flooding (700ms) |
| 5 | Success + 700ms | Entry printed; seal strikes at its foot (200ms press) |
| 6 | Error + 0ms | Offending rule turns; note prints in the hand; focus moves to the first error |

#### 6.12 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Ruled empty form | Same, single column |
| Focus | Wash + thick rule | Same |
| Error | Warning rule + italic note, text preserved | Same |
| Submitting | Buoy dipped, `ENTERING…` | Same |
| Success | Confirmation entry, sealed | Same |
| Disabled (no sailings) | Form replaced by the closed entry (§6.17) | Same |
| No-JS | Plain form post | Same |

#### 6.12 v2 — Breakpoint behaviour

≥1200px: two-column ruled form (fields paired as ledger columns).
768–1199px: two columns narrow, sailing select full width. <768px:
single column; tally stepper becomes a select (tally marks need
width to be read as tallies).

#### 6.12 v2 — Edge cases & failure modes

*The chosen sailing's tide passes while the form is open:* on
submit, the office answers with the note `— that tide has gone;
the next is 18:40` and re-presents the form with the next sailing
selected — never a silent substitution. *Party larger than the
boat:* the error is the harbourmaster's arithmetic, stated plainly
(`— the boat takes 12; your party is 14`). *Duplicate submission:*
the confirmation's entry number is idempotent — a double press
returns the same `No. 214`, because the book has one entry for one
booking.

#### 6.12 v2 — Accessibility spec

Real labels, `aria-describedby` for notes, errors announced via a
polite live region *and* printed (the note is the announcement's
text). Focus moves to the first error on submit-failure and to the
confirmation heading on success. The buoy's accessible name includes
the sailing (§6.9). All inputs ≥ 44px tall on touch; the tally
stepper's buttons are real buttons with text names (`one more`,
`one fewer`).

#### 6.12 v2 — Tokens consumed

`--ink`, `--brass`, `--glass`, `--buoy`, `--buoy-deep`,
`--ease-drift`, `--ease-press`, `--dur-flood` (900ms).

### 6.13 The closing ledger — tide table (page family: data table)

- **What & why.** The page closes with its evidence: the day's tide
  table, printed in full — every extremum with its time and height,
  the hourly interpolated heights between them, and the harbour hours
  beneath — the same table §6.2 plotted, §6.5 stamped from, and §6.6
  joined against. It belongs at the close because a logbook's tables
  are its back pages: the reader who has trusted the day's entries
  can now audit every figure in them, in the book's own hand. This
  table is the theme's source of truth, and every other element on
  the page is a view of it.
- **Structure.** A real `<table>`: columns `TIDE · TIME · HEIGHT ·
  OFFICE` (the fourth is §6.6's computed join, printed here in
  full). Extremum rows in Source Serif 600 with their heights in
  mono; hourly rows in mono at 55% ink (they are computed, and the
  book says so — a footnote under the table reads `Hourly heights by
  the rule of twelfths from the observed extrema.`). The source line
  closes the table: the port, the datum (`Heights above Chart
  Datum`), and the table's origin as supplied by the build's real
  data. Beneath it, the harbour hours as a second small table.
- **Motion spec.** The table floods in as an entry (§6.3). Extremum
  rows stamp their heights with §6.18's counters as they enter —
  the one place counting is allowed to be seen twice, because here
  the numbers are being *entered into evidence*. Row hover is §6.7.
  Nothing else moves: tables in a logbook are read, not performed.
- **States.** *Rest:* printed in full. *Hover:* wet-ink rows.
  *Focus:* rows are not focusable except a row that links (to the
  booking entry, §6.6's rule) — wash + ring. *Scrolled-past:*
  printed.
- **Content merge.** Total: the table is not a view of the content;
  it is the content every other element viewed. Its footnote and
  source line are part of the table, not captions about it.
- **Failure fallback.** The table is server-rendered HTML; there is
  no state in which the page's evidence depends on a script. If the
  build's data source fails, the table prints the last verified
  day's table with its date corrected and a note in the hand —
  `— yesterday's table; today's not yet received` — a dated truth,
  never an undated guess.
- **Reduced-motion variant.** Printed; counters land instantly
  (§6.18's variant). 
- **Performance budget & mobile variant.** Static table; negligible.
  Mobile: the table keeps all four columns at mono 12.5px (a tide
  table that drops its heights column to fit a phone has stopped
  being a tide table); horizontal scroll is forbidden — the columns
  are sized to fit 360px by the apparatus abbreviations (`HW`, `LW`,
  heights to one decimal).

#### 6.13 v2 — Choreography timeline

Entry trigger → table floods 900ms (§6.3 beats) → as each extremum
row clears the waterline, its height counter runs (§6.18: 800ms,
landing exact) → footnote and source line print with the table's
foot → the closing totals in the footer (§6.14) become countable,
because their source now exists on the page.

#### 6.13 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed table | Printed, mono 12.5px |
| Hover (row) | Wet-ink wash | n/a |
| Focus (linked row) | Wash + ring | Same |
| Scrolled-past | Printed | Printed |
| Disabled / no-JS | Printed (server-rendered) | Printed |

#### 6.13 v2 — Breakpoint behaviour

≥1200px: full table in the entry column + data margin width.
768–1199px: full table, hourly rows collapsible behind a `HOURLY
HEIGHTS` disclosure (they are derived; the extrema are the evidence).
<768px: extrema + office columns always; hourly rows behind the
disclosure; abbreviations per spec above.

#### 6.13 v2 — Edge cases & failure modes

*A day with three extrema (a short tidal day):* the table prints
three; the curve (§6.2) plots three; no fourth is implied. *Heights
that tie (a stand):* both rows print with `STAND` in the office
column's place for the hour between. *Datum change between data
supplies:* the source line names the datum per table; two tables on
one page with different datums is a build error the gate rejects —
figures that cannot be compared must not share a page.

#### 6.13 v2 — Accessibility spec

A real table with `<caption>` (`Tides for the port, [date], heights
above Chart Datum`), scoped headers, and the footnote as a
`tfoot`-adjacent paragraph referenced by `aria-describedby`. This
table is the accessible original of §6.2's chart and §6.5's stamps;
its completeness is an accessibility requirement, not a courtesy.

#### 6.13 v2 — Tokens consumed

`--ink`, `--brass`, `--glass-deep`, `--ease-swell`, `--dur-flood`
(900ms), `--row-rest-ink` (55%).

### 6.14 Ledger closed (page family: footer)

- **What & why.** The footer is the foot of the day's page: a closing
  rule, the day's totals counted from the page itself, the office's
  standing information, and the harbourmaster's signature flourish —
  the line a logbook day ends with. It belongs because a ledger does
  not trail off into a sitemap; it *closes*, and its closing is a
  small ceremony of account: what came in, what went out, who kept
  the book.
- **Structure.** A `--harbour` ground block (the office's dark wood
  desk the book rests on at night): the closing rule drawn in
  `--brass`; the day's totals in mono (`ENTRIES 9 · SEALED 4 ·
  HIGHEST WATER 4.7 m · 14:20`) — each counted or read from the DOM
  and the table, never typed by hand; standing office information
  (address, the office's own hours summary, the port's name) in
  paper-coloured text; and the signature — an SVG flourish in
  Caslon-italic style drawn at the foot, the harbourmaster's name as
  the site supplies it. Links are ledger rows (§6.7 grammar, paper
  ink).
- **Motion spec.** On entry: the closing rule draws left→right,
  800ms `--ease-draw`; the totals count (§6.18) as they enter; the
  signature flourish draws last, 900ms, stroke by stroke — the day
  is signed after it is totalled, never before. The margin curve
  (§6.2) ends at the footer's top edge, its final height the day's
  closing height.
- **States.** *Rest:* printed, signed. *Hover:* rows wash (paper-ink
  variant). *Focus:* rows ring in `--brass`. *Scrolled-past:* the
  foot of the book; nothing follows it but the night scheme's dark.
- **Content merge.** The totals are the page's own account of itself —
  entries counted from the DOM, sealed counted from §6.8's states,
  highest water read from §6.13's table. A footer total that
  disagrees with the page above it is a §10 gate failure, because in
  a ledger a wrong total is not a typo, it is a false account.
- **Failure fallback.** Printed footer, totals as server-computed
  values (the build counts its own entries), signature as a static
  SVG. No-JS loses only the draw.
- **Reduced-motion variant.** Rule and signature printed; totals land
  instantly.
- **Performance budget & mobile variant.** Two stroke draws + counters;
  negligible. Mobile: totals wrap to two lines mono 12.5px; the
  signature scales to 60% width; office information stacks.

#### 6.14 v2 — Choreography timeline

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Footer enters; closing rule begins drawing (800ms) |
| 2 | t₀ + 300ms | Totals begin counting (§6.18) as the rule passes them |
| 3 | t₀ + 900ms | Totals landed, exact |
| 4 | t₀ + 1000ms | Signature flourish draws (900ms), stroke by stroke |
| 5 | t₀ + 1900ms | The day is signed; the page is closed |

#### 6.14 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed, signed | Same |
| Hover (row) | Paper-ink wash | n/a |
| Focus | Wash + brass ring | Same |
| Scrolled-past | Closed | Closed |
| Disabled / no-JS | Printed, server totals | Same |

#### 6.14 v2 — Breakpoint behaviour

≥1200px: full spec. 768–1199px: totals on one line at 13px.
<768px: totals two lines, signature 60%, office block stacked, rule
draw 600ms.

#### 6.14 v2 — Edge cases & failure modes

*A day with nothing sealed:* the total reads `SEALED 0` — a true
zero, printed; a build that omits a zero total to look busier has
falsified the account. *Highest water tied across two tides:* both
times print. *The signature name absent (an unnamed office):* the
flourish draws and the name line reads the office's title (`The
Harbour Office`) — the day is signed by the office, if not by the
man.

#### 6.14 v2 — Accessibility spec

Footer landmarks and headings are real (`<footer>`, visually-ruled
headings in the DOM). Paper on `--harbour` is 10.64:1. The signature
SVG is `aria-hidden` beside its text name. Totals are text, read in
order.

#### 6.14 v2 — Tokens consumed

`--harbour`, `--paper`, `--brass`, `--ease-draw`, `--dur-rule`
(800ms), `--dur-sign` (900ms).

### 6.15 Porthole frames (page family: images)

- **What & why.** Photographs in the harbour office hang in brass
  portholes, and the page's images do the same: circular frames with
  a real brass rim (a double ring with four bolt heads), the image
  inside under a faint sea-glass sheen, the whole frame moored in the
  data margin where it bobs on §6.4's sine. It belongs because it is
  the theme's only image treatment and it is total: there are no
  rectangular photographs in this world, because the office has no
  rectangular frames — the round window is how this harbour looks at
  everything, including its own pictures.
- **Structure.** A `<figure class="porthole">`: outer rim (border
  6px `--brass` with an inset shadow ring), four bolt dots at the
  diagonals (pseudo-elements), the image clipped to the inner circle,
  a sheen layer (a `--glass` radial at 12%, top-left) above the image
  at `pointer-events: none`, and the caption beneath in apparatus
  mono — caption as log entry (`THE MORNING BOAT, FROM THE OFFICE
  WINDOW · HW 09:40`). The figure sits in a §6.4 bobbing wrapper.
  Diameter 180–320px per §4's ration.
- **Motion spec.** The bob (§6.4). On entry, the porthole floods with
  its entry (§6.3) — no separate reveal. Hover: the sheen brightens
  12% → 20% and drifts 8px toward the pointer's side over 400ms
  `--ease-drift` — light on glass, nothing more; the image itself
  never scales (a photograph in a frame does not grow; §5's refusal
  of image zoom for this theme is recorded here). Focus (where the
  figure links): sheen at 20% + focus ring on the rim.
- **States.** *Rest:* framed, bobbing gently. *Hover:* sheen lit.
  *Scrolled-past:* bob frozen at exit phase. *Missing image:* the
  porthole shows `--paper-deep` with the caption and a line in the
  hand — `— the glass is out being cleaned` — a frame awaiting its
  photograph, never a broken-image icon in a brass rim.
- **Content merge.** The caption is an entry about the photograph,
  timed to a tide like everything else in the book; the frame's bolts
  and rim are the office's furniture applied to the site's real
  images. An image that is itself evidence (a chart, a document)
  must not be portholed — §7 rules those pages out or frames them
  rectangular by exception, because evidence is not hung as décor.
- **Failure fallback.** The figure prints framed and static; the
  sheen is an enhancement layer whose absence changes nothing.
- **Reduced-motion variant.** No bob; sheen static at 12%; hover
  brightening becomes instant.
- **Performance budget & mobile variant.** Sheen is one gradient
  layer; bob per §6.4's caps. Mobile: portholes centre above their
  entry, diameter = min(240px, 72vw), bolts kept (they are 6px of
  charm at any size).

#### 6.15 v2 — Choreography timeline

With its entry: floods (§6.3 beats) → bob takes up the scroll sine
from the entry's completion → hover: sheen drifts and brightens over
400ms → leave: sheen settles back over 550ms (the §6.7 asymmetry —
light leaves glass slower than it arrives).

#### 6.15 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Framed, bobbing ±5px | Framed, bobbing ±3px, centred |
| Hover | Sheen 20%, drifted to pointer side | n/a |
| Focus (linked) | Sheen 20% + rim ring | Same |
| Scrolled-past | Bob frozen | Same |
| Missing image | Paper-deep glass + hand note | Same |
| Disabled / no-JS | Framed, static | Same |

#### 6.15 v2 — Breakpoint behaviour

≥1200px: in the data margin, 180–320px. 768–1199px: margin or above
entry, ≤ 260px. <768px: centred above the entry, min(240px, 72vw),
caption centred beneath.

#### 6.15 v2 — Edge cases & failure modes

*Portrait-orientation image in a round frame:* the crop is set at
build with `object-position` per image and recorded in the caption's
data — a porthole crop that cuts a face is a build error, caught by
eye at the gate. *Very small source image:* below 360px wide the
porthole is not used; the entry prints without a photograph rather
than upscaling into blur behind glass. *Caption without a tide:* the
caption's tide is the entry's stamp tide — never a second, different
figure (§1).

#### 6.15 v2 — Accessibility spec

Real `alt` on every image, written as the office would describe the
photograph; the rim, bolts and sheen are decorative layers
(`aria-hidden` where separate). The caption is a real `<figcaption>`.
Focus ring on the rim at 2px `--brass-deep`, offset outside the brass
so it reads against paper.

#### 6.15 v2 — Tokens consumed

`--brass`, `--glass`, `--paper-deep`, `--glass-deep`, `--ease-bob`,
`--ease-drift`, `--bob-amp` (5px).

---

### 6.16 Waterline transition & unruled skeleton (page family: loader / transition)

- **What & why.** Leaving a page in this theme, the water rises over
  it and falls on the next: a full-viewport waterline sweep, the
  meniscus crossing once, 500ms — because the whole book is kept at
  the harbour and its pages turn under water. And a page not yet
  written shows its *ruling*: the unruled skeleton — the entry's
  number, its brass rules, and empty ruled lines where the writing
  will go. A logbook page is never blank; it is ruled and awaiting
  entries, and the skeleton says exactly that.
- **Structure.** *Transition:* a fixed `.waterline-veil` (the
  `--waterline` band grown to full height, `--brass` meniscus at its
  leading edge) parked below the viewport; on an intercepted internal
  navigation it rises to cover (250ms `--ease-swell`), the route
  swaps at full cover, and the veil falls away on the new page
  (250ms). *Skeleton:* the entry markup rendered with `.is-unwritten`:
  head rule and entry number real, prose lines as `--paper-deep`
  ruled bars at the prose's own line-height (29.16px pitch — the
  skeleton respects the ruling), porthole as an empty rim.
- **Motion spec.** Transition 500ms total as above; browser
  back/forward is never intercepted. Skeleton: unwritten entries
  resolve by flooding (§6.3) as their content lands; a hard cap of
  1200ms — any entry still unwritten at 1200ms has its bars replaced
  by the printed note `— not yet written` in the hand, and receives
  its content plainly when it comes. No spinner exists in this theme,
  at any size, for any wait.
- **States.** *Veil:* idle (parked) → covering → covered (swap) →
  falling → idle. *Skeleton:* unwritten → resolving (flood) →
  written; unwritten → noted (1200ms cap) → written-plain.
  *Hover/focus:* links behave normally; the veil decorates only
  clicks it can intercept (modified clicks, new tabs, external links
  bypass it entirely).
- **Content merge.** The veil is the page's own water, risen; the
  skeleton is the entry's own ruling, unwritten. Neither imports a
  foreign loading idiom into the book.
- **Failure fallback.** No JS: ordinary navigation, server-rendered
  pages (skeletons exist only inside client fetches that own their
  watchdog). A navigation that stalls under the veil: at 2500ms the
  veil falls back and the browser's own load proceeds — the water
  never traps a reader in the harbour.
- **Reduced-motion variant.** No veil; instant navigation with the
  masthead's tide line flashing once (opacity step) to mark the new
  page. Skeleton bars are plain, resolving without flood.
- **Performance budget & mobile variant.** One fixed layer, one
  transform. Mobile: veil 420ms; skeleton bars at the phone's prose
  pitch.

#### 6.16 v2 — Choreography timeline

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Internal link activated; veil begins rising, meniscus leading |
| 2 | t₀ + 250ms | Full cover; route swaps; new page at its opening |
| 3 | t₀ + 500ms | Veil fallen; new page's opening (§6.11) already printed beneath it |
| 4 | t₀ + 2500ms | Abort deadline: a veil still covering falls back and native load proceeds |

#### 6.16 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Idle | Veil parked below viewport | Same |
| Covering | 250ms rise | 210ms rise |
| Covered | Route swap, scroll to opening | Same |
| Falling | 250ms fall | 210ms fall |
| Skeleton | Ruled bars at prose pitch | Same |
| Disabled / no-JS | Plain navigation; no skeletons | Same |

#### 6.16 v2 — Breakpoint behaviour

≥1200px: veil 500ms. 768–1199px: 460ms. <768px: 420ms, meniscus 1.5px.
Skeleton pitch follows each breakpoint's prose leading.

#### 6.16 v2 — Edge cases & failure modes

*Same-page anchors:* no veil — anchors scroll (§6.10's strip tracks
them). *A page that is mostly skeleton on arrival (slow data):* the
1200ms cap converts bars to `— not yet written` notes entry by entry;
the page reads as an honest, partly-written day, never as a spinner
farm. *Prefetched route:* the veil still runs its 500ms — the ritual
is the transition, not the wait.

#### 6.16 v2 — Accessibility spec

During the veil, the outgoing page is `inert`; on cover, focus moves
to the new page's `<h1>` (tabindex −1) with a polite announcement
`Turned to: [page]`. Skeleton regions carry `aria-busy="true"` until
written, announced once per page (`Part of the day is still being
written`), not per entry.

#### 6.16 v2 — Tokens consumed

`--waterline`, `--brass`, `--paper-deep`, `--ease-swell`,
`--dur-veil` (500ms), `--cap-unwritten` (1200ms).

### 6.17 The closed harbour (page family: empty state / 404)

- **What & why.** An empty day and a missing page are harbour facts,
  and the theme states them as such: the empty state is a page of the
  log ruled and headed, with one entry in the hand — `— no sailings
  today; the water is low and the office is shut` — and the 404 is
  an entry for a page the book does not contain: `This page is not
  in the ledger.` It belongs because a theme is judged at its edges:
  the day nothing happened is still a day in the book, kept with the
  same ruling.
- **Structure.** The standard page frame (masthead, rail, rules) with
  a single entry: its stamp (§6.5) reads the true state (`LW 1.1 m ·
  ALL DAY` for a low-water closure, or `NOT ENTERED` for the 404),
  the hand's note as the entry's prose, and the index (§6.10) offered
  as the way back into the book. The margin curve plots the day as
  usual — for the 404 it plots *today's* real curve, because the
  harbour exists even where the page does not.
- **Motion spec.** The entry floods (§6.3) and its stamp strikes —
  the full ceremony, deliberately: an empty page given the book's
  full honours reads as honesty, where a bare centred message would
  read as an error page wearing a costume. Nothing else moves.
- **States.** *Rest:* the closed entry, printed. *Hover/focus:* the
  index rows behave per §6.10. There is no retry button, no search
  box dressed as a chart — the way back is the index, as it is in
  the book.
- **Content merge.** The state's facts are real (today's actual low
  water, the actual absence of the page) and its furniture is the
  page's own. Remove the harbour and the state has nothing to say —
  which is the test every element here must pass.
- **Failure fallback.** This *is* the fallback, and it is static by
  construction.
- **Reduced-motion variant.** Printed; stamp by step.
- **Performance budget & mobile variant.** One entry; negligible.
  Mobile: the hand's note at 17px italic, never truncated — a closed
  harbour's notice is read whole or not at all.

#### 6.17 v2 — Choreography timeline

Page load → frame prints → the single entry floods (700ms at its
size) → stamp strikes (200ms) → stillness. The stillness is the
content: after the stamp, nothing on the page moves except the
curve's undulation, which on this page is also stilled (§6.2's
variant below) — a shut harbour's water, at slack, does not perform.

#### 6.17 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | Closed entry printed, curve at slack | Same |
| Hover (index row) | Wash + tick | n/a |
| Focus | Wash + tick + ring | Same |
| Scrolled-past | n/a — the page is one entry | Same |
| Disabled / no-JS | Printed | Printed |

#### 6.17 v2 — Breakpoint behaviour

All breakpoints identical in structure; <768px the entry's stamp
sits beneath its title per §6.5's mobile rule, and the curve strip
shows the day's low-water flat line.

#### 6.17 v2 — Edge cases & failure modes

*A search result promised content that was removed:* the 404 entry's
note names the removal plainly when the build knows it (`— the
Thursday sailing was withdrawn on 12 November`) — a dated fact, in
the hand. *The harbour is closed but bookings exist for tomorrow:*
the booking entry (§6.12) still appears below, for tomorrow's tide —
closed today is not closed for ever, and the page must not say it is.

#### 6.17 v2 — Accessibility spec

The 404 carries a real `<h1>` (`This page is not in the ledger`) and
the index as its recovery path; the empty state announces its fact
in its heading, not in a toast. Contrast and focus per the standing
rules.

#### 6.17 v2 — Tokens consumed

`--ink`, `--glass-deep`, `--brass-deep`, `--ease-swell`,
`--stamp-tilt` (−3°).

### 6.18 Counting to value (page family: data counters)

- **What & why.** The original entry's ambient promise — "tide
  heights and catch weights count to value" — kept and disciplined:
  figures in the data margin and the closing tables count from the
  last true value (or from zero where zero is a true start) to the
  figure the record holds, landing *exactly* on it, in tabular mono.
  It belongs because in a logbook a number is written digit by digit
  by a hand that knows where it will end; the count is that writing,
  performed once, at the speed of a careful pen — and a count that
  lands anywhere but the printed figure is a mis-entry.
- **Structure.** Any `.count` figure carries `data-to` (the true
  value, with its unit outside the counting span) and `data-from`
  (default the previous printed value for that figure, else 0). The
  shared loop animates the textContent in mono tabular figures over
  800ms with `--ease-drift`, formatting to the figure's own precision
  (heights 1 decimal, weights integers, counts integers). The DOM
  ships with the final value as the text; JS rewinds to `data-from`
  only for figures below the fold that it will actually count.
- **Motion spec.** Trigger: the figure's entry floods (§6.3) or the
  figure crosses 60% viewport height. Duration 800ms; heights count
  in 0.1 m steps (the pen writes tenths, not thousandths — the count
  is quantised to the figure's precision, so it reads as entries
  being made, not as a slot machine). A figure whose value changes
  while counted (a live catch total) re-counts from its current
  displayed value to the new true value over 500ms — the book is
  corrected by writing the new figure, never by erasing to zero.
- **States.** *Rest:* the true figure, printed. *Counting:* 800ms of
  quantised steps. *Scrolled-past:* landed, permanent. *Hover:* none.
  *Focus:* a focused figure (where focusable) shows its final value
  instantly — no one reads a number that is still travelling.
- **Content merge.** The figures counted are the page's own data —
  the table's heights (§6.13), the day's catch weights in their
  entry, the footer's totals (§6.14) — and `data-to` is generated
  from the same record as the printed text, so the count and the
  print cannot disagree. A figure important enough to count is
  important enough to be true (§1).
- **Failure fallback.** The DOM's text *is* the final figure; no-JS
  and loop-failure both leave the truth standing. A count interrupted
  (tab hidden) lands on the true value on return.
- **Reduced-motion variant.** No count: figures stand at their true
  values from first paint. The original entry's spirit — numbers as
  facts, not effects — is most itself here.
- **Performance budget & mobile variant.** ≤ 6 figures counting
  concurrently, textContent writes throttled to 30Hz; ≤ 0.2ms/frame.
  Mobile: duration 650ms, concurrency 4.

#### 6.18 v2 — Choreography timeline

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Entry flooded / figure at 60% vh: count begins from `data-from` |
| 2 | t₀ + 0–800ms | Quantised steps at the figure's precision, `--ease-drift` |
| 3 | t₀ + 800ms | Lands exactly on `data-to`; the printed figure and the counted figure are one |
| 4 | Value change | Re-count from displayed value, 500ms, to the new true figure |

#### 6.18 v2 — State matrix

| State | Desktop | Touch |
|---|---|---|
| Rest | True figure printed | Same |
| Counting | 800ms quantised count | 650ms |
| Hover | No change | n/a |
| Focus | Final value instantly | Same |
| Scrolled-past | Landed, permanent | Same |
| Disabled / no-JS | True figure printed | Same |

#### 6.18 v2 — Breakpoint behaviour

≥1200px: 800ms, cap 6. 768–1199px: 750ms, cap 5. <768px: 650ms, cap
4; figures in the closing table count only their extrema (§6.13),
hourly rows print directly — a phone's table is evidence, not theatre.

#### 6.18 v2 — Edge cases & failure modes

*A figure of zero:* counts to 0 by standing at 0 — the book prints a
true zero without ceremony (§6.14's rule). *Negative values (a
falling total):* count downward with the same quantisation; the
minus sign is part of the figure from the first frame, never appears
mid-count. *Very large weights (a 12,400 kg catch):* thousands
separators are present in every intermediate value, formatted by the
same formatter as the final print — a count that changes its own
formatting mid-run is a §9 failure.

#### 6.18 v2 — Accessibility spec

Counting figures are `aria-hidden` during the count with the final
value present in a visually-hidden twin — AT reads the truth once,
not forty intermediate tenths. At rest the twin is removed and the
figure is ordinary text. The count is never the only carrier of a
value: every counted figure also exists in §6.13's table or its
entry's prose.

#### 6.18 v2 — Tokens consumed

`--ink`, `--ease-drift`, `--dur-count` (800ms), `--count-cap` (6).

---

## 7. Page application map

| Page type | How the theme plays out |
|---|---|
| **Home (the day's page)** | The full instrument: opening of the log (§6.11), the day's entries in tidal order each flooded and stamped (§6.3, §6.5), the pinned hours (§6.6), the closing ledger (§6.13), the booking entry (§6.12), ledger closed (§6.14). The curve runs the whole page. |
| **Listing (sailings / catches / berths)** | Entries are the listed things, ordered by their tide, not by price or alphabet — the book's order is the water's order, and a sort control, if the host insists on one, is printed as an office note (`The office lists by tide; ask at the desk for otherwise.`) rather than pretending the book re-sorts itself. Each row is a ledger row (§6.7) with its stamp; sealing (§6.8) marks the office's processed items where the listing is a working list. |
| **Detail (one sailing / one catch / one berth)** | A single long entry: its stamp is the subject's own tide; its porthole (§6.15) is the subject's photograph; its figures count (§6.18); the booking entry (§6.12) follows with the subject pre-selected. The curve still plots the whole day — a detail page is one line of the book, read closely, not a page torn out. |
| **About (the harbour / the office)** | The book kept over years: entries are the harbour's history, each stamped with its *historical* tide where the record holds one (a founding stamped with the tide of its day, from the archive's table — real or omitted, never reconstructed). Portholes rationed to one per era. |
| **Timetable / reference** | §6.13 promoted to the whole page: the tables *are* the content, entries reduced to the table's own sections. The curve plots the table's full range (a week, a season) with the map re-declared in the table's source line. No booking entry — a reference page in this theme does not sell; its footer carries the office's note directing the reader to the day's page. |
| **Contact (the office)** | The harbour hours (§6.6) unpinned and complete, the office's address as an entry, and a message form ruled as §6.12's form but ending in a note, not a seal: a message is correspondence, and correspondence is acknowledged, not approved (`— received at the office; expect an answer by the next tide but one`). |
| **404 / empty** | §6.17, exactly as specced — the closed harbour, the unentered page. |

---

## 8. Worked examples

### 8.1 The hero — a ferry operator's opening (end-to-end)

*Build:* "Harbourlight Ferries", Friday. Masthead (§6.10): port name
in Caslon small caps, `FRIDAY · 14 NOVEMBER` in mono, the live tide
line at right reading `TIDE 2.8 m · MAKING` (it is 06:40; LW was
1.1 m at 05:52, HW 4.7 m at 12:05 — the day's printed table, §6.13).
The H1 — `HARBOURLIGHT` over `The day's crossings` — surfaces per
§6.1: line draws 700ms, waterline climbs 1600ms, letters bob as they
break. The standfirst: *A fair day on the water. Three crossings
before high water, and the office open from seven.* The figure row:
`OPENING TIDE LW 1.1 m · 05:52 · WIND NW 12 KT · FIRST SAILING 07:30 ·
HW 4.7 m`. The opening stamp strikes at the row's end: `LW 1.1 m ·
05:52` with the remark `— the early boat goes on the ebb`.

*Scroll timeline:* 0–15% — the curve's brass fill stands at the
opening height; the first entry (the morning crossing) floods at 82%
vh. 15–40% — entries 1–3 read; stamps strike as each flood settles;
the fill climbs the curve's morning rise by the rule of twelfths.
The visitor has not been shown a single number that is not in the
table at the page's foot.

### 8.2 Mid-page — the day's catch (end-to-end)

*Build:* a fish market's entry, `No. 5 — THE MORNING CATCH`, stamped
`3.9 m · MAKING` as it floods. In the data margin: the catch's
porthole (§6.15, the boat at the quay, caption `THE MORNING BOAT,
FROM THE OFFICE WINDOW · HW 09:40` — the entry's own tide, per §6.15's
law), and the catch figures as a small ruled table: species, weight,
price — weights counting to value (§6.18) as the entry settles:
`MACKEREL 212 kg`, `HAKE 86 kg`, `CRAB 41 kg`. Each row is a ledger
row (§6.7); the market's own working copy of the page lets the
fishmonger seal (§6.8) a row as it sells out, and the sealed row's
weight cell prints `— GONE AT 3.9 m` in the hand: the catch's record
keeps the tide at which it went.

*Scroll timeline:* entry floods 900ms → stamp strikes 200ms →
porthole takes up its bob → weights count 800ms, staggered 90ms in
table order → the reader is reading prices while the last weight
lands. Total ceremony after first visibility: ≈ 1.9s, none of it
blocking the text, which was readable from the flood's first 200ms.

### 8.3 Conversion — booking the crossing (end-to-end)

*Build:* §6.12's form at the day's close. Sailing select lists the
day's remaining crossings with their tides: `14:20 · HW 4.7 m ·
PLACES OPEN`, `16:05 · 4.1 m · FALLING · PLACES OPEN`, `18:40 · LW
1.3 m · LAST CROSSING`. The visitor picks 14:20, party of four (tally
stepper), name on the ruled line. Focus wets each column in turn.
Submit: the buoy — the page's only orange object, labelled `BOOK THE
CROSSING` with `FRI 14:20 · HW 4.7 m` beneath — dips; the office
answers; the form retires and the confirmation entry floods in:
`ENTRY No. 214 — FOUR PERSONS · HARBOURLIGHT · FRI 14:20 · HW 4.7 m ·
£46.00`, sealed at its foot by §6.8's seal, with the hand's line
beneath: `— be at the quay by 14:00; the boat does not wait for the
tide, and the tide does not wait for you.`

*Failure path, worked:* the same form submitted at 14:21 for the
14:20 boat returns the §6.12 note — `— that tide has gone; the next
is 16:05` — with 16:05 pre-selected and every other field exactly as
the visitor left it.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **An invented tide.** A stamp, curve or counter showing a height
   that is not in the printed table or derivable from it by the rule
   of twelfths. *Cure:* the law (§1); one `tideAt()`; the gate's
   three-point audit (§10). This is the theme's capital offence.
2. **A second orange thing.** A sale badge, an orange link hover, a
   "new" sticker. *Cure:* the buoy count at the gate; warnings use
   `--buoy-deep` inside the form only, everything else finds its
   colour in the four harbour anchors.
3. **Random stamp angles.** Stamps at −2°, −5°, −1° "for hand-made
   charm". One hand, one stamp, one angle: −3.0°. *Cure:* the
   `--stamp-tilt` token, no per-instance overrides.
4. **Everything bobbing.** Prose, tables and the footer riding the
   sine. Print is still; cargo floats. *Cure:* §6.4's grammar — only
   `.float` wrappers, never text blocks.
5. **A percentage progress bar** (or any second progress indicator)
   beside the curve. *Cure:* §6.2 is the only clock; remove the bar.
6. **Flood as a fade.** Entries cross-fading in with a rise of 10px —
   the generic reveal wearing a sou'wester. *Cure:* the flood is a
   waterline with a meniscus and a swell ease (§6.3), or the entry
   prints plainly; nothing between.
7. **Counters that slot-machine.** Figures rolling through random
   digits, or landing near the value. *Cure:* §6.18's quantised
   steps at the figure's own precision, landing exact, from the same
   record as the print.
8. **A remark on every stamp.** The harbourmaster's italic line under
   every entry until it reads as a design pattern. *Cure:* remarks
   are rationed (a minority of entries; §6.5) and each must be about
   *that* entry's tide.
9. **Portholes around evidence.** A chart, a timetable screenshot or
   a document cropped into a circle. *Cure:* §6.15's exception —
   evidence is framed rectangular or not at all; portholes are for
   photographs.
10. **Tide times without heights, heights without times.** Half-facts
    in mono. *Cure:* §3 law 2 — every sailing time carries its tide;
    the gate greps for bare times in data contexts.
11. **The pin that never releases, the flood that never finishes.**
    Apparatus left on a read page. *Cure:* the watchdogs (§6.3,
    §6.6) and the rule that finished animations remove their own
    machinery (clips, bands, masks) from the DOM.
12. **Generic empty states.** A cartoon boat and "Ahoy! Nothing
    here". *Cure:* §6.17 — the closed harbour, stated in the hand,
    with the day's real low water.

---

## 10. Quality gate

**Blocking — the build fails if any item fails:**

1. **Tide-truth audit.** Three scroll positions are chosen at random;
   the stamp, the rail head and `tideAt()` at each must agree with a
   hand computation from the printed table by the rule of twelfths,
   to 0.1 m. Any disagreement, any figure on the page not traceable
   to the table — fail.
2. **Buoy count.** Exactly one rendered element uses `--buoy` as a
   background. (Its own pressed/focus states in `--buoy-deep`, and
   §6.12's error rules, are the same object's family and are counted
   as such — a second *element* fails.)
3. **JS-off read.** With JavaScript disabled, the whole day reads:
   entries printed, stamps printed, tables complete, the curve
   static at mean level and labelled as such.
4. **Watchdog pass.** With the observer and loop artificially
   stalled, every entry, stamp and figure reaches its final state
   within its watchdog window (1000ms entries/stamps, 1200ms
   skeletons, 2400ms headline).
5. **Reduced-motion pass.** `prefers-reduced-motion` yields: no bob,
   no flood, no undulation, no tug; stamps and totals by step; all
   content and all figures identical.
6. **Stamp consistency.** All stamps at −3.0°; every stamp's values
   recomputed from the table match its print; moving an entry in a
   test build changes its stamp (the §6.5 test).
7. **Footer agreement.** The footer's totals equal a fresh count of
   the DOM (entries, sealed) and the table's maximum (highest
   water). 
8. **Focus survival.** Every focusable element is reachable and
   visibly ringed in every state — inside bobbing wrappers, pinned
   stages, and flooded entries alike; no focus ever lands in water
   (§6.3's instant-flood on focus fires).

**Standard — required, verified by inspection:**

9. Contrast spot-checks: body 13.11:1; stamp fact line 4.96:1;
    aligned-row rest ink ≥ AA at its size; buoy label at ≥ 18px bold.
10. The two ambient loops only: curve undulation, buoy sway. A third
    looping motion anywhere — fail this item and fix before ship.
11. Concurrency caps held: floods ≤ 2, bobbing floaters ≤ 8, counting
    figures ≤ 6 (measured on the heaviest page type).
12. Remarks ration: no more than one stamp in three carries the
    italic remark, and each remark names its own entry's water.
13. The datum and source line print under §6.13's table, and the
    hourly footnote names the rule of twelfths.

---

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Anything not listed is built from these; anything listed as refused
is refused with its replacement named.

| Component | Treatment in this theme |
|---|---|
| Primary button | The buoy (§6.9) — one per page, orange, pill. No second primary may exist. |
| Secondary button | A ruled entry line: mono label on a brass head rule, wash on hover (§6.7); reads as an index line that acts. |
| Text link | `--glass-deep`, underlined with the tide line's own stroke (a 1px wave rule via SVG background); hover deepens to `--ink`. |
| Form inputs | §6.12's ruled writing lines; focus wets the column. |
| Select | §6.12's table-excerpt select; options carry tide states. |
| Stepper | Tally-mark stepper (§6.12); buttons named in words for AT. |
| Checkbox / radio | Small brass squares / porthole dots; checked = filled with the seal's ring. |
| Table | §6.13's closing-ledger pattern: brass head rule, extremum rows strong, derived rows at 55% with the derivation footnoted. |
| Data row | The ledger row (§6.7): wet-ink hover, sealable where state allows (§6.8). |
| Card | **Refused as a floating card.** The theme's unit is the *entry*: ruled, numbered, stamped. A grid of lifted cards is another theme's furniture; listings here are entries in tidal order (§7). |
| Badge / tag | **Refused.** A fact about an entry goes in its stamp (§6.5) or its margin; there are no stickers in a logbook. |
| Alert / notice | An entry in the hand (Caslon italic) with a double brass rule — the office's note, pinned at the relevant entry, never a banner across the top of the book. |
| Toast | **Refused.** Nothing in a harbour pops up. Confirmations are entries (§6.12's sealed confirmation); transient states print in the margin note of the thing they concern. |
| Modal | **Refused.** A logbook has no overlays; a decision the visitor must make becomes an entry of its own (the booking entry pattern) or a page. |
| Tabs | **Refused.** Days are not tabs; a week is seven pages of the book, reached by the index (§6.10) and the leaf-turn (§6.16). |
| Accordion | The *folded entry*: a sub-entry whose prose is under a ruled head line that, on activation, floods open (§6.3 at 500ms). Used for the hourly rows (§6.13) and long office notes — the book folds, it does not stack panels. |
| Pagination | `THE NEXT DAY →` as a ledger line with tomorrow's first tide printed beside it; numbered page pills are refused — days have dates, not numbers. |
| Breadcrumbs | The entry's own heading path printed as an office line (`THE DAY'S PAGE · No. 5`) above the entry — position in the book, stated once, statically. |
| Progress | §6.2's curve only. Bars, percentages and step-dots are refused (§5). |
| Skeleton | §6.16's unruled lines. Spinners refused in all sizes. |
| Tooltip | **Refused.** An explanation becomes a margin note in the hand beside the thing it explains — the margin is this book's tooltip, and it is printed, not hovered into being. |
| Search | The index (§6.10) extended: a `FIND IN THE BOOK` line in the masthead opening the full entry index with a ruled input; results are index lines with their tides. |
| Date display | Always with its tide where a time is involved (§3 law 2); a bare date is permitted, a bare sailing time is not. |
| Price display | Mono, in the entry's data margin, with its unit and its basis (`£46.00 · FOUR PERSONS`) — a price in a ledger states what it is for. |
| Empty state | §6.17's closed harbour. |
| Error state | §6.12's hand-written note + warning rule; the visitor's input is never eaten. |
| Focus ring | 2px `--brass-deep` outline, offset 2px, on paper; 2px `--buoy-deep` on the buoy. One ring style per ground, everywhere. |

---

## 12. Content & copywriting voice

Two voices keep the book. **The Ledger** (mono apparatus + Source
Serif prose) writes facts: complete, dated, figured, unadorned. **The
Harbourmaster** (Caslon italic) writes judgement: remarks, notes,
errors, apologies — a person of few words who has seen every tide
twice. Nothing on the page speaks in a third voice; there is no
marketing voice in the harbour office.

**Headline style (the Ledger).** Names and facts, sentence case,
no exclamation, no adjective that the table cannot cash.
✓ `The morning catch, landed before high water`
✗ `Fresh-off-the-boat delights you won't believe!`

**Labels (apparatus mono).** Uppercase, tracked, factual:
✓ `FIRST SAILING 07:30 · HW 4.7 m` ✗ `DON'T MISS OUT!!`

**The Harbourmaster's remarks (stamps, margins).** Short, dry,
specific to the water at hand.
✓ `— the early boat goes on the ebb`
✓ `— a fair tide for the crossing`
✗ `— what a lovely day for it!` (loveliness is not recorded)

**Error voice (the Harbourmaster, correcting the entry).** States
what is wrong, in figures where figures exist, and what to do; never
blames the visitor; never loses their writing.
✓ `— the boat takes 12; your party is 14`
✓ `— that tide has gone; the next is 16:05`
✗ `Invalid input. Please try again.`

**Empty-state voice.**
✓ `— no sailings today; the water is low and the office is shut`
✗ `Ahoy! Nothing to see here, sailor!`

**Confirmation voice (the Ledger, sealed).**
✓ `ENTRY No. 214 — FOUR PERSONS · FRI 14:20 · HW 4.7 m`
✗ `Woohoo! You're all booked! 🎉`

**Fixed strings (verbatim, do not paraphrase):** the rail head's
states (`TIDE {h} m · MAKING` / `· FALLING` / `· SLACK`), the table's
footnote (`Hourly heights by the rule of twelfths from the observed
extrema.`), the datum line (`Heights above Chart Datum`), §6.17's
`This page is not in the ledger.`, and the footer's closing word —
the day's page ends with `— Ledger closed` and nothing after it but
the signature.

**Banned words:** *amazing, stunning, breathtaking, nestled, gem,
vibrant, world-class, seamless, effortless, simply* (as a softener),
and any use of *literally* the table cannot support. **Owned words:**
*making, falling, slack, stand, datum, entered, sealed, gone at*
(a thing that sold out at a tide), *by the next tide but one*.

---

## 13. Full-page scroll choreography map

The day's page (home), top to foot. Every beat is a function of
scroll position or of an entry trigger; nothing is timed to wall
clock except the two ambient loops.

| # | Beat | What the visitor sees and feels |
|---|---|---|
| 1 | Load | The tide line draws; the headline surfaces and bobs dry (§6.1, §6.11). The book opens. |
| 2 | Hero rest | Opening figures printed, opening stamp struck; the curve's fill at the opening height. The day is stated. |
| 3 | First scroll | The compact strip (§6.10) takes the masthead's place; the fill begins to climb the curve. Time starts moving. |
| 4 | Entry 1 | Flood rises over the morning entry; its stamp strikes as the water settles. |
| 5 | Entries 2–3 | Floods and stamps in tidal order; portholes bob in the margins; figures count as their entries settle. The day fills in. |
| 6 | Mid-page extremum | The fill touches HW on the curve; the brass dot brightens; the entry at the extremum is stamped `HW … · SLACK` if within the slack window. The top of the tide — the page's held breath. |
| 7 | The pinned hours | The office's hours pin; the day's tides scroll and ink beside them (§6.6). The visitor checks the join: open when the water is right. |
| 8 | Afternoon entries | Floods continue on the ebb; stamps now read `FALLING`; the fill descends the curve — the only progress indicator in the theme that is allowed to go down, because the water does. |
| 9 | The closing ledger | The tide table floods in; extremum heights count into evidence (§6.13, §6.18). The day's figures, auditable at last. |
| 10 | The booking entry | The form's columns wet as they are written; the buoy rides at its mooring below (§6.12, §6.9). |
| 11 | The close | The closing rule draws; the totals count; the signature signs (§6.14). The curve ends at the day's closing height. `— Ledger closed`. |

**Reverse pass.** Scrolling up: fills ebb (§6.2), pinned hours
re-pin and re-ink symmetrically (§6.6), but floods, stamps, seals
and counts never un-happen — the book does not unwriting itself.
The asymmetry is the theme's memory: water reverses; ink does not.

**Jump-scroll catch-up.** An anchor jump or a restored scroll
position lands with everything above already in its final state —
flooded, struck, counted — applied by the watchdog pass on the
first frame. A reader who teleports to the foot of the page finds a
written book, never a page of water.

---

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Total page weight (home, with fonts) | ≤ 780 KB (fonts ≤ 210 KB subsetted to Latin + figures; images in portholes ≤ 90 KB each, ≤ 4 per page) |
| JavaScript | ≤ 38 KB gzipped — one loop, one observer, `tideAt()`, the arming code; no framework |
| Shared-loop frame cost | ≤ 1.6 ms/frame total (curve 0.3, bob 0.3, parallax + rows 0.4, buoy 0.2, headroom 0.4) |
| Long tasks | None > 50 ms; the curve's path generation (≤ 400 points) runs at build or in idle time, never in the scroll path |
| Concurrent animation caps | Floods ≤ 2 · bobbing floaters ≤ 8 · counting figures ≤ 6 · stamps striking ≤ 1 |
| Layout shift | CLS 0 from all theme motion (transforms and clips only; every animated element's box is reserved) |

**Cut order when the budget is exceeded** (cut in this order, and
only in this order):
1. The buoy's time-based sway (its scroll bob stays — the buoy still
   rides the reader's water).
2. Parallax depths collapse from three to one (prose only).
3. The curve's undulation (the chart prints still; the fill stays).
4. Bob amplitude halves, then bob is cut for data-margin figures
   (portholes keep it longest — they are the theme's face).
5. Flood duration shortens 900 → 600ms.

**Never cut:** the fill of the curve (it is the progress and the
data), the stamps, the watchdogs, any figure's accuracy, the
reduced-motion variants. A build that ships the theme without its
watchdogs to save bytes has saved the wrong thing.

---

## 15. Build-order checklist

1. **The table first.** Build §6.13's closing ledger from the real
   data source; print its source and datum lines. Nothing else in
   the theme can be built truthfully until the table exists.
2. **`tideAt()` second.** Implement the rule of twelfths against the
   table; unit-test it at the extrema, at mid-rise (3 twelfths ≈
   half range at hour 3), and at one hand-computed hour, before any
   element consumes it.
3. **The static page.** Masthead, entries, stamps (server-computed),
   tables, form, footer — complete and readable with no JS and no
   animation. This is the page; everything after is weather.
4. **Tokens and ruling.** Palette (§2), type (§3), the rail/entry/
   margin grid and 9px rhythm (§4).
5. **The curve.** Plot §6.2 from the table; static mean-level state;
   then the fill in the shared loop; then the undulation.
6. **The loop.** Stand up the single rAF loop (lerp 0.12) and the
   IntersectionObserver; register flood (§6.3), bob (§6.4), parallax,
   pinned-hours inking (§6.6) as its clients — in that order, testing
   the frame budget after each.
7. **Stamps and seals.** §6.5's strike (with the server-print
   default), §6.8's seal with its persistence and failure note.
8. **The hero ceremony.** §6.1's surfacing and §6.11's assembly, with
   the session flag and the 2400ms watchdog.
9. **The instruments.** §6.6's computed office column verified
   against the hours by hand for one full day; §6.18's counters
   wired to the same records as their print.
10. **The buoy and the form.** §6.9 (count the orange), §6.12 with
    its error voice and its never-eat-the-input rule.
11. **Transitions and edges.** §6.16's veil and skeletons, §6.17's
    closed harbour, §6.14's closing ceremony with DOM-counted totals.
12. **Reduced-motion pass.** Every element's variant, verified as a
    set (§10 item 5).
13. **The gate.** §10 in full, in order, signed by someone who did
    not build the page — a harbourmaster does not audit his own log.

*— End of the expanded specification for theme #32, The Tidal Ledger.*
