# 72. Solar Weather Almanac — Expanded (v1 + v2)

Space weather reported like a 19th-century farmer's almanac: sunspots,
solar wind and aurora forecasts set in woodcut illustration and dense
almanac tables — the cosmos as daily practical wisdom. This expansion
preserves the theme's identity exactly: the same five palette anchors
(almanac paper `#F1E8D2`, woodcut black `#26221C`, aurora green
`#4C956C`, flare scarlet `#C0392B`, eclipse indigo `#2E4057`), the same
two type families (Playfair Display + Newsreader), the same ten
signature elements deepened — never redesigned — and eight page-family
elements added to complete the publication.

**The theme's one law: nothing is prophesied in the dress of the
observed.** Every figure on the page is one of two kinds and is set as
what it is: an *observation*, printed plain in the observed column, or
a *prognostication*, printed in the prophesied column and liable to the
errata slip. When a prophecy misses beyond its stated tolerance, the
miss is not corrected silently — it is marked in scarlet in the table
itself and confessed on the printed errata slip. The almanac's
authority comes from this honesty, and every element below either
prints an observation, marks a prophecy, or keeps the record straight.

**The Season Record (declared once, read everywhere).** All figures
in this theme trace to one record: the almanac's year of **365 days**
in **12 month plates** (31 · 28 · 31 · 30 · 31 · 30 · 31 · 31 · 30 ·
31 · 30 · 31). The worked "present day" of the examples is **Day 214
= 2 August** (cumulative days through July = 212). The August plate's
table (§6.6, §8.2) carries five rows with stated tolerances — sunspot
number ±10, radio flux ±5 sfu, solar wind ±25 km/s, greatest Kp exact,
aurora limit ±2° — of which three miss and are confessed: sunspot
prophesied 132 / observed **147**, wind prophesied 380 / observed
**412 km/s**, greatest Kp prophesied 5 / observed **4**; flux 168/171
and aurora 55°/55° agree within tolerance and carry no mark. The
season's errata tally therefore stands at **20** (17 through July + 3
upon the August plate), the subscriber roll at **1,213**, and the
Almanac's price at **$18 per annum, posted**. Any figure anywhere in
the theme that cannot be re-derived from this record does not ship.

## 1. Concept & world

The Solar Weather Almanac is a working space-weather publication —
daily sunspot numbers, solar wind speeds, Kp indices, aurora
forecasts — dressed and disciplined as a 19th-century farmer's
almanac. The dress is not nostalgia. The almanac form carries an
epistemology the modern dashboard lacks: it *prints* its predictions
in advance, in ink, where they cannot be quietly edited, and then it
prints what actually happened beside them, and then — this is the
part the theme exists for — it prints an errata slip confessing where
it was wrong. A live dashboard overwrites yesterday's forecast with
today's; the almanac cannot. Every page of the site is therefore a
leaf of a bound, dated, accountable volume.

The world of the theme is the printer's workshop as much as the
observatory. Paper is almanac paper, foxed at the edges. Illustrations
are woodcuts — cross-hatched, black, cut at reading speed. Type is
set, not rendered: Playfair Display for the almanac's public voice
(month names, titles, prognostication headings), Newsreader for its
working voice (tables, columns of figures, the small print of
tolerances and confessions). Colour is rationed like ink: black does
nearly all the work, aurora green is spent only where the aurora
itself is the subject, scarlet only where the record must confess or
a stamp must fall, eclipse indigo only where the sun is eclipsed —
the storm plate, the night of the forecast.

**Best-fit sites and audiences.** Space-weather services and aurora
forecast publications; observatories and astronomy societies
publishing daily solar reports; satellite operators and amateur radio
communities who read Kp and flux figures daily and keep long
memories; science museums running a "solar weather" desk; any
publication whose value is a *dated, checkable prediction* — the
theme generalises to weather, tides and market almanacs only where
the publisher is genuinely willing to print its misses. The audience
is the returning daily reader: the almanac is a habit object, opened
each morning like the paper it imitates, and its design rewards the
reader who comes back to check whether yesterday's prophecy held.

**When NOT to use it.** Not for real-time alerting where seconds
matter — the almanac's slowest ceremony (the sun inking in) is a
deliberate 2 seconds, and a geomagnetic storm warning that must
interrupt should use the storm plate's indigo (§6.12) as a banner,
never wait for a plate to print. Not for data-dense operational
consoles (grid operators paging through thousands of rows need a
tool, not a volume). Not for any publisher unwilling to keep the
errata slip honest: the moment a miss is silently corrected, the
theme becomes costume, and costume is the failure mode §9 names
first. Not for audiences who need a light, airy marketing page —
this theme is dense by conviction; its whitespace is the margin of a
printed page, not the breathing room of a landing page.

**The reader's contract.** Everything on the page is already printed
before any motion begins. Motion in this theme is the *printing*
catching up with the reader's eye — ink arriving, rays extending,
plates settling — never content arriving late. If every script on the
page failed, the almanac would stand open, complete and legible,
exactly as the reduced-motion variant presents it.

## 2. Palette

Five anchors, four derived tokens. Ink is rationed: woodcut black
carries ≈78% of all marks on a typical plate; paper is the ground;
green, scarlet and indigo together never exceed ≈10% of a viewport
outside the forecast section, where the aurora curtain (§6.8) is
licensed to spend green overhead — and even there it spends it as
light, not as type.

| Token | Hex | Role | Usage ratio | Pairing & contrast (measured) |
|---|---|---|---|---|
| `--paper` | `#F1E8D2` | Almanac paper — page ground, plate grounds, table body | ≈62% of viewport | Ground for `--ink` (13.0:1), `--eclipse` (8.7:1), `--flare` (4.5:1) |
| `--ink` | `#26221C` | Woodcut black — all body type, woodcut illustration, rules, table figures | ≈78% of marks | On `--paper` 13.0:1 — the theme's default pairing, AAA |
| `--aurora` | `#4C956C` | Aurora green — the curtain, aurora data, ray accents in the forecast plate | ≈4% (licensed to ≈25% of the forecast viewport as light) | On `--paper` 3.0:1 — display and graphics only, never body text; on `--eclipse` 2.9:1 — graphics only |
| `--flare` | `#C0392B` | Flare scarlet — errata markers, the PROPHESIED stamp, storm figures | ≈2% | On `--paper` 4.5:1 — passes AA for text at stamp/marker sizes; on `--ink` 2.9:1 — forbidden, scarlet never sits on black |
| `--eclipse` | `#2E4057` | Eclipse indigo — the storm plate ground, night headers, the eclipsed sun | ≈4% | `--paper` on it 8.7:1 — the storm plate's pairing; on `--paper` 8.7:1 as display type |
| `--paper-deep` | `#E7D9B8` | Derived — plate grounds, the errata slip, coupon stock, zebra row tint at 40% | ≈8% | Under `--ink` 11.4:1; distinguishes a pasted slip from the leaf it is pasted on |
| `--fox` | `#C9AE7E` | Derived — foxing spots, aged edges, the gutter shadow's warm edge | <1% | Decorative only; never text, never a data colour |
| `--candle` | `#D98E32` | Derived — the candle-warm hover glow only (§6.10) | transient | Exists only as a radial gradient at ≤18% opacity; never a fill, never text |
| `--aurora-pale` | `#4C956C` at 12–28% | Derived — curtain gradient stops (§6.8) | forecast only | Always over `--paper` or `--eclipse`; the curtain is light through air, not a surface |

**Contrast rulings (blocking, §10).** Body text is `--ink` on
`--paper` or `--paper-deep` only. `--aurora` never sets text smaller
than 24px and never sets figures — aurora *data* is set in `--ink`
with a green ray-spoke beside it, because a number you cannot read at
3.0:1 is a prophecy disguised as decoration. `--flare` is licensed
for the errata dagger (†), the stamp, and storm figures at ≥16px;
its 4.5:1 on paper is the floor of the theme and it is spent nowhere
else. The storm plate (§6.12) inverts to `--paper` on `--eclipse`
(8.7:1) — the theme's only inverted surface, licensed because an
eclipse is the one place the almanac's sun goes dark.

**Dark-mode behaviour.** There is none, and the refusal is in-world:
an almanac is printed once, on paper, and does not re-print itself at
night. The single dark surface is the eclipse storm plate, which is
dark at noon too. A visitor's `prefers-color-scheme: dark` changes
nothing; the candle-warm hover (§6.10) is the theme's only
acknowledgement of lamplight, and it is transient by design.

## 3. Typography

Two families, no third. **Playfair Display** is the almanac's public
voice — engraved, high-contrast, used where the publication speaks
with authority: the masthead, month names, plate titles,
prognostication headings, the hero title. **Newsreader** is its
working voice — tables, figure columns, body prognostications,
tolerances, errata text, captions, form labels — set with
`font-feature-settings: "tnum" 1` wherever figures must align in
columns, because an almanac's tables are its credibility and a
wobbling column is a misprint.

| Role | Family & cut | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Masthead | Playfair Display 800 | clamp(44px, 7vw, 84px) / 0.95 | −0.01em | Small-caps season line above it in Newsreader |
| Month name | Playfair Display 700 | clamp(34px, 4.6vw, 56px) / 1.0 | 0 | Prints at the reading line (§6.4); never abbreviated — "AUGUST", not "AUG" |
| Plate title | Playfair Display 600 | 26px / 1.15 | 0 | One per plate; the plate's subject, not a slogan |
| Prognostication heading | Playfair Display 600 italic | 19px / 1.3 | 0 | Italic is the voice of prophecy — headings over prophesied matter are always italic |
| Body / prognostication text | Newsreader 400 | 17px / 1.55 | 0 | Measure 58–68ch; observations in roman, prophecies introduced by the italic heading above them |
| Table figures | Newsreader 500, `tnum` | 15px / 1.45 | 0 | Right-aligned in figure columns; units in 12px small type after the figure |
| Observed / prophesied heads | Newsreader 600 small caps | 12.5px / 1.2 | 0.14em | The two column heads are never renamed, reordered or abbreviated anywhere in the theme |
| Tolerances & small print | Newsreader 400 italic | 13px / 1.45 | 0 | Every table's tolerance line is mandatory (§6.6); no table ships without it |
| Errata text | Newsreader 400 | 14.5px / 1.5 | 0 | Set on `--paper-deep`; the dagger and the missed figure in `--flare` |
| Corona type (§6.2) | Newsreader 600 small caps | 11px | 0.32em | The only letterspaced ring text; letterforms stay upright as they orbit |
| Date rule (§6.5) | Newsreader 600, `tnum` | 13px | 0.06em | "DAY 214 OF THE SEASON" — the day in figures, always the record's day |
| Stamp (§6.11) | Playfair Display 700 small caps | 15px | 0.18em | "PROPHESIED" — scarlet, rotated −4°, set as type, never as an image |

**Type laws.** (1) *Figures are Newsreader, always* — Playfair never
sets a data figure; its numerals are for dates in display lines and
the masthead year only. (2) *Italic means prophecy* — the italic cut
appears only where the almanac is predicting, confessing (tolerance
lines) or quoting; an italic observation is a category error and
fails §10. (3) *The two column heads are sacred* — OBSERVED and
PROPHESIED, in that order, in small caps, on every table in the
theme, so a reader can audit any table at a glance. (4) *Nothing is
set in scarlet except the confession and the stamp* — scarlet
headlines are a news-site habit and are refused. (5) *Type never
moves* — no animation translates, scales or fades a text block as a
block; the theme's kinetic type is confined to the corona ring
(§6.2), whose letters are ornament around an already-printed hero.
Counters change figure *values*, never figure *positions*: tabular
figures, fixed-width columns, zero layout shift.

## 4. Layout language

The page is a bound volume opened flat. The organising unit is the
**spread**: a two-page opening with a **stitched binding gutter** —
a 48px vertical band at the centre of wide viewports carrying a
dashed stitch line (2px dashes of `--ink` at 35%) and a soft gutter
shadow (a 24px linear gradient, `--fox` at 12% to transparent) —
down its middle. Content is set in two columns across the spread on
≥1200px; the gutter is never crossed by text, only by plates that are
explicitly "bound in" (the forecast plate, §6.8, spans the gutter
because the aurora is overhead, not on the page).

**The year is the sitemap.** Sections advance by months: each month
is a **calendar plate** (§6.4), a full-width leaf carrying the month's
table, its woodcut plate illustration and its prognostications.
Plates stack in calendar order, January at the top of the archive,
the current month at the reading position on the home page. Between
plates, a **month rule** — a double hairline (3px + 1px, `--ink`)
with the month name centred in Playfair — acts as both divider and
anchor target.

**Grid and rhythm.** ≥1200px: 12 columns, 24px gutters, 72px page
margins inside a 1280px maximum leaf width; the date-rule rail
(§6.5) occupies a fixed 132px margin column on the left of the
spread. Spacing follows the almanac's own measure: the **line** —
17px body × 1.55 ≈ 26px — is the vertical unit; section padding is
multiples of 4 lines (104px), plate padding 3 lines (78px), table
cell padding a half line. Density is high and deliberate: an almanac
plate fills its leaf. Whitespace lives in the margins and around
woodcut plates, where it reads as the paper a plate was printed on —
never as empty modernist air between floating cards.

**Frames.** Every illustration sits in a **cross-hatched frame**: a
3px `--ink` outer rule, a 10px inner field of diagonal hatching
(repeating-linear-gradient, 45°, `--ink` at 18%, 5px period), then
the plate. The frame is part of the illustration's cost and is
counted in §14's budget. Tables are ruled, not boxed: hairlines
between rows, a double rule under the column heads, no outer border
— the table is type on paper, held by its rules.

**The margin is a working column.** The left margin carries the date
rule (§6.5); plate margins carry ray-spoke draws (§6.9) and the
reader's stamps (§6.11); the errata slip (§6.7) is pasted into the
margin of the year's final plate, slightly rotated, overlapping the
gutter — the one licensed break of the grid, because a pasted slip
is a physical afterthought in a bound book and reads as one.

## 5. Full motion system

Every motion term is either given its almanac form or refused with
an in-world reason. Motion here is printing, settling and orbiting —
processes of a physical volume — and nothing moves that paper could
not.

**The one engine.** All scroll-driven values (ray rotation, date
rule position, aurora intensity, plate settle offsets) are computed
in a single `requestAnimationFrame` loop reading one lerped scroll
position: `current += (target − current) × 0.12` per frame
(`--lerp`), so the page has the almanac's weight — it settles
*onto* each month rather than snapping to it. The loop sleeps when
the tab is hidden and when no scroll delta has occurred for 120
frames. No element runs its own scroll listener.

**Named easings (tokens).** `--ease-press` cubic-bezier(0.22, 1,
0.36, 1) — the page-settle, a press coming down; `--ease-ink`
cubic-bezier(0.65, 0, 0.35, 1) — stroke drawing, even and deliberate;
`--ease-stamp` cubic-bezier(0.2, 2.2, 0.4, 1) — the stamp's single
overshoot; `--ease-turn` cubic-bezier(0.7, 0, 0.3, 1) — the spread
turning; `--ease-orbit` linear — the corona, which must never appear
to hurry. Durations are tokens per element (§6) and are never
re-tuned ad hoc.

| Motion term | Almanac form | Spec |
|---|---|---|
| Scroll-triggered reveals | Plates print at the reading line | Month plate settles 6px + gutter shadow shift, 480ms `--ease-press`, triggered when the plate's month rule crosses 62% viewport height (§6.4) |
| Scroll-driven / scrub | The sun's rays rotate & extend; the date rule advances | Ray rotation 0–40° across the hero's scroll range; date rule day = f(page progress) mapped onto the 365-day record (§6.1, §6.5) |
| Parallax | Print depths | Three depths only: foxing layer 0.96×, plate illustrations 0.99×, tables 1.0× — paper depths, never landscape depths; total differential ≤14px on any plate |
| Pinned sections | The forecast plate pins | Forecast plate pins for 160vh while the aurora curtain plays overhead (§6.8); the pin is the only one in the theme |
| Masked reveals | The title through the sun's disc | Hero title revealed by a circular mask expanding with the sun disc as it inks (§6.1); masks are discs and rules only — no diagonal wipes |
| Blur-to-sharp | **Refused** | A woodcut has no blur state; focus effects belong to lenses. The enlarger of theme #73 owns focus; here, ink is binary — a line is printed or not yet printed |
| Kinetic typography | The corona ring only | Small-caps type orbits the sun at 0.5rpm, letters uprighting (§6.2); no other text moves, ever (§3, law 5) |
| Marquee | **Refused** | An almanac does not scroll sideways; its one circular text is the corona, which orbits because the sun's corona does |
| Animated counters | Figures count in tabular type | Count duration 900ms `--ease-ink`, values only from the Season Record, counting *up to the observed figure* — the count is the observation arriving (§6.6) |
| Progress indicator | The date rule | A calendar, not a bar: the margin rule fills day by day with the day readout in figures (§6.5) |
| SVG line-draw | Ray spokes & the aurora ribbon | 1,200ms `--ease-ink` per plate as it arrives (§6.9); strokes are engraved lines, drawn at engraving speed |
| Image scale-in-frame | Plates scale inside their frames | 1.06 → 1.0 across the plate's settle, inside the cross-hatched frame; the frame never scales (§6.4) |
| Hover micro-interactions | Candle-warm glow; page-lift tilt | Glow follows the pointer (§6.10); plates tilt ≤2° as a heavy leaf lifting; links underline with a drawn rule (stroke-draw 180ms) |
| Magnetic / tilt physics | Tilt only, rationed | Max 2°, plates only, never on tables or forms — a table that tilts spills its figures |
| Custom cursor | **Refused** | Normal system cursor; the reader's lamp is the hover glow, not a cursor costume |
| Skeleton loading | Ruled blanks | Empty ruled columns print first; figures ink into them (§6.15); the rules are visible from first paint so layout never shifts |
| Page transitions | The stitched spread turns | Gutter shadow crosses the page, 600ms `--ease-turn`, stitch line visible at centre (§6.16) |
| Ambient loops | Exactly two | The corona orbit (§6.2) and the woodcut grain shimmer (opacity 0.02–0.035, 7s period, on plate illustrations only — candlelight on paper, subliminal or cut). Foxing deepens once per session by 4% and then is still — deepening is a state change, not a loop |
| Reduced motion | The almanac open and fully printed | All plates printed, rays still at their engraved angles, aurora absent, counters at final figures, no pin, no orbit (§6 passim) |

**The watchdog law.** Every JS-armed pre-state in the theme carries
a named watchdog: a `setTimeout` (token `--dur-watchdog-*` per
element) that forces the element to its printed rest state if its
animation has not completed. The DOM ships complete and printed;
JS may *hold back* a printed state only by arming a class, and every
armed class has a watchdog that disarms it. A page whose scripts die
mid-load is a fully printed almanac within the longest watchdog
(4,000ms) — §10 drills this by killing scripts in test.

**Scroll-back-up behaviour.** The almanac does not un-print.
Reveals, draws and counts are ratcheted: scrolling up shows the
plate as printed, rays at their drawn length, figures at their
observed values. Only scrubbed values (ray rotation, date rule,
aurora intensity) follow scroll in both directions, because they
are positions, not events.

## 6. Signature elements

### 6.1 The woodcut sun

- **What & why.** The hero's instrument: a woodcut sun disc, 300px
  at desktop, that inks in on load — the disc's cross-hatched face
  printing from the centre outward — while its **24 engraved rays
  extend in sequence, 40ms apart, stroke-drawn**, and the hero title
  is revealed through the disc's mask, the rays acting as the
  reveal's spokes. Thereafter the rays rotate slowly and extend
  further scrubbed to scroll. It belongs because the almanac's
  authority is its sun: every figure on every plate below is a
  measurement of this disc, and the publication opens by printing
  its subject in its own woodcut hand before it dares to print a
  number.
- **Structure.** One inline SVG (≤9KB): a disc of concentric
  hatched rings (paths, not filters), 24 ray paths in three length
  classes (long 96px ×8, mid 64px ×8, short 44px ×8, alternating),
  and a face — the almanac sun has a face, engraved, eyes closed,
  in the 19th-century manner. The title sits beneath in the DOM;
  the mask is a CSS `clip-path: circle()` on a wrapper, animated
  in step with the disc's ink-in. The DOM ships the sun fully
  printed and the title fully visible; JS arms the un-inked state
  (rays at 0 length via `stroke-dashoffset`, disc at 12% ink) only
  after first paint.
- **Motion spec.** Trigger: load, once per session (a returning
  reader finds the sun already printed — `sessionStorage` flag).
  t=0 gated on `document.fonts.ready` raced against 700ms (the
  title must reveal in Playfair or not move at all): disc inks
  0–700ms `--ease-ink` (radial mask grows 0→52% of disc radius);
  rays extend in sequence 300–1,260ms (24 × 40ms stagger, each ray
  220ms `--ease-ink`); title mask opens 500–1,100ms; day-count
  (§6.5's hero instance) ticks to the record's day across
  900–1,800ms. Total ceremony 1,800ms. Thereafter: rays rotate
  0–40° and extend +12% scrubbed across the hero's 120vh scroll
  range via the shared lerp loop (§5).
- **States.** Un-inked (JS-armed only) → inking → printed (rest).
  Hover: none — the sun is not a control. Scrolled-past: printed,
  rays at scrubbed angle. No-JS / watchdog: printed at first paint.
- **Content merge.** The sun is not a logo above the content; it is
  the hero's content — the day-count ticks inside its lower rays,
  the season's standfirst is set across its disc's diameter, and
  the same disc, eclipsed, is the storm plate's sun (§6.12). One
  instrument, three postings.
- **Failure fallback.** Watchdog `--dur-watchdog-sun` 2,600ms from
  DOMContentLoaded: rays snap to full length, mask removed, title
  plain. No-JS: never armed. Slow network: the SVG is inline; only
  the ceremony script is deferred.
- **Reduced-motion variant.** The sun stands printed, rays at their
  engraved rest angles, title unmasked, day-count at 214.
- **Performance budget & mobile variant.** One inline SVG ≤9KB,
  transforms and dash-offsets only, no filters. Mobile (<768px):
  disc 200px, rays 16 (short class cut), stagger 30ms, ceremony
  1,300ms, scrub range halved.
- **Choreography timeline (v2).** t=0 fonts ready (or race lost →
  rest) → 0–700 disc inks → 300–1,260 rays extend → 500–1,100
  title mask opens → 900–1,800 day-count ticks → 1,800 sun at
  rest, scrub arms → watchdog ceiling 2,600ms.
- **State matrix (v2).** *Rest:* printed, rays full, slow scrub
  live. *Hover:* none. *Focus:* n/a (not focusable; the hero's
  first focusable element is the masthead's current-month link,
  §6.3). *Active:* n/a. *Scrolled-past:* printed; rotation holds
  at range end. *Disabled:* printed. *Touch:* identical; no tap
  behaviour.
- **Breakpoints (v2).** ≥1200px: 300px disc, 24 rays, full
  ceremony. 768–1199px: 248px, 24 rays, stagger 34ms. <768px:
  200px, 16 rays, ceremony 1,300ms, scrub 0–20°.
- **Edge cases & failure modes (v2).** *Tab hidden mid-ceremony:*
  rAF pauses; wall-clock watchdog fires on return and the sun
  rests printed. *Hero title edited longer in a CMS:* the mask is
  centred on the disc, not the title's box — a three-line title
  still reveals through it, spokes unchanged. *Second visit:*
  session flag ships it printed; the almanac does not re-print
  its frontispiece hourly.
- **Accessibility spec (v2).** The sun is `aria-hidden` ceremony
  over a complete hero: the title, standfirst and day-count are
  real text, present in the DOM in reading order, never dependent
  on the mask. The day-count's final value (214) is the text
  content; the tick is a visual performance of it, with an
  `aria-live="off"` wrapper so screen readers hear the figure
  once, at rest.
- **Tokens consumed (v2).** `--ink`, `--paper`, `--aurora`
  (two licensed rays at the disc's east — the aurora's first
  appearance, §10 census), `--ease-ink`, `--lerp`, `--dur-sun`
  (1,800ms), `--dur-watchdog-sun` (2,600ms).

### 6.2 Orbiting corona type

- **What & why.** A ring of small-caps Newsreader type —
  "PROGNOSTICATIONS FOR THIS SEASON · OBSERVED & PROPHESIED ·" —
  orbits the woodcut sun continuously at **0.5rpm** (one revolution
  per 120s), each letter uprighting as it travels, so the ring is
  always readable at its top. It belongs because the sun's corona
  *is* the almanac's subtitle: the publication's promise — that it
  predicts, and then checks — literally circles its subject,
  endlessly, at the speed of an instrument, not an advertisement.
- **Structure.** An SVG `textPath` on a circular path (radius =
  disc radius + 34px), the string set twice to fill the ring;
  rotation applied to the SVG group while a counter-rotation per
  letter is pre-computed in the path geometry (letters are placed
  upright at build time by the path's own curvature — the standard
  textPath treatment, no per-frame letter math). DOM ships the
  ring static and complete around the printed sun.
- **Motion spec.** Trigger: time loop, arming only after §6.1's
  ceremony completes (or immediately, at rest angle, if the sun
  shipped printed). Rotation: linear, 360° per 120s,
  `--ease-orbit`. Pause conditions: tab hidden, hero off-screen
  (IntersectionObserver), or `prefers-reduced-motion`. The ring
  never accelerates, never reacts to scroll or pointer — an
  instrument's indifference is the effect.
- **States.** Rest (static ring, no JS) → orbiting. Hover: none.
  Scrolled-past: paused off-screen, resumes at its angle — the
  angle is kept in a CSS variable so resumption has no jump.
- **Content merge.** The ring's text is the hero's subtitle — it
  exists nowhere else, and its two clauses name the theme's two
  columns (observed / prophesied), so the orbit continuously
  restates the law (§1) around the instrument the law governs.
- **Failure fallback.** No JS: the ring stands printed around the
  sun — a corona of type is still a corona. Script failure
  mid-orbit: the group freezes at its current angle; nothing is
  hidden, nothing depends on it.
- **Reduced-motion variant.** Static ring, printed, at the rest
  angle (text centred at top).
- **Performance budget & mobile variant.** One SVG ≤2KB, one
  rotating group (transform only, GPU-cheap). Mobile: ring radius
  shrinks with the disc; the string shortens to one clause
  ("PROGNOSTICATIONS FOR THIS SEASON ·") so letters never crowd
  below 11px.
- **Choreography timeline (v2).** t=§6.1 rest → ring fades its
  rotation in over 600ms (no fade of opacity — the *motion*
  starts from rest speed 0 and eases to 0.5rpm across 2,400ms,
  so there is no visible "switch-on") → steady 120s/rev →
  pauses off-screen, resumes at kept angle.
- **State matrix (v2).** *Rest:* printed ring, motion 0.
  *Hover:* none — pointer over the ring does not slow it (an
  instrument is not shy). *Focus:* n/a. *Active:* n/a.
  *Scrolled-past:* paused, angle kept. *Disabled:* printed.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full two-clause string, radius
  +34px. 768–1199px: full string, radius +28px. <768px:
  one-clause string, radius +22px, period 150s (slower on the
  smaller ring, same linear speed).
- **Edge cases & failure modes (v2).** *Long translations:* the
  string is set twice only if it fits at 11px/0.32em; a locale
  whose clause overflows ships the one-clause ring at all sizes
  rather than shrinking type below the floor. *Font swap:* the
  ring is inside the §6.1 fonts race — if Newsreader loses, the
  ring still orbits (type on a path tolerates the fallback face
  better than the masthead does), but letter-spacing is recomputed
  on `fonts.ready` to prevent a visible re-flow of the ring.
- **Accessibility spec (v2).** The ring is `aria-hidden="true"`;
  its text is duplicated as the hero's visually-set standfirst
  line in the DOM (§8.1), so the promise is available to screen
  readers once, statically. Motion is decorative, pausable by
  reduced-motion and by leaving the viewport.
- **Tokens consumed (v2).** `--ink`, `--ease-orbit`,
  `--dur-corona-rev` (120s), `--dur-corona-spinup` (2,400ms).

### 6.3 The masthead & month index — navigation

- **What & why.** The almanac's running head: a masthead leaf at
  the top of every page carrying the publication's name in
  Playfair, the season line ("FOR THE YEAR OF THE SUN · 365
  DAYS"), and the **month index** — the twelve months set as a
  contents row, each a link to its plate, the current month
  underlined with a drawn double rule and marked with a small
  woodcut sun glyph. It belongs because an almanac's navigation
  *is* its calendar: there is no "menu" in this world, there is
  the year, and you turn to the month you need.
- **Structure.** A `<header>` with the masthead block and a
  `<nav aria-label="Months of the season">`: an ordered list of
  twelve month links in calendar order, set in Newsreader small
  caps across the spread's width, divided by hairlines. The
  current month carries `aria-current="page"` (on plate pages)
  or `aria-current="date"` (on the home page's current plate).
  Utility links (the errata slip, the order coupon, search of the
  archive) sit in a secondary row set smaller, after a double
  rule — the almanac's "advertisements" position, in-world.
- **Motion spec.** On load: the masthead prints with the page (no
  ceremony — the running head is furniture, not an event). The
  current month's double rule draws in 400ms `--ease-ink` when
  the nav first enters view. On scroll: the masthead leaf
  *shortens* — past 240px of scroll the Playfair nameplate
  collapses to a one-line running head (name + current month +
  day readout from §6.5) over 300ms `--ease-press`, and the month
  index remains, sticky, as the volume's thumb-index. The
  collapse is a height transition on a wrapper; the sticky index
  is `position: sticky`, no JS.
- **States.** Rest: full masthead. Scrolled: running head +
  sticky index. Hover on a month: the month's name warms
  (§6.10's glow at 40% strength, confined to the link) and a
  hairline draws beneath it, 180ms. Focus: visible double-rule
  outline in `--ink` (see accessibility). Active month: double
  rule + sun glyph. Disabled: n/a.
- **Content merge.** The index is not chrome around the content —
  it is the table of contents of the volume the visitor is
  inside, and its current-month marker is driven by the same
  Season Record day that drives the date rule (§6.5) and the
  hero count (§6.1): one record, three postings, never divergent.
- **Failure fallback.** No JS: full masthead, index static, no
  collapse — the page is a printed volume's opening and loses
  nothing essential. Watchdog: the collapse is scroll-driven via
  the shared loop; if the loop dies, the masthead simply stays
  full-height, which is its printed state.
- **Reduced-motion variant.** No rule draw (rule printed), no
  collapse animation (the running head swaps at the threshold
  without transition), sticky index retained (position, not
  motion).
- **Performance budget & mobile variant.** Pure HTML/CSS + one
  height transition; ≤4KB. Mobile (<768px): the month index
  becomes a horizontally scrollable thumb-row (scroll-snap,
  months as 44px targets) beneath a centred nameplate; the
  season line shortens to the year only.
- **Choreography timeline (v2).** t=0 masthead printed → first
  view: current-month rule draws 0–400ms → scroll >240px:
  collapse 300ms → scroll back <40px: full masthead restores
  300ms (hysteresis prevents flutter at the threshold).
- **State matrix (v2).** *Rest:* full. *Hover:* warm + hairline
  per link. *Focus:* double-rule outline, offset 3px.
  *Active:* current month marked. *Scrolled-past:* running-head
  form. *Disabled:* n/a. *Touch:* no hover warm; tap targets
  44px; the thumb-row scrolls with momentum.
- **Breakpoints (v2).** ≥1200px: two-row masthead across the
  spread, index in one line. 768–1199px: nameplate 40px, index
  wraps to two lines of six. <768px: thumb-row form, nameplate
  centred, secondary row collapses behind a "MORE OF THE VOLUME"
  disclosure set as a printed contents line.
- **Edge cases & failure modes (v2).** *A thirteenth month:*
  never — the record is a year; archive years are separate
  volumes with their own mastheads, linked from the colophon
  (§6.17). *Very long month names in translation:* the index
  allows two-line wrap at tablet rather than shrinking below
  12.5px. *Sticky + iOS Safari:* the index uses sticky within
  the header's parent, tested; fallback is a static index —
  navigation never depends on stickiness.
- **Accessibility spec (v2).** Landmark `header` + labelled
  `nav`; current month programmatically current, not colour
  alone (double rule + glyph + `aria-current`); focus outline
  2px double `--ink` on `--paper` (13.0:1); thumb-row is a
  single tab stop with arrow-key month movement on mobile form.
- **Tokens consumed (v2).** `--ink`, `--paper`, `--paper-deep`,
  `--candle` (hover warm at 40%), `--ease-ink`, `--ease-press`,
  `--dur-nav-rule` (400ms), `--dur-nav-collapse` (300ms).

### 6.4 Month plates

- **What & why.** The theme's section unit: each month is a
  calendar plate — a full leaf carrying the month rule with its
  name in Playfair, the month's observed-vs-prophesied table
  (§6.6), one woodcut plate illustration in its cross-hatched
  frame, and the month's prognostications. As each plate reaches
  the reading line it **settles like a page under a press: a 6px
  drop with the gutter shadow shifting across it**, and its
  illustration scales 1.06 → 1.0 inside its frame. It belongs
  because time is the information architecture: the year is the
  sitemap (§6.3), reading is the seasons passing, and the settle
  is the physical acknowledgment that a new month has come under
  the reader's hand.
- **Structure.** A `<section class="plate" id="august">` per
  month: month rule (double hairline + centred Playfair name),
  a two-column spread body (table left of the gutter, plate
  illustration and prognostications right, on ≥1200px), plate
  footer with the month's errata count and day range ("DAYS
  213–243 OF THE SEASON"). The DOM ships every plate complete
  and visible; JS arms a 6px translate + gutter-shadow offset
  only on plates below the fold at load.
- **Motion spec.** Trigger: the plate's month rule crossing 62%
  of viewport height, via the shared loop's observer. Settle:
  480ms `--ease-press` — translateY(6px → 0), gutter shadow
  sweeps 24px and rests, illustration scale 1.06 → 1.0 across
  the same 480ms. Plates stagger only by calendar order of
  arrival (each settles when *it* reaches the line — no
  artificial cascade). Ratcheted: a settled plate never
  un-settles on scroll-up (§5).
- **States.** Un-settled (JS-armed, below fold only) → settling
  → printed (rest). Hover: the plate illustration warms
  (§6.10). Scrolled-past: printed; its month becomes the date
  rule's "current plate" for §6.5's readout. Disabled/no-JS:
  printed.
- **Content merge.** The plate is not a container decorated as a
  month — its contents *are* the month: the table's rows are the
  month's days aggregated, the illustration is the month's
  woodcut (August: the sun at harvest height, rays long), the
  footer counts the month's own errata. Remove the month and
  there is nothing left to decorate.
- **Failure fallback.** Watchdog `--dur-watchdog-plate` 2,000ms
  after a plate's trigger window opens: if the settle has not
  run (observer failure, loop stall), transforms clear and the
  plate stands printed. No-JS: never armed.
- **Reduced-motion variant.** Plates printed; no settle, no
  scale; the month rule is the only divider.
- **Performance budget & mobile variant.** Transform + shadow
  only; plate illustrations are the page's main image cost
  (budgeted in §14: ≤38KB each as optimised woodcut-style
  rasters or inline SVG for the line plates). Mobile: plates
  stack single-column (table above illustration), settle reduced
  to 3px / 360ms, gutter shadow omitted (no gutter on mobile).
- **Choreography timeline (v2).** Trigger (rule at 62%) → 0–480
  settle + shadow sweep + illustration scale → at 240ms the
  plate's table counters arm (§6.6) → at 480ms plate printed,
  §6.9's ray-spoke draw for this plate arms → watchdog ceiling
  2,000ms.
- **State matrix (v2).** *Rest:* printed. *Hover:* illustration
  warm (§6.10); table rows highlight with `--paper-deep` at 40%
  on the hovered row only. *Focus:* plate is not focusable;
  its links/table controls take the standard focus (§6.3).
  *Active:* n/a. *Scrolled-past:* printed; month marked current
  in §6.5 while it straddles the reading line. *Disabled:*
  printed. *Touch:* no hover states; settle identical.
- **Breakpoints (v2).** ≥1200px: two-column spread across the
  gutter, 6px settle. 768–1199px: two columns without gutter
  (gutter appears only ≥1200), settle 5px. <768px: single
  column, settle 3px/360ms, month name 30px.
- **Edge cases & failure modes (v2).** *A month with no
  observations yet* (the current month, mid-course): the plate
  prints its prophesied column complete and its observed column
  filled only to today's row, the remaining rows ruled and
  blank with the printed note "OBSERVATIONS TO COME" — blank
  ruled rows are the almanac's honest state, never skeleton
  shimmer (§6.15 governs load, not the future). *Content longer
  than the design:* plates grow; the settle is transform-only
  and indifferent to height. *Jump-scroll to the foot:* all
  plates above the line settle instantly (duration 0) — the
  reader who teleports finds a printed book, not a cascade.
- **Accessibility spec (v2).** Each plate is a `section` with
  `aria-labelledby` pointing at its month name; day ranges are
  text, not just position; the settle is decorative and never
  moves focus; row hover highlight is never the sole carrier of
  row identity (rows are labelled by their row heads, §6.6).
- **Tokens consumed (v2).** `--paper`, `--paper-deep`, `--ink`,
  `--fox` (gutter shadow edge), `--ease-press`, `--dur-plate`
  (480ms), `--dur-watchdog-plate` (2,000ms).

### 6.5 Date-rule progress

- **What & why.** The theme's progress indicator is a calendar:
  a rule in the left margin rail that **advances day by day**
  with scroll, its day readout in tabular figures — "DAY 214 OF
  THE SEASON" — with a tick and a slightly longer rule at each
  month boundary, and the month name printing beside the tick as
  it is crossed. It belongs because in an almanac, *how far you
  have read is what date it is*: progress measured in days of the
  record, not in percent of a scrollbar, binds the reader's
  position to the publication's own time.
- **Structure.** A fixed-position rail (132px margin column,
  §4) on ≥1200px: a vertical hairline track of 365 day ticks
  (rendered as one SVG, ≤3KB, ticks pre-drawn), a filled portion
  in `--ink` 2.5px, a day readout block (Newsreader `tnum`:
  "DAY 214" / "OF THE SEASON" / current month name), and month
  ticks labelled in 11px small caps. The mapping is declared:
  page scroll progress × 365 = the displayed day, *except* the
  readout never displays a day beyond the record's "today" (214)
  on the home page — reading ahead shows the plate you are on,
  and the rail's day is min(scrollDay, 214) there; on archive
  plates the rail maps to that plate's day range. The DOM ships
  the rail at the record's day, complete.
- **Motion spec.** Scrubbed, both directions, via the shared
  lerp loop (§5): the fill length and readout update from the
  lerped scroll value; the readout's figures change only when
  the computed day changes (integer steps — a calendar ticks, it
  does not slide). At a month boundary the tick draws 160ms
  `--ease-ink` and the month name cross-fades 200ms. No other
  animation: the rail is an instrument the reader consults, not
  a performance.
- **States.** Rest: at the record's day for the scroll position.
  Hover: the rail widens its hit area and shows the hovered
  position's date in the readout as a preview ("DAY 96 —"), with
  the printed day restored on leave; clicking the rail scrolls
  to that day's plate (the rail is the volume's thumb-index,
  §6.3's sibling). Focus: the rail is one focusable slider-like
  control (see accessibility). Scrolled-past: n/a — it is fixed.
  Disabled: printed at the record's day.
- **Content merge.** The rail's day, the masthead's current
  month (§6.3) and the hero's day-count (§6.1) are three
  printings of the Season Record's single "today" — §10's
  figure audit greps all three. The rail is the record's margin,
  not a widget beside it.
- **Failure fallback.** No JS: the rail stands printed at Day
  214 with all ticks drawn — a margin rule in a book. Loop
  failure: the rail freezes at its last day; nothing else
  depends on it.
- **Reduced-motion variant.** The rail still updates (it is
  information, not decoration) but without lerp smoothing —
  values step with scroll — and the month-name cross-fade is
  removed.
- **Performance budget & mobile variant.** One SVG ≤3KB, one
  lerped value, integer-day updates only (≤365 DOM writes per
  full scroll). Mobile (<1200px): the rail leaves the margin
  and becomes a **top rule** under the running head — a
  horizontal day rule with the readout inline ("DAY 214 · AUGUST
  "), same mapping, same ticks at month boundaries compressed
  to dots.
- **Choreography timeline (v2).** Continuous: scroll delta →
  lerp (0.12/frame) → day integer changes → readout updates,
  fill extends → month boundary: tick draw 160ms + name fade
  200ms → rest. No start/end ceremony.
- **State matrix (v2).** *Rest:* record day for position.
  *Hover:* date preview. *Focus:* keyboard control live
  (arrows ±1 day, PgUp/PgDn ±1 month, Home/End to season
  bounds; activation scrolls to the plate). *Active:* while
  dragging on touch, readout previews the dragged date.
  *Scrolled-past:* n/a. *Disabled:* printed at 214. *Touch:*
  drag on the top-rule form; 44px tall hit area.
- **Breakpoints (v2).** ≥1200px: left margin rail, full ticks +
  month labels. 768–1199px: top rule form, month dots +
  readout. <768px: top rule, readout only ("DAY 214 · AUG"),
  ticks as dots.
- **Edge cases & failure modes (v2).** *Pages shorter than a
  plate* (the errata slip page): the rail maps across the page's
  own length but its day is pinned to the record's today — a
  short page is still read on Day 214. *Reader scrolls faster
  than the lerp:* the integer day steps skip — correct; a
  calendar flipped fast shows fewer dates, and the fill always
  lands exactly on release. *Print stylesheet:* the rail prints
  at the record's day, as a margin rule should.
- **Accessibility spec (v2).** The rail is a `role="slider"`
  with `aria-valuemin=1`, `aria-valuemax=365`,
  `aria-valuenow`, and `aria-valuetext="Day 214 of the season,
  August"`; arrow-key operation as in the state matrix; the
  visual readout duplicates the value as plain text for
  non-slider-aware AT. Contrast: readout `--ink` on `--paper`
  13.0:1; the fill is never the sole carrier (the figure is
  printed beside it).
- **Tokens consumed (v2).** `--ink`, `--paper`, `--paper-deep`,
  `--ease-ink`, `--lerp`, `--dur-rail-tick` (160ms).

### 6.6 Observed vs prophesied tables

- **What & why.** The theme's heart and its anti-slop detail
  made structural: every data table in the almanac carries the
  two sacred columns — **OBSERVED** and **PROPHESIED** — with
  the month's figures in tabular Newsreader, a printed tolerance
  line beneath, and, where the prophecy missed beyond tolerance,
  a **scarlet errata dagger (†)** in the prophesied cell that
  links to the errata slip (§6.7). As a plate centres, its
  observed figures **count up in tabular figures** to their
  recorded values — the observation arriving — while prophesied
  figures stand printed from the start: they were printed last
  season, and ink does not count.
- **Structure.** A semantic `<table>`: row heads name the
  quantity and unit (SUNSPOT NUMBER · SOLAR WIND KM/S · RADIO
  FLUX 10.7CM SFU · GREATEST KP · AURORA TO LATITUDE), columns
  PROPHESIED then OBSERVED (prophecy first — it was printed
  first, chronologically and morally), a TOLERANCE column in
  small italic, and the dagger as a real `<a href="#errata">`
  with `aria-label="Errata: sunspot number prophesied 132,
  observed 147"`. Beneath the table, the mandatory tolerance
  line in italic: "Tolerances of this table: sunspot ±10 · flux
  ±5 · wind ±25 · Kp exact · aurora ±2°. Beyond tolerance, the
  miss is confessed upon the slip." All values ship complete in
  the DOM.
- **Motion spec.** Trigger: the table's plate settling (§6.4).
  Observed figures count from the previous plate's closing
  value (or from 0 for the year's first plate) to the recorded
  figure over 900ms `--ease-ink`, staggered 90ms per row,
  figures only — no cell movement, tabular widths fixed so
  columns never breathe. The dagger, where present, inks in
  last, 200ms, at the count's end — the confession arrives after
  the fact it confesses. Ratcheted; never re-counts.
- **States.** Rest: printed, observed at recorded values.
  Counting (transient, once per plate). Hover: row warms with
  `--paper-deep` 40% (shared with §6.4). Focus: daggers are
  links and take the standard focus; the table itself is not
  interactive beyond them. Scrolled-past: printed. Disabled:
  printed complete.
- **Content merge.** The table is not *in* the theme; the table
  is the theme's reason to exist. Its two columns are the law
  (§1) in tabular form, its tolerance line is the law's terms,
  and its daggers are the law's enforcement — every other
  element on the page exists to bring the reader to a table and
  keep the table honest.
- **Failure fallback.** No JS / watchdog `--dur-watchdog-table`
  2,400ms: figures stand at recorded values (they were never
  hidden — the count is a textContent performance over printed
  values, armed by replacing the text only when the count is
  ready to run; if the script dies first, the printed values
  remain).
- **Reduced-motion variant.** No counts; figures printed;
  daggers printed with the table.
- **Performance budget & mobile variant.** Text-only animation,
  ≤5 counters per table on one rAF; zero layout shift (fixed
  tabular widths). Mobile: the table scrolls horizontally
  within the plate (the columns are never stacked — stacking
  OBSERVED under PROPHESIED would break the audit-at-a-glance
  the layout exists for), with the row-head column sticky and a
  printed "TABLE CONTINUES →" rule at the fold.
- **Choreography timeline (v2).** Plate settle (§6.4) → +240ms
  row 1 count 900ms, rows stagger +90ms → last row ends ≈
  1,500ms → daggers ink 200ms → table at rest → watchdog
  ceiling 2,400ms.
- **State matrix (v2).** *Rest:* printed. *Hover:* row warm.
  *Focus:* dagger links, double-rule outline. *Active:* dagger
  follows to §6.7 and returns focus to the same dagger
  (focus is restored, §6.7). *Scrolled-past:* printed.
  *Disabled:* printed. *Touch:* no hover; dagger targets 44px
  via padding that does not disturb the ruling.
- **Breakpoints (v2).** ≥1200px: full five-column table in the
  spread's left column. 768–1199px: full table, plate width.
  <768px: horizontal scroll form, row heads sticky, figures
  14.5px (never below — a misread figure is worse than a
  scrolled table).
- **Edge cases & failure modes (v2).** *A quantity with no
  prophecy* (a new instrument): the prophesied cell prints an
  em-dash and the tolerance line gains "— : not prophesied; the
  almanac does not invent a prophecy to fill a column."
  *Observed not yet known* (current month): observed cell ruled
  blank with "TO COME" in small caps (§6.4) — never a zero,
  never an estimate dressed as an observation (the law, §1).
  *A tie at tolerance:* within tolerance is agreement; the
  dagger appears only beyond it, and the boundary rule is
  printed in the tolerance line so the reader can check the
  almanac's arithmetic.
- **Accessibility spec (v2).** Real `<table>` semantics with
  `<th scope>` on both axes; the count is `aria-hidden` during
  its run with the final value as the cell's accessible text
  (screen readers hear 147 once, not a rising scale); dagger
  links have full-sentence labels naming quantity, prophecy
  and observation; tolerance line is table-adjacent text, not
  a caption AT may skip.
- **Tokens consumed (v2).** `--ink`, `--paper`, `--paper-deep`,
  `--flare` (daggers only), `--ease-ink`, `--dur-count`
  (900ms), `--dur-watchdog-table` (2,400ms).

### 6.7 The errata slip

- **What & why.** A slip of `--paper-deep` stock, pasted into the
  margin of the year's final plate at a −1.5° rotation, headed
  "ERRATA OF THE SEASON" in Playfair, listing every confessed
  miss in the form the almanac has used for two centuries: the
  plate, the quantity, what was prophesied, what was observed,
  and the difference signed. The August entries read: "AUGUST ·
  SUNSPOT NUMBER — prophesied 132, observed 147 · +15 beyond the
  tolerance of ±10." It is the target of every dagger in every
  table (§6.6). It belongs because the slip is the theme's moral
  centre made visible: a publication that pastes its corrections
  *into the bound volume*, where they cannot be separated from
  the error, has nowhere to hide — and the reader trusts the
  prophecies precisely because the slip exists.
- **Structure.** An `<aside id="errata">` styled as pasted stock:
  `--paper-deep` ground, a torn top edge (clip-path polygon,
  6 points), a foxed thumbprint of paste at its head, entries as
  a definition list grouped by month, and a footer tally: "IN
  ALL, 20 ERRATA UPON THE SEASON" — the record's figure (§1),
  reconciled with the plates' own counts by §10's audit. The
  slip ships fully printed, in the margin, in the DOM order
  after the final plate.
- **Motion spec.** The slip has almost none, by conviction: it
  was pasted before the reader arrived. Its one motion is
  *arrival acknowledgment* — when a dagger link (§6.6) brings
  the reader here, the referenced entry warms with
  `--paper-deep` deepening to full and a hairline draws beneath
  it, 300ms `--ease-ink`, and the entry is scrolled to the
  reading line. No entrance animation on page load; a confession
  does not perform.
- **States.** Rest: printed, pasted. Targeted (arrived via
  dagger): entry marked as above for 4s, then resting — the
  mark is a state, not a loop. Hover: none (the slip is read,
  not handled). Focus: entries are not focusable; the slip's
  one link ("RETURN TO THE AUGUST PLATE") returns the reader,
  restoring focus to the originating dagger (§6.6).
- **Content merge.** The slip's entries are generated from the
  same record as the tables' daggers — one miss, two printings
  (dagger in the table, confession on the slip) — and its tally
  (20) is the third printing of the season's errata count,
  audited in §10. It also carries the season's only apology, set
  in italic Newsreader: "The Almanac regrets its errors as it
  regrets the weather: publicly, and in print."
- **Failure fallback.** None needed and none armed: the slip is
  static printed matter. If JS dies, the slip is exactly itself.
- **Reduced-motion variant.** Identical; the arrival mark
  appears without its draw.
- **Performance budget & mobile variant.** Static HTML/CSS ≤3KB.
  Mobile: the slip un-rotates (0°) and takes the plate's full
  width below the final plate — a pasted slip on a narrow leaf
  would cover the text it corrects, and covering content is
  forbidden (§5 standing rules).
- **Choreography timeline (v2).** Dagger activation → slip
  scrolls to line (native, or 500ms `--ease-press` smooth where
  armed) → entry mark draws 300ms → holds 4,000ms → mark rests
  at a persistent hairline (the reader was here; the slip
  remembers without glowing).
- **State matrix (v2).** *Rest:* printed. *Hover:* none.
  *Focus:* return link only. *Active:* targeted entry marked.
  *Scrolled-past:* printed. *Disabled:* printed. *Touch:*
  identical; dagger targets already 44px (§6.6).
- **Breakpoints (v2).** ≥1200px: margin-pasted, −1.5°, 340px
  wide, overlapping the gutter. 768–1199px: in-flow after the
  final plate, −1° rotation, full plate width. <768px: in-flow,
  0°, full width.
- **Edge cases & failure modes (v2).** *A season with no
  errata:* the slip still prints, headed as ever, with the
  single entry "NONE RECORDED — the Almanac notes this with
  suspicion." (A slip that only appears when there are errors
  would teach readers its absence means perfection; the slip is
  furniture of honesty, printed either way.) *Errata longer
  than the margin:* the slip grows downward past the plate —
  a long confession is a long slip; it is never truncated,
  scrolled internally, or paginated.
- **Accessibility spec (v2).** `aside` with
  `aria-labelledby="errata"` heading; entries are text, fully
  readable without the rotation (rotation is visual only);
  dagger arrival moves focus to the slip's heading (tabindex
  −1) so screen-reader users land on the confession, not
  mid-list; the return link restores focus to the dagger.
- **Tokens consumed (v2).** `--paper-deep`, `--ink`, `--flare`
  (missed figures only), `--fox` (paste mark), `--ease-ink`,
  `--dur-errata-mark` (300ms).

### 6.8 Aurora curtain — the forecast plate

- **What & why.** The theme's one pin and its only theatrical
  element: the forecast plate pins for 160vh while a **curtain
  of layered aurora light ripples across the top of the
  viewport** — translucent green gradients whose **ripple
  amplitude and speed are tied to scroll velocity**: vigorous
  when the reader moves, settling to a slow breathe when they
  rest. Beneath it, the forecast table (§6.6's form, pointed at
  the nights ahead) stands printed. It belongs because the
  forecast should *perform itself* overhead while it is read:
  the aurora is the one phenomenon in the almanac that cannot be
  woodcut without lying about it, so the almanac lets it be
  light instead of ink — the single licensed exception to the
  printed world, fenced inside this one plate.
- **Structure.** The pinned plate is a normal plate (§6.4) whose
  top 38vh carries a `<canvas>` (or three stacked gradient divs
  where canvas is unavailable) behind a scrim of the plate's own
  prognostication heading. The curtain renders as 3 sine-layered
  bands of `--aurora-pale` (12–28% alpha) with a vertical falloff
  — rays suggested by vertical striping at 4% alpha, never drawn
  as objects. The forecast table below is ordinary DOM, fully
  printed, and the pin is a CSS `position: sticky` stage, not a
  JS hijack: scroll remains the reader's.
- **Motion spec.** Pin range 160vh. Curtain physics: a velocity
  value from the shared loop (|Δlerped scroll| per frame) maps
  to ripple amplitude 4px (rest) → 26px (fast) and wavelength
  speed ×1 → ×3.2, easing back to rest over 900ms when scrolling
  stops (`--ease-press` on the decay). At rest the curtain
  breathes at 0.08Hz, amplitude 4px — present, never busy. The
  curtain exists **only while the forecast plate is in view**;
  it fades its alpha to 0 across the plate's exit (200ms) and is
  not rendered anywhere else on the page.
- **States.** Unpinned (plate above/below) → pinned, curtain
  live → released. Hover: none — the sky does not respond to a
  pointer; the tables beneath keep their own hover (§6.6).
  Scrolled-past: curtain gone, plate printed as any other.
  Disabled/no-JS: no pin, no curtain — the forecast plate is a
  plate with a printed green ray-spoke (§6.9) where the curtain
  would be.
- **Content merge.** The curtain is not behind arbitrary
  content: it plays only over the forecast plate, its intensity
  is the reader's own motion (the faster you travel through the
  season, the more the sky stirs), and its colour is the exact
  green of the aurora figures in the table beneath it. When the
  forecast is for quiet nights (greatest Kp ≤ 2 in the record),
  the curtain ships at half alpha with the printed note "THE
  CURTAIN IS QUIET TONIGHT" — the sky obeys the record, not the
  designer's wish for spectacle.
- **Failure fallback.** Canvas failure / no-canvas: the stacked
  -div fallback renders the same bands as CSS gradients with a
  9s keyframed drift (velocity response lost, presence kept).
  Watchdog `--dur-watchdog-curtain` 3,000ms: if the rAF loop
  stalls, the curtain freezes at rest amplitude — a still sky,
  never a stuck page; the pin is CSS and cannot strand content.
- **Reduced-motion variant.** No pin, no curtain. The forecast
  plate prints with a static aurora ray-spoke illustration
  (§6.9) and the note "THE AURORA, PRINTED" — the almanac's own
  acknowledgment that in the still edition, the sky is ink.
- **Performance budget & mobile variant.** Canvas capped at
  0.5× devicePixelRatio, bands drawn as pre-rendered gradient
  strips offset per frame (no per-pixel work); frame cost
  ≤0.9ms (§14). Mobile: pin shortened to 110vh, curtain height
  30vh, two bands instead of three, velocity response halved —
  the sky on a small leaf is a smaller sky.
- **Choreography timeline (v2).** Plate reaches pin → curtain
  alpha 0→full 400ms, amplitude at rest → scroll velocity
  drives amplitude/speed continuously → scroll stops: decay to
  breathe over 900ms → pin releases at 160vh: alpha →0 200ms →
  plate scrolls away printed.
- **State matrix (v2).** *Rest (in view, no scroll):* breathing
  curtain. *Hover:* none. *Focus:* curtain is `aria-hidden`;
  focus passes to the forecast table normally — the pin never
  traps focus (sticky, not fixed). *Active:* n/a.
  *Scrolled-past:* absent. *Disabled:* printed plate, no pin.
  *Touch:* identical physics from touch scroll velocity;
  amplitude cap 20px (smaller viewport, smaller sky).
- **Breakpoints (v2).** ≥1200px: pin 160vh, curtain 38vh, 3
  bands. 768–1199px: pin 140vh, curtain 34vh, 3 bands.
  <768px: pin 110vh, curtain 30vh, 2 bands, alpha cap 22%.
- **Edge cases & failure modes (v2).** *Reader scrolls the pin
  range very fast:* amplitude caps at 26px and the decay
  extends — the sky never strobes; a hard rule caps band-edge
  velocity to avoid any flashing above 3Hz (photosensitivity,
  §10 check). *Low-power device:* `navigator.hardwareConcurrency
  ≤ 2` or a dropped-frame counter ships the CSS-div fallback.
  *The forecast is wrong:* the curtain performed a prophecy;
  when the observed plate prints next month, its errata dagger
  (§6.6) is the curtain's confession — the spectacle is as
  accountable as the figures.
- **Accessibility spec (v2).** Canvas `aria-hidden="true"`,
  role presentation; the forecast's content is entirely in the
  table beneath; the curtain never carries information (its
  quiet/loud states are duplicated as printed text — the Kp
  figures and the "CURTAIN IS QUIET" note); photosensitivity
  caps as above; reduced-motion removes it entirely.
- **Tokens consumed (v2).** `--aurora`, `--aurora-pale`,
  `--eclipse` (night strip behind the curtain's top edge),
  `--paper`, `--ease-press`, `--lerp`, `--dur-watchdog-curtain`
  (3,000ms).

### 6.9 Ray-spoke & ribbon draws — plate engravings

- **What & why.** Every month plate carries marginal engravings
  that **draw themselves as the plate arrives**: a small sun in
  the plate's margin whose ray spokes stroke-draw in sequence,
  and an aurora ribbon — a single undulating line — drawn along
  the plate's foot for months whose record includes aurora. Each
  draw takes **~1,200ms**, at engraving speed. It belongs because
  an almanac's illustrations were produced by a hand at a bench;
  drawing them at reading speed, in the plate's own margins,
  makes each month feel *engraved on arrival* rather than
  pasted in — the difference between a printed book and a
  printed-on-demand one.
- **Structure.** Per plate, one inline SVG (≤4KB): 8 ray spokes
  around a 28px margin sun, and/or one ribbon path (a smooth
  sine stroke, `--aurora` at 70%, 2px) spanning the plate's
  width. Paths ship with their full geometry in the DOM; JS arms
  `stroke-dasharray` hiding only when the plate is below the
  fold and the draw is queued. Months without aurora in the
  record draw spokes only — the ribbon's absence is data.
- **Motion spec.** Trigger: plate settle (§6.4) at +480ms.
  Spokes draw in rotational sequence, 8 × 90ms stagger, each
  300ms `--ease-ink`; the ribbon draws left-to-right 1,200ms
  `--ease-ink`, overlapping the spokes' second half. Total
  ≈1,200ms. Ratcheted: drawn stays drawn.
- **States.** Undrawn (JS-armed, below fold) → drawing → drawn
  (rest). Hover: none. Scrolled-past: drawn. Disabled: drawn
  (printed).
- **Content merge.** The margin sun's ray count encodes the
  month's longest day rank (August's margin sun carries the
  full 8 spokes at longest length; December's are shortest) —
  the engraving is a small chart of the month's daylight, and
  the ribbon exists exactly when the month's table records
  aurora. Ornament that is secretly data is the almanac's
  oldest trick, and here it is a rule, not a hope (§10 audits
  spoke lengths against the record).
- **Failure fallback.** Watchdog `--dur-watchdog-draw` 2,200ms
  from plate trigger: dash-arrays cleared, engraving printed.
  No-JS: printed.
- **Reduced-motion variant.** Engravings printed; no draw.
- **Performance budget & mobile variant.** ≤4KB SVG per plate,
  dash-offset animation only. Mobile: ribbon omitted on plates
  where the month had aurora on ≤2 nights (the record decides),
  spokes reduced to 6 — the margin of a small leaf is narrow.
- **Choreography timeline (v2).** Settle (480ms) → spokes
  480–1,380ms staggered → ribbon 780–1,980ms → drawn rest →
  watchdog ceiling 2,200ms (ribbon tail may finish under the
  watchdog's grace — the watchdog checks spokes, the ribbon is
  checked at 2,600ms by the same timer's second phase).
- **State matrix (v2).** *Rest:* drawn. *Hover:* none.
  *Focus:* n/a (decorative, `aria-hidden`). *Active:* n/a.
  *Scrolled-past:* drawn. *Disabled:* drawn. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: margin sun left, ribbon full
  width. 768–1199px: margin sun above the plate title, ribbon
  full width. <768px: sun inline with the month rule, ribbon
  per the record rule above.
- **Edge cases & failure modes (v2).** *Jump-scroll past
  several plates:* all queued draws complete instantly
  (duration 0) — engravings are printed for a reader who
  teleports (§6.4's rule). *A plate reused across pages*
  (archive index): the draw runs once per page view, not per
  session — a fresh opening of the volume re-engraves, which
  is correct; only the hero sun (§6.1) is session-rationed.
- **Accessibility spec (v2).** Entirely decorative:
  `aria-hidden="true"`, no focus, no information carried that
  is not also in the plate's table (daylight rank is stated in
  the plate footer's day range; aurora nights are rows in the
  table).
- **Tokens consumed (v2).** `--ink`, `--aurora`, `--ease-ink`,
  `--dur-draw` (1,200ms), `--dur-watchdog-draw` (2,200ms).

### 6.10 Candle-warm hover

- **What & why.** The reader's lamp. Hovering a plate warms its
  ink: a soft **candle-amber radial glow (~200px)** follows the
  pointer across the plate at ≤18% opacity while the plate's
  blacks deepen slightly (a 3% contrast lift on the plate's
  `--ink` elements), and the plate **tilts at most 2°**, as a
  heavy leaf lifts toward the light. It belongs because an
  almanac is read by candlelight: attention in this world is not
  a highlight colour, it is a lamp brought closer to the page
  being read — warmth, not chrome.
- **Structure.** A pointer-tracked radial-gradient layer
  (`--candle` at 18% → transparent at 200px) composited over the
  plate, `mix-blend-mode: multiply` so it warms rather than
  washes; the tilt is a transform on the plate's illustration
  frame only (never the table — §5), driven from the same
  pointer position, clamped to 2°. One listener per plate,
  throttled through the shared rAF.
- **Motion spec.** Glow follows with a 90ms trailing lerp (a
  lamp carried, not a laser); fade-in 240ms on enter, fade-out
  320ms on leave; tilt eases at `--ease-press` 300ms. Blacks
  deepen across the same 240ms. On touch devices the element
  does not exist — there is no lamp without a pointer, and
  nothing is lost.
- **States.** Rest: unwarmed print. Hover: warmed, tilted ≤2°
  (illustration only). Focus (keyboard): a focused link or
  control inside a plate warms the plate at 50% strength centred
  on the control — keyboard readers get a lamp too. Active:
  press states are the controls' own (§6.11, §11). Scrolled-past:
  unwarmed. Disabled: printed.
- **Content merge.** The glow is centred on the reader's actual
  point of attention and warms the *content under it* — the
  figures, the woodcut, the prognostication being read — never
  the plate's frame or margins alone. It is the theme's only
  pointer effect, and it is spent exclusively on reading.
- **Failure fallback.** Pointer events unsupported or script
  dead: plates are simply printed — the lamp is an enhancement
  with no informational role. No watchdog needed; nothing is
  ever hidden by its absence.
- **Reduced-motion variant.** The glow still warms (it is a
  light state, not a motion) but appears at the pointer without
  trailing lerp, and the tilt is removed entirely.
- **Performance budget & mobile variant.** One gradient layer +
  one transform per hovered plate; ≤0.3ms/frame. Mobile/touch:
  absent, at zero cost — the variant is the printed plate.
- **Choreography timeline (v2).** Enter → glow 0→18% over
  240ms, blacks deepen in step, tilt → ≤2° over 300ms → move:
  glow trails at 90ms lerp → leave: glow →0 over 320ms, tilt
  →0 over 300ms.
- **State matrix (v2).** *Rest:* print. *Hover:* full lamp.
  *Focus:* 50% lamp on the focused control's plate. *Active:*
  unchanged (presses belong to controls). *Scrolled-past:*
  print. *Disabled:* print. *Touch:* no lamp; tap targets and
  content unaffected.
- **Breakpoints (v2).** ≥1200px: glow 220px radius. 768–1199px:
  180px. <768px: pointer is rare; where present (mouse on a
  small screen) 150px, tilt 1°.
- **Edge cases & failure modes (v2).** *Pointer races across
  plates:* each plate's lamp fades on its own leave; two lamps
  never burn at once (the entering plate's fade-in cancels any
  other plate's). *Multiply blend unsupported:* fall back to a
  plain low-alpha gradient — slightly flatter warmth, same
  contract. *Hover over the forecast plate:* the lamp is
  disabled there — the aurora (§6.8) is that plate's light, and
  two skies do not share a plate.
- **Accessibility spec (v2).** Purely decorative and
  pointer-bound; no information is carried by warmth (deepened
  blacks only *raise* contrast, never lower it — §10 checks the
  warmed state still meets 13.0:1 body contrast); keyboard
  focus remains the double-rule outline, with the 50% lamp as
  supplement, never substitute.
- **Tokens consumed (v2).** `--candle`, `--ink`, `--ease-press`,
  `--dur-lamp-in` (240ms), `--dur-lamp-out` (320ms).

### 6.11 Prophesied-stamp click

- **What & why.** The reader's hand in the almanac's
  epistemology. Clicking a prophesied figure **stamps
  "PROPHESIED" beside it in scarlet** — Playfair small caps,
  rotated −4°, landing with a **120ms press** and a single
  overshoot — and the stamp **joins the plate's tally of marked
  prophecies**, printed in the plate footer ("MARKED PROPHESIED
  UPON THIS PLATE: 3 BY THE READER'S HAND"). It belongs because
  the law (§1) is not only the publisher's discipline: the
  reader who marks a prediction *as* a prediction, in the
  margin, in scarlet, has understood the almanac — and months
  later, when the observed column fills, their own stamps show
  them what they believed.
- **Structure.** Prophesied cells in §6.6's tables are
  `<button class="prophecy">` elements (real buttons, real
  labels: "Sunspot number, prophesied 132 — mark as
  prophesied"). The stamp is an absolutely positioned span of
  set type (never an image) inside the cell, `aria-hidden`,
  rotated −4° with a 1.5px scarlet double border — a rubber
  stamp set in type. Stamps persist for the session
  (`sessionStorage` list of stamped cell ids); the plate
  footer's tally is a live text node updated on each stamp.
- **Motion spec.** Trigger: click/activation. Stamp lands:
  scale 1.6 → 1.0 with opacity 0 → 1 over 120ms `--ease-stamp`,
  a 1px settle at the end (the stamp's weight), done. No exit
  animation: a stamp, once down, is down — clicking again
  *lifts* it with a plain 160ms fade (ink can be blotted, §6's
  world allows un-marking, and the tally decrements). The
  tally figure updates at the stamp's landing frame.
- **States.** Unmarked (button, prophesied figure plain) →
  stamping (120ms) → stamped (scarlet stamp beside the figure,
  button's `aria-pressed="true"`). Hover on an unstamped cell:
  a ghost of the stamp at 25% scarlet shows where it would fall
  — the reader sees the consequence before committing.
  Scrolled-past: stamps persist. Disabled: figures printed,
  buttons inert and unrendered as controls.
- **Content merge.** The stamp lands on the *figure itself*, in
  its own cell, and its count lives in the plate's own footer —
  the reader's marks join the plate's printed apparatus
  (errata count, day range) rather than floating in a toolbar.
  And the errata dagger (§6.6) outranks the stamp: a figure
  already confessed cannot be stamped (its button is disabled
  with the printed reason "ALREADY CONFESSED UPON THE SLIP") —
  the record's marks take precedence over the reader's.
- **Failure fallback.** No JS: prophesied figures print with a
  small standing "PROPH." mark in the margin (the printed
  edition's equivalent) and no buttons exist. Storage failure:
  stamps last the page view only; the tally still counts them.
- **Reduced-motion variant.** The stamp appears without press
  or overshoot — a fade of 120ms only. The ghost hover remains
  (it is a state, not a motion).
- **Performance budget & mobile variant.** Trivial: one span +
  transform per stamp. Mobile: stamps land at the cell's right
  edge rotated −3°, size 13px, so they never cover the figure
  they mark (a stamp that hides its figure has destroyed the
  evidence — forbidden).
- **Choreography timeline (v2).** Activation → 0–120ms stamp
  press (scale/opacity) → 120ms settle 1px → tally increments
  at 120ms → rest. Un-stamp: 160ms fade → tally decrements.
- **State matrix (v2).** *Rest:* unmarked or stamped per
  session. *Hover:* ghost stamp 25%. *Focus:* double-rule
  outline on the button; ghost shows (keyboard readers preview
  too). *Active:* press runs. *Scrolled-past:* persisted.
  *Disabled:* confessed figures' buttons disabled with reason
  in the label. *Touch:* no ghost; tap stamps directly; target
  is the full cell, ≥44px tall via row padding.
- **Breakpoints (v2).** ≥1200px: stamp 15px, −4°. 768–1199px:
  14px, −4°. <768px: 13px, −3°, positioned to the cell's right
  edge within the table's scroll area (§6.6's mobile form).
- **Edge cases & failure modes (v2).** *Stamping every figure
  on a plate:* licensed — the tally counts them all; at 10+
  the footer line gains the printed aside "(THE READER MARKS
  FREELY; THE SLIP WILL JUDGE)" — the almanac's wit, in its own
  voice (§12). *Print:* stamps print (they are the reader's
  marks in their copy); the tally prints its session value.
  *A figure updated by a correction:* corrections never edit
  the cell (§1) — they add errata; a stamped, later-confessed
  figure keeps its stamp beneath its dagger, both marks
  visible: belief and outcome on one line.
- **Accessibility spec (v2).** Real buttons with
  `aria-pressed`, labels naming quantity, figure and action;
  the stamp span is `aria-hidden` (the state is conveyed by
  `aria-pressed` and the tally, which is `aria-live="polite"`
  and announces "3 prophecies marked upon this plate"); scarlet
  on paper 4.5:1 at 15px bold small caps — the stamp is large
  text by weight and size and passes; the figure it marks
  remains `--ink` and fully legible beside it.
- **Tokens consumed (v2).** `--flare`, `--paper`, `--ease-stamp`,
  `--dur-stamp` (120ms), `--dur-stamp-lift` (160ms).

### 6.12 The storm plate — alerts in eclipse indigo

- **What & why.** The almanac's alarm, and its only inverted
  surface: when the record carries a geomagnetic storm warning
  (greatest Kp prophesied ≥ 7, or a flare of class X in the
  observed record), a plate prints in **eclipse indigo with the
  sun blacked out** — a paper-white disc occluded by an indigo
  circle, its corona rays printed white — carrying the warning,
  its hours, and the aurora it promises, in `--paper` type at
  8.7:1. It belongs because an eclipse is the almanac's native
  image of the sun turned dangerous and strange: the warning is
  not a red banner borrowed from software, it is the one plate
  in the volume where day is night, and readers learn to feel
  it before they read it.
- **Structure.** A plate variant (`class="plate plate--storm"`)
  inserted in calendar position (it interrupts the month it
  falls in, ruled before and after by scarlet hairlines — the
  only scarlet rules in the theme): eclipsed-sun SVG (white
  disc, indigo occluder offset by the record's eclipse
  magnitude, white ray spokes), the warning table in §6.6's
  exact form (prophesied storm figures, observed column ruled
  "TO COME" until the storm passes), and the standing line:
  "THE ALMANAC DOES NOT CRY ECLIPSE LIGHTLY: 2 SUCH PLATES IN
  THE LAST 10 SEASONS" — the plate's rarity is printed on it,
  from the record, so the alarm keeps its credit.
- **Motion spec.** The storm plate does not settle like other
  plates (§6.4's press would be frivolous here). On reaching
  the reading line: the occluder **crosses the disc over
  1,600ms `--ease-ink`** — an eclipse at eclipse speed, the
  slowest motion in the theme — while the white rays draw
  (§6.9's method, in paper white) across the same span. Then
  stillness: the storm plate has no ambient motion at all. A
  warning that fidgets is a warning ignored.
- **States.** Rest (no storm in record): the plate does not
  exist — absence is its resting state, and a quiet season
  prints no indigo anywhere. Armed (storm in record) →
  eclipsing → eclipsed (rest). Hover: the candle lamp (§6.10)
  is disabled — lamplight on an eclipse is a category error;
  links take paper-white underlines instead. Scrolled-past:
  eclipsed. Disabled: printed eclipsed (occluder at final
  offset in the DOM).
- **Content merge.** The plate is generated from the record's
  own figures (Kp, flare class, hours), sits in the calendar
  where the storm falls, uses the tables' own form, and is
  answered afterwards by the observed column and, where the
  storm missed, by the errata slip (§6.7) — the alarm is inside
  the accountability system, not above it.
- **Failure fallback.** No JS: the eclipse prints complete
  (occluder at rest offset). Watchdog `--dur-watchdog-storm`
  2,600ms forces the occluder to its final offset mid-crossing
  if the animation stalls — a half-eclipse held forever is the
  one state this element must never rest in.
- **Reduced-motion variant.** Printed eclipsed; no crossing.
- **Performance budget & mobile variant.** One SVG ≤5KB, one
  transform. Mobile: disc 160px, crossing 1,200ms, table in
  §6.6's scroll form with paper-on-indigo ruling.
- **Choreography timeline (v2).** Reading line → 0–1,600ms
  occluder crosses + rays draw → 1,600ms eclipse complete,
  warning table's figures count (§6.6, in paper white) →
  rest, motionless → watchdog ceiling 2,600ms.
- **State matrix (v2).** *Rest:* absent, or eclipsed.
  *Hover:* no lamp; link underlines. *Focus:* paper-white
  double-rule outline (8.7:1). *Active:* n/a beyond controls.
  *Scrolled-past:* eclipsed. *Disabled:* printed eclipsed.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full spread, disc 260px.
  768–1199px: disc 210px. <768px: disc 160px, plate stacks,
  scarlet rules retained (they are the plate's signature at
  every size).
- **Edge cases & failure modes (v2).** *Two storms in one
  month:* one plate per storm, each dated; the rarity line
  counts plates, not storms passed. *Storm downgraded before
  it arrives:* the plate is never un-printed (§1) — it gains a
  pasted amendment slip (miniature of §6.7, indigo stock)
  reading "THE STORM SPARED US: GREATEST KP OBSERVED 4" —
  relief is also printed, and the original warning stands
  beneath it. *False alarm fatigue:* the rarity line is the
  design's defence and §10 fails any build whose record shows
  storm plates in >15% of plates.
- **Accessibility spec (v2).** The plate is a `section` with
  `role="alert"` *only on the live warning instance* (archive
  storm plates are history, not alerts); heading announces the
  storm in text ("GEOMAGNETIC STORM PROPHESIED — NIGHTS OF 14–
  15 AUGUST"); all figures in the table form AT already knows;
  paper-on-indigo 8.7:1 throughout; the eclipse is decorative
  over complete text.
- **Tokens consumed (v2).** `--eclipse`, `--paper`, `--flare`
  (rules only), `--ink` (occluder edge), `--ease-ink`,
  `--dur-eclipse` (1,600ms), `--dur-watchdog-storm` (2,600ms).

### 6.13 Prognostication cards — the nights ahead

- **What & why.** The listing unit of the forecast: one card per
  night for the seven nights ahead, each a small woodcut plate —
  cross-hatched frame, the night's date in Playfair, its
  prophesied figures (greatest Kp, wind, aurora limit) in
  tabular Newsreader, and a one-line prognostication in italic
  ("AURORA TO 55° · BEST AFTER MIDNIGHT"). It belongs because
  the daily reader does not always want the month's table; they
  want *tonight*, and the almanac has always answered tonight
  with a small printed card's worth of type — dense, dated, and
  signed by the same record as the tables.
- **Structure.** A `<ul>` of seven `<li>` cards in a ruled row
  (grid, §11's card treatment): date head, a miniature ray-spoke
  sun whose spoke lengths encode the night's Kp (longer spokes,
  greater Kp — the same data-as-engraving rule as §6.9), three
  figure rows, the italic line, and a footer link "THE NIGHT'S
  FULL PLATE →" to the detailed plate. Cards ship fully printed
  in the DOM, in date order.
- **Motion spec.** Entry: cards print in date order as the row
  reaches the reading line — each card's frame rules draw
  (stroke, 260ms `--ease-ink`) staggered 70ms apart, figures
  already printed (a card is a clipping, not a performance; the
  stagger is the binder laying seven cards in a row). Hover:
  the card lifts as a leaf (§6.10's tilt ≤2° + lamp at the
  card's centre). No other motion; a card that has been read
  does not perform again.
- **States.** Rest: printed. Hover: lamp + tilt. Focus: the
  card's plate link takes focus; the whole card warms (§6.10's
  focus rule). Scrolled-past: printed. Disabled: printed.
  *Tonight's card* carries a standing distinction: a scarlet
  date-line rule and the printed word "TONIGHT" — position and
  text, never colour alone.
- **Content merge.** Every figure on a card is a cell of the
  forecast table (§6.6/§6.8) wearing a smaller dress — same
  record, same values, audited in §10 — and the card's spoke
  sun is its Kp in engraving. A card whose figures disagree
  with its plate is a misprint and fails the gate.
- **Failure fallback.** No JS: cards printed, frames ruled
  (the draw is armed only over printed rules). Watchdog
  `--dur-watchdog-card` 1,600ms completes any undrawn frame.
- **Reduced-motion variant.** Frames printed; no draw, no tilt;
  lamp without trail (§6.10).
- **Performance budget & mobile variant.** Seven small SVGs
  ≤1.5KB each (or one sprite), CSS transforms only. Mobile:
  cards stack in a single column of full-width rows (a card
  per night, never a horizontal card carousel — the week is
  read downward, like a calendar), spoke suns at 22px.
- **Choreography timeline (v2).** Row at reading line → frames
  draw 0–260ms staggered +70ms per card → all printed by
  ≈680ms → rest → watchdog ceiling 1,600ms.
- **State matrix (v2).** *Rest:* printed. *Hover:* lamp + ≤2°
  tilt. *Focus:* card warms via its link. *Active:* link's own
  press. *Scrolled-past:* printed. *Disabled:* printed.
  *Touch:* no lamp/tilt; the full card's link area is the
  target (≥44px).
- **Breakpoints (v2).** ≥1200px: seven across (one row) inside
  the spread. 768–1199px: four + three in two ruled rows.
  <768px: single column stack, date head left, figures right —
  a ledger of nights.
- **Edge cases & failure modes (v2).** *A night with no
  prophecy yet* (beyond the forecast horizon): the seventh
  card may print its figures as "NOT YET PROPHESIED" in italic
  with ruled blanks — the horizon is printed, not padded with
  invented figures (§1). *A storm night among the seven:* that
  card alone gains the eclipse treatment in miniature — indigo
  ground, paper type (§6.12's pairing) — one dark card in the
  row is the week's alarm, and §10 caps them at two per row.
- **Accessibility spec (v2).** List semantics; each card's
  figures are text (the spoke sun is `aria-hidden`, its Kp
  printed beside it); "TONIGHT" is text, not colour; focus
  order follows date order; contrast per §2 rulings (the indigo
  mini-card keeps paper-on-indigo 8.7:1).
- **Tokens consumed (v2).** `--paper`, `--paper-deep`, `--ink`,
  `--aurora` (spokes), `--flare` (tonight rule only),
  `--eclipse` (storm mini-card), `--ease-ink`, `--ease-press`,
  `--dur-card-draw` (260ms), `--dur-watchdog-card` (1,600ms).

### 6.14 The order coupon — subscription form

- **What & why.** The conversion section, in the only form this
  world allows: a **printed order coupon** at the foot of the
  volume, bounded by a dashed cut-line rule with a small
  scissors glyph, headed "ORDER FOR THE ALMANAC OF NEXT YEAR",
  its fields ruled like a form clipped from a back page — name,
  postal address, the edition chosen (PRINTED & POSTED /
  PRINTED & DIGITAL), and the price printed on the coupon
  itself: **$18 PER ANNUM** (§1's record). Submitting does not
  produce a toast: the coupon is **stamped "RECEIVED"** in
  scarlet (§6.11's stamp, at form scale) with the subscriber's
  number printed beneath — **№ 1214**, derived from the roll of
  1,213 (§1) — and a pasted confirmation slip joins the volume.
  It belongs because almanacs were sold exactly so, by coupon,
  and because a subscription to a publication that prints its
  errors should be taken on a form that looks like it will be
  *kept*.
- **Structure.** A `<form>` on `--paper-deep` stock inside the
  dashed rule: labels in Newsreader small caps above ruled
  input lines (inputs are transparent, borderless but for a
  bottom hairline — writing on a ruled line), edition choice as
  two radio "boxes" drawn as printed squares, the price set in
  Playfair at the coupon's foot, and the submit as a printed
  button styled as the coupon's own instruction: "CUT HERE IS
  NOT REQUIRED — PRESS TO SEND THE ORDER". Errors print beneath
  their fields in italic Newsreader with a scarlet dagger
  (§12's error voice). The confirmation replaces the form's
  fields with the stamped coupon + slip, focus moved to its
  heading.
- **Motion spec.** Focus on a field: its rule draws to full
  `--ink` (from 35%) over 180ms `--ease-ink` — the line darkens
  as the pen approaches. Submit: the coupon presses (§6.4's
  settle at form scale, 300ms) while the order is sent; on
  success the RECEIVED stamp lands at §6.11's spec, enlarged:
  200ms `--ease-stamp`, then the confirmation slip fades its
  paste shadow in over 400ms. On failure (network): no stamp; a
  printed amendment line appears above the coupon ("THE POST
  HAS FAILED US — YOUR ORDER IS KEPT UPON THIS PAGE; PRESS
  AGAIN") and the filled coupon remains, values intact.
- **States.** Rest: blank ruled coupon, price printed. Focus:
  rule darkens per field. Invalid: dagger + italic note per
  field, coupon unshaken (forms in this theme never shake — a
  coupon is paper). Submitting: press + fields disabled,
  button text "SENDING BY POST…". Success: stamped coupon +
  slip, form retired. Disabled/no-JS: the coupon prints with a
  postal fallback line ("OR BY POST TO THE ALMANAC OFFICE") —
  the conversion never depends entirely on script.
- **Content merge.** The coupon's price, the subscriber number
  and the edition names are the record's (§1, §6.17's third
  printing); the stamp is §6.11's own device promoted to form
  scale; the confirmation slip is §6.7's pasted-stock language.
  Nothing about the form is imported software furniture — no
  floating labels, no material ripples, no toast (§11 refuses
  them with these replacements).
- **Failure fallback.** Watchdog `--dur-watchdog-order`
  4,000ms (the theme's longest — the post is slow): if the
  request has not resolved, the submitting state releases with
  the amendment line above; no order is ever left "sending"
  forever, and no success is shown that the server did not
  confirm (the law applies to commerce: a RECEIVED stamp is an
  observation, never a prophecy).
- **Reduced-motion variant.** Rule-darkening and stamp are
  instant/fade-only; the press is removed; states identical.
- **Performance budget & mobile variant.** Form is HTML/CSS;
  the stamp is type. Mobile: coupon full-width, cut-line
  retained (it is the coupon's identity), fields single column,
  radio squares 24px with 44px targets.
- **Choreography timeline (v2).** Focus → rule 180ms → submit
  → press 300ms → request → success: stamp 200ms at resolve →
  slip shadow 400ms → focus to confirmation heading →
  watchdog ceiling 4,000ms on the request.
- **State matrix (v2).** *Rest:* blank coupon. *Hover:*
  fields warm faintly (§6.10 at 25%, the lamp over paper
  about to be written on). *Focus:* rule darkens; visible
  focus is the darkened rule + a double-rule outline on the
  field's row. *Active:* button press (§11). *Scrolled-past:*
  as left. *Disabled:* during submit only. *Touch:* labels
  remain above fields (never placeholder-only); targets ≥44px.
- **Breakpoints (v2).** ≥1200px: coupon two-column (name/
  address left, edition/price right) across the gutter foot.
  768–1199px: two columns within the plate. <768px: single
  column; price line stays with the submit (never separated
  from the act it prices).
- **Edge cases & failure modes (v2).** *Duplicate order* (same
  address on the roll): the confirmation slip prints the
  existing number instead — "ALREADY UPON THE ROLL AS № 1214"
  — because the roll is the record and it does not enroll
  twice. *Price changed for next year:* the coupon's price is
  rendered from the record at build; a stale cached page whose
  coupon disagrees with the colophon (§6.17) fails §10's audit
  — the volume must agree with itself.
- **Accessibility spec (v2).** Real labels, `aria-describedby`
  for the italic field notes, errors announced via
  `role="alert"` on the amendment line only (field errors are
  described, not shouted); focus order follows the coupon's
  reading order; the stamp is `aria-hidden` with the
  confirmation heading carrying its meaning ("ORDER RECEIVED —
  SUBSCRIBER № 1214"); contrast per §2 (scarlet stamp 4.5:1 at
  19px bold — large text, passes).
- **Tokens consumed (v2).** `--paper-deep`, `--ink`, `--flare`,
  `--ease-ink`, `--ease-stamp`, `--ease-press`,
  `--dur-stamp-form` (200ms), `--dur-watchdog-order` (4,000ms).

### 6.15 Ruled blanks — skeleton & loading

- **What & why.** Loading in an almanac is not a spinner; it is
  **ruled empty columns that fill with figures**. When a plate's
  table data is still arriving, the table prints its rules, its
  column heads (OBSERVED · PROPHESIED, §3's sacred pair) and its
  row heads immediately, with the figure cells ruled blank — and
  the figures ink in as they arrive, cell by cell, in the order
  the observatory reported them. It belongs because the printed
  page precedes its figures in this world's manufacture too:
  the press rules the columns before the numbers are known, and
  a reader who sees the ruled table already knows the shape of
  what is coming — layout never shifts, because the page was
  always the page.
- **Structure.** The real `<table>` (§6.6) rendered server-side
  with heads, row heads and tolerance line complete; figure
  cells contain either their figures or a ruled blank (a
  hairline mid-cell, `aria-hidden`) with `data-pending`. As
  each value resolves, the figure replaces the blank with a
  160ms ink fade. A plate-level note in italic under the table
  — "FIGURES ARRIVING FROM THE OBSERVATORY" — stands while any
  cell is pending and is replaced by the table's usual footnote
  when the last figure lands. No shimmer, no pulse: ruled paper
  does not shimmer.
- **Motion spec.** Cell ink-in: opacity 0→1, 160ms `--ease-ink`,
  in arrival order (no stagger imposed — the observatory's
  order is the choreography). The pending note cross-fades
  200ms at completion. Hard ceiling: at 3,000ms any still-pending
  cell prints "NOT REPORTED" in italic small caps — the
  almanac's honest blank, which is a *state of the record*,
  not an error spinner — and the note changes to "THE
  OBSERVATORY HAS NOT REPORTED ALL FIGURES".
- **States.** Ruled (heads + blanks) → filling (cells inking in
  arrival order) → printed (complete) or printed-with-blanks
  (ceiling reached, NOT REPORTED cells stand). Disabled/no-JS:
  server rendering ships figures inline whenever it has them —
  the ruled state is a client-arrival state only, never the
  no-JS experience.
- **Content merge.** The skeleton *is* the table — same rules,
  same heads, same tolerance line — so what loads is not a
  placeholder for the content but the content's own ruled
  form. The NOT REPORTED blank obeys the law (§1): an absent
  observation is printed as absent, never filled with the
  prophecy (the prophesied column stands beside it, visibly
  separate — the temptation the layout exists to refuse).
- **Failure fallback.** The 3,000ms ceiling *is* the fallback,
  and it is a designed print state, not a degradation. Total
  data failure prints the table fully NOT REPORTED with the
  note — a page a reader can still read, cite and return to.
- **Reduced-motion variant.** Figures appear without the ink
  fade; the ceiling and states are identical.
- **Performance budget & mobile variant.** No additional assets;
  the ruled blank is a border. Mobile: identical (the table's
  scroll form, §6.6, rules its blanks the same way).
- **Choreography timeline (v2).** t=0 table ruled, heads
  printed → figures ink per arrival (160ms each) → last figure
  → note cross-fades 200ms → printed; or t=3,000ms ceiling →
  remaining cells print NOT REPORTED → note updates → printed-
  with-blanks.
- **State matrix (v2).** *Rest:* printed (post-load).
  *Hover/focus:* as §6.6 at all times — the ruled table is
  already the table. *Active:* daggers arm only on printed
  prophesied cells. *Scrolled-past:* filling continues
  off-screen (arrival is not a performance). *Disabled:*
  printed or NOT REPORTED. *Touch:* identical.
- **Breakpoints (v2).** All: identical behaviour; the ruled
  form follows §6.6's per-breakpoint table layout exactly.
- **Edge cases & failure modes (v2).** *Figures arriving out
  of row order:* licensed and preferred — the ink order shows
  the observatory's reporting order, and the plate footer
  gains no apology for it. *A figure revised after printing:*
  never edited in place (§1) — the cell keeps its figure, gains
  a dagger, and the slip (§6.7) confesses. *Slow first paint on
  a cached page:* figures are in the HTML; the ruled state
  never appears — correct; ruling is for live arrival only.
- **Accessibility spec (v2).** The table is a table from t=0
  (AT can navigate its structure immediately); pending cells
  expose the text "not reported yet" to AT while showing the
  ruled blank visually; the completion note is
  `aria-live="polite"`; NOT REPORTED is real text in the cell.
- **Tokens consumed (v2).** `--ink`, `--paper`, `--ease-ink`,
  `--dur-ink-cell` (160ms), `--dur-pending-ceiling` (3,000ms).

### 6.16 Stitched-spread transition — page turns

- **What & why.** Moving between pages of the volume is turning
  a leaf: on navigation, a **gutter shadow crosses the page
  (~600ms)** — a soft band of `--fox`-edged shadow travelling
  from one side to the other with the **binding stitch line
  visible at its centre** — as the old spread gives way to the
  new. It belongs because the site's pages are spreads of one
  bound book (§4), and a reader who has been reading a volume
  should feel the leaf turn when they move within it; a hard
  cut would be a different book altogether.
- **Structure.** A transition layer (fixed, `pointer-events:
  none`): a 180px-wide gradient band (transparent → `--ink` at
  14% with a `--fox` warm edge) whose centre carries the stitch
  line (dashed 2px, `--ink` at 40%). The band sweeps across via
  transform; the incoming page is already rendered beneath
  (client-side routing swaps content at the sweep's midpoint,
  when the band covers the centre). The DOM of both pages is
  complete at all times; the band is pure ceremony over a real
  change.
- **Motion spec.** Trigger: in-app navigation. Band sweeps
  0–600ms `--ease-turn`, content swaps at 300ms (band at
  centre), old spread's scroll is preserved per-page by the
  router for back-navigation. No fade of content, no slide of
  the page itself — only the shadow of the turning leaf crosses.
  Rapid successive navigations: the sweep restarts from the
  band's current position (no queue, no pile-up).
- **States.** Rest: no band. Turning: band in transit.
  Interrupted (user navigates back mid-sweep): the band
  reverses from its position at the same speed — a leaf
  half-turned can be turned back. Disabled/no-JS: full-page
  loads, no band — the volume's pages still follow one another.
- **Content merge.** The stitch line at the band's centre is
  §4's gutter stitch, travelling: the binding that holds the
  spreads is the thing that moves between them. The band's
  width and shadow strength match the printed gutter exactly,
  so the transition is the layout, in motion.
- **Failure fallback.** If the router or script fails, links
  behave as ordinary links (the enhancement is layered on
  standard anchors); a stalled sweep is cleared by watchdog
  `--dur-watchdog-turn` 1,200ms, band removed — a shadow may
  never park on a page.
- **Reduced-motion variant.** No sweep; pages change plainly,
  with the destination's month rule (§6.4) briefly underlined —
  a finger's mark on the new leaf, not a turning.
- **Performance budget & mobile variant.** One gradient band,
  transform only. Mobile: band 120px, sweep 480ms; on
  <768px the stitch line is retained (it is the signature) at
  30% opacity.
- **Choreography timeline (v2).** Navigate → band enters
  0–300ms → content swaps at 300ms → band exits 300–600ms →
  destination plate's settle (§6.4) arms → watchdog ceiling
  1,200ms.
- **State matrix (v2).** *Rest:* none. *Hover:* n/a (transient
  layer). *Focus:* focus moves to the destination's heading at
  the swap (300ms) — never left on a removed page. *Active:*
  n/a. *Scrolled-past:* n/a. *Disabled:* plain navigation.
  *Touch:* identical; swipe-back gestures use the platform's
  own transition (the leaf does not fight the OS).
- **Breakpoints (v2).** ≥1200px: band 180px, 600ms.
  768–1199px: 150px, 560ms. <768px: 120px, 480ms.
- **Edge cases & failure modes (v2).** *Navigation to the same
  page (anchor within a plate):* no sweep — turning a leaf to
  reach the same spread is nonsense; anchor jumps use the
  shared lerp scroll instead. *Print:* the layer never prints.
  *Slow route fetch:* the band holds at centre past 300ms
  until content is ready (the leaf is mid-turn, honestly),
  with the watchdog releasing it at 1,200ms to the *old* page
  intact if the fetch failed.
- **Accessibility spec (v2).** The layer is `aria-hidden`,
  `pointer-events: none`; route changes are announced by the
  destination heading receiving focus and by the document
  title (the almanac's running head names the new spread);
  reduced-motion and vestibular-safe per the variant above.
- **Tokens consumed (v2).** `--ink`, `--fox`, `--ease-turn`,
  `--dur-turn` (600ms), `--dur-watchdog-turn` (1,200ms).

### 6.17 The printer's colophon — footer & the season's reckoning

- **What & why.** Every almanac ends with its printer's
  colophon, and this one carries the **season's reckoning**:
  the footer leaf prints the volume's closing accounts — days
  elapsed of the season (214 of 365), the errata tally (20),
  the subscriber roll (1,213), the price of next year's volume
  ($18) — above the colophon proper ("PRINTED FOR THE ALMANAC
  OFFICE · SET IN PLAYFAIR & NEWSREADER · THE SUN'S FIGURES
  FROM THE OBSERVATORY'S OWN TABLES") and the archive of past
  seasons, each a link to its volume. It belongs because a
  bound volume is *closed* as deliberately as it is opened: the
  reckoning lets a reader audit the whole season from its last
  leaf, and the colophon is the printer signing his work.
- **Structure.** A `<footer>` leaf across the spread: a double
  rule, the reckoning as a four-figure ruled table (label +
  tabular figure, §6.6's ruling without the prophecy columns),
  the archive row (seasons as years, linked), the colophon
  block in small Newsreader, and the volume's final line — the
  almanac's traditional closer, set in Playfair italic: "FINIS
  · THE SUN KEEPS ITS OWN HOURS" — the only "Finis" in the
  theme, printed once (§10 greps it). All figures are the
  record's (§1), rendered at build.
- **Motion spec.** The footer prints like a plate (§6.4's
  settle at half depth, 3px) as it reaches the reading line;
  its reckoning figures count (§6.6's count, 700ms) — the
  season adding itself up as the reader arrives at its end.
  Nothing else moves; a colophon is still.
- **States.** Rest: printed. Hover: archive links warm
  (§6.3's nav treatment). Scrolled-past: printed. Disabled:
  printed, figures at rest values.
- **Content merge.** The reckoning is the third printing of the
  season's master figures (hero §6.1/§6.5, errata §6.7, coupon
  §6.14) — the audit trail closes here, and §10's figure audit
  reconciles the footer's 214 / 20 / 1,213 / $18 against every
  other printing. The archive row is the volume's memory: past
  seasons are past *volumes*, each with its own errata, and the
  footer is where the set is shelved.
- **Failure fallback.** Static by construction; watchdog
  `--dur-watchdog-plate` (shared with §6.4) covers its settle
  and count.
- **Reduced-motion variant.** Printed; figures at rest.
- **Performance budget & mobile variant.** Static HTML ≤4KB.
  Mobile: the reckoning table stacks to two columns of two;
  the colophon centres; "Finis" retained at every size — the
  volume closes properly on a small leaf too.
- **Choreography timeline (v2).** Reading line → settle
  0–480ms (3px form) → reckoning counts 240–940ms → rest →
  watchdog ceiling 2,000ms.
- **State matrix (v2).** *Rest:* printed. *Hover:* archive
  link warm. *Focus:* standard. *Active:* n/a.
  *Scrolled-past:* printed. *Disabled:* printed. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: reckoning four-across across
  the spread. 768–1199px: four-across within the plate.
  <768px: two-by-two.
- **Edge cases & failure modes (v2).** *Mid-season footer:*
  the reckoning is rendered from the record *as of today* —
  days elapsed is 214, not 365; the footer of an unfinished
  season says so ("THE SEASON STILL RUNNING"). *A season
  closed:* the figures freeze at their finals and the closer
  gains the season's year. The reckoning never projects —
  projected figures in a footer would be prophecies in the
  dress of observations (§1).
- **Accessibility spec (v2).** `contentinfo` landmark; the
  reckoning is a real table with row heads; the colophon's
  small type is ≥12.5px (never below the theme's floor);
  "Finis" is text, findable and readable by AT.
- **Tokens consumed (v2).** `--ink`, `--paper`, `--paper-deep`,
  `--ease-press`, `--ease-ink`, `--dur-count` (700ms footer
  form).

### 6.18 The unprinted day — the 404 page

- **What & why.** The almanac's missing page, printed as one: a
  leaf headed "THIS DAY WAS NEVER PRINTED" in Playfair, its
  table ruled complete — column heads, tolerance line — with
  every figure cell blank and the single italic entry "NO
  OBSERVATION · NO PROPHECY · THE LEAF IS BLANK BECAUSE THE DAY
  IS NOT IN THE VOLUME", followed by the days that *are* in the
  volume (the month index, §6.3, offered as the way back). It
  belongs because a 404 in this world is not a error mascot; it
  is a day the almanac does not contain — and the almanac,
  characteristically, prints the blank honestly rather than
  pretending the day exists.
- **Structure.** A single plate: month-rule frame with no month
  name (the rule's centre is blank — the only unnamed rule in
  the theme), the heading, the blank table (§6.15's ruled form
  as a permanent state), the way-back index, and the colophon
  line. The sun (§6.1) does not appear — a day never printed has
  no sun. That absence is the page's whole illustration.
- **Motion spec.** Specified as *nearly none*: the page prints
  (no settle — §6.4's press does not dignify a blank), the way-
  back links take their ordinary hovers. One licensed motion:
  the blank table's rules draw once, 600ms `--ease-ink`, as if
  the press ruled a page for a day that never came — and stop.
- **States.** Rest: printed blank. All states identical; the
  page has no transient states. Disabled: identical.
- **Content merge.** The 404 is generated from the volume's own
  apparatus — its table is §6.6's form, its index is §6.3's,
  its blankness obeys §6.15's rule that an absent figure prints
  as absent. A visitor who lands here learns the volume's
  system from its emptiest page.
- **Failure fallback.** The page *is* a fallback; it has no
  dependencies beyond the stylesheet.
- **Reduced-motion variant.** Rules printed; no draw.
- **Performance budget & mobile variant.** The lightest page in
  the theme (≤30KB total); mobile identical in structure.
- **Choreography timeline (v2).** t=0 page printed → rules
  draw 0–600ms (where armed) → stillness.
- **State matrix (v2).** *Rest:* blank, printed. *Hover:*
  way-back links only. *Focus:* heading is the focus target on
  load (the router's rule, §6.16). *Active:* n/a.
  *Scrolled-past:* n/a (the page is short). *Disabled:*
  identical. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: blank table in the spread's
  left column, index right. 768–1199px: stacked. <768px:
  stacked, table in scroll form.
- **Edge cases & failure modes (v2).** *A day that exists but
  whose plate failed to build:* that is a defect, not a 404 —
  the build (§15) verifies every day in the record resolves to
  a plate, so the unprinted day is only ever reached for days
  truly outside the volume. *Search engines:* the page returns
  a true 404 status; the almanac does not dress its blanks as
  content for crawlers either.
- **Accessibility spec (v2).** Heading states the situation in
  words; the blank table's cells expose "no figure recorded"
  to AT; the way-back index is a labelled nav; status is never
  carried by the missing sun (an absence AT cannot see) but by
  the heading text.
- **Tokens consumed (v2).** `--ink`, `--paper`, `--ease-ink`,
  `--dur-draw-404` (600ms).

## 7. Page application map

| Page type | How the theme plays out |
|---|---|
| **Home — the current plate** | Masthead (§6.3) → hero sun + corona (§6.1–6.2) with the day-count → tonight's prognostication cards (§6.13) → the current month plate (§6.4) with its table (§6.6) → the forecast plate pinned under its aurora (§6.8) → the season so far (plates of elapsed months, condensed to their tables) → order coupon (§6.14) → colophon (§6.17). The date rule (§6.5) runs the whole descent. |
| **Month archive (listing)** | The twelve plates in calendar order, each condensed: month rule, table, margin sun (§6.9), plate footer. Elapsed months show both columns filled; the current month shows observations "TO COME" (§6.4); future months show prophecy only, observed column ruled and headed "NOT YET OBSERVED" — the archive page is the law (§1) at a glance. |
| **Day / night detail** | One day as a plate: the day's full table (hourly wind, Kp by 3-hour block), its prognostication card grown to plate size (§6.13), the night's aurora forecast with the curtain's printed form (ray-spoke, §6.9 — detail pages do not pin; the pin belongs to the home forecast plate alone), and, if the day has passed, its observed column and any dagger to the slip. |
| **Forecast page** | The aurora plate (§6.8) at full length: seven nights of cards (§6.13), the forecast table, the curtain overhead, quiet-night notes from the record. Storm nights surface the storm plate (§6.12) in calendar position. |
| **Errata page** | The slip (§6.7) grown to a page: the season's confessions by month, each entry linking back to its table and dagger; past seasons' slips archived beneath, unedited — errata are never revised, only added to. |
| **About — the Almanac Office** | Set as the volume's preface: the publication's history and method in prognostication voice (§12), its tolerance doctrine printed in full, its observatory sources named, a specimen plate. No marketing sections; the preface *is* the about page. |
| **Order / subscribe** | The coupon (§6.14) as the page: coupon, the editions' printed particulars, the postal fallback, past subscribers' reckoning (the roll count, §6.17). Checkout beyond the coupon (payment) leaves the theme's dress at the payment step — a printed note says so: "THE PAYMENT IS TAKEN BY THE OFFICE'S BANKERS, UPON THEIR OWN PAGE" — honesty about the seam (§9). |
| **404** | The unprinted day (§6.18). |

## 8. Worked examples

### 8.1 The hero (home) — the frontispiece of the season

The home page opens as the volume's frontispiece. The masthead
(§6.3) prints first — "THE SOLAR WEATHER ALMANAC" in Playfair at
84px, the season line beneath: "FOR THE YEAR OF THE SUN · 365
DAYS · PRICE $18 THE YEAR, POSTED" (the record's price, printed
where almanacs have always printed it: on the cover). The month
index runs beneath in small caps, AUGUST carrying the double rule
and the sun glyph.

Below, the hero: the woodcut sun (§6.1) centred on the spread at
300px, its face engraved and eyes closed, the corona ring (§6.2)
around it carrying "PROGNOSTICATIONS FOR THIS SEASON · OBSERVED &
PROPHESIED ·". Across the disc's lower third, the standfirst in
Newsreader 19px: "The Sun's weather, prophesied in advance and
observed in the event; where the prophecy has missed, the miss is
confessed upon the Errata Slip at the season's end." Inside the
sun's lower rays, the day-count: "DAY 214 OF THE SEASON" in
tabular figures.

**Scroll/load timeline.** t=0: masthead and standfirst are
printed (they never wait). Fonts race resolves by 700ms; the
sun's disc inks 0–700ms; rays extend 300–1,260ms in sequence;
the title mask — here the standfirst's first line — opens
500–1,100ms through the disc; the day-count ticks 900–1,800ms,
landing on 214 and stopping dead (a counter that overshoots its
record is a prophecy, and the hero prints observations). The
corona begins its spin-up at 1,800ms, reaching 0.5rpm by
4,200ms, and the reader has, by then, already read the
standfirst — the ceremony never held the text hostage, because
the text was printed before the ink performed. Scrolling, the
rays rotate toward 40° and the date rule (§6.5) wakes in the
margin at Day 214, awaiting the descent into August's plate.

### 8.2 Mid-page: the August plate (journey detail)

The reader reaches August's month rule — double hairline,
"AUGUST" in Playfair 56px, the footer-to-come promising "DAYS
213–243 OF THE SEASON". The plate settles 6px under the press
(§6.4); the margin sun draws its eight spokes (§6.9), August's
at their longest; the ribbon draws along the plate's foot,
because August's record holds aurora on 11 nights.

The plate's table (§6.6) stands in the spread's left column:

| Quantity | Prophesied | Observed | Tolerance |
|---|---|---|---|
| SUNSPOT NUMBER | 132 † | 147 | ±10 |
| RADIO FLUX 10.7CM · SFU | 168 | 171 | ±5 |
| SOLAR WIND · KM/S | 380 † | 412 | ±25 |
| GREATEST KP | 5 † | 4 | exact |
| AURORA TO LATITUDE | 55° | 55° | ±2° |

As the plate centres, the observed column counts up — 147, 171,
412, 4, 55 — staggered 90ms a row, and the three daggers ink in
last, scarlet, each a link. The tolerance line beneath reads:
"Tolerances of this table: sunspot ±10 · flux ±5 · wind ±25 ·
Kp exact · aurora ±2°. Beyond tolerance, the miss is confessed
upon the slip." A reader who follows the sunspot dagger lands on
the errata slip (§6.7), its August entry warming: "AUGUST ·
SUNSPOT NUMBER — prophesied 132, observed 147 · +15 beyond the
tolerance of ±10", and the slip's tally at its foot: "IN ALL, 20
ERRATA UPON THE SEASON" — the 17 of January–July plus August's
three, reconciled. The plate's own footer, back up the page,
prints "ERRATA UPON THIS PLATE: 3" — the same fact at plate
scale. To the right of the table, August's prognostications for
the nights ahead stand in italic-headed paragraphs, and one
prophesied figure — wind 380 — already wears a reader's stamp
from an earlier visit (§6.11): no, it does not; 380 is confessed,
and confessed figures cannot be stamped (§6.11). The stamp the
reader sees is on the flux prophecy of the *September* plate
below, placed last month, awaiting its observation. The volume
keeps its tenses straight.

### 8.3 Conversion: ordering next year's Almanac (the coupon)

At the volume's foot, above the colophon, the order coupon
(§6.14) waits inside its dashed cut-line: "ORDER FOR THE ALMANAC
OF NEXT YEAR — $18 PER ANNUM, POSTED". The reader writes their
name and postal address on the ruled lines (each rule darkening
as its field takes focus), marks the PRINTED & POSTED box, and
presses "PRESS TO SEND THE ORDER".

**Submit timeline.** Press: the coupon settles 300ms under its
small press; the button reads "SENDING BY POST…"; the request
resolves at ≈900ms; the RECEIVED stamp lands in scarlet at the
coupon's head — 200ms, one overshoot — rotated −4°, and beneath
it the confirmation slip pastes in, its shadow arriving over
400ms: "RECEIVED WITH THANKS · SUBSCRIBER № 1214 UPON THE ROLL"
— 1,213 being the roll before this order (§1, §6.17), the new
subscriber is the 1,214th, and the number is *derived*, never
invented. Focus moves to the confirmation's heading. Had the
post failed, the coupon would have kept its writing, printed
its amendment line, and waited — an order form in this theme is
a piece of paper the reader has already written on, and paper
is not cleared because a network sneezed.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The silently corrected figure.** A prophesied value edited
   after the fact to match observation. This is not a design
   flaw; it is fraud, and it kills the theme outright. *Cure:*
   the law (§1) — corrections exist only as errata (§6.7);
   §10's audit diffs published prophecy values against the
   season's first printing.
2. **Costume woodcut.** Stock "vintage" clip-art, distressed
   textures bought by the pack, a sun with clip-art rays. The
   plates must be drawn in one hand — the theme's own ray
   classes, hatch period and face (§6.1) — or the volume reads
   as a themed template. *Cure:* all illustration is built from
   the theme's declared SVG geometry; no external vintage art.
3. **Scarlet everywhere.** Errata daggers, stamps, storm rules
   and "SALE" banners all screaming at once. Scarlet is the
   confession's colour and is rationed to ≈2% (§2). *Cure:*
   the §10 scarlet census — any viewport spending scarlet
   beyond its licensed elements fails.
4. **Aurora wallpaper.** The curtain (§6.8) leaking onto other
   pages, hero backgrounds, footers. The curtain is licensed to
   one pinned plate; elsewhere the aurora is ink (§6.9).
   *Cure:* the curtain component renders only inside the
   forecast plate's stage; §10 checks for stray instances.
5. **Wobbling columns.** Figures set in a proportional font so
   counts make the table breathe. *Cure:* Newsreader `tnum`
   everywhere figures live (§3, law 1); the count is a
   textContent change inside fixed-width cells.
6. **Prophecy dressed as observation.** A forecast figure set
   in the observed column's style "because it looks cleaner",
   an estimate in an observed cell, a zero where "TO COME"
   belongs. *Cure:* the two columns' typography is fixed by
   §3's laws and §6.6's structure; §10's category audit samples
   cells against the record.
7. **The apologetic skeleton.** Shimmering grey boxes that look
   like a SaaS app wearing a paper hat. *Cure:* loading is
   ruled blanks (§6.15) — the table's own rules, printed first.
8. **Invented precision.** "Kp 4.37", "wind 412.6 km/s" —
   figures more precise than the instruments print. The
   almanac's figures are integers and printed tolerances; false
   precision is a prophecy about the instrument. *Cure:* the
   record's figures are integers; §8's tables are the standard.
9. **A mascot sun.** The woodcut sun winking, grinning, giving
   a thumbs-up in the 404. The sun's face is engraved, eyes
   closed, and absent from the unprinted day (§6.18). *Cure:*
   one sun geometry, three postings (§6.1), no expressions.
10. **Modern furniture in period dress.** Toasts, floating
    action buttons, hamburger menus with woodcut borders.
    Dressing software furniture in hatching is the theme's
    cheapest trick. *Cure:* §11's inventory — every component
    has an almanac form or is refused with its replacement.
11. **The perpetual aurora.** A forecast of quiet nights
    rendered with a vigorous curtain because it demos better.
    *Cure:* the curtain obeys the record (§6.8) — quiet Kp,
    quiet sky, printed note.
12. **Finis everywhere.** "FINIS" as a decorative sign-off on
    every page. It is printed once, in the colophon (§6.17),
    where a volume ends. *Cure:* §10 greps for exactly one.

## 10. Quality gate

Blocking checks — the theme may not ship in a build unless all
pass:

1. **Figure audit.** Every figure on the page traces to the
   Season Record: hero day-count = rail day = masthead month
   (214 · August); August table = §8.2's values; errata tally
   20 = 17 + 3 across all three printings (§6.7, §6.6 plate
   footer, §6.17); subscriber № derived as roll + 1 (1,213 →
   1,214); price $18 identical on masthead, coupon and
   colophon.
2. **Prophecy integrity.** Published prophesied values diff
   against the season's first printing: zero silent edits;
   every miss beyond tolerance carries a dagger and a slip
   entry; every dagger resolves to an entry.
3. **Category audit.** No italic observations; no figures in
   Playfair; OBSERVED/PROPHESIED heads exact, ordered,
   unabbreviated on every table; no observed cell containing an
   estimate, a zero-for-blank, or a prophecy.
4. **Watchdog drill.** Scripts killed at load, mid-ceremony and
   mid-scroll: within the longest watchdog (4,000ms) the page
   is a complete printed almanac — sun printed, plates settled,
   tables at recorded values, curtain absent or stilled,
   coupon usable by its postal fallback.
5. **Reduced-motion pass.** With `prefers-reduced-motion`, the
   full journey (hero → August plate → forecast → coupon) is
   completable and identical in content: no pin, no orbit, no
   curtain, no counts — and no missing information.
6. **Scarlet census.** Scarlet appears only as: errata daggers,
   stamps (reader's + RECEIVED), storm-plate rules, tonight's
   date rule (§6.13). Any other scarlet fails.
7. **Aurora confinement.** The live curtain renders only within
   the forecast plate; its alpha/velocity caps hold (no band
   edge above 3Hz); quiet-record forecasts render the quiet
   curtain with its printed note.
8. **Contrast audit.** Body `--ink`/`--paper` 13.0:1; storm
   plate `--paper`/`--eclipse` 8.7:1; scarlet reserved to its
   licensed large/bold uses at 4.5:1; aurora green never sets
   text under 24px nor any figure; the candle-warmed state
   (§6.10) still meets body contrast.
9. **No-JS pass.** The entire volume readable with JavaScript
   disabled: every table complete, the slip present, the coupon
   showing its postal fallback, navigation functional.
10. **Performance pass.** §14's budget met on a mid-tier Android
    over 4G: LCP ≤ 2.5s (the masthead and standfirst are LCP —
    they are printed HTML, never waited on the sun's ceremony),
    CLS ≤ 0.05 (counts and draws are transform/textContent
    only), frame budget held during the forecast pin.
11. **Finis count.** Exactly one "FINIS" in the volume
    (§6.17).
12. **Spoke audit.** Margin-sun spoke lengths and ribbon
    presence per plate match the record (daylight rank, aurora
    nights) — the engravings are data (§6.9) and are audited
    as data.

## 11. Component inventory

Every component a real site in this theme needs, with its
almanac treatment. Anything not listed is refused; anything
listed is built as described, not imported.

| Component | Almanac treatment |
|---|---|
| Buttons (primary) | A printed instruction block: `--ink` ground, `--paper` small-caps Newsreader, double-rule border; press = 1px settle (§6.14's button). Used once per plate at most. |
| Buttons (secondary) | Ruled text links with a drawn underline (180ms, §6.3); no boxes. |
| Inputs | Ruled lines on paper (§6.14): transparent field, bottom hairline, label above in small caps; focus darkens the rule. |
| Textarea | A ruled leaf: repeating hairlines at the 26px line unit; writing sits on the rules. |
| Selects | A printed list, opened as a pasted slip (§6.7's stock) with the options as entries; native `<select>` beneath for AT and no-JS. |
| Radio / checkbox | Printed squares (radios) and dagger-marks (checkboxes read as † when marked — the almanac's own tick); 24px glyph, 44px target. |
| Tables | §6.6's form is the only table form in the theme. |
| Badges | Refused. A figure's status is printed beside it in words ("TO COME", "CONFESSED"); a coloured pill is software furniture. |
| Alerts | The storm plate (§6.12) for record-level warnings; inline amendment lines (§6.14) for form-level notices. No banners. |
| Pagination | The month index (§6.3) and "NEXT PLATE →" rules at plate feet; numbered page lists are refused — the volume is navigated by its calendar. |
| Modal | Refused. Anything worth saying is printed on a plate or pasted as a slip (§6.7); nothing in an almanac floats above the page. |
| Toast | Refused. Confirmations are stamps and slips (§6.14); errors are amendment lines. |
| Tabs | Refused. Months are sequential plates, not tabs; editions on the coupon are radios. |
| Accordion | The archive's past seasons: each season a plate whose plates are listed when its rule is followed — implemented as ordinary links/pages, not disclosure widgets; where an index must collapse (mobile secondary nav), a printed contents disclosure (§6.3) is used. |
| Cards | Prognostication cards (§6.13) are the only card form. |
| Search | "The Index of Days": a page set as the volume's index — alphabetical entries (AURORA · ERRATA · SUNSPOT) with day references as links; the search field is a ruled line (§6.14's input) and results print as index entries, not as cards. |
| Breadcrumbs | A running-head line: "THE SEASON › AUGUST › THE NIGHT OF THE 14TH" in small caps — the volume's own foliation. |
| Progress | The date rule (§6.5); no other progress component exists. |
| Loader | Ruled blanks (§6.15); spinners are refused absolutely. |
| Tooltip | A margin note: on focus/hover, a small italic note prints in the margin beside the term (definitions from the volume's glossary); never a floating grey box. |
| Skip link | A printed line at the volume's head: "PASS TO THE CURRENT PLATE" — styled as the first line of the contents. |

## 12. Content & copywriting voice

The almanac speaks in two registers, and the boundary between
them is the law (§1) wearing a voice.

**The Observatory register** (observations, tables, reckonings):
plain, past-tense, numbered. Headlines state the fact with its
figure: "SUNSPOT NUMBER 147, THE SEASON'S HIGHEST". Labels are
the sacred small caps of §3. Sentences are short; nothing is
"exciting"; a record does not enthuse.

**The Prognosticator register** (forecasts, prognostication
headings, the preface): italic-headed, future-tense, hedged with
the almanac's own calibrated phrases — "IS EXPECTED", "MAY BE
SEEN TO", "THE ALMANAC VENTURES" — and never more certain than
its tolerances. A prophecy that sounds like a fact has broken
the register and, with it, the law.

- **Headline style.** Observatory: "THE WIND AT 412 KM/S, AND
  RISING AT THE LAST REPORT". Prognosticator: "*Aurora may be
  seen to 55° upon the nights of the 14th and 15th*". ✓ both.
  ✗ "HUGE SOLAR STORM SMASHES EARTH!!" (news voice, scarlet
  thinking); ✗ "Solar Weather Update #214" (software voice).
- **Label style.** Small caps, nouns, no verbs: OBSERVED ·
  PROPHESIED · TOLERANCE · ERRATA UPON THIS PLATE · DAY 214 OF
  THE SEASON. ✗ "Click here to see more" — the almanac says
  "THE NIGHT'S FULL PLATE →".
- **Error-message voice.** The post has failed us; the office
  regrets; the figure has not reported. Errors are printed as
  amendments in the almanac's own person: "THE POST HAS FAILED
  US — YOUR ORDER IS KEPT UPON THIS PAGE; PRESS AGAIN." Field
  errors: "THE ADDRESS WANTS A TOWN — A LETTER CANNOT TRAVEL
  WITHOUT ONE." ✗ "Invalid input"; ✗ "Oops! Something went
  wrong."
- **Empty-state voice.** Absence is printed as a fact of the
  record: "NOT REPORTED", "OBSERVATIONS TO COME", "NONE
  RECORDED — THE ALMANAC NOTES THIS WITH SUSPICION" (§6.7).
  ✗ "Nothing here yet 🎉" — the almanac does not celebrate a
  blank, it rules it.
- **Confirmation voice.** Stamps and slips (§6.14): "RECEIVED
  WITH THANKS · SUBSCRIBER № 1214 UPON THE ROLL". The
  confirmation states what is now true and its number; it does
  not congratulate.
- **Fixed strings (verbatim, never paraphrased).** "DAY N OF
  THE SEASON" · "IN ALL, N ERRATA UPON THE SEASON" · "THE
  ALMANAC REGRETS ITS ERRORS AS IT REGRETS THE WEATHER:
  PUBLICLY, AND IN PRINT" · "NOT YET PROPHESIED" · "FINIS ·
  THE SUN KEEPS ITS OWN HOURS".

## 13. Full-page scroll choreography map

The home page, top to footer, in order. Every beat names its
trigger and what the visitor sees and feels; beats are
ratcheted (§5) except the scrubbed instruments, which are
marked.

| # | Beat | Trigger | What happens | What it feels like |
|---|---|---|---|---|
| 1 | The masthead stands | Load | Nameplate, season line, month index printed; August's rule draws 400ms | A volume opened at its title page |
| 2 | The sun inks | Fonts ready | Disc inks 700ms; 24 rays extend in sequence to 1,260ms; standfirst's first line unmasks through the disc | The frontispiece being printed for you |
| 3 | The count lands | 900–1,800ms | Day-count ticks to 214 and stops dead; corona begins its 2,400ms spin-up to 0.5rpm | The season's date, settled; the promise begins its slow circling |
| 4 | The descent begins | First scroll | Rays rotate toward 40° (scrub); date rule wakes in the margin at Day 214 (scrub) | Turning from the frontispiece into the year |
| 5 | Tonight's cards | Cards row at line | Seven frames draw in date order, 70ms stagger; tonight's card wears its scarlet rule | The week laid out as clippings |
| 6 | August settles | Month rule at 62% | Plate presses 6px; gutter shadow sweeps; illustration scales home | A new month under the reader's hand |
| 7 | The observations arrive | Settle +240ms | Observed column counts to 147 · 171 · 412 · 4 · 55; three daggers ink in scarlet last | The record filling with what actually happened — and where it hurt |
| 8 | The margin engraves | Settle +480ms | Margin sun's spokes draw; the aurora ribbon draws along the plate's foot | The month being illustrated as it is read |
| 9 | The sky performs | Forecast plate pins | 160vh pin; curtain ripples overhead, answering scroll velocity, settling to a breathe at rest | The forecast happening above its own table |
| 10 | The season so far | Scroll resumes | Elapsed months' plates settle in turn, condensed; each table already printed (their counts run only on first arrival, quietly) | The year passing under the hand, faster now |
| 11 | The coupon | Coupon at line | Cut-line and ruled fields print; the price stands at its foot | The volume asking, plainly, to be continued next year |
| 12 | The reckoning | Footer at line | Colophon settles 3px; 214 · 20 · 1,213 · $18 count up; FINIS prints once | The book closing its own accounts |

**Reverse pass.** Scrolling up: scrubbed instruments (rays,
date rule, curtain if re-entered) follow back; every printed
beat stays printed — the reader re-reads a finished volume.
**Jump scroll** (scrollbar drag, anchor leap): all queued beats
complete instantly at duration 0 (§6.4); the page found is the
page printed.

## 14. Whole-page performance budget

| Budget line | Limit | Notes |
|---|---|---|
| Total page weight (home, first load) | ≤ 860KB | HTML + CSS + JS + the hero sun and one plate illustration; remaining plate illustrations lazy-print below the fold |
| Inline SVG (sun §6.1 + corona §6.2) | ≤ 11KB | The hero's entire ceremony is inline; no hero image request exists |
| Plate illustrations | ≤ 38KB each, ≤ 6 loaded before first interaction | Woodcut plates compress brutally (2–3 colours); line plates ship as SVG ≤ 6KB |
| JavaScript | ≤ 55KB gz | One lerp loop, one observer, counters, curtain, coupon — no framework on the reading pages |
| CSS | ≤ 38KB gz | Tokens + plate system; the hatching and frames are gradients, not images |
| Fonts | Playfair Display (2 cuts) + Newsreader (3 cuts), subset, ≤ 120KB total | `font-display: swap` with the §6.1 race; figures must land in Newsreader or the tables hold at ruled blanks (§6.15) rather than flash in a fallback face |
| Animation frame budget | ≤ 1.6ms script per frame | Lerp loop + curtain (≤0.9ms) + at most one counter set; the curtain pauses off-screen, the loop sleeps at rest (§5) |
| Long tasks | None > 50ms after load | Counting and drawing are rAF-distributed; no single task may block a plate settle |
| LCP / CLS | ≤ 2.5s on 4G mid-tier Android / ≤ 0.05 | LCP is printed HTML text (§10 check 10); CLS is zero by construction (fixed tabular cells, pre-ruled tables, frames sized in CSS) |

**Cut order when the budget is exceeded** (cut in this order,
never silently): (1) plate illustrations below the fold drop to
their line-SVG form; (2) the grain shimmer loop is cut (it is
subliminal by design — §5); (3) the curtain drops to the CSS-div
fallback at all sizes; (4) corona spin-up shortens to 1,200ms.
**Never cut:** any watchdog, the tolerance lines, the errata
apparatus, the ruled-blank loading state, or the reduced-motion
variant. A build that meets budget by cutting honesty has failed
§10 regardless of its numbers.

## 15. Build-order checklist

1. **The Season Record first.** Encode the record (365 days, 12
   plates, today's day, all figures, tolerances, errata, roll,
   price) as the single data source every component reads. No
   component hard-codes a figure.
2. **The printed volume, static.** Masthead, plates, tables,
   slip, coupon (with postal fallback), colophon — complete,
   legible, navigable with no JS and no motion. This is the
   product; everything after is the printing of it.
3. **Tokens & type.** §2's palette as CSS variables, §3's scale
   and laws, tabular figures verified in columns.
4. **The gutter & spread system.** §4's layout, frames, margin
   rail space reserved (the date rule's absence must not shift
   layout when it arms).
5. **The shared loop & observers.** §5's one rAF lerp engine;
   every scrubbed value registered with it; sleep conditions
   tested.
6. **Watchdogs before ceremonies.** Every `--dur-watchdog-*`
   implemented and drilled (§10 check 4) *before* the animation
   it guards is written — a ceremony without its watchdog does
   not merge.
7. **The sun & corona (§6.1–6.2)**, session rationing included.
8. **Plates & tables (§6.4, §6.6, §6.15)** — settle, counts,
   daggers, ruled blanks, in that order.
9. **The date rule (§6.5)** and its three-printings
   reconciliation with §6.1/§6.3.
10. **The slip (§6.7)** and dagger round-trip focus behaviour.
11. **The forecast plate & curtain (§6.8)** with velocity caps
    and the quiet-record ruling; then the storm plate (§6.12).
12. **Engravings (§6.9)**, cards (§6.13), lamp (§6.10), stamps
    (§6.11) — the reader's layer, after the record's layer
    stands.
13. **The coupon (§6.14)** end-to-end: focus rules, press,
    stamp, slip, amendment line, watchdog, duplicate-roll case.
14. **Transitions, colophon, unprinted day (§6.16–6.18)**; the
    Finis grep wired into the build.
15. **The gate.** §10's twelve checks run by a builder who did
    not build the theme; failures return to the step that owns
    them. The theme ships when the gate passes — not when the
    words are long.
