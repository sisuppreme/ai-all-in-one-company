# 82. Containment Log: Tokamak Shift B — Expanded (v1 + v2)

> A fusion experiment told as the night-shift log of the machine's
> operators — plasma shots numbered, parameters held, one anomaly
> at 03:40 that everyone initialled. Deep tech sold through the
> calm of the people who run it. The page is not a product site
> wearing a lab coat. It is a shift: panels that wake in order,
> shots that fire as you read down the night, numbers that count
> up and then hold dead steady, and one moment at 03:40 that the
> page refuses to explain.

**The theme's one law: the log never exaggerates, and a held
value never moves.** Every figure printed anywhere on the page
traces to one declared shift record (§6.17) and stops at its
exact logged value — 118.2 MK, never "about 120 MK". Once a
parameter has counted up and held, nothing on the page may make
it tremble, pulse or drift; the steadiness is the claim. Alarm
red exists exactly once in the entire build — a single ~80ms
frame inside the anomaly shot (§6.5) — and the anomaly is never
mentioned in hero or marketing copy, only in the log, initialled.
And no panel ever hides its content behind an effect: every
panel ships lit, printed and complete, and firing is an
enhancement the script arms over the finished log, each effect
with a named watchdog. A build that rounds a number, wobbles a
held value, spends the red twice, or explains the anomaly in a
headline has broken the law four ways.

---

## 1. Concept & world

A tokamak is a machine that holds a star still for a fraction of
a second at a time, and the people who run one do it in shifts,
in the dark, in writing. This theme takes that literally: the
site is Shift B's log, kept in the control room between 22:00
and 06:00, and the visitor reads the night the way the operators
lived it — shot by shot, in order, at operator pace. Sections
are not "sections"; they are shots in a laminated log, each with
a number, a timestamp, parameters that count up and hold, and —
where the night earned it — a line of handwriting initialled by
whoever was watching.

The world has three materials and no fourth: **slate** (the
control-room panels, the bezels, the grids), **paper** (the log
itself — entries, tables, the handover), and **light** (amber for
the plasma and everything the machine does, cyan for exactly one
class of thing — diagnostics — and red for exactly one frame in
the whole night). Nothing else is permitted to glow. The room is
dark because control rooms are dark; the log is paper because
the log predates the website and will outlast it.

The emotional register is calm under load. The machine is the
most extreme object most visitors will ever read about —
127.4 MK, a magnetic field of 5.4 T, a star held for 1.120
seconds — and the page's entire rhetoric is that the people
running it write it down in mono, in sentence case, and go back
to work. Premium here is not spectacle; it is the visible
absence of panic. Every design decision is tested against one
question: *would an operator at 03:40 find this believable?*

**Best-fit sites and audiences.** Fusion and advanced-energy
startups raising technical credibility with investors, partners
and recruits; national-lab and university experiment pages;
deep-tech hardware companies whose product is operated, not
clicked (fusion, quantum testbeds, particle instruments, space
propulsion); recruitment pages for operations and engineering
roles, where the shift-log voice is itself the culture signal.
The audience is technical and sceptical: physicists, engineers,
energy investors, journalists who cover them. They will check
the numbers. The numbers must therefore be real-shaped —
plausible magnitudes, consistent units, one record behind all
of them (§6.17).

**When NOT to use it.** Not for consumer energy products
(rooftop solar, home batteries) — the control-room register
would read as costume. Not for anything that needs warmth,
speed or appetite: no food, no fashion, no entertainment. Not
for a product whose story is abundance or scale — this theme's
grammar is scarcity and restraint (six shots a night, one red
frame ever). Not if the client wants the anomaly-style moment
explained, dramatised or turned into a campaign: the theme's
most valuable asset is a thing it refuses to say, and a client
who will not protect that refusal should be sold a different
theme. And never for a site that must convert in the first
screen — the log converts at the handover, after the night has
been read.

---

## 2. Palette

Five anchors from the original entry, unchanged. Seven derived
tokens do the daily work. Contrast values below are measured
from the hex values for this expansion.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--slate` | `#23282C` | Control-room slate — panel faces, section ground | ~55% of pixels | Ground for paper text (13.1:1) and amber display (5.8:1) |
| `--amber` | `#E8873A` | Plasma amber — the machine's light: ring, held values, shot numbers | ~6% | On slate 5.8:1 — display and numerals only, never body text; on paper 3.1:1 — forbidden pairing |
| `--cyan` | `#5BC0BE` | Diagnostic cyan — the single diagnostic accent: traces, trace-linked data | ~2% | On slate 7.4:1 — may set small mono labels; never a second diagnostic hue beside it |
| `--paper` | `#E9E6DC` | Log paper — text on slate; ground of log sheets and the handover | ~30% | On slate 13.1:1 — the page's reading contrast; slate on paper also 13.1:1 |
| `--alarm` | `#C0392B` | Alarm red — appears exactly once (§6.5's single frame) | one frame, ever | On slate 3.4:1 — never text, never an icon, never a border; a frame of light only |
| `--slate-deep` | `#16191C` | Page ground behind panels | ~7% | Panels sit on it; paper on deep 14.6:1 |
| `--slate-raise` | `#2C3237` | Bezel faces, raised keys, header bar | within slate share | Distinguishes the frame from the panel it frames |
| `--paper-dim` | `#B7B2A4` | Secondary text on slate — captions, units, retired values | within paper share | On slate 7.9:1 — the dimmest text token permitted on slate |
| `--grid-line` | `rgba(233,230,220,0.07)` | Oscilloscope grid lines on panels | hairlines only | Never carries meaning alone; always behind a trace or a value |
| `--amber-dim` | `#9A5A26` | Standby ring, un-fired shot markers | <1% | The ring asleep; brightens only by firing |
| `--cyan-dim` | `#336463` | Idle trace baseline | within cyan share | Idle traces idle in dim; one brightens on hover (§6.6) |
| `--sheen` | `linear-gradient(105deg, transparent 42%, rgba(233,230,220,0.09) 50%, transparent 58%)` | Laminated sheen over bezels | transient | The only gradient allowed on a panel face |

**Rules that outrank the table.**

- **The red census.** `--alarm` may be referenced by exactly one
  rule in the shipped CSS — the anomaly frame in §6.5. The
  quality gate (§10) greps for it. Error states, sale badges,
  required-field markers and "live" dots are all forbidden from
  borrowing it; errors speak in paper and amber (§12).
- **Cyan is a job, not a colour scheme.** Cyan appears only
  where a diagnostic trace or its data appears. A cyan button,
  a cyan link hover or a cyan heading is a category error: the
  visitor must learn within one screen that cyan *means*
  diagnostics, the way amber *means* the machine.
- **Amber never sets a sentence.** Amber is for numerals, the
  ring, shot numbers and the word HELD. Body copy in amber on
  slate fails contrast discipline and reads as decoration.
- **No light scheme.** There is no inverted "day mode". The log
  sheets (§6.11, §6.16) are the light surfaces, and they are
  paper, not a theme inversion — a deliberate material inside
  the dark room, exactly as a laminated log is.
- **Dark-mode behaviour.** The theme *is* the dark mode. On
  operating systems forcing light contrast, nothing changes:
  the control room does not open its blinds for a media query.

---

## 3. Typography

Two families, as in the original entry — **Space Grotesk** for
display, **IBM Plex Mono** for shot parameters, log timestamps
and everything the machine or the log says. There is no third
voice; handwriting does not exist in this theme, because the
log is typed — the operators' initials are set in mono, and
their restraint is typographic before it is anything else.

**Type scale** (1.25 ratio on a 16px base, tightened at display
sizes where Space Grotesk's geometry carries the size):

| Role | Font | Size / line-height | Tracking | Used for |
|---|---|---|---|---|
| Display | Space Grotesk 500 | 56px / 1.02 (clamp 40–64px) | −0.02em | Hero statement only — one per page |
| Shot title | Space Grotesk 500 | 32px / 1.1 | −0.01em | Section (shot) headings |
| Panel title | Space Grotesk 500 | 19px / 1.25 | 0 | Panel and card headings |
| Body | IBM Plex Mono 400 | 15px / 1.65 | 0 | Log entries, explanatory copy — the log is the body |
| Parameter | IBM Plex Mono 500 | 22px / 1.2, tabular | +0.01em | Held values: `118.2 MK` |
| Data small | IBM Plex Mono 400 | 12.5px / 1.5, tabular | +0.02em | Tables, timestamps, units, captions |
| Label | IBM Plex Mono 500 | 11px / 1.4 | +0.14em, uppercase | Panel labels, bezel stamps, status words |

**Type laws.**

1. **Numerals are mono, always.** No figure ever appears in
   Space Grotesk — not in a headline, not in a button. If a
   number matters enough to print, it is a parameter, and
   parameters are mono with tabular figures so columns of shots
   align digit-for-digit down the log.
2. **Timestamps are a format, not a style.** `03:40` — 24-hour,
   zero-padded, mono, always followed by the shot number it
   belongs to (`03:40 · SHOT #4,815`). A time without a shot
   number is an anecdote; the log does not keep anecdotes.
3. **Space Grotesk never sets a value.** Display type may say
   *what the night was*; it may not say *what the machine did*.
   The moment a temperature appears in display type it becomes
   marketing, and the law is broken.
4. **Held values are set once, at full size, and never
   restyled.** A parameter's typography does not change between
   its counting state and its held state — same size, same
   weight, same colour. Only the digits change, then stop. Any
   visual "celebration" on arrival (a flash, a scale pop) is a
   wobble by another name.
5. **Uppercase is rationed to labels ≤ 3 words.** `CONFINEMENT`,
   `SHOT #4,812`, `HELD`. Sentences in uppercase are shouting,
   and nobody on Shift B shouts — including at 03:40.

---

## 4. Layout language

The page is a wall of panels over a darker ground, read top to
bottom as a shift is lived: header (the console), hero (the
machine), shots in chronological order, the log book, the
handover. Density is control-room density — information is
close together because the room is small and everything must be
reachable — but each panel holds one job.

- **Grid.** 12 columns at ≥1200px, 24px gutters; panels span in
  whole bezels, never half-bezels. The hero is a 7/5 split: the
  torus panel takes 7 columns, the hero parameter stack 5. Shot
  sections alternate 8/4: log entry wide, parameter panel
  narrow — the night reads as writing first, numbers second.
- **The bezel is the unit.** Every panel sits in a screw-cornered
  bezel (§6.9): 1px `--slate-raise` border, 10px radius, four
  screw heads (8px SVG circles with a slot line) inset 10px from
  each corner. Content never touches a bezel edge; inner padding
  is 28px, and the oscilloscope grid (`--grid-line`, 24px cells)
  prints behind parameter panels only — grids belong to
  instruments, not to prose.
- **Spacing rhythm.** A 4px base unit; intra-panel gaps 16px,
  panel-to-panel 24px, shot-to-shot 96px. The 96px gap is the
  held beat between shots (§5) — the scroll distance the page
  asks for between one shot's hold and the next shot's fire.
  Whitespace here is not air; it is *time between firings*.
- **The header is a console bar, not a nav bar.** 56px,
  `--slate-raise`, carrying the shift mark, the shot counter
  (§6.2) pinned right-of-centre, and the confinement clock
  (§6.7) at the far right. It never grows, never gains a
  background blur, never hides on scroll — a console does not
  leave the room.
- **Paper appears twice only.** The log book (§6.11) and the
  handover footer (§6.16) are paper sheets laid on the slate —
  the two moments the visitor touches the physical log. All
  other surfaces are panels. Paper used anywhere else dilutes
  the material story.
- **Reading line.** Motion triggers key to a line at 62% of the
  viewport height — low enough that a shot's panel is mostly
  visible before it fires, high enough that the fire is seen,
  not scrolled past. The choreography map (§13) is written
  against this line.

---

## 5. Full motion system

One shared `requestAnimationFrame` loop drives every scrubbed
and timed value on the page — ring phase, parameter counts,
digit rolls, trace drawing, sheen position — with a lerp factor
of **0.10** toward each target. 0.10 is slower than a marketing
site's 0.12–0.16 on purpose: the page advances the way the room
advances, in measured steps with weight behind them. The loop
keeps a phase clock (elapsed visible time) so ambient behaviour
resumes from phase after a hidden tab, and it idles at zero
cost when nothing is registered.

**Named easings** (the only five the theme owns):

| Token | Curve | Character |
|---|---|---|
| `--ease-fire` | `cubic-bezier(0.6, 0.05, 0.2, 1)` | The ring's race: a hard strike, a fast circuit, a clean stop |
| `--ease-hold` | `cubic-bezier(0.25, 0.6, 0.3, 1)` | Parameter counts decelerating into the hold — arrival without bounce |
| `--ease-wake` | `cubic-bezier(0.4, 0, 0.2, 1)` | Panel lights waking in sequence |
| `--ease-roll` | `steps()`-equivalent via the loop | Mechanical digit roll — digits are machinery, they do not glide |
| `--ease-sheen` | `linear` | The laminated sheen's single pass — glass does not ease |

**Every motion term, in this theme's language:**

- **Scroll-triggered reveals** are *shots firing*. A shot
  section fires when its panel crosses the 62% reading line:
  the ring races (§6.1), parameters count and hold (§6.3), the
  counter increments (§6.2). A reveal that merely fades content
  in is not a shot and is not permitted — on this page, arrival
  means the machine ran.
- **Scroll-scrubbed values** are *dials under the reader's
  hand*: within a shot's approach zone (the 96px beat before the
  reading line), the ring's standby arc and the parameter
  panels' grid brightness are scrubbed to scroll position
  through the shared loop, so the reader feels the shot being
  prepared before it fires. Scrubbing never moves a held value —
  scrub applies only to a shot that has not yet fired.
- **Pinned scenes.** Two pins only: the console header (the
  whole page) and the hero torus (§6.1), which pins for 140vh
  while its parameters are revealed through the ring's mask.
  Nothing else pins; a log does not freeze its middle pages.
- **Masked line reveals** happen through the ring's circular
  mask (§6.1) and nowhere else. Text does not slide out from
  behind rectangles on this site; the one mask is the machine's
  own shape.
- **Blur-to-sharp** is refused. Instruments do not defocus;
  a blurred parameter is an unreadable parameter. Focus-pull
  belongs to cameras, not consoles.
- **Animated counters** are the theme's core grammar (§6.2,
  §6.3): digits count with `--ease-hold` and stop dead. A
  counter that eases past its value and settles back has
  overshot, and overshoot is exaggeration — the law (§1) bans
  it in motion as in copy.
- **Progress indicators.** Progress is the shot number (§6.2)
  and, inside a shot, the confinement clock (§6.7). There is no
  scroll bar, no percentage, no reading-progress rail: the
  visitor is not "62% through the content"; they are at shot
  #4,815 of the night.
- **Marquees** are refused. Nothing in a control room scrolls
  sideways forever. The one horizontal motion permitted is the
  sheen's single pass (§6.9).
- **Kinetic typography** is refused except for the digit roll —
  letters do not swell, stagger or dance. Log entries appear
  whole, the way typed lines do.
- **Ambient loops.** Exactly two are licensed: the idle
  diagnostic traces (§6.6) and the torus ring's standby glow
  (§6.1, a 6s opacity breath between 55% and 70%, the machine
  asleep with one eye open). A third ambient loop of any kind
  fails the quality gate — a control room at rest is mostly
  still, and the stillness is what makes a firing legible.
- **Micro-interactions.** Hover brightens a trace (§6.6) or
  lifts a bezel's sheen readiness; clicks fire (§6.8), stamp
  (§6.14) or turn a log page (§6.11). Every interaction answers
  within one frame and finishes within 450ms; the room responds
  like equipment, not like a toy.
- **Hover physics.** No magnetic pull, no tilt. Panels are
  bolted to the wall; they do not lean toward visitors.
  The pointer's only physics is light: traces brighten under it
  because the operator is looking there.
- **Page transitions** are *between shots* (§6.15): panels dim
  to standby in bezel order, the ring fires once on the new
  page's hero, panels wake. 900ms total, skippable by any input.
- **Image treatments.** Photographs sit behind bezel glass with
  the sheen (§6.9); they are never filtered, duotoned or
  parallaxed. The room's photography is documentary — operators,
  the machine hall, the console at night — and is treated with
  the respect of evidence.

**Trigger discipline.** Every scroll trigger is one-shot and
latched: a fired shot stays fired. Scrolling back up never
un-fires, un-counts or un-holds anything (§13's reverse pass) —
the log is a record, and records do not run backwards. The only
repeatable fires are deliberate: click-to-fire (§6.8) and the
hero ring's replay on explicit visitor action.

**Watchdog architecture.** Every armed effect registers a
deadline with the loop (named per element in §6, between
1200ms and 3000ms). If the deadline passes with the effect
incomplete — blocked script, starved frames, a stalled observer
— the watchdog completes the effect's end state instantly and
prints it: values at their held figures, ring drawn full,
panels lit. The DOM ships in the end state (complete, printed,
readable with no JavaScript at all); scripts *rewind* to the
pre-state only at arm time, in the same frame they register
their watchdog. There is therefore no ordering of failures in
which content is missing.

**Reduced motion, globally.** Under `prefers-reduced-motion`:
no ring race (the ring ships drawn, §6.1), no counts (values
print held), no digit roll, no sheen, traces printed as static
waveforms, the anomaly's red frame absent entirely — the log
entry remains, initialled, which is where the story always
lived. The shift is fully logged and legible; §6 gives each
element's variant in full.

---

## 6. Signature elements

### 6.1 The firing torus ring

- **What & why.** An SVG ring of light — a bright amber head
  with a comet tail of fading stroke — races once around the
  torus outline each time a shot fires: on load in the hero,
  per section as shots fire, and on demand via click-to-fire
  (§6.8). As the head completes its circuit, the shot's headline
  parameters are revealed through the ring's circular mask, as
  if the light itself printed them. It belongs because the
  machine's operation *is* the page's transition grammar: every
  section begins with the experiment actually running, so the
  visitor never merely arrives at content — the night advances.
- **Structure.** One inline SVG per firing site (hero + one per
  shot panel), viewBox 400×400: a faint full torus outline
  (two concentric circles + inner ellipse suggesting the torus's
  far wall, stroke `--amber-dim`), and the firing path — a
  circle path whose `stroke-dasharray` is driven by the shared
  loop. The head is a short, fully-lit dash segment (14% of
  circumference) with an SVG Gaussian glow filter used once,
  statically defined; the tail is the preceding 46% at falling
  opacity stops. The parameter mask is a `<clipPath>` circle
  whose radius is keyed to the head's angular position — as the
  head passes each parameter's station (120°, 210°, 330°), that
  parameter's group is unclipped. No canvas; the ring is
  document, and screen readers meet a labelled figure, not a
  movie.
- **Motion spec.** Trigger: hero — on load after the wake
  sequence (§6.15), then on pin (§5); shots — the reading-line
  crossing; clicks — §6.8. Circuit duration 900ms under
  `--ease-fire` for a nominal shot; per-shot variations are
  §6.4's grammar (wobble-damp 1400ms, long run 2600ms, anomaly
  ~1250ms with a stutter). Standby state: the ring rests at
  `--amber-dim` with the 6s standby breath (55%→70% opacity)
  — the second of the theme's two licensed ambient loops. After
  firing, the ring settles to a full, steady `--amber` outline
  at 85% and stays: a fired shot's ring is a printed result,
  not a screensaver.
- **States.** Standby (dim, breathing) / firing (head racing,
  mask opening) / fired (full outline at 85%, parameters held) /
  re-firing (§6.8, from a log entry's mini-ring) / parked (hero
  scrolled past — breath continues, it is ambient, not content).
- **Content merge.** The ring carries the shot's parameters
  inside its mask and the shot's number at its centre; remove
  the shot and the ring has nothing to fire for. It is never a
  logo, never a loading spinner, never decoration on a section
  that is not a shot — a page region without a shot number does
  not get a ring.
- **Failure fallback.** Watchdog at 2400ms from arm: if the
  circuit has not completed, the ring snaps to the fired state —
  full outline drawn, mask fully open, parameters printed at
  held values. No-JS: the SVG ships in the fired state; the
  script rewinds the dashoffset only when it arms the fire, in
  the same frame it registers the watchdog.
- **Reduced-motion variant.** The ring ships drawn at 85%,
  parameters printed; no race, no breath. The shot still
  "fires" in the only sense that matters to the log: its number
  increments in the header (§6.2) as the section passes.
- **Performance budget & mobile variant.** One SVG path update
  per frame from the loop; ≤0.3ms/frame. The glow filter is
  pre-rendered by the browser as a static filter region — no
  per-frame filter cost. Mobile (<768px): the torus panel goes
  full-width, ring diameter 72vw, the tail shortens to 30% and
  the glow filter is dropped (head is a plain bright segment) —
  the circuit and the mask reveal are unchanged.
- **Choreography timeline (v2).** t=0 panel crosses the reading
  line (or load, for the hero) → t=0–120ms grid brightness scrubs
  to full → t=120ms head strikes at the top of the torus →
  t=120–1020ms circuit under `--ease-fire`, mask opening at the
  three stations as the head passes → t≈1050ms final station
  unclips, parameters begin their count (§6.3) → t=1400ms ring
  settles to 85% steady → watchdog deadline t=2400ms passes
  unused.
- **State matrix (v2).** *Rest:* standby breath (or drawn, after
  firing). *Hover:* nothing — the ring is the machine's, not the
  pointer's; hovering the panel brightens the grid by 10% only.
  *Focus:* the ring's figure carries a text alternative; it is
  not itself focusable. *Active:* n/a. *Scrolled-past:* fired
  state persists; breath continues in the hero only.
  *Disabled:* n/a. *Touch:* identical; no hover grid brightening.
- **Breakpoints (v2).** ≥1200px: ring 400px in a 7-column panel,
  parameters inside the mask. 768–1199px: ring 320px, panel
  stacks above the parameter stack. <768px: ring 72vw centred,
  parameters print *below* the ring (the mask reveal still
  sequences them, the layout no longer nests them).
- **Edge cases & failure modes (v2).** *Slow network:* the ring
  is inline SVG — it fires before any image arrives; panels do
  not wait for photography. *No SVG filter support:* the head
  renders unglowed, circuit unaffected. *User scrolls through a
  shot during its circuit:* the fire completes off-screen; the
  shot is fired when they return — latched, never re-run.
  *Very fast scroll through all shots:* each fire is queued by
  the loop at most one circuit at a time; later shots snap to
  fired state via their watchdogs rather than racing six rings
  at once.
- **Accessibility spec (v2).** The SVG is `role="img"` with
  `aria-label` naming the shot and its outcome ("Torus, shot
  4,812: confinement held"). Parameter values are real text in
  the DOM at all times (the mask is visual only; assistive
  technology is never masked). The firing is not announced —
  ambient machine behaviour must not spam a live region; the
  *result* is the printed parameters, already present.
- **Tokens consumed (v2).** `--amber`, `--amber-dim`, `--slate`,
  `--grid-line`, `--ease-fire`, `--loop-lerp` (0.10),
  `--dur-circuit` (900ms), `--dur-settle` (1400ms).

### 6.2 The shot counter header

- **What & why.** `SHOT #4,812` sits pinned in the console
  header for the whole visit and increments as each shot section
  fires, each increment a mechanical digit roll. It belongs
  because progress on this page is the experiment's own unit:
  the visitor is not scrolling a document, they are attending a
  shift, and the shift is counted in shots. The counter is also
  the page's memory — it never decrements, so it tells the truth
  about how much of the night has been witnessed.
- **Structure.** A mono label in the header (§4): the fixed word
  `SHOT #` in `--paper-dim`, then six digit cells, each a 1ch×1em
  window over a vertical strip of digits 0–9, translated by the
  shared loop. Digits that do not change do not move — a roll
  from 4,812 to 4,813 moves exactly one strip. The counter's
  value is rendered from `shiftState.shot` (§6.17); the DOM
  ships at the record's opening value, 4,812.
- **Motion spec.** Trigger: a shot section's fire (§6.1).
  Increment lands 150ms after the ring's circuit completes —
  the shot is counted once it has run, not when it starts. Roll:
  240ms per digit under `--ease-roll`, staggered right-to-left
  at 40ms intervals when several digits change (4,809 → 4,810
  rolls two strips). No bounce, no overshoot — machinery.
- **States.** At rest (showing the highest shot fired) / rolling
  (≤240ms) / complete (header also carries the word `LOGGED` in
  label style once the final shot, #4,817, has fired).
- **Content merge.** The counter is the choreography map made
  visible (§13): every increment corresponds to a real section
  the visitor has passed, and the header's other resident, the
  confinement clock (§6.7), shares its grammar. It cannot be
  pasted onto a page without shots; it would have nothing to
  count.
- **Failure fallback.** Watchdog at 1200ms: a missed observer
  leaves the counter at the last fired shot — wrong by omission,
  never by invention; on the next successful fire it jumps
  directly to the true value with no roll. No-JS: the header
  prints `SHOT #4,812` statically and the log below it is
  complete; the count is a convenience, not a gate.
- **Reduced-motion variant.** Increments are instant text
  changes; the value is identical. Nothing else differs.
- **Performance budget & mobile variant.** ≤6 transform updates
  for ≤240ms per increment; negligible. Mobile: the counter
  stays — it is the header's reason to exist — but the shift
  mark shortens to `SHIFT B` and the clock (§6.7) moves to a
  second header row rather than crowding the digits.
- **Choreography timeline (v2).** Shot fires (t=0 circuit
  complete) → t=150ms roll begins, units digit first → t=390ms
  roll ends → value rests. If the visitor is looking at the
  header, they see the night advance by one; if not, the number
  is simply correct when they next look — both are the design.
- **State matrix (v2).** *Rest:* current value. *Hover:* none.
  *Focus:* the counter is a single focusable element only in
  the header's skip-nav context; its focus ring is a 2px
  `--amber` outline. *Active:* n/a. *Scrolled-past:* n/a — it is
  the header; it is never past. *Disabled:* n/a. *Touch:* same,
  no roll change.
- **Breakpoints (v2).** ≥1200px: counter right-of-centre, full
  `SHOT #4,812` with label. 768–1199px: same, clock abbreviated
  to seconds. <768px: counter centred, clock on row two (§6.7).
- **Edge cases & failure modes (v2).** *Jump scroll to the
  footer:* all intermediate shots fire in sequence under their
  watchdogs; the counter rolls once, directly to 4,817, rather
  than performing six rolls. *Scroll back up:* the counter does
  not decrement — §5's latch rule; a visitor re-reading shot
  #4,813 sees the header honestly showing #4,817, the shift's
  furthest reach, exactly as a log's page count behaves.
  *Record mismatch:* if `shiftState` and the DOM disagree, the
  record wins and the header corrects without animation.
- **Accessibility spec (v2).** The counter is `aria-live="off"`:
  increments are not announced (they are ambient bookkeeping);
  a visually-hidden text equivalent, "Shot 4,812 of 4,817 this
  shift", updates with it for AT users who query the header.
  Digit strips are `aria-hidden`; the accessible value is a
  single text node.
- **Tokens consumed (v2).** `--paper`, `--paper-dim`, `--amber`,
  `--slate-raise`, `--ease-roll`, `--dur-roll` (240ms).

### 6.3 Parameters that count and hold

- **What & why.** Each shot's parameters — core temperature,
  toroidal field, confinement time — count up in mono from zero
  (temperature, field) or from the previous shot's value
  (confinement, where the log compares) and then **hold dead
  steady**. No idle wobble, no breathing digits, no pulse on the
  decimal. The steadiness is the flex: motion design as
  characterisation of the operators' calm, and the theme's law
  (§1) in its purest form — a held value never moves.
- **Structure.** A parameter stack inside the shot's panel:
  three rows, each a label (`CORE TEMP`, `FIELD`, `CONFINEMENT`)
  in label style, a value in parameter style (§3) with tabular
  mono figures, and a unit. Values are text nodes written by the
  shared loop from the record (§6.17); the DOM ships with the
  held values printed, and the script rewinds them to the count's
  start only at arm time. Beneath the stack, once counting
  completes, the status line prints: `CONFINEMENT: HELD.` —
  set in mono, in `--paper`, with the word HELD in `--amber`.
- **Motion spec.** Trigger: the shot's ring circuit completing
  (§6.1). Count duration: 1100ms under `--ease-hold`, all three
  parameters starting together (instruments settle together;
  staggered counts read as a slot machine). Values are rounded
  to the record's precision at every frame — temperature to
  0.1 MK, field to 0.1 T, confinement to 0.001 s — so the count
  passes only through values the machine could have printed.
  At completion the status line prints in a single frame — no
  fade, typed lines do not fade — and from that frame the values
  are never written again.
- **States.** Printed (pre-arm, = held values) / counting
  (≤1100ms) / held (terminal; the stack's grid dims by 15% so
  the eye leaves the instruments and returns to the log) /
  re-fired (§6.8 re-counts a single entry's stack from 92% of
  its held values — a re-fire is a shorter, shallower count,
  because the machine was already warm).
- **Content merge.** These are the shot's facts, not a chart
  pasted beside them: the log entry beside the stack refers to
  the same figures in prose ("held 0.905 s — the long one"), and
  the parameter table (§6.12) prints the same row. One record,
  three printings, zero decoration.
- **Failure fallback.** Watchdog at 2000ms from arm: values snap
  to held, status line prints. No-JS: values and the status line
  ship printed; nothing about the stack requires the count to
  have been seen.
- **Reduced-motion variant.** No count: values print held, the
  status line prints with the section. The information and its
  emphasis are identical; only the 1100ms of theatre is removed.
- **Performance budget & mobile variant.** Three text writes per
  frame for ≤1100ms per shot; ≤0.2ms/frame. Mobile: the stack
  goes full-width under the ring (§6.1), value size 19px, and
  confinement counts from zero (the comparison baseline is a
  desktop refinement; the held value is unchanged).
- **Choreography timeline (v2).** t=0 ring circuit completes →
  t=0–1100ms the three values count under `--ease-hold`,
  passing only machine-printable values → t=1100ms all three
  land in the same frame → t=1150ms `CONFINEMENT: HELD.` prints
  → t=1400ms grid dims 15% → the stack is never written again.
  Watchdog deadline t=2000ms passes unused.
- **State matrix (v2).** *Rest:* held values. *Hover:* hovering
  a row prints its full-precision record value in the row's
  caption slot (e.g. confinement `0.905 s · τE, energy`) — data
  on request, still not motion. *Focus:* rows are not focusable;
  the stack is a figure with a text alternative. *Active:* n/a.
  *Scrolled-past:* held, grid dimmed. *Disabled:* n/a. *Touch:*
  tap a row = the hover caption, toggled.
- **Breakpoints (v2).** ≥1200px: stack in the 4-column panel
  beside the log entry. 768–1199px: stack below the entry, three
  rows in a 3-column strip. <768px: stacked rows full-width,
  value 19px, caption slot under each row.
- **Edge cases & failure modes (v2).** *Record value longer
  than the design expects* (a future 1,000+ MK machine): the
  value column is sized for 7 characters + unit and grows
  without wrapping — tabular mono keeps the column honest.
  *A shot with a missing parameter* (diagnostic down): the row
  prints `— · NOT LOGGED` in `--paper-dim`; the count skips it;
  the log explains. Absence is data; the stack never invents a
  zero. *User scrolls away mid-count:* the count completes
  off-screen under its watchdog; returning shows held values.
- **Accessibility spec (v2).** The stack is a `<figure>` with a
  `<figcaption>` giving the shot's outcome in prose. Counting
  values are `aria-hidden` during the count; a single
  visually-hidden text node carries the held values from the
  start, so AT users never wait for, or hear, a slot machine.
  Contrast: values in `--paper` on `--slate` 13.1:1; HELD in
  `--amber` 5.8:1 at 22px — display-size, compliant.
- **Tokens consumed (v2).** `--paper`, `--paper-dim`, `--amber`,
  `--slate`, `--grid-line`, `--ease-hold`, `--dur-count`
  (1100ms), `--loop-lerp` (0.10).

### 6.4 Per-shot ring behaviours — the shot grammar

- **What & why.** Repetition with variation is the log's
  narrative: the machine has a night, not a loop. Each shot's
  ring therefore behaves according to a small declared grammar —
  **nominal** (the clean 900ms circuit), **wobble-damp** (the
  ring's radius oscillates and settles), **long run** (a 2600ms
  circuit for a shot that held longer), and the anomaly's
  **stutter** (§6.5 owns the moment; this element owns the
  grammar slot it occupies). The grammar is declared per shot in
  the record (§6.17), so behaviour is data, not a designer's
  whim per page.
- **Structure.** A behaviour field on each shot object in the
  record: `behaviour: nominal | wobble | long | anomaly`, plus
  its parameters (`wobbleAmp`, `wobbleDecay`, `circuitMs`). The
  ring renderer (§6.1) reads the field; the wobble is applied as
  a radial modulation of the firing path, recomputed per frame
  by the shared loop — path radius = base ± amp·sin(phase·3)·
  decay^(t). No separate components per behaviour: one ring,
  four weathers.
- **Motion spec.** *Nominal:* 900ms, §6.1 as specified.
  *Wobble-damp:* 1400ms circuit; radial oscillation starts at
  ±6px, three visible cycles, decaying to ±0px by 1200ms — the
  ring steadies exactly as the parameters land, and shot
  #4,813's confinement (0.388 s, the shift's lowest) prints as
  the wobble dies: behaviour and data tell the same story.
  *Long run:* 2600ms at a visibly slower head speed; the
  parameter count stretches to 1900ms to match, and #4,814's
  0.905 s confinement is the reason printed in its log entry.
  *Anomaly:* §6.5.
- **States.** Per shot: declared (in the record) / performed
  (during its fire) / printed (afterwards, the behaviour is a
  word in the log entry — `WOBBLE, DAMPED` — so the variation
  survives as text when motion is gone).
- **Content merge.** The grammar is how the log *characterises*
  shots without adjectives: a reader who watches three sections
  has learned to read the machine's moods from the ring alone,
  and the log entry's behaviour word confirms what they saw.
  It merges because the behaviour is never arbitrary — each
  variation is bound to that shot's actual parameters.
- **Failure fallback.** Any behaviour failure degrades to
  nominal: the watchdog (§6.1) completes a plain circuit and
  the parameters print. A wobble that cannot render is a shot
  that fired cleanly, which is a lie the log tolerates better
  than a missing shot — and the behaviour word in the entry
  still tells the truth in text.
- **Reduced-motion variant.** No behaviours are performed; each
  shot's behaviour word prints in its entry, and the long shot's
  entry carries its duration in figures. The narrative —
  variation across the night — survives entirely as record.
- **Performance budget & mobile variant.** Wobble adds one path
  recompute per frame during its 1400ms; ≤0.4ms/frame, the
  theme's most expensive frame, still inside §14's budget.
  Mobile: wobble amplitude ±4px (smaller ring), long run
  shortens to 2000ms — a phone's reading line moves faster, and
  the grammar compresses rather than disappears.
- **Choreography timeline (v2).** *Wobble-damp:* t=0 head
  strikes → radius oscillation ±6px at 3 cycles over the circuit
  → t=1200ms oscillation reaches ±0 → t=1400ms circuit completes
  → parameters land as the ring steadies. *Long run:* t=0 strike
  → head at 0.35× nominal speed → t=2600ms completes → count
  (1900ms) overlaps the circuit's second half, landing 150ms
  after the head.
- **State matrix (v2).** *Rest:* behaviour declared, ring in
  standby. *Hover / focus / active:* none — the grammar is
  performed, not operated. *Scrolled-past:* behaviour word
  printed in the entry. *Disabled:* n/a. *Touch:* identical
  performance; mobile amplitudes per above.
- **Breakpoints (v2).** ≥1200px: full amplitudes. 768–1199px:
  wobble ±5px, long run 2300ms. <768px: wobble ±4px, long run
  2000ms; nominal and anomaly timings unchanged at every size —
  the night's facts do not shrink with the screen.
- **Edge cases & failure modes (v2).** *A record with two
  anomaly behaviours:* invalid — the record validator (§6.17)
  refuses more than one `anomaly` per shift, because the red
  census (§2) is a law, not a style. *Unknown behaviour string:*
  renders nominal and logs a console warning naming the shot;
  the page never breaks for a vocabulary it has not met.
  *Wobble on a low-power device:* if the loop's frame time
  exceeds 24ms twice during a wobble, the behaviour completes
  as nominal — steadiness is also the fallback's character.
- **Accessibility spec (v2).** Behaviours are never the sole
  carrier of their meaning: the behaviour word and the
  parameters print in text beside every performance. The
  wobble's motion is radial and small (±6px), below vestibular
  concern thresholds, and it is removed entirely under reduced
  motion.
- **Tokens consumed (v2).** `--amber`, `--amber-dim`,
  `--ease-fire`, `--dur-circuit` (900ms), `--dur-wobble`
  (1400ms), `--dur-long` (2600ms), `--loop-lerp` (0.10).

---

### 6.5 The 03:40 anomaly

- **What & why.** At the anomaly section — shot #4,815, logged
  03:40 — the ring stutters once: it halts mid-circuit, alarm
  red replaces amber for a single ~80ms frame, and the circuit
  resumes and completes as if nothing happened. Below, the log
  entry is initialled by three operators — `R.O. · M.L. · T.H.` —
  with the note, in full: *"seen before. watching."* Nothing
  else on the page changes. The hero copy never mentions it; no
  section heading names it; the shot's parameters are nominal.
  It is the theme's most memorable moment precisely because it
  is its quietest: story told by restraint, and the one place
  the law (§1) spends its single red frame.
- **Structure.** A behaviour flag on shot #4,815 in the record
  (§6.17) plus one dedicated CSS rule — the only rule in the
  build referencing `--alarm` — applied to the ring's head
  segment for the stutter frame. The log entry is ordinary DOM:
  timestamp, shot number, nominal parameters, the initials line,
  the note. There is deliberately no anomaly component, no
  special markup, nothing for a crawler or a skimmer to find
  exciting; the entry differs from its neighbours by eleven
  words and three sets of initials.
- **Motion spec.** Trigger: the section's fire. Circuit runs
  nominally to ~60% (t≈540ms) → head halts for 120ms (a held
  frame, not a fade) → one 80ms frame in `--alarm` at the halt
  position → amber resumes → circuit completes at ~1250ms total.
  Parameters count and hold exactly as §6.3 specifies — 124.3 MK,
  5.4 T, 0.417 s, all unremarkable, and that unremarkableness is
  the point the design is making. The stutter happens once per
  page load; re-entering the section never replays it. The log
  does not flinch twice.
- **States.** Unfired (indistinguishable from any shot) / the
  stutter (200ms total) / fired (indistinguishable from any
  shot, except the entry's initials). There is no "alarm state"
  the page can be left in.
- **Content merge.** The anomaly *is* content — the night's one
  story — and its treatment is the theme's thesis: an unexplained
  thing, recorded accurately, initialled by witnesses, and not
  merchandised. It merges because everything around it refuses
  to react; remove the surrounding calm and the moment is a
  jump scare, which is a different and cheaper theme.
- **Failure fallback.** If the fire is watch-dogged (§6.1), the
  circuit completes without the stutter — the red frame is an
  enhancement over the entry, never a load-bearing one. The
  entry, initials and note ship printed in the DOM; with no
  JavaScript the anomaly exists in full, as text, which is its
  canonical form.
- **Reduced-motion variant.** The red frame is absent entirely —
  no flash of any kind is permitted under reduced motion, and a
  single-frame colour event is a flash. The entry remains,
  initialled. Nothing is lost that the log itself considers
  information.
- **Performance budget & mobile variant.** One class toggle for
  one frame; zero measurable cost. Mobile: identical — the
  stutter's timing does not compress, because 80ms is already
  the minimum legible event, and below legibility the honest
  choice is the reduced-motion treatment.
- **Choreography timeline (v2).** t=0 section crosses the
  reading line → circuit runs → t≈540ms head reaches 60% →
  t=540–660ms halt → t=660ms the red frame (80ms) → t=740ms
  amber resumes → t≈1250ms circuit completes → parameters count
  (1100ms) and hold → `CONFINEMENT: HELD.` prints → the entry's
  initials line is simply there, as it always was.
- **State matrix (v2).** *Rest:* a shot among shots. *Hover:*
  hovering the entry does nothing — no highlight, no tooltip,
  no "anomaly" cursor. The page does not point. *Focus:* the
  entry is text; focus behaves as text. *Active:* §6.8's
  click-to-fire is disabled on this entry — the one entry the
  visitor may not re-fire. Some shots are not the visitor's to
  repeat. *Scrolled-past:* unchanged. *Disabled:* n/a.
  *Touch:* identical; the no-refire rule applies to tap.
- **Breakpoints (v2).** Identical at all sizes: timings, the
  single frame, the entry's layout (it follows §6.3's stack
  rules). Restraint does not have a mobile variant.
- **Edge cases & failure modes (v2).** *Photosensitivity:* one
  80ms frame, a colour substitution on a 14% arc segment — not
  a luminance flash, no alternation, once per load; it sits far
  inside WCAG flash thresholds, and reduced-motion removes it
  outright. *A second anomaly in a future shift's record:* the
  validator (§6.17) refuses the build — one red frame per page
  is law (§2), so a shift with two anomalies is published as
  two pages or not at all. *Visitor arrives via a deep link to
  the entry:* the section fires on entry as usual; the stutter
  performs for the anchored arrival too — the log keeps no
  privileged readers.
- **Accessibility spec (v2).** The stutter is never announced;
  the entry's text is the accessible event, including the
  initials and the note, in reading order. The ring's
  `aria-label` for this shot reads "shot 4,815: confinement
  held" — identical in form to its neighbours. Assistive
  technology is given the log's version of the night, which is
  the true one.
- **Tokens consumed (v2).** `--alarm` (its single licensed use),
  `--amber`, `--ease-fire`, `--dur-stutter-hold` (120ms),
  `--dur-alarm-frame` (80ms).

### 6.6 Idle diagnostic traces

- **What & why.** Oscilloscope traces idle on the side panels
  beside the torus — low-amplitude, instrument-true waveforms
  drawn on fine grids, the room alive with instruments between
  shots. One trace brightens to full `--cyan` under the pointer:
  the operator is looking at that diagnostic now. It belongs
  because diagnostics are the theme's one cyan job (§2), and
  because a control room's ambience is not decoration — it is
  instrumentation that happens to be beautiful at 03:00.
- **Structure.** Each trace is an inline SVG path on a
  `--grid-line` panel (24px grid), drawn from a declared
  waveform function per diagnostic — a damped sinusoid for
  density, a slow sawtooth for neutral-beam current, a flat
  line with seeded noise for radiated power — sampled at 120
  points and redrawn by the shared loop at 4Hz (instruments
  refresh; they do not stream at 60fps). Three traces on the
  home page (hero side panel + two shot panels), each captioned
  with its diagnostic name and current value in data-small mono,
  the value agreeing with the record (§6.17).
- **Motion spec.** Trigger: time, from panel wake. Idle: path
  redraws at 4Hz in `--cyan-dim`, amplitude per its function
  (≤6px vertical). Hover/focus: the trace's stroke transitions
  to `--cyan` over 200ms and its caption value prints at full
  `--paper`; the other traces are unaffected — attention is
  local. The redraw is phase-based from the loop's clock, so a
  hidden tab pauses the instruments and resumes them in phase.
- **States.** Idle (dim, redrawing) / attended (hover or focus —
  full cyan) / printed (reduced motion or no-JS: a static path,
  the waveform's declared shape at phase zero) / off-screen
  (redraw suspended by IntersectionObserver; the last drawn
  frame holds).
- **Content merge.** Each trace is labelled with a real
  diagnostic and a value from the record; the hero's density
  trace is the same density the hero shot's log entry cites.
  A trace that measured nothing would be a screensaver, and
  screensavers fail §9.
- **Failure fallback.** The static path ships in the DOM (phase
  zero of the declared function); the script replaces it with
  live redraws only after the loop's first successful frame.
  Watchdog at 1500ms: if redraws stall, the shipped path stays
  — the panel shows a held trace, which instruments also do.
- **Reduced-motion variant.** Static printed waveforms, full
  captions. Hover still brightens (a colour change, not motion)
  for visitors who allow it via focus; the redraw never starts.
- **Performance budget & mobile variant.** Three paths × 120
  points at 4Hz: ≤0.3ms/frame amortised. Mobile: one trace only
  (the hero's density trace), 80 points, still 4Hz; the other
  panels print static waveforms — a phone is a smaller control
  room, not a lesser one.
- **Choreography timeline (v2).** t=0 panel wakes → static path
  visible (it shipped that way) → t≈300ms first live redraw
  replaces it seamlessly at phase → idle redraws at 4Hz → hover
  at any t: 200ms brighten → pointer leaves: 300ms return to
  dim (slower out than in — attention lingers a beat, like an
  operator's eye).
- **State matrix (v2).** *Rest:* idle dim redraw. *Hover:* full
  cyan + caption at full paper. *Focus:* the trace panel is
  focusable as a figure; focus = attended, with a 2px `--cyan`
  outline on the panel bezel. *Active:* n/a. *Scrolled-past:*
  redraw suspended, last frame held. *Disabled:* n/a. *Touch:*
  tap toggles attended; a second tap elsewhere moves attention.
- **Breakpoints (v2).** ≥1200px: three traces, 120 points.
  768–1199px: two traces (density + beam), 100 points. <768px:
  one trace, 80 points, grid cells 20px.
- **Edge cases & failure modes (v2).** *Waveform function
  missing from the record:* the panel prints its caption with
  `TRACE NOT LOGGED` and a flat baseline — an honest instrument
  failure, in the theme's own language. *Content longer than
  the panel:* traces are fixed-height (96px); they never grow
  the bezel. *Pointer over a trace during a shot's fire:* the
  brightening holds; firing does not steal attention from a
  diagnostic the visitor is reading.
- **Accessibility spec (v2).** Each trace is a figure with a
  text alternative giving the diagnostic's current value and
  trend in words ("electron density, 8.4×10¹⁹ m⁻³, steady").
  The live redraw is `aria-hidden` — a 4Hz visual refresh must
  never reach a live region. Cyan on slate is 7.4:1, so the
  attended caption is legible to low-vision visitors, not only
  bright to sighted ones.
- **Tokens consumed (v2).** `--cyan`, `--cyan-dim`, `--paper`,
  `--paper-dim`, `--grid-line`, `--slate`, `--dur-trace-refresh`
  (250ms), `--loop-lerp` (0.10).

### 6.7 The confinement clock

- **What & why.** A real-time counter in the header accumulates
  the visitor's time on page *counted as the machine counts* —
  in seconds, to one decimal, labelled `ON SHIFT`. It pauses
  when the tab hides and resumes when it returns, because the
  machine does not credit unattended time either. It belongs
  because it quietly enrols the reader in the shift: by the
  handover (§6.16), the footer can print the night's held plasma
  (3.672 s across 6 shots) beside the visitor's own watched
  time, and the comparison — a star held for 3.672 s, attended
  by you for 4:12 — is the theme's scale argument made personal.
- **Structure.** A mono readout in the console header (§4):
  label `ON SHIFT` in label style, value in data-small tabular
  mono, format `0.0 s` under a minute, `M:SS` beyond it. Driven
  by the shared loop's phase clock (accumulated *visible*
  elapsed time, not wall time). The value is session state, not
  record state — it is never written to the log, and it resets
  per visit, as a visitor's shift does.
- **Motion spec.** Trigger: page load. Updates at 10Hz (every
  100ms of visible time), text write only — no roll, no easing;
  clocks tick, they do not perform. `visibilitychange` freezes
  accumulation within one frame; returning resumes from the
  frozen value with no catch-up jump.
- **States.** Running (tab visible) / paused (tab hidden —
  indistinguishable on screen, which is the point) / printed
  (no-JS: the header shows `ON SHIFT —:——`, an honest blank,
  since a printed page cannot know how long it was read).
- **Content merge.** The clock shares the header with the shot
  counter (§6.2): one counts the machine's night, the other
  counts the visitor's attendance at it, and the handover
  (§6.16) reconciles the two. It is the only element that
  measures the reader, and it measures them in the machine's
  unit — participation, not surveillance; nothing is stored or
  sent.
- **Failure fallback.** Watchdog at 1000ms: if the loop stalls,
  the clock freezes at its last value rather than jumping when
  frames resume — a clock that leaps is lying about the gap.
  On loop recovery it resumes from the frozen value, having
  honestly lost the stalled seconds, like any instrument that
  was down.
- **Reduced-motion variant.** Identical — a 10Hz text tick is
  information, not animation, and it is exempt by the same
  reasoning that exempts a real clock. Visitors who disable
  JavaScript get the printed blank above.
- **Performance budget & mobile variant.** One text write at
  10Hz; ≤0.05ms/frame. Mobile: the clock moves to the header's
  second row (§6.2) at data-small size; the tick rate is
  unchanged.
- **Choreography timeline (v2).** t=0 load → clock starts at
  0.0 → ticks at 100ms visible-time intervals → at the
  handover, the footer reads the final value once and prints
  the reconciliation line → the clock keeps running above the
  footer for as long as the visitor stays; the printed line is
  a snapshot, labelled with the time it was taken.
- **State matrix (v2).** *Rest:* ticking. *Hover:* none.
  *Focus:* not focusable; it is a readout. *Active:* n/a.
  *Scrolled-past:* n/a — header resident. *Disabled:* n/a.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: header right, `ON SHIFT 04:12`.
  768–1199px: seconds-only format beyond 99.9 s is replaced by
  `M:SS` from 60 s (same rule, tighter cell). <768px: second
  header row, left-aligned under the counter.
- **Edge cases & failure modes (v2).** *Very long visits:* the
  format caps at `59:59` then rolls to `1:00:00` — a visitor
  who has attended a full hour of shift gets the hour format
  the log itself uses for shift elapsed time. *System clock
  changes mid-visit:* the phase clock is monotonic
  (`performance.now`-based); wall-clock jumps cannot move it.
  *Multiple tabs:* each tab runs its own attendance; the log
  does not arbitrate between a visitor's windows.
- **Accessibility spec (v2).** `aria-live="off"` and the value
  node is `aria-hidden`; a visually-hidden static text reads
  "Time on this page is counted in the header" — a 10Hz readout
  must never be announced. The handover's reconciliation line
  (§6.16) is ordinary text and fully accessible: the meaningful
  number reaches everyone, once, in prose.
- **Tokens consumed (v2).** `--paper`, `--paper-dim`,
  `--slate-raise`, `--dur-clock-tick` (100ms).

### 6.8 Click-to-fire

- **What & why.** Clicking a log entry (§6.11) fires a shot from
  it: a mini-ring in the entry's bezel races once, its parameter
  readouts re-count shallowly (§6.3's re-fire state), and the
  entry gains the console operator's initials — `J.M.` — with a
  line: `RE-FIRED FROM THIS ENTRY · <visitor's time>`. The
  reader takes a turn on shift; interaction as participation in
  the log, not a game bolted onto it. One entry refuses: the
  anomaly (§6.5) cannot be re-fired.
- **Structure.** Each log entry card (§6.11) carries a 44px
  mini-ring SVG in its bezel corner and a real `<button>` —
  labelled with the shot number and "fire this shot again" —
  styled as a console key (§11). The fire is local: the entry's
  own ring and readouts perform; the main torus does not refire
  (the visitor is re-running a logged shot at the bench, not
  re-running the night). The initials line is appended to the
  entry's DOM and to `shiftState.refired` (§6.17) for the
  session.
- **Motion spec.** Trigger: click/tap/Enter on the entry's key.
  Mini-ring circuit 700ms under `--ease-fire` → readouts
  re-count over 600ms from 92% of held values under
  `--ease-hold` → the initials line prints in one frame →
  the key settles to its fired state. Total interaction ≤1400ms,
  and the entry is inert during it (double-fires are queued out,
  not stacked).
- **States.** Armed (key live, ring at standby) / firing
  (≤1400ms) / fired (key disabled, labelled `FIRED · J.M.`, ring
  drawn full at 85%) / refused (the anomaly entry: no key is
  rendered at all — refusal by absence, not by a greyed button
  begging the question).
- **Content merge.** The re-fire is logged *in the entry
  itself*, in the log's own format, with the console operator's
  initials — the visitor's action becomes part of the record
  they are reading, attributed to the person on console, exactly
  as the room would attribute it. Nothing about it leaves the
  log's grammar: no confetti, no score, no share button.
- **Failure fallback.** Watchdog at 1800ms: the entry completes
  to fired state with values at held figures and the initials
  printed. No-JS: entries render without keys — the log is
  complete; firing is a shift privilege, not a reading
  requirement.
- **Reduced-motion variant.** The key works: no circuit, no
  re-count — the initials line prints and the key settles to
  `FIRED · J.M.` The participation survives; the performance
  is what is removed, which is the correct trade.
- **Performance budget & mobile variant.** One small SVG +
  three text writes for ≤1400ms; ≤0.3ms/frame. Mobile: the key
  is a full-width strip at the entry's foot (44px tall) — a
  bench key you can hit with a thumb — and the mini-ring sits
  left of it at 36px.
- **Choreography timeline (v2).** t=0 key press → key depresses
  (40ms) → t=60ms mini-ring strikes → t=760ms circuit completes
  → t=760–1360ms readouts re-count → t=1400ms initials line
  prints, key settles to fired → watchdog deadline t=1800ms
  passes unused.
- **State matrix (v2).** *Rest:* armed. *Hover:* key face lifts
  1px, ring brightens to full `--amber-dim` readiness. *Focus:*
  2px `--amber` outline, offset 2px; Enter/Space fire. *Active:*
  depressed during the fire. *Scrolled-past:* state persists —
  a fired entry stays fired for the session. *Disabled:* the
  fired state *is* the disabled state, labelled with its reason
  (`FIRED · J.M.`), never a bare grey. *Touch:* tap fires; no
  hover lift.
- **Breakpoints (v2).** ≥1200px: key in the bezel corner, 44px.
  768–1199px: key at the entry's foot, right-aligned. <768px:
  full-width key strip, mini-ring 36px.
- **Edge cases & failure modes (v2).** *Rapid clicking:* the
  first press owns the entry until it settles; later presses
  are ignored, not queued — a console key mashed is a key
  pressed once. *Visitor re-fires every entry:* permitted; the
  handover (§6.16) gains a session line, `6 ENTRIES RE-FIRED
  FROM THE LOG · J.M.`, printed only if the count is >0 — the
  night acknowledges participation in its own format.
  *Session state lost (reload):* entries return to armed; the
  log's printed record is untouched — re-fires were session
  annotations, and the theme never pretends otherwise.
- **Accessibility spec (v2).** The key is a native button with a
  full label ("Fire shot 4,813 again from this entry"); after
  firing, its label updates to the fired state and the initials
  line is announced once via a polite live region — the one
  announcement the theme makes, because the visitor caused it.
  Touch target 44px minimum at every breakpoint.
- **Tokens consumed (v2).** `--amber`, `--amber-dim`, `--paper`,
  `--slate-raise`, `--ease-fire`, `--ease-hold`,
  `--dur-refire` (700ms), `--dur-recount` (600ms).

### 6.9 Panel-screw bezels with laminated sheen

- **What & why.** Every panel and photograph sits in a
  screw-cornered bezel, and as a panel enters view a slow
  laminated sheen passes across it once — light moving over
  control-room glass. Even photography is behind the machine's
  framing here: the frame is part of the instrument, and the
  sheen is the room's light acknowledging a panel as it joins
  the wall. It is the theme's one permitted glamour, and it is
  rationed to a single pass per panel per visit.
- **Structure.** The bezel is CSS: 1px `--slate-raise` border,
  10px radius, and four screw heads as inline SVG backgrounds
  (8px circles, a slot line at a seeded rotation per screw — no
  two panels' screws share a rotation pattern, because real
  screws don't). The sheen is a `::after` layer carrying
  `--sheen`, translated from −20% to 120% across the panel,
  clipped by the bezel's radius, `pointer-events: none`.
- **Motion spec.** Trigger: the panel's first crossing of the
  62% reading line. One pass, 1600ms, `--ease-sheen` (linear —
  glass does not ease), then the layer parks off-panel and is
  never re-run for that panel. Panels already in view at load
  sheen in bezel order during the wake sequence (§6.15),
  staggered 90ms apart.
- **States.** Unseen (sheen parked left) / passing (1600ms) /
  settled (sheen gone; the bezel is matte from then on) /
  printed (no-JS and reduced motion: no sheen layer at all).
- **Content merge.** The bezel is how the theme frames *every*
  content type — parameters, traces, photographs, the form —
  so the material story is told by the container system, not by
  a hero decoration. The sheen merges because it is the room's
  light, and it stops after one pass precisely so it stays
  light and never becomes a glitter loop.
- **Failure fallback.** The sheen is pure enhancement: if its
  observer never fires, panels are simply matte, which is their
  settled state anyway. No watchdog is needed for content —
  none is hidden — but a 3000ms sweep removes any sheen layer
  caught mid-pass by a stalled loop, parking it off-panel.
- **Reduced-motion variant.** No sheen, ever. Bezels and screws
  remain — the material without the light pass.
- **Performance budget & mobile variant.** One transform on one
  layer per panel, once; ≤0.1ms/frame during a pass. Mobile:
  screws shrink to 6px, sheen pass shortens to 1200ms (smaller
  panels, shorter travel), everything else unchanged.
- **Choreography timeline (v2).** t=0 panel crosses the reading
  line → t=100ms sheen enters the bezel's left edge → t=1700ms
  sheen exits right → layer parks; the panel is matte for the
  rest of the visit. At load: wake order governs, §6.15.
- **State matrix (v2).** *Rest:* matte bezel. *Hover:* no sheen
  replay — hover instead raises the bezel border to `--paper-dim`
  at 40% for as long as the pointer rests (a held light, not a
  moving one). *Focus:* a focused panel's bezel takes the 2px
  `--amber` focus outline outside the screws. *Active:* n/a.
  *Scrolled-past:* settled, permanently. *Disabled:* n/a.
  *Touch:* no hover state; the single entry pass still runs.
- **Breakpoints (v2).** ≥1200px: screws 8px, inset 10px.
  768–1199px: screws 7px, inset 8px. <768px: screws 6px,
  inset 7px; sheen 1200ms.
- **Edge cases & failure modes (v2).** *Very tall panels* (the
  parameter table, §6.12): the sheen passes across the visible
  head of the panel only — the layer is capped at 480px tall,
  so a long table does not take 4s of glass-light. *Panels
  added dynamically* (form confirmation, §6.14): the new panel
  sheens once on insertion, in the same grammar. *Print
  stylesheet:* bezels print as hairline frames, screws omitted —
  paper logs do not have screws, and the printout is the log's
  home format.
- **Accessibility spec (v2).** Bezels and sheen are decorative
  (`aria-hidden` pseudo-elements and background SVGs); panel
  semantics come from the content's own landmarks and headings.
  The sheen's contrast is ≤9% white over slate — far below any
  flash or distraction threshold — and it never overlays text
  at higher contrast while text is being read (it passes once,
  on arrival, before reading begins).
- **Tokens consumed (v2).** `--slate-raise`, `--slate`,
  `--sheen`, `--paper-dim`, `--amber`, `--dur-sheen` (1600ms),
  `--ease-sheen`.

---

### 6.10 Control-room masthead & shot navigation

- **What & why.** The page-family navigation, in the room's
  language: a console masthead carrying the shift mark
  (`SHIFT B — CONTAINMENT LOG`), links styled as labelled
  console keys, and a shot index — direct links to each shot
  section by number (`#4,812` … `#4,817`) — so a returning
  visitor can go straight to a shot the way an operator flips
  the log to a page. Navigation here is not a menu; it is the
  console's key bank plus the log's thumb index.
- **Structure.** The header (§4) is the masthead: left, the
  shift mark in Space Grotesk panel-title size; centre-left,
  the key bank (Home / The Log / The Machine / Visit — the
  site's real sections); right, §6.2's counter and §6.7's clock.
  The shot index is a secondary strip under the header on the
  home page only: six mono shot chips, one per shot, each
  showing number + timestamp. A chip fills with `--amber-dim`
  once its shot has fired — the index is also a progress record.
- **Motion spec.** Trigger: scroll and navigation events. Chip
  fill: when a shot fires, its chip transitions to filled over
  300ms under `--ease-hold` — bookkeeping, not celebration.
  Anchor jumps to a shot: the browser's instant jump is kept
  (the log does not smooth-scroll its readers around), and the
  target shot fires on arrival if it has not already (§5's
  trigger discipline). Key press feedback: 40ms depress.
- **States.** Keys: rest / hover (face lifts 1px) / current
  (the key for the page being read is held down — a console key
  stays depressed while its circuit is live) / focus (2px
  `--amber` outline). Chips: unfired (outline only) / fired
  (filled) / the anomaly chip — visually identical to its
  neighbours when filled; the index does not point either (§6.5).
- **Content merge.** The index's chips are the record's shot
  list (§6.17) rendered as navigation — same numbers, same
  timestamps, same order. Add a shot to the record and the
  index grows a chip; the nav can never promise a shot the log
  does not contain.
- **Failure fallback.** Everything here is plain anchors and
  printed state: no-JS leaves a fully working masthead and an
  index of unfired-styled chips linking to real section ids.
  Watchdog unnecessary — nothing is hidden or animated into
  existence.
- **Reduced-motion variant.** Chip fills are instant; key
  depression is a static style. Navigation is unchanged in
  structure and order.
- **Performance budget & mobile variant.** Static DOM; one
  class toggle per shot fire. ≤0.05ms/frame. Mobile: the key
  bank collapses behind one `INDEX` key that opens the strip
  as a panel (not an overlay menu — a panel that pushes content
  down, because overlays are not furniture a control room has);
  the shot index becomes a horizontal snap-scroll row.
- **Choreography timeline (v2).** t=0 load → masthead printed,
  chips outlined → first shot fires → its chip fills (300ms) →
  subsequent fires fill in order → final shot fires → the
  header gains `LOGGED` (§6.2) and the index is a complete,
  filled record of the night.
- **State matrix (v2).** *Rest:* as above. *Hover:* key lift,
  chip border brightens. *Focus:* visible `--amber` outline on
  keys and chips alike. *Active:* 40ms depress. *Scrolled-past:*
  n/a (header resident). *Disabled:* a chip for a shot with no
  section on the current page is not rendered — the index only
  indexes what this page logs. *Touch:* tap = navigate; the
  depressed state shows for 120ms so the press is felt.
- **Breakpoints (v2).** ≥1200px: full masthead, index strip
  inline. 768–1199px: key bank compresses to three keys +
  `INDEX`. <768px: two-row header (counter + clock per §6.2),
  key bank behind `INDEX`, index as snap-scroll row.
- **Edge cases & failure modes (v2).** *A site with more pages
  than keys:* the key bank caps at five keys; further sections
  live in the log book's index (§6.11), not in the console —
  consoles have fixed key banks and the theme respects the
  furniture. *Deep link to a mid-page shot:* the masthead and
  index render normally; earlier chips stay unfired until their
  sections are passed — the index records attendance, not
  existence.
- **Accessibility spec (v2).** A real `<nav>` with an
  aria-label ("Shift B console"); the shot index is a second
  nav ("Shot index") whose chips are links with full labels
  ("Shot 4,812, fired 22:04"). Current-page key carries
  `aria-current`. Focus order: skip link → keys → index →
  counter is skipped (readout, §6.7). All targets ≥44px on
  touch layouts.
- **Tokens consumed (v2).** `--slate-raise`, `--slate`,
  `--paper`, `--paper-dim`, `--amber`, `--amber-dim`,
  `--ease-hold`, `--dur-chip` (300ms).

### 6.11 Log entry cards & the shot index

- **What & why.** The log book: the shift's entries as paper
  cards on a slate surface (§4's first paper appearance) — one
  card per shot, carrying timestamp, shot number, behaviour
  word, parameters in brief, the operator's entry text, and
  initials. This is the listing page-family element, and on the
  home page it doubles as the night's archive beneath the live
  shots: the same six shots, in their kept form. Cards are
  where click-to-fire (§6.8) lives, and where the anomaly entry
  sits — third of six, unmarked, initialled.
- **Structure.** Cards are `<article>`s on a paper ground
  (`--paper`, slate text at 13.1:1), laid in a single column at
  reading measure (68ch) — a log is read, not browsed in a
  grid. Each card: a header rule (timestamp · shot number ·
  behaviour word), the entry text in mono body, a parameter
  line in data-small, and the footer line (initials + the
  §6.8 key where permitted). Cards carry a faint ruled line
  every 26px — ledger ruling, printed in the paper's CSS, not
  an image.
- **Motion spec.** Trigger: scroll into view. Cards do not
  animate in — paper does not perform. The only motion on a
  card is §6.8's fire and a 200ms `--ease-hold` background
  settle from `--paper` at 92% brightness to full as the card
  crosses the reading line, the page "coming under the lamp".
  On listing pages, pagination is a log-page turn: the column
  crossfades 240ms while the page marker (`LOG PAGE 2 OF 5`)
  updates — a turn, not a reload spinner.
- **States.** Rest (printed) / under the lamp (reading-line
  settle) / re-fired (§6.8 states) / archived (on listing
  pages, entries from previous shifts print at 88% brightness
  with a `SHIFT A` stamp — history is dimmer, never hidden).
- **Content merge.** The cards *are* the log — the site's
  primary content in its kept form. Every field on a card is a
  field of the record (§6.17); the card layout is the record's
  print format, so the archive can never drift from the data.
- **Failure fallback.** Cards ship fully printed; no-JS is the
  canonical experience minus §6.8's keys. There is nothing to
  watchdog: paper has no failure mode short of the page itself.
- **Reduced-motion variant.** No lamp settle, no page-turn
  crossfade (instant swap). Cards identical in content and
  order.
- **Performance budget & mobile variant.** Static DOM; the lamp
  settle is one background transition per card. ≤0.05ms/frame.
  Mobile: cards full-width, parameter line wraps to two rows,
  the §6.8 key becomes the full-width strip (§6.8's mobile
  rule). Ruling stays 26px — the ledger's line spacing is a
  material constant.
- **Choreography timeline (v2).** Card crosses 75% line → lamp
  settle begins (200ms) → card at full paper brightness as its
  header rule crosses the reading line → if the visitor fires
  it, §6.8's timeline runs inside the card → nothing else ever
  moves on the card.
- **State matrix (v2).** *Rest:* printed. *Hover:* the card's
  header rule darkens 10% — the only hover a paper card gets.
  *Focus:* cards are not focusable; their §6.8 keys are.
  *Active:* n/a. *Scrolled-past:* printed, unchanged — paper
  does not reset. *Disabled:* n/a. *Touch:* no hover darkening;
  tap targets are the keys only.
- **Breakpoints (v2).** ≥1200px: 68ch column centred on the
  slate. 768–1199px: 60ch. <768px: full-width with 18px paper
  margins, entry text 14.5px, parameter line two rows.
- **Edge cases & failure modes (v2).** *A long shift* (a real
  lab's 40-shot night): the home page prints the six shots of
  the narrative shift; the full book paginates on the listing
  page at 12 entries per log page, in record order, with the
  index (§6.10) extended by page markers. *An entry with no
  prose* (a shot fired and held, nothing to say): the card
  prints `HELD. NOTHING TO REPORT.` — the log's empty entry is
  a sentence, not a gap. *Very long entry text:* cards grow;
  ruling is a background repeat, so the ledger lines continue
  honestly under any length.
- **Accessibility spec (v2).** Cards are articles with headings
  ("Shot 4,813 — 23:17") so AT users navigate the log by shot.
  The anomaly card's heading and text are ordinary in form
  (§6.5). Slate on paper and paper on slate both measure
  13.1:1; the archived dimming never drops text below 7:1.
- **Tokens consumed (v2).** `--paper`, `--slate`, `--paper-dim`,
  `--amber`, `--ease-hold`, `--dur-lamp` (200ms).

### 6.12 The parameter table

- **What & why.** The shift's numbers as one ruled table — every
  shot, its timestamp, temperature, field, confinement and
  behaviour — the page-family data table and the record's most
  literal printing (§6.17). It belongs because technical
  visitors will want the night on one screen, comparable
  digit-for-digit, and because a theme that asks to be believed
  must offer its figures in the least theatrical format it owns.
  The table is the log's evidence page.
- **Structure.** A real `<table>` on a slate panel inside a
  bezel (§6.9): six columns (`SHOT`, `TIME`, `CORE TEMP`,
  `FIELD`, `CONFINEMENT`, `BEHAVIOUR`), six rows from the
  record, a footer row printing the shift totals — `6 SHOTS ·
  HELD TOTAL 3.672 s · PEAK 127.4 MK · BEST 1.120 s` — each
  total computed from the rows it sums, so the table can be
  audited by eye. Numerals tabular mono (§3); the anomaly row
  is formatted identically to its neighbours.
- **Motion spec.** Trigger: none for the table itself — tables
  do not perform. The single permitted behaviour: when a shot
  fires elsewhere on the page, its already-printed row is
  already correct (the table ships complete); a 300ms
  `--paper-dim` underline draws under the most recently fired
  row, a pencil line under the current entry, nothing more.
  Sorting is not offered: the log's order is time, and time is
  not a preference.
- **States.** Printed (complete from first paint) / underlined
  (the latest fired shot's row) / archived (previous shifts'
  tables print under their own shift stamps on the log page).
- **Content merge.** The table is the record (§6.17) with rules
  drawn around it — the purest content-merge on the page. Its
  totals row is the handover's figures (§6.16) in their second
  printing; all three printings must agree, and §10's gate
  checks them against each other.
- **Failure fallback.** None required: a static table is its
  own fallback. No-JS loses only the underline.
- **Reduced-motion variant.** The underline prints instantly
  under the latest fired row (which, without firing, is the
  final row). Identical content.
- **Performance budget & mobile variant.** Static. Mobile: the
  table becomes a stacked card list — one mini-card per shot
  with the same six fields as label/value pairs — because a
  six-column table squeezed to 360px would falsify the digits'
  alignment, and the log does not falsify. The totals row
  becomes the list's footer card, word for word.
- **Choreography timeline (v2).** t=0 the table is on the page,
  complete → as shots fire during the reading, the underline
  moves (300ms draw) → at the final shot, the underline rests
  under #4,817 and the totals row is simply correct, as it was
  at t=0 — the table never waited for the theatre to know the
  night.
- **State matrix (v2).** *Rest:* printed. *Hover:* a row's
  background lifts 4% — the reader's finger on a line of the
  ledger. *Focus:* rows are not focusable; the table is reached
  by its caption and read linearly. *Active:* n/a.
  *Scrolled-past:* printed. *Disabled:* n/a. *Touch:* no hover
  lift; the underline still tracks firing.
- **Breakpoints (v2).** ≥1200px: full table, 12.5px data.
  768–1199px: full table, `BEHAVIOUR` column abbreviates to its
  first word. <768px: stacked card list per above.
- **Edge cases & failure modes (v2).** *A shot with a missing
  parameter:* the cell prints `— · NOT LOGGED` (§6.3's rule) and
  the totals row recomputes over logged values only, footnoted
  `TOTALS OVER LOGGED SHOTS`. *A 40-shot shift:* the table
  paginates with the log book (§6.11) at 12 rows per page, the
  totals row on the final page only — a total printed before
  its rows is a promise, not a sum.
- **Accessibility spec (v2).** Proper `<th scope="col">`
  headers, a `<caption>` naming the shift, and totals in a
  `<tfoot>` — the table is fully legible to AT in source order.
  The underline is decorative and `aria-hidden`; the "latest
  fired" fact is available in the shot index (§6.10) for anyone
  who needs it as data.
- **Tokens consumed (v2).** `--slate`, `--slate-raise`,
  `--paper`, `--paper-dim`, `--grid-line`, `--dur-underline`
  (300ms).

### 6.13 The operator roster & initials legend

- **What & why.** A strip naming Shift B's five operators —
  name, role, initials — set as a console-plate roster. It
  belongs because the log's initials are everywhere (`R.O. ·
  M.L. · T.H.` at 03:40; `J.M.` on re-fires; `A.O.` on the
  handover), and initials without a legend are a code the
  visitor cannot read. The roster turns the log's shorthand
  into people: the theme sells the calm of specific humans, so
  the humans are named, with their jobs, once, without
  sentimentality.
- **Structure.** A slate panel (§6.9 bezel) with five rows, one
  per operator: initials in a 44px amber-outlined cell, name in
  panel-title Space Grotesk, role in mono body (`SHIFT LEAD`,
  `MAGNETICS`, `DIAGNOSTICS`, `FUELLING`, `CONSOLE`), and a
  watch line in data-small (`ON CONSOLE NOW` for J. Marek —
  the one live fact the roster carries, and the reason §6.8's
  initials are J.M.'s). The roster is record data (§6.17): the
  anomaly's three witnesses are rows 2–4, and nothing on the
  roster marks them.
- **Motion spec.** Trigger: none ambient. On §6.8's first
  re-fire anywhere on the page, J. Marek's watch line gains
  the suffix `· LOGGING RE-FIRES` — one text change, printed in
  a frame, the roster acknowledging the session. That is the
  roster's entire motion budget, spent once.
- **States.** Printed / annotated (after a re-fire, Marek's
  line) / archived (previous shifts' rosters print on the log
  page under their shift stamps).
- **Content merge.** The roster is the legend the rest of the
  page depends on: it explains 03:40's initials, the re-fire
  attribution and the handover signature in one panel. It is
  placed directly before the log book (§6.11) in the page
  order, so the visitor learns the handwriting before they
  read the entries — the way a new operator is briefed.
- **Failure fallback.** Static panel; no fallback required.
- **Reduced-motion variant.** Identical — there is no motion to
  reduce beyond a text change, which remains.
- **Performance budget & mobile variant.** Static DOM.
  Mobile: rows stack with the initials cell inline-left; the
  panel stays one bezel, five rows, no accordion — a roster is
  read whole or not at all.
- **Choreography timeline (v2).** t=0 printed → (optional)
  first re-fire: Marek's line updates in one frame, in step
  with §6.8's initials printing → nothing else, ever. The
  roster's stillness is its character: people, listed, at work.
- **State matrix (v2).** *Rest:* printed. *Hover:* a row's
  initials cell fills `--amber-dim` — looking at a person.
  *Focus:* rows are not focusable (the panel is a figure with a
  caption). *Active:* n/a. *Scrolled-past:* printed.
  *Disabled:* n/a. *Touch:* no hover fill.
- **Breakpoints (v2).** ≥1200px: five rows, watch line right-
  aligned. 768–1199px: watch line moves under the role.
  <768px: stacked rows per the mobile rule.
- **Edge cases & failure modes (v2).** *An operator with two
  roles in a small lab:* the role cell lists both, comma-
  separated; initials stay unique — the record validator
  (§6.17) refuses duplicate initials within a shift, because
  an ambiguous initial is a broken log. *A mid-shift personnel
  change:* the roster gains a watch line (`TOOK CONSOLE 04:00`)
  rather than a second roster — the log records handovers, it
  does not rewrite the plate.
- **Accessibility spec (v2).** The panel is a figure captioned
  "Shift B — operators"; initials cells carry `aria-label`s
  with the full name, so the legend works non-visually: an AT
  user meeting `R.O.` at 03:40 can resolve it here. Contrast:
  initials in `--amber` on slate 5.8:1 at 19px display size.
- **Tokens consumed (v2).** `--slate`, `--slate-raise`,
  `--paper`, `--paper-dim`, `--amber`, `--amber-dim`.

### 6.14 The request-a-visit form & its stamped confirmation

- **What & why.** The conversion element, in the log's grammar:
  a request to visit the control room (partners, researchers,
  press, recruits) submitted not with a success toast but by
  being *entered in the log* — the confirmation is a log line
  bearing the next entry number after the book's printed count
  (`ENTRY № 215`, the book holding 214), a timestamp, and the
  line `LOGGED. THE SHIFT WILL ANSWER.` A conversion that
  becomes part of the record is worth more than one that
  vanishes into a CRM animation, and it is the theme's proof
  that its grammar can carry a real business function.
- **Structure.** A slate panel form (§11's inputs): name,
  organisation, reason (a select: `PARTNERSHIP / RESEARCH /
  PRESS / CAREERS`), a date window (two date inputs), and a
  free line (`WHAT DO YOU WANT TO SEE`). The submit key is a
  console key labelled `LOG THIS REQUEST`. On submit, the form
  panel is replaced — in place, same bezel — by the confirmation
  panel: a paper log line (§6.11's card format, miniaturised)
  with the entry number, the visitor's stated reason and name,
  the timestamp from the visitor's clock formatted `HH:MM`, and
  the fixed line. The entry number is computed as printed
  count + 1 from the record (§6.17) — arithmetic the visitor
  can verify against the log book's own header.
- **Motion spec.** Trigger: submit. The submit key depresses
  (40ms) → the ring mini (§6.8's) in the panel corner fires a
  700ms circuit — the request is fired into the log → the form
  crossfades 240ms to the confirmation panel → a stamp effect:
  the word `LOGGED` in label style scales from 1.15 to 1.0 over
  180ms under `--ease-hold` with a 1-frame `--paper` flash on
  the stamp's border — the one stamp the theme permits itself,
  because logs are stamped. Total ≤1200ms.
- **States.** Ready / invalid (errors per §12's voice, fields
  marked in `--paper` with a written reason — never `--alarm`)
  / submitting (key held down, form inert, ≤1200ms) / logged
  (confirmation panel; the form does not return this session —
  a request is in the book) / failed (network error: the panel
  prints `NOT LOGGED — CONNECTION DOWN. YOUR WORDS ARE KEPT
  BELOW.` and restores the filled form; nothing the visitor
  typed is discarded, because the log does not lose entries).
- **Content merge.** The form's output is a log entry in the
  site's own archive format, numbered from the archive's own
  count — the conversion is continuous with the content on
  both sides of the submit. It also closes the theme's loop:
  the visitor arrived as a reader of the log and leaves as an
  entry in it.
- **Failure fallback.** Watchdog at 3000ms on the submit: if no
  response state has rendered, the failed state above prints
  with the form intact. No-JS: the form posts to a real endpoint
  and the confirmation is a server-rendered page in the same
  panel format — the entry number then comes from the server's
  count, same arithmetic.
- **Reduced-motion variant.** No circuit, no stamp scale: the
  confirmation panel replaces the form instantly, `LOGGED`
  printed at rest. The entry number and line are unchanged —
  the substance was never the stamp's motion.
- **Performance budget & mobile variant.** One panel swap +
  one mini circuit; ≤0.3ms/frame for 700ms. Mobile: the form
  stacks single-column, the submit key full-width 48px, the
  confirmation card follows §6.11's mobile card rules.
- **Choreography timeline (v2).** t=0 submit → key depresses →
  t=60ms mini-ring strikes → t=760ms circuit completes →
  t=760–1000ms crossfade to the confirmation panel → t=1000ms
  stamp lands (180ms) → t=1200ms panel settles; the entry is
  in the book. Watchdog deadline t=3000ms passes unused.
- **State matrix (v2).** *Rest:* ready. *Hover:* key lift 1px.
  *Focus:* fields take a 2px `--amber` outline; focus order is
  reading order, reason select before dates. *Active:* key
  depressed while submitting. *Scrolled-past:* n/a (state
  persists in place). *Disabled:* after logging, the form is
  replaced, not disabled — absence over greyness, as with
  §6.5's refused key. *Touch:* full-width key, 48px targets,
  native date inputs.
- **Breakpoints (v2).** ≥1200px: two-column form (name/org,
  dates paired), panel in the 8-column measure. 768–1199px:
  single column, panel 10 columns. <768px: single column,
  full-width key, confirmation card per §6.11 mobile.
- **Edge cases & failure modes (v2).** *Double submit:* the
  first owns the panel; a second request in the same session
  is a new visit, not a form state — the confirmation panel
  carries a text link, `LOG ANOTHER REQUEST`, that re-opens
  the form with the count now at 215, so the next entry is
  № 216: the arithmetic stays honest across repeats.
  *Validation failure on the date window* (end before start):
  the error prints in the log's voice — `WINDOW ENDS BEFORE IT
  OPENS. CHECK THE DATES.` — beside the fields, never as a
  modal. *Very long names/organisations:* the confirmation
  line wraps inside the card; the entry number never wraps.
- **Accessibility spec (v2).** Native inputs with visible
  labels (label style, §3); errors are text beside their
  fields, linked via `aria-describedby`, and the error summary
  is the first focus target after a failed submit. The
  confirmation panel is announced politely, once, with its
  entry number — the visitor caused it, so the theme speaks.
  All targets ≥44px; contrast per §2 throughout (errors in
  `--paper` 13.1:1, never red).
- **Tokens consumed (v2).** `--slate`, `--slate-raise`,
  `--paper`, `--paper-dim`, `--amber`, `--ease-hold`,
  `--ease-fire`, `--dur-stamp` (180ms), `--dur-refire` (700ms).

---

### 6.15 Panel-wake skeleton & the between-shots transition

- **What & why.** The page-family loader and transition, in the
  room's grammar: panels do not skeleton-shimmer like a social
  feed; they *wake* — bezel first, grid second, content last —
  the way a console's panels come up when the shift powers the
  wall. On first load the wake is the entrance (§5); between
  pages it is the transition: panels dim to standby in bezel
  order, the new page's hero ring fires once, panels wake. A
  hard ceiling rules both: no wake may exceed 1500ms, and
  content is never behind the wake — the DOM ships complete,
  so the wake is a lighting sequence over a finished room.
- **Structure.** The skeleton state of a panel is its bezel +
  grid at 40% with content regions shown as `--slate-raise`
  blocks in the content's true shapes (parameter stacks as
  three bars, log lines as ruled rows) — shapes, not grey
  soup, so layout never shifts when content lands. The wake is
  a class sequence driven by the shared loop; the transition
  reuses the same classes in reverse for the dim.
- **Motion spec.** Trigger: load, and route change. Wake order:
  bezels fade in (200ms, `--ease-wake`) staggered 60ms per panel
  in reading order → grids print (150ms) → content replaces its
  shapes in one frame per panel, staggered 90ms → the hero ring
  fires (§6.1). Total ≤1500ms, and any input (scroll, key,
  tap) completes the wake instantly — the room does not make a
  visitor wait for its lighting. Transition (client-side
  routes): dim 300ms in reverse bezel order → swap → wake as
  above, ring firing on the new hero.
- **States.** Asleep (skeleton shapes) / waking (≤1500ms) /
  awake (terminal; the skeleton classes are removed, not
  hidden) / dimming (transition out) / printed (no-JS: no
  skeleton ever renders — content ships awake).
- **Content merge.** The wake is the room's own power-up
  ritual, and its order — frame, instrument, reading — is the
  theme's hierarchy performed once per visit. Because the
  skeleton uses the content's true shapes, even the loading
  state teaches the page's structure; it is the log's furniture
  arriving before its entries, never a branded spinner.
- **Failure fallback.** Watchdog at 1500ms per panel: any panel
  still asleep completes instantly to awake with content
  printed. The skeleton is JS-inserted over shipped content —
  if the script dies before inserting, the page is simply
  awake, which is the fallback and the default at once.
- **Reduced-motion variant.** No wake sequence: panels render
  awake. Transitions are instant swaps. The 1500ms ceiling is
  honoured by having nothing to wait for.
- **Performance budget & mobile variant.** Class toggles and
  opacity only; ≤0.2ms/frame during a wake. Mobile: the stagger
  tightens to 40ms (fewer panels per screen), ceiling 1200ms —
  a smaller room wakes faster.
- **Choreography timeline (v2).** t=0 navigation → t=0–200ms
  first bezels → t≈400ms grids → t≈600–1200ms content lands
  panel by panel → hero ring strikes at t≈900ms, circuit
  completing as the last panel wakes → t=1500ms ceiling;
  watchdog passes unused on a healthy load.
- **State matrix (v2).** *Rest:* awake. *Hover / focus /
  active:* input during a wake completes it — interactivity is
  the skip. *Scrolled-past:* panels below the fold wake on
  approach, not at load, so a long page's wake budget is spent
  where the visitor is. *Disabled:* n/a. *Touch:* tap completes
  the wake, same as any input.
- **Breakpoints (v2).** ≥1200px: stagger 60/90ms as specified.
  768–1199px: stagger 50/75ms. <768px: stagger 40/60ms, ceiling
  1200ms.
- **Edge cases & failure modes (v2).** *Slow network with
  late images:* panels wake on DOM content; photographs arrive
  into their bezels (§6.9) whenever they arrive — the wake
  never waits for media, and a bezel holding an empty frame
  prints its caption, so the room reads complete with the
  photograph still in transit. *Back-button return:* the page
  renders awake from cache with no wake — the room remembers
  being on. *A route with no hero ring:* the transition's ring
  beat is skipped; dim and wake still total ≤900ms.
- **Accessibility spec (v2).** The wake is visual only: content
  is in the accessibility tree from first paint (the skeleton
  shapes are `aria-hidden` siblings, never replacements), so
  AT users are never "loaded at" later than sighted users.
  `aria-busy` is not used — the page is never busy; it is lit
  or unlit, and its content exists in both states.
- **Tokens consumed (v2).** `--slate`, `--slate-raise`,
  `--slate-deep`, `--grid-line`, `--ease-wake`,
  `--dur-wake-ceiling` (1500ms).

### 6.16 The shift handover footer

- **What & why.** The footer is the handover: the moment Shift
  B signs the night over. On paper (§4's second paper surface)
  it prints the shift's reconciled figures for the third time —
  6 shots, held total 3.672 s, peak 127.4 MK, best confinement
  1.120 s, the anomaly's one line (`03:40 · #4,815 · INITIALLED
  R.O. M.L. T.H.`) among them at the same size as everything
  else — then the visitor's reconciliation (`YOU WATCHED FOR
  4:12 OF IT`, from §6.7), the sign-off (`SHIFT B — HANDED OVER
  COMPLETE.`), and A. Osei's initials as shift lead. A footer
  that closes the record, not a sitemap with a logo.
- **Structure.** A paper sheet (§6.11's material) laid across
  the page foot: a totals table in miniature (the §6.12 totals
  row restated as prose lines), the session lines (re-fires
  §6.8, requests §6.14 — printed only when they happened), the
  reconciliation line, the sign-off, and beneath, in slate
  again, the site's legal line and secondary links in
  data-small — the room's small print, kept off the paper.
  The handover's figures are read from the record (§6.17) at
  render; they are not re-typed by the footer.
- **Motion spec.** Trigger: scroll into view. The sheet does
  not animate in (paper, §6.11); the single event is the
  reconciliation line printing in one frame when the sheet
  crosses the reading line — the visitor's watched time is
  typeset into the log at the moment they reach the end of it.
  If §6.8 re-fires happened, their session line is already
  printed above it, having been added at fire time.
- **States.** Printed / reconciled (the visitor line added) /
  signed (always — the sign-off is part of the sheet, not an
  event).
- **Content merge.** The handover is the content's conclusion:
  every figure the night produced is restated here from the
  same record, and the gate (§10) reconciles this printing
  against §6.12's totals and §6.17's record — three printings,
  one truth. The visitor's own line merges their session into
  the record they have been reading, the theme's final and
  quietest participation.
- **Failure fallback.** Static sheet; the reconciliation line
  is the only scripted part, and its absence (no-JS) leaves
  the handover complete — a printed blank (`YOU WATCHED FOR
  —:——`) is not printed at all in the no-JS sheet; the line is
  omitted rather than left empty, because the paper log would
  not have the line either.
- **Reduced-motion variant.** Identical; there is no motion to
  reduce beyond a one-frame print, which remains.
- **Performance budget & mobile variant.** One text write on
  entry. Mobile: the sheet's lines stack; the totals become
  two-column label/value pairs; the sign-off keeps its full
  sentence — it is never abbreviated to fit.
- **Choreography timeline (v2).** Sheet crosses the reading
  line → reconciliation line prints (one frame) with the
  clock's value at that instant → the visitor reads the night
  restated → below the paper, the slate small print ends the
  page. Reverse scroll: nothing unprints.
- **State matrix (v2).** *Rest:* printed. *Hover:* none — the
  handover is read, not operated; its secondary links hover
  per §11. *Focus:* links focus normally with paper-side focus
  style (2px `--slate` outline on paper). *Active:* n/a.
  *Scrolled-past:* printed. *Disabled:* n/a. *Touch:* links at
  44px targets in the small-print row.
- **Breakpoints (v2).** ≥1200px: sheet at the 8-column measure,
  totals in three columns. 768–1199px: two columns. <768px:
  stacked label/value lines.
- **Edge cases & failure modes (v2).** *A visitor who fired
  nothing and requested nothing:* the session lines are absent
  and the reconciliation line still prints — attendance alone
  is a fact worth logging. *A shift record updated between
  page render and footer entry* (a live deployment): the
  footer reads the record at render and the reconciliation is
  a snapshot labelled with its time (§6.7); the gate's
  three-printings check runs at build, not at scroll.
- **Accessibility spec (v2).** The sheet is a `<footer>` with
  an aria-label ("Shift B handover"); figures are prose lines,
  fully legible to AT in order. Slate on paper 13.1:1
  throughout the sheet.
- **Tokens consumed (v2).** `--paper`, `--slate`, `--paper-dim`,
  `--amber`.

### 6.17 The shift record — the one source of every figure

- **What & why.** The declared data record from which every
  number, timestamp, initial and behaviour on the page is
  printed: Shift B's six shots with their parameters and
  behaviours, the five operators, the log book's entry count,
  and the anomaly's single flagged entry. It is an element
  because the theme's law (§1) needs an object: *the log never
  exaggerates* is enforceable only if there is exactly one
  place the truth lives, and every printing — hero stack, log
  card, table row, handover line — is a rendering of it, never
  a re-typing.
- **Structure.** A build-time JSON object, validated before
  render: `shift: "B"`, `window: "22:00–06:00"`, `shots: […]`
  (each: `n`, `time`, `tempMK`, `fieldT`, `confS`, `behaviour`,
  `entry`, `initials[]`), `operators: […]` (each: `initials`,
  `name`, `role`, `watch`), `logEntries: 214`, and derived
  totals computed by the build, never authored (`heldTotal`,
  `peakTemp`, `bestConf`). The canonical Shift B record:
  #4,812 22:04 · 118.2 MK · 5.3 T · 0.412 s · nominal ·
  #4,813 23:17 · 121.7 · 5.3 · 0.388 · wobble · #4,814 00:52 ·
  126.9 · 5.4 · 0.905 · long · #4,815 03:40 · 124.3 · 5.4 ·
  0.417 · anomaly · initials R.O./M.L./T.H., note *"seen
  before. watching."* · #4,816 04:26 · 122.8 · 5.4 · 0.430 ·
  nominal · #4,817 05:31 · 127.4 · 5.4 · 1.120 · nominal —
  held total 3.672 s, peak 127.4 MK, best 1.120 s.
- **Motion spec.** None — the record does not move; it is what
  motion answers to. Its one dynamic relation: session state
  (`shiftState` — shots fired, entries re-fired, the visitor
  clock) is kept in a separate object that may *reference* the
  record but never mutate it. The night that happened is not
  editable by the night being read.
- **States.** Authored / validated (build gate: sums check,
  initials unique, exactly one `anomaly` behaviour, timestamps
  ascending, every shot's entry present) / rendered (printings
  generated) / archived (previous shifts' records power the
  log page's archived tables and rosters).
- **Content merge.** Total: the record is the content's source
  code. §6.3's stacks, §6.11's cards, §6.12's table, §6.13's
  roster, §6.14's entry arithmetic (214 → № 215) and §6.16's
  handover are all printings of this one object; a figure that
  cannot be traced to a field here does not ship.
- **Failure fallback.** If validation fails, the build fails —
  loudly, at build time, naming the shot and the rule. There is
  no runtime fallback for a broken record because a runtime
  fallback would be an invented figure, and invented figures
  are the one thing the theme exists to refuse.
- **Reduced-motion variant.** Identical; the record is data.
- **Performance budget & mobile variant.** The record for a
  six-shot shift is ≤4KB JSON, parsed at build into the DOM;
  the runtime never fetches it. Mobile renders the same
  record; only its printings change shape (§6.12's stacked
  cards).
- **Choreography timeline (v2).** Authoring → validation →
  printings generated → session state initialised from it
  (`shot: 4812`, fired set empty) → the page runs → session
  state accrues (fires, re-fires, clock) → the handover reads
  record + session state once, at entry, and prints the
  reconciliation.
- **State matrix (v2).** *Rest:* validated and rendered.
  *Hover / focus / active:* n/a — the record is not a surface.
  *Scrolled-past:* n/a. *Disabled:* n/a. *Touch:* n/a. Its
  states are the lifecycle above, and every surface element's
  matrix in this section is downstream of them.
- **Breakpoints (v2).** The record is breakpoint-invariant;
  its printings carry the breakpoint behaviour (§6.3, §6.11,
  §6.12). A figure that changes value with viewport width is
  a bug the gate (§10) hunts by name.
- **Edge cases & failure modes (v2).** *Two shots with the
  same number:* validation refuses — shot numbers are the
  log's primary key. *A behaviour string outside the grammar
  (§6.4):* refuses at build (unlike §6.4's runtime tolerance
  for legacy records, new records are held to the vocabulary).
  *An operator initialling a shot they did not witness:* a
  process failure no software can catch — the record carries a
  `witnessed: true` attestation per initialled entry, and the
  theme's documentation states plainly that the log's honesty
  is ultimately kept by its keepers.
- **Accessibility spec (v2).** The record itself is not a
  surface; its printings carry the accessibility specs (§6.3,
  §6.11, §6.12). One rule lives here: every figure's text
  printing includes its unit in text (`118.2 MK`, never a
  bare `118.2` relying on a visual column header), so any
  single printing, read alone by AT, is complete.
- **Tokens consumed (v2).** None — the record consumes no
  presentation tokens; that separation is its discipline.

### 6.18 No shot logged — the 404

- **What & why.** The error page, in the log's voice: a slate
  panel, a torus outline drawn but un-fired, and the entry
  that isn't: `NO SHOT LOGGED AT THIS POSITION.` — followed by
  the log's practical help: the shift's real index (§6.10's
  chips as full links) and the way back to the console. It
  belongs because a missing page in this theme is a gap in the
  log, and the log's way with gaps is to record them plainly
  and point at what exists.
- **Structure.** A single centred panel (§6.9 bezel): the ring
  SVG in its standby state (§6.1) at 240px, the message in mono
  body, the requested path printed in data-small exactly as
  requested (the log records what was asked for, including the
  typo), then the shot index and a `RETURN TO CONSOLE` key
  (§11). No illustration, no humour, no mascot — a gap, logged.
- **Motion spec.** Trigger: none. The ring does not fire — that
  is the message, performed once by omission: this position
  never ran. The standby breath (§6.1) is also stilled here;
  the 404's ring is fully at rest, the only completely still
  ring on the site.
- **States.** Printed — the only state. There is nothing to
  fire, hover or complete.
- **Content merge.** The 404 uses the theme's furniture
  (bezel, ring, index) to say the theme's sentence about
  absence, and its links are the record's real index — the
  recovery path is the content itself, not a marketing card.
- **Failure fallback.** The page is static; it is what other
  elements fall back to being. If the 404 itself fails to
  render, the server's plain-text default carries the same
  sentence — the words are the design.
- **Reduced-motion variant.** Identical — there is no motion.
- **Performance budget & mobile variant.** A static panel;
  ≤30KB total page. Mobile: ring 180px, index chips wrap to
  two rows, the return key full-width.
- **Choreography timeline (v2).** t=0 the panel is printed,
  complete → the visitor reads the gap, chooses a real shot or
  the console → leaves. The timeline is a reading, and the
  spec says so rather than inventing beats.
- **State matrix (v2).** *Rest:* printed. *Hover:* the index
  chips and key behave per §6.10/§11. *Focus:* the return key
  is the first focusable element after the message.
  *Active:* n/a. *Scrolled-past:* n/a (single panel).
  *Disabled:* n/a. *Touch:* 44px targets throughout.
- **Breakpoints (v2).** ≥1200px: panel at 6-column measure.
  768–1199px: 8 columns. <768px: full-width, ring 180px.
- **Edge cases & failure modes (v2).** *A requested path with
  markup in it:* the path prints as escaped text — the log
  records the request, it does not execute it. *A visitor
  arriving from a stale external link to a real-but-moved
  shot:* the 404's index includes a `MOVED` line only when
  the record declares a redirect for that path — otherwise
  the log does not guess where things went.
- **Accessibility spec (v2).** The message is the page's `<h1>`
  in mono — headings in this theme may be mono when the
  content is a log line (§3's laws govern values, and this
  sentence is one). Reading order: message, requested path,
  index, return key. Contrast 13.1:1 throughout.
- **Tokens consumed (v2).** `--slate`, `--slate-raise`,
  `--paper`, `--paper-dim`, `--amber-dim`.

---

## 7. Page application map

- **Home (the shift).** The full night in order: console header
  (§6.10, §6.2, §6.7), hero shot #4,812 with the pinned torus
  (§6.1, §6.3), shots #4,813–#4,817 as sections (the anomaly
  third among them, unannounced), roster (§6.13), log book
  (§6.11), parameter table (§6.12), visit form (§6.14),
  handover (§6.16). The home page *is* the theme's argument;
  every other page is a room off it.
- **The Log (listing).** Previous shifts as archived books:
  shift selector tabs (§11) for A / B / C, each shift's cards
  (§6.11 archived state), tables (§6.12) and rosters (§6.13)
  under their shift stamps, paginated at 12 entries per log
  page. Shift B's book is the home page's record (§6.17); the
  listing proves the format survives other nights.
- **Shot detail.** One shot, full page: its ring at hero scale,
  full parameter stack, its traces (§6.6) at panel size, the
  entry's full text, neighbouring shots as index chips. For
  labs publishing per-shot public data; the anomaly's detail
  page is formatted identically to the other five.
- **The Machine (about/technology).** The torus and systems
  explained in the log's voice: bezel panels, photographs
  behind glass (§6.9), parameter tables for the machine's
  design envelope (clearly labelled `DESIGN`, never mixed with
  logged values — the record's honesty rule extends to
  projections: a projected figure wears its label).
- **Visit (contact/conversion).** §6.14's form at page scale,
  with the control room's visiting rules as log entries beside
  it (what visitors see, when, what they may not photograph —
  rules written like entries, because they are kept like
  entries).
- **Careers.** Shifts as the job description: rosters of real
  teams, a worked night as the page's spine, application as a
  log entry (the §6.14 grammar with `CAREERS` pre-selected).
  The theme's strongest recruiting argument is a true night,
  kept well.
- **404.** §6.18. **Print.** The log book and table print as
  paper: bezels become hairlines, the ring prints drawn, red
  never prints (the anomaly prints as its entry, as it should).

## 8. Worked examples

### 8.1 The hero — shot #4,812 fires (worked example 1)

The visitor lands. The console header is already correct:
`SHOT #4,812`, clock at `ON SHIFT 0.0`. Panels wake in bezel
order (§6.15) — the hero's torus panel third — and at t≈900ms
the ring strikes. For 900ms the head races the torus under
`--ease-fire`; as it passes 120°, 210°, 330°, the mask unclips
`CORE TEMP`, `FIELD`, `CONFINEMENT` in turn. The circuit
completes; the three values count together for 1100ms under
`--ease-hold`, passing only machine-printable figures, and land
— `118.2 MK · 5.3 T · 0.412 s` — in the same frame. 50ms later
the line prints, whole, in one frame: `CONFINEMENT: HELD.` The
grid behind the stack dims 15%. The headline, in Space Grotesk
at 56px, has been readable since first paint — *"The night
shift holds a star still."* — because headlines are not values
and were never masked. Beside the torus, the density trace
idles in `--cyan-dim` at 4Hz, captioned `8.4×10¹⁹ m⁻³ ·
STEADY`. The visitor scrolls; at the reading line the counter
has already rolled, once, to `#4,813` as shot two's panel
begins its approach scrub. Nothing on the hero has moved since
the hold. That stillness, after ninety seconds of reading, is
the loudest claim the page makes.

### 8.2 Mid-page — the anomaly, as the visitor lives it (worked example 2)

Shot #4,814 has run long and held at `0.905 s`; its log entry
calls it "the long one" and moves on. The next panel approaches
like the others — approach scrub brightening its grid — and
fires. The ring runs clean to 60%, stops for 120ms, shows one
80ms frame of red, and finishes. The parameters count and hold:
`124.3 MK · 5.4 T · 0.417 s` — ordinary numbers, the shift's
most ordinary shot on paper. `CONFINEMENT: HELD.` prints. Only
then, reading the entry card below, does the visitor find it:
`03:40 · SHOT #4,815` … the entry text, two level sentences
about a fluctuation the instruments caught and the parameters
do not show … and the line `INITIALLED R.O. · M.L. · T.H. —
seen before. watching.` There is no key on this card (§6.8's
refusal by absence). The counter in the header has rolled to
`#4,816` by the time the visitor looks up. In the choreography
map (§13) this beat is listed with the same weight as every
other beat, in the same type. The design's entire effort here
is spent on *not* spending effort — and on the three sets of
initials, which the roster (§6.13), read earlier, has already
turned into three named people who were awake at 03:40.

### 8.3 Conversion — a visit enters the log (worked example 3)

Below the table, the form panel: `REQUEST A CONTROL-ROOM
VISIT`. A researcher from a university lab fills name,
organisation, selects `RESEARCH`, picks a window, writes
*"The 03:40 entry. We run the same diagnostic."* — the theme
cannot prevent its readers from being interesting, and the log
will keep their line verbatim. She presses `LOG THIS REQUEST`.
The key depresses; the corner mini-ring fires its 700ms
circuit; the panel crossfades to paper. A log line, ruled,
stamped `LOGGED`: `ENTRY № 215 · 21:47 · RESEARCH — <name>,
<organisation>` and beneath, the fixed sentence: `LOGGED. THE
SHIFT WILL ANSWER.` The number is not theatre — the log book
above prints `214 ENTRIES THIS QUARTER` in its header, and
215 is 214 + 1, checkable by the visitor in five seconds of
scrolling. Had her window ended before it opened, the form
would have answered in the same voice, beside the field:
`WINDOW ENDS BEFORE IT OPENS. CHECK THE DATES.` — and kept
everything she typed. The conversion completes not with a
thank-you page but with a line in a book, which is the only
promise this theme makes: *you will be recorded accurately,
and answered by the shift.*

## 9. Anti-slop — what makes THIS theme look cheap

1. **Sci-fi neon overload.** Glow on everything, cyan and amber
   competing, lens flares. *Cure:* two licensed ambient loops,
   cyan rationed to diagnostics (§2), glow exactly where §6
   licenses it. A control room is dim because eyes adapt; the
   page is dim because meaning needs contrast.
2. **Alarm red as an accent.** A red badge, a red error, a red
   "live" dot — and 03:40 becomes worthless. *Cure:* the red
   census (§2, §10). One frame, ever. Errors speak in paper.
3. **Held values that tremble.** A subtle pulse on the
   temperature "to keep it alive". *Cure:* the law (§1). After
   the hold, the values are never written again (§6.3); if a
   reviewer can see a held digit move, the build fails.
4. **Explaining the anomaly.** A hero subheading that winks at
   "the night something unexplained happened". *Cure:* the
   anomaly exists only in its entry (§6.5); the gate greps
   hero and marketing copy for it. Restraint is the asset.
5. **Rounded numbers.** "120 million degrees", "over a second
   of confinement". *Cure:* every figure prints at the record's
   precision (§6.17) — 118.2 MK, 1.120 s — because the audience
   checks, and rounding is the first exaggeration.
6. **Glitch aesthetics.** Datamoshing, RGB splits, VHS noise
   "for atmosphere". *Cure:* instruments fail honestly or not
   at all; the theme's one irregularity is a single 80ms frame
   with a log entry behind it. Decoration-grade malfunction is
   a costume.
7. **The torus as a logo.** Ring motifs repeated as bullets,
   dividers, favicon confetti. *Cure:* the ring exists only
   where a shot fires (§6.1). A ring that decorates is a ring
   that will not be believed when it fires.
8. **Random-noise traces.** Squiggles drawn by a sine stack
   with random jitter. *Cure:* each trace has a declared
   waveform function and a captioned value from the record
   (§6.6). If it measures nothing, it is a screensaver.
9. **Marketing voice in the log.** Entries that say "achieved
   an incredible milestone". *Cure:* §12's two registers and
   the entry style — level sentences, figures inline, no
   adjectives the instruments did not supply.
10. **Sheen on everything, forever.** The laminated pass
    looping, or replaying on hover. *Cure:* one pass per panel
    per visit (§6.9). Glass light that repeats is glitter.
11. **Digit rolls everywhere.** Rolling timestamps, rolling
    totals in the table. *Cure:* the roll belongs to the shot
    counter (§6.2); the table prints (§6.12). Machinery is
    rationed like red.
12. **A dashboard cosplay.** Charts.js defaults, gauge widgets,
    card grids of KPIs. *Cure:* the page is a log with panels,
    not an analytics product; any component that could appear
    in a SaaS template fails §11's inventory review.

## 10. Quality gate

Blocking checks — all must pass before this theme ships in a
build, signed off by someone who did not build it:

1. **Figure audit.** Every printed figure on the page traces
   to a field in the shift record (§6.17); the three printings
   of the totals (hero-adjacent copy if any, §6.12's footer
   row, §6.16's handover) agree digit-for-digit.
2. **Red census.** `grep` the shipped CSS and JS for the alarm
   token: exactly one rule, inside §6.5's stutter. Any other
   occurrence — including in error styles — fails the build.
3. **Held-value audit.** With the page open for 5 minutes,
   no held parameter's text node changes after its hold frame.
   Automated: mutation observer on the stacks, zero writes
   after t=hold+1s.
4. **Anomaly restraint check.** Hero, headings and marketing
   copy contain no reference to the anomaly; §6.5's entry is
   the only place it exists, and click-to-fire is absent from
   its card.
5. **Watchdog drill.** With the animation loop artificially
   stalled, every armed effect completes to its printed end
   state inside its deadline (ring 2400ms, parameters 2000ms,
   wake 1500ms, form 3000ms).
6. **No-JS pass.** The full page — every shot, entry, table,
   roster, form (posting to its endpoint) and handover — is
   complete and readable with JavaScript disabled.
7. **Reduced-motion pass.** No ring race, no counts, no sheen,
   no red frame; all values printed; the anomaly present as
   text. Verified with the OS setting on, not a simulator.
8. **Loop budget.** The shared loop's frame cost ≤1.4ms with
   all citizens registered (ring + wobble + traces + clock)
   on a mid-tier laptop; long tasks none >50ms.
9. **Counter truth.** Jump-scroll to the footer and back: the
   header counter reads the true furthest shot, never more,
   never decrements.
10. **Contrast sweep.** Every text pairing meets §2's stated
    ratios at every state, including archived dimming (≥7:1)
    and the attended trace caption.
11. **Voice pass.** Log entries and UI strings read against
    §12: no unlogged adjectives in entries, no red-error
    language, fixed strings verbatim (grep for `seen before.
    watching.` and `CONFINEMENT: HELD.`).
12. **Mobile pass.** At 360px: the ring fires, parameters
    stack and hold, the table is the card list, keys are
    ≥44px, and the anomaly's timing is unchanged.

---

## 11. Component inventory

Every component a real site in this theme needs, with its
themed treatment. Anything not listed here does not appear; a
component that arrives from a generic UI kit is refused at
review (§9.12).

| Component | Themed treatment |
|---|---|
| Primary button | **Console key** — `--slate-raise` face, 1px lift on hover, 40ms depress, label in label style (`LOG THIS REQUEST`). One per panel maximum; a console does not have two big keys side by side. |
| Secondary button | **Panel link** — mono body text, `--paper`, underline drawn on hover; no box. Used for `LOG ANOTHER REQUEST`, `RETURN TO CONSOLE`. |
| Text input | Recessed slate well, `--paper` text, label above in label style; focus = 2px `--amber` outline. No floating labels — labels on a console are engraved, they do not move. |
| Select | Console key styling with a mono list; options are the log's vocabulary (`PARTNERSHIP / RESEARCH / PRESS / CAREERS`). |
| Date input | Native input in the well styling; format hint `DD MMM` printed beside it in data-small. |
| Textarea | The well, 4 rows, ruled at 26px like the log paper (§6.11) — writing a request is writing in the log. |
| Checkbox / radio | **Watch toggles** — small square wells that fill `--amber` when set; the fill is a state, not a checkmark glyph. |
| Table | §6.12 as specified: ruled, tabular mono, totals in `tfoot`, no sorting, no zebra striping (the ruling is the rhythm). |
| Badge / chip | **Shot chips** (§6.10): mono number + time, outline → `--amber-dim` fill when fired. Status chips (`HELD`, `WOBBLE, DAMPED`, `LONG`, `ANOMALY — LOGGED`) print in label style; the anomaly chip is styled identically to the others. |
| Alert | **Refused as a banner.** Notices are log lines appended to the relevant panel in mono (`NOT LOGGED — CONNECTION DOWN.`), in `--paper`. Nothing slides in from the top of a control room. |
| Toast | **Refused.** Same reason, same replacement: the log line, in place, permanent until read. |
| Modal | **Refused.** Consoles do not dim the room to ask a question. Confirmations happen inline in the panel (§6.14's logged state) or not at all. |
| Tabs | **Shift selector** (A / B / C) on the log page: three console keys in a bank, the active shift's key held down. Content swaps instantly; no slide. |
| Accordion | **Log archive folds** — previous months' entries fold under a ruled header line; opening prints the entries whole (240ms height, `--ease-hold`). Used only in the archive, never for primary content. |
| Pagination | **Log page markers** — `LOG PAGE 2 OF 5` with prev/next as panel links (§6.11). No numbered page buttons; a log is paged, not numbered like search results. |
| Tooltip | **Parameter gloss** — hovering/focusing a parameter label prints its full definition in the caption slot (§6.3's hover rule), in place. No floating bubble; the gloss is part of the panel. |
| Progress | The shot counter (§6.2) and confinement clock (§6.7) are the only progress components. No bars, no percentages, no spinners anywhere in the theme. |
| Skeleton | §6.15's panel-wake shapes — content-true shapes in `--slate-raise`, never shimmer. |
| Breadcrumbs | **Refused on the home page** (a shift is read in order); on detail pages, a single mono line: `LOG / SHIFT B / SHOT #4,815` — set as text, not a component with separators and hovers. |
| Avatar / byline | Operators are initials cells (§6.13), never photographs in circles. Faces appear only in bezel photography (§6.9), at documentary scale. |
| Search | On the log page only: a well input filtering entries by shot number or word, results printing as cards (§6.11) — the log is searched like an archive, with the count of matches logged (`3 ENTRIES`). |
| Empty state | A log sentence in place: `NO ENTRIES UNDER THIS HEADING. THE SHIFT LOGS WHAT HAPPENS.` (§12's empty-state voice), never an illustration. |
| Error state (field) | Written reason beside the field in `--paper` (§6.14); the field's well takes a `--paper` border. Red is not available (§2). |
| 404 | §6.18 as specified. |

## 12. Content & copywriting voice

Two registers, kept apart as strictly as the palette:

- **Console voice** — labels, keys, statuses. Uppercase rationed
  per §3 law 5, mono, ≤3 words where possible: `SHOT #4,812`,
  `CONFINEMENT`, `LOG THIS REQUEST`. The console names things;
  it does not describe them.
- **Log voice** — entries, explanations, errors, empty states.
  Sentence case, mono body, level and specific: figures inline
  at record precision, adjectives only where an instrument
  supplied them (`steady`, `nominal`, `long`). The log's model
  sentence: *"Shot held 0.905 s. Density steady throughout.
  Nothing to report beyond the duration."*

**Headline style.** Space Grotesk, a claim about the night or
the machine, never a figure (§3 law 3) and never the anomaly.
✓ *"The night shift holds a star still."* ✗ *"127 million
degrees, held for over a second!!"* — figures in display type,
rounding, and an exclamation: three violations in nine words.
Exclamation marks do not exist in this theme, in either
register.

**Label style.** Nouns and units, no verbs of marketing:
`CORE TEMP`, `FIELD`, `ON SHIFT`. ✗ `AMAZING POWER` — the
console does not admire the machine; it runs it.

**Error voice.** State what did not happen, what was kept, and
what to do — in that order, in the log's sentences.
✓ `NOT LOGGED — CONNECTION DOWN. YOUR WORDS ARE KEPT BELOW.`
✓ `WINDOW ENDS BEFORE IT OPENS. CHECK THE DATES.`
✗ `Oops! Something went wrong 😢` — every word of that is from
another theme.

**Empty-state voice.** Absence is a logged fact, stated once:
✓ `HELD. NOTHING TO REPORT.` / `NO ENTRIES UNDER THIS HEADING.
THE SHIFT LOGS WHAT HAPPENS.` ✗ *"Nothing here yet — check back
soon!"* — the log does not promise; it records.

**Fixed strings (verbatim, grepped by the gate).**
`CONFINEMENT: HELD.` · `seen before. watching.` · `LOGGED. THE
SHIFT WILL ANSWER.` · `NO SHOT LOGGED AT THIS POSITION.` ·
`SHIFT B — HANDED OVER COMPLETE.` · `RE-FIRED FROM THIS ENTRY`.
These sentences are part of the theme's identity; paraphrase
is drift, and drift is how the log stops being the log.

## 13. Full-page scroll choreography map

The home page, top to footer, in the order the visitor lives
it. One shared rAF loop (lerp 0.10) drives every scrubbed
value; beats are listed at their trigger points against the
62% reading line (§4).

1. **First paint.** Header correct at `SHOT #4,812`; clock
   starts; all content printed and complete. *Feels like:* the
   room was already on.
2. **Wake (≤1500ms).** Panels wake in bezel order (§6.15);
   hero sheen passes (§6.9). Input skips it instantly.
3. **t≈900ms — the hero fires.** Ring circuit (900ms), mask
   stations opening, parameters count (1100ms) and hold;
   `CONFINEMENT: HELD.` prints (§8.1). The density trace idles
   beside the torus from the first wake.
4. **Hero pin (140vh).** The torus holds centre while its
   parameter stack finishes and the approach scrub for shot
   #4,813 begins below. Releasing the pin is the visitor's
   first deliberate act of the shift.
5. **Shot #4,813 — wobble-damp.** Ring oscillates ±6px, decays
   by 1200ms, lands as parameters settle at the shift's lowest
   confinement (0.388 s). Header rolls to `#4,813` 150ms after
   the circuit. Chip fills in the index.
6. **Shot #4,814 — long run.** 2600ms circuit, count stretched
   to 1900ms, hold at 0.905 s. The 96px beat after it is the
   night's longest pause before a fire.
7. **Shot #4,815 — the anomaly.** Circuit, halt, one red frame,
   completion; nominal parameters; the initialled entry
   (§8.2). Same type, same weight as every beat around it.
8. **Shots #4,816, #4,817 — the watch and the best.** #4,816's
   parameters take an extra 400ms beat before HELD prints —
   the operators watching a little longer. #4,817 runs the
   shift's best: 1.120 s, and after its hold the header gains
   `LOGGED`.
9. **The roster.** Stillness. Five people, read whole (§6.13).
10. **The log book.** Paper. The six entries in kept form;
    the visitor may re-fire five of them (§6.8) — the night's
    second act is participation.
11. **The table.** The night on one screen (§6.12); the
    underline rests under #4,817.
12. **The form.** A request is logged, № 215 (§8.3) — or read
    past; the log does not require the visitor's paperwork.
13. **The handover.** Paper again: totals for the third time,
    the visitor's watched time printed into the record, the
    sign-off (§6.16). *Feels like:* being signed out by the
    shift lead.
14. **Reverse pass.** Scrolling back up: nothing un-fires,
    un-counts or un-holds. Chips stay filled, the counter
    stays at the furthest shot, initials stay on re-fired
    entries. Only scrubbed approach values (grid brightness on
    un-fired shots) respond to position. The log reads the
    same backwards because it is a record, and the visitor
    feels the difference between a page and a document.

## 14. Whole-page performance budget

| Budget line | Limit | Notes |
|---|---|---|
| Total page weight (home) | ≤ 780KB | Fonts are the floor: two families, subset, ≤ 160KB total |
| Photography | ≤ 110KB each, ≤ 4 on home | WebP, bezel-sized, lazy below the fold (§6.9) |
| JS (theme system) | ≤ 42KB gz | One loop, one record, no framework in the theme layer |
| CSS | ≤ 32KB gz | Bezels, grids and the single `--alarm` rule included |
| Frame budget (shared loop) | ≤ 1.4ms/frame | Ring path, wobble recompute, ≤3 trace redraws at 4Hz, counters, clock — measured in the gate's drill |
| Long tasks | none > 50ms | The record renders at build; runtime never parses the shift |
| Layout shift | CLS ≤ 0.02 | Panels reserve their shapes (§6.15); values are tabular mono so counting never reflows |
| Time to readable | first paint, JS or not | Content ships complete; JS arms theatre over the printed log |

**Cut order when the budget is exceeded** (in order, never
skip ahead): 1) photography count on home (4 → 2); 2) trace
count (3 → 2, hero's density trace is last to go); 3) the
hero pin (140vh → unpinned; the fire and mask remain); 4) the
sheen on below-fold panels; 5) approach scrub (grid brightness
static). **Never cut:** the printed completeness, the
watchdogs, the held-value discipline, the anomaly entry and
its initials, the record's precision, the reduced-motion
variants, the form's kept-words failure state. A shorter night
is legal; a rounded, wobbling or stranding one is not.

## 15. Build-order checklist

1. **The record first.** Author and validate the shift record
   (§6.17): six shots, figures summing to the derived totals,
   initials unique, exactly one anomaly, timestamps ascending.
   No design work precedes the data — the page is the record's
   printout.
2. **Static lit panels.** Build the complete page with no JS:
   header with counter printed, every shot's parameters held,
   cards, table, roster, form posting to its endpoint,
   handover reconciled. This is the fallback and it must
   already be good.
3. **Typography and tokens.** Load the two faces subset; set
   §3's laws and §2's tokens; grep the CSS to confirm the
   alarm token appears exactly once — in a rule that is not
   yet connected to anything.
4. **Bezels and grids.** §6.9's bezel system, screws with
   seeded rotations, oscilloscope grids on instrument panels.
5. **The shared loop.** rAF + lerp 0.10 + phase clock +
   watchdog registry; register nothing yet.
6. **The ring.** §6.1's torus, mask stations, standby breath;
   then §6.4's grammar (nominal, wobble, long) against test
   records.
7. **Counter and clock.** §6.2's digit roll, §6.7's visible-
   time accumulation, header integration.
8. **Parameters.** §6.3's count-and-hold with the
   never-written-again rule; the mutation-observer audit from
   §10 wired as a development check.
9. **Traces.** §6.6's declared waveforms, 4Hz redraw, attended
   state.
10. **The anomaly.** §6.5 last among the shots: connect the
    single `--alarm` rule, set the stutter timing, verify the
    no-refire absence on its card.
11. **Log book, table, roster.** §6.11–§6.13 printings from the
    record; reconcile the three totals printings.
12. **Click-to-fire.** §6.8's keys, mini-rings, re-counts,
    session state and the handover's session line.
13. **The form.** §6.14's validation in the log's voice,
    entry-number arithmetic, stamped confirmation, kept-words
    failure state.
14. **Wake, transition, 404, handover.** §6.15's wake under
    its ceiling, §6.18, §6.16's reconciliation line.
15. **Reduced-motion pass and the gate.** Every element's
    variant verified with the OS setting on; then §10's twelve
    checks, signed by a non-builder. Only then may the theme
    be used in a build.
