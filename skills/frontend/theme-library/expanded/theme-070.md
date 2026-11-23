# 70. Telemetry Tape — Expanded (v1 + v2)

> The site is one continuous strip of punched telemetry tape from a
> 1970s mainframe reader: every word of content is printed onto the
> tape in monospace blocks, sprocket holes run down both edges, and
> reading the page is literally spooling through the record. There
> is no "content area" decorated with a tape motif. There is a
> tape, it is 196.0 metres long, it holds one satellite pass from
> 14 March 1978, and the visitor reads it the way the machine did —
> one line at a time, under a read-head fixed at the centre of the
> screen.

**The theme's one law: the tape prints the record as it was
punched — never tidied, never rounded, never corrected in place.**
Every figure printed anywhere on the page traces to one declared
record, the Pass Record (§6.17): 49 blocks, 196.0 metres, 78,400
characters, one checksum failure. A block whose checksum fails is
not silently fixed and not hidden — it is printed garbled, stamped
RETRANSMIT REQUESTED, and followed by its retransmission, exactly
as the archive holds it. Corrections on this tape are always
*additional* tape, never edits. And the inverse rule binds the
motion system: punching, spooling and lighting are enhancements
performed over a page that ships fully printed — every block is
complete, legible text in the DOM from the first byte, and no
animation is ever the only copy of anything. A build that rounds
196.0 to "about 200 metres", repairs BLK 0027 in place, or leaves
a block unpunched because a script failed has broken the law
three ways.

---

## 1. Concept & world

The world is a specific room at a specific hour: a ground-station
tape library in 1978, where a satellite pass came down as sound,
was decoded onto punched paper tape, and the tape — not a screen,
not a printout — is the archival object. Paper tape is a ruthless
medium and the theme takes its discipline from it. It is
*sequential*: you cannot skim a tape, you can only spool it, so
the page's order is the record's order and there is no sidebar,
no tab bar, no "jump to the good part". It is *append-only*: a
mistake stays on the tape forever and is answered by more tape.
It is *self-checking*: every block carries a checksum, and the
medium expects you to verify as you read. And it is *physical*:
progress is not a percentage, it is footage — metres of paper
that have passed through the reader and now lie in the take-up
bin.

The mood is quiet, mechanical and faintly melancholic: buff paper,
ink, the green of a verifier lamp, one amber reserved for the
machine's doubts. Nothing glows. Nothing floats. The page's
beauty is the beauty of a well-kept record — even columns, honest
numbers, holes punched clean through.

**Best-fit sites and audiences.**

- **Archives, museums and data-rescue projects** — anywhere the
  artefact is a historical record and the institution's claim is
  *we kept it exactly as it was*: space-history collections,
  early-computing archives, declassified telemetry, digitised
  logbooks.
- **Engineering and infrastructure retrospectives** — postmortems,
  incident histories, "ten years of uptime" reports, where the
  append-only, never-tidied ethic is the message: the failures
  stay on the tape, stamped and answered.
- **Documentation with a chain of custody** — calibration records,
  test-bench results, audit trails, standards compliance logs:
  content whose value is that it was checked, block by block.
- **Slow, single-thread narratives** — a launch told as its
  countdown tape, a voyage told as its log, one pass, one dive,
  one night: stories that gain authority from being a single
  unbroken strip.

**When NOT to use it.**

- **Anything the visitor must search, filter or compare.** A tape
  has no index except its block numbers and no random access at
  all. Catalogues, dashboards and marketplaces fight the medium
  on every screen.
- **Anything urgent or transactional.** Checkout, booking and
  alerting need speed and forgiveness; the tape offers neither —
  §7 routes checkout off the tape entirely.
- **Content that will be edited after publication.** The law
  forbids in-place correction. A living document that changes
  weekly cannot live on a medium whose whole point is that
  nothing is ever changed, only answered.
- **Short pages.** Below roughly eight blocks the machinery —
  read-head, footage, checksums — outweighs the record. A
  two-screen announcement does not need 196 metres of theatre.

## 2. Palette

Five anchors, inherited unchanged from the original entry, plus
four derived tokens. The palette is paper and ink: every colour
is something that could physically be on or in the tape — the
paper itself, the ink ribbon, the shadow inside a punched hole,
the amber of a warning stamp, the green of the verifier lamp.
There is no colour in this theme that is not a material.

| Token | Hex | Role | Usage ratio | Notes |
|---|---|---|---|---|
| `--tape` | `#E8DFC8` | The tape itself: page ground, block ground | ~78% | Warm buff, never pure white; the whole page is this paper |
| `--ink` | `#2A2620` | Print ink: all body text, headlines, numerals | ~14% | 11.33:1 on `--tape` — the only colour body text may use |
| `--shadow` | `#CFC4A4` | Sprocket shadow: hole interiors, perforation rules, tape edge | ~5% | 1.31:1 on `--tape` — decorative only, never text, never an indicator alone |
| `--amber` | `#D98E04` | Alert amber: doubt — parity failures, cells under the read-head, stamp fills | ~2% | 2.02:1 on `--tape` (never text on tape); 5.60:1 as a fill under `--ink` text |
| `--green` | `#3E6B48` | Verifier green: the read-head line, verified marks, the lamp | ~1% | 4.65:1 on `--tape` — stamps, ticks and short labels only, never body text |

**Derived tokens.**

| Token | Hex | Derivation & role | Contrast |
|---|---|---|---|
| `--ink-soft` | `#57503F` | Ink at half pressure: margin notes, block metadata, captions | 6.03:1 on `--tape` — secondary text |
| `--amber-deep` | `#9A6202` | Stamp-pad amber: the RETRANSMIT REQUESTED stamp's lettering, error rules | 3.84:1 on `--tape` — large bold caps only (stamps are ≥14px, 700 weight) |
| `--buff-deep` | `#D9CCA6` | Aged tape: the strip's outer edges, the take-up bin zone in the footer | 1.20:1 — decorative ageing only |
| `--ink-faint` | `#8A8172` | A punch that didn't take: unpunched cell ghosts, disabled print | 2.90:1 — never text; ghosts and disabled states only, always paired with a label |

**Pairing rules.**

- Text is `--ink` on `--tape`, full stop. `--ink-soft` may set
  metadata and captions. Nothing else sets text on the tape.
- `--amber` is a *fill and a light*, never a letterform on tape:
  it appears as the highlight behind ink glyphs passing under the
  read-head (5.60:1, ink on amber), as the garbled cells of the
  failed block, and as the stamp's fill behind its lettering.
  Amber always means *the machine doubts this* — it is never a
  link colour, never a button, never decoration.
- `--green` is the verifier's colour and means *checked*: the
  read-head line, the ✓ after a verified checksum, the lamp. It
  is never spent on branding, headings or success confetti; a
  green element that has not verified something is a lie.
- `--shadow` draws holes and perforations — absences in the
  paper. It never carries meaning alone: a perforation is always
  also a gap in layout, a hole is always also a circle.

**Dark-mode behaviour.** There is none, and that is a designed
decision, not an omission: the tape is a physical object under
station light, and a "dark tape" would be a different artefact
that never existed. A visitor whose OS requests dark mode gets
the same buff tape — the theme documents this refusal in its
quality gate (§10) so a future builder does not "fix" it. The
one concession to environment: at night the *room around the
tape* (the page margin outside the strip, §4) deepens from
`--buff-deep` toward `--ink` under a `prefers-color-scheme: dark`
query — the desk gets darker; the paper does not.

## 3. Typography

**One typeface, no exceptions: IBM Plex Mono** — display sizes
included. The original entry's ruling stands verbatim:
*commitment to the bit.* A tape punch cannot set a serif, and a
second typeface anywhere on the page — a sans for buttons, a
display face for the hero — breaks the fiction that every glyph
on the page came through the same machine. Weights used: 400
(body print), 500 (block headers, table emphasis), 700 (the
punched headline, stamps). No italics: the punch has none; what
would be emphasis is done with weight, spacing, or a rule.

**The type scale** (rem, with the character grid as the real
unit — 1ch at body size = 9.63px at 16px/1.602):

| Role | Size | Weight | Line-height | Tracking | Case |
|---|---|---|---|---|---|
| Punched headline | 3.5rem (56px) | 700 | 1.05 | 0 | Upper, as punched |
| Block headline | 1.75rem (28px) | 700 | 1.15 | 0 | Upper |
| Section marker | 1.125rem (18px) | 500 | 1.3 | 0.08em | Upper |
| Body print | 1rem (16px) | 400 | 1.75 | 0 | Sentence |
| Margin print | 0.8125rem (13px) | 400 | 1.6 | 0.02em | Upper for labels |
| Data / checksum | 0.8125rem (13px) | 500 | 1.6 | 0.06em | Upper, hex in caps |
| Stamp | 0.875rem (14px) | 700 | 1.2 | 0.12em | Upper |

**Per-role rules.**

- **Display.** The punched headline (§6.2) is the only display
  setting on the page. It is set in the dot-matrix rendering of
  Plex Mono 700, not in a novelty dot font — the matrix is an
  effect applied to the real glyphs, and the real text sits
  underneath it for every non-visual reader.
- **Headings.** Block headlines are plain printed lines, upper
  case, preceded by their block number (`BLK 0014 — SPECIMEN
  CARDS`). A heading never centres; tape prints from the left
  margin, always.
- **Body.** 16px at 1.75 line-height: the line spacing is the
  tape's line pitch, and body copy is set in lines of ≤72ch so a
  line can pass under the read-head as one unit (§6.3). Body
  text never justifies — the punch prints ragged-right.
- **Data.** Every number on the page is tabular by construction
  (Plex Mono is monospace; figures align because the grid is the
  grid). Numbers are never kerned, never set in a "display"
  style, and never rounded for appearance (§1's law).
- **Labels and margin print.** Upper case, letterspaced, set in
  the margins the layout reserves (§4). A label is a thing the
  machine printed about the record — `TAPE: 042.0 M`, `CHK B7 ✓`
  — never marketing voice.

**The character grid is law.** Because the face is monospace,
layout is counted in characters: the content column is 72ch, a
block's header line is exactly one line, checksums sit at a
fixed column (ch 64–72) in every block header so the eye can
scan the tape's right edge and read the verification column as
one continuous strip. Any component that breaks the grid — a
proportional icon font, an image without a cell (§6.8), a button
that centres its label — is out of theme before it is ugly.

## 4. Layout language

**One strip.** The page is a single vertical tape, centred in
the viewport, running the full height of the document. There are
no columns beside it except the two margins the tape itself
carries: the left margin holds footage and block numbers, the
right margin holds the verifier lamp, parity ticks and stamps.
Everything the visitor reads is *on* the tape; the margins are
the reader machine's furniture, printed on the tape's own edges.

**Geometry (≥1200px).**

- Tape strip: 880px wide, ground `--tape`, edges aged with
  `--buff-deep` in the outer 24px each side.
- Sprocket columns: 40px each side, holes of 12px diameter on a
  24px pitch, drawn in `--shadow` with a 1px `--buff-deep` lower
  lip — a hole is a circle of shadow with light under it.
- Content column: 72ch centred in the remaining ~800px.
- Margins: the 56px between sprocket column and content column
  each side — left margin right-aligned (footage, block
  numbers), right margin left-aligned (lamp, ticks, stamps).
- The desk: outside the strip, the page ground is `--buff-deep`;
  the tape is an object lying on it, with a soft 24px shadow.

**The block is the unit of everything.** Content is divided into
blocks of one record each, and the block is simultaneously the
layout unit, the motion unit and the data unit: a block has a
number, a header line (`BLK nnnn — TITLE … CHK xx`), a body, and
a torn perforation at its foot. Blocks are separated by the
perforation — a dashed rule in `--shadow` across the full strip
width with 28px of air above and below — never by cards, shadows
or background changes. The tape is one surface; blocks are
divisions *in* it, not boxes *on* it.

**Spacing rhythm.** Vertical rhythm is the line pitch: 28px
(16px × 1.75). All spacing is a multiple of 7px (a quarter
pitch): block padding 28px, perforation air 28px, section gaps
84px (three full lines). Horizontal rhythm is the character:
margins and indents are counted in ch. Whitespace on this tape
is not emptiness — it is *unpunched tape*, and it is spent the
way the archive spent paper: generously between records (the
machine needed room to tear), never inside one. A block's
interior is dense; the air lives between blocks.

**Density rules.**

- One block, one record. If content needs two ideas, it is two
  blocks with two numbers and two checksums.
- The read-head (§6.3) must always have exactly one line under
  it: line-height and block padding are tuned so lines pass the
  centre singly, never two half-lines straddling the line.
- No element may extend past the sprocket columns. Images live
  inside tape cells (§6.8); tables live inside the 72ch column
  (§6.13); the stamp (§6.6) is the single licensed exception — a
  hand stamp lands where a hand lands, rotated 4°, overlapping
  the right margin by up to 18px, and it is the only thing on the
  page allowed to be crooked.

**Section choreography.** The page reads as the pass happened:
header block, station block, the record table, the block index,
the failure and its answer at the record's own position (BLK
0027 sits where 0027 fell, mid-page — not in a "reliability"
section), the remaining blocks, the pictures the pass carried,
the request block, and the end-of-tape block. The layout never
reorders the record for narrative convenience; §13 maps the full
sequence against the Pass Record's block ranges.

## 5. Full motion system

All scroll-driven motion on the tape runs from **one shared
requestAnimationFrame loop** reading a single lerped scroll
progress value (`--loop-lerp: 0.12` — heavy enough to feel like
paper, light enough never to lag the reader's hand). Nothing
else may drive scroll-scrubbed values: no per-element scroll
listeners, no CSS scroll-timelines competing with the loop, no
second rAF. The loop's one progress value is the tape's position
in the reader, and every scrubbed effect — the read-head's
highlight, the footage count, the sprocket-step, image
resolution — derives from it, so the whole machine can never
disagree with itself about where the tape is.

**Named easings** (the machine's five):

| Token | Curve | Used by |
|---|---|---|
| `--ease-ratchet` | `steps`-like custom: advance 70% in 60ms, catch, settle 40ms — cubic-bezier(0.2, 0.9, 0.25, 1) with a 3px overshoot | Spool-in (§6.1), block seating, tear feed-in (§6.10) |
| `--ease-punch` | cubic-bezier(0.7, 0, 0.3, 1), hard in, no bounce | Dot-matrix stamping (§6.2), punch click (§6.10) |
| `--ease-spool` | linear | Tape creep, footage counting, anything the machine does at constant speed |
| `--ease-stamp` | cubic-bezier(0.16, 1.4, 0.4, 1) — one overshoot, like a hand coming down | The verifier stamp (§6.1), the RETRANSMIT stamp (§6.6) |
| `--ease-settle` | cubic-bezier(0.25, 0.8, 0.35, 1) | Cell-lighting decay (§6.9), block tilt return (§6.9), lamp state changes |

**Watchdogs are part of the motion system, not an afterthought.**
Every armed animation registers a named timeout by which its
end-state is forced: spool-in 2000ms, headline punch 1600ms,
block print-in 1200ms, tear transition 900ms, form write 4000ms.
A watchdog that fires is invisible to the visitor — the content
simply *is* there, as it was in the DOM all along — and is
logged to the console as a machine note (`TAPE: WATCHDOG 1200
FIRED, BLK 0031 PRINTED UNPUNCHED`). The page is forbidden from
waiting on animation: the record prints on time or the machine
admits it printed late.

**Motion-term translation table** — every standard term, in the
tape's own language, applied or refused with its reason:

| Term | On the tape |
|---|---|
| Scroll-triggered reveals | Blocks print in as their header crosses the read-head's approach zone (§6.3) — a reveal is the machine reaching the block, never a fade for its own sake |
| Scroll-driven / scrub animation | The master mode: read-head highlight, footage, image resolution and the tear line of §6.6 are all scrubbed from the one progress value |
| Parallax | Three mechanical depths only: sprocket columns at 0.98×, print layer at 1.0×, tape-warp grain at 1.02× — paper layers, never scenery |
| Pinned sections | The read-head pins at viewport centre for the entire page (§6.3); nothing else pins — a tape has one fixed part, the reader |
| Smooth scrolling | Deliberately *roughened*: the sprocket-step (§6.4) quantises advance into 3px catches over the native smooth scroll |
| Progress indicator | Footage (§6.5): metres spooled, printed in the margin — progress as physical record consumed |
| Staggered reveals | Blocks stagger in spool order, cell by cell within the headline (§6.2), never in decorative cascades |
| Masked line reveals | Refused as masks; replaced by the read-head's line lighting (§6.3) — a line is revealed by being *read*, lit amber cell by cell, not by a clip-path wipe |
| Blur-to-sharp | Refused for text (punched print is never blurry — it is punched or it is not); applied to images only, as dot-matrix resolution (§6.8) |
| Kinetic typography | Refused as motion; the headline's kinetics are *production*, not movement — letters are stamped into existence (§6.2) and then never move again |
| Marquee | Refused: a tape already moves; a marquee would be a second, lying motion. The tape creep (§6.7's companion) is the only continuous travel |
| Animated counters | Footage (§6.5) and the block counter count in punched numerals, at spool speed, from the one progress value |
| SVG line-draw | Exactly one: the tear line of the parity pair (§6.6) draws itself as the pair centres |
| Image scale-in-frame | Dot-matrix images resolve coarse→fine and settle 1.03 → 1.0 as they pass the read-head (§6.8) |
| Hover micro-interactions | Cell-lighting sweep (§6.9) and the 1° platen tilt (§6.9) — inspection as a machine pass |
| Magnetic / tilt | Magnetic refused (paper does not attract a hand); tilt kept at the medium's truth: max 1°, tape lifting off the platen |
| Custom cursor | Refused absolutely — normal system cursor only; the machine does not follow the visitor's hand |
| Skeleton loading | Blank tape that punches in as data arrives (§6.15) — the skeleton is unpunched paper, not grey boxes |
| Page transitions | The tear (§6.10): the strip tears at a perforation and the next strip feeds in |
| Reduced motion | The tape lies fully spooled and printed; every variant is specified per element in §6 |

**Ambient loops — exactly two are licensed.** (1) The verifier
lamp's blink (§6.7): on 900ms / off 300ms while the tape moves,
steady while it rests. (2) The tape creep: with the page idle
and a block centred, the strip drifts up by one sprocket pitch
(24px) over 6s under `--ease-spool`, pauses 4s, and returns —
paper breathing in the reader, amplitude small enough that no
line under the read-head ever changes during it. Any third
ambient loop — a blinking cursor, a pulsing badge, a rotating
anything — is out of theme. Motion on this page is the machine
working; when the machine is not working, the page is still.

## 6. Signature elements

Eighteen elements: the original ten, deepened, plus eight
page-family elements (§6.11–§6.18) the original entry implied
but never specified. Every figure any element prints comes from
the Pass Record (§6.17); an element that needs a number the
record does not declare is redesigned until it doesn't.

### 6.1 Spool-in hero

- **What & why.** On load, the tape feeds into the reader from
  the left: the strip slides in with a mechanical ratchet —
  advance, catch, advance — while sprocket holes punch along
  both edges in sequence, until the header block (BLK 0001)
  seats under the read-head and a verifier stamp lands on it.
  It belongs because arrival on this site is a machine operation:
  before the visitor reads a word, the record has been *loaded*,
  and the loading is done to the content itself, not around it.
- **Structure.** The hero is the tape's first 4.0 m: BLK 0001's
  block element inside the strip. The strip is a DOM element
  translated on X by the loop; the sprocket holes are two
  repeating-linear-gradient columns whose punch-in is a mask
  sweep (holes exist in the DOM as a background from the start;
  the "punching" is a `--shadow` overlay retracting hole by
  hole). The stamp is an inline SVG text-on-path-free stamp:
  a bordered, rotated (4°) group reading `VERIFIED — KIRUNA-2`
  in `--green`, opacity-armed by script only.
- **Motion spec.** Trigger: load, after first paint. Strip
  advance: 8 ratchet steps over 1200ms under `--ease-ratchet`,
  each step ~110px with a 40ms catch; holes punch in sequence
  with the advance, one pitch (24px) per 18ms; the block seats
  with a final 3px settle over 120ms; the stamp lands at
  t=1350ms, 180ms under `--ease-stamp`, rotating from 7° to its
  resting 4°. Total ceremony: 1530ms, skippable by any scroll
  or keypress (the tape snaps to seated).
- **States.** Loading (strip off-left, holes unpunched) /
  spooling / seated (stamp landed, hero at rest) / skipped
  (visitor interrupted — seated instantly, stamp printed at
  full opacity, no apology, no replay).
- **Content merge.** The hero *is* BLK 0001 — the pass header
  with the satellite's name, the station, the date and
  `CHK B7 ✓`. The spool-in does not decorate a hero; it delivers
  the record's first block into the reader, and the stamp that
  lands on it is the verification the block's own header claims.
- **Failure fallback.** Watchdog at 2000ms from arm: if the
  strip has not seated, transforms are cleared and the stamp
  prints — the hero is simply there. No-JS: the strip ships
  seated, holes punched, stamp printed; the script performs the
  rewind only in the same frame it registers the watchdog.
- **Reduced-motion variant.** No spool, no punch sequence, no
  stamp landing: the hero ships seated and stamped, exactly as
  the no-JS state. The load is a non-event; the record is
  already in the reader.
- **Performance budget & mobile variant.** One transform on one
  element plus a mask sweep; ≤0.3ms/frame, no layout after the
  first frame. Mobile (<768px): 5 ratchet steps over 800ms,
  stamp lands at t=950ms — the ceremony shortens, it does not
  change kind.
- **Choreography timeline (v2).** t=0 first paint (strip
  off-left, hero text already in DOM) → t=0–1200ms 8 ratchet
  steps, holes punching in sequence → t=1200ms block seats,
  3px settle → t=1350ms stamp begins → t=1530ms stamp at rest,
  hero live → watchdog deadline t=2000ms passes unused.
- **State matrix (v2).** *Rest:* seated, stamped. *Hover:* none
  — the hero is a record, not a control. *Focus:* the hero's
  one link (the station name, to §6.11's index) takes the
  standard 2px `--ink` outline at 3px offset. *Active:* n/a.
  *Scrolled-past:* the stamp and block remain printed; nothing
  re-spools on return. *Disabled:* n/a. *Touch:* identical;
  a tap during spool-in skips to seated, as a keypress does.
- **Breakpoints (v2).** ≥1200px: full 880px strip, 8 steps.
  768–1199px: strip 92vw, 6 steps over 1000ms. <768px: strip
  100vw with sprocket columns narrowed to 28px, 5 steps over
  800ms, stamp scaled 0.85.
- **Edge cases & failure modes (v2).** *Slow network:* the hero
  is inline DOM and CSS — it spools before any image arrives;
  nothing in the ceremony waits for an asset. *Visitor reloads
  mid-spool:* the ceremony restarts; it is 1.5s and skippable,
  never persisted as "already seen" — the archive does not
  remember you. *Very tall hero content:* BLK 0001 is fixed by
  the record; if a build's header block exceeds 80vh, the
  read-head seats on its third line and the stamp lands on the
  header line, never mid-body.
- **Accessibility spec (v2).** The ceremony is `aria-hidden`
  decoration over real text: the headline and block are in the
  accessibility tree from first paint, in final position. The
  stamp's SVG carries `role="img"` and `aria-label="Verified,
  Kiruna-2 station"`. Focus is never moved by the spool-in.
  Skip-by-interaction includes keyboard: any key seats the tape.
- **Tokens consumed (v2).** `--tape`, `--ink`, `--shadow`,
  `--green`, `--ease-ratchet`, `--ease-stamp`, `--loop-lerp`
  (0.12), `--dur-spool-in` (1200ms), `--dur-watchdog-spool`
  (2000ms).

### 6.2 The punched headline

- **What & why.** The headline does not fade, slide or wipe in:
  it is *punched*. Each character cell fills its 5×7 dot-matrix
  — dots stamping in over ~40ms per letter, staggered left to
  right — so the title becomes legible the way output becomes
  legible, one struck character at a time. It belongs because
  the headline is the machine's own output: the biggest text on
  the page must obey the medium most strictly, or the theme is a
  costume.
- **Structure.** An `<h1>` with real text (`PASS 0417 — HELIOS-3,
  AS RECEIVED`), over which the script builds a dot-matrix
  overlay: for each character, a 5×7 grid of dots (CSS circles
  in a per-character inline SVG, generated from a fixed 5×7
  bitmap table for A–Z, 0–9 and the five punctuation marks the
  record uses). The overlay is `aria-hidden`; the real text is
  visually hidden *only* while its character's matrix is
  incomplete, and the hiding is done by the overlay covering it,
  never by removing it from the tree. Unmapped characters
  (anything outside the table) print as plain glyphs — the
  machine punches what it can and the record does not pretend
  otherwise.
- **Motion spec.** Trigger: the spool-in's seat (§6.1), t=1200ms
  in the load ceremony. Per character: dots stamp in 3 passes
  (columns 1–2, 3–4, 5) over 40ms under `--ease-punch`;
  stagger 26ms per character; the headline is 24 characters, so
  the last dot lands at ~1050ms after trigger. A completed
  character never changes again — punched is punched.
- **States.** Unpunched (overlay empty, real text covered by
  blank cells) / punching (partial matrices) / punched (final,
  permanent). There is no hover, focus or active state: the
  headline is output, not a control.
- **Content merge.** The headline is BLK 0001's title line — the
  same line its block header counts and checksums. The matrix
  is not a headline *effect*; it is the headline's encoding,
  the same 5×7 the parity block's garbling (§6.6) corrupts, so
  the failure later in the page is legible as damage to *this*
  system.
- **Failure fallback.** Watchdog at 1600ms from trigger: any
  character not yet punched prints as its plain glyph and the
  overlay for it is removed. No-JS: no overlay is ever built;
  the headline is a plain printed line, full stop.
- **Reduced-motion variant.** The headline ships punched: the
  overlay, if built at all, is built complete. Nothing stamps.
- **Performance budget & mobile variant.** 24 characters × 35
  dots = 840 static dots, built once, animated by class toggles
  in 3 passes per character; build cost ≤8ms on a mid phone,
  per-frame cost zero between staggers. Mobile (<768px): the
  headline wraps to two lines at the space before `AS RECEIVED`;
  the matrix cell shrinks to 4px dots on a 5px pitch and the
  stagger tightens to 20ms — the line is shorter per row, the
  ceremony keeps its pace.
- **Choreography timeline (v2).** Seat (t=0) → t=26ms first
  character's first column stamps → characters complete at
  26ms intervals, 40ms each → t≈1050ms final character (`D`)
  completes → headline permanent → watchdog deadline t=1600ms
  passes unused.
- **State matrix (v2).** *Rest:* punched, permanent. *Hover:*
  none. *Focus:* the `<h1>` is not focusable. *Active:* n/a.
  *Scrolled-past:* unchanged — scrolling away and back never
  re-punches. *Disabled:* n/a. *Touch:* identical; no
  touch-specific behaviour exists or is needed.
- **Breakpoints (v2).** ≥1200px: one line, 56px setting, 6px
  dots. 768–1199px: one line at 44px if the strip allows, else
  wraps at the same break. <768px: two lines, 34px setting,
  4px dots; the block header's checksum column (§3) holds its
  position regardless.
- **Edge cases & failure modes (v2).** *A longer headline in a
  real build:* the matrix table caps the ceremony at 40
  characters; beyond that, characters punch in pairs (stagger
  halves) so the ceremony never exceeds ~1200ms. *Font not yet
  loaded:* the overlay is positioned in ch units against the
  real text; if Plex Mono swaps in late, the matrix rebuilds
  once on `document.fonts.ready` — before the seat trigger, or
  the watchdog prints plain glyphs. *A character outside the
  bitmap table:* prints plain, mid-headline, without ceremony —
  declared behaviour, not a bug.
- **Accessibility spec (v2).** Screen readers meet only the real
  `<h1>` text, once, unbroken — the overlay is `aria-hidden`
  and the per-character covering never enters the tree. The
  punching is not announced. Contrast of completed dots: `--ink`
  on `--tape`, 11.33:1, identical to print.
- **Tokens consumed (v2).** `--tape`, `--ink`, `--ease-punch`,
  `--dur-punch-char` (40ms), `--dur-punch-stagger` (26ms),
  `--dur-watchdog-punch` (1600ms), `--matrix-dot` (6px).

### 6.3 The read-head line

- **What & why.** A fixed horizontal line at viewport centre —
  verifier green, 2px, with bracket ends — spans the tape for
  the entire page. Whatever line of print is passing under it is
  *being read*: its character cells light amber as they cross,
  line by line, top to bottom of the record. It belongs because
  it makes reading a machine state the visitor can see: the tape
  does not merely scroll, it is *read*, and the line is the
  reader — the one fixed part in a page where everything else
  moves.
- **Structure.** A `position: fixed` element at `top: 50vh`,
  width equal to the strip, pointer-events none: a 2px rule in
  `--green` at 55% opacity, with 14px bracket ticks at both
  ends dropping 8px below the line. The lighting is done on the
  text side: the loop computes which line box straddles the
  centre for each block in view and toggles a `.under-head`
  class whose cells render on an `--amber` highlight behind the
  glyphs (ink on amber, 5.60:1). Cell-level lighting uses a
  background gradient sized in ch, positioned by the loop's
  progress within the line — no per-character DOM.
- **Motion spec.** Trigger: scroll, continuous, from the shared
  loop. As a line enters the centre band (±14px, half the line
  pitch), its highlight sweeps left to right across 72ch over
  the time the line spends crossing the band — at reading speed
  roughly 300–600ms — under `--ease-spool` (linear: the head
  does not ease, it *tracks*). A line fully past dims its
  highlight over 200ms under `--ease-settle`. Lines never light
  twice in one pass direction; scrolling back up re-lights them
  downward-crossing only — the head reads in the direction of
  travel.
- **States.** Idle (page at rest: the line under the head holds
  its highlight at 70% — the machine is parked on that line) /
  reading (scrolling: sweeps active) / between blocks (the head
  crosses a perforation: the line shows only its brackets and
  the footage margin prints `—` for the current line) / at end
  (footer reached: the line rests under the END OF RECORD stamp,
  §6.16).
- **Content merge.** The highlight is not an effect applied to
  text; it *is* the reading position, and two other elements
  swear by it: the block counter (§6.5) increments when a
  block's header crosses the line, and dot-matrix images (§6.8)
  resolve as they cross it. Remove the line and the page loses
  its clock — every other timing in the theme is referenced to
  this one.
- **Failure fallback.** Watchdog: the line is CSS-fixed and
  present with no script at all — only the *lighting* is
  script-driven. If the loop dies, the line remains, unlit text
  passes under it, and the page is a tape beside a parked
  reader: fully readable, honestly degraded. No-JS: identical.
- **Reduced-motion variant.** No sweep: the line under the head
  is highlighted as a whole, statically, updating by line as the
  visitor scrolls (class toggles only, no gradient travel). The
  reading position is still shown; it just doesn't perform.
- **Performance budget & mobile variant.** One class toggle per
  line-crossing plus one gradient position update per frame for
  the single active line; ≤0.2ms/frame. Mobile (<768px): the
  line spans the full strip width, brackets shorten to 10px,
  and the centre band widens to ±18px — thumbs scroll faster
  than mice, and the head must not flicker between lines.
- **Choreography timeline (v2).** Line enters band → highlight
  begins at ch 0 → sweeps with scroll progress → line centred:
  fully lit → line exits band: highlight holds 70% while the
  line is the parked line → next line enters: previous dims
  over 200ms as the new sweep begins.
- **State matrix (v2).** *Rest:* parked line lit at 70%.
  *Hover:* none — the line ignores the pointer entirely.
  *Focus:* when focus lands on an element (a link, a field),
  the head does not move to it; the focused element's own
  outline (§6.11, §6.14) does that work. *Active:* n/a.
  *Scrolled-past:* lines above rest unlit, printed. *Disabled:*
  n/a. *Touch:* identical; the band is wider, per the budget
  line above.
- **Breakpoints (v2).** ≥1200px: line spans the 880px strip,
  band ±14px. 768–1199px: spans 92vw strip, band ±14px.
  <768px: spans 100vw, band ±18px, brackets 10px.
- **Edge cases & failure modes (v2).** *Jump scroll (End key,
  anchor link):* the loop's lerp settles within ~400ms; lines
  skipped are never lit retroactively — the head read none of
  them and does not pretend it did. *A block taller than the
  viewport:* its lines light one by one as they cross; the
  block counter waits for the *header* line specifically.
  *Perforation exactly at centre:* the between-blocks state
  shows; footage prints the last completed block — the machine
  never claims a block it is between.
- **Accessibility spec (v2).** The line and its lighting are
  `aria-hidden` presentation: reading position is fully
  available from the document's own order, and no information
  exists *only* in the highlight. The highlight never reduces
  contrast (ink on amber 5.60:1 ≥ the 4.5:1 floor for the 16px
  body). Nothing flashes: the sweep is a gradient translation,
  not a blink.
- **Tokens consumed (v2).** `--green`, `--amber`, `--ink`,
  `--loop-lerp` (0.12), `--head-band` (28px), `--ease-spool`,
  `--ease-settle`.

### 6.4 Sprocket-step advance

- **What & why.** The tape does not glide. Layered over the
  browser's smooth scroll, the strip's advance is quantised
  into tiny ratcheted catches — the content moves in ~3px steps
  with a 40ms settle — strongest near block boundaries, where
  the machine works hardest. It belongs because the scroll
  itself should feel sprocketed: the visitor's hand is on the
  take-up spool, and the medium's mechanics govern the reading
  rhythm, not the OS's easing curve.
- **Structure.** Not a scroll hijack: the document scrolls
  natively, and the loop applies a small `translateY` offset to
  the strip's inner wrapper equal to the quantisation error —
  the difference between the lerped scroll position and that
  position rounded to the 3px step grid — so the *print layer*
  catches while the scroll position itself stays truthful.
  Scrollbars, find-in-page, anchor jumps and assistive scrolling
  all operate on the real position; only the rendered paper
  ratchets. Amplitude is modulated by distance to the nearest
  perforation: full 3px within 200px of a block boundary,
  tapering to 1px mid-block.
- **Motion spec.** Trigger: scroll, continuous. Step: 3px
  catches; each catch settles over 40ms under `--ease-ratchet`.
  The quantisation follows the loop's lerped value (0.12), so a
  fast flick produces a run of catches — the machine rattling —
  and a slow read produces distinct, countable steps near
  boundaries. Above a scroll velocity of ~2400px/s the step
  amplitude fades to 0 (the machine cannot ratchet faster than
  its pawl; pretending otherwise is noise).
- **States.** Resting (no offset) / catching (mid-step) /
  free-running (velocity above the fade threshold — offset 0,
  print layer smooth) / returning (scrolling up: identical
  quantisation — the pawl works both ways on this reader).
- **Content merge.** The step is keyed to the record's own
  divisions: it strengthens at perforations, the places where
  the tape is meant to tear. The visitor feels the block
  structure through the scroll before they ever read a block
  number — the record's anatomy is in the hand, not just the
  eye.
- **Failure fallback.** Watchdog: the offset is written by the
  loop each frame and defaults to 0; if the loop dies the last
  written offset is cleared by the loop's own death handler and
  by a 500ms no-frame watchdog that zeroes it. A stuck offset of
  ≤3px would in any case misalign nothing — content is never
  positioned *by* the offset, only nudged. No-JS: no offset ever.
- **Reduced-motion variant.** Removed entirely. Scrolling is
  native and smooth; the tape's printed perforations still mark
  the boundaries the step would have announced.
- **Performance budget & mobile variant.** One transform write
  per frame on one wrapper; ≤0.1ms/frame. Mobile (<768px): step
  reduces to 2px and the boundary zone to 140px — touch scroll
  is already inertial and heavily damped, and a full 3px catch
  reads as jank rather than machinery.
- **Choreography timeline (v2).** Scroll begins → loop lerps →
  quantisation error computed per frame → wrapper offset steps
  in 3px catches, 40ms settle each → velocity crosses 2400px/s:
  amplitude fades over 120ms → scroll ends: final catch settles,
  offset returns to 0 within 80ms.
- **State matrix (v2).** *Rest:* offset 0. *Hover:* n/a.
  *Focus:* keyboard scrolling (arrows, Page Down, space)
  ratchets identically — the pawl does not care what drives the
  spool. *Active:* n/a. *Scrolled-past:* n/a (it is a property
  of motion, not of position). *Disabled:* n/a. *Touch:*
  2px steps, per the budget line.
- **Breakpoints (v2).** ≥1200px: 3px step, 200px boundary zone.
  768–1199px: 3px step, 180px zone. <768px: 2px step, 140px
  zone, velocity fade at 1800px/s.
- **Edge cases & failure modes (v2).** *Browser with its own
  scroll smoothing off:* the quantisation still applies — it
  reads the position, not the input. *Overscroll at the page
  ends:* offset clamps to 0 in the rubber-band zone so the tape
  never detaches from the strip. *A visitor who hates it:* the
  step is ≤3px and dies under reduced-motion; there is no
  separate toggle because the amplitude is below the threshold
  of obstruction — verified in the quality gate's scroll-feel
  check (§10).
- **Accessibility spec (v2).** The effect is purely visual,
  sub-3px, and never alters scroll position, focus order or
  reading order. It is fully removed under
  `prefers-reduced-motion` and must also be removed if the
  visitor's browser reports a vestibular-risk signal the build
  can detect. Screen readers are unaffected — the DOM never
  moves.
- **Tokens consumed (v2).** `--loop-lerp` (0.12), `--ease-ratchet`,
  `--step-size` (3px), `--step-settle` (40ms), `--step-zone`
  (200px).

### 6.5 Footage progress

- **What & why.** In the left margin, the machine prints how
  much record the visitor has consumed: `TAPE: 042.0 M`, in
  punched numerals, counting with the scroll — plus the current
  block number, `BLK 0011`, beneath it. It belongs because
  progress on a tape is physical: not 22% of a page but 42
  metres of paper that have passed through the reader and are
  now in the bin. The number is also a promise the footer keeps
  (§6.16): spool the whole record and the counter stops at
  exactly 196.0 M, the record's declared length.
- **Structure.** A margin element, `position: sticky` within the
  strip's left margin at read-head height, containing two lines
  of margin print: the footage line and the block line. Values
  are real text nodes updated by the loop (throttled to when
  the printed value changes — the footage prints to 0.1 M, so
  at most one update per 0.1 m of travel). The numerals are
  styled as punched: the same dot-matrix treatment as §6.2 at
  small size, applied as a static texture — the digits do not
  re-punch on change; a counting machine's digits are wheels,
  not stamps, and they roll.
- **Motion spec.** Trigger: scroll scrub, from the loop's
  progress value mapped linearly to the record's geometry:
  footage = progress × 196.0 M, printed to one decimal. The
  block number increments in the frame the block's header line
  crosses the read-head (§6.3) — a discrete event, never
  interpolated: the machine is *in* a block or between blocks
  (between blocks, the block line prints the last completed
  block and the footage keeps counting — paper moves even
  between records). Digit changes roll over 120ms under
  `--ease-spool`.
- **States.** At head (0.0 M, BLK 0001) / spooling (counting) /
  between blocks (footage live, block held) / at end (196.0 M,
  BLK 0048, and a third line appears: `END OF TAPE` in
  `--ink-soft`) / returned (scrolling up counts *down* — the
  tape rewinds through the reader and the footage honestly
  decreases; this machine has no "furthest read" vanity metric).
- **Content merge.** The counter's maximum, its block count and
  its increments are the Pass Record's own figures (§6.17) —
  196.0 M and 49 blocks, no others exist. A build whose content
  overruns its record finds out here first: the counter is the
  record's geometry made visible, and §10's gate reconciles the
  two.
- **Failure fallback.** Watchdog: the values are text; if the
  loop dies they freeze at their last true reading — a stopped
  counter on a stopped tape, wrong only about a page the visitor
  can still read in full. No-JS: the margin prints the record's
  totals statically (`TAPE: 196.0 M — 49 BLOCKS`) — the archive
  label, not a counter.
- **Reduced-motion variant.** Values update in whole metres
  (196 steps instead of 1960) with no digit roll — the
  information is identical, the performance of counting is not.
- **Performance budget & mobile variant.** ≤1 text update per
  0.1 m of scroll; negligible. Mobile (<768px): the left margin
  is too narrow for the sticky counter, so the footage line
  moves into the read-head's left bracket (§6.3) as a single
  line `042.0 M` — same value, same source, smaller furniture.
- **Choreography timeline (v2).** Scroll → progress lerps →
  footage value crosses a 0.1 M boundary: digit roll 120ms →
  block header crosses the head: block line increments in the
  same frame, parity tick check (§6.10) updates → footer enters:
  counter lands on 196.0 M exactly as the END OF RECORD block
  centres.
- **State matrix (v2).** *Rest:* holding its reading. *Hover:*
  none. *Focus:* not focusable; the values are also printed in
  the footer (§6.16) for anyone who needs them in the document
  flow. *Active:* n/a. *Scrolled-past:* n/a. *Disabled:* n/a.
  *Touch:* identical values; placement per the budget line.
- **Breakpoints (v2).** ≥1200px: two-line sticky counter in the
  left margin. 768–1199px: same, margin print at 12px. <768px:
  single-line footage inside the read-head bracket; block
  number prints in each block's own header (where it always
  was) and the sticky block line is cut.
- **Edge cases & failure modes (v2).** *Content images loading
  late and shifting layout:* the progress mapping is computed
  from document geometry each second by the loop's slow tick,
  so the footage-to-position mapping self-corrects; image cells
  (§6.8) reserve their height in ch-based aspect boxes precisely
  to keep this rare. *A block added in a real build:* the record
  (§6.17) must be re-declared first — the counter reads the
  record, not the DOM, so an undeclared block makes the gate
  fail loudly rather than the counter lie quietly.
- **Accessibility spec (v2).** The counter is `aria-hidden` —
  progress is fully available from the document itself (block
  headers carry their numbers in the flow). A visually hidden
  status in the footer states the totals for assistive readers.
  Digits are `--ink` on `--tape`, 11.33:1.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--tape`,
  `--loop-lerp` (0.12), `--ease-spool`, `--tape-total` (196.0 M),
  `--block-total` (49).

### 6.6 The parity-error block

- **What & why.** Mid-page, exactly where the record puts it,
  BLK 0027 is wrong: flipped-bit characters garble its lines,
  amber shows through the damaged cells, and a hand stamp —
  rotated 4°, the page's only crooked thing — reads
  RETRANSMIT REQUESTED. Immediately after it, BLK 0027R prints
  the same record clean, its checksum verified, and a tear line
  draws itself across the perforation between the pair as they
  centre. It belongs because reliability on this site is not
  claimed, it is *performed inside the data*: the archive kept
  the corruption, stamped it, and answered it with more tape —
  the theme's law (§1) with its sleeves rolled up.
- **Structure.** Two consecutive block elements. BLK 0027's body
  text is the true text with a declared garble map: specific
  character positions (listed in the record, §6.17 — 23
  characters) render as their bit-flipped counterparts from the
  5×7 matrix table (§6.2), shown as damaged matrix glyphs on an
  `--amber` cell wash. The garbling is *rendering*, not data:
  the DOM text of BLK 0027 is the true text (the archive's
  catalogue holds the reading; the tape shows the damage), and
  a visually hidden note states the block failed its checksum.
  The stamp is an inline SVG, `--amber-deep` lettering on an
  `--amber` wash border, `role="img"`. Between the blocks, the
  perforation carries an SVG path — the tear line — whose
  stroke is scrubbed by the loop. BLK 0027R's header prints
  `CHK 9A ✓` in `--green`; BLK 0027's prints `CHK 4F ✗ 9A` —
  the punched checksum, a cross, and the recomputed value.
- **Motion spec.** Trigger: scroll — the pair entering the
  centre third. The stamp lands when BLK 0027's header crosses
  the read-head: 180ms under `--ease-stamp`, from 7° to 4°,
  scale 1.15 → 1. The tear line draws over the pair's passage
  through the centre band, scrubbed (stroke-dashoffset from the
  loop's progress), completing exactly as BLK 0027R's header
  reaches the head. The garbled cells do not animate — damage
  is static; only the machine's *response* (stamp, tear line)
  moves.
- **States.** Approaching (pair printed, stamp unlanded) /
  stamped (stamp down, tear line drawing) / answered (0027R
  under the head, its ✓ lit by the head's amber like any line)
  / passed (all static print; scrolling back re-draws nothing —
  the stamp stays down and the tear line stays drawn: the
  machine does not un-answer).
- **Content merge.** This is the record's own event at the
  record's own position — block 27 of 49, after 104.0 M of tape.
  It is not a "trust section": remove the pair and the footage
  counter (§6.5), the record (§6.17) and the footer's totals
  (§6.16) all stop reconciling. The theme's credibility is
  arithmetic, and this pair is where the arithmetic is hardest.
- **Failure fallback.** Watchdog at 1200ms from the pair's first
  entry into the viewport: stamp prints at rest, tear line
  draws complete. No-JS: identical end state — stamp printed,
  line drawn, garble rendered by the static matrix glyphs (they
  are inline SVG, not script output). The pair is fully legible
  as an event with no motion at all.
- **Reduced-motion variant.** Stamp printed at rest from the
  start; tear line fully drawn; the pair reads as pure print.
  The garble, the stamp and the answer — the *content* of the
  element — are untouched.
- **Performance budget & mobile variant.** One SVG stroke update
  per frame while the pair is in the centre band; ≤0.15ms/frame.
  Mobile (<768px): the stamp scales to 0.8 and its overlap into
  the margin is capped at 8px so it never covers body text on a
  narrow strip; the tear line and garble are unchanged.
- **Choreography timeline (v2).** Pair enters viewport → BLK
  0027 header crosses head: stamp falls (180ms) → pair crosses
  centre band: tear line draws, scrubbed → BLK 0027R header
  crosses head: its ✓ line lights, tear line complete → pair
  passes: all print, permanently.
- **State matrix (v2).** *Rest:* stamped, drawn, answered.
  *Hover:* hovering either block runs §6.9's cell-lighting over
  it — including over the garbled cells, which light like any
  cells: the head reads damage without flinching. *Focus:* the
  pair contains no controls. *Active:* n/a. *Scrolled-past:*
  static, as printed. *Disabled:* n/a. *Touch:* identical;
  no tap behaviour on the pair itself.
- **Breakpoints (v2).** ≥1200px: stamp at full size, 18px margin
  overlap licensed. 768–1199px: stamp 0.9 scale, 12px overlap.
  <768px: stamp 0.8 scale, 8px overlap, tear line stroke 1.5px.
- **Edge cases & failure modes (v2).** *A build tempted to add
  a second error block:* refused by the record — exactly one
  failure exists (§6.17), and §10's gate counts garble maps.
  Two failures would make the archive look careless; one makes
  it look honest. *The garble map drifting from the text in an
  edit:* the map is position-based, so the gate re-renders the
  block and diffs the flipped positions against §6.17's list.
  *Print stylesheets:* the pair prints with stamp and garble —
  a paper copy of the page keeps the evidence.
- **Accessibility spec (v2).** BLK 0027's DOM text is the true
  text; a visually hidden prefix announces "Block 27: checksum
  failed; garbled as received. Corrected text follows in block
  27R." The stamp's SVG is labelled. The amber wash behind
  damaged glyphs keeps ink-on-amber contrast at 5.60:1 — the
  damage is visible without the text becoming unreadable, to
  anyone, in any state.
- **Tokens consumed (v2).** `--amber`, `--amber-deep`, `--green`,
  `--ink`, `--ease-stamp`, `--loop-lerp` (0.12),
  `--dur-watchdog-pair` (1200ms), `--stamp-rotate` (4deg).

### 6.7 The verifier lamp

- **What & why.** A small green lamp lives in the right margin
  at read-head height. While the tape is moving it blinks in a
  slow verify rhythm — on 900ms, off 300ms — and when the reader
  stops, it holds steady. It belongs because it is the machine's
  heartbeat made visible: the lamp's state *is* the tape's
  state, and a visitor glancing at the margin knows whether the
  record is being checked or is at rest without reading a word.
- **Structure.** A DOM element in the right margin, sticky at
  50vh beside the read-head's right bracket: a 10px circle in
  `--green` with a 1px `--ink-soft` bezel ring and a printed
  label beneath, `VERIFY`, in margin print. The blink is a
  class toggle driven by the loop's clock, not a CSS animation
  — the loop owns it so the lamp can never blink out of sync
  with the machine's actual state (a CSS loop would keep
  "verifying" while the tab is throttled and the tape is still;
  the loop knows better).
- **Motion spec.** Trigger: scroll state + the loop's clock.
  Moving (scroll velocity > 4px/s sustained 100ms): blink
  cycle 1200ms — on 900ms, off 300ms, transitions 60ms under
  `--ease-settle` (a lamp fades; it does not strobe). Stopping:
  the lamp completes its current on-phase and holds steady from
  the next on-beat — it never freezes mid-blink. Idle 30s: the
  lamp dims to 40% (the machine is awake but unattended) and
  returns to full on the next scroll or hover of the strip.
- **States.** Verifying (blinking) / holding (steady on) /
  unattended (steady at 40%) / at end (footer reached: three
  slow blinks — on 600 / off 600, ×3 — then steady: the
  machine signing off the record) / failed-loop (if the loop
  dies, the lamp freezes in whatever state it held — see
  fallback).
- **Content merge.** The lamp verifies *this* record: its
  rhythm is the rhythm §6.3's read-head and §6.5's counter
  obey, and its sign-off sequence at the end is triggered by
  the same footage value (196.0 M) that stops the counter. It
  is not a status widget for the website; nothing about the
  site (uptime, availability, offers) may ever be wired to it.
- **Failure fallback.** Watchdog: if the loop dies, a 1500ms
  no-frame watchdog sets the lamp to steady-on and prints a
  console machine note. A lamp frozen mid-blink would claim the
  machine is checking when it is not — the one lie this element
  must never tell. No-JS: the lamp is printed steady-on with its
  label; a static lamp beside a static tape is the truth.
- **Reduced-motion variant.** No blinking, ever: the lamp is
  steady while the page is open, and its label gains a state
  word updated without animation — `VERIFY` while scrolling,
  `HELD` at rest — so the information survives the removal of
  the blink. (This is also the photosensitivity ruling: 900/300
  is far below flash thresholds, but the theme does not argue
  with a visitor's setting.)
- **Performance budget & mobile variant.** One class toggle per
  cycle; zero per-frame cost. Mobile (<768px): the right margin
  disappears, so the lamp moves into the read-head's right
  bracket (§6.3), label cut — the lamp alone, 8px, same rhythm,
  same states.
- **Choreography timeline (v2).** Scroll starts → 100ms
  sustained velocity → lamp enters blink on the next on-beat →
  scroll stops → current on-phase completes → steady → 30s
  idle: dims to 40% → footage reaches 196.0 M: three slow
  blinks → steady, page done.
- **State matrix (v2).** *Rest:* steady (or 40% unattended).
  *Hover:* hovering the strip returns an unattended lamp to
  full; hovering the lamp itself does nothing — it is not a
  control. *Focus:* not focusable. *Active:* n/a.
  *Scrolled-past:* n/a (it is fixed furniture). *Disabled:*
  n/a. *Touch:* identical; scroll state comes from touch
  scrolling the same way.
- **Breakpoints (v2).** ≥1200px: lamp + `VERIFY` label in the
  right margin. 768–1199px: lamp + label, label at 11px.
  <768px: lamp only, in the read-head bracket.
- **Edge cases & failure modes (v2).** *Background tab:* rAF
  throttles, the loop's clock is wall-clock based, so on return
  the lamp resumes in the correct phase for a stopped tape
  (steady) rather than mid-blink. *Rapid scroll-stop-scroll:*
  the 100ms sustain rule prevents blink chatter; the lamp
  changes state at most twice per second. *The sign-off blinks
  while the visitor scrolls back up:* the sequence cancels and
  normal state resumes — sign-off is for a reader who stays.
- **Accessibility spec (v2).** `aria-hidden`: the lamp is a
  visual state echo, and its information (moving / held) is a
  nicety, not content. Under reduced motion the label's state
  word is *not* put in a live region — a screen reader user
  gains nothing from hearing "held" forty times a page. The
  lamp's green on tape is 4.65:1, legible as an object though
  it carries no text.
- **Tokens consumed (v2).** `--green`, `--ink-soft`, `--tape`,
  `--ease-settle`, `--lamp-on` (900ms), `--lamp-off` (300ms),
  `--dur-watchdog-loop` (1500ms).

### 6.8 Dot-matrix images

- **What & why.** Pictures on this tape exist in the tape's
  encoding: every image prints as a dot-matrix halftone inside a
  tape cell, resolving from coarse dots to fine as the cell
  passes under the read-head, and settling from scale 1.03 to
  1.0 as it clears. It belongs because a photograph cannot be
  *on* paper tape any other way — the medium has one way of
  making a picture, out of punched dots, and the resolution of
  the image is tied to the act of reading it: a picture becomes
  clear at the moment the machine reads it.
- **Structure.** A `<figure>` occupying a full tape cell (a
  block-width band, §4) containing a real `<img>` with full
  `alt`, rendered through a dot-matrix treatment: the image is
  drawn to an offscreen canvas at cell resolution and re-drawn
  as dots at three declared densities — coarse (6px dots on an
  8px pitch), reading (3px dots, 4px pitch), fine (the image
  itself, dot layer faded to a 12% texture). The canvas is
  `aria-hidden`; the `<img>` remains in the DOM, visually
  presented through the canvas only while the enhancement runs.
  Captions print beneath in margin print with the cell's block
  number: `BLK 0041 — THE DISH AT KIRUNA-2, 1978`. The pass
  carries four images, BLK 0040–0043 (§6.17): the dish, the
  tape room, the pass chart, the night crew.
- **Motion spec.** Trigger: the cell crossing the read-head,
  scrubbed from the loop. Coarse → reading across the cell's
  approach (the 40vh before the centre), reading → fine across
  its passage through the centre band; scale 1.03 → 1.0 across
  the same passage, under the loop's lerp (no separate easing —
  the head's travel is the easing). A cell scrolled past holds
  its fine state permanently: once read, a picture stays read.
- **States.** Unread (coarse) / reading (resolving) / read
  (fine, dot texture at 12%, scale 1.0) / re-approached from
  below (scrolling up: holds fine — the machine does not
  un-read on rewind; resolution is a latch, not a scrub).
- **Content merge.** The images are the record's own plates —
  the four photographs the pass file contains, numbered as
  blocks, captioned from the record, occupying 16.0 of its
  196.0 metres. They are not illustrations of the text; they
  are entries in it, and the footage counter counts them.
- **Failure fallback.** Watchdog: if the canvas pass has not
  run within 1000ms of the cell entering the viewport, the
  plain `<img>` is shown at fine state. No canvas support: the
  `<img>` shows directly, with the 12% dot texture as a CSS
  overlay — the picture is slightly less theatrical and
  completely present. No-JS: the `<img>`, plain, with its
  caption. At no layer of failure is a picture missing.
- **Reduced-motion variant.** Images print at reading density
  (3px dots) statically — recognisably dot-matrix, fully
  legible — with no resolution change and no scale. The
  encoding is kept; the performance of resolving is not.
- **Performance budget & mobile variant.** Canvas redraws only
  while a cell is in the centre band, at most one cell at a
  time (the layout forbids two cells in the band at once);
  ≤1.2ms/frame during a passage, zero otherwise. Source images
  ≤120KB each, responsive sizes. Mobile (<768px): two densities
  only (coarse → fine), pitch floors at 5px dots — small
  screens get the same story with fewer steps.
- **Choreography timeline (v2).** Cell enters viewport: coarse
  → cell approaches centre: dots refine, scale eases 1.03 →
  1.01 → cell centred under the head: fine, scale 1.0 → cell
  passes: latched fine → caption line crosses the head and
  lights like any line (§6.3).
- **State matrix (v2).** *Rest (unread):* coarse dots. *Hover:*
  hovering a read cell does nothing; hovering an unread cell
  below the fold does nothing — resolution belongs to the head,
  not the pointer. *Focus:* if the figure's caption link is
  focused, the cell resolves to fine out of courtesy (a
  keyboard reader is reading it). *Active:* n/a.
  *Scrolled-past:* latched fine. *Disabled:* image failed to
  load → the cell prints its caption and `PLATE NOT RECEIVED`
  in the cell's place (§6.18's voice) — an empty cell on the
  record, never a broken-image icon. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: cell spans the 72ch column,
  three densities. 768–1199px: cell spans the column, three
  densities, coarse pitch 7px. <768px: cell spans the strip's
  inner width, two densities.
- **Edge cases & failure modes (v2).** *A very dark photograph:*
  dot density is computed from luminance with a floor — no cell
  may render as a black rectangle; the gate checks the dish
  plate (the darkest) by eye. *Image taller than the band:* the
  centre band is computed on the cell's middle third, so a tall
  plate resolves progressively rather than waiting for its
  centre. *Slow image load:* the cell reserves its box by
  aspect ratio (§6.5's geometry rule); a late image resolves
  from coarse whenever it arrives, or the watchdog shows it
  plain.
- **Accessibility spec (v2).** The `<img>` carries real `alt`
  written as an archive caption ("The 32-metre dish at
  Kiruna-2, seen from the tape room door, March 1978"). The
  canvas is `aria-hidden`. The image is fully legible in its
  no-JS state; the dot treatment never drops effective contrast
  of the picture's subject below recognition — checked per
  plate in §10.
- **Tokens consumed (v2).** `--ink`, `--tape`, `--shadow`,
  `--loop-lerp` (0.12), `--dot-coarse` (6px), `--dot-fine`
  (3px), `--dur-watchdog-image` (1000ms).

### 6.9 Cell-lighting hover

- **What & why.** Hovering a block runs the reader over it: its
  current line lights cell by cell, left to right, in a 200ms
  sweep of amber cells, and the block lifts minutely off the
  platen — a tilt of at most 1°. It belongs because inspection
  on this site is a machine pass: to look closely at a record
  is to run it under the head again, and the hover performs
  exactly that, on the block itself, in the medium's own terms.
- **Structure.** The sweep reuses §6.3's lighting machinery at
  block scope: the block's first body line (or the line under
  the pointer, if the block is tall) gets the `.under-head`
  treatment driven by a per-block timer instead of the loop.
  The tilt is a `rotateX` transform on the block, origin at its
  top perforation, driven from pointer position within the
  block and clamped to 1°. Both effects are armed per block on
  first hover; nothing is pre-built for blocks never touched.
- **Motion spec.** Trigger: pointerenter / focus-within. Sweep:
  200ms across the line's cells under `--ease-spool`, amber
  wash rising to full and holding while hovered. Tilt: follows
  the pointer with the loop's lerp, max 1° at the block's
  vertical extremes, 0° at its centre line. On leave: the wash
  decays over 300ms under `--ease-settle` and the tilt settles
  back over 400ms with no overshoot — paper does not bounce.
- **States.** Rest (flat, unlit) / inspecting (sweep complete,
  wash held, tilt live) / leaving (decaying) / focused (keyboard
  focus inside the block: the sweep runs once on the focused
  element's line, tilt does not engage — a tray does not tilt
  for a voice) / disabled blocks (the unreceived plate cell,
  §6.8: hover prints nothing extra; its label already says all).
- **Content merge.** The sweep lights the block's *own print* —
  the highlight is behind the glyphs the visitor is inspecting,
  and the tilt lifts the block around its own perforation, the
  place tape actually flexes. Nothing is added to the block; the
  reader's attention is the only overlay, and it is made of the
  block's own cells.
- **Failure fallback.** Watchdog: both effects are class- and
  transform-driven from a timer the hover itself starts; if the
  script is absent, hover falls back to the CSS-only state every
  interactive descendant already has (link colour, focus ring —
  §11). A block can never be left tilted: the leave handler and
  a 600ms no-pointer-move watchdog both zero the transform.
- **Reduced-motion variant.** No sweep, no tilt: hovering a
  block shows a static amber wash on the current line (an
  instant class change) and nothing else. Inspection is still
  marked; it is not performed.
- **Performance budget & mobile variant.** One line's background
  position + one transform; ≤0.15ms/frame for the single hovered
  block. Mobile (<768px): no hover exists — tap-and-hold on a
  block runs the sweep once (300ms) as the touch equivalent;
  tilt is cut entirely (a held phone is already tilted).
- **Choreography timeline (v2).** Pointer enters → sweep starts
  at ch 0 → 200ms: line fully lit → tilt lerps toward pointer
  angle → pointer moves within block: tilt tracks, sweep holds
  on the pointer's line, re-sweeping (120ms) when the pointer
  changes lines → pointer leaves: wash decays 300ms, tilt
  settles 400ms → rest.
- **State matrix (v2).** *Rest:* flat, unlit. *Hover:* sweep +
  tilt as above. *Focus:* sweep once on the focused line, no
  tilt, plus the standard focus outline on the element itself.
  *Active:* a pressed block hands over to §6.10's punch.
  *Scrolled-past:* a block scrolled out mid-hover resets
  instantly (no decay — it is gone, not leaving). *Disabled:*
  no response, per above. *Touch:* tap-hold sweep only.
- **Breakpoints (v2).** ≥1200px: full treatment. 768–1199px:
  tilt max 0.7°. <768px: sweep only, on tap-hold; tilt cut.
- **Edge cases & failure modes (v2).** *Pointer racing across
  many blocks:* sweeps are per-block and cheap; a block entered
  and left within 60ms shows a partial sweep that decays — the
  reader skimming is a true picture, not an error. *A block
  taller than the viewport:* the sweep follows the pointer's
  line, not the block's first line; the tilt origin stays at
  the top perforation and the angle clamps harder (0.5°) so a
  tall block never levers its foot off the tape visually.
  *Hover during the spool-in:* the hero is exempt until seated
  (§6.1) — the machine finishes loading before it inspects.
- **Accessibility spec (v2).** The wash never carries state
  alone: links and controls inside a block keep their own
  colours and outlines in every state. Ink on the amber wash is
  5.60:1. Focus outline: 2px `--ink` at 3px offset, present
  with or without the sweep. Touch targets inside blocks are
  ≥44px regardless of the tilt.
- **Tokens consumed (v2).** `--amber`, `--ink`, `--ease-spool`,
  `--ease-settle`, `--loop-lerp` (0.12), `--tilt-max` (1deg),
  `--dur-sweep` (200ms).

### 6.10 Punch click & tear transition

- **What & why.** Clicking a block punches it: a dot-matrix
  thud — the block scales to 0.99 for 80ms — and a parity tick
  appears in its right margin, the visitor's own mark on the
  record. And leaving the page tears the tape: the strip splits
  at a perforation in a jagged tear (~400ms) and the next page's
  strip feeds in from the left. It belongs because every action
  on this site is a tape operation — marking a record, tearing
  the strip — performed on the medium the whole site is made
  of, never on chrome that floats above it.
- **Structure.** The punch: a class on the block driving a
  transform (scale 0.99, origin centre) plus a burst of the
  §6.2 matrix treatment across the block's header line (a
  120ms re-stamp shimmer — dots, not a flash). The parity tick
  is a margin element, `✓` in `--green` with the visitor's
  session count (`×3` after the third punch of the same block),
  persisted for the session only (sessionStorage) — the mark is
  a reader's pencil, not an account feature. The tear: a
  full-strip overlay whose top edge is an SVG jagged path
  matching the perforation pitch; on navigation the overlay
  splits — top half holds, bottom half drops 12px and fades —
  while the incoming page's strip performs §6.1's spool-in at
  60% duration.
- **Motion spec.** Punch: scale to 0.99 in 40ms under
  `--ease-punch`, hold 20ms, release over 80ms under
  `--ease-settle`; tick prints at t=60ms with a 100ms stamp
  under `--ease-stamp` at 0° rotation (ticks are machine marks,
  not hand stamps — only §6.6 gets to be crooked). Tear:
  400ms total — split 160ms, drop 240ms — then the new strip's
  feed-in, 720ms. Watchdog on the whole transition: 900ms to a
  fully printed new page.
- **States.** Unpunched / punched (tick in margin) /
  re-punched (tick count increments; the thud repeats — the
  machine allows emphasis) / tearing / feeding / settled.
  A block that failed its checksum (§6.6) can be punched like
  any other; its tick prints in `--amber-deep` — the visitor
  has marked a doubtful block, and the margin says so.
- **Content merge.** The tick lives in the block's own margin,
  at the block's own line height, and means *a reader was here
  and checked this* — the same claim the verifier's ✓ makes in
  the block headers, one rank down. The tear happens at a real
  perforation between real blocks: the page boundary is placed
  where the tape was always meant to divide.
- **Failure fallback.** Watchdog at 900ms on transitions: the
  destination page forces its printed state (strip seated,
  stamp printed) — a transition may never strand a visitor
  between pages. No-JS: plain navigation, no tear, no ticks;
  links work, blocks read. Punch without JS: clicks on blocks
  do nothing (blocks are not controls; nothing is lost).
- **Reduced-motion variant.** No thud, no tear: the tick prints
  instantly on click, and navigation is a plain page change
  whose destination arrives fully spooled (§6.1's variant).
- **Performance budget & mobile variant.** Punch: one transform
  + one class; negligible. Tear: two transforms on one overlay;
  ≤0.4ms/frame for 400ms. Mobile (<768px): the tear shortens to
  260ms and the feed-in to 500ms; the punch is identical (a tap
  is a punch — the medium finally agrees with the hardware).
- **Choreography timeline (v2).** Click → t=0 scale dips →
  t=40ms bottom of thud → t=60ms tick stamps → t=140ms block at
  rest, tick printed. Navigation click → tear splits 160ms →
  bottom drops 240ms → new strip feeds 720ms → new page seated
  → watchdog deadline t=900ms (from tear start, for the print
  guarantee) passes unused.
- **State matrix (v2).** *Rest:* unpunched or ticked, flat.
  *Hover:* §6.9's inspection runs; the punch does not pre-fire.
  *Focus:* keyboard activation (Enter/Space on a block's
  control, or on the block if it is itself a link target)
  punches identically — a keyboard reader marks records too.
  *Active:* the thud itself. *Scrolled-past:* ticks persist
  (session). *Disabled:* n/a. *Touch:* tap = punch, full
  treatment.
- **Breakpoints (v2).** ≥1200px: full tear + 720ms feed.
  768–1199px: tear 340ms, feed 600ms. <768px: tear 260ms,
  feed 500ms, tick at 12px.
- **Edge cases & failure modes (v2).** *Double-click / click
  storm:* punches queue at most one deep — a second click
  during a thud restarts the release phase, never stacks
  scales; tick count increments once per completed punch.
  *Navigation away mid-tear to an external site:* the tear is
  cancelled instantly; the machine does not perform for a
  visitor who has left the archive. *Back button:* the previous
  strip arrives seated and stamped (its §6.1 state is latched
  per page in the session), ticks intact.
- **Accessibility spec (v2).** The punch is never the sole
  feedback for an action: blocks that are controls announce
  their own results (§6.14's form, §6.11's navigation). The
  tick is `aria-hidden` decoration — a session marker for the
  eye; an `aria-live` polite note ("Block 31 marked") fires
  once per block per session for screen-reader visitors who
  punch. Scale 0.99 is below any vestibular concern and is
  removed under reduced motion regardless.
- **Tokens consumed (v2).** `--green`, `--amber-deep`, `--ink`,
  `--ease-punch`, `--ease-stamp`, `--ease-settle`,
  `--dur-tear` (400ms), `--dur-watchdog-transition` (900ms).

### 6.11 Tape masthead & block-index navigation

- **What & why.** The site's navigation is the tape's own
  header furniture: a slim masthead printed at the strip's head
  carrying the archive's name in block capitals, and — the real
  navigation — a block index: the record's sections listed by
  block number (`BLK 0006 — THE RECORD TABLE`), each entry a
  link that spools the tape to that block. It belongs because a
  tape is navigated by footage and block numbers, not by menus:
  you do not open a section, you *wind to it*.
- **Structure.** A `<header>` printed as the strip's head band
  (above BLK 0001, on the tape, separated by a perforation):
  the archive name (`KIRUNA-2 TAPE LIBRARY`), the pass
  identifier, and a `<nav aria-label="Block index">` whose list
  is the index — one entry per page region, block number first,
  in record order. The current region's entry carries a
  `--green` ✓ and `aria-current="location"`, driven by the same
  boundary table the footage counter (§6.5) reads — one source
  of "where am I" for the whole machine. The masthead is
  sticky within the strip's head for the first screen only;
  after BLK 0001 passes, it scrolls away like everything else —
  the reader does not carry the box lid down the tape.
- **Motion spec.** Index click: the page spools — a scripted
  scroll at the reader's nominal rate (the loop's lerp governs,
  ~9.2 cm/s of tape made visible as a fast but ratcheted
  travel, §6.4's steps audible in the motion) — capped at
  1200ms for any distance; longer jumps land by native scroll
  with the tape arriving seated (the machine fast-forwards; it
  does not make you watch 190 metres). Current-entry changes:
  the ✓ prints with a 100ms stamp under `--ease-stamp`.
- **States.** Rest (current entry ✓-marked) / spooling (during
  an index jump, entries disable — the machine is winding) /
  arrived (the target block's header crosses the head and its
  entry takes the ✓). Disabled: an entry for a region a build
  has not published prints in `--ink-faint` with no link and
  the note `NOT ON THIS TAPE` — an honest gap in the index.
- **Content merge.** The index *is* the record's table of
  contents, printed in the record's own units: entries are
  block ranges from §6.17, and the masthead's pass identifier
  is BLK 0001's own first line. Navigation chrome that is not
  made of the record — a logo, a search box, a hamburger — does
  not exist here.
- **Failure fallback.** Watchdog: the spool is a scroll; if the
  scripted scroll has not arrived within 1500ms it completes by
  native jump. No-JS: entries are ordinary anchor links to
  block ids — the index works completely, merely without the
  winding performance. The ✓ is then static on the first entry.
- **Reduced-motion variant.** Index clicks jump natively (no
  winding), and the ✓ changes instantly. Nothing else differs:
  navigation was never the performance.
- **Performance budget & mobile variant.** Scrollspy by
  IntersectionObserver on block headers; zero per-frame cost.
  Mobile (<768px): the index becomes a single printed line —
  `INDEX:` followed by the block numbers alone (`0006 · 0014 ·
  0027 · 0040 · 0044`), titles cut — numbers are the navigation
  on a narrow strip, and the full titles live in the blocks
  themselves.
- **Choreography timeline (v2).** Load → masthead printed →
  BLK 0001 seats (§6.1) → first entry takes ✓ → visitor clicks
  an entry → spool (≤1200ms, ratcheted) → target header crosses
  head → ✓ moves (100ms stamp) → rest.
- **State matrix (v2).** *Rest:* current entry marked. *Hover:*
  an entry's line lights cell-by-cell (§6.9's sweep at nav
  scale, 120ms). *Focus:* 2px `--ink` outline at 3px offset;
  the entry's block number underlines. *Active:* the spool
  begins; the entry prints its number in `--green` while
  winding. *Scrolled-past:* the masthead is gone; the index's
  state lives on in §6.5's counter. *Disabled:* `NOT ON THIS
  TAPE` entries, unlinked, unfocusable. *Touch:* entries are
  ≥44px tall; tap = spool.
- **Breakpoints (v2).** ≥1200px: full index with titles.
  768–1199px: full index, titles at 13px. <768px: numbers-only
  index line, masthead wraps to two lines.
- **Edge cases & failure modes (v2).** *Many regions (a
  12-region build):* the index wraps to two printed lines;
  block numbers never abbreviate. *A region removed in a CMS:*
  the boundary table is built from the DOM's actual blocks, so
  index, counter and read-head can never disagree with the tape
  that exists. *Spool interrupted by the visitor's own scroll:*
  the winding cancels instantly — the visitor's hand outranks
  the machine's itinerary, always.
- **Accessibility spec (v2).** Landmark header + labelled nav;
  `aria-current` on the active entry; the ✓ is decorative
  (`aria-hidden`) — currentness is in the semantics. Skip link
  is the masthead's first element, printed `--ink` on `--tape`,
  visible on focus. Entry contrast 11.33:1 at rest.
- **Tokens consumed (v2).** `--ink`, `--ink-faint`, `--green`,
  `--tape`, `--ease-stamp`, `--loop-lerp` (0.12),
  `--dur-spool-jump` (1200ms), `--dur-watchdog-spool-jump`
  (1500ms).

### 6.12 Block index cards

- **What & why.** The long middle of the record — BLK 0014–0026
  and BLK 0028–0039 — is a run of short records, and they print
  as an index of cards *on the tape*: each card is one block,
  with its number, its one-line title, its first printed line,
  and its checksum at the fixed right column (§3). It belongs
  because a tape library is browsed by its index: the cards are
  not teasers for content elsewhere, they are the record's own
  entries, each carrying the whole of its (short) record.
- **Structure.** A `<ul>` of `<li>` blocks in the strip's flow —
  visually one continuous tape, each card separated by the
  standard perforation (§4), never by card chrome: no shadows,
  no rounded boxes, no background change. A card's whole area
  links to its full block view (the detail page type, §7) when
  the record has one; short records that are complete in the
  card carry no link and print `COMPLETE ON TAPE` in their
  margin. The checksum column aligns across all 25 cards — the
  right edge of this section is a verification strip the eye
  can run down in one pass.
- **Motion spec.** Cards print in as their headers cross the
  read-head's approach (§6.3's reveal), in spool order, one per
  perforation — no stagger cascade beyond the scroll itself:
  the tape's travel *is* the stagger. Hover runs §6.9's sweep
  and 1° tilt. A card's checksum ✓ lights `--green` in the
  frame its header crosses the head — verification happens at
  reading time, in order, never pre-lit below the fold.
- **States.** Unread (printed, ✓ unlit) / read (✓ lit, card at
  rest) / hover (sweep + tilt, §6.9) / focused (sweep once, no
  tilt) / complete-on-tape (no link; hover sweeps but the card
  does not punch, §6.10 — there is nowhere to go) / punched
  (visitor's tick in the margin, §6.10).
- **Content merge.** Every field on a card is a record field:
  number, title, first line, checksum — all from §6.17's block
  list. The 25 cards' metreage (13 + 12 blocks × 4.0 M = 100.0 M
  of the tape's 196.0) is counted by §6.5's footage as the
  visitor spools through them: the index is not *about* the
  record, it is a hundred metres *of* it.
- **Failure fallback.** Watchdog: cards are print; the only
  script behaviour is the ✓ lighting, whose absence leaves a
  fully readable index with unlit ticks. No-JS: identical, ✓s
  printed lit (the archive verified them in 1978; the lighting
  is a re-enactment, and without the script the printed result
  stands).
- **Reduced-motion variant.** ✓s print lit; no sweep; no tilt.
  The index is a table of contents that has already been
  checked — which, in the fiction, it has.
- **Performance budget & mobile variant.** Class toggles on
  scroll; ≤0.1ms/frame. Mobile (<768px): the checksum column
  holds (it is the section's point), the first-line excerpt
  truncates at 48ch instead of 72ch, and cards' padding drops
  to 21px — the tape narrows, the verification strip does not.
- **Choreography timeline (v2).** Card header enters approach
  zone → card prints (it was always printed; the reveal is the
  head's arrival) → header crosses head → ✓ lights, footage
  increments (§6.5) → hover: sweep 200ms, tilt to pointer →
  leave: settle (§6.9).
- **State matrix (v2).** *Rest:* printed, ✓ per read state.
  *Hover:* sweep + ≤1° tilt. *Focus:* sweep once + outline on
  the card's link. *Active:* punch (§6.10) then navigation.
  *Scrolled-past:* ✓ stays lit — read is read. *Disabled:*
  complete-on-tape cards are not disabled; they are complete,
  and print so. *Touch:* tap = punch + navigate; no tilt.
- **Breakpoints (v2).** ≥1200px: full cards, 72ch excerpt.
  768–1199px: 64ch excerpt. <768px: 48ch excerpt, checksum
  column fixed at the right edge, padding 21px.
- **Edge cases & failure modes (v2).** *A card whose record is
  long:* the excerpt is the record's first line by rule, never
  an editor's summary — summaries are tidying, and §1 forbids
  tidying; the card links to the full block. *Two cards with
  the same title:* impossible in a valid build — titles come
  from the record's block list, and §10's gate checks
  uniqueness. *The failed block's card:* BLK 0027 is not a card
  — it is §6.6's full pair, in place, between 0026 and 0028;
  the index prints a one-line pointer at its position
  (`BLK 0027 — SEE TAPE, 104.0 M`) so the numbering never
  silently skips.
- **Accessibility spec (v2).** Each card is one link with one
  accessible name ("Block 31 — Antenna temperatures — checksum
  verified"); the ✓ is `aria-hidden` with the word "verified"
  in the name. List semantics are real (`ul`/`li`). Contrast:
  body 11.33:1, metadata `--ink-soft` 6.03:1.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--green`,
  `--tape`, `--ease-settle`, `--tilt-max` (1deg),
  `--dur-sweep` (200ms).

### 6.13 The record table

- **What & why.** For the visitor who needs the pass plain: a
  true data table of the record's ranges — one row per section
  of tape, with its block range, its footage, its character
  count and its verification result — printed in data voice,
  totals row at the foot carrying the record's 196.0 M, 49
  blocks and 78,400 characters. It belongs because a record that
  cannot be read as a table is a light show; the table is the
  theme's honesty made structural, and it is where §6.17's
  arithmetic is set out to be checked by anyone, line by line.
- **Structure.** A semantic `<table>` inside BLK 0006–0013's
  span of the tape, `<caption>` "The Pass Record, by section",
  `scope="col"` headers (SECTION / BLOCKS / TAPE / CHARS /
  CHECK), `scope="row"` section names, tabular figures
  throughout (the grid is the grid, §3). Nine rows — the nine
  ranges of §6.17 — plus a `<tfoot>` totals row ruled with a
  double perforation. The CHECK column prints `9 VERIFIED`,
  `1 FAILED — RETRANSMITTED` for the parity row, and the totals
  row prints `48 VERIFIED / 1 FAILED`. No row is a link; the
  table is a reading, not a menu.
- **Motion spec.** The table does not animate. No reveal beyond
  its blocks' print-in (§6.3), no row hover effect beyond
  §6.9's line sweep on the hovered row's first line. The
  restraint is the spec: the one element a hurried visitor uses
  is the one element that never performs. Its checksums' ✓s
  light as their rows cross the head, as §6.12's do — the
  single concession, because verification-at-reading-time is
  the page's clock, not a decoration.
- **States.** Printed / rows crossing the head (✓s lighting in
  order) / hovered row (sweep, §6.9) / the parity row (its
  CHECK cell prints in `--amber-deep`, bold — the table admits
  the failure in the same type as everything else, coloured
  like a stamp).
- **Content merge.** The table *is* §6.17 presented in the flow:
  same ranges, same figures, same totals. Its rows are the
  index's (§6.11) sections and the choreography map's (§13)
  beats. Table, index and counter are three readings of one
  record, and §10's gate re-adds all three.
- **Failure fallback.** Watchdog: none required — static HTML
  and a CSS hover; it cannot fail into invisibility. No-JS:
  identical, ✓s printed lit. This element is the fallback's
  fallback: if every script on the page died, the table would
  still tell the whole story.
- **Reduced-motion variant.** Identical, minus the row sweep.
- **Performance budget & mobile variant.** Zero JS beyond the
  shared ✓ lighting. Mobile (<768px): the table becomes a
  stacked list — each row a block of margin-print lines (SECTION,
  then BLOCKS / TAPE / CHARS / CHECK as labelled lines), same
  order, same totals, no horizontal scroll: a record you must
  pan is a record lost. The transformation is semantic markup +
  CSS chosen at build, not a JS re-render.
- **Choreography timeline (v2).** Blocks 0006–0013 print in by
  §6.3 → rows cross the head in order, ✓s light → the parity
  row's CHECK cell is read (amber-deep, as printed from the
  start — colour is not an animation) → totals row crosses:
  footage counter (§6.5) shows 52.0 M, the table's own
  cumulative to that point being the whole record's plan, not
  its partial sum — the table prints the record entire, wherever
  it sits on the tape.
- **State matrix (v2).** *Rest:* printed. *Hover:* row sweep
  (§6.9). *Focus:* rows are not focusable; no cell is a control.
  *Active:* n/a. *Scrolled-past:* printed, ✓s lit. *Disabled:*
  n/a. *Touch:* tap on a row sweeps it once (§6.9's touch rule).
- **Breakpoints (v2).** ≥1200px: full 5-column table in the
  72ch column. 768–1199px: 5 columns, data at 12.5px.
  <768px: stacked list form, totals row last, double-ruled.
- **Edge cases & failure modes (v2).** *A range with zero
  verified blocks:* cannot occur in this record; in a build
  whose record has one, the CHECK cell prints `0 VERIFIED —
  NOT RECEIVED` in `--ink-soft` — an absence admitted in the
  table's own voice, never a hidden row. *Figures with
  thousands separators:* printed as the record prints them
  (78,400 — comma, per the station's house style, §12), tabular,
  right-aligned; the totals row never wraps.
- **Accessibility spec (v2).** Real table semantics with caption
  and scoped headers; the totals row is a `<tfoot>` with
  `scope="row"`. Screen readers get the record in its most
  native form. Contrast: body 11.33:1. The parity row's CHECK
  cell is the one place `--amber-deep` (3.84:1) touches data
  text, so the cell's ruling is strict: the failure is carried
  by the words `1 FAILED — RETRANSMITTED` set in `--ink`, and
  the amber-deep is a stamp tint on the cell's rule and count
  only — colour is never the sole carrier of the failure, and
  §10's gate audits exactly this cell.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--amber-deep`,
  `--green`, `--tape`, `--shadow`.

### 6.14 The transcript request form

- **What & why.** The record's conversion: a visitor who needs
  the pass as a certified transcript — a researcher, a museum,
  another archive — files a request, printed as BLK 0044–0047's
  block on the tape. The form asks for the requester's name,
  institution, the format (PAPER REPRINT / PUNCHED DUPLICATE /
  DIGITAL TRANSCRIPTION) and a line of purpose. On submit, the
  confirmation is not a toast: the request itself is *punched
  into the record's margin* as REQUEST № 313 — the next number
  after the 312 on file, which the block's preamble prints
  before the visitor types a character. It belongs because it
  is the only place the visitor adds tape to the archive, and
  the theme's law holds there too: the new entry is numbered
  from the record, and it stays.
- **Structure.** A real `<form>` with native validation,
  enhanced never replaced: labelled inputs printed on the tape
  (fields are ruled lines, not boxes — a bottom rule in
  `--shadow`, `--ink` text, focus thickens the rule to 2px
  `--ink` and runs §6.9's sweep along the field's line). The
  preamble prints: `REQUESTS ON FILE: 312. YOURS WILL BE № 313.`
  On success the form region is replaced by the confirmation
  block: the request's own mini-record (number, name, format,
  the station's fixed reply line, §12) stamped `RECEIVED —
  KIRUNA-2` in `--green`. Without JS the form posts to its
  endpoint and the confirmation is a server-rendered block with
  the same number.
- **Motion spec.** Field focus: rule thickens over 120ms; sweep
  200ms (§6.9). Submit: the block punches (§6.10's thud at form
  scale — the whole form block dips 0.99), then a writing state:
  the form's lines print out under a blank-tape shimmer (§6.15)
  for the request's duration — never a spinner. Success: the
  confirmation block spools in from the perforation above over
  600ms under `--ease-ratchet`, and its stamp lands at t=500ms
  (180ms, `--ease-stamp`). Error: the offending field's rule
  turns `--amber-deep` and its error line prints beneath in
  `--ink` — no shake, no red: the machine corrects in stamp
  ink, and red does not exist in this palette.
- **States.** Rest (preamble showing № 313) / filling (sweeps
  per field) / writing (submitting: fields disabled, shimmer) /
  received (confirmation block, stamp down, requests-on-file
  count now reading 313 in the preamble's place) / error
  (fields marked, values preserved, focus moved to the first
  error) / closed (endpoint down: the block prints `THE LIBRARY
  IS NOT RECEIVING REQUESTS THIS WEEK` and holds the visitor's
  entries in the fields, unsent and unlost).
- **Content merge.** The form's number derives from the record;
  its formats are the archive's real products; its confirmation
  is a block on the same tape, numbered in the same sequence as
  the request log the preamble cites. The conversion is not
  decorated with the theme — it is *filed in* it.
- **Failure fallback.** Watchdog at 4000ms on submission: if no
  response, the writing state clears and the block prints
  `THE REQUEST COULD NOT BE WRITTEN — YOUR WORDS ARE STILL
  HERE`, values intact, submit re-enabled; the request token is
  idempotent per form instance so a retry can never file № 313
  twice. No-JS: native post, server confirmation, same number.
- **Reduced-motion variant.** No shimmer, no spool-in: the
  confirmation block prints instantly with its stamp down.
  Errors print without transition. The writing state is a
  printed line, `WRITING…`, in place of the shimmer.
- **Performance budget & mobile variant.** The form's script is
  the page's only non-loop script: ≤5KB gz, deferred. Mobile
  (<768px): single column (it already is), fields full measure,
  the format choice becomes three full-width ruled lines with
  radio behaviour — no select dropdown: the tape does not do
  dropdowns, it does ruled lines you mark.
- **Choreography timeline (v2).** Focus field → rule thickens
  120ms, sweep 200ms → submit → block punches (140ms) → writing
  state → response → confirmation spools 600ms → stamp lands
  t=500–680ms → count line updates to 313 → rest. Watchdog
  ceiling 4000ms on the write.
- **State matrix (v2).** *Rest:* printed, № 313 promised.
  *Hover:* field lines sweep (§6.9). *Focus:* thickened rule +
  sweep + the standard outline on the control. *Active:*
  writing state as above. *Scrolled-past:* the form waits; an
  in-flight submission completes regardless of scroll.
  *Disabled:* closed state, values held. *Touch:* identical;
  targets ≥48px, submit full-width.
- **Breakpoints (v2).** ≥1200px: form measure 56ch within the
  block, two fields (name / institution) side by side as ruled
  half-lines. 768–1199px: same, measure 52ch. <768px: single
  column full measure, format as ruled radio lines.
- **Edge cases & failure modes (v2).** *A request for a
  different pass:* the purpose line is free text and the
  confirmation's fixed reply covers it — `THE LIBRARIAN WILL
  ANSWER FROM THE SHELF, NOT FROM THIS TAPE` (§12) — the form
  files requests about the archive, from a page that is one
  record of it. *Duplicate submission (double-click, retry
  after timeout):* idempotency token; the second response
  returns the same № 313 confirmation, never № 314.
  *Institution left blank:* not an error — the archive serves
  private readers; the confirmation prints `INSTITUTION: —`
  (a dash is a value on this tape, never a scolding).
- **Accessibility spec (v2).** Native labels, visible, `--ink`
  (11.33:1). Errors use `aria-describedby` and an
  `aria-live="polite"` summary in the form's own voice; the
  confirmation is an `aria-live` region announcing "Request
  № 313 received" once. Focus management: first error on
  failure, confirmation heading on success. The stamp is
  labelled; the shimmer is `aria-hidden`.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--shadow`,
  `--green`, `--amber-deep`, `--ease-ratchet`, `--ease-stamp`,
  `--ease-punch`, `--dur-watchdog-form` (4000ms).

### 6.15 Blank-tape loader & page transition feed

- **What & why.** Loading on this site is unpunched paper: a
  region whose content is still arriving shows as blank tape —
  the strip's buff, sprocket holes running, a faint ghost of the
  coming block's shape in `--ink-faint` — and as its data lands,
  the block punches in (§6.2's stamping at block scale) and the
  print appears. The page transition is the same physics at
  full scale, owned by §6.10's tear. It belongs because a
  spinner would be a machine from another decade in the reader;
  blank tape is this machine's honest idle state — paper,
  waiting to be written on.
- **Structure.** A loading region is a block-shaped element with
  `data-blank` set: ground `--tape`, sprocket columns live, and
  a ghost outline (dashed `--ink-faint` rules where the header
  and lines will sit — shaped like the coming block, never a
  generic grey bar). When the region's content is ready, the
  real block (already fully built off-DOM or server-printed for
  no-JS) replaces it and the punch-in plays over it. The initial
  page load uses the same device below the fold: blocks beyond
  the first screen are never "loading" — they are printed
  server-side; blank tape exists only for genuinely deferred
  data (a late index range, the form's writing state, §6.14).
- **Motion spec.** Ghost pulse: the ghost rules breathe at
  30% ±8% opacity on a 2.4s sine — barely alive, clearly
  waiting; opacity only, no movement. Punch-in on arrival:
  header stamps over 300ms, body lines print in spool order at
  40ms per line under `--ease-punch`, total capped at 900ms for
  any block. Hard ceiling: any region still blank at 1500ms
  prints its content anyway, stamped or not — the archive does
  not hold a reader hostage to a slow shelf.
- **States.** Blank (ghost breathing) / punching (arrival) /
  printed (rest) / failed (the region's data fails: the ghost
  is replaced by a printed note in the record's voice —
  `THIS RANGE HAS NOT REACHED THE READER — [RETRY]` with a real
  retry control; blank tape never breathes forever) / no-JS
  (no blank regions exist; content is server-printed complete).
- **Content merge.** The blank is shaped like the block it
  precedes and made of the block's own material — the same
  paper, the same holes, the same measure. A visitor who sees
  blank tape knows exactly what is coming and how much room it
  will take: the skeleton *is* the tape, unpunched.
- **Failure fallback.** Watchdog per region at 1500ms (print
  regardless) and on the transition at 900ms (§6.10). A region
  whose data never arrives prints its failure note at the
  ceiling, not an eternal ghost. No-JS: no loader exists.
- **Reduced-motion variant.** No ghost pulse, no punch-in:
  blank regions are static paper that swap to print instantly
  on arrival; the failure note prints the same.
- **Performance budget & mobile variant.** Ghost fields are CSS
  gradients and rules — zero raster, zero per-frame JS. The
  punch-in reuses §6.2's stamper. Mobile (<768px): the ghost
  pulse is cut (static paper) to save battery; punch-in caps
  at 600ms.
- **Choreography timeline (v2).** Region requested → blank tape
  prints with the layout → data lands → header stamps 300ms →
  lines print 40ms each, capped 900ms → block at rest. Ceiling
  1500ms forces print or the failure note.
- **State matrix (v2).** *Rest:* printed content. *Hover:* n/a
  on a blank region (nothing to inspect yet). *Focus:* blank
  regions are not focusable and are `aria-hidden` until printed.
  *Active:* the form's writing state (§6.14) is this element at
  form scale. *Scrolled-past:* regions below the fold print on
  arrival regardless of visibility. *Disabled / no-JS:*
  server print, no blanks. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full treatment. 768–1199px:
  full, ghost pulse period 2.8s. <768px: static ghosts, 600ms
  punch cap.
- **Edge cases & failure modes (v2).** *Data arrives before the
  ghost paints (fast cache):* the block prints directly — a
  blank that never appears is the best kind. *Partial arrival
  (an index range lands in two parts):* landed blocks print;
  the unlanded range holds blank until its own ceiling, then
  prints its note — the tape opens with a gap admitted, not
  with the page held shut. *Retry clicked twice:* the region
  re-blanks once; the second click is ignored until the ceiling
  or arrival.
- **Accessibility spec (v2).** Blank regions carry
  `aria-busy="true"` on their container and stay out of the
  accessibility tree until printed; one polite announcement
  ("Tape loaded") fires when the last above-fold region prints
  — not one per region. The failure note's contrast: `--ink` on
  `--tape`, 11.33:1; its retry control is a real button, ≥44px.
- **Tokens consumed (v2).** `--tape`, `--ink-faint`, `--ink`,
  `--shadow`, `--ease-punch`, `--dur-blank-ceiling` (1500ms),
  `--dur-punch-block` (900ms).

### 6.16 End-of-tape footer

- **What & why.** The tape ends the way tapes end: a final
  block — BLK 0048, the end block — and after its perforation,
  the take-up furniture: the record's totals printed a third
  time (196.0 M / 49 BLOCKS / 78,400 CHARACTERS / 48 VERIFIED /
  1 FAILED), the verifier's sign-off line, the lamp's three
  slow blinks (§6.7), and a stamped `END OF RECORD` in
  `--green`. Below that, the strip's last 400px age into
  `--buff-deep` and the final sprocket holes simply stop — the
  paper runs out. It belongs because an archive page must end
  by *accounting*: the footer is where the counter's promise
  (§6.5) is audited in print.
- **Structure.** A `<footer>` printed as the tape's tail: the
  end block, a double perforation, the totals table in margin
  print (five lines, labels left, figures right, ruled), the
  sign-off (`VERIFIED AGAINST THE STATION LOG — KIRUNA-2, 14
  MARCH 1978`), the stamp (inline SVG, `--green`, rotated 4° —
  the second and last licensed crooked thing, answering
  §6.6's), and the archive's colophon line: who holds the tape,
  under what shelf mark (`SHELF: K2/1978/0417`). No links farm,
  no newsletter, no social row: the tape's tail carries the
  record's accounting and the library's ordinary footer links
  (about the library, other shelves) printed as one margin line.
- **Motion spec.** As the footer centres: the totals print in
  line by line at 120ms intervals under `--ease-punch` (they
  were always in the DOM; the print-in is the head's ceremony),
  the stamp lands at the totals' completion (180ms,
  `--ease-stamp`), and the lamp runs its sign-off (§6.7) in
  parallel. The footage counter (§6.5) lands on 196.0 M in the
  same frame the end block's header crosses the head — footer
  and counter agree because both read the record.
- **States.** Approaching (printed, unstamped) / signing off
  (totals printing, lamp blinking its three) / closed (stamp
  down, lamp steady, counter at 196.0 M) / returned (scrolling
  back up: everything stays printed and stamped — the machine
  does not un-close a record).
- **Content merge.** The footer's figures are the record's
  figures, third printing (§6.5's counter, §6.13's table, here)
  — three printings, one set of numbers, and §10's gate
  reconciles all three. The colophon's shelf mark is the
  record's own identifier. Nothing in the footer is about the
  website; it is the tape's tail and the library's mark.
- **Failure fallback.** Watchdog at 1200ms from the footer's
  first entry: totals printed, stamp down, regardless of the
  ceremony. No-JS: identical end state. The footer cannot fail
  into absence — it is the page's most static element by
  design.
- **Reduced-motion variant.** Totals and stamp printed from the
  start; the lamp does not blink its sign-off (its label's
  state word reads `HELD`). The accounting is complete; the
  ceremony is not required to trust it.
- **Performance budget & mobile variant.** Five class toggles
  and one stamp; negligible. Mobile (<768px): the totals table
  stacks (label above figure), the stamp scales 0.85, and the
  aged tail shortens to 240px.
- **Choreography timeline (v2).** End block header crosses head
  → counter lands 196.0 M → totals print, 120ms per line →
  stamp lands 180ms → lamp: three slow blinks (600/600 ×3) →
  steady → page closed.
- **State matrix (v2).** *Rest:* closed and printed. *Hover:*
  the footer's one margin line of links sweeps per §6.9.
  *Focus:* links take the standard outline. *Active:* n/a.
  *Scrolled-past:* n/a (it is the end). *Disabled:* n/a.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: totals as a ruled two-column
  table. 768–1199px: same, margin print 12px. <768px: stacked
  totals, stamp 0.85, tail 240px.
- **Edge cases & failure modes (v2).** *A build whose record
  changes length:* the footer reads §6.17, never a hardcoded
  total — a footer that disagrees with its record fails §10's
  three-printings audit. *Visitor never scrolls to the end:*
  the record remains unclosed *for them*; nothing on the page
  claims otherwise (the counter simply never shows 196.0 M).
  *Print:* the footer is the print stylesheet's last page —
  totals, sign-off and stamp all print; a paper copy of this
  page is a complete archival copy.
- **Accessibility spec (v2).** The totals are a real table (or
  list) in the flow — the third printing is the one assistive
  readers are pointed to, since §6.5's counter is `aria-hidden`.
  The stamp is labelled ("End of record"). Contrast throughout:
  11.33:1 body, `--green` stamp lettering at 14px bold on
  `--tape` (4.65:1, large-text floor met).
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--green`,
  `--buff-deep`, `--tape`, `--ease-punch`, `--ease-stamp`,
  `--dur-watchdog-footer` (1200ms).

### 6.17 The Pass Record — the one source of every figure

- **What & why.** This element is not rendered; it is *kept*.
  The Pass Record is the single declared data object from which
  every number, name and checksum on the page derives — the
  hero's header, the table's rows, the counter's maximum, the
  footer's totals, the form's next number. It belongs as an
  element of the spec because the theme's law (§1) is
  unenforceable without it: one record, declared once, printed
  three times, audited by the gate (§10). A build that lets a
  figure enter the page from anywhere else has already failed,
  however good it looks.
- **Structure.** A single data object (JSON or a typed module)
  held beside the build, with exactly these fields — no more
  are needed, and any build needing more must amend the record
  here first: `pass` (0417), `satellite` (HELIOS-3), `station`
  (KIRUNA-2), `date` (1978-03-14), `aos` (03:12:04 UTC), `los`
  (03:47:41 UTC), `duration_s` (2137), `block_m` (4.0),
  `chars_per_block` (1600), `blocks` (the ordered list of 49:
  number, title, checksum, status), `failed_block` (0027, with
  its printed checksum 4F, recomputed 9A, and its 23-position
  garble map), `requests_on_file` (312). Derived values are
  computed, never stored: total tape = 49 × 4.0 = 196.0 M;
  total characters = 49 × 1600 = 78,400; verified records =
  48; verified characters = 48 × 1600 = 76,800.
- **Motion spec.** None — and that is specified, not omitted.
  The record does not animate, load asynchronously on the
  client, or hydrate. It is a build-time constant. Any figure
  the visitor sees was printed from it before the page shipped.
- **States.** One state: declared. A record under amendment is
  a build error, not a state — amendments happen by editing
  this declaration and re-running §10's audits, never at
  runtime.
- **Content merge.** Total, by construction: the record is not
  merged with the content, it *is* the content's source. §6.13's
  table prints its ranges; §13's choreography map walks its
  block order; §6.6's pair is its `failed_block` entry, in
  place.
- **Failure fallback.** If a figure on the page cannot be traced
  to this object, the build fails the gate — there is no runtime
  fallback for a broken source, only the refusal to ship. The
  object itself is plain data in the repo; it cannot fail to
  load because it is never loaded.
- **Reduced-motion variant.** Identical. Data does not have a
  motion variant, and the spec says so to close the question.
- **Performance budget & mobile variant.** Zero bytes at
  runtime beyond the figures it prints (which are text).
  Identical at every breakpoint — the record does not know what
  a breakpoint is.
- **Choreography timeline (v2).** Build time: record declared →
  §6.13's table generated from it → counters and footer take
  their totals from it → §10's audits run against it → ship.
  Runtime: no beats. The record's timeline is the build's.
- **State matrix (v2).** *Rest:* declared and shipped.
  *Hover / focus / active / scrolled-past / disabled / touch:*
  n/a — recorded explicitly so the matrix has no silent gaps:
  a data object has no interactive states, and any tool that
  tries to give it one is modelling the wrong thing.
- **Breakpoints (v2).** None. The same record prints at 320px
  and at 2560px; only its presentation (§6.13's stacked form)
  changes.
- **Edge cases & failure modes (v2).** *The historical record
  is corrected by the archive* (a checksum re-read, a title
  amended): the amendment is a new printing of this declaration
  with a dated note appended — the site follows its own law:
  corrections are additional, never silent edits, and the
  note prints in the colophon (§6.16). *Two builders derive
  different totals:* impossible if both derive — the gate
  recomputes; a stored total found anywhere in the build is
  deleted on sight. *A figure needed that the record lacks*
  (a second pass, a comparison): out of scope for this page —
  another pass is another tape (another page), not a new field
  smuggled into this one.
- **Accessibility spec (v2).** The record's figures reach
  assistive readers through its printings (§6.13's table,
  §6.16's totals) in semantic markup. The object itself is
  never the only carrier of any figure: every value it holds
  is printed in the flow at least once, in text.
- **Tokens consumed (v2).** None. The record consumes no design
  tokens; it *supplies* the values several tokens reference
  (`--tape-total`, `--block-total`, §6.5).

### 6.18 Off-tape — the empty state & 404

- **What & why.** Where the tape has nothing — a shelf with no
  pass under the requested number, a search of the index with
  no match, a URL that names no tape at all — the page shows
  the reader with no tape loaded: the strip's furniture
  (sprocket columns, the read-head line, the lamp, steady) runs
  down an empty reader bed, and in the bed, one printed block:
  `NO TAPE LOADED` and the shelf note. It belongs because
  absence in an archive is a finding, not an error: the shelf
  is either empty or the number is wrong, and the page says
  which, in the library's voice, on the library's furniture.
- **Structure.** The 404 page is a short tape of one block: the
  masthead (§6.11) printed, the strip running 60vh of unpunched
  bed (sprocket holes present — the reader is real; the tape is
  absent), the single block centred on the read-head, and the
  footer's colophon line. The block prints the shelf mark that
  was asked for, verbatim from the URL, and the two true exits:
  the block index (§6.11) and the shelf list. The in-page empty
  state (an index search with no match) is the same block at
  section scale, printed inside the strip where the results
  would have spooled.
- **Motion spec.** Almost none, deliberately: the strip does
  not spool (there is nothing to load), the block does not
  punch in (it was always on the reader's instruction plate,
  not on a tape). The lamp holds steady. The one motion: on
  arrival, the read-head's brackets settle onto the block's
  first line over 300ms under `--ease-settle` — the machine
  acknowledging the empty bed. A page that performs cheerfully
  over a missing record would be obscene in this theme's terms.
- **States.** Loaded-empty (the block printed, exits live) /
  searching-from-empty (a new index search spools normally —
  §6.11 — the bed is left behind without ceremony).
- **Content merge.** The empty state is made of the page's own
  furniture and the request's own identifier — the asked-for
  shelf mark is the content. It never prints a generic "oops",
  a mascot, or a joke: the archive's voice (§12) admitting an
  empty shelf *is* the content.
- **Failure fallback.** Watchdog: none needed — the page is
  static print. It is itself the fallback for a missing route,
  and it is built to the same standard as every block: complete
  with no script at all.
- **Reduced-motion variant.** Identical, minus the brackets'
  settle. Nothing else moves here in any variant.
- **Performance budget & mobile variant.** The lightest page in
  the build: no canvas, no images, ≤40KB total. Mobile
  (<768px): the bed shortens to 44vh; the block and exits are
  unchanged — an empty shelf reads the same at any width.
- **Choreography timeline (v2).** Arrival → masthead printed,
  bed empty → brackets settle onto the block (300ms) → lamp
  steady → rest. Departure via an exit: normal §6.10 tear from
  the block's perforation — even an empty tape tears properly.
- **State matrix (v2).** *Rest:* printed, steady. *Hover:* the
  exit links sweep per §6.9. *Focus:* exits take the standard
  outline; focus order is masthead → block's exits → colophon.
  *Active:* exits navigate (§6.10). *Scrolled-past:* n/a (the
  page barely scrolls). *Disabled:* n/a. *Touch:* exits ≥48px.
- **Breakpoints (v2).** ≥1200px: 60vh bed. 768–1199px: 54vh.
  <768px: 44vh bed, block measure full strip width.
- **Edge cases & failure modes (v2).** *A shelf mark that never
  existed vs one whose tape is out on loan:* the block
  distinguishes them only if the library's data does — `NOT ON
  THIS SHELF` vs `OUT — RETURN EXPECTED` (§12's fixed strings);
  if the build cannot know, it prints the former. Guessing at
  a warmer message would be tidying. *A malformed URL:* the
  asked-for mark prints exactly as received (escaped, always)
  — the record of the request is the request.
- **Accessibility spec (v2).** The block's heading is the page's
  `<h1>` ("No tape loaded"); the asked-for mark is real text.
  The empty bed is `aria-hidden` furniture. HTTP status is a
  true 404 — the theme's honesty extends to the protocol.
- **Tokens consumed (v2).** `--tape`, `--ink`, `--ink-soft`,
  `--shadow`, `--green`, `--ease-settle`.

## 7. Page application map

The theme is a medium, not a homepage skin: every page type is
a tape, and the differences between page types are differences
in what was recorded.

| Page type | How the tape plays it |
|---|---|
| **Home / the pass page** | The full record: BLK 0001 → 0048 in order, all §6 elements in their places, the parity pair at its true position. This is the reference build every other page type is a variation of. |
| **Listing / shelf page** | A shelf of tapes: each row is a tape's header block (pass number, satellite, date, length, verification summary) printed as a short strip segment with its own sprocket edges; rows are separated by perforations. There is no grid of cards — shelves are horizontal, and so is the page. Winding to a tape opens its pass page with §6.10's tear. |
| **Detail / one block in full** | A single block spooled out long: the block's full record, its checksum worked in the margin (the character sums that produce it, §6.17's rule), and its neighbours' headers above and below as context — you always see where a block sits in its tape. |
| **About / the library** | The library's own tape: its history printed as blocks in the same format, because an archive that will not archive itself is not trusted with anyone else's. The masthead (§6.11) is identical; only the record changes. |
| **Contact / request** | §6.14's form as a whole page: the request block with the shelf's full request log preamble. The form is the page; there is no contact "info" beside it — the library's address is a line in the colophon. |
| **Checkout** | **Refused.** The tape does not sell. A build that needs payment hands off at a perforation — a printed line, `THE TAPE ENDS HERE — THE DESK IS NEXT DOOR`, and a plain link — to a checkout in the institution's ordinary design system. Commerce performed in dot-matrix would be a costume, and the theme's law is that nothing here is a costume. |
| **Search results** | Results spool as an index (§6.12) of the blocks that matched, in tape order, with the match count printed as footage (`3 BLOCKS IN 196.0 M`). No match: §6.18's empty block, in place. |
| **404** | §6.18: the empty reader bed. |

## 8. Worked examples

### 8.1 The hero — Pass 0417 loads (worked example 1)

**What the visitor gets.** The desk (`--buff-deep`), and on it a
buff strip, 880px wide, its head band printed: `KIRUNA-2 TAPE
LIBRARY` left, `SHELF K2/1978/0417` right, a perforation under
both. Below the perforation, the strip's left edge is still
off-screen: the tape has not loaded. The read-head line sits at
viewport centre, green, brackets down, with nothing under it
but desk. The margin where the footage counter will live is
blank. This is the page at t=0 — and every word of the hero is
already in the DOM, readable by any tool that does not wait.

**The build.** BLK 0001 is a standard block element (§4) whose
header line reads `BLK 0001 — PASS HEADER ……… CHK B7 ✓` (the
checksum at ch 64–72, §3), body: the satellite's name as the
punched headline (§6.2), then four printed lines — station,
date, AOS/LOS, and the pass in one sentence: `HELIOS-3 CAME OVER
KIRUNA-2 AT 03:12:04 UTC AND WAS GONE BY 03:47:41. THIS TAPE IS
WHAT THE STATION HEARD.` The stamp SVG (§6.1) sits in the right
margin, opacity armed.

**Scroll/load timeline.** t=0 first paint → the spool-in runs
(8 ratchet steps, 1200ms, holes punching) → t=1200ms BLK 0001
seats under the head, its header line lights amber as it
crosses → the headline punches (24 characters × 26ms stagger,
done by ~t=2250ms) → t=1350ms the `VERIFIED — KIRUNA-2` stamp
lands → the footage counter fades its first reading into the
margin: `TAPE: 004.0 M / BLK 0001` → the lamp (§6.7) begins its
blink as the visitor's first scroll moves the tape. Total
ceremony ≈2.3s, every beat skippable, every end-state the
no-JS state. If the visitor never scrolls, the page rests as a
loaded reader with one verified block under its head — which
is a complete, honest first screen, not a teaser.

### 8.2 Mid-page — the failure, as the visitor lives it (worked example 2)

**What the visitor gets.** They have spooled 104.0 metres. The
counter says so. The index cards (§6.12) have been passing in
order — 0014, 0015 … 0026 — each lighting its ✓ as it crossed
the head. Then a pointer line: `BLK 0027 — SEE TAPE, AT THIS
POSITION`. The next block is not a card. Its header reads `BLK
0027 — ANTENNA TEMPERATURES ……… CHK 4F ✗ 9A`, and the ✗ is the
first cross on the whole tape. Its body is damaged: most lines
read clean, but 23 characters across them are wrong — rendered
as broken matrix glyphs on an amber wash, a word with its
middle punched out, a figure whose digits stutter. It is still
readable. That is the point: the archive is showing damage, not
hiding the block.

**The build.** §6.6 exactly: the true text in the DOM, the
garble as rendering from §6.17's declared 23-position map, the
stamp as SVG, the tear line as an SVG path across the pair's
perforation, BLK 0027R following with `CHK 9A ✓`.

**Scroll timeline.** BLK 0027's header crosses the head → the
RETRANSMIT REQUESTED stamp falls (180ms, to its 4° rest) → the
pair crosses the centre band → the tear line draws itself,
scrubbed, across the perforation → BLK 0027R's header crosses
the head → its ✓ line lights like any other line, and the
counter ticks from 108.0 M to 112.0 M as the pair completes.
The visitor scrolls on. Nothing follows them: no banner, no
"we take reliability seriously" — the tape has already said it,
in the only language it has. Scrolling back up later, the stamp
is still down and the line still drawn: answered is answered.

### 8.3 Conversion — a request enters the record (worked example 3)

**What the visitor gets.** At 176.0 metres the pictures end
(BLK 0040–0043) and the tape changes key: BLK 0044's header
reads `BLK 0044 — TRANSCRIPT REQUESTS`, and its preamble prints
the terms before any field: `REQUESTS ON FILE: 312. YOURS WILL
BE № 313. THE LIBRARIAN ANSWERS WITHIN FOURTEEN DAYS, BY POST
OR BY WIRE.` The form (§6.14) is ruled lines on the tape: NAME,
INSTITUTION (a dash is acceptable), FORMAT as three markable
lines, PURPOSE one line. The submit is a printed block of text:
`PUNCH THIS REQUEST INTO THE LOG`.

**The build.** §6.14 exactly, with the record's
`requests_on_file: 312` as the preamble's source and the
idempotency token generated per form instance.

**Scroll/submit timeline.** The block crosses the head → its
header lights, the preamble is read → the visitor focuses NAME:
the rule thickens, the sweep runs → they complete the fields
and submit → the block punches (the form-scale thud) → the
writing state: blank-tape shimmer over the form's lines, the
lamp (§6.7) blinking — the machine is working, and its working
is visible in furniture the visitor already trusts → at
response, the confirmation block spools in from the perforation
above: `REQUEST № 313 — RECEIVED. [NAME], [FORMAT]. THE
LIBRARIAN WILL ANSWER FROM THE SHELF, NOT FROM THIS TAPE.`
stamped `RECEIVED — KIRUNA-2` in green → the count line now
reads `REQUESTS ON FILE: 313`. The visitor's request is a
numbered entry in the same sequence as the 312 before it. That
— not a checkmark animation — is the conversion's reward, and
it is why the form converts in this theme's tests of tone: the
visitor has not submitted a form, they have been *filed*.

## 9. Anti-slop — what makes THIS theme look cheap

Each failure below is specific to the tape; each cure is a
return to the record.

1. **The sepia photograph treatment.** The page is styled like
   an old photo — vignettes, coffee stains, "aged paper"
   textures bought from a stock site. *Cure:* the tape's age is
   in its content (1978, checksums, a failure kept), not in a
   filter. Ground is flat `--tape`; the only ageing is
   `--buff-deep` at the strip's edges and tail.
2. **A second typeface "for readability".** A clean sans for
   body text with mono reserved for headings — the costume
   worn halfway. *Cure:* §3's ruling is absolute. Plex Mono at
   16px/1.75 is readable; what the build actually lacked was
   line-length discipline (72ch), so fix the measure, not the
   face.
3. **Sprocket holes as wallpaper.** Holes running down a sidebar,
   a card, a modal — the motif sprayed wherever the design felt
   empty. *Cure:* holes exist only in the strip's two columns,
   on the 24px pitch, because they are how *this* tape feeds.
   An element that is not tape does not get holes.
4. **Amber as a brand colour.** Amber buttons, amber links, an
   amber logo — the doubt colour spent on cheer. *Cure:* §2's
   census: amber is ~2% of the page and always means the
   machine doubts. The gate counts amber elements; §6.6's pair
   and the read-head's wash are nearly the whole budget.
5. **The error block as a marketing section.** Moving BLK 0027
   into a "Why trust us" area, or adding a headline above it
   ("We catch our mistakes!"). *Cure:* the pair sits at its
   record position, mid-tape, unheralded (§6.6). Trust performed
   as placement is advertising; trust performed as arithmetic
   is the theme.
6. **Rounded figures.** "Over 190 metres of tape", "nearly
   80,000 characters". *Cure:* §1's law — the record's figures,
   exact, everywhere: 196.0 M, 78,400, 49, 48, 1. A rounded
   number on this page is a factual error, not a style choice.
7. **Fixing the garble.** An editor "cleans up" BLK 0027 because
   the broken glyphs look like a rendering bug, or SEO complains.
   *Cure:* the garble is declared in §6.17 with its map; the
   DOM text is already the true text, so nothing is actually
   broken — and the visually hidden note explains the block to
   anyone who cannot see the damage.
8. **Smooth, buttery scroll.** A build that drops the
   sprocket-step (§6.4) because testers called it "janky" in
   the first five seconds. *Cure:* keep the amplitude honest
   (3px, velocity-faded) and let the perforation-keyed rhythm
   teach itself; the gate includes a scroll-feel check with a
   reader who has lived with it for a full pass, not a first
   impression.
9. **A blinking cursor after the headline.** Terminal cosplay —
   the other machine. *Cure:* this is a tape reader, not a
   terminal; nothing on the page waits for input at a prompt.
   The lamp (§6.7) is the only blink, and it blinks for the
   tape, not for a cursor.
10. **Generic skeleton screens.** Grey rounded rectangles during
    load. *Cure:* §6.15 — blank tape, shaped like the block,
    punching in on arrival. Grey boxes are another medium's
    furniture.
11. **The stamp as clip-art.** A grungy "VERIFIED" starburst,
    rotated −17°, in a red that is not in the palette. *Cure:*
    stamps here are bordered rectangles in `--green` or
    `--amber-deep`, rotated exactly 4°, set in Plex Mono 700
    caps. Two stamps exist (§6.1, §6.6) plus the footer's
    sign-off (§6.16); that is the census, and the gate counts.
12. **Dark mode "support".** An inverted tape — black paper,
    glowing green text — added because the design system
    requires a dark variant. *Cure:* §2's documented refusal.
    The desk darkens; the paper does not.

## 10. Quality gate

Blocking checks — every one must pass before this theme may be
used in a build. The gate is signed by a non-builder.

1. **Three-printings audit.** The record's totals appear in
   §6.5's counter (as its maximum), §6.13's table (totals row)
   and §6.16's footer. All three are recomputed from §6.17 by
   hand: 49 blocks, 196.0 M, 78,400 characters, 48 verified,
   1 failed. Any disagreement, anywhere, fails the build.
2. **Figure trace.** Ten figures sampled at random from the
   page must each trace to a field or a derivation in §6.17.
   A figure that traces to a designer's head fails the build.
3. **Checksum census.** Every block header prints a checksum at
   ch 64–72; exactly one prints a ✗ (BLK 0027, `4F ✗ 9A`); its
   retransmission prints `9A ✓`. Grep the build: one ✗, no more.
4. **Garble audit.** BLK 0027's rendered damage matches
   §6.17's 23-position map exactly; its DOM text is the true
   text; the visually hidden failure note is present.
5. **Amber census.** Amber elements enumerated: the read-head
   wash, BLK 0027's damaged cells, §6.6's stamp wash, §6.14's
   error rules (state-dependent). Anything else amber fails.
6. **Stamp census.** Exactly three stamps (§6.1, §6.6, §6.16),
   all 4°, all palette colours, all Plex Mono 700. A fourth
   stamp — however small — fails.
7. **Watchdog drill.** With the loop killed mid-scroll: every
   block readable, the lamp steady (not frozen mid-blink), the
   counter frozen at a true reading, no offset stuck on the
   strip (§6.4), no block left unpunched past its ceiling.
8. **No-JS pass.** JavaScript disabled: the entire record reads
   top to bottom, the form posts, the index navigates, the
   footer accounts. Any content missing fails.
9. **Reduced-motion pass.** `prefers-reduced-motion`: no spool,
   no punch ceremony, no ratchet, no blink — and the page loses
   no information thereby (the lamp's state word, §6.7, is
   present and correct).
10. **Read-head integrity.** At every scroll position exactly
    one line is under the head; the block counter's increments
    coincide with header crossings in a screen recording checked
    frame by frame for three blocks, including BLK 0027R.
11. **§6.13 cell audit.** The record table's parity row carries
    its failure in `--ink` words, with `--amber-deep` confined
    to the rule and count tint (§6.13) — colour is never the
    sole carrier.
12. **Grid audit.** Ten blocks sampled: header is one line,
    checksum at ch 64–72, measure ≤72ch, no element crosses the
    sprocket columns, the stamp (§6.6) is the only overlap
    exception and stays within its 18px licence.
13. **Scroll-feel check.** A reader who has not seen the build
    spools the full pass: the sprocket-step reads as machinery
    by the second block and is not mentioned as jank at the
    debrief; if it is, amplitude drops to 2px and the check
    re-runs (the step is tuned, never deleted — §9.8).
14. **Performance sign-off.** §14's budget measured on the
    reference mid-range phone: frame cost, page weight, and the
    cut order rehearsed by disabling the first cut item and
    re-measuring.

## 11. Component inventory

Every component a real site in this theme needs, with its
themed treatment. Components the medium cannot honestly do are
refused, with the in-theme replacement named — a refusal is a
design decision, not a gap.

| Component | Treatment on the tape |
|---|---|
| **Primary button** | A printed block: `--ink` ground, `--tape` text, no radius, label in caps (`PUNCH THIS REQUEST INTO THE LOG`). Press = §6.10's thud. It is a punch key, not a pill. |
| **Secondary button** | Ruled text: `--ink` label over a 2px bottom rule; hover runs §6.9's sweep along the rule. |
| **Text input** | A ruled line (§6.14): bottom rule in `--shadow`, thickening on focus; label above in margin print; no box, no placeholder text (the tape does not print hints that vanish — the label is the hint, permanently). |
| **Select** | Refused. Replaced by ruled radio lines (§6.14): the options printed in full, the chosen one marked with a punched `●` in its margin. |
| **Checkbox / radio** | A square cell in the margin that punches in (fills with a matrix dot pattern) when marked. Unmarked = an empty cell outline in `--shadow`. |
| **Table** | §6.13 exactly: caption, scoped headers, checksum column discipline, double-perforation totals rule. |
| **Badge / tag** | A margin stamplet: bordered rectangle, caps, 4° rotation *only* for hand stamps; machine marks (✓ VERIFIED) sit straight. Never a coloured pill. |
| **Alert / banner** | A block. Urgency in this theme is expressed by position and a stamp, never by a coloured bar across the top: a station notice is BLK-numbered and spooled like everything else. |
| **Toast** | Refused. Nothing floats over the tape. Confirmations are entries (§6.14's confirmation block) or margin ticks (§6.10). |
| **Modal** | Refused. The tape is one surface; a modal would be a second surface pretending to be the first. Anything that would be a modal is a block the tape spools to. |
| **Tabs** | Refused — a tape has no parallel tracks. Parallel content is consecutive blocks; the index (§6.11) is the navigation between them. |
| **Accordion** | Refused in its hiding sense: nothing on the tape is collapsed, because collapsed content on an append-only medium is a lie about what the record holds. Long blocks print long. |
| **Pagination** | Footage. `YOU ARE AT 104.0 M OF 196.0 M` with the block index (§6.11) as the pager. Numbered page links do not exist; block numbers do. |
| **Progress bar** | §6.5's counter. A bar would be a second, vaguer progress claim beside the exact one; the theme permits one. |
| **Spinner** | Refused. Loading is blank tape (§6.15); waiting is the lamp (§6.7). |
| **Search box** | A ruled line in the masthead labelled `FIND IN THE RECORD`; results spool as §6.12 index cards of the matching blocks (§7). No-match prints §6.18's block in place. |
| **Breadcrumb** | The margin itself: footage + current block (§6.5) is the breadcrumb, always visible, always true. |
| **Tooltip** | Refused. If a thing needs explaining, the explanation is printed on the tape, in the margin, permanently — hover-hidden text is unpublished text. |
| **Card** | §6.12's block-card: a perforation-divided segment of the one strip. No shadow, no radius, no lift beyond §6.9's 1°. |
| **Image** | §6.8's dot-matrix cell, always. A raw `<img>` presentation anywhere else on the page fails the gate. |
| **Video** | Refused on the tape. A build with film links out at a perforation, like checkout (§7) — the medium does not pretend to be a projector. |
| **Form error** | §6.14: `--amber-deep` rule + the error printed beneath in `--ink`, in the voice of §12. Never red, never a shake, never an icon-only signal. |
| **Empty state** | §6.18's block. |
| **Footer** | §6.16 exactly: totals, sign-off, stamp, colophon. No link farm. |
| **Skip link** | Printed at the masthead's head, visible on focus: `SKIP TO BLK 0001`. |

## 12. Content & copywriting voice

The tape has two registers, and every word on the page is in
one of them.

**The Machine** prints the record: headers, data, counters,
checksums. Its voice is uppercase, terse, and entirely without
adjectives. It states what was received and what was verified.
It never summarises, never sells, never apologises.

- ✓ `BLK 0027 — ANTENNA TEMPERATURES ……… CHK 4F ✗ 9A`
- ✓ `TAPE: 104.0 M — BLK 0027 OF 49`
- ✗ `Oops! This block had a little hiccup`
- ✗ `Amazing telemetry from an incredible satellite!`

**The Librarian** writes the prose blocks and the form: the
human who keeps the shelf. Sentence case, plain words, dry
warmth, no nostalgia cosplay — the librarian works in the
archive today and writes like it. The librarian explains; the
machine records; a sentence that tries to do both fails.

- ✓ `Helios-3 came over Kiruna-2 at 03:12:04 UTC and was gone
  by 03:47:41. This tape is what the station heard.`
- ✓ `The librarian answers within fourteen days, by post or by
  wire.`
- ✗ `Journey back to a golden age of space exploration!`
- ✗ `Don't miss this historic pass!!`

**Headline style.** Headlines are block titles: a number, a
name, no promise. The one display headline (§6.2) is the
record's own title, not a hook written for the page.

**Label style.** Labels name physical things and states:
`REQUESTS ON FILE`, `END OF RECORD`, `NOT ON THIS TAPE`. A
label that names a feeling (`You're all set!`) is rewritten
until it names a fact (`REQUEST № 313 — RECEIVED`).

**Error-message voice.** Errors are machine findings, stated
flatly, with the remedy printed in the same breath:

- ✓ `THE NAME LINE IS EMPTY. THE LOG CANNOT FILE A REQUEST
  WITHOUT A NAME.`
- ✓ `THE REQUEST COULD NOT BE WRITTEN — YOUR WORDS ARE STILL
  HERE. PUNCH AGAIN.`
- ✗ `Something went wrong 😞`
- ✗ `Invalid input`

**Empty-state voice.** §6.18's fixed strings, verbatim:
`NO TAPE LOADED` / `NOT ON THIS SHELF` / `OUT — RETURN
EXPECTED`. The librarian does not joke about an empty shelf.

**Fixed strings (verbatim, never paraphrased).**

1. `RETRANSMIT REQUESTED` — the stamp, §6.6.
2. `VERIFIED — KIRUNA-2` — the hero stamp, §6.1.
3. `END OF RECORD` — the footer stamp, §6.16.
4. `REQUESTS ON FILE: 312. YOURS WILL BE № 313.` — the form
   preamble, §6.14 (the numbers derive from §6.17; the sentence
   does not change).
5. `THE LIBRARIAN WILL ANSWER FROM THE SHELF, NOT FROM THIS
   TAPE.` — the confirmation's reply line, §6.14/§8.3.
6. `THIS TAPE IS WHAT THE STATION HEARD.` — BLK 0001's closing
   line, §8.1.

**Numbers house style.** Metres to one decimal with a thin
space before the unit (`196.0 M`); counts with comma separators
(`78,400`); times in UTC, 24-hour, seconds always shown
(`03:47:41`) — the record never prints a time it cannot
support to the second; checksums as two uppercase hex digits
after `CHK`. A number that breaks the house style is treated
as a wrong number by the gate.

## 13. Full-page scroll choreography map

Every beat from the head of the tape to its tail, in order.
Footage is cumulative from §6.17; the visitor's experience is
the record's order, and this map is §6.17 read as a journey.

| Beat | Tape position | What the visitor sees and feels |
|---|---|---|
| 1. The desk | before 0.0 M | Buff strip on the aged desk, masthead printed (§6.11), read-head line waiting at centre over bare desk. Stillness. The machine is off but present. |
| 2. Loading the record | 0.0–4.0 M | The spool-in (§6.1): ratchet steps, holes punching, BLK 0001 seating under the head. The visitor's first feeling: this page was *put into* something. |
| 3. The title struck | within BLK 0001 | The punched headline (§6.2) stamps out letter by letter; the `VERIFIED — KIRUNA-2` stamp lands. The counter wakes: `TAPE: 004.0 M`. |
| 4. The station | 4.0–20.0 M (BLK 0002–0005) | The librarian's prose (§12): where Kiruna-2 is, what a pass is, why the tape exists. The lamp begins blinking with the first scroll; the sprocket-step (§6.4) is noticed here, at the first perforations. |
| 5. The record, plain | 20.0–52.0 M (BLK 0006–0013) | The table (§6.13): the whole pass in nine rows. The reader who goes no further has still read the truth entire — the map's most important beat is this early honesty. |
| 6. The long index I | 52.0–104.0 M (BLK 0014–0026) | Thirteen index cards (§6.12), ✓s lighting in order as they cross the head. Rhythm establishes: perforation, card, tick, perforation. The tape creep (§5) is felt in pauses. |
| 7. The failure | 104.0–112.0 M (BLK 0027 + 0027R) | The pointer line, the ✗, the garble, the stamp falling, the tear line drawing, the clean retransmission (§6.6, §8.2). The emotional centre of the page, placed by the record, not by an editor. |
| 8. The long index II | 112.0–160.0 M (BLK 0028–0039) | Twelve more cards. The rhythm resumes — and its resumption *is* the message: after the failure, the record simply continues, verified line after verified line. |
| 9. The plates | 160.0–176.0 M (BLK 0040–0043) | Four dot-matrix images (§6.8) resolving as they pass the head: the dish, the tape room, the pass chart, the night crew. The page's only pictures, earned by 160 metres of print. |
| 10. The request | 176.0–192.0 M (BLK 0044–0047) | The form (§6.14): preamble, ruled lines, the promise of № 313. The visitor may act here (§8.3) or spool on; the tape does not detain them. |
| 11. The end block | 192.0–196.0 M (BLK 0048) | One short block: the station signing off the pass in the librarian's voice, three lines, nothing more. The counter reaches for its total. |
| 12. The accounting | after 196.0 M | The footer (§6.16): counter lands on 196.0 M as the end block centres; totals print; `END OF RECORD` stamps down; the lamp blinks its three slow blinks and holds. The strip ages into the desk and the holes stop. The visitor has read a whole record and the page *closes* — a feeling almost no website gives. |

**Reverse pass.** Scrolling back up is rewinding: the footage
counts down (§6.5), lines re-light as they cross downward
through the head, and every latch holds — stamps stay down,
✓s stay lit, images stay resolved, the tear line stays drawn.
The map's beats do not un-happen; only position reverses.
**Jump scroll.** A jump (index click, End key) lands the tape
seated at the target with all intermediate latches in their
true states (§6.11) — the machine fast-forwards honestly: it
does not pretend the skipped metres were read, and the counter
shows position, not virtue.

## 14. Whole-page performance budget

| Budget line | Limit | Notes |
|---|---|---|
| Total page weight (first load) | ≤ 640 KB | Of which images ≤ 480 KB (4 plates × ≤120 KB, §6.8); the record itself is text and costs almost nothing — weight discipline is spent where the medium is heavy. |
| JS | ≤ 38 KB gz | The shared loop + stamper + form script (§6.14's ≤5 KB included). No framework: the machine is hand-built, like the reader. |
| CSS | ≤ 22 KB gz | The strip, the grid, the matrix texture. |
| Fonts | Plex Mono 400/500/700, subset to the record's character set + Latin-1 | ≤ 64 KB total woff2. The 5×7 bitmap table (§6.2) is data, ~2 KB, counted under JS. |
| Per-frame cost (scroll, mid-range phone) | ≤ 1.4 ms | The loop's whole work: lerp, one line-lighting update (§6.3), one offset write (§6.4), counter check (§6.5), at most one canvas cell (§6.8). |
| Long tasks | none > 50 ms | The headline's 840 dots build in 3 passes split across frames (§6.2). |
| Animation count | 1 rAF loop, 2 licensed ambient loops (§5) | The lamp is loop-driven; the creep is the loop at idle. There is no third clock on the page. |

**Cut order** — when the budget is exceeded, cut in this order,
and stop cutting the moment the budget is met:

1. The tape creep (§5) — the page's one pure luxury.
2. Image densities from three to two (§6.8's mobile treatment
   at all widths).
3. The sprocket-step amplitude 3px → 2px (§6.4).
4. The headline's per-character stagger 26ms → 13ms (the
   ceremony shortens; the punching itself is not cut).
5. The tear transition (§6.10) shortens to its mobile timing.

**Never cut, at any budget:** the read-head (§6.3), the footage
counter's accuracy (§6.5), the parity pair's garble and stamp
(§6.6), any watchdog, any reduced-motion variant, the no-JS
completeness of the record. A build that cuts a never-cut item
to meet the budget has not met the budget; it has changed the
theme.

## 15. Build-order checklist

The sequence in which this theme is implemented. Each step is
done before the next begins; the record comes first because
everything else is derived from it.

1. **Declare the record.** Write §6.17's Pass Record object —
   every field, the block list, the garble map, the counts.
   Nothing is designed before this exists.
2. **Print the tape statically.** The full page as pure HTML/CSS:
   strip, sprocket columns, perforations, all 49 blocks, the
   table, the form, the footer — complete and readable with no
   script. This state is the product's floor and its fallback;
   it is reviewed on its own before any motion is added.
3. **The character grid.** Verify §3's discipline on the static
   build: 72ch measure, checksum column at ch 64–72, header =
   one line, per §10's grid audit.
4. **The shared loop.** One rAF, the lerped progress value, the
   watchdog registry. Nothing animates before this exists —
   no element may bring its own clock.
5. **The read-head.** §6.3's line and line-lighting, driven by
   the loop. The page's clock is now running.
6. **Footage & lamp.** §6.5's counter and §6.7's lamp, both
   reading the loop and the record. Verify the counter's
   maximum against the record before proceeding.
7. **The sprocket-step.** §6.4's quantised offset, tuned
   against §10's scroll-feel check at first-pass amplitude.
8. **The spool-in & headline.** §6.1 and §6.2, with their
   watchdogs registered before their ceremonies are armed.
9. **The parity pair.** §6.6: garble from the record's map,
   stamp, tear line. Run §10's checksum and garble audits now,
   while the pair is the newest thing on the page.
10. **Images.** §6.8's cells, aspect boxes first (the geometry
    rule, §6.5), canvas treatment second.
11. **Index, cards, table lighting.** §6.11's scrollspy,
    §6.12's ✓ lighting, §6.13's row sweeps — all from the
    loop's boundary table.
12. **The form.** §6.14 with its idempotency token and 4000ms
    watchdog; the confirmation block printed from the record's
    count.
13. **Loader, transitions, ticks.** §6.15's blank tape, §6.10's
    punch and tear, §6.9's hover system.
14. **The footer & the empty page.** §6.16 and §6.18; run the
    three-printings audit (§10.1) end to end.
15. **The gate.** All of §10, signed by a non-builder, including
    the watchdog drill, the no-JS pass and the reduced-motion
    pass. Only then may the theme ship.
