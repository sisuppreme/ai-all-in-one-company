# 67. Calibre & Escapement — Expanded (v1 + v2)

A watchmaker's calibre diagram come to life: the site is built like a
movement — gears, jewels and bridges — and every interaction is timed like
a mechanism. This expansion writes that idea to the full 50x standard:
fifteen sections, eighteen elements with complete build specs, and one
declared calibre record (§6.17) from which every number on the page is
taken. Nothing here is generic horology wallpaper. The balance wheel beats
at a true 28,800 vibrations per hour because the record says it does; the
gear train's ratios are the record's tooth counts divided out; the form's
confirmation number is the service register's next entry. If a figure
cannot be traced to §6.17, it does not ship.

**The theme's one law: every wheel on the page turns something — nothing
is pictured that is not also working.** A gear that spins for decoration
is a lie a watchmaker can see. So the margin train is driven by the
reader's actual scroll velocity, the mainspring barrel fills with actual
reading progress, the beat counter counts the actual beats of the wheel
beside it, and the spec table lists the page's own movement — its real
component count, its real interactive elements as jewels, its real
session length as power reserve. The mechanism is the interface; the
interface is the mechanism. Everything in this file is downstream of
that law.

---

## 1. Concept & world

The world is the watchmaker's bench, seen through the loupe: a rhodium
mainplate brushed with Geneva stripes, bridges spanning the content like
bridges span a movement, jewel bearings glowing ruby at every pivot
point, blued-steel screws and hands, gilt lettering reserved for the
calibre's name and its totals. The visitor is not browsing a website;
they are holding a movement up to the light and turning it slowly in
their fingers. Reading is winding. Scrolling is the crown. Hovering is
the loupe. Clicking is a tick of the escapement — one tooth, no more.

The mood is precision you can hear in your eyes: quiet, exact, faintly
ceremonial. Nothing bounces for joy. Nothing floats. Every motion in
this theme terminates in a settle — a tooth seating, a letter casing, a
bridge screwing down — because a movement is a machine for arriving
exactly and staying there. Where other themes use ease-out curves, this
one uses the escapement's own physics: advance, catch, recoil a hair,
lock. The page should feel like it was regulated, not designed.

**Best-fit sites and audiences.** A watch manufacture or independent
watchmaker first — the theme is native there. Beyond horology it fits
any maker whose product is a precision mechanism or a timed craft:
camera-lens and microscope makers, high-end audio (turntables, tape
machines), precision machining and metrology services, observatory and
planetarium programmes, a master restorer's portfolio, an engineering
firm that wants its tolerances felt rather than stated. The audience is
the connoisseur-reader: patient, detail-literate, willing to watch a
number count because the number is true. This theme rewards slow
reading; its ambient loops run on timescales of seconds and minutes,
not milliseconds of confetti.

**When NOT to use it.** Never for anything that must feel fast, loud or
cheap: flash sales, youth streetwear, food delivery, meme content,
anything with a countdown-to-buy urgency. Never where the content
cannot supply real figures — the law requires a record, and a page
whose numbers are invented collapses the whole conceit (see §9). Never
for a data-dense dashboard: the movement architecture spends space on
bridges and apertures that a 40-column table cannot afford. And never
as a skin over an unrelated template — the layout language (§4) is the
movement's architecture, not a colour scheme; if the bridges do not
span real content blocks and the jewels do not sit at real pivots, the
theme has not been used, only quoted.

**The one record.** §6.17 declares Calibre C&E 67 "Atelier No. 7" in
full: 28,800 vph, 212 parts, 27 jewels, 62 hours of reserve, a barrel
that turns 6.5 times from let-down to full wind, a going train of
84 / 60 / 48 / 40 / 15 teeth, an escape wheel that advances one tooth
per beat, a balance of ±270° amplitude, regulation at +4 seconds per
day, and a service register standing at 1,137 entries. Every element
below cites the figures it consumes. §10's quality gate re-derives
them. A builder who changes a number in §6.17 must change it
everywhere, or the gate fails — that is the point of having one record.

---

## 2. Palette

Five anchors from the original entry, held exactly. Rhodium plate is the
ground — a movement is read against its plate. Blued steel is the
working accent: screws, hands, links, the train. Jewel ruby is rationed
to bearings and to the single moments of regulation truth. Gilt is the
ceremonial metal: the calibre's name, totals, the wind arc — never body
text on the plate, where its contrast fails. Ebony is the bench beneath
the movement and the ink of display type.

| Token | Hex | Role | Usage ratio | Pairing & contrast |
|---|---|---|---|---|
| `--plate` | `#D9D7D2` | Mainplate ground; section fields; card faces | ~62% | Ground for `--ink` (11.8:1) and `--steel` (5.9:1) |
| `--steel` | `#2B4C7E` | Blued steel: links, screws, hands, train strokes, focus rings | ~14% | On `--plate` 5.9:1 — text-grade for labels ≥14px and all UI |
| `--ruby` | `#9E1B32` | Jewel bearings; regulation marks; the one error colour of the bench | ~3% | On `--plate` 6.8:1 — headings/marks only, never body copy |
| `--gilt` | `#B08D3C` | Calibre name, totals, wind arc, hairline rules on ebony | ~6% | On `--ebony` 5.6:1; on `--plate` 2.9:1 — **never text on plate** |
| `--ebony` | `#17181A` | Bench ground (footer, 404, apertures' depth); display ink on plate | ~15% | On `--plate` 11.8:1; `--plate` on it 11.8:1 |

**Derived tokens** (computed from the anchors; a builder uses these
names and no others):

| Token | Value | Derivation / use |
|---|---|---|
| `--plate-shadow` | `#B9B6AF` | Plate shaded one step — bridge undersides, aperture rims, pressed states |
| `--plate-deep` | `#A8A49B` | Perlage fields, skeleton plates, disabled grounds |
| `--steel-bright` | `#4A6FA5` | Blued steel under the loupe / on hover — heat-lightened, never a new hue |
| `--steel-deep` | `#1E3659` | Steel in ebony apertures; the train's shadow side |
| `--ruby-bright` | `#C22747` | A jewel lit by the loupe or seating — saturation lift only, ≤300ms at a time |
| `--gilt-pale` | `#D6BC7E` | Gilt at reading distance: wind-arc track, hairlines on plate |
| `--ink` | `#26282B` | Body text on plate (12.9:1) — softer than ebony, still text-grade |
| `--hairline` | `#8F8B83` | Rules, table strokes, the chapter ring's minute track on plate |

**Usage discipline.** The plate dominates because a movement is mostly
plate; a page that is mostly ruby or mostly gilt is a jewellery shop,
not a calibre. Ruby's 3% is a hard census (§10 counts it): 27 jewel
bearings exist in the record and the page sets exactly 27 — ruby appears
at those bearings, at the regulation mark in §6.13, and nowhere else.
Gilt appears where a watchmaker would engrave and fill: the calibre
name, totals rows, the wind arc, the register number on a confirmation.
Blued steel does all the ordinary work of an accent colour — if an
element wants emphasis, it turns steel first.

**Dark-mode behaviour.** There is no separate dark theme; the movement
has two native grounds and the page uses both in daylight order: plate
sections for reading, ebony sections where the movement is opened over
the bench (the spec chapter, the footer, the 404). An ebony section
inverts text to `--plate`, steel to `--steel-bright` for contrast
(6.1:1 on ebony), gilt stays gilt (5.6:1). A builder must not invent a
third ground. `prefers-color-scheme: dark` changes nothing structural —
it swaps which ground the *hero* opens on (ebony bench, movement laid
on it) and leaves the section order intact.

---

## 3. Typography

Three voices, each with a bench job. **Instrument Serif** is the
engraver's hand: display type, the calibre name, section titles — set
the way a name is engraved on a bridge, in one line, never stacked for
effect. **Inter** is the specification voice: body copy, labels, table
text, form fields — the neutral hand of a technical document.
**IBM Plex Mono** is the readout voice: beat rates, tooth counts,
register numbers, every figure that the movement itself would print.
The original entry names a "mono readout" for the beat counter; this
expansion gives that readout its typeface and confines it to readouts —
mono never sets a paragraph.

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Display (calibre name, hero) | Instrument Serif | clamp(2.75rem, 6vw, 4.5rem) / 1.04 | −0.01em | One line where possible; italic only for the calibre's nickname |
| Section title | Instrument Serif | 2rem / 1.12 | −0.005em | Sits on its bridge (§4); never centred |
| Bridge label | Inter 600 | 0.8125rem / 1.3 | +0.14em, uppercase | The label a bridge would carry engraved: part name + count |
| Body | Inter 400 | 1rem / 1.62 | 0 | Measure 34–38rem; numerals in body copy are tabular |
| Specification | Inter 400/500 | 0.875rem / 1.5 | +0.01em | Table and spec text; values right-aligned in `--mono` |
| Readout / data | IBM Plex Mono 500 | 0.8125–1rem / 1.4 | +0.02em | Every live figure: vph, beats, teeth, hours, register № |
| Caption / bench note | Inter 400 italic | 0.8125rem / 1.5 | 0 | The watchmaker's aside; max two per section |

**Type laws.** (1) *Numerals are always mono or tabular* — a
proportional figure in a readout is a defect, because readouts are
compared column-wise like a timing machine's tape. (2) *Instrument
Serif never sets a number that matters* — display numerals in the serif
are for the calibre name's "67" only. (3) *Uppercase is engraved, not
shouted*: bridge labels and table headers only, always letterspaced,
never above 0.875rem. (4) *No text between 1.0625rem and 1.9375rem* —
the scale jumps from body to section title the way a movement jumps
from wheel to bridge; mid-size mush is how this theme goes slop (§9).
(5) *Gilt text only on ebony* (§2's contrast ruling), set in the serif
or in spaced uppercase Inter — the two engraved voices.

**Loading behaviour.** Fonts are the movement's parts and are loaded
like them: `font-display: swap` with the fallback stack (Georgia for
the serif, system-ui for Inter, ui-monospace for the readout) sized by
`size-adjust` so the cased headline (§6.2) does not change measure when
the true faces arrive. The assembly sequence (§5) does not wait for
fonts beyond a 900ms race (§6.2's watchdog) — a movement that cannot
start because a part is late is a movement that ships its fallback and
starts anyway.

---

## 4. Layout language

The page is a mainplate and the content is laid out the way a calibre
is laid out: a going train of sections runs down the reading column in
drive order, bridges span across the column to carry the sections that
bear load, jewel bearings sit at the pivot points where a section's
argument turns, and the margin is the movement's edge — where the
balance wheel, the gear train and the mainspring barrel live and work
for the whole read. Nothing is placed because a grid had a hole; things
are placed where the mechanism needs them.

**Grid and measures.** ≥1200px: a three-zone plate — left margin rail
152px (the train, §6.3), reading column max 44rem, right margin rail
152px (balance wheel §6.1 above, barrel §6.5 below), gutters 32px. The
rails are not sidebars; they are the movement's edge, and their contents
are pinned for the full read. 768–1199px: rails narrow to 88px and
carry only the wheel and barrel; the train moves to a horizontal strip
under the masthead. <768px: single column, rails dissolve — the wheel
shrinks to a 64px instrument in the masthead, the barrel becomes a gilt
arc across the top of the reading column, and the train is cut (§14's
cut order protects the wheel and barrel first).

**Bridges.** A bridge is a full-width band of `--plate-shadow`-edged
plate that spans the reading column and both gutters, carrying a
section's title on its left, its bridge label (part name + count, §3)
on its right, and two blued screws at its ends — the screws are real:
they are the section's anchor links, and their slots rotate 90° when
the section is the reader's current one (§6.11). Sections that carry
data (the spec table, the register) get a bridge; prose sections flow
on open plate between bridges, the way wheels turn in the open between
a movement's bridges. Maximum one bridge per section, minimum one per
three sections — a page of nothing but bridges is a movement with no
wheels visible.

**Jewel bearings.** At each point where a section's content pivots — a
card's corner, a table's totals corner, the form's submit pivot, the
point where a bridge meets the column — a ruby bearing is set: a 10px
ruby disc in a gilt chaton ring, drawn in SVG, still. There are exactly
27 on a full page, allocated in §6.17, and §10 counts them. A bearing
never sits somewhere merely decorative; if a builder cannot name the
pivot, the bearing is not set.

**Geneva stripes and perlage.** The plate's ground carries Geneva
stripes: broad vertical bands of alternating `--plate` and a 3%-darker
plate tone, 96px period, visible only where no content sits — under
text the stripes fade to flat plate, because finishing is for the
movement's open faces, not a texture under reading. Circular perlage
(a field of overlapping 28px polished circles at 4% contrast) appears
only on skeleton/loading plates (§6.15) and the 404 (§6.18). Both
finishes are CSS gradients, zero raster cost, and both are cut before
any mechanism is cut (§14).

**Density and whitespace.** Whitespace in this theme is the air between
wheels: exact, functional, never padded for luxury. Section gaps are
96px (the "held beat" — long enough for the previous section's settle
to finish in the reader's eye). Inside a section, related figures sit
16px apart, groups 40px. The reading column's measure (44rem) is the
movement's diameter made text: at 30.4mm in the record, the column is
the calibre opened to reading size, and every aperture (§6.12) is
sized as a multiple of the same module (aperture Ø = column ÷ 3,
÷ 4, ÷ 6).

**Section choreography.** Sections arrive in assembly order, which is
also the movement's drive order: plate (hero) → bridges (the argument's
load-bearers) → train (how it works) → escapement (the proof) →
barrel (the offer) → register (the record). A page type may omit a
movement, never reorder the train: you cannot meet the escapement
before the wheels that drive it. §13 maps the full scroll.

---

## 5. Full motion system

One shared `requestAnimationFrame` loop drives every scrubbed value in
the theme — scroll position, gear angles, barrel wind, cage rotation,
loupe position — through a single lerped progress value per element
family. There are no independent scroll listeners and no CSS scroll
timelines; a second loop is a second movement, and the page has one
movement. The master lerp is **0.12** for scroll-driven values (the
page feels geared, not glued), **0.055** for the balance wheel's own
phase (it answers to time, not to the reader), and **0.2** for the
loupe (the hand is quicker than the page).

**Named easings — the escapement's own.** Every duration in §6 cites
one of these five; a builder who reaches for a generic `ease` has left
the bench.

| Token | Curve | Bench meaning | Used for |
|---|---|---|---|
| `--ease-tick` | `steps(1)` + 40ms hold | One tooth advances and locks | Clicks (§6.9), digit flips (§6.6), screw turns |
| `--ease-settle` | `cubic-bezier(.2,1.6,.3,1)` damped, 180ms | Overshoot 2px / 1.5°, one recoil, lock | Casing (§6.2), cage steps (§6.4), bridge drops |
| `--ease-slew` | `cubic-bezier(.3,.7,.2,1)`, velocity-fed | A gear spun by a hand: fast, then tooth-by-tooth | The train (§6.3) |
| `--ease-draw` | `linear` at stated px/s | A line drawn by a steady hand at the bench | Profile draws (§6.7), rules, underlines |
| `--ease-beat` | `sin(t·π)` phase | The balance's own sinusoid — dwell at extremes | The wheel (§6.1), the sheen's phase (§6.10) |

**Every motion term, in this theme's language** (the standard requires
each term applied or refused with an in-world reason):

- **Scroll-triggered reveals** — sections step in by cage (§6.4):
  rotate 1.5°, translate 12px → register, 60ms two-step lock.
- **Scroll-driven / scrubbed animation** — the train (§6.3) and barrel
  (§6.5) are pure scrub: angle and wind are functions of lerped scroll
  position and velocity, reversible at every pixel.
- **Parallax** — three movement depths only: plate 1.0×, bridges 0.97×,
  jewels/apertures 0.94× — the depth of a movement under a crystal,
  never a landscape's sprawl. Amplitudes ≤18px over a section's travel.
- **Pinned sections** — the margin instruments pin for the whole read;
  the spec table's bridge pins for its own section (§6.13) while its
  rows scroll beneath — the one content pin, used once.
- **Smooth scrolling** — native scroll, lerped read-out: the page
  itself is never hijacked; the *instruments* smooth what they report.
  Ratchet feel comes from the cage steps and the train's settle, not
  from fighting the reader's wheel.
- **Progress indicator** — the mainspring barrel (§6.5): a gilt wind
  arc filling to 6.5 turns at the footer's threshold.
- **Staggered reveals** — assembly order (§6.2): plate → bridges →
  jewels → wheel, 150ms between families, never a uniform cascade.
- **Masked reveals** — the cased headline is revealed through the
  movement's circular aperture (§6.2): a real mask with a real rim.
- **Blur-to-sharp** — refused for text (a calibre is never out of
  focus); licensed only for the loupe's edge falloff (§6.8), where
  blur is the instrument's optics.
- **Kinetic typography** — refused. Letters in this theme are cased,
  screwed or flipped like split-flap digits (§6.6) — they are never
  stretched, bounced or danced. Type behaves like parts.
- **Marquee** — refused. Nothing in a movement travels sideways
  forever; the chapter ring (§6.16) rotates at the seconds hand's
  pace, which is the closest this theme comes, and it is a dial.
- **Counters** — mechanical digit flips only (§6.6): a figure changes
  by flipping to the next engraved digit, never by tweening through
  fractional values a timing machine could not print.
- **SVG line-draw** — the gear profile and hairspring (§6.7), drawn at
  stated rates in assembly order.
- **Image scale-in-frame** — plates scale 1.04 → 1.0 inside their
  polished apertures (§6.12), as a movement settles under its crystal.
- **Hover / magnetic / tilt micro-interactions** — the loupe (§6.8)
  is the hover; tilt is capped at 2° and belongs to bridges only,
  pivoting on their screws like a movement tilted in the hand.
  Magnetic pull is refused — parts do not lean toward fingers.
- **Custom cursor** — refused, absolutely. Normal system cursor only;
  the loupe is an element on the page, not a cursor replacement.
- **Skeleton loading** — unfinished plates gaining jewels (§6.15).
- **Page transitions** — the cage rotation (§6.15): old page steps
  out, new page steps in, 60° of cage travel, never a fade.
- **Ambient loops** — exactly two are licensed: the balance wheel
  (§6.1, it *is* the theme) and the Geneva sheen (§6.10, 14s). A third
  ambient loop fails §10.
- **Reduced motion** — the movement rests fully assembled (§6 per
  element): wheel stopped at its drawn position, train at rest angle,
  barrel showing true progress as a static arc, all content printed.
  Nothing is hidden, greyed or apologised for — a stopped movement is
  still a movement.

**Watchdog law.** Every JS-armed pre-state (uncased letters, unstepped
sections, unflipped digits) carries a named timeout — 1,000–3,000ms per
element in §6 — after which the element assumes its final, readable
state regardless of what failed. The DOM ships complete and legible;
JavaScript arms the *starting* positions only. A page whose script
never runs is a movement at rest, fully readable — §10 drills this by
killing the script and reading the page.

---

## 6. Signature elements

### 6.1 The beating balance wheel

- **What & why.** An SVG balance wheel with a drawn hairspring, pinned
  in the right margin rail, oscillating at the record's true rate —
  28,800 vph, 4 Hz, ±270° amplitude with sinusoidal dwell — for the
  entire read. It is the theme's heartbeat and its proof of law: the
  wheel is not a picture of a balance, it is a clock the page keeps.
  The beat counter (§6.6) counts this wheel's beats; if the wheel
  stopped and the counter kept counting, the page would be lying, and
  the law (§1) forbids it.
- **Structure.** One inline SVG (Ø 120px in the rail): an annular rim
  with four gilt timing screws, two crossing arms, a blued hairspring
  spiral of 7 coils (§6.17) drawn as a single path, and a ruby impulse
  jewel at the staff. Rotation is applied to the wheel group only; the
  hairspring "breathes" by scaling its path's coil spacing ±2% in
  anti-phase — a transform on the group, not a path redraw. The whole
  instrument sits inside a polished aperture ring (`--plate-shadow`
  rim, 1px `--hairline`).
- **Motion spec.** Continuous time loop from the shared rAF loop's
  clock channel: angle θ(t) = 270° · sin(2π · 4 · t). Period 0.5s per
  full oscillation, 0.25s per beat; dwell at extremes is the
  sinusoid's own, not an added pause. Phase is read from
  `performance.now()` so a throttled tab resumes in true phase — the
  wheel never "catches up" with a spin. Start: on load, the wheel is
  already beating (a movement is delivered running); there is no
  start-up animation.
- **States.** Rest = beating (rest *is* motion here; the still state
  is the exception). Hover: none — the wheel ignores the pointer, it
  keeps the page's time, not the visitor's. Focus: the wheel is not
  focusable. Scrolled-past: it is pinned in the rail; there is no
  past. Tab hidden: rAF stops, phase is clock-derived, so on return
  the wheel is simply correct. Reduced-motion: stopped at θ = +38°,
  the drawn position in §6.17, hairspring at rest spacing.
- **Content merge.** The wheel beats beside the copy for the whole
  read and its beats are the page's unit of time: the beat counter
  (§6.6) tallies it, the chapter ring (§6.16) is stepped by it, the
  regulation mark (§6.13) is a claim about it (+4 s/day). Remove the
  copy and the wheel is a toy; remove the wheel and three other
  elements lose their source. That interlock is the merge.
- **Failure fallback.** Watchdog `WD-WHEEL` at 2,000ms: if the rAF
  loop has not ticked, the SVG is left at its shipped static angle
  (+38°, set as the group's initial transform in markup) and the beat
  counter switches to its printed static value "28,800 VPH" (§6.6) —
  the page shows a stopped movement and a true specification, never a
  frozen mid-swing blur. No JS: identical stopped state.
- **Reduced-motion variant.** Wheel stopped at +38°, hairspring at
  rest, counter printed statically. The rail keeps the instrument —
  a stopped balance is still the calibre's portrait — and §12's voice
  rules forbid any copy apologising for the stillness.
- **Performance budget & mobile variant.** One SVG group transform per
  frame; ≤0.05ms/frame; no layout, no paint beyond the aperture.
  Mobile (<768px): the wheel moves to the masthead at Ø 64px, still
  beating (it is §14's last cut, never taken); the hairspring drops
  to 5 coils for legibility at size.
- **Choreography timeline (v2).** t=0 page load → wheel already at
  phase θ(now) → beats continue 8/s → reader scrolls (no change) →
  tab hidden (phase held by clock) → tab visible (wheel correct at
  first frame) → footer reached (wheel still beating; it stops only
  when the page closes).
- **State matrix (v2).** *Rest:* beating at 4 Hz. *Hover:* ignored.
  *Focus:* n/a. *Active:* n/a. *Scrolled-past:* n/a (pinned).
  *Disabled:* n/a. *Touch:* ignored identically; the rail is not a
  tap target. *Hidden tab:* phase preserved by clock derivation.
- **Breakpoints (v2).** ≥1200px: Ø 120px in the right rail, 7-coil
  spring. 768–1199px: Ø 88px, rail narrows, spring 6 coils. <768px:
  Ø 64px in the masthead, 5 coils, aperture ring drops its inner rim.
- **Edge cases & failure modes (v2).** *System clock skew / rAF
  drift:* phase derives from elapsed clock each frame, so drift
  cannot accumulate. *Very long sessions:* sin() argument is reduced
  modulo the period before evaluation — no float-precision wobble at
  hour 3. *Low-power device:* if the frame budget trips (§14), the
  wheel's update halves to every second frame (2 Hz sampling of a
  4 Hz phase still lands on true angles at half the beats; the
  counter §6.6 remains exact because it counts time, not frames).
- **Accessibility spec (v2).** The wheel is `aria-hidden` decoration
  with a text equivalent: the beat-rate readout (§6.6) is the
  accessible instrument, in the DOM beside it. No information is
  carried by the wheel alone. It never flashes: brightness is
  constant; only rotation moves, at 4 Hz small-angle — below
  photosensitive thresholds, and stopped entirely under
  reduced-motion.
- **Tokens consumed (v2).** `--plate-shadow`, `--hairline`, `--gilt`,
  `--steel`, `--ruby`, `--ease-beat`, `--loop-lerp-phase` (0.055),
  `--wheel-size` (120px), `--dur-watchdog-wheel` (2000ms).

### 6.2 Cased headline

- **What & why.** The hero headline — the calibre's name, "Calibre &
  Escapement" in the worked build — is cased like a movement: revealed
  through the movement's circular aperture, its 18 glyphs dropping
  into place one by one with a 2px mechanical overshoot and one damped
  settle, after the plate, bridges and jewels have assembled around
  it. A brand name that renders is a logo; a brand name that is cased
  is a manufacture. The assembly order is the watchmaker's: you do not
  see the name until the movement exists to carry it.
- **Structure.** An `<h1>` of 18 glyph spans inside an aperture mask:
  a circular SVG mask (Ø = column ÷ 3, §4) with a polished rim, over a
  plate field carrying two bridge ends left and right. Each glyph span
  is `display:inline-block`, shipped at its final position in the DOM;
  JS arms the pre-state (translateY −10px, opacity 0) per glyph only
  after the assembly sequence begins. The aperture rim and bridges are
  inline SVG, static once dropped.
- **Motion spec.** Assembly: plate fades its stripes in over 300ms
  `--ease-draw` → bridge ends drop 14px with `--ease-settle` (180ms)
  at t=150 → two jewel bearings seat (scale 0.6 → 1, ruby flash to
  `--ruby-bright` for 120ms) at t=300 → glyphs case from t=420, 60ms
  stagger, each 180ms `--ease-settle` with exactly 2px overshoot and
  one recoil → last glyph locks at t ≈ 420 + 17×60 + 180 = 1,620ms →
  the beat-rate readout (§6.6) begins its count at t=1,650. Total
  ceremony ≤1.7s, once per session (a `sessionStorage` flag returns
  visitors to the assembled state instantly).
- **States.** Rest: fully cased, still. Hover: none on glyphs; the
  aperture's bridge screws are the hero's links (§6.11) and take
  their own states. Focus: skip-link and nav precede it in order; the
  headline itself is not focusable. Scrolled-past: the aperture stays
  assembled; the hero does not re-case on return scroll — a movement
  is cased once. Disabled: n/a.
- **Content merge.** The headline is the calibre's name and the
  aperture is the movement's own opening — the name is read *through*
  the mechanism the page is about, framed by the bridges that §4's
  layout uses for every section below. The hero teaches the layout
  language while it introduces the brand.
- **Failure fallback.** Watchdog `WD-CASE` at 1,800ms from arming: any
  glyph not yet cased is set to final state. No JS: glyphs were never
  armed — the DOM ships cased. Font race: if Instrument Serif has not
  arrived by t=900, casing proceeds in the fallback serif (measures
  pre-matched by `size-adjust`, §3); a late font swap re-runs no
  animation.
- **Reduced-motion variant.** No assembly: plate, bridges, jewels and
  headline ship in final state, instantly. The aperture remains — it
  is composition, not motion.
- **Performance budget & mobile variant.** 18 transform/opacity
  animations on inline-blocks, compositor-only; ≤0.3ms/frame during
  the 1.7s ceremony, zero thereafter. Mobile: aperture Ø = column ÷ 2,
  stagger tightens to 40ms, overshoot 1px — total ≤1.1s; bridge ends
  shorten to stubs.
- **Choreography timeline (v2).** t=0 load → 0–300 stripes draw →
  t=150 bridges drop → t=300 jewels seat → t=420–1,440 glyphs case
  (60ms stagger) → t=1,620 lock → t=1,650 readout counts → hero at
  rest, wheel (§6.1) beating throughout.
- **State matrix (v2).** *Rest:* cased and still. *Hover:* none
  (glyphs); screws per §6.11. *Focus:* n/a. *Active:* n/a.
  *Scrolled-past:* stays cased, no replay. *Disabled:* n/a. *Touch:*
  identical; no tap behaviour on the name.
- **Breakpoints (v2).** ≥1200px: aperture Ø ≈ 235px (44rem ÷ 3),
  60ms stagger. 768–1199px: Ø 200px, 50ms stagger. <768px: Ø = half
  column, 40ms stagger, display size clamps to 2.75rem so the 18
  glyphs hold one or two lines inside the rim.
- **Edge cases & failure modes (v2).** *Longer brand names:* the
  casing spec is per-glyph, so a 30-glyph name cases in 2.2s — the
  watchdog rises to 2,600ms by formula (420 + n×60 + 400). *Two-line
  headlines:* glyphs case in reading order across the break; the
  aperture becomes an ellipse (rim redrawn), never a clip.
  *Revisit in session:* assembled instantly, no ceremony, no flag
  text announcing the shortcut.
- **Accessibility spec (v2).** The `<h1>` is a single text node to
  assistive technology — glyph spans are `aria-hidden` and the full
  string is set as the heading's accessible name, so a screen reader
  hears the name once, whole, immediately; the visual casing is
  presentation only. Contrast: `--ink` on `--plate` 12.9:1 at
  display size. The ceremony never delays content availability: the
  heading is in the accessibility tree from parse.
- **Tokens consumed (v2).** `--plate`, `--plate-shadow`, `--gilt`,
  `--ruby`, `--ruby-bright`, `--ink`, `--ease-settle`, `--ease-draw`,
  `--dur-stagger-case` (60ms), `--dur-watchdog-case` (1800ms).

### 6.3 Velocity gear train

- **What & why.** A train of five meshing gears in the left margin
  rail — barrel 84T, centre 60T, third 48T, fourth 40T, escape 15T,
  the record's own counts (§6.17) — driven by the reader's scroll
  velocity. Fling the page and the train spins up with a slight
  motion blur; stop, and the escapement settles it tooth by tooth,
  3–5 ticks, into rest. The reader's hand is the crown: scrolling
  winds and drives the very mechanism the copy describes, so the
  page's physics are the product's physics.
- **Structure.** One inline SVG, five gear paths generated at build
  time from the tooth counts (module constant across the train, so
  the teeth truly mesh: centre distances = sum of pitch radii). Each
  gear is a `<g>` rotated about its own centre; angular velocities
  obey the mesh ratios 1 : 1.4 : 1.75 : 2.1 : 5.6 (84÷60, 84÷48,
  84÷40, 84÷15) with alternating sign per mesh. The escape gear
  carries 15 club teeth, visibly different — a reader who counts
  teeth finds the record's numbers.
- **Motion spec.** Input: lerped scroll velocity from the shared loop
  (master lerp 0.12). Gear angle integrates velocity × ratio × a
  scale of 0.9° per px/s at the barrel. While |velocity| > 40 px/s a
  1px motion blur (SVG filter, pre-rendered) fades in on the two
  fastest gears only. On stop (velocity < 2 px/s), the train does not
  glide: it settles — the escape gear advances in discrete tooth
  steps (24° per tooth = 360/15) of 40ms `--ease-tick`, 3–5 steps,
  each driving the train backward through the ratios, until residual
  angle is consumed; then rest, teeth meshed, no two teeth ever
  drawn interpenetrating (phase offset per mesh is fixed at build).
- **States.** Rest: still, meshed, escape gear's marked tooth (one
  gilt tooth) at top. Hover: none — the train answers scroll, not
  pointers. Focus: not focusable. Active: while scrolling, state =
  driven. Scrolled-past: the train is in the pinned rail; it reports
  the whole page's velocity including the footer. Disabled: n/a.
- **Content merge.** The train is the going train of §6.17 made
  visible, running down the margin beside the copy that specifies it
  — and §6.7 draws these same five profiles in the spec chapter, so
  the reader meets the wheels twice: working in the margin, drawn at
  the bench. Its speed is the reader's own reading speed, geared.
- **Failure fallback.** Watchdog `WD-TRAIN` at 2,000ms: if the loop
  is dead, the train rests at its shipped angle (gilt tooth top) —
  markup ships the SVG unrotated, JS applies rotation, so failure is
  a still, correct train. No JS: same. Canvas is never used here;
  SVG failure is not a mode (inline SVG is markup).
- **Reduced-motion variant.** The train does not respond to velocity.
  It rests at shipped angle for the whole read — a movement at rest
  shows its train as a diagram, which §6.7's draws then animate
  nothing either; the spec still reads true.
- **Performance budget & mobile variant.** Five group rotations +
  one filter toggle per frame; ≤0.15ms/frame. The blur filter is the
  budget's first cut (§14): below 60fps sustained, blur is disabled
  before any angle is dropped. Mobile (<768px): train cut entirely
  (rail dissolves, §4); 768–1199px it runs horizontally under the
  masthead at 60% size, same ratios, same settle.
- **Choreography timeline (v2).** Scroll begins → t=0 velocity rises
  → train spins up over ~120ms of lerp → fling: blur in at >40px/s →
  reader stops → velocity decays → settle: 3–5 tooth-steps × 40ms →
  rest with gilt tooth within one tooth of top (the settle always
  ends on a tooth boundary — never mid-tooth).
- **State matrix (v2).** *Rest:* meshed, still. *Hover:* none.
  *Focus:* n/a. *Active (scrolling):* driven, blur above threshold.
  *Scrolled-past:* n/a (pinned). *Disabled:* n/a. *Touch:* touch
  scroll drives identically — velocity is velocity, finger or wheel.
- **Breakpoints (v2).** ≥1200px: full train, gears Ø 44–96px by
  pitch. 768–1199px: horizontal strip, 60% scale, blur kept.
  <768px: cut (see budget) — the margin's other instruments (§6.1,
  §6.5) carry the rail's duties alone.
- **Edge cases & failure modes (v2).** *Violent scroll flings:*
  velocity is clamped at 4,000 px/s input so the escape gear never
  exceeds a readable spin; blur caps at 1.5px. *Scroll bounce
  (overscroll):* negative velocity at page ends drives the train
  backward — correct behaviour, kept, since a crown can be turned
  both ways. *Reader scrolls back up:* the train reverses through
  the same ratios and settles tooth-by-tooth in reverse; no state
  is latched, everything is a function of velocity and angle.
- **Accessibility spec (v2).** `aria-hidden`; the train's information
  (the ratios, the counts) is printed in §6.13's table and §6.7's
  draws with captions. Motion is peripheral, small, and stops with
  reduced-motion. No focusable parts.
- **Tokens consumed (v2).** `--steel`, `--steel-deep`, `--steel-bright`,
  `--gilt`, `--plate-shadow`, `--ease-slew`, `--ease-tick`,
  `--loop-lerp` (0.12), `--dur-watchdog-train` (2000ms).

---

### 6.4 Tourbillon section steps

- **What & why.** Each content section enters the reading position the
  way a tourbillon cage presents its escapement: it rotates 1.5° and
  translates 12px into register, then locks with a 60ms two-step
  ratchet settle. Sections are carried by the mechanism, not faded in
  by a stylesheet. The cage itself turns one revolution per 60
  seconds in the record (§6.17) — the section step borrows the cage's
  bearing, not its speed: presentation is a step, not a spin.
- **Structure.** Sections are ordinary `<section>` elements shipped in
  final position. JS arms a pre-state per section
  (`transform: rotate(1.5deg) translateY(12px)`, transform-origin at
  the section's jewel bearing — its pivot, §4) and an
  IntersectionObserver at the reading line (62% viewport height)
  triggers the step. Transform only; content is never opacity-gated.
- **Motion spec.** Trigger: section's top crosses the reading line.
  Step: 260ms `--ease-settle` to rotate(0) translateY(0), then the
  lock: two 30ms `--ease-tick` micro-advances of 0.5px — the ratchet
  taking up the last play — total 320ms per section, one section at a
  time (a queue drains at 90ms intervals if the reader scrolls fast).
  Reverse scroll never un-steps a section: a cage does not un-present
  what it has presented; the state latches per section per session.
- **States.** Rest (pre-trigger): printed, complete, rotated 1.5° —
  readable even if the step never fires. Hover: none. Focus: if focus
  lands inside an unstepped section (keyboard jump), the section
  steps instantly with no animation — focus must never wait for a
  mechanism. Scrolled-past: latched in register. Disabled: n/a.
- **Content merge.** The rotation pivots on the section's own jewel
  bearing (§4) — the point where its argument turns — so the motion
  describes the content's structure. Bridge sections (§4) step with
  their bridge; the bridge's screws (§6.11) turn as the lock engages,
  tying navigation state to arrival.
- **Failure fallback.** Watchdog `WD-STEP` at 2,500ms per armed
  section: unstepped sections are set to register regardless of the
  observer. No JS: no pre-state was armed; sections ship in register.
  Observer unsupported: the watchdog path is the path.
- **Reduced-motion variant.** No pre-state, no step: sections are
  simply in register, as printed. The cage language survives in the
  layout (bearings, bridges), not in motion.
- **Performance budget & mobile variant.** One transform per section,
  320ms, compositor-only; ≤0.1ms/frame while stepping. Mobile:
  rotation halves to 0.75° and translate to 6px — small screens make
  rotation read as error, so the step becomes mostly a seat.
- **Choreography timeline (v2).** Section approaches → top crosses
  62% line → t=0 step begins → 260ms settle to register → 260–290ms
  lock tick 1 → 290–320ms lock tick 2 → screws turn (§6.11) →
  section at rest, latched.
- **State matrix (v2).** *Rest:* in register (latched) or printed at
  1.5° awaiting the line. *Hover:* none. *Focus:* instant register,
  no animation. *Active:* n/a. *Scrolled-past:* latched. *Disabled:*
  n/a. *Touch:* identical triggers — the reading line is scroll
  geometry, not pointer geometry.
- **Breakpoints (v2).** ≥1200px: 1.5° / 12px, pivot at the bearing.
  768–1199px: 1.25° / 10px. <768px: 0.75° / 6px, pivot moves to the
  section's top-left bearing (the only one on a narrow plate).
- **Edge cases & failure modes (v2).** *Jump scroll (anchor link,
  find-in-page):* all sections above the landing point latch silently
  to register; the landed section steps only if it lands below the
  line. *Very short sections:* two sections may cross in one frame —
  the 90ms queue keeps their locks audible-in-eye as separate ticks,
  never a chord. *Reader scrolls back up:* nothing reverses; the page
  stays assembled, as a cased movement stays cased.
- **Accessibility spec (v2).** Motion is transform-only on fully
  rendered content; reading order and focus order are DOM order,
  untouched by the latch. Screen readers never encounter a pre-state
  (arming is visual transform, content is present and legible at
  1.5°). Focus-jump rule above guarantees no focus lands in a moving
  target for more than one frame.
- **Tokens consumed (v2).** `--ease-settle`, `--ease-tick`,
  `--dur-step` (260ms), `--dur-lock` (60ms), `--step-angle` (1.5deg),
  `--dur-watchdog-step` (2500ms).

### 6.5 Mainspring progress — the barrel

- **What & why.** The progress indicator is the mainspring barrel in
  the right margin rail beneath the balance wheel: a gilt wind arc
  fills as the reader progresses, and the barrel's spiral visibly
  tightens. Reading winds the watch. At the footer's threshold the
  barrel stands at full wind — 6.5 turns, the record's figure
  (§6.17) — and the reserve readout beside it has counted from
  0 to 62 hours of stored reading. Progress is stored energy, in the
  movement itself, not a line borrowed from a video player.
- **Structure.** An SVG barrel (Ø 96px): outer drum ring, a spiral
  path of 6.5 turns whose stroke tightens (coil spacing interpolates
  from let-down to full-wind geometry — two precomputed path states
  morphed by stroke-dasharray-weighted scaling, implemented as two
  paths cross-faded by opacity at 10% increments to avoid path-morph
  cost), a gilt arc around the drum showing wind fraction, and a mono
  readout under it: "RESERVE 00.0 H / 62 H".
- **Motion spec.** Pure scrub from the shared loop: wind fraction =
  lerped scroll progress (0 at hero top, 1 at footer threshold).
  Barrel rotates 2,340° over the full read (6.5 × 360°) — geared
  down in display: the visible drum turns 0.25× that (585°) so the
  spiral's tightening, not the spin, carries the information. The
  gilt arc draws at `--ease-draw` rates as a function of the same
  progress; the reserve readout flips (§6.6's flip mechanism) in
  0.5-hour increments — 124 flips over a full read.
- **States.** Rest: arc at true progress. Hover: the barrel is a
  link to the register (§6.17 anchor) — hover lights the arc to
  `--gilt-pale` and the readout underlines; the drum does not move
  for a pointer. Focus: same lighting + 2px `--steel` focus ring on
  the link. Active: click jumps to the record section. Scrolled-past:
  at footer, full wind, arc complete — the state the whole page
  promised. Disabled: n/a.
- **Content merge.** The barrel's numbers are the record's: 6.5 turns
  and 62 hours are §6.17's wind and reserve, and §6.13's spec table
  prints the same two figures as the calibre's specification. The
  indicator, the table and the record agree because they are one
  object read three ways.
- **Failure fallback.** Watchdog `WD-BARREL` at 2,000ms: if scroll
  progress cannot be computed, the barrel ships and stays at its
  markup state — arc at 0, readout printed "RESERVE — / 62 H" — a
  true statement (nothing has been wound by a reader the page cannot
  see). No JS: same printed state; the page loses its gauge, never
  its content.
- **Reduced-motion variant.** The arc and readout update in discrete
  jumps at 10% progress increments with no lerp and no spiral
  tightening (spiral shown at mid-wind geometry) — the gauge still
  gauges, without continuous motion.
- **Performance budget & mobile variant.** One arc dash update + at
  most one digit flip per frame; ≤0.08ms/frame. Mobile (<768px): the
  barrel becomes the gilt arc alone across the top of the reading
  column (no drum, no spiral), readout moves to the footer (§6.16);
  budget halves.
- **Choreography timeline (v2).** Hero: 0 turns, 0.0 H → first scroll:
  arc begins, drum turns → mid-page: ≈3.25 turns, 31 H → spec
  chapter: the table (§6.13) prints the same figures the barrel
  shows → footer threshold: 6.5 turns, 62.0 H, arc closes → register
  link pulses once (gilt flash 200ms) — the wound movement points at
  its record.
- **State matrix (v2).** *Rest:* true progress shown. *Hover:* arc
  lights, readout underlines. *Focus:* as hover + ring. *Active:*
  navigates to §6.17. *Scrolled-past:* full wind at footer.
  *Disabled:* n/a. *Touch:* tap = the link; progress itself is
  scroll state, identical.
- **Breakpoints (v2).** ≥1200px: Ø 96px barrel in rail, spiral live.
  768–1199px: Ø 72px, spiral cross-fade steps coarsen to 20%.
  <768px: arc-only progress across the column top, 3px gilt stroke.
- **Edge cases & failure modes (v2).** *Short pages (detail pages
  with little scroll):* progress is normalised to the page's own
  scrollable length — a short page still winds fully, because the
  reserve is a property of the read, not the metre count; §6.17
  states this mapping so the figure stays honest. *Reader jumps to
  footer via keyboard:* arc lerps over 600ms to full — the wind is
  shown happening, never teleported, except under reduced motion
  (jump is instant). *Print:* the barrel prints at its current wind
  with the readout as static text.
- **Accessibility spec (v2).** The barrel link's accessible name
  carries the data: "Reading progress, 34 of 62 hours wound — go to
  the calibre record", updated at 10% increments only (never a
  per-scroll announcement). The SVG itself is `aria-hidden`; the
  readout text is the instrument. Focus ring contrast: `--steel` on
  `--plate` 5.9:1.
- **Tokens consumed (v2).** `--gilt`, `--gilt-pale`, `--steel`,
  `--plate-shadow`, `--ease-draw`, `--loop-lerp` (0.12),
  `--barrel-turns` (6.5), `--reserve-hours` (62), `--dur-watchdog-barrel`
  (2000ms).

### 6.6 Beat-rate readout

- **What & why.** A mono readout that counts up to 28,800 on load and
  thereafter keeps two live figures: the rate ("28,800 VPH") and a
  beat counter that ticks in time with the balance wheel (§6.1) —
  8 beats per second, 28,800 per hour, the record's arithmetic
  (§6.17). The number is the wheel beside it, counted. Specification
  and mechanism agree, live, in front of the reader — the theme's law
  in its smallest possible form.
- **Structure.** A readout block in the right rail under the wheel:
  two mono lines. Line 1: "RATE 28,800 VPH" with each digit a
  split-flap cell (a clipped two-half digit that flips top-down).
  Line 2: "BEAT 000000" — a six-digit counter of the same cells.
  Digits are DOM spans; a flip is a 90ms two-frame swap of the top
  and bottom halves — no 3D, a printed digit replaced by the next
  printed digit, the way a timing machine's tape advances.
- **Motion spec.** Load count-up: from 0 to 28,800 over 2,400ms
  beginning at §6.2's lock (t=1,650), digits flipping at most every
  90ms per cell, easing by digit place (units spin, ten-thousands
  step twice) — the count is a display ceremony, then it stops dead
  at 28,800 and the word RATE steadies. Beat counter: +1 per beat
  from the loop's clock channel (8/s), flipping only the cells that
  change. After 3,600 beats (7.5 minutes) the counter has visibly
  done an eighth of an hour's work — §8.2 uses this.
- **States.** Rest: rate steady, counter ticking. Hover: none.
  Focus: not focusable. Scrolled-past: pinned with the rail.
  Disabled: n/a. Hidden tab: the counter is clock-derived
  (beats = floor(elapsed × 8)), so it is exact on return — it counts
  time, not frames.
- **Content merge.** The readout is §6.13's first spec row made live,
  and §6.17's rate figure with a pulse. It sits directly under the
  wheel it counts — adjacency is the argument: this number, that
  wheel, same beats.
- **Failure fallback.** Watchdog `WD-READOUT` at 2,500ms: if the
  count-up has not completed, all cells snap to "28,800" and the
  counter prints "BEAT ——" (a stopped tape). No JS: markup ships
  "RATE 28,800 VPH" printed and the counter line absent — a
  specification without a claim of liveness.
- **Reduced-motion variant.** No count-up, no flips: rate printed at
  28,800 from parse; the counter updates as a whole-text replacement
  once per second, printing the true beat count as static text
  (rising by 8 each second). Still true, never animated.
- **Performance budget & mobile variant.** ≤6 cell flips per beat
  worst case, typically 1; ≤0.04ms/frame amortised. Mobile: the
  readout joins the wheel in the masthead at 0.75rem mono, counter
  line dropped (rate only) — the count is a rail luxury, the rate is
  the fact.
- **Choreography timeline (v2).** t=1,650 (headline locked) →
  count-up 2,400ms → t≈4,050 rate steady at 28,800 → counter starts
  from beat 0 at the same instant the rate steadies (the ceremony
  ends, the work begins) → 8 flips/s of the units cell thereafter.
- **State matrix (v2).** *Rest:* rate steady, counter live. *Hover:*
  none. *Focus:* n/a. *Active:* n/a. *Scrolled-past:* n/a (pinned).
  *Disabled:* n/a. *Touch:* no interaction; identical display.
- **Breakpoints (v2).** ≥1200px: two lines, 1rem mono. 768–1199px:
  two lines at 0.8125rem. <768px: rate line only, in the masthead.
- **Edge cases & failure modes (v2).** *Counter overflow:* six digits
  roll at 999,999 beats (34.7 hours of session — beyond any real
  read; the roll is specified anyway: to 000000 with a gilt tick in
  the margin of the readout, an hour-hand's honesty). *Reader
  compares counter to a wall clock:* the counter counts the page's
  session beats, not time of day — §12's copy rules name it "BEAT",
  never "TIME", precisely so the claim stays true.
- **Accessibility spec (v2).** The whole readout is `aria-hidden`
  except one visually-hidden static line: "Beat rate: 28,800
  vibrations per hour." A live counter must never chatter to a
  screen reader; the fact is stated once, the counting is visual.
  Digit contrast: `--ink` on `--plate` 12.9:1.
- **Tokens consumed (v2).** `--ink`, `--plate`, `--gilt`, `--ease-tick`,
  `--dur-flip` (90ms), `--dur-countup` (2400ms), `--vph` (28800),
  `--dur-watchdog-readout` (2500ms).

---

### 6.7 Hairspring & gear-profile draws

- **What & why.** In the spec chapter, the going train's profile —
  the five gears of §6.3 in section view — and the hairspring spiral
  stroke themselves in over ~1.8s, tooth by tooth and coil by coil,
  beside the specifications they define. These are the bench drawings
  of the very wheels the reader has watched working in the margin:
  the page first shows the mechanism alive, then shows it drawn, the
  way a manufacture first runs a calibre and then publishes its
  technical sheet.
- **Structure.** Two inline SVGs on an ebony bench field (§2's second
  ground): (a) the train profile — five gear outlines side by side in
  drive order with centre lines, tooth counts lettered under each in
  gilt mono ("84 · 60 · 48 · 40 · 15"); (b) the hairspring — a 7-coil
  Archimedean spiral with an overcoil terminal curve, stud and
  regulator pins marked. All paths ship complete in markup; JS arms
  `stroke-dasharray` to path length and scrubs the offset.
- **Motion spec.** Trigger: the drawing field crosses the reading
  line (§6.4's 62%). The train draws first: each gear's outline at
  `--ease-draw`, 120ms per tooth-equivalent of path — escape wheel
  (15 teeth) 1.8s total across the train's combined path at a
  constant hand speed of ≈900 px/s, gears in drive order, centre
  lines striking in at 40ms `--ease-tick` as each gear completes.
  Then the hairspring: coils draw centre-outward over 1.4s, the
  overcoil last, its terminal curve slowing to 300 px/s — the hand
  takes care at the overcoil, as a watchmaker's does. Total sequence
  ≈3.4s, once, latched.
- **States.** Rest (post-draw): the finished drawing, still. Hover:
  hovering a gear outline lights it `--steel-bright` and prints its
  ratio in the caption line ("CENTRE — ×1.40") — inspection of a
  drawing. Focus: gears are list items in an adjacent text list
  (§6.13's table carries the same data); the SVG itself is not
  focusable. Scrolled-past: drawn, latched. Disabled: n/a.
- **Content merge.** The drawings are not illustrations *of* the
  spec; they are the spec's figures, generated from the same tooth
  counts that §6.3 meshes and §6.13 tabulates. Change a count in
  §6.17 and all three change — the build generates the paths from the
  record, never by hand.
- **Failure fallback.** Watchdog `WD-DRAW` at 3,000ms from arming:
  dash offsets zeroed, drawing complete. No JS: paths ship undashed —
  the drawing is simply there, as a printed technical sheet's would
  be.
- **Reduced-motion variant.** No drawing: both SVGs appear complete
  when the chapter arrives. The caption still names the order ("drawn
  in drive order") — under reduced motion the caption is edited by
  §12's rules to "shown in drive order"; copy must not claim a motion
  that did not happen.
- **Performance budget & mobile variant.** Dash-offset updates on two
  paths for ≈3.4s; ≤0.1ms/frame. Mobile: the two drawings stack, the
  train profile scrolls horizontally within its bench field (a
  drawing wider than the plate is examined by sliding it, like a
  sheet on the bench), draw durations unchanged.
- **Choreography timeline (v2).** Field crosses line → t=0 barrel
  outline begins → gears complete in drive order (centre lines tick
  in) → t≈1,800 train complete → t=1,900 hairspring begins centre-out
  → coils 1–6 at 900px/s → overcoil at 300px/s → t≈3,400 drawing
  rests; the spec table (§6.13) steps in beneath it.
- **State matrix (v2).** *Rest:* complete drawing. *Hover:* gear
  lights + ratio caption. *Focus:* n/a (data in §6.13). *Active:*
  n/a. *Scrolled-past:* latched complete. *Disabled:* n/a. *Touch:*
  tap a gear = the hover state, latched until another tap.
- **Breakpoints (v2).** ≥1200px: drawings side by side on one bench
  field. 768–1199px: stacked, full width. <768px: stacked; train
  field horizontally slidable; hairspring at 85% scale.
- **Edge cases & failure modes (v2).** *Reader scrolls through
  quickly:* if the field leaves the viewport mid-draw, the draw
  completes off-screen at 3× speed — a drawing half-drawn on return
  would look broken; finished is the only stable state. *Path length
  mis-measure:* lengths are computed at build time and inlined as
  data attributes, never measured at runtime, so a font or zoom
  change cannot desync the dash.
- **Accessibility spec (v2).** Each SVG carries `role="img"` and a
  full text description ("Going train profile: five wheels of 84,
  60, 48 and 40 teeth driving a 15-tooth escape wheel"); the same
  figures are tabulated in §6.13 for non-visual reading. Gilt
  lettering on ebony: 5.6:1 — the one licensed gilt text pairing
  (§2).
- **Tokens consumed (v2).** `--ebony`, `--gilt`, `--steel-bright`,
  `--plate`, `--ease-draw`, `--ease-tick`, `--draw-rate` (900px/s),
  `--dur-watchdog-draw` (3000ms).

### 6.8 Loupe hover

- **What & why.** Hovering a component — a card, a bridge, a spec row
  — is the watchmaker's loupe: the area beneath the pointer enlarges
  ~15% inside a polished loupe ring, and jewel bearings under focus
  brighten to `--ruby-bright`. Inspection is this world's core verb,
  and it happens on the part itself, through the instrument the trade
  actually uses — never as a tooltip, a popover or a zoom modal that
  takes the reader somewhere else.
- **Structure.** A loupe layer per inspectable component: a clipped
  duplicate of the component's content, scaled 1.15, inside a circular
  mask (Ø 180px) with a drawn rim (plate-shadow ring, gilt hairline,
  a knurled edge suggested by 24 tick marks). The duplicate is
  `aria-hidden` and pointer-transparent; the original remains the
  interactive layer. The loupe's position is lerped (0.2) from the
  shared loop — the hand is steady, not glued.
- **Motion spec.** Enter: rim fades/scales in 140ms `--ease-settle`
  (0.96 → 1.0). Move: position lerp 0.2, magnification constant 1.15 —
  a loupe does not zoom while moving. Jewel brighten: bearings within
  the ring lift to `--ruby-bright` over 120ms, release over 300ms
  `--ease-draw` (light leaves a jewel slowly). Exit: rim out 120ms.
  Bridges under the loupe also tilt — max 2°, pivoting on their
  nearer screw (§4) — the one tilt in the theme, because a movement
  tilted in the hand is how bridges are read.
- **States.** Rest: no loupe. Hover: as above. Focus: keyboard focus
  on an inspectable component summons the loupe centred on it,
  static — a keyboard reader inspects too; focus-visible ring
  (2px `--steel`) sits *outside* the loupe rim so the two circles
  never blur into one. Active (pressed): loupe magnification steps
  to 1.25 for the press duration (the loupe leans closer) — 100ms.
  Scrolled-past: loupe dismissed on scroll start; it never chases a
  moving page. Disabled components: no loupe — an unfinished part is
  not inspected, and §6.15's skeleton states say why.
- **Content merge.** The loupe magnifies the component's own content —
  its engraving, its figures, its bearings — and the brightening
  jewels are the component's actual pivots (§4). It reveals nothing
  that was not already printed; it makes the printed thing legible
  at the watchmaker's working distance. That is the difference
  between an instrument and a gimmick.
- **Failure fallback.** Watchdog: the loupe is pure enhancement — if
  the loop dies, no loupe appears and components are fully legible at
  1.0 (they were designed to be). No JS: no loupe; nothing was hidden
  in anticipation of it. The fallback is the design's resting face.
- **Reduced-motion variant.** No travelling loupe. Focus/hover instead
  applies a static 1.15 scale to the component's figure area only
  (not text — text never scales, §3) with the rim drawn in place:
  inspection without motion.
- **Performance budget & mobile variant.** One clipped layer
  transform + ≤ a few bearing colour transitions; ≤0.2ms/frame while
  hovering. The duplicate-content cost is bounded: only components in
  the viewport get loupe layers, built lazily on first hover. Touch:
  no loupe on tap (a tap is a decision, not an inspection); long-press
  (≥400ms) summons the static variant, released on lift.
- **Choreography timeline (v2).** Pointer enters component → 140ms
  rim in → bearings inside brighten 120ms → pointer moves: loupe
  follows at lerp 0.2, bridge tilts ≤2° → press: 1.25 step 100ms →
  pointer leaves → jewels release 300ms → rim out 120ms → rest.
- **State matrix (v2).** *Rest:* none. *Hover:* loupe live. *Focus:*
  static centred loupe + outside ring. *Active:* 1.25 step.
  *Scrolled-past:* dismissed at scroll start. *Disabled:* never
  summoned. *Touch:* long-press static variant only.
- **Breakpoints (v2).** ≥1200px: Ø 180px, 1.15×. 768–1199px: Ø 150px,
  1.12×. <768px: loupe cut for pointer (no hover exists); the focus
  variant remains for keyboard/switch users at Ø 140px.
- **Edge cases & failure modes (v2).** *Component smaller than the
  loupe:* the ring overflows the component and magnifies the plate
  around it too — correct loupe behaviour, kept. *Text under the
  loupe:* body text is excluded from the magnified duplicate (only
  figures, drawings and bearings magnify) — magnified body text
  would break the measure and the law that type behaves like parts.
  *Fast pointer sweeps:* the lerp makes the loupe trail and fade if
  the pointer exits the component by >240px — it never teleports
  across the page.
- **Accessibility spec (v2).** The loupe is presentational
  (`aria-hidden` duplicate); all content is available unmagnified in
  the original layer, and magnification never gates information.
  Focus variant guarantees keyboard parity of inspection. Rim ticks
  are decorative. Magnification is user-agent-independent — browser
  zoom composes normally (the loupe scales its own layer, not the
  page).
- **Tokens consumed (v2).** `--plate-shadow`, `--gilt`, `--ruby-bright`,
  `--steel`, `--ease-settle`, `--ease-draw`, `--loupe-zoom` (1.15),
  `--loupe-size` (180px), `--loop-lerp-loupe` (0.2), `--tilt-max` (2deg).

### 6.9 Escapement-tick click

- **What & why.** Clicking an interactive component is an escapement
  tick: the nearest gear — in the component's own bearing train —
  advances exactly one tooth, with a crisp 40ms step and a settle
  tick, and the related readout flips by one unit. A click in this
  theme is never a ripple or a bounce; it is the mechanism
  registering the act in its own units. One tooth, one unit, no
  more — the escapement's whole virtue is that it cannot advance two.
- **Structure.** Each interactive component declares its tick target:
  a small gear glyph (SVG, tooth count matching its §6.17 family —
  form gears use the centre wheel's 60, cards the third wheel's 48)
  in its corner bearing, and a readout binding (the spec figure it
  increments). The step is a rotation of 360/teeth degrees on the
  glyph plus a one-unit flip (§6.6 mechanism) of the bound readout.
  The binding is data, declared in markup (`data-tick-gear`,
  `data-tick-readout`), so the behaviour is auditable in the DOM.
- **Motion spec.** Press: glyph rotates one tooth over 40ms
  `--ease-tick`, with a 1px recoil (the escapement's draw) settling
  by 90ms. Readout flips at t=40 (as the tooth locks). The component's
  own action (navigation, submit, toggle) proceeds independently and
  is never delayed by the tick — the tick is the mechanism's receipt,
  printed as the act happens, not a toll before it.
- **States.** Rest: glyph at a tooth boundary. Hover: glyph's bearing
  brightens (§6.8's jewel rule) — the tick is promised before it is
  given. Focus: same brighten + ring. Active: the tick itself.
  Scrolled-past: n/a. Disabled: no tick, no brighten — a disabled
  control is a part out of the train, and the escapement does not
  pretend otherwise; its glyph is drawn `--plate-deep`, visibly
  unjewelled.
- **Content merge.** The readout that flips is the component's own
  figure — the form's register count, the card's beat tally, the
  table's regulation mark — so the click's feedback is denominated in
  the content's own units. And the glyph's tooth count is the real
  count of the wheel it stands for (§6.17): the receipt is printed
  by the actual train.
- **Failure fallback.** The tick is cosmetic to function: if the loop
  or the glyph fails, the component's action is untouched (it never
  depended on the animation). Watchdog `WD-TICK` at 1,000ms clears
  any mid-step glyph to the next tooth boundary — a gear may never
  rest between teeth.
- **Reduced-motion variant.** No rotation: the readout still flips
  (as a static text swap, §6.6's reduced rule) and the bearing
  flashes `--ruby-bright` for 120ms — the registration happens, the
  motion does not.
- **Performance budget & mobile variant.** One 40ms transform + one
  digit flip per click; negligible. Mobile: identical — taps tick.
  Rapid tapping: ticks queue at most 3 deep; beyond that the glyph
  advances without animation (the count stays true even when the eye
  is spared) — the escapement under a frantic hand slips its display,
  never its count.
- **Choreography timeline (v2).** Pointer down → t=0 tooth begins →
  t=40 tooth locks, readout flips → t=90 recoil settled → component
  action completes on its own timeline → glyph at rest on a boundary.
- **State matrix (v2).** *Rest:* on a boundary. *Hover:* bearing
  brightens. *Focus:* brighten + ring. *Active:* one tooth, one
  unit. *Scrolled-past:* n/a. *Disabled:* no tick, unjewelled glyph.
  *Touch:* tap = click, identical.
- **Breakpoints (v2).** All sizes identical; glyph Ø 18px at ≥768px,
  16px below — the tick does not shrink its meaning with the plate.
- **Edge cases & failure modes (v2).** *Double-clicks:* two teeth,
  two units — correct; the escapement counts acts, not intentions.
  *Click during the glyph's own step:* the queue rule above applies;
  the readout is incremented synchronously in data, so the printed
  figure is never behind the act. *A readout at its maximum (e.g.
  reserve at 62.0):* the tick still turns the gear, but the readout
  holds and the margin prints "AT FULL WIND" once — the mechanism
  registers the act, the figure refuses to lie past its record.
- **Accessibility spec (v2).** The tick is never the sole feedback:
  every component's action has its own result (navigation, state
  change, confirmation) per §11. The glyph is `aria-hidden`; readout
  changes that matter (form submission) are announced by the
  component's own live region (§6.14), not by the flip. Touch target
  sizes are the components' own (≥44px), unaffected by the 18px
  glyph, which is not itself a target.
- **Tokens consumed (v2).** `--ruby-bright`, `--plate-deep`, `--steel`,
  `--ease-tick`, `--dur-tick` (40ms), `--dur-recoil` (90ms),
  `--dur-watchdog-tick` (1000ms).

---

### 6.10 Geneva-stripe sheen

- **What & why.** A slow specular sheen travels across the
  Geneva-striped plates on a ~14s loop, catching the brushing at a
  low angle — the finishing behaving the way finishing behaves when a
  movement is turned in the hand. It is the theme's second and last
  licensed ambient loop (§5): the wheel proves the movement runs;
  the sheen proves the plate is finished. Both are evidence, not
  decoration.
- **Structure.** A CSS gradient layer over each exposed plate field:
  a 22° linear sheen band (white at 6% → transparent) translating
  across the stripe field, masked to the plate's exposed areas only
  (never over text — the mask is the inverse of the content boxes, so
  the sheen passes *around* reading matter the way light passes
  around a bridge's engraving). Implemented as a single shared
  pseudo-element per plate section, animated by the shared loop's
  clock channel — not a CSS animation, so it pauses with the tab.
- **Motion spec.** Period 14s: the band crosses a plate field in
  3.2s `--ease-beat`-phased (slow at the edges of its travel, as a
  hand's turn slows), then the field rests unlit for 10.8s. Opacity
  peaks at 0.06 — a breath on the metal, never a shine. Phase is
  offset per section by section index × 1.7s so the whole page never
  flashes in chorus; light travels down the movement like a hand
  turning it end over end.
- **States.** Rest: between passes, flat plate. Hover: a hovered
  plate section holds its sheen if the band is present (the hand
  steadies) — no new sheen is summoned. Focus: none. Scrolled-past:
  passes continue only for fields in the viewport (off-screen fields
  skip their phase; no catch-up). Disabled: n/a.
- **Content merge.** The sheen exists only where Geneva striping
  exists (§4) and only on exposed plate — it is a property of the
  finishing, positioned by the layout's real material map. On
  perlage fields (§6.15) it does not run: perlage is polished
  differently, and the theme keeps its finishes distinct.
- **Failure fallback.** If the loop dies, no sheen — the plate is
  flat, which is its printed state. Nothing was depending on light.
  No JS: flat plate, stripes still visible as static bands.
- **Reduced-motion variant.** No sheen, ever. The stripes remain as
  the plate's static finish. (A still photograph of a movement shows
  stripes without sheen; the variant is that photograph.)
- **Performance budget & mobile variant.** One gradient translation
  per exposed field in view, compositor-only; ≤0.05ms/frame. Mobile:
  sheen cut (§14's first cuts are finishes before mechanisms) —
  stripes remain, light does not travel.
- **Choreography timeline (v2).** t=0 section's phase offset elapses
  → band enters field edge → 3.2s crossing (ease-beat phase) →
  field rests 10.8s → next pass. Down-page sections follow at
  1.7s offsets — a slow wave of light down the plate, once per 14s.
- **State matrix (v2).** *Rest:* flat or mid-pass per phase. *Hover:*
  band holds if present. *Focus:* none. *Active:* none.
  *Scrolled-past:* phase skipped off-screen. *Disabled:* n/a.
  *Touch:* no touch behaviour.
- **Breakpoints (v2).** ≥1200px: full treatment. 768–1199px: period
  lengthens to 18s (smaller fields, same dignity). <768px: cut.
- **Edge cases & failure modes (v2).** *Brightness:* the 6% ceiling
  is a hard token (`--sheen-peak`), not a guideline — a brighter
  sheen turns the plate into a screen, and §9 names it a failure.
  *Dark sections:* on ebony fields the sheen does not run (ebony is
  the bench, not the plate); a builder who sheens the bench has
  confused the furniture with the movement.
- **Accessibility spec (v2).** Purely decorative, `aria-hidden` by
  construction (a background layer). 6% luminance change over 3.2s
  is far below any photosensitivity concern, and it is the first
  thing removed by reduced-motion. No information is carried.
- **Tokens consumed (v2).** `--plate`, `--sheen-peak` (0.06),
  `--sheen-period` (14s), `--ease-beat`, `--loop-lerp-phase` (0.055).

### 6.11 Bridge-span navigation

- **What & why.** The site's navigation is a bridge: a single plate
  band spanning the top of the movement, carrying the calibre name
  (the wordmark, set as an engraving), the section links as bridge
  stations, and two blued screws at its ends — which are real links
  (home, register) whose slots turn 90° as their sections become
  current. In a movement, a bridge is what holds the wheels in
  relation; the navigation is what holds the page's sections in
  relation. The metaphor is structural, so it is used structurally.
- **Structure.** A `<header>` containing a real `<nav>`: wordmark
  left (gilt on the bridge's ebony nameplate inset — the one gilt
  text the theme allows off a footer), station links in Inter spaced
  uppercase (§3), each with a small unjewelled pivot dot above it
  that takes a ruby bearing when its section is current. Scrollspy
  reads the same section boundaries as §6.4's reading line — one
  source of "where am I" for step, screw and bearing alike.
- **Motion spec.** On load, after the hero assembly begins (t=300),
  the bridge drops 10px with `--ease-settle` and its screws rotate
  from random bench angles to vertical — the movement is picked up
  and oriented. Scrollspy changes: the old station's bearing dims
  over 300ms `--ease-draw`, the new bearing seats (scale 0.7 → 1,
  140ms `--ease-settle`), and the current section's bridge screw
  (§4) rotates 90° over 200ms `--ease-tick`-stepped (two 45° ticks).
  The header bridge is sticky; its stripes flatten to solid plate on
  scroll so text over moving content stays legible.
- **States.** Rest: current station jewelled, others' pivots bare.
  Hover: station label turns `--steel`, its pivot dot warms to
  `--steel-bright`. Focus: label + 2px `--steel` outline below the
  bridge line. Active (current section): ruby bearing seated, label
  in `--ink` 600 weight, `aria-current="location"`. Scrolled-past:
  n/a (sticky). Disabled: a station for an unpublished section
  prints at 50% `--hairline`, no pivot, no link — a bridge end with
  no wheel under it.
- **Content merge.** The stations are the movement's own stations —
  the nav names the page's sections by their movement names (The
  Train, The Escapement, The Record) as §13's map does — and its
  screws are the same screws §4 sets at section bridges, turning in
  sympathy. Navigation state and section state are one mechanism
  read at two distances.
- **Failure fallback.** Watchdog: if scrollspy has not initialised
  within 1,500ms, the first station is jewelled by default (the
  reader is at the hero; that is never wrong). No JS: all stations
  unjewelled, all links live; the bridge is printed complete.
- **Reduced-motion variant.** The bridge ships in place (no drop);
  bearing changes are instant swaps; screws do not rotate (current
  screw is drawn at 90° statically when current — state by drawing,
  not by turning).
- **Performance budget & mobile variant.** Scrollspy via
  IntersectionObserver — zero per-frame cost. Mobile (<768px): the
  bridge holds wordmark, the balance wheel (§6.1's masthead move)
  and a menu button; stations move into a plate panel that drops
  from the bridge like a movement lowered on its rest, 220ms
  `--ease-settle`, stations full-width with bearings.
- **Choreography timeline (v2).** Load → t=300 bridge drops, screws
  orient → hero's station jewelled → reader scrolls: section bridge
  steps (§6.4) → its screw ticks 45°+45° → nav bearing swaps → at
  footer, the register station is jewelled and the end screw (the
  register link) stands at 90°.
- **State matrix (v2).** *Rest:* current jewelled. *Hover:* steel
  warm. *Focus:* label + outline. *Active:* bearing + weight +
  `aria-current`. *Scrolled-past:* n/a. *Disabled:* dim, linkless,
  pivotless. *Touch:* stations are ≥44px targets; bearings light on
  scrollspy only.
- **Breakpoints (v2).** ≥1200px: full bridge, all stations labelled.
  768–1199px: stations abbreviate to movement short-names ("Train",
  "Record"). <768px: wordmark + wheel + menu; stations in the drop
  panel.
- **Edge cases & failure modes (v2).** *Many sections (an 8-station
  page):* below 9px pivot spacing, labels abbreviate further to
  initials engraved style ("T", "E", "R") with full names in the
  drop panel and in `aria-label`s. *A section removed in the CMS:*
  the boundary table is built from the DOM's actual sections, so
  spy, steps and screws can never disagree with the page that
  exists.
- **Accessibility spec (v2).** Landmark header + `nav
  aria-label="Movement"`; skip link is the bridge's first element,
  printed `--ink` on `--plate`, visible on focus. Bearings and
  screws are `aria-hidden`; current-ness lives in `aria-current`,
  not only in the jewel. Label contrast: `--ink` 12.9:1, `--steel`
  5.9:1 on plate.
- **Tokens consumed (v2).** `--plate`, `--ebony`, `--gilt`, `--ink`,
  `--steel`, `--steel-bright`, `--ruby`, `--hairline`,
  `--ease-settle`, `--ease-tick`, `--ease-draw`.

### 6.12 Movement-aperture plates & calibre cards

- **What & why.** Images and index entries live in movement
  apertures: circular polished openings in the plate, rimmed in
  `--plate-shadow` with a gilt hairline, through which a photograph
  (a movement detail, a watchmaker's hands, a finished calibre) is
  seen as through a display back. Listing cards are small plates of
  their own, each carrying one aperture, its figures in mono, and two
  jewel bearings at its pivot corners (§4's allocation: 6 across the
  card row). A picture in this theme is never pasted on the plate; it
  is *under* it, seen through the opening made for it.
- **Structure.** A `<figure>` aperture: outer rim ring (SVG circle
  strokes), an inner shadow gradient giving the opening depth (6px),
  the `<img>` clipped to the circle, scaling inside it. Cards: an
  `<article>` plate with the aperture left, title in Instrument
  Serif, two mono figure lines (drawn from the card's record — e.g.
  "TEETH 60 · RATIO ×1.40" for a wheel card), and a text link. Image
  `alt` is mandatory and written as a bench description (§12).
- **Motion spec.** Entry: as the aperture crosses the reading line,
  the image scales 1.04 → 1.0 over 700ms `--ease-draw` (the movement
  settling under its crystal) while the rim's gilt hairline draws
  itself once around (stroke draw, 500ms, `--ease-draw`) — the
  opening is machined as it arrives. Cards step with §6.4 like all
  sections' children (their bearings are the pivots). Hover: the
  loupe (§6.8) applies; the image itself does not zoom further — a
  crystal does not magnify.
- **States.** Rest: image settled, hairline complete. Hover: loupe +
  bearings brighten. Focus: the card's link takes the ring; the
  aperture's hairline turns `--steel`. Active: the tick (§6.9) at
  the card's bearing. Scrolled-past: settled, still. Disabled
  (image failed): the aperture shows the plate's perlage field with
  the alt text printed as a bench-note caption inside the opening —
  a missing photograph is an empty aperture on the record, never a
  broken-image icon.
- **Content merge.** The aperture's diameter is a module of the
  column (§4: ÷3, ÷4, ÷6), the bearings are two of the record's 27,
  and a card's mono figures are its subject's actual data from
  §6.17's family tables (wheel cards carry tooth counts; service
  cards carry register figures). The frame is sized by the layout's
  module and filled by the record's numbers — nothing about it is
  stock.
- **Failure fallback.** Watchdog: the scale and hairline are
  scrub-armed only; if the loop is dead, images ship at 1.0 with the
  hairline fully drawn (markup state). No JS: identical. Slow image:
  the aperture holds perlage until the image arrives, then a single
  300ms cross-fade — the opening waits like a bench waits for a part.
- **Reduced-motion variant.** No scale, no hairline draw: apertures
  arrive complete. The loupe's static variant (§6.8) still serves
  inspection.
- **Performance budget & mobile variant.** Images are the page's
  raster budget (§14: ≤150KB each, WebP/AVIF, responsive sizes);
  motion is transform/opacity only, ≤0.1ms/frame per in-view
  aperture. Mobile: apertures shrink one module (÷4 → ÷3 of the
  narrower column), cards stack single-column, hairline draw cut.
- **Choreography timeline (v2).** Aperture crosses line → hairline
  draws 500ms while image settles 1.04 → 1.0 over 700ms → bearings
  seat with the card's step (§6.4) → rest → hover: loupe timeline
  (§6.8) → leave: release.
- **State matrix (v2).** *Rest:* settled, complete. *Hover:* loupe,
  bearings bright. *Focus:* hairline steel + link ring. *Active:*
  tick at bearing. *Scrolled-past:* settled. *Disabled (no image):*
  perlage + printed alt. *Touch:* tap follows the link; no hover
  states are load-bearing.
- **Breakpoints (v2).** ≥1200px: apertures at ÷3/÷4 modules, cards
  3-up. 768–1199px: ÷4 module, cards 2-up. <768px: cards 1-up,
  aperture ÷3 of column, hairline static.
- **Edge cases & failure modes (v2).** *Portrait images in a circular
  aperture:* the crop is set per-image at build (`object-position`
  from the image's declared focal point in its record); a builder
  never centre-crops a movement photo blind — hands and wheels crop
  differently, and the record says which. *A listing with 40 cards:*
  pagination per §11, 12 per page; bearings per page still sum
  within the record's allocation because bearings belong to the page
  template, not to each card's data.
- **Accessibility spec (v2).** Real `alt` on every image, bench-written
  ("Centre wheel and bridge, calibre C&E 67, before casing"). The
  aperture rim is decorative (`aria-hidden` SVG). Card = one link
  with a single accessible name including its figures ("Centre wheel
  — 60 teeth, ratio ×1.40"). Focus ring 2px `--steel` at 3px offset.
- **Tokens consumed (v2).** `--plate-shadow`, `--gilt`, `--gilt-pale`,
  `--steel`, `--ruby-bright`, `--ease-draw`, `--aperture-module`,
  `--img-budget` (150KB).

---

### 6.13 The movement spec table

- **What & why.** The specification table is the theme's honesty made
  structural — and by the original entry's anti-slop ruling, it lists
  *the site's own movement*: total parts (the page's real component
  count), jewels (its interactive elements), power reserve (its
  average session length) — printed beside the calibre's own figures,
  which are §6.17's. Two columns of numbers, one object described
  twice: the watch's movement and the page's. A hurried reader comes
  here and gets every fact without watching a single wheel turn.
- **Structure.** A semantic `<table>` under a pinned bridge (§4):
  caption "Specification — Calibre C&E 67 and this page's movement",
  rows in three groups (Rate, Train, Reserve) with `<th scope="row">`
  labels, values right-aligned in IBM Plex Mono. The calibre column
  carries §6.17's figures verbatim: 28,800 vph; 212 parts; 27 jewels;
  teeth 84/60/48/40/15; reserve 62 h; wind 6.5 turns; rate +4 s/day.
  The page column carries the site's measured equivalents (components
  rendered, interactive elements, median session from analytics),
  each with its "as measured" date in a footnote row — the page's
  figures are data with a provenance, not poetry.
- **Motion spec.** The table itself barely moves: its bridge pins
  for the section's duration while rows pass beneath (the one content
  pin, §5). Rows print in with the section step (§6.4). The single
  licensed flourish: the rate row's figure is live — it is §6.6's
  readout restated in the table, flipping with the wheel. Every
  other figure is print. Restraint is the spec: the table a
  connoisseur trusts is the table that does not perform.
- **States.** Rest: printed, bridge pinned. Hover (row): row ground
  lifts to `--plate-shadow` at 40% over 180ms `--ease-draw`, and the
  row's pivot bearing (4 allocated here, §6.17) brightens. Focus:
  rows are not focusable; the table's one link (to the record,
  §6.17) takes standard states. Scrolled-past: printed. Disabled:
  a figure not yet measured (a new page type without analytics)
  prints as "—" with the footnote "not yet on the timing machine" —
  an admitted gap, never an invented number.
- **Content merge.** This table *is* §6.17 presented in reading flow —
  same figures, same order, same totals — and §6.5's barrel shows two
  of its rows (6.5 turns, 62 h) as a working gauge while §6.3's train
  shows its teeth as working wheels. Table, gauge and train are three
  readings of one record; §10's figure audit re-derives all three
  from §6.17 and fails the build if any disagrees.
- **Failure fallback.** None required beyond the theme's base law:
  the table is static HTML; it cannot fail into invisibility. No JS:
  identical, minus the live rate figure, which prints statically at
  28,800 — still true.
- **Reduced-motion variant.** Identical, minus the row-lift
  transition (instant) and the live flip (rate printed statically;
  the wheel's own readout §6.6 carries liveness for those who want
  it, in its reduced form).
- **Performance budget & mobile variant.** Zero JS beyond the shared
  live figure. Mobile (<768px): the two value columns stack into
  paired lines per row (label, then "Calibre — · Page —" in mono),
  same order, same figures; no horizontal scroll is ever permitted —
  a specification you must pan is a specification lost.
- **Choreography timeline (v2).** Section steps in (§6.4) → bridge
  pins → rows pass beneath as the reader scrolls the group order
  Rate → Train → Reserve → the regulation row arrives last: "+4
  S/DAY" with its ruby mark — the table's one ruby, spent where the
  claim is boldest → bridge unpins at the section's foot.
- **State matrix (v2).** *Rest:* printed, pinned bridge. *Hover:*
  row lift + bearing. *Focus:* record link only. *Active:* n/a.
  *Scrolled-past:* printed. *Disabled:* unmeasured figures print
  "—" with the footnote. *Touch:* tap on a row = the lift for 600ms.
- **Breakpoints (v2).** ≥1200px: full 3-column table (label, calibre,
  page). 768–1199px: same, values at 0.8125rem mono. <768px: stacked
  paired-line layout.
- **Edge cases & failure modes (v2).** *Page figures change (a
  redesign adds components):* the page column is regenerated from the
  build's component manifest at deploy, and the "as measured" date
  updates — a stale page column is a wrong specification, and §10
  fails it against the manifest. *Analytics absent:* the reserve row
  prints "—" per the disabled rule rather than borrowing the
  calibre's 62 — the two columns must never quietly become one.
- **Accessibility spec (v2).** Real table semantics: caption, scoped
  headers, a `<tfoot>` footnote row. Screen readers receive the
  specification in its most native form. Contrast: `--ink` on
  `--plate` 12.9:1; mono values `--steel`-deepened to `--ink` for
  text (steel is for labels); the ruby regulation mark is paired
  with the printed word "regulation" — never colour-alone.
- **Tokens consumed (v2).** `--plate`, `--plate-shadow`, `--ink`,
  `--steel`, `--ruby`, `--hairline`, `--ease-draw`.

### 6.14 The regulation-request form

- **What & why.** The conversion: a visitor whose watch runs fast or
  slow — or who simply wants the manufacture to regulate it — files a
  regulation request. The form is a service-register page on plate:
  fields for the owner's name, the watch's calibre and serial, its
  observed rate ("+9 s/day, as timed at home"), and the service
  asked for. On submit, the confirmation is a register entry —
  "Entered in the service register as № 1,138" — and the register
  count printed in the preamble ("1,137 entries stand in the
  register") increments by the escapement tick (§6.9). The visitor's
  act is booked into the same ledger the theme has been keeping all
  page long.
- **Structure.** A real `<form>` with native validation, enhanced
  never replaced: labelled inputs on `--plate`, `--ink` text, 2px
  `--steel` focus outlines plus the field's pivot bearing brightening
  (§6.8's jewel rule). The preamble prints the derivation before a
  word is written: "The register stands at 1,137 entries. Yours will
  be № 1,138." — so the confirmation number is a kept promise, not a
  surprise. Submit is a bridge-styled button with its own tick gear
  (§6.9, 60-tooth centre glyph). Without JS the form posts natively
  and the server returns the same register entry with the next
  number.
- **Motion spec.** Field focus: bearing brightens 120ms, field ground
  lifts plate → plate + 4% steel tint over 200ms. Submit: the button
  ticks (§6.9); the form dims to 65% over 250ms while the entry is
  written, the button showing the unfinished-plate shimmer (§6.15)
  — never a spinner; a register is written, not loaded. Success: the
  confirmation entry prints in with a 320ms `--ease-settle` rise; at
  t=200 the register readout flips 1,137 → 1,138 (§6.6 mechanism)
  and the form's jewel (3 allocated here, §6.17) seats ruby. Error:
  the offending field's bearing turns `--ruby` (the bench's one
  error colour) and its error line prints beneath in `--ink` —
  no shake, no amber, ever (§12's error voice).
- **States.** Rest: register printed, № 1,138 promised. Focus: per
  field, above. Active (submitting): form at 65%, button shimmering,
  fields disabled. Success: entry + flipped register + seated jewel.
  Error: field marked, error line printed, focus moved to the first
  error, values preserved. Scrolled-past: an in-flight submission
  completes regardless of scroll. Disabled (endpoint down): the form
  prints a register note — "The register is closed this evening;
  requests resume at the bench tomorrow" — and holds the visitor's
  words in the fields, unsent and unlost.
- **Content merge.** The form's calibre select *is* §6.17's calibre
  family; its rate field is denominated in the record's own unit
  (s/day, against the record's +4); its preamble number is the
  register's count and its confirmation is that count + 1, derived
  in print before the visitor acts. The conversion is transacted
  inside the theme's ledger, not decorated with it.
- **Failure fallback.** Watchdog `WD-FORM` at 4,000ms on submission:
  no response → the form restores from 65%, prints "the entry could
  not be written — your words are still here" with values intact;
  the submit token is idempotent per form instance, so nothing can
  double-book. Canvas/loop failure: irrelevant — the form is DOM;
  its tick and flips degrade per §6.9/§6.6 fallbacks.
- **Reduced-motion variant.** Confirmation prints instantly; the
  register number swaps as static text; no dimming transition
  (fields disable without the fade). Errors print without motion.
- **Performance budget & mobile variant.** Form JS ≤5KB gz deferred,
  the page's only non-loop script. The tick and flip reuse shared
  mechanisms — zero extra per-frame cost. Mobile (<768px): single
  column, fields full measure, submit sticky at the form's foot
  inside its own box, targets ≥48px.
- **Choreography timeline (v2).** Focus field → bearing 120ms →
  submit: tick 40ms → form dims 250ms → shimmer while writing →
  response → entry rises 320ms → t=200 register flips to 1,138 →
  jewel seats → confirmation at rest. Watchdog ceiling 4,000ms.
- **State matrix (v2).** *Rest:* printed, № 1,138 promised. *Hover:*
  field bearing warms. *Focus:* bearing + tint + outline. *Active:*
  submitting state as above. *Scrolled-past:* waits; submission
  completes. *Disabled:* register-closed note, values held.
  *Touch:* identical; submit full-width.
- **Breakpoints (v2).** ≥1200px: two-column register (calibre +
  serial side by side), measure 42rem. 768–1199px: single column,
  36rem. <768px: single column full measure, sticky submit.
- **Edge cases & failure modes (v2).** *A rate entered beyond
  plausible (±600 s/day):* the register voice accepts and annotates —
  the entry prints "as reported; the timing machine will have its
  say" — the ledger records claims as claims (§12). *Duplicate
  request (same serial, same week):* the entry prints with the
  marginal note "second entry for this calibre — the bench will
  marry the two", corroboration not duplication. *Serial not in the
  family list:* the form does not reject; it books the request as
  "calibre as stated" — a register records what it is given.
- **Accessibility spec (v2).** Visible native labels on every field
  (`--ink` on `--plate`, 12.9:1); errors via `aria-describedby` plus
  an `aria-live="polite"` summary in the register's own words; the
  confirmation is an `aria-live` region announcing "Entered in the
  service register as № 1,138" once. Focus management: first error
  on failure, confirmation heading on success. The ruby bearing is
  always paired with printed error text — never colour-alone.
- **Tokens consumed (v2).** `--plate`, `--plate-shadow`, `--ink`,
  `--steel`, `--ruby`, `--ease-settle`, `--ease-tick`,
  `--dur-watchdog-form` (4000ms), `--register-count` (1137).

### 6.15 Unfinished-plate loader & cage page transition

- **What & why.** Loading in this theme is an unfinished movement:
  content regions still arriving show a bare plate with perlage
  shimmer and the *outlines* of their bridges and apertures — parts
  not yet fitted — and as each region's content lands, its jewels
  seat (ruby points kindle at its pivots) and the content prints in.
  The page transition is the tourbillon cage: leaving, the cage
  rotates the old page out in cage steps; arriving, the new page
  steps in and its balance wheel is already beating. A spinner would
  be a part from another machine; an unfinished plate is this
  movement, not yet finished — the same object in an earlier state.
- **Structure.** Skeleton regions are DOM elements with
  `data-unfinished` styling: perlage field (CSS gradient, §4),
  bridge/aperture outlines in `--hairline`, pivot points drawn as
  empty gilt chatons. Completion is a class swap (`.is-jewelled`):
  chatons fill ruby over 200ms, outlines lift, real content —
  already in the DOM or injected complete — prints beneath. The
  transition is a mode of §6.4's step applied to the page root: the
  outgoing page rotates 3° and steps down over 300ms `--ease-settle`;
  the incoming page arrives pre-stepped and locks with the 60ms
  ratchet.
- **Motion spec.** Perlage shimmer: the skeleton's circles catch a
  slow light pass at 8% opacity on a 2.6s `--ease-beat` phase —
  metal awaiting parts, barely alive. Jewelling on data: pivots
  fill over 200ms staggered 40ms in assembly order, content rises
  240ms `--ease-settle` as outlines fade. Hard ceiling: any region
  unfinished at 1,500ms prints its content anyway, jewelled or not —
  the bench does not hold a reader hostage to a late part.
  Transition: out-step 300ms, navigation, in-step 320ms + lock —
  total perceived interruption ≤900ms, watchdogged at 1,200ms.
- **States.** Unfinished (shimmer, empty chatons) → jewelling →
  finished (rest). Error (a region's data fails): the plate prints
  its bench note in `--ink` — "This part has not reached the bench —
  [retry]" — with a real retry control; the skeleton never shimmers
  forever. Focus: skeleton regions are unfocusable and `aria-hidden`
  until printed. Scrolled-past: regions below the fold jewel on
  arrival regardless of visibility — by the time the reader arrives,
  they are finished movements.
- **Content merge.** The skeleton is the region's own plate, drawn
  with its own bridges and pivots — the unfinished state is shaped
  like the finished content because it *is* the finished content's
  substrate. The transition's cage step is §6.4's section step at
  page scale: one gesture, two sizes, the theme's coherence kept.
- **Failure fallback.** Watchdogs per region at 1,500ms (print
  regardless) and on the transition at 1,200ms (the destination
  forces its finished state — a reader may never be stranded
  between pages inside a rotating cage). No JS: no skeletons, no
  transition; plain navigation, complete pages.
- **Reduced-motion variant.** No shimmer, no cage step: skeletons
  are static perlage fields that swap to print instantly on data;
  transitions are plain navigations with the destination fully
  assembled.
- **Performance budget & mobile variant.** Skeletons are gradients —
  zero raster, zero per-frame JS. The transition reuses §6.4's
  mechanism. Mobile: out-step rotation halves to 1.5°, shimmer cut
  (static perlage) to save battery.
- **Choreography timeline (v2).** Region requested → unfinished
  plate prints with the layout → data lands → chatons jewel 200ms
  staggered → content rises 240ms → region finished. Ceiling
  1,500ms forces print. Transition: click → out-step 300ms →
  navigate → in-step 320ms → lock 60ms → finished page, wheel
  beating. Watchdog ceiling 1,200ms.
- **State matrix (v2).** *Rest:* finished content. *Hover:* n/a.
  *Focus:* skeletons unfocusable, `aria-hidden`. *Active:* the
  form's submitting button (§6.14) wears this shimmer. *Scrolled-past:*
  pre-jewelled print. *Disabled / no-JS:* server print, no skeletons.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full treatment. 768–1199px: shimmer
  period 3.2s. <768px: static skeletons, 1.5° transition step.
- **Edge cases & failure modes (v2).** *Data arrives before the
  skeleton paints (fast cache):* the region prints directly — a
  skeleton that never appears is the best kind. *Partial arrival
  (2 of 5 cards):* arrived cards jewel and print; the rest hold
  unfinished until their own retry or the ceiling, then print their
  bench notes individually — the movement opens with gaps admitted,
  not with the page held shut. *Double navigation mid-transition:*
  the watchdog belongs to the destination; the final page still
  lands finished.
- **Accessibility spec (v2).** Skeleton containers carry
  `aria-busy="true"` and are removed from the accessibility tree
  until printed; one polite announcement ("The movement is
  assembled") fires when the last above-fold region prints — not one
  per region. The transition is never announced. Bench-note contrast:
  `--ink` on `--plate` 12.9:1.
- **Tokens consumed (v2).** `--plate-deep`, `--hairline`, `--gilt`,
  `--ruby`, `--ink`, `--ease-settle`, `--ease-beat`,
  `--dur-unfinished-ceiling` (1500ms), `--dur-watchdog-transition`
  (1200ms).

---

### 6.16 Chapter-ring footer

- **What & why.** The footer is the movement's chapter ring laid on
  the ebony bench: a broad dial whose minute track carries the
  site's closing stations (colophon, register, contact, legal) as
  engraved markers, a blued seconds hand stepped by the balance
  wheel's beats, and at its centre the calibre's totals printed for
  the third and final time — 212 parts, 27 jewels, 62 hours — the
  record's figures at the page's foot, where a watchmaker signs. The
  footer is where the movement is signed and set down; it should
  feel like both.
- **Structure.** A `<footer>` on `--ebony`: a wide, shallow chapter
  ring (SVG arc, not a full circle — a ring segment spanning the
  footer's width, radius ≈ column width) with 60 minute ticks, the
  closing stations as gilt-engraved labels at their minute
  positions, a seconds hand (blued, counterweighted) pivoting at the
  ring's centre below the fold line, and the totals line in mono:
  "PARTS 212 · JEWELS 27 · RESERVE 62 H — C&E 67". Two jewel
  bearings (§6.17's allocation) flank the totals. Colophon and legal
  lines print beneath in `--plate` at 70%.
- **Motion spec.** The seconds hand is stepped by §6.1's beats:
  one beat = one step of 0.75° (a true seconds hand at 28,800 vph
  advances 8 steps per second — the hand visibly trembles forward in
  escapement steps of 60ms `--ease-tick`, exactly as a deadbeat
  seconds does). It starts at the minute position corresponding to
  the reader's arrival minute — the footer tells the session's time,
  not the factory's. The ring's gilt labels draw in once (§6.7's
  draw, 600ms) as the footer first arrives. Nothing else moves: a
  signature does not animate.
- **States.** Rest: hand stepping, totals printed. Hover: a station
  label warms to `--gilt-pale` and its tick lengthens 2px. Focus:
  label + 2px `--steel-bright` outline (steel on ebony must be the
  bright cut, §2). Active: the station's tick (§6.9) at the footer's
  nearest bearing. Scrolled-past: the footer is the end; beyond it,
  the barrel (§6.5) stands at full wind — the two end-states agree.
  Disabled: a station with no page prints dimmed, unticked.
- **Content merge.** The footer's totals are §6.17's third printing
  (§10 audits all three: hero readout family, §6.13's table, here),
  its hand is driven by the same wheel that has beaten down the
  whole margin, and its stations are the page's closing stations in
  the movement's own geometry. The page ends the way the movement
  is signed: name, numbers, and a hand still moving.
- **Failure fallback.** If the loop is dead, the hand rests at the
  arrival minute (its markup position is computed at build for the
  hour's :00 — a static footer prints the hand at top, totals
  intact). No JS: identical printed footer.
- **Reduced-motion variant.** The hand is still, set to the arrival
  minute as static drawing; labels print without the draw. The
  totals — the footer's actual content — are untouched.
- **Performance budget & mobile variant.** One 60ms hand step per
  beat (8/s) — a transform on one SVG group; ≤0.03ms/frame. Mobile:
  the ring flattens to a straight minute track across the footer
  top (a ring segment too shallow reads as a mistake on a narrow
  plate), hand kept at 60% length, totals wrap to two mono lines.
- **Choreography timeline (v2).** Footer enters → labels draw 600ms
  → hand already stepping (it never stopped) → reader reaches the
  totals: the barrel (§6.5) completes its arc in the rail at the
  same scroll moment → page at rest, movement signed, wheel still
  beating above.
- **State matrix (v2).** *Rest:* hand stepping, totals printed.
  *Hover:* label warms, tick lengthens. *Focus:* label + bright
  outline. *Active:* tick at bearing. *Scrolled-past:* end-state,
  barrel full. *Disabled:* dim, unticked station. *Touch:* stations
  are ≥44px targets along the track.
- **Breakpoints (v2).** ≥1200px: full ring segment, hand 120px.
  768–1199px: ring radius tightens, hand 88px. <768px: straight
  track, hand 64px, totals two lines.
- **Edge cases & failure modes (v2).** *Reader lingers at the
  footer for minutes:* the hand keeps true session time (beat-
  derived, §6.6's clock rule), completing a revolution per minute —
  the footer quietly becomes a clock, which is the correct fate for
  a watch site's footer. *Print:* the footer prints on plate (the
  bench inverts to save ink; totals and stations remain, hand drawn
  at its position) — print styles are specified, not inherited.
- **Accessibility spec (v2).** Footer landmark with `aria-label`;
  stations are real links with full names ("Service register",
  never just a tick). The hand and ring are `aria-hidden`. Totals
  contrast: `--gilt` on `--ebony` 5.6:1 for the mono line (large/
  data text), body lines `--plate` on `--ebony` 11.8:1.
- **Tokens consumed (v2).** `--ebony`, `--gilt`, `--gilt-pale`,
  `--plate`, `--steel-bright`, `--ruby`, `--ease-tick`,
  `--ease-draw`, `--dur-step-hand` (60ms).

### 6.17 The calibre record — the one source of every figure

- **What & why.** Every theme in this library keeps one declared
  record; this theme's is the calibre itself, and it is an element
  of the page, not a note in a drawer: a register section, printed
  near the foot, where Calibre C&E 67 "Atelier No. 7" is specified
  completely — the single source from which the wheel's rate, the
  train's teeth, the barrel's turns, the table's figures and the
  form's register number are all taken. The record exists so the
  page can be *checked*: a reader, a builder or §10's gate can lay
  any number on the page against this section and find it exact.
- **Structure.** A `<section>` styled as a register page on plate
  under its bridge (§4): the calibre's name engraved (Instrument
  Serif), then the record in mono register lines, grouped as
  Rate / Train / Reserve / Register. It is data in prose's clothing
  — no table chrome (§6.13 is the table; this is the ledger it was
  copied from), each line a label and a figure, figures in IBM Plex
  Mono.
- **Motion spec.** None of its own: the record steps in with §6.4
  like every section and then does not move. A ledger that performs
  is a ledger auditioning; this one simply stands open. Its one
  live line is the register count, which flips (§6.6) if §6.14's
  form is submitted during the session — the record acknowledges
  its own amendment, in place, once.
- **States.** Rest: printed, complete. Hover: register lines lift
  like §6.13's rows (they are kin). Focus: the section's anchor is
  the barrel's link target (§6.5) — focus lands on its heading with
  the standard outline. Scrolled-past: printed. Disabled: n/a — the
  record is never disabled; a page may lose its gauges before it
  loses its record.
- **Content merge.** This section is the merge made visible: every
  other element in §6 cites it, and it cites nothing but the
  manufacture's facts. It is placed after the form and before the
  footer deliberately — the visitor who has acted (booked a
  regulation) can now read the ledger their act was entered into.
- **Failure fallback.** Static HTML; the record cannot fail. If
  every script on the page dies, this section remains the page's
  complete specification — which is precisely its job.
- **Reduced-motion variant.** Identical. (The record had no motion
  to reduce.)
- **Performance budget & mobile variant.** Zero. Mobile: register
  lines stack label-over-figure; grouping heads remain.
- **Choreography timeline (v2).** Section steps in (§6.4 timeline) →
  lines at rest → (if §6.14 succeeded earlier or later) the register
  line flips 1,137 → 1,138 once, at the moment of the entry → rest.
- **State matrix (v2).** *Rest:* printed. *Hover:* line lift.
  *Focus:* heading outline via anchor. *Active:* n/a.
  *Scrolled-past:* printed. *Disabled:* never. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: two-column register lines.
  768–1199px: two columns, narrower figures. <768px: stacked lines.
- **Edge cases & failure modes (v2).** *The record must change (a
  new calibre replaces C&E 67):* the change is made here first;
  §10's audit then fails every stale figure elsewhere until they
  are updated — the failure is the feature: one source, enforced.
  *Session amendments:* only the register count may change in
  session (1,137 → 1,138 by §6.14); no other line is writable by
  interaction — rate, teeth and reserve are facts, not settings.
- **Accessibility spec (v2).** A headed section with a definition
  list's semantics (`<dl>`), so each figure is programmatically its
  label's value. Read in full by a screen reader in under a minute —
  the record is short because a calibre's truth is short.
- **Tokens consumed (v2).** `--plate`, `--ink`, `--steel`, `--gilt`,
  `--hairline`, `--ease-draw`.

**The record, as printed:**

| Group | Entry | Figure |
|---|---|---|
| Rate | Beat rate | 28,800 vph (4 Hz; 8 beats per second) |
| Rate | Balance amplitude | ±270° |
| Rate | Regulation | +4 seconds per day |
| Rate | Hairspring | 7 coils, overcoil terminal |
| Train | Barrel | 84 teeth |
| Train | Centre wheel | 60 teeth (×1.40 on the barrel) |
| Train | Third wheel | 48 teeth (×1.75) |
| Train | Fourth wheel | 40 teeth (×2.10); 1 revolution per 60 s |
| Train | Escape wheel | 15 club teeth (×5.60); one tooth per beat; 1 revolution per 15 beats (1.875 s) |
| Train | Fourth-to-escape ratio | 32 : 1 (60 s ÷ 1.875 s) |
| Reserve | Power reserve | 62 hours |
| Reserve | Full wind | 6.5 barrel turns (2,340°) |
| Whole | Parts | 212 |
| Whole | Jewels | 27 — set on this page as: hero 3 · margin train 5 · spec table 4 · card row 6 · form 3 · footer 2 · record section 2 · 404 2 |
| Whole | Dimensions | Ø 30.4 mm (13½ lignes), 4.2 mm thick |
| Register | Entries standing | 1,137 — the next entry is № 1,138 |

*Arithmetic audit (printed so the gate need not trust): ratios are
84 divided by each wheel's teeth — 84/60 = 1.40, 84/48 = 1.75,
84/40 = 2.10, 84/15 = 5.60. Beats: 28,800 ÷ 3,600 = 8 per second;
escape revolution 15 beats ÷ 8 = 1.875 s; fourth-to-escape
60 ÷ 1.875 = 32. Wind: 6.5 × 360° = 2,340°. Jewels: 3+5+4+6+3+2+2+2
= 27. Register: 1,137 + 1 = 1,138.*

### 6.18 The stopped movement — empty state & 404

- **What & why.** Where the page finds nothing — a search with no
  calibre, a listing with no wheels, a URL with no page — the
  movement is stopped: a perlage plate with the balance wheel drawn
  at rest (+38°, §6.1's drawn position), the train still, and the
  bench's plain statement of the fact, with the way back printed as
  real links. A stopped movement is not a broken one — it is the
  honest state of a mechanism with nothing to drive — and this theme
  treats absence as a state of the machine, never as an error page
  borrowed from another site.
- **Structure.** A full plate field on the ebony bench: perlage
  ground (§4), a large still movement drawing (SVG: wheel at +38°,
  train at rest angle, barrel unwound) at the field's left, the
  statement at right — heading in Instrument Serif ("The movement
  has stopped"), one line of bench copy (§12's empty voice), and
  exits: back to the plate (home), open the record (§6.17), file a
  regulation request (§6.14 — a visitor lost may well be a visitor
  whose watch needs the bench). Two jewel bearings (§6.17) sit at
  the drawing's pivots, lit — a stopped movement keeps its jewels;
  only its drive is gone.
- **Motion spec.** None, and the none is specified: no wheel turns,
  no sheen passes, no step plays on arrival. The stillness is the
  message, held for exactly as long as the visitor stays. (The
  site's global instruments do not intrude: the rail is absent on
  this page type — §7 rules the 404 a bench page, not a movement
  page.) One exception, deliberate: if the visitor arrived from a
  mistyped calibre URL, the suggested correct calibre's name is
  cased (§6.2's mechanism, instant variant) — the single moving
  thing is the way back.
- **States.** Rest: still, printed. Hover: exit links take §6.11's
  station states. Focus: first exit is the primary action and takes
  initial focus on load for the 404 only (an empty state inside a
  working page never steals focus). Scrolled-past: the page is
  short; n/a. Disabled: n/a.
- **Content merge.** The drawing is the page's own movement at rest —
  the same wheel, train and barrel the visitor has watched working,
  now stopped — so the absence reads as *this* site's absence, in
  its own mechanism's language. The exits are the theme's real
  destinations, and the record link offers the one thing a lost
  visitor can still do: read the specification of the thing they
  were looking for.
- **Failure fallback.** The 404 is the fallback's fallback: static
  HTML on the bench ground, no script required for any part of it.
  If the whole site is degraded, this page is the last one standing,
  and it is complete.
- **Reduced-motion variant.** Identical — the page already honours
  stillness absolutely.
- **Performance budget & mobile variant.** One static SVG, zero JS
  budget. Mobile: drawing above statement, at 70% width; exits stack
  full-width.
- **Choreography timeline (v2).** Arrival → stillness (no beats) →
  the suggested calibre's name, if any, cases instantly at t=0 →
  visitor chooses an exit → normal transition (§6.15) resumes the
  working site.
- **State matrix (v2).** *Rest:* stopped, printed. *Hover:* exit
  states per §6.11. *Focus:* primary exit focused (404 only).
  *Active:* exits navigate. *Scrolled-past:* n/a. *Disabled:* n/a.
  *Touch:* exits are ≥48px targets.
- **Breakpoints (v2).** ≥1200px: drawing left, statement right.
  768–1199px: same, drawing 40%. <768px: stacked, drawing 70%.
- **Edge cases & failure modes (v2).** *Empty search (not a 404):*
  the same stopped plate appears inside the listing page as a
  section — the movement stops locally, the site around it keeps
  beating; the copy changes ("No calibre answers to that name") but
  the state language does not. *A filter with one result:* not an
  empty state — one wheel is still a train of one; the plate shows
  the single result without ceremony.
- **Accessibility spec (v2).** The 404's heading is the page's `<h1>`
  and its status is conveyed in text, never only by the still
  drawing. The drawing is `aria-hidden` with the statement carrying
  its meaning. Exit contrast on ebony: `--plate` 11.8:1, gilt
  labels 5.6:1 (labels are large/engraved style, §3).
- **Tokens consumed (v2).** `--ebony`, `--plate`, `--plate-deep`,
  `--gilt`, `--ink`, `--ruby`, `--hairline`.

---

## 7. Page application map

The movement's drive order (§4) governs every page type; a page may
omit a movement, never reorder the train.

| Page type | Movement arrangement | Elements in play | Notes |
|---|---|---|---|
| **Home** | Full calibre: hero aperture → bridges → train chapter → escapement proof → spec → form → record → chapter-ring footer | All 18 | The reference build; §8 and §13 describe this page |
| **Listing** (calibres / wheels) | Plate of apertures; the train runs as the filter mechanism — filtering re-meshes the card grid in cage steps | §6.3 (as filter drive), §6.4, §6.12, §6.18 (empty) | Jewels per page stay within §6.17's allocation — bearings belong to the template, not per-card data |
| **Detail** (one calibre) | That calibre's own record replaces §6.17's figures *everywhere* on the page — wheel rate, train, barrel all re-derive | §6.1–§6.7 at the detail's figures, §6.13 (single column), §6.14 | The one-source law is per-page: a detail page for a 21,600 vph calibre beats at 3 Hz or it does not ship |
| **About / the bench** | The manufacture's story told in assembly order; the drawings chapter (§6.7) leads | §6.2 (the founder's name cased), §6.7, §6.12, §6.16 | Ambient loops unchanged — history does not license a third loop |
| **Journal / log** | Entries as register lines (§6.17's clothing); the beat counter is replaced by the entry count, flipped by §6.9 ticks as entries are opened | §6.4, §6.11, §6.17 styling | Mono stays for figures; entry prose is Inter, always |
| **Contact / service** | The form (§6.14) is the page; the record stands beneath it | §6.14, §6.17, §6.16 | No hero ceremony — a visitor with a stopped watch is not made to watch a casing |
| **Checkout equivalent** | **Refused the full theme.** Payment is not a movement ceremony: checkout uses plate ground, Inter, the form's field/focus/error language and the tick on the confirm button — no wheel, no train, no loupe | §6.14's language, §6.9 only | §9 names a beating wheel beside a card form as this theme's gravest slop; money is taken plainly or not at all |
| **404 / empty** | The stopped movement (§6.18) | §6.18, §6.11 stations | A bench page: no rails, no ambient loops |

---

## 8. Worked examples

### 8.1 The hero — the calibre is cased (worked example 1)

The visitor arrives. The plate is already there — DOM-complete,
stripes flat, the headline printed in the fallback serif at matched
measure, the wheel drawn at +38°. Nothing is invisible; the ceremony
has not begun and the page is already honest. Then the loop starts:
the balance wheel takes its phase from the clock and is beating —
not starting up, *beating*, as a delivered movement beats when the
case is opened. At t=150 the hero's bridge ends drop 14px and settle
with one recoil. At t=300 two jewels seat ruby at the aperture's
pivots. At t=420 the casing begins: C-A-L-I-B-R-E, glyph by glyph,
60ms apart, each dropping 10px with a 2px overshoot and a single
damped bounce, through the aperture's circular mask; the ampersand
takes its beat; ESCAPEMENT follows — eighteen glyphs, the last
locking at t≈1,620. At t=1,650 the readout beneath the wheel in the
rail begins its count, flipping up through the digit places until at
t≈4,050 it steadies: RATE 28,800 VPH, and below it the beat counter
starts at 000001 and ticks, eight to the second, in time with the
wheel the reader can see. Down the left rail the train stands meshed,
gilt tooth at top, waiting for the reader's hand. The barrel reads
RESERVE 00.0 H / 62 H. Total ceremony: about four seconds, of which
the reader needed none — every fact was printed from the first byte.
What the ceremony added was not information but *evidence*: this
page assembles itself the way its subject is assembled, in the
order a watchmaker works, and then it keeps time.

### 8.2 Mid-page — the escapement chapter, as the visitor lives it (worked example 2)

Ninety seconds into the read, the visitor reaches the spec chapter —
the page's ebony bench section. The section steps in on its bearing:
1.5°, a two-tick lock, its bridge screw turning 45° + 45° in the
header's sympathy. The bench field carries the two drawings. As the
field crosses the reading line the train profile begins to draw
itself — barrel first, 84 teeth of outline at a steady hand's
900 px/s, its centre line ticking in as it completes; centre, third,
fourth; then the little escape wheel, 15 club teeth, and under each
the gilt count: 84 · 60 · 48 · 40 · 15. The visitor has seen these
wheels working in the margin since the hero — flung by their own
scrolling, settled tooth by tooth — and now meets them drawn, in
drive order, like a technical sheet laid beside the running
movement. The hairspring follows, coils blooming centre-outward,
the overcoil slowing the hand at the end. Beneath, the spec table's
bridge pins and the rows pass: Rate — 28,800; Train — the same five
counts, tabulated; and the beat counter in the rail, glanced at,
reads 000720 — ninety seconds at eight beats a second, exactly.
Nothing the visitor has seen disagrees with anything they now read,
because there was only ever one record for all of it to come from.
The regulation row arrives last under the pinned bridge: +4 S/DAY,
its single ruby mark. The visitor scrolls on; the bridge unpins;
the barrel in the rail stands near half wind.

### 8.3 Conversion — a regulation is booked (worked example 3)

The visitor's own watch gains nine seconds a day, and the page's
last movement is the offer: the regulation form, a register page on
plate. Before they type, the preamble has already made the theme's
promise in figures: "The register stands at 1,137 entries. Yours
will be № 1,138." They focus the first field — its pivot bearing
brightens, the field's ground warms a breath toward steel. Name;
calibre — the select offers the family from §6.17's record, their
watch among them; serial; and the rate field, where they write +9 —
the form's hint text denominates it for them: "seconds per day, as
timed at home; the record's own rate is +4". They press the bridge
button. It ticks — one tooth of its 60-tooth glyph, a one-unit flip
somewhere in the mechanism — and the form dims to 65%, the button
wearing the unfinished-plate shimmer while the entry is written: a
register being written, not a page loading. At 900ms the answer
comes. The form rises back, and where it stood there is now an
entry, printed like a register line: "Entered in the service
register as № 1,138 — [name], calibre as stated, rate +9 as
reported; the timing machine will have its say." In the preamble's
place, the count has flipped: 1,138 entries stand in the register.
The form's third jewel has seated ruby. If the visitor scrolls down
to the record section, its register line reads 1,138 too — one
session, one amendment, everywhere the figure stands. The promise
made before the first keystroke has been kept to the digit.

---

## 9. Anti-slop — what makes THIS theme look cheap

Each failure below is specific to a calibre theme; each cure is a
rule a builder can check.

1. **Decorative gears that mesh with nothing.** Random cogs pasted
   behind headings, teeth interpenetrating, ratios impossible.
   *Cure:* every drawn gear carries a tooth count from §6.17, meshes
   at true centre distances, and turns something (§6.3) or is a
   drawing of one that does (§6.7).
2. **A balance wheel at the wrong rate.** A generic 1 Hz sway, or a
   wheel spinning like a fan. *Cure:* 4 Hz, ±270°, sinusoidal dwell,
   clock-derived phase (§6.1). If it doesn't match §6.6's counter,
   both are wrong.
3. **Gold everywhere.** Gilt body text on rhodium (2.9:1 — unreadable
   and instantly cheap). *Cure:* §2's census — gilt is engraved
   names, totals and arcs, on ebony or as hairlines only.
4. **Ruby as a general accent.** Red buttons, red links, red badges.
   *Cure:* 27 bearings + the regulation mark + form error bearings.
   §10 counts ruby occurrences; a 28th is a defect.
5. **Steampunk cosplay.** Rivets, brass pipes, Victorian clip-art,
   sepia. *Cure:* this is a modern manufacture's plate — rhodium,
   blued steel, Geneva stripes; the palette has no brown and no
   brass. Gilt is gold, not brass.
6. **Numbers that disagree.** Hero says 28,800, table says 21,600,
   footer says "38 jewels". *Cure:* one record (§6.17) and §10's
   three-printings audit. Disagreement is the theme's unforgivable
   sin because agreement is its whole claim.
7. **Bouncy, elastic motion.** Parts that spring like toys.
   *Cure:* the five named easings only (§5); every motion ends in a
   settle or a lock. If it bounces twice, it is not an escapement.
8. **A custom cursor shaped like a loupe.** The original standing
   rule and this theme's explicit refusal (§5). *Cure:* the loupe is
   an element (§6.8); the cursor is the system's, always.
9. **A beating wheel beside the checkout.** Ceremony wrapped around
   a card form (§7's refusal). *Cure:* checkout gets the plate, the
   form language and one tick — money is taken plainly.
10. **Screws as decoration.** Screw heads sprinkled on cards that
    hold nothing. *Cure:* screws exist where a bridge is fastened
    (§4) or a state must turn (§6.11) — a screw that fastens nothing
    is a rivet in cosplay (see 5).
11. **Stripes under text.** Geneva striping run beneath body copy
    for "texture". *Cure:* stripes fade to flat plate under reading
    matter (§4); finishing is for open faces.
12. **A "power reserve" that means nothing.** A progress ring
    copied from a music app. *Cure:* the barrel winds 6.5 turns to
    62 hours (§6.5) because the record says so, and the readout
    prints both figures.

---

## 10. Quality gate

Blocking checks — the theme may not be used in a build until every
one passes. The gate is signed by someone other than the builder.

1. **Figure audit.** Every figure on the page re-derived from
   §6.17: 28,800 vph, 8 beats/s, ratios 1.40 / 1.75 / 2.10 / 5.60,
   escape rev 1.875 s, fourth-to-escape 32:1, 6.5 turns = 2,340°,
   62 h, 212 parts, 27 jewels, +4 s/day, register 1,137 → 1,138.
   Any mismatch, anywhere, fails.
2. **Three-printings agreement.** Rate and totals agree across the
   readout family (§6.6), the table (§6.13) and the footer (§6.16).
3. **Jewel census.** Exactly 27 ruby bearings, at §6.17's allocated
   pivots; ruby appears nowhere else except the regulation mark and
   §6.14's error bearings.
4. **Gilt census.** Gilt text only on ebony; no gilt on plate except
   hairlines and the wind arc.
5. **Wheel truth drill.** The beat counter is paused and compared
   against the wheel's phase after 60s: beats counted = 480 ± 0.
6. **Script-dead drill.** All JS disabled: the page reads complete —
   headline cased, sections in register, table and record printed,
   form submittable. Any invisible content fails.
7. **Watchdog drill.** Loop killed at runtime: every armed element
   reaches its final state within its named watchdog (1,000–4,000ms).
8. **Reduced-motion pass.** With `prefers-reduced-motion`: zero
   continuous motion; wheel at +38°; all content present; the copy
   nowhere claims a motion that did not occur.
9. **Ambient census.** Exactly two ambient loops (wheel, sheen).
   A third fails.
10. **Easing audit.** Every animation cites one of §5's five named
    easings; a generic `ease`/`ease-in-out` in the stylesheet fails.
11. **Cursor check.** No custom cursor anywhere; no `cursor: none`.
12. **Performance pass.** §14's budgets met on a mid-tier device:
    frame cost ≤1.6ms, page weight ≤640KB, no long task >50ms
    outside the hero ceremony.
13. **Focus pass.** Every interactive element reachable and visibly
    focused; focus never lands in a moving target (§6.4's rule);
    the loupe's focus variant works with keyboard alone.
14. **Page-column freshness (for §6.13).** The page's own movement
    figures match the build's component manifest and carry a current
    "as measured" date.

---

## 11. Component inventory

Every component a real site in this theme needs, with its themed
treatment. Components the theme refuses are listed with their
in-world replacement — a refusal without a replacement is a gap.

| Component | Treatment in this theme |
|---|---|
| Primary button | A bridge segment: plate ground, `--ink` label in spaced uppercase, tick gear (§6.9) at its right bearing; press = one tooth |
| Secondary button | Open plate, hairline rule beneath the label, steel on hover; no fill — a part not yet bridged |
| Text link | `--steel`, underline drawn `--ease-draw` on hover (the underline is a scribed line) |
| Input / select / textarea | Register fields per §6.14: plate ground, bearing at the label's pivot, steel focus outline |
| Checkbox / radio | A jewel setting: an empty gilt chaton; checked = the ruby seats. Radio groups are a row of chatons, one seated |
| Toggle | Refused as a sliding switch — a movement has no sliders. Replaced by a two-position regulator lever: a small steel arm that ticks 30° between two engraved stops |
| Table | §6.13: pinned bridge, mono values, totals in gilt on the footer's ebony only |
| Badge / tag | An engraved bridge label (§3): uppercase, letterspaced, hairline-ruled — never a coloured pill |
| Alert / notice | A register note: plate-deep band, bench voice (§12), a bearing at its head; warnings take ruby text sparingly — the bench has one serious colour |
| Toast | Refused. Nothing in a manufacture floats over the movement and vanishes. Replaced by the register note pattern, placed in flow, persistent until dismissed by tick |
| Modal | A movement lifted onto the bench: an ebony field dims the plate, the modal is a plate of its own with bridges at head and foot; opens with §6.4's step, never a scale-pop |
| Tabs | A station selector: stations on a bridge (§6.11's language), the current station jewelled; panels step in by §6.4 |
| Accordion | Bridges that lower: the bridge band stays, the section beneath unsteps downward 240ms `--ease-settle`; one open at a time, like one bridge lifted at a time |
| Pagination | The chapter ring in miniature: page numbers on a minute track, the current at the hand's position; prev/next are the ring's end screws |
| Breadcrumbs | The drive order: "Plate / Train / Escapement" — the path *is* the going train of the site, each step a station link |
| Progress | Only the barrel (§6.5). No linear bars anywhere |
| Spinner | Refused absolutely (§6.15). Loading is unfinished plate |
| Skeleton | §6.15: perlage plate, empty chatons, bridge outlines |
| Tooltip | Refused. Inspection is the loupe (§6.8); explanation is a bench-note caption in flow |
| Card | §6.12: aperture plate with bearings at its pivots |
| Form errors | §6.14: ruby bearing + printed line in the register voice; never a red border alone, never a shake |
| Empty state | §6.18: the stopped movement |
| Search | A register query: input on plate, results as register lines; no-results = §6.18 in miniature |
| Footer | §6.16: the chapter ring on the bench |

---

## 12. Content & copywriting voice

Two registers, as a manufacture speaks two ways: **the Engraving**
(display and ceremonial text — spare, declarative, set like a name on
a bridge) and **the Register** (everything functional — exact,
figure-first, written by a clerk who knows the record).

**Headline style (the Engraving).** Short; a name or a claim that can
be checked. ✓ "Calibre & Escapement." ✓ "Regulated to +4 seconds a
day." ✗ "Time, reimagined!!" ✗ "Where precision meets passion" —
unverifiable warmth is the voice's one unforgivable sin, because the
theme's law is that claims are figures.

**Label style (the Register).** Part name + count, uppercase,
letterspaced: ✓ "CENTRE WHEEL — 60 TEETH" ✓ "REGISTER — 1,137
ENTRIES". ✗ "Our amazing wheels!" Labels state what the thing is and
how many; adjectives are left to the reader.

**Data style.** Figures in mono, units always attached, always from
the record: ✓ "28,800 VPH" ✓ "+4 S/DAY" ✓ "RESERVE 62 H". ✗ "super
fast beat rate". A figure without a unit is a part without a calibre.

**Error voice.** The bench admits, locates, and says what happens
next — in that order, without apology theatre: ✓ "The entry could
not be written — your words are still here. The register reopens at
the bench tomorrow." ✓ field level: "A serial is nine characters —
check the case back." ✗ "Oops! Something went wrong 🙁" — no
exclamations, no emoji, no "oops" in a manufacture.

**Empty-state voice.** A fact, then the way back: ✓ "The movement
has stopped. No calibre answers to that name — the record stands
open below." ✗ "404 lol".

**Fixed strings (verbatim, do not paraphrase):** "RATE 28,800 VPH" ·
"The register stands at 1,137 entries. Yours will be № 1,138." ·
"Entered in the service register as № 1,138" · "RESERVE — / 62 H"
(the un-wound gauge) · "The movement has stopped" · "AT FULL WIND"
(the barrel's ceiling note, §6.9).

**Banned phrases.** "Cutting-edge", "revolutionary", "passion for
excellence", "timeless elegance" (unless followed by a figure that
proves it), "oops", "just a second!" on any loader, and any sentence
in which a number appears that is not in §6.17.

---

## 13. Full-page scroll choreography map

The home page, top to footer, in order. Every beat names what the
visitor sees and what the mechanism does; beats are triggered by the
reading line (§6.4) unless stated.

1. **Arrival.** Plate printed complete; wheel takes phase and beats;
   barrel at 0.0 H. *Feel: a case opened on a running movement.*
2. **The casing (t=150–1,650).** Bridges drop, jewels seat, the name
   cases glyph by glyph (§6.2). *Feel: assembly, witnessed.*
3. **The count (t=1,650–4,050).** Readout flips to 28,800; the beat
   counter starts (§6.6). *Feel: the specification wakes up.*
4. **First scroll.** The train answers the hand — spin-up, blur at
   speed, tooth-by-tooth settle at rest (§6.3). *Feel: the crown in
   the fingers.*
5. **The argument's bridges.** Prose sections step in on their
   bearings; screws turn in the header as stations change (§§6.4,
   6.11). *Feel: the movement presenting its parts in order.*
6. **The apertures.** Photographs settle under their crystals;
   hairlines machine themselves (§6.12). *Feel: display backs,
   opened one by one.*
7. **The bench (ebony).** The drawings draw themselves in drive
   order (§6.7). *Feel: from the running movement to its technical
   sheet — the same wheels, twice known.*
8. **The specification.** The table's bridge pins; rows pass; the
   regulation row spends the table's one ruby (§6.13). *Feel: the
   claim, tabulated, at reading pace.*
9. **The offer.** The form's preamble makes its numbered promise
   (§6.14). The barrel stands near full wind. *Feel: the register
   opened, pen ready.*
10. **The record.** §6.17 stands printed and still — the stillness
    after all that motion is itself a beat. *Feel: the ledger,
    checked against everything above it.*
11. **The signature.** The chapter ring; the hand stepping; the
    totals for the third time; the barrel's arc closing at the same
    scroll moment (§§6.16, 6.5). *Feel: wound, signed, set down —
    still beating.*

**Reverse pass.** Scrolling up reverses only what is a function of
position: the barrel unwinds, the train reverses, parallax returns.
Latched things stay latched — casing, steps, draws, jewels: a
movement does not unassemble because its owner turns it back over.
**Jump scroll.** Anchor landings latch everything above silently
(§6.4) and set the barrel by lerp, never teleport (§6.5).

---

## 14. Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight | ≤640KB | Fonts ≤180KB (three families, subset to Latin + figures); images ≤150KB each, ≤300KB total on home |
| JS | ≤45KB gz | One loop, one observer set, the form's ≤5KB (§6.14); no framework on the movement's account |
| Per-frame cost | ≤1.6ms | Wheel 0.05 + train 0.15 + loupe 0.2 (hover only) + barrel 0.08 + draws (during 3.4s only) 0.1 + sheen 0.05 — worst-case sum ≈0.65ms, leaving headroom the gate (§10.12) verifies on device |
| Long tasks | None >50ms outside the hero ceremony | The casing's 18 glyphs are compositor transforms, not layout |
| Ambient loops | Exactly 2 | Wheel + sheen (§5) |

**Cut order** (when the budget is exceeded, cut in this order, never
skip ahead): 1. Geneva sheen (§6.10) — a finish before a mechanism.
2. Train motion blur (§6.3). 3. Loupe magnification on tablet.
4. Hairline draws on cards (§6.12) — hairlines ship drawn. 5. The
casing ceremony's bridge drops (glyphs still case). **Never cut:**
the balance wheel, the barrel, the watchdogs, the DOM-complete
fallback, the record section. A build that cuts a never-cut to save a
finish has misunderstood the theme at the level of its law.

**Low-power behaviour.** If sustained frame time exceeds 24ms, the
loop steps down in the cut order automatically and the wheel halves
its update rate per §6.1's edge case — the counter stays exact
because it counts time, not frames.

---

## 15. Build-order checklist

The sequence in which this theme is implemented. Record first — a
movement is specified before it is cased.

1. **Write the record.** §6.17's figures for the actual calibre/page;
   generate §6.3's gear paths and §6.7's drawings from it.
2. **Ship the stopped page.** Complete DOM: headline cased, sections
   in register, table and record printed, form functional. No JS.
   This is the fallback and the foundation — verify it reads whole.
3. **Tokens and type.** §2's palette (with censuses as lint rules),
   §3's scale and laws.
4. **Layout.** §4's plate: rails, bridges, bearings at their pivots;
   stripes flat under text.
5. **The wheel.** §6.1, clock-phased, with `WD-WHEEL`.
6. **The readout.** §6.6, counting the wheel; static line for
   assistive technology.
7. **The shared loop.** Lerp channels (0.12 / 0.055 / 0.2); scroll
   position and velocity published to subscribers.
8. **The train.** §6.3 on the velocity channel, with its settle.
9. **The barrel.** §6.5 on the progress channel.
10. **Section steps.** §6.4 + scrollspy (§6.11), one boundary table.
11. **The casing.** §6.2's assembly, session-flagged, `WD-CASE`.
12. **The draws.** §6.7 in the bench section, build-time path data.
13. **The loupe and the tick.** §§6.8–6.9 as the interaction layer.
14. **The form.** §6.14 with its register derivation and `WD-FORM`.
15. **Loader, transition, footer, 404.** §§6.15, 6.16, 6.18.
16. **The sheen, last** — the finish is applied to a working
    movement, never before.
17. **Run §10's gate** — signed by a non-builder. Failures return to
    the step that owns them.

---
