# #97 Reel to Reel — 50x Expanded Specification

An oral-history archive built as a reel-to-reel tape machine. Stories are
reels; the visitor presses play on people's voices. This document is the full
build specification: concept, palette, typography, layout, motion system,
eighteen fully specified elements, page application map, three worked
examples, anti-slop law, quality gate, component inventory, copywriting
voice, scroll choreography map, performance budget and build order. It is
written to be built from directly — two builders following it produce the
same archive.

---

## §1 Concept & world

**The world.** A listening room that happens to be a website. The archive
presents itself as one machine: a reel-to-reel deck built from brushed
bakelite plate, twin reels, VU meters, a mechanical tape counter and a
record lamp, sitting in front of shelves of hand-labelled tape boxes. Every
story in the archive is a physical object first and a web page second: it has
a reel number, a box, a spine label typed on a label-maker, a condition note
in pencil, a duration, a catalogue number, and a waveform that is the shape
of one person's actual voice. The visitor does not "browse content"; the
visitor threads a tape, presses play, and listens at the speed of their own
scrolling hand.

**The theme's one law — the machine never pretends.** Every number the page
shows must be the number the archive actually holds. The tape counter reads
the visitor's true position in the page, denominated in tape. The supply
reel empties by exactly the tape the take-up reel gains — pack radii obey
area conservation (§6.1), never a decorative shrink. A waveform is the
testimony's real waveform data, drawn once and honestly; a duration printed
on a box is the duration the scrub math uses; a "copies digitised" figure is
counted from the catalogue printed on the page. If a figure cannot be
traced to data on the page, the figure is absent. A tape machine cannot fake
a reading, and neither can this interface: the moment a counter is decorative,
the archive becomes a picture of a machine instead of a machine, and the
theme is dead.

**Second law — silence is printed.** Every testimony's full transcript is
present in the DOM, complete and readable, beneath and independent of every
animation. The waveform draw, the playhead, the highlight sweep are readings
laid over a document that already exists. A stuck playhead never hides a
story; a stopped reel never eats a word. This is the archive's central
courtesy, mechanised: these are people's voices, often the only record of
them, and the interface treats their words as more durable than its own
machinery.

**Mood.** Patient, mechanical, reverent without being funereal. The room is
dim (bakelite), the boxes are the colour of card that has waited forty years
in a dry cupboard, the one warm light is the record lamp's amber — somebody
is being recorded, presence is signalled the studio way. Motion is physical:
things have inertia, needles overshoot, reels take ~600ms to stop because a
real reel does. Nothing bounces like a toy; nothing glows like a game.

**Best-fit sites and audiences.** Oral-history projects and memory archives;
podcast and radio archives with back catalogues worth treating as objects;
museums of memory, community history and migration; documentary filmmakers'
companion sites; university sound archives; local-history societies
digitising cassette and reel collections. Audiences: researchers who need
catalogue discipline (numbers, conditions, provenance), descendants looking
for one person's voice, and general visitors who will give a story four
minutes if the machine makes those minutes feel held.

**When NOT to use it.** Breaking news or anything whose value is speed —
the machine's patience reads as indifference there. High-frequency commerce
(carts, flash sales): the transport grammar fights checkout urgency and the
counter-as-progress insults a two-step form. Children's products: the
reverence curdles into gloom. Pure video platforms: the theme is built for
audio testimony and the printed word; bolting a video grid onto the shelf
breaks the object discipline. Any archive that cannot supply real metadata
(durations, conditions, catalogue numbers): the law requires the data, and
without it the builders will be tempted to invent readings — which this
theme forbids absolutely.

**What the visitor should feel, in order.** *This is a real place* (the deck
is powered, the lamp is lit, the needles tremble). *These are real objects*
(the boxes have conditions, the labels were typed by someone). *I am trusted
with this* (scrolling is transport — my hand runs the machine). *The words
matter more than the machine* (the transcript is always there, whole).

---

## §2 Palette

Five anchors, inherited exactly from the theme's original entry, plus
derived tokens for the states a real build needs. Contrast values below were
measured for this expansion (relative-luminance ratio, WCAG formula), not
estimated.

| Token | Hex | Role | Usage ratio | Pairing / contrast ruling |
|---|---|---|---|---|
| `--bakelite` | `#1A1A18` | The deck plate; page ground in deck zones; footer ground | ~45% of first viewport, ~30% of page | Ground for card text (10.46:1 ✓) and record light (9.03:1 ✓). Never a text colour on card. |
| `--box-card` | `#CFC8B8` | Tape boxes, labels, transcript sheets' stock, primary text on bakelite | ~30% | On bakelite 10.46:1 ✓ all text sizes. As a ground it takes `--ink` (9.57:1 ✓). |
| `--oxide` | `#B4552D` | Tape oxide: reel pack edges, waveform stroke, splice tint, spines, stamps | ~8% | On bakelite 3.55:1 — graphics and ≥24px display only, never body text. On card 2.95:1 — **forbidden as text on card**; graphic rules/spines only. On transcript paper 3.80:1 — ≥18px only. |
| `--khaki` | `#7C8471` | Faded label green: secondary labels, shelf captions, catalogue furniture | ~7% | On bakelite 4.48:1 — labels ≥14px bold or ≥18px only, never body text, never the sole carrier of meaning. On card 2.34:1 — **forbidden as text on card**; graphic tint only. |
| `--rec` | `#E3B505` | The record light. A lamp, not a colour. | <0.5% — one lamp, ≤14px disc | On bakelite 9.03:1 ✓. On card 1.16:1 — **forbidden pairing**: the lamp only ever sits on bakelite. Never text, never a button fill, never a badge. |
| `--bakelite-2` | `#23231F` | Raised plate: header bar, meter bridge, form plate | (derived) | One step off the deck so plates read as bolted on, not printed. |
| `--plate-line` | `#3A3A34` | Hairlines, bolt rings, meter graticule on bakelite | (derived) | Graphic only. |
| `--ink` | `#23221C` | Text on card and on transcript paper | — | On card 9.57:1 ✓; on transcript paper 12.33:1 ✓. The archive's handwriting-black. |
| `--paper` | `#E8E2D2` | Transcript sheet stock (lighter than box card: it was kept in the dark) | ~15% | Takes `--ink` 12.33:1 ✓ and `--pencil` 5.66:1 ✓. |
| `--pencil` | `#5A564C` | Condition notes, pencil annotations, archivist's marginalia | ~2% | On card 4.39:1 — condition notes set ≥14px and always paired with a stamped status chip in `--ink` (the note is never the only carrier). On paper 5.66:1 ✓. |
| `--metal-hi` | `#8F8F86` | Brushed-metal highlight: secondary text on bakelite, reel arms, counter bezel | ~3% | On bakelite 5.35:1 ✓ secondary text at all sizes. |
| `--tape` | `#2E211A` | The tape pack itself (oxide-brown, near-black) | — | Graphic only; pack edge catches `--oxide` as a 1px rim light. |
| `--splice` | `#D8D2C0` | Splice tape: translucent diagonal bands, leader tape | — | At 55% opacity over bakelite or card; text never sits on a splice band. |

**Usage discipline.** The page is a dark room with pale objects in it:
bakelite grounds, card objects, oxide only where tape or rust would
physically be, khaki only where a faded label would be, and the record
light exactly once per viewport — if two lamps are visible, one of them is
lying about recording. Oxide is rationed by physics: it appears on reel
packs, waveforms, spines and stamps because those are the places oxide and
rust actually live on a machine; it never becomes a generic accent, a link
colour, or a call-to-action fill.

**Dark-mode behaviour.** The theme is already a dark room; there is no
light-mode inversion and `prefers-color-scheme: light` changes nothing —
a tape archive's listening room does not get repainted by the visitor's OS.
What does adapt: under `prefers-contrast: more`, `--khaki` labels on
bakelite are promoted to `--metal-hi` (5.35:1) and pencil notes on card are
promoted to `--ink`; the lamp gains a 2px `--rec` ring so it survives as a
shape, not only a colour.

---

## §3 Typography

Two typefaces, inherited exactly, and no third voice. **Oswald** (400, 500,
600) is the machine plate and the typed label: condensed, uppercase,
letterspaced — everything the machine or the label-maker "says". **IBM Plex
Mono** (400, 500, 600) is the document: timecodes, catalogue data,
transcripts, body text, and — set italic in `--pencil` — the archivist's
hand. The pencil hand is a treatment of Plex Mono (italic, pencil token,
−0.4° rotation on its line), never a third font: the archive owns a
typewriter and a label-maker, not a calligraphy set.

| Role | Font | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Display (hero headline) | Oswald 600 | clamp(44px, 7.2vw, 96px) / 0.98 | +0.01em | Uppercase. Stamps in (§6.6 machinery). Never more than 3 lines; the deck is wide, the headline is a plate, not a paragraph. |
| Section heading | Oswald 500 | clamp(26px, 3.4vw, 40px) / 1.05 | +0.02em | Uppercase, preceded by its reel/chapter number in Plex Mono oxide. |
| Box label (story title) | Oswald 500 | 19–22px / 1.1 | +0.015em | The typed label on the box. Two lines maximum; longer titles shorten, never shrink below 17px. |
| Machine label / nav | Oswald 500 | 13px / 1 | +0.14em | Uppercase. Transport keys, meter captions, shelf names. |
| Body / transcript | IBM Plex Mono 400 | 16.5px / 1.65 | 0 | Transcripts set on `--paper` sheets, measure 58–66ch. Mono is the point: transcripts are typed documents. |
| Timecode / counter / data | IBM Plex Mono 600 | 14–20px, tabular | +0.04em | Always tabular figures; a timecode that jiggles its width is a broken counter. Format `MM:SS` under an hour, `H:MM:SS` above. |
| Condition note (pencil) | IBM Plex Mono italic 400 | 14px / 1.5 | 0 | `--pencil`, −0.4° line rotation, always paired with a stamped status chip (§6.10). |
| Caption / catalogue small | IBM Plex Mono 400 | 12.5px / 1.5 | +0.02em | Provenance lines, digitisation credits. Never below 12px anywhere on the page. |

**Type laws.**
1. **Numerals are Plex Mono, always.** Oswald never sets a figure that
   carries data; its numerals are display shapes, and a counter in Oswald
   would be a poster, not a reading.
2. **The machine speaks in caps; the archive speaks in sentence case.**
   Oswald is always uppercase (plates are stamped, not written). Plex Mono
   body and pencil are sentence case — transcripts reproduce the speaker's
   words with ordinary capitalisation, never styled into caps for effect.
3. **A transcript is a document, not a style.** Speaker turns are labelled
   `WHITFIELD:` / `INTERVIEWER:` in Plex Mono 600 small caps treatment
   (uppercase, +0.08em), timestamps in the margin every turn. No pull-quote
   styling inside a transcript; the words are the exhibit.
4. **Type never moves except by machine actions.** The only kinetic type on
   the page is the counter's tumbling digits and the headline's label-stamp
   entrance (§5). Headlines do not float, breathe or drift — plates are
   bolted down.
5. **Line-length discipline.** Transcript measure 58–66ch; catalogue and
   caption text ≤72ch; box labels are objects, so their measure is the box.

---

## §4 Layout language

**The room.** The page is built in horizontal strata, like the machine and
its shelves: the **deck stratum** (bakelite, full-bleed, the hero and any
featured testimony), the **shelf stratum** (a darker wall, `--bakelite` at
full depth with shelf boards implied by hairlines, holding tape-box cards),
and the **paper stratum** (transcript sheets on `--paper`, the only light
surfaces, always presented as physical sheets with a ruled margin and a
punched-hole or clip detail at the top). Strata alternate; a page never has
two paper strata adjacent — sheets live on shelves or on the deck, not in
the air.

**Grid and rhythm.** A 12-column grid, 24px gutters, max content width
1320px, with a strict **8px vertical rhythm** — every plate, box and sheet
height is a multiple of 8, because machines and shelves are built to
modules. Section spacing is 96px desktop / 64px tablet / 48px mobile,
always closed by a splice band or a shelf board line, never by whitespace
alone: in this archive, chapters are joined by visible splices (§6.4) and
shelves end at boards.

**The deck.** The hero deck is a full-bleed bakelite plate, edge to edge,
with a 1px `--plate-line` inner border and four bolt heads (12px discs,
`--plate-line` ring, `--metal-hi` slot) at its corners. Inside: meter bridge
across the top (VU meters left and right, record lamp centred, counter
right), the two reels flanking the headline plate in the middle band, and
the featured testimony's transport strip along the bottom. The deck's
aspect discipline: at ≥1200px the middle band is 520px tall; the reels are
280px diameter, their centres on the headline's baseline axis — the headline
is *between* the reels, threaded like tape through the machine.

**Shelves.** Story boxes sit on shelf boards: each row of boxes rests on a
4px `--plate-line` board with a soft shadow beneath (the only large soft
shadow on the page — shelves have depth, plates do not). Boxes are
`--box-card` rectangles, ratio ~4:3, spine visible on the left edge (an
oxide or khaki spine strip, 10px, carrying the reel number rotated −90°).
Shelf rows hold 4 boxes at ≥1200px, 3 at 768–1199px, and become a single
vertical stack of full-width boxes <768px — a shelf you scroll down, like
walking along it.

**Density rules.** The deck stratum is dense (it is a machine: every square
centimetre works). The shelf stratum is medium (boxes breathe by exactly
one gutter). The paper stratum is the least dense (documents need air and a
margin for the archivist's pencil). Whitespace in this theme is *the dark
of the room*: bakelite emptiness around an object means the object matters;
emptiness is never used inside a box or a sheet, where it would read as a
missing label.

**The diagonal.** One angle governs the whole theme: the splice cut at
**−4°**. Splice bands, the shelf's "recently shelved" ribbon, the
tape-stop transition's wipe and the pencil note's −0.4° (its tenth) all
derive from it. No other diagonals exist; a second angle would be a second
machine.

---

## §5 Full motion system

Every motion term, in this theme's own language. One shared
requestAnimationFrame loop drives all scroll-scrubbed values with a lerp of
**0.12** (transport values) — no scroll handler ever writes styles directly.
Named easings, used throughout §6:

- `--ease-transport`: `cubic-bezier(0.22, 0.9, 0.24, 1)` — capstan engage:
  fast take-up, long mechanical tail.
- `--ease-spool`: `cubic-bezier(0.7, 0, 0.2, 1)` — wind-down and spool-up:
  slow to start leaving, decisive arrival.
- `--ease-stamp`: `cubic-bezier(0.2, 0, 0, 1)` — the label stamp's attack:
  60ms of fall, then contact.
- `--ease-needle`: `cubic-bezier(0.3, 1.4, 0.4, 1)` — CSS fallback only; the
  live needles are a damped spring in the shared loop (stiffness 90,
  damping ratio 0.18), because a needle's overshoot must be physics, not a
  curve pretending.
- `--ease-settle`: `cubic-bezier(0.25, 1, 0.35, 1)` — mechanical settle,
  the ~600ms decay of a real reel.

**Term by term.**

- **Scroll-triggered reveals** — shelf boxes stagger onto their board
  (§6.6), 70ms apart, translateY 14px → 0 with `--ease-transport` 420ms;
  triggered at 85% viewport. Pre-state is JS-armed only; the DOM ships with
  every box on its shelf.
- **Scroll-driven / scrub animation** — the featured testimony's waveform
  draw and playhead (§6.3) are scrubbed 1:1 with scroll through its section;
  reel pack radii scrub with page position (§6.1). Scrubbed values are
  never eased — scrub means the visitor's hand *is* the transport.
- **Parallax** — three depths only: tape-box spines drift at 0.94× scroll,
  shelf boards at 1.0×, the brushed-metal sheen on the deck plate at 1.06×
  (a light effect, not a layer). Waveforms and transcripts never parallax —
  documents stay registered to their sheets.
- **Pinned sections** — the hero deck pins for 60vh of extra scroll while a
  reel fast-forwards (§6.1/§6.2): the counter spins, the packs trade tape,
  then the pin releases. Pinning is abolished <768px and under reduced
  motion — the deck simply sits at the top, complete.
- **Smooth scrolling** — the shared lerp loop *is* the smoothing; native
  scroll position is the target, rendered transport state chases it at
  0.12/frame. Anchor jumps (contents leaf, chapter links) are instant —
  a tape machine does not glide to a chapter, it winds (§6.9 covers the
  wind).
- **Progress indicator** — the tape counter (§6.2) plus the pack ratio of
  the hero reels: position in the archive is a counter reading and a
  visible quantity of tape, never a percentage bar. A thin oxide rule under
  the header plate echoes the same value for visitors who never look at the
  deck — same data object, second printing.
- **Staggered + masked reveals** — chapter headings reveal through the
  diagonal splice mask (§6.4): a −4° `--splice` band sweeps 520ms and the
  heading is uncovered behind it, letters never partially transparent.
- **Kinetic typography** — one instance only: the counter's tumbling digits
  (§6.2) and, at load, a single timecode tumble-and-lock in the featured
  box label (digits cycle 480ms, lock left to right at 60ms intervals).
  Kinetic type anywhere else is refused — plates do not perform.
- **Marquee** — refused as a marquee; admitted as **leader tape**: a slow
  (28s loop, linear) horizontal strip of accession numbers and shelf marks
  between the shelf stratum and the footer, printed on a `--splice`-toned
  band like the leader between recordings. It pauses on hover/focus and is
  cut entirely <768px (the information repeats the catalogue; nothing is
  lost).
- **Counters** — catalogue figures (reels held, hours digitised, narrators)
  count in spinning-digit style (§6.2 machinery) from their printed
  previous-edition values — never from zero, never to a number that is not
  the catalogue's own count, printed adjacent as their source line.
- **SVG line-draw** — every testimony's waveform is an SVG path drawn by
  scroll scrub (featured) or by play (others, §6.8); the draw is a reading,
  and the full path is present underneath at 18% oxide from the start, so
  the undrawn remainder is a fainter print of the same voice, not an
  absence.
- **Image scale-in-frame** — narrator portraits (where the archive holds
  one) sit in the box's window and settle from 1.04 scale to 1.0 over
  600ms `--ease-settle` as the box takes its shelf place — a photograph
  being slid into its sleeve. Portraits never zoom on hover.
- **Hover / micro-interactions** — hover leans a reel 2° toward play and
  sets its needle quivering (§6.5); buttons are transport keys with 2px of
  physical travel (translateY + shadow collapse) on press; links underline
  with a splice-toned rule. **Magnetic hover is refused** — machine keys do
  not lean toward fingers; they wait, then clunk.
- **Custom cursor** — refused. Normal system cursor only, per standing rule.
- **Skeleton loading** — unlabelled boxes (§6.17): blank card rectangles on
  a shelf board, spines unpainted, resolving to labelled boxes within a
  1200ms ceiling.
- **Page transitions** — the tape-stop (§6.9): wind-down blur and settle,
  then the new page spools up.
- **Reduced motion** — a real variant per element in §6; globally: reels
  still at their true pack ratio for the current position, waveforms fully
  drawn, counter reading correct and static, no pin, no jolt, no tumble.
- **Watchdogs** — every JS-armed pre-state carries a named watchdog timer
  (listed per element) that forces the finished state if the loop stalls;
  a single global 3000ms lifeboat clears any remaining pre-state. Content
  is complete in the DOM before any of this runs.

---

## §6 Signature and page-family elements

Eighteen elements: the theme's ten originals (§6.1–§6.10) deepened, plus
eight page-family elements (§6.11–§6.18) the original entry implied but did
not specify. Every element carries the full v1 field set and every v2 layer.
Shared machinery (the rAF loop, lerp 0.12, JS-arming, the 3000ms global
lifeboat) is defined in §5 and referenced, never re-invented, per element.

### §6.1 Velocity-driven reels

**What & why.** The hero deck's two reels — supply (left) and take-up
(right) — rotate at speeds proportional to scroll velocity, with inertia:
scroll fast and tape flies between them; stop, and they settle over ~600ms
with `--ease-settle`. Their pack radii change honestly as the page is read:
the supply pack empties into the take-up pack by area conservation,
`r(p) = √(r_hub² + (1−p)·(r_full² − r_hub²))` for supply and the mirror for
take-up, where `p` is the visitor's true position in the page (0–1),
`r_hub = 30px`, `r_full = 128px` at desktop scale. It belongs because it is
the theme's thesis made physical: scrolling *is* transport, and the
machine keeps honest books about how much tape has passed.

**Structure.** Two inline SVGs (280px diameter at ≥1200px), each: outer
flange (bakelite-2 disc, plate-line ring), three cut-out windows, hub,
and the tape pack as a filled annulus in `--tape` with a 1px `--oxide` rim
on its outer edge whose radius is set per frame from the conservation
formula. Rotation is a single `transform: rotate()` on the flange group;
pack radius is an SVG `r` update on the annulus — no canvas, no images.

**Motion spec.** Angular velocity derives from tape speed:
`v_tape = clamp(|scrollVelocity| × 0.5, 0, 1400) px/s`, and each reel's
`ω = v_tape / r_pack` — so the take-up reel visibly slows as its pack
grows and the supply reel spins faster as it empties, exactly as a real
deck behaves at constant tape speed. Direction: supply rotates
counter-clockwise, take-up clockwise on downward scroll; both reverse on
scroll-up. On scroll stop, velocity decays with `--ease-settle` over
600ms. Idle: a 0.6°/s creep on the take-up reel only (the machine is
powered, §6.7's lamp agrees).

**Choreography timeline (scroll burst, t=0 = first fast scroll event).**
0ms — loop reads velocity, reels begin accelerating (no ramp-in delay;
the capstan is already engaged). 0–120ms — pack radii begin trading at
the scrubbed rate. 120ms — VU needles (§6.5) cross −10 VU. ~600ms after
last scroll event — velocity reaches 0 via settle curve; reels hold
their true pack ratio for the resting position. Idle creep resumes at
t+1400ms of stillness.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (top of page) | Packs at p=0 ratio (supply full, take-up at hub + leader), idle creep on take-up | Same; creep runs (it is ambient, not scroll feedback) |
| Hover (over deck) | Nearest reel leans 2° toward play (rotateZ on plate axis), its needle quivers (§6.5) | No hover; first tap on deck = focus state |
| Focus (deck in tab order region) | No reel change; focus belongs to controls, reels are aria-hidden machinery | Same |
| Active (scrolling) | ω per formula; direction follows scroll sign | Identical — scroll is the input on both |
| Scrolled-past (deck above viewport) | Loop skips reel rendering entirely (offscreen pause); state stays true to p | Same |
| Disabled (JS off / loop dead) | Static SVG at p=0 ratio, fully drawn — the deck is a picture of a machine at rest, and every word below it is readable | Same |

**Content-merge.** The reels are not beside the content; they are the
page's transport. The headline sits between them, the featured story's
duration is the tape they hold (the hero deck is threaded with the
featured testimony — its box label is printed on the deck plate, §6.11),
and p is the visitor's real reading position. Remove the reels and the
page loses its progress, its featured story and its physics at once.

**Failure fallback & watchdog.** If the rAF loop stalls >900ms
(`reel-watchdog`), reels freeze at their last true ratio — a stopped
machine, not a broken page; all text was never dependent on them. If SVG
fails to render, the deck plate, headline and transport strip remain
(plain HTML), and the packs' absence is a cosmetic loss only.

**Reduced motion.** Reels do not rotate. Pack radii are set once, statically,
to the true ratio for the visitor's landing position (anchor or top), and
do not update. The deck reads as a photographed machine.

**Breakpoints.** ≥1200px: 280px reels, full physics. 768–1199px: 200px
reels, headline drops below the reel band (the plate reflows to a stacked
deck), physics unchanged. <768px: 128px reels flanking a shortened plate;
idle creep cut; ω capped at 60% (small reels spinning fast read as toys).

**Edge cases & failure modes.** Very fast flick-scroll on touch: velocity
clamps at 1400px/s so reels never strobo-spin. Scroll-up at p=0: packs
already at origin; ω applies, radii clamp at the formula's ends — tape
never "rewinds past the leader". Content shorter than one viewport: p
stays 0, reels rest full/empty honestly. Tab hidden: loop suspends;
on return, state re-derives from live scroll position (no catch-up spin).

**Accessibility.** Reels are `aria-hidden="true"` decoration-with-physics;
their information (position in page) is duplicated by the counter (§6.2),
which is text. No focusable parts. Motion respects `prefers-reduced-motion`
as above; vestibular note: rotation is the theme's core gesture, so the
reduced variant removes it entirely rather than slowing it.

**Performance & mobile.** Two SVG transform updates + two `r` updates per
frame, <0.3ms/frame budget; rendering skipped while offscreen. Mobile
variant: same SVGs at 128px, creep cut, as above.

**Tokens.** `--bakelite`, `--bakelite-2`, `--plate-line`, `--tape`,
`--oxide` (rim), `--rec` (none — lamp is §6.7), `--ease-settle`,
`--lerp-transport: 0.12`.

### §6.2 The tape counter

**What & why.** A mechanical 0000–9999 counter — four digit drums in a
bezel on the meter bridge — whose reading is the visitor's position in
the archive denominated in tape: `reading = round(p × 9999)`. It is the
page's progress indicator, and it belongs because a tape archive measures
journeys in counter readings ("the good part starts at 0417"), not in
percentages, which are a spreadsheet's unit.

**Structure.** Four drum windows (Plex Mono 600, 20px, tabular), each drum
a vertical strip of digits 0–9 translated in Y; bezel in `--bakelite-2`
with `--plate-line` ring and `--metal-hi` caption `TAPE COUNTER` beneath.
A visually-hidden text twin (`aria-live="off"`, updated on settle) carries
the reading for assistive tech as `Position 0417 of 9999`.

**Motion spec.** Drums chase the target reading through the shared loop:
each drum's Y offset lerps at 0.12 toward its digit, lower drums moving
first, higher drums tumbling only when carried — the mechanical cascade.
During fast scroll the drums blur through digits at up to 24 digit-steps/s
per drum; on settle, the last digit clicks in with a 40ms `--ease-stamp`
overshoot of 1px. At load (home page only), one tumble-and-lock: digits
cycle 480ms and lock left→right at 60ms intervals onto the true reading.

**Choreography timeline (page load).** 0ms — record lamp blinks on
(§6.7). 120ms — drums begin cycling from 0000. 600ms — first drum locks.
660/720/780ms — remaining drums lock; reading = true p (0 at top → 0000;
an anchored arrival locks onto its real reading, never 0000-then-jump).

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Shows true reading, static | Same |
| Hover | None (it is a reading, not a control) | n/a |
| Focus | Not focusable; its text twin is reachable in DOM order after the meter bridge | Same |
| Active (scrolling) | Drums cascade per above | Same |
| Scrolled-past | Counter lives in the sticky header plate too (§6.11) — same data object, second bezel | Same, in the compact header |
| Disabled | Prints the reading as static Plex Mono text `0000 / 9999` at p=0; position info degrades to the oxide rule (§5) | Same |

**Content-merge.** Archivists cite counter readings; the archive honours
that: every story box (§6.6) prints the counter reading at which its
section begins on the home page (`STARTS 0417`), computed from the same p
mapping — the counter is the archive's citation system, not a widget.

**Failure fallback & watchdog.** If drum strips fail, the bezel falls back
to the static text twin (always in the DOM). `counter-watchdog` at
1500ms: if rendered reading ≠ computed reading by >2, snap to truth —
a counter that lies is worse than a counter that jumps.

**Reduced motion.** No tumble, no cascade: the reading prints as static
digits and updates in whole steps when scroll settles (debounced 200ms).

**Breakpoints.** ≥1200px: 20px drums on the bridge and in the header.
768–1199px: 17px drums, bridge only; header carries the text twin styled
as a reading. <768px: drums cut from the bridge; the header shows the
compact reading `0417 / 9999` in 14px Plex Mono — the citation system
survives, the machinery shrinks.

**Edge cases.** Anchor arrival mid-page: first lock is the true reading
(see timeline). Extremely long pages: p mapping is linear across the full
document; readings near 9999 occur only in the footer stratum, as they
should. Print: the counter prints its text twin.

**Accessibility.** `role="img"` on the drum assembly with `aria-label`
from the text twin; the twin updates at most once per settle (never a
live-region chatter). Contrast: digits are `--box-card` on `--bakelite`
10.46:1 ✓.

**Performance & mobile.** Four transform updates/frame worst case,
<0.15ms; drums are the only animated text on the page. Mobile: text-twin
form only (above).

**Tokens.** `--bakelite-2`, `--plate-line`, `--box-card`, `--metal-hi`,
`--ease-stamp`, `--lerp-transport: 0.12`.

### §6.3 Scrubbed waveform playhead

**What & why.** The featured testimony's waveform — an SVG path generated
from the recording's real amplitude data — draws left to right in exact
scroll sync as the visitor scrolls through its section, a playhead line
travelling with them, the transcript beneath highlighting in step. It is
the archive's central courtesy mechanised: you read a voice at your own
speed, and the machine keeps your place in the sound as faithfully as in
the text. It belongs because every other element is furniture; this one is
the act of listening itself.

**Structure.** A section ~180vh tall (desktop) containing a sticky stage:
waveform SVG (100% × 120px, path pre-rendered from the testimony's peak
data, ~600 points decimated to the section's pixel width), a 2px playhead
rule in `--oxide` with a small triangular head, the current timecode
(`MM:SS / TOTAL`) in Plex Mono, and the transcript sheet (§6.13) below,
its turns carrying `data-t` start times. The full path is printed
underneath at 18% `--oxide` from the start; the "drawn" pass overprints
it at full strength with a clip rect whose width is the scrub value.

**Motion spec.** Scrub is 1:1 and un-eased: `progress = clamp((scrollY −
sectionTop) / (sectionHeight − viewportHeight))`, mapped linearly onto
the testimony's real duration (printed on its box; e.g. 47:12 = 2832s —
the mapping uses the data attribute, never a hardcoded number). Playhead
timecode = progress × duration, formatted per §3. Transcript turns whose
`data-t` ≤ playhead time are `played` (ink at full strength, a khaki
margin tick appears); the current turn carries an oxide margin rule.
Scroll-up reverses everything exactly — tape rewinds, ticks withdraw.

**Choreography timeline (entering the section).** Stage sticks at
viewport centre. First 10% of scrub: playhead leaves the leader (the
path's first 2% is flat leader tape, printed as such — silence before a
voice is part of the recording). 10–90%: voice. Final 5%: run-out —
waveform decays, timecode reaches the printed total exactly as the stage
unsticks. No beat is decorative; the timeline *is* the recording's shape.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (before section) | Full path at 18%, playhead at 0, transcript unmarked, all readable | Same |
| Hover (on waveform) | A ghost playhead shows the timecode at the hovered point (`title` in the margin readout) — inspection without commitment | No hover; tap on waveform jumps scroll to that point of the section (the scrub is the control) |
| Focus (section via keyboard) | Transcript turns are focusable in order; the playhead follows focus (scroll-into-view drives the same scrub) | Same |
| Active (scrubbing) | Per motion spec; timecode updates each frame | Same |
| Scrolled-past | Stage unstuck; a compact "played" state remains: path full strength, final timecode printed, transcript ticks persist | Same |
| Disabled | Full path at full strength, transcript complete and unmarked — a printed waveform above a printed transcript | Same |

**Content-merge.** The waveform is the story; the transcript is the same
story in words; the playhead binds them. The section exists for this one
testimony (its box, its condition note, its narrator's name plate are all
on the stage) — remove the story and there is nothing left to specify.

**Failure fallback & watchdog.** If the peak data fails to load, the path
is replaced by a printed flat leader line and a pencil note — *"Waveform
not yet drawn for this reel; the words are complete."* — and the
transcript stands alone, which it always could. `scrub-watchdog` 1200ms:
if the clip width has not matched scroll position after a jump
(anchor arrival), snap to truth.

**Reduced motion.** No scrub: the stage does not stick, the path prints
full-strength, the transcript prints complete with all ticks shown as a
static "heard in full" state available via a plain toggle button
("Mark as read" — a real button, keyboard-operable, that sets the same
played state without motion).

**Breakpoints.** ≥1200px: 180vh scrub length, waveform 120px tall.
768–1199px: 150vh, waveform 96px. <768px: scrub length 130vh, waveform
72px, timecode moves above the path (margin is too narrow beside it);
transcript measure full width.

**Edge cases & failure modes.** Testimony with no transcript (some reels
are music or ambient sound): the stage scrubs the waveform alone and the
sheet is replaced by the archivist's listening notes — the element
degrades to sound + notes, never to an empty sheet. Very short testimony
(<60s): scrub length floors at 120vh so the gesture still has room.
Browser find-in-page jumping mid-section: watchdog snaps the playhead.

**Accessibility.** The waveform is `role="img"`, `aria-label="Waveform of
Reel 014, 47 minutes 12 seconds"`; the timecode readout is text, updated
on settle (not per frame) for screen readers; transcript turns are plain
text in reading order — the scrub adds ticks, never gates words. Playhead
oxide on bakelite is a graphic (3.55:1, ≥3:1 for graphics ✓).

**Performance & mobile.** One clip-rect width + one transform per frame
(<0.2ms); path data ≤40KB inline for the featured testimony only — all
other waveforms on the page are static prints until played (§6.8). Mobile
variant per breakpoints; the sticky stage uses `position: sticky`, no JS
pinning.

**Tokens.** `--oxide`, `--bakelite`, `--paper`, `--ink`, `--khaki`
(ticks), `--plate-line`, `--lerp-transport: 0.12` (readout smoothing
only — the scrub itself is un-eased).

### §6.4 Diagonal splice chapters

**What & why.** Chapter changes are physical edits: a translucent splice
band at the theme's −4° crosses the layout, and the new chapter is
uncovered behind its sweep. Chapters are joined, not linked — the band is
the visible joint between two pieces of tape, printed with the chapter's
number and the counter reading at the join. It belongs because an archive
of edited testimony should show its edits; a seamless page would pretend
these voices were recorded in one breath.

**Structure.** A full-bleed band, height 54px, `--splice` at 55% opacity
with 1px `--plate-line` edges, rotated −4° around its centre, extending
12px beyond both viewport edges so the cut never shows a blunt end. On it,
left-aligned: chapter number and title in Oswald on a small bakelite chip
(the band itself carries no text directly — §2 forbids text on splice).
Beneath the band, the chapter heading it introduces.

**Motion spec.** As the band's trigger line crosses 70% viewport height,
the band sweeps in from the left over 520ms `--ease-transport` (translateX
−30px → 0, opacity 0 → 1 — it is *laid down*, not faded from nothing: the
first frame is already 40% opaque so the band never ghosts), and the
chapter heading beneath is uncovered by a matching −4° clip-path wipe,
560ms, completing 40ms after the band lands. Scroll-up: no reverse
animation; the band is a fact of the page once laid.

**Choreography timeline.** t=0 trigger — band starts its lay-down.
120ms — band at full opacity, still travelling. 520ms — band lands;
heading wipe begins (it started at 480ms, overlapped by design so the eye
reads one gesture). 1040ms — heading fully uncovered; the band's chip
stamps its counter reading (60ms `--ease-stamp`).

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (unreached) | Band and heading fully present (DOM state) — JS-arming hides nothing in the shipped DOM | Same |
| Hover | None | n/a |
| Focus (heading via anchor) | Band present; anchor arrival never replays the sweep | Same |
| Active (sweeping) | Per timeline | Same |
| Scrolled-past | Static band, reading stamped | Same |
| Disabled | Static band and heading — the joint is printed, not performed | Same |

**Content-merge.** The band carries the chapter's real metadata (number,
title, counter reading at the join) and sits exactly at the editorial
join it represents — between the two chapters it splices. It is the
table of contents, drawn on the page at the points of use.

**Failure fallback & watchdog.** The sweep is a transform on an already
visible band; if the animation never runs, `splice-watchdog` (900ms
after trigger) forces the end state. The heading's clip-path is JS-armed
only; no-JS prints headings uncovered.

**Reduced motion.** No sweep, no wipe: band and heading static, reading
printed. The joint remains legible as a printed band.

**Breakpoints.** ≥1200px: 54px band, −4°. 768–1199px: 46px, −4°.
<768px: 38px, angle softens to −2.5° (a full −4° across 360px of width
eats 25px of vertical room the small page cannot spare); chip text
shortens to chapter number only, title lives in the heading alone.

**Edge cases.** Two chapters within one viewport (short chapters): the
second band's trigger defers until the first sweep completes — splices
never overlap mid-gesture. Chapter at the very top (Chapter 1): no band;
the deck itself is the first joint (the leader).

**Accessibility.** The band is decorative (`aria-hidden`); the heading is
a real `<h2>` in document order; the counter reading on the chip is
duplicated in the heading's visually-hidden suffix for screen readers.

**Performance & mobile.** One transform + one clip-path per sweep,
<0.1ms/frame, only while sweeping. Mobile: per breakpoints.

**Tokens.** `--splice`, `--plate-line`, `--bakelite` (chip), `--box-card`
(chip text), `--ease-transport`, `--ease-stamp`.

---

### §6.5 VU needles

**What & why.** Twin VU meters on the meter bridge — cream faces, oxide
red zone, black needles — whose needles bounce with scroll velocity and
tremble at idle, settling with real needle physics: overshoot and damped
oscillation. They belong because they are the room's proof of power: the
deck is on, it is listening, and the levels of the archive rise when the
visitor handles the machine. A dead meter would make the whole deck a
photograph.

**Structure.** Two SVG meter faces (118×84px desktop), each: face in
`--box-card`, graticule arc (−20…+3 VU) in `--ink`, red zone in `--oxide`,
needle as a 1.5px line from a hub pivot, `L` / `R` captions in Oswald
beneath. Needle angle range −38° (rest, −20 VU) to +34° (+3 VU). The two
needles are driven by the same signal with a 6% phase difference — a
stereo pair listening to one mono archive, never perfectly in step,
because no two real needles are.

**Motion spec.** Needle dynamics are a damped spring in the shared loop:
target angle maps from scroll velocity (`v=0 → −20 VU rest with tremble`;
`v=1400px/s → +1 VU`), stiffness 90, damping ratio 0.18 — a fast scroll
flicks the needle into the red with two visible overshoots before settle
(~700ms). Idle tremble: ±0.7° at ~7Hz, amplitude modulated by a slow
0.1Hz wander, so the tremble never looks looped. While the featured
testimony's section (§6.3) is centred, the target instead follows the
waveform's local amplitude at the playhead — the meters read the voice
when a voice is playing, and read the room (scroll) when it is not. That
priority is absolute and stated on the bridge caption: `METERS: TAPE /
ROOM`.

**Choreography timeline (page load).** 0ms — needles at rest pin.
200ms — lamp on (§6.7); needles lift to the tremble band. 480ms — one
calibration swing to 0 VU and back (a meter being switched on checks
itself), 380ms `--ease-needle` fallback curve, spring in the loop.
900ms — tremble only. The calibration swing happens once per session,
never on later pages.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (idle) | Tremble band ±0.7° | Same |
| Hover (over a reel) | That side's needle quivers: tremble amplitude ×2.2, band centre +3 VU — the machine anticipates play | No hover state |
| Focus | Meters are not focusable; no change | Same |
| Active (scrolling / playing) | Spring response per spec; playing overrides scroll | Same |
| Scrolled-past (bridge offscreen) | Loop skips meter updates; needles freeze at last true angle | Same |
| Disabled | Needles printed at −7 VU (a machine at rest with signal history), faces fully drawn | Same |

**Content-merge.** The meters read real signals only: scroll velocity
(the visitor's handling) or the featured voice's actual amplitude at the
playhead. They are instruments, not decoration — §9 lists a meter that
moves without a signal as a firing offence.

**Failure fallback & watchdog.** Spring integration is clamped: if a
frame's dt exceeds 50ms (jank, tab switch), the step is subdivided so the
needle can never teleport or NaN. `needle-watchdog`: if the loop dies,
needles hold their last angle — a held needle is honest; a spinning one
is not.

**Reduced motion.** Needles printed at the tremble band's centre and
still; during play they step between 1-second amplitude averages
(discrete updates, no sweep). The calibration swing is cut.

**Breakpoints.** ≥1200px: 118×84px faces on the bridge. 768–1199px:
96×68px. <768px: one meter only (L), 84×60px, right meter cut — the
bridge keeps lamp + counter as its non-negotiables (§6.2, §6.7).

**Edge cases.** Sustained maximum scroll: needle pins at +2 VU, never
past the +3 stop — the stop is physical in the mapping, not a clamp
applied after. Amplitude data missing for a playing testimony: meters
fall back to ROOM mode and the caption says so.

**Accessibility.** `aria-hidden` instruments; their state is never the
only carrier of anything (playing state is announced by the record lamp's
text twin, §6.7). Faces meet graphic contrast: ink graticule on card
9.57:1 ✓, oxide red zone on card is a graphic zone boundary, not text.

**Performance & mobile.** Two spring integrations + two transforms per
frame <0.1ms; skipped offscreen. Mobile: single meter (above).

**Tokens.** `--box-card`, `--ink`, `--oxide`, `--bakelite-2`,
`--plate-line`, `--ease-needle` (fallback only).

### §6.6 Stamped box labels (story cards)

**What & why.** Every story is a tape box on a shelf: a `--box-card`
rectangle with a spine strip, a typed label (narrator, title, year), a
catalogue number, a duration, and — §6.10 — its pencil condition note.
On arrival the boxes stagger onto their shelf board and each headline
stamps in like a typed label: letters landing with slight weight
variation, the way a label-maker embosses unevenly. It belongs because
the catalogue is hand-kept: every story is an object with a history, and
the card is the object, not a tile about the object.

**Structure.** `<article>` per story: spine strip (10px, oxide or khaki
alternating by shelf, reel number rotated −90° in Plex Mono 11px), label
block (Oswald title, Plex Mono narrator + year line), window (portrait
SVG/photo if held, else a printed reel glyph — never a stock image),
data row (duration, catalogue №, `STARTS nnnn` on listing contexts),
condition note (§6.10) along the bottom edge. Whole card is one link to
the story page (§6.13 context), with the title as the link text.

**Motion spec.** Shelf entry: boxes translateY 14px → 0, opacity
0→1, 420ms `--ease-transport`, staggered 70ms in reading order, triggered
at 85% viewport, once. The stamp: the title's letters are spans; each
lands with scale 1.06→1 and a 1px y-drop, 90ms `--ease-stamp`, staggered
18ms per letter, with per-letter opacity jitter drawn from a seeded
sequence (letters land at 82–100% ink — embossing is uneven, and the
seed is fixed per box so the label is identical on every visit: a label
does not re-type itself differently each morning). Portrait settles
1.04→1 scale over 600ms `--ease-settle` (§5).

**Choreography timeline (shelf row entering).** t=0 first box crosses
85%: box 1 rises. +70ms box 2 … row of 4 fully placed by ~700ms. Title
stamps begin 120ms after their box lands; a 12-letter title completes
its stamp by ~420ms after landing. The shelf is fully quiet by ~1.2s —
shelves settle, then stay settled.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Box on board, label stamped, portrait settled | Same |
| Hover | Box lifts 3px, board shadow deepens, spine brightens one step (oxide spine → full oxide); title does NOT re-stamp | No hover; touch-down gives the lift for 120ms |
| Focus | 2px oxide outline offset 3px (the only outline style in the theme), board shadow as hover | Same |
| Active (pressed) | The clunk (§6.8): half-frame jolt, then navigation | Same |
| Scrolled-past | Static; entry never replays on scroll-up | Same |
| Disabled | Boxes printed on the board in order, labels at full ink | Same |

**Content-merge.** The card's every field is catalogue data: reel №,
catalogue №, duration, year, condition. The stagger order is the shelf
order is the catalogue order. Nothing on the card is decorative except
the board shadow, which is the shelf's.

**Failure fallback & watchdog.** Entry pre-states are JS-armed only;
`shelf-watchdog` 1000ms after trigger forces any unlanded box to its
rest state. A missing portrait falls back to the printed reel glyph
in the window — the box exists whether or not the archive holds a face.

**Reduced motion.** No stagger, no stamp: boxes present, labels at full
ink (the seeded jitter is a print quality and remains — it is not
motion), portraits at scale 1.

**Breakpoints.** ≥1200px: 4 per row, box ~296×222px. 768–1199px: 3 per
row. <768px: full-width boxes stacked, spine becomes a top strip (a box
lying flat), title 19px, window 64px square at right.

**Edge cases.** Very long narrator names: the label shortens the
*narrator line* (middle-ellipsis in the data, not CSS clipping) — a
label-maker runs out of tape, it does not shrink its type. A story with
no year: the label prints `YEAR NOT RECORDED` in khaki — absence is
catalogued, never silently blank. Shelves with 1–3 boxes: the row is
left-aligned on its board; boxes never stretch to fill a shelf.

**Accessibility.** One link per card (the whole card), title as link
name, data row as plain text after it in DOM order; condition chip
(§6.10) is text. Focus outline per state matrix. Card text: ink on
card 9.57:1 ✓; khaki year-absent line is ≥14px bold-equivalent (Plex
Mono 500) per §2's khaki ruling and is never the only signal (the field
label `YEAR` precedes it).

**Performance & mobile.** Entry animates transform/opacity only; letter
spans capped (titles >28 chars stamp as whole-word units instead — the
label-maker embosses words when the line is long). Mobile: stack layout
above; stamp stagger halves to 35ms between boxes.

**Tokens.** `--box-card`, `--ink`, `--oxide`, `--khaki`, `--pencil`,
`--plate-line`, `--ease-transport`, `--ease-stamp`, `--ease-settle`.

### §6.7 Record light

**What & why.** A small amber lamp — 12px disc in a bakelite bezel on the
meter bridge — that blinks on at load and pulses softly while the
featured story "plays" (its section centred, §6.3) or a real recording
plays (§6.8). Somebody is being recorded; presence is signalled the
studio way. It is the theme's only use of `--rec`, and its scarcity is
the meaning: one lamp, one truth — *a recording is happening now*.

**Structure.** Disc + bezel (HTML/CSS, no SVG needed), with a text twin
in the bridge: `● REC` in Plex Mono 11px, `--rec` when lit, `--metal-hi`
when dark, reading `STANDBY` when dark. The twin is the accessible form;
the lamp is its light.

**Motion spec.** Load: lamp strikes at t=200ms (after the needles lift,
§6.5) — a single 90ms fade-in, then steady. Playing: a breathing pulse,
opacity 1→0.55→1 over 2400ms, sine-shaped, only while playing is true.
Not playing: lamp dark (12% `--rec` print — the bulb is visible, unlit).
The lamp never blinks at attention-seeking rates; 2400ms is a breath,
not an alarm.

**Choreography timeline.** Load: 0ms dark → 200ms strike → steady
standby (the archive is ready, not recording) → lamp lights fully when
the featured section centres or a play is pressed → pulse for the
duration of play → on pause/stop, one 300ms fade to dark. Page leave
via §6.9: lamp dies in the first 100ms of the wind-down — the session
ends before the tape stops.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (standby) | Lamp dark-print, twin reads `STANDBY` | Same |
| Hover | None — a lamp is not a control | n/a |
| Focus | Not focusable | Same |
| Active (playing) | Lit + 2400ms pulse, twin reads `REC ● <story reel №>` | Same |
| Scrolled-past (playing section left) | If play was scrub-driven, lamp returns to standby when the section leaves centre; if a §6.8 playback is running, lamp stays lit (the recording outlives the scroll) | Same |
| Disabled | Lamp printed dark, twin `STANDBY` as static text | Same |

**Content-merge.** The lamp's state is bound to the archive's real play
state — the same boolean the meters (§6.5) and the waveform (§6.8) read.
It is never lit for ambience, never lit in the footer, never lit twice.

**Failure fallback & watchdog.** If the play-state source fails, the
lamp defaults dark: a lamp that cannot know must not claim to record.
`lamp-watchdog` reconciles lamp vs. play state every 2000ms.

**Reduced motion.** Lamp lights and darkens in whole steps; the pulse
becomes a steady lit state (a steady lamp is the reduced-motion dialect
of the same sentence).

**Breakpoints.** All sizes: lamp + twin stay on the bridge; <768px the
twin shortens to `REC` / `—`. The lamp is never cut — it is 12px and it
is the theme's signature.

**Edge cases.** Two play sources at once is impossible by construction
(one shared play state; starting §6.8 playback pauses the scrub's claim).
Autoplay is never attempted: the lamp only lights from a visitor's
gesture or the centred-section rule, and no audio ever starts unasked.

**Accessibility.** The lamp itself is `aria-hidden`; the twin text is
the announcement, updated on state change only (polite live region,
state changes are rare and meaningful). `--rec` on bakelite 9.03:1 ✓;
the dark twin `--metal-hi` 5.35:1 ✓.

**Performance & mobile.** One opacity animation; negligible. Mobile:
unchanged (above).

**Tokens.** `--rec`, `--bakelite`, `--bakelite-2`, `--metal-hi`.

### §6.8 Clunk-and-jolt click (story playback)

**What & why.** Playing a story is a mechanical commitment. Pressing a
story card's play key (or the card itself outside listing pages) lands
with a deep mechanical clunk: the card jolts a half-frame, its reel glyph
spins up, the lamp lights (§6.7), and its waveform begins drawing as the
audio plays. The machine engages — playback in this archive is an act
with weight, because pressing play on a person's testimony should feel
like something was set in motion, not like a link was followed.

**Structure.** Each story card and the featured stage carry a real
`<button class="transport-key play">` (44×44px minimum, bakelite-2 key
with a stamped ▶ in `--box-card`). Playback state lives in one shared
controller (the same play state §6.5/§6.7 read). The card's waveform
strip (a 36px-tall print of the story's path) sits under its data row;
on play it draws via the §6.3 clip technique at the audio's real
currentTime — the draw is the playback position, not an animation
approximating it.

**Motion spec.** Press: key travels 2px (80ms `--ease-stamp`), card
jolts translateY +1px then −0.5px settle (total 140ms — a half-frame
shudder, felt more than seen). Reel glyph spin-up: 0→full speed over
900ms `--ease-spool`. Waveform draw tracks `audio.currentTime` through
the shared loop. Pause: spin-down 600ms `--ease-settle`, draw holds.
End of tape: a printed `END OF REEL n` line appears under the strip and
the key becomes REWIND (⤺), which returns the draw to 0 over 1200ms
`--ease-spool` — rewinding takes time in this archive, though the audio
seeks instantly only after the rewind gesture completes or is skipped
by a second press.

**Choreography timeline (press play).** 0ms key travel + clunk jolt.
90ms lamp strikes (§6.7). 120ms meters switch to TAPE (§6.5). 200ms
audio starts (post-gesture, permitted). 900ms reel glyph at speed.
Draw proceeds with the voice. Pause reverses the order in 600ms.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Key at full height, waveform strip at 18% print, draw at 0 or at remembered position | Same |
| Hover (key) | Key brightens one plate step (`--bakelite-2` → #2B2B26), glyph needle quivers | n/a |
| Focus | Oxide outline (theme standard); pressing Space/Enter = the clunk, identical | Same |
| Active (playing) | Key shows ❚❚ (pause), lamp lit, draw advancing, meters on TAPE | Same |
| Scrolled-past (playing, card offscreen) | Playback continues; the header's compact transport (§6.11) mirrors the key so the commitment is never orphaned | Same |
| Disabled (no JS / no audio support) | The button is replaced by a native `<audio controls>` element under the strip — the story plays, the theatre steps aside | Same |

**Content-merge.** The clunk is not feedback theatre pasted onto a link:
it is the archive's transport engaging with this story's tape. The draw
is the story's real waveform at its real position; the reel glyph is the
story's own reel number made kinetic.

**Failure fallback & watchdog.** Audio load failure: the key returns to
rest, a pencil note appears under the strip — *"This reel would not play.
The transcript is complete below."* — and the transcript (§6.13) is
offered, because the words outrank the sound (§1, second law).
`play-watchdog`: if `currentTime` stalls >3000ms while state=playing,
the controller drops to pause and the note explains.

**Reduced motion.** No jolt, no spin-up: the key changes state, the draw
steps in 1-second increments, the lamp lights steady (§6.7 variant).
The commitment is communicated by state, not by shudder.

**Breakpoints.** ≥1200px and 768–1199px: identical transport; strip
36px. <768px: key grows to 48px (touch), strip 28px, rewind gesture
unchanged; the header mirror (§6.11) is the primary control on small
screens once the card scrolls away.

**Edge cases.** Pressing a second story mid-play: the first tape stops
(§6.9's grammar in miniature — 300ms wind-down of its draw state,
remembered), then the new clunk. Only one tape ever plays; the lamp's
one-truth rule (§6.7) enforces it. Remembered positions persist per
story for the session (sessionStorage), printed on the card as
`RESUME 12:40` in khaki when present.

**Accessibility.** Real button, `aria-label="Play Reel 014, Whitfield,
47 minutes"` / `aria-pressed` state via `aria-label` swap to Pause;
playback state announced through the lamp twin (§6.7). The jolt is
transform-only on the card, never on focus outline. Keyboard: the whole
transport is three keys (play/pause, rewind, transcript jump) in tab
order after the card's link.

**Performance & mobile.** Draw = one clip width per frame while playing
only; spin = one transform. Audio is streamed, never preloaded beyond
`metadata`. Mobile: per breakpoints; audio element identical.

**Tokens.** `--bakelite-2`, `--box-card`, `--oxide`, `--khaki`, `--rec`,
`--pencil`, `--ease-stamp`, `--ease-spool`, `--ease-settle`.

### §6.9 Tape-stop transition

**What & why.** Leaving a story feels like stopping its tape. On
navigation, the current page winds down: reels decelerate, content gains
a directional motion blur and settles, the lamp dies — then the new page
spools up: its deck already turning at low speed, counter tumbling to
its reading. Transport is the navigation grammar; the visitor never
teleports inside an archive, they stop one tape and thread another.

**Structure.** A transition layer over the app shell (the header plate
§6.11 persists across the transition — the machine's frame does not get
replaced, only its tape). Implemented as a view-transition with theme
overrides where supported, with a class-driven fallback: `.tape-leaving`
on the outgoing page root, `.tape-entering` on the incoming.

**Motion spec.** Leave: 460ms total — lamp dies 0–100ms; reels and any
playing draw wind down with `--ease-spool`; page content blurs
(blur 0→3px + translateY +6px, the pitch-drop smear) 120–380ms; counter
drums release and spin free briefly. Enter: new page arrives at 90%
assembled — reels at creep, counter tumbles to reading (480ms, §6.2),
splice band of the first chapter lays down; full rest by 700ms. Total
perceived transition ≤900ms; beyond that the archive is dawdling and
the spec forbids it.

**Choreography timeline.** t=0 navigation committed → lamp dies (100ms)
→ wind-down blur (120–380ms) → swap at 460ms (content already readable
in its static state beneath the entering layer) → spool-up (460–820ms)
→ rest, counter locked, by 900ms.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | n/a (transition is an event) | Same |
| Hover/Focus | Unchanged — transition triggers on activation only | Same |
| Active (leaving) | Per timeline; interactions on the leaving page are dead after t=0 | Same |
| Active (entering) | Incoming page is scrollable from swap; scrub states initialise to truth | Same |
| Scrolled-past | n/a | n/a |
| Disabled (no JS) | Plain navigation, instant — pages are complete documents | Same |

**Content-merge.** The transition carries state truthfully: if a tape
was playing, it audibly winds down (playback stops with a 300ms
pitch-fade where the platform allows, else a clean stop) — the new page
never inherits a phantom playing state, and the lamp (§6.7) agrees on
both sides of the swap.

**Failure fallback & watchdog.** `transition-watchdog` 1100ms: if the
entering animation has not completed, all transition classes are
stripped and the new page stands in its static finished state. A failed
transition must never strand a visitor between pages — the fallback is
the ordinary web, instantly.

**Reduced motion.** No blur, no wind: a 120ms splice-toned crossfade of
the header plate only, content swaps instantly. The grammar survives as
a cut — which is also an edit, and this archive respects cuts.

**Breakpoints.** Identical at all sizes except <768px: blur radius
caps at 2px (small screens smear illegibly at 3px) and the counter
tumble shortens to 320ms.

**Edge cases.** Back/forward navigation: the transition runs in
reverse grammar (spool-up first is impossible — history arrives as a
cut with a 200ms spool settle; the spec accepts the asymmetry rather
than faking symmetry). Same-page anchor navigation never triggers the
tape-stop; it uses §6.4's splice or instant jump. Prefetch: pages may
prefetch, transitions may not pre-run.

**Accessibility.** The transition is visual only; focus moves to the
new page's `<h1>` at swap (standard SPA practice), route changes are
announced by the page title. No content is unreachable during the
transition — the leaving page's content is replaced, not hidden behind
an overlay that traps focus.

**Performance & mobile.** Blur is the only expensive paint; it is
limited to the leaving root, 260ms of it, and cut entirely on
`prefers-reduced-data` or when the device reports ≤2GB RAM (UA-CH /
manual flag) — those visitors get the crossfade dialect.

**Tokens.** `--splice`, `--rec`, `--bakelite`, `--ease-spool`,
`--ease-transport`.

---

### §6.10 Condition notes

**What & why.** Every recording's card and story page lists its physical
condition in the archivist's pencil hand — *"Reel 6: vinegar syndrome,
digitised 2019, handle with care"* — beside a stamped status chip. The
archive admits its own decay. It belongs because provenance is the
difference between an archive and a playlist: a story that has survived
vinegar syndrome, a flood, or forty years in an attic carries that
survival as part of its meaning, and the visitor handles it differently
for knowing.

**Structure.** On the card: bottom edge, pencil line (Plex Mono italic,
`--pencil`, −0.4°) + a stamped chip (Oswald 10.5px, `--ink` on card,
1px ink border, 1.5° rotation the other way — stamps and pencil disagree
in angle because different hands made them). Chip vocabulary is closed:
`SOUND`, `FAIR`, `FRAGILE`, `HANDLE WITH CARE`, `AWAITING DIGITISATION`.
On the story page the note expands to the full condition record:
medium, generation, known damage, digitisation date and engineer,
restrictions. The chip and the note are generated from the same record
field — they can never disagree.

**Motion spec.** Essentially a print element — and that restraint is the
spec. The note has one motion: when its card lands on the shelf (§6.6),
the pencil line "finishes being written": a clip wipe left→right over
380ms ending 100ms after the box lands, as if the archivist signed the
card as it was shelved. The chip stamps with the title's stamp beat
(§6.6). Nothing else ever moves; pencil does not perform.

**Choreography timeline.** Box lands (t=0 per §6.6) → chip stamps at
t+60ms → pencil wipe runs t+100→480ms → card quiet.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Note and chip printed in full (DOM state) | Same |
| Hover (card) | Note unchanged; never highlighted, never tooltip'd — the pencil is not a UI control | n/a |
| Focus | Note is plain text in the card's reading order, after the data row | Same |
| Active | Unchanged during the clunk (§6.8) | Same |
| Scrolled-past | Printed | Same |
| Disabled | Printed — the note predates the machinery and survives it | Same |

**Content-merge.** The note is catalogue data with a field, a controlled
vocabulary and a source (the digitisation log) — it sits on the object
it describes, in the hand of the person who handled it. It is the
anti-slop detail the original entry named, promoted to a system: every
reel, no exceptions, including the honest `CONDITION NOT YET ASSESSED`
for new accessions (printed in khaki, chip `UNASSESSED`).

**Failure fallback & watchdog.** None needed and none permitted: the note
is static text in the DOM. If the condition record is missing, the
fallback is the printed absence above — never a blank space, never a
borrowed note from another reel.

**Reduced motion.** The pencil wipe is cut; note and chip print whole.

**Breakpoints.** All sizes: note stays on the card's bottom edge.
<768px: the note wraps to two lines max, then the card grows — boxes
make room for their pencil, the pencil never truncates. An ellipsis on
a condition note is a lie by omission about a fragile object.

**Edge cases.** Long damage histories: the card prints the first
condition sentence + `FULL RECORD ON THE REEL PAGE →` as part of the
note (a data decision, not a CSS clamp). Restricted recordings (family
restrictions, cultural protocols): chip `RESTRICTED` in oxide-stamped
ink, note states the restriction plainly; the play key (§6.8) is
replaced by the restriction text and a contact line — the archive's
refusals are also printed, never hidden behind a dead button.

**Accessibility.** Note text ink-adjacent contrast handled per §2:
pencil on card 4.39:1 at 14px is paired with the chip (ink, 9.57:1)
carrying the status word, so meaning never rides on the pencil alone.
The note is real text, screen-reader available in card order.

**Performance & mobile.** One clip wipe per card entry; zero ongoing
cost. Mobile: per breakpoints.

**Tokens.** `--pencil`, `--ink`, `--box-card`, `--khaki` (unassessed),
`--oxide` (restricted stamp), `--ease-transport` (wipe).

### §6.11 Deck-plate navigation (header & transport bar)

**What & why.** The site's header is a strip of the machine itself: a
bakelite-2 plate carrying the archive's wordmark as a stamped plate,
catalogue links set as machine labels, the compact counter (§6.2), the
record lamp twin (§6.7), and — once any story is playing — a compact
transport mirror (play/pause + reel № + timecode). It belongs because
in an archive built as one machine, the wayfinding cannot switch
dialects at the top of the page; you navigate the machine by its plate.

**Structure.** Sticky plate, 56px tall, `--bakelite-2`, bottom hairline
`--plate-line`, four bolt heads at its corners (shared with §4's deck
grammar). Left: wordmark plate (Oswald 600, 17px, `--box-card`, stamped
in a recessed rectangle). Centre/left: nav links (Oswald 500 13px,
+0.14em): `THE SHELVES`, `REELS`, `NARRATORS`, `LEND A REEL`, `ABOUT
THE ARCHIVE` — the archive's own nouns, never "Home / Products / Blog".
Right: counter (compact form), lamp twin, and the transport mirror
slot (empty, zero-width when nothing plays — the plate does not reserve
a grave for a control that isn't there).

**Motion spec.** The plate itself is bolted: it never slides, shrinks
or hides on scroll (a machine's plate does not duck). Its motions are
its instruments': counter drums (§6.2), lamp (§6.7), and the transport
mirror's arrival — when playback starts, the mirror spools in from the
right over 380ms `--ease-transport` (width + opacity), pushing nothing:
the nav compresses its tracking by 0.02em to make room, a plate
adjusting, not a layout jumping. Link hover: a splice-toned underline
rule draws 160ms; active section: the link's label gains an oxide
leader dot before it (the chapter you are in is the reel on the deck).

**Choreography timeline (playback starts).** 0ms clunk (§6.8) → 90ms
lamp twin lights here too (same state) → 150ms mirror begins spool-in →
530ms mirror seated, timecode live. Playback ends: mirror holds 1200ms
(the visitor may resume), then spools out 300ms.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Plate static, counter live, mirror absent | Plate static; nav collapses (below) |
| Hover (link) | Splice rule draws; wordmark plate brightens one step | n/a |
| Focus | Oxide outline on the focused link/key; plate never moves | Same |
| Active (playing) | Mirror present and live; counter continues (it measures the page, not the tape — both readings coexist, labelled) | Mirror becomes the primary transport (card keys scroll away) |
| Scrolled-past | The plate IS the scrolled-past state of the deck: it persists | Same |
| Disabled | Static plate, links as plain anchors, counter as text twin, mirror absent (native audio controls live on cards, §6.8) | Same |

**Content-merge.** The plate's instruments are the page's instruments —
same counter object, same lamp state, same play controller (§6.2/§6.7/
§6.8). The header is not a chrome layer over the archive; it is the
archive's control surface, and its links are the shelf names the visitor
is already learning.

**Failure fallback & watchdog.** Sticky failure (old browser) degrades
to a static plate at the top — navigation intact. `plate-watchdog`:
mirror state reconciles with the play controller every 2000ms (shared
with §6.7's lamp check).

**Reduced motion.** Mirror appears/disappears in whole steps; underline
is instant; counter per §6.2 variant.

**Breakpoints.** ≥1200px: full plate as structured. 768–1199px: nav
keeps 4 links (`ABOUT` folds into the footer plate), counter in drum
form. <768px: plate carries wordmark, lamp twin, compact counter text
and a `SHELVES` key that opens the contents drawer (§6.12); transport
mirror takes the plate's full right half when playing.

**Edge cases.** Extremely long archive names: the wordmark plate
shortens to its stamped initials (a data decision in the plate's
config, e.g. `MRT` for the Mill Road Tapes) — never a smaller font.
Print: the plate prints as a plain header line; instruments print
their text twins.

**Accessibility.** Real `<nav>` with a list; `aria-current="page"` on
the active shelf (the oxide dot is its visual twin, never the only
signal). Skip-link styled as a stamped chip lands before the plate.
All plate text ≥ §2 contrasts (card on bakelite-2 ✓).

**Performance & mobile.** Sticky via CSS only; mirror animation is
width/opacity on one slot <0.1ms/frame. Mobile: drawer per §6.12.

**Tokens.** `--bakelite-2`, `--plate-line`, `--box-card`, `--oxide`,
`--splice`, `--metal-hi`, `--ease-transport`.

### §6.12 Contents drawer (the card catalogue)

**What & why.** Navigation below the plate — the full catalogue — opens
as a card-catalogue drawer: a bakelite cabinet face whose drawer pulls
out carrying index cards of shelves, chapters and narrators. It belongs
because an archive's deep navigation is a catalogue, and a catalogue is
consulted, not browsed: you pull the drawer, you find the card, you go
to the shelf. On mobile it is the primary nav; on desktop it is the
`CATALOGUE` key's answer.

**Structure.** Overlay panel sliding from the left, 400px desktop /
100vw mobile, `--bakelite-2` ground; inside, drawers as horizontal
bands (one per collection), each with a label holder (brass-toned
`--khaki` frame, Oswald label). Expanded drawer lists its cards:
Plex Mono entries with catalogue numbers and counter readings, each a
real link. A search slot at the top is styled as a typed request slip
(§6.15 shares the slip grammar).

**Motion spec.** Open: drawer pulls toward the visitor — translateX
−24px→0 + opacity, 340ms `--ease-transport`, drawers stagger their
label holders by 40ms. Expand a drawer: its band height animates
220ms `--ease-settle`, cards stagger 30ms. Close: 240ms
`--ease-spool` (drawers shut faster than they open; putting things away
is brisk). The page behind dims with bakelite at 60% — no blur (the
room darkens; it does not smear).

**Choreography timeline.** t=0 key press → dim 120ms → panel seated
340ms → first drawer pre-expanded (the current shelf) at 380ms → focus
lands on the request slip at 400ms.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (closed) | Absent from tab order entirely | Same |
| Hover (drawer band) | Label holder brightens; band does not pre-open (drawers open on pull, not on proximity) | n/a |
| Focus | Visible oxide outlines; Esc closes from anywhere inside; focus returns to the invoking key on close | Same |
| Active (open) | Focus trapped politely (focus cycles within the panel); page scroll locked | Same; swipe-left on the panel also closes |
| Scrolled-past | n/a (overlay) | n/a |
| Disabled | The catalogue exists as a plain page (`/catalogue`) linked from the footer plate; the drawer is an enhancement of it | Same |

**Content-merge.** The drawer's contents are the catalogue itself —
same numbers, same readings, same shelf names as §6.11 and the shelf
strata. It introduces no navigation vocabulary of its own.

**Failure fallback & watchdog.** If the panel's JS fails, the
`CATALOGUE` key is a plain link to `/catalogue` (progressive
enhancement: the key starts as that link; JS upgrades it). No watchdog
needed beyond the global lifeboat — a drawer that never opens leaves a
working link.

**Reduced motion.** Panel appears in place (opacity step 120ms),
drawers expand instantly, no stagger.

**Breakpoints.** ≥1200px: 400px panel, catalogue key in the plate.
768–1199px: 360px panel. <768px: full-width panel; this is the primary
nav (§6.11); drawer bands 56px tall for touch.

**Edge cases.** Deep catalogues (a shelf with 200 reels): drawer lists
shelf-level cards only, with `ALL 214 REELS →` as the last card — the
drawer is an index, not the collection. Search with no results hands
over to §6.18's blank-tape state inside the panel.

**Accessibility.** `role="dialog"`, `aria-modal`, labelled by the
request slip's heading; drawer bands are `<button aria-expanded>`;
cards are links in a list. Contrast: khaki label holders carry Oswald
in `--ink` on a `--box-card` insert (the holder is a frame; the label
card inside it is card stock — contrast solved by construction).

**Performance & mobile.** Panel transform/opacity only; catalogue data
is the page's own index, no extra fetch for the current collection.
Mobile: full-width form above.

**Tokens.** `--bakelite-2`, `--bakelite`, `--khaki`, `--box-card`,
`--ink`, `--oxide`, `--ease-transport`, `--ease-settle`, `--ease-spool`.

### §6.13 Transcript sheet

**What & why.** The testimony as a typed document: a `--paper` sheet
with a ruled left margin, punched-hole marks at the top, speaker turns
labelled, timestamps in the margin, and the archivist's pencil
annotations where the tape was unclear (`[coughs]`, `[inaudible 03:12 —
traffic]`, `[laughs]`). It belongs because §1's second law makes the
transcript the most important object in the archive — the sheet is
where the theme's reverence becomes typography.

**Structure.** `<article>` sheet, max-width 720px, padding 48px 56px,
top clip detail (a bakelite clip bar, 8px, with two bolt dots). Margin
column 72px carries turn timestamps (Plex Mono 12.5px, `--pencil` at
rest → `--ink` when played). Turns: label line (`WHITFIELD:` Oswald-ish
treatment per §3 law 3 — Plex Mono 600 uppercase +0.08em) then the words
at 16.5px/1.65. Pencil annotations inline in italic `--pencil`.
Uncertainty is printed, never smoothed: `[inaudible]` spans carry a
dotted underline in oxide — the sheet shows its own gaps.

**Motion spec.** The sheet's motion is the playhead's (§6.3/§6.8):
turns transition ink colour `--pencil`-grey print → full `--ink` as
their timestamp passes (300ms colour ease — a reading settling, not a
highlight flashing), the current turn's margin gains the oxide rule.
Standalone (story page, audio playing via §6.8): the sheet auto-scrolls
only if the visitor has enabled `FOLLOW THE VOICE` (a real toggle,
off by default — the archive never drags a reader's page). On the
story page without play, the sheet is gloriously static.

**Choreography timeline (with §6.3 scrub).** Playhead crosses a turn's
`data-t` → margin timestamp inks (100ms) → turn text settles to full
ink (300ms) → previous turn's oxide rule fades to its tick (200ms).
Three overlapping small settles; the sheet never jumps.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (unplayed) | Full text at full ink — the unplayed state is NOT greyed; greying unplayed text would gate words behind a gesture (§1 law 2). Margin timestamps in pencil | Same |
| Hover (a turn) | Margin timestamp underlines (the turn is addressable: clicking it seeks play/scrub to its `data-t`) | Tap = same seek |
| Focus (turn via keyboard) | Turn is focusable (`tabindex="0"`, role note in §Accessibility); oxide margin rule shows | Same |
| Active (current turn) | Oxide margin rule + timestamp in ink; text was already full ink — only the margin performs | Same |
| Scrolled-past (played turns) | Khaki margin tick remains per played turn — the sheet keeps the reading's evidence | Same |
| Disabled | The complete printed sheet. This is the fallback and the point | Same |

**Content-merge.** The sheet *is* the content; every other element on
the story page (deck, waveform, condition record) is the sheet's
machinery and provenance. Its annotations come from the transcript
data, including the honest gaps.

**Failure fallback & watchdog.** None applicable in the machinery
sense: the sheet is server-rendered text. If turn timestamps are
missing from the data, the sheet prints without a margin column and
the playhead sync (§6.3) is disabled for that testimony with a pencil
note saying so — absence admitted, never faked with estimated times.

**Reduced motion.** Margin states change in whole steps; no colour
easing; auto-follow toggle unavailable (hidden) — following is motion.

**Breakpoints.** ≥1200px: sheet 720px, margin 72px. 768–1199px: sheet
full column, margin 56px, padding 40px. <768px: margin collapses —
timestamps move inline before each turn in pencil brackets
`[03:12]`; sheet padding 28px 20px; font 16px/1.6.

**Edge cases.** Very long testimonies (3h+): the sheet paginates by
chapter splices (§6.4) — the document is a sheaf, each chapter-sheet
its own clip bar, counter readings at each join. Multi-speaker
roundtables: labels carry surnames; overlapping speech is printed as
the transcriber heard it, `[both speaking]` in pencil — the sheet
never invents a clean turn out of a messy room.

**Accessibility.** The sheet is the accessible form of the audio: full
text, logical order, headings per chapter. Turn seeking is a bonus,
never a requirement. Ink on paper 12.33:1 ✓; pencil annotations
5.66:1 ✓ at 14px italic (they are annotations, and any `[inaudible]`
is also announced by its dotted underline + the word itself).

**Performance & mobile.** Colour transitions on margin elements only;
long sheets use `content-visibility: auto` per chapter-sheet. Mobile:
inline-timestamp form above.

**Tokens.** `--paper`, `--ink`, `--pencil`, `--khaki`, `--oxide`,
`--bakelite` (clip bar).

### §6.14 Shelf index (listing & filters)

**What & why.** The catalogue listing: shelves of boxes (§6.6) with a
filter rail built as label-maker chips — decade, narrator, condition,
digitisation status — and a sort key stamped like a shelf mark
(`ORDER: CATALOGUE № / YEAR / DURATION`). It belongs because an
archive is found through its catalogue discipline; the listing is
where the theme proves its objects can be *searched* without stopping
being objects.

**Structure.** Left rail (240px desktop) of filter groups, each a
small bakelite plate with Oswald caption and chip rows (chips are
real `<button aria-pressed>`, card stock, ink text, oxide pressed
state shown as a stamped inset). Main column: shelf strata (§4) with
a shelf heading per group (the grouping is physical: `SHELF 3 —
MILL WORKERS, 1955–1979`). Result count printed as a counter reading
(`SHOWING 0417 OF 214 REELS` — the count is the catalogue's own).

**Motion spec.** Filtering: boxes that leave fold to their spine
(rotateY to 12° + fade, 240ms `--ease-spool`) — they are reshelved,
not deleted; boxes that arrive take their places with §6.6's rise
(300ms, stagger 35ms, capped at 12 animated — beyond 12, the rest
print instantly: a shelf does not perform a ballet for a large
accession). Filter changes never scroll the page. Sort: the shelf
re-lays with the same grammar, 400ms total.

**Choreography timeline (filter press).** 0ms chip stamps in →
60ms leaving boxes begin fold → 300ms shelf re-lays → arriving boxes
rise (35ms stagger) → count reading tumbles to its new truth (§6.2
machinery, 300ms) → quiet by ~800ms.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Full shelf, chips unpressed, count true | Same; rail collapses (below) |
| Hover (chip) | Chip lifts 1px | n/a |
| Focus | Oxide outline; chips are buttons in a group with a real `<fieldset>`/legend per group | Same |
| Active (filtering) | Per timeline; the shelf region carries `aria-busy` until quiet | Same |
| Scrolled-past | Static shelves | Same |
| Disabled | Filters are a GET form that submits to a filtered server page — the catalogue works without a single animation | Same |

**Content-merge.** Filters are catalogue fields (the same decade,
condition and status data printed on the boxes), and the count is the
catalogue's count. Nothing is faceted that is not printed on an
object in the room.

**Failure fallback & watchdog.** If the client filter fails, the GET
form fallback stands (the form is the DOM; JS intercepts it).
`shelf-watchdog` (§6.6) covers box landing. A filter combination with
no reels hands over to §6.18 — inside the shelf, not on an error page.

**Reduced motion.** No folds, no rises: the shelf swaps instantly,
count updates as text.

**Breakpoints.** ≥1200px: rail + 4-wide shelves. 768–1199px: rail
collapses to a top plate with chip rows, shelves 3-wide. <768px:
filters in the §6.12 drawer (a `FILTERS` drawer), shelves stacked;
count reading stays visible above the first shelf.

**Edge cases.** A shelf group emptied by filters: its board remains
with a pencil line — *"Shelf 3 is empty under these labels."* — the
room admits an empty shelf rather than collapsing the architecture.
Deep links with filters in the URL restore exactly, with the count
reading locking to truth on arrival (§6.2).

**Accessibility.** Chip groups labelled; result count is a polite
live region updated on quiet (not mid-animation); boxes remain links
(§6.6). Pressed chip: oxide inset + `aria-pressed` — state never by
colour alone (the inset is a shape).

**Performance & mobile.** Fold/rise are transform/opacity; the
12-animation cap bounds the frame cost on big shelves (<1.2ms/frame
worst case). Mobile: drawer filters above.

**Tokens.** `--box-card`, `--ink`, `--oxide`, `--bakelite-2`,
`--khaki`, `--pencil`, `--ease-spool`, `--ease-transport`.

---

### §6.15 Lend-a-reel form (contribution & booking)

**What & why.** The archive's conversion surface: a visitor lends a
recording, books a digitisation slot, or offers a testimony. The form
is a tape-box label being filled in — fields ruled like label lines on
card stock, set into a bakelite plate — and its confirmation is a
stamped accession label bearing a real number: the next catalogue
number, derived from the catalogue count printed on the page. It
belongs because contributing to an archive is an act of custody; the
form should feel like handing an object across a desk, not like a
checkout.

**Structure.** Plate (`--bakelite-2`) holding a card-stock label
(680px max) with ruled fields: your name, the recording (format
select styled as a stamped chip row: REEL / CASSETTE / DIGITAL FILE /
A STORY, NO TAPE YET), its year if known, its condition in your words,
contact. Each field: Oswald caption above a ruled line; the input is
the line. Submit is a transport key (§6.8's key grammar, labelled
`THREAD THIS TAPE`). The accession counter beside the form prints the
catalogue's current last number (`LAST ACCESSION № 214`) — the source
line for the confirmation's number.

**Motion spec.** Field focus: the ruled line inks in oxide from the
left (200ms) and the caption stamps one step darker — the label is
being written on. Validation error: the field's line goes oxide
double-ruled, the error prints beneath in pencil register but in
`--ink` (errors are not marginalia; §12), and the label jolts 2px
once (120ms) — a typewriter carriage hitting a stop. Submit: the key
travels (§6.8), the whole label lifts 2px as if taken from the desk,
and the confirmation stamps in (§6.6 stamp machinery): accession
label, number = printed last + 1, with the words the archive will
write back and when.

**Choreography timeline (submit).** 0ms key travel → 150ms label
lifts → 400ms form plate settles empty behind → 520ms confirmation
label stamps (letters 18ms stagger) → 900ms its counter reading chip
stamps → quiet. No spinner anywhere: if the request takes >1200ms,
a printed line appears — *"The desk is writing your label…"* — words,
not a whirligig (§6.17 covers true loading states).

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Label blank-ruled, last-accession source line printed | Same |
| Hover (field) | Ruled line warms to `--metal-hi` | n/a |
| Focus | Oxide ink-in + caption stamp (above); focus order is the label's reading order | Same; fields ≥48px tall |
| Active (submitting) | Key held down, fields inert but readable, desk line if slow | Same |
| Scrolled-past | n/a (form is a destination) | n/a |
| Disabled | A plain HTML form posting to the archive's endpoint — the label styling is CSS on a real form | Same |

**Content-merge.** The form's fiction is its function: the fields are
the accession record's fields (the archive will keep exactly this
data), the confirmation number continues the printed catalogue, and
the condition-in-your-words field feeds §6.10's record (marked
`DONOR'S ACCOUNT` until assessed — provenance again).

**Failure fallback & watchdog.** Submission failure: the label stays
filled (input is never eaten), a pencil-voice line explains and the
key re-arms after 800ms. Double-submit is impossible (key inert while
held) and the accession number is only consumed on success — a failed
attempt never burns a catalogue number, because in a real archive it
wouldn't.

**Reduced motion.** No lift, no stamp stagger: confirmation appears
whole; the jolt becomes a static double rule on the errored field.

**Breakpoints.** ≥1200px: plate + label side by side with the
accession source plate. 768–1199px: stacked, label full width.
<768px: plate padding 16px, label padding 24px, chip row wraps to
2×2, key full width (48px tall).

**Edge cases.** A donor with no tape (a story only): selecting
`A STORY, NO TAPE YET` swaps the format fields for a "how shall we
record you" pair (visit / we come to you) — the form's fields follow
the object's reality. Year unknown: the field accepts `NOT SURE` as a
printed value (catalogued absence, §6.6's rule). Very long condition
descriptions: the textarea grows; labels make room, as boxes do.

**Accessibility.** Real `<label>` per field (the Oswald caption IS
the label element), errors linked via `aria-describedby`, error
summary at the top of the label in ink on submit failure, focus
moves to the summary. Confirmation is a status region. Contrast:
ink on card 9.57:1 ✓ throughout the label.

**Performance & mobile.** Animations are transform/opacity/width on
single elements (<0.2ms/frame during the submit beat only). Mobile:
per breakpoints.

**Tokens.** `--bakelite-2`, `--box-card`, `--ink`, `--oxide`,
`--pencil`, `--khaki`, `--ease-stamp`, `--ease-transport`.

### §6.16 Archive colophon plate (footer)

**What & why.** The footer is the machine's back plate: bakelite,
bolted, carrying the archive's colophon the way a deck carries its
maker's plate — who keeps this archive, where the shelves live, the
catalogue's totals as counter readings, the digitisation credits, and
the leader-tape strip (§5) running above it. It belongs because an
archive's footer is its provenance page, and provenance is printed on
the machine, not floated in a grey band.

**Structure.** Full-bleed `--bakelite` plate, top edge closed by the
leader-tape band. Three columns: the keeper's plate (archive name
stamped, address, contact, visiting hours for the listening room);
the catalogue plate (totals as Plex Mono readings: `REELS HELD 214`,
`HOURS DIGITISED 611:24`, `NARRATORS 168` — each the same data object
as §6.14's counts and §8's worked figures); the credits plate
(digitisation engineers, funders, the line *"Every reel in this
archive remains the property of its narrator's family."*). Bottom
line: shelf-mark nav repeated in machine labels + the printed line
`— End of catalogue` above a final splice band.

**Motion spec.** The footer's one motion is arrival honesty: its
totals count in via §6.2's drum machinery when the plate first enters
(from their printed previous-edition values, §5) — the only place
besides the hero where drums turn for data rather than position.
The leader-tape band scrolls its 28s loop until the footer is reached,
then stops mid-strip (tape rests where it stops; it does not rewind
for the footer).

**Choreography timeline.** Plate enters 30% → drums begin (200ms) →
readings lock left→right by 900ms → leader band halts within one
strip-length → quiet.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (unreached) | Totals printed at their true values in the DOM | Same |
| Hover (links) | Splice rule (plate grammar, §6.11) | n/a |
| Focus | Oxide outline | Same |
| Active | n/a | n/a |
| Scrolled-past | The footer is the end; beyond it, nothing | Same |
| Disabled | Printed plate, totals as text | Same |

**Content-merge.** Every figure on the plate is the catalogue's figure
(third printing of the same data: hero counter, listing count, footer
totals — §8's example keeps all three in agreement). The ownership
line is the archive's ethics, placed where colophons live.

**Failure fallback & watchdog.** Totals are static text beneath the
drum treatment; `counter-watchdog` (§6.2) applies if drums are used.
No other machinery, no other failure mode.

**Reduced motion.** Totals print statically; leader band is a static
strip (its text fully present, duplicated in the credits column for
anyone who cannot read a moving band — though under reduced motion it
does not move at all).

**Breakpoints.** ≥1200px: three columns. 768–1199px: two columns
(credits under keeper). <768px: single column, plates stacked, leader
band cut (§5), totals remain — the numbers outrank the ornament.

**Edge cases.** An archive with no physical room: the keeper's plate
prints its real arrangement (`VISITS BY APPOINTMENT — WRITE TO THE
DESK`) — the plate describes the archive that exists. Totals that
change between page build and visit are the build's figures, labelled
with their date in pencil: `COUNTED 14 NOV 2026`.

**Accessibility.** Footer landmarks and lists are semantic; totals
are text. The ownership line is ordinary body text, not fine print —
14px minimum, card on bakelite 10.46:1 ✓.

**Performance & mobile.** Drum beat <0.15ms/frame for 900ms once.
Mobile: stacked form above.

**Tokens.** `--bakelite`, `--box-card`, `--ink`, `--pencil`,
`--splice`, `--plate-line`, `--ease-stamp`.

### §6.17 Spooling skeleton (loading state)

**What & why.** When a shelf or a story loads asynchronously, the
archive shows unlabelled boxes: blank card rectangles on a shelf
board, spines unpainted, a faint leader-tape line where the label
will be. It belongs because loading in this room is a physical state
— the tape is being fetched from the shelf — and a generic spinner
would be a foreign object from a different building.

**Structure.** Shelf board (per §4) + N blank boxes at the exact
geometry of §6.6 cards (same ratio, same spine width, label area
shown as two ruled lines in `--plate-line`-on-card tones). On story
pages: the deck plate prints whole (it is furniture) with the
waveform area as flat leader (§6.3's 18% print at 0 amplitude) and
the transcript sheet as ruled blank paper — lines, not lorem.

**Motion spec.** One restrained gesture: a sheen passes across the
blank boxes left→right over 1600ms, linear, infinite — light across
card in a dim room, not a shimmer advertisement. Boxes resolve by
§6.6's landing as their data arrives, in shelf order regardless of
arrival order (a shelf is filled left to right; the catalogue does
not shelve by network speed).

**Choreography timeline.** t=0 board + blanks print (they are in the
initial HTML for the first shelf — no layout shift when they fill).
Data lands → boxes land 70ms stagger → sheen stops when the last box
of the shelf lands. Ceiling: 1200ms — past it, whatever has not
arrived is replaced by §6.18's blank-tape card in place, with a RETRY
key; the shelf never shimmers forever.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (loading) | Blanks + sheen | Same |
| Hover/Focus | Blanks are inert, unfocusable; a visually-hidden `Loading the shelf…` status exists for AT | Same |
| Active (resolving) | Boxes land in order | Same |
| Scrolled-past | Resolution continues offscreen; landing animations are skipped for offscreen boxes (they print seated) | Same |
| Disabled | No skeleton state exists: server-rendered pages arrive complete | Same |

**Content-merge.** The skeleton is the shelf's own geometry with its
labels not yet written — it reserves the object's true space, so
nothing on the page moves when the archive answers. It contains no
fake text, no grey paragraphs pretending to be a transcript.

**Failure fallback & watchdog.** The 1200ms ceiling + §6.18 handover
is the watchdog (`shelf-load-watchdog`). A partial shelf (7 of 8
boxes) lands its 7 and puts the blank-tape card in the 8th place —
the shelf's order is sacred.

**Reduced motion.** No sheen: blanks are static, resolving in whole
steps.

**Breakpoints.** Identical geometry rules to §6.6 at each size;
<768px the story-page skeleton drops the deck's reel detail (rings
only) to keep the blank page light.

**Edge cases.** Instant cache hits (<100ms): skeleton never paints
(a 150ms paint-delay on the sheen only; the blanks' geometry is
present from first paint so there is still no shift). Slow single
box: it alone becomes blank-tape at the ceiling; neighbours are
unaffected.

**Accessibility.** `aria-busy` on the shelf region, one polite
announcement when the shelf completes. Blanks are `aria-hidden`.

**Performance & mobile.** The skeleton is the cheapest state on the
page (flat colour + one sheen gradient). Mobile: per breakpoints.

**Tokens.** `--box-card`, `--plate-line`, `--bakelite`, `--splice`.

### §6.18 Blank tape (empty state & 404)

**What & why.** The archive's empty state is an unrecorded reel: a
box labelled in pencil — *"Nothing on this reel yet."* — with the
reason and the way forward printed as catalogue facts. It serves
filtered-to-empty shelves (§6.14), empty search (§6.12), new
collections, and the 404 (a shelf mark that was never issued). It
belongs because an archive does not error; it reports a holding's
absence in the same hand it reports its presence.

**Structure.** A single tape box at shelf scale, centred on a board,
its label area carrying the pencil line as the headline treatment
(Plex Mono italic, 17px, `--ink` — for once the pencil gets the big
line, because absence is the message), beneath it the factual line
(`NO REELS MATCH THOSE LABELS` / `SHELF MARK MRT-999 IS NOT IN THE
CATALOGUE`), and one transport key with the way forward (`CLEAR THE
LABELS`, `BACK TO THE SHELVES`, `ASK THE DESK`). For 404, the box
additionally prints the nearest real shelf marks as links — the
catalogue guessing politely, in print.

**Motion spec.** Deliberately almost none: the box is already on its
board when seen (it does not stagger in — an absence should not
perform an entrance). Its one motion is the way-forward key's hover/
press grammar (§6.8 keys). On `CLEAR THE LABELS`, the return to the
full shelf uses §6.14's re-lay, 400ms.

**Choreography timeline.** None — specified as none. The state's
power is that the room goes quiet: no drums, no sheen, needles at
rest if visible.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Box printed, key at rest | Same |
| Hover (key) | Plate-step brighten (§6.8) | n/a |
| Focus | Oxide outline on the key; the pencil headline is the region's heading in DOM order | Same |
| Active (key pressed) | Clunk grammar; the shelf re-lays or navigation proceeds via §6.9 | Same |
| Scrolled-past | n/a (the state replaces its region) | n/a |
| Disabled | Identical — the state is pure print | Same |

**Content-merge.** The blank box is a catalogue object with the same
geometry, board and grammar as every filled box; its text is the
catalogue's true statement about its own holdings. The 404's
nearest-shelf links are computed from the real catalogue, not a
generic sitemap.

**Failure fallback & watchdog.** None — nothing here can fail that
the page itself hasn't already survived. If the catalogue itself is
unreachable, the server returns this state as a static page (the
archive's last honest word).

**Reduced motion.** Identical (there is no motion to reduce).

**Breakpoints.** All sizes: one box, centred, max-width 420px;
<768px the board spans full width and the box sits at shelf-stack
width (§6.6 mobile geometry).

**Edge cases.** A brand-new archive (zero reels): the home shelf
stratum uses this state at full scale with the lend-a-reel key
(§6.15) as the way forward — the empty archive's first page is an
invitation, printed as a label. Search for a narrator who exists
but has no digitised reels: the state names that truth —
*"WHITFIELD, A. — 3 REELS HELD, NONE YET DIGITISED"* — with `ASK
THE DESK` as the key; absence has kinds, and the catalogue knows
them.

**Accessibility.** The state is a region with a real heading; the
factual line is body text (ink on card 9.57:1 ✓); the key is a
button or link with a descriptive label.

**Performance & mobile.** Static; the lightest element in the theme.
Mobile: per breakpoints.

**Tokens.** `--box-card`, `--ink`, `--pencil`, `--plate-line`,
`--bakelite-2` (key).

---

## §7 Page application map

**Home — the listening room.** Deck hero (§6.1/§6.2/§6.5/§6.7) threaded
with the featured testimony; its scrub stage (§6.3) immediately below;
shelf strata of featured collections (§6.6); one chapter splice (§6.4)
into the archive's own story (a short paper stratum, §6.13 sheet
grammar used for the keeper's letter); the lend-a-reel plate (§6.15)
as the closing stratum; colophon (§6.16). The home page is the whole
machine demonstrated once, in order.

**Listing — the shelves.** §6.14 in full: filter rail, grouped
shelves, count reading. The deck does not appear; the room's wall
carries the page, and the header plate (§6.11) supplies the machinery.

**Story (detail) — the reel page.** A compact deck (reels at 160px,
the story's own waveform strip and transport, §6.8) pinned as the
page's first stratum; condition record (§6.10 full form); transcript
sheet (§6.13) as the body; chapter splices (§6.4) within long
testimonies; at the foot, the story's shelf-mates ("FROM THE SAME
SHELF") as one row of boxes, and the colophon. The story page is
where the theme's laws are most visible: one voice, its object, its
words, its provenance.

**Narrator page.** The person's shelf: their boxes in catalogue
order, a portrait plate (where held), a short biographical sheet in
§6.13 grammar (written by the archive, sourced, dated in pencil),
and their total tape as a counter reading. A narrator is a shelf,
not a profile — no follower counts, no social furniture, ever.

**About — the archive's own record.** Paper strata and plates
alternating: the keeper's letter (sheet), the machine's history
(plate with the deck photographed/drawn), the digitisation lab's
condition vocabulary explained (§6.10's chips as a printed table),
funding and ethics (the ownership line from §6.16, expanded).

**Contribute / book — the desk.** §6.15 as the page's single stratum
over a quiet shelf backdrop (one row of boxes, dimmed — the desk
faces the shelves). Confirmation is a page state, not a new page:
the stamped accession label (§6.15) with the desk's reply time
printed.

**Catalogue page.** §6.12's content as a full page (the drawer's
static twin): every shelf, every reading, no overlay.

**404 / empty.** §6.18.

---

## §8 Worked examples

One fictional but fully consistent archive runs through all three:
**The Mill Road Tapes** — a community oral-history archive. Catalogue
truth (printed identically everywhere it appears): **214 reels held,
168 narrators, 611:24 hours digitised, last accession № 214.**
Featured testimony: **Reel 014 — Mrs. A. Whitfield, b. 1938, "The
night the mill whistle stopped", duration 47:12 (2832s), digitised
2019, condition FAIR** (*"Reel 14: oxide shed at the leader, spliced
twice before digitisation, handle with care"*).

### §8.1 The hero — the deck, threaded

**Build.** Full-bleed bakelite deck (§4). Meter bridge across the top:
left VU meter, record lamp + `STANDBY` twin centred, right VU meter,
counter bezel at the bridge's right end reading `0000`. Middle band
(520px): supply reel left (pack full, r=128px), take-up reel right
(pack at leader, r=34px), headline plate between them: eyebrow in
Plex Mono khaki `A COMMUNITY SOUND ARCHIVE — EST. 2016`, headline in
Oswald 600/96px: `THE MILL ROAD TAPES` (two lines), standfirst in
Plex Mono 16.5px card: *"214 reels of the town remembering itself.
Thread a tape. Press play."* — the 214 is the catalogue's number,
sourced from the same data as §6.16's totals. Bottom strip: the
featured box label as a plate strip — `NOW ON THE DECK — REEL 014 ·
WHITFIELD, A. · 47:12` with its play key (§6.8) and condition chip
`FAIR` (§6.10).

**Scroll timeline.** Arrival: lamp strikes 200ms; needles calibrate
(§6.5); counter tumbles and locks `0000` by 780ms; headline stamps in
as a typed label (letters 18ms stagger, from 300ms, done by ~900ms);
reels at rest ratio. Visitor scrolls: the deck pins for 60vh — during
the pin, scroll fast-forwards Reel 014's tape: packs trade by the
conservation formula mapped to the pin's length (not the whole page —
the pin is one reel's length; the page-position mapping resumes after
the pin), the counter spins toward the reading the featured section
will start at, needles ride the velocity. Pin releases into §8.2's
stage with the playhead at 00:00 and the lamp lit — the hand-off is
continuous: the tape you fast-forwarded is the tape you now scrub.

**Why it works.** Every figure on the hero (214, 47:12, the counter)
is a figure the rest of the page will honour; the hero is the machine
demonstrating its honesty before asking for attention.

### §8.2 Mid-page — scrubbing Mrs. Whitfield

**Build.** §6.3's stage, 180vh. Sticky stage contents: the testimony's
plate line (`REEL 014 — WHITFIELD, A. — RECORDED 12 MAY 2019, HER
KITCHEN`), waveform 120px from Reel 014's real peak data (leader flat
for the first 2%), playhead + timecode `00:00 / 47:12`, and the
transcript sheet (§6.13) with 23 turns, timestamps from the real
transcript (first turn `00:07` — seven seconds of room tone before
she speaks, printed as `[room tone, a clock]` in pencil, because the
sheet prints silence too).

**Scroll timeline.** 0–10% of scrub: leader and room tone; timecode
climbs to 04:43; the first turn inks at its 00:07 mark as the playhead
passes (the scrub is un-eased, so "passing" means the visitor's hand
put it there). 10–90%: the voice — turns ink in step; at 51% the
waveform shows the long pause before she describes the whistle, and
the sheet shows `[silence — 11 seconds]` in pencil; the scrub makes
the visitor *wait through it at their own speed*, which is the
archive's whole ethic in one gesture. 90–100%: run-out; at exactly
100% the timecode reads 47:12, the stage unsticks, the lamp returns
to standby, and the shelf of her other reels (§6.6, 3 boxes) is the
next stratum. Scroll back up: every tick withdraws in reverse; the
tape rewinds because the hand rewinds.

**Data discipline.** The mapping uses `data-duration="2832"` from the
same record that printed `47:12` on the box, the hero strip and the
story page. If the archive corrects the duration, all four printings
move together or the build fails §10's figure-truth audit.

### §8.3 Conversion — lend a reel

**Build.** §6.15's plate on the Contribute page. Beside the label,
the source plate prints `LAST ACCESSION № 214` and `REELS HELD 214`
(the catalogue object). The label's fields: name; format chips
(`CASSETTE` preselected by nobody — the donor's object decides);
year (with `NOT SURE` accepted); condition in your words; contact.

**Walk-through with scroll/interaction timeline.** The page is one
stratum; no scroll choreography beyond arrival (label present,
source line printed). Donor Amara O. offers a 1987 cassette of her
grandfather at the bakery. She picks `CASSETTE`, year `1987`,
condition: *"Kept in a biscuit tin. Plays, but the middle warps."*
Focus beats per §6.15 (line inks, caption stamps). Submit: key
travels, label lifts, and at 520ms the confirmation stamps in:
`ACCESSION № 215 — RESERVED` / *"The desk will write to you within
five working days. Your tape stays yours; we borrow the sound."* —
215 = printed 214 + 1, computed at success, and the footer's next
build will print 215 as the new last accession because the catalogue
object moved. Her condition words enter Reel 215's record as
`DONOR'S ACCOUNT` (§6.15), to become a §6.10 note after assessment.
Error path (she had left contact blank): the field double-rules, the
ink error prints *"The desk needs a way to write back — an email or
a phone number."*, focus moves to the summary, and her typed words
are all still there. Nothing was eaten; a number was not burned.

---

## §9 Anti-slop — what makes THIS theme look cheap, and the cure

1. **The decorative counter.** A counter that spins for delight and
   reads nothing. *Cure:* §6.2's mapping or no counter; §10 audits
   the reading against scroll position at three depths.
2. **Reels that shrink for show.** Pack radii eased toward arbitrary
   sizes. *Cure:* the conservation formula (§6.1) is the only legal
   radius; both packs are computed from the same `p` every frame.
3. **A waveform that is a sine doodle.** Generic wavy SVG behind a
   "story". *Cure:* waveforms are generated from the recording's peak
   data at build time; a testimony without data gets the printed
   leader line and the pencil admission (§6.3), never a fake voice
   shape.
4. **Meters moving without a signal.** VU needles dancing on a timer
   while nothing plays and nobody scrolls. *Cure:* §6.5's two legal
   inputs only (scroll velocity, playing amplitude), and the bridge
   caption states which is live.
5. **The record light as decoration.** Amber dots sprinkled as
   badges, bullets, "live" tags. *Cure:* one lamp, one boolean
   (§6.7); §10 counts `--rec` usages in the built page.
6. **Sepia nostalgia filter.** The whole page dipped in tea to fake
   age. *Cure:* the palette is physical (bakelite, card, oxide), not
   a filter; photographs are reproduced straight — age lives in the
   objects' conditions (§6.10), not in a colour wash.
7. **Skeuomorphic chrome overload.** Screws, vents, leather corners
   and brand badges until the page is a fancy-dress deck. *Cure:*
   the plate grammar is four bolts and a hairline (§4); every other
   detail must carry data or be cut.
8. **Transcripts hidden behind the player.** Words revealed only as
   audio plays — the archive holding testimony hostage to its
   theatre. *Cure:* §1 law 2 and §6.13's rest state: full ink, always.
9. **Invented provenance.** Condition notes, years and catalogue
   numbers written as flavour text. *Cure:* every such string comes
   from the record; absence prints as absence (`YEAR NOT RECORDED`,
   `CONDITION NOT YET ASSESSED`).
10. **Percentage progress.** A 62% bar anywhere. *Cure:* position is
    a counter reading and a quantity of tape (§5); percentages are
    refused at review.
11. **Bouncy toy physics.** Elastic cards, springy logos. *Cure:*
    the five named easings and the needle spring are the whole
    physics vocabulary; nothing else overshoots except a needle,
    which overshoots because it is one.
12. **Stock-photo "vintage" imagery.** Library photos of strangers'
    grandparents. *Cure:* portraits only from the archive's own
    holdings; absent a portrait, the printed reel glyph (§6.6) —
    an honest absence over a borrowed face.

---

## §10 Quality gate

Blocking checks — all must pass before this theme ships in a build.

1. **Figure-truth audit.** Every printed figure (counter readings,
   durations, catalogue totals, accession numbers, `STARTS nnnn`)
   traced to its data object; the same figure agrees in every
   printing (hero / listing / footer). One invented number fails
   the build.
2. **Conservation test.** At p = 0, 0.25, 0.5, 0.75, 1: rendered
   pack radii satisfy the §6.1 formula within 1px, both reels, from
   the same `p`.
3. **Counter test.** At three scroll depths, the counter reading
   equals `round(p × 9999)` ±1.
4. **No-JS completeness.** With JavaScript disabled: every story,
   transcript, condition note and figure is present and readable;
   forms submit; navigation works.
5. **Reduced-motion pass.** `prefers-reduced-motion`: no rotation,
   no scrub pin, no jolt, no tumble; play state still fully
   operable; transcripts complete.
6. **Waveform provenance.** Every waveform path on the page maps to
   a peak-data file in the build; the flat-leader fallback exists
   for data-less reels.
7. **Lamp census.** Exactly one `--rec` element visible per
   viewport; lamp state matches the play controller in all states
   (standby / scrub-centred / playing / paused).
8. **Watchdog drill.** Kill the rAF loop mid-scroll: reels freeze
   at true ratios, counter snaps within tolerance, splice and shelf
   pre-states clear, no content invisible after 3000ms.
9. **Contrast audit.** Khaki never sets text below its §2 ruling;
   oxide never sets text on card; pencil notes always paired with
   their ink chip; all body text ≥4.5:1.
10. **Transcript integrity.** For three sampled testimonies: turns,
    timestamps and `[inaudible]` spans match the source transcript
    exactly; no turn is gated behind play.
11. **One-angle audit.** Every diagonal on the page is −4° (or its
    documented mobile/tenth variants); no other rotated decoration
    exists.
12. **Performance sign-off.** §14's budgets measured on a mid-tier
    Android over the story page: frame budget held during scrub,
    no long task >50ms from theme code.

---

## §11 Component inventory

Every component a real archive site needs, with its Reel to Reel
treatment. Components the theme refuses are listed with their
in-theme replacement — a refusal is a design decision, not a gap.

| Component | Treatment |
|---|---|
| Primary button | Transport key (§6.8): bakelite-2 key, stamped Oswald label, 2px travel, clunk grammar. One per view — the key you press is the commitment you're making. |
| Secondary button | Label chip: card stock, ink text, 1px ink rule; hover lifts 1px; no travel (it is paper, not a key). |
| Text link | Ink/card text with splice-toned underline rule drawing 160ms (§6.11). |
| Text input | Ruled label line (§6.15): Oswald caption, oxide ink-in on focus, the line is the field. |
| Select | Stamped chip row (≤5 options) or, beyond 5, a native select restyled as a label line — the archive never builds a fake dropdown machine. |
| Checkbox / radio | Stamp boxes: 18px card squares, checked = oxide stamp fill with a 1.5° rotation (a hand stamped it). |
| Toggle | Admitted once: `FOLLOW THE VOICE` (§6.13) — a transport-style slide key labelled in words at both ends (`OFF` / `FOLLOW`), never an anonymous pill. |
| Tabs | Refused. Chapters are splices (§6.4) and collections are shelves; a tab strip is neither. Multi-view data uses stacked plates with splice joins. |
| Accordion | The catalogue drawer's bands (§6.12) are the theme's only expansion pattern; elsewhere, content prints in full (an archive does not fold its documents). |
| Modal | The contents drawer (§6.12) is the only overlay. Confirmations are page states (§6.15), never popups. |
| Toast | Refused. Messages are printed lines in place (pencil or ink per §12) — a toast would be a Post-it on a machine. |
| Tooltip | Refused. Anything worth saying is printed (condition notes, captions); instruments carry text twins instead. |
| Badge / chip | The condition chip (§6.10) is the only badge: stamped, closed vocabulary. No counts-in-circles, no "NEW" flashes — new accessions get a pencil line `SHELVED 14 NOV` on their box. |
| Table | The condition vocabulary table and catalogue ledgers: Plex Mono, ruled rows in `--plate-line`, Oswald header row stamped on a bakelite strip. Numbers right-aligned, always tabular. |
| Pagination | Counter grammar: `REELS 0001–0040 · TURN THE SHELF →` — a shelf-turn key, never numbered page pills. The reading updates from the catalogue count. |
| Progress bar | Refused (§9.10). Position is the counter + pack ratio (§6.1/§6.2). |
| Spinner | Refused. Loading is §6.17's unlabelled boxes or a printed desk line (§6.15). |
| Skeleton | §6.17 spooling skeleton. |
| Alert / notice | A printed plate strip: bakelite band, card text, Oswald caption (`FROM THE DESK:`), in place in the flow — alerts are letters from the desk, not banners from the system. |
| Breadcrumbs | Shelf marks: `THE SHELVES / MILL WORKERS / REEL 014` in machine labels with splice slashes — the catalogue's own path language. |
| Audio player | §6.8's transport + §6.3's waveform; native `<audio controls>` is the no-JS form. No third-party player chrome ever. |
| Search | The request slip (§6.12): a typed card field; results are a shelf (§6.14) with the count reading restated for the query. |
| Skip link | Stamped chip, first in tab order (§6.11). |

---

## §12 Copywriting voice

Two registers, and the page never confuses them.

**The Machine** (Oswald, uppercase, terse): labels, keys, captions,
readings. The machine does not explain itself; it states. Max ~5
words per label. ✓ `THREAD THIS TAPE` · `METERS: TAPE / ROOM` ·
`END OF REEL 14`. ✗ `Click here to start listening now!` · `Oops!`
· anything with an exclamation mark — the machine owns none.

**The Pencil** (Plex Mono italic, sentence case, the archivist's
hand): condition notes, marginalia, admissions. First person plural,
plain, kind. ✓ *"Reel 14: oxide shed at the leader, spliced twice
before digitisation, handle with care."* · *"[silence — 11 seconds]"*
· *"Waveform not yet drawn for this reel; the words are complete."*
✗ Marketing warmth (`"Dive into amazing stories!"`), ✗ archival
jargon as a gate (`"accession pending appraisal"` when *"the desk
has not listened to this one yet"* is true and kinder).

**Headlines** are plates, not hooks: they name the place or the
person (*THE MILL ROAD TAPES*, *WHITFIELD, A. — B. 1938*), never a
promise. **Labels** name the object in the catalogue's nouns (reel,
shelf, narrator, desk). **Errors** are written by the desk in ink
(not pencil — errors are official): factual, blameless, with the way
forward in the same breath. ✓ *"The desk needs a way to write back —
an email or a phone number."* ✗ *"Invalid input."* **Empty states**
report holdings truthfully (§6.18): ✓ *"WHITFIELD, A. — 3 REELS
HELD, NONE YET DIGITISED."* **Fixed strings** (verbatim, do not
paraphrase): the condition example *"Reel 6: vinegar syndrome,
digitised 2019, handle with care"*; the ownership line *"Every reel
in this archive remains the property of its narrator's family."*;
the standby twin `STANDBY`; the closing line `— End of catalogue`.

**Numbers in copy** follow §1's law: a number appears only if the
page's data carries it, and durations are always `MM:SS`, counts
always plain (`214 reels`, never `200+ reels`).

---

## §13 Scroll choreography map (home page, top to footer)

1. **Arrival (no scroll).** Lamp strikes (200ms) → needles calibrate
   → counter tumbles to `0000` → headline stamps → featured strip
   prints. The room powers on in under a second.
2. **The pin (0–60vh of scroll).** The deck fast-forwards Reel 014:
   packs trade, counter spins, needles ride velocity. The visitor's
   hand learns the machine's physics before any content asks
   anything of them.
3. **The scrub (the featured stage, 180vh).** Lamp lit; playhead
   crosses leader, room tone, the voice, the 11-second silence,
   run-out; transcript inks in step (§8.2). The emotional centre of
   the page, placed where a first scroll reaches it.
4. **First splice.** The −4° band lays down: `CHAPTER — THE SHELVES`.
   The machine opens into the room.
5. **Shelf strata.** Boxes land row by row (§6.6), spines parallax
   at 0.94×, portraits settle into sleeves. Browsing rhythm:
   land, read, land, read — the stagger never outruns reading.
6. **Leader-tape band.** A breath: accession numbers drift past at
   28s/loop. The archive's heartbeat between collections.
7. **The keeper's letter.** Paper stratum; the splice into it is the
   page's quietest beat — no drums, no needles in view, just the
   sheet. Pacing by absence.
8. **Second shelf stratum (narrators).** Boxes again, now grouped by
   person; the landing stagger shortens (35ms) — the visitor knows
   this dance now, and the room respects fluency.
9. **The desk (§6.15 plate).** Motion narrows to field grammar; the
   room quiets around the form the way a room does when someone is
   writing.
10. **The colophon (§6.16).** Totals drum in once; the leader band
    halts; `— End of catalogue`; final splice. Scrolling up reverses
    every scrubbed value exactly (tape rewinds), replays no entrances
    (shelves stay shelved), and returns the deck to its true ratio —
    the page ends, in both directions, with the machine at rest and
    honest.

---

## §14 Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight (home, first load) | ≤ 780KB | Fonts subset (Oswald 500/600 + Plex Mono 400/500/600, latin) ≈ 120KB; peak-data for the featured waveform ≤ 40KB; all other waveforms are print-weight SVG ≤ 6KB each until played. |
| Images | Portraits only, ≤ 60KB each, lazy below the first shelf | No deck photography — the machine is drawn (SVG/CSS), which is both lighter and more honest. |
| Frame budget (shared loop) | ≤ 1.6ms/frame total JS | Reel transforms + pack radii 0.3ms; needles 0.1ms; counter 0.15ms; scrub clip + readout 0.2ms; headroom reserved. Offscreen systems skip entirely. |
| Long tasks | None > 50ms from theme code | Peak-data parsing happens at build time, never in the browser. |
| Layout shift | CLS ≤ 0.02 | Skeleton geometry (§6.17) reserves every object's true space; pack radii animate inside fixed reel boxes. |
| Interaction response | Transport press → first visible change ≤ 100ms | The clunk's key travel is frame one. |

**Cut order when the budget is exceeded** (in this order, never
reordered): 1) leader-tape loop becomes a static strip; 2) spine
parallax cut (shelves go flat-registered); 3) portrait settle cut
(portraits print seated); 4) needle tremble amplitude halves;
5) headline stamp becomes a whole-label stamp (no per-letter
stagger). **Never cut:** the counter's truth, the conservation
formula, transcript completeness, the lamp, any fallback or watchdog,
the reduced-motion variants. A cheaper Reel to Reel is a quieter
machine, never a lying one.

---

## §15 Build-order checklist

1. **Static room first.** Deck plate, shelves, sheets and colophon as
   pure HTML/CSS with every word, figure and transcript in place.
   Verify §10 check 4 (no-JS completeness) before any motion exists.
2. **Catalogue data objects.** One source per figure (durations,
   counts, conditions, peak data); printings wired to sources.
   Figure-truth audit (§10.1) on the static page.
3. **Typography and palette tokens** per §2/§3, including the
   forbidden-pairing rules as lint checks in the build.
4. **The shared loop** (rAF, lerp 0.12, offscreen skipping, dt
   clamping) with the global 3000ms lifeboat.
5. **Counter + reels** (§6.1/§6.2) against the loop; conservation and
   counter tests (§10.2/10.3) green before proceeding.
6. **Needles + lamp** (§6.5/§6.7) on the shared play state (a stub
   controller at this stage).
7. **Waveform pipeline**: build-time peak-data generation; §6.3
   stage with scrub, timecode, transcript sync; provenance check
   (§10.6).
8. **Playback controller** (§6.8) binding lamp, meters, draws and
   the header mirror (§6.11); failure note path tested with a
   deliberately broken audio URL.
9. **Shelf system** (§6.6/§6.10/§6.14): cards, stamps, condition
   records, filters with GET fallback; §6.17 skeleton + §6.18
   states wired to the same shelf geometry.
10. **Splices + transitions** (§6.4/§6.9) with their watchdogs.
11. **Forms** (§6.15): label grammar, ink errors, accession-number
    derivation tested for the failure path (no number burned).
12. **Drawer + catalogue page** (§6.12), drawer as enhancement of
    the page, never the only route.
13. **Reduced-motion variants** for every element, verified as a
    set (§10.5) — built last as code, but designed from step 1.
14. **Watchdog drill + performance sign-off** (§10.8/10.12) on a
    mid-tier Android; cut order (§14) applied if needed.
15. **Final gate**: all twelve §10 checks signed by someone who did
    not build the page. The machine is not certified by its own
    needles.

*— End of theme #97 specification.*
