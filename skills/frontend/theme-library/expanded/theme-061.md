# 61. The Flight Director's Ledger — Expanded (v1 + v2)

> A 1968 mission-control flight log kept by hand — the whole
> site is one continuous ruled ledger page where a mission's
> story is written in, stamped, and signed off entry by entry.
> Data becomes handwriting, not dashboards. The page is not a
> history site wearing a typewriter font. It is the log itself:
> paper that feeds in, a headline typed by the flight director's
> own machine, entries written as the reader arrives at them,
> one mistake struck through and corrected in carbon blue rather
> than erased, and a margin ruler that has been ticking off
> mission elapsed time since the first line.

**The theme's one law: nothing is on this page that is not in
the log, and the log does not erase.** Every figure printed
anywhere traces to the one declared Mission Record (§6.17) and
is printed at record precision — insertion at T+00:11:48, never
"about twelve minutes in"; cabin pressure 4.9 psi, never "about
5". The one error in the record is struck through in pencil and
corrected above the line in carbon blue (§6.4); it is never
deleted, never hidden, and never repeated as a gimmick anywhere
else on the page. Stamp-pad red is spent on stamps and stamps
only — LOGGED, CONFIRMED, FILED — and the quality gate (§10)
greps the build to prove no error message, badge or link ever
borrowed it. And no entry may be hidden by its own theatre:
the ledger ships fully typed, complete in the DOM, and every
type-in, stamp and scrub is an enhancement the script arms over
the finished page, each with a named watchdog. A build that
rounds a timestamp, erases the mistake, spends the red on an
error, or leaves a line blank when a trigger is missed has
broken the law four ways.

---

## 1. Concept & world

**The world.** Houston, November 1968. A flight director keeps
the mission log by hand and typewriter on a ruled ledger sheet:
one line per event, a timestamp in the margin, initials beside
every entry, stamps for the moments that matter. The sheet is
the mission's memory — the consoles, the loops and the
telemetry all feed into it, and when the flight is over the
sheet is what remains. This theme takes that sheet as the
entire interface. There are no dashboards, no cards floating on
a background, no chrome: there is a page, its ruling, its
margin, and what has been written in it.

**The story the page tells.** One flight, Kestrel IV, from
liftoff to splashdown in twelve entries (§6.17). The reader
does not browse the mission; the reader *keeps* it — entries
are typed as they reach the centre rule, the margin ruler's
hand advances with the reading, the flight strip clipped to
the top of the sheet names the phase the reader is inside, and
at the end the reader is invited to do the one thing a visitor
to an archive can do: request the file, and have the request
entered as the log's next numbered item (§6.14).

**Mood.** Calm under load. The prose is terse because the
people were busy; the page is warm because the paper is. The
emotional register is competence recorded plainly — a signal
lost for four minutes and reacquired "on schedule", a crew
that "asks for more work. None given." Premium here is not
polish; it is the feeling that every line was written by
someone who was there and initialled by someone who checked.

**Best-fit sites and audiences.**

- Space, aviation and engineering heritage brands, museums and
  archives publishing a real chronology.
- Any organisation whose product is *a record kept well*:
  audit and compliance tools, observatories, expedition and
  survey outfits, race and rally timing, restoration workshops
  publishing a build log.
- Long-form storytelling: a launch, a voyage, a season, a
  construction — anything with a timeline that deserves
  timestamps rather than chapters.
- Audiences who read: engineers, historians, enthusiasts,
  students. The theme rewards slow reading and punishes
  skimming by design — that is a feature to sell, not hide.

**When NOT to use it.**

- Anything that needs live data. The ledger is a record of
  what happened; a real-time dashboard in this theme is a lie
  in period costume. (A "live" page may *replay* a log; it may
  not pretend the typewriter is a sensor.)
- E-commerce checkout, pricing tables, comparison grids. The
  sheet has one column and one voice; a store needs neither.
  §7 routes checkout out of the ledger entirely.
- Short-attention landing pages. If the whole message must
  land in five seconds, a page whose first act is a headline
  typing itself is the wrong instrument.
- Brands that cannot tolerate a visible mistake. The struck-
  through correction (§6.4) is load-bearing: a client who
  wants it removed wants a different theme, and §9 says so.

## 2. Palette

Five anchors from the original entry, unchanged. Six derived
tokens do the daily work. Contrast values are measured from
the hex values for this expansion.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--paper` | `#F2ECDC` | Ledger paper cream — the sheet itself, all grounds | ~78% of pixels | Ground for graphite text (9.5:1) and carbon entries (7.6:1) |
| `--graphite` | `#3B3A36` | Pencil graphite — body text, rules that carry meaning, the plot | ~14% | On paper 9.5:1 — the page's reading contrast |
| `--stamp` | `#B3402A` | Stamp-pad red — stamps only: LOGGED, CONFIRMED, FILED | <1%, stamps only | On paper 6.7:1 — legible at stamp sizes; forbidden for text, errors, links (§10 census) |
| `--carbon` | `#2E4A6B` | Carbon-copy blue — corrections, the ghost, links, the route | ~4% | On paper 7.6:1 — may set body-size text; the only blue on the sheet |
| `--ruling` | `#C9C2AC` | Faded ruling — the sheet's horizontal rules, hairlines | ~3% | On paper ~1.5:1 — hairlines only, never text, never a border that carries meaning |
| `--paper-deep` | `#E6DCC2` | Aged paper — the sheet's edge shade, skeleton lines' ground, footer band | within paper share | Graphite on paper-deep 8.6:1 |
| `--graphite-soft` | `#6E6A61` | Soft pencil — margin notes, exhibit captions, retired timestamps | ~2% | On paper 4.9:1 — captions and marginia only, never entry text, never below 12px |
| `--carbon-pale` | `rgba(46,74,107,0.14)` | The carbon ghost's ink (§6.5) | transient | A duplicate at one-line offset; decorative layer over printed text, never the only copy |
| `--stamp-bloom` | `rgba(179,64,42,0.16)` | The imprint bloom behind a fresh stamp (§6.7) | transient | Fades to a printed `--stamp` at full strength; the bloom is ink still wet |
| `--tape` | `rgba(238,230,198,0.62)` | Tape strips on exhibit frames (§6.9) | <1% | Translucent over photo corners; sheen is a lighter band of the same token |
| `--coffee` | `rgba(122,84,40,0.13)` | Coffee-ring stains at two margins (§4) | 2 rings, fixed | A stain, not a colour: never text, never a background fill, never a third ring |

**Rules that outrank the table.**

- **The red census.** `--stamp` may appear only inside stamp
  elements (`.stamp` and its imprint states). The gate (§10)
  greps the shipped CSS and JS: any other reference — an error
  style, a "new" badge, a sale price, a required-field asterisk
  — fails the build. Errors speak in graphite and carbon (§12).
  Red on this page means *a person authorised this*, and the
  meaning survives only if nothing else is allowed to mean it.
- **Carbon is the colour of the second copy.** Corrections,
  the ghost, links and the flight-plan route are carbon blue
  because all four are the same thing in the ledger's world:
  the copy, the amendment, the reference elsewhere. A carbon
  heading or a carbon button is a category error.
- **Graphite sets every sentence.** Entry text, body copy and
  table figures are graphite. Special Elite's typed display is
  graphite too — the typewriter's ribbon was black; the red on
  the sheet comes only from the stamp pad.
- **The ruling never argues.** `--ruling` lines organise the
  page and carry no information; any line that *does* carry
  information (the progress rule, §6.10; the route, §6.6) is
  drawn in graphite or carbon at full strength so the reader
  can tell the sheet's furniture from its writing.
- **Dark-mode behaviour.** There is no dark mode. The sheet is
  paper under a lamp in 1968; an OS dark preference does not
  repaint an archive. Forced-colours mode is honoured by
  removing the paper tint and stamps' fill (stamps become
  outlined text) while keeping every word — see §6 elements'
  accessibility specs.

## 3. Typography

Two families, as in the original entry — **Special Elite** for
typewriter display, **IBM Plex Mono** for entries, timestamps
and readouts. There is no third voice and no handwriting font:
the director's hand appears as behaviour (pencil strokes,
stamps, initials in mono), never as a script typeface — a
handwriting font is the theme's most common counterfeit (§9).

**Type scale** (ledger-based: sizes are set against the 32px
ruled line, §4, so text always sits on the ruling):

| Role | Font | Size / line-height | Tracking | Used for |
|---|---|---|---|---|
| Display | Special Elite 400 | 44px / 64px (2 ruled lines), clamp 30–48px | 0 | The typed headline — one per page |
| Entry head | Special Elite 400 | 21px / 32px | 0 | Entry titles (`ORBIT INSERTION`), phase names on the strip |
| Body / entry | IBM Plex Mono 400 | 15.5px / 32px (one ruled line) | 0 | Log entries, explanatory copy — the log is the body |
| Margin | IBM Plex Mono 500 | 12.5px / 32px, tabular | +0.02em | Timestamps (T+ and GMT), initials, exhibit numbers |
| Data | IBM Plex Mono 500 | 15.5px / 32px, tabular | 0 | Table figures, readouts, the MET hand's figures |
| Label | IBM Plex Mono 500 | 11px / 16px | +0.16em, uppercase | Stamp-adjacent labels, index heads, form labels |
| Stamp | Special Elite 400 | 15–19px / 1 | +0.06em, uppercase | LOGGED, CONFIRMED, FILED — set in the typewriter face because the stamps were typed on their dies |

**Type laws.**

1. **Timestamps are dual, always.** Every entry carries both
   clocks: mission elapsed time (`T+05:47:05`) and GMT
   (`14 NOV 1968 · 20:19:05`). One clock is the mission's, the
   other is the world's; the log keeps both and a timestamp
   with only one is an anecdote.
2. **Numerals are mono and tabular, always.** No figure ever
   appears in Special Elite — the typewriter types words and
   titles; figures are entered in the mono hand so columns of
   entries align digit-for-digit down the sheet.
3. **Typed text sits still.** The mechanical jitter (§6.1)
   belongs to the act of typing and ends with it. A headline
   that keeps trembling after it is typed is a broken
   typewriter, not a style; body entries never jitter at all.
4. **The correction is set above the line, in carbon.** A
   struck word stays on its line in graphite under a pencil
   stroke; its correction is entered in the interlinear space
   above in carbon blue (§6.4). Corrections are never set in
   red, never in a margin, never in a footnote — the log
   corrects itself where it stands.
5. **Uppercase is rationed to stamps, phases and labels.**
   `LIFTOFF`, `CONFIRMED`, `EXHIBIT B`. Sentences in uppercase
   are a shout, and nobody in the front room shouts — not even
   during the four minutes of lost signal (§6.17, № 009).

---

## 4. Layout language

**One sheet.** The page is a single continuous ledger sheet:
a `--paper` ground ruled with horizontal `--ruling` lines
every 32px (the line grid all type sits on, §3), running the
full height of the document without section breaks, cards on
backgrounds, or alternating bands. Sections are entries. The
sheet's edges are the viewport's edges on mobile and a centred
1,160px column on desktop, shaded at the very edge with
`--paper-deep` for the last 24px — the thickness of the pad.

**The margin column.** A 148px margin at the left of the sheet
(desktop) carries what margins carry: timestamps (T+ above
GMT, §3 law 1), initials, exhibit numbers, and the elapsed-
time ruler (§6.3) fixed within it. A single vertical rule in
`--ruling` separates margin from body; the one vertical line
that carries information — the ruler's track — is graphite.
Nothing else lives in the margin except the two coffee rings
(§2), which sit at the margin of entries № 004 and № 009
because that is where the cup was put down: beside the
correction and beside the lost signal. Their positions are in
the record (§6.17), not in a designer's whim.

**Entry anatomy.** Every entry is the same furniture, in the
same order: margin block (entry number, T+, GMT, initials) →
ruled entry line with its title in Entry-head type → body lines
on the ruling → the director's sign-off mark (a short graphite
rule and initials) where the record has one. Entries are
separated by exactly three blank ruled lines — the ledger
breathes in lines, not in pixels of empty background, and the
blank lines are ruled like all the others: the sheet was ruled
before anything was written on it.

**Density rules.** One entry per screen at desktop reading
size, roughly; never two entry titles in one viewport if the
entries can be given their lines. Tables (§6.13) are the only
dense region — a table is the log summarising itself, and its
density is the point. Photography appears only as exhibits
(§6.9), taped to the sheet at the entry it proves, never as
full-bleed atmosphere: the sheet has no bleed.

**The reading line.** Scroll-driven reveals key to a "centre
rule" at 55% of viewport height — slightly below centre,
because the eye reads a ledger a little below where it looks.
The pinned flight strip (§6.11) rides the top of the sheet
like the strip clipped to the director's board, and the
margin ruler (§6.3) and progress rule (§6.10) are the same
instrument read two ways: how long the mission has run, and
how much of this entry has been read.

## 5. Full motion system

One shared `requestAnimationFrame` loop drives every scrubbed
value on the page (lerp **0.11** — the weight of a carriage
being eased, not snapped). Everything else is triggered,
timed, and finished: this theme's motion is a sequence of
*acts of record* — typing, stamping, pencilling — each with a
beginning, an end, and a printed result that stays.

**Named easings** (the ledger's own; no generic ease may be
substituted):

| Token | Curve | Used for |
|---|---|---|
| `--ease-type` | `steps(1)` per character with randomised 55–85ms intervals (JS-timed, not CSS) | Typing (§6.1, §6.2) — a typewriter has no easing, it has a mechanism |
| `--ease-thump` | `cubic-bezier(0.2, 2.2, 0.36, 0.9)` settling by 260ms | Stamps and stamp-thump clicks (§6.1, §6.7) — compression with one overshoot, then stillness |
| `--ease-pencil` | `cubic-bezier(0.45, 0, 0.3, 1)` | Pencil strokes: underlines, the strike-through, the route (§6.4, §6.6, §6.8) — a hand accelerating then lifting |
| `--ease-drift` | `cubic-bezier(0.25, 0.6, 0.3, 1)` | The carbon ghost's lag, tape sheen, parallax layers (§6.5, §6.9) |
| `--ease-feed` | `cubic-bezier(0.6, 0.05, 0.3, 1)` | Paper feed-in and the carbon-sheet transition (§6.15) — heavy at the start, decisive at the end |

**Motion-term translation table** — every standard term, in
this theme's language, or refused with its reason:

| Term | In this theme |
|---|---|
| Scroll-triggered reveals | Entries type in as they cross the centre rule (§6.2) |
| Scroll-driven / scrub | Margin ruler hand (§6.3), ink-filling progress rule (§6.10), route pencil (§6.6) — all from the one loop |
| Parallax | Carbon ghost at 0.96× (§6.5), margin notes and coffee rings at pencil depth (§4) — shallow, ≤8px of travel; deep parallax would tear the sheet |
| Pinned sections | The flight-phase strip (§6.11) pins like a strip clipped to the board; nothing else pins — a ledger is read down, not staged |
| Smooth scrolling | Native, plus carriage increments: `scroll-snap-type: y proximity` at entry tops on ≥1200px only, so the sheet settles at entries without ever trapping the reader (§6.2 edge cases) |
| Progress indicator | The ruled line filling with ink, timestamped at each quarter (§6.10); a progress *bar* is refused — the sheet has lines, not bars |
| Staggered reveals | Entries stagger line by line at 30ms, a typist's returns (§6.2) |
| Masked reveals | Refused. A mask hides writing; the ledger's reveals *produce* writing (typing, pencilling) instead of uncovering it |
| Blur-to-sharp | Refused. Blurred text reads as a smudged carbon; the ghost (§6.5) is the theme's only softness and it is a second sheet, not a blur |
| Kinetic typography | The typing itself (§6.1) and the mission clock's flipping mono digits (§6.3) — type moves when a machine moves it, never decoratively |
| Marquee | Refused. Nothing in a control room scrolls sideways forever; the phase strip (§6.11) changes state, it does not travel |
| Counters | MET and entry numbers count in mono at record precision (§6.3, §6.17) — a counter that lands anywhere but the record's figure is a broken instrument |
| SVG line-draw | The flight-plan route pencilling itself (§6.6) and the pencil underline (§6.8) |
| Image scale-in-frame | Exhibits scale 1.05 → 1.0 inside taped frames (§6.9) |
| Hover / micro-interactions | Pencil underline (§6.8); stamp-pad rock on cards, max 3° (§6.12) — magnetic hover is refused: paper does not follow a hand it cannot feel |
| Custom cursor | Refused — normal system cursor only (standing rule). The ledger is paper; the pointer is the reader's finger, and the theme does not draw on the reader |
| Skeleton loading | Faint ruled lines with a blinking caret (§6.15) — the sheet before the typing starts |
| Page transitions | A carbon-copy sheet slides over and lifts away (§6.15) |
| Reduced motion | The ledger arrives fully typed; stamps static at their angles; the ghost printed as a still duplicate (§6 elements, per element) |

**Ambient loops — exactly two are licensed.** (1) The paper
grain's sub-1% positional drift on a 14s cycle, as if the sheet
were being handled — it moves the grain, never the text. (2)
The skeleton caret's blink (§6.15), only while a skeleton is
actually on screen. Everything else that moves is triggered
by load, scroll, or the reader's hand, and stops when its act
is done. A third ambient loop is a §9 failure.

**Watchdogs.** Every armed effect registers a deadline with
the shared loop's watchdog registry: typing 90ms per character
past its schedule, the stamp 400ms, the route 2,600ms, the
transition 1,800ms, the form 3,000ms. A missed deadline snaps
the element to its printed end state. The page the reader can
get with JavaScript disabled is the same page, minus the acts
— never minus the record.

---

## 6. Signature elements

### 6.1 The typewriter headline

- **What & why.** The hero headline — the mission's title,
  `KESTREL IV — THE FLIGHT LOG` — types itself character by
  character at load, with mechanical jitter, and the moment the
  last character lands the red LOGGED stamp slams in at −4°
  over the headline's right end. It belongs because the page's
  first act must be the act the whole theme is about: a person
  entering the mission into the record. The headline is not
  displayed; it is *filed*, and the stamp is the filing.
- **Structure.** An `<h1>` in Special Elite containing the full
  headline as real text. The script, when it arms, wraps each
  character in a span and reveals them on the typing schedule;
  before arming — and forever, with no JS — the headline is
  simply printed. The stamp is a separate absolutely-positioned
  element (`.stamp`) with a double-rule border in `--stamp`,
  rotated −4°, initially `scale(1.6)` and transparent only in
  its JS-armed pre-state. The headline's line box reserves the
  stamp's overlap so nothing reflows when it lands.
- **Motion spec.** Trigger: load, after first paint (the sheet
  feeds in first, §6.15, 500ms `--ease-feed`). Typing: 55–85ms
  per character, randomised per keystroke, 1px vertical jitter
  on the character being struck, settling instantly; a carriage
  return between the headline's two lines costs a 260ms pause
  and a 6px leftward snap of the whole block. Full headline:
  31 characters ≈ 2.2s. At the final character +120ms, the
  stamp lands: `scale(1.6 → 1)` and opacity over 120ms under
  `--ease-thump`, with a 2px compression of the sheet beneath
  it (a transform on the hero block, 120ms, recovering by
  260ms) — the thud is in the paper, not in a sound file. There
  is no sound anywhere in this theme.
- **States.** Untyped (pre-arm, printed) / typing / stamped
  (rest — the state the page keeps) / re-typed (never: the
  headline types once per page load, and a return visit in the
  same session arrives already stamped, §6.15's rule).
- **Content merge.** The typed text is the mission's actual
  title from the record (§6.17) and the stamp is the record's
  own status word; remove the mission and there is nothing to
  type. The element is never reused for marketing headlines on
  other pages — sub-pages open with their entry title already
  typed and a smaller stamp only where the record has one.
- **Failure fallback.** Watchdog at (characters × 90ms) + 600ms
  from arm: if typing has not completed, all characters print
  and the stamp lands in its static state. No-JS: headline
  printed, stamp printed at −4° at rest opacity — the shipped
  DOM is the finished hero.
- **Reduced-motion variant.** The headline arrives fully typed
  with the stamp already on it. Nothing types, nothing slams.
  The hero is a photograph of the finished first page, which
  is what the log looks like in the archive anyway.
- **Performance budget & mobile variant.** One timer chain,
  ≤0.1ms/frame; the jitter is a transform on one span at a
  time. Mobile (<768px): the headline sets on three lines at
  30px, typing interval tightens to 45–70ms so the act stays
  under ~2s, and the stamp lands at −4° at 15px — same act,
  smaller sheet.
- **Choreography timeline (v2).** t=0 first paint (sheet
  printed, headline visible in fallback state) → t=0–500ms
  paper feed (§6.15) → t=500ms script arms, characters rewind
  → t≈500–2,700ms typing, carriage return at the line break
  (t≈1,600ms, 260ms pause) → t≈2,820ms stamp lands, sheet
  compresses 2px → t≈2,960ms compression recovered, hero at
  rest → watchdog deadline t≈3,400ms passes unused.
- **State matrix (v2).** *Rest:* typed and stamped. *Hover:*
  none — the headline is a record, not a control. *Focus:* the
  h1 is not focusable; the skip link lands above it. *Active:*
  n/a. *Scrolled-past:* stays typed; the stamp does not
  re-fire on return. *Disabled:* n/a. *Touch:* identical;
  typing is load-triggered, not gesture-triggered.
- **Breakpoints (v2).** ≥1200px: 44px display on two lines,
  stamp 19px at −4° overlapping the second line's right end.
  768–1199px: 36px, stamp 17px. <768px: 30px on three lines,
  stamp 15px, overlap reduced so the stamp never covers a
  typed character — it sits in the line's trailing space.
- **Edge cases & failure modes (v2).** *Slow font load:*
  Special Elite swaps in under `font-display: swap`; typing
  begins only after the face is ready or 900ms passes,
  whichever first, so characters never re-type in a second
  font. *Very long mission title in a CMS variant:* the
  headline wraps to a third line and the typing budget grows
  by the character count — the watchdog formula is per-
  character, so it scales; a title past 64 characters is a
  §10 gate failure, not a layout problem. *Reader reloads
  mid-typing:* a fresh load is a fresh act; no state is
  carried in the DOM.
- **Accessibility spec (v2).** The h1's text is complete in the
  accessibility tree at all times (the character spans are
  `aria-hidden` duplicates of a visually-hidden full string —
  or, simpler and preferred, the spans themselves are the text
  and only their *visibility* is animated, with the full string
  present from first paint in the fallback state). Typing is
  never announced character-by-character; a single polite
  announcement is unnecessary — the heading is simply there.
  The stamp is decorative duplication of the record's status
  and is `aria-hidden`; the status is stated in the entry text
  (§6.17 № 001).
- **Tokens consumed (v2).** `--paper`, `--graphite`, `--stamp`,
  `--stamp-bloom`, `--ease-type`, `--ease-thump`,
  `--ease-feed`, `--dur-type-min` (55ms), `--dur-type-max`
  (85ms), `--stamp-angle` (−4deg).

### 6.2 Centre-rule entry reveals

- **What & why.** Each ledger entry types itself in — line by
  line, ruled line drawing across first — as the entry crosses
  the viewport's centre rule at 55% height (§4). It belongs
  because reading this page *is* the mission unfolding: the
  entry does not exist for the reader until the reader arrives
  at its moment, and then it is written in front of them, the
  way it was written in front of the room in 1968.
- **Structure.** Each entry is an `<article>` with the §4
  anatomy: margin block, title line, body lines, sign-off. Body
  lines are real text lines in the DOM (the entry ships
  complete). When armed, the script sets each line's clip to
  zero width and the entry's title rule to undrawn; an
  IntersectionObserver on the centre-rule band triggers the
  write sequence. Lines are revealed by clip, not re-typed
  character-by-character — the entry was typed by the room's
  machine in one pass, and line-level reveal keeps a long
  entry's act under 1.4s.
- **Motion spec.** Trigger: entry's title crossing the centre
  rule. Sequence: the entry's ruled line draws left→right over
  300ms `--ease-pencil`; then lines reveal at 30ms stagger,
  each line's clip opening over 180ms `--ease-pencil` with the
  faintest carbon edge at the reveal front (the line is being
  laid down, not faded in — opacity is never animated on text).
  The margin block (T+, GMT, initials) prints with the first
  line, not before: the timestamp belongs to the act.
  Sign-off mark draws last, 200ms. Total for a five-line entry:
  ≈1.35s. Entries already above the centre rule on load are
  written instantly (they are history the reader has passed).
- **States.** Unwritten (pre-arm only; the DOM is written) /
  writing / written (rest, permanent) / re-entered (stays
  written — the log does not unwrite on scroll-up).
- **Content merge.** The reveal is the entry's own content
  arriving; there is no separate animation layer. An entry
  with a photo (§6.9) or the correction (§6.4) runs its own
  act inside the same sequence, cued by the same trigger.
- **Failure fallback.** Per-entry watchdog: 1,800ms after the
  trigger should have fired (armed via a scroll listener
  backup to the observer), the entry snaps to fully written.
  Observer unsupported → all entries written at arm time.
  No-JS: all entries printed. Nothing on this page may depend
  on the observer existing.
- **Reduced-motion variant.** Entries are simply present.
  The centre rule does nothing; scrolling the ledger is
  reading a finished book, which the archive copy is.
- **Performance budget & mobile variant.** One observer, clip
  updates on ≤6 lines per entry, ≤0.3ms/frame during a write.
  Mobile (<768px): the margin block moves above the title
  (stacked, §4), lines reveal in the same sequence, stagger
  tightens to 24ms so a long entry stays under ~1.2s.
- **Choreography timeline (v2).** Entry title reaches centre
  rule → t=0 rule draws (300ms) → t=150ms margin block prints
  → t=300ms first body line opens → lines follow at 30ms
  stagger, 180ms each → final line + sign-off draw (200ms) →
  entry at rest, latched. Watchdog deadline: trigger + 1,800ms.
- **State matrix (v2).** *Rest:* written. *Hover:* the entry
  is not a control; its links and cards carry their own states
  (§6.7, §6.8, §6.12). *Focus:* focus entering an unwritten
  entry writes it immediately (a keyboard reader must never
  tab into a blank line). *Active:* n/a. *Scrolled-past:*
  written, latched. *Disabled:* n/a. *Touch:* identical;
  reveals are scroll-triggered.
- **Breakpoints (v2).** ≥1200px: full margin anatomy, snap-
  proximity active (§5). 768–1199px: margin narrows to 120px,
  no snap. <768px: margin stacks above the title; the centre
  rule stays at 55%; line stagger 24ms.
- **Edge cases & failure modes (v2).** *Jump-scroll (reader
  drags the scrollbar to the end):* every entry passed is
  written instantly in order — the loop processes the backlog
  as state, not as twelve simultaneous typings. *Scroll back
  up:* nothing unwrites (§5 reverse rule). *Entry longer than
  the design expects (a CMS entry of 14 lines):* the sequence
  caps at 1.8s by tightening the stagger to a floor of 12ms —
  the act shortens, the text is never truncated. *Entry
  shorter (one line):* the rule draw and sign-off still run;
  a one-line entry is a complete act.
- **Accessibility spec (v2).** Entries are articles with their
  titles as headings; the reveal animates clip only, so the
  accessibility tree holds the full text from first paint.
  Focus-into-entry forces the written state (above). The
  centre-rule trigger is visual only; nothing about the
  content's availability to assistive technology depends on
  scroll position.
- **Tokens consumed (v2).** `--graphite`, `--ruling`,
  `--carbon`, `--ease-pencil`, `--dur-line-draw` (300ms),
  `--dur-line-open` (180ms), `--stagger-line` (30ms),
  `--reading-line` (55%).

### 6.3 The elapsed-time margin ruler

- **What & why.** A vertical ruler in the margin whose hand
  scrubs with scroll depth, ticking off mission elapsed time —
  T+ readouts against the record's total of 76:18:00 — with a
  small tick-jump as each entry passes. It belongs because on
  this page progress is not a percentage; it is *how long the
  mission has run*, and the ruler is the clock the director
  actually watched. How far you have read is how far the
  flight has got.
- **Structure.** A fixed-within-the-margin track (graphite,
  2px) running the sheet's full height, with tick marks at
  each entry's T+ position (computed from the record, §6.17)
  and longer ticks at the four quarter marks (§6.10). The hand
  is a small graphite wedge with a mono readout beside it
  (`T+31:15:44`) in Margin type. The readout is a real text
  node updated by the loop; the wedge is a transform. Below
  1200px the ruler leaves the margin and becomes a slim track
  under the masthead (§6.11) with the same readout.
- **Motion spec.** The hand's position is the page's scroll
  progress mapped onto the record's total MET, read from the
  shared loop's lerped value (0.11) — so the hand *eases*
  through time rather than jumping with the wheel. At each
  entry tick, the hand gives a 40ms tick-jump: a 2px overshoot
  and settle, the mechanical register of a clock that counts
  in events, not in seconds. The readout's digits flip in mono
  (each digit slot rolls one step, 60ms) as values change —
  the mission clock flipping its number wheels (§5). The hand
  never runs backwards past an entry already passed: on
  scroll-up it retreats freely *within* the current entry's
  span but the furthest-entry marker (a small carbon tick)
  stays at the deepest point reached — the log remembers how
  far the flight got even when the reader looks back.
- **States.** Running (scrolling) / resting (at an entry —
  the hand sits on the tick) / at total (footer reached: hand
  at 76:18:00, readout prints `T+76:18:00 · LOG CLOSED`).
- **Content merge.** The ruler's ticks *are* the entries —
  their T+ positions from the record, spaced by real elapsed
  time, so the long quiet stretch between № 008 and № 009 is
  visibly longer on the ruler than the crowded first hour.
  The margin's emptiness is the mission's pacing, drawn.
- **Failure fallback.** The ruler is loop-driven decoration
  over a complete page: if the loop dies, the hand parks at
  the top and the readout prints the record's total
  (`T+76:18:00 TOTAL`) — a static label, still true. No-JS:
  the margin carries the entries' printed timestamps only;
  the ruler track and hand are script-added enhancements and
  are absent, leaving the sheet exactly as archived.
- **Reduced-motion variant.** No hand, no flipping digits.
  The margin prints each entry's T+ as it always does, and a
  single static line at the sheet's head gives the total.
  Time on the reduced page is read, not watched.
- **Performance budget & mobile variant.** One transform + one
  text update per frame, throttled to when the lerped value
  changes by ≥1 second of MET; ≤0.1ms/frame. Mobile: the
  track under the masthead is 100% wide, the readout sits at
  its right end, tick-jumps are cut (the hand simply arrives).
- **Choreography timeline (v2).** Scroll begins → hand leaves
  the entry tick after the lerp catches up (~90ms) → readout
  digits flip as seconds accumulate → entry tick reached →
  40ms tick-jump, carbon furthest-marker advances → scroll
  stops → hand settles on or between ticks → footer reached →
  hand at total, `LOG CLOSED` prints beside it.
- **State matrix (v2).** *Rest:* hand on the current tick.
  *Hover:* hovering the ruler prints the hovered position's
  T+ in the readout (a preview, graphite-soft) without moving
  the hand. *Focus:* the ruler is not focusable; it is an
  instrument, not a control. *Active:* n/a. *Scrolled-past:*
  the furthest-marker persists. *Disabled:* n/a. *Touch:* no
  hover preview; the hand and readout behave identically.
- **Breakpoints (v2).** ≥1200px: margin ruler, full ticks and
  readout. 768–1199px: ruler in a narrowed 120px margin,
  quarter ticks only, readout retained. <768px: under-
  masthead track, readout at right, entry ticks drawn but
  unlabelled.
- **Edge cases & failure modes (v2).** *Entries reordered in
  a CMS:* ticks are computed from the record's T+ values at
  build, sorted ascending — a mis-ordered entry list fails
  the §10 record validation before it can bend the ruler.
  *A page shorter than the mission (detail pages):* the ruler
  maps to that page's own span of the record (a single-entry
  page's ruler runs from that entry's T+ to the next entry's),
  declared per page in §7. *Reader at exact total:* the hand
  clamps at 76:18:00; footer overscroll cannot push it past
  splashdown.
- **Accessibility spec (v2).** The ruler is `aria-hidden` as an
  instrument; its information content — each entry's T+ — is
  printed in the margin text beside every entry, where screen
  readers meet it in order. The live readout is *not* a live
  region: a clock that announces itself 60 times a minute is
  a denial-of-service on the reader's ears.
- **Tokens consumed (v2).** `--graphite`, `--graphite-soft`,
  `--carbon`, `--ruling`, `--loop-lerp` (0.11),
  `--dur-tick` (40ms), `--dur-digit` (60ms).

---

### 6.4 The struck-through mistake

- **What & why.** Entry № 004 contains the log's one admitted
  error: the line types `Cabin pressure falling.` — then a
  hand-drawn pencil stroke strikes the word *falling* (300ms),
  a beat passes, and the correction is typed in carbon blue in
  the interlinear space above: `holding at 4.9 psi. Gauge fault
  traced to the panel, not the cabin.` It belongs because it is
  the theme's thesis performed inside the record itself: this
  archive is trustworthy not because it is flawless but because
  its flaw is still visible, corrected where it stands. The
  brand's honesty is not claimed in copy; it is *in the log*.
- **Structure.** The entry's line is real text: the struck word
  in a `<s>`-equivalent span (a styled span with the pencil
  stroke as an inline SVG laid over it, stroke path slightly
  irregular, hand-plotted points), and the correction as an
  interlinear line above, in `--carbon`, in Body type at 14px,
  left-aligned to the struck word. In the shipped DOM both are
  fully present: the stroke drawn, the correction printed. The
  script rewinds the stroke's dashoffset and hides the
  correction's typed state only when it arms the sequence.
- **Motion spec.** Trigger: the entry's own centre-rule write
  (§6.2), at its line's turn — the mistake is made *during* the
  entry's typing, not as a separate show. Beat by beat: the
  line types with the wrong word → 500ms hold (the room
  notices) → the pencil stroke draws across *falling* over
  300ms `--ease-pencil`, with the stroke's pressure varying
  (stroke-width 2.5px → 1.5px, a hand pressing then lifting) →
  350ms hold → the correction types in carbon at 40ms per
  character above the line → the entry continues to its next
  line. Total added time to the entry's write: ≈2.6s. It runs
  **once** — first write only, never on re-entry, never on any
  other entry. There is exactly one mistake in this log.
- **States.** Unmade (pre-arm) / typing-wrong / struck /
  corrected (rest, permanent). The corrected state is the
  shipped state; the sequence is a re-enactment the script
  performs once for a first-time reader.
- **Content merge.** The error is inside a real record entry
  whose figures (4.9 psi) are the record's figures (§6.17);
  the correction is the entry's actual content, not a caption
  about honesty. Remove the performance and the printed entry
  still carries the strike and the correction — the archive
  copy is identical, only less alive.
- **Failure fallback.** Watchdog at the entry's write deadline
  +1,200ms: stroke drawn, correction printed, entry complete.
  No-JS: the finished, corrected entry, which is the truth of
  the document anyway.
- **Reduced-motion variant.** The entry arrives in its
  corrected printed state. The mistake is still visible —
  struck, corrected — because the *fact* of the correction is
  content; only its re-enactment is motion.
- **Performance budget & mobile variant.** One SVG stroke
  animation + one short typing chain; ≤0.2ms/frame. Mobile:
  the interlinear correction sits above the line as on
  desktop (the line grid has room — the entry's lines are
  double-spaced by the §4 anatomy wherever a correction
  lives); typing interval 32ms/char so the beat stays tight.
- **Choreography timeline (v2).** Entry write reaches the
  line → line types with *falling* → t=+500ms hold → stroke
  draws 300ms → t=+1,150ms hold ends → correction types
  (≈38 chars × 40ms ≈ 1.5s) → entry's next line begins →
  entry completes, initialled PN (§6.17). Watchdog: write
  deadline + 1,200ms.
- **State matrix (v2).** *Rest:* corrected entry, stroke and
  carbon line printed. *Hover:* hovering the struck word
  prints nothing extra — the log does not annotate its
  annotation. *Focus:* if focus lands in the entry mid-
  sequence, the sequence completes instantly to the corrected
  state (§6.2's rule). *Active:* n/a. *Scrolled-past:*
  corrected state. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: as specified. 768–1199px:
  correction at 13.5px, still interlinear. <768px: the line
  wraps; the correction prints above the *wrapped segment*
  containing the struck word — the layout reserves the
  interlinear line in the entry's grid so wrapping never
  pushes the correction onto a different line's space.
- **Edge cases & failure modes (v2).** *A second mistake in a
  CMS variant:* forbidden by the record — §10's gate counts
  strike-throughs on the page; the count must be exactly one.
  *Long correction text:* the record's correction is fixed at
  build; a variant correction longer than the line wraps
  within its interlinear band (two interlinear lines are
  reserved) and the typing interval tightens to hold the
  ≈2.6s budget. *Reader scrolls away mid-sequence:* the
  sequence completes off-screen and latches; returning shows
  the corrected entry.
- **Accessibility spec (v2).** The struck word is marked with
  a real `<s>` element so assistive technology announces it
  as struck; the correction is a normal line of text read in
  order, prefixed in the text itself by the entry's flow (the
  sentence reads correctly with the correction substituted).
  The stroke SVG is `aria-hidden`. Contrast: carbon on paper
  7.6:1 at 14px — passes for body text; the struck graphite
  under the stroke remains 9.5:1 stock, legible through the
  2px stroke by design (a strike you cannot read through is
  an erasure, and the log does not erase).
- **Tokens consumed (v2).** `--graphite`, `--carbon`,
  `--ease-pencil`, `--dur-strike` (300ms),
  `--dur-correct-type` (40ms/char), `--hold-notice` (500ms).

### 6.5 The carbon-copy ghost

- **What & why.** A faint carbon-blue duplicate of the entry
  currently at the centre rule drifts exactly one ruled line
  behind the real text, parallaxed at 0.96× — visible at the
  edges of lines as the reader scrolls, like the copy sheet
  shifting under the original. It belongs because the ledger
  was a carbon set: every entry existed twice the moment it
  was typed, once for the room and once for the file. The
  ghost is the file copy being made of the very entry being
  read.
- **Structure.** A duplicate of the active entry's text block,
  rendered in `--carbon-pale`, positioned one line (32px)
  below the real block and offset by the parallax delta,
  `aria-hidden`, `pointer-events: none`, clipped to the
  entry's own box so it never bleeds into the next entry's
  lines. Only one ghost exists at a time — for the entry at
  the centre rule; when the centre rule passes to the next
  entry, the ghost is re-laid under that entry. The ghost is
  generated by the script from the entry's own DOM text (never
  a second copy in the markup), so the two can never disagree.
- **Motion spec.** Continuous, from the shared loop: the
  ghost's vertical offset = real position × 0.96 relative to
  the centre rule, so it lags the real text by up to 8px at
  the extremes of an entry's passage and coincides with it
  (one line below, aligned) at the centre. The one-line offset
  is constant — the copy sits one line behind because the
  typist's carbon shifted by exactly the line being typed.
  Crossfade between entries' ghosts: 240ms `--ease-drift` as
  the centre rule changes hands. No other property animates.
- **States.** Absent (no entry at the rule — at the sheet's
  head and foot) / laid (under the active entry) / handing
  over (240ms crossfade) / printed-still (reduced-motion and
  fallback states: a static pale duplicate, no drift).
- **Content merge.** The ghost is the entry's own words, made
  of the entry itself; it cannot be pasted onto a section
  that is not an entry, and it never appears under headings,
  tables or the form — copies are made of log entries, not of
  furniture.
- **Failure fallback.** If the loop dies, the ghost freezes
  where it lies — a still carbon copy, which is physically
  what a carbon copy is. If the script never runs, there is
  no ghost and nothing is missing from the record: the
  original is complete without its copy.
- **Reduced-motion variant.** The ghost is printed as a static
  duplicate one line behind the active entry, laid once when
  the entry becomes active, with no parallax drift. (A build
  may also omit it entirely under reduced motion; the printed
  duplicate is the preferred variant because the copy is part
  of the world's texture, and stillness — not absence — is
  what reduced motion asks for.)
- **Performance budget & mobile variant.** One transform on
  one element per frame; the text is a single duplicated node,
  re-laid on entry change only; ≤0.1ms/frame. Mobile (<768px):
  the ghost is cut — a one-line offset under wrapped mobile
  lines reads as a rendering bug, and §14's cut order spends
  it first. The entry loses nothing but its copy.
- **Choreography timeline (v2).** Entry crosses into the
  centre band → ghost fades/laid in 240ms at one-line offset →
  scroll continues → ghost lags to −8px at the band's edge →
  next entry takes the rule → crossfade 240ms, ghost re-laid
  → sheet's foot → ghost fades out with the last entry.
- **State matrix (v2).** *Rest:* laid under the active entry.
  *Hover:* none. *Focus:* when focus enters an entry, that
  entry becomes the ghost's host immediately (the copy follows
  the reading, however the reading is done). *Active:* n/a.
  *Scrolled-past:* the ghost never lingers under a passed
  entry. *Disabled:* n/a. *Touch:* identical drift; no hover
  states involved.
- **Breakpoints (v2).** ≥1200px: full drift, 8px lag range.
  768–1199px: drift range 5px. <768px: cut (above).
- **Edge cases & failure modes (v2).** *Entry shorter than
  one screen:* the ghost still lays — a two-line entry gets a
  two-line copy. *Rapid scrolling:* the ghost's host changes
  are debounced by the loop to one re-lay per 240ms; it never
  strobes between entries. *Print:* the ghost is excluded from
  print styles — the archive prints originals.
- **Accessibility spec (v2).** `aria-hidden` and generated
  from the live DOM, so assistive technology meets each entry
  exactly once. Its colour (`--carbon-pale` at 14% over paper)
  is far below text contrast and is never the only carrier of
  anything — it is a texture with the entry's own words, all
  of which exist at full contrast one line above.
- **Tokens consumed (v2).** `--carbon-pale`, `--ease-drift`,
  `--parallax-ghost` (0.96), `--ghost-offset` (32px),
  `--dur-ghost-handover` (240ms).

### 6.6 The flight-plan route

- **What & why.** On the sign-off page (and in miniature at
  the home sheet's foot), an SVG route — launch → orbit →
  rendezvous → recovery — pencils itself across the sheet as
  the section centres, with a small cross stamped at each
  waypoint as the line reaches it. It belongs because the plan
  and the log are one document: the route the flight *was to
  take* is drawn on the same sheet as the entries recording
  the flight it *did* take, and the two agree — the route's
  waypoints are the record's own phases at the record's own
  times (§6.17).
- **Structure.** One inline SVG spanning the content column:
  a smooth path (the planned trajectory as a rising arc,
  descent, and recovery leg) drawn in `--carbon` at 2px, five
  waypoint crosses (launch, insertion, rendezvous, deorbit,
  splashdown) as small graphite × marks with mono labels
  beneath giving phase name and T+ from the record. The path's
  total length is measured at build; the draw is a dashoffset
  read from the shared loop. Waypoint crosses stamp in with a
  90ms `--ease-thump` micro-thud (scale 1.3 → 1) as the line
  reaches them. The shipped SVG is fully drawn; the script
  rewinds the dash only when arming.
- **Motion spec.** Trigger: the section's top crossing the
  centre rule. Draw duration ≈2,000ms scrubbed — not timed:
  the draw is *scrubbed to scroll* across the section's
  passage through the centre band, so the reader pencils the
  route at reading speed; scrolling back unpencils it (the
  plan, unlike the log, may be redrawn — it is a plan). If the
  reader stops mid-passage, the route stops mid-line, a pencil
  lifted. Waypoint crosses appear when the line reaches them
  and remain while the section is in the band.
- **States.** Undrawn (below the band) / drawing (in the
  band, scrubbed) / drawn (section centred; the state held
  while the sign-off content is read) / undrawing (scrolled
  past upward — reverses symmetrically).
- **Content merge.** Every waypoint label is a record fact
  (phase + T+), and the route's shape is the mission's shape:
  the long flat orbit leg carries the rendezvous cross at its
  true proportional position (T+12:08:31 of 76:18:00 ≈ 16%
  along the mission — placed on the arc at the record's
  fraction, not at a designer's thirds). The drawing *is* the
  flight plan; there is no decorative squiggle version.
- **Failure fallback.** Watchdog: if the loop dies mid-draw,
  the route snaps fully drawn with all crosses printed — the
  plan is content, and content completes. No-JS: fully drawn.
- **Reduced-motion variant.** The route is printed drawn,
  crosses in place. The sign-off page reads as the filed plan
  — which, in the archive, is exactly what it is.
- **Performance budget & mobile variant.** One dashoffset
  update per frame; ≤0.1ms/frame. Mobile: the SVG compresses
  vertically (arc height 60% of desktop), labels stack under
  their crosses at 11px, and the draw remains scrubbed — the
  plan survives the small sheet intact.
- **Choreography timeline (v2).** Section top enters the
  centre band → draw begins from the launch cross (already
  printed — the flight has a start before it has a route) →
  line scrubs with scroll: insertion cross at its fraction →
  rendezvous cross → deorbit → splashdown cross stamps as the
  line lands → section centred: route complete, sign-off
  entries below it begin their writes (§6.2).
- **State matrix (v2).** *Rest:* drawn while its section is
  centred. *Hover:* hovering a waypoint cross prints its
  entry's first line in a margin note beside the route (the
  plan citing the log). *Focus:* crosses are focusable links
  to their entries (§6.11's index behaviour); focus draws the
  route to that cross instantly if it is not yet drawn.
  *Active:* following a cross scrolls to the entry — the plan
  is an index. *Scrolled-past:* undrawn symmetrically.
  *Disabled:* n/a. *Touch:* no hover note; tap follows the
  link behaviour.
- **Breakpoints (v2).** ≥1200px: full arc, labels beside
  crosses. 768–1199px: arc height 80%, labels beneath.
  <768px: arc height 60%, labels beneath at 11px, the hover
  margin-note becomes a line under the route.
- **Edge cases & failure modes (v2).** *Reader jumps straight
  to the sign-off (anchor link):* the route draws over 600ms
  timed (not scrubbed) to its complete state — an arrival by
  reference still gets the whole plan. *A variant mission
  with more phases:* crosses are generated from the record's
  phase list; past seven phases the labels alternate above/
  below the line to hold legibility — the gate (§10) caps
  phases at seven for this element. *Print:* drawn, labelled,
  in carbon — the plan prints with the sheet.
- **Accessibility spec (v2).** The SVG is `role="img"` with an
  `aria-label` summarising the route in record words ("Flight
  plan: launch, orbit insertion at T+00:11:48, rendezvous at
  T+12:08:31, deorbit at T+75:44:00, splashdown at
  T+76:18:00"). The waypoint links are real links in a list
  beside the SVG in the DOM (visually the crosses), so the
  plan is navigable without sight of the drawing.
- **Tokens consumed (v2).** `--carbon`, `--graphite`,
  `--ease-pencil`, `--ease-thump`, `--dur-route-draw`
  (scroll-scrubbed, ≈2000ms across the band), `--loop-lerp`
  (0.11).

---

### 6.7 The stamp-thump click

- **What & why.** Clicking an entry card (§6.12) or an entry's
  sign-off line compresses it 2px with a thud ease and blooms
  a red imprint — the entry's status word from the record,
  `CONFIRMED` — across its corner at −4°, where it stays for
  the session. It belongs because it hands the reader the
  flight director's one physical power: to sign off what has
  been read. Interaction on this page is authorisation, and
  authorisation leaves a mark on the document itself.
- **Structure.** The imprint is a `.stamp` element inside the
  clicked card, absolutely positioned at its top-right corner,
  double-rule border in `--stamp`, the status word in Stamp
  type (§3). Its pre-state (armed by script only) is
  `scale(1.5)`, transparent, with a `--stamp-bloom` radial
  behind it. The card itself carries the compression transform.
  Stamped state is held in `sessionStorage` by entry number,
  so a reader who signs off № 003 and navigates to its detail
  page finds it signed there too.
- **Motion spec.** Trigger: click/activation. t=0 the card
  compresses 2px over 60ms; the imprint scales 1.5 → 1 and
  fades in over 120ms `--ease-thump`; the bloom flashes at
  16% opacity and settles by 400ms to the stamp's printed
  rest (full `--stamp`, no bloom — ink dries). A second click
  on a stamped card does nothing: you cannot stamp the same
  entry twice, and the card says so by not moving (§12's
  voice: the margin note `ALREADY SIGNED.` prints beside it).
- **States.** Unsigned (no imprint) / stamping (160ms) /
  signed (imprint at rest, permanent for the session) /
  signed-and-revisited (identical — the mark does not fade
  with time or scroll).
- **Content merge.** The imprint's word is the entry's own
  status from the record (§6.17) — every entry's status is
  `CONFIRMED` except № 009, whose stamp reads `REACQUIRED`
  (the signal came back; the stamp says what happened, not a
  generic OK). A card without a record status cannot be
  stamped and does not carry the interaction.
- **Failure fallback.** The stamp is an enhancement over a
  complete card; if the script is absent the card is simply
  read, and the record's statuses are printed in the flight-
  data table (§6.13) regardless — the information never
  depends on the reader clicking anything.
- **Reduced-motion variant.** The imprint appears printed —
  no compression, no bloom, no scale. Signing off is a state
  change, and the state still changes; only the thud is cut.
- **Performance budget & mobile variant.** One transform + one
  opacity per stamp event; no loop involvement; ≤0.1ms/frame.
  Mobile: identical, with the imprint at 13px and the corner
  inset increased so it never covers the card's title.
- **Choreography timeline (v2).** Click → t=0 compression
  begins (60ms) → t=40ms imprint strikes (120ms thump) →
  t=160ms compression recovered, bloom at peak → t=400ms
  bloom settled, stamp printed dry → session record written.
  Watchdog: 600ms — a stamp that has not landed by then is
  printed dry instantly.
- **State matrix (v2).** *Rest:* unsigned or signed as per
  session. *Hover:* the card rocks (§6.12) and the pencil
  underline (§6.8) offers the interaction; an unsigned card's
  corner shows a hairline stamp ghost at 12% — the outline of
  where the stamp *would* land (printed in `--ruling`, not
  red: the pad has not touched it yet). *Focus:* same ghost,
  plus the standard focus outline (§6.12). *Active:* the
  thump. *Scrolled-past:* state persists. *Disabled:* an
  entry whose record status is absent renders its card
  without the ghost and without the interaction. *Touch:* tap
  = click, identical; no hover ghost — the ghost prints on
  first tap and the stamp lands on the second only if the
  card is not itself a link (cards that navigate never
  stamp-block their first tap).
- **Breakpoints (v2).** ≥1200px: imprint 17px at the corner,
  −4°. 768–1199px: 15px. <768px: 13px, −3°, inset 10px from
  the corner so it clears the stacked margin block.
- **Edge cases & failure modes (v2).** *Session storage
  unavailable (private mode):* stamps still land and persist
  for the page view; cross-page persistence is lost, and the
  footer (§6.16) omits its signed-count line rather than
  printing a wrong one. *Rapid double-click:* the second
  activation lands inside the 160ms window and is absorbed —
  one stamp, one thud. *A card stamped, then the record
  corrected in a CMS:* stamps are session furniture; the
  printed record (table, entry) always outranks the reader's
  session marks.
- **Accessibility spec (v2).** The stamp action is a real
  `<button>` wrapping the card's sign-off affordance with an
  accessible name ("Sign off entry number 3, orbit
  insertion"); the imprint itself is `aria-hidden` decoration
  whose meaning — the status word — is printed in the card's
  text and announced via a polite live region once
  (`Entry 3 signed: CONFIRMED`). The hairline ghost is
  decorative. Focus outline: 2px `--carbon` at 2px offset —
  never `--stamp` (the census, §2).
- **Tokens consumed (v2).** `--stamp`, `--stamp-bloom`,
  `--ruling`, `--carbon`, `--ease-thump`, `--stamp-angle`
  (−4deg), `--dur-thump` (120ms), `--dur-bloom-settle`
  (400ms).

### 6.8 The pencil-underline hover

- **What & why.** Hovering or focusing a link sketches a
  graphite underline beneath it: a slightly wobbling hand line
  that strokes in over 250ms, darker at the start, feathered
  at the end. It belongs because annotation is the ledger's
  native gesture — the director underlined what mattered, in
  pencil, on the record. Attention on this page leaves a
  pencil mark, and the mark is honest about being a hand's
  work: no two underlines are perfectly straight.
- **Structure.** An inline SVG under each link (or a
  background SVG data-URI per link class), a path with three
  hand-plotted points giving ≤1px of wobble, stroke
  `--graphite`, width tapering 2px → 1px via two overlapping
  path segments. The draw is a dashoffset transition. Links in
  entries, the index (§6.11), the table (§6.13) and the footer
  (§6.16) all carry it; stamp buttons and the form's submit
  do not (they thump, §6.7 — a control is either annotated or
  authorised, never both).
- **Motion spec.** Trigger: hover or `:focus-visible`. Stroke
  draws left→right over 250ms `--ease-pencil`. On leave, the
  line does not un-draw; it lightens to 35% graphite over
  200ms and stays as a faint trace until the pointer next
  rests elsewhere — a page the reader has been through carries
  faint pencil under what they considered, which is what a
  worked-in ledger looks like. Focus keeps the line at full
  strength while focus holds.
- **States.** Unmarked / drawing / marked (hover/focus) /
  traced (visited-by-pointer, 35%) / current-page link in the
  index (permanently marked at 60% — the reader is *here*).
- **Content merge.** The underline sits under the link's own
  words on the entry's own line; it is sized to the text, not
  to a container. It never appears under headings or body text
  that is not a link — pencil is for references, and a page
  underlined everywhere is underlined nowhere (§9).
- **Failure fallback.** CSS-only: if the SVG path fails, the
  fallback is a plain `text-decoration: underline` in graphite
  — specified in the same rule, so a degraded underline is
  still an underline. No JS is involved at any point.
- **Reduced-motion variant.** The underline is simply present
  on hover/focus at full strength, no draw, no trace
  transition. The gesture is a state, and the state remains.
- **Performance budget & mobile variant.** Pure CSS/SVG, zero
  loop cost. Mobile/touch: no hover — links show a permanent
  35% trace underline so touch readers can still tell a link
  from the record's text (on paper, a reference must be
  findable without a pencil in hand).
- **Choreography timeline (v2).** Pointer enters → t=0 stroke
  begins → t=250ms line complete, feathered end settled →
  pointer leaves → t=+200ms line at 35% trace → next hover
  elsewhere: this trace persists; the new line draws.
- **State matrix (v2).** *Rest:* unmarked (or traced, if
  visited). *Hover:* drawing → marked. *Focus:* marked at
  full strength + the element's focus outline where the
  element is a control. *Active:* line at full strength,
  1px downward shift with the press. *Scrolled-past:* traces
  persist — the sheet remembers being read. *Disabled:* a
  disabled link takes no underline and prints in
  `--graphite-soft`. *Touch:* permanent 35% trace (above).
- **Breakpoints (v2).** All sizes identical in behaviour; at
  <768px the wobble amplitude halves (0.5px) so small text
  stays crisp, and the trace strength rises to 45% for
  legibility on small screens.
- **Edge cases & failure modes (v2).** *Multi-line links
  (index entries that wrap):* the underline draws under the
  last line only — a hand underlines the end of a reference.
  *Very long link text (>40 chars):* the draw duration scales
  at 6ms/char past 250ms so the hand keeps a constant speed.
  *Forced-colours mode:* the SVG is replaced by the system's
  underline; the trace states collapse to marked/unmarked.
- **Accessibility spec (v2).** Links are never identified by
  the underline alone in body text: entry links also carry
  carbon colour (§2) — colour + line, two signals. The
  underline is decorative SVG (`aria-hidden`). Focus-visible
  always pairs the underline with the theme's focus outline on
  controls, so keyboard users get a stronger signal than
  mouse users, not a weaker one.
- **Tokens consumed (v2).** `--graphite`, `--graphite-soft`,
  `--carbon`, `--ease-pencil`, `--dur-underline` (250ms),
  `--trace-strength` (35%).

### 6.9 Taped-corner photos

- **What & why.** The mission's photographs sit in frames with
  translucent tape strips at two corners, scale 1.05 → 1.0 as
  they enter, the tape's sheen shifting with scroll parallax.
  They belong because evidence in a log is *taped in*: the
  photo is an exhibit, attached to the entry it proves, on the
  same sheet, under the same ruling. There are exactly three
  exhibits (§6.17): A at № 001 (liftoff), B at № 005
  (rendezvous), C at № 012 (splashdown) — the beginning, the
  middle and the end, each taped beside its own entry.
- **Structure.** A `<figure>` inside the entry's body column:
  the photograph (real `<img>`, documentary, monochrome-leaning
  — period photography, not a stock render), a graphite 1px
  frame rule, two tape strips (rotated rectangles in `--tape`
  with a lighter sheen band) across the top-left and
  bottom-right corners, and a caption in Margin type beneath:
  `EXHIBIT B — RENDEZVOUS, T+12:08:31` with the photographer's
  station initialled. The figure sits *on* the ruling — its
  height is a whole number of ruled lines (multiples of 32px)
  so the sheet's grid is never broken by its own exhibits.
- **Motion spec.** Trigger: the figure crossing the centre
  rule with its entry (§6.2). Scale 1.05 → 1.0 over 700ms
  `--ease-drift`, read from the loop across the figure's
  passage through the centre band — the photo settles onto the
  sheet as it is read. The tape sheen (a lighter band across
  each strip) translates at 0.94× parallax against the figure,
  ≤6px of travel — the one place the sheet's surface catches
  light differently from its paper. No zoom on hover, no
  lightbox: an exhibit is examined by reading its caption and
  its entry, not by enlarging it off the sheet.
- **States.** Approaching (scale >1, in the band) / taped
  (rest, scale 1.0) / scrolled-past (taped; sheen at its
  resting offset).
- **Content merge.** The exhibit's caption cites its entry's
  T+ and the entry's text cites the exhibit (`…at 120 feet.
  (Exhibit B.)`) — the two refer to each other in the record's
  own words. A photo without an entry, or an entry claiming a
  photo that is not taped beside it, is a §10 failure.
- **Failure fallback.** The figure ships at scale 1.0, taped,
  captioned; the script only ever *starts* it at 1.05 when
  arming. A failed image load prints the caption and an empty
  frame with the margin note `EXHIBIT B — PRINT NOT RECEIVED.`
  (§12's voice): a missing exhibit is recorded as missing,
  never hidden.
- **Reduced-motion variant.** The photo is taped at scale
  1.0, sheen static. Exhibits in the archive do not settle;
  they are already where they were put.
- **Performance budget & mobile variant.** One transform on
  one figure per frame while in the band; ≤0.1ms/frame.
  Images ≤140KB each, WebP with a monochrome JPEG fallback,
  lazy below the fold. Mobile: the figure takes the full
  content column, tape strips shrink to 54px, the scale range
  narrows to 1.03 → 1.0 and the sheen is cut (§14's order).
- **Choreography timeline (v2).** Figure enters the centre
  band → scale begins 1.05 → sheen starts its 6px traverse →
  figure centred: scale 1.0, sheen mid-travel → figure leaves
  the band upward: scale holds 1.0 (an exhibit does not
  un-tape), sheen completes → rest.
- **State matrix (v2).** *Rest:* taped at 1.0. *Hover:* the
  caption's exhibit line takes the pencil underline (§6.8) if
  it links to the full record; the photo itself does not
  respond. *Focus:* as hover, on the caption link only.
  *Active:* n/a. *Scrolled-past:* taped. *Disabled (image
  failed):* the `PRINT NOT RECEIVED` state above. *Touch:*
  identical scrub; no hover behaviour.
- **Breakpoints (v2).** ≥1200px: figure spans 7 of the content
  column's 9 columns, offset one column right — taped *into*
  the text, not centred like a hero image. 768–1199px: full
  content width. <768px: full width, tape 54px, scale range
  narrowed.
- **Edge cases & failure modes (v2).** *A variant entry with
  two exhibits:* forbidden by the record — one exhibit per
  entry, three per log; §10 counts figures on the home sheet.
  *Portrait-orientation photo:* the frame's height rounds
  *up* to the next multiple of 32px and the photo crops to
  the frame (the tape holds the print, the print was trimmed
  to the sheet). *Slow network:* the frame, tape and caption
  print at first paint; the photo fills its frame when it
  arrives — the exhibit's place in the log never waits for
  its print.
- **Accessibility spec (v2).** Real `alt` written as an
  archivist would: "Kestrel IV at station-keeping distance
  from the target vehicle, photographed from the cabin
  window, T+12:08:31." The tape and sheen are `aria-hidden`.
  Caption contrast: `--graphite-soft` on paper 4.9:1 at
  12.5px — permitted for captions only (§2), and the caption
  duplicates the entry's own reference, so nothing rests on
  it alone.
- **Tokens consumed (v2).** `--tape`, `--graphite`,
  `--graphite-soft`, `--ease-drift`, `--parallax-sheen`
  (0.94), `--dur-exhibit-settle` (700ms), `--line-unit`
  (32px).

---

### 6.10 The ink-filling progress rule

- **What & why.** The current entry's ruled line fills with
  ink from left to right, scrubbed to that entry's own read
  progress, and at each quarter of the entry a small timestamp
  prints beneath the line — the entry's T+ at that quarter of
  the *mission*, computed from the record. It belongs because
  progress in a ledger is a line being written: the reader
  watches the record of their own reading being made, in ink,
  on the very line the entry stands on.
- **Structure.** The entry title's ruled line is a 2px track
  in `--ruling` with an ink layer above it in `--graphite`,
  width driven by the loop. Quarter timestamps are small mono
  nodes under the line at 25/50/75/100% positions, printed
  (opacity via the ink reaching them — they are revealed by
  the ink's arrival, not by a fade of their own). For the home
  sheet, the quarters are the mission's quarters (§6.17):
  `T+19:04:30`, `T+38:09:00`, `T+57:13:30`, `T+76:18:00` — the
  sheet-level rule at the foot of the log carries those; each
  entry's own rule carries its entry's span quarters.
- **Motion spec.** Pure scrub from the shared loop: ink width
  = the entry's passage through the centre band, lerped at
  0.11. The ink's leading edge has a 3px wet taper (a gradient
  from graphite to transparent — ink soaking into the rule).
  When the ink crosses a quarter point, that quarter's
  timestamp prints with a 60ms digit-flip (§6.3's clock
  behaviour, miniature). Scrolling back drains the ink
  symmetrically — this rule, alone among the page's marks,
  is allowed to retreat, because it records *reading*, and
  reading can go back; the entries themselves never unwrite
  (§6.2), and the ruler's furthest-marker never retreats
  (§6.3). Three instruments, three honesties.
- **States.** Empty (entry below the band) / filling /
  full (entry read; the line stays inked while the entry is
  the current one, then hands over to the next entry's rule) /
  handed-over (previous rules return to `--ruling` — the ink
  was the *current* line's; a sheet with every line inked
  would say nothing).
- **Content merge.** The line is the entry's own title rule —
  the furniture of §4's anatomy, given a job. The quarter
  timestamps are record figures, not percentages: the reader
  is never told "50%"; they are told the mission time their
  reading has reached.
- **Failure fallback.** Loop dead: the current entry's line
  prints fully inked with all four quarter timestamps — a
  completed line, still true. No-JS: title rules are plain
  `--ruling` lines and the quarter timestamps do not exist;
  the entries' margin timestamps carry the same information
  in their static form.
- **Reduced-motion variant.** No scrub. The current entry's
  line is inked in full when the entry becomes current, and
  its quarter timestamps print with it. Progress is stated,
  not performed.
- **Performance budget & mobile variant.** One width update
  per frame on one element; ≤0.05ms/frame. Mobile: the rule
  and its timestamps are unchanged (the line is the column's
  full width at every size); timestamp size drops to 11px and
  the 25/75% labels are cut at <380px, keeping 50% and 100% —
  a narrow sheet keeps its halves and its end.
- **Choreography timeline (v2).** Entry takes the centre rule
  → its title rule becomes the ink line → ink advances with
  scroll, wet edge leading → quarter crossings print their
  timestamps (60ms flips) → entry yields the rule → ink
  completes to 100% and the final timestamp prints → next
  entry's rule takes over; this rule returns to `--ruling`
  over 300ms `--ease-drift`.
- **State matrix (v2).** *Rest:* the current entry's line
  inked to its read fraction. *Hover:* hovering the line
  prints the exact T+ at the hovered fraction in the margin
  (graphite-soft preview, as §6.3's ruler). *Focus:* not
  focusable. *Active:* n/a. *Scrolled-past:* handed-over
  state. *Disabled:* n/a. *Touch:* no hover preview; scrub
  identical.
- **Breakpoints (v2).** ≥1200px and 768–1199px: full four
  quarter timestamps. <768px: four, dropping to two under
  380px (above).
- **Edge cases & failure modes (v2).** *Very short entry
  (one line):* the rule still fills across the entry's
  passage; its quarters are close together in time and the
  timestamps may collide — at spans under 90 seconds of MET
  the 25/75% labels are suppressed by the build rule, halves
  and end kept. *Reader parks mid-entry:* the ink parks too;
  the wet edge dries (taper fades over 2s) — a small truth:
  ink left alone dries. *Jump-scroll:* the ink snaps to the
  true fraction; quarter timestamps for crossed quarters
  print instantly.
- **Accessibility spec (v2).** The rule is `aria-hidden`; its
  content — mission time reached — is the same figure the
  margin ruler's readout and the entries' own timestamps
  carry in text. Nothing is communicated by ink alone.
- **Tokens consumed (v2).** `--graphite`, `--ruling`,
  `--graphite-soft`, `--ease-drift`, `--loop-lerp` (0.11),
  `--dur-digit` (60ms), `--ink-taper` (3px).

### 6.11 Ledger masthead, entry index & the pinned flight strip

- **What & why.** The sheet's head carries the ledger's title
  block — `FLIGHT OPERATIONS — FLIGHT LOG` in label type, the
  mission name, and the entry index: the twelve entries listed
  by number, T+ and title, each a link to its entry. Below it,
  clipped to the sheet's top edge as the reader scrolls, rides
  the flight strip: a narrow band naming the current phase
  (`PHASE — RENDEZVOUS`), the current entry number, and the
  MET readout — the strip a flight director clips to the board
  so the room always knows where the flight is. It belongs
  because navigation in a ledger is an *index and a strip*,
  not a menu: you find an entry by its number, and you know
  where you are by the strip.
- **Structure.** The masthead is the sheet's first entry-like
  block: title block, then the index as a ruled table of
  contents (number / T+ / title / initials columns, §6.13's
  table grammar in miniature). The strip is a separate element
  that becomes `position: sticky` at the sheet's top once the
  masthead scrolls away: a 40px band on `--paper-deep` with a
  graphite bottom rule, phase in Entry-head type at 15px, MET
  in mono at right, and — below 1200px — the margin ruler's
  track set into its bottom edge (§6.3). Index links carry the
  pencil underline (§6.8); the current entry's index row is
  marked at 60% underline strength and a carbon entry number.
- **Motion spec.** The strip does not animate in; it is
  *clipped on* — when the masthead's bottom passes the
  viewport top, the strip is simply there (a 120ms
  `--ease-feed` settle of 4px, the clip seating). Phase
  changes print with a 60ms digit-flip on the MET and a
  180ms crossfade of the phase name — the strip is re-clipped,
  not scrolled. Index rows print with the masthead's own write
  (§6.2's sequence applied to the sheet's head). No other
  motion: the strip is the calmest element on the page.
- **States.** Masthead state (strip absent, index visible) /
  stripped (index gone, strip riding) / at the foot (strip
  prints `LOG CLOSED — T+76:18:00` and stops changing) /
  current-row marking in the index follows the centre rule.
- **Content merge.** The index is the record's entry list —
  numbers, times and titles from §6.17, in order; the strip's
  phase is the current entry's record phase. Neither contains
  a word that is not in the record. A nav item like "About"
  or "Contact" does not exist on the sheet; §7's pages are
  reached as the archive's other volumes (the footer's
  sign-off block, §6.16, carries those links as a clerk's
  references, in the margin voice).
- **Failure fallback.** No-JS: the masthead and index print
  complete; the strip is a static band under the masthead
  naming the flight and its total MET (it never rides, and
  the page loses an instrument, not its contents). Loop dead:
  the strip rides but its phase freezes at the last computed
  entry — the entries' own margin blocks still tell the truth
  line by line.
- **Reduced-motion variant.** The strip clips on instantly
  (no settle), phase names swap without crossfade, MET prints
  without digit flips.
- **Performance budget & mobile variant.** Sticky positioning
  is compositor work; phase updates are one text change per
  entry crossing; ≤0.05ms/frame. Mobile: the index becomes a
  single column (number + title, T+ folded into the title
  line), and the strip holds phase + MET on one line at 13px
  — the strip never wraps to two lines; if a phase name is
  long, the MET readout is what yields (it lives in every
  margin anyway).
- **Choreography timeline (v2).** Load → masthead writes
  (index rows in §6.2 stagger) → reader scrolls → masthead
  bottom exits → strip clips on (120ms settle) → each entry
  crossing updates phase + MET (60ms flip) → footer's sign-off
  reached → strip prints `LOG CLOSED` and freezes → scroll
  back to top → strip unclips at the masthead, index's current
  row returns to № 001.
- **State matrix (v2).** *Rest:* strip showing current phase.
  *Hover:* index rows take the pencil underline (§6.8); the
  strip itself has no hover. *Focus:* index links show
  underline + outline; the strip is not focusable. *Active:*
  an index link scrolls to its entry (native anchor; the
  entry writes instantly on arrival per §6.2's jump rule).
  *Scrolled-past:* n/a — the strip is the scrolled state.
  *Disabled:* an index row for an entry not on this page
  (detail pages index the whole log) links to the home sheet's
  anchor — never disabled, never dead. *Touch:* identical;
  tap targets in the index ≥44px tall (rows are 32px lines —
  the touch target extends 6px above and below the row into
  the blank ruled lines, which are the sheet's own space).
- **Breakpoints (v2).** ≥1200px: four-column index, strip
  with separate ruler in the margin. 768–1199px: three-column
  index (initials folded into the title), ruler track in the
  strip. <768px: one-column index, strip at 13px, MET yields
  before phase does.
- **Edge cases & failure modes (v2).** *A log with more
  entries than twelve (a variant mission):* the index
  paginates as the archive does — `INDEX CONTINUED` at a ruled
  break, never a scrollable box on the sheet. *Sticky
  unsupported (very old browser):* the strip degrades to the
  static band of the no-JS state, positioned under the
  masthead. *The reader's font scaling at 200%:* the strip
  grows to two lines rather than truncating the phase name —
  legibility outranks the one-line rule at accessibility
  sizes, and §10 checks it at 200%.
- **Accessibility spec (v2).** The index is a `<nav>` with an
  ordered list — entry order is mission order, and screen
  readers get the chronology as a list, which it is. The strip
  is `aria-hidden` (its phase and MET duplicate the current
  entry's own heading and margin). Current index row carries
  `aria-current="true"`. Focus outlines: 2px `--carbon`,
  never red.
- **Tokens consumed (v2).** `--paper`, `--paper-deep`,
  `--graphite`, `--graphite-soft`, `--carbon`, `--ruling`,
  `--ease-feed`, `--dur-digit` (60ms), `--strip-height`
  (40px).

### 6.12 Station cards

- **What & why.** Where the log must be browsed rather than
  read — the archive's listing pages, the home sheet's
  "stations" summary — entries condense into cards: ruled
  blocks carrying entry number, phase, T+, the entry's first
  line, and its status. Hovering rocks a card like a stamp pad
  being picked up (max 3°); clicking stamps it (§6.7). They
  belong because a card in this theme is not a UI tile — it is
  the entry's *flight strip*, the small card the room actually
  handled, and it behaves like card stock: it rocks, it takes
  a stamp, it does not float or glow.
- **Structure.** An `<article>` on the sheet (no background —
  the card is a heavier ruling: a graphite 1px border with a
  double rule at its head), containing the margin block
  condensed to one line (`№ 005 · T+12:08:31 · MR`), the title
  in Entry-head type, the first line of the entry text, and
  the status word printed small in the foot. Cards sit in a
  single column on the sheet (the ledger has one column);
  on listing pages they run in the index's order. The tilt is
  a transform driven by pointer position over the card,
  computed in the shared loop from lerped pointer values.
- **Motion spec.** Tilt: rotateX/rotateY toward the pointer,
  max 3°, lerped at the loop's 0.11 so the card feels like
  stock rocking on the sheet, not a screen effect; on leave
  it settles flat over 500ms `--ease-drift` with a 0.2°
  overshoot — card stock rocks once before it rests. The
  card's head rule draws in (§6.2's pencil draw, 300ms) when
  the card first enters. Click: §6.7's stamp-thump. Nothing
  else moves; a card at rest is printed paper.
- **States.** Flat (rest) / rocking (hover) / settling /
  stamped (§6.7's imprint at its corner) / current (the card
  of the entry at the centre rule: its number in carbon).
- **Content merge.** Every field on the card is a record
  field — number, phase, T+, first line, status — and the
  first line is the entry's actual first line, so the listing
  reads as the log in miniature and the counts reconcile: the
  archive page's twelve cards are the twelve entries, no
  more, and §10 counts them.
- **Failure fallback.** Cards ship flat and complete; tilt
  and stamps are script-armed. No-JS: a ruled list of entry
  summaries with working links — the archive's card catalogue
  in its paper form.
- **Reduced-motion variant.** No tilt, no settle; hover
  prints the pencil underline on the card's title link
  (§6.8) and nothing else. The stamp still lands printed
  (§6.7's variant).
- **Performance budget & mobile variant.** Tilt math is two
  lerped values on the one hovered card; ≤0.1ms/frame.
  Mobile: tilt is cut (no pointer); tap on the card's title
  navigates; the stamp action lives on the card's explicit
  sign-off button (§6.7's touch rule), ≥44px.
- **Choreography timeline (v2).** Card enters → head rule
  draws 300ms → rest → pointer enters → rock lerps to ≤3°
  tracking the pointer → pointer leaves → settle 500ms with
  0.2° overshoot → flat → click (any time) → §6.7's thump
  sequence on this card.
- **State matrix (v2).** *Rest:* flat, printed. *Hover:*
  rock ≤3°. *Focus:* the card's link focus prints the
  underline (§6.8) and a 2px carbon outline on the card;
  tilt does not follow focus. *Active:* §6.7 compression.
  *Scrolled-past:* flat. *Disabled:* a card whose entry is
  not yet published (archive variants) prints with its status
  `NOT YET LOGGED` in graphite-soft, no link, no stamp —
  the catalogue admits the gap. *Touch:* no rock; tap =
  navigate or stamp per target.
- **Breakpoints (v2).** ≥1200px: cards at the content column's
  width, in one column, tilt 3°. 768–1199px: tilt 2°.
  <768px: tilt off, card padding tightens to one ruled line
  (32px) of air above and below the text block.
- **Edge cases & failure modes (v2).** *Long first lines:*
  the card prints the entry's first *sentence*, truncated
  only at a sentence boundary with the record's own
  continuation mark `— cont. at № 005` — never an ellipsis
  mid-word. *Many cards (a 40-entry variant log):* listing
  pages paginate (§11), the home sheet never carries cards
  for all entries — its summary strip shows the current
  phase's cards only, ≤4. *Pointer leaves mid-settle then
  re-enters:* the rock retargets from the current angle; no
  snap.
- **Accessibility spec (v2).** The whole card is not a link;
  the title is the link, with an accessible name carrying
  number and phase ("Entry 5, rendezvous"). Tilt is
  `aria-hidden` behaviour on a non-interactive wrapper.
  Contrast: all card text is graphite on paper (9.5:1);
  the carbon current-number is 7.6:1.
- **Tokens consumed (v2).** `--graphite`, `--graphite-soft`,
  `--carbon`, `--ruling`, `--ease-drift`, `--ease-pencil`,
  `--tilt-max` (3deg), `--loop-lerp` (0.11).

---

### 6.13 The flight-data table

- **What & why.** On the sign-off page the log summarises
  itself as a ruled table: one row per entry — number, T+,
  GMT, phase, the entry's key figure, status — with a totals
  row at the foot carrying the record's totals (76:18:00,
  49 orbits, 1,107,400 nautical miles). It belongs because a
  log that cannot be totalled is a diary; the table is where
  the sheet proves its arithmetic, and it is the hurried
  reader's page: the whole flight, checkable, on one screen
  of ruling.
- **Structure.** A semantic `<table>` on the sheet: caption
  `FLIGHT DATA — KESTREL IV, FROM THE LOG (§6.17)`, column
  headers in Label type, figures in Data type (tabular mono),
  row rules in `--ruling`, the totals row set off by a
  graphite double rule with its figures in graphite at Data
  size. Rows are the record's entries in order; the key-figure
  column carries each entry's declared figure (insertion
  velocity, cabin pressure, burn ΔV, signal loss, splashdown
  offset — §6.17's table). No sorting, no zebra striping: the
  ruling is the rhythm, and a log is read in order.
- **Motion spec.** The table does not perform. It prints with
  its section's write (§6.2's line sequence applied to rows at
  24ms stagger — the clerk ruling off the summary). Row hover:
  the pencil underline (§6.8) draws under the row's entry
  number, and the margin ruler (§6.3) previews that row's T+
  — the table and the ruler are two readings of one record,
  and hovering is how the reader cross-checks them. That is
  all the motion this element is allowed.
- **States.** Printed (rest) / row-hovered (underline +
  ruler preview) / totals-verified (a static state: the
  totals row is printed from the record's derived totals at
  build, and §10's audit re-adds the columns — the table
  never computes at runtime).
- **Content merge.** The table *is* §6.17 in tabular form:
  same entries, same figures, same order. Its totals are the
  hero's total MET, the ruler's full scale and the footer's
  closing figures — four printings of one arithmetic, and the
  gate checks them digit-for-digit.
- **Failure fallback.** None needed and none permitted to be
  needed: the table is static HTML that cannot fail into
  invisibility. No-JS: identical, minus the ruler preview.
- **Reduced-motion variant.** Identical, minus the row
  stagger (rows print with the section) and the hover draw
  (underline present instantly).
- **Performance budget & mobile variant.** Zero loop cost.
  Mobile (<768px): the table becomes a stacked summary list —
  each entry a block: number + T+ on the margin line, figure
  and status beneath — same order, same totals block at the
  foot. Horizontal scrolling a table on a narrow sheet is
  forbidden; a summary you must pan is a summary lost.
- **Choreography timeline (v2).** Section write begins →
  caption and header print → rows stagger at 24ms → totals
  row prints last, after its double rule draws (300ms
  `--ease-pencil`) → rest. Hover at any later time: underline
  250ms + ruler preview.
- **State matrix (v2).** *Rest:* printed. *Hover:* per-row,
  above. *Focus:* a row's entry-number link focuses like any
  link (§6.8 + outline). *Active:* following the link goes to
  the entry. *Scrolled-past:* printed. *Disabled:* a figure
  the record marks provisional prints in graphite-soft with
  the word `PROVISIONAL` in its cell — the table admits the
  state of its evidence rather than dropping the row (the
  Kestrel IV record has none; the rule exists for variant
  logs). *Touch:* tap on a row holds the underline for 600ms;
  the ruler preview is cut (the ruler is under the strip,
  §6.3, and still shows the row's T+ when scrolled to).
- **Breakpoints (v2).** ≥1200px: six columns. 768–1199px:
  five (GMT folds under T+ in the same cell). <768px: the
  stacked list (above).
- **Edge cases & failure modes (v2).** *A figure with a unit
  that wraps:* figure cells are `white-space: nowrap` and the
  key-figure column is sized to the record's longest figure
  at build — the build knows its data. *Totals that do not
  reconcile in a variant record:* the build fails (§10 check
  1), the page does not ship with a totals row that disagrees
  with its rows — there is no runtime state for "the table is
  wrong". *Print:* the table is the print stylesheet's
  centrepiece after the entries themselves.
- **Accessibility spec (v2).** Real table semantics: caption,
  `scope="col"` headers, entry numbers as `scope="row"`. The
  totals row is a `<tfoot>`. Contrast: graphite on paper
  9.5:1 throughout; the provisional state's graphite-soft is
  4.9:1 and is always paired with the printed word
  PROVISIONAL, never colour alone.
- **Tokens consumed (v2).** `--graphite`, `--graphite-soft`,
  `--ruling`, `--ease-pencil`, `--dur-underline` (250ms),
  `--stagger-row` (24ms).

### 6.14 The request-the-file form & its stamped confirmation

- **What & why.** The archive's one conversion: a visitor who
  wants the mission's file — the full log, the exhibits, the
  data table — files a request, and the request is *entered
  in the log* as its next numbered item. The form is styled as
  the log's next entry: ruled lines for fields, the request
  numbered before it is written (`REQUEST № 088` — the record
  holds 87 requests on file, §6.17, and the number is printed
  in the form's margin before the visitor types a word, so the
  confirmation is a kept promise). On submit, the confirmation
  is the entry itself, stamped FILED in red at −4°. It belongs
  because it is the only element where the visitor writes in
  the ledger — and the ledger treats their line with the same
  discipline as the flight's: numbered, timestamped, stamped,
  and never lost.
- **Structure.** A real `<form>` laid out as an entry: margin
  block (`№ 088`, the visitor's T+ — the elapsed time of their
  visit, read from §6.3's clock, printed as `VISITOR T+` — and
  the initials field they will fill), then ruled-line fields:
  name, email, and "what the file is for" (a select in the
  archive's vocabulary: `RESEARCH / TEACHING / PRESS /
  PERSONAL`). Fields are bottom-ruled lines (the ruling in
  graphite at rest), labels above in Label type — on a form
  you write *on the line*, and the label is the clerk's
  printed prompt. Submit is a stamp button: a bordered
  `FILE THIS REQUEST` that thumps (§6.7's ease) when pressed.
- **Motion spec.** Field focus: the field's rule darkens from
  `--ruling` to graphite over 200ms and the carbon ghost of
  the *form entry* lays beneath (§6.5's behaviour, hosted by
  the form while it holds focus — the copy of the request is
  being made as it is written). Typing in a field prints in
  mono at the field's line. Submit: the button thumps (120ms),
  the form's lines hold for the request's round trip under a
  3,000ms watchdog with the skeleton caret (§6.15) blinking at
  the entry's end — never a spinner. Success: the form block
  is replaced by the completed entry — the visitor's details
  summarised in log voice, `FILED.` in the margin, and the
  FILED stamp lands at −4° (160ms, §6.7's choreography).
  Error: the offending field's prompt gains the carbon
  correction treatment (§6.4's language at form scale): the
  wrong value is struck in pencil and the reason prints above
  the line in carbon — the form corrects itself the way the
  log does. No shake, no red, ever.
- **States.** Open (numbered, awaiting) / writing (ghost laid,
  rules darkening per field) / filing (caret blinking,
  fields disabled) / filed (the completed entry + stamp,
  permanent for the session; the record's request count is
  now 88 and any second form on the page would open as
  № 089) / error (per-field correction state, values
  preserved) / archive-closed (endpoint down: the margin
  prints `THE ARCHIVE IS CLOSED TONIGHT. YOUR REQUEST IS
  KEPT BELOW.` and the values stay in the fields, unsubmitted
  and unlost).
- **Content merge.** The form's number derives from the
  record's request count; its margin clock is the page's own
  mission clock; its confirmation is an entry in the same
  anatomy as № 001–012; its stamp is the pad's third word
  (LOGGED, CONFIRMED, FILED — §2's census). The conversion is
  not decorated with the theme; it is *transacted inside* it.
- **Failure fallback.** Watchdog at 3,000ms: no response →
  the archive-closed state above, values intact, no silent
  loss and no double-submit (the request carries its number
  as an idempotency key — № 088 can only ever be filed once).
  No-JS: the form posts natively and the confirmation is a
  server-rendered page in the same entry anatomy with the
  same number and stamp, printed static.
- **Reduced-motion variant.** Confirmation prints instantly
  with the stamp already on it; the ghost does not lay; errors
  print without the strike drawing (the strike is present,
  drawn). The number, the entry and the kept-words failure
  state are unchanged — they are content, not motion.
- **Performance budget & mobile variant.** The form's script
  is the page's only non-loop script: ≤5KB gz, deferred.
  Mobile: single column, fields full width, the margin block
  stacks above (number + visitor T+ on one line), the stamp
  button is full-width at the form's foot, ≥48px tall.
- **Choreography timeline (v2).** Form enters the centre band
  → its entry writes (§6.2) with № 088 already in its margin →
  first field focus: rule darkens 200ms, ghost lays 240ms →
  submit: button thumps 120ms → filing state, caret blinking
  → response → completed entry writes its summary lines
  (30ms stagger) → FILED stamp lands at +160ms → entry at
  rest; the footer's request count (§6.16) now reads 88.
  Watchdog ceiling 3,000ms throughout the filing state.
- **State matrix (v2).** *Rest:* open and numbered. *Hover:*
  fields' rules lift to graphite-soft; the stamp button
  rocks 1° (§6.12's gesture, miniature). *Focus:* rule
  graphite, ghost laid, 2px carbon outline on the field's
  line box. *Active:* filing state. *Scrolled-past:* the form
  waits; an in-flight filing completes regardless of scroll.
  *Disabled:* archive-closed state (above). *Touch:* targets
  ≥48px; the ghost does not lay on touch (no hover-focus
  distinction worth copying for).
- **Breakpoints (v2).** ≥1200px: form at the content column's
  width with its margin block. 768–1199px: margin narrows
  with the sheet (§4). <768px: margin stacks, fields full
  width, select becomes a ruled list of radio lines (a native
  select on a narrow sheet breaks the ruling; the radio lines
  keep it — each option its own ruled line, marked in pencil
  graphite when chosen).
- **Edge cases & failure modes (v2).** *Duplicate request
  (same email, same purpose):* the confirmation entry prints
  with the margin note `SECOND REQUEST — NOTED AS
  CORROBORATION.` and keeps № 088's filing (the number is not
  spent twice). *Absurd input (a name of 200 characters):*
  fields hold what fits the line and the error correction
  reads `THE LINE HOLDS FORTY CHARACTERS. SHORTEN IT.` — the
  log's voice, stating the physical fact of the sheet.
  *Visitor T+ at filing:* read once at submit from §6.3's
  clock and printed in the confirmation — a visitor who read
  for nine minutes files at `VISITOR T+09:00` and the entry
  says so.
- **Accessibility spec (v2).** Native labels, visible, tied to
  fields; errors use `aria-describedby` with the carbon
  correction text, and an `aria-live="polite"` summary reads
  the log's own sentence (`Request 88 filed.`). Focus moves
  to the first error field on error, to the confirmation
  heading on success. The FILED stamp is `aria-hidden`; its
  word is in the entry text. Required fields are marked with
  the printed word `REQUIRED` in the label — never an
  asterisk in red (the census) and never colour alone.
- **Tokens consumed (v2).** `--graphite`, `--graphite-soft`,
  `--ruling`, `--carbon`, `--carbon-pale`, `--stamp`,
  `--ease-thump`, `--ease-pencil`, `--stamp-angle` (−4deg),
  `--dur-watchdog-form` (3000ms).

### 6.15 Ruled skeleton, paper feed & the carbon-sheet transition

- **What & why.** Three moments of the sheet's own handling,
  one element family. *Loading:* regions still arriving show
  faint ruled lines with a blinking caret at the last line's
  end — the sheet before the typing starts. *First load:* the
  paper feeds in from the top, 500ms, before the headline
  types (§6.1). *Page transitions:* a carbon-copy sheet slides
  over the page and lifts away — you leave through the copy,
  and arrive on the next sheet as its own first entry writes.
  They belong together because all three are the same physical
  fact: paper is handled by people and machines, and the
  handling is visible.
- **Structure.** Skeleton regions are the real layout boxes
  with `data-unwritten` — ruled lines (the sheet's own ruling,
  §4) plus 2–4 heavier graphite-soft line stubs at the coming
  text's lengths, and a caret (a 2px graphite block) at the
  final stub's end. The feed is a transform/clip on the sheet
  wrapper for the first 500ms only. The transition is a full-
  viewport `--carbon-pale`-tinted sheet layer carrying a pale
  duplicate of the destination's title, sliding down over
  450ms `--ease-feed`, holding 120ms, lifting over 450ms as
  the destination's head writes.
- **Motion spec.** Skeleton caret: blink 1,060ms steps(1) —
  the theme's second licensed ambient loop (§5), alive only
  while a skeleton is on screen. Hard ceiling: any region
  still unwritten at 1,500ms prints its content anyway — the
  log does not hold a reader hostage to a slow exhibit.
  Transition total ≤1,020ms, watchdogged at 1,800ms: if the
  destination is not ready, the carbon sheet lifts anyway and
  the destination shows its skeleton — a reader may wait on a
  sheet, never *between* sheets in the dark.
- **States.** Unwritten (skeleton + caret) / writing (the
  region's own §6.2 sequence) / written. Transition: covering
  / holding / lifting / gone. Feed: feeding (first load only,
  once per session — a returning visitor's sheet is already on
  the desk).
- **Content merge.** The skeleton is shaped like the entry it
  precedes and ruled by the same grid; the transition's carbon
  sheet carries the destination's actual title, pale, the way
  a copy carries the original's words. Continuity of paper
  across pages is the theme's answer to the page boundary:
  it is one pad, leaf by leaf.
- **Failure fallback.** Watchdogs per region (1,500ms) and on
  the transition (1,800ms) as above. No-JS: no skeletons, no
  feed, no transition — plain navigation between complete
  sheets, which is how the archive has always been used.
- **Reduced-motion variant.** Skeletons are static ruled
  stubs (no caret blink) that swap to print instantly on
  arrival; no feed; transitions are plain navigations whose
  destination arrives fully typed at its head.
- **Performance budget & mobile variant.** Skeletons are CSS
  (gradients + one caret element), zero loop cost. The
  transition reuses one layer element. Mobile: feed shortens
  to 350ms; the transition's hold is cut (cover 400ms, lift
  400ms); skeleton caret cut (static stubs) to save battery.
- **Choreography timeline (v2).** First load → feed 500ms →
  headline arms (§6.1). Region requested → skeleton prints
  with the layout → data lands → region writes (§6.2) →
  caret gone with the first line. Ceiling 1,500ms forces
  print. Transition: activate a cross-page link → cover
  450ms → hold 120ms → navigate → lift 450ms → destination
  head writes. Watchdog 1,800ms.
- **State matrix (v2).** *Rest:* printed content. *Hover:*
  n/a. *Focus:* skeleton regions are `aria-hidden` and
  unfocusable until printed; focus is never placed inside an
  unwritten region — if the reader tabs toward one, the
  region prints instantly (the §6.2 focus rule). *Active:*
  the form's filing state (§6.14) uses this caret. *Scrolled-
  past:* regions below the fold write on arrival regardless
  of visibility. *Disabled / no-JS:* server print, no
  skeletons. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full timings. 768–1199px:
  full, feed 450ms. <768px: shortened timings (above).
- **Edge cases & failure modes (v2).** *Data arrives before
  the skeleton paints:* the region prints directly — a
  skeleton that never appears is the best kind. *Partial
  failure (an exhibit's data fails):* that region prints its
  `PRINT NOT RECEIVED` note (§6.9) at the ceiling while the
  rest of the sheet completes — the log opens with the gap
  admitted. *Back-button arrival:* no transition, no feed;
  the sheet is as it was left, stamps and all (§6.7's session
  state) — the desk remembers.
- **Accessibility spec (v2).** Skeleton containers carry
  `aria-busy="true"` until printed and are removed from the
  accessibility tree's focus order; one polite announcement
  (`The log is open.`) fires when the last above-fold region
  prints. The transition is never announced and never traps
  focus. The caret blink is disabled under reduced motion and
  for `prefers-reduced-transparency` the carbon sheet renders
  as plain `--paper-deep`.
- **Tokens consumed (v2).** `--ruling`, `--graphite-soft`,
  `--graphite`, `--carbon-pale`, `--paper-deep`,
  `--ease-feed`, `--dur-feed` (500ms), `--dur-unwritten-
  ceiling` (1500ms), `--dur-watchdog-transition` (1800ms).

---

### 6.16 The sign-off footer

- **What & why.** The sheet ends the way the log ends: with a
  sign-off. The footer band (on `--paper-deep`, the pad's last
  leaf) prints the mission's totals for the third time, the
  flight director's closing line and initials, the count of
  requests on file (87 — or 88, if the visitor filed, §6.14),
  the count of entries the visitor signed (§6.7) if any, and
  the clerk's references: links to the archive's other volumes
  (the data table page, the exhibits, the request form) set as
  margin references, not a corporate footer menu. It belongs
  because a ledger is *closed*, not abandoned — the last act
  of the record is a person signing it complete.
- **Structure.** A footer block in the sheet's own anatomy:
  a graphite double rule, then the closing entry — unnumbered,
  titled `SIGN-OFF` — carrying the totals in Data type
  (`DURATION T+76:18:00 · ORBITS 49 · DISTANCE 1,107,400 NM ·
  ENTRIES 12 · REQUESTS ON FILE 87`), the closing line in Body
  type (`The flight is complete. The log is closed and filed.`)
  and the director's initials `E.C.` beside a short graphite
  signature rule. Below, in Margin type, the clerk's
  references and the sheet's own colophon: `SET IN SPECIAL
  ELITE AND IBM PLEX MONO. RULED AT 32PX. NO ENTRY WAS ERASED
  IN THE KEEPING OF THIS LOG.`
- **Motion spec.** The footer writes with §6.2's sequence when
  it first crosses the centre rule — it is an entry, and it is
  written like one. As it completes, the margin ruler's hand
  (§6.3) reaches the total and the strip (§6.11) prints
  `LOG CLOSED`. Nothing else moves; a closed log is still.
- **States.** Unwritten / writing / closed (rest). The
  requests count and signed count are computed at print time
  from session state and then fixed — the footer's figures do
  not tick after closing.
- **Content merge.** Every figure is a record figure in its
  third printing (hero-adjacent copy, §6.13's totals row, and
  here), and §10's audit requires the three to agree digit-
  for-digit. The colophon's last sentence is the theme's law
  restated as the archive's boast — it is printed, not
  animated, because it is a claim about the document the
  reader is holding.
- **Failure fallback.** Static HTML; the session-derived
  counts fall back to the record's printed values (87
  requests; the signed line is omitted entirely if session
  state is unavailable — §6.7's rule — rather than printing
  zero, which would be a false entry).
- **Reduced-motion variant.** The footer arrives printed.
  `LOG CLOSED` is simply the strip's state at the foot.
- **Performance budget & mobile variant.** No loop cost beyond
  §6.2's write. Mobile: totals stack two per line in Data
  type; the clerk's references become a single ruled list;
  the colophon keeps its three sentences — the small sheet
  does not abridge the closing.
- **Choreography timeline (v2).** Footer crosses the centre
  rule → double rule draws 300ms → totals print (line
  stagger 30ms) → closing line writes → signature rule draws
  200ms `--ease-pencil` → ruler hand lands on the total,
  strip prints `LOG CLOSED` → sheet at rest, permanently.
- **State matrix (v2).** *Rest:* closed. *Hover:* reference
  links take the pencil underline (§6.8). *Focus:* as hover,
  with outlines. *Active:* links navigate (§6.15's
  transition). *Scrolled-past:* closed. *Disabled:* a
  reference to a volume not in this build prints in
  graphite-soft without a link and the words `NOT IN THIS
  VOLUME` — the clerk does not cite what the archive does
  not hold. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: totals on one line.
  768–1199px: totals wrap to two lines at the middle dot.
  <768px: two per line (above).
- **Edge cases & failure modes (v2).** *Visitor filed a
  request then reads the footer:* the count reads 88 and a
  margin line adds `YOUR REQUEST IS № 088.` — the footer
  acknowledges the visitor's own entry in the log. *Visitor
  signed entries:* `SIGNED BY YOU: 3 OF 12.` prints; if they
  signed none, the line is absent (the log does not nag).
  *Print:* the footer is the print stylesheet's last block;
  the colophon prints in full.
- **Accessibility spec (v2).** A real `<footer>`; totals are
  text, not a graphic; the signature rule is `aria-hidden`
  (the initials beside it carry the meaning). Contrast:
  graphite on `--paper-deep` 8.6:1.
- **Tokens consumed (v2).** `--paper-deep`, `--graphite`,
  `--graphite-soft`, `--carbon`, `--ease-pencil`,
  `--dur-line-draw` (300ms).

### 6.17 The mission record — the one source of every figure

- **What & why.** This section is not an element on the page;
  it is the document the page is printed from. Every figure,
  timestamp, status and initial anywhere in the theme traces
  to the record declared here, and the quality gate (§10)
  audits the shipped page against it. The record is a single
  fictional-but-internally-exact flight: Kestrel IV, November
  1968. A build may substitute another mission (the theme
  serves any log), but it must declare the substitute in full,
  here, with the same completeness — an undeclared figure on
  the page is a §9 failure and a §10 block.
- **Structure.** The record is one data object at build (a
  table in the source, rendered into entries, index, ruler,
  table and footer — never hand-copied between them). Its
  fields: flight constants, the station roster, the twelve
  entries verbatim, the derived totals with their derivations,
  the exhibits, the stamps' vocabulary, and the archive's
  request count.
- **Motion spec.** None — the record does not move. It is the
  still point every moving element reads from: the ruler's
  scale, the counters' targets, the route's fractions, the
  form's next number. (This field is present so the element
  count of this section's spec matches its siblings: the
  record's "motion" is that everything else's motion must
  land on *its* figures.)
- **States.** The record has one state: declared. A figure in
  `PROVISIONAL` state (§6.13) is a different record, declared
  as such here, with the word printed wherever the figure
  appears.
- **Content merge.** Total — the record is the content's
  source, not its decoration. The merge rule runs the other
  way: any page content that cannot name its record field is
  removed at review.
- **Failure fallback.** If a record field is missing at build,
  the build fails (§15 step 1); there is no runtime fallback
  for an undeclared figure, by design — the page is not
  allowed to improvise its facts.
- **Reduced-motion variant.** n/a — and stated so: the record
  is identical for every reader, which is rather the point of
  a record.
- **Performance budget & mobile variant.** The record renders
  at build; runtime cost is zero beyond the values it feeds.
  It exists once in the source; the shipped page carries only
  its printings.
- **Choreography timeline (v2).** Build-time only: constants
  declared → entries validated (timestamps ascending, GMT =
  launch + T+ for every row) → totals derived → printings
  generated. The visitor's timeline never touches it.
- **State matrix (v2).** *Rest:* declared. *Hover / focus /
  active / scrolled-past / disabled / touch:* n/a in all —
  the record is not an interface element; its printings carry
  their own matrices (§6.1–§6.16, §6.18).
- **Breakpoints (v2).** n/a — the record is size-invariant;
  its printings' breakpoints are specified per element.
- **Edge cases & failure modes (v2).** *A GMT that disagrees
  with launch + T+:* build validation fails — the two clocks
  (§3 law 1) are one clock read twice, and a disagreement is
  an arithmetic error in the record, not a design choice.
  *An entry whose figure contradicts its text:* the text is
  the record (entries are verbatim); figures in the table
  (§6.13) are derived from the text at build and audited.
  *A thirteenth entry added in a CMS:* permitted only by
  re-declaring the record — totals, index, ruler ticks and
  the form's numbering all derive from the entry list, so a
  re-declared record re-derives the whole page consistently;
  an undeclared thirteenth entry breaks §10 checks 1 and 9.
- **Accessibility spec (v2).** The record's printings are
  specified per element; the record itself additionally
  requires that every figure it declares be available as real
  text somewhere in the DOM at full contrast — no figure may
  exist only inside a canvas, an image, or an animation.
- **Tokens consumed (v2).** None directly; every token its
  printings consume is listed in their own specs.

**The record — KESTREL IV.**

*Constants.* Flight: KESTREL IV, crewed orbital test flight,
three crew — Commander J. Hale (JH), Pilot D. Whitfield (DW),
Systems R. Calloway (RC). Launch: Pad 34, 14 November 1968,
14:32:00 GMT. Flight Director: E. Crane (EC). Total mission
elapsed time: **76:18:00** (splashdown 17 November 1968,
16:50:00 GMT). Orbits completed: **49**. Mean orbital
circumference as logged: 22,600 nautical miles; distance
travelled: 49 × 22,600 = **1,107,400 nautical miles**.
Mission quarters (for §6.10): Q1 T+19:04:30, Q2 T+38:09:00,
Q3 T+57:13:30, Q4 T+76:18:00. Requests on file at the
archive: **87** (the form opens at № 088, §6.14).

*Stations polled (the room's eleven):* FLIGHT (EC), FDO (TA),
GUIDO (MR), EECOM (PN), TELMU (SO), CAPCOM (WB), GNC, INCO,
O&P, SURGEON, RECOVERY — six initialled in this log's entries,
eleven polled at № 003; the legend is printed in the index
(§6.11) so no initial on the page is a stranger.

*The twelve entries (verbatim — text, figures, status):*

| № | T+ | GMT | Phase | Entry | Initials | Status |
|---|---|---|---|---|---|---|
| 001 | 00:00:00 | 14 NOV 14:32:00 | LIFTOFF | "Liftoff. Kestrel IV away clean off Pad 34. All stations report GO." | EC | CONFIRMED |
| 002 | 00:11:48 | 14 NOV 14:43:48 | ORBIT | "Orbit insertion confirmed. 25,572 feet per second. Orbit 141 by 117 nautical miles." | TA | CONFIRMED |
| 003 | 01:34:20 | 14 NOV 16:06:20 | ORBIT | "First systems pass complete. Eleven stations polled. Eleven GO." | EC | CONFIRMED |
| 004 | 05:47:05 | 14 NOV 20:19:05 | ORBIT | "Cabin pressure falling." — struck; corrected above the line: "Cabin pressure holding at 4.9 psi. Gauge fault traced to the panel, not the cabin." | PN | CONFIRMED |
| 005 | 12:08:31 | 15 NOV 02:40:31 | RENDEZVOUS | "Rendezvous complete. Range closed from 42 miles to station-keeping at 120 feet. (Exhibit B.)" | MR | CONFIRMED |
| 006 | 24:00:00 | 15 NOV 14:32:00 | ORBIT | "Day two opened on the second. Crew rested, fed, and ahead of the plan." | EC | CONFIRMED |
| 007 | 31:15:44 | 15 NOV 21:47:44 | BURN | "Burn number three. Six point two seconds. Delta-V 48 feet per second. Trim nominal." | TA | CONFIRMED |
| 008 | 42:52:10 | 16 NOV 09:24:10 | ORBIT | "Experiments six of eight complete. The crew asks for more work. None given." | WB | CONFIRMED |
| 009 | 55:03:27 | 16 NOV 21:35:27 | ORBIT | "Signal lost four minutes twelve seconds over the Pacific. Reacquired on schedule. No action taken, none needed." | SO | REACQUIRED |
| 010 | 63:40:00 | 17 NOV 06:12:00 | RETURN | "Deorbit preparation complete. Thirty-eight items checked, thirty-eight. Experiments eight of eight." | EC | CONFIRMED |
| 011 | 75:44:00 | 17 NOV 16:16:00 | RETURN | "Deorbit burn. One hundred eighty-eight seconds. The ship is coming home." | TA | CONFIRMED |
| 012 | 76:18:00 | 17 NOV 16:50:00 | SPLASHDOWN | "Splashdown. Two point eight miles from the aim point. Crew well. The log is closed." | EC | CONFIRMED |

*Derived figures, with derivations (the gate re-derives
them).* Every GMT above = 14 NOV 14:32:00 + T+ (checked per
row at build). Quarters: 76:18:00 ÷ 4 = 19:04:30; ×2 =
38:09:00; ×3 = 57:13:30. Signal loss: 4 min 12 s = 252 s.
Experiments: 6 of 8 at № 008, 8 of 8 at № 010. Checklist:
38 of 38 at № 010. Route fractions (§6.6): insertion at
11:48 / 76:18:00 ≈ 1.5% — the route's first cross sits at the
arc's foot; rendezvous at ≈15.9%; deorbit at ≈99.1% —
the plan's shape is the mission's shape: a long orbit leg
and everything else at the ends.

*Exhibits.* A — liftoff photograph, at № 001. B — rendezvous
photograph, at № 005. C — splashdown photograph, at № 012.
Coffee rings: two, at the margins of № 004 and № 009 (§4).

*Stamp vocabulary.* LOGGED (the headline, §6.1), CONFIRMED
(entry sign-off, §6.7 — and REACQUIRED for № 009 only), FILED
(the request form, §6.14). No other red words exist.

### 6.18 Never logged — the 404 & empty state

- **What & why.** A page the archive does not hold is itself
  entered in the log — as the entry that was never written.
  The 404 sheet is ruled like every other, its margin carries
  the requested position, and its body carries one line in the
  log's voice: `NO ENTRY AT THIS POSITION.` — followed by the
  way back: the index (§6.11) printed in full, so the lost
  reader is handed the whole contents and picks a real entry.
  The empty state (an archive search or index filter with no
  matches) is the same ruling at component scale: `NO ENTRIES
  UNDER THIS HEADING. THE LOG RECORDS WHAT HAPPENED.` It
  belongs because absence in an archive is a finding, not an
  error — and it is recorded in the same hand as everything
  else.
- **Structure.** The 404 is a full sheet: masthead (static),
  one entry block whose margin prints `№ —` and the requested
  path in Margin type (the only place a URL appears on the
  sheet, set as data, not as a link), the line in Entry-head
  type, a short Body line (`The sheet you asked for is not in
  this volume. The index follows.`), then the complete index.
  No stamp: nothing here was authorised, so nothing is red.
  The empty state is an entry-shaped block with the same
  margin anatomy and no number.
- **Motion spec.** The 404 entry writes with §6.2's sequence
  (it is an entry; it is written like one) — except the
  margin's entry number never types: the dash is printed from
  the start, because there is no number to write. The index
  below prints in full without stagger (a lost reader is not
  made to watch twelve rows type). No other motion.
- **States.** One state: printed and written. There is no
  loading state for a page whose content is an absence.
- **Content merge.** The 404's index is the record's index —
  the same twelve rows as §6.11, generated from §6.17 — so
  the recovery is the document itself, not a sitemap pasted
  under an apology. The requested path in the margin is the
  reader's own input, echoed as data.
- **Failure fallback.** The 404 is static HTML served as a
  document; it has no script dependencies at all (its write
  sequence is the only enhancement, and §6.2's fallback covers
  it). If the index generation fails at build, the build
  fails — a 404 without the index is a dead end, and dead
  ends are §9 failures.
- **Reduced-motion variant.** Printed, unwritten, complete.
- **Performance budget & mobile variant.** The lightest page
  in the theme: no exhibits, no form script. Mobile: the
  index is the one-column variant (§6.11); the requested path
  wraps in the margin block above the entry rather than
  overflowing it.
- **Choreography timeline (v2).** Arrival (no transition —
  §6.15's carbon sheet does not cover an error arrival) →
  masthead static → the entry writes (rule draw 300ms, line
  opens) → the dash in the margin simply *is* → index already
  printed below → rest.
- **State matrix (v2).** *Rest:* printed. *Hover:* index rows
  take the pencil underline (§6.8). *Focus:* index links as
  §6.11. *Active:* following a row goes to a real entry.
  *Scrolled-past:* n/a. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: as specified. 768–1199px:
  index three-column variant. <768px: index one column; the
  margin block stacks above the entry.
- **Edge cases & failure modes (v2).** *A requested path with
  markup in it:* the path is echoed as text, escaped — the
  margin records data, it does not execute it. *Search empty
  state with a query that almost matches an entry title:* the
  block adds one margin line, `NEAREST ENTRY: № 005 —
  RENDEZVOUS.` — computed from the record's titles, in the
  clerk's voice, never an algorithmic "did you mean" in
  another theme's words. *A filtered index with zero of
  twelve:* the empty block prints where the rows would be;
  the filter itself stays visible and changeable.
- **Accessibility spec (v2).** The 404's heading is the line
  itself (`NO ENTRY AT THIS POSITION.`) as an `<h1>`; the
  HTTP status does the rest — no `role="alert"`, nothing
  flashes. The empty state is a polite live region when it
  results from a filter change, so a screen-reader user hears
  the log's sentence once. Contrast: graphite on paper, 9.5:1,
  throughout — the emptiest page keeps the full reading
  contrast.
- **Tokens consumed (v2).** `--graphite`, `--graphite-soft`,
  `--ruling`, `--carbon`, `--ease-pencil`, `--dur-line-draw`
  (300ms).

---

## 7. Page application map

| Page | How the theme plays |
|---|---|
| **Home — the log itself** | The full sheet: masthead + index (§6.11), the twelve entries in order with all ten signature acts, exhibits A–C in place, the flight-data summary strip (current phase's cards, §6.12), the request form as the final entry (§6.14), the sign-off footer (§6.16). The home page *is* the document. |
| **Listing — the archive** | Other volumes (other flights, other years) as station cards (§6.12) on a fresh sheet, one column, each card a volume's first entry. Pagination is `VOLUME 2 OF 5` with clerk's links (§11) — an archive is volumed, not paged like search results. |
| **Detail — a single entry** | One entry at full size on its own sheet: margin ruler spanning that entry's T+ to the next (§6.3's rule), its exhibit at full column width, the route (§6.6) drawn to its waypoint, prev/next entries as margin references (`PREV: № 004 — CABIN PRESSURE`), and the entry's stamp state carried from the session (§6.7). |
| **About — the room** | The stations and the keeping of the log: the roster (§6.17's legend) as entries in the same anatomy — each station a short entry, initialled. No team-grid, no avatars; the room is described the way it described flights. |
| **Contact — request the file** | §6.14's form as the whole page: the form entry, the archive's terms printed as margin notes (`THE FILE IS SENT BY POST AND BY WIRE.`), nothing else. Contact here is a filing, not a chat. |
| **Sign-off / plan page** | §6.6's route at full width above the flight-data table (§6.13) and the sign-off entry — the document's own summary leaf, linked from the footer as a clerk's reference. |
| **Checkout / commerce** | **Refused.** The ledger does not sell inside its own pages. A build that must take payment links out to a plainly separate, unthemed checkout and returns to a confirmation *entered as an entry* (`PAYMENT RECEIVED — ENTERED AS № …`) using §6.14's anatomy. The sheet records the transaction; it does not perform it. |
| **404** | §6.18 as specified. |

## 8. Worked examples

### 8.1 The hero — liftoff, entered (worked example 1)

**What the visitor lives.** The sheet feeds in (500ms,
§6.15). The headline types — `KESTREL IV —` carriage return,
`THE FLIGHT LOG` — at 55–85ms a character with its 1px jitter,
and at the last character the LOGGED stamp slams at −4° and
the paper compresses 2px under it (§6.1). Below, entry № 001
is already written (it is above the centre rule's first
reading): `T+00:00:00 · 14 NOV 14:32:00 · EC` in the margin,
`LIFTOFF` on its line, and the entry: *"Liftoff. Kestrel IV
away clean off Pad 34. All stations report GO."* Exhibit A is
taped at the entry's right, settling from 1.05 as the reader
begins to scroll (§6.9). The margin ruler's hand sits at
T+00:00:00; the strip has not yet clipped on. *Feels like:*
being handed the log at the moment the flight begins, by the
person who kept it.

**Build notes.** Headline and stamp per §6.1 (watchdog
≈3,400ms); № 001 ships written — its write sequence is armed
only if the reader arrives with the entry below the fold
(small viewports), in which case §6.2 runs it on the centre
rule like any entry. The hero contains no figure that is not
in № 001 or the constants (§6.17): no altitude claim, no
speed — those belong to № 002, one entry down, where the
record puts them.

### 8.2 Mid-page — the correction, as the visitor lives it (worked example 2)

**What the visitor lives.** Entry № 004 reaches the centre
rule. Its ruled line draws; the margin prints `T+05:47:05 ·
14 NOV 20:19:05 · PN`; the title `CABIN PRESSURE` sets; the
body line types: *Cabin pressure falling.* — and stops. Half
a second of nothing (the room noticing). A pencil stroke
draws itself across *falling*, pressing then lifting. Above
the line, in carbon blue, the correction types: *holding at
4.9 psi. Gauge fault traced to the panel, not the cabin.* The
entry signs off `P.N.` and the reader scrolls on — past the
coffee ring in this entry's margin, which was there all
along. The whole act takes ≈2.6s longer than a normal entry's
write, and it is the moment visitors describe to other
people. *Feels like:* watching a professional catch an error
in real time and handle it exactly right.

**Build notes.** §6.4 in full: `<s>` semantics, stroke SVG
hand-plotted, correction in the reserved interlinear band,
watchdog at write deadline +1,200ms, exactly-once latch, and
the §10 census that counts precisely one strike-through on
the page. The coffee ring is a background layer at the
margin, positioned from the record (§6.17), parallaxed at
pencil depth (§5) — present in the printed state, since a
stain does not need JavaScript to have happened.

### 8.3 Conversion — a request enters the log (worked example 3)

**What the visitor lives.** After splashdown (№ 012) and
before the sign-off, the sheet offers its final entry — not
numbered with the flight's, but with the archive's: margin
`№ 088 · VISITOR T+09:12` (their own reading time, from
§6.3's clock), title `REQUEST THE FILE`. The preamble line
reads: *"Requests on file: 87. Yours will be entered as
№ 088."* They write their name on a ruled line, their email
on the next, choose `RESEARCH` from the ruled options; the
carbon ghost lays under the form as they write (§6.14). They
press `FILE THIS REQUEST` — it thumps — the caret blinks at
the entry's end for a second, and then the entry completes
itself: *"Request entered. The file of Kestrel IV — log,
exhibits, and data table — will be sent to the address
given."*, `FILED.` in the margin, and the red FILED stamp at
−4° across the corner. When they reach the footer, it reads
`REQUESTS ON FILE 88` and, in the margin, `YOUR REQUEST IS
№ 088.` *Feels like:* not a conversion — a filing. The
visitor has not been funnelled; they have been *entered in
the log*, between splashdown and sign-off, where the record
keeps them.

**Build notes.** §6.14 in full: number derived from the
record (87 + 1), idempotent by number, 3,000ms watchdog into
the kept-words archive-closed state, error corrections in
the §6.4 pencil-and-carbon language, no-JS native post to a
server-rendered confirmation in the same anatomy.

## 9. Anti-slop — what makes THIS theme look cheap

1. **A handwriting font.** The instant entries are set in a
   script face, the log becomes a greeting card. *Cure:* two
   families only (§3); the hand appears as behaviour —
   strokes, stamps, initials in mono.
2. **Dashboard creep.** A stat card, a donut chart, a "live"
   KPI anywhere on the sheet. *Cure:* figures live in entries
   and in §6.13's table, set in mono, at record precision.
   If it has a widget, it is not this theme.
3. **Red everywhere.** Red links, red errors, a red "NEW"
   badge. *Cure:* the §2 census — red is stamps, full stop;
   the gate greps it (§10 check 2).
4. **The mistake as a gimmick.** Strike-throughs in headlines,
   a "fun" typo per section. *Cure:* exactly one correction,
   inside № 004, in a real entry, with real figures (§6.4);
   the gate counts them.
5. **Erasing by another name.** A strike so heavy the word
   can't be read, or the correction replacing the line.
   *Cure:* the struck word stays legible through a 2px stroke
   (§6.4's accessibility spec) — an unreadable strike is a
   deletion wearing the theme's clothes.
6. **Clip-art coffee rings.** Stains scattered decoratively,
   a ring per section. *Cure:* two rings, at № 004 and № 009,
   positions declared in the record (§6.17); a third ring
   fails the gate.
7. **Typewriter sound.** Keystroke audio, a ding at the
   carriage return. *Cure:* no audio anywhere in the theme;
   the thud is a 2px compression of paper (§6.1), felt, not
   heard.
8. **Jitter as wallpaper.** Headlines trembling forever,
   body text with a permanent shake. *Cure:* §3 law 3 —
   jitter belongs to the act of typing and dies with it.
9. **Rounded figures in display type.** "Over a million
   miles!" in the headline. *Cure:* §3 laws 1–2 and the law
   itself: figures are mono, exact, and traced (1,107,400,
   in the table and footer, never in a headline).
10. **Tape and stamps as decoration pack.** Tape on headings,
    a stamp on every card regardless of status. *Cure:*
    tape exists only on exhibits (§6.9); stamps land only
    where the record has a status (§6.7) — furniture without
    a record field is refused at review.
11. **Sepia filter nostalgia.** A brown wash over modern
    photography, "vintage" gradients. *Cure:* exhibits are
    documentary photographs presented plainly (§6.9); the
    paper token is the only ageing on the page.
12. **Entries that are really marketing.** An entry that says
    "our world-class team achieved excellence". *Cure:* §12's
    voice — the log's sentences report events with figures;
    an entry an editor would call copy is rewritten until a
    flight director could have typed it.

## 10. Quality gate

Blocking checks — all must pass before this theme ships in a
build, signed off by someone who did not build it:

1. **Figure audit.** Every printed figure traces to a field
   in the Mission Record (§6.17); the three printings of the
   totals (table §6.13, footer §6.16, and the ruler's full
   scale §6.3) agree digit-for-digit; every GMT re-derives
   from launch + T+.
2. **Red census.** `grep` the shipped CSS/JS/HTML for the
   stamp token and the `.stamp` class: red appears only
   inside stamp elements (LOGGED, CONFIRMED/REACQUIRED,
   FILED). Any other occurrence fails the build.
3. **Strike census.** Exactly one struck word on the home
   sheet (§6.4, № 004), legible through its stroke; the
   correction present in carbon above the line, in the DOM,
   with JavaScript disabled.
4. **Watchdog drill.** With the loop artificially stalled,
   every armed effect completes to its printed end state
   inside its deadline (headline ≈3,400ms, entries 1,800ms,
   correction +1,200ms, transition 1,800ms, form 3,000ms).
5. **No-JS pass.** The full sheet — headline, twelve entries
   with the correction visible, index, exhibits with captions,
   table, form (posting natively), footer — complete and
   readable with JavaScript disabled.
6. **Reduced-motion pass.** Ledger fully typed on arrival,
   stamps static, ghost printed still or absent, no typing,
   no thumps; verified with the OS setting on.
7. **Loop budget.** The shared loop's frame cost ≤1.2ms with
   all citizens registered (ruler, ghost, ink rule, route,
   exhibit settle, card tilt) on a mid-tier laptop; no long
   task >50ms.
8. **Timestamp audit.** Every entry shows both clocks (§3
   law 1); the strip's MET never exceeds the current entry's
   T+ and never runs past 76:18:00; the ruler's furthest-
   marker never retreats.
9. **Count audit.** Twelve index rows, twelve entries,
   twelve cards where cards are used, three exhibits, two
   coffee rings, six phases on the strip — counted in the
   shipped DOM against the record.
10. **Contrast sweep.** Every text pairing meets §2's ratios
    at every state, including graphite-soft captions (≥4.5:1,
    captions only) and the stamp at its smallest size.
11. **Voice pass.** Entries, errors, empty states and fixed
    strings read against §12; grep for `NO ENTRY AT THIS
    POSITION.` and `FILED.` verbatim; no exclamation mark
    anywhere in log voice.
12. **Mobile pass.** At 360px: the headline types, entries
    write with stacked margins, the strip holds phase on one
    line, the table is the stacked list, the form's stamp
    button is ≥48px, the correction's interlinear band does
    not collide with wrapped lines.

---

## 11. Component inventory

Every component a real site in this theme needs, with its
themed treatment. Anything not listed does not appear; a
component arriving from a generic UI kit is refused at
review (§9.2's dashboard creep begins at the component tray).

| Component | Themed treatment |
|---|---|
| Primary button | **Stamp button** — double-rule graphite border, Stamp type label (`FILE THIS REQUEST`), thumps 2px on press (§6.7's ease). One per view; a sheet is stamped at its moments, not studded with them. |
| Secondary button | **Margin reference** — mono text with the pencil underline (§6.8); no box. `RETURN TO THE INDEX`, `SEE THE DATA TABLE`. |
| Text input | A ruled line: bottom rule in `--ruling`, darkening to graphite on focus (§6.14); label above in Label type; text in mono sitting on the line. No boxes, no floating labels — you write on lines. |
| Select | Ruled radio lines (§6.14's mobile pattern at all sizes on form pages): each option its own ruled line, chosen option marked with a graphite pencil tick. On non-form pages a native select in mono is permitted, styled to the ruling. |
| Textarea | Ruled at 32px like the sheet, 4 lines, mono; the visitor writes an entry, not a message in a bubble. |
| Checkbox / radio | **Pencil marks** — a small ruled box the visitor's choice fills with a graphite × (drawn, 150ms `--ease-pencil`, when motion allows). The mark is a hand's, not a glyph font's. |
| Table | §6.13 as specified: ruled, tabular mono, totals in `tfoot` behind a double rule, no sorting, no striping. |
| Badge / chip | **Phase tags** — the entry's phase printed in Label type in the margin, no pill, no fill. Status words print as text; only stamps are stamped. A coloured chip is refused. |
| Alert | **Refused as a banner.** Notices are margin notes in graphite-soft beside the relevant entry (`THE ARCHIVE IS CLOSED TONIGHT.`), in place, permanent until read. Nothing slides over a log. |
| Toast | **Refused.** Same replacement: the margin note, in place (§6.14's filing states). |
| Modal | **Refused.** A ledger does not dim its own page to ask a question. Confirmations happen as entries (§6.14's filed state) or not at all. |
| Tabs | **Refused.** The log is read in order; §7's pages are volumes, reached by the index and the clerk's references, not by a tab bar pretending the sheet has sides. |
| Accordion | **Index folds** — on archive pages, a volume's entries fold under its card; opening prints them whole (240ms height, `--ease-drift`). Archive furniture only, never for primary content. |
| Pagination | **Volume markers** — `VOLUME 2 OF 5` with prev/next as margin references. A log is volumed; it is not paged like search results. |
| Tooltip | **Margin gloss** — hovering/focusing a figure or initial prints its expansion in the margin (`PN — EECOM, P. NOVAK`), in place. No floating bubble; the margin is where glosses have always lived. |
| Progress | The margin ruler (§6.3) and the ink rule (§6.10) are the only progress components. No bars, no percentages, no spinners anywhere in the theme. |
| Skeleton | §6.15's ruled stubs with the blinking caret — content-true shapes on the sheet's own ruling, never a grey shimmer. |
| Breadcrumbs | **Refused on the home sheet** (the log is read in order); on detail pages a single margin line: `LOG / № 005 — RENDEZVOUS`, set as text. |
| Avatar / byline | People are initials in the margin (§6.17's legend), never photographs in circles. Faces appear only inside exhibits (§6.9), at documentary scale. |
| Search | On archive pages only: a ruled-line input filtering volumes and entries by number, word or initial; the result count is itself entered as a margin note (`3 ENTRIES`). §6.18's empty state covers no-match. |
| Empty state | §6.18's entry-shaped block: `NO ENTRIES UNDER THIS HEADING. THE LOG RECORDS WHAT HAPPENED.` |
| Error state (field) | The §6.4 treatment at form scale: strike in pencil, reason in carbon above the line (§6.14). Red is not available (§2). |
| 404 | §6.18 as specified. |

## 12. Content & copywriting voice

Two registers, kept apart as strictly as the palette:

- **Log voice** — entries, explanations, errors, empty
  states. IBM Plex Mono, sentence case, past tense, figures
  at record precision, adjectives only where an instrument
  or an event supplied them (`clean`, `nominal`, `on
  schedule`). The log's model sentence: *"Signal lost four
  minutes twelve seconds over the Pacific. Reacquired on
  schedule. No action taken, none needed."* Short sentences.
  Full stops. The drama is in the facts.
- **Margin voice** — the director's asides: index heads,
  glosses, clerk's references, the form's preamble. Briefer
  than the log, personal where the log is procedural:
  `Requests on file: 87. Yours will be entered as № 088.`
  The margin may acknowledge the reader; the log never does
  — the log was written in 1968 and does not know the reader
  exists. Keeping that fiction unbroken is the theme's
  central discipline.

**Headline style.** Special Elite, the mission's name and
nature, never a figure and never a boast. ✓ *"Kestrel IV —
the flight log."* ✗ *"1.1 MILLION MILES OF TRIUMPH!"* — a
rounded figure, a superlative and an exclamation: three
violations in five words. Exclamation marks do not exist in
this theme, in either register.

**Label style.** Nouns and units, no marketing verbs:
`CABIN PRESSURE`, `REQUEST № 088`, `EXHIBIT B`. ✗ `BLAST
OFF INTO SAVINGS` — the sheet does not sell; it records.

**Error voice.** State what did not happen, what was kept,
and what to do — in that order, in the log's sentences.
✓ `NOT FILED — THE WIRE IS DOWN. YOUR WORDS ARE KEPT BELOW.`
✓ `THE LINE HOLDS FORTY CHARACTERS. SHORTEN IT.`
✗ `Oops! Something went wrong` — every word of that is from
another theme.

**Empty-state voice.** Absence is a logged fact, stated
once: ✓ `NO ENTRIES UNDER THIS HEADING. THE LOG RECORDS
WHAT HAPPENED.` ✗ *"Nothing here yet — check back soon!"* —
the log does not promise; it records.

**Fixed strings (verbatim, grepped by the gate).**
`LOGGED.` · `CONFIRMED` · `REACQUIRED` · `FILED.` ·
`NO ENTRY AT THIS POSITION.` · `THE LOG IS CLOSED.` ·
`ALREADY SIGNED.` · `PRINT NOT RECEIVED.` These sentences
are part of the theme's identity; paraphrase is drift, and
drift is how the log stops being the log.

## 13. Full-page scroll choreography map

The home sheet, top to footer, in the order the visitor
lives it. One shared rAF loop (lerp 0.11) drives every
scrubbed value; beats are listed at their trigger points
against the centre rule (55% of viewport height, §4).

1. **First paint.** The complete sheet, printed: headline,
   stamps, entries, exhibits, footer — all present. *Feels
   like:* the log was already kept.
2. **Feed (500ms, first visit only).** The paper feeds in;
   the headline arms and types (≈2.2s); LOGGED slams at −4°,
   the sheet compresses 2px and recovers (§8.1).
3. **№ 001–002 — the loud first hour.** Entries write at the
   centre rule (§6.2); Exhibit A settles beside № 001; the
   ruler's hand leaves T+0 and its digits begin flipping;
   the strip clips on as the masthead leaves.
4. **№ 003–004 — the room settles, then the correction.**
   № 003 writes plainly (eleven GO). № 004 performs §6.4:
   the wrong word, the half-second, the pencil, the carbon
   correction — the page's stillest two seconds, and its
   most remembered (§8.2). The coffee ring in the margin has
   been there since first paint.
5. **№ 005 — rendezvous.** The entry writes; Exhibit B
   settles; the route (§6.6) is not here — but the ruler's
   tick spacing teaches the mission's shape: the ticks crowd
   early, then the long quiet begins.
6. **№ 006–008 — the long orbit.** Writes grow familiar; the
   ghost (§6.5) drifts one line behind whichever entry holds
   the rule; № 007's burn entry is the shortest write on the
   sheet. The ink rule (§6.10) fills and hands over, entry by
   entry.
7. **№ 009 — the lost signal.** The entry writes at the same
   pace as every other — the log does not dramatise — and
   its stamp, if the reader signs it, reads REACQUIRED
   (§6.7). Second coffee ring in the margin.
8. **№ 010–011 — the return.** Checklist and burn; the
   ruler's hand is visibly nearing the total; the strip's
   phase reads RETURN.
9. **№ 012 — splashdown.** The last entry writes; Exhibit C
   settles; the hand reaches the final tick with its 40ms
   jump (§6.3).
10. **The request entry (§8.3).** № 088 offered, ghost laid
    on focus, FILED stamped on success — or read past; the
    log does not require the visitor's paperwork.
11. **The sign-off (§6.16).** Totals for the third time; the
    director's initials; the strip prints `LOG CLOSED`;
    the colophon's claim — *no entry was erased* — now has
    twelve entries of evidence behind it.
12. **Reverse pass.** Scrolling back up: nothing un-writes,
    un-stamps or un-corrects. The ruler's hand retreats
    within spans but its carbon furthest-marker holds; the
    ink rule alone drains and refills, because it records
    reading, not history. The sheet reads the same backwards
    because it is a record, and the visitor feels the
    difference between a page and a document.

## 14. Whole-page performance budget

| Budget line | Limit | Notes |
|---|---|---|
| Total page weight (home) | ≤ 720KB | Fonts are the floor: two families, subset, ≤ 150KB total |
| Photography | ≤ 140KB each, exactly 3 on home | WebP, exhibit-sized, lazy below the fold (§6.9) |
| JS (theme system) | ≤ 38KB gz | One loop, one record, no framework in the theme layer |
| CSS | ≤ 30KB gz | Ruling, stamps and the single `--stamp` rule set included |
| Frame budget (shared loop) | ≤ 1.2ms/frame | Ruler, ghost, ink rule, route, one exhibit settle, one card tilt — measured in the gate's drill |
| Long tasks | none > 50ms | The record renders at build; runtime never parses the log |
| Layout shift | CLS ≤ 0.02 | Entries reserve their ruled lines (§6.15); mono tabular figures mean counting never reflows |
| Time to readable | first paint, JS or not | Content ships complete; JS arms the acts over the printed log |

**Cut order when the budget is exceeded** (in order, never
skip ahead): 1) the carbon ghost on mid-tier devices (§6.5 —
it is already cut on mobile); 2) exhibit sheen parallax
(photos keep their settle); 3) carriage snap-proximity
(§5); 4) the paper feed on repeat visits within the hour
(the sheet is simply there); 5) card tilt above the fold
only. **Never cut:** the printed completeness, the
watchdogs, the correction and its legibility, the dual
timestamps, the record's precision, the reduced-motion
variants, the form's kept-words failure state. A plainer
sheet is legal; a rounded, erased or stranding one is not.

## 15. Build-order checklist

1. **The record first.** Author and validate the Mission
   Record (§6.17): twelve entries, GMT = launch + T+ per row,
   totals derived, one correction, three exhibits, request
   count 87. No design work precedes the data — the page is
   the record's printout.
2. **Static printed sheet.** Build the complete page with no
   JS: headline typed and stamped, every entry written with
   the correction visible, index, ruler's static form,
   exhibits, table, form posting to its endpoint, footer
   reconciled. This is the fallback and it must already be
   good.
3. **Typography and tokens.** Load the two faces subset; set
   §3's laws and §2's tokens; grep the CSS to confirm the
   stamp token appears only inside `.stamp` rules.
4. **The ruling and anatomy.** §4's line grid, margin column,
   entry anatomy, the two coffee rings at their recorded
   positions.
5. **The shared loop.** rAF + lerp 0.11 + phase clock +
   watchdog registry; register nothing yet.
6. **Entry writes.** §6.2's centre-rule sequence with its
   observer and scroll-listener backup; the jump-scroll and
   focus rules wired.
7. **Headline and stamp.** §6.1's typing with its per-
   character watchdog; §6.7's stamp system and session store.
8. **The correction.** §6.4: stroke path, interlinear band,
   once-only latch; verify the strike census by hand.
9. **Instruments.** §6.3's ruler (ticks derived from the
   record), §6.10's ink rule, §6.11's strip and index
   current-row marking.
10. **Ghost and route.** §6.5's single ghost (DOM-generated,
    never a second copy in markup), §6.6's route with
    waypoint fractions from the record.
11. **Exhibits and cards.** §6.9's taped figures at ruled
    heights; §6.12's cards on listing pages; reconcile the
    counts (3 exhibits, 12 of everything else).
12. **Table and footer.** §6.13 and §6.16 printings from the
    record; reconcile the three totals printings digit-for-
    digit.
13. **The form.** §6.14's numbering from the record,
    idempotency, carbon corrections, kept-words failure
    state, server-rendered confirmation.
14. **Loader, transition, 404.** §6.15's ceilings, §6.18's
    index-carrying 404.
15. **Reduced-motion pass and the gate.** Every element's
    variant verified with the OS setting on; then §10's
    twelve checks, signed by a non-builder. Only then may
    the theme be used in a build.
