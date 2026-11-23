# 75. Seismograph Diary — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never
redesigned).** The whole site is a tremor diary written by a
needle on a moving drum: calm sections are a nearly flat line,
important moments spike, and the reader feels the ground of the
story move under the text. Palette anchors: drum paper
`#EFE9DA`, trace ink `#33302A`, event red `#B03A2E`, station
green `#38604A`, grid rose `#D8C9B8`. Type: Spectral (literary
display and body) and IBM Plex Mono (station logs, magnitudes,
every figure the instrument states). A continuous margin trace
runs the page's whole length, written by a needle assembly
pinned at the reader's line; sections are diary entries on
smoked drum paper ruled with a faint time-grid; major
statistics are literal spikes in the trace with magnitude
labels pinned to their peaks. For geological surveys' public
education sites, observatory and museum earthquake exhibits,
disaster-preparedness diaries, and long-form journalism where
the ground itself is a character. The original entry's
anti-slop detail is kept verbatim as §6.4's caption: the
background micro-tremors never fully stop, and a caption names
the station the noise mimics.

## 1. Concept & world

The Seismograph Diary is the website of a recording instrument
that keeps a diary. On a real drum recorder — the smoked-paper
helicorders that turned in observatory basements for a
century — the day does not arrive as articles and cards. It
arrives as a line. The drum turns at its fixed speed whether
anything happens or not; the needle rests near the centre line
through the quiet hours, breathing with the earth's own small
restlessness, and when the ground moves, the needle writes
what it felt, at the amplitude it felt it, in the only ink it
has. This page works the same way on its own content. The
visitor does not browse a site; they read over the
instrument's shoulder while it writes. The margin trace runs
the full length of the page and is drawn as the reader's line
passes the needle; calm prose registers as a near-flat line
with an honest noise floor; a section carrying real data
agitates; and a major statistic is not typeset — it *happens*,
drawn as a spike at its place in the text with its magnitude
label pinned to the peak, the way the event itself is pinned
to a moment in the diary. The page is not decorated with a
seismograph. The page is the record the seismograph is
keeping, and reading it is standing in the drum room while the
drum turns.

The world the page performs is one room: a hilltop station, a
drum turning under a glass case, a keeper who comes in twice a
day to change the sheet, smoke it, fix it, and write the diary
in the margin of the record itself. Everything on the page
belongs to that room. Navigation is the ruler along the drum's
edge. Progress is station time, ticked in mono along the drum
edge. Images are prints pasted onto the sheet inside
smoked-paper frames, with the trace running under them like
under everything that day. The form is a felt report — the
card a reader files when the ground moved under *them* — and
its confirmation is an entry in the station log with a number
derived from the log's own count. There is no dashboard
chrome, no card-grid modernity, no "live" badge: the diary is
a record of what has happened, written by an instrument that
cannot know the future and does not pretend to.

**The theme's one law: the needle writes only the truth, and
only behind the reader.** Three clauses, all audited by the
gate (§10). (1) *Amplitude is data.* Every deflection on the
page — margin trace, statistic spike, readout overshoot — is
computed from the station record (§6.14) by the one published
deflection function (§5): drum-scale deflection
`d(M) = 6 × 2^(M−2)` px. A spike with no entry in the record
is a forged tremor; a decorative wiggle sized "to look right"
is the theme's capital crime, because the whole page's claim
is that its line means something. (The two licensed exceptions
are labelled as what they are: the noise floor (§6.4), which
is the instrument's character and is captioned as such, and
the reader's own touch (§6.9, §6.10), which is the reader's
event, never the earth's.) (2) *The drum writes the past.*
The trace is written at and behind the needle — the reading
line (§4). Paper ahead of the needle is blank ruled grid: the
instrument cannot record what has not happened, and a trace
pre-drawn below the fold and merely "revealed" is a diary
written in advance, which is fiction wearing a lab coat.
Scrolling back up never unwrites: the record is permanent,
the written trace stays written, readouts stay settled. A
diary that erases itself when revisited is a lie about the
day. (3) *The printed record underlies the performance.*
Every trace, spike and figure ships complete in the DOM —
the full trace printed flat, every spike's value printed as a
figure beside it. The writing is a mask laid over a finished
record, never the record's only form. With JavaScript dead or
a loop stalled, what remains is the whole diary, legible,
with every event's number in print. Clause 3 is the original
entry's safety rule kept in spirit and letter: the trace
decorates complete text, and no event hides inside an
animation.

**Best-fit sites and audiences.** First, the original entry's
own territory: any site whose content is a chronological
record of a restless thing — a geological survey's public
education pages (what the ground did this year, explained),
an observatory's or science museum's earthquake exhibit
microsite, a volcano or landslide monitoring service's public
diary, a disaster-preparedness NGO's season log. Then, by the
law's logic, any diary whose quiet stretches and spikes are
the story: a climate station's year of weather extremes, a
hospital foundation's diary of a ward (with the register
handled gently — see below), a long-form journalism piece
tracing one event's aftershocks, a research lab's field-season
log, a lighthouse or lifeboat station's log published for
supporters. The audience it suits reads slowly and trusts
instruments: people who will believe a number because the
page shows the needle writing it, and who understand that a
near-flat line held honestly for three sections is what makes
the fourth section's spike terrifying. Conversion on such
sites is a felt report filed (§6.13), a visit to the drum room
booked, a subscription to the station's letter — acts taken
at a spike or at a calm moment of trust, in the diary's own
grammar.

**When NOT to use it.** Not for anything that must claim to be
live. The diary is a record; a page that needs a real-time
feed (an actual early-warning dashboard, a control room)
needs an instrument panel, not a diary — and dressing a live
feed in smoked paper would slow the one reading that must
never be slowed. Not for commerce: a product grid has no
quiet stretches and no events, and forcing spikes onto prices
forges tremors (§9, failure 2). Not for content with no
chronology — the trace is time's shape, and a page whose
sections could be shuffled without loss has no business on a
drum. Not for tragedy handled closely: where the events are
recent deaths, the diary's restraint is a virtue but its
playfulness (the case-tap, the overshoot) must be governed by
§12's sombre register, and some houses will rightly choose a
plainer theme. And not where the client cannot supply a real
record — real times, magnitudes, depths (§6.14's record
object): a trace drawn over invented events is a forgery with
good typography, and §10's record audit exists to catch it.

## 2. Palette

Five anchors, inherited exactly. Derived tokens form a closed
list: a token not in this table does not exist in the theme,
and the gate greps built CSS for undeclared hex values.
Contrast figures below are measured, not estimated.

| Token | Hex | Role | Usage ratio | Pairing & contrast (measured) |
|---|---|---|---|---|
| `--paper` | `#EFE9DA` | Drum paper — the page's ground, the sheet itself | ~54% of viewport area | Carries `--ink` at **10.86:1**, `--ink-deep` at 13.71:1, `--ink-soft` at 6.00:1, `--event` at 4.97:1, `--station` at 5.90:1. The ground is a material, not a background colour: smoke grain and the time-grid (§4) live on it. |
| `--ink` | `#33302A` | Trace ink — the needle's line, body text, entry rules | ~15% | On paper 10.86:1 — the reading colour and the writing colour are the same ink: what the needle writes and what the keeper types are one substance. On `--paper-deep` 9.39:1. Ink is never a surface. |
| `--event` | `#B03A2E` | Event red — the alarm ink: spikes above threshold, the headline event, felt markers | ≤3% (rationed, §5) | On paper 4.97:1 — licensed for the trace itself (a line, read as a record, audited as a graphic), magnitude display ≥24px, and spike labels. Small text in the red register uses `--event-deep` (6.89:1). On `--drum-dark` 2.68:1 — **forbidden for text**; on the dark ground red appears only as the printed trace line over its paper underlay (§6.16). |
| `--station` | `#38604A` | Station green — the keeper's ink: navigation, links, confirmations, the log's apparatus | ~7% | On paper 5.90:1 — labels, links and apparatus at ≥13px; body-length green text uses `--station-deep` (8.12:1). On `--paper-deep` 5.10:1. On `--drum-dark` 2.26:1 — **forbidden**; the dark ground's green text is `--station-pale` (6.12:1). |
| `--grid` | `#D8C9B8` | Grid rose — the time-grid ruled on the sheet, hairlines, unwritten rules | ~18% (as line-work) | On paper 1.34:1 — a ruling, not a colour: it is never text, never a border that must be perceived to be understood, never a state indicator. Carries `--ink` at 8.12:1 where a ruled band must hold a caption. |
| `--ink-deep` (derived) | `#211E19` | Fresh ink — display headings, a spike's settled label, the diary's title | — | On paper 13.71:1. A figure still in `--ink` is a figure still settling; the settled record prints deep (§6.7). |
| `--paper-warm` (derived) | `#F5F0E4` | The fair sheet — raised entry panels, the record table's ground, the form's card | — | Carries `--ink` at 11.56:1, `--event-deep` at 7.33:1, `--event` at 5.29:1. Slightly lighter than the drum ground so a panel reads as a fresh sheet laid on the drum, not a hole in it. |
| `--paper-deep` (derived) | `#E3D9C4` | Smoked edge — inset panels, the trace rail's bed, skeleton tone, frame stock | — | Carries `--ink` at 9.39:1, `--ink-soft` at 5.19:1, `--station` at 5.10:1. The tone of paper that has been in the smoke box: insets and instruments sit on it. |
| `--ink-soft` (derived) | `#5C564B` | Pencil — captions, marginalia, source lines, the keeper's asides | — | On paper 6.00:1, on `--paper-deep` 5.19:1. Everything that explains the record rather than being it (§12). |
| `--event-deep` (derived) | `#8E2B21` | Dried red — small text in the event register: spike captions, form errors, felt counts | — | On paper 6.89:1, on `--paper-warm` 7.33:1. Fresh spikes render in `--event`; their printed captions use the deep tone. |
| `--station-deep` (derived) | `#2A4A38` | Deep station green — green-register body text, the log's settled entries | — | On paper 8.12:1. Carries `--paper` at 8.12:1 when it is the ground (the record table's head row, §6.14 — the one licensed green surface). |
| `--station-pale` (derived) | `#7FA98E` | Lamplight green — green-register text on the dark ground only | — | On `--drum-dark` 6.12:1. Exists for one room (the footer, §6.16); on paper it is never used — daylight green is `--station` or `--station-deep`. |
| `--drum-dark` (derived) | `#262019` | The drum room at night — footer ground (§6.16), the 404's ground (§6.18) | — | Carries `--paper` at 13.31:1, `--paper-warm` at 14.17:1, `--station-pale` at 6.12:1. The only dark ground in the theme; it is the room after hours, not a mode. |
| `--smoke` (derived) | `rgba(51,48,42,.055)` | Smoke — the grain layer over drum paper (§4) | — | A layer, never a colour: ink-toned, so smoked paper reads as the same sheet after the smoke box, not as a different page. Its drift is a scrubbed value (§5), never a static texture choice. |

**Usage discipline.** A page is roughly half drum paper, a
sixth grid line-work, a seventh ink (most of it the trace
itself, not text), green as the keeper's working ink, and red
as a rationed alarm: red appears where the record spikes and
almost nowhere else. The ratio is audited in the gate (§10):
event-red pixels above 4% of any viewport means alarm
inflation — if everything is an event, nothing is (§9,
failure 4); a page whose largest spike is drawn in `--ink`
while a lesser one wears red has inverted the record and
fails outright.

**Dark behaviour — the sheet does not invert; the drum room
darkens around it.** The Seismograph Diary is a light theme
by material: drum paper is pale because smoked paper is pale.
Under `prefers-color-scheme: dark` the sheet grounds stay
paper — a drum record does not turn black at night; the room
does. What changes: the page's outer margins and the gutters
beyond the sheet deepen to `--drum-dark`, the smoke layer's
strength rises from .055 to .08 (a sheet read by lamplight
smokes darker), the grid's rose deepens one step in role (hex
unchanged; its bed, `--paper-deep`, carries more of the
sheet), and the needle assembly's pivot gains its second
licensed highlight (§6.5). Every text pairing in the table is
unchanged in class, because no text ground changes. A build
that "adds dark mode" by inverting paper to charcoal has
burned the record to light the room, and fails §9.

## 3. Typography

**Faces.** Spectral — the diary's hand: a literary serif with
a bookish, slightly old-style cut, used for display and for
body copy, because a diary is a book the instrument is
writing. Spectral Italic is the keeper's aside voice (§12) —
the one place the diary sounds like a person rather than an
instrument. IBM Plex Mono — the station's hand: timestamps,
magnitudes, depths, distances, table data, form apparatus,
every figure the instrument states. The division is
constitutional: **the diary speaks Spectral; the station
speaks Mono; the two never swap jobs.** A magnitude set in
Spectral is a rumour; a diary entry set in Mono is a printout.

**The scale** (desktop; §6 breakpoint tables carry the smaller
sizes):

| Role | Face | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Hero display | Spectral 500 | 54px / 1.08 | −0.01em | The headline event's title (§6.1); max 9 words (§12) |
| Entry display | Spectral 500 | 34px / 1.14 | −0.005em | One per diary entry, at the needle's arrival (§4) |
| Magnitude display | IBM Plex Mono 500 | 44px / 1.1 | 0 | The overshooting readouts (§6.7); tabular figures mandatory |
| Spike label | IBM Plex Mono 500 | 13px / 1.4 | +0.02em | Pinned to peaks (§6.3): "M 6.2 — 14 KM DEEP" |
| Body | Spectral 400 | 17.5px / 1.65 | 0 | Measure 60–68ch (§4) |
| Body small | Spectral 400 | 15.5px / 1.6 | 0 | Entry-card body, log asides |
| Keeper's aside | Spectral Italic 400 | 15.5px / 1.6 | 0 | `--ink-soft`; marginalia and diary asides (§12) |
| Station log | IBM Plex Mono 400 | 13px / 1.55 | 0 | Timestamps, log stream (§6.15), source lines |
| Apparatus / labels | IBM Plex Mono 500 | 12px / 1.45 | +0.08em, uppercase | Station labels, drum-edge ticks (§6.11), form labels |
| Table data | IBM Plex Mono 400 | 13.5px / 1.5 | 0, tabular lining | The station record (§6.14) — read comparatively, so the instrument's hand |

**Five type laws.**
1. **Magnitudes are mono, always.** A magnitude, depth,
   distance or timestamp is IBM Plex Mono wherever it appears
   — in a spike label, a table, a headline's apparatus. The
   moment a figure puts on Spectral it has left the record
   and joined the storytelling, and the diary's whole
   credibility is that the two are distinguishable at a
   glance.
2. **The needle never moves type.** Entries are printed
   complete; the trace writes *past* them. Reveals are the
   sheet settling and the trace arriving — type itself never
   fades, rises, scales or jitters into place, with one
   licensed exception: the headline event's letters jitter
   with the needle's own sampled waveform (§6.1), because
   there the type is standing on the ground that moved.
   Layout at first paint is pixel-identical to layout at
   rest — zero CLS is a law, not a metric.
3. **Red never sets a sentence.** `--event` at 4.97:1 sets
   spike labels, magnitude display and the trace. A sentence
   in the red register — a caption, an error, a felt count —
   is set in `--event-deep` (6.89:1). A paragraph in event
   red is alarm inflation in typographic form (§9, failure 4).
4. **The station never shouts in serif.** Spectral sets no
   table, no log line, no form apparatus. If a builder reaches
   for Spectral to make a data table "warmer", they have put
   the diary's dress on the instrument (§9, failure 7).
5. **A magnitude never travels alone.** Every printed
   magnitude carries its depth, and where the record holds it,
   its distance and station time: "M 6.2 — 14 KM DEEP — 38 KM
   SSW — DAY 3, 14:22:08". A bare "M 6.2" is half a fact, and
   the diary does not print half-facts (§12). The apparatus
   may compress across a figure's repetitions, never at its
   first printing.

## 4. Layout language

**One sheet on a turning drum.** The page's foundation is a
single sheet: a centred column (max 920px at ≥1200px) of drum
paper on a wider smoked ground, ruled with the time-grid for
its full height. The grid is the drum's own ruling: vertical
rules every 64px stand for one hour of drum travel, horizontal
rules every 160px for the trace's amplitude bands, all in
`--grid` at its 1.34:1 whisper — present to the eye as texture,
never as information. Sections are diary entries laid on the
sheet in chronological order; an entry's head (date stamp in
mono, title in Spectral) sits at the entry's declared fraction
of the page (§5's record function), so the sheet's geography
*is* the diary's chronology: where an entry sits is when it
happened.

**The trace rail.** At ≥1200px a rail 128px wide runs the
sheet's full height at its left edge, bedded on
`--paper-deep`. The continuous margin trace (§6.2) writes down
its centre; the needle assembly (§6.5) pins in it at the
reading line; spike labels (§6.3) pin in it at their peaks,
rotated 0° (labels read horizontally, always — a label the
reader must tilt their head for is a label on a chart, not in
a diary). At 768–1199px the rail narrows to 72px and labels
move into the entry head. Below 768px the rail folds into the
sheet's top edge as a horizontal band (the drum turned on its
side, §6.2's breakpoint spec) — the trace is never deleted,
only re-bedded.

**The reading line.** One constant governs every trigger in
the theme: the needle's writing position sits at 38% of
viewport height. An entry is *at the needle* when its head
crosses that line; spikes draw, readouts count, images settle
as the needle passes them (§6). Every element's trigger in §6
is stated against this line, and the line is printed in §5
because the gate tests it: a build whose elements trigger at
assorted improvised offsets has a room full of instruments
disagreeing about where "now" is.

**Density — calm and event.** The sheet breathes in two
densities. Calm stretches (prose entries, the quiet days) run
at the diary's reading density: 17.5px body, 96px entry
separations, the trace near-flat in the rail. Event stretches
(the spike chapters) tighten: separations compress to 56px,
the entry head's apparatus doubles (spike label, felt band,
readout), and the rail's trace takes the room. The rhythm is
the record's own — a busy week crowds the diary; a quiet week
leaves paper. A build that spaces every entry identically has
typeset a diary as if all days were equal, which is the one
thing a diary exists to deny.

**Whitespace is unwritten paper.** Space on the sheet is not
emptiness; it is drum paper the needle has not reached or did
not need. It is therefore never filled with ornament: no
decorative rules beyond the grid, no filler graphics in quiet
stretches (the quiet *is* the content, §6.4). The widest
licensed whitespace is the hush before a spike chapter — one
viewport of near-flat trace and sparse prose — and it is
load-bearing: §9, failure 9 is the builder who "fixes" it.

**The smoked edge.** Every sheet and frame carries the smoke:
a `--smoke` layer over its ground plus a 1px `--grid` rule at
its edge, deepening toward the sheet's foot (the drum's lower
edge smokes darkest, where it passes nearest the lamp). The
grain is one shared SVG turbulence texture, printed once,
referenced by every sheet — never a per-section generated
noise (§14 budgets it once).

## 5. Full motion system

Five named easings, defined once, used everywhere; an element
that invents a sixth fails the gate's grep.

| Easing token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-drift` | `cubic-bezier(.3,.05,.25,1)` | The drum's advance — a soft start, then a speed that never varies | Paper drift (§6.1), smoke drift (§4), drum transition (§6.10) |
| `--ease-write` | `cubic-bezier(.4,.06,.26,1)` | Ink laid at even pressure — the needle drawing a line it means | Trace writes (§6.2), spike draws (§6.3), log inking (§6.15) |
| `--ease-needle` | `cubic-bezier(.24,1.32,.34,1)` | A needle answering — one overshoot, damped to rest | Readouts (§6.7), needle swings (§6.5), seal-of-record settle (§6.13) |
| `--ease-lift` | `cubic-bezier(.32,.58,.28,1)` | A sheet lifting at the edge — light, brief, put back down | Entry tilt (§6.9), drum-frame settle (§6.8), card hover (§6.12) |
| `--ease-tap` | `cubic-bezier(.58,.02,.88,.46)` | A tap on the case — reluctant, then sudden | Case-tap jump (§6.10), button press (§6.13), spike redraw (§6.10) |

**Durations ledger** (the theme's complete vocabulary; an
element may combine but not invent): drum paper drift 18px/s
(continuous while the hero is on screen); hero idle 800ms;
headline spike decay ≈1000ms (three damped oscillations,
§6.1); readout overshoot settle 1400ms; spike draw at the
needle's pass 600ms; entry sheet settle 500ms; tremor hover
500ms decay; case-tap jump 90ms out, redraw 350ms; drum
transition 700ms (one revolution); image settle scrubbed
across 30vh; station-time readout — scrubbed, no fixed
duration (the scroll is the clock); noise-floor recompute
every 240ms (§6.4); watchdogs 2500ms (headline event), 1500ms
(trace, spikes, readouts), 1200ms (drum transition), 1800ms
(unwritten sheet, §6.17).

**Every motion term, translated or refused.**
- *Scroll-triggered reveals* — entries settle as they cross
  the reading line (§4): the sheet flattens, the trace
  arrives, the apparatus prints. Nothing fades up from below;
  the diary was always on the sheet — the needle reaching it
  is the event.
- *Scroll-scrubbed animation* — the margin trace (§6.2),
  station time (§6.6), image settling (§6.8), smoke drift
  (§4): all scrubbed from the one shared loop (below).
- *Parallax* — three depths: smoke 0.94×, grid 0.98×, sheet
  1.0×. Capped ±14px. The trace itself never parallaxes: a
  record that drifts from its own ruling is a broken
  instrument.
- *Pinned sections* — exactly one assembly: the needle
  (§6.5), pinned in the rail for the diary's whole length. A
  second pin is refused; a drum has one needle, and a page
  that pins its sections like posters has left the drum room.
- *Masked reveals* — the trace's write mask (§6.2) and the
  spike's draw mask (§6.3). Masks always sit over a complete
  printed record (§1 clause 3 is the theme's constitution:
  the diary is beneath, whole).
- *Blur-to-sharp* — **refused.** A seismogram is never out of
  focus; the needle is sharp or the instrument is broken. The
  theme's softness is smoke — a layer *above* the paper that
  drifts (§4) — never a blur applied to the record itself.
- *Kinetic typography* — the headline event's jitter (§6.1)
  and nothing else. Letters elsewhere are print; they do not
  dance. The one exception exists because there the ground
  under the type genuinely moved, and §3 law 2 fences it.
- *Marquee* — **refused.** A drum turns; it does not scroll
  sideways forever. The station log band (§6.15) is the
  page's only stream, and it advances one entry at a time, at
  the drum's pace, when the needle reaches it.
- *Animated counters* — magnitudes, depths, counts (§6.7):
  counted once, with the needle's overshoot, latched. A
  counter that re-runs on scroll-back is a diary being
  rewritten (§1 clause 2 forbids it).
- *Progress indicators* — station time (§6.6) and the written
  fraction of the trace (§6.2). Percentages are banned from
  progress contexts (§12): the ticking clock and the written
  line *are* the progress, in the instrument's units.
- *Micro-interactions* — tremor hover (§6.9), case-tap
  (§6.10), the needle's tremble (§6.5), the form's ruling ink
  (§6.13).
- *Ambient loops* — exactly two licensed: the noise floor
  (§6.4) and the smoke drift (§4). Both pause off-screen and
  on hidden tabs. A third loop is a screensaver growing on a
  record (§9, failure 1).
- *Page transitions* — the drum revolution (§6.10): the sheet
  advances one full turn, the new page rolling under the same
  needle.
- *Reduced motion* — every element's variant, stated per
  element in §6; the global rule is the original entry's,
  verbatim in spirit: **a still drum, the full trace printed
  flat, all entries legible.**

**The shared loop.** One `requestAnimationFrame` loop drives
every scrubbed value — trace write fraction, station time,
image settle, smoke phase, needle angle — with a lerp factor
of **0.09** for scroll-scrubbed values. A drum answers the
hand a beat late and never jerks; the record answers scroll
the same way, so the ink lags the reader's hand by at most a
breath while the *content* — sheets, text, controls — is
always exactly where the reader put it. Native scroll is
never intercepted. The loop sleeps when every scrubbed value
is within 0.1% of target and when the tab is hidden; the
noise floor (§6.4) runs on its own 240ms timer, not the loop,
because the earth's restlessness is not keyed to the reader's
hand. Time-based acts (the headline spike, overshoots, taps)
run on CSS transitions or one-shot rAF timers with sampled
waveforms, never on the shared loop.

**The deflection function.** One function serves every
trace-writing element, so two builders — or two elements —
can never disagree about how big an event was. Drum-scale
deflection in px: `d(M) = 6 × 2^(M−2)`. The record's values,
computed, not eyeballed: M 1.8 → 5.2px; M 2.1 → 6.4px; M 2.9 →
11.2px; M 3.1 → 12.9px; M 3.4 → 15.8px; M 4.7 → 39.0px; M 6.2
→ 110.3px. The margin rail runs at a gearing of 0.45× (M 6.2
→ 49.6px against the rail's ±52px cap) — a real instrument's
gain switch, stated on the rail itself (§6.2), never a silent
rescale. The hero drum band (§6.1) runs at full drum scale.
A builder who sizes a spike by eye has forged a tremor, and
§10's amplitude audit samples three spikes and measures them
against this function to the pixel.

**The record function.** Page progress `p` (scroll fraction
of the document, 0–1) maps to written trace fraction
`w = p` exactly — the trace is the page's own length, kept as
a diary. But station *time* is not linear in `p`, and the
theme says so on the sheet: the diary compresses the quiet
days (the drum at the station did not — §6.6 prints the
distinction). Time at the reading line is the record's time:
each entry declares its fraction (§4) and its station time
(§6.14); between entries, the readout interpolates linearly
across the gap; at an entry, it stands at that entry's time.
So the readout crossing the Day 3 chapter stands at exactly
DAY 3 — 14:22:08 when the needle is on the spike. The mapping
and the fractions are printed here because the gate tests
them (§10).

**Event-red ration.** Red is spent like the keeper's one
bottle of alarm ink: per page, at most the spikes above the
print threshold (§6.3), the headline event (§6.1), felt
markers (§6.13), and error text in `--event-deep`. A page
rendering more red than that has made a livery out of an
alarm and fails §10's pixel audit.

## 6. Signature elements

The ten elements of the original entry (§6.1–§6.10), deepened,
plus eight page-family elements (§6.11–§6.18) the original's
world implies: the drum-edge navigation, the entry sheets, the
felt-report form, the station record table, the station log
band, the drum-room footer, the unwritten sheet, and the
silent page. Every figure any element prints traces to the
station record (§6.14): the October watch, Days 1–30 — 186
events logged, 7 printed at or above the diary's threshold of
M 1.8, 3 felt at the station house, 405 felt reports filed by
readers across the watch.

### 6.1 The headline event

- **What & why.** The hero is the diary's biggest event,
  performed by the instrument itself. On load the drum begins
  its slow rotation — paper drifting leftward at 18px/s under
  a horizontal trace band — the trace idles near-flat for
  ~800ms, and then the headline event hits: the needle spikes
  violently through three decaying oscillations while the
  headline's letters jitter with the same sampled waveform,
  and the magnitude readout overshoots and damps to its
  settled value. It belongs because it is the theme's thesis
  before a word of body copy is read: this site is written by
  the ground moving, and the title is the largest thing the
  ground did. In the worked site (§8.1) the headline event is
  the watch's largest: DAY 3 — 14:22:08 — M 6.2, 14 km deep,
  38 km SSW of the ridge.
- **Structure.** A real `<h1>` printed complete on the sheet
  at full contrast from first paint, above a horizontal drum
  band (one inline SVG, full width of the sheet, 280px tall)
  carrying the hero trace: a finished path of the event's full
  waveform — idle, spike train, settle, noise floor — wearing
  a stroke mask whose reveal is the only animated property.
  The waveform is sampled at build time from the deflection
  function (§5) and the damping curve below; it is data drawn
  once, not a runtime improvisation. The magnitude readout is
  a mono `<output>` beside the band. No canvas: the record
  must remain inspectable, printable SVG (§1 clause 3).
- **Motion spec.** Trigger: load, once per session
  (`sessionStorage`; a returning visitor finds the hero
  already written, readout settled — the diary does not
  re-perform its worst day for regulars). Gated on
  `document.fonts.ready` raced against 900ms — jittering in a
  fallback face would misalign the letters, so if fonts lose
  the race the hero ships written. t=0: paper drift begins
  (18px/s, `--ease-drift`). Trace idles at the noise floor
  (±2px, §6.4) until t=800. Spike onset t=800: peak +110.3px
  (the function's drum-scale value for M 6.2) at t=860; −74px
  at t=1010; +38px at t=1180; −14px at t=1330; inside the
  noise floor by t=1800 — three decaying oscillations over
  ≈1000ms, sampled at 60Hz from `A·e^(−t/340)·sin(2πt/310)`.
  Headline letters jitter on the same samples, scaled 0.045×
  (peak ≈5px, vertical only, per-letter phase offset ≤12ms —
  letters on one sheet of paper move together, not in a
  choreographed wave). The readout (§6.7) counts 0 → 6.5 peak
  at t≈1250, damps through 6.0 at t≈1600, settles at 6.2 at
  t=2200 in `--ink-deep`.
- **States.** Unwritten (JS-armed only) → idling → spiking →
  settled (rest). Hover/focus: none — the hero is not a
  control. Scrolled away mid-spike: the spike is time-based
  and completes off-screen; returning shows the written
  record. Focus entering the hero settles everything
  instantly — a keyboard visitor is never asked to wait for
  an earthquake.
- **Content merge.** The spike *is* the page's subject: the
  headline names the event, the band writes it, the readout
  states it, and the entry below (§8.1) is its diary entry.
  Nothing here is an intro screen in front of the content;
  the hero is the diary's first and largest entry, written
  at drum scale because in the record it is the largest.
- **Failure fallback.** Watchdog at 2500ms: if the spike has
  not settled, the mask snaps to written, letters stand at
  rest, the readout prints 6.2. No JS: the mask is never
  applied; the hero ships written, readout printed. Slow
  network: the hero is HTML-first; the writing script is
  deferred and the watchdog runs from DOMContentLoaded.
- **Reduced-motion variant.** The written hero: full waveform
  printed in the band, headline still, readout settled at
  6.2, paper not drifting — the original entry's still drum
  applied at the first screen.
- **Performance budget & mobile variant.** Hero SVG ≤16KB;
  the jitter transform applies to ≤40 letter spans, compositor
  only. Mobile (<768px): band height 200px, spike sampled at
  30Hz (the waveform coarsens, its peaks do not move), letter
  jitter capped at 3px, paper drift 12px/s.
- **Choreography timeline (v2).** t=0 fonts ready (or 900ms
  race lost → written state, ceremony skipped) → t=0 paper
  drift starts → t=0–800 trace idles at noise floor → t=800
  spike onset → t=860 peak +110.3px → t=1010 −74px → t=1180
  +38px → t=1330 −14px → t=1800 trace inside noise floor →
  t=1250 readout peaks 6.5 → t=1600 readout 6.0 → t=2200
  readout settled 6.2, printed deep. Watchdog ceiling 2500ms
  cancels anything unfinished.
- **State matrix (v2).** *Rest (returning visitor):* written
  band, settled readout, drift running while on screen.
  *Hover:* none. *Focus:* focus within hero settles a running
  spike. *Active:* n/a. *Scrolled-past:* written, latched;
  the drift pauses off-screen. *Disabled / no-JS:* printed
  written at first paint. *Touch:* identical; no touch
  gesture is required or intercepted.
- **Breakpoints (v2).** ≥1200px: band 280px, full 60Hz
  sampling, readout 44px. 768–1199px: band 240px, sampling
  45Hz, readout 38px. <768px: band 200px, sampling 30Hz,
  jitter cap 3px, readout 32px, apparatus wraps beneath the
  band.
- **Edge cases & failure modes (v2).** *Headline longer than
  9 words:* §12 caps it; a longer title wraps to two lines
  and both lines jitter on the same samples (one sheet, one
  shock). *Tab hidden mid-spike:* rAF pauses; on return,
  wall-clock past 2500ms fires the watchdog. *Session
  returning mid-scroll:* the hero is above the fold's history
  — it ships settled; no replay, no catch-up performance.
- **Accessibility spec (v2).** The `<h1>` is complete in the
  accessibility tree from first paint; the band SVG is
  `aria-hidden` (its information — M 6.2, 14 km, Day 3,
  14:22:08 — is carried accessibly by the readout and the
  entry's apparatus in text). The readout's settled value is
  in the DOM from first paint; the count is visual only and
  never announced. Contrast is the printed layer's at all
  times: ink on paper 10.86:1.
- **Tokens consumed (v2).** `--paper`, `--paper-warm`,
  `--ink`, `--ink-deep`, `--event`, `--grid`, `--smoke`,
  `--ease-drift`, `--ease-needle`, `--dur-idle` (800ms),
  `--dur-spike` (1000ms), `--dur-readout` (1400ms),
  `--dur-watchdog-hero` (2500ms).

### 6.2 The continuous margin trace

- **What & why.** An SVG trace runs the page's full length in
  the rail (§4), written scrubbed to scroll: the written
  fraction of the trace is the read fraction of the page
  (§5's record function, `w = p`). Its amplitude is driven by
  each section's data density — calm prose near-flat at the
  noise floor, data-heavy sections agitated, event chapters
  spiking to their record values at 0.45× gearing. It belongs
  because it is the page's emotional seismology made literal:
  the margin registers how much is happening in the text
  beside it, and a reader can feel the diary's shape — where
  the quiet days are, where the ground moved — without
  reading a word. It is the theme's spine: spikes (§6.3), the
  needle (§6.5), station time (§6.6) and the log band (§6.15)
  all read their state from it.
- **Structure.** One inline SVG in the rail, authored as a
  finished path for the whole document height — every calm
  stretch, agitation and spike drawn at build time from the
  record (§6.14) and the density map (§4) — wearing a vertical
  write mask driven by the shared loop. Path resolution: one
  point per 2px of rail length, capped at 4000 points per
  page; longer diaries paginate (§7), they do not thin the
  record. A printed gain note at the rail's head, in mono
  apparatus: "MARGIN GAIN 0.45× — DRUM SCALE IN THE ENTRIES".
  The honesty is printed where the rescale happens (§1 clause
  1). Beneath the path, a 6px paper underlay stroke keeps the
  trace legible where it crosses the rail's smoked bed.
- **Motion spec.** Trigger: scroll, scrubbed — written length
  = lerped `w × L`, lerp 0.09, so the trace's writing head
  trails the reader's true position by at most a breath and
  settles when they stop. The writing is ratcheted (§1 clause
  2): the mask's revealed fraction is `max(w)` this session —
  scrolling up never unwrites. Amplitude is not animated
  separately; it is in the path. The only live motion in the
  rail is the write head's advance and the noise floor's
  breathing at the head (§6.4).
- **States.** Unwritten ahead of the needle (blank ruled
  rail — the future) → writing at the head → written behind
  (rest, permanent). Hover: none on the trace itself (the
  rail is a record, not a control). Focus: n/a. Scrolled-past:
  written and latched; the rail above the viewport is a
  finished record. *Disabled / no-JS:* the mask is never
  applied; the whole trace ships printed.
- **Content merge.** The trace is not beside the content; it
  is the content's register. Its calm stretches are calm
  because the entries beside them are calm — the density map
  is derived from the entries' own data (events per day,
  figures per section), never assigned for looks. A redesign
  of the text that changes its data changes the trace,
  because the trace is drawn from the same record (§6.14).
- **Failure fallback.** Watchdog at 1500ms after any scroll
  stall: if the write head lags the reader's position by more
  than 5% of page length, the mask snaps to the reader's
  position. No JS: printed in full. If the SVG fails to parse
  (a build error), the rail renders its bed and a printed
  flat trace as a background image — the diary never ships
  with an empty margin pretending the ground was still.
- **Reduced-motion variant.** The full trace printed flat for
  the whole rail, no write mask, no breathing head — the
  original entry's printed fallback, applied to the spine.
- **Performance budget & mobile variant.** Rail SVG ≤22KB;
  one dash-offset write per frame at most. Mobile (<768px):
  the rail folds to a horizontal band at the sheet's head and
  at each entry head (a per-entry trace strip at drum scale
  for that entry's own span) — the continuous rail is a
  wide-sheet luxury, but every entry keeps its own written
  line; gearing note prints once, at the first strip.
- **Choreography timeline (v2).** Continuous: scroll → shared
  loop lerps `w` toward `p` (0.09) → mask offset writes →
  write head crosses an entry's fraction → that entry's
  settle arms (§4) → head crosses a spike's fraction → §6.3's
  draw arms. On load mid-page (a deep link): the trace ships
  written to the anchor's fraction instantly — the diary
  does not make an arriving reader watch the past being
  written before they may read.
- **State matrix (v2).** *Rest:* written to the furthest
  point reached; ahead, blank ruled rail. *Hover:* none.
  *Focus:* none (non-interactive). *Active:* n/a.
  *Scrolled-past:* latched written. *Disabled / no-JS:*
  printed full-length. *Touch:* identical; the write head
  follows touch scroll through the same loop.
- **Breakpoints (v2).** ≥1200px: rail 128px, gearing 0.45×,
  cap ±52px, labels in rail (§6.3). 768–1199px: rail 72px,
  gearing 0.30× (M 6.2 → 33.1px against a ±34px cap), labels
  move to entry heads. <768px: rail folded to per-entry
  strips at full drum scale (a strip is short; the full
  spike fits its entry's band, §6.1's geometry).
- **Edge cases & failure modes (v2).** *Very long diary:*
  the 4000-point cap paginates the watch (§7) — a build that
  silently thins point density has falsified calm stretches
  and fails §10. *Content edited in a CMS:* the trace is
  regenerated from the record at build; an edit that adds an
  event to the text without adding it to §6.14 fails the
  record audit — by design. *Reader flings to the foot:*
  every latch between here and there fires in order (§13's
  jump-scroll rule); the trace stands written, readouts
  settled — the diary never makes a jumping reader watch the
  month they skipped.
- **Accessibility spec (v2).** The rail SVG is `aria-hidden`;
  its entire information content — every spike's magnitude,
  depth and time — is printed in the entries' apparatus and
  in §6.14's table, in text, in reading order. The trace is
  never the sole carrier of any fact (§1 clause 3). The gain
  note is real text in the rail head, available to all.
- **Tokens consumed (v2).** `--paper-deep`, `--paper`,
  `--ink`, `--event`, `--grid`, `--ease-write`, `--dur-loop`
  (lerp 0.09), `--gain-margin` (0.45), `--cap-margin` (52px),
  `--dur-watchdog-trace` (1500ms).

### 6.3 Statistic spikes

- **What & why.** A major statistic is not typeset in the
  entry that reports it; it is drawn as a literal spike in the
  margin trace at its section's position — a full waveform
  (rise, peak, damped settle) at the deflection the function
  assigns its magnitude — with a magnitude label pinned to its
  peak: "M 6.2 — 14 KM DEEP". It belongs because it makes the
  diary's numbers *events*: a statistic is something that
  happened to the ground, at a place in the text, and the
  reader meets it the way the station met it — as a
  deflection with a size that can be compared, by eye, against
  every other deflection on the page. Seven spikes print in
  the worked watch — one per record event at or above M 1.8
  (§6.14) — and no others: the threshold is the diary's
  editorial line, stated on the sheet, and a figure below it
  is reported in prose, not spiked.
- **Structure.** Each spike is a finished SVG path segment
  within the rail's trace (§6.2), drawn at build from the
  damping template (attack 60ms-equivalent of arc length,
  three oscillations, settle) scaled by `d(M) × 0.45`. Its
  label is a real text element — mono, 13px, `--ink` with the
  magnitude in `--event` — positioned at the peak's arc
  coordinate, with a 1px leader pin from label to peak. The
  statistic's value also prints as a figure in the entry's
  apparatus (§1 clause 3): the spike is the figure's portrait,
  never its only printing.
- **Motion spec.** Trigger: scroll — the spike draws as the
  write head (§6.2) reaches its fraction: the segment's mask
  sweeps in 600ms `--ease-write` (arc-length proportioned, so
  a big spike and a small one draw at the same ink speed),
  the label prints at the moment the sweep crosses the peak
  (opacity, 120ms), and the local trace settles into the
  noise floor behind it. Latched: once drawn, drawn for the
  session and every later one (`localStorage` — the diary
  remembers what the reader has witnessed; §6.2's ratchet
  made persistent).
- **States.** Unprinted (ahead of the needle — the segment
  exists in the DOM, masked) → drawing → printed (rest).
  Hover: the label's pin warms to `--event` and the entry's
  corresponding figure highlights in the text (§6.9's tremor
  grammar, shared) — the spike and its figure are one fact in
  two inks. Focus: a spike label is not a control; the
  entry's apparatus carries the focusable fact. Scrolled-past:
  printed, latched. *Disabled / no-JS:* printed with the
  trace, label in place.
- **Content merge.** The spike stands at its statistic's own
  position in its own entry — the Day 19 spike rises beside
  the paragraph that reports the deepest event, at the arc
  position of Day 19 in the watch. It is never floated to a
  "stats section": the diary has no stats section, because in
  a diary a number belongs to its day.
- **Failure fallback.** Watchdog at 1500ms: a spike whose
  draw has not completed when the reader is 10vh past it
  snaps printed, label and all. No JS: printed. A spike whose
  record entry is deleted in the CMS is deleted from the
  trace in the same build — an orphan spike is a forgery and
  §10 greps for it.
- **Reduced-motion variant.** All spikes printed with the
  flat trace, labels pinned — the record complete, the
  drawing ceremony skipped.
- **Performance budget & mobile variant.** Seven spikes ≈
  3KB of path in the rail's budget (§6.2). Mobile (<768px):
  the spike draws in its entry's own strip at full drum
  scale (§6.2), label above the peak in the entry head —
  bigger, if anything: on a small sheet the event is the
  entry's headline, not its margin.
- **Choreography timeline (v2).** Write head reaches spike
  fraction → t=0 mask sweep starts → sweep crosses peak
  (≈55% of arc) → label prints (120ms) → t=600 sweep complete
  → trace continues into the settle tail → latch writes to
  storage. Watchdog ceiling 1500ms.
- **State matrix (v2).** *Rest:* printed, label pinned.
  *Hover:* pin warms, twin figure highlights. *Focus:* n/a
  (apparatus carries it). *Active:* n/a. *Scrolled-past:*
  printed, latched, persistent across sessions. *Disabled /
  no-JS:* printed. *Touch:* no hover warm; the twin-figure
  link is carried by the label's print alone.
- **Breakpoints (v2).** ≥1200px: spike in rail at 0.45×,
  label in rail at peak. 768–1199px: spike in rail at 0.30×,
  label in the entry head, pin omitted. <768px: spike in the
  entry strip at 1.0× drum scale, label above peak.
- **Edge cases & failure modes (v2).** *Two events one day:*
  the record allows it; spikes draw in time order along the
  day's arc, labels stacked with 18px clearance, never
  overlapping a peak. *A statistic revised after publication:*
  the diary corrects like a diary — the spike redraws at the
  corrected deflection and the entry's apparatus prints the
  correction with its date (§6.15's grammar); the old
  deflection is struck in the log, never silently replaced.
  *Threshold dispute:* an event at M 1.7 does not spike, and
  its prose says why ("below the diary's print threshold") —
  the line is editorial and admitted, not hidden.
- **Accessibility spec (v2).** The label is real text in
  reading order within its entry; the spike path is
  `aria-hidden`. The twin figure in the apparatus is the
  accessible fact; the spike adds shape, never information.
  Label contrast: `--ink` on `--paper-deep` 9.39:1; the
  magnitude's `--event` on `--paper-deep` is ≥18px-equivalent
  display usage in the label's bold mono — audited as graphic
  + large text (§2).
- **Tokens consumed (v2).** `--ink`, `--event`, `--paper`,
  `--paper-deep`, `--ease-write`, `--dur-spike-draw` (600ms),
  `--gain-margin` (0.45), `--dur-watchdog-spike` (1500ms).

### 6.4 Micro-tremor noise — the honest floor

- **What & why.** The trace never fully stills. Between
  events, in the calmest prose, the written line breathes with
  a low-amplitude noise floor (±2px at drum scale) of real
  seismometer character — irregular, clustered, occasionally
  pricked by a tiny distant eventlet too small to print as a
  spike. It belongs because it is the theme's honesty at rest:
  an instrument that draws a dead-straight line between events
  is claiming the earth stopped, and the earth does not stop.
  The floor is also the reader's proof of life — the diary is
  being kept by something awake. The original entry's
  anti-slop detail lives here as a printed caption at the
  rail's head: *"The quiet on this page is real quiet,
  recorded, not drawn: the floor breathes with the character
  of the public feed of station ANMO, Albuquerque, whose
  restlessness the keeper admires and does not copy."* The
  caption names the station the noise mimics — mimics in
  character, modelled at build time from the feed's published
  character (its amplitude distribution and eventlet rate),
  never a live scrape and never presented as live data.
- **Structure.** The floor is part of the rail trace's path
  (§6.2) for all written stretches — baked into the finished
  path at build from a seeded noise model (seed printed in
  the build's source line, so the "randomness" is
  reproducible and auditable) — plus one live segment: the
  120px of trace immediately behind the write head, redrawn
  every 240ms from the same seeded model advanced by a step
  counter, so the line at the needle visibly breathes while
  everything behind it is settled history. Eventlets (a
  3–5px, sub-second-shaped prick) occur in the model at the
  captioned station's character rate: roughly one per 90
  seconds of reading, never within an entry's spike chapter
  (the floor does not heckle an event).
- **Motion spec.** Trigger: time — the live segment recomputes
  every 240ms (not on the shared loop; §5), each recompute
  shifting the segment's points by ≤0.6px from the last, so
  the breathing is a drift, never a jitter. Amplitude ±2px
  drum scale, ±2px in the rail (the floor is drawn at floor
  value at both gainings — §5's function governs events, and
  the floor is not an event). The baked floor in written
  stretches does not move: history does not breathe, only the
  present does — a distinction the theme insists on, because
  a diary whose past wiggles is being rewritten.
- **States.** Breathing (rest, at the head) → settled (behind
  the head, baked) — the only two states, by design. Hover:
  none. Focus: none. Scrolled away: the live segment pauses
  with the loop's sleep; the diary does not perform
  restlessness for an empty room. *Disabled / no-JS:* the
  baked floor prints along the whole trace; the caption's
  "breathes" reads as the printed character, which it is.
- **Content merge.** The floor is the calm sections' content
  in the rail: where the text says the week was quiet, the
  line shows what quiet looks like on this instrument —
  not nothing, but almost-nothing, honestly rendered. It is
  also the control against which every spike is read: without
  a visible floor, a 5.2px M 1.8 spike and a flat line would
  be indistinguishable, and the small events would be
  unbelievable.
- **Failure fallback.** If the live segment's timer fails or
  the device is low-power (§14's detection), the head segment
  ships baked like the rest — the floor reads as character,
  not animation, and nothing is lost but the breathing.
  Watchdog: if two consecutive recomputes throw, the timer
  stops and the baked state stands; no error surfaces on the
  sheet.
- **Reduced-motion variant.** The floor prints baked along the
  whole trace; the live segment does not run. The caption
  stands — under reduced motion it is the caption, not the
  animation, that carries the honesty.
- **Performance budget & mobile variant.** Live segment: 60
  points, one path `d` write per 240ms — under 0.1ms of work,
  the cheapest licensed loop on the page. Mobile (<768px):
  the live segment runs in the entry strip at the reader's
  current entry only; background tabs and off-screen strips
  are baked.
- **Choreography timeline (v2).** Page load → baked floor
  visible along written trace → live segment arms at the
  write head → every 240ms: step counter advances, segment
  redraws (≤0.6px drift) → eventlet windows (model-scheduled,
  ~1 per 90s): a 4px prick forms over 2 recomputes, decays
  over 3 → scroll moves the head: the live segment hands its
  tail to the baked path (the path is one; only the last
  120px is live).
- **State matrix (v2).** *Rest:* breathing at the head.
  *Hover:* none. *Focus:* none. *Active:* n/a.
  *Scrolled-past:* baked, still. *Disabled / no-JS:* baked
  full-length. *Touch:* identical; the timer is
  scroll-independent.
- **Breakpoints (v2).** ≥1200px: live segment 120px in the
  rail. 768–1199px: 96px, amplitude ±1.6px (the narrower rail
  compresses the floor with the gearing). <768px: live
  segment in the current entry's strip only, ±2px.
- **Edge cases & failure modes (v2).** *A real event while
  reading:* the diary is a record, not a feed (§1) — nothing
  on the page claims otherwise, and the caption's wording is
  the guard. *Motion-sickness reports:* the floor's drift is
  sub-pixel per step; if a reader's device reports
  `prefers-reduced-motion` mid-session, the variant applies
  on the next recompute, not the next page load.
  *Seed collision:* two builds with different seeds produce
  different floors — acceptable; the seed is printed, and
  §10 audits the floor's *statistics* (amplitude, eventlet
  rate), not its exact shape.
- **Accessibility spec (v2).** The floor is `aria-hidden`
  decoration over a complete text record; it announces
  nothing and its absence removes nothing. The caption is
  real text. The breathing is below vestibular concern
  thresholds (≤0.6px per 240ms, no oscillation of content) —
  and is nonetheless fully removed under reduced motion.
- **Tokens consumed (v2).** `--ink`, `--paper-deep`,
  `--ink-soft`, `--dur-floor` (240ms), `--floor-amp` (2px),
  `--floor-drift` (0.6px).

### 6.5 Needle assembly

- **What & why.** A needle-and-pivot assembly pins in the rail
  at the reading line (38% of viewport height, §4) for the
  diary's whole length: a brass-toned pivot (drawn in
  `--ink` and `--grid` line-work — the theme's metals are
  ink, §2), a needle arm reaching to the trace's centre, its
  tip at the write head. It trembles faintly at event sections
  and rests steady in calm ones. It belongs because it makes
  the writer visible at work: the reader watches their own
  position being recorded, and understands — physically, not
  metaphorically — that the trace below the needle is the
  future and the trace above it is the past. It is the page's
  only pinned element (§5), and it earns the pin: a drum has
  one needle.
- **Structure.** One inline SVG (≤3KB) in a `position: sticky`
  rail cell at the reading line: pivot circle, counterweight,
  arm, and the tip's ink point. The arm's angle is a CSS
  custom property written by the shared loop; the needle's
  deflection at any moment equals the trace's deflection at
  the write head (read from the same path data — the needle
  and the line cannot disagree, §10 tests it). In calm
  stretches the arm rests at centre ± the floor's ±2px; at
  spike fractions it stands deflected to the spike's arc
  position as the head passes.
- **Motion spec.** Trigger: scroll position + section state,
  via the shared loop (lerp 0.09). Tremble: at event sections
  (declared in the density map), the tip adds the floor's
  live segment motion (§6.4) amplified 1.5× — the instrument
  feels what it is writing. At spike peaks the arm holds the
  peak deflection for 300ms before following the settle —
  a real needle's inertia, stated, not faked with a generic
  bounce. Swing between distant deflections (jump scroll):
  1100ms `--ease-needle`, one overshoot, damped.
- **States.** Resting (calm sections: centre, floor tremble)
  → trembling (event sections) → deflected (at a spike) →
  resting. Hover: none — the needle is not a control and does
  not react to the pointer; a needle that performs for the
  cursor has left the instrument for the toy shop (§9,
  failure 6). Focus: none. Scrolled to the foot: the needle
  parks at the final entry's rest position, tip on the last
  written point. *Disabled / no-JS:* the assembly prints
  static at the rail's head — present as the sheet's
  furniture, claiming nothing.
- **Content merge.** The needle writes the trace the reader
  is reading; its position *is* the reader's position,
  stated in the instrument's terms. It merges by function,
  not by placement: remove it and the trace loses its author;
  remove the trace and the needle is a weather vane.
- **Failure fallback.** If the loop stalls, the needle freezes
  where it stands — an honest failure (a stopped instrument
  looks stopped) — and the 1500ms watchdog (§6.2) snaps the
  trace written, after which the needle's stillness reads as
  rest, not breakage. No JS: static print, as above.
- **Reduced-motion variant.** The needle prints at centre rest
  at the rail's head; it does not pin, tremble or deflect —
  under reduced motion the sheet carries a printed diagram of
  the assembly in the rail head, and the trace is the flat
  printed record (§6.2's variant).
- **Performance budget & mobile variant.** One custom-property
  write per frame; the SVG is 3KB. Mobile (<768px): no pinned
  assembly — each entry strip carries a small printed needle
  glyph at its head (static), and the current entry's strip
  shows the live tip position as a dot on its trace. The pin
  is a wide-sheet ceremony; the record survives its absence.
- **Choreography timeline (v2).** Scroll → loop lerps write
  fraction → needle angle property writes (same frame as the
  trace mask, §6.2 — one cause, two witnesses) → head enters
  event section: tremble gain ramps 1.0→1.5× over 400ms →
  head crosses spike peak: arm holds 300ms → follows settle →
  section exits: gain ramps back over 400ms.
- **State matrix (v2).** *Rest:* centre ± floor. *Hover:*
  none, by law. *Focus:* none. *Active:* n/a.
  *Scrolled-past:* the assembly remains at the reading line
  (it is pinned to the reader, not the page). *Disabled /
  no-JS:* static print at rail head. *Touch:* identical; no
  gesture drives it.
- **Breakpoints (v2).** ≥1200px: full assembly, 128px rail.
  768–1199px: assembly at 72px rail scale (arm shortened,
  pivot same size — instruments miniaturise their arms, not
  their bearings). <768px: printed glyph per entry strip, as
  above.
- **Edge cases & failure modes (v2).** *Reader at the very
  foot:* the needle parks (above) rather than sliding off the
  record. *Browser without sticky support:* the assembly
  falls back to the rail head, static — the trace still
  writes; §10's browser floor makes this a legacy-only path.
  *Deflection disagreement:* if path data and arm angle ever
  diverge (a build bug), the gate's needle test (§10) fails
  the build — the two are one datum with two renderings.
- **Accessibility spec (v2).** `aria-hidden` throughout: the
  needle conveys position, which the station-time readout
  (§6.6) conveys in text, accessibly, in the same rail. No
  information is needle-only.
- **Tokens consumed (v2).** `--ink`, `--grid`, `--paper-deep`,
  `--ease-needle`, `--dur-loop` (lerp 0.09), `--dur-swing`
  (1100ms), `--line-reading` (38%).

### 6.6 Station-time progress

- **What & why.** Elapsed station time is ruled along the drum
  edge — a mono readout in the rail head, ticking with scroll:
  "DAY 3 — 14:22:08". One drum revolution of the readout's
  chapter ticks corresponds to one major chapter of the diary.
  It belongs because it makes progress *temporal in the
  diary's own units*: the reader is not 34% through a page,
  they are at Day 3, mid-afternoon, three minutes before the
  ground moved. It is also the theme's honesty about its own
  compression, printed on the readout's apparatus line: "THE
  DIARY COMPRESSES THE QUIET DAYS. THE DRUM AT THE STATION
  DID NOT." — the mapping from scroll to time (§5's record
  function) is admitted on the instrument that displays it.
- **Structure.** A mono `<output>` (13px, tabular) in a ruled
  cell at the rail's head, beneath the gain note (§6.2), with
  a chapter tick row: one tick per chapter, ticks printing
  `--station-deep` as their chapters are entered. The readout
  value is computed by the shared loop from the record
  function: at an entry's fraction it stands at that entry's
  declared station time; between entries it interpolates
  linearly across the gap in diary-time. The DOM ships with
  the readout standing at the final time (DAY 30 — 23:59:59);
  the JS-armed state starts it at DAY 1 — 00:00:00.
- **Motion spec.** Trigger: scroll, scrubbed — the readout
  ticks as the lerped write fraction moves (lerp 0.09): within
  a chapter gap it advances smoothly, second by second; at an
  entry fraction it lands exactly on the entry's time and
  holds while the entry is at the needle. It never ticks
  backward on scroll-up (§1 clause 2): the displayed time is
  `max(time)` this session — a reader re-reading Day 2 is
  visiting the past, and the station clock, like the trace,
  does not unlive it. Chapter ticks print as their fractions
  cross, 120ms `--ease-write`, latched.
- **States.** Ticking (rest, while scrolling) → holding (at
  an entry) → complete (at the foot: DAY 30 — 23:59:59,
  standing). Hover: none. Focus: the readout is not a control.
  Scrolled-past: holds the maximum reached. *Disabled /
  no-JS:* stands at the final time, printed — the diary's
  full span stated on its face.
- **Content merge.** The readout is the diary's clock, and
  every entry's date stamp (§6.12) is a reading of it: when
  the needle is on the Day 3 entry, the readout and the
  entry's stamp agree to the second, because both are read
  from the record (§6.14). A progress indicator that agrees
  with the content it progresses through is not decoration;
  it is the same fact at two sizes.
- **Failure fallback.** If the loop stalls, the readout
  freezes — and the watchdog (§6.2) snaps trace and time
  together to the reader's position, so clock and line can
  never be caught disagreeing. No JS: final time printed.
- **Reduced-motion variant.** The readout prints the current
  entry's time as the reader scrolls (updated on entry
  change only, no smooth ticking) — station time as a series
  of printed stamps, which is what a paper diary has.
- **Performance budget & mobile variant.** One text write per
  frame at most, and only when the displayed second changes.
  Mobile (<768px): the readout moves to a slim ruled bar
  above the current entry strip (§6.2's fold), same value,
  same law.
- **Choreography timeline (v2).** Scroll → loop lerps `w` →
  record function maps `w` to diary time → if the displayed
  second changed, the readout writes → needle crosses an
  entry fraction: readout lands on the entry time, holds →
  chapter tick prints (120ms) → scroll resumes: interpolation
  continues from the entry's time.
- **State matrix (v2).** *Rest:* holding at the current
  entry's time or interpolating in a gap. *Hover:* none.
  *Focus:* none. *Active:* n/a. *Scrolled-past:* maximum
  reached, latched. *Disabled / no-JS:* final time printed.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: readout in rail head, 13px,
  chapter ticks in a row of ≤8. 768–1199px: readout in rail
  head, ticks wrap to two rows. <768px: readout in the bar
  above the entry strip; chapter ticks become the strip's
  chapter stamp.
- **Edge cases & failure modes (v2).** *A diary with one
  entry:* the readout stands at that entry's time throughout;
  interpolation across a single point is the point — stated,
  not faked with a fake span. *Entries out of order in a CMS:*
  the build sorts by record time and fails §10 if the page
  order and the time order disagree — a diary whose Day 9
  follows its Day 12 has a torn page, and the gate says so.
  *Midnight boundaries:* times are station-local, printed
  with the station's offset in the record (§6.14); the
  readout never converts to the reader's timezone — the
  diary happened at the station.
- **Accessibility spec (v2).** The readout is plain text,
  updated silently (no `aria-live` — a ticking clock must
  never chatter at a screen reader); its information is
  duplicated in every entry's printed date stamp. Contrast:
  `--ink` on `--paper-deep` 9.39:1.
- **Tokens consumed (v2).** `--ink`, `--station-deep`,
  `--paper-deep`, `--grid`, `--ease-write`, `--dur-loop`
  (lerp 0.09), `--dur-tickprint` (120ms).

### 6.7 Overshooting magnitude readouts

- **What & why.** A magnitude figure does not fade in; it
  counts the way the needle writes — swinging past its value
  and damping back: "M 6.2" arrives via 6.5, shivers through
  6.0, and settles at 6.2 as the local spike settles. It
  belongs because it makes typography obey the instrument's
  physics: numbers on this page were *measured*, and a
  measured number carries the trace of its measuring. The
  overshoot is also information — its size is proportional to
  the event: an M 1.8 readout overshoots by 0.1 and settles
  almost apologetically; the M 6.2 throws 0.3 past and takes
  its full 1400ms to calm. A reader learns the scale in their
  peripheral vision before they learn it in the table.
- **Structure.** A mono `<output>` (tabular figures, so the
  counting never jiggles the layout — §3 law 2) whose settled
  value is in the DOM from first paint. The count is driven by
  the same damping function as the spikes,
  `v(t) = M + A·e^(−t/τ)·sin(2πt/T)`, with `A = 0.05 × d(M)`
  capped at 0.3, `τ = 340ms`, `T = 310ms` — the readout and
  the spike are one event rendered in line and in figure, and
  §10 samples them against each other. The settled state
  prints in `--ink-deep`; mid-count values print in `--ink`
  (a figure still in `--ink` is still settling, §2).
- **Motion spec.** Trigger: scroll into view — the readout
  counts when the needle (§6.5) passes its figure's position:
  1400ms total, peak overshoot at ≈310ms, two visible
  crossings, settled by 1400ms, latched (never re-counts on
  scroll-back, §1 clause 2). Depth and distance figures in
  the same apparatus count plainly (no overshoot — they were
  computed, not felt; the theme distinguishes what the needle
  measured from what the keeper derived, and only the needle's
  own quantity gets the needle's physics).
- **States.** Settled-printed (DOM state) → counting → settled
  (rest, deep ink, latched). Hover: none. Focus: focus
  landing on the figure settles it instantly. Scrolled-past
  quickly: if the needle passes a figure at fling speed, the
  count is skipped and the settled value stands — the diary
  does not perform for a reader who has left. *Disabled /
  no-JS:* settled value printed.
- **Content merge.** The readout stands in its entry's
  apparatus beside its spike (§6.3) and its prose — the same
  fact in the record's three inks: line, figure, sentence.
  It is never floated into a hero metric or a dashboard tile;
  a magnitude belongs to its event (§6.3's law, shared).
- **Failure fallback.** Watchdog at 1500ms: an unsettled
  readout snaps to its printed value. No JS: printed. If the
  damping function throws, the value stands settled — the
  fallback for every figure on this page is the figure.
- **Reduced-motion variant.** The settled value, printed.
  The overshoot is the one piece of pure performance in the
  theme's typography, and it is the first thing reduced
  motion retires — the number loses nothing.
- **Performance budget & mobile variant.** One rAF timer per
  counting readout, ≤2 concurrent; text writes only when the
  displayed tenth changes (≤24 writes per count). Mobile:
  identical, at the entry's apparatus size (32px display).
- **Choreography timeline (v2).** Needle crosses figure
  fraction → t=0 count starts at 0.0 → t≈310 peak (M + A) →
  t≈620 first crossing below M → t≈930 second, smaller peak →
  t=1400 settled, ink deepens (120ms colour transition) →
  latch writes. Watchdog ceiling 1500ms.
- **State matrix (v2).** *Rest:* settled, deep. *Hover:*
  none. *Focus:* settles instantly. *Active:* n/a.
  *Scrolled-past:* settled, latched, persistent across
  sessions (§6.3's storage, shared). *Disabled / no-JS:*
  printed settled. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: 44px display in apparatus.
  768–1199px: 38px. <768px: 32px, apparatus stacks beneath
  the entry title; count duration unchanged (physics does
  not shrink with the sheet).
- **Edge cases & failure modes (v2).** *A revised magnitude:*
  the diary corrects in the open (§6.3) — the readout
  re-counts once, on the correction's publication, to the
  corrected value, and the log prints the correction; it
  never silently re-settles. *Two readouts in one viewport:*
  they count in needle order, never simultaneously — one
  needle, one event at a time. *M below 1.0 (a micro-event in
  prose):* no readout; prose carries it (§6.3's threshold,
  shared).
- **Accessibility spec (v2).** The settled value is the DOM
  text from first paint; the count is a visual overlay on
  that text (the accessible value never changes). No
  `aria-live`. Contrast: `--ink-deep` on `--paper` 13.71:1
  settled; mid-count `--ink` on `--paper` 10.86:1.
- **Tokens consumed (v2).** `--ink`, `--ink-deep`, `--paper`,
  `--ease-needle`, `--dur-readout` (1400ms), `--dur-watchdog-
  readout` (1500ms).

### 6.8 Drum-frame images

- **What & why.** Photographs — the station, the ridge, the
  drum room, a crack in a wall the keeper walked out to see —
  sit in smoked-paper drum frames: a `--paper-deep` mount with
  time-grid edges, a mono caption giving the station time the
  photograph was taken, and a faint trace line crossing the
  frame's bottom edge, continuous with the page's own trace.
  As the needle passes the frame, the image scales 1.04 → 1.0
  and settles onto the sheet. It belongs because in a diary a
  photograph is not an illustration dropped in from a library;
  it is a print pasted onto the sheet at the moment it
  occurred, and the trace runs under it like under everything
  that day.
- **Structure.** A `<figure>` on the sheet: mount
  (`--paper-deep`, grid-ruled edges, `--smoke` layer), the
  image at 1.04 scale inside an overflow-clipped well, and a
  `<figcaption>` in mono apparatus: station time, place, and
  the day's trace state ("taken during the Day 3 aftershock
  hours — the line under this print is still restless"). The
  trace crossing is an SVG segment in the frame's own layer,
  drawn from the record for that timestamp — at a calm
  timestamp it crosses flat; the Day 3 frame's crossing is
  visibly unsettled. The image ships at its settled scale in
  the DOM; the 1.04 is a JS-armed pre-state.
- **Motion spec.** Trigger: scroll — as the needle (§6.5)
  passes the frame's centre, the scale lerps 1.04 → 1.0
  scrubbed across 30vh of travel (shared loop, lerp 0.09),
  and the caption's trace segment draws in 600ms
  `--ease-write` as the frame enters. No zoom on hover, no
  lightbox: the diary does not open its pasted prints into a
  gallery.
- **States.** Pasted (rest, settled, the DOM state) → settling
  (needle passing) → pasted. Hover: the frame lifts 1°
  maximum (§6.9's sheet grammar) — no scale change; the print
  is handled, not browsed. Focus: a frame is not a control
  unless it is a link (on listing pages, §6.12, where the
  whole sheet is the link and focus settles the image
  instantly). Scrolled-past: settled, latched. *Disabled /
  no-JS:* settled at 1.0, caption printed, trace segment
  printed.
- **Content merge.** The frame's timestamp is in the record:
  the photograph stands in the diary at the hour it was
  taken, in the entry for that day, and its caption's trace
  is that hour's trace. A photograph that could be moved to
  any other entry without anything breaking is stock, and
  §9 failure 8 names it.
- **Failure fallback.** Watchdog: if the settle has not
  completed 10vh past the frame, scale snaps to 1.0. Broken
  image: the mount prints the caption and a ruled empty well
  with the log's line ("PRINT MISSING — the negative is in
  the station drawer") — a diary admits a lost print; it does
  not show a broken-image icon on smoked paper.
- **Reduced-motion variant.** The print pasted at 1.0, caption
  and trace segment printed — the frame complete, the
  settling retired.
- **Performance budget & mobile variant.** Photography ≤380KB
  per page (§14), lazy-loaded below the second entry with the
  mount and caption printed first (the sheet never waits for
  its prints). Mobile (<768px): frames full-sheet width, the
  scale settle shortened to 20vh, caption beneath the mount.
- **Choreography timeline (v2).** Frame enters lower viewport
  → caption trace draws (600ms) → needle reaches frame centre
  → scale lerps 1.04 → 1.0 across 30vh → settled; latch.
  Watchdog: snap at +10vh past centre.
- **State matrix (v2).** *Rest:* pasted at 1.0. *Hover:* 1°
  lift, no scale. *Focus:* settles instantly if linked.
  *Active:* n/a. *Scrolled-past:* settled, latched. *Disabled
  / no-JS:* printed settled. *Touch:* no hover lift; the
  settle is scroll-driven only.
- **Breakpoints (v2).** ≥1200px: frames at sheet width or
  two-up at 46% for paired prints (before/after the same
  wall). 768–1199px: single column, 100% sheet width.
  <768px: full width, caption below, settle 20vh.
- **Edge cases & failure modes (v2).** *A photograph with no
  timestamp:* it does not enter the diary — the frame's
  contract is a time; undated images live on the about page
  (§7) in plain mounts, outside the record. *Very tall
  image:* frames cap at 70vh with the print cropped by the
  well (the crop is the mount's, stated in the caption if it
  cuts the subject). *Print pairs disagreeing (a "before"
  dated after its "after"):* the build fails §10's record
  audit — the diary's chronology is its spine.
- **Accessibility spec (v2).** Real `alt` text (what the print
  shows), the caption as visible text, the trace segment
  `aria-hidden`. Focus order follows reading order; a linked
  frame's focus ring is §11's ink ring on the mount.
- **Tokens consumed (v2).** `--paper-deep`, `--paper`,
  `--grid`, `--smoke`, `--ink`, `--ink-soft`, `--ease-lift`,
  `--ease-write`, `--dur-framedraw` (600ms).

### 6.9 Tremor hover

- **What & why.** Hovering a diary entry agitates its underline
  trace in a small local tremor — ±3px, ~500ms, decaying — and
  the entry tilts 1° like a drum sheet lifting at the edge.
  It belongs because it is the reader's own event in the
  diary, honestly labelled as theirs (§1 clause 1's licensed
  exception): touching the record stirs the ground beneath it,
  briefly and locally, and the diary admits the touch by
  registering it. It is the theme's only hover theatric, and
  it is rationed to entries and entry-cards — the instrument
  does not tremble at navigation, buttons or chrome.
- **Structure.** Each entry carries an underline trace: a short
  SVG segment (the entry's own span of the record, at entry
  scale) beneath its title, printed flat at rest. The tremor
  is a transform on that segment's group (vertical jitter from
  a 500ms sampled decay, seeded per entry so two entries never
  tremor identically) plus a `rotate(1deg)` on the entry sheet
  with its transform-origin at the sheet's top edge — a sheet
  lifts from its free edge, not its bound one.
- **Motion spec.** Trigger: hover or focus-within. Tremor:
  amplitude 3px decaying exponentially over 500ms (three
  visible crossings), `--ease-lift` for the tilt (180ms in,
  260ms out — a sheet settles slower than it lifts). One
  tremor per entry per hover-entry; re-hovering after leaving
  re-arms it. On touch: a tap on the entry head fires the same
  tremor once (and nothing else — the tap is not a navigation
  on a detail page).
- **States.** Rest (flat underline, sheet flat) → trembling →
  rest. Focus: identical to hover (keyboard readers get the
  same stir). Active (pressed, on cards): the tremor halves
  and the case-tap (§6.10) takes over if the card is a link.
  Scrolled-past: rest. *Disabled / no-JS:* rest, printed — the
  underline is complete without the stir.
- **Content merge.** The trembling line is the entry's own
  record span — hovering the Day 7 entry stirs Day 7's ground,
  at Day 7's character (its underline carries its small spike,
  and the tremor rides over it). The interaction is keyed to
  the content's data, not pasted over it.
- **Failure fallback.** The tremor is pure enhancement: if its
  timer throws, the entry stands at rest. No watchdog is
  needed because nothing is ever hidden, masked or pending —
  the fallback is the rest state itself.
- **Reduced-motion variant.** No tremor, no tilt. Hover
  instead deepens the underline's ink (`--ink-soft` →
  `--ink`, 120ms) — attention is still registered, in print
  rather than in motion.
- **Performance budget & mobile variant.** One 500ms timer per
  tremor, transform-only. Mobile (<768px): tilt off (a small
  sheet's lift reads as a layout bug), tremor on tap retained
  at ±2px.
- **Choreography timeline (v2).** Pointer enters entry → t=0
  tilt starts (180ms) → tremor samples: +3px at 40ms, −2.2px
  at 130ms, +1.2px at 240ms, −0.5px at 360ms → t=500 underline
  at rest → pointer leaves: tilt returns (260ms).
- **State matrix (v2).** *Rest:* flat. *Hover:* tremor + 1°
  lift. *Focus:* same as hover. *Active:* tremor halved,
  §6.10 grammar if linked. *Scrolled-past:* rest. *Disabled /
  no-JS:* rest printed. *Touch:* tap fires one tremor, no
  tilt under 768px.
- **Breakpoints (v2).** ≥1200px: full spec. 768–1199px: tilt
  0.7°. <768px: tilt off, tremor ±2px on tap.
- **Edge cases & failure modes (v2).** *Pointer crossing many
  entries quickly:* each entry's tremor is independent and
  short; a diagonal sweep stirs a ripple of small tremors —
  acceptable, and capped: at most 3 concurrent tremor timers,
  further entries stand at rest until a slot frees. *Hover
  during a spike's draw:* the draw (§6.3) wins; the tremor
  queues until the segment is printed — the record outranks
  the reader's touch in the record's own moment.
- **Accessibility spec (v2).** The tremor is decorative and
  `aria-hidden`; focus triggers it for parity of feedback,
  and the focus ring (§11) is the actual focus indicator —
  the tremor never replaces it. Tilt never moves the entry's
  text out of its box (transform only, origin at the bound
  edge).
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--event`,
  `--ease-lift`, `--dur-tremor` (500ms), `--tilt-entry` (1deg).

### 6.10 Case-tap click & the drum revolution

- **What & why.** Clicking a spike label, a readout or an
  entry's "tap the case" affordance taps the instrument case:
  the needle jumps once — a single spike — and the element's
  own spike redraws, crisper. On navigation, the drum advances
  one full revolution (~700ms), rolling the new sheet under
  the same needle. It belongs because it closes the theme's
  contract: every action on this page is recorded by the
  instrument. The reader's click is an event, so the needle
  writes it; the reader's departure turns the drum, so the
  next page begins on fresh paper. Nothing on this site
  happens off the record.
- **Structure.** The tap target is the element itself (spike
  labels and entry heads carry a `data-tap` affordance with a
  printed hint in apparatus: "TAP THE CASE"). The jump is a
  transform on the needle arm (§6.5) plus a redraw of the
  tapped element's spike segment (its mask sweeps at 2× ink
  speed, 350ms, ending at a marginally deeper ink — the redraw
  is the same path; "crisper" is a 10% ink deepen, stated
  honestly in the build, not a new drawing). The transition is
  a full-sheet overlay: the current sheet's bottom edge rolls
  (a cylinder gradient + translate, `--ease-drift`) as the new
  page's sheet rolls in beneath the rail, needle and all —
  the rail and needle assembly persist across the roll; only
  the sheet changes.
- **Motion spec.** Tap: needle jumps +18px drum-scale
  equivalent in 90ms `--ease-tap`, decays through two
  crossings by 420ms; the tapped spike redraws concurrently
  (350ms). Transition: 700ms total — 300ms the old sheet
  rolls away, 400ms the new sheet settles under the needle,
  its trace shipping written to the arrival fraction (§6.2's
  deep-link rule). Interruption: a second navigation during a
  roll cancels to the newest sheet instantly — the drum never
  queues revolutions.
- **States.** Idle → tapped (jump + redraw) → idle. Transition:
  resting sheet → rolling → resting sheet. Hover: tap targets
  show the tremor (§6.9) at half amplitude — the case hums
  before it is tapped. Focus: Enter/Space on a tap target
  fires the tap; focus is never hijacked by the roll — after
  a transition, focus lands on the new page's `<h1>` per
  §11's routing rule. *Disabled / no-JS:* taps do nothing
  (the record is already printed); navigation is a plain page
  load — the roll is an enhancement over a working site.
- **Content merge.** The tap redraws *that element's* spike —
  the reader asks the instrument to write the Day 19 event
  again, and it does, from the same record. The roll turns
  the drum the site actually lives on: the persistent rail
  and needle across pages are the theme's claim that it is
  one instrument keeping one diary, not a set of themed pages.
- **Failure fallback.** Watchdog at 1200ms on the transition:
  if the roll has not completed, the new sheet snaps in,
  fully written to its arrival fraction. A tap whose redraw
  throws leaves the original printed spike — the first
  writing stands.
- **Reduced-motion variant.** No jump (the tapped spike's
  label deepens in ink instead), no roll — navigation is an
  instant sheet change with the new page's apparatus line
  noting "SHEET CHANGED" in the log band (§6.15), so the
  record still registers the turn.
- **Performance budget & mobile variant.** The roll is one
  compositor transform on a sheet-sized layer; on devices
  under §14's low-power detection the roll shortens to a
  200ms crossfade of the sheet only. Mobile: same roll,
  drum-speed unchanged (a revolution is a revolution at any
  sheet size).
- **Choreography timeline (v2).** Tap: t=0 needle +18px (90ms)
  → redraw sweep starts → t=180 needle −9px → t=350 redraw
  complete, ink deepened → t=420 needle at rest. Roll: t=0
  old sheet releases → t=300 old sheet gone, new sheet's head
  under needle → t=700 new sheet settled, its first entry
  arming. Watchdog ceiling 1200ms.
- **State matrix (v2).** *Rest:* idle, sheet resting.
  *Hover:* half-tremor on tap targets. *Focus:* tap fires on
  Enter/Space. *Active:* the tap itself. *Scrolled-past:*
  n/a. *Disabled / no-JS:* plain navigation, printed record.
  *Touch:* tap = tap; no hover state.
- **Breakpoints (v2).** ≥1200px: full roll with rail
  persisting. 768–1199px: full roll, rail at 72px persists.
  <768px: the roll becomes a vertical sheet slide (the folded
  drum, §6.2) at the same 700ms.
- **Edge cases & failure modes (v2).** *Rapid double-tap:* the
  second tap re-jumps the needle from its current deflection
  (the samples add, capped at +26px) — the instrument answers
  twice, honestly, and the redraw restarts. *Back button:*
  the drum rolls *backward* one revolution (the sheet returns
  the way it left) — the one licensed reverse motion, because
  it is the reader retracing, not the record unwriting; the
  arriving sheet's trace stands as written as the reader left
  it. *Prefetch:* sheets prefetch on link hover/focus so the
  roll never waits on the network; a failed prefetch degrades
  to a plain load.
- **Accessibility spec (v2).** Tap targets are real buttons or
  links with visible focus (§11); the jump and redraw are
  `aria-hidden` performance. The transition never traps
  focus; a `prefers-reduced-motion` reader gets the log's
  "SHEET CHANGED" line instead of the roll.
- **Tokens consumed (v2).** `--ink`, `--ink-deep`, `--paper`,
  `--grid`, `--ease-tap`, `--ease-drift`, `--dur-tap` (420ms),
  `--dur-roll` (700ms), `--dur-watchdog-roll` (1200ms).

### 6.11 Drum-edge navigation — the masthead & ruler

- **What & why.** The site's navigation is the ruler along the
  drum's edge: a masthead band across the sheet's head carrying
  the station's name in Spectral, and beneath it the chapter
  ruler — the diary's chapters (The Watch, The Events, The
  Record, The Station, File a Report) as ruled ticks with mono
  labels, the current chapter's tick printed deep with a small
  needle mark. It belongs because a drum's edge is where its
  keeper reads position; navigation here is not a menu laid
  over the diary but the instrument's own furniture, and the
  reader's place in the site is stated the way their place in
  the diary is — by a mark on a ruled edge.
- **Structure.** A `<header>` on `--paper-warm`: station name
  (Spectral 500, 26px), the station's one-line apparatus
  ("BRACKEN RIDGE — EST. 1962 — DRUM 4") in mono, and a `<nav>`
  as a ruled row: a 1px `--grid` rule, ticks (8px `--ink`
  strokes) at each chapter, labels in mono apparatus beneath
  their ticks. The current chapter's tick is 14px and carries
  the needle mark (a 6px `--event` point — one of the page's
  rationed red appearances, §5). On scroll past the hero, the
  masthead compresses to the ruler alone, sticky at the sheet's
  top, the station name reduced to its initials in mono.
- **Motion spec.** Compression: on scroll past 120px, the
  masthead's name block collapses (height, 300ms
  `--ease-write`) leaving the sticky ruler; it re-expands at
  the page top. Chapter change (on navigation or scrollspy
  within the diary page): the needle mark slides along the
  ruler to the new tick (400ms `--ease-needle`, one small
  overshoot — the mark is a needle, and needles overshoot,
  §6.7's physics at furniture scale). No dropdowns, no
  hamburger theatre: at every width the ruler shows all
  chapters or wraps to two ruled rows.
- **States.** Expanded (page top) → compressed (scrolled) →
  expanded. Hover on a tick: its label deepens to
  `--station-deep` and the tick lengthens 2px (120ms) — the
  ruler acknowledges a hand. Focus: §11's ink ring on the
  label. Active chapter: deep tick + needle mark.
  *Disabled / no-JS:* the full masthead stands, uncompressed;
  every chapter is a plain link.
- **Content merge.** The ruler's ticks are the diary's chapters
  in the diary's order — on the home page they are the watch's
  own chapter ticks, shared with §6.6's readout; the nav and
  the progress are one ruled edge read two ways.
- **Failure fallback.** Sticky failure (legacy browser): the
  masthead simply scrolls away and the footer (§6.16) carries
  the full ruler again — no page on this site is more than
  one sheet away from its navigation.
- **Reduced-motion variant.** The masthead does not compress
  (it stands full, and the sticky ruler still sticks —
  position is not motion); the needle mark changes tick
  instantly.
- **Performance budget & mobile variant.** Header ≤4KB of
  markup, no script beyond the shared loop's compression
  check. Mobile (<768px): the ruler wraps to two rows, ticks
  and labels at 44px touch height, the station name at 22px —
  chapters are never hidden behind a menu button on a site
  with five of them.
- **Choreography timeline (v2).** Scroll crosses 120px →
  name block collapses (300ms) → ruler sticks → chapter
  fraction crosses → needle mark slides (400ms, overshoot
  ≈2px) → tick deepens. Reverse at page top: expansion
  (300ms).
- **State matrix (v2).** *Rest:* expanded at top, compressed
  scrolled. *Hover:* tick lengthens, label deepens. *Focus:*
  ink ring. *Active:* current chapter marked. *Scrolled-past:*
  n/a (it is the frame). *Disabled / no-JS:* full, static.
  *Touch:* ticks are 44px targets; no hover lengthening.
- **Breakpoints (v2).** ≥1200px: one row, name 26px.
  768–1199px: one row, name 22px, apparatus line drops.
  <768px: two rows, name 22px, sticky ruler only (name block
  does not stick).
- **Edge cases & failure modes (v2).** *A sixth chapter added:*
  the ruler re-spaces; at seven chapters the labels abbreviate
  per §12's apparatus style rather than shrinking below 12px —
  below seven, a site has outgrown the diary's furniture and
  §7's archive pattern takes the overflow. *Long station
  name:* wraps to two lines in the name block; the ruler never
  wraps its labels mid-word.
- **Accessibility spec (v2).** A real `<nav>` with a list of
  links; the current chapter carries `aria-current="page"`;
  ticks and the needle mark are `aria-hidden` furniture.
  Contrast: labels `--ink` on `--paper-warm` 11.56:1.
- **Tokens consumed (v2).** `--paper-warm`, `--paper`, `--ink`,
  `--station-deep`, `--event`, `--grid`, `--ease-write`,
  `--ease-needle`, `--dur-nav` (300ms).

### 6.12 Entry sheets — the diary entry & its cards

- **What & why.** The theme's core content unit: a diary entry
  as a sheet on the drum — date stamp in mono, title in
  Spectral, body, and its apparatus (spike, readout, felt line)
  composed at the entry's declared fraction of the page. On
  listing pages the same sheet, shortened, is the entry card.
  It belongs because it *is* the theme: if the entries were
  ordinary article blocks, the trace would be wallpaper around
  someone else's website. The entry sheet is where the diary's
  two voices (§12) meet the instrument: the Diarist writes,
  the station stamps, the needle passes.
- **Structure.** An `<article>` on the sheet: head (mono date
  stamp "DAY 3 — FRI 03 OCT" + station time; Spectral title;
  the underline trace, §6.9), body at the diary's measure,
  apparatus row (the entry's readout §6.7 where it has one,
  its felt line — "FELT AT THE STATION HOUSE" or "NOT FELT —
  TOO DEEP, TOO FAR" — in mono apparatus), and the keeper's
  aside in Spectral Italic where the diary has one. Event
  entries carry their spike in the rail (§6.3); calm entries
  carry a printed "QUIET" stamp in apparatus when the day
  logged no event above the floor — a calm day is stamped,
  not skipped.
- **Motion spec.** Trigger: the entry's head crossing the
  reading line (§4): the sheet settles (a 2px translate and
  the smoke layer's local phase aligning, 500ms
  `--ease-write`), its underline trace draws to the entry's
  span (600ms), its apparatus prints. Nothing else moves: an
  entry is read, not performed. Card variant (listing pages):
  sheets stack with 24px smoked overlaps; hover lifts the top
  sheet (§6.9's grammar at 0.7°).
- **States.** Unreached (printed, awaiting the needle — fully
  legible; "unreached" is a position, not a visibility) →
  settling (at the needle) → read (rest, latched). Hover:
  §6.9's tremor. Focus-within: the settle fires if it has not.
  *Disabled / no-JS:* every entry printed, settled, complete.
- **Content merge.** The entry is the content; the theme's
  other elements are its instruments. Its fraction on the
  sheet is its date's fraction in the watch (§4), its
  underline is its own ground, its apparatus is its own
  record row (§6.14) rendered in place.
- **Failure fallback.** The settle is transform-and-layer
  only; its failure leaves a printed entry. No watchdog is
  required because no state hides anything — the entry's
  pre-state is a 2px offset, stated here so a builder cannot
  "improve" it into a fade (§9, failure 3).
- **Reduced-motion variant.** Entries print without settling;
  the underline stands drawn; the QUIET stamp and apparatus
  are identical — the diary read flat is still the diary.
- **Performance budget & mobile variant.** Entries are HTML;
  the settle is one transform per entry, armed once. Mobile
  (<768px): the apparatus stacks beneath the title, the entry
  strip (§6.2) heads the sheet, separations compress to 64px
  calm / 40px event.
- **Choreography timeline (v2).** Head crosses reading line →
  t=0 settle starts → underline draws (600ms) → apparatus
  prints (stagger 60ms per item, opacity only, all items in
  the DOM throughout) → t=500 settled → latch.
- **State matrix (v2).** *Rest:* printed, read or unreached.
  *Hover:* tremor + lift. *Focus:* settle fires. *Active:*
  n/a on detail; on cards, §6.10's tap grammar. *Scrolled-
  past:* read, latched. *Disabled / no-JS:* printed complete.
  *Touch:* tap on head fires the tremor (§6.9).
- **Breakpoints (v2).** ≥1200px: apparatus row inline, rail
  carries the spike. 768–1199px: apparatus wraps under the
  title. <768px: apparatus stacks; entry strip heads the
  sheet; aside indents 16px.
- **Edge cases & failure modes (v2).** *An entry with no
  event and no aside (a truly empty day):* the sheet prints
  its stamp, its QUIET line, and one sentence of the diary's
  prose — the theme never pads a quiet day with decoration,
  and never omits it: a skipped day would falsify the watch's
  count of days. *An entry longer than 3 viewports:* its
  underline completes at its head; the needle does not wait
  for long entries, and the apparatus prints at the head, not
  the foot. *Two entries one day:* two sheets, one date
  stamp shared, times distinguished (§6.3's rule, shared).
- **Accessibility spec (v2).** Semantic `<article>` with a
  real heading hierarchy; the date stamp is text, not an
  image of a stamp; apparatus in reading order after the
  body it belongs to (DOM order: head, body, apparatus —
  visual order matches). Contrast per §2's pairs.
- **Tokens consumed (v2).** `--paper`, `--paper-warm`,
  `--ink`, `--ink-soft`, `--station-deep`, `--smoke`,
  `--grid`, `--ease-write`, `--dur-settle` (500ms).

### 6.13 The felt-report form — "Did you feel it?"

- **What & why.** The theme's conversion: a reader who felt an
  event files a report — the card the station has collected
  from the public since before the web, now the page's form.
  It belongs because it is the diary's one door opening
  outward: the instrument records the ground, but only people
  can record what the ground did to their houses, and the
  station's archive of felt reports (405 across the worked
  watch) is half its scientific value. The form's confirmation
  is an entry in the station log with a number derived from
  the printed count — for the Day 3 event, whose printed count
  stands at 268 reports, the visitor's confirmed report is
  № 269 — so the visitor leaves *inside* the record they came
  to read.
- **Structure.** A form on a `--paper-warm` card styled as the
  station's printed report card: fields for the event (a radio
  row of the watch's three felt events — Day 3 M 6.2, Day 7
  M 3.4, Day 19 M 4.7 — each printed with its full apparatus,
  §3 law 5), where the reader was (text, "village, street or
  landmark — as you would tell the keeper"), what moved (a
  checkbox row in the log's vocabulary: "the windows", "the
  hanging lamps", "the water in the tank", "the floor itself",
  "nothing moved — I felt it in myself"), an optional sentence
  in the reader's own words, and a name or mark (optional —
  the station accepts anonymous reports and says so). Labels
  in mono apparatus; the submit is a seal-button (§11) reading
  the fixed string *"Enter it in the station log."* (§12).
- **Motion spec.** Field focus: the field's baseline rule inks
  in (220ms `--ease-write`, a 1px `--grid` rule drawing to
  2px `--station-deep`) — the card is filled in by hand, so
  its rules ink like a pen arriving. Radio selection: the
  chosen event's row prints its spike miniature beside the
  apparatus (350ms draw, §6.3's template at card scale).
  Submit: the card taps (§6.10's grammar — the needle in the
  rail jumps once) and the confirmation prints as a log line
  (§6.15) at the card's head: timestamp (the reader's local
  time, labelled as such — the one place reader time appears,
  labelled, §6.6's law), report number, and the station's
  thanks in the Log's voice. No spinner: the card's skeleton
  state is §6.17's unwritten sheet at card scale, ceiling
  1800ms.
- **States.** Blank (printed card, all fields legible) →
  filling (rules inking, spike miniatures printing) →
  submitting (card dims one step to `--paper-deep` ground,
  fields disabled, the needle armed) → confirmed (log line
  printed, card returns, a fresh blank card offered beneath
  for a second event) / error (the offending field's rule
  prints `--event-deep`, its error in the Log's voice beneath
  it — §12 — and focus moves to it; nothing shakes: this
  instrument does not shake its forms, the ground does the
  shaking here).
- **Content merge.** The form's events are the record's felt
  three, with the record's own figures; its confirmation
  number is the record's count plus one, computed from the
  printed count and reprinted in the log band (§6.15) and the
  record table's felt column (§6.14) — three printings of one
  number, audited in §10. The form is not a widget on the
  diary; it is the diary's next page, which the reader writes.
- **Failure fallback.** Submission failure (network, server):
  the card prints the Log's line — "THE LINE TO THE STATION
  IS DOWN. YOUR REPORT IS KEPT ON THIS SHEET — TRY AGAIN, OR
  POST IT." — and the filled card remains, printable; no
  report is ever lost to a spinner. No JS: the form posts
  natively and the confirmation is a returned page in the
  same card grammar.
- **Reduced-motion variant.** Rules ink instantly, the spike
  miniature prints without drawing, the needle does not jump;
  the confirmation log line is identical.
- **Performance budget & mobile variant.** The form is HTML
  and one small script (≤6KB) for the in-place confirmation;
  the page works without it. Mobile (<768px): one column,
  radio rows at 52px, the checkbox row wraps as printed
  squares; the card is the sheet's full width.
- **Choreography timeline (v2).** Focus → rule inks (220ms) →
  event chosen → spike miniature draws (350ms) → submit →
  card dims, needle jumps (90ms, §6.10) → response → log line
  prints at card head (apparatus stagger 60ms) → count in
  §6.15/§6.14 printings updates → fresh card offered.
  Ceiling: unwritten-sheet state never exceeds 1800ms.
- **State matrix (v2).** *Rest:* blank printed card. *Hover:*
  seal-button deepens 120ms. *Focus:* rule inks; ring per
  §11. *Active:* submit press = 1px translate + the tap.
  *Scrolled-past:* n/a. *Disabled:* during submit only, with
  the state printed ("ENTERING…") in apparatus. *No-JS:*
  native post, returned confirmation page. *Touch:* 52px
  targets; the tap grammar on submit retained.
- **Breakpoints (v2).** ≥1200px: card at 640px within the
  sheet, two-column field pairs (where / what moved).
  768–1199px: card full sheet width, pairs stack. <768px:
  single column, spike miniatures omit (the apparatus
  carries the figure).
- **Edge cases & failure modes (v2).** *A report for an
  unfelt event:* the radio row offers only the felt three,
  plus a fourth printed line — "ANOTHER TIME — the ground
  moved and the diary has not printed it" — which files the
  report as *unmatched* and says so in the confirmation: the
  station does not force a reader's memory into its three
  boxes. *Duplicate report (same reader, same event):* the
  log accepts it and marks it "SECOND REPORT — SAME HOUSE";
  felt science counts houses, and the diary counts honestly.
  *A report filed days later:* the confirmation prints both
  times (event time from the record, filing time labelled
  reader-local) — the diary never back-dates a report into
  the event's day.
- **Accessibility spec (v2).** Real `<form>`, real labels,
  errors associated with `aria-describedby` and announced by
  the log line's `role="status"` (the confirmation only —
  never the ticking apparatus). Targets ≥44px. Contrast:
  labels `--ink` on `--paper-warm` 11.56:1; errors
  `--event-deep` on `--paper-warm` 7.33:1.
- **Tokens consumed (v2).** `--paper-warm`, `--paper-deep`,
  `--paper`, `--ink`, `--station-deep`, `--event-deep`,
  `--grid`, `--ease-write`, `--ease-tap`, `--dur-ink`
  (220ms), `--dur-ceiling-form` (1800ms).

### 6.14 The station record table

- **What & why.** The watch's whole record on one sheet: the
  one licensed table (§11), printing every event at or above
  the diary's threshold with its station time, magnitude,
  depth, distance and bearing, felt reports, and the felt-at-
  the-station mark — followed by the watch's totals row. It
  belongs because a diary that performs its numbers owes the
  reader one place where all of them stand still, in rows,
  to be checked against each other and against the spikes
  they met along the page. Every figure in §6 traces here;
  this table is the theme's single source of truth, and §10's
  audits are run against it.
- **Structure.** A `<table>` on `--paper-warm`, head row on
  `--station-deep` with `--paper` text (the one licensed green
  surface, §2), body rows ruled with `--grid`, figures in mono
  tabular. The worked watch prints seven event rows:

  | Day | Station time | Mag | Depth | Distance | Felt reports | At the house |
  |---|---|---|---|---|---|---|
  | 1 | 06:03:12 | M 2.1 | 6 km | 9 km E | 0 | Not felt |
  | 3 | 14:22:08 | M 6.2 | 14 km | 38 km SSW | 268 | Felt — the house event |
  | 7 | 21:15:44 | M 3.4 | 9 km | 11 km NE | 41 | Felt — a rattle |
  | 12 | 03:58:02 | M 1.8 | 4 km | 5 km W | 0 | Not felt |
  | 19 | 02:47:51 | M 4.7 | 31 km | 64 km S | 96 | Felt — deep and slow |
  | 24 | 11:31:19 | M 2.9 | 12 km | 22 km NNW | 0 | Not felt |
  | 30 | 23:59:41 | M 3.1 | 18 km | 47 km SE | 0 | Not felt |

  Totals row, printed beneath in the Log's voice: "186 EVENTS
  LOGGED IN 30 DAYS — 7 PRINTED — 3 FELT AT THE HOUSE — 405
  REPORTS FILED." (268 + 41 + 96 = 405; the arithmetic is the
  audit's first check.) The table is unsortable by law: a
  record is in time order, and a control that reorders it
  teaches the reader that chronology is a preference.
- **Motion spec.** Trigger: the table entering the needle's
  reach — its rows do not animate in; the table is *already
  printed* (it is the record). The one motion: as the needle
  passes each row's day-position, the row's magnitude cell
  prints deep (`--ink` → `--ink-deep`, 200ms) — the needle
  acknowledging its own entries as it passes them in summary.
  The totals row's figures count plainly (§6.7's rule: derived
  figures do not overshoot) over 900ms when the needle reaches
  the table's foot.
- **States.** Printed (rest, the only honest state) → rows
  acknowledging (needle passing) → printed. Hover on a row:
  its rule deepens and the rail shows that day's spike at the
  rail's position (the trace scrolls its window — no: the
  rail is the page's own length; instead the row's spike label
  in the rail warms, §6.3's twin grammar). Focus: rows are not
  controls; the table's caption carries its summary for
  assistive reading. *Disabled / no-JS:* printed, complete.
- **Content merge.** The table is the record the whole page
  was drawn from, printed at the diary's end like the summary
  sheet a keeper pastes inside the drum-room door. Its
  position is structural: after the last entry, before the
  footer — the diary first tells, then tables.
- **Failure fallback.** None needed and none invented: a
  static table is its own fallback. If its data fails to
  load in a CMS build, the sheet prints the Log's line ("THE
  RECORD IS BEING COPIED FROM THE DRUM — RETURN AT THE NEXT
  SHEET") in place of rows — never an empty ruled grid
  pretending to be a quiet month.
- **Reduced-motion variant.** Identical table; the row
  acknowledgement becomes a printed deep state applied on
  entry (no transition); totals stand printed.
- **Performance budget & mobile variant.** The table is HTML
  text, ≈2KB. Mobile (<768px): the table becomes a stack of
  ruled row-cards (day + time as the head, figures as
  apparatus pairs) — the figures never shrink below 13px mono
  to fit a width; the layout yields, the record doesn't.
- **Choreography timeline (v2).** Needle reaches table head →
  caption prints → needle passes each row's day → its
  magnitude deepens (200ms) → needle reaches totals → totals
  count (900ms, plain) → latch.
- **State matrix (v2).** *Rest:* printed. *Hover:* row rule
  deepens, rail twin warms. *Focus:* n/a. *Active:* n/a.
  *Scrolled-past:* rows acknowledged, totals settled.
  *Disabled / no-JS:* printed complete. *Touch:* no hover;
  acknowledgement is scroll-driven only.
- **Breakpoints (v2).** ≥1200px: full table, seven columns.
  768–1199px: the "At the house" column folds into the felt
  column as a mark. <768px: row-cards, as above.
- **Edge cases & failure modes (v2).** *A watch with 40
  printed events:* the table paginates by week (§7), totals
  always whole-watch, printed on every page of the table —
  a partial total is a wrong total. *A corrected figure:*
  the cell prints the corrected value and the log (§6.15)
  carries the correction entry; the table never silently
  changes (§6.3's rule). *Zero-event watch (a silent month):*
  the table prints its head, no rows, and the Log's line
  "NO EVENT REACHED THE PRINT THRESHOLD. THE FLOOR IS THE
  RECORD." — with the noise-floor caption beneath (§6.4).
- **Accessibility spec (v2).** A real `<table>` with `<th>`
  scope, a `<caption>` summarising the watch ("Seven printed
  events, Days 1–30; largest M 6.2 on Day 3; 405 felt reports
  filed"). Figures are text. Contrast: head `--paper` on
  `--station-deep` 8.12:1; body `--ink` on `--paper-warm`
  11.56:1.
- **Tokens consumed (v2).** `--paper-warm`, `--station-deep`,
  `--paper`, `--ink`, `--ink-deep`, `--grid`, `--ease-write`,
  `--dur-ack` (200ms), `--dur-totals` (900ms).

### 6.15 The station log band

- **What & why.** A running band of the station's log entries
  — mono, timestamped, terse — set into the sheet at the
  diary's joints: corrections, instrument notes, arrivals of
  reports, the changing of the sheet. It belongs because a
  real diary has two hands in it: the Diarist's entries and
  the station's log, and the log is where the diary admits
  things — a corrected magnitude, a missed hour, a drum that
  stopped in the night and says so. It is also the theme's
  notification system (§11): anything the site must tell the
  reader appears here, as an entry, timestamped and kept —
  never as a toast that vanishes.
- **Structure.** A ruled band (`--paper-deep` bed, `--grid`
  rules) holding log lines in mono 13px: "DAY 4 — 09:12 —
  SHEET CHANGED. THE DAY 3 SHEET IS IN THE FLAT DRAWER,
  UNFIXED, FOR ANY WHO ASK." / "DAY 19 — 03:40 — CORRECTION:
  THE DAY 19 DEPTH READS 31 KM, NOT 29. THE FIGURE IN THE
  TABLE IS CORRECTED; THIS LINE IS ITS RECEIPT." Each line
  prints with its timestamp; the band appears at three
  licensed joints on a diary page (after the hero entry,
  mid-watch, before the record table) and carries at most
  four lines per appearance — a log that sprawls is a second
  diary competing with the first.
- **Motion spec.** Trigger: scroll — as the band crosses the
  reading line, its lines ink in one at a time (opacity +
  a 1px rule draw beneath each, 90ms stagger, `--ease-write`)
  — a log being written as it is reached. Confirmations from
  §6.13 print into the nearest band below the form as well as
  at the card, in the same line, so the site has one voice
  for "it is entered". Lines never delete or auto-dismiss;
  the log is a record (§1 clause 2 applies to the log's own
  lines first of all).
- **States.** Unwritten (lines in DOM, un-inked — legible;
  inking is a ceremony, not a reveal) → inking → printed
  (rest). Hover: none. Focus: a line is not a control; a
  line containing a link (to the corrected table) carries
  §11's link treatment. *Disabled / no-JS:* printed.
- **Content merge.** The band's lines are about *this* diary:
  its sheets, its corrections, its reports. A log line that
  could appear on any site ("WELCOME TO OUR WEBSITE") fails
  §12's voice audit — the log speaks of the instrument and
  its record, or it does not speak.
- **Failure fallback.** The inking is opacity over printed
  text; failure leaves print. A confirmation that fails to
  print into the band still stands at the form card (§6.13)
  — the band is the second printing, and §10 checks both.
- **Reduced-motion variant.** Lines print without stagger;
  the band reads as a pasted log slip, which is what it is.
- **Performance budget & mobile variant.** Text and rules;
  the stagger is ≤4 timers. Mobile: the band spans the sheet,
  lines wrap at 13px mono without shrinking.
- **Choreography timeline (v2).** Band head crosses reading
  line → line 1 inks (rule 160ms) → +90ms line 2 → … → last
  line → band printed; latch. Form confirmation: prints at
  card instantly, inks into the band when reached.
- **State matrix (v2).** *Rest:* printed. *Hover:* none.
  *Focus:* link lines carry focus normally. *Active:* n/a.
  *Scrolled-past:* printed, kept. *Disabled / no-JS:*
  printed. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: band inset 48px from the
  sheet's edges. 768–1199px: inset 24px. <768px: full sheet
  width, lines at 12.5px (mono apparatus floor — never
  below 12px, §3).
- **Edge cases & failure modes (v2).** *A correction to a
  correction:* lines stack in time order; the log never
  edits a line, it appends — "DAY 20 — THE LINE OF DAY 19
  READ 29 KM IN ERROR; THE DEPTH IS 31 KM." *An empty band
  (a joint with nothing to admit):* the band does not render
  — the log has no filler voice, and an empty ruled band
  would be a lie of omission in reverse.
- **Accessibility spec (v2).** The band is a `<section>` with
  an apparatus heading ("STATION LOG"); confirmations use
  `role="status"` at the form only (§6.13), the band's copy
  is plain text in reading order. Contrast: `--ink` on
  `--paper-deep` 9.39:1.
- **Tokens consumed (v2).** `--paper-deep`, `--ink`,
  `--ink-soft`, `--grid`, `--ease-write`, `--dur-logline`
  (160ms), `--dur-logstagger` (90ms).

### 6.16 The drum-room footer

- **What & why.** The footer is the drum room after hours: a
  `--drum-dark` ground carrying the watch's whole trace printed
  flat in miniature (the diary's month at a glance, in
  `--paper` line over a red spike train), the station's
  imprint, the full chapter ruler repeated (§6.11's fallback
  promise), and the totals in lamplight inks. It belongs
  because a diary should end the way the day ends at the
  station: the sheet comes off the drum, the room darkens, and
  what remains is the record, whole, small, and checkable —
  the footer's miniature trace is the page the reader just
  read, drawn once more at a size where its shape can be
  judged.
- **Structure.** A dark band: the miniature trace (one SVG,
  the full watch's waveform at footer scale, spikes in
  `--event` as lines only — on the dark ground red is a line,
  never text, §2), the imprint block (station name in Spectral
  on dark, apparatus in `--station-pale`), the chapter ruler
  in paper line-work, and the closing line in Spectral Italic:
  *"The drum turns whether or not anyone is watching."*
  (§12's fixed string.) The totals print in mono: "186 EVENTS
  — 7 PRINTED — 405 REPORTS" — the third printing of the
  watch's figures (§6.14's audit chain).
- **Motion spec.** Trigger: the footer entering view — the
  miniature trace draws once (900ms `--ease-write`, left to
  right, the month in a breath) and the totals count plainly
  (§6.7's rule). Nothing else moves in the dark room; the
  footer is the page at rest, and its stillness after the
  diary's trembling is the point.
- **States.** Undrawn (printed in DOM) → drawing → printed
  (rest). Hover on ruler links: §6.11's grammar in paper ink.
  Focus: §11's paper ring on dark. *Disabled / no-JS:*
  printed, totals standing.
- **Content merge.** The miniature is *this page's* trace —
  same record, same deflections, scaled once more and with
  the scaling stated ("THE WATCH AT 1:40 — THE SPIKES ARE
  TRUE"). A generic footer graphic would fail §10's record
  audit like any other forgery.
- **Failure fallback.** The draw is a mask over the printed
  miniature; watchdog 1500ms snaps it drawn. The dark ground
  and imprint are static HTML.
- **Reduced-motion variant.** The miniature stands drawn; the
  totals stand printed.
- **Performance budget & mobile variant.** Miniature SVG ≤6KB
  (the record's path, decimated honestly at build — decimation
  stated in its source line, peaks preserved exactly: a
  miniature that rounds its spikes has lied at small size).
  Mobile: the miniature spans the sheet width; the imprint
  stacks.
- **Choreography timeline (v2).** Footer enters → miniature
  draws (900ms) → totals count (900ms, overlapping the draw's
  second half) → closing line stands → latch.
- **State matrix (v2).** *Rest:* printed, still. *Hover:*
  ruler grammar. *Focus:* paper ring. *Active:* n/a.
  *Scrolled-past:* n/a (it is the foot). *Disabled / no-JS:*
  printed. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: miniature at 480px beside the
  imprint. 768–1199px: miniature full width above the imprint.
  <768px: miniature full width, ruler wraps two rows.
- **Edge cases & failure modes (v2).** *A one-entry diary:*
  the miniature is that entry's waveform at footer scale —
  small, honest, mostly floor. *The dark ground in a light
  room (print):* the footer prints as its line-work on paper
  (print stylesheet inverts the ground, keeps the trace) —
  the record is the content; the room is not.
- **Accessibility spec (v2).** The miniature is `aria-hidden`;
  its figures are the printed totals beside it. Contrast:
  `--paper` on `--drum-dark` 13.31:1; `--station-pale` on
  `--drum-dark` 6.12:1; red appears as line-work only.
- **Tokens consumed (v2).** `--drum-dark`, `--paper`,
  `--paper-warm`, `--station-pale`, `--event`, `--ease-write`,
  `--dur-minidraw` (900ms), `--dur-watchdog-footer` (1500ms).

### 6.17 The unwritten sheet — skeleton & loading

- **What & why.** Loading in this theme is unwritten drum
  paper: a sheet of blank ruled grid with the needle printed
  at its head and a mono status line — *"The drum is
  turning."* (§12's fixed string) — while the diary's sheet is
  fetched and laid. It belongs because it is the only honest
  loading state this world has: before the record arrives,
  there is paper and an instrument, and nothing else — no
  shimmering fake entries pretending to be the diary arriving
  early (§1 clause 1 applies to loading too: nothing is drawn
  before it exists).
- **Structure.** A sheet at the real layout's dimensions (the
  skeleton *is* the layout: masthead ruler, entry blocks as
  ruled blank spans at their true heights, the rail as a blank
  ruled rail) — built from the page's own template with its
  content areas emptied to grid, never a generic grey-block
  approximation. The status line is visually mono apparatus
  and a visually-hidden live text for assistive readers. A
  hard ceiling of 1800ms: at 1800ms the sheet either carries
  the diary or carries the Log's delay line ("THE SHEET IS
  LATE. THE DRUM HAS NOT STOPPED — ONLY THE POST HAS.") with
  a retry — the skeleton never outlives its excuse.
- **Motion spec.** The grid's smoke layer drifts at drum speed
  (18px/s, §5) and the needle at the rail head breathes with
  the floor's character (§6.4) — the instrument is awake while
  the paper is blank. On content arrival, the sheet does not
  crossfade: the diary's first entry settles (§6.12) and the
  trace writes from the arrival fraction — the skeleton hands
  over to the record by being written on.
- **States.** Unwritten (rest) → writing (arrival) → written
  (the page). Timeout state: delay line + retry, as above.
  *Disabled / no-JS:* server-rendered pages ship written; the
  skeleton exists only for client-fetched sheets, and a
  no-JS client never sees it.
- **Content merge.** The skeleton is the page's own sheet with
  the writing not yet on it — its proportions teach the
  diary's shape (where the rail runs, where entries sit)
  before a word arrives, which is all a loading state is for.
- **Failure fallback.** The 1800ms ceiling *is* the fallback,
  with the delay line in the Log's voice (§12) and a working
  retry; a second failure prints the station's plain-text
  fallback link ("READ THE WATCH AS PLAIN SHEETS") — the
  diary degrades to paper, never to a dead spinner.
- **Reduced-motion variant.** The smoke does not drift; the
  needle stands still; the status line and ceiling are
  identical.
- **Performance budget & mobile variant.** The skeleton is the
  template's own CSS (≤3KB incremental); it is the first thing
  painted and costs no extra request. Mobile: identical at
  sheet width.
- **Choreography timeline (v2).** Request → skeleton paints
  (first paint) → drift + floor breathing → content arrives →
  skeleton's spans are replaced entry by entry in reading
  order (no global fade) → trace writes to arrival fraction →
  skeleton gone. Ceiling 1800ms → delay line.
- **State matrix (v2).** *Rest:* unwritten, drifting.
  *Hover:* n/a. *Focus:* focus is held at the sheet's head;
  on arrival it is *not* moved (the reader's place is the
  arrival fraction). *Active:* retry is a real button.
  *Scrolled-past:* n/a. *Disabled / no-JS:* never shown.
  *Touch:* identical.
- **Breakpoints (v2).** All widths: the skeleton matches the
  target layout at that width (§6.2's rail fold included) —
  a skeleton shaped like a different page is a lie about
  what is coming.
- **Edge cases & failure modes (v2).** *Instant cache hit:*
  if content arrives within 120ms, the skeleton never paints
  (a flash of blank paper is worse than none) — the diary
  simply opens written. *Partial arrival (entries stream):*
  entries settle in reading order as they land; the trace
  writes only across arrived spans — the sheet is written as
  far as it exists, and no further (§1 clause 2's loading
  form).
- **Accessibility spec (v2).** `aria-busy` on the sheet region
  with the status as its label; the visually-hidden text
  updates once at the ceiling ("still loading"), never per
  second. Focus is never inside the skeleton's blank spans.
- **Tokens consumed (v2).** `--paper`, `--paper-deep`,
  `--grid`, `--smoke`, `--ink-soft`, `--ease-drift`,
  `--dur-ceiling-sheet` (1800ms).

### 6.18 The silent page — 404

- **What & why.** The 404 is a page the needle has not
  reached: a dark sheet (`--drum-dark`, the room after hours)
  carrying a printed flat trace that runs calmly across it and
  stops mid-line, a Spectral line — *"Nothing is recorded
  here."* — and the Log's apparatus beneath: "NO ENTRY EXISTS
  AT THIS ADDRESS. THE DRUM HAS NOT STOPPED; THIS PAGE WAS
  NEVER ON IT." with links, as ruled ruler ticks, to the
  watch, the record and the station. It belongs because it is
  the theme's one licensed use of darkness and of the stopped
  line: an address outside the diary is a place where the
  record genuinely does not run, and the page says so in the
  diary's own grammar instead of borrowing a mascot.
- **Structure.** A dark sheet: the flat trace (printed, at
  floor amplitude, ending in a clean cut at 60% of its run —
  the line stops because there is nothing after it, not as a
  glitch effect), the line in Spectral 34px `--paper`, the
  apparatus in `--station-pale` mono, three ruler-tick links.
  Its choreography is specified as *nearly none*: the floor
  breathes in the trace's printed segment (§6.4's character,
  baked) and nothing else moves — the stillest page on the
  site, on purpose.
- **Motion spec.** None beyond the baked floor. No spike, no
  roll-in beyond §6.10's sheet change that brought the reader
  here. The absence is the design: a 404 that performs has
  mistaken itself for content.
- **States.** Printed (the only state). Hover on the tick
  links: §6.11's grammar in paper ink. Focus: paper ring.
  *Disabled / no-JS:* identical — this page ships no script
  beyond the shared furniture.
- **Content merge.** The stopped trace is the diary's line,
  recognisably, ending where the reader's address left the
  record; the links are the ruler that runs the whole site.
  The page is inside the world precisely by marking where the
  world ends.
- **Failure fallback.** None required: static print on a dark
  ground. If the dark ground fails to load (CSS failure), the
  page prints dark text on paper with the same words — the
  sentence survives its room.
- **Reduced-motion variant.** Identical. (The page is the
  variant's own proof: a complete page with no motion at all
  still reads as this theme.)
- **Performance budget & mobile variant.** The lightest page
  on the site (≤40KB total). Mobile: the trace spans the
  sheet, the line wraps at 28px, ticks stack.
- **Choreography timeline (v2).** Sheet change (§6.10) →
  the silent page stands. That is the whole timeline, and
  §10 checks that no builder has added to it.
- **State matrix (v2).** *Rest:* printed. *Hover:* link
  grammar. *Focus:* paper ring. *Active:* n/a. *Scrolled-
  past:* n/a. *Disabled / no-JS:* identical. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: line 34px, trace at 60% run.
  768–1199px: line 30px. <768px: line 28px, ticks stack at
  44px.
- **Edge cases & failure modes (v2).** *A soft 404 (an empty
  archive page):* uses this page's grammar at paper ground —
  the record exists but this shelf is empty — with the Log's
  line "THE WATCH IS KEPT; THIS SHELF IS EMPTY." Darkness is
  reserved for addresses outside the record entirely.
- **Accessibility spec (v2).** A real `<h1>` (the Spectral
  line), links as links with descriptive text, contrast
  `--paper` on `--drum-dark` 13.31:1, `--station-pale` 6.12:1.
- **Tokens consumed (v2).** `--drum-dark`, `--paper`,
  `--station-pale`, `--ink`, `--floor-amp` (2px).

## 7. Page application map

**Home — the current watch.** The diary itself: hero (§6.1,
the watch's largest event), entries in time order (§6.12),
log bands at their joints (§6.15), the record table (§6.14),
the felt form after the largest event's entry and again at
the foot (§6.13 — a reader files when the ground has just
moved under the text, or when the diary has earned them),
footer (§6.16). The full choreography is §13.

**Listing — the archive of watches.** Past watches as entry
sheets (§6.12's card variant) stacked by season, each card
carrying its watch's miniature trace (its own record at card
scale — a card without its trace is a title without a diary)
and its totals in apparatus. The rail on listing pages is a
summary rail: one spike per watch (its largest), so the
archive's margin is a skyline of worst days, honestly scaled
by the same function.

**Detail — one event.** A single event's page is one entry
grown to a sheet of its own: the event's waveform at full drum
scale across the head (the hero grammar without the jitter —
the event is examined now, not re-lived), its full apparatus,
its felt reports as a log stream (§6.15's grammar, uncapped —
this is the one page where reports *are* the content), its
drum-frame prints (§6.8), and the felt form for that event
alone. Neighbouring events are the ruler's previous/next
ticks: chronology as pagination.

**About — the station & the instrument.** The one page allowed
off the drum: plain mounts (§6.8's undated rule), the
instrument's description with a printed diagram of the needle
assembly, the keeper's account in the Diarist's voice, and
the station's facts in the Log's. Its single trace is the
current day's, printed flat in its head — the station page
still signs itself with today's line.

**Contact / visit — the drum room.** The felt form's sibling:
a visit request in the report card's grammar (§6.13), the
station's visiting hours as a log table, and a map treated as
a drum-frame print with a station time ("the road to the
ridge, photographed on a quiet day"). Conversion here is a
visit booked; its confirmation is a log line with a number
derived from the printed count of booked visits, by §6.13's
rule.

**404 — the silent page** (§6.18). **Search — the diary
index:** one log-ruled field (§11) on its own sheet; results
as entry cards (§6.12), each with its day and magnitude in
apparatus — a result without its figures is a rumour, and the
index does not print rumours.

## 8. Worked examples

The worked site throughout: **Bracken Ridge Station** — a
one-keeper observatory publishing its tremor diary; the
October watch, Days 1–30, as recorded in §6.14.

### 8.1 The hero — "The Day 3 Event" (home)

The visitor arrives. The sheet is drum paper; the masthead
ruler (§6.11) stands expanded; below it the hero band (§6.1):
a horizontal drum band 280px tall, its trace idling at the
floor. The `<h1>` stands printed above the band: "The day the
ridge answered back." — the Diarist's headline, eight words,
making a claim the band is about to verify. Beside the band,
the readout stands at its DOM value, M 6.2, with its full
apparatus (§3 law 5): "14 KM DEEP — 38 KM SSW — DAY 3,
14:22:08". At t=800 the event hits: the needle throws
+110.3px, the headline's letters ride the same waveform at
5px peak, the readout swings to 6.5 and damps home to 6.2 by
t=2200. Below the band, the Day 3 entry (§6.12) waits already
printed — its first line the keeper's: *"At 14:22 the house
shook the way it did in the photographs of other people's
earthquakes."* The visitor has been on the page for three
seconds and has already read the diary's method: a claim, an
instrument's performance of it, and a person's sentence under
both. Scroll timeline: first scroll — the margin trace (§6.2)
begins writing at the rail; the station clock (§6.6) stands
at DAY 1 — 00:00:00 and starts its compressed climb; the
hero's drift pauses as the band leaves the screen.

### 8.2 Mid-page — the Day 19 entry & the record band

Deep in the watch, the diary's second-greatest entry: DAY 19
— 02:47:51 — M 4.7, 31 km deep, the deepest of the watch. The
reader arrives through the quiet stretch (Days 12–18: two
short entries, one QUIET stamp, the trace near-flat for a
full viewport — §4's load-bearing hush). The Day 19 sheet
settles at the needle; its spike has already drawn in the
rail at 17.5px margin deflection (39.0px × 0.45) as the write
head crossed its fraction; its readout counts to 4.7 with a
0.3-capped overshoot it visibly struggles less with than
Day 3's did — the reader *feels* the scale difference before
reading either figure. The keeper's aside, in italic: *"Too
deep to hear. The needle heard it for us."* Beneath the
entry, the log band (§6.15) carries the correction line of
Day 19 — 03:40, the depth revised 29 → 31 km — and the entry's
apparatus and §6.14's table both print 31: the correction is
visible in the log, and invisible in the figures, which is
exactly how a trustworthy record behaves. Scroll timeline:
hush (floor only) → spike draw (600ms) → readout count
(1400ms) → entry settle → log lines ink (90ms stagger) →
needle tremble gain falls back as Day 24's calm begins.

### 8.3 Conversion — filing a felt report for Day 3

After the record table, the report card (§6.13) stands on its
warm sheet: "DID YOU FEEL IT?" in apparatus, and the Diarist's
one line above it: *"The needle keeps the ground's diary.
Only you can keep your house's."* The visitor selects the
Day 3 row — its spike miniature draws beside the apparatus —
checks "the hanging lamps" and "the floor itself", writes
"The wardrobe door swung open and shut, once." in the
sentence field, and presses the seal-button: *"Enter it in
the station log."* The card dims a step; the rail's needle
jumps once (the reader's event, recorded); the confirmation
prints at the card's head as a log line: the filing time
labelled reader-local, then — "REPORT № 269 FOR THE DAY 3
EVENT. ENTERED. THE STATION THANKS YOU." — № 269 because the
printed count stood at 268 (§6.14's felt column), and as the
visitor scrolls on, the log band below carries the same line
and the table they passed now reads 269 in its cell and 406
in its totals when they return to it: one number, three
printings, no contradictions. Scroll timeline: card at the
needle → fields ink on focus → submit tap (90ms) → log line
prints (apparatus stagger) → fresh blank card offered beneath
for the Day 7 event the visitor also felt.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The screensaver seismograph.** A random wiggle looping
   decoratively behind a hero, sized by eye, meaning nothing.
   *Cure:* every deflection is computed from the record by
   §5's function; the only unscripted line on the page is the
   captioned noise floor (§6.4), and it is small, honest and
   labelled.
2. **Spikes without entries.** A dramatic spike in a section
   whose text reports no event — drama borrowed against a
   record that does not hold it. *Cure:* §10's record audit:
   every spike's fraction, magnitude and label must match a
   §6.14 row, or the build fails.
3. **The fade-up diary.** Entries fading and rising like every
   other site on the internet, the trace reduced to a border.
   *Cure:* §3 law 2 and §6.12's stated pre-state (a 2px
   settle). The diary's reveal is the needle arriving, not
   the content performing.
4. **Alarm inflation.** Red everywhere — red links, red
   headings, a red "live" badge — until the Day 3 spike is
   just the reddest thing on a red page. *Cure:* §5's red
   ration and §10's pixel audit (≤4% per viewport).
5. **The dead floor.** A trace drawn ruler-straight between
   events, claiming the earth holds its breath for your
   prose. *Cure:* §6.4's floor, baked and live, with its
   caption. A flat calm is a broken instrument, not a calm
   day.
6. **The cursor needle.** A custom cursor shaped like a needle,
   or a needle that follows the pointer. *Cure:* forbidden
   outright — normal system cursor (§ standing rules), and
   §6.5's needle answers scroll and record only. The reader's
   hand is not the earth's hand.
7. **Serif magnitudes, mono diary.** The two voices swapped for
   "warmth" or "techiness" until neither means anything.
   *Cure:* §3's constitution and its five laws; the gate
   greps figure elements for their computed font.
8. **Stock prints.** Photographs that could illustrate any
   earthquake article anywhere, dropped between entries.
   *Cure:* §6.8's contract — a frame carries a station time
   from the record, or it does not enter the diary.
9. **Filling the hush.** A quiet stretch "enlivened" with
   graphics, pull-quotes or a mid-page promo because the
   analytics feared boredom. *Cure:* §4 — the hush before a
   spike is load-bearing. The diary's quiet days are its
   credibility; a builder who decorates them has not
   understood what the spikes are worth.
10. **The fake "LIVE".** A pulsing badge claiming the page is
    live when it is a written diary. *Cure:* §1 — the theme
    is a record. The floor's caption (§6.4) is the model: it
    says what the noise *is*, including what it is not.
11. **Overshoot theatre.** Every number on the page bouncing —
    depths, distances, counts — until the needle's physics is
    a house style. *Cure:* §6.7's distinction: only what the
    needle measured overshoots; derived figures count plainly
    or stand printed.
12. **The unwriting diary.** Scroll up and the trace erases,
    readouts reset, the month performs itself again for the
    returning reader. *Cure:* §1 clause 2's ratchet, audited
    by §10's scroll-back test. A record that resets is a toy.

## 10. Quality gate

Blocking checks; the theme ships when all pass, run by a
non-builder.

1. **Record audit.** Every spike, readout and printed figure
   on the page is sampled against §6.14: fraction, magnitude,
   depth, distance, time. One orphan figure fails the build.
2. **Amplitude audit.** Three spikes (largest, median,
   smallest) are measured on screen against `d(M) = 6 ×
   2^(M−2)` at their gearing: within ±2px, or the build has
   forged a tremor.
3. **Figure reconciliation.** The watch's numbers agree in
   every printing: 186 / 7 / 3 / 405 in §6's prose, §6.14's
   totals, §6.16's footer; the felt counts 268 / 41 / 96 sum
   to 405; a filed report increments all printings to 269 /
   406 consistently (§8.3).
4. **Dead-JS test.** With JavaScript disabled: the full trace
   printed, every entry legible, every figure at its settled
   value, the form submittable. Anything invisible fails.
5. **Watchdog drill.** With the shared loop artificially
   stalled: hero written by 2500ms, trace and readouts
   settled by 1500ms, transitions snapped by 1200ms, skeleton
   ceiling at 1800ms honoured with the delay line.
6. **Ratchet test.** Scroll to the foot, return to the head:
   nothing unwrites, no readout re-counts, station time holds
   its maximum. Any re-performance fails.
7. **Needle agreement.** At five scroll positions, the needle's
   deflection equals the trace's deflection at the write head
   (±1px). The instrument and its record are one datum.
8. **Floor statistics.** The noise floor's amplitude stays
   within ±2px (drum scale) outside event spans; eventlets
   occur at the captioned character rate; the floor never
   flatlines for more than 4s of reading at the head segment.
9. **Red ration.** Event-red pixels ≤4% of any viewport at
   five scroll positions; no red text below the licensed
   sizes/registers (§2, §3 law 3).
10. **Contrast audit.** Every text pairing meets §2's measured
    figures in every state — including mid-count readouts
    (`--ink`, 10.86:1) and the dark room (`--station-pale`,
    6.12:1).
11. **Reduced-motion pass.** With `prefers-reduced-motion`:
    the still drum, flat printed trace, settled figures,
    printed log — the complete diary, verified on a device,
    not a devtools toggle alone.
12. **Voice audit.** §12's registers sampled: no magnitude
    without depth at first printing, no banned phrase, errors
    and empty states in the Log's voice with specifics.
13. **Performance audit.** §14's budgets measured on the
    reference device: frame ≤1.6ms in the loop, no long task
    >50ms after load, page weight within budget.

## 11. Component inventory

Every component a real Seismograph Diary site needs, with its
themed treatment. Components the theme refuses are listed with
the refusal's reason and the in-theme replacement — a refusal
without a replacement is a gap, and there are no gaps.

| Component | Treatment in this theme |
|---|---|
| Primary button | The seal-button: `--station-deep` rectangle, `--paper` text, radius 0, press = 1px translate + the case-tap (§6.10). One per view; its label is a fixed string where §12 owns one. |
| Secondary button | Paper ground, 1px `--ink` rule, ink text; hover rule doubles 200ms. |
| Text link | `--station-deep` with a drawn rule (220ms); in the footer, `--paper` with a `--station-pale` draw. |
| Navigation | The drum-edge ruler (§6.11). |
| Hero | The headline event (§6.1) on home; an event's full-scale waveform (§7, detail) elsewhere. |
| Cards | Entry sheets (§6.12), stacked with smoked overlaps on listing pages. |
| Data table | The station record (§6.14) — the only table pattern; time-ordered, unsortable by law. |
| Form fields | Report-card fields (§6.13): baseline rule inking on focus, mono labels, errors in `--event-deep` in the Log's voice. |
| Radio / choice | Event rows (§6.13): full apparatus + spike miniature; the diary's choices are always few and always figured. |
| Checkbox | A small printed square with an ink tick — a mark on a card, not an OS widget. Label in the Log's vocabulary ("the hanging lamps"). |
| Select | **Refused** — a native dropdown is a machine part from another room. Replacement: radio rows (§6.13) for ≤7 options; an index page (§7) for more. |
| Tabs | **Refused** — a diary is read along its length, not filed. Replacement: chapters on the ruler (§6.11) + the log band (§6.15) at the joints. |
| Accordion | The instrument-notes accordion — the one licensed pattern: ruled rows that open like a sheet lifting (§6.9's tilt at 0.5°), for "how the drum works" apparatus on the about page. |
| Modal / dialog | **Refused as overlay.** Replacement: a dedicated sheet via the drum revolution (§6.10), or an in-flow panel on `--paper-warm`. A legal consent that must interrupt prints as a plain panel in flow, unadorned. |
| Toast | **Refused.** Replacement: a log line (§6.15) — timestamped, kept, in the Log's voice. Nothing on this site appears and vanishes; the diary keeps what it says. |
| Tooltip | **Refused.** Replacement: the marginalia aside — if a figure needs explaining, its source line prints beside it (§6.7), not on hover. |
| Progress bar | **Refused.** Replacement: station time (§6.6) and the written trace (§6.2). |
| Spinner | **Refused.** Replacement: the unwritten sheet (§6.17) with its 1800ms ceiling. |
| Pagination | **Refused** for the diary and the record (the record is whole). For the archive: whole watches as sheets (§7), linked by the ruler's ticks — a diary is not sliced. |
| Badge / tag | The magnitude chip: a small `--paper-deep` lozenge (radius 2px — sheets are squared; the chip is a label pasted on) with "M 4.7" in mono 11px. For facts ("FELT AT THE HOUSE"), never for marketing. |
| Alert / notice | A log entry panel (§6.15): `--paper-deep` ground, 2px `--event-deep` left rule only when the log admits an error or correction, the Log's voice, printed — never auto-dismissing. |
| Breadcrumbs | **Refused** — the needle (§6.5) and station time (§6.6) carry orientation; a crumb trail on a diary is a second, worse chronology. |
| Search | The diary index (§7): one log-ruled field; results as entry cards with day + magnitude in apparatus. |
| Image | Drum-frame prints (§6.8) with station times; undated photography only on the about page, in plain mounts, outside the record. |
| Footer | The drum-room footer (§6.16). |
| 404 | The silent page (§6.18). |
| Focus ring (cross-cutting) | `--ink` 2px, 2px offset on paper grounds; `--paper` 2px on `--drum-dark`. Never red (the alarm's colour is not a state), never green at 2.26:1 on dark (the ring on dark is paper). |
| Radius law (cross-cutting) | 0 everywhere — sheets are cut square — except the instruments that are round by craft: the needle's pivot (§6.5), the drum's edge itself. A rounded card has wandered in from another theme. |

## 12. Content & copywriting voice

Two registers, kept apart as strictly as the palettes.

**The Diarist** — the keeper's voice: the person who changes
the sheet, walks out to look at the crack, and writes the
entry. Literary, dry, exact; first person plural ("we heard
the lamps before we felt the floor"); speaks in sentences a
diary would keep. Never sensational — the Diarist has stood
in the house during the event and does not need adjectives
for it. Headlines are claims the instrument then verifies
("The day the ridge answered back." — verified by the band,
§8.1). Maximum 9 words for a display line.

**The Log** — the station's voice: timestamps, magnitudes,
corrections, errors, empty states. Figures with their full
apparatus (§3 law 5), always. The Log never exclaims, never
apologises in the abstract, and — its signature — *the Log
admits*: a correction is printed with its receipt (§6.15), a
missed hour is entered as missed, a quiet month is tabled as
quiet (§6.14).

**Headline style.** ✓ "The day the ridge answered back."
✓ "Thirty days, and the ground spoke seven times." ✗ "The
earthquake that SHOOK our town!!" ✗ "Welcome to Bracken
Ridge — your home for live seismic thrills!" (the diary is
not live, and it does not thrill).

**Label style.** Labels are station apparatus: fact + figure.
✓ "DAY 19 — 02:47:51 — M 4.7 — 31 KM DEEP". ✓ "FELT AT THE
HOUSE — 96 REPORTS". ✗ "Big one!!" ✗ "Event #5 (details
inside)" (the apparatus *is* the details).

**Error voice** (the Log, correcting an entry — never the
machine's fault, never the visitor's). ✓ "The log wants a
place for this report — a village or a landmark will do."
✓ "That time is after the event it reports. The drum keeps
the order; give the hour as you remember it and the log will
mark it remembered." ✗ "Invalid input." ✗ "Oops! Something
went wrong."

**Empty-state voice.** ✓ (a silent watch's table) "NO EVENT
REACHED THE PRINT THRESHOLD. THE FLOOR IS THE RECORD."
✓ (an archive shelf) "THE WATCH IS KEPT; THIS SHELF IS
EMPTY." ✗ "No results found." ✗ Any empty state that fills
itself with a decorative waveform and an apology — the
silent page (§6.18) is the model: stillness and a fact.

**Banned words & constructions.** "Earth-shattering" and
every quake pun ("rocked", "shook the internet", "tremor
with excitement"), "live" for anything recorded, "real-time"
in any form, exclamation marks in the Log's register (the
Diarist may have one per page; the worked examples have
none), a magnitude without its depth at first printing,
percentages in progress contexts (station time is the
progress, §6.6), "content" for the site's own material (it is
*the diary*, *the record*, *the watch*), and any figure
without its source — the record (§6.14) — within the same
figure's apparatus.

**Owned words.** The watch, the drum, the needle, printed (an
event is *printed* when it reaches the threshold), felt, the
floor (for the noise floor, never for a storey), station
time, the house (for the station house and its felt marks),
to enter (in the log).

**Verbatim fixed strings** (builders do not paraphrase):
- The form's submit: *"Enter it in the station log."* (§6.13)
- The skeleton's status: *"The drum is turning."* (§6.17)
- The footer's close: *"The drum turns whether or not anyone
  is watching."* (§6.16)
- The silent page's line: *"Nothing is recorded here."*
  (§6.18)
- The floor's caption: *"The quiet on this page is real
  quiet, recorded, not drawn: the floor breathes with the
  character of the public feed of station ANMO, Albuquerque,
  whose restlessness the keeper admires and does not copy."*
  (§6.4)

## 13. Full-page scroll choreography map

The home page (§8's site), top to bottom, one watch. Every
beat names what the visitor sees and what it is *for*; a beat
with no purpose is cut, not kept.

1. **Load — the event (fraction 0.00).** Masthead expanded,
   drum drifting, trace idling at the floor for 800ms, then
   the Day 3 spike fires in the hero band and the readout
   damps to 6.2. *The diary's thesis performed before its
   first sentence: this page is written by the ground.*
2. **First scroll — the record begins (0–0.10).** The margin
   trace starts writing at the rail; the station clock stands
   at DAY 1 — 00:00:00 and begins its compressed climb; the
   needle pins at the reading line. *The visitor's hand is on
   the drum; the page teaches its physics by being read.*
3. **Day 1 — the watch opens (0.14).** The first entry settles;
   its small spike (M 2.1, 2.9px in the rail) draws almost
   shyly. *Scale is taught at the small end first: this is
   what a little event looks like on this instrument.*
4. **Day 3 — the house event (0.30).** The chapter the hero
   promised: the rail spike throws 49.6px, the readout counts
   with its full overshoot, the felt line prints, the log band
   below carries the sheet-change line. *The page's centre of
   gravity — every instrument agreeing at once, at maximum.*
5. **Days 7–12 — the falling rhythm (0.44–0.56).** A rattle
   (M 3.4, felt, 41 reports) and the watch's smallest printed
   event (M 1.8); entries at reading density. *After the
   climax, the diary breathes — and the reader learns the
   middle of the scale.*
6. **The hush — Days 13–18 (0.60).** One viewport of near-flat
   trace, one QUIET stamp, sparse prose. *The floor, held
   honestly, is what the next spike will be believed by.*
7. **Day 19 — the deep one (0.68).** The second-greatest
   spike (17.5px in the rail), the correction in the log band,
   the keeper's aside. *Depth as a different kind of size:
   smaller on the rail, larger in the apparatus.*
8. **Days 24–30 — the close (0.80–0.90).** Two calm entries;
   the last, timestamped 23:59:41 on Day 30, nineteen seconds
   before the watch ended — the diary's own joke, told in
   apparatus. *The record ends the way it ran: exactly.*
9. **The record band (0.95).** The table (§6.14) in ink, rows
   acknowledging as the needle passes, totals counted plain.
   *Belief, having been earned entry by entry, is tabled.*
10. **The report & the dark room (1.00).** The felt form
    (§8.3) at the foot of the diary, then the footer (§6.16):
    the whole watch redrawn in miniature under lamplight.
    *The reader leaves through the drum room, past the whole
    month at a glance.*

**Reverse pass.** Scrolling up: nothing unwrites (clause 2).
The needle stays at the reader's line over a finished record;
readouts stand settled; station time holds its maximum. The
reader going back up reads a *kept* diary — every spike
standing, every figure deep — which is correct: they have
witnessed it. The only motion licensed on the reverse pass is
the masthead re-expanding at the top and the needle's tremble
gain falling as calm sections re-pass.

**Jump scroll.** An anchor jump or a scrollbar drag to the
record band: every latch between here and there fires in
order — spikes print complete (no draw queue), readouts stand
settled, the clock stands at the target entry's time, the
hero's ceremony is not replayed. The diary never makes a
jumping visitor watch the month they skipped; the record
simply stands kept, and the log band at the landing joint
carries its ordinary lines.

## 14. Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight (home) | ≤ 780KB | Of which photography ≤ 380KB (drum-frame prints, §6.8); the record itself is drawn, not photographed |
| Record script | ≤ 38KB gz | The shared loop, record & deflection functions, latch system and all §6 acts |
| Inline SVG (whole page) | ≤ 64KB total | Rail trace ≤22KB (§6.2), hero band ≤16KB (§6.1), needle ≤3KB (§6.5), footer miniature ≤6KB (§6.16), frames' trace segments ≤6KB, spikes inside the rail's budget |
| Fonts | Spectral (400/500 + italic) + IBM Plex Mono (400/500), subset, ≤ 120KB | `font-display: swap` with §6.1's font race as the guard |
| Frame budget | ≤ 1.6ms of JS per frame in the shared loop | The loop computes values; CSS/compositor applies them. At most 3 transform layers live at once + 1 dash-offset write + the needle's property write |
| Noise floor | ≤ 0.1ms per 240ms recompute | 60 points, one path write (§6.4) — audited separately because it runs off-loop |
| Long tasks | None > 50ms after load | The rail SVG's parse is the risk; it is inline and capped above |
| CLS | 0.00 target, 0.02 ceiling | §3 law 2 (type never moves) and §6.17 (skeleton = real layout) are the mechanisms |

**Cut order** (when a build exceeds budget, cut in this
order — never improvise):
1. The drum revolution (§6.10) — navigation goes plain; the
   record keeps everything else.
2. The smoke drift (§4) — the sheets stand still; the smoke
   remains as a printed layer.
3. The headline letter jitter (§6.1) — the spike and readout
   stay; the type stands on steady ground.
4. The tremor hover (§6.9) — hover deepens ink instead (the
   reduced-motion treatment, promoted).
5. Drum-frame scale settle (§6.8) — prints paste in flat; the
   captions and trace crossings stay.
6. The live floor segment (§6.4) — the floor ships fully
   baked; its caption and statistics stay.

**Never cut:** the printed-DOM guarantee (§1 clause 3), any
watchdog, the ratchet, the record object and its three
printings (§6.13/§6.14/§6.16), the deflection function, the
reduced-motion variants. A build that ships the writing
without the finished record beneath it has not saved weight;
it has removed the theme and kept its riskiest surface.

## 15. Build-order checklist

1. **Static diary first.** The complete site with the record
   fully printed: trace flat full-length, every spike and
   figure settled, table in ink, form working, log lines
   printed. This is the page §10's dead-JS test will grade —
   build it as a deliverable, not as a by-product.
2. **Tokens & type.** §2's closed token list (grep-gated),
   §3's scale and five laws; the forbidden pairings (red text
   small, green on dark) encoded as lint rules, not
   intentions.
3. **The record object.** One data source for §6.2/§6.3/
   §6.6/§6.7/§6.13/§6.14/§6.16 — days, times, magnitudes,
   depths, distances, felt counts; the three-printings audit
   wired into CI before any element that prints a figure is
   built.
4. **Layout.** The sheet, the rail, the time-grid, the
   reading-line constant shared by every trigger (§4).
5. **The shared loop + deflection & record functions +
   latch.** §5's functions implemented once, unit-tested
   against the printed table (d(6.2) = 110.3px; the Day 3
   fraction reads DAY 3 — 14:22:08) before any element
   consumes them; the ratchet proven in miniature.
6. **The trace (§6.2) and the floor (§6.4)** — the spine and
   its breathing; then the needle (§6.5) and the clock
   (§6.6) reading from it.
7. **Spikes and readouts.** §6.3 and §6.7 — the latch's
   ceremonies, in that order, each with its watchdog; the
   needle-agreement test (§10.7) wired here.
8. **The headline event (§6.1)** — after §6.2, because its
   band's settle hands over to the rail's first writing.
9. **Entries (§6.12) and frames (§6.8)** — the content units,
   with their settles and stamps.
10. **Interactions.** Tremor (§6.9), case-tap and the roll
    (§6.10) — the reader's events, recorded.
11. **The record chain.** Table (§6.14), log band (§6.15),
    footer miniature (§6.16) — in §7's order: claim,
    instrument, record.
12. **Form (§6.13)**, footer (§6.16), masthead compression
    (§6.11) — the frame, last, because it is the part that
    may be cut (§14) and must therefore be the part least
    depended upon.
13. **Unwritten sheet (§6.17); the silent page (§6.18)**
    shipped without ceremonies.
14. **Reduced-motion pass** — every element's variant verified
    against §10.11, on a device, not a toggle in devtools
    alone.
15. **The gate (§10)** run by a non-builder; failures return
    to the step that owns them. The theme ships when the gate
    passes, not when the trace looks handsome in the builder's
    browser.
