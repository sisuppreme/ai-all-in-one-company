# 65. Waveform Observatory — Expanded (v1 + v2)

Identity preserved exactly from the original entry: a listening station for
the world's sounds — the entire page is an oscilloscope trace the content
rides on; headlines are waveforms, sections are frequencies, silence is a
design material. Same five palette anchors — oscilloscope charcoal
`#14161A`, trace phosphor `#8FD14F`, grid slate `#2A2E35`, signal red
`#E5484D`, paper annotation `#D8DDE3`. Same three voices — Unbounded
(display, sparingly), Space Grotesk (body), JetBrains Mono (labels and
readouts). All 10 original signature elements deepened, not redesigned —
the erupting hero waveform, the morphing page trace, measurement-cursor
progress, peak-read stats, station-locking readouts, the breathing idle
trace, probe hover, waveform blip click, scope-frame images, flatline
transition — plus 8 page-family elements (masthead & navigation, channel
cards, the session log table, the request form, the flat-line loader, the
footer, the session record itself, and the no-signal 404).

**The theme's one law: *the trace never lies about level.*** Every
amplitude drawn anywhere on the page is computed from the session log's
printed dBFS figure by the one conversion in §6.17 —
`A(div) = 4 × 10^(dBFS ÷ 20)` against the graticule's 4-division
half-height. Every frequency printed is a channel's station frequency from
the same record. Silence is a measurement (−61.5 dBFS, §6.17), printed and
drawn at its true 0.003-division height — which is to say, honestly flat —
never a blank region, never a decorative wave substituted for a quiet one.

**The one record:** Session № 214, "the Night Log" — 14 November 2026,
22:00–02:00 UTC, six channels, 240 minutes — is declared in full in §6.17.
The hero waveform, the channel cards, the log table, the peak stats, the
form's receipt number and the footer's totals are all printings of that
single record, and §10's gate re-derives each one.

## 1. Concept & world

The visitor has walked into a listening station at night. The room is one
instrument: a bench oscilloscope whose screen is the size of the page,
left running by people who measure sound for a living. Everything the
site has to say is said the way the instrument says it — as a trace on a
graticule, with the readings printed beside it in a careful hand. Sections
are **channels**: you do not scroll to the next chapter, you tune to the
next station, and the trace you have been riding changes character under
you — sine, square, sawtooth, noise — until the last channel, which is
the sound of the room itself: nothing, measured precisely.

The emotional register is *attentive quiet*. This is not a loud theme
wearing a dark skin; its drama is the drama of a needle moving, of a flat
line that suddenly is not flat. Silence is budgeted like money (§4): the
page deliberately contains long near-empty stretches of graticule where
the only event is the idle trace breathing, because a listening station
that never stops talking cannot claim to listen. The one moment of
violence is the hero eruption — and it is the sound of the station's own
name, spoken once, at the start (§6.1).

**Best-fit sites and audiences.** Field-recording labels and sound-art
archives presenting releases as logged signals; audio research labs and
acoustics institutes publishing measurements; podcast and radio networks
with a measurement culture (spectrograms in their artwork, engineers in
their credits); synthesizer and test-equipment makers whose customers
already read traces for pleasure; nature-sound and bioacoustics projects
(hydrophone stations, dawn-chorus archives) where "what we heard, and how
loud, and when" is the entire content model. The audience is listeners
who trust numbers: recordists, engineers, birders with notebooks, the
kind of visitor who reads a spec table before a headline.

**When NOT to use it.** Not for high-energy commerce, launch hype, or
anything whose conversion depends on urgency — the instrument refuses
urgency on principle (§5's refused motions). Not for content that cannot
supply real measurements: the law (§6.17) requires every figure to trace
to a declared record, so a team unwilling to publish its actual numbers
will either fabricate (forbidden) or strip the readouts that make the
theme itself. Not for bright, photographic, lifestyle-led brands — the
screen is charcoal by physics, not by mood (§2). Not for checkout: the
observatory takes *requests*, not payments (§7 routes commerce out);
bolting a cart onto the graticule breaks the room's neutrality and the
theme says so rather than pretending otherwise. Not for very young
audiences — the pleasures here (a readout locking, a peak being read) are
adult pleasures of precision.

## 2. Palette

One screen, five inks. The charcoal is not "dark mode styling"; it is the
inside of an instrument, and the phosphor is not an accent colour — it is
the beam. Ratios are of visible page area in a typical full session page.

| Token | Hex | Role | Share | Contrast on `--char` |
|---|---|---|---|---|
| `--char` | `#14161A` | Screen ground; every panel, the page itself | ~78% | — |
| `--grid` | `#2A2E35` | Graticule lines, panel rules, frame edges | ~10% | 1.3:1 — decorative only |
| `--paper` | `#D8DDE3` | Annotation: body text, captions, table print | ~7% | 13.3:1 |
| `--phosphor` | `#8FD14F` | The trace; primary readouts; totals; the one interactive voice | ~4% | 9.8:1 |
| `--red` | `#E5484D` | Over-range only: a signal that broke the instrument | <0.1% | 4.6:1 |
| `--char-2` | `#1B1E24` | Lifted panel ground (cards, form, table stripes) | within char | paper 12.2:1, phosphor 9.1:1 |
| `--phosphor-dim` | `#6FA843` | Standby trace, secondary readouts, spent peaks | ~1% | 6.3:1 |
| `--paper-dim` | `#9AA3AD` | Labels, captions, log furniture | ~2% | 7.1:1 |

**Pairing rules, measured not vibes.** Paper on char (13.3:1) is the only
pairing licensed for body text. Phosphor on char (9.8:1) carries readouts,
totals and any text the instrument "says" — it is large or mono in
practice (§3) and passes AA at every size used. Paper-dim (7.1:1) is
licensed for labels and captions down to 11px. Phosphor-dim (6.3:1) is
licensed for readouts and spent-state figures, never for body copy. Grid
(1.3:1) must never carry information alone: graticule lines are a
coordinate system the *eye* uses against the trace, and any figure that
matters is printed in paper or phosphor beside them. Red (4.6:1) passes
for large text and UI marks only, and is governed by the census below, so
its contrast is nearly moot — it is almost never on the page.

**The red census.** Signal red means exactly one thing in this world: the
signal exceeded the instrument — a clip, an over-range, a broken limit.
Session № 214 clipped zero times (peak −3.2 dBFS, 3.2 dB of headroom,
§6.17), so red appears on a session page **exactly twice**: the 0 dBFS
threshold tick at the top of the hero's scale (§6.1) and its legend swatch
in the record table (§6.17). Both are the same fact — where the ceiling
is — printed in the two places a reader looks for it. A build whose
session *did* clip prints red at each clip marker in the log table and
nowhere else; red is never an error colour for forms (the form corrects
in paper and phosphor, §6.14), never a sale badge, never a hover state.
§10's gate greps the count.

**Dark-mode behaviour.** There is no light mode, and the theme declines
to apologise: a phosphor screen in a lit room is a different instrument
with different physics, and shipping a "light theme" would be a costume.
An OS-level light preference changes nothing except honouring
`prefers-contrast: more`, which raises the standby trace from
`--phosphor-dim` to full `--phosphor` and thickens graticule lines from
1px to 1.5px. Print is the theme's true second mode (§14): the print
stylesheet inverts to a paper ground with an ink trace — the log as it
would come off the bench printer — because the observatory's archive is
paper, and §6.13's table is its centrepiece.

## 3. Typography

Three voices, and each is a job. **Unbounded** is the beam's handwriting
— the display voice, rationed hard (law 1 below). **Space Grotesk** is the
annotation hand: body text, card prose, table print, everything a person
wrote next to the instrument's output. **JetBrains Mono** is the
instrument itself: readouts, frequencies, dB figures, timestamps, labels —
anything measured is mono, anything said is Grotesk, and the two never
swap jobs.

| Role | Font | Size | Weight | Line-height | Tracking |
|---|---|---|---|---|---|
| Hero headline | Unbounded | clamp(2.6rem, 6vw, 4.6rem) | 600 | 1.05 | −0.01em |
| Channel title | Space Grotesk | 1.75rem | 600 | 1.2 | 0 |
| Section head | Space Grotesk | 1.25rem | 600 | 1.3 | 0 |
| Body | Space Grotesk | 1.0rem | 400 | 1.65 | 0 |
| Readout (primary) | JetBrains Mono | 1.25rem | 500 | 1.3 | 0.04em |
| Readout (station) | JetBrains Mono | 0.8125rem | 500 | 1.3 | 0.08em, uppercase |
| Label / caption | JetBrains Mono | 0.6875rem | 400 | 1.4 | 0.08em, uppercase |
| Table figure | JetBrains Mono | 0.875rem | 400 | 1.45 | 0, tabular |

**Type laws.** (1) *Unbounded ration:* at most two Unbounded settings per
page — the hero headline (§6.1) and the masthead wordmark (§6.11). A
third setting is a build error §10 greps for; display type that appears
everywhere is a poster, not an instrument. (2) *Measured is mono:* any
string containing a unit (Hz, dBFS, ms, div, min) is JetBrains Mono with
tabular numerals, in body text too — a frequency set in Grotesk is a
category error the gate rejects. (3) *The readout floor:* no readout or
label below 0.6875rem (11px); a bench readout you must squint at has
failed as an instrument, however elegant the squint. (4) *Case is
meaning:* station readouts and labels are uppercase (the instrument's
stencil); body and card prose are sentence case (the annotator's hand);
headlines are title case in Grotesk, uppercase in Unbounded only inside
the hero envelope, where the letters are a waveform before they are
words. (5) *dB always carries its reference:* figures print as `−3.2
dBFS`, never bare `−3.2` — a level without a reference is the typographic
form of the lie the law forbids.

## 4. Layout language

The page is one screen. The **graticule** — the oscilloscope's measuring
grid, 10 divisions wide × 8 tall — is drawn under everything as dotted
`--grid` lines on a 64px division at desktop sizes (40px below 768px),
with a solid centre cross (the 0-division axes) slightly stronger. The
division is the layout's module: section padding is counted in divisions
(3 div of silence above a channel, 2 below), card gutters are 1 div, the
content column is 15 div wide at most (960px of print inside a wider
screen of trace). Whitespace here is not emptiness; it is **silence,
budgeted**: every channel is preceded by at least 24vh in which nothing
is printed but graticule and the breathing trace, because the ear — and
the eye — needs the quiet to hear the next station as an event.

**The spine.** One fixed canvas (`position: fixed; inset: 0`, behind all
content, `pointer-events: none`) draws the trace as a horizontal waveform
band centred on the **measurement line** at 42% of viewport height. The
band's amplitude envelope is ±4 divisions around that line. Content is
laid out to cross the line: each channel's headline sits in a transparent
stretch of its section so that, as the section centres, the headline
passes through the band and rides the trace (§6.2). Prose and data sit on
solid `--char`/`--char-2` panels that occlude the band — the trace is
visible in the silences, the margins and the hero, and ghosts at 12%
opacity behind panel-free stretches; it never runs *through* text. That
occlusion rule is the layout's conscience: the instrument decorates the
room, never the sentence.

**Density rules.** One channel per section, one idea per screenful. A
channel section is 100–160vh tall: silence, headline crossing, content
panel, readout furniture. No section may contain more than one table, one
card grid or one form — a second instrument readout in the same screenful
splits the measurement. The measurement cursor (§6.3) is the only
full-height vertical element; the masthead (§6.11) is the only fixed
horizontal one; nothing else is pinned, sticky or floating — a bench has
one screen, one cursor, one lamp.

**The trace's parallax depths** (subtle, signal-true): graticule scrolls
at 0.96× (it is printed on the glass, nearest the eye), annotations and
readouts at 1.0× (they are the page), the trace band at 1.0× in position
but its *phase* advances with scroll (§6.2) — parallax here is phase, not
drift, because a waveform that slid sideways would be a different signal.


## 5. Full motion system

One loop runs everything. A single `requestAnimationFrame` loop owns the
canvas trace, the measurement cursor, every scrubbed value and every
counter; nothing in the theme animates on its own timer. The loop keeps
two smoothed values: `scrollLerp` (factor 0.09 — the *tape-spooling*
feel, a faint mechanical settle as motion eases into its target, never a
bounce) for scroll-driven quantities, and `probeLerp` (factor 0.12) for
pointer-driven ones. Scroll position is read, never animated; the loop
lerps toward it. When the tab is hidden the loop sleeps; when the frame
budget is exceeded the loop sheds load in §14's order.

**Named easings** (the station's own, used by name everywhere below):
`--ease-strike: cubic-bezier(0.16, 1.3, 0.3, 1)` — the struck note: fast
attack, one overshoot, long settle; `--ease-lock: cubic-bezier(0.22,
1.25, 0.36, 1)` — a dial settling onto its station, smaller overshoot;
`--ease-sweep: linear` — the measurement cursor travels at constant
velocity because a sweep that eased would be lying about time;
`--ease-settle: cubic-bezier(0.22, 1, 0.36, 1)` — ordinary arrivals;
`--ease-print: cubic-bezier(0.4, 0, 0.2, 1)` — annotations fading in, the
pen touching paper.

**The motion-term translation table** — every standard term, in this
theme's language or refused with its reason:
- *Scroll-triggered reveals* → sections print as they cross the
  measurement line (§6.2): opacity is never the reveal — the section's
  readout locks (§6.5) and its panel rises 12px under `--ease-settle`
  while the trace behind it takes the section's character.
- *Scroll-driven / scrubbed animation* → the trace's waveform morph
  (sine → square → sawtooth → noise → flat) and phase are pure functions
  of lerped scroll progress (§6.2); the cursor's travel is scrubbed the
  same way (§6.3).
- *Parallax* → phase and the three signal depths of §4 (0.96 / 1.0 /
  phase-advance). Nothing slides decoratively.
- *Pinned sections* → the trace band is pinned for the whole page; the
  hero envelope pins for its first 120vh while the eruption settles.
  No content section pins — pinning print would trap the reader inside
  someone else's measurement.
- *Masked reveals* → the hero headline is clipped inside the waveform's
  amplitude envelope (§6.1): the mask *is* the signal. No other masking;
  a mask that hides print is a fault in this theme, not a flourish.
- *Blur-to-sharp* → beam focus: the hero headline enters 2px defocused
  and sharpens as the struck note settles (§6.1) — a beam finding its
  focus, used exactly once per page.
- *Kinetic typography* → refused, except the envelope swell of §6.1.
  Letters that dance are a broadcast studio; this is a bench.
- *Marquee* → refused. A scope has no ticker. The channel index (§6.11)
  is a static dial; urgency is not a frequency this station transmits.
- *Counters* → two species only: peak-read stats (§6.4), counted as the
  cursor passes their peaks, and station-lock sweeps (§6.5). No counter
  runs on a timer or on mere visibility.
- *Progress indicator* → the measurement cursor itself (§6.3): progress
  is a measurement being taken of the page, with readouts. No bar.
- *SVG line-draw* → the scope-frame flicker (§6.9) and the 404's single
  attempted sweep (§6.18) draw as line work; nothing else draws itself.
- *Image scale-in-frame* → §6.9: 1.05 → 1.0 inside the frame as it
  crosses the line, with one trace flicker across the glass.
- *Hover / magnetic / tilt micro-interactions* → probe hover (§6.7) is
  the hover system; magnetic pull is refused (a probe does not drag the
  bench toward the hand); card tilt survives at max 3° (§6.12), scoped
  like a screen catching bench light.
- *Custom cursor* → refused, standing rule: the system pointer is the
  probe's handle; §6.7's amplification is drawn on the trace, never on
  the pointer.
- *Skeleton loading* → the flat-line loader (§6.15): a line that gains
  signal as data arrives. No grey boxes; an unloaded channel is a silent
  one, drawn flat.
- *Page transitions* → the flatline (§6.10): 200ms of silence, a sweep,
  the new signal erupts.
- *Ambient loops* → exactly two licensed: the idle breath with its
  transient spikes (§6.6), and CRT grain/vignette shimmer at ≤3% opacity
  on an 8s cycle. A third ambient loop is a §10 failure.
- *Reduced motion* → §6 elements each carry their variant; globally, the
  trace prints once, static, per section character, and every readout
  ships at its locked value (§6.5).

## 6. Signature elements

### 6.1 The erupting hero waveform

- **What & why.** On load, the screen holds a flat line in silence for
  ~600ms. Then the waveform erupts — one struck note with amplitude
  overshoot, settling over ~900ms — and the headline's letters, clipped
  inside the waveform's amplitude envelope, swell with it. The waveform
  is not an artist's squiggle: it is the amplitude envelope of the actual
  FFT of the station's spoken name, "Waveform Observatory," recorded at
  44.1 kHz/24-bit, 1.84s long (§6.17), and a caption under the trace says
  so. It belongs because the hero is the station introducing itself the
  only way it honestly can: by sounding its name and showing the
  measurement. The title is heard with the eyes.
- **Structure.** The hero is a transparent 100vh section over the fixed
  canvas (§4): the trace band crosses it at the measurement line. The
  headline is an SVG `<text>` (Unbounded) whose clip path is the name
  envelope sampled to 128 points from the record's FFT data, inlined as a
  path in the document — the envelope is data, shipped with the page, not
  generated decoration. Beside the band: the hero scale, a vertical
  dBFS ruler (−60 / −40 / −20 / −12 / −6 / −3 / 0) in mono, with the
  single red 0 dBFS threshold tick (§2's census) at its top. Under the
  trace, the annotation caption in paper: *"The name, spoken once.
  Envelope from its FFT — Session № 214, CH 01."* The DOM ships with the
  headline fully printed and the envelope at its settled amplitude; the
  script rewinds both only in the frame it arms the eruption.
- **Motion spec.** Trigger: load, after fonts or the 900ms font race
  (§6.17's watchdog discipline). t=0–600ms: flat line at the noise
  floor's true height (0.003 div — visually flat, honestly not zero),
  headline at rest size, 2px defocused. t=600ms: attack under
  `--ease-strike` — amplitude overshoots to 118% of the logged envelope
  by t≈780ms, rings down through 96% at t≈1050ms, settles at 100% by
  t≈1500ms; the headline's clip swells with the same curve and the
  defocus resolves across t=600–1200ms. The caption prints last,
  `--ease-print`, t=1300–1700ms. After settling, the hero stretch of the
  trace joins the page morph (§6.2) as CH 01's composite character.
- **States.** Silent (pre-eruption, ≤600ms) / erupting / settled (the
  resting state for the rest of the visit) / returning (a repeat visit
  within the session skips the silence and the overshoot — the station
  does not re-introduce itself; §6.17's returning-visitor rule).
- **Content merge.** Remove the name and there is no waveform: the
  envelope's every bump is the two words' syllables. The peak of the
  envelope is the session peak, −3.2 dBFS, and the scale beside it is the
  same scale the log table uses (§6.13) — the hero is the record's first
  printing, not an illustration of it.
- **Failure fallback.** Watchdog at 2000ms from arm: if the eruption has
  not settled, amplitude snaps to 100%, defocus clears, caption prints.
  No-JS: the shipped state *is* the settled state — full headline, full
  envelope, caption present. Canvas failure: the SVG envelope path still
  renders as a static phosphor line under the headline (§6.2's fallback
  rendering), so the hero keeps its meaning with no canvas at all.
- **Reduced-motion variant.** No silence, no eruption: the envelope
  prints at settled amplitude, headline sharp, caption present. The
  name is still shown as its measured shape — the information survives;
  only the striking is removed.
- **Performance budget & mobile variant.** The hero adds zero per-frame
  cost beyond the shared loop's trace pass (≤0.9ms/frame total canvas
  budget, §14). The envelope path is ≤6KB inlined. Mobile (<768px): the
  eruption is unchanged in timing (it is the theme's handshake) but the
  scale ruler collapses to three ticks (−60 / −3 / 0) and the headline
  sets on two lines inside a taller envelope (±4 div over 2 lines of
  Unbounded at clamp floor 2.6rem).
- **Choreography timeline (v2).** t=0 load, flat line, defocused
  headline → t=600 attack begins → t≈780 overshoot peak 118% →
  t≈1050 ring-down 96% → t=1200 focus resolved → t=1300–1700 caption
  prints → t=1500 settled → watchdog deadline t=2000 passes unused →
  scroll hands the stretch to §6.2's morph.
- **State matrix (v2).** *Rest (settled):* envelope at 100%, headline
  sharp. *Hover:* none — the hero is the station's, not the pointer's;
  hovering the caption does nothing. *Focus:* the hero contains no
  focusable element before its scroll cue, which behaves per §11.
  *Active:* n/a. *Scrolled-past:* the stretch becomes CH 01 of the morph;
  scrolling back re-enters it settled — the eruption never replays
  within a visit. *Disabled:* n/a. *Touch:* identical; the silence is
  not skippable by tap (600ms is the theme's held breath, and §12's
  voice explains it in the caption's second line on touch devices only:
  *"Hold — the station listens first."*).
- **Breakpoints (v2).** ≥1200px: full scale ruler, one-line headline.
  768–1199px: ruler drops the −40/−12 ticks. <768px: three-tick ruler,
  two-line headline, envelope ±4 div maintained by raising band height
  to 34vh.
- **Edge cases & failure modes (v2).** *Slow font load:* the eruption
  waits for Unbounded or the 900ms race, whichever first; a late font
  swap after settling never re-triggers the eruption. *Very tall
  viewport (>1100px):* the band stays at 42% and the hero grows more
  silence below the caption — acceptable, silence is the material.
  *Name changed in a CMS:* the envelope path is record data (§6.17);
  changing the wordmark without re-recording invalidates the build at
  §10's gate — the caption would be lying.
- **Accessibility spec (v2).** The headline is real text (SVG `<text>`
  with a `<title>`, and an HTML `<h1>` visually hidden twin is *not*
  used — the SVG text itself is the h1's content via `role="img"` on
  the figure plus the caption as its description; the spoken name is
  also the page's `<h1>` in the masthead's accessible name). The
  eruption is never announced; the settled state is the content. The
  defocus phase never applies to any text a visitor must read to
  proceed — the hero has no links until settled.
- **Tokens consumed (v2).** `--char`, `--phosphor`, `--paper`,
  `--paper-dim`, `--red` (the threshold tick — census 1 of 2),
  `--ease-strike`, `--ease-print`, `--dur-silence` (600ms),
  `--dur-erupt` (900ms), `--loop-lerp-scroll` (0.09).

### 6.2 The morphing page trace

- **What & why.** One continuous trace runs the whole page: as the
  visitor scrolls, the waveform they are riding morphs through the
  channels' characters in the record's order — CH 01 composite → CH 02
  sine → CH 03 square → CH 04 sawtooth → CH 05 noise → CH 06 flat. It
  belongs because the spine of the page is the signal the sections are
  about: scroll position is literally which waveform you are inside, and
  the morph is how the station changes the subject.
- **Structure.** The fixed canvas of §4 draws one waveform across the
  full width at the measurement line, sampled at 2px steps. Each channel
  owns a *character function* (sine, square with 40ms-equivalent edge
  softening, sawtooth, band-limited noise from a seeded generator, the
  composite hero envelope, and flat-at-floor). A morph parameter `m`
  (0–5, continuous) is a pure function of lerped scroll progress mapped
  through the sections' offsets; the drawn sample is the crossfade of
  the two adjacent characters weighted by `frac(m)`, with amplitude
  always scaled by the *current* channel's logged peak via §6.17's
  conversion — a morph may change the shape mid-screen, never the level
  law. Phase advances with scroll at 0.5 cycles per viewport height so
  the wave appears to be spooled past the screen, tape over a head.
- **Motion spec.** Continuous, loop-driven; no triggers of its own.
  Character crossfades occupy the middle 30% of each inter-section
  stretch; within a channel's own stretch the character is pure.
  Amplitude transitions between channels' logged peaks are smoothed by
  the same `scrollLerp` (0.09) — a level change takes ~400ms of scroll
  to fully arrive, like a fader, not a switch. The trace redraws every
  frame the loop runs; when scroll is idle for >2s the trace hands its
  character to §6.6's breathing (same canvas, same pass).
- **States.** Per-channel pure / crossfading / breathing (idle, §6.6) /
  printed (fallbacks). Scrolled-past channels are simply behind the
  morph parameter; scrolling up reverses the morph symmetrically —
  the function is stateless in scroll position, so there is nothing to
  latch or replay.
- **Content merge.** The morph order is the record's channel order and
  the page's section order — three printings of one sequence (§6.11's
  dial, §6.13's table, this trace). A section inserted or removed in a
  CMS changes the record first (§6.17) and the morph follows; the trace
  can never show a waveform the page doesn't contain.
- **Failure fallback.** Canvas absent or failing: each section ships a
  static inline SVG trace in its own character at its logged amplitude,
  printed in its silence stretch — the page reads identically, section
  by section, with no morph. The loop probes the canvas on arm; a
  failed probe swaps the fixed canvas out and the SVGs (present in the
  DOM, hidden only while the canvas lives) take over. No-JS: SVG state.
- **Reduced-motion variant.** No morph, no phase advance: the fixed
  canvas is replaced by the per-section static SVGs, each in character,
  each at level. The visitor still reads shape-per-section — the
  information content of the morph — with none of the spooling.
- **Performance budget & mobile variant.** One canvas pass, ≤0.9ms/frame
  at desktop width (§14); sample step rises to 3px below 768px and the
  noise character switches to a 256-sample pre-rendered loop (seeded
  identically, §6.17) — the noise must be the *same* noise, only cheaper.
  The canvas is capped at devicePixelRatio 1.5.
- **Choreography timeline (v2).** Scroll → `scrollLerp` eases progress →
  `m` crosses a boundary's 35% point → crossfade begins → 65% point →
  new character pure, its station readout begins its lock (§6.5) → the
  section's headline crosses the measurement line inside the new
  character's envelope.
- **State matrix (v2).** *Rest:* current channel pure, breathing if idle
  (§6.6). *Hover:* §6.7's probe modifies amplitude locally; the morph is
  untouched. *Focus:* keyboard scrolling morphs identically — the
  function reads scroll position, not input device. *Active:* n/a.
  *Scrolled-past:* symmetric on return. *Disabled:* n/a. *Touch:*
  identical; momentum scrolling is absorbed by the lerp, which is what
  the 0.09 factor is for.
- **Breakpoints (v2).** ≥1200px: band ±4 div, 2px sampling.
  768–1199px: band ±3.2 div. <768px: band ±2.6 div, 3px sampling,
  pre-rendered noise; the measurement line rises to 38% so the band
  clears the collapsed masthead.
- **Edge cases & failure modes (v2).** *Content shorter than designed*
  (a channel section removed): the morph map is built from the DOM's
  actual sections at load — `m` spans the channels that exist, in
  record order. *Jump scroll (anchor link to CH 05):* `m` lerps across
  the intervening characters in ~600ms — a fast spool through stations,
  legible, never a teleport cut. *Resize mid-scroll:* offsets are
  re-measured on a debounced resize; the trace never draws from stale
  geometry for more than one frame. *Low-power device:* §14's cut order
  halves the frame rate of the trace pass before touching anything
  printed.
- **Accessibility spec (v2).** The canvas is `aria-hidden`; every fact it
  carries (channel, character, level) is printed in the section's
  readout (§6.5) and the log table (§6.13). No information exists only
  in the morph. The static-SVG fallback traces carry `role="img"` and
  labels naming channel and character ("CH 03 — square wave, peak −6.8
  dBFS").
- **Tokens consumed (v2).** `--char`, `--phosphor`, `--phosphor-dim`,
  `--grid`, `--loop-lerp-scroll` (0.09), `--band-half` (4 div),
  `--measure-line` (42%).


### 6.3 Measurement-cursor progress

- **What & why.** A thin vertical cursor line travels the trace as the
  visitor scrolls — left to right across the current channel's stretch,
  then resetting for the next — and where it crosses a peak, a mono
  readout prints that peak's values. It belongs because progress on this
  page is not a bar filling; it is a measurement being taken of the
  signal, and reading the page *is* scoping it. The cursor is the
  visitor's instrument, lent by the station.
- **Structure.** One absolutely-positioned 1px `--phosphor` rule inside
  each channel section's trace stretch (DOM element, not canvas, so it
  survives canvas failure), height = the band (±4 div), with a small
  triangular index at its foot and a readout chip (`--char-2` ground,
  mono) that prints beside the peak it is crossing. Peak positions are
  data: each channel declares its peaks in the record (§6.17) as
  fractions of its stretch, with the values to print. The cursor's `x`
  is driven by the shared loop from the section's lerped scroll
  progress — a pure function, reversible, no state.
- **Motion spec.** Travel is `--ease-sweep` — constant velocity across
  the stretch, because the cursor is a timebase: it crosses the
  section's printed duration (its minutes from the record, §6.17)
  mapped linearly to the stretch's scroll length, and its chip prints
  the elapsed time per division as it goes (e.g. CH 02: 5 ms/div across
  10 div = a 50ms window, §6.17). At a peak (±1.5% of stretch around the
  peak's fraction) the cursor dwells: its colour lifts from
  `--phosphor-dim` to `--phosphor`, the chip prints the peak's values
  over 180ms `--ease-print`, and §6.4's stat — if the peak carries one —
  begins its count. Leaving the peak, the chip holds 600ms, then clears.
- **States.** Travelling / dwelling at a peak / at rest at a stretch's
  end (the cursor parks at the right edge, dimmed, until the next
  channel's stretch begins) / printed (fallbacks: the cursor rests at
  the *last* peak and all chips print statically beneath the stretch).
- **Content merge.** The peaks are the channel's actual loudest moments
  from the log, at their actual positions in the channel's duration —
  CH 03's 96 transients are summarised by its three printed peaks
  (§6.17), and the cursor reads them in the order they happened. The
  progress of reading and the chronology of the recording are the same
  line.
- **Failure fallback.** The cursor is loop-driven decoration on printed
  data: if the loop dies, a watchdog at 1500ms parks the cursor at the
  final peak and prints every chip statically. No-JS: all chips printed
  under their peaks from the start; the cursor is absent and nothing
  references it.
- **Reduced-motion variant.** No travel: the cursor prints at each peak
  in turn as the section scrolls into view (position jumps are state
  changes, not motion), chips pre-printed. The measurement reads as a
  series of stills — a strip of scope photographs.
- **Performance budget & mobile variant.** One transform update per
  frame for the visible section's cursor only; negligible. Mobile:
  the chip prints *below* the band rather than beside the peak (no
  room at the margins), and the dwell window widens to ±2.5% so touch
  scrolling still triggers readings.
- **Choreography timeline (v2).** Section stretch enters → cursor fades
  in at left edge (200ms) → travels at sweep velocity → peak fraction
  −1.5%: brighten → at peak: chip prints (180ms), stat counts (§6.4) →
  +1.5%: chip holds → 600ms later clears → stretch end: cursor parks,
  dims → next channel: reset to left edge.
- **State matrix (v2).** *Rest:* parked at a stretch end, dim.
  *Hover:* hovering the band pauses nothing — the cursor answers to
  scroll, not the pointer; hovering a chip keeps it printed while
  hovered. *Focus:* chips are not focusable; their values are in the
  section's printed readout (§6.5). *Active:* n/a. *Scrolled-past:*
  position is a pure function of scroll — returning re-travels it
  symmetrically. *Disabled:* n/a. *Touch:* identical travel; dwell
  window widened (above).
- **Breakpoints (v2).** ≥1200px: chip beside peak, max-width 220px.
  768–1199px: chip beside peak, 180px. <768px: chip below band, full
  column width, cursor height ±2.6 div matching §6.2's band.
- **Edge cases & failure modes (v2).** *Two peaks close together*
  (CH 03's peaks at 0.41 and 0.47): chips queue — the second waits for
  the first's 600ms hold, printing in chronological order even if the
  cursor has passed; a reading is never skipped, only delayed.
  *Scrolling backwards across a peak:* the chip reprints (the
  measurement is re-taken) but §6.4's stat does not recount — it holds
  its read value (§6.4's latch). *Section stretch shorter than the
  dwell geometry* (very short channel): peaks print in the section's
  readout instead, cursor travels bare — §10 checks the geometry at
  build.
- **Accessibility spec (v2).** Cursor and chips are `aria-hidden`
  instruments; every value they print exists in the section's text or
  §6.13's table. The chip's contrast is phosphor on `--char-2` (9.1:1)
  for values, paper-dim on `--char-2` (≈6.4:1) for its label — both
  pass for their sizes. No focus interaction is modelled on the cursor.
- **Tokens consumed (v2).** `--phosphor`, `--phosphor-dim`, `--char-2`,
  `--paper-dim`, `--ease-sweep`, `--ease-print`, `--dur-chip` (180ms),
  `--loop-lerp-scroll` (0.09).

### 6.4 Peak-read stats

- **What & why.** The session's four headline numbers — **240 minutes on
  air, 218 transients logged, session peak −3.2 dBFS, dynamic range
  58.3 dB** — sit at four peaks of the trace, and each counts up as the
  measurement cursor (§6.3) passes its peak. It belongs because on this
  page a statistic is not a tile in a grid; it is a reading, taken off
  the waveform at the moment the waveform earns it.
- **Structure.** Four stat blocks in the session section (the page's
  second stretch, after the hero), each anchored to a declared peak of
  CH 02's sine at fractions 0.18 / 0.41 / 0.66 / 0.89 of the stretch
  (§6.17). Each block: a mono label in `--paper-dim` (`MINUTES ON AIR`),
  the value in primary readout size (`--phosphor`, JetBrains Mono
  1.25rem, tabular), and a hairline marker from the value to its peak on
  the band. The values are printed in the DOM at their final readings
  from the first byte; the count is a JS-armed performance over printed
  truth, per the standing rule.
- **Motion spec.** Trigger: the cursor's dwell at the stat's peak
  (§6.3). Count duration 400ms exactly, linear steps in the unit's own
  grain — minutes and transients count in whole numbers, dB figures in
  0.1 steps — under the loop, ending dead on the record's value. The
  marker hairline draws (scaleY 0→1, 240ms `--ease-settle`) as the
  count begins, pinning the reading to its peak. A stat counts **once
  per visit** (latched); the cursor may re-dwell, the reading stands.
- **States.** Printed-unread (value at final reading, marker undrawn,
  label dim) / counting / read (marker drawn, label at full paper) /
  latched (all later passes). The unread state is a *print* state, not
  a hidden one — a visitor who never triggers the count still reads
  every number.
- **Content merge.** Each stat is the record's total, and the peak it
  sits on is a real peak of the channel playing beneath it: the dynamic
  range stat (58.3 dB) sits on the stretch's tallest peak because it is
  the difference between that peak (−3.2 dBFS is CH 01's; the stretch
  annotates the derivation in its caption: *peak −3.2 minus floor
  −61.5*) — the arithmetic is printed where the number is claimed
  (§6.17's reconciliation, §10's audit).
- **Failure fallback.** No count without the loop: watchdog per stat at
  its peak's expected crossing +1500ms draws the marker and leaves the
  printed value — the fallback state is indistinguishable from the read
  state except the count never ran. No-JS: markers drawn, values
  printed; the page loses nothing but 400ms of theatre.
- **Reduced-motion variant.** No counting: the marker draws instantly
  (a state change) when the peak enters the viewport centre band, value
  always at final reading. The pinning — the information — survives.
- **Performance budget & mobile variant.** Four counters on the shared
  loop; ≤0.05ms/frame while any count runs. Mobile: stats stack in a
  2×2 grid below the band, markers become short ticks, counts unchanged
  (400ms is cheap at any size).
- **Choreography timeline (v2).** Cursor reaches peak −1.5% → marker
  begins drawing → at peak: count starts (400ms, unit grain) → count
  lands on the record's value → label lifts dim→full (200ms) → latch
  set → cursor departs; marker and value persist for the visit.
- **State matrix (v2).** *Rest:* read or printed-unread, value always
  legible. *Hover:* the stat block brightens its marker to full
  phosphor — a finger on the reading. *Focus:* stats are not focusable;
  the same figures are focusable content in §6.13's table.
  *Active:* n/a. *Scrolled-past:* latch persists; scrolling back shows
  read stats, no recount. *Disabled:* n/a. *Touch:* no hover
  brightening; counts trigger identically via the cursor.
- **Breakpoints (v2).** ≥1200px: four stats in a row along the stretch,
  each under its peak. 768–1199px: 2×2 grid, markers diagonal.
  <768px: 2×2 grid below the band, tick markers.
- **Edge cases & failure modes (v2).** *Visitor scrolls fast past all
  four peaks:* the loop's dwell test uses the lerped cursor position,
  so a fast pass still crosses each ±1.5% window across successive
  frames; if a window is jumped entirely between frames, the stat's
  watchdog (§ above) reads it anyway — a reading is never skipped.
  *Record corrected* (a recount changes 218): the stat, the table and
  the footer print from the one record (§6.17); §10 re-derives all
  three printings before the build ships.
- **Accessibility spec (v2).** Values are text, always final, never
  announced mid-count; the count is `aria-hidden` performance over a
  visually identical static value exposed to AT (the DOM value is
  replaced only in a presentation clone — AT reads the printed figure
  once). Contrast: phosphor on char 9.8:1 at 1.25rem; labels paper-dim
  7.1:1 at 11px uppercase — passes AA for its size class.
- **Tokens consumed (v2).** `--phosphor`, `--paper`, `--paper-dim`,
  `--char`, `--ease-settle`, `--dur-count` (400ms), `--dur-marker`
  (240ms).

### 6.5 Station-locking readouts

- **What & why.** Every channel section carries a readout — `CH 03 ·
  SQUARE · 440.00 Hz` — whose frequency figure sweeps rapidly upward
  with phosphor flicker as the section enters, and locks onto the
  channel's station frequency with a small overshoot settle. It belongs
  because arriving at a chapter here is tuning to its frequency: the
  section announces itself as a station on the dial before it says
  anything else, and the lock is the visitor's confirmation that the
  tuning took.
- **Structure.** A readout strip pinned to the top of each channel
  section's content panel: channel number and waveform character in
  station style (§3), the frequency as a single mono figure with its
  unit, and at the strip's right edge the channel's logged peak
  (`PEAK −6.8 dBFS`) and timebase (`0.5 MS/DIV`). All values are the
  record's (§6.17), printed in full in the DOM; the sweep is a
  presentation clone over the printed figure, as in §6.4. CH 06's
  readout locks onto `0.00 Hz` and adds the station's driest line:
  `NOTHING, MEASURED.` — printed, in the annotator's hand (Grotesk,
  sentence case), beneath the strip.
- **Motion spec.** Trigger: the section's panel crossing the
  measurement line. Sweep: 700ms, the figure counting upward from 0 in
  the channel's own grain (Hz to two decimals below 1 kHz; CH 05 sweeps
  in Hz and reprints as `7.300 kHz` at lock), with phosphor flicker —
  opacity jitter between 0.55 and 1.0 at 90ms steps, seeded per channel
  so the flicker is the same on every visit (a faulty tube flickers
  with a pattern, not with dice). Lock: the figure overshoots by +0.4%
  and settles under `--ease-lock` over 240ms; at the settle's end the
  peak and timebase print (`--ease-print`, 200ms). A readout locks once
  per visit; re-entry shows the locked state.
- **States.** Printed-unlocked (full values, no flicker — the honest
  rest state) / sweeping / locked (values full, a 2px phosphor index
  tick appears at the strip's left edge and stays) / the CH 06 special
  case: its sweep is a *fall* — the figure counts down from the
  previous channel's frequency to 0.00 over 900ms, the dial running
  down into silence.
- **Content merge.** The readout is the section's identity card and its
  data in one: frequency, character, peak and timebase are exactly the
  row §6.13's table prints for the channel and the card §6.12 prints on
  the index — three printings, one record, §10 audits the agreement.
- **Failure fallback.** Watchdog at 1200ms after the trigger: if the
  sweep has not locked, the printed figure stands and the tick appears
  — locked by fiat, never left flickering. No-JS: locked state shipped.
  A flicker that never ends is this theme's version of a spinner, and
  it is banned by name in §9.
- **Reduced-motion variant.** No sweep, no flicker: the tick appears
  and the peak/timebase print as the section enters. The lock — the
  information — is the state change; the tuning was the theatre.
- **Performance budget & mobile variant.** One figure update per frame
  per sweeping readout (at most one section sweeps at a time — sections
  are a screenful apart); negligible. Mobile: the strip wraps to two
  lines (identity, then peak/timebase), sweep unchanged.
- **Choreography timeline (v2).** Panel crosses line → t=0 sweep
  begins, flicker on → t=700 figure reaches station value → t=700–940
  overshoot settle (`--ease-lock`) → t=940 tick prints, peak/timebase
  fade in (200ms) → locked; watchdog deadline t=1200 passes unused.
- **State matrix (v2).** *Rest:* locked (after first pass) or
  printed-unlocked. *Hover:* hovering the strip lifts the tick's
  brightness — nothing else; a readout is not a control. *Focus:* the
  strip is not focusable; its channel link lives in §6.11's dial.
  *Active:* n/a. *Scrolled-past:* locked state persists on return.
  *Disabled:* n/a. *Touch:* identical; no hover lift.
- **Breakpoints (v2).** ≥1200px: single-line strip. 768–1199px:
  single line, peak/timebase drop the `PEAK`/`TIMEBASE` labels to
  bare values with units. <768px: two-line strip as above.
- **Edge cases & failure modes (v2).** *Two sections entering in one
  fast scroll:* sweeps queue on the loop — the later section's sweep
  starts only when the earlier locks or watchdogs out; two flickering
  readouts at once would read as a fault, not a feature. *Frequency
  changed in the record:* sweep target, table row and card all derive
  from §6.17 — one edit, three printings, §10 re-checks.
- **Accessibility spec (v2).** The sweep is presentation-only; AT reads
  the printed locked figure once. The tick is decorative. Readout
  contrast: phosphor on `--char-2` 9.1:1 (figure), paper-dim on
  `--char-2` ≈6.4:1 (labels at 11px uppercase — AA for its class).
  The CH 06 line is ordinary text, not a live region.
- **Tokens consumed (v2).** `--phosphor`, `--phosphor-dim`, `--paper`,
  `--paper-dim`, `--char-2`, `--ease-lock`, `--ease-print`,
  `--dur-sweep` (700ms), `--dur-lock` (240ms).

### 6.6 Breathing idle trace & transient spikes

- **What & why.** Between interactions the trace does not freeze: it
  breathes at low amplitude (±3%) and, every 7–15 seconds, fires one
  real transient spike that rings and decays. It belongs because the
  station is always listening — the page's silence is *live* silence,
  with the world's noise still in it. A frozen idle trace would be a
  screenshot of a station, not a station.
- **Structure.** A mode of the shared canvas pass (§6.2), not a second
  system: when scroll and pointer have both been idle for 2s, the loop
  blends the current channel's amplitude toward its breathing envelope
  (a 0.11 Hz sine on amplitude, ±3% — roughly one breath per 9 seconds,
  an resting engineer's rate). Spikes are drawn from the current
  channel's *logged transient profile* (§6.17): CH 03's spikes are
  square-edged and frequent in character, CH 02's are smooth humps —
  the spike's shape is the channel's waveform character, its height a
  seeded draw from the channel's logged transient amplitudes, capped at
  the channel's logged peak (a spike may never exceed the record).
- **Motion spec.** Breath: continuous while idle, blended in over 800ms
  so the transition from scrolled morph to breathing is inaudible.
  Spike: attack 30ms (a transient is fast or it is not a transient),
  ring-down exponential over 1200ms (loop-computed `e^(−t/400ms)`),
  overshoot below baseline −8% at ~500ms — a real spike's undershoot.
  Cadence: seeded interval in [7s, 15s], one spike live at a time; any
  scroll or pointer movement ends idle mode within one frame and the
  spike, if mid-ring, is cut — the visitor's action always outranks the
  room's ambience.
- **States.** Attentive (visitor active; no breath, no spikes) /
  breathing / spiking (a breath with a spike ringing through it) /
  suspended (tab hidden, loop asleep; on return, idle timers restart —
  no spike is owed).
- **Content merge.** The spikes are re-enactments of the record's
  transients, compressed: the record's true rate (218 across 240
  minutes, §6.17) is printed in the section's caption beside the trace —
  *"218 transients tonight — one every 66 seconds. Here, they are
  replayed closer together, so you can hear the room think."* The
  compression is disclosed on the page, in the annotator's hand; an
  undisclosed compression would be the law broken politely.
- **Failure fallback.** Idle mode is pure ambience: if the loop is
  running the morph, it is running this. Canvas fallback (§6.2) has no
  idle mode — the static SVGs are still, and the caption's disclosure
  line is omitted from the fallback rendering since there is nothing
  being replayed.
- **Reduced-motion variant.** No breath, no spikes. The idle trace is
  the printed static character (§6.2's variant). The room is still
  honest — a still photograph of silence is still silence.
- **Performance budget & mobile variant.** Zero additional cost: the
  breath is an amplitude multiplier in the existing pass; spikes are
  sample offsets in the same pass. Mobile: breath depth halves (±1.5%)
  and the spike interval widens to [12s, 20s] — a small screen's room
  is quieter, and battery is a bench resource too.
- **Choreography timeline (v2).** Last interaction → t=2000 idle
  declared → t=2000–2800 breath blends in → seeded interval elapses →
  spike attack 30ms → ring-down 1200ms with undershoot at ~500ms →
  breath continues → any input: idle exits within one frame.
- **State matrix (v2).** *Rest:* breathing. *Hover:* §6.7's probe takes
  precedence — hover is an interaction, idle exits. *Focus:* keyboard
  focus changes count as interaction; idle exits. *Active:* clicks
  fire §6.8's blip instead. *Scrolled-past:* the breath applies to
  whichever channel is current; there is no per-section idle state.
  *Disabled:* n/a. *Touch:* touch scroll is interaction; a resting
  finger on glass is not (no hover channel) — idle may begin under a
  still finger, which is correct: the room breathes around a quiet
  hand.
- **Breakpoints (v2).** ≥1200px: full breath ±3%, spikes [7s, 15s].
  768–1199px: ±2.5%, [9s, 16s]. <768px: ±1.5%, [12s, 20s].
- **Edge cases & failure modes (v2).** *Visitor reading a long panel
  without touching anything:* idle begins, the trace breathes behind
  the panel's transparent margins — intended; the panel's text ground
  is solid (§4), so the breath never touches legibility. *Spike during
  a §6.4 count:* the count's peak is data, the spike is ambience on a
  different stretch of band (spikes fire only in the current
  viewport's *unoccupied* band segments, never within a stat's marker
  zone). *Seeded cadence across visits:* the seed is the session
  number (214) — the room behaves identically for every visitor, so a
  spike a visitor reports is reproducible by the builder.
- **Accessibility spec (v2).** Purely decorative (`aria-hidden` canvas);
  nothing is announced, nothing flashes above 3 per second (the spike
  is a single event with a 1200ms decay — far below photosensitivity
  thresholds, and its peak luminance change is confined to a 2px line).
  Reduced-motion removes it entirely (above).
- **Tokens consumed (v2).** `--phosphor`, `--phosphor-dim`,
  `--ease-settle`, `--dur-idle` (2000ms), `--breath-depth` (±3%),
  `--spike-cadence` (7–15s).


### 6.7 Probe hover

- **What & why.** Hovering an element locally amplifies the trace
  around it — ±40% amplitude within ~160px of the element, lerped — as
  a probe touching a signal brightens the trace on a real bench. It
  belongs because attention here is *contact*: the signal responds
  where you touch the page, on the element you are examining, and the
  response is drawn in the page's physics, not in a tooltip.
- **Structure.** The loop maintains a probe field: the hovered (or
  focused) element's horizontal centre and the band segment nearest it.
  The canvas pass multiplies sample amplitudes by
  `1 + 0.4 × falloff(distance)` where falloff is a raised-cosine over
  160px either side of the centre. Elements opt in by being
  *measurable* — cards, stat blocks, table rows, form fields, links —
  a `data-probe` attribute set at build; prose paragraphs do not probe
  (you do not touch a signal with a whole paragraph). The amplification
  is drawn on the trace in the margins and silences around the element
  (§4's occlusion rule keeps it out of the text itself).
- **Motion spec.** Attack: `probeLerp` 0.12 per frame toward the target
  field — full amplification in ~250ms, soft as a hand settling.
  Release: on leave, the field decays over 500ms (`e^(−t/160ms)` in the
  loop) — a probe lifted off a signal leaves a small ring of settling.
  Moving between adjacent elements retargets the field without a reset:
  the brightening slides along the band like a probe dragged across
  contacts.
- **States.** Untouched / probing (hover or focus) / releasing /
  probing-elsewhere (retarget mid-release). Focus probing is identical
  to hover probing — a keyboard visitor's attention is also contact,
  and the trace answers it the same way. Disabled elements do not
  probe: the trace stays flat past them, and that flatness, backed by
  the element's printed dimming, is itself the disabled signal.
- **Content merge.** The probe amplifies the *current channel's*
  waveform in the element's neighbourhood — hovering a CH 03 card
  brightens square wave, not a generic glow — and the amplification
  ceiling respects the law: local amplitude may reach at most the
  channel's logged peak × 1.0 of full scale, so a probe can reveal the
  signal's full height but never invent a taller one.
- **Failure fallback.** The probe is a steering overlay on §6.2's pass;
  if the canvas has fallen back, hover falls back to the printed
  responses specified per component in §11 (link colour, card lift,
  focus ring) — no element's state depends on the canvas to be visible.
  No-JS: CSS `:hover`/`:focus-visible` print responses only.
- **Reduced-motion variant.** No amplification travel: the trace segment
  near a hovered element brightens in place (phosphor-dim → phosphor, a
  value change, not a motion) and the print responses carry the state.
- **Performance budget & mobile variant.** The field is one multiply in
  the existing sample loop, ≤0.15ms/frame while probing. Mobile/touch:
  no hover channel — probing fires on tap-focus for cards and rows
  (first tap brightens, second activates) and is skipped for links and
  buttons, which activate immediately with a brief §6.8 blip instead.
- **Choreography timeline (v2).** Pointerenter/focus → t=0 field
  target set → t≈250 full ±40% within the falloff → hold while hovered
  → leave/blur → t=0–500 decay → untouched. Retarget: new target set,
  field slides, no decay phase.
- **State matrix (v2).** *Rest:* no field. *Hover:* full probe.
  *Focus:* full probe, plus the element's printed focus ring (§11).
  *Active:* the press fires §6.8's blip at the element; the probe holds
  through the press. *Scrolled-past:* an element scrolled out mid-hover
  releases immediately. *Disabled:* no probe. *Touch:* tap-focus
  behaviour above.
- **Breakpoints (v2).** ≥1200px: falloff radius 160px. 768–1199px:
  130px. <768px: tap-only, radius 110px, amplification ±30% (a small
  screen's band is shorter; the probe is gentler).
- **Edge cases & failure modes (v2).** *Element wider than the falloff*
  (a full-width table row): the field anchors to the pointer's x within
  the element, not the element's centre — the probe brightens where the
  hand is. *Fast pointer skim across a card grid:* retargeting with the
  0.12 lerp smooths the skim into a travelling brightening; no card
  reaches full amplification from a skim, which is the correct physics.
  *Probe during a §6.4 count:* the count's stat block is itself
  probeable; amplification is capped so the stat's peak marker zone is
  never visually inflated past its printed value's position.
- **Accessibility spec (v2).** The probe never carries state alone:
  every probeable element has a printed hover/focus response (§11), and
  the visible focus indicator is a 2px `--paper` outline at 3px offset,
  present with or without canvas. Amplification is not announced.
  Touch targets ≥44px; the 160px field is visual only.
- **Tokens consumed (v2).** `--phosphor`, `--phosphor-dim`,
  `--loop-lerp-probe` (0.12), `--probe-gain` (±40%), `--probe-radius`
  (160px).

### 6.8 Waveform blip click

- **What & why.** Clicking fires one clean blip in the current section's
  waveform shape at the trace beside the clicked element — sine sections
  blip round, square sections blip square — decaying over ~600ms. It
  belongs because feedback here is emitted in the section's own signal
  language: the click speaks the local frequency, and the visitor hears
  the answer in the dialect of the room they're standing in.
- **Structure.** A blip is an entry in the loop's blip list: origin x
  (the clicked element's band-nearest point), birth time, and the
  current channel's character function. The canvas pass adds the blip's
  contribution — one cycle of the character at the channel's logged
  peak amplitude × 0.6 — into the samples within one period either side
  of the origin, weighted by the decay envelope. Clickable elements
  keep their own behaviour untouched; the blip is a parallel response
  to the same event, fired from a delegated pointerdown listener.
- **Motion spec.** Attack 20ms (a blip is a pulse, not a swell). Decay:
  exponential over 600ms (`e^(−t/200ms)`), no overshoot — a blip is
  cleaner than a spike (§6.6's transients ring; a blip is the
  instrument's own test pulse and does not). Maximum 3 concurrent
  blips; a fourth replaces the oldest. Keyboard activation (Enter/Space
  on a focused element) fires the blip from the element's centre —
  keyboard touch speaks too.
- **States.** Idle / blipping / decayed (removed). A click on a disabled
  control fires no blip — dead air over a dead control, consistent with
  §6.7's disabled ruling. A click during CH 06 (silence) fires the
  *smallest* blip on the page: one cycle at the noise floor's printed
  height, which is to say almost nothing, with the section's caption
  noting *"CH 06 answers at −61.5 dBFS. That was full volume."* — the
  joke is the record's, and it is told once, in print.
- **Content merge.** The blip's shape is the section's character and its
  height derives from the section's logged peak — the feedback is
  *about* the content it answers. Clicking the form's submit (§6.14)
  fires the blip that becomes the confirmation's first signal, before
  the receipt prints: cause, then paperwork.
- **Failure fallback.** Fire-and-forget on the shared loop: if the
  canvas has fallen back, clicks simply produce no blip and every
  control's own feedback (§11) is unaffected. No-JS: no blips; controls
  work.
- **Reduced-motion variant.** No travelling pulse: the band segment
  beside the element brightens to full phosphor for 200ms and returns —
  an acknowledgement lamp, not a wave.
- **Performance budget & mobile variant.** Blip evaluation folds into
  the existing sample loop; ≤0.1ms/frame with 3 live. Mobile: blip
  amplitude × 0.45 (matching §6.7's gentler small-screen physics), max
  2 concurrent.
- **Choreography timeline (v2).** Pointerdown → t=0 blip born at
  origin → t=20 peak (one cycle, channel character) → decay 600ms →
  removed. Keyboard: same, from element centre.
- **State matrix (v2).** *Rest:* no blip. *Hover:* none (hover is
  §6.7's). *Focus:* keyboard activation fires the blip. *Active:* full
  blip from the pointer point. *Scrolled-past:* n/a — blips are
  viewport events. *Disabled:* no blip. *Touch:* tap = pointerdown,
  identical.
- **Breakpoints (v2).** ≥1200px: full amplitude (peak × 0.6), 3
  concurrent. 768–1199px: × 0.55, 3 concurrent. <768px: × 0.45,
  2 concurrent.
- **Edge cases & failure modes (v2).** *Click storms:* the 3-blip cap
  with oldest-replacement keeps the band legible; beyond 8 clicks in
  2s, new blips are suppressed for 1s — the instrument does not reward
  panic, and §12's voice says so nowhere (some disciplines are silent).
  *Click during the hero eruption:* blips queue until the eruption
  settles (t=1500ms) — the name is being spoken; the room does not
  interrupt it. *Click on the masthead dial:* the blip fires in the
  *destination* channel's character after navigation (§6.10) — the
  answer comes from the room you asked for.
- **Accessibility spec (v2).** The blip is never the sole feedback for
  any action; every control's activation has its printed result (§11).
  It is `aria-hidden` canvas behaviour, unannounced. One cycle at 2px
  line width is far below any photosensitivity concern.
- **Tokens consumed (v2).** `--phosphor`, `--dur-blip` (600ms),
  `--blip-gain` (0.6), `--ease-print`.

### 6.9 Scope-frame images

- **What & why.** Photographs — the bench, the harbour hydrophone, the
  station at night — sit inside oscilloscope frames: a graticule border,
  four corner screws, and a fine division scale along the bottom edge.
  They scale 1.05 → 1.0 on entry while a brief trace flicker crosses the
  frame. It belongs because in this room a picture is a signal under
  observation: framed by the same instrument that measures everything
  else, captioned like a reading, never pasted on as decoration.
- **Structure.** A `<figure>` with a real `<img>` (complete `alt`, real
  dimensions, lazy below the fold), wrapped in a frame div: 1px `--grid`
  border, an inner graticule overlay (the §4 grid at 40% opacity,
  `pointer-events: none`), four screw heads as inline SVG (one
  definition, four `<use>`), and a bottom scale strip printing the
  frame's division size and the photograph's provenance in label style
  — *"BENCH 2 — 10 MS/DIV — FILM, OCT 2026."* The caption prints beneath
  in paper, written as a reading (§12), not a description.
- **Motion spec.** Trigger: the frame crossing the measurement line.
  Scale 1.05 → 1.0 over 700ms `--ease-settle`, scrubbed to the frame's
  passage through the centre band (not time-based — the approach is
  scroll's, like a specimen sliding under a lens). The flicker: one
  phosphor trace in the frame's channel character crosses the glass
  left-to-right over 300ms at the moment the scale completes, at 30%
  opacity, drawn on the frame's own small canvas-free SVG line (a
  `stroke-dashoffset` draw — §5's licensed line-draw). Hover: the
  graticule overlay lifts to 60% and §6.7's probe gathers at the
  frame's edge.
- **States.** Approaching (scale >1.0, below the line) / seated (1.0,
  flicker spent) / scrolled-past (seated persists; the flicker never
  replays) / image failed (below).
- **Content merge.** The frame's scale strip prints a timebase from the
  record's world and the caption reports the photograph as a session
  artefact — the bench photograph is credited to the night of Session
  № 214 (§6.17). A photograph with no provenance does not get a frame;
  §11's plain-image component exists for unmeasured pictures, and it is
  deliberately plainer.
- **Failure fallback.** The shipped state is seated (scale 1.0); the
  loop only ever *raises* scale toward 1.05 for frames below the line
  and settles them as they cross — a dead loop leaves every image
  seated and complete. Image failed to load: the frame holds, its
  graticule overlay stays, and the alt text prints inside the frame in
  paper with the scale strip intact — a labelled empty frame on the
  record, never a broken icon.
- **Reduced-motion variant.** Seated at all positions; no scale, no
  flicker. The frame and its provenance remain — the observation
  survives its theatre.
- **Performance budget & mobile variant.** The scale is a compositor
  transform on the `<img>`; the flicker is one SVG path draw. Images
  are budgeted in §14 (≤180KB each, responsive sizes, WebP/AVIF).
  Mobile: scale range narrows to 1.03 → 1.0, screws shrink to 8px, the
  scale strip drops its division figure and keeps provenance.
- **Choreography timeline (v2).** Frame enters centre band → scale
  scrubs 1.05 → 1.0 across the passage → at seat: flicker crosses
  (300ms) → frame at rest, probeable.
- **State matrix (v2).** *Rest:* seated. *Hover:* overlay 60%, edge
  probe (§6.7). *Focus:* a figure is not focusable; a linked caption
  probes per §6.7. *Active:* n/a. *Scrolled-past:* seated, flicker
  spent. *Disabled (image failed):* printed alt inside the frame.
  *Touch:* identical scrub; no hover lift.
- **Breakpoints (v2).** ≥1200px: full frame, scale 1.05. 768–1199px:
  scale 1.04. <768px: scale 1.03, 8px screws, shortened scale strip.
- **Edge cases & failure modes (v2).** *Portrait image in a landscape
  frame:* the frame fits the image's real aspect (frames are built per
  image, not cropped to a house ratio) — a scope is fitted to its
  signal, and cropping a photograph to fit furniture is banned in §9.
  *Two frames in one viewport:* §4's density rule forbids it; if a CMS
  build violates it, the second frame's flicker is suppressed (one
  observation at a time).
- **Accessibility spec (v2).** Real `alt`, written as a reading
  ("The bench at Listening Post 1 during Session № 214: scope,
  hydrophone pre-amp, the night log open at CH 03"). Frame furniture is
  `aria-hidden`. Caption contrast paper on char 13.3:1; scale-strip
  labels paper-dim 7.1:1 at 11px.
- **Tokens consumed (v2).** `--grid`, `--phosphor`, `--paper`,
  `--paper-dim`, `--char`, `--ease-settle`, `--dur-flicker` (300ms).

### 6.10 Flatline transition

- **What & why.** On navigation, the trace flatlines for 200ms, a sweep
  clears the graticule, and the new page's signal erupts from silence
  with its own waveform character. It belongs because leaving a page
  here is a channel going silent and arriving is a new signal —
  navigation as tuning, the theme's grammar applied to the site's
  skeleton.
- **Structure.** A transition mode of the shared canvas plus a DOM
  sweep element: on an internal navigation click, the loop drives the
  current trace's amplitude to the floor over 200ms (a true flatline —
  to CH 06's 0.003-div height, not to a hidden canvas), the sweep (a
  2px phosphor vertical line) crosses the viewport left-to-right over
  350ms dimming the graticule behind it, the router swaps content, and
  the destination page's first channel erupts per §6.1's grammar at
  60% duration (silence 360ms, settle 540ms) with its own character.
  The whole sequence is skippable: a second click or any keypress
  during it completes the navigation instantly.
- **Motion spec.** Flatline 200ms `--ease-settle` (amplitude only;
  phase freezes — a dying signal stops, it does not slide). Sweep
  350ms `--ease-sweep`. Total perceived interruption ≤1400ms,
  watchdogged (below). External links, downloads and `target=_blank`
  never flatline — the station does not perform silence for a door it
  doesn't own.
- **States.** Live / flatlining / sweeping / erupting (destination) /
  aborted (skip input → destination printed settled). Browser
  back/forward: the transition runs in reverse grammar — no flatline,
  the restored page fades its trace in at settled amplitude (history is
  a recording; you don't re-tune to a tape you rewound).
- **Content merge.** The destination's eruption uses *its* first
  channel's character and logged peak — arriving at the archive sounds
  different from arriving at the log, because they are different
  stations. The sweep clears the *graticule*, the shared glass: the
  room persists, the signal changes.
- **Failure fallback.** Watchdog at 1400ms: the destination forces its
  settled state — a transition may never strand a visitor in silence
  between pages. No-JS / no-router: plain navigation, complete pages,
  no transition — the fallback is the web's own.
- **Reduced-motion variant.** No flatline, no sweep: plain navigation;
  the destination's hero prints settled. Nothing about the route's
  information changes.
- **Performance budget & mobile variant.** The transition reuses the
  loop and one DOM element; zero added assets. Mobile: sweep shortens
  to 250ms and the destination eruption uses the hero's mobile timing
  (§6.1) — total ≤1100ms.
- **Choreography timeline (v2).** Click → t=0 flatline begins →
  t=200 flat → sweep t=200–550 → content swap at sweep's midpoint
  (t≈375, behind the line) → destination silence 360ms → eruption
  settles by t≈1250 → live. Watchdog ceiling t=1400.
- **State matrix (v2).** *Rest:* live page. *Hover:* n/a. *Focus:*
  focus moves to the destination's `<h1>` at swap (announced by the
  router per §11) — the transition never leaves focus in a removed
  page. *Active:* the triggering link's blip (§6.8) fires in the
  destination's character after arrival. *Scrolled-past:* n/a.
  *Disabled:* a link to an unpublished page does not flatline; it
  routes to §6.18's no-signal page by plain navigation. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: full sequence. 768–1199px: full,
  sweep 300ms. <768px: sweep 250ms, eruption at mobile timing.
- **Edge cases & failure modes (v2).** *Slow destination data:* the
  flatline holds at the floor with §6.15's flat-line loader taking
  over after 600ms — silence that is *loading* is drawn as a line
  gaining signal segment by segment, never as a spinner. *Navigation
  cancelled by the router* (guard, auth): the trace re-erupts on the
  *current* page at 40% duration and the visitor has lost nothing but
  800ms. *Two rapid navigations:* the second supersedes; watchdogs
  belong to the newest destination only.
- **Accessibility spec (v2).** The transition is never announced; the
  destination's heading is, once, by the router's live region
  (§11). Focus management as in the state matrix. The flatline is a
  2px line dimming — no flash, no large-area luminance change.
- **Tokens consumed (v2).** `--phosphor`, `--grid`, `--char`,
  `--ease-settle`, `--ease-sweep`, `--dur-flatline` (200ms),
  `--dur-sweep` (350ms), `--dur-watchdog-transition` (1400ms).


### 6.11 Channel-index masthead & navigation

- **What & why.** The masthead is the station's dial: the wordmark at
  the left, and the six channels laid out as a tuner strip — `CH 01 ·
  196.00` through `CH 06 · 0.00` — with the channel the visitor is
  currently inside lit in phosphor. It belongs because navigation here
  is tuning: the index is not a menu of pages but the front panel of
  the instrument, and it tells you which frequency you are on before
  it offers you another.
- **Structure.** A `<header>` with a real `<nav aria-label="Channels">`,
  sticky at top, ground a vertical gradient from `--char` to
  transparent over 64px so the panel dissolves into the screen rather
  than ending at a rule. The wordmark is Unbounded (§3's ration: this
  is its second licensed setting). Each dial entry is a link: channel
  number, station frequency in mono, and a small character glyph (a
  24px static SVG of the channel's waveform at its logged relative
  height — CH 06's glyph is a flat line, honestly). The current
  channel's entry carries `aria-current="location"`, its glyph at full
  phosphor; others sit in `--paper-dim` with glyphs in
  `--phosphor-dim`. A scrollspy reading the same section offsets as
  §6.2's morph map — one source of "where am I" for dial, morph and
  readouts — drives the current state.
- **Motion spec.** On load, after the hero eruption settles, the dial
  entries light in sequence (60ms stagger, 200ms `--ease-print` each) —
  the panel warming up. Current-channel changes: the old entry dims
  over 300ms, the new entry's glyph draws itself (dashoffset, 240ms)
  and its figure lifts to phosphor. On scroll the masthead's gradient
  deepens (ground to 94% opacity) so print over the moving trace stays
  legible; on scroll-stop it relaxes over 500ms. No hide-on-scroll:
  the dial stays where a dial belongs.
- **States.** Rest: current channel lit. Hover: an entry's glyph
  brightens and its frequency figure lifts to paper. Focus: as hover,
  plus the §11 focus outline. Active (current): lit, `aria-current`.
  A channel whose page is unpublished prints as a *dead station*:
  dimmed to 45%, no link, glyph flat, annotated `OFF AIR` — the dial
  admits the gap rather than hiding the slot.
- **Content merge.** The dial *is* the record's channel list (§6.17) in
  front-panel form — same order, same frequencies, same characters as
  §6.2's morph and §6.13's table. A channel added to the record appears
  on the dial by the same edit; the three printings cannot drift.
- **Failure fallback.** Scrollspy failure (observer never fires within
  1000ms of load): CH 01 lights by default — the visitor starts at the
  hero, so that is never wrong. No-JS: no entry is marked current;
  every link works; the dial is a printed index.
- **Reduced-motion variant.** No warm-up sequence, no glyph draw:
  entries print lit or unlit as state dictates; changes are instant.
- **Performance budget & mobile variant.** Scrollspy via
  IntersectionObserver; zero per-frame cost. Mobile (<768px): the dial
  collapses to wordmark, current-channel readout, and a `TUNE` button
  opening a full-width panel (ground `--char-2` at 98%) listing all six
  stations at 48px targets, 200ms `--ease-settle`; the panel's entries
  carry the same glyphs and the same dead-station honesty.
- **Choreography timeline (v2).** Load → wordmark printed → hero
  settles → dial warms (60ms stagger) → first scroll: gradient deepens
  → section boundary crossed: old dims 300ms as new glyph draws 240ms
  → footer reached: CH 06 lit, figure `0.00`.
- **State matrix (v2).** *Rest:* current lit at full phosphor.
  *Hover:* glyph brightens, figure to paper. *Focus:* as hover +
  outline. *Active:* current channel — lit, `aria-current`.
  *Scrolled-past:* n/a (sticky). *Disabled:* dead stations, as above.
  *Touch:* entries ≥44px; current state by scrollspy only.
- **Breakpoints (v2).** ≥1200px: full dial, glyphs + figures.
  768–1199px: glyphs shrink to 18px, channel names drop (numbers and
  frequencies carry it). <768px: collapsed dial + TUNE panel.
- **Edge cases & failure modes (v2).** *Seven-plus channels in a
  future record:* below 9px glyph spacing the dial switches to the
  mobile pattern at any width — the panel is the overflow behaviour,
  designed now, not improvised later. *A channel removed in a CMS:*
  the offsets table is built from the DOM's actual sections, so dial,
  morph and scrollspy agree with the page that exists.
- **Accessibility spec (v2).** Landmarks as above; `aria-current` on
  the active link; glyphs decorative (`aria-hidden`) — current-ness
  lives in the link's semantics and its printed figure, not only in
  light. Skip link is the masthead's first element, paper on
  `--char-2`, visible on focus. Figure contrast: phosphor 9.8:1 lit,
  paper-dim 7.1:1 unlit — both pass at 11–13px mono.
- **Tokens consumed (v2).** `--char`, `--char-2`, `--phosphor`,
  `--phosphor-dim`, `--paper`, `--paper-dim`, `--ease-print`,
  `--ease-settle`, `--dur-dial-stagger` (60ms).

### 6.12 Channel programme cards

- **What & why.** The channel index page — and the home page's second
  stretch — presents the six channels as programme cards: what is on
  each station, when it was logged, how loud it got. A card is a
  bench tag tied to a tape box: channel number, name in the
  annotator's hand, its waveform glyph drawn at its true relative
  height, station frequency, logged peak, minutes on air. It belongs
  because the index is the station's programme guide, and a guide
  printed from the log is a promise the recordings keep.
- **Structure.** A `<ul>` of `<li>` cards on `--char-2`, each an
  `<article>` wrapping one link to the channel's page. The glyph is an
  inline SVG trace in the channel's character, its amplitude scaled by
  the record's conversion (§6.17) relative to the session peak — CH 02's
  sine stands at 1.05 div against CH 01's 2.77, and the card grid's
  shared baseline makes the loudness *visible* before a figure is read.
  Figures print in mono beneath: `55.00 HZ · PEAK −11.6 DBFS · 48 MIN`.
  The grid's header prints the totals it must sum to: `6 CHANNELS ·
  240 MINUTES · 218 TRANSIENTS` (§6.17).
- **Motion spec.** Cards print in as the grid crosses the measurement
  line: rise 12px + `--ease-print` opacity, staggered 70ms in reading
  order. Tilt: pointer-driven rotateX/rotateY to max 3°, computed in
  the shared loop from lerped pointer values (never raw events) — a
  scope screen catching bench light. The glyph does not animate on
  hover; instead §6.7's probe brightens the band behind the grid at the
  card's position, and the card's own glyph lifts from
  `--phosphor-dim` to `--phosphor` over 200ms. Figures never animate.
- **States.** Rest: flat, glyph dim. Hover: tilt ≤3°, glyph full,
  edge probe (§6.7). Focus: the card's link focus lifts the glyph and
  shows the §11 outline; no tilt (a tag does not tilt for a voice).
  Active (pressed): tilt flattens to 0° in 100ms — the tag is picked
  up flat — then the link follows. A channel with no detail page is a
  *log-only* card: no link, glyph at 40%, annotated `LOG ONLY` — the
  guide admits which stations are summaries.
- **Content merge.** Every field is a record field (§6.17): number,
  name, character, frequency, peak, minutes. The six cards' minutes
  sum to the grid header's 240 and §10 re-adds them; the glyphs'
  relative heights are the peaks' relative heights — the grid is the
  table (§6.13) you can see from across the room.
- **Failure fallback.** Tilt and probe are loop-driven; a dead loop
  leaves flat printed cards with dim glyphs — complete. No-JS:
  identical, with CSS hover lift on the glyph. Glyphs are inline SVG:
  nothing to break, nothing to load.
- **Reduced-motion variant.** No tilt, no stagger: cards print as a
  block; hover lifts the glyph only.
- **Performance budget & mobile variant.** Tilt math is two lerped
  values on the one hovered card; glyphs are static SVG. Grid: 3
  columns ≥1200px, 2 at 768–1199px, 1 below 768px. Mobile: tilt off;
  tap fires the edge probe as a 300ms farewell brightening as §6.10's
  transition begins.
- **Choreography timeline (v2).** Grid crosses line → cards rise in
  70ms stagger → rest → pointer enters a card → glyph lifts 200ms,
  tilt lerps to pointer angle, probe gathers (§6.7) → pointer leaves →
  probe releases, tag settles 500ms `--ease-settle`.
- **State matrix (v2).** *Rest:* flat, glyph dim. *Hover:* tilt ≤3°,
  glyph full, probe. *Focus:* glyph lift + outline, no tilt.
  *Active:* flatten 100ms, then navigate. *Scrolled-past:* flat print.
  *Disabled:* log-only cards, as above. *Touch:* no tilt; tap probe +
  transition.
- **Breakpoints (v2).** ≥1200px: 3 columns, tilt on. 768–1199px:
  2 columns, tilt max 2.5°. <768px: 1 column, tilt off, glyph height
  48px.
- **Edge cases & failure modes (v2).** *A channel louder than the
  session peak is added mid-season:* glyph scaling is relative to the
  *grid's* declared maximum (§6.17's session peak at build); a new
  maximum rescales every glyph in the same edit — §10 checks glyph
  heights against peaks. *Long channel names:* names set in Grotesk at
  1.25rem and wrap to two lines; the figure row never wraps (units are
  short by §3's law).
- **Accessibility spec (v2).** The whole card is one link with one
  accessible name ("CH 03 — Switchyard — square — 440 hertz — peak
  minus 6.8 dBFS — 44 minutes"); the glyph is `aria-hidden` (its height
  is data, and the same data is printed as figures). Focus outline 2px
  `--paper` at 3px offset on the card. Text contrast: paper on
  `--char-2` 12.2:1; figures paper-dim on `--char-2` ≈6.4:1 at 11px
  mono — AA for its class.
- **Tokens consumed (v2).** `--char-2`, `--phosphor`,
  `--phosphor-dim`, `--paper`, `--paper-dim`, `--ease-print`,
  `--ease-settle`, `--tilt-max` (3deg), `--loop-lerp-probe` (0.12).

### 6.13 The session log table

- **What & why.** For the visitor who wants the night plain: a true
  data table of Session № 214 — one row per channel with its station
  frequency, waveform, timebase, logged peak (in dBFS and in the
  divisions the trace actually drew), transients counted and minutes
  on air — with a totals row carrying 218 and 240. It belongs because
  a listening station that cannot be read as a table is a light show;
  the table is the theme's honesty made structural, and §1's audience
  reads it first.
- **Structure.** A semantic `<table>` with `<caption>` ("Session № 214
  — the Night Log, 14 November 2026, 22:00–02:00 UTC"), `<th
  scope="col">` headers, `<th scope="row">` channel names, tabular
  mono numerals throughout. Rows alternate `--char` / `--char-2`. The
  peak column prints both units — `−6.8 dBFS · 1.83 DIV` — because the
  conversion (§6.17) is the theme's law and the table shows its working.
  The totals row is separated by a phosphor hairline and its figures
  set in phosphor (§3: the instrument's voice totals). The red legend
  swatch (§2's census, 2 of 2) sits in the table's footnote: *"0 dBFS —
  the ceiling. Nothing tonight reached it."*
- **Motion spec.** The table does not animate — no reveal beyond its
  section's print rise (§5). Row hover: ground lifts to a 6% phosphor
  tint over 200ms and §6.7's probe gathers along the row's band segment.
  That is all. The restraint is the spec: the one element a hurried
  reader uses is the one element that never performs.
- **States.** Rest: printed, striped. Hover (row): lift + probe.
  Focus: rows are not focusable; the channel-name links inside them
  probe per §6.7. A channel whose figures are provisional (a night
  still being verified) prints its row in `--paper-dim` with a
  `PROVISIONAL` tag — the table admits the state of its evidence
  rather than hiding the row.
- **Content merge.** The table *is* §6.17's record in reading flow —
  same rows, same order, same totals — and its peaks are the heights
  §6.2's trace drew and §6.12's glyphs stand at. Table, trace and
  cards are three readings of one night.
- **Failure fallback.** None required: static HTML with a CSS hover.
  This element is the fallback's fallback — §10's canvas-failure drill
  ends here, with the night still fully readable.
- **Reduced-motion variant.** Identical, minus the hover transition
  (instant lift) and the probe.
- **Performance budget & mobile variant.** Zero JS beyond §6.7's shared
  probe. Mobile (<768px): the table becomes a stacked log — each
  channel a block with its figures in definition-list layout, same
  order, same totals, the dual-unit peak kept. No horizontal scroll is
  ever permitted: a log you must pan is a log lost.
- **Choreography timeline (v2).** Section print rise → table at rest →
  row hover: lift 200ms, probe gathers (§6.7) → leave: release 500ms.
  Nothing else, ever.
- **State matrix (v2).** *Rest:* printed stripes. *Hover:* row lift +
  probe. *Focus:* cell link probe. *Active:* n/a. *Scrolled-past:*
  printed. *Disabled:* provisional rows dimmed and tagged.
  *Touch:* tap on a row lifts it for 600ms (no probe gather).
- **Breakpoints (v2).** ≥1200px: full 7-column table. 768–1199px:
  6 columns (timebase folds into the channel cell as a sub-line).
  <768px: stacked log blocks.
- **Edge cases & failure modes (v2).** *A channel with zero
  transients* (a perfectly smooth night): the row prints `0` in full
  paper — an absence counted is not an absence hidden, and CH 06's
  row already models the principle with its `−61.5 dBFS · 0.003 DIV`
  peak. *Print:* the table is the print stylesheet's centrepiece —
  full grid, ink on paper, totals in bold (§2's print mode).
- **Accessibility spec (v2).** Real table semantics with caption and
  scoped headers; the totals row is a `<tfoot>` with `scope="row"`.
  Screen readers receive the night in its most native form. Contrast:
  paper on char 13.3:1, paper on `--char-2` 12.2:1, phosphor totals
  9.8:1, paper-dim footnote 7.1:1. The probe is `aria-hidden`
  decoration on a table that needs nothing from it.
- **Tokens consumed (v2).** `--char`, `--char-2`, `--phosphor`,
  `--paper`, `--paper-dim`, `--red` (the legend swatch — census 2 of
  2), `--ease-settle`.

### 6.14 Request-a-recording form & its stamped confirmation

- **What & why.** The observatory's conversion: a visitor who has heard
  something — a harbour at dawn, a stairwell's hum — asks the station to
  record it. The form is a log-book page: the requester's name, the
  place, the sound described in their own words, and the night they'd
  like it captured. On submit, the confirmation is a log entry —
  *"REQUEST № 1,209 — LOGGED"* — stamped onto the page, and one blip
  (§6.8) fires in CH 01's character beside it: your sound, entered into
  the station's night. It belongs because it is the only element where
  the visitor adds a signal to the station, and the law is honoured:
  the new entry is numbered from the record (§6.17), not from a
  database's convenience.
- **Structure.** A real `<form>` with native validation semantics,
  enhanced never replaced: labelled inputs on `--char-2`, paper text,
  2px `--paper` focus outline plus the field's edge probe (§6.7). The
  preamble prints the record's line: *"1,208 requests on file. Yours
  will be № 1,209."* — the derivation shown before the visitor writes a
  word, so the confirmation number is a kept promise. On submit (JS
  intercepts, posts, and on success swaps the form region for the
  confirmation entry); without JS the form posts to its endpoint and
  the confirmation is a server-rendered page with the same entry and
  number.
- **Motion spec.** Field focus: edge probe gathers (§6.7); the field's
  ground lifts with a 5% phosphor tint over 250ms. Submit: §6.8's blip
  fires from the button; the form dims to 60% over 300ms while the
  entry is written — the "logging" state is §6.15's flat-line pulse on
  the button, never a spinner. Success: the confirmation entry prints
  in with a 500ms rise `--ease-settle`, and its stamp — the request
  number in a phosphor rule box, rotated −2° — lands at t=300 with a
  120ms scale settle (1.06 → 1.0, `--ease-lock`): a hand stamp, once.
  Error: the offending field's marker draws in phosphor (a small
  caret, the log's correction mark) and its error line prints beneath
  in paper — no shake, no red, ever (§2's census).
- **States.** Rest: printed log page, preamble showing № 1,209. Focus:
  per-field probe + lift. Active (submitting): form at 60%, button
  pulsing flat-line, fields disabled. Success: confirmation entry +
  stamp + blip. Error: field marked, error line printed, focus moved
  to the first error, values preserved. Disabled (endpoint down): the
  form prints a log note — *"The log is closed tonight; requests
  resume at dusk."* — and holds the visitor's words in the fields,
  unsubmitted, unlost.
- **Content merge.** The preamble number is the record's request count;
  the confirmation number is that count + 1; the blip is CH 01's
  character because a spoken request enters through the station's own
  channel. The conversion is not decorated with the theme — it is
  transacted inside it.
- **Failure fallback.** Watchdog at 4000ms on submission: if no
  response, the form restores from 60% and prints the log note *"the
  entry could not be written — your words are still here"* with values
  intact; the submit token is idempotent per form instance, so nothing
  double-logs. No-JS: native post, server confirmation, as above.
  Canvas absent: the confirmation prints without the blip — the number
  is the record; the blip is its portrait.
- **Reduced-motion variant.** Confirmation prints instantly; the stamp
  lands without scale (present, unrotated at −2° as print). Errors
  print without transition.
- **Performance budget & mobile variant.** The form's JS is ≤5KB gz,
  deferred, beyond the shared loop. The stamp is one transform.
  Mobile: single column, fields full measure, submit full-width at
  ≥48px; the stamp lands at the entry's head rather than its side.
- **Choreography timeline (v2).** Focus field → probe gathers → submit
  → blip fires, form dims 300ms → logging pulse → response → entry
  rises 500ms → t=300 stamp lands (120ms settle) → confirmation at
  rest. Watchdog ceiling 4000ms on the submission.
- **State matrix (v2).** *Rest:* log page printed, № 1,209 promised.
  *Hover:* field edge probes (§6.7). *Focus:* probe + ground lift +
  outline. *Active:* submitting state as above. *Scrolled-past:* the
  form waits; an in-flight submission completes regardless of scroll.
  *Disabled:* log-closed note, values held. *Touch:* identical;
  targets ≥48px on fields.
- **Breakpoints (v2).** ≥1200px: two-column log page (place + night
  side by side), measure 44rem. 768–1199px: single column, 38rem.
  <768px: single column full measure, stamp at entry head.
- **Edge cases & failure modes (v2).** *A request for an impossible
  recording* (a sound that no longer exists — a demolished hall): the
  log voice accepts and annotates — the confirmation entry adds the
  annotator's line *"Noted as a memorial request. The station records
  what remains: the room tone of the site, as it is now."* — the form
  never refuses a sound, it reclassifies it honestly. *Duplicate
  request* (same place, same sound): the entry prints with the
  marginal note *"second request for this sound — corroboration, not
  duplication."* *Empty description:* the error voice is the log's
  (§12): *"The log needs the sound in your words — even three will
  do."*
- **Accessibility spec (v2).** Native labels on every field (visible,
  paper, 13.3:1); errors use `aria-describedby` and an
  `aria-live="polite"` summary in the log's own words; the confirmation
  is an `aria-live` region announcing "Request № 1,209 — logged" once.
  Focus management: on error, to the first invalid field; on success,
  to the confirmation heading. The stamp and blip are `aria-hidden`.
  Error markers are never colour-alone: the caret pairs with the
  printed words "correct this".
- **Tokens consumed (v2).** `--char-2`, `--phosphor`, `--paper`,
  `--paper-dim`, `--ease-settle`, `--ease-lock`, `--ease-print`,
  `--dur-watchdog-form` (4000ms).


### 6.15 Flat-line loader & signal-acquisition skeleton

- **What & why.** Loading in this station is a flat line that gains
  signal: a region still arriving shows the trace at the floor, and as
  its data lands, the stretch of trace beside it takes the arriving
  channel's character segment by segment, left to right, until the
  region prints in full. It belongs because a spinner would be a
  machine from another room; an unloaded channel is simply a silent
  one, and the honest drawing of "nothing yet" is a flat line — the
  same drawing the station uses for measured silence, distinguished by
  its caption: *"ACQUIRING."*
- **Structure.** Skeleton regions are DOM elements with a `data-acquire`
  attribute, each paired with a segment of the section's static fallback
  trace (an SVG line, §6.2) whose dash pattern is the mask: unacquired
  segments render at floor height; as the region's data resolves, its
  segment redraws in character and the real content — already in the
  DOM or injected complete — prints in beneath it with a 300ms
  `--ease-print` rise. The acquisition caption prints in label style at
  the region's foot and is removed when the region lands. Page-level
  first load uses the same system at full width: the hero's band runs
  flat with `ACQUIRING` until the record (§6.17) and fonts resolve,
  then §6.1's silence begins — acquisition is *before* the held breath,
  and the two are never blurred.
- **Motion spec.** Segment acquisition is discrete, not tweened: each
  segment snaps from flat to character in one frame as its data lands
  (a channel coming online is an event, not a fade). The flat line
  itself carries a barely-alive floor shimmer — the noise floor's true
  ±0.003 div is invisible, so the loader draws the floor at a declared
  0.5px with the caption disclosing it: *"floor drawn at half a pixel —
  the real floor is lower."* Hard ceiling: any region still acquiring
  at 1500ms prints its content anyway, signal or not — the station does
  not hold a reader hostage to a slow tape.
- **States.** Acquiring (flat + caption) / landing (segment in
  character, content rising) / landed (caption gone). Error (a region's
  data fails): the segment stays flat and the region prints its log
  note — *"this channel did not reach the bench — [retry]"* — in paper
  with a real retry control; the line never shimmers forever.
- **Content merge.** The skeleton's shape is the arriving channel's own
  trace acquiring its own character: the loader is the content in its
  not-yet state, drawn by the same functions (§6.2) that will draw it
  live. There is no grey-box vocabulary anywhere in the theme.
- **Failure fallback.** Watchdog per region at 1500ms (print
  regardless); on the page transition, §6.10's 1400ms watchdog owns the
  ceiling. No-JS: no skeletons exist; content is server-printed
  complete.
- **Reduced-motion variant.** No shimmer, no segment drama: regions
  print when their data lands, with the `ACQUIRING` caption as the only
  signal of state; the ceiling is unchanged.
- **Performance budget & mobile variant.** Segments are SVG dash
  updates — zero per-frame cost. Mobile: the page-level acquisition
  caption moves above the band (the band sits higher, §6.2), segments
  otherwise identical.
- **Choreography timeline (v2).** Region requested → flat segment +
  caption print with layout → data lands → segment snaps to character,
  content rises 300ms → caption removed → region at rest. Ceiling
  1500ms forces print.
- **State matrix (v2).** *Rest:* printed content. *Hover:* n/a.
  *Focus:* acquiring regions are `aria-hidden` until printed and never
  focusable. *Active:* the form's submitting state (§6.14) borrows the
  flat-line pulse on its button. *Scrolled-past:* regions below the
  fold acquire regardless of visibility — by the time the visitor
  tunes down to them, they are print. *Disabled / no-JS:* server
  print, no skeletons. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full treatment. 768–1199px: full.
  <768px: caption above band; segment count per region halves (longer
  segments, same information).
- **Edge cases & failure modes (v2).** *Data arrives before the
  skeleton paints (fast cache):* the region prints directly — a loader
  that never appears is the best kind. *Partial failure (4 of 6 cards
  land):* landed cards print; unlanded regions hold flat until their
  own retry or the ceiling, then print their log notes individually —
  the index opens with gaps admitted, not held shut.
- **Accessibility spec (v2).** Acquiring containers carry
  `aria-busy="true"` and are removed from the accessibility tree until
  printed; one polite announcement ("Session loaded") fires when the
  last above-fold region lands — not one per region. The error note's
  contrast: paper on char 13.3:1; the retry control is a §11 button.
- **Tokens consumed (v2).** `--phosphor`, `--phosphor-dim`, `--paper`,
  `--char`, `--ease-print`, `--dur-acquire-ceiling` (1500ms).

### 6.16 End-of-transmission footer

- **What & why.** The page ends the way a session ends: the trace
  settles to the floor, the totals are printed one last time, and the
  station signs off. The footer carries the session's third printing of
  its totals (240 minutes · 218 transients · peak −3.2 dBFS), the
  colophon — including the disclosure that the hero waveform is the
  FFT of the spoken name — and the station's standing line: *"END OF
  SESSION № 214 — THE STATION KEEPS LISTENING."* It belongs because a
  log that does not close is not a log; the footer is the night being
  signed.
- **Structure.** A footer section on solid `--char` (the band has
  ended; the canvas trace parks at the floor above it). Three columns
  at desktop: totals (mono, phosphor figures, paper labels), the
  colophon in the annotator's hand (Grotesk, paper, two short
  paragraphs), and the station index repeated small (the six channels
  with frequencies — the dial's print form, §6.11). A hairline
  `--grid` rule above, set like the log table's totals rule (§6.13).
  The sign-off line sets in station style, uppercase mono, letterspaced,
  last on the page.
- **Motion spec.** As the footer crosses the measurement line, the
  trace performs its one closing gesture: amplitude eases to the floor
  over 900ms `--ease-settle` and the final transient of the visit — a
  single spike in CH 06's near-nothing character — fires at the
  footer's rule and decays (§6.6's physics, scripted once, not ambient).
  The totals do not count (they were read at §6.4; the footer *confirms*
  them — a signature, not a performance). Nothing else moves.
- **States.** Open (page above still live) / signed (footer crossed:
  trace at floor, sign-off printed). Scrolling back up re-opens the
  session: the trace resumes the current channel's character — the
  sign-off is a state of position, not a latch, because a visitor who
  scrolls back is a session resumed.
- **Content merge.** The footer's totals are the record's (§6.17),
  printed for the third time (stats §6.4, table §6.13, here) so §10 can
  audit three printings for agreement — the theme's idea of a checksum.
  The colophon discloses the hero's method and the spike cadence
  compression (§6.6) a second time, at the point of leaving, where
  disclosures belong.
- **Failure fallback.** Static by construction: the closing gesture is
  loop garnish on printed totals. No-JS: footer complete, trace absent
  or static per §6.2's fallback.
- **Reduced-motion variant.** No closing gesture: the trace prints at
  its channel character above the footer and the footer is simply read.
  The sign-off line carries the ending alone.
- **Performance budget & mobile variant.** One amplitude tween on the
  shared loop; zero assets. Mobile: columns stack — totals, colophon,
  index — sign-off last, unchanged.
- **Choreography timeline (v2).** Footer approaches line → amplitude
  eases down 900ms → at the rule: one floor spike fires, decays 1200ms
  → trace rests at floor → sign-off in view → signed. Scroll up: trace
  resumes within one lerp cycle (~300ms).
- **State matrix (v2).** *Rest:* signed (when in view). *Hover:* index
  links behave per §11; nothing else responds. *Focus:* links per §11.
  *Active:* n/a. *Scrolled-past:* scrolling beyond is impossible; the
  footer is the floor. *Disabled:* dead-station entries in the index
  print per §6.11's ruling. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: three columns. 768–1199px: two columns
  (totals + colophon; index full-width below). <768px: stacked single
  column.
- **Edge cases & failure modes (v2).** *Short page (a single-channel
  page):* the footer still signs with that page's session totals from
  its own record — every page of the station is a session, and §6.17's
  record is per-page data, with the Night Log as the home page's.
  *The closing spike under reduced motion:* omitted entirely (above) —
  never replaced by a flash or a colour change.
- **Accessibility spec (v2).** Footer landmark (`contentinfo`); the
  totals are text; the closing gesture is `aria-hidden`. Sign-off
  contrast phosphor on char 9.8:1 at 13px mono uppercase — passes AA.
  Link contrast per §11.
- **Tokens consumed (v2).** `--char`, `--grid`, `--phosphor`,
  `--paper`, `--paper-dim`, `--ease-settle`, `--dur-signoff` (900ms).

### 6.17 The session record — the one source of every figure

- **What & why.** Every figure on the page traces to one declared
  record, printed in full on the record page (and summarised in the log
  table, §6.13): **Session № 214, the Night Log — Waveform Observatory,
  Listening Post 1, 14 November 2026, 22:00–02:00 UTC.** It belongs
  because the theme's law (§1) is unenforceable without a single source:
  the record is where a builder — or a sceptical visitor — goes to check
  that the trace never lied. This element is the record's own build
  spec: how it is stored, printed and audited.
- **Structure.** One data object (JSON in the build, a printed table on
  the record page) with five blocks. *(a) The session:* number 214;
  window 22:00–02:00 UTC = **240 minutes**; operator initials (two,
  printed); the spoken name — "Waveform Observatory," recorded
  44.1 kHz/24-bit, duration **1.84s**, mean fundamental **196.00 Hz**,
  its FFT envelope sampled to the 128-point path §6.1 ships. *(b) The
  conversion:* full scale = ±4 divisions; **A(div) = 4 ×
  10^(dBFS ÷ 20)**. *(c) The channels:*

  | CH | Name | Freq | Wave | Timebase | Peak dBFS | Peak div | Transients | Minutes |
  |---|---|---|---|---|---|---|---|---|
  | 01 | The Spoken Name | 196.00 Hz | composite | 1 ms/div | −3.2 | 2.77 | 1 | 12 |
  | 02 | Harbour Hum | 55.00 Hz | sine | 5 ms/div | −11.6 | 1.05 | 38 | 48 |
  | 03 | Switchyard | 440.00 Hz | square | 0.5 ms/div | −6.8 | 1.83 | 96 | 44 |
  | 04 | Sawmill Dawn | 82.41 Hz | sawtooth | 2 ms/div | −8.9 | 1.44 | 57 | 52 |
  | 05 | Shortwave Weather | 7.300 kHz | noise | 0.1 ms/div | −14.3 | 0.77 | 23 | 60 |
  | 06 | The Room Itself | 0.00 Hz | flat | 1 s/div | −61.5 | 0.003 | 3 | 24 |

  *(d) The totals:* minutes 12+48+44+52+60+24 = **240**; transients
  1+38+96+57+23+3 = **218**; session peak **−3.2 dBFS** (CH 01); noise
  floor **−61.5 dBFS** (CH 06); dynamic range −3.2 − (−61.5) =
  **58.3 dB**; headroom to 0 dBFS = **3.2 dB**; clips **0**. Cycles
  visible per channel at its timebase (10-div window): CH 01 1.96,
  CH 02 2.75, CH 03 2.20, CH 04 1.65 — each the frequency × window
  product, printed so the drawn trace can be checked against the
  arithmetic. *(e) The requests:* **1,208** audition requests on file
  before tonight — §6.14's preamble and receipt (№ 1,209) derive from
  this line and no other.
- **Motion spec.** The record itself does not move. Its printings move
  per their own elements (§6.1's envelope at 2.77 div, §6.2's per-channel
  amplitudes, §6.4's stats, §6.12's glyph heights, §6.13's table) — and
  every one of those motions is parameterised from this object at build
  time, never hand-copied into a component.
- **States.** The record has versions, not states: a corrected night
  (a recount, a re-measured peak) increments the record's printing —
  *"Session № 214, second printing"* — and the correction is footnoted
  on the record page with the old figure struck through in the
  annotator's hand, never silently replaced. Corrections in this
  station are errata, not edits (§12's voice rule).
- **Content merge.** This element *is* the content merge, stated as
  data: hero, trace, stats, cards, table, form and footer are seven
  printings of this one object, and the theme is the discipline of
  keeping them identical.
- **Failure fallback.** If the record object fails to load at runtime,
  the page does not improvise: every printing was server-rendered from
  the same object at build, so the page stands complete and the runtime
  merely loses its animations. A build whose record is missing a
  channel field fails §10 and does not ship — the record is the first
  build step (§15), not content to be filled in later.
- **Reduced-motion variant.** Identical — print is print. The record
  page under reduced motion is the same table with the same totals.
- **Performance budget & mobile variant.** The record is ≤4KB of JSON
  and one table; its cost is the discipline, not the bytes. Mobile: the
  record page prints the channels as stacked blocks per §6.13's mobile
  ruling, totals last, conversion stated above them.
- **Choreography timeline (v2).** Build-time only: record declared →
  printings derived → §10 audit re-derives each printing → ship. A
  correction: record re-printed with its footnote → all printings
  re-derived in the same commit → audit re-run.
- **State matrix (v2).** *Rest:* current printing stands. *Hover /
  focus / active:* n/a — the record page's table behaves per §6.13.
  *Scrolled-past:* n/a. *Disabled:* a channel field marked provisional
  prints per §6.13's provisional ruling everywhere it appears.
  *Touch:* as §6.13.
- **Breakpoints (v2).** As §6.13 (the record prints through the table's
  geometry) with the conversion block and totals always above the fold
  of the record page at every size.
- **Edge cases & failure modes (v2).** *A figure that cannot be
  derived* (a marketing number with no measurement behind it): it does
  not enter the record, and therefore does not enter the page — the
  theme would rather print one fewer stat than one unmeasured one,
  and §9 names the unmeasured stat as this theme's original sin.
  *Rounding:* dBFS prints to 0.1, divisions to the table's precision
  (2.77 / 1.05 / 1.83 / 1.44 / 0.77 / 0.003) — divisions are computed
  from the unrounded dBFS and then printed, so a reader re-computing
  from the printed dBFS lands within 0.01 div; §10's audit uses the
  unrounded chain.
- **Accessibility spec (v2).** The record page is a table (§6.13's
  semantics) plus text blocks; the conversion formula prints as text
  ("A in divisions equals 4 times 10 to the power of dBFS over 20") in
  a visually-hidden gloss beside the formula's notation, so the law is
  available to every reader, not only to those who parse notation.
- **Tokens consumed (v2).** `--char`, `--char-2`, `--phosphor`,
  `--paper`, `--paper-dim`, `--red` (the ceiling legend, shared with
  §6.13's footnote — the census counts *printings of the mark*, and
  the record page carries it once).

### 6.18 No signal — the 404 & empty states

- **What & why.** A page that does not exist is, in this room, a
  frequency with nothing on it: a flat line, a readout locked on
  `0.00 Hz`, and the annotator's plain statement — *"No signal on this
  frequency."* — with the way back printed as station links. Empty
  states (a search with no channels, an archive month with no
  sessions) use the same drawing at region scale. It belongs because
  absence is a measurement here too: the 404 is not an error page
  wearing the theme, it is CH 06's lesson applied to the site itself —
  nothing, measured, with the exits lit.
- **Structure.** The full-page form: the fixed canvas holds the trace
  at the floor (its true 0.003-div height, drawn at the loader's
  declared 0.5px floor line, §6.15); a centred readout block prints
  `NO SIGNAL` in station style, the readout `0.00 HZ · −61.5 DBFS ·
  THE FLOOR`, the annotator's line in Grotesk, and three exits as real
  links — *the dial* (home), *the log* (session index), *request a
  recording* (§6.14 — a visitor who arrived on a dead frequency may
  well have a sound in mind). One attempted sweep (§5's line-draw): on
  load, the measurement cursor crosses the band once, slowly, finds no
  peak, and parks — the search performed, the nothing confirmed.
- **Motion spec.** The sweep: 2400ms `--ease-sweep`, once, on load.
  Nothing else moves; the breath (§6.6) is suspended on this page — a
  dead frequency does not breathe, and the stillness is the message.
  Region-scale empty states omit the sweep (a list is not a page) and
  print the flat segment with the statement in place.
- **States.** Searched (sweep running) / confirmed-empty (sweep parked,
  exits at full print) — the exits are fully printed and focusable from
  the first byte; the sweep is ceremony over an already-usable page.
- **Content merge.** The 404's readout prints the *floor's* figures
  from the record (§6.17) — the emptiest real measurement the station
  owns — and its exits are the site's actual stations, not a generic
  "back home" button. Even the dead page is tuned to the dial.
- **Failure fallback.** The page is static HTML with one optional
  canvas ceremony; every fallback (no canvas, no JS, loop dead) leaves
  the identical printed page minus the sweep. There is nothing here
  that can fail into invisibility.
- **Reduced-motion variant.** No sweep: the cursor prints parked at the
  right edge, the state it would have reached. The statement and exits
  are unchanged.
- **Performance budget & mobile variant.** The lightest page on the
  station: no images, no record fetch (its figures are the floor's,
  inlined). Mobile: the readout block stacks, exits at 48px targets,
  sweep unchanged.
- **Choreography timeline (v2).** Load → flat line, exits printed →
  sweep crosses 2400ms, no peak found → cursor parks → confirmed-empty
  → visitor leaves by a lit exit. Nothing loops; nothing waits.
- **State matrix (v2).** *Rest:* confirmed-empty. *Hover:* exits probe
  per §6.7 — even on a dead frequency, attention brightens what little
  signal the exits carry (their glyphs are the live channels').
  *Focus:* exits per §11, in printed order: dial, log, request.
  *Active:* §6.10's transition to the chosen station. *Scrolled-past:*
  the page is one screenful; n/a. *Disabled:* n/a. *Touch:* exits
  ≥48px.
- **Breakpoints (v2).** ≥1200px: readout block centred on the band.
  768–1199px: same, exits in a row of three → wrap to column under
  480px content width. <768px: block left-aligned to the column, exits
  stacked.
- **Edge cases & failure modes (v2).** *A search with results that are
  all log-only channels (§6.12):* not an empty state — the results
  print with their `LOG ONLY` tags; emptiness is reserved for true
  zero. *The 404 reached via §6.10's transition:* the flatline of the
  transition and the flat line of the 404 are the same drawing — the
  visitor arrives already looking at the answer, and the sweep still
  runs to confirm it.
- **Accessibility spec (v2).** The heading is the statement ("No signal
  on this frequency"), not the code; the HTTP status does its own
  work. Exits are links with real names. Contrast: paper on char
  13.3:1 (statement), phosphor 9.8:1 (readout), paper-dim 7.1:1
  (figures). The sweep is `aria-hidden`.
- **Tokens consumed (v2).** `--char`, `--phosphor`, `--paper`,
  `--paper-dim`, `--ease-sweep`, `--dur-sweep-404` (2400ms).


## 7. Page application map

- **Home (the Night Log page).** The full session in order: hero (§6.1),
  the peak-read stats (§6.4), the six channels as sections riding the
  morph (§6.2) with their readouts (§6.5), the channel cards (§6.12) as
  the index stretch, the log table (§6.13), the request form (§6.14),
  the footer (§6.16). This is the reference build §8 walks through.
- **Channel detail page.** One channel, deep: its trace character owns
  the whole page's morph (a one-station spool), its peaks get a
  dedicated cursor stretch (§6.3), its scope-frame photographs (§6.9)
  and its full log row expanded into prose. The dial (§6.11) marks it
  current throughout.
- **Session index / archive.** Cards (§6.12) per session, each grid
  headed by its own totals; past sessions print their records in the
  table's geometry (§6.13). A month with no sessions is §6.18's empty
  state at region scale.
- **The record page.** §6.17 printed in full: the conversion, the
  channel table, the totals with their derivations, the errata
  footnotes of any second printing. The least decorated page on the
  station, deliberately — it is the page the other pages are checked
  against.
- **About / the station.** The bench, the hydrophones, the operators:
  scope-frame images (§6.9) and Grotesk prose on panels; the morph runs
  CH 02's sine throughout (the station's resting hum) — an about page
  does not get its own frequency, because it is about the listener, not
  a sound.
- **Request / contact.** §6.14's form as a full page, preceded by the
  record's request line and a short list of recent logged requests
  (numbers and places only — the log's public face).
- **Search.** Results as log rows (§6.13's geometry, compressed); zero
  results is §6.18's region state with the query printed as the
  frequency that was tried: *"No signal on 'harbour, dawn'."*
- **Checkout.** Refused (§1). If the station sells recordings, the
  catalogue lives in this theme and the transaction hands off to a
  neutral checkout off-theme, linked plainly as *"the shop's till"* —
  the instrument does not take money, and pretending otherwise would
  cost the room its credibility for a cart's sake.

## 8. Worked examples

### 8.1 The hero — the name, spoken once (worked example 1)

The visitor arrives. The screen is charcoal, the graticule printed, the
masthead's dial unlit. The band at the measurement line is flat — not
empty, *flat*: the floor, at its declared half-pixel (§6.15), because
the record and the display font are still resolving. The caption corner
reads `ACQUIRING`. At t≈300ms both have landed; the caption clears.
Now the held breath: 600ms of true silence, the headline present but
defocused, printed at rest size — a visitor who screenshots this moment
has a legible page, because the fallback *is* the design (§6.1). At
t=600 the name strikes. The envelope — the real FFT shape of
"Waveform Observatory," its two-word syllable bumps visible as two
swell groups — overshoots to 118% and rings down; the Unbounded letters
inside the clip swell with it; the beam-focus resolves. The peak of the
second word's swell is the tallest thing on the screen, and beside it
the scale's phosphor figure reads `−3.2 DBFS` — the session peak, earned
in the first two seconds. The caption prints last: *"The name, spoken
once. Envelope from its FFT — Session № 214, CH 01."* The dial warms,
entry by entry. The visitor scrolls; the composite envelope spools into
CH 02's sine and the night begins. Total elapsed theatre: under two
seconds, every millisecond of it a measurement or a disclosed convention.

### 8.2 Mid-page — reading the Switchyard (worked example 2)

CH 03's stretch. The morph has been crossfading through the silence
above the section — sawtooth's ancestor sine rounding, then sharpening
— and by the time the channel's panel crosses the measurement line the
band is pure square wave at 1.83 divisions, edges softened exactly as a
real 440 Hz square wave softens on a bench scope. The readout strip
sweeps: figures flickering upward in CH 03's seeded pattern, locking at
`440.00 Hz` with the overshoot settle; `PEAK −6.8 DBFS` and `0.5 MS/DIV`
print beside it. The visitor reads the panel — what a switchyard is,
why the station logs it — while the measurement cursor travels the
stretch at sweep velocity, the printed time beneath it spooling through
the channel's 44 minutes. At 41% the cursor dwells: CH 03's loudest
logged transient, a shunting impact at minute 18, prints its chip —
`−6.8 DBFS · 440 HZ · MIN 18` — and holds. The visitor hovers the
paragraph's card; the band beside it brightens ±40% in square character
(§6.7), and a click answers with one square blip (§6.8). They scroll
on; the square wave's edges begin to lean, and by the next silence the
band is sawtooth. Nothing in the section moved except the instruments.

### 8.3 Conversion — a request enters the log (worked example 3)

The form section rides CH 01's stretch — requests enter through the
station's own channel, so the band behind the form is the spoken-name
envelope, breathing (§6.6). The preamble has already made the promise:
*"1,208 requests on file. Yours will be № 1,209."* The visitor writes —
name, the place (a stairwell in Karachi), the sound ("the lift's cable
hum, just before the doors") — each field focus gathering the probe at
its edge (§6.7). On submit, a blip fires in the envelope's character
from the button; the form dims to 60%; the button's flat-line pulse
runs. 700ms later the entry prints where the form stood: the visitor's
words, set as a log line, and at t=300 into the print the stamp lands —
`REQUEST № 1,209 — LOGGED`, phosphor-ruled, two degrees off square.
The live region speaks the number once. The band's envelope swells a
single ±3% breath — the room acknowledging a new sound to listen for —
and settles. The visitor leaves with a number that §6.17's record can
prove: there were 1,208, and now there is one more.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The decorative squiggle.** A hero waveform drawn by a designer
   "because it looked nice" is the theme's founding lie. Cure: the
   envelope is the spoken name's FFT, shipped as data, captioned as
   such (§6.1); §10 fails any build whose envelope path is not the
   record's.
2. **Levels that don't add up.** A trace drawn taller in the hero than
   its channel's logged peak "for impact." Cure: the conversion
   (§6.17) is applied by the build, not eyeballed; §10 re-derives every
   printed division figure.
3. **Red as a vibe.** Signal red on buttons, badges or hover states.
   Cure: the census (§2) — two printings, both the ceiling. A red CTA
   in this theme is a fire alarm used as a doorbell.
4. **The endless flicker.** A readout sweep that never locks, a CRT
   flicker at full opacity over text. Cure: every flicker is seeded,
   ≤700ms, and watchdogged to a printed lock (§6.5); grain stays ≤3%
   (§5).
5. **Glow soup.** Phosphor bloom filters on every element until the
   page is a neon sign. Cure: the trace is a 2px line; glow exists
   only as the beam's own softness in the hero envelope. Panels are
   flat charcoal. A scope is not a casino.
6. **Fake precision.** Readouts like `440.000000 Hz` or dB to three
   decimals — precision theatre over unmeasured content. Cure: §3's
   grain rules (Hz to two decimals, dB to one) and §6.17's refusal to
   admit an unmeasured figure.
7. **The hidden-content reveal.** Sections that fade in from
   `opacity: 0` on scroll and strand blank when JS fails. Cure: the
   standing rule — print is the shipped state; reveals are performances
   over it (§6.4's discipline everywhere).
8. **Silence as leftover.** Treating the quiet stretches as padding to
   be filled with badges, banners or a newsletter strip. Cure: §4's
   silence budget is a build requirement; a section that fills its
   silence fails review like a wrong figure.
9. **Generic dark-tech styling.** Cyan gradients, glassmorphism,
   floating orbs — the "audio startup" costume. Cure: this palette has
   no cyan and no gradients on panels (§2); the room is charcoal,
   phosphor and paper, and it can prove every colour's job.
10. **The marquee of urgency.** "LISTEN NOW" tickers, countdowns to a
    drop. Cure: refused in §5 by name; the station's only urgency is a
    transient, and transients are the world's, not the marketing
    department's.
11. **Cropped photographs in uniform frames.** Every image forced to
    16:9 for grid neatness. Cure: §6.9 fits the frame to the image; a
    scope is fitted to its signal.
12. **A cursor with a trail.** A phosphor comet following the pointer
    "because oscilloscope." Cure: standing rule — the pointer is the
    probe's handle; the *trace* answers (§6.7), the cursor stays the
    system's.

## 10. Quality gate

Blocking checks; every one must pass before this theme ships in a build.

1. **Figure audit.** Every printed number on the page is re-derived
   from §6.17's record by a non-builder: minutes sum to 240,
   transients to 218, range 58.3, headroom 3.2, form number 1,209.
2. **Division audit.** Each channel's printed division figure matches
   `4 × 10^(dBFS ÷ 20)` from its unrounded dBFS within 0.01 div;
   glyph heights in §6.12 are re-measured against the peaks.
3. **Red census.** `grep` the build for the red token: exactly the
   licensed printings (§2, §6.13/§6.17's legend) and no more.
4. **Envelope provenance.** The hero envelope path is byte-identical to
   the record's 128-point FFT sample; the caption's claim is true.
5. **Watchdog drill.** With the loop killed mid-visit, every element
   reaches its printed state within its watchdog ceiling (2000 / 1500 /
   1400 / 1200 / 4000ms per element) — no invisible content, no endless
   flicker, no stranded skeleton.
6. **No-JS pass.** The full page read with JavaScript disabled: every
   figure, table row, form and exit usable; static traces in character.
7. **Reduced-motion pass.** The full page under
   `prefers-reduced-motion`: no morph, no sweep, no breath, no count —
   and every reading still taken (locks, pins, confirmations all occur
   as state changes).
8. **Lock audit.** Every readout locks within its watchdog; CH 06's
   falls to 0.00; no readout on the page is found mid-sweep after 2s.
9. **Silence budget.** Each channel section carries ≥24vh of
   print-free graticule before its panel (§4); measured, not eyeballed.
10. **Unbounded ration.** At most two Unbounded settings in the page's
    CSS (§3, law 1).
11. **Contrast spot-check.** Body text 13.3:1, readouts 9.8:1, labels
    7.1:1 — sampled from the built page, not the token table.
12. **Ambient census.** Exactly two ambient loops running (§5): breath
    and grain. A third is a fail, however subtle.
13. **Gate signed by a non-builder** — the record's auditor, per §15.

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components the theme refuses are listed with their replacement — an
inventory that only lists what exists hides the discipline.

- **Buttons.** Primary: phosphor text on `--char-2`, 1px `--grid`
  rule, mono uppercase 0.8125rem; on hover the rule brightens to
  phosphor and §6.8's blip answers the press. No filled phosphor
  button exists — the beam is not a paint. Secondary: paper text,
  no rule until hover.
- **Inputs.** §6.14's pattern: `--char-2` ground, paper text, label in
  station style above, focus = 2px paper outline + edge probe.
- **Selects / textareas.** Same ground and rules; the select's chevron
  is a small mono `▾` in paper-dim, never a drawn icon.
- **Tables.** §6.13 exactly; sortable columns announce their sort in
  the header's mono (`FREQ ↑`) and never animate rows.
- **Cards.** §6.12's bench tags. No other card species exists.
- **Badges / tags.** Printed as log annotations: mono uppercase in a
  `--grid` rule box (`LOG ONLY`, `PROVISIONAL`, `OFF AIR`) — a badge
  here is a stamp in the margin, never a coloured pill.
- **Alerts.** A log note, full-width, paper text on `--char-2` with a
  phosphor caret: the station reports; it does not shout. Red alerts
  do not exist (§2); a genuinely over-range event is reported in the
  log table, in figures.
- **Pagination.** Printed as a dial strip: `‹ CH 01–06 › · PAGE 2 OF 5`
  in mono, numbers as links; no infinite scroll — a log has pages.
- **Modal.** Refused. Anything modal in this world is a dedicated
  channel (its own page) or a log note inline; a dialogue box floating
  over the trace would be a second instrument in the room.
- **Toast.** Refused. Confirmations are log entries (§6.14) that stay
  printed where they happened; a message that vanishes was never
  logged.
- **Tabs.** Refused. Channels are navigated by the dial (§6.11) and
  read by scrolling; a tab strip would be a second tuner competing
  with the first.
- **Accordion.** Permitted once, for the record page's errata and
  derivations: rows open with a 240ms `--ease-settle` height change,
  headers in station style, one open at a time — a log's appendix, not
  a navigation system.
- **Breadcrumbs.** Printed as a tuning path in mono: `DIAL / CH 03 /
  SWITCHYARD` — where you are on the dial, not a file path.
- **Progress.** §6.3's cursor only. Bars, spinners and percentage
  counters are refused by name (§5).
- **Search field.** An input per the input pattern, its submit labelled
  `TUNE`; results per §7; the empty result is §6.18's region state.
- **Links.** Paper, underlined with a `--grid` rule that lifts to
  phosphor on hover; visited links dim to paper-dim — the log
  remembers where you've been.
- **Focus indicator.** 2px `--paper` outline, 3px offset, everywhere,
  no exceptions — the one piece of chrome the station standardises
  across every component above.

## 12. Content & copywriting voice

Two registers, never blended. **The Instrument** (JetBrains Mono,
uppercase, units always attached) prints measurements and nothing else:
`CH 03 · SQUARE · 440.00 HZ · PEAK −6.8 DBFS`. It does not persuade,
welcome or apologise; a readout that says "Oops!" has been written by
someone who has never trusted an instrument. **The Annotator** (Space
Grotesk, sentence case) is the person at the bench: dry, exact, quietly
funny at the world's expense, never at the visitor's. Headlines are the
annotator naming what the channel *is* — "Switchyard", "The Room
Itself" — never what it does for your brand.

- **Headline style.** Names, not slogans. ✓ "Sawmill Dawn" ✗ "Rise and
  grind with the sounds of industry!" If a headline contains an
  exclamation mark, it is wrong; the station's one licensed exclamation
  in history is not yours to reuse.
- **Label style.** Instrument register, terse, units attached:
  ✓ `MINUTES ON AIR` ✗ `Total listening time (approx.)`. Approximate is
  a confession; if the figure is approximate, the annotator says why in
  a sentence, and the instrument prints the figure it has.
- **Error voice.** The log corrects without blame and without red:
  ✓ "The log needs the sound in your words — even three will do."
  ✗ "Error: description is a required field." Every error names the
  fix in the visitor's vocabulary, not the schema's.
- **Empty-state voice.** A measurement, then the exits: ✓ "No signal on
  this frequency." (§6.18) ✗ "Oops! Nothing here." The word "oops" is
  banned station-wide; nothing here is an accident, including absence.
- **Confirmation voice.** Numbered and kept: ✓ "Request № 1,209 —
  logged." ✗ "Thanks! We've received your request 🎉" — no emoji, no
  confetti; the log's receipt is the celebration.
- **Fixed strings** (verbatim, never paraphrased): the CH 06 line
  `NOTHING, MEASURED.`; the sign-off `END OF SESSION № 214 — THE
  STATION KEEPS LISTENING.`; the loader's disclosure *"floor drawn at
  half a pixel — the real floor is lower."*; the transient disclosure
  of §6.6. These are the station's liturgy; a build that rewords them
  has changed stations.

## 13. Full-page scroll choreography map

The home page, top to footer, as one continuous measurement. (Per-element
timings live in §6; this map is the order of events and what the visitor
feels.)

1. **Arrival.** Acquiring → silence → the name erupts (§8.1). Feeling:
   a room powering up, then holding its breath, then speaking once.
2. **The dial warms.** Six stations light in sequence; CH 01 marked.
   The visitor now owns a map of the night.
3. **First scroll.** The composite envelope spools; phase advances; the
   trace becomes CH 02's sine as the stats stretch approaches.
4. **The readings.** The cursor travels the stats stretch; four peaks
   dwell, four numbers count and pin (§6.4). Feeling: being shown the
   night's evidence by someone who trusts it.
5. **CH 02 — Harbour Hum.** Readout locks at 55.00 Hz falling *up* from
   zero; the panel reads over a breathing sine; the harbour photograph
   seats in its frame with one flicker.
6. **The silences between channels.** Each inter-channel stretch: morph
   crossfade in the middle 30%, idle breath if the visitor lingers.
   The quiet is paced, not padded.
7. **CH 03 — Switchyard.** Square lock at 440.00; the minute-18
   transient dwells under the cursor (§8.2); probes and blips answer in
   square character.
8. **CH 04 — Sawmill Dawn.** Sawtooth; the readout sweeps to 82.41 —
   the slowest lock on the page, because the dial travels furthest in
   feel. A scope-frame image of the mill seats.
9. **CH 05 — Shortwave Weather.** Noise; the readout reprints as
   `7.300 KHZ` at lock; the band's noise is the seeded loop of the
   record, so two visitors argue about the same static.
10. **CH 06 — The Room Itself.** The readout *falls* to 0.00 over
    900ms; the band flattens to the floor; the section is mostly
    silence with one short panel — the night's quietest room, and the
    page's bravest section. `NOTHING, MEASURED.`
11. **The index.** Channel cards print in stagger; the grid header's
    totals hang over six glyphs of honestly different heights.
12. **The log.** The table, at rest, performing nothing. Visitors who
    skimmed everything above stop here and check it. It agrees.
13. **The request.** CH 01's envelope returns behind the form; the
    promise of № 1,209; the stamp lands (§8.3).
14. **Sign-off.** The trace eases to the floor, one last floor-spike,
    the totals a third time, the standing line. The visitor leaves a
    room that is still listening.

## 14. Whole-page performance budget

- **Total page weight (home):** ≤820KB compressed, of which: HTML/CSS
  ≤120KB, JS ≤90KB gz (the loop, the morph, the form — no framework on
  the trace path), fonts ≤150KB (three families, subsetted; Unbounded
  is display-rationed so its subset is small), images ≤400KB across the
  page (scope frames at ≤180KB each, §6.9), the record + envelope data
  ≤12KB.
- **Frame budget.** The shared loop's canvas pass ≤0.9ms/frame at
  1440px wide, DPR ≤1.5; total main-thread animation work ≤1.6ms/frame;
  no long task >50ms during scroll; the loop must hold 60fps on a
  mid-range 2021 laptop with the probe active and a blip live.
- **Cut order** (when the budget is exceeded, cut in this order, never
  skip ahead): (1) CRT grain shimmer; (2) trace frame rate halves to
  30fps (the morph is slow; nobody can tell, and §10 measures that
  claim); (3) noise character switches to its pre-rendered loop at all
  sizes; (4) probe falloff radius shrinks to 110px; (5) card tilt
  disabled (probe remains).
- **Never cut:** the watchdogs, the printed fallbacks, the reduced-motion
  variants, the record's data, the focus outlines. A build that buys
  its frame rate with its fallbacks has bought a different, worse theme.
- **Print budget.** The print stylesheet (§2) must produce the log
  table, the record and all body text legibly on A4 with the trace as a
  single ink line per section — the archive copy is a deliverable, not
  an afterthought.

## 15. Build-order checklist

1. **Declare the record (§6.17) first** — session, channels, conversion,
   totals, request count. No component is built before its figures
   exist.
2. Server-render every printing from the record: hero envelope + scale,
   stats, readouts, cards, table, form preamble, footer totals.
3. Verify the no-JS page end-to-end (§10, check 6) before any script is
   written.
4. Lay the graticule and the layout system (§4): divisions, silences,
   panels, the measurement line.
5. Build the static-SVG fallback traces per section (character +
   logged amplitude) — the reduced-motion and no-canvas rendering.
6. Wire the shared loop: scroll lerp, morph map from DOM offsets (§6.2).
7. Add the measurement cursor and peak chips (§6.3), then the peak-read
   stats' counts (§6.4) on its dwells.
8. Add station-lock sweeps (§6.5) with their watchdogs.
9. Add idle behaviour (§6.6): breath blend, seeded spikes, the
   disclosure caption.
10. Add probe (§6.7) and blips (§6.8) on the shared pass.
11. Frames (§6.9), transition (§6.10), masthead scrollspy (§6.11).
12. The form (§6.14) with its watchdog and idempotent token; the loader
    (§6.15); the footer gesture (§6.16); the 404 (§6.18).
13. Reduced-motion pass across every element; verify §10 check 7.
14. Run the full quality gate (§10), signed by a non-builder.
15. Ship only on a signed gate. A failed check returns the build to the
    step that owns it — figure failures to step 1, always.

