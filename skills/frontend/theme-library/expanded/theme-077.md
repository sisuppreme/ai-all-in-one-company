# 77. The Listening Dish — Expanded (v1 + v2)

## 1. Concept & world

A radio-telescope station at night, listening. Not observing, not
broadcasting — *listening*, which is a different posture: the dish is
turned toward a patch of sky and held there for hours while the
universe decides whether to say anything. The site is built in that
posture. Vast quiet layouts. One enormous dish. Meaning that arrives
as a faint signal you have to lean toward. Nothing on the page shouts,
nothing performs, and the single joke the page permits itself is
buried in the footer log, where it belongs.

**The theme's one law: faint is a state, never a fate.** Anything the
page shows faint — blurred, dimmed, unresolved — is on a published
journey to full sharpness with a guaranteed arrival: every focus-in
completes within 6 seconds of its trigger, the hero headline is fully
tuned by 6 seconds after load whether or not its pulses fire, and the
no-JavaScript page ships with every word already sharp. Faintness is
this theme's suspense; it is never permitted to become a hiding place.
Every other rule in this document is that law wearing a uniform.

**The world in one paragraph.** It is always night at the station —
not night as a colour scheme but night as a working condition. The
desert around the array is `#101216` because that is what a desert
looks like at 2 a.m. The dish is bone-white because moonlight and
sodium-free darkness leave it that colour. The one warm colour, signal
thread `#E0A458`, is the colour of a signal on a scope and of nothing
else. Control-room red `#A63D2F` appears only where a real control
room would use it — a recording dot, a warning stamp — because red
light is what you use when you must not destroy anyone's night vision.
The page's clock is not the visitor's clock: the station runs on
integration time and local sidereal time, and both are printed.

**Best-fit sites and audiences.**

- SETI institutes and radio-astronomy observatories publishing their
  programmes, targets and observing requests.
- Deep-tech research labs (fusion, quantum sensing, gravitational-wave
  groups) whose real product is patience and precision, and whose
  audience — funders, collaborators, graduate students — reads
  restraint as competence.
- Space-agency programme pages, array visitor centres, and
  citizen-science listening projects that take proposals from the
  public.
- Any organisation whose honest claim is "we are very good at waiting
  for something faint" — the theme fails the moment the claim is
  louder than that.

**When NOT to use it.**

- Anything that must convert in the first screen: commerce, sign-up
  funnels, event sales. The theme's first screen deliberately resolves
  over ~6 seconds; a checkout built on it would be malpractice.
- News, listings or dashboards with dense mid-size information. The
  type system (§3) forbids the entire middle register; a page that
  needs 1.4rem body copy with bold subheads cannot live here.
- Brands whose voice is warm, chatty or exclamatory. The copy rules
  (§12) ban exclamation marks outright; if the client needs one, this
  is not their theme.
- Daylight products. There is no light scheme (§2); a "day mode"
  request ends the engagement with this theme, politely.

**The emotional contract.** The visitor is treated as a colleague on
the night shift: trusted with real coordinates, real frequencies and
unresolved results. The page never pretends a signal was found. Its
strongest number (§6.6) sits *below* its own confirmation line for the
entire visit, and says so. That honesty is the brand.

## 2. Palette

Five anchors from the original entry, held exactly, plus six derived
tokens for surfaces and hairlines. All contrast ratios below were
measured for this expansion from the hex values (WCAG relative
luminance) against `--night-desert`, the page ground.

| Token | Hex | Role | Ratio on night | Usage share | Pairing rules |
|---|---|---|---|---|---|
| `--night-desert` | `#101216` | Page ground; the desert at 2 a.m. | — | ~78% | Everything sits on it; never used as text |
| `--dish-bone` | `#E3DED2` | Display type, dish fill, primary text | 14.0:1 | ~12% | The only colour allowed at display size; primary reading colour |
| `--signal-thread` | `#E0A458` | The signal: trace, ticks, locks, links, the one warm accent | 8.6:1 | ~3% | Text-legal at any size; rationed — see census below |
| `--star-grey` | `#7A8191` | Whisper labels, coordinates at rest, secondary log text | 4.8:1 | ~5% | Labels and secondary text only; never the sole carrier of a fact a visitor must act on |
| `--control-red` | `#A63D2F` | Dark-adapted accents: recording dot, warning stamp, form error rule | 3.0:1 | <0.5% | **Never text.** Graphical markers only, always paired with a mono label |
| `--night-deep` | `#0B0D10` | Page edge, footer well, vignette behind the dish | — | ~8% | Depth cue only; text on it uses bone at 14.9:1 |
| `--night-panel` | `#17191E` | Card and table surfaces, one step above the desert | — | ~6% | Separated from ground by a `--grey-faint` hairline, never by shadow |
| `--bone-dim` | `#B7B1A2` | Standfirsts, card body, log prose | 8.8:1 | ~4% | The reading grey-beige; body copy lives here or in bone |
| `--thread-pale` | `#F2CD96` | Pulse core, the locked digit flash, hover-lit thread | 12.5:1 | <0.5% | Only inside a pulse or a lock event; never a resting colour |
| `--thread-dim` | `#8F6C38` | Thread at rest: hairline rules under headings, the log's thread line | 3.9:1 | ~1% | Graphical only; a resting rule may be dim, a resting word may not |
| `--grey-faint` | `#4A505C` | Hairlines, table rules, mesh lines at rest, card borders | 2.3:1 | ~1% | Structure only; carries no information alone |

**The thread census.** Signal thread is the page's only warmth and is
rationed like it: at any scroll position, at most **four** thread-
coloured objects may be in the viewport — typically the trace, the
current pointing's tick, one link or lock indicator, and one spare.
`--thread-pale` exists only during an event (a pulse, a lock) and must
decay back to `--signal-thread` or `--thread-dim` within the event's
own duration. A page that glows amber everywhere has mistaken the
signal for the station.

**The red discipline.** Control-room red is dark-adapted light: it
exists so the eye keeps its night vision. It marks exactly three
things — the recording dot in the status strip (§6.14), the
`BELOW CONFIRMATION` stamp beside the SNR counter (§6.6), and the
error rule on the proposal form (§6.15) — always beside a mono text
label, never as the label. Any fourth use is a defect (§9).

**Dark-mode behaviour.** There is none, by ruling. The theme *is* the
dark; a light scheme would be a photograph of the station at noon,
which is a different site for a different theme. `color-scheme: dark`
is declared so form controls and scrollbars render honestly. If the
visitor's OS forces a light inversion, the printed page still reads —
bone and thread both hold on white at 1.4:1 and 2.2:1, which is to say
badly — and the theme accepts this rather than pretend a day shift
exists; the quality gate (§10) does not test it.

## 3. Typography

Two families, two registers, and a forbidden band between them. This
is the theme's strictest discipline and the first thing a careless
build breaks.

**Families.**

- **Instrument Serif** — display only. A quiet, high-contrast serif
  with an instrument-maker's restraint; set huge and given room. Never
  bolded (the family ships one weight and the theme forbids
  synthesising another), never tracked tight, never set below 3rem.
- **IBM Plex Mono** — everything else: labels, readouts, coordinates,
  body prose, tables, forms, the log. The station's paperwork voice.
  Tabular figures always (`font-variant-numeric: tabular-nums`) —
  a readout whose digits change width while it slews is a broken
  instrument.

**The two registers and the dead band.**

| Register | Family | Sizes | Used for |
|---|---|---|---|
| Display | Instrument Serif | 3rem – 10rem (fluid, see scale) | Hero headline, pointing names, section statements, the 404 |
| Log | IBM Plex Mono | 0.6875rem – 1rem | Labels, readouts, coordinates, body prose, tables, forms, buttons, the footer log |

**No text may be set between 1.0625rem and 2.9375rem.** That band —
where ordinary websites keep their subheads and lead paragraphs — is
the theme's dead air. A build that needs it has the wrong content:
either the sentence is a statement (promote it to Display) or it is
paperwork (demote it to Log). The quality gate greps the compiled CSS
for font-sizes in the band (§10).

**Type scale.**

| Role | Size | Line-height | Tracking | Case |
|---|---|---|---|---|
| Hero headline | clamp(4.5rem, 11vw, 10rem) | 0.98 | −0.01em | Sentence case, as written |
| Pointing name | clamp(3rem, 6vw, 5.5rem) | 1.02 | −0.005em | Sentence case |
| Section statement | clamp(3rem, 4.5vw, 4.25rem) | 1.05 | 0 | Sentence case |
| Standfirst (Log, bone) | 1rem | 1.7 | 0 | Sentence case |
| Body / log prose | 0.875rem | 1.75 | 0 | Sentence case |
| Readout (coordinates, counters) | 0.8125rem | 1.5 | 0.04em | As printed by the instrument |
| Label / whisper | 0.6875rem | 1.45 | 0.14em | UPPERCASE, always |
| Table cell | 0.8125rem | 1.55 | 0.02em | Mixed per column |

**Five type laws.**

1. **Coordinates are headings.** Every pointing is introduced by its
   RA/Dec in Log register *above* its serif name — the instrument
   speaks first, the poetry second (§6.2).
2. **Numerals are mono, always.** No serif figure appears anywhere on
   the page, including inside display lines: a year or a count inside
   a headline is set in IBM Plex Mono at 0.32em, baseline-aligned —
   the instrument interrupting the statement, deliberately.
3. **Whispers stay whispers.** Labels are 0.6875rem uppercase at
   0.14em tracking in `--star-grey`; making a label bigger to "help"
   it is the theme's most common act of vandalism (§9).
4. **Serif never carries data.** If a number must be believed, it is
   mono. If a sentence must be felt, it is serif. The registers never
   swap jobs.
5. **Nothing is ever bold.** Emphasis is achieved by register change
   (grey → bone, dim → thread), by position, or not at all.
   `font-weight` above 500 does not exist in this theme.

## 4. Layout language

**The stage.** The page is a desert floor with one instrument on it.
The dish (§6.1) is drawn at `60vw` (capped at 880px, floored at 340px)
and anchored centre-frame in the hero; through the pointings act it
stays in view as a sticky stage (§5) while the pointings pass around
it. Everything else is arranged the way a night crew arranges itself
around a dish: sparsely, at a respectful distance, with the paperwork
at the edges.

**Grid and measure.**

- One column, centred, max measure 72rem for the stage; text measures
  are far narrower — Log prose at 56ch, standfirsts at 44ch. The
  desert is the margin: at ≥1200px, at least 34% of the viewport width
  is empty night on each side of the text measure.
- Pointings are **offset, alternating**: odd pointings sit left of the
  dish's axis, even pointings right, each with its coordinate block
  (§6.2) on the dish side — the text leans toward the instrument that
  is aimed at it. On <1200px the alternation collapses to a single
  left-aligned column and the dish becomes a header object per act,
  not a sticky stage.
- The hero's base carries a horizon hairline (`--grey-faint`) — the
  desert floor — along which the noise trace (§6.4) runs. Below the
  horizon, the page is paperwork: pointings, tables, forms, log.

**Spacing rhythm.** Vertical space is measured in *integrations*, not
pixels: the gap between pointings is 24vh minimum, between a pointing
and its neighbour sections 16vh, inside a pointing 1.5rem–4rem. A
section may never be closer than 12vh to the next — crowding is the
visual form of shouting. Whitespace here is not emptiness; it is the
silence the station works in, and it is budgeted like a material:
a build that "tightens up" the page has removed its subject.

**Density rules.**

- One idea per pointing, one pointing per screen (at 100vh a pointing
  section is 110–160vh tall including its air).
- At most one Display statement per viewport; at most one table or
  form per act.
- The footer log (§6.18) is the only dense element on the page, and it
  earns the right by being a record, not a design.

**The Schedule — the page's one record.** Every coordinate,
frequency, angle and count printed anywhere on the page derives from
a single declared data object, the night's pointing schedule,
published in the page (as a `<script type="application/json">` block
and as the printed table in §6.13's neighbourhood). The reference
night used throughout this document:

| ID | Target | RA (J2000) | Dec (J2000) | Band | Stage aim (rot / tilt) | Integration target |
|---|---|---|---|---|---|---|
| P-01 | Tau Ceti | 01h 44m 04.08s | −15° 56′ 13.9″ | 1,420.406 MHz (H) | −6° / +3° | 4 h |
| P-02 | Kepler-186f | 19h 54m 36.65s | +43° 57′ 18.1″ | 1,665.402 MHz (OH) | +4° / +6° | 6 h |
| P-03 | Sagittarius A* | 17h 45m 40.04s | −29° 00′ 28.1″ | 1,612.231 MHz (OH) | +8° / +2° | 2 h |
| P-04 | TRAPPIST-1 | 23h 05m 52.36s | −05° 02′ 36.0″ | 1,420.406 MHz (H) | −3° / +7° | 8 h |
| P-05 | The Wow! field | 19h 25m 31s ± | −26° 57′ ± | 1,420.456 MHz (see note) | +6° / +4° | 3 h |

Programme total: **23 h** of integration across five pointings. The
Wow! field's coordinates and frequency are printed with their real
uncertainty — two candidate positions and the 1,420.356/1,420.456 MHz
ambiguity are stated in its pointing (§8) rather than smoothed over;
the schedule is a scientific document, not a poster. The dish's parked
position (hero rest, footer) is rot 0° / tilt 0°. Stage aim angles are
the dish *drawing's* aim, a stylised instrument space of ±8° — they
are not sky azimuth, and the page never claims they are.

## 5. Full motion system

**One loop, one cause.** All scroll-driven and ambient motion runs on
a single `requestAnimationFrame` loop. Scroll position is read once
per frame and smoothed into channel values; nothing listens to scroll
events directly. Per-channel lerp rates: scroll channel `0.08`, dish
channel `0.055` (the dish is heavy; its lag *is* the design — at
60fps it settles to 99% of a new aim in ≈1.37s, matching the original
entry's ~1.4s), trace and counters are functions of elapsed time, not
of the lerp. When the tab is hidden or the relevant act is off-screen,
the loop unregisters channels rather than idling them.

**Named easings** (the station's own; no other easing may appear):

| Token | Curve | Used for |
|---|---|---|
| `--ease-slew` | cubic-bezier(0.22, 0.61, 0.21, 1) | Dish re-aim tweens, re-pointing transition |
| `--ease-settle` | cubic-bezier(0.17, 0.67, 0.24, 1) | Readout digit locks, counter arrivals |
| `--ease-focus` | cubic-bezier(0.33, 0.00, 0.20, 1) | Focus-in reveals, lean-in, mesh-frame focus |
| `--ease-pulse` | cubic-bezier(0.16, 1.00, 0.30, 1) | Pulse blips and rings — fast attack, long decay |
| `--ease-drift` | linear | The noise trace's crawl, the horizon shimmer |

**Every motion term, in this theme's language:**

| Term | The Listening Dish form | Where |
|---|---|---|
| Scroll-triggered reveals | Focus-in: blur(2px) + 70% contrast → sharp, no translation, no fade-up | §6.5 |
| Scroll-driven / scrubbed | The dish re-aims continuously against lerped scroll through the pointings act | §6.1 |
| Parallax | Three night depths: star field ×0.00 (perfectly still), dish mesh ×0.06, desert shadow ×0.12 | §6.10 |
| Pinned sections | The dish stage pins (sticky) for the five pointings; one pointing (P-03) holds an extra 40vh while its readout completes | §6.1, §13 |
| Smooth scrolling | Native scroll, lerped read; no scroll-jacking, no virtual scroll — the desert is scrolled honestly | §5 |
| Progress indicator | Refused as a bar. Progress is the readout's lock state and the integration clock; a bar is a promise and the station promises only resolution | §6.2, §6.6 |
| Staggered reveals | The readout's digits lock left-to-right; log rows append one at a time. No other staggering exists | §6.2, §6.18 |
| Masked line reveals | **Refused.** A mask is a curtain; the station has no curtains. Lines resolve by focus instead | §6.5 |
| Kinetic typography | **Refused,** except the headline's tuning (§6.3) — type here does not perform, it resolves | §6.3 |
| Marquee | **Refused.** A marquee is shouting across the desert. The page's only travelling line is the trace | §6.4 |
| Counters | Reluctant counters: integration clock and SNR, creeping at published rates, stopping below the confirmation line | §6.6 |
| SVG line-draw | The trace draws itself continuously; the log's thread line extends one blip per recorded pulse | §6.4, §6.18 |
| Image scale-in-frame | Photographs focus 1.04 → 1 inside dish-mesh frames as they enter the aim | §6.9 |
| Hover / micro-interactions | Lean-in proximity focus (§6.7); click-to-send pulse (§6.8). No magnetic pull — a dish does not lean toward a visitor; the visitor leans toward it | §6.7, §6.8 |
| Custom cursor | **Refused.** Normal system cursor only; the pointer is a visitor, not an instrument | — |
| Skeleton loading | "Acquiring" state: the destination printed at 70% contrast under an idling trace, ceiling 1200ms | §6.16 |
| Page transitions | Re-pointing: dish slews to parked, trace sweeps once, new page resolves by focus | §6.16 |
| Ambient loops | Exactly two licensed: the noise trace (§6.4) and the counters (§6.6). The star field is the anti-loop (§6.10) | §6.4, §6.6, §6.10 |
| Reduced motion | Station fully lit and focused, every pointing printed, dish parked at each pointing's aim as a static rotation, trace a printed line | per element |

**The 6-second guarantee (the law, mechanised).** Three watchdogs
enforce §1's law: (1) a global timer at 6000ms after load adds
`.tuned` to the document, forcing the headline and every armed
pre-state to its resolved end state; (2) each focus-in element carries
a 6000ms watchdog from first entering the viewport — if its reveal
has not completed, it is snapped sharp; (3) the re-pointing transition
and the acquiring state carry 1200ms ceilings (§6.16). A watchdog
firing is logged to the console as an instrument fault, never shown
to the visitor as an error — the visitor simply sees a sharp page,
which is what they were owed.

**Trigger discipline.** Time-based elements (pulses, counters) run on
elapsed wall-clock from a single `performance.now()` origin, so a
backgrounded tab returns to a page whose clocks are *true*, not
paused-and-wrong. Scroll-based elements read only the lerped channel.
Nothing in the theme uses `setInterval` shorter than 1000ms except
the trace's own draw, which is the rAF loop itself.

## 6. Signature elements

### 6.1 The enormous dish that re-aims

- **What & why.** One SVG dish — parabolic reflector, mesh
  triangulation, feed arm and receiver cabin — drawn at 60vw and
  anchored centre-frame. As scroll moves between pointings, the dish
  re-aims: it rotates and tilts toward the pointing being read, with
  a heavy, patient settle. It belongs because the dish is the page's
  narrator: it literally points at whatever the reader is reading,
  and its slowness teaches the visitor the station's timescale before
  a single word is read.
- **Structure.** One inline `<svg>` (viewBox 0 0 880 620): reflector
  as a parabolic path filled `--dish-bone` at 92% with the mesh as
  ~120 triangulated `<line>` elements in `--grey-faint` (a separate
  `<g class="mesh">` so it can parallax at ×0.06 against the
  reflector), feed arm as two struts and a cabin block, pedestal and
  desert shadow as an ellipse in `--night-deep`. Aim is applied as a
  CSS transform on the reflector group: `rotate(r)` plus a tilt
  faked by `scaleY(1 − t·0.004)` and a feed-arm counter-shift, so the
  drawing reads as a three-dimensional slew in a ±8° stage space.
  The whole dish is `aria-hidden`; its information (current target)
  is carried by the readout (§6.2) in real text.
- **Motion spec.** Trigger: lerped scroll channel through the
  pointings act. The aim interpolates between the Schedule's stage
  angles (§4) as the act's progress crosses each pointing's band;
  dish channel lerp 0.055 (≈1.37s to 99% settle), transform composed
  per frame from the channel — no CSS transitions on the dish, ever.
  Parked (0°/0°) in the hero and again at the footer. A faint
  pedestal shadow shift (±6px) accompanies rotation so the mass
  reads as moving, not sliding.
- **States.** Parked (hero/footer) / aiming (between pointings) /
  locked (settled within 0.1° of a pointing's aim for >800ms — the
  readout's lock event, §6.2, keys off this) / past (act scrolled
  away: channel unregistered, dish holds its last aim at zero cost).
- **Content merge.** The dish aims at the *text*: each pointing's
  coordinate block sits on the side the dish rotates toward, so the
  instrument and the words it names are in one sightline. Remove the
  pointings and the dish is a logo; with them, it is the act of
  reading, drawn.
- **Failure fallback.** Watchdog: if the rAF loop has not painted
  two consecutive frames by 3000ms, the dish is set by CSS class to
  the current pointing's printed aim (a static rotation per section,
  applied by `:target`-free scrollspy classes) — and with no JS at
  all, the dish ships parked above the pointings and each pointing
  prints its own small static dish glyph at its aim angle beside its
  coordinates. The page never depends on the slew to be understood.
- **Reduced-motion variant.** No slew. The dish appears at each
  pointing's aim as a static rotation (the scrollspy-class fallback
  above becomes the primary rendering), changing by instant cut at
  section boundaries. The mass and the information survive; only the
  patience is abridged.
- **Performance budget & mobile variant.** One SVG, ~140 nodes,
  transform-only per frame; budget ≤0.4ms/frame. Mobile (<768px):
  dish at 88vw in the hero only, not sticky, aim changes by cut at
  pointing boundaries, mesh lines thinned to every third triangle.
- **Choreography timeline (v2).** t=0 first paint: dish printed
  parked, mesh and shadow complete → JS arms the loop → hero holds
  parked through the headline's tuning (§6.3) → first scroll into
  the act: aim begins slewing toward P-01 (−6°/+3°) → ≈1.37s settle
  → lock event fires the readout's final digit (§6.2) → per pointing
  thereafter; final beat: footer approach slews back to parked over
  the same channel.
- **State matrix (v2).** *Rest:* parked or locked at a pointing.
  *Hover:* none — the dish is not a control and does not react to the
  pointer (lean-in belongs to text and frames, §6.7). *Focus:* not
  focusable. *Active:* n/a. *Scrolled-past:* holds last aim, loop
  channel unregistered. *Disabled:* n/a. *Touch:* identical to
  desktop; aim follows scroll only.
- **Breakpoints (v2).** ≥1200px: 60vw sticky stage centred, full
  mesh, continuous slew. 768–1199px: 72vw, sticky within the act,
  mesh at 2/3 density. <768px: 88vw hero object, non-sticky, aim by
  cut, mesh at 1/3 density, shadow shift removed.
- **Edge cases & failure modes (v2).** *Fast scroll through the
  whole act:* the channel interpolates across skipped pointings —
  the dish sweeps through intermediate aims without locking, and no
  lock events fire for skipped pointings (their readouts print
  pre-locked, §6.2). *Scroll back up:* the slew reverses along the
  same interpolation; aims are positions, not animations, so reverse
  is free. *SVG blocked/inlined poorly:* the dish's alt role is
  carried by a printed caption under the hero ("THE 64-METRE DISH,
  PARKED AT THE MERIDIAN") that ships in the DOM regardless.
  *Very long act (pointings added):* aims interpolate between
  schedule entries generically — a sixth pointing needs a schedule
  row, not new code.
- **Accessibility spec (v2).** `aria-hidden="true"` on the SVG; the
  current target is announced by the readout's real text (§6.2),
  which sits in reading order before each pointing's name. No
  information exists only in the drawing. The dish never overlaps
  text at any breakpoint (stage and text measures are disjoint by
  the §4 grid).
- **Tokens consumed (v2).** `--dish-bone`, `--grey-faint`,
  `--night-deep`, `--ease-slew`, `--loop-lerp` (dish channel 0.055).

### 6.2 Target coordinate readout that slews and locks

- **What & why.** Above every pointing's serif name, its real RA/Dec
  in IBM Plex Mono — and as the pointing enters the dish's aim, the
  figures *slew*: each digit cycles through wrong values,
  decelerating, and locks onto the schedule's true coordinate. It
  belongs because coordinates are this theme's headings (§3, law 1):
  the readout performs the act of acquisition — the instrument
  hunting, then holding — in the two seconds before the visitor reads
  a word of the section.
- **Structure.** A `<p class="readout">` per pointing containing the
  true coordinate string twice: once as visually-hidden real text
  (the DOM's source of truth, read by assistive tech and printed
  with no JS), and once as an `aria-hidden` visual layer of
  per-digit `<span>`s that JS animates. Beside it, a lock tick: a
  14px signal-thread rule and the whisper label `LOCKED` (or
  `SLEWING` during the hunt). Band and integration target print on
  the same block, static, from the Schedule.
- **Motion spec.** Trigger: the pointing's band crossing 55% of the
  lerped scroll channel (the "reading line"), once per pointing per
  direction. Each digit span cycles glyphs 0–9 (RA/Dec punctuation
  never cycles — the frame holds while the values hunt) on an
  interval that grows 40ms → 260ms across 1400ms, `--ease-settle`;
  digits lock left-to-right, one per ~140ms, each lock flashing its
  digit `--thread-pale` for 120ms before resting at
  `--signal-thread`, then the whole string decays to `--star-grey`
  over 2000ms — locked coordinates go quiet; they have been read.
  The final lock coincides with the dish's lock event (§6.1).
- **States.** Printed (no-JS / pre-trigger: true string, grey) /
  slewing (cycling, thread) / locking (digits landing left-to-right)
  / locked-quiet (true string, grey, tick lit) / re-slew (on reverse
  scroll past the reading line, a shortened 700ms hunt — the
  instrument re-acquires faster the second time).
- **Content merge.** The readout *is* the heading: it names the
  section in the only terms the station trusts. Its values are the
  Schedule's, character-for-character; the serif name below it is
  the human gloss on the instrument's fact.
- **Failure fallback.** The true string is the DOM default; the
  cycling layer is JS-built over it. Watchdog: any readout still
  slewing 3000ms after its trigger is snapped to the true string by
  class. If the dish's lock event never fires (loop fault), the
  readout completes on its own timer — the two elements are
  choreographed together but fail independently.
- **Reduced-motion variant.** No hunt. The string prints true, the
  tick lights by instant change when the pointing crosses the
  reading line, and `LOCKED` appears. All information, no theatre.
- **Performance budget & mobile variant.** Per readout: ≤22 digit
  spans, text-content writes only during the 1400ms hunt; budget
  ≤0.1ms/frame, zero when idle. Mobile: identical (digits are cheap);
  the hunt shortens to 1000ms because the reading line arrives
  sooner on a small screen.
- **Choreography timeline (v2).** Reading line crossed → t=0 tick
  label flips to `SLEWING` → digits begin cycling at 40ms intervals
  → t≈140ms first (leftmost) digit locks, pale flash 120ms → locks
  proceed rightward ≈140ms apart → t=1400ms final digit locks with
  the dish's lock → tick label `LOCKED` → t=3400ms string decayed to
  grey; the section's text (§6.5) completes its focus-in inside the
  same window.
- **State matrix (v2).** *Rest:* printed grey. *Hover:* the string
  warms to `--bone-dim` (a whisper leaning in, §6.7) — values never
  change on hover. *Focus:* the readout is text, not a control; when
  its pointing's card (§6.12) is focused, the readout warms the same
  way. *Active:* n/a. *Scrolled-past:* locked-quiet persists; the
  hunt does not re-run downward. *Disabled:* n/a. *Touch:* no hover
  warm; hunt and lock identical.
- **Breakpoints (v2).** ≥1200px: readout at 0.8125rem above the
  name, tick left. 768–1199px: same, name wraps under it.
  <768px: readout stacks RA over Dec on two lines (never truncated —
  a coordinate may wrap, it may not be cut), hunt 1000ms.
- **Edge cases & failure modes (v2).** *Skipped pointing (fast
  scroll):* prints pre-locked, tick lit, no hunt — the instrument
  does not perform for an empty room. *Coordinate longer than the
  line (P-05's ± values):* wraps as a block; the ± and its note
  print in the same string, never separated from the digits they
  qualify. *Schedule edited:* the readout renders from the Schedule
  JSON at build time — a hand-edited readout that disagrees with the
  Schedule fails the §10 figure audit.
- **Accessibility spec (v2).** The animated layer is `aria-hidden`;
  screen readers meet only the true string, in reading order, before
  the pointing's name (heading order: readout is a `<p>`, the name
  is the `<h2>` — the instrument speaks first without breaking the
  outline). `LOCKED` state is visual only; no live region announces
  it (a lock is ambience, not news). Contrast: grey string 4.8:1 at
  rest, thread 8.6:1 while slewing.
- **Tokens consumed (v2).** `--font-log`, `--star-grey`,
  `--signal-thread`, `--thread-pale`, `--bone-dim`, `--ease-settle`.

### 6.3 Headline that tunes in by pulses

- **What & why.** The hero headline arrives the way the station's
  signals do: not all at once, and not on demand. It begins at 3px
  blur and 55% contrast; a sequence of acquisition pulses sharpens it
  step by step until, inside 6 seconds, it stands fully tuned. It
  belongs because the brand statement should be *received*, not
  displayed — the visitor's first experience of the site is the
  station's whole method in miniature: wait, and it resolves.
- **Structure.** The `<h1>` in Instrument Serif at the §3 hero size,
  text fully present in the DOM at full contrast — the blurred state
  is a JS-armed class applying `filter: blur(3px)` and a
  `color`/`opacity` step via CSS custom property `--tune` (0→1 in
  four steps). The pulses that drive it are the trace's (§6.4)
  acquisition blips, rendered on the hero trace at the horizon; each
  pulse's peak applies the next `--tune` step. No text is ever
  re-flowed: blur and contrast only, so layout never shifts.
- **Motion spec.** Trigger: load. Acquisition pulses at t=900ms,
  2200ms, 3500ms, 4800ms (the entrance cadence — faster than the
  ambient 6–14s rhythm the trace settles into afterwards, §6.4).
  Each pulse: trace blip 700ms `--ease-pulse`; at its peak, `--tune`
  steps 0→0.25→0.5→0.75→1, mapping to blur 3px→2.25→1.5→0.75→0 and
  contrast 55%→66%→77%→88%→100%, the step itself eased over 900ms
  `--ease-focus`. Fully tuned at ≈5.7s. Watchdog: the global 6000ms
  `.tuned` class (§5) forces `--tune: 1` regardless.
- **States.** Untuned (armed, before first pulse) / tuning (steps
  1–3) / tuned (step 4, classes removed, filter released) / forced
  (watchdog path — visually identical to tuned; the visitor cannot
  tell, and is not meant to).
- **Content merge.** The headline's content is the station's claim,
  and its *behaviour* is the claim's evidence: a page about receiving
  faint signals that opens with a faint statement resolving. The
  standfirst beneath it prints sharp from the start — the paperwork
  does not perform; only the signal tunes.
- **Failure fallback.** No-JS: headline prints sharp (the armed class
  is JS-applied). JS with a stalled loop: the 6000ms watchdog.
  Blocked fonts: the tuning applies to the fallback serif identically
  — blur does not care which serif it softens.
- **Reduced-motion variant.** Headline prints sharp at load. The
  trace still idles (§6.4's variant) but no pulse touches the type.
  The 6-second law is honoured trivially: arrival time zero.
- **Performance budget & mobile variant.** One element's filter,
  stepped four times; filter is on the headline only (never a
  container — a blurred ancestor would rasterise the hero). Budget
  ≤0.2ms/frame during steps. Mobile: identical cadence; blur steps
  start at 2.5px (small screens forgive less softness at display
  size, and the type is smaller).
- **Choreography timeline (v2).** t=0 first paint: sharp headline
  (un-armed DOM) → JS arms within one frame: blur 3px/55% → t=900ms
  pulse 1 → step 1 (2.25px/66%) by t≈1800ms → t=2200ms pulse 2 →
  step 2 → t=3500ms pulse 3 → step 3 → t=4800ms pulse 4 → step 4,
  tuned ≈t=5700ms → t=6000ms watchdog deadline passes (used or
  unused) → signal log (§6.18) opens as the hero's last beat.
- **State matrix (v2).** *Rest:* tuned. *Hover:* none — the headline
  is not leaned on (§6.7 excludes the h1; it has already been
  received). *Focus:* not focusable. *Active:* n/a.
  *Scrolled-past:* stays tuned; scrolling back up never un-tunes it
  — a received signal stays received. *Disabled:* n/a. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: full clamp size, four steps.
  768–1199px: same cadence. <768px: headline at clamp floor 4.5rem,
  blur origin 2.5px, steps unchanged — the ritual is not shortened
  for small screens, only softened.
- **Edge cases & failure modes (v2).** *Slow font load (FOUT):* the
  armed blur applies to whatever face is rendering; if the serif
  swaps mid-tuning, the swap is hidden inside the blur — the one
  moment a font swap is welcome. *Visitor scrolls immediately:*
  tuning continues off-screen and completes by watchdog; returning
  to the top shows a tuned headline. *`--tune` unsupported (ancient
  browser):* the class-based fallback sets the four steps as discrete
  classes with the same values.
- **Accessibility spec (v2).** The headline is real text, first in
  reading order, never `aria-hidden`; its blurred states are purely
  visual and brief, and contrast never drops below 55% of a 14:1
  pairing (≈5.4:1 effective at the worst step — above AA for large
  text at every instant of the tuning). Motion-sensitive visitors
  get the reduced variant. The pulses are visual only; nothing
  flashes above 3 per second (the cadence is one per ≥1.3s, and the
  blip is a thin line, not a luminance flash).
- **Tokens consumed (v2).** `--dish-bone`, `--font-display`,
  `--ease-focus`, `--ease-pulse`.

### 6.4 Idle noise trace with rare pulses

- **What & why.** A thin trace — one signal-thread line on a canvas
  along the hero's horizon — that idles at noise amplitude forever,
  and at irregular intervals lets a single clean pulse blip through
  it. It is the station's live instrument, drawn under the headline
  it keeps almost interrupting. It belongs because a listening site
  needs a pulse of its own: proof, continuous and quiet, that the
  listening is actually happening.
- **Structure.** One `<canvas>` (full hero width, 72px tall) pinned
  to the horizon hairline, drawing a 1.5px polyline in
  `--signal-thread` at 80% over a `--thread-dim` baseline. Noise is
  a seeded random walk (amplitude ±3px); a pulse is a Gaussian blip
  (width ~90px, height 26px) that travels the line once at 220px/s
  and is gone. A static SVG copy of the trace (noise + one blip at
  62% width) ships beneath the canvas as the no-JS/no-canvas print.
- **Motion spec.** Trigger: time, continuous from load. Noise redraws
  per rAF frame from the walk (dt-clamped). Ambient pulses are
  scheduled at randomised 6000–14000ms intervals (uniform draw,
  re-drawn after each pulse — irregularity is specified, not
  emergent). Entrance pulses (§6.3's cadence) pre-empt the ambient
  schedule; the ambient clock starts after the fourth entrance
  pulse. Every pulse — ambient, entrance, or click-sent (§6.8) — is
  reported to the signal log (§6.18) with its timestamp.
- **States.** Idling (noise only) / pulsing (a blip in transit,
  ~1.9s across a 1440px hero) / stilled (reduced motion or act
  off-screen: one frozen frame, still printed) / printing (the SVG
  fallback state).
- **Content merge.** The trace is not decoration under the headline;
  it is the headline's power supply — its entrance pulses tune the
  type (§6.3), its click pulses carry the reader's own transmissions
  (§6.8), and its log (§6.18) is the footer's content. One line,
  three jobs, all of them the station's work.
- **Failure fallback.** Canvas blocked or loop fault: the baked SVG
  trace shows (watchdog 3000ms, as §6.1). No-JS: the SVG ships in the
  DOM and the canvas is JS-inserted over it. The horizon hairline
  itself is CSS and cannot fail.
- **Reduced-motion variant.** The printed SVG trace, static, with
  its one blip. No pulses fire; the log (§6.18) records none and
  prints its empty-state line. Stillness is a legitimate reading of
  the instrument.
- **Performance budget & mobile variant.** One canvas ≤1440×72
  device px, one polyline of ≤240 points per frame; budget
  ≤0.4ms/frame, and the channel unregisters when the hero is <10%
  visible. Mobile: canvas height 48px, 160 points, pulse height
  18px; intervals unchanged (patience is not a desktop feature).
- **Choreography timeline (v2).** t=0 SVG print visible → canvas
  fades over it in 500ms once its first frame paints → noise walk
  begins → t=900/2200/3500/4800ms entrance blips (each also stepping
  §6.3) → ambient schedule arms after the fourth → first ambient
  blip somewhere in the following 6–14s → steady state: noise,
  rare blips, each logged.
- **State matrix (v2).** *Rest:* idling. *Hover:* none — the trace
  is an instrument readout, not a control; hovering it does nothing
  (lean-in applies to the horizon's caption, not the line).
  *Focus:* not focusable. *Active:* n/a. *Scrolled-past:* frozen
  frame, channel unregistered. *Disabled:* n/a. *Touch:* identical;
  pulses remain time-triggered.
- **Breakpoints (v2).** ≥1200px: 72px tall, blip 26px.
  768–1199px: 56px, blip 22px. <768px: 48px, blip 18px, walk
  amplitude ±2px (the line stays a whisper at every size).
- **Edge cases & failure modes (v2).** *Pulse scheduled while tab
  hidden:* pulses are computed from wall-clock on return — a pulse
  whose moment passed in the background is *not* back-filled; the
  log records only pulses that actually rendered (the log is a
  record of the visit, not of the clock). *Two pulses colliding
  (click during ambient):* the click blip queues 300ms after the
  ambient one clears the click's x-position; both are logged
  separately. *Canvas resized mid-pulse:* the walk re-seeds, the
  blip completes on the new width — a resized instrument recalibrates,
  it does not crash.
- **Accessibility spec (v2).** Canvas is `aria-hidden`; its content
  (that listening is live, that pulses occurred) is available as
  text in the status strip (§6.14) and the log (§6.18). The blip's
  peak luminance stays within the thread's 8.6:1 — a line brightening,
  never a flash; pulse frequency is far below any photosensitivity
  threshold.
- **Tokens consumed (v2).** `--signal-thread`, `--thread-dim`,
  `--thread-pale`, `--grey-faint`, `--ease-pulse`, `--ease-drift`.

### 6.5 Focus-in section reveals

- **What & why.** Every pointing's text resolves into focus as it
  enters the dish's aim: from blur(2px) and 70% contrast to sharp —
  no translation, no fade-up, no rise. It belongs because reading, in
  this theme, *is* receiving: a section that slides up is a section
  performing; a section that resolves is a signal arriving. This is
  the theme's only reveal grammar, applied to every section, card
  and table row-block on the page.
- **Structure.** Any element with `[data-focus]` ships in the DOM at
  full sharpness. JS arms it by adding `.armed`, which sets
  `filter: blur(2px); color: color-mix(in srgb, currentColor 70%, transparent)`
  via a `--resolve` custom property (1 = sharp). An
  IntersectionObserver (threshold 0.25, rootMargin bottom −10%)
  starts the resolve; the animation itself is driven on the shared
  rAF loop so it scrubs coherently with the dish's aim (§6.1) rather
  than running on its own clock.
- **Motion spec.** Trigger: entering the aim (observer) — resolve
  over 900ms, `--ease-focus`, blur 2px→0 and contrast 70%→100%
  together, starting when the element's top crosses 75% of the
  viewport. Elements in the same pointing resolve in reading order
  with a 90ms stagger between siblings (the only stagger besides
  §6.2's digits). Once resolved, an element never re-blurs on the
  same pass downward; scrolling back up, elements above the reading
  line stay sharp (a received signal stays received, §6.3).
- **States.** Printed (un-armed: sharp) / armed (2px, 70%) /
  resolving (mid-flight) / resolved (sharp, classes released) /
  forced (watchdog-snapped sharp — indistinguishable from resolved).
- **Content merge.** The reveal is not applied *to* the content; it
  is the content's mode of arrival, timed to the dish's aim at the
  same pointing — dish, readout and text resolve as one act of
  acquisition across three elements. A section out of focus while
  the dish points elsewhere is the theme's spatial logic made
  visible.
- **Failure fallback.** The un-armed DOM is sharp; arming is
  JS-only. Per-element watchdog: 6000ms after first entering the
  viewport, an unresolved element is snapped sharp by class (§5).
  Observer unsupported: all elements resolve on a single 1000ms
  timer after load — the page degrades to "everything tunes in at
  once", never to "everything stays blurred".
- **Reduced-motion variant.** No arming. Everything prints sharp;
  the observer is never created. The law (§1) is honoured by never
  creating faintness in the first place.
- **Performance budget & mobile variant.** Filter on leaf text
  blocks only (never on a section container — rasterisation cost),
  ≤6 elements resolving concurrently; budget ≤0.3ms/frame. Mobile:
  blur origin 1.5px, resolve 700ms — smaller type forgives less
  softness and the reading line arrives sooner.
- **Choreography timeline (v2).** Element crosses 75% line → t=0
  resolve starts (sibling stagger +90ms each) → t=450ms half-sharp
  (1px, 85%) → t=900ms sharp, classes released → watchdog deadline
  t=6000ms from viewport entry passes unused (or fires, §5).
- **State matrix (v2).** *Rest:* resolved. *Hover:* n/a (hover has
  its own system, §6.7, and never re-blurs). *Focus:* a focused
  element inside an armed block forces that block's resolve to
  complete instantly — a keyboard visitor must never tab into fog.
  *Active:* n/a. *Scrolled-past:* stays resolved. *Disabled:* n/a.
  *Touch:* identical triggers; no hover dependency anywhere in the
  reveal path.
- **Breakpoints (v2).** ≥1200px: as spec'd. 768–1199px: stagger
  70ms. <768px: blur 1.5px, 700ms, stagger 50ms, concurrency ≤4.
- **Edge cases & failure modes (v2).** *Very long pointing (text
  taller than 200vh):* resolves in viewport-sized waves as each
  block enters — the tail of a long section is never left blurred
  because its head resolved. *Jump-scroll to the footer (anchor
  link):* every element above the destination is marked resolved
  without animation; the destination resolves normally. *Print:*
  a print stylesheet forces `--resolve: 1` on everything — paper
  gets the tuned page.
- **Accessibility spec (v2).** Blurred text is a visual state only;
  the DOM text is complete and readable by assistive tech at all
  times. Worst instant contrast: 70% of the resting pairing — bone
  prose at ≈7.4:1 effective, grey labels at ≈3.4:1 *during a 900ms
  transition only*, which is why labels inside armed blocks use
  `--bone-dim` until resolved (a build detail the gate checks, §10).
  Focus-forcing (above) guarantees keyboard parity.
- **Tokens consumed (v2).** `--ease-focus`, `--bone-dim`,
  `--dish-bone`, `--star-grey`.

### 6.6 The reluctant counters — integration time & SNR

- **What & why.** Two numbers in mono, counting the way the station
  counts: slowly, and without encouragement. The integration clock
  accumulates the night's listening (from 03:12:44 already elapsed
  at load, §4's night) in real seconds. The SNR readout starts at
  4.2 and creeps toward — but never reaches — the printed
  confirmation line of 8.0, beside a control-red dot and the stamp
  `BELOW CONFIRMATION`. They belong because they are the theme's
  honesty engine: the page's most-watched numbers describe work in
  progress and a signal *not* found, and the visitor trusts
  everything else on the page because these two refuse to flatter.
- **Structure.** A counter pair in the hero's paperwork block and
  repeated in the status strip (§6.14) — both instances render from
  one state object (a start timestamp + the creep function), so the
  page can never disagree with itself. Values are real text,
  `tabular-nums`, updated by text-content writes at 1Hz for the
  clock and on creep steps for SNR. The confirmation line is printed
  as a hairline with its label — the threshold is a drawn object,
  not a footnote.
- **Motion spec.** Trigger: time, from load. Clock: +1s per real
  second, computed as `elapsed = tonight_base + (now − load_time)`
  so backgrounding never loses or gains time. SNR creep: +0.1 per
  540s of *attended* dwell (tab visible), from 4.2, hard-capped at
  4.9 for any single visit — the published creep function lives
  beside the Schedule, and the counter may not exceed what the
  function yields. Digit changes land with a 200ms `--ease-settle`
  colour settle (grey → thread → grey) — a number arriving, not
  flipping. No count-up-on-scroll, no odometer theatrics.
- **States.** Counting (tab visible) / holding (tab hidden: values
  freeze on screen, recompute true on return) / printed (no-JS: the
  load-time values as static text — 03:12:44 and 4.2, correct at the
  moment of print and labelled as the night's figures, not live).
- **Content merge.** The counters are the pointings' sum: the
  clock's base (03:12:44) is time already spent inside P-01's 4h
  target, and the SNR is P-01's strongest channel. They sit beside
  the Schedule's programme total (23 h) so the visitor can do the
  station's arithmetic: 3¼ hours in, 23 to go, nothing confirmed.
  Numbers that reconcile are content; numbers that merely animate
  are decoration, and these reconcile.
- **Failure fallback.** No-JS prints the static values (above).
  Clock fault (system time changed mid-visit): the clock clamps to
  monotonic `performance.now()` deltas if wall-clock jumps by
  >60s — the instrument notes the fault in the console and keeps
  honest time.
- **Reduced-motion variant.** Values still update (they are data,
  not motion), but the colour settle is removed — digits change
  plainly. A visitor who asks for less motion still gets true
  numbers.
- **Performance budget & mobile variant.** Two text writes per
  second worst case; budget ≈0ms/frame. Mobile: identical — the
  counters are the cheapest element on the page and are never cut.
- **Choreography timeline (v2).** t=0 printed values (03:12:44 /
  4.2) → JS takes over within one frame, values continuous (no
  jump) → t=1s first clock tick → SNR first creep step at t=540s
  of attended dwell → the pair repeats in the status strip with
  identical values at every instant (one state object, two renders).
- **State matrix (v2).** *Rest:* counting. *Hover:* the pair warms
  to `--bone-dim` and shows the whisper caption `STRONGEST CHANNEL
  — P-01, TAU CETI` (§6.7's lean applies to the caption, not the
  digits). *Focus:* the counters are text; the caption is reachable
  as part of the status strip's reading order. *Active:* n/a.
  *Scrolled-past:* keep counting (they are the page's clock, not a
  section's ornament). *Disabled:* n/a. *Touch:* no hover caption;
  the caption prints beneath the pair instead.
- **Breakpoints (v2).** ≥1200px: pair inline in the hero paperwork
  block, repeated in §6.14. 768–1199px: same. <768px: stacked two
  lines, caption printed beneath (as touch).
- **Edge cases & failure modes (v2).** *Very long visit (>9h):*
  SNR caps at 4.9 by the creep function's asymptote — a marathon
  visit still does not confirm the signal; the honesty is structural,
  not a timer oversight. *Clock crossing a pointing boundary:* when
  elapsed passes P-01's 4h target, the caption updates to P-02 and
  the log (§6.18) gains a `POINTING COMPLETE — NO CONFIRMATION` row:
  the counters, the schedule and the log agree, or the build is
  wrong (§10 figure audit).
- **Accessibility spec (v2).** `aria-live` is **off**: a screen
  reader is not read a ticking clock. The values are available on
  demand as ordinary text, with a visually-hidden sentence giving
  the state in words ("Integration tonight: 3 hours 12 minutes.
  Strongest signal 4.2, below the confirmation line of 8."). The red
  dot is always paired with the `BELOW CONFIRMATION` text label
  (§2's red discipline).
- **Tokens consumed (v2).** `--font-log`, `--star-grey`,
  `--signal-thread`, `--control-red`, `--bone-dim`, `--ease-settle`.

### 6.7 Lean-in hover focus

- **What & why.** Attention is physical at a listening station: you
  lean toward faint things. Elements in the lean set — pointing
  names, card titles, mesh frames, readout blocks — sit very
  slightly soft at rest (blur 0.6px, contrast 92%) and ease sharper
  as the pointer approaches within ~120px, fully sharp at contact.
  It belongs because it makes the visitor's body do the theme's
  gesture: the page rewards leaning in, exactly as its copy asks.
- **Structure.** Pointer position is tracked on the shared rAF loop
  (pointermove writes coordinates; the loop computes distances — no
  per-element listeners). Each `[data-lean]` element gets a
  `--lean` property (0 at ≥120px, 1 at 0px) mapped to
  `blur(0.6px × (1 − lean))` and contrast `92% + 8% × lean`.
  Distance is to the element's border box, not its centre, so large
  frames start sharpening at their edges.
- **Motion spec.** Trigger: pointer proximity, continuous. `--lean`
  is lerped at 0.18 per frame (fast enough to feel responsive,
  slow enough to feel like focus pulling, ≈250ms to full). Ease is
  the lerp itself over `--ease-focus`'s curve family. Leaving the
  radius decays at the same rate — focus relaxes, it does not snap.
- **States.** Resting-soft (≥120px) / leaning (in transit) / sharp
  (contact or within the element) / exempt (touch, keyboard,
  reduced motion: permanently sharp).
- **Content merge.** Lean-in applies only to things that are
  *allowed* to be faint: Display-register names and images. Log
  text — coordinates, prose, data — is never in the lean set (§3,
  law 4: paperwork does not perform). The softness is a property of
  the poetry, never of the facts.
- **Failure fallback.** The rest state (0.6px / 92%) is itself
  readable — worst-case effective contrast for a pointing name is
  bone at ≈11:1 through the softness — so a total failure of the
  pointer system leaves a page that is merely 8% less crisp. No
  watchdog is needed because nothing is ever hidden; the §10 gate
  verifies the rest-state contrast instead.
- **Reduced-motion variant.** Exempt state: everything in the lean
  set prints sharp, proximity is never measured.
- **Performance budget & mobile variant.** Distance maths for ≤14
  lean elements per frame, transform-free (filter only on the
  elements themselves); budget ≤0.2ms/frame. Mobile/touch: disabled
  entirely — there is no pointer to lean with, and elements print
  sharp (the exempt state is the mobile state).
- **Choreography timeline (v2).** Pointer enters 120px radius →
  `--lean` rises 0→1 over ≈250ms (lerp 0.18) → element sharp at
  contact → pointer leaves → decay over ≈250ms → resting-soft.
  No other beats; the element's whole life is approach and release.
- **State matrix (v2).** *Rest:* resting-soft. *Hover:* sharp (by
  definition of the system). *Focus:* keyboard focus forces `--lean:
  1` instantly on the focused element and its readout block — focus
  is a form of leaning and is honoured faster than the pointer.
  *Active:* click on a lean element also fires §6.8's pulse.
  *Scrolled-past:* elements outside the viewport are skipped by the
  distance pass. *Disabled:* n/a. *Touch:* exempt/sharp always.
- **Breakpoints (v2).** ≥1200px: radius 120px. 768–1199px: radius
  100px (denser layout, shorter leans). <768px: system off (touch
  assumed; a fine-pointer media query may re-enable it at 80px for
  small laptops in portrait).
- **Edge cases & failure modes (v2).** *Pointer leaves the window:*
  all leans decay to rest — nothing stays sharp for an absent
  visitor. *Two elements equidistant:* both sharpen; the system has
  no winner-takes-all rule, because attention is not exclusive.
  *Element mid-resolve (§6.5) while leaned on:* the two filters
  compose by taking the sharper of the two states per property —
  focus systems never stack blur.
- **Accessibility spec (v2).** Proximity is never the only path to
  sharpness: focus forces it (above), touch exempts it, reduced
  motion exempts it, and the rest state passes contrast on its own
  (gate-checked). No information is gated behind the lean. Pointer
  users with tremor get the lerp's forgiveness: the 120px radius
  and 250ms pull mean approximate aim still sharpens the target.
- **Tokens consumed (v2).** `--ease-focus`, `--dish-bone`,
  `--bone-dim`.

### 6.8 Click-to-send pulse

- **What & why.** Clicking any pointing sends a pulse: a faint ring
  expands from the element, a blip crosses the hero trace if it is
  in view, and the transmission is appended to the footer signal log
  with its real timestamp. It belongs because it completes the
  theme's circuit — the station listens, and once per click, the
  visitor transmits. Interaction as participation in the station's
  work, not as interface chrome.
- **Structure.** The ring is a single reusable `<div class="pulse-ring">`
  (border 1px `--signal-thread`, border-radius 50%) positioned at
  the click point over the clicked element, scaled 0→3.2× the
  element's smaller dimension and faded out. The log append is a
  call into §6.18's writer with source `SENT`. Keyboard equivalent:
  Enter or Space on a focused pointing card (§6.12) sends from the
  card's centre — the ring is drawn there identically.
- **Motion spec.** Trigger: click/Enter. Ring: 900ms `--ease-pulse`,
  opacity 0.85→0, scale as above; a second, fainter ring follows at
  +140ms at 0.5× scale (the echo off the dish — one reflection, no
  more). Trace blip (if hero in view): 700ms across the trace from
  the click's relative x-position. Log row lands at ring end
  (t=900ms) — the record is written when the pulse *arrives*, not
  when it is sent, which is the theme's whole cosmology in one
  timing decision.
- **States.** Idle / sending (rings in flight) / logged (row
  appended, ring gone) / throttled (a second click within 600ms on
  the same element is absorbed — the station does not stutter;
  clicks on *different* elements are never throttled).
- **Content merge.** The pulse is sent *from the pointing* — its
  origin is the content, its destination is the log, and the log
  entry names the pointing it came from (`SENT — FROM P-02,
  KEPLER-186F`). It is the only element that writes to another
  element, and the write is the meaning.
- **Failure fallback.** If the log is unavailable (JS partially
  failed), the rings still fire — feedback never depends on the
  record. If animation fails entirely, the click still focuses the
  pointing (native anchor behaviour): participation degrades to
  navigation, never to nothing.
- **Reduced-motion variant.** No rings. The log row appends
  immediately on click, and the pointing's tick (§6.2) flashes once
  by colour change only. The record — the part that matters —
  survives intact.
- **Performance budget & mobile variant.** Two absolutely-positioned
  divs, transform/opacity only; budget ≤0.1ms/frame during the
  900ms. Mobile: identical; ring scale capped at 2.4× (small
  elements, small sky).
- **Choreography timeline (v2).** t=0 click → ring 1 expands →
  t=140ms echo ring → t≈350ms trace blip launches (if hero visible)
  → t=900ms rings complete → log row appends (§6.18's own beat) →
  throttle window closes at t=600ms from the *first* click.
- **State matrix (v2).** *Rest:* idle. *Hover:* no pre-state (the
  lean, §6.7, is the hover language; the pulse does not tease).
  *Focus:* focused pointings show the whisper hint `ENTER — SEND A
  PULSE` in their readout block (the affordance is labelled for
  keyboard users, invisible to no one who needs it). *Active:*
  sending. *Scrolled-past:* n/a. *Disabled:* during the 600ms
  throttle, the element is inert to re-clicks but never visually
  disabled — the station ignores a stutter, it does not grey out.
  *Touch:* tap = click, identical.
- **Breakpoints (v2).** ≥1200px: as spec'd. 768–1199px: echo ring
  at 0.4×. <768px: single ring, 2.4× cap, trace blip skipped if the
  hero is off-screen (it usually is) — the log append is the beat
  that matters.
- **Edge cases & failure modes (v2).** *Click during a re-pointing
  transition (§6.16):* absorbed — transmissions wait for the new
  page, and the log of the *new* page opens empty (logs are
  per-visit, per-page-load; §6.18). *Rapid clicking across many
  pointings:* each sends; the log caps at 40 rows (§6.18) and the
  rings are pooled (max 4 concurrent) so enthusiasm cannot jank the
  page.
- **Accessibility spec (v2).** The send action is a real button
  behaviour on real focusable elements (pointing cards are
  `<article>`s with a button, not click-divs); the hint text is in
  the button's accessible name. The log append is announced via a
  polite live region with the row's text — the one live announcement
  the theme permits itself, because the visitor caused it. Ring
  animation is decorative and `aria-hidden`.
- **Tokens consumed (v2).** `--signal-thread`, `--thread-pale`,
  `--ease-pulse`.

### 6.9 Dish-mesh image frames

- **What & why.** Photographs — the array at dawn, a receiver being
  craned in, the control room's one window — are presented as
  *received signals*: each sits inside a frame overlaid with the
  dish's fine mesh triangulation, and resolves into focus
  (scale 1.04 → 1, mesh fading to 12%) as it enters the aim. It
  belongs because in this theme a photograph is not an illustration;
  it is something the instrument caught, and the frame says so.
- **Structure.** A `<figure>` with the `<img>`, an SVG mesh overlay
  (the same triangulation generator as §6.1's mesh, clipped to the
  frame, lines in `--star-grey` at 34%), and a `<figcaption>` in Log
  register that always includes the photograph's provenance line —
  date, band or camera, and who took it. The mesh is a separate
  layer so its fade never touches the image's own focus resolve
  (§6.5 composes with it: mesh opacity and image scale are this
  element's; blur is §6.5's, and the sharper state wins per §6.7's
  composition rule).
- **Motion spec.** Trigger: entering the aim (§6.5's observer).
  Image scale 1.04→1 over 1200ms `--ease-focus`; mesh opacity
  34%→12% over the same window, delayed 150ms (the frame releases
  its grip just after the picture lands). The mesh never reaches 0 —
  a received signal keeps its grain. Hover (§6.7 lean): mesh eases
  to 8% and the caption warms — leaning strips a little more mesh
  away.
- **States.** Framed (mesh 34%, scale 1.04) / resolving / received
  (mesh 12%, scale 1) / leaned (mesh 8%) / printed (no-JS: mesh at
  12%, scale 1 — the received state is the shipped state).
- **Content merge.** The caption is part of the element, not an
  afterthought: provenance is what makes a photograph a signal
  rather than stock. A build that ships a mesh frame with a missing
  or decorative caption has pasted the theme onto a picture; the
  gate (§10) rejects frames without provenance lines.
- **Failure fallback.** Ships received (above). Image fails to load:
  the frame holds its aspect box with the mesh at 34% and the
  caption plus a mono line `FRAME NOT RECEIVED — [alt text]` — a
  failed reception, honestly logged in place, never a broken-image
  icon.
- **Reduced-motion variant.** Received state, static; mesh at 12%;
  hover still lightens the mesh by colour only (no scale anywhere).
- **Performance budget & mobile variant.** Scale on the `<img>`
  only (compositor transform), mesh fade is opacity; ≤3 frames
  resolving concurrently; budget ≤0.2ms/frame. Mobile: mesh density
  halved (every second triangle), scale origin 1.03 — the gesture
  survives at lower resolution.
- **Choreography timeline (v2).** Enters aim → t=0 §6.5 resolve
  begins and scale starts → t=150ms mesh fade begins → t=1200ms
  scale lands, mesh at 12% → received. Caption was sharp from t=0
  (paperwork never waits for the picture).
- **State matrix (v2).** *Rest:* received (after first resolve) or
  framed (before). *Hover:* leaned (mesh 8%, caption warms).
  *Focus:* the figure is not focusable unless it links (in cards,
  §6.12, the whole card is the link and focus leans the frame).
  *Active:* n/a. *Scrolled-past:* stays received. *Disabled:* n/a.
  *Touch:* no leaned state; received is the resting state.
- **Breakpoints (v2).** ≥1200px: frames up to 34rem wide, offset
  toward the dish per §4. 768–1199px: up to 28rem, centred in the
  measure. <768px: full-measure width, mesh halved, caption below
  (never overlaid — captions are paperwork and sit on the page, not
  on the signal).
- **Edge cases & failure modes (v2).** *Very tall image (portrait
  receiver shots):* frame caps at 70vh with `object-fit: cover`
  and the caption notes the crop (`FRAME CROPPED FROM 4:5`) —
  crops are admitted, like everything else here. *Slow network:*
  the frame box and mesh print immediately at 34%; the image fades
  in inside its frame when it arrives (opacity, 400ms) — the
  instrument shows its empty frame honestly while it waits.
- **Accessibility spec (v2).** Real `alt` text describing the
  photograph (the mesh is `aria-hidden` decoration over it, and the
  `FRAME NOT RECEIVED` fallback reuses the alt as its text). The
  mesh overlay never reduces caption contrast (caption sits outside
  the frame box). Focus state for linked frames: a thread outline
  at 2px, offset 3px — visible against the night at 8.6:1.
- **Tokens consumed (v2).** `--star-grey`, `--grey-faint`,
  `--signal-thread`, `--ease-focus`, `--font-log`.

### 6.10 The perfectly still star field

- **What & why.** Behind everything: ~190 stars, bone and grey at
  20–70% opacity — and they do not move. No twinkle, no drift, no
  parallax (depth factor ×0.00, §5). It belongs because stillness is
  this theme's texture discipline: in a page about listening, the
  sky refuses to perform. Every other element's motion is legible
  *because* the field behind it holds still; animate the stars and
  the whole page starts to shimmer like a screensaver, and the
  station becomes a planetarium gift shop.
- **Structure.** One inline SVG, `position: fixed; inset: 0`, stars
  as `<circle>`s (r 0.8–1.6) placed by a seeded generator at build
  time (the same sky on every load — a real sky does not reshuffle
  nightly). Density is higher above the horizon line and thins
  toward the footer, where the paperwork takes over. The SVG is
  pure markup: no script touches it after parse, and a CSS rule
  (`animation: none !important` on the layer) is shipped as a
  tripwire against future vandalism.
- **Motion spec.** Trigger: none. Duration: the life of the page.
  The field's parallax factor is 0.00 — it is one of the three night
  depths (§5) precisely by being the depth that does not move,
  against which the mesh (×0.06) and the desert shadow (×0.12) are
  measured.
- **States.** Still. (Printed / still / still — the state matrix
  below is the shortest in this document, deliberately.)
- **Content merge.** The stars are the only element that is pure
  setting — and they earn it by carrying the theme's argument: the
  things being listened *to* are up there, unmoving and unhurried,
  and the page's refusal to animate them is its thesis statement.
  They also do practical work: their stillness is the control group
  that makes the dish's 1.4s slew feel massive.
- **Failure fallback.** If the SVG fails to inline, the ground is
  `--night-desert` and the page loses texture, nothing else. No
  watchdog watches the thing that cannot move.
- **Reduced-motion variant.** Identical. This element is the
  reduced-motion variant of a sky, shipped as the default for
  everyone.
- **Performance budget & mobile variant.** One static SVG, ~190
  nodes, zero per-frame cost, composited once. Mobile: 110 stars
  (density thins, the argument doesn't).
- **Choreography timeline (v2).** t=0 printed → nothing → nothing →
  nothing. (The timeline is the spec.)
- **State matrix (v2).** *Rest:* still. *Hover:* still. *Focus:*
  not focusable; still. *Active:* n/a. *Scrolled-past:* fixed, so
  always present; still. *Disabled:* n/a. *Touch:* still.
- **Breakpoints (v2).** ≥1200px: 190 stars. 768–1199px: 150.
  <768px: 110, and none within the top 12vh (the headline's sky is
  kept emptier — even stillness is composed).
- **Edge cases & failure modes (v2).** *A future contributor adds a
  twinkle:* the quality gate (§10) greps the star layer for
  `animation`, `transition` and rAF references and fails the build —
  stillness is enforced by audit, not by trust. *High-DPI:* circles
  are vector; no retina variant exists or is needed. *Forced-colors
  mode:* the field may vanish entirely; the page must and does read
  perfectly on flat ground.
- **Accessibility spec (v2).** `aria-hidden`, no text, no contrast
  obligations (stars at 20% opacity are texture, and no information
  is carried by them). The field never sits behind text at densities
  that could shimmer against it — density thins behind the text
  measures by construction of the generator's exclusion zones.
- **Tokens consumed (v2).** `--dish-bone`, `--star-grey`,
  `--night-desert`.

### 6.11 Pointing index navigation

- **What & why.** The site's navigation is the night's schedule: a
  slim top bar carrying the station wordmark and three Log-register
  links (POINTINGS / RECEIVERS / REQUEST TIME), and below the hero,
  the pointing index — all five pointings as rows of number, name
  and coordinates, each row an anchor to its section. It belongs
  because a listening station does not have a "menu"; it has a
  schedule of where the dish will be, and navigation here is the
  visitor choosing where to listen next.
- **Structure.** Top bar: `position: sticky`, `--night-desert` at
  92% with a `--grey-faint` bottom hairline, wordmark in Instrument
  Serif at the Display floor (3rem is too large for a bar — the
  wordmark is the one licensed exception to the dead band, set in
  serif at 1.5rem as a *logotype*, a drawn mark rather than text;
  the gate whitelists exactly this one rule). Index rows: real
  `<a>` elements, grid of [number | name (serif, 3rem floor at
  ≥1200, wrapping under on small) | coordinates (mono) | lock tick].
  The current pointing's row carries the thread tick and the whisper
  `IN AIM`, driven by the same scroll channel as §6.2's locks.
- **Motion spec.** Trigger: scroll (for `IN AIM`) and hover/focus
  (for row states). Row hover: background lifts to `--night-panel`
  over 240ms `--ease-focus`, coordinates warm grey → bone-dim.
  `IN AIM` tick: lights by colour change only (300ms) when its
  pointing locks (§6.2) — the nav learns where the dish is at the
  same moment the reader does. Bar hide/show: the bar never hides;
  a listening station does not duck.
- **States.** Rest / hover (lifted, warmed) / focus (thread outline
  2px offset 3px, row lifted) / current (`IN AIM` tick lit) /
  visited (pointings already read show their tick dimmed to
  `--thread-dim` — the schedule remembers where the visitor has
  listened).
- **Content merge.** The index is not a sitemap pasted on top; its
  rows are the Schedule (§4) rendered as wayfinding — same order,
  same coordinates, same numbers as the sections they lead to. The
  visitor navigates by target, because that is the only geography
  the station has.
- **Failure fallback.** Plain anchors in a printed list: with no JS,
  every row still links, `IN AIM` simply never lights (the schedule
  is complete without its live marker). The bar's links are ordinary
  and crawlable.
- **Reduced-motion variant.** Hover lift becomes instant; tick
  changes remain colour-only (they already were). Nothing else
  changes — navigation was never theatrical.
- **Performance budget & mobile variant.** Colour/opacity only;
  ≈0ms/frame. Mobile: the bar condenses to wordmark + REQUEST TIME
  (the conversion survives every condensation; §15's build order
  protects it), index rows stack name over coordinates.
- **Choreography timeline (v2).** Page load → bar printed, index
  unlit → visitor scrolls → P-01 locks (§6.2) → its row's tick
  lights within the same frame budget → reading proceeds → ticks
  accumulate dimmed behind the current one → footer: all five rows
  either lit or dimmed — the index ends the page as a record of the
  visit's listening, rhyming with the log (§6.18).
- **State matrix (v2).** *Rest:* printed. *Hover:* lifted/warmed.
  *Focus:* outlined, lifted. *Active:* the row's anchor behaves
  natively (jump scrolls mark intervening pointings resolved, §6.5).
  *Scrolled-past:* the index section itself focus-resolves like any
  section (§6.5). *Disabled:* n/a. *Touch:* no hover lift; tap
  target per row ≥56px tall.
- **Breakpoints (v2).** ≥1200px: full rows, serif names at 3rem.
  768–1199px: names at the 3rem floor, coordinates right-aligned.
  <768px: rows stack (name, then coordinates, then tick), bar
  condenses as above, row height ≥56px.
- **Edge cases & failure modes (v2).** *A sixth pointing added:*
  the index renders from the Schedule — a new row appears with
  correct everything, or the build fails the figure audit (§10).
  *Long target names (Sagittarius A*):* the name wraps to two serif
  lines; the row grows; coordinates never truncate.
- **Accessibility spec (v2).** Real `<nav>` landmarks (bar and
  index labelled separately), links with full accessible names
  ("Pointing 3 — Sagittarius A*, RA 17h 45m 40.04s"), `aria-current`
  on the `IN AIM` row's link, skip-link in Log register at the very
  top (`SKIP TO THE POINTINGS`). Focus outlines thread at 8.6:1.
- **Tokens consumed (v2).** `--night-desert`, `--night-panel`,
  `--grey-faint`, `--signal-thread`, `--thread-dim`, `--star-grey`,
  `--bone-dim`, `--ease-focus`.

### 6.12 Observation log cards

- **What & why.** The listing form of the Schedule: one card per
  pointing, styled as an entry in the station's observation log —
  serif target name, mono coordinates, band, integration target, a
  mesh-framed thumbnail (§6.9), and a status stamp (`QUEUED` /
  `IN AIM` / `INTEGRATED`). Cards belong because a research station
  publishes its programme as a log, not a catalogue: these are not
  products with prices, they are nights with targets, and the card
  format keeps that grammar on listing pages, home-page indexes and
  search results alike.
- **Structure.** `<article>` per card on `--night-panel`, hairline
  border, no shadow (night has no shadows to cast — depth is the
  hairline and the panel step). Grid: thumbnail left (≥1200),
  stacked above (<1200). The status stamp is a bordered mono label,
  rotated −2°, in `--star-grey`; `IN AIM` stamps in
  `--signal-thread`. The whole card is one link (stretched-link
  pattern with a real `<a>` on the title) to the pointing's detail
  page, and the card is the focusable sender for §6.8's pulse
  (Enter sends from the card).
- **Motion spec.** Trigger: scroll (focus-in, §6.5) and the dish's
  lock (for stamps). Cards resolve with §6.5's grammar (900ms,
  stagger 90ms between cards in a row). Stamp change `QUEUED →
  IN AIM` when the corresponding pointing locks: the stamp's colour
  steps grey → thread over 300ms with a 120ms `--thread-pale` flash
  on arrival — paperwork acknowledging the instrument. No lift, no
  tilt, no shadow growth on hover: cards here are log entries, and
  log entries do not jump up to meet you; the lean (§6.7) sharpens
  the title and thins the thumbnail's mesh instead.
- **States.** Queued / in aim / integrated (stamp states, driven by
  the Schedule + clock, §6.6) / hover (title sharpens, mesh 8%,
  §6.9) / focus (thread outline on the card, title sharp) /
  printed (no-JS: stamps show the *scheduled* status from the
  Schedule — `QUEUED` for all but the night's current pointing,
  which the build stamps `IN AIM`).
- **Content merge.** A card contains nothing that is not in the
  Schedule or the pointing itself — it is the record's row, wearing
  a thumbnail. Its integration figure is the Schedule's target; its
  stamp is the clock's truth. A card with marketing copy in it has
  broken the log's grammar (§9).
- **Failure fallback.** Cards are DOM-complete; the stamp's live
  updates are JS decoration on a printed scheduled status.
  Thumbnail failure degrades per §6.9's `FRAME NOT RECEIVED` rule.
- **Reduced-motion variant.** Resolve and stamp theatrics removed;
  stamps change by colour only; cards print in their scheduled
  state.
- **Performance budget & mobile variant.** Cards share §6.5's
  resolve budget; stamps are two colour writes per lock. Mobile:
  single column, thumbnail 16:9 above the title, stamp inline
  beside the coordinates (never rotated — small paperwork stays
  level).
- **Choreography timeline (v2).** Card enters aim → resolve
  (900ms, staggered) → when its pointing locks elsewhere on the
  page, stamp warms (300ms + flash) → when the integration clock
  (§6.6) passes the pointing's target, stamp steps to `INTEGRATED`
  and the log (§6.18) gains its completion row — card, clock and
  log move as one record or not at all.
- **State matrix (v2).** *Rest:* scheduled stamp. *Hover:* leaned
  (§6.7). *Focus:* outlined + leaned instantly. *Active:* Enter/click
  sends §6.8's pulse and follows the link on second activation —
  no: one activation follows the link; the pulse is bound to the
  card's dedicated `SEND` whisper-button beside the stamp, so
  navigation and transmission never fight over the same click.
  *Scrolled-past:* stays resolved. *Disabled:* a pointing whose
  night is full (integration target met) shows `INTEGRATED` and its
  SEND button disables with the label `NIGHT COMPLETE` — disabled
  states here are facts, not UI moods. *Touch:* tap = click; SEND
  target ≥44px.
- **Breakpoints (v2).** ≥1200px: two-column card grid, thumbnail
  left 40%. 768–1199px: one column, thumbnail left 32%.
  <768px: stacked, stamp unrotated inline.
- **Edge cases & failure modes (v2).** *More pointings than the
  night holds (archive listings):* cards paginate as log pages
  (§11's pagination), 8 per page, stamps frozen at their night's
  final state — archive cards never pretend to be live. *Missing
  thumbnail in the record:* the card renders without a frame
  (coordinates take the space) rather than with a placeholder
  image — an empty frame is a claim; an absent frame is a fact.
- **Accessibility spec (v2).** One link per card (the title),
  accessible name includes target + coordinates; the SEND button is
  separately labelled ("Send a pulse from Pointing 2, Kepler-186f").
  Stamp text is real text (never an image), grey stamp 4.8:1,
  thread stamp 8.6:1. Card focus outline 2px thread, offset 3px.
- **Tokens consumed (v2).** `--night-panel`, `--grey-faint`,
  `--star-grey`, `--signal-thread`, `--thread-pale`, `--font-log`,
  `--ease-focus`, `--ease-settle`.

### 6.13 Receiver & band table

- **What & why.** The station's published instrument table: every
  receiver, its band, its tuned line, its system temperature, its
  status. It belongs because deep-tech audiences believe tables, not
  adjectives — and because this table is the Schedule's other half:
  §4 says where the dish points; this says what it can hear when it
  gets there. The proposal form's band choices (§6.15) are this
  table's rows, so the table is also a form control's documentation.
- **Structure.** A real `<table>` in Log register on
  `--night-panel`, hairline row rules (`--grey-faint`), no zebra
  striping (the night does not alternate). Columns: RECEIVER / BAND /
  LINE / Tsys / STATUS. Reference build rows (the record the form
  reads):

  | Receiver | Band | Line | Tsys | Status |
  |---|---|---|---|---|
  | L-1 | 1,420.406 MHz | Hydrogen (H I) | 18 K | ON SKY |
  | L-2 | 1,612.231 MHz | Hydroxyl (OH) | 21 K | ON SKY |
  | L-3 | 1,665.402 MHz | Hydroxyl (OH) | 21 K | ON SKY |
  | L-4 | 1,667.359 MHz | Hydroxyl (OH) | 22 K | STANDBY |
  | S-1 | 2,380.000 MHz | Quiet band | 26 K | MAINTENANCE |

  The Wow! field's candidate frequency (1,420.456 MHz) is L-1's
  second printed tuning, footnoted as such — the ambiguity lives in
  the table, where ambiguities are filed.
- **Motion spec.** Trigger: scroll. The table focus-resolves as one
  block (§6.5, 900ms) — rows never stagger (a table is read as a
  unit; staggering data is vandalism). The `ON SKY` status cells
  carry the only life: a 3px thread dot that breathes opacity
  55%→100% over 4s `--ease-drift` — slow enough to be a state, not
  a blink. Row hover: background lifts one step and the row's band
  figure warms to bone (240ms).
- **States.** Printed / resolved / row-hover / row-focus (a row
  containing the focused cell link, if any) / maintenance (S-1's
  row prints in `--star-grey` throughout with its status in
  `--control-red` *text-adjacent dot + label* per the red
  discipline: the word MAINTENANCE is grey text; the red is a dot
  beside it, never the word).
- **Content merge.** The table is the form's band list, the
  pointings' band column and the status strip's receiver line, all
  rendered once from the receiver record. Change a Tsys here and
  the form's options change — one record, three printings (§10
  audits the agreement).
- **Failure fallback.** A table needs no fallback: it is text in a
  grid, printed whole, sharp, with no JS. The breathing dot is a
  CSS animation on an enhancement class; without it the dot is
  static at 80%.
- **Reduced-motion variant.** Dot static at 80%; resolve removed;
  the table prints. (Data tables are where reduced motion should
  feel like nothing happened.)
- **Performance budget & mobile variant.** One block resolve; the
  dot is one CSS animation. Budget ≈0ms/frame. Mobile: the table
  scrolls horizontally inside a hairline frame with the RECEIVER
  column sticky — coordinates and figures are never truncated or
  stacked into cards; a table that becomes cards has stopped being
  a record.
- **Choreography timeline (v2).** Enters aim → block resolve 900ms
  → dots begin their 4s breath (offset per row by 700ms so the
  column never pulses in unison — instruments do not synchronise
  their breathing) → steady state.
- **State matrix (v2).** *Rest:* printed/resolved. *Hover:* row
  lift + figure warm. *Focus:* cells are text; if a build links a
  receiver name to its detail page, the link takes the standard
  thread outline. *Active:* n/a. *Scrolled-past:* dots keep
  breathing only while the table is ≥10% visible (observer-gated,
  like §6.4). *Disabled:* the MAINTENANCE row is the disabled state,
  expressed as content. *Touch:* no hover; the table scrolls.
- **Breakpoints (v2).** ≥1200px: full table in the 72rem measure.
  768–1199px: Tsys column tightens (label shortens to `T/K` in the
  header, values unchanged). <768px: horizontal scroll frame,
  sticky first column, min cell padding 0.75rem — figures keep
  their tabular alignment at every size.
- **Edge cases & failure modes (v2).** *A receiver added:* one
  record row → table row + form option + audit update; a receiver
  typed directly into the form's HTML is a §10 failure. *Status
  changes mid-visit (S-1 returns):* statuses are the night's
  printed record and do not live-update — the table is tonight's
  edition, and its footer line says so (`AS PRINTED AT DUSK`).
- **Accessibility spec (v2).** Proper `<th scope="col">`, caption
  `RECEIVERS — AS PRINTED AT DUSK` as the table's accessible name.
  Status is text, never dot-alone. Grey body cells 4.8:1 minimum;
  figures in `--bone-dim` 8.8:1. The horizontal-scroll frame on
  mobile is focusable with a visible outline and an aria-label, so
  keyboard users can scroll the record too.
- **Tokens consumed (v2).** `--night-panel`, `--grey-faint`,
  `--font-log`, `--star-grey`, `--bone-dim`, `--signal-thread`,
  `--control-red`, `--ease-focus`, `--ease-drift`.

### 6.14 Tonight at the array — status strip

- **What & why.** A single hairline strip — under the hero on the
  home page, at the top of programme pages — carrying the night's
  working facts in one line of whispers: local sidereal time, wind,
  temperature, humidity, the receiver on sky, and the recording dot.
  It belongs because a real station's every screen carries exactly
  this line; it is how the visitor knows the page is a workplace and
  not a brochure. It is also the counters' (§6.6) second printing.
- **Structure.** One `<div>` strip, Log register 0.6875rem labels
  with 0.8125rem values, separated by `--grey-faint` ticks. Fields:
  `LST` (computed, §below), `WIND 14 KM/H NW`, `TEMP 6.2°C`,
  `HUM 31%`, `RECEIVER L-1 ON SKY`, the integration/SNR pair
  (§6.6), and the red recording dot with its label `REC`. The
  weather fields are the night's printed values from the Schedule's
  night block — they change at dusk, not per refresh; LST and the
  counters are the live fields.
- **Motion spec.** Trigger: time. LST advances by formula from the
  visitor's clock and the station's printed longitude (the reference
  build prints `LON 115.92°E` in the strip's end cap and computes
  LST by the standard GMST formula — the strip shows its working).
  Updates at 1Hz, plain digit changes, no settle animation (a clock
  in a status strip is furniture). The REC dot breathes on §6.13's
  4s cycle, offset so strip and table never breathe together.
- **States.** Live / held (tab hidden: LST recomputes true on
  return — sidereal time does not pause for a backgrounded tab) /
  printed (no-JS: LST field shows the dusk-printed value with the
  label `LST AT DUSK` — the label changes so the static value never
  lies about being live).
- **Content merge.** Every field is a fact the rest of the page
  uses: the receiver named here is §6.13's `ON SKY` row and §4's
  P-01 band's instrument; the counters are §6.6's. The strip is the
  page's front page — a summary that must reconcile with the paper
  inside, audited in §10.
- **Failure fallback.** No-JS prints the dusk edition (above). LST
  computation fault: the field falls back to the visitor's local
  time labelled `LOCAL` — a wrong-labelled clock is a defect; a
  relabelled one is an instrument admitting its mode.
- **Reduced-motion variant.** REC dot static; everything else is
  data updates, unchanged.
- **Performance budget & mobile variant.** Two 1Hz text writes;
  ≈0ms. Mobile: the strip wraps to two lines and sheds fields in a
  published order — humidity first, then wind, then temperature;
  LST, receiver, counters and REC are never shed (they are the
  strip's reason to exist).
- **Choreography timeline (v2).** t=0 dusk values printed → JS
  takes LST live within one frame (label flips `LST AT DUSK` →
  `LST`) → 1Hz ticks → REC breath offset from §6.13 by 2s → steady
  state for the visit.
- **State matrix (v2).** *Rest:* live. *Hover:* none (the strip is
  read, not operated; §6.6's caption hover belongs to the hero
  printing of the counters, not this one). *Focus:* fields are
  text; the strip is reachable in reading order. *Active:* n/a.
  *Scrolled-past:* sticky variant on programme pages keeps the
  strip at top (it is the workplace's clock); on the home page it
  scrolls away and the counters' hero printing remains the live
  one — one state object, so both printings always agree.
  *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: one line. 768–1199px: one line,
  humidity shed. <768px: two lines, shed order applied, REC and
  LST on the first line always.
- **Edge cases & failure modes (v2).** *Visitor in a timezone the
  formula mishandles (DST edges):* LST derives from UTC internally,
  so DST cannot touch it — the formula's inputs are printed in the
  build notes for the §10 audit. *Extreme weather in the night
  block (wind 90 km/h):* the strip prints it and P-01's card
  (§6.12) gains the stamp `STOWED — WEATHER` — the strip is where
  the page learns the dish cannot aim tonight, and the choreography
  (§13) has a weather variant for exactly this.
- **Accessibility spec (v2).** The strip is a `<section>` with
  aria-label `Tonight at the array`; fields are a definition list
  so label/value pairing survives linearisation. `aria-live` off
  (a ticking strip must not narrate itself). The REC dot is paired
  with its text label (§2 red discipline).
- **Tokens consumed (v2).** `--font-log`, `--star-grey`,
  `--bone-dim`, `--grey-faint`, `--control-red`, `--signal-thread`,
  `--ease-drift`.

### 6.15 Request-a-pointing form — the proposal

- **What & why.** The conversion act of a listening station is not a
  purchase; it is a *proposal*: request observing time. The form
  asks for what a time-allocation committee asks for — who you are,
  what you want to listen to, on which receiver, for how long, and
  why — and its confirmation is a numbered proposal entered in the
  signal log (§6.18) stamped `IDENTIFIED — YOURS.` It belongs
  because it is the one loud thing a visitor may do here, and the
  theme makes it feel like what it is: asking a 64-metre instrument
  to spend its night on your question.
- **Structure.** A single-column form in Log register on
  `--night-panel`, fields: NAME / INSTITUTION / TARGET (select: the
  five scheduled targets + `A NEW TARGET`) / RA + DEC (two mono
  inputs, shown when NEW TARGET is chosen; pre-filled and locked to
  the Schedule's values when a scheduled target is chosen — the
  form teaches the record by refusing to let you mistype it) /
  RECEIVER (select from §6.13's record, MAINTENANCE row disabled
  with its reason printed) / INTEGRATION REQUESTED (select 1 / 2 /
  4 / 8 H) / JUSTIFICATION (textarea, with the whisper guidance
  `ONE PARAGRAPH. THE COMMITTEE READS AT NIGHT.`). Submit button:
  full-width hairline-bordered mono `SUBMIT FOR THE NIGHT` — no
  filled button exists in this theme (§11).
- **Motion spec.** Trigger: interaction. Field focus: the field's
  label warms grey → thread and a 1px thread rule draws under the
  input over 300ms `--ease-settle` (the instrument noting where you
  are). Target select change: RA/Dec fields crossfade values over
  200ms — paperwork updating, not performing. Submit: the button
  label steps `SUBMIT FOR THE NIGHT` → `LOGGING…` for exactly the
  §6.8 ring's duration (900ms) → confirmation replaces the form
  (below). No spinner exists; waiting is represented by the trace
  (§6.4) idling in the confirmation block.
- **States.** Rest / focused (label warm, rule drawn) / filled
  (label rests at bone-dim — completed paperwork sits darker) /
  error (below) / submitting (900ms, inputs disabled) / confirmed
  (form replaced by the receipt: proposal number, the pointing as
  requested, and the log stamp; a `FILE ANOTHER` whisper link
  restores a fresh form).
- **Content merge.** Every choice in the form is a record the page
  has already published — targets from §4, receivers from §6.13,
  integrations in the Schedule's own units. The confirmation writes
  into §6.18's log, the page's own record of the visit: the
  visitor's proposal becomes one of the night's signals, which is
  precisely the station's promise to proposers.
- **Failure fallback.** The form is a real `<form>` with a real
  action: with no JS it submits to the server endpoint and the
  confirmation is a server-rendered page in the same theme (receipt
  block, proposal number from the server's count). Client-side
  enhancement never becomes a single point of failure for the
  site's one conversion.
- **Reduced-motion variant.** Rule-draw and crossfades become
  instant; the 900ms logging beat shortens to 200ms (waiting is
  motion's cousin); confirmation identical.
- **Performance budget & mobile variant.** Form interactions are
  colour/width writes; ≈0ms/frame. Mobile: identical single column
  (it was always single column — forms at a listening station are
  filled in slowly, at a desk), inputs at 1rem to prevent iOS zoom
  — the one licensed Log-register size exception, recorded here so
  the §10 dead-band grep whitelists `input` selectors.
- **Choreography timeline (v2).** Visitor completes fields (rules
  draw per focus) → submit → t=0 label `LOGGING…`, inputs disable →
  t=900ms log row appends in §6.18 (`IDENTIFIED — YOURS`) → form
  crossfades 300ms to the receipt showing proposal № (printed count
  + 1, §8.3) → receipt's trace idles → end state persists (no
  auto-dismiss; a proposal is not a toast).
- **State matrix (v2).** *Rest:* printed form. *Hover:* button
  border warms to thread (the only hover a button gets). *Focus:*
  label + rule (above); focus outline is the drawn rule plus a 2px
  thread outline on the input itself for keyboard clarity.
  *Active:* submitting state. *Scrolled-past:* n/a (the form is a
  destination, §13 beat 9). *Disabled:* MAINTENANCE receiver option
  disabled with reason; submit disabled only during the 900ms beat.
  *Touch:* targets ≥48px; selects are native (the station does not
  rebuild a select).
- **Breakpoints (v2).** ≥1200px: form measure 40rem, beside it the
  night's remaining-time readout (23 h programme, §4 — the form
  shows the budget it is asking against). 768–1199px: readout moves
  above the form. <768px: single column, readout as a whisper line
  above the first field.
- **Edge cases & failure modes (v2).** *Validation errors:* inline,
  in the instrument's voice (§12), each error a mono line under its
  field with the red rule (§2: the rule is red, the words are bone)
  — `RA MUST BE HH MM SS.S — THE DISH CANNOT GUESS.` Focus moves to
  the first error; errors are listed in a summary at the form's top
  for screen readers. *Duplicate submission:* the 900ms disabled
  window + a proposal-token make double-filing impossible; a second
  click is absorbed like §6.8's throttle. *Justification overlong:*
  the field accepts it; the counter whispers the committee's real
  limit (`THE COMMITTEE READS 200 WORDS AT NIGHT`) past 200 words
  without truncating — guidance, not a wall.
- **Accessibility spec (v2).** Every input has a real `<label>`;
  hints and errors are `aria-describedby`-linked; the error summary
  is `role="alert"` on submit. Required fields are marked in text
  (`REQUIRED` whisper), never by colour or asterisk alone. The
  receipt is focus-targeted on arrival (`tabindex="-1"`) so
  keyboard and screen-reader visitors land on their proposal
  number. Contrast: labels grey 4.8:1 minimum, values bone 14:1,
  error text bone on panel with the red rule as supplement, never
  the sole signal.
- **Tokens consumed (v2).** `--night-panel`, `--grey-faint`,
  `--font-log`, `--star-grey`, `--bone-dim`, `--dish-bone`,
  `--signal-thread`, `--control-red`, `--ease-settle`.

### 6.16 Re-pointing transition & the acquiring loader

- **What & why.** Moving between pages is re-pointing the dish: the
  current page's dish slews to parked, the trace sweeps once, and
  the new page resolves by focus (§6.5) with its own dish already
  travelling to its first aim. The loader state — shown only if the
  new page's content is not ready within 300ms — is *acquiring*: the
  destination printed at 70% contrast under an idling trace, with
  its coordinates slewing (§6.2). It belongs because a listening
  station has no spinners and no blank screens; it has slewing and
  acquiring, which are honest names for waiting.
- **Structure.** A client-side layer over ordinary multi-page
  navigation (progressive enhancement: links remain links; the
  transition intercepts only when JS and the router are healthy).
  The overlay is the outgoing page's own dish + trace, reused — no
  separate loader DOM exists to drift out of theme. The acquiring
  state renders the destination's hero skeleton as printed text at
  70% (its real headline and readout, unresolved) — never grey
  boxes: this theme's skeleton is the page, unfocused.
- **Motion spec.** Trigger: navigation. Outgoing: dish slews to
  parked over 700ms `--ease-slew` (faster than a pointing slew —
  parking is a smaller thought), trace sweeps one blip 500ms.
  Incoming: focus resolve per §6.5 with the hero headline *already
  tuned* (the tuning ritual is a first-visit ceremony; internal
  arrivals resolve in 900ms flat). Hard ceiling: 1200ms from click
  to interactive destination, enforced by watchdog — past it, the
  destination prints as-is, transition abandoned mid-slew if
  necessary.
- **States.** Idle / departing (slew to parked) / acquiring (only
  if >300ms) / arriving (resolve) / abandoned (watchdog path —
  plain navigation, no shame attached).
- **Content merge.** The transition uses the page's own instruments
  rather than a branded overlay: the dish the visitor has been
  watching does the travelling. The destination's acquiring state
  shows the destination's *actual* coordinates slewing — the wait
  itself is spent acquiring the next target, which is the station's
  real between-pointings activity.
- **Failure fallback.** Any fault — router error, slow network,
  watchdog — degrades to ordinary browser navigation. The
  transition is the most expendable element in the theme and is
  built to be abandoned; §14's cut order removes it first.
- **Reduced-motion variant.** No slew, no sweep: instant navigation
  (the browser's own), destinations print sharp. Reduced-motion
  visitors never meet the acquiring state unless the network forces
  it, and then it is static printed text.
- **Performance budget & mobile variant.** Reuses existing DOM; the
  1200ms ceiling is the budget. Mobile: the slew is replaced by the
  trace sweep alone (300ms) — small screens travel light.
- **Choreography timeline (v2).** t=0 click → dish departs toward
  parked → t=300ms acquiring threshold (if content unready, printed
  skeleton fades in at 70%) → content ready → resolve 900ms →
  interactive; watchdog deadline t=1200ms caps all of it.
- **State matrix (v2).** *Rest:* idle. *Hover:* n/a. *Focus:*
  during transition, focus is held on a visually-hidden
  `NAVIGATING` status and delivered to the destination's `<h1>`
  (tabindex −1) on arrival — keyboard visitors are never left
  focused on a departed page. *Active:* departing/acquiring.
  *Scrolled-past:* n/a. *Disabled:* if the router is unhealthy, the
  layer disables itself for the session (one fault is enough).
  *Touch:* identical, with the mobile motion reduction above.
- **Breakpoints (v2).** ≥1200px: full slew transition.
  768–1199px: slew at 600ms. <768px: trace-sweep only, 300ms,
  ceiling unchanged at 1200ms.
- **Edge cases & failure modes (v2).** *Back button:* the browser's
  own history wins; the layer never traps or replays transitions
  for popstate (arrivals by history print sharp instantly).
  *Mid-transition second click:* absorbed; the first destination
  stands. *Prefetch available:* if the destination is prefetched,
  the departing beat shortens to 350ms — the dish does not perform
  a full park for a journey already made.
- **Accessibility spec (v2).** A polite live region announces
  `NAVIGATING — [destination name]` once, and arrival moves focus
  as above. The acquiring skeleton's text is real text, readable by
  AT in its unresolved visual state (visual softness never gates
  the DOM, §6.5's rule). No content is ever *only* in the overlay.
- **Tokens consumed (v2).** `--ease-slew`, `--ease-pulse`,
  `--ease-focus`, `--signal-thread`, `--dish-bone`.

### 6.17 The lost pointing — 404

- **What & why.** A wrong URL at a listening station is a pointing
  at coordinates where nothing was scheduled: the dish parked, the
  trace flat at noise, and the requested path printed as a target
  that does not resolve. The page says so in Display register —
  `No signal at these coordinates.` — and then does the station's
  one helpful thing: it prints the five pointings that *do* exist,
  sharp, with their coordinates, as links. It belongs because even
  the error page keeps the theme's cosmology: absence, honestly
  reported, with the schedule as the way back.
- **Structure.** The standard stage, stripped: dish parked (static,
  §6.1's reduced rendering), a short trace (§6.4's SVG print, flat
  noise, no pulses), the statement in serif, the requested path
  rendered as a failed readout (`TARGET — [path]` in mono, its lock
  tick unlit, stamped `NO LOCK`), and the pointing index (§6.11)
  reused whole as the recovery list.
- **Motion spec.** Trigger: load. Choreography is specified as
  *nearly none*: at t=2000ms the trace lets one pulse blip through
  — the station checking the empty frequency once, out of diligence
  — and thereafter stillness. The statement prints sharp at load
  (no tuning ritual: an error page does not make a lost visitor
  wait 6 seconds for the bad news; the law's guarantee is honoured
  by immediacy here).
- **States.** Printed / checked (after the single t=2000ms pulse) /
  still. There are no others; the page's restraint is its state
  machine.
- **Content merge.** The recovery list is the real Schedule (§4) —
  the same rows as navigation, so the 404 teaches the site's
  geography while apologising for its absence. The failed readout
  names the actual requested path: the error is specific, not a
  generic shrug.
- **Failure fallback.** The 404 is a static page by construction;
  its only JS beat is the single pulse, whose absence changes
  nothing. Server-rendered, it works with every enhancement dead.
- **Reduced-motion variant.** No pulse. Identical otherwise.
- **Performance budget & mobile variant.** The cheapest page on the
  site; budget ≈0. Mobile: identical layout, index stacked (§6.11's
  small-breakpoint form).
- **Choreography timeline (v2).** t=0 everything printed sharp,
  dish parked → t=2000ms one trace pulse → stillness → visitor
  chooses a real pointing (or doesn't; the page does not pursue
  them).
- **State matrix (v2).** *Rest:* printed. *Hover:* index rows lean
  per §6.11/§6.7. *Focus:* the first index link is reachable in
  two tabs from the statement; focus outlines standard. *Active:*
  n/a. *Scrolled-past:* n/a (the page is one screen and a list).
  *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: statement at section-statement
  size, index full rows. 768–1199px: same, tighter air (a lost
  visitor gets 12vh gaps, the one licensed tightening — mercy is a
  layout value here). <768px: stacked index, statement at the 3rem
  floor.
- **Edge cases & failure modes (v2).** *A path that almost matches
  a pointing (typosquat of `/pointings/tau-ceti`):* the failed
  readout prints the requested path and, if a slug edit-distance of
  ≤2 matches a scheduled target, one extra whisper line — `NEAREST
  SCHEDULED POINTING — P-01, TAU CETI` — as a link. Helpful, in
  register, and never an auto-redirect (the station suggests; it
  does not grab the dish). *Truly deep garbage paths:* printed
  truncated at 80 characters with an ellipsis in the readout —
  the only truncation the theme permits, because a URL is data
  about an error, not content.
- **Accessibility spec (v2).** The statement is the `<h1>`; the
  failed readout is text; the HTTP status is a real 404 (the theme
  never soft-404s — an instrument does not pretend a lock). Reading
  order: statement → what was requested → the five real pointings.
- **Tokens consumed (v2).** `--dish-bone`, `--font-display`,
  `--font-log`, `--star-grey`, `--signal-thread`, `--ease-pulse`.

### 6.18 Footer signal log

- **What & why.** The footer's whole content: a log of every pulse
  fired during the visit — ambient (§6.4), entrance (§6.3),
  click-sent (§6.8) and the visitor's own proposal (§6.15) — each
  row timestamped with the real local time, sourced, and stamped
  `UNIDENTIFIED — PROBABLY US.` (The proposal row alone is stamped
  `IDENTIFIED — YOURS.` — the visit's one identified signal is the
  visitor.) It is the original entry's anti-slop jewel and the
  theme's signature: the footer is a genuine record of *this*
  visit, and its one joke is placed where only someone who stayed
  will find it. A single signal-thread line runs along the log's
  head, and each recorded pulse adds one blip to it — the log draws
  its own trace of the night.
- **Structure.** A `<footer>` on `--night-deep`: a whisper heading
  (`SIGNAL LOG — THIS VISIT`), the thread-line SVG (a polyline that
  extends one blip per row), and a table-like list of rows:
  `HH:MM:SS` / source (`AMBIENT`, `SENT — FROM P-02`, `ENTRANCE`,
  `PROPOSAL № 1,209`) / stamp. Below the rows, the station's
  ordinary footer paperwork (address, funders, © line) in the same
  Log register — the log does not evict the legal text; it outranks
  it visually by sitting above it. Rows are capped at 40; beyond
  that, the oldest ambient rows are summarised into one line
  (`+N EARLIER PULSES, UNIDENTIFIED`) — sent and proposal rows are
  never summarised away.
- **Motion spec.** Trigger: pulse events (the log is written by
  §6.3, §6.4, §6.8, §6.15 — it has no triggers of its own). Row
  append: the row fades-resolves (§6.5 grammar, 600ms) and the
  thread line draws its new blip (stroke-dashoffset, 400ms
  `--ease-pulse`) — the only place line-draw and append coincide.
  If the footer is off-screen when a row lands (it usually is), no
  animation runs; the row is simply *there* when the visitor
  arrives, which is how logs work.
- **States.** Empty (printed line: `NO PULSES YET. THE NIGHT IS
  YOUNG.`) / recording (rows accumulating) / capped (summary line
  present) / printed (no-JS: the empty state plus the night's
  *scheduled* rows from §4 stamped `SCHEDULED` — the paper log of
  the night's plan, honest about being a plan).
- **Content merge.** The log is the visit's memoir written by the
  page's other elements; delete the pulses elsewhere and the log is
  empty, delete the log and the pulses lose their meaning. Its
  timestamps are real (the visitor's clock, labelled `LOCAL TIME`
  in the heading) — the one place the theme uses the visitor's time
  rather than the station's, because the log is *theirs*.
- **Failure fallback.** No-JS prints the scheduled edition (above).
  Partial JS failure (a writer throws): rows already written
  persist (they are DOM, not state); the log degrades to a partial
  record — which, the theme notes, is what real logs are.
- **Reduced-motion variant.** Rows append instantly, the thread
  line's blips appear drawn. The record is untouched; only its
  handwriting slows down.
- **Performance budget & mobile variant.** One row append per pulse
  (rare by design); the thread SVG stays ≤41 blips. Budget ≈0ms.
  Mobile: rows stack time over source; the stamp never truncates
  (it is the joke and the point; it wraps if it must).
- **Choreography timeline (v2).** Hero's fourth entrance pulse
  lands (≈t=4800ms) → the log's first row writes (`ENTRANCE —
  ACQUISITION COMPLETE`) and the footer becomes the page's final
  live element → ambient and sent rows accumulate through the visit
  → proposal row (if any) writes at §6.15's t=900ms → the visitor
  reaches the footer and reads their own night back.
- **State matrix (v2).** *Rest:* as printed. *Hover:* rows warm to
  bone-dim (a reader leaning over the logbook, §6.7's spirit at
  table scale). *Focus:* rows are text; the footer links
  (paperwork) take standard outlines. *Active:* n/a.
  *Scrolled-past:* n/a — the log is the bottom; there is no past
  it. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: three-column rows. 768–1199px:
  stamp moves under the source. <768px: fully stacked rows,
  thread line full width, heading wraps.
- **Edge cases & failure modes (v2).** *A very long visit (40+
  pulses):* the cap and summary rule (above) — and the summary
  line itself is stamped `UNIDENTIFIED — PROBABLY US.`, because at
  that point, it was. *Clock skew (visitor's clock wrong):* the
  log prints the visitor's time as theirs; the heading's `LOCAL
  TIME` label keeps the page honest about whose clock it was.
  *Privacy:* the log is session-only DOM — nothing is stored,
  nothing leaves the page; the footer's paperwork line says so
  (`THIS LOG IS KEPT ONLY HERE, ONLY TONIGHT.`).
- **Accessibility spec (v2).** The log is a real `<table>` with a
  caption (`Signal log — this visit`); row appends are announced
  only for visitor-caused rows (§6.8's polite announcement) —
  ambient rows never interrupt a screen reader's night. Stamps are
  text at 4.8:1 minimum (grey) and 8.6:1 (the proposal's thread
  stamp). The thread-line SVG is `aria-hidden`; its information is
  the rows themselves.
- **Tokens consumed (v2).** `--night-deep`, `--font-log`,
  `--star-grey`, `--bone-dim`, `--signal-thread`, `--thread-dim`,
  `--ease-pulse`, `--ease-focus`.

## 7. Page application map

| Page type | How the theme plays out |
|---|---|
| **Home** | The full night: status strip (§6.14) → hero (dish parked, headline tuning §6.3, trace §6.4, counters §6.6) → pointing index (§6.11) → the five pointings as acts around the sticky dish (§6.1, §6.2, §6.5) → receiver table (§6.13) → proposal form (§6.15) → signal log footer (§6.18). The home page *is* one night's listening, top to bottom. |
| **Programme / listing** | Observation log cards (§6.12) for the season's nights, each card a scheduled night with its pointings; archive nights paginate as log pages (§11). The dish appears once, small and parked, in the header — on listing pages the paperwork leads. |
| **Pointing detail** | One target, whole page: readout and name at Display scale, the dish aimed and locked for the entire page (no re-aiming — the page *is* one pointing), mesh-framed photography (§6.9), past nights' results printed as log excerpts (including the null results — especially the null results), and the proposal form pre-set to this target (§6.15). |
| **About / the station** | The institution in the same grammar: history as a log (dated mono entries, serif statements between them), the array's facts in tables (§6.13's treatment), staff listed as the night crew with their shifts. No separate "brand" styling exists to switch to. |
| **Request time (conversion)** | §6.15's form as a full page: the night's remaining budget printed beside it, the committee's process as three log entries (RECEIVED / READ AT NIGHT / ANSWERED BY DAWN — with real turnaround figures from the record, or none printed), the form, and the log footer so the confirmation's stamp has its home. |
| **News / results** | Results are log entries, dated and stamped (`CONFIRMED` is a stamp this page type may finally use — when the record says so, and the record is linked). A null result and a confirmation get identical typography; the theme does not let typography editorialize data. |
| **404** | The lost pointing (§6.17). |
| **Search** | Results as readout lines — target, coordinates, one line of context — resolving by focus as they enter. No thumbnails; search is an instrument query, and its results print like one. |

## 8. Worked examples

The reference client throughout: the **Meridian Listening Station**,
a SETI institute running the §4 schedule. All figures below are the
Schedule's and the receiver record's — nothing is invented per
example.

### 8.1 The hero — first light of the night shift

**What the visitor gets.** Darkness and a horizon. The dish parked
at centre-frame, 60vw of bone against the desert; above it the
standfirst, sharp, in Log register: `MERIDIAN LISTENING STATION —
EST. 1987 — CURRENTLY LISTENING.` Below the horizon line, the trace
idles. The headline — `The universe is under no obligation to be
loud.` — is a blur the visitor can almost read.

**Scroll/timing timeline.** t=0: page printed whole (headline sharp
in the DOM, dish parked, counters at 03:12:44 / 4.2, status strip
showing dusk values). JS arms within a frame: headline to blur 3px /
55%. t=900ms: the trace's first acquisition blip; headline steps to
2.25px / 66%. t=2200ms, 3500ms: steps two and three. t=4800ms: the
fourth blip; the headline lands at full sharpness ≈t=5700ms, and in
the same beat the signal log (§6.18) writes its first row —
`ENTRANCE — ACQUISITION COMPLETE` — in a footer the visitor will not
see for minutes. The counters have ticked four honest seconds. The
dish has not moved: the hero is parked, because the night's first
pointing has not begun, and the page does not pretend otherwise.

**Build notes.** The headline's tuning is §6.3 with the §5 watchdog
at 6000ms; the standfirst and counters never arm (§6.5 excludes the
hero paperwork block — paperwork does not perform). On
`prefers-reduced-motion`, the hero arrives complete: sharp headline,
printed trace, true counters.

### 8.2 Mid-page — Pointing 01, Tau Ceti

**What the visitor gets.** After 24vh of desert, the pointing
arrives the way the dish does: slowly. The dish — sticky at
centre-frame since the index — begins its slew from parked toward
−6° / +3°. On the left of the stage, P-01's coordinate block enters
the aim: `RA 01H 44M 04.08S — DEC −15° 56′ 13.9″ — 1,420.406 MHZ —
INTEGRATION TARGET 4H` slews and locks digit by digit (§6.2) as the
dish settles. Then the name resolves into focus in Instrument
Serif: `Tau Ceti, listening for a neighbour.` Beneath it, Log prose
at 56ch: eleven point nine light-years, a star enough like ours to
make the silence interesting, four hours of tonight's twenty-three
budgeted to it — the arithmetic printed, not implied. A mesh-framed
photograph (§6.9) of the dish at dawn, captioned with its
provenance, resolves at the pointing's right.

**Scroll timeline.** Reading line approaches → dish channel starts
slewing (lerp 0.055) → readout trigger at 55%: digits hunt 1400ms,
locking left-to-right → dish lock event and final digit land
together ≈1.4s after the slew began → name and prose focus-resolve
(900ms, staggered 90ms) inside the same window → photograph resolves
1200ms, mesh settling to 12% → the pointing rests, fully sharp, and
the visitor reads it in stillness while the counters (§6.6) — whose
caption now names P-01 — creep in the strip above. Scroll on, and
the dish begins its longer travel toward Kepler-186f's +4° / +6°.

**Build notes.** The pointing's three systems (dish, readout, text)
share the one lerped channel (§5); nothing here has its own scroll
listener. Reverse scroll re-runs the hunt at 700ms (§6.2) and the
dish returns along the same interpolation — the visitor scrolling
back up is the dish coming back, not an animation rewinding.

### 8.3 Conversion — a proposal for the Wow! field

**What the visitor gets.** The request-time page. Beside the form
(§6.15), the night's budget as printed paperwork: `PROGRAMME
TONIGHT — 23 H SCHEDULED — PROPOSALS LOGGED THIS SEASON: 1,208`.
The visitor selects `P-05 — THE WOW! FIELD` from the target list;
the RA/Dec fields fill themselves from the Schedule — `19H 25M 31S
± / −26° 57′ ±` — and lock, with the whisper beneath: `COORDINATES
FROM THE SCHEDULE. THE FIELD'S TRUE POSITION IS UNCERTAIN; THE
DISH WILL SEARCH THE ERROR ELLIPSE.` They choose receiver L-1 (the
form notes its second tuning, 1,420.456 MHz, unprompted — the table
in §6.13 taught the form that), request 2 H, and write their
paragraph.

**Submit timeline.** Click → button reads `LOGGING…`, inputs hold →
900ms (the §6.8 duration: the proposal travels at the speed of a
pulse) → in the footer, a row appends: the real local time /
`PROPOSAL № 1,209 — P-05, THE WOW! FIELD` / `IDENTIFIED — YOURS.` →
the form crossfades to the receipt: the same number, the pointing
as requested, and one serif line at the Display floor: `The dish
will spend two hours on your question.` The season count the next
visitor sees is 1,209 — the receipt, the log and the budget line
are one record in three printings, and §10's audit greps that they
agree.

**Build notes.** The number is `printed_count + 1` computed from
the same record that prints the budget line — never a separate
counter that could drift. No-JS path: the server issues the number
and renders the same receipt page; the stamp text is identical, so
a proposal's dignity does not depend on JavaScript.

## 9. Anti-slop — what makes THIS theme look cheap

1. **Twinkling stars.** The instant the sky animates, the station
   becomes a screensaver. *Cure:* §6.10's stillness, enforced by the
   §10 grep audit, not by good intentions.
2. **A glowing green "matrix" anything.** Signal colour here is
   thread amber on desert night; green-on-black is a film reference,
   and this theme references instruments, not films. *Cure:* the
   palette has no green; a build that introduces one has left the
  theme.
3. **Mid-size type.** A 1.5rem subhead or a 1.25rem lead paragraph
   collapses the two-register discipline into ordinary web mush.
   *Cure:* the dead band (§3) and its CSS grep in §10.
4. **Fade-up reveals.** Sections rising and fading is every AI
   template's first move; here it reads as the page performing.
   *Cure:* focus-in only (§6.5) — blur and contrast, never
   translation or opacity.
5. **A signal that gets found.** Marketing will ask for the SNR to
   hit 8.0 "for the demo". The moment the counter confirms, the
   theme's honesty — its entire brand — is spent. *Cure:* the creep
   function caps at 4.9 (§6.6); the cap is in the spec so a builder
   can point at it.
6. **Exclamation marks and urgency copy.** "Don't miss this
   pointing!" is a theme error before it is a copy error. *Cure:*
   §12's banned list, checked in review.
7. **Amber everywhere.** Thread used as a general accent (buttons,
   borders, icons, hover states) spends the signal's meaning in a
   page. *Cure:* the thread census (§2) — four objects per viewport,
   counted in the gate.
8. **A fake "live" feel.** Randomly jittering numbers, a waveform
   that dances to nothing, timestamps from `Date.now()` rendered as
   if they were observations. *Cure:* every number traces to the
   Schedule, the creep function, or the visitor's real clock
   (§6.18) — the §10 figure audit samples all three.
9. **Stock nebula photography.** A purple Hubble wallpaper behind
   the hero turns the station into a poster. *Cure:* photography is
   of *the array and its people*, mesh-framed with provenance
   (§6.9); the sky in this theme is drawn, sparse and still.
10. **Dish clip-art.** A satellite-dish emoji-style icon or a
    generic parabola with no mesh, no feed arm, no shadow. *Cure:*
    §6.1's drawing spec (~140 nodes, three named parts) — the dish
    must look engineered, because it is the logo, the narrator and
    the hero in one object.
11. **Blur that strands.** Any build where a JS fault leaves text
    at 2px forever has broken the law (§1) in its most literal
    form. *Cure:* armed states are JS-applied only, watchdogs at
    6000ms, and the §10 drill that kills the loop and reloads.
12. **A chatty footer.** Social icons, a newsletter shout, "follow
    our journey". The footer is a log (§6.18). *Cure:* the log's
    paperwork block carries the legal necessities in Log register;
    anything louder is removed in review.

## 10. Quality gate

All checks are blocking. The gate is signed by someone other than
the builder (§15).

1. **The law drill.** Disable the rAF loop (devtools override) and
   reload: headline fully sharp by 6000ms, every `[data-focus]`
   element sharp, dish at a printed aim. Any element still faint at
   6s = fail.
2. **No-JS pass.** JavaScript off: every word readable, dish parked
   with per-pointing glyphs, readouts showing true coordinates,
   counters showing dusk values with `AT DUSK` labels, log showing
   the scheduled edition, form submittable.
3. **Figure audit.** Every printed coordinate, frequency, angle,
   integration and count on the page greps back to the Schedule
   (§4), the receiver record (§6.13) or the creep function (§6.6).
   One orphan number = fail.
4. **Stillness audit.** Grep the star layer and its CSS for
   `animation`, `transition`, `transform` and rAF references: zero
   hits. Screenshot-diff the sky between t=1s and t=30s: identical.
5. **Dead-band audit.** Grep compiled CSS for font-sizes between
   1.0625rem and 2.9375rem: zero hits outside the two whitelisted
   rules (the §6.11 logotype, §6.15's 1rem inputs).
6. **Thread census.** At five scroll positions, count
   `--signal-thread`/`--thread-pale` objects in the viewport: ≤4
   thread, and thread-pale only inside a live pulse or lock.
7. **Red census.** `--control-red` appears only as: REC dot, the
   `BELOW CONFIRMATION` stamp's dot, the form's error rules, the
   MAINTENANCE dot. Any red *text* = fail.
8. **Watchdog drills.** Block the canvas → SVG trace prints. Block
   the router → plain navigation works. Stall a focus-in mid-flight
   → 6000ms snap. Each drill passes or the gate fails.
9. **Reduced-motion pass.** With `prefers-reduced-motion`: no slew,
   no tuning, no pulses, no lean — and every fact from the animated
   pass still present. Compare content inventories, not screenshots.
10. **Contrast spot-check.** Bone on night 14.0:1, bone-dim 8.8:1,
    thread 8.6:1, grey labels 4.8:1, lean-set rest state ≥11:1
    effective through 0.6px softness.
11. **Agreement audit.** Counters vs. Schedule (base 03:12:44 inside
    P-01's 4h), strip vs. table (receiver L-1 `ON SKY` in both),
    proposal number = budget-line count + 1 (§8.3). Three printings,
    one record.
12. **Copy audit.** Zero exclamation marks outside quoted material;
    zero uses of "live" for anything that is not (the strip's dusk
    labels are the test); the log's stamps verbatim:
    `UNIDENTIFIED — PROBABLY US.` / `IDENTIFIED — YOURS.`

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components not listed do not get invented ad hoc; they get a spec
amendment.

| Component | Treatment in this theme |
|---|---|
| Primary button | Does not exist as a filled object. Actions are hairline-bordered mono labels (`SUBMIT FOR THE NIGHT`), border warming to thread on hover (§6.15) |
| Secondary link | Mono, `--star-grey` → `--bone-dim` on hover, thread underline drawn 300ms |
| Text input | `--night-panel` field, mono value, label above in whisper register; focus draws the thread rule (§6.15) |
| Select | Native `<select>`, unmodified behaviour, themed surface; options are record rows, never free invention |
| Textarea | As input; whisper guidance line beneath (the committee line, §6.15) |
| Checkbox / radio | Rare; when needed, a 12px hairline square/circle, checked = thread tick drawn as an SVG stroke (the readout's lock tick, reused) |
| Table | §6.13's treatment: hairlines, no zebra, tabular figures, `AS PRINTED AT DUSK` caption |
| Card | §6.12's log-entry card: panel, hairline, stamp |
| Badge / stamp | Bordered mono label, −2° rotation on paper surfaces, 0° on small screens; stamps state facts (`QUEUED`, `NO LOCK`), never marketing |
| Alert | A log line, not a banner: mono, bone text, red rule if it is an error (§2 discipline); page-level alerts sit where a log entry would |
| Toast | **Refused.** Nothing at a listening station pops up. Transient facts go to the signal log (§6.18) or inline where they belong |
| Modal | **Refused.** The theme has no overlays; a confirmation is a page state (the receipt, §6.15), a detail is a page |
| Tabs | **Refused.** Programmes are schedules (lists in time order), not tabbed panels; use the pointing index (§6.11) |
| Accordion | One licensed use: past-nights results on detail pages, rows expanding as log entries, chevron replaced by a `+ / −` mono glyph; expansion 300ms `--ease-focus`, content focus-resolves as it opens |
| Pagination | Log pages: `PAGE 2 OF 7 — OLDER NIGHTS →` in mono at the archive's foot; numbered, honest, no infinite scroll (a log has pages) |
| Breadcrumbs | A readout line: `STATION / POINTINGS / P-01` in mono whispers — coordinates grammar applied to wayfinding |
| Search field | One mono input in the index header; results per §7's search row treatment |
| Progress bar | **Refused** (§5). Progress is readouts and clocks |
| Spinner | **Refused.** Waiting is acquiring (§6.16) or the trace idling |
| Tooltip | Whisper captions on hover/focus, mono, `--night-panel`, appearing after 600ms — a tooltip here is a label leaned toward (§6.7), never a bubble with an arrow |
| Skip link | `SKIP TO THE POINTINGS`, first element, Log register (§6.11) |
| Footer | §6.18's signal log + paperwork block; no other footer exists |
| 404 | §6.17's lost pointing |
| Cookie/consent notice | If legally required: one log-line strip at the footer's top in the log's own grammar (`THIS STATION KEEPS NO COOKIES. THE LOG ON THIS PAGE IS SESSION-ONLY.`) — factual, dismissible by a mono `NOTED` |

## 12. Content & copywriting voice

Two registers, matching §3's two typefaces. The registers never
blend inside one element.

**The Instrument** (IBM Plex Mono — labels, readouts, errors,
stamps, buttons). Terse, factual, uppercase for labels, values as
printed. The instrument does not apologise, enthuse or hedge; it
reports. Error messages are instrument readings:

- ✓ `RA MUST BE HH MM SS.S — THE DISH CANNOT GUESS.`
- ✓ `RECEIVER L-4 IS IN MAINTENANCE UNTIL DAWN.`
- ✗ `Oops! That RA looks a bit off — try again?`
- ✗ `Please enter a valid right ascension.`

**The Station** (Instrument Serif — headlines, pointing names,
section statements). Quiet, patient, declarative; sentences that
sound like they were written by someone who has waited a long time
and expects to wait longer. Understatement is the house style; the
strongest claim the voice permits itself is a true one.

- ✓ `The universe is under no obligation to be loud.`
- ✓ `Tau Ceti, listening for a neighbour.`
- ✓ `Eleven years of nights. Nothing yet. The dish is patient.`
- ✗ `BREAKTHROUGH SIGNALS FROM DEEP SPACE — LIVE!`
- ✗ `Join 10,000 stargazers on an incredible journey!`

**Fixed strings (verbatim, never paraphrased):**

- `UNIDENTIFIED — PROBABLY US.` (log stamp, §6.18)
- `IDENTIFIED — YOURS.` (proposal stamp)
- `BELOW CONFIRMATION` (SNR stamp, §6.6)
- `NO PULSES YET. THE NIGHT IS YOUNG.` (log empty state)
- `THIS LOG IS KEPT ONLY HERE, ONLY TONIGHT.` (log privacy line)
- `No signal at these coordinates.` (404 statement, §6.17)

**Empty states** speak in the instrument's voice and state the
programme, not the absence: a search with no results prints
`NOTHING ON THIS FREQUENCY. THE DISH KEEPS LISTENING.` followed by
the five scheduled pointings. **Numbers** are always printed with
their units and their uncertainty where uncertainty exists (P-05's
± is the model). **Dates and times:** station times in the log are
the visitor's local time and labelled so; programme times are
integration hours; LST is labelled LST. No time appears without its
frame.

## 13. Full-page scroll choreography map

The home page, top to bottom. One lerped channel drives beats 2–8;
the dish's aim at each beat is the Schedule's (§4).

| Beat | Visitor's position | What happens | Dish aim |
|---|---|---|---|
| 0 | Load | Page prints whole; JS arms the headline (§6.3) and trace (§6.4); counters live (§6.6); strip flips LST live (§6.14) | Parked |
| 1 | Hero, t=0.9–5.7s | Four acquisition pulses tune the headline to sharp; log writes its first row in the unseen footer | Parked |
| 2 | Hero exit → status strip passes | Trace channel idles on (ambient pulses now possible, 6–14s); hero dish begins to be the sticky stage | Parked |
| 3 | Pointing index (§6.11) | Index resolves by focus; rows unlit; the visitor sees the whole night's geography at once | Parked |
| 4 | P-01 Tau Ceti | Slew to −6°/+3°; readout hunts and locks (1400ms); name and prose resolve; photo resolves; counters' caption names P-01 | −6° / +3° |
| 5 | P-02 Kepler-186f | Longer slew to +4°/+6°; same acquisition grammar; P-01's index tick dims to visited | +4° / +6° |
| 6 | P-03 Sagittarius A* | Slew to +8°/+2° — the stage's extreme; the act holds an extra 40vh while this readout completes (the galactic centre gets the page's longest pause) | +8° / +2° |
| 7 | P-04 TRAPPIST-1 | Slew back across the stage to −3°/+7° — the longest single travel; the dish crossing centre-frame is the act's quiet climax | −3° / +7° |
| 8 | P-05 The Wow! field | Slew to +6°/+4°; this readout prints its ± values and its uncertainty note resolves last in the pointing — the act ends on an admitted unknown | +6° / +4° |
| 9 | Receiver table (§6.13) | The dish leaves the stage (sticky ends); the table resolves as one block; dots begin breathing; the page's register shifts from sky to paperwork | — (off-stage) |
| 10 | Proposal form (§6.15) | Stillness. No scroll-driven motion in the form's act except its focus-in arrival; the budget line and the form wait | — |
| 11 | Footer (§6.18) | The log: the visitor reads their own visit back — entrance row, ambient rows with real times, any sent pulses, the proposal if filed. The dish, printed small in the footer's paperwork block, is parked | Parked |

**Reverse pass.** Scrolling up retraces the map with two
differences: readouts re-hunt at the shortened 700ms (§6.2), and
nothing un-resolves (§6.5) — the page remembers being read. The
dish's return travel is the same interpolation run backwards; beat
6's extra hold does not apply upward (the pause was for acquisition,
not for departure).

**Jump scroll.** Anchor jumps (index rows, skip link) mark all
skipped pointings resolved and pre-locked, land the dish directly at
the destination's aim by a single 700ms slew (or a cut, reduced
motion), and fire no lock ceremonies for skipped pointings (§6.1,
§6.2). The map is a path, not a toll road.

**Weather variant.** If the night block (§6.14) reports the dish
stowed, beats 4–8 keep their text and readouts but the dish holds
parked throughout and each pointing's card stamp reads `STOWED —
WEATHER`: the choreography has a published bad-weather edition, so
a stowed night degrades the page's story, never its coherence.

## 14. Whole-page performance budget

**Page weight (home, reference build):**

| Asset | Budget |
|---|---|
| HTML + inline SVG (dish, stars, mesh) | ≤ 120 KB |
| CSS | ≤ 38 KB |
| JS (loop, observers, form, log) | ≤ 46 KB |
| Fonts (Instrument Serif + IBM Plex Mono, subset, woff2) | ≤ 120 KB |
| Photography (all mesh frames, responsive, AVIF/WebP) | ≤ 420 KB |
| **Total** | **≤ 744 KB** |

**Frame budget.** The shared loop's per-frame ceiling is 1.6ms on a
mid-tier laptop: dish transform composition ≤0.4ms, trace ≤0.4ms,
lean pass ≤0.2ms, resolves ≤0.3ms, headroom 0.3ms. Long tasks: none
over 50ms after load; the digit hunt writes text content only.
Channels unregister off-screen (§5) — a page scrolled to the footer
costs the counters' 1Hz writes and nothing else.

**Cut order** (when the budget is exceeded, cut in this order, and
note the cut in the build log):

1. The re-pointing transition (§6.16) — plain navigation.
2. Lean-in proximity (§6.7) — elements print sharp.
3. Mesh-frame scale (keep the mesh fade; drop 1.04→1).
4. Trace point count (240 → 160) and hero canvas height.
5. Star count (190 → 110) — the mobile number.

**Never cut:** the 6000ms watchdog and the sharp-by-default DOM
(the law, §1); the readout's true strings; the counters' honesty
cap; the log's stamps. A build that ships without the watchdog to
save bytes has cut the theme's load-bearing wall.

## 15. Build-order checklist

1. Publish the Schedule (§4) and the receiver record (§6.13) as the
   page's data objects; print them in the page for the audit.
2. Build the static page complete: every word sharp, dish parked
   with per-pointing glyphs, dusk-labelled counters, scheduled log.
   **This version must pass §10 checks 2, 3, 5, 7 and 12 before any
   motion exists.**
3. Lay the star field (§6.10) and lock it: add the tripwire rule and
   the audit grep to the build.
4. Draw the dish (§6.1) as a static SVG at all five aims + parked;
   verify each aim against the Schedule's angles.
5. Stand up the shared rAF loop with the scroll and dish channels;
   wire the sticky stage and the aim interpolation.
6. Readouts (§6.2): true strings in DOM first, animated digit layer
   second, independent 3000ms snap watchdog third.
7. Focus-in system (§6.5) with per-element 6000ms watchdogs and the
   focus-forcing rule for keyboard visitors.
8. Trace (§6.4) over its baked SVG; entrance cadence; ambient
   scheduler; pulse reporting interface.
9. Headline tuning (§6.3) on the trace's pulses; global 6000ms
   `.tuned` watchdog.
10. Counters (§6.6) from the single state object; creep function
    published beside the Schedule; both printings (hero + strip).
11. Status strip (§6.14) with the LST formula and dusk fallbacks;
    lean-in (§6.7) and click-to-send (§6.8) on the shared loop.
12. Cards (§6.12), table (§6.13), index (§6.11) — all rendered from
    the records, none hand-typed.
13. Form (§6.15) with its server path first, enhancement second;
    log (§6.18) writers wired from §6.3/§6.4/§6.8/§6.15; the
    proposal-number agreement (§8.3) tested end-to-end.
14. Transition layer (§6.16) last and most expendable; 404 (§6.17).
15. Run the full §10 gate — drills included — signed by a
    non-builder; then the reduced-motion and no-JS passes are
    re-run on the signed build, not on a draft.
