# 80. The Ephemeris Press — Expanded (v1 + v2)

**Identity (preserved exactly from the original entry).** A letterpress print
shop that publishes the sky — daily astronomical tables set in metal type and
printed on a treadle press. The site feels typeset, inked and pulled by hand:
computation as craft. Palette: Pressroom cream `#F4EEE1` · type ink `#23211D`
· proof red `#B23A2E` · forme steel `#5A6068` · gold size `#B98A2F`.
Typography: Playfair Display (display) + EB Garamond (body), with letterpress
bite on display type. Every section is a *forme* — a locked chase of type
with visible furniture in the margins and registration marks at its corners.
The colophon is a full final forme printing the day's real sunrise and
moonrise times.

**The theme's one law.** *Nothing on this page is displayed — it is printed,
and a print can be checked.* Every element is type first and interface
second: figures are set, sections are locked, feedback is an impression.
And every number printed anywhere on the page traces to one declared record
— the Day's Forme (§6.17), the press's computed table for the date — so a
visitor with an almanac can verify the whole page from the one record, the
way a proofreader verifies a sheet against the copy.

**How to read this spec.** §1–§5 define the world, tokens, type, layout and
the motion system as a whole. §6 gives all 18 elements (the 9 original
signature elements, deepened not redesigned, plus 9 page-family elements)
with full v1 fields and v2 layers each (the ninth original element, the
honest colophon, is specified as §6.18's closing note, where it closes
every page). §7–§15 give the page map, three
worked examples, anti-slop, the quality gate, the component inventory, the
copywriting voice, the scroll choreography map, the performance budget and
the build order. Worked figures throughout use the press's example day —
**Tuesday 14 April 2026** — and reconcile everywhere they are printed.

---

## 1. Concept & world

The Ephemeris Press is a working print shop whose product is the sky. Each
morning the press computes the day's astronomical table — sunrise, solar
transit, sunset, moonrise, moonset, the moon's illumination, the evening
planet — sets it in metal type, locks it into a chase, and pulls the day's
sheet. The website is that sheet, and the day's page is quite literally the
day's forme: it is composed at the top (the headline set sort by sort),
printed down its length (each section locked into the chase as the reader
reaches it), and signed at the foot by an honest colophon that names the
typefaces, credits the hand-setting, and prints the reader's own hemisphere
times.

The world is material and specific. Type lives in a California job case —
a shallow tray of compartments, capitals in the small boxes at the top,
lowercase in the large ones below. The compositor works with a composing
stick in the left hand, setting type upside down and backwards, justifying
each line with thin spaces. A forme is the locked page of type: type,
furniture (the wood blocks that fill the empty space and hold everything
under pressure), quoins (the wedges that lock it), all inside the steel
chase. A proof is a trial pull, marked up in red pencil by the proofreader.
The treadle press rocks on its flywheel all day; the pressman pulls a proof,
checks it against the copy, corrects, and prints the run. Ink is not a
colour here, it is a substance: it squashes under pressure, it sheens when
fresh, it misregisters by a hair when the sheet shifts.

**Best-fit sites.** Publishers of daily or periodic reference matter
(almanacs, tide and ephemeris services, observatory public pages); type
designers and letterpress studios showing craft as process; heritage craft
brands whose making is slow, manual and verifiable; journals and newsletters
whose identity is "set by hand, checked twice". The theme is at its best
when the site's content genuinely is a daily computed table — the theme's
central promise (every figure traceable to one record) is a feature only
when the figures are real.

**When NOT to use it.** Not for real-time data that changes by the second
(the press prints once a day; live tickers break the world). Not for
checkout or payment flows — commerce is routed out of the theme (§7), the
way the press takes orders on a printed slip rather than at the press bed.
Not for content that must feel instant, weightless or futuristic: this
theme's whole value is resistance, weight and dwell. Not for image-led
portfolios — the press prints type and the occasional ruled diagram; a
photograph has to be admitted as a pasted-in plate (§11) and the theme
rations those. And not when the client cannot supply real figures: an
Ephemeris Press page with invented times is a forgery, and §9 names it one.

**The press's characters.** Two voices share the page (§12): the
*Compositor*, who sets and labels (measured, tabular, never lyrical), and
the *Pressman*, who speaks in the colophon, the errata slip and the margins
(dry, plain, admits faults). Neither is a mascot; both are trades.

**The one dishonesty the theme refuses.** Decorative astronomy. A crescent
moon icon that does not match the printed illumination, a sunrise time that
differs between the hero and the colophon, a "daily" table that is actually
static — each is a misprint, and §10's gate treats them as blocking faults,
not embellishments.

---

## 2. Palette

Five anchors from the original entry, plus six derived tokens. Every ratio
below was computed from the hex values for this expansion; the rulings are
part of the theme, not advice.

| Token | Hex | Role | Ratio & ruling |
|---|---|---|---|
| `--cream` | `#F4EEE1` | Pressroom cream — the sheet itself; page ground, forme interiors | ~76% of any viewport. The paper everything is printed on |
| `--ink` | `#23211D` | Type ink — all body text, display type, rules, the type itself | On cream **13.8:1** — the page's workhorse pairing |
| `--proof` | `#B23A2E` | Proof red — corrections, the errata slip, one licensed accent per forme | On cream **5.1:1** — passes AA for text; still rationed (§9), because a proof covered in red is a proof that failed |
| `--steel` | `#5A6068` | Forme steel — chase frames, furniture shadows, secondary labels, table rules | On cream **5.4:1** — AA for text; the colour of the apparatus, never of the message |
| `--gold` | `#B98A2F` | Gold size — the solar arc's fill, the sun disc, gilded initials | On cream **2.7:1** — **never text on cream**; on ink **5.1:1**, the one licensed gold lettering (colophon band, case labels on dark wood) |
| `--paper-shadow` | `#E6DCC4` | Derived — cream in shadow: forme edges, the case tray's inner walls, skeleton paper | Decoration only; text on it uses `--ink` (11.9:1) |
| `--ink-70` | `#23211D` @70% | Derived — Garamond captions, figure labels, furniture grain lines | On cream ≈6.9:1 effective; captions and labels only, never body |
| `--ink-40` | `#23211D` @40% | Derived — hairline rules inside tables, registration-mark ghosts | Never text; rules and marks only |
| `--furniture` | `#B49B72` | Derived — the wood of the furniture blocks (a lightened tint of gold size, as beech is a lightened walnut) | Blocks and margin wood only; its grain is drawn in `--ink-40` |
| `--gold-deep` | `#8F6B24` | Derived — gold under pressure: the arc's already-travelled portion at its leading edge, the sun disc's rim | Decoration only |
| `--proof-pale` | `#B23A2E` @12% | Derived — the wash behind a corrected line, the errata slip's ground tint | Grounds only; text on it is `--ink` or full `--proof` |

**Pairing law.** Text is ink on cream, full stop — with exactly three
exceptions: proof red for corrections and the errata voice (5.1:1, AA),
steel for apparatus labels (5.4:1, AA), and gold on ink inside the colophon
band and on the dark case tray (5.1:1). Gold on cream is a misprint wherever
it letters; §10 greps for it.

**Dark-mode behaviour.** There is none, by ruling. A print shop's sheet does
not invert at night; the page is the paper. What the theme offers instead is
the *evening pull*: nothing. The ruling is stated plainly so no builder
invents a night scheme — the press prints one sheet, in one light. (A
reader's OS dark mode leaves the page untouched; the sheet is the sheet.)

**Usage ratios per viewport.** Cream ~76%, ink ~14% (type, rules, the case),
steel ~5% (chases, apparatus), furniture ~3% (margins), gold ~1.5% (the arc,
one initial), proof red ~0.5% (corrections only — a viewport with more red
than that is a page failing its proof, §9).

---

## 3. Typography

Two families, as the original entry rules — Playfair Display and EB
Garamond. No third family is admitted; tabular data is set in EB Garamond
with `font-variant-numeric: tabular-nums lining-nums`, because a printer's
figures are lining figures in a ruled table, and importing a mono font
would be importing another shop's type.

**The scale** (root 16px; Garamond runs small, so body is set larger than
web habit):

| Role | Font | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Display (headline) | Playfair Display 700 | 64px / 1.04 | −0.01em | Set sort by sort in the hero (§6.1); letterpress bite always on |
| Forme title (H2) | Playfair Display 600 | 38px / 1.12 | 0 | The title of each forme, set at its head like a running title |
| Subhead (H3) | Playfair Display 600 | 26px / 1.2 | 0 | Within-forme divisions |
| Body | EB Garamond 400 | 19px / 1.55 | 0 | The reading text; measure 34–38em |
| Body emphasis | EB Garamond 500 italic | 19px / 1.55 | 0 | Italic is the press's emphasis — there is no bold in body text |
| Caption / label | EB Garamond 500 | 13.5px / 1.4 | 0.08em, uppercase | Compositor's labels: figure names, case labels, table heads |
| Data figure | EB Garamond 500 | 22px / 1.2 | 0 | Tabular lining figures; the times themselves |
| Colophon | EB Garamond 400 italic | 16.5px / 1.5 | 0 | The Pressman's voice (§12) |

**Five type laws.**

1. **The bite is structural, not a filter.** Display type carries the
   letterpress bite — `text-shadow: 0 1px 0 rgba(244,238,225,.55), 0 -1px
   1px rgba(35,33,29,.22)` — the highlight of the paper showing below the
   impression and the ink's squash above it. It is applied to Playfair at
   ≥26px only; at body sizes the bite would be dirt, and the press does not
   print dirt.
2. **Figures are set, never kerned by eye.** All times and counts use
   tabular lining figures and are right-aligned in tables to the colon;
   a figure that wobbles horizontally between rows is a loose sort (§9).
3. **Garamond italic is the only emphasis in body text.** Bold body text
   does not exist in this shop's case; a builder reaching for `<strong>`
   in a paragraph gets the compositor's italic instead. (Strong is
   permitted inside table heads and labels, set in caps.)
4. **The headline is furniture-complete.** The hero headline is set from
   real sort elements (§6.1) — its text is in the DOM as ordinary text
   first; the sorts are an enhancement laid over a set line, never the
   only copy.
5. **Red is a pencil, not a typeface.** Proof red never sets a headline or
   a paragraph; it corrects, annotates and signs. A red headline is a
   proofreader who has taken over the shop (§9).

**Fallbacks.** Playfair Display → `Didot, "Bodoni MT", Georgia, serif`;
EB Garamond → `Georgia, "Times New Roman", serif`. The fallback stack is
a respectable book face, not a sans — a page waiting for its fonts still
looks printed, merely by another printer.

---

## 4. Layout language

**The page is a chase.** The whole page sits inside one great steel chase —
a `--steel` frame, 2px, inset 14px from the viewport edges on desktop —
and each section is a **forme** locked inside it: a block of set matter
with its own hairline rule head, registration marks at its four corners
(12px crosshair-and-circle marks in `--ink-40`, printed, never animated
except at the lock, §6.3), and furniture visible in its margins.

**Grid.** A 12-column grid inside the chase, column gap 24px, but the
theme's true structure is the forme's internal measure: body formes set
their text in a centred 7-column measure (34–38em of Garamond); the day's
table forme (§6.9) uses the full 12; the margins between forme edge and
chase — 1 column each side on desktop — are where the furniture lives
(§6.4) and where the solar arc runs (§6.7). Whitespace in this theme is
not empty: it is *furniture*, wood that exists to hold the type under
pressure, and it is drawn as such.

**Spacing rhythm.** A 8px base unit, but formes breathe in press units:
forme padding 48px top / 40px bottom on desktop; the gap between formes
is one furniture course — 32px of visible margin wood and shadow — so the
reader feels each section as a separate locked block, not a continuous
scroll of cards. Within a forme, vertical rhythm follows the 19px/1.55
body line: all internal spacing is a multiple of the 29.45px line (rounded
to the 8px grid at build time, per forme, and held constant down the page).

**Density rules.** One forme, one subject: a forme that needs a second
headline is two formes. Maximum one data table per forme. Maximum one red
element per forme (the proofing ration, §2). The hero forme is the only
one permitted to fill the first viewport entirely; all others size to
their matter — a short forme is short, and its furniture course below is
taller, which is how the press fills a chase honestly rather than
stretching type to fit a template.

**The reading line.** Reveals, locks and figure-settings key to a reading
line at 62% of viewport height — the line where the pressman's eye rests
on the proof. Anything scrubbed (§6.4, §6.7) is scrubbed against the
forme's own travel across that line, never against raw document height.

**Breakpoints in the layout.** ≥1200px: as above, furniture margins both
sides. 768–1199px: the chase inset shrinks to 8px, furniture margins
collapse to the left side only (the arc keeps the right margin, §6.7),
body measure widens to 9 columns. <768px: the chase becomes a single
hairline frame at 6px inset; furniture is drawn as a single top course
per forme instead of side margins; formes stack full-width; the arc moves
to a horizontal band at the foot of the hero (§6.7).

---

## 5. Full motion system

Motion in this shop is the press's own physics: things are *set* (placed
with a snap), *locked* (driven home with a clunk), *pulled* (drawn off the
forme in one steady peel), and *impressed* (pressed down, squashing ink).
Nothing floats, bounces or springs like a toy; metal and wood do not
bounce. Every motion term from the standard list is either given its press
form below or refused with its reason.

**Named easings** (the only curves in the theme; tokens in §6 elements):

| Token | Curve | Used for |
|---|---|---|
| `--ease-clunk` | `cubic-bezier(.76,0,.24,1)` + a 16ms settle frame | Formes locking (§6.3): fast travel for ~70% of duration, hard stop, one frame of settle |
| `--ease-set` | `cubic-bezier(.2,.9,.25,1.12)` | Sorts landing (§6.1), figures setting (§6.6): a slight overshoot that reads as ink-squash, never as bounce |
| `--ease-peel` | `cubic-bezier(.6,.05,.2,1)` | The proof pull (§6.2) and re-proof transition (§6.15): slow, steady, one direction |
| `--ease-treadle` | `cubic-bezier(.45,0,.55,1)` (sine in-out) | The treadle rock (§6.5), ink-sheen breathing: the flywheel's own curve |
| `--ease-snap` | `cubic-bezier(.9,0,.1,1)` | The stick rule's snap (§6.11), stamp landings: near-instant with a hard end |

**The shared loop.** All scroll-scrubbed values — furniture packing (§6.4),
the solar arc (§6.7), the stick rule (§6.11), the peel's scroll variant —
are driven by **one** `requestAnimationFrame` loop lerping a single
scroll-progress value per forme at **0.12** (heavy enough to feel like
paper moving on a bed, light enough to track). No element runs its own
scroll listener; §14 budgets the loop at ≤1.2ms/frame. Discrete animations
(setting, locking, impressions) are CSS transitions/keyframes fired by an
IntersectionObserver at the reading line — they are events, not scrubs.

**Term by term.**

- *Scroll-triggered reveals* — formes lock (§6.3); figures set (§6.6);
  corrections draw (§6.13). All fire once, at the reading line, and stay
  printed: scrolling back up never un-prints a page.
- *Scroll-driven / scrubbed* — furniture packing, solar arc, stick rule,
  via the shared loop only.
- *Parallax* — refused in its web form (layers drifting at different
  speeds is the opposite of a locked forme, where everything moves as
  one locked block or not at all). The theme's single depth effect is the
  proof peel (§6.2), where two states of one object separate.
- *Pinned sections* — one pin is licensed: the stick rule (§6.11) pins
  beneath the active forme. No section pins its content; a forme is read
  by travelling through it, as a sheet is read.
- *Smooth scrolling* — the browser's own; the theme adds no scroll
  hijack. The clunk is in the formes, not in the reader's hand.
- *Progress indicator* — the solar arc (§6.7) and nothing else; a
  percentage or a thin top bar would be a foreign instrument on the page.
- *Staggered reveals* — sorts at 45ms (§6.1); table rows set line by line
  at 30ms (§6.9). Stagger is a compositor setting a line, never confetti.
- *Masked reveals* — the peel (§6.2) is the theme's mask; line-mask text
  reveals are refused (a line of type is revealed by being set, §6.1).
- *Kinetic typography* — rationed to the headline's setting and the
  figures' snap. Playfair never slides, splits or waves; display type in
  this shop is heavy and stays where it was set.
- *Marquee* — refused. A print shop has no ticker; the day's figures are
  set once, in the table, where they can be checked.
- *Counters* — figures that set (§6.6): count fast in tabular figures,
  then each digit snaps 1px and darkens — the count is the compositor
  rough-counting, the snap is the sort going home.
- *SVG line-draw* — the solar arc (§6.7) and the proofreader's drawn
  corrections (§6.13) only; both are drawn by a hand or by the sun, not
  by a chart library.
- *Image scale-in-frame* — plates (the rationed images, §11) are admitted
  under a printed plate mark and do not scale; a photograph clipped into
  a book does not breathe. Refused.
- *Hover / magnetic / tilt* — hover lifts a sort 2px and darkens its ink
  (§6.10, §6.1 sorts). Magnetic pull and tilt are refused: type in a
  chase does not lean toward the reader's hand.
- *Custom cursor* — refused; normal system cursor, as the standing rules
  require. The pressman's tools are on the page, not on the pointer.
- *Skeleton loading* — un-inked standing type (§6.16).
- *Page transitions* — the re-proof (§6.15).
- *Reduced motion* — the day's paper, fully printed and still: every
  element ships its printed state; setting, locking, peeling and rocking
  are all enhancement (§6, per element).

**Ambient loops.** Exactly two are licensed: the treadle rock (§6.5) and
the ink sheen breathing on set display type (a 6s `--ease-treadle` cycle
moving a highlight across the bite's shadow by 1px — fresh ink settling).
Both pause when the tab is hidden, and the treadle pauses while the
reader interacts with a forme — the pressman stops the press to talk.

**Master timing table** (details per element in §6): sort stagger 45ms;
sort travel 380ms; peel 1200ms; forme lock 520ms (travel ~365ms, stop,
16ms settle, then registration settle 90ms); figure count 600ms + snap
60ms; furniture re-pack scrubbed; arc scrubbed; impression 120ms down,
180ms recover; treadle period 3200ms; stick-rule snap 140ms.

---

## 6. Signature elements

### 6.1 Live typesetting of the headline

**What & why.** The hero headline is manufactured in front of the reader:
individual sorts — letters in metal-type blocks — slide out of a type-case
grid at the hero's left edge into a composing stick, one by one, and the
line sets itself. It is the shop's craft performed as the hero, and it
makes the theme's promise before a word is read: this page was *made*, by
hand, just now. The original entry's first element, deepened.

**Structure.** The headline exists in the DOM as a plain `<h1>` in
Playfair Display. On enhancement, JS wraps each grapheme in a sort: a
`<span class="sort">` rendered as a type block — the letter reversed-out
of an ink-dark face (the sort's face shows the letter mirror-wise in the
metal, a detail drawn with a subtle inset), body of the block in
`--steel`-shadowed ink. The type case is a grid of shallow compartments
drawn at the hero's left (desktop) holding the unused sorts of the same
fount. The composing stick is a ruled channel beneath the headline line
into which the sorts travel.

**Motion spec.** Per sort: travel 380ms `--ease-set` from its case
compartment to its stick position, staggered 45ms per sort, reading order.
Landing: ink-squash — scale 1.04→1 over 90ms with a 1px blur settle
(blur 1.5px→0 across the same 90ms) and the face's ink darkening from
`--ink-70` to full `--ink`. Spaces travel as blank sorts (a sort with no
letter — the space is a physical thing in this shop, lower than type
height, drawn as a shorter block). A 24-sort headline completes in
24×45 + 380 ≈ 1.46s.

**Choreography timeline.** t=0 hero forme is already locked and printed
(the fallback state) → JS arms: sorts begin at their case positions,
headline line shows the stick empty → t=120 first sort travels → sorts
land in stagger, each with its squash → last sort lands ≈ t=1.46s →
t=+120ms the stick rule snaps beneath the line (§6.11's rule, in its hero
position) → t=+300ms the proof pull (§6.2) begins. If the reader scrolls
before completion, remaining sorts set instantly (no stranded half-line).

**State matrix.** *Rest (no JS / pre-arm):* headline printed as ordinary
type, bite applied — complete. *Setting:* as timeline. *Hover (a landed
sort):* lifts 2px, face ink darkens a further step, 120ms — the
compositor's finger testing a sort. *Focus:* the headline is a heading,
not a control; sorts are `aria-hidden` duplicates of the real text (see
Accessibility). *Scrolled-past:* stays set; never re-runs within a
session (`press.headlineSet` flag). *Disabled:* n/a. *Touch:* identical;
no hover lift.

**Breakpoints.** ≥1200px: case at the hero's left, 5 columns of
compartments, sorts at full 64px display size. 768–1199px: case becomes a
single row beneath the stick; sort travel distance shortens, stagger
holds at 45ms. <768px: headline caps at 40px; the case is not drawn —
sorts travel from the forme's top edge (from "the case off-screen"),
stagger tightens to 30ms so the line sets inside ~1.1s; squash retained
(it is the point), blur settle dropped (mobile GPUs smear it).

**Edge cases & failure modes.** Long headline (>34 sorts): the stagger
compresses to `max(18ms, 1420/N)` for N sorts so total setting stays ≤1.8s — the
compositor hurries, he does not dawdle. Font not yet loaded: sorts render
in the Georgia fallback and swap when Playfair arrives; travel paths are
computed after `document.fonts.ready` or at 300ms, whichever is first, so
a late font never re-flows a travelling sort. Tab hidden mid-set: the
timeline is timestamp-driven and completes silently. Reader scrolls
during setting: instant-complete (above). RTL languages: sorts travel
from the right case; the shop sets Arabic in the same stick, mirrored.

**Accessibility.** The real `<h1>` text is the accessible headline; the
sort layer is `aria-hidden="true"` and the plain text is visually
replaced only while the sort layer is present and complete. Screen
readers never meet a letter-by-letter headline. The setting is announced
nowhere (it is decoration over available content). Focus is never moved.
Bite contrast: the headline is `--ink` on `--cream`, 13.8:1, at every
frame of the squash (the darkening runs from 6.9:1-equivalent upward —
never below AA at any instant).

**Tokens.** `--ink`, `--ink-70`, `--cream`, `--steel`, `--ease-set`,
`--sort-stagger` (45ms), `--sort-travel` (380ms).

**Content-merge.** The sorts are the headline's own letters and the case
holds the headline's own fount — change the headline and the case
re-fills. On the day's page, the headline is the date line itself ("The
Sky for Tuesday the Fourteenth of April"), so the first thing the shop
sets is the day it is printing.

**Failure fallback & watchdog.** A 2,000ms watchdog from first paint: if
the setting has not completed (rAF stalled, JS error mid-run), all sorts
snap to their set positions and the stick shows the finished line. Because
the DOM ships printed, every failure ends with the headline simply *set*.

**Reduced motion.** No setting: the headline stands printed with its
bite; the case is drawn as a still plate beside it (the shop at rest,
case open). The stick rule is present beneath the line from the start.

**Performance & mobile.** Sort layer: one span per grapheme, transforms
only, no layout thrash (positions pre-computed as transforms from a
single measurement pass). Budget: ≤0.4ms/frame during setting. Mobile:
as breakpoints — no blur, tighter stagger, case undrawn.

### 6.2 The proof-pull peel reveal

**What & why.** After the headline sets, a proof is pulled: a vertical
peel mask lifts over the hero forme's impression block — the day's key
figures panel — revealing the printed impression beneath the set type.
Set type and printed page are shown as two states of one object, which is
the press's whole metaphysics in one gesture: the page the reader reads
was *pulled* from the type the reader just watched being set.

**Structure.** Two stacked layers of the same block: beneath, the printed
impression (the figures panel, fully rendered); above, the "forme side" —
the same panel drawn as set type (figures reversed, in steel and ink-70,
as if seen in the forme). A `clip-path: inset()` peel edge, drawn as a
soft 24px gradient band (the paper's leading edge, slightly curled via a
gradient shadow), wipes the top layer away top-to-bottom. Both layers are
in the DOM; the top layer is `aria-hidden`.

**Motion spec.** Peel duration 1,200ms `--ease-peel`, top to bottom,
beginning 300ms after the headline's last sort lands (§6.1). The peel
edge's shadow deepens at mid-travel (the sheet lifting off the forme)
and releases at the end. On completion the forme-side layer is removed
from the DOM, not hidden.

**Choreography timeline.** t=0 (headline set) → t=300 peel begins →
t=600 edge at mid-panel, shadow deepest → t=1,200 peel completes, layer
removed → t=1,260 the revealed figures set (§6.6) as the reader's eye
lands on them. Total hero ceremony ≈ 3.5s from first paint with the
worked day's 43-sort date line (§8.1) — long, and
deliberately: this is the shop's front door, and §6.15's re-proof keeps
interior transitions to 450ms so the ceremony is paid once.

**State matrix.** *Rest:* impression visible, forme-side absent (the
no-JS state). *Peeling:* as timeline. *Interrupted (scroll):* peel
completes instantly — a proof half-pulled is a proof spoiled, so the
theme never leaves one hanging. *Scrolled-past:* done, layer gone.
*Focus/disabled:* n/a (not a control). *Touch:* identical.

**Breakpoints.** ≥1200px: peel over the full figures panel (7-column
measure). 768–1199px: same, panel narrows with the measure. <768px: the
peel shortens to 800ms and the forme-side layer is simplified (figures
only, no reversed-letter drawing) — the gesture survives, the engraving
doesn't.

**Edge cases & failure modes.** Slow device: the peel is one clip-path
animation on one layer — if frame time exceeds 24ms sustained, the peel
steps to a 3-frame crossfade of the same two layers (the proof is still
pulled, just on a tired press). Print stylesheet: only the impression
prints (the forme-side is `display:none` in print — you cannot print a
peel). Repeat visit in session: peel suppressed, hero arrives printed
(the reader has seen the shop work; the paper is on the table).

**Accessibility.** Both layers carry identical content; the forme-side is
`aria-hidden`, the impression is the accessible copy throughout — a
screen reader reads the figures once, unpeeled. The peel never covers
content that isn't simultaneously present beneath it in the a11y tree.
No focus interaction. Contrast of the impression: ink on cream, 13.8:1.

**Tokens.** `--cream`, `--ink`, `--ink-70`, `--steel`, `--ease-peel`,
`--peel-duration` (1200ms).

**Content-merge.** The block peeled is the day's own key figures (sunrise,
transit, sunset, moonrise — §6.17), not a decorative panel: the reveal
*is* the day's data being published. A page without figures (the about
page) peels its first forme's opening block instead (§7).

**Failure fallback & watchdog.** A 2,600ms watchdog removes the
forme-side layer unconditionally if the peel stalls. The impression is
beneath it the whole time — failure looks like the proof already pulled.

**Reduced motion.** No peel: the impression stands printed; the forme
side is never inserted. (A still plate of the forme may appear in the
about forme, as a picture of the shop's type — a photograph of work, not
a performance of it.)

**Performance & mobile.** One composited layer, clip-path only; ≤0.5ms/
frame. Mobile: 800ms, simplified top layer (above), no curl shadow
gradient (a flat 8px band instead).

### 6.3 Clunk-locking formes

**What & why.** Every section enters the page the way a forme enters the
chase: it travels fast, stops hard, and settles for one frame. Sections
do not "appear" — they are locked in, and the reader feels the page being
*built under pressure* as they read down it. This is the theme's
scroll-reveal, and its easing is a fingerprint: once felt, the clunk is
recognisable on any page in the theme.

**Structure.** Each `<section class="forme">` carries its chase hairline,
corner registration marks (inline SVG, 12px, `--ink-40`), and content set
complete in the DOM. Enhancement adds `data-armed` and a transform start
position: translateY(26px) + a 0.3° rotation (a forme carried slightly
askew, as a man carries it). The marks are two-part: a fixed circle in
the chase (the target) and the forme's crosshair, which must land inside
it.

**Motion spec.** On crossing the reading line: travel 520ms total —
translate/rotate to zero over ~365ms on `--ease-clunk` (70% of the curve
covers 92% of the distance), hard stop, one 16ms settle frame (a 1px
overshoot down and back — the quoins driving home), then the registration
marks settle over 90ms as the crosshair centres in its circle and both
ink from `--ink-40` to `--ink-70`. A forme already past the line on load
(the hero, formes above the fold) arrives locked, marks already inked.

**Choreography timeline.** Trigger (forme's head crosses reading line) →
t=0 travel begins → t=365 hard stop → t=381 settle frame done → t=390
marks begin inking → t=480 marks inked; the forme's figures, if any,
begin setting (§6.6) → t=520 forme at rest, `data-locked`. Scrolling back
up: nothing reverses; a locked forme stays locked (type does not unlock
because the reader looked away).

**State matrix.** *Rest (no JS):* forme printed in place, marks at
`--ink-40` (the printed state — marks are printed furniture, faint by
design). *Armed:* translated 26px, opacity unchanged (the forme is
solid; it never fades — a fade would be a ghost, and this shop prints
solids). *Locking:* as timeline. *Locked:* rest state, marks inked.
*Hover:* none (a forme is not a control; its inner controls have their
own states). *Scrolled-past:* locked. *Touch:* identical.

**Breakpoints.** ≥1200px: full travel 26px + 0.3°. 768–1199px: travel
20px, rotation 0.2°. <768px: travel 14px, no rotation (a small forme is
carried in both hands, level), settle frame retained — the clunk's stop
is the signature, the rotation is garnish.

**Edge cases & failure modes.** Very tall forme (>2 viewports): locks
when its *head* crosses the line — the reader never waits for a long
forme's foot. Very short forme: locks identically; brevity is not
exempted from the ceremony. Rapid scroll: formes crossed between frames
lock instantly in sequence (stagger 40ms) rather than animating late
beneath the reader — the press catches up by printing, not by panting.
Content re-flow after lock (late image): the forme's marks stay aligned
to its corners because they are positioned to the forme, not the page.

**Accessibility.** The lock is transform-only over fully present content;
reading order is DOM order at all times. Screen readers are unaffected.
The motion is brief, non-repetitive and below vestibular concern; the
reduced-motion variant removes it entirely. Marks are decorative
(`aria-hidden`), their inking announced nowhere.

**Tokens.** `--steel`, `--ink-40`, `--ink-70`, `--ease-clunk`,
`--lock-travel` (26px), `--lock-duration` (520ms).

**Content-merge.** The lock is not decoration around the section — the
section *is* a forme, and locking is what makes it one. The registration
marks are shared across all formes on a page (one grid, §4), so each
lock visibly enrols the section into the page's single chase.

**Failure fallback & watchdog.** Each armed forme carries a 1,500ms
watchdog from arming: if its lock has not run (observer failure, rAF
stall), the transform is removed and the forme stands printed. The armed
state is JS-applied only; no-JS pages never arm.

**Reduced motion.** No travel, no settle: formes stand printed, marks at
their printed `--ink-40`. The page reads as the finished sheet — which
is the correct reduced form of a newspaper, not a diminished one.

**Performance & mobile.** One transform per forme, fired once; zero
per-frame cost after lock. Mobile: reduced travel (above), same
watchdog.

---

### 6.4 Adjusting furniture blocks

**What & why.** The margins of each forme are filled with furniture —
wood spacing blocks that hold the type under pressure. As a forme
settles, its furniture visibly re-packs: blocks shuffle by a few pixels,
rotate by fractions, and wedge home. The page's negative space is shown
being *made*, in the trade's own material — the only theme in the library
whose margins are a performed craft rather than an absence.

**Structure.** Each forme's margin carries 4–9 furniture blocks: `<div
class="furn">` rectangles in `--furniture` with grain drawn in
`--ink-40` (two or three hairlines per block, CSS gradients), sized in
the press's real furniture proportions (multiples of 12px wide, heights
in pica steps). Blocks are absolutely positioned in the margin column;
their packed positions are their DOM/rest positions. Enhancement offsets
each block by a seeded 3–7px and a 0.4–1.1° rotation (seeded per forme
from its index, so the pack is deterministic and identical for every
builder).

**Motion spec.** Scrubbed, not fired: as the forme travels across the
reading line, the shared loop (§5) lerps a per-forme settle value `s`
from 0→1 across the forme's first 60vh of travel; each block's offset
scales by `(1−s)`. At `s=1` the blocks are home and the forme's lock
(§6.3) fires its settle frame — the two motions are one event seen from
the margin and from the type. No easing curve: the lerp *is* the curve.

**Choreography timeline.** Forme head enters viewport foot → `s` begins
→ blocks drift home over the forme's travel → forme head crosses reading
line → §6.3 lock fires, blocks take their final 1px wedge (a last
translate toward the type, the quoin pressure) → `s=1`, blocks leave the
loop's active set. Scrolling up: `s` does not decrease — packed
furniture is not unpacked by a reader changing their mind.

**State matrix.** *Rest:* blocks packed (the printed state — margins
look like margins). *Settling:* offsets shrinking with scroll. *Packed:*
rest. *Hover:* none. *Focus:* none (decorative). *Scrolled-past:*
packed. *Touch:* identical (scroll-driven, not gesture-driven).

**Breakpoints.** ≥1200px: furniture in both margins, 4–9 blocks per
forme. 768–1199px: left margin only, 3–5 blocks; the right margin is the
arc's (§6.7). <768px: side furniture is cut; one horizontal furniture
course is drawn at each forme's head (3 blocks in a row) and packs
vertically by the same `s` value — the material survives, the margin
doesn't.

**Edge cases & failure modes.** Short forme: its `s` travel compresses to
its own height — the pack still completes by its foot. Forme taller than
2 viewports: `s` completes across the first 60vh regardless (above).
Margin too narrow after a late font swap: blocks are positioned from the
forme's box, measured once at arm time and once on resize (debounced
200ms); a resize mid-scroll re-derives offsets without a visible jump
because `(1−s)` multiplies the new offsets too. No-canvas/WebGL: the
blocks are pure CSS — unaffected.

**Accessibility.** Purely decorative: `aria-hidden`, no text, no focus.
The margin's meaning (this space is made, not empty) is carried for
sighted readers; nothing informational is lost without it. Grain lines
are `--ink-40` on `--furniture` — decoration contrast, exempt, and never
the carrier of content.

**Tokens.** `--furniture`, `--ink-40`, `--cream`, `--ease-clunk` (final
wedge only), `--loop-lerp` (0.12).

**Content-merge.** The furniture fills exactly the space the forme's own
content leaves: a forme with a wide table (§6.9) has thin margins and
few blocks; a short forme has a tall furniture course. The margin is
computed from the content, the way a compositor cuts furniture to the
forme in front of him — it is the content's offcut, not a frame bought
separately.

**Failure fallback & watchdog.** Blocks' rest positions are their packed
positions; the offsets exist only as JS-applied transforms. If the loop
stalls, a 2,400ms watchdog per forme clears transforms — the margins
simply look packed, which is the printed state.

**Reduced motion.** Blocks stand packed. The margin reads as quiet wood
— still furniture, still honest, no shuffle.

**Performance & mobile.** Transforms on ≤9 small divs per forme, only
while the forme is in the loop's active window; ≤0.3ms/frame worst case.
Mobile: 3 blocks per forme, vertical pack only (above).

### 6.5 The treadle idle rock

**What & why.** A small press ornament — a line-drawn treadle press in
the hero forme's margin — rocks slowly for the whole visit: ±2° on a
3.2s period, the flywheel's idle. It is the shop's heartbeat and its
only purely ambient signature: the press is at work behind the page
whether or not the reader is watching. It pauses while the reader
interacts with a forme, because the pressman stops the press to talk.

**Structure.** One inline SVG (press frame, flywheel, treadle bar) drawn
in `--ink` hairlines with the flywheel picked out in `--steel`, ~90×120px,
placed in the hero's right margin (in the furniture field, §6.4, where it
sits like a tool left on the bench). The rock is a rotation about the
flywheel's axle point (SVG `transform-origin` at the axle), applied to a
`<g>` wrapping the moving parts; the frame stays still — only the
machine's working parts move, as on a real press.

**Motion spec.** Rotate −2°→+2°→−2°, 3,200ms per full cycle,
`--ease-treadle` (sine in-out, the flywheel's own curve). Continuous
while the page is visible and the reader is not interacting. Pause
conditions: pointer down or focus within any forme, `visibilitychange`
to hidden, or the ornament off-screen (IntersectionObserver) — resume
400ms after the last interaction ends, easing back into phase from the
current angle (never a jump to phase zero).

**Choreography timeline.** Page load → rock begins at first paint (it is
already moving when the headline sets — the shop was open before you
arrived) → interaction anywhere in a forme → rock decays to rest over
300ms → interaction ends → 400ms stillness → rock resumes, phase
continuous. Hero scrolled away → rock pauses off-screen; its phase is
kept, so returning finds the same press at the same point in its cycle.

**State matrix.** *Rest (reduced motion / no JS):* the ornament printed
still, flywheel at 0°. *Rocking:* as spec. *Paused-interacting:* at rest
angle, mid-decay or held. *Paused-hidden/off-screen:* frozen at current
angle. *Hover:* none of its own (it is not a control). *Scrolled-past:*
paused (off-screen). *Touch:* identical pause rules (touch counts as
interaction).

**Breakpoints.** ≥1200px: full ornament in the hero margin. 768–1199px:
same, 76×102px. <768px: the ornament moves to the colophon forme (§6.18's
closing note, at the foot) — the hero on mobile has no margin to keep a press
in — at 64×86px, rock retained (it is identity, not garnish).

**Edge cases & failure modes.** Low-power device: if the shared frame
budget (§14) is exceeded for 3 consecutive seconds, the rock's period
doubles to 6.4s (a press idling slower), then, if still exceeded, stops
at 0° and stays a still plate — degradation in the world's own terms.
Multiple pages/tabs: each page's press is its own; no sync is attempted.
SVG failure (ancient engine): the ornament's `<img>` fallback is the
same drawing as a static plate.

**Accessibility.** Decorative, `aria-hidden`, no text alternative beyond
the colophon's printed credit. The rock is slow (3.2s), small (±2°) and
peripheral — well inside vestibular safety; reduced motion stills it
entirely. It never overlaps content (it lives in the furniture field).

**Tokens.** `--ink`, `--steel`, `--ease-treadle`, `--treadle-period`
(3200ms), `--treadle-angle` (2deg).

**Content-merge.** The ornament is the press that printed the page the
reader is holding — it sits in the hero's margin among the furniture
like the shop's own tool, and its printed twin stands in the colophon
forme (§6.18's closing note). It is not a logo pasted in a corner; it is
the machine of the whole metaphor, idling in shot.

**Failure fallback & watchdog.** The rock is a CSS animation on an SVG
group; if it never runs, the press stands still — the printed state.
No watchdog is needed for a still press, and none is faked.

**Reduced motion.** Still plate, 0°, forever. The colophon still credits
the press; a stopped press is a true thing in a shop at rest.

**Performance & mobile.** One CSS rotation on one small SVG group;
negligible (<0.05ms/frame). Mobile: smaller, relocated (above), same
period.

### 6.6 Figures that set, not fade

**What & why.** Every ephemeris figure on the page — sunrise, transit,
sunset, moonrise, a count of subscribers — arrives the way type arrives:
it counts quickly in tabular figures, then each digit *snaps* down 1px
with a faint ink-darkening, set into place. Numbers in this shop are
physical sorts, not tweens; the snap is the difference between a figure
that was *printed* and a number that was *animated*, and readers feel it
without knowing why.

**Structure.** A figure is a `<span class="fig" data-value="06:04">` with
its final value as its text content (the DOM ships the true figure —
always). Enhancement splits the value into digit spans for the snap; the
count phase runs on the numeric value behind the display (for times, the
count runs over minutes-of-day and formats as HH:MM, so 06:04 counts
through real earlier times, never through impossible ones like 06:75).

**Motion spec.** Count: 600ms, linear-ish tally on `--ease-set`'s front
half, tabular figures throughout (no width wobble). Set: at count end,
each digit translates Y +1px over 60ms `--ease-snap`, staggered 24ms
left to right, with ink colour stepping `--ink-70`→`--ink` at the snap.
Total ≈ 600 + (digits×24) + 60 ≈ 780ms for a 5-digit time. Figures in a
table (§6.9) set row by row instead (§6.9's own spec).

**Choreography timeline.** Figure's forme locks (§6.3, t=0) → t=120
count begins → t=720 count lands on the true value → digits snap in
stagger → t≈900 figure at rest, `data-set`. A figure scrolled past
unseen (fast scroll) is found already set — the watchdog (below) sets
any figure whose forme is above the reading line.

**State matrix.** *Rest:* the true figure, printed — the only state a
no-JS reader ever sees, and the correct one. *Counting:* intermediate
real values (for times, always valid times). *Setting:* snaps running.
*Set:* rest. *Hover:* none (figures are not controls; a figure inside a
button inherits §6.8). *Scrolled-past:* set. *Touch:* identical.

**Breakpoints.** All sizes identical in timing; <768px the count shortens
to 400ms (a small page sets faster; the snap — the signature — is kept
at full 60ms/24ms).

**Edge cases & failure modes.** Figure is not a time (a count, a
percentage): counts over its own unit; percentages count in tenths and
set with the % as a final sort. Negative or ranged values (elongation
24° E): the count runs over the magnitude, the suffix sets last. Value
changed by data (a corrected time): the figure re-sets with a proof-red
tick beside it (§6.13's correction language) — a corrected figure is
visibly a corrected figure, never silently swapped. Extremely long count
(day length in minutes): counts in its printed unit (13h 48m counts as
hours then minutes), never as 828 raw minutes.

**Accessibility.** The figure's text is its final value at all times in
the accessibility tree (the counting spans are `aria-hidden`; a visually
hidden static copy carries the value, or equivalently the figure is
`aria-label`led with its final value during the count). Screen readers
never hear a number mid-count. Snap motion is 1px — imperceptible as
motion, present as texture; reduced motion removes it regardless.

**Tokens.** `--ink`, `--ink-70`, `--ease-set`, `--ease-snap`,
`--fig-count` (600ms), `--fig-snap` (60ms).

**Content-merge.** The figures are the site's content — the day's times
themselves (§6.17) — and the setting is how the shop publishes them.
There is no decorative number on an Ephemeris Press page: a count that
doesn't trace to the Day's Forme is a misprint (§9).

**Failure fallback & watchdog.** The DOM value is final from the start;
enhancement only animates *toward* it. A 1,200ms watchdog per forme sets
any unset figure instantly. Failure is indistinguishable from success at
rest — by design.

**Reduced motion.** Figures stand printed at their true values. No
count, no snap. The table is a table.

**Performance & mobile.** Digit spans only on figures in the active
forme; count runs on the shared loop's clock (no per-figure timers).
≤0.2ms/frame. Mobile: 400ms count (above).

---

### 6.7 The solar arc — progress

**What & why.** The page's progress indicator is the commodity the shop
sells: the day's arc. A margin SVG arc runs from sunrise (left) to
sunset (right) across a shallow dome; as the reader scrolls, the arc
fills with gold size and a small sun disc travels it. At the foot of the
page the sun has set — the reader has read the whole day. Progress
measured in daylight is progress the reader can *feel* finishing.

**Structure.** An SVG arc fixed in the right margin (desktop), spanning
the page's full scroll length conceptually but drawn as one dome: path
length normalised to 1; the travelled portion stroked `--gold-deep`
with a `--gold` leading edge, the untravelled in `--ink-40`; a sun disc
(circle, r=7, `--gold` with `--gold-deep` rim — gold lettering's
exception does not apply, the disc is an object, not text) positioned on
the path by `getPointAtLength`. Sunrise and sunset times are printed at
the arc's feet, in caption caps, from the Day's Forme (§6.17) — the
arc's endpoints are labelled with the real times it measures between.

**Motion spec.** Scrubbed by the shared loop (§5): scroll progress
`p ∈ [0,1]` over the whole document maps linearly to arc length. The
disc and fill use the loop's lerped value (0.12), so the sun glides a
fraction behind the reader's hand and settles — a body with weight, not
a scrollbar thumb. No easing token; the lerp is the motion.

**Choreography timeline.** Page top: disc at sunrise foot, arc empty —
06:04. Reader scrolls: fill and disc advance together, always agreeing.
Mid-page: disc near the dome's crown — the printed transit time (12:58)
is marked with a hairline tick at the crown, and the disc crosses it at
exactly p=0.5 of the *document*, by construction of the map (below).
Page foot: disc at the sunset foot, arc full — 19:52. Scrolling up: the
sun retreats along the same arc (progress is a measurement, not a
ratchet — unlike the formes' locks, the arc honestly reports position).

**State matrix.** *Rest (no JS):* the arc printed complete — full gold
arc, disc at the crown, both times labelled: the day's whole arc as a
plate. (Progress is an enhancement; the plate is the content.) *Travelling:*
as spec. *At foot:* full arc, disc set at sunset. *Hover:* none.
*Focus:* none (decorative progress; an `role="progressbar"` twin is
visually hidden — see Accessibility). *Touch:* identical.

**Breakpoints.** ≥1200px: right-margin vertical dome, ~64px wide,
running the chase's full height. 768–1199px: same margin, 48px wide
(the furniture yields the left margin to it, §4). <768px: the arc leaves
the margin and becomes a horizontal dome band fixed at the foot of the
hero forme only while the hero is on screen, then a slim horizontal arc
in the colophon — on a small sheet there is no margin for a sky, so the
sky is printed at the day's head and foot instead. The times remain
printed at both ends in all variants.

**Edge cases & failure modes.** Short page (a single-forme page): the
arc still maps the whole scroll; a page with no scroll shows the arc at
its printed state (full) — a one-sheet day is a whole day. Print: the
arc prints in its rest state. `getPointAtLength` unsupported (legacy):
the disc is positioned by precomputed Bézier points (the path is a
fixed quadratic; the fallback table ships in the code, 33 points).
Resize: path length re-measured on the debounced resize; the disc never
jumps because `p` is unchanged.

**Accessibility.** Decorative in the visual tree; a visually hidden
`role="progressbar"` with `aria-valuemin/max/now` updated at most once
per second carries the same fact for assistive tech ("Reading progress,
about halfway"). The endpoint times are real text in the DOM. The gold
fill is never the only carrier — position of the disc and the printed
times agree, and neither is text-bearing gold-on-cream (§2's law holds:
the disc is an object).

**Tokens.** `--gold`, `--gold-deep`, `--ink-40`, `--ink` (endpoint
labels), `--loop-lerp` (0.12).

**Content-merge.** The arc's endpoints are the day's actual sunrise and
sunset from §6.17, its crown tick the actual transit; on a different
day's page the arc is a different day's sky. It is the table's own data
drawn as a dome — the progress bar *is* the product.

**Failure fallback & watchdog.** If the loop never runs, the arc stands
in its printed rest state (full arc, crown disc). A 2,400ms watchdog
confirms the disc is within the arc's box; a disc lost to a transform
error is reset to the crown. No state of failure shows an empty sky.

**Reduced motion.** The arc prints complete and still, disc at the
crown — the plate state. Scroll does not move it. The hidden progressbar
twin still updates (it is information, not motion).

**Performance & mobile.** One path stroke-dash update + one transform
per frame from the shared loop; ≤0.15ms/frame. Mobile: band variant
(above), same cost.

### 6.8 The impression click

**What & why.** Every clickable thing on the page answers like a press:
it goes down 1px, scales to .99, its ink squashes (a brief bloom of
darkening at the edges) and lands with a hair of misregistration — a
0.4px offset that settles back over 180ms. Feedback with the press's
fingerprint: nothing on this page is digitally clean, because nothing
the shop makes is. It is the theme's micro-interaction signature,
replacing the web's ripple/hover-glow vocabulary entirely.

**Structure.** A press-wide behaviour, not a component: any element with
`.impress` (buttons, links styled as sorts, cards' press areas, the
form's submit, §6.14) gets the treatment via one delegated pointer
handler adding `.impressing` for the press duration; the misregistration
is a duplicated ghost layer — the element's `::after` carrying its
border/label shadow in `--proof` at 18% — offset 0.4px during the press
and easing home. (The ghost is a shadow layer, not a text duplicate:
text itself never doubles, so nothing ever looks broken — just printed
by hand.)

**Motion spec.** Pointer down: translateY(1px) + scale(.99) over 120ms
`--ease-snap`; ink bloom: box-shadow inset deepens 120ms; ghost offset
0.4px appears at full press. Release: all recover over 180ms
`--ease-set`, ghost last (it is the sheet settling back onto the forme).
Keyboard activation (Enter/Space on a focused control): the same press
runs on keydown/keyup — the press does not care what drove the treadle.

**Choreography timeline.** t=0 pointer down → t=120 full press (down,
squashed, ghost offset) → hold while pressed (a long press stays
pressed — the pressman holds the impression for a heavy pull) → release
→ t=+180 recovered, ghost home. A click's navigation (link) begins on
release as normal; the press never delays the action it decorates.

**State matrix.** *Rest:* printed, ghost at 0 offset, invisible.
*Hover:* the element's own hover applies first (a sort lifts, §6.10; a
button's face darkens one step) — hover is the hand approaching.
*Pressed:* as timeline. *Focus-visible:* a 2px `--proof` outline offset
2px — the proofreader's pencil ring around the sort you're about to
pick; the press never replaces the focus ring. *Disabled:* no press, no
ghost; the element is printed in `--ink-40` with the caption "out of
the case" (§12's voice) where a reason is needed. *Scrolled-past:* n/a.
*Touch:* press on touchstart visuals, same timings; no hover state is
faked.

**Breakpoints.** Identical at all sizes; <768px the ghost offset reduces
to 0.3px (small type misregisters less visibly and more honestly).

**Edge cases & failure modes.** Rapid repeated clicks: each press
restarts cleanly (the class is re-triggered, transforms are absolute not
accumulative — a sort pressed twenty times is not twenty pixels down).
Press during a forme's lock: the lock wins (transform on the forme, the
press transforms the child — no conflict, different elements). Element
removed mid-press: the delegated handler is null-safe; nothing throws.
Drag-off release: the press recovers on pointerup anywhere (pointer
capture on the element).

**Accessibility.** The press is pure decoration on a real control: the
control's native semantics, focus and activation are untouched. Focus
ring (above) is 2px proof red on cream — 5.1:1, visible at every state
including mid-press. Touch targets: interactive sorts and buttons are
≥44px in their hit area even when the visible sort is smaller (the
compositor's fingers are not pointers; the reader's are). No information
is carried by the ghost or the squash.

**Tokens.** `--proof` (ghost, focus), `--ink`, `--ease-snap`,
`--ease-set`, `--press-depth` (1px), `--press-ghost` (0.4px).

**Content-merge.** The impression is how the page's own objects respond
— a link in this shop is a sort you pick and press; the feedback is the
metaphor completing itself on the content itself, not an effect layered
over foreign material.

**Failure fallback & watchdog.** Without JS, controls are native and
instant — the press is enhancement only; the delegated handler is the
single point of failure and its absence is invisible. No watchdog: a
press that never animates is just a click, which is the fallback.

**Reduced motion.** No travel, no ghost: activation is instant, and the
only feedback is the focus/hover state change. (The press at rest
prints; it does not perform.)

**Performance & mobile.** Transforms + one shadow on the pressed element
only, event-driven; zero idle cost. Mobile: 0.3px ghost (above).

### 6.9 The day's table forme

**What & why.** The product itself: the day's ephemeris as a set table —
rows for sunrise, solar transit, sunset, moonrise, moonset, the moon's
illumination, the evening planet — each row a line of type with its
figure set (§6.6) at the row's end. This is the forme the whole site
exists to print, and its spec is the theme's data-table law: a table
that looks *set* — ruled, justified, tabular — because it was.

**Structure.** A real `<table>`: caption (the date line, set as the
forme's running title), two columns (phenomenon / time) plus a narrow
third for notes ("waning", "24° E") where the record carries them.
Hairline row rules in `--ink-40`; a heavier rule under the caption in
`--ink`; figures right-aligned to the colon. The table sits in a
full-measure forme (12 columns, §4) with its registration marks; the
moon's row carries a small drawn phase disc (SVG, filled to the printed
illumination — 18% waning: the disc's lit portion is computed from the
record's figure, never drawn freehand).

**Motion spec.** On lock (§6.3): rows set line by line — each row's
figure runs §6.6's count-and-snap, staggered 90ms per row (the
compositor sets the table a line at a time), row rules draw in from the
left over 200ms `--ease-peel` as their row sets. The phase disc fills to
its printed fraction over 600ms as its row sets. Total for 7 rows ≈
90×7 + 780 ≈ 1.4s, overlapping the lock.

**Choreography timeline.** Forme locks t=0 → t=100 first row's figure
begins → rows set at 90ms stagger → phase disc fills with its row
(row 4) → t≈1.4s table fully set → the stick rule (§6.11) parks beneath
the table forme while it is the active forme. Rows never re-set on
re-scroll; a set table stays set.

**State matrix.** *Rest:* the complete table, printed — the no-JS and
print state, and the correct one. *Setting:* rows in stagger. *Set:*
rest. *Hover (a row):* the row's rule darkens to `--ink-70` and the
figure lifts none — a table is read, not played with; the only row
interaction is the correction tick if the row was corrected (§6.13).
*Focus:* the table is not focusable as a whole; any linked row (a
phenomenon linking to its back-number, §6.12) is a normal link with
§6.8's press. *Scrolled-past:* set. *Touch:* identical.

**Breakpoints.** ≥1200px: full measure, 22px figures. 768–1199px: notes
column folds into the phenomenon cell as a following phrase. <768px:
figures 19px; the table keeps two columns (phenomenon/time) with notes
as a second line in the cell — a table never becomes cards in this
shop; a forme is a forme at any width.

**Edge cases & failure modes.** A phenomenon missing from the day's
record (no moonrise on a given date — a real astronomical occurrence):
the row prints an em-dash and the note "none today — the moon does not
rise", set like any other row. The dash is data, not an error state.
Long phenomenon names: wrap within the cell; figures never wrap. Data
arriving late (client-fetched table): the forme shows §6.16's un-inked
skeleton for at most one beat, then the table sets whole — a table is
never streamed row by row from the network; the stagger is theatre over
complete data, not a loading pattern.

**Accessibility.** Real table semantics: `<caption>`, `<th scope="row">`
per phenomenon, figures as cell text. The phase disc is `aria-hidden`
with its figure ("18%") as text in the row — the disc illustrates the
number, the number is the content. Row stagger is `aria-hidden` during
setting exactly as §6.6 specifies; the table's accessible content is
complete from first paint. Contrast: figures ink on cream 13.8:1; notes
in `--ink-70` ≈6.9:1.

**Tokens.** `--ink`, `--ink-40`, `--ink-70`, `--gold` (phase disc's lit
edge only), `--ease-peel`, `--fig-count`, `--fig-snap`.

**Content-merge.** This element *is* the content — the day's table is
the site's reason to exist, and every other element on the page (the
arc, the colophon, the back numbers) prints figures drawn from the same
record this table prints in full (§6.17).

**Failure fallback & watchdog.** The table ships complete in the DOM;
the stagger is JS theatre over it. The §6.6 watchdog sets any unset
figure; a 1,800ms table watchdog clears all row animations. Print: the
table prints exactly as it reads — it is, after all, a printed table.

**Reduced motion.** The table stands printed, all figures at value,
rules drawn. Nothing sets; everything is legible — the newspaper state.

**Performance & mobile.** 7 figures + 7 rule draws, once; ≤0.3ms/frame
during the set. Mobile: same, with §6.6's shortened counts.

---

### 6.10 The job-case navigation

**What & why.** The site's navigation is a California job case: a
shallow tray of compartments laid across the head of the page, each
compartment holding one destination as a standing sort — the section's
name set in a block of type. The reader picks a page the way a
compositor picks a sort: from the case, by name, by place. The current
page's compartment is *picked* — its sort lifted and resting in the
composing stick that rides beneath the case.

**Structure.** A `<nav>` as a tray: `--paper-shadow` tray walls, hairline
compartment dividers in `--ink-40`, each item an `<a class="case-sort">`
— the label in Playfair small caps within a sort block (ink face,
`--steel` body shadow at its foot). Compartments size to their labels as
real case compartments size to their sorts (capitals' row narrower). The
"stick" is a ruled channel beneath the tray holding the current item's
sort, duplicated there by layout (the original stays in its compartment,
dimmed to `--ink-70` — the case shows a gap where the sort was taken
*and* the stick shows it held; the duplication is the honest drawing of
"picked").

**Motion spec.** Page load: the current sort lifts from its compartment
(translateY −3px, 160ms `--ease-set`) and settles into the stick (the
stick's copy fades its ink from `--ink-70` to `--ink` over 200ms) —
300ms total, after the hero's setting begins (it is a quiet ceremony,
not a rival to §6.1). Hover on any sort: lift 2px + face darken, 120ms.
Activation: §6.8's impression, then §6.15's re-proof carries the reader
away.

**Choreography timeline.** t=0 (first paint): case printed, current
compartment's sort at rest, stick empty-looking (its copy at
`--ink-70`) → t=400 lift begins → t=560 sort held → t=760 stick copy at
full ink. On navigation the sequence reverses within §6.15's transition
(the sort goes back, the new page's case arrives with its own sort
already in its stick — cases are per-page furniture, printed with the
page).

**State matrix.** *Rest:* as printed. *Current page:* sort held in the
stick, `aria-current="page"`. *Hover:* lift + darken. *Focus-visible:*
§6.8's proof-red ring. *Active/pressing:* §6.8. *Disabled:* a section
with no pages yet sits as an *empty compartment* — the tray shows the
compartment, labelled in `--ink-40` caps "NOT YET SET", not a link: the
case honestly shows what the shop doesn't have. *Scrolled:* the case is
in the hero forme's head; it scrolls away with the page (the stick rule,
§6.11, takes over wayfinding below the fold — the shop has two
instruments and uses each where it belongs). *Touch:* no hover lift;
press only.

**Breakpoints.** ≥1200px: full tray, all compartments in one case.
768–1199px: tray compresses (compartment padding tightens, labels to
15px). <768px: the case becomes two rows — the tray wraps as real cases
stack — with the stick beneath the second row; below 5 items it stays
one row and scrolls horizontally within the tray (the tray has walls;
the sorts slide inside it, the page never scrolls sideways).

**Edge cases & failure modes.** Many sections (>9): the case gains a
second tray beneath (cases stack in a cabinet — the metaphor holds),
stick under the lower tray. Very long label: the compartment widens and
its neighbours narrow, as a compositor re-divides a case; labels never
truncate (a truncated sort is a broken sort). No JS: the case is a
plain nav of links, current item marked by ink weight — fully usable,
merely unlifted.

**Accessibility.** A real `<nav>` with a list of links; `aria-current`
on the present page. The stick's duplicate is `aria-hidden` (the link in
the case is the one address). Hit areas ≥44px tall regardless of the
drawn compartment height. Focus order = case order = reading order.
Labels are text (Playfair), never images of type.

**Tokens.** `--paper-shadow`, `--ink`, `--ink-70`, `--ink-40`, `--steel`,
`--ease-set`, `--proof` (focus ring).

**Content-merge.** The nav is the shop's own furniture holding the site's
own sections; the current-page state is expressed in the world's verb
(picked, held in the stick) rather than a coloured pill. A section added
to the site is a compartment added to the case — the furniture grows
with the content, visibly.

**Failure fallback & watchdog.** No watchdog needed: every state is a
rest state of a printed nav. If the lift never runs, the current sort
sits in its compartment at full ink with `aria-current` doing the work —
the case still reads correctly.

**Reduced motion.** No lift: the current sort stands at full ink in its
compartment and the stick copy is printed full-ink beneath — position,
not motion, tells the story.

**Performance & mobile.** One small transform on load, hover transforms
on sorts; negligible. Mobile: wrapped tray (above), same behaviour.

### 6.11 The compositor's stick rule

**What & why.** Below the fold, wayfinding belongs to the stick rule: a
hairline rule with the active forme's running title set in it, which
pins beneath whichever forme the reader is inside and snaps to the next
as formes change. It is the theme's scrollspy, drawn as the brass rule
the compositor lays under the line he is setting — it tells the reader
which forme they are in, and it is the one licensed pin in the theme
(§5).

**Structure.** A `<div class="stick-rule">` — 1px `--ink` rule, 120px
wide, with the active forme's title in caption caps set into its left
end and the forme's number ("FORME III OF VII") at its right. It lives
in the left furniture margin, rotated 0° (a rule is horizontal; the
margin column carries it at the reading line's height, `position:
sticky` within the chase). Each forme declares its title/number in
`data-stick` attributes; the rule's text swaps as the active forme
changes.

**Motion spec.** The rule rides sticky at the reading line (62% height).
On forme change: the old title's letters fade to `--ink-40` over 90ms,
the rule snaps 6px toward the new forme (translateY, 140ms
`--ease-snap` — the compositor tapping the rule down), and the new title
sets in (ink to full, figures-style, §6.6's snap without the count).
The rule itself never scrolls smoothly with content — it *hops* forme
to forme, as a rule is picked up and laid down.

**Choreography timeline.** Forme N's head crosses the reading line →
t=0 old title fades → t=90 rule snaps → t=140 new title begins setting →
t=230 title set, rule at rest under forme N. Between formes (in a
furniture course): the rule keeps the last forme's title — the
compositor's rule stays under the last line set until the next begins.

**State matrix.** *Rest (no JS):* no rule — the formes carry their own
printed titles; the rule is an enhancement for the travelling reader.
*Active:* as spec. *First forme:* the rule is present from the hero
(under the date line) once the hero's setting completes. *Last forme
(colophon):* the rule's title reads "COLOPHON" and its number the final
count; at the page foot the rule unpins and rests in the colophon's
margin (sticky released by the chase's end). *Hover/focus:* none (not a
control). *Touch:* identical.

**Breakpoints.** ≥1200px and 768–1199px: left margin, as spec (on
tablet the left margin is the furniture margin, §4 — the rule shares it,
parked above the blocks). <768px: no side margin exists; the rule
becomes a slim sticky band at the page head's foot — rule + title in a
28px strip under the case (§6.10) — same snap, same titles. The
instrument survives the loss of its margin.

**Edge cases & failure modes.** Two formes crossing the line in one
frame (fast scroll): the rule takes the *lower* forme (the one being
entered) and snaps once — intermediate titles are skipped, never queued
(the compositor does not flip through). Forme without `data-stick`:
the rule keeps the previous title (a forme that forgot its running
title is a build error §10 catches; the rule degrades to silence rather
than inventing one). Resize: sticky position re-derives from CSS; no JS
state to repair.

**Accessibility.** Decorative wayfinding: `aria-hidden`. The formes'
own headings carry the same information in the document outline — the
rule repeats for the eye what the headings say to the machine, and
neither depends on the other. Its title text is small caps Garamond at
13.5px in `--ink` (13.8:1).

**Tokens.** `--ink`, `--ink-40`, `--ease-snap`, `--loop-lerp` (0.12,
for the reading-line tracking only).

**Content-merge.** The rule's text is the formes' own running titles and
their count — it is set from the page's actual sections at build time.
Add a forme and the rule's "OF VII" becomes "OF VIII" everywhere,
because the count is derived, not typed (§6.17's discipline applied to
furniture).

**Failure fallback & watchdog.** If the observer driving it fails, the
rule simply never appears — the page loses an ornament of wayfinding,
never its headings. A 3,000ms watchdog removes a rule whose title has
gone stale against the actual scroll position (recomputed once), rather
than letting it lie.

**Reduced motion.** The rule appears under the active forme with its
title printed — no snap, no fade; it changes as a printed label changes
between pages: instantly, between frames the reader doesn't watch.

**Performance & mobile.** Sticky positioning is compositor-cheap; title
swaps are rare events. ≤0.1ms/frame amortised. Mobile: band variant
(above).

### 6.12 The back-numbers index

**What & why.** The archive of past days: each past day is a back number
— a small pulled proof card carrying its date, its sunrise and sunset,
and its moon's phase disc. A listing page in this shop is not a grid of
thumbnails; it is a drawer of yesterday's sheets, each one checkable
against its own day exactly as today's is (§6.9). This is the theme's
listing/card element.

**Structure.** A forme containing a grid of proof cards: each card is an
`<article>` drawn as a small sheet — cream on `--paper-shadow` (a sheet
lying on the bench), hairline border, its own miniature registration
marks, date line in Playfair, the day's two times set as figures, a
phase disc (SVG, computed from that day's illumination), and the whole
card a link to that day's page. Cards sit in the grid slightly
un-aligned — rotated within ±0.4° and offset by ≤2px, seeded per card —
because a drawer of sheets is never a CSS grid's fantasy of order; the
grid's rows still align (the drawer is tidy, the sheets are paper).

**Motion spec.** The index forme locks as §6.3; then cards set in
reading order, stagger 60ms, each with a miniature lock (translateY
10px→0, `--ease-clunk` at 300ms) — a drawer being filled sheet by
sheet. Hover: the card lifts 3px and its shadow deepens (a sheet picked
up by one corner — shadow shifts toward the lifted corner, drawn with a
skewed gradient). Press: §6.8. Phase discs fill as their card sets
(§6.9's rule).

**Choreography timeline.** Forme locks t=0 → t=150 first card sets →
cards stagger 60ms → last card (12 per page) set by t≈1.05s → the
index's own stick-rule title (§6.11) reads "BACK NUMBERS". Pagination
(§11) pulls the next drawer via §6.15's re-proof, not an infinite
scroll — a drawer is finite, and so is a page of them.

**State matrix.** *Rest:* all cards printed and readable (the no-JS
archive is complete). *Setting:* stagger running. *Hover:* lift (above).
*Focus-visible:* proof-red ring (§6.8). *Current day's card* (if listed):
its compartment treatment — a gold tick at its corner, the one licensed
gold mark per card. *Empty drawer* (a month with no issues): §6.18's
empty language, in miniature — a single printed slip, "No numbers were
pulled in March — the press was being repaired." (§12's voice.)
*Scrolled-past:* set. *Touch:* no hover lift; press only.

**Breakpoints.** ≥1200px: 4 cards across. 768–1199px: 3 across.
<768px: 2 across, rotations halved (small sheets in a small drawer
wobble less), figures at 17px.

**Edge cases & failure modes.** A day whose record lacks a moonrise: its
card prints the em-dash line (§6.9's rule) — the drawer shows the gap
honestly. Hundreds of back numbers: paginated by month-formes (each
month its own forme and drawer), never one endless grid. A card whose
day-page doesn't exist (data error): the card is not rendered — the
index never links to a missing sheet (§10 gate). Late images: cards
carry no images (type and discs only), so there is nothing to late-load
— a deliberate consequence of the world's materials.

**Accessibility.** Cards are links with real text: the accessible name
is the full date line ("Tuesday the Seventh of April — sunrise 06:08,
sunset 19:48"), not "read more". Phase discs `aria-hidden`, their
figures present as text ("moon 34%"). Rotation never affects focus
order; focus ring follows the card's unrotated box (outline on the
link, transform on an inner wrapper — the ring stays rectangular and
findable).

**Tokens.** `--cream`, `--paper-shadow`, `--ink`, `--ink-40`, `--gold`
(corner tick only), `--ease-clunk`, `--proof` (focus).

**Content-merge.** Each card's figures are that day's own record,
printed in the same forms as today's table (§6.9) — the archive is the
product's history, in the product's own type. The worked set (§8)
reconciles: 13 April 06:06/19:50, 12 April 06:08/19:48, 11 April
06:11/19:46 — each day 2 minutes earlier at dawn, 2 later at dusk,
walking toward today's 06:04/19:52 (§6.17).

**Failure fallback & watchdog.** Cards ship printed; the stagger is
enhancement. A 1,600ms watchdog settles any unset card. Failure looks
like a filled drawer.

**Reduced motion.** Cards stand printed in their seeded places — the
drawer is simply already full when you open it.

**Performance & mobile.** ≤12 cards animate per page, transforms only;
≤0.3ms/frame during the set. Mobile: 2-across, halved rotation (above).

---

### 6.13 The proofreader's forme

**What & why.** The about/method forme: a proof of the day's table shown
*being corrected* — proof red annotations draw themselves in the margin
(a circled figure, a transposition mark, a caret with an inserted word),
each correction keyed to a line of method text beside it. It is how this
shop explains itself: not with a mission statement, but with a marked
proof demonstrating that the figures are read by a second pair of eyes
before they are printed. The theme's storytelling element — and its
trust argument, performed.

**Structure.** A two-part forme: left, a miniature proof sheet (the
day's first three table rows, set small, on `--paper-shadow`); right,
the method text. Annotations are inline SVG paths over the proof —
circle, caret, transpose curve — drawn in `--proof` at 1.5px, with the
proofreader's marginal words in a Garamond italic hand (the font's
italic, letterspaced slightly — the theme admits no handwriting font;
a proofreader in this shop writes in italic Garamond, and the slight
formality is the joke the shop tells on itself). Each annotation is
paired with its paragraph by number (❶ ❷ ❸ in proof red).

**Motion spec.** As the forme locks and the reader reaches each
annotation's beat (the forme's own scroll progress thirds), the SVG path
draws over 450ms `--ease-peel` (a pencil drawn at reading speed), and
its marginal word fades its ink in over 200ms after the stroke
completes. The corrected figure on the proof — the worked example uses
the moonrise, first set as 05:21, struck through in red, corrected to
05:12 (§6.17) — has its strike draw first (300ms), then the correction
sets above it (§6.6's snap, in proof red, then inking to `--ink` over
600ms as the correction is *accepted* into the table — the only place
in the theme where red becomes ink, because that is what a correction
is).

**Choreography timeline.** Forme locks t=0 → first third: annotation ❶
draws (450ms) + word (200ms) → second third: the strike and correction
(the centrepiece, ~900ms total) → final third: annotation ❸ draws →
forme at rest, the proof fully marked. Scrolling back: marks stay —
a read proof stays read.

**State matrix.** *Rest (no JS):* the proof fully marked, all
annotations drawn, correction in place — the finished proof is the
content; the drawing is the performance of it. *Drawing:* per beat.
*Complete:* rest. *Hover (an annotation):* its paired paragraph's
number ticks in red (the pairing made visible both ways). *Focus:* the
annotations are not controls. *Scrolled-past:* complete. *Touch:*
identical; hover pairing is a mouse-only courtesy, never the only link
(the numbers pair them in print regardless).

**Breakpoints.** ≥1200px: proof left, text right, as spec. 768–1199px:
proof narrows, annotations keep their positions relative to the proof
(they are positioned on the proof's box, not the page's). <768px:
stacked — proof forme first (full width), method text below; annotation
beats key to the proof's own travel instead of the combined forme's.

**Edge cases & failure modes.** If the day's data carries no correction
(the proof was clean): the forme shows a clean proof with one marginal
line — "Read and passed, no corrections" in the proofreader's italic,
signed with initials. A clean proof is also a true story, and the forme
must be able to tell it (the element degrades to honesty, not to a
fabricated error). Long method text: annotations stay three — a proof
with nine corrections is a different, worse story (§9). The struck
figure remains legible under its strike (strike at 1.5px, figure at
full ink) — a correction you cannot read the original of is a cover-up.

**Accessibility.** The proof sheet is an illustration of the method
text: the text carries every fact in prose ("the moonrise was first set
as 05:21 and corrected to 05:12 before printing"), and the proof is
`aria-hidden` except its caption. The struck figure uses a real
`<s>`-equivalent styling with the correction as adjacent text, so the
pair reads correctly in the text flow. Red annotations on cream are
5.1:1; the marginal words are text at 5.1:1, AA.

**Tokens.** `--proof`, `--proof-pale` (wash behind the corrected line),
`--ink`, `--paper-shadow`, `--ease-peel`, `--ease-snap`.

**Content-merge.** The proof being corrected is the day's own table's
first rows, and the correction is the day's own real correction (the
worked 05:21→05:12 moonrise is the same figure the table prints and the
colophon repeats — §6.17). The method forme doesn't describe checking;
it *shows the check that today's page actually passed*.

**Failure fallback & watchdog.** The marked proof ships complete in the
DOM (paths at full draw length); drawing is JS theatre over it. A
1,500ms watchdog per annotation completes any partial stroke. Failure
= a finished proof, which is the point of the exercise.

**Reduced motion.** The proof stands fully marked. The correction's
red-to-ink acceptance is shown as the final state: correction in ink,
strike in red, original legible — the whole story in one still frame.

**Performance & mobile.** Three SVG path draws per page at most;
≤0.2ms/frame. Mobile: stacked layout (above), draws retained (they are
the content's performance, not garnish).

### 6.14 The subscription forme — the conversion

**What & why.** The press sells one thing: the Daily Impression, the
day's sheet posted to subscribers each morning. Its conversion forme is
set as a forme: the offer is a composed block of type, the fields are
lines ruled into it, and submitting is *making an impression* — the
forme stamps its confirmation, "RECEIVED & SET", with the subscriber's
number drawn from the press's own count. A signup that behaves like the
product it sells.

**Structure.** A forme containing: the offer set as a forme title and
two lines of Garamond (what the sheet is, what it costs — §6.17's
record: £6 per month, £60 per year, one sheet each morning); a real
`<form>` with three fields — name, postal address (it is a *posted*
sheet; the form asks for a postal address, not an email, and says why),
and plan (two radio sorts: Monthly / Yearly); labels as compositor's
caption caps above ruled lines (inputs are transparent fields over a
rule — the reader writes on the line, as on a printed order slip); the
submit as a large sort (§6.8) lettered "SET MY NAME". The confirmation
replaces the forme's inner block with the stamped receipt (§ below).

**Motion spec.** Fields: on focus, the rule beneath thickens from 1px
`--ink-40` to 2px `--ink` over 150ms (the compositor's pencil under the
line being written) and the label inks from `--ink-70` to `--ink`. The
radio sorts press with §6.8. Submit: the whole forme takes §6.8's
impression at forme scale (translateY 1px, ghost in `--proof` at 0.4px)
over 200ms, then the receipt stamps in: "RECEIVED & SET" in proof red,
rotated −3°, scale 1.15→1 over 160ms `--ease-snap` with the ink-squash
bloom — a rubber stamp on the slip — followed by the subscriber number
setting (§6.6) as "№ 215 on the list" (the record's 214 + 1, §6.17).
Stamp first, number second: the press acknowledges, then files.

**Choreography timeline.** Forme locks (as §6.3) → fields at rest →
reader completes the form → submit press (200ms) → t=+250 stamp lands
→ t=+450 number sets → receipt complete; a printed line beneath offers
the way back ("Set another name" resets the forme to its unset state —
the slip is re-usable, the stamp was on the copy, not the original).
Error path: an invalid field's rule turns `--proof`, its correction
note appears in the proofreader's italic beneath it (§12's error
voice), and the forme does *not* stamp — an uncorrected form is never
received.

**State matrix.** *Rest:* offer + empty ruled fields. *Filling:* focus
states as spec. *Invalid (per field):* red rule + correction note;
the field's entered value is never cleared by an error (the compositor
does not throw away your copy). *Submitting:* submit sort held pressed,
fields disabled for the beat (≤600ms; the press is pulling). *Received:*
the receipt state (stamp + number + the first sheet's promise: "Your
first sheet is tomorrow's forme — the sky for Wednesday the Fifteenth
of April", the date computed from the record's day + 1). *Disabled
(submit before required fields):* the submit is *not* disabled — the
press accepts the slip and corrects it (errors are the proofreader's
job, §12); disabling a submit is a web habit this forme refuses.
*Touch:* identical; stamp and number unchanged.

**Breakpoints.** ≥1200px: forme in the 7-column measure, fields full
measure. 768–1199px: 9 columns. <768px: single column, fields full
width, the stamp at −2° (a smaller slip stamps straighter), submit sort
full-width (a treadle you can reach).

**Edge cases & failure modes.** Network failure on submit: the forme
keeps the reader's entries, the stamp does not fall, and an errata-line
appears in the Pressman's voice (§12): "The slip did not reach the
press — your words are still on it above. Try the treadle again."
Retry reuses the same entries. Duplicate submission: the receipt's
number is issued once per successful response; a double-press during
the submitting beat is swallowed by the held state. Very long address:
the ruled line grows downward (the slip is paper; paper accommodates)
— fields are auto-growing textareas in slip's clothing. Plan pricing
must match §6.17 exactly; §10's gate greps the forme against the
record.

**Accessibility.** A real form: `<label>` per field (the caption caps
*are* the labels, associated, not decorative), errors linked via
`aria-describedby` and announced in a polite live region ("The address
line needs a town — the postman is good, but he is not psychic" is the
*voice*; the region announces the same correction plainly first, wit
second — §12's rule). The stamp is `aria-hidden`; the receipt's text
("Received and set. You are № 215 on the list.") is the accessible
confirmation, present in the DOM at receipt time. Focus moves to the
receipt's heading on success — the one licensed focus move in the
theme, because the forme's whole content changed. Contrast: stamp red
on cream 5.1:1 at 20px+ bold-equivalent — AA for large text, and the
same words exist in ink beside it.

**Tokens.** `--ink`, `--ink-40`, `--ink-70`, `--proof`, `--proof-pale`,
`--ease-snap`, `--ease-set`, `--fig-snap`.

**Content-merge.** The forme sells the press's own product at the
record's own prices, issues a number from the record's own count, and
promises a first sheet dated from the record's own day. Change the
record — a price rise, a new count — and the forme, the stamp and the
promise all change together, because all three are set from it.

**Failure fallback & watchdog.** Without JS the form is a plain,
working order slip posting to its endpoint — ruled lines and a button,
fully usable; the stamp is enhancement. A submission watchdog at 4,000ms
returns the forme to its filling state with the errata-line if the
request hangs — the reader is never left watching a held press.

**Reduced motion.** No forme-press, no stamp animation: the receipt
appears printed — stamp present as a still red impression (a stamp's
final state is a still thing anyway), number at value.

**Performance & mobile.** Event-driven only; the stamp is one transform.
≤0.2ms/frame during its 160ms. Mobile: single column (above), stamp
retained at reduced rotation.

### 6.15 The re-proof — page transition & loader

**What & why.** Moving between pages is re-proofing: the outgoing page
is pulled off the forme and the new page's proof is laid down. It is
the §6.2 peel run at travelling speed — 450ms, not the hero's 1,200 —
because the ceremony is paid once at the front door and afterwards the
shop works briskly. It is also the theme's loader: a navigation that
takes longer than the peel shows the new page's formes as un-inked
skeletons (§6.16) rather than a spinner — this shop has no spinner; it
has standing type awaiting impression.

**Structure.** A peel layer (as §6.2: a full-viewport cream sheet with
the outgoing page's ghost — a 6%-ink impression of the old page,
generated by cloning its main forme into the layer at low ink) that
wipes down over the incoming page. Implemented as an enhancement over
ordinary navigation: same-page (SPA) transitions run the full peel;
full document loads run a shortened entry peel (the new page arrives
under a sheet that lifts in 300ms) so both directions feel like one
press. The layer is `aria-hidden`, inserted and removed by JS.

**Motion spec.** Exit peel (same-page nav): 450ms `--ease-peel`, top to
bottom, the ghost sheet covering the old page, then the new page
revealed already locked and printed beneath (its formes do not re-lock
on a transition arrival — the reader has no patience for a second
ceremony, and §6.3's locks are for first arrivals and scroll). Entry
peel (fresh load of an interior page): sheet lifts over 300ms.
Threshold: if the incoming content isn't ready within the exit peel,
the sheet holds as a printed "pulling the proof" slip (the day's date
line and the treadle ornament, still) for up to 1,200ms, then §6.16
skeletons take over in place.

**Choreography timeline.** Click (§6.8 press, 120ms) → t=120 exit peel
begins → t=570 new page beneath, sheet lifting → t=870 transition
complete, layer removed, focus at the new page's head (SPA) — total
under 900ms for ready content. Fresh interior load: sheet present at
first paint (server-rendered as the page's top layer in its printed
state) → lifts at fonts-ready or 300ms → gone by 600ms.

**State matrix.** *Rest:* no layer; pages stand printed. *Transitioning:*
as timeline. *Held (slow content):* the printed slip state. *Skeleton
handoff:* >1,200ms → §6.16 in the new page's formes. *Back/forward
cache restore:* no peel (the browser's own return is instant; the press
does not re-pull a sheet the reader just put down). *Focus:* SPA
transitions move focus to the new page's `<h1>` (tabindex −1) at peel
end and announce the page title via a live region — the one place the
theme manages focus, because the page changed. *Touch:* identical.

**Breakpoints.** Identical at all sizes; <768px the ghost impression is
omitted (the sheet is plain cream with the date line) — a small sheet
carries less ghost.

**Edge cases & failure modes.** Navigation to an anchor on the same
page: no peel (a finger moving down the same sheet). External links: no
peel — the sheet is ours, the destination isn't. Failed navigation
(404 from an SPA route): the peel completes onto §6.18's errata slip —
the transition never fails open onto a blank. Peel interrupted by a
second click: the layer completes its current wipe instantly and the
newest navigation wins. `prefers-reduced-motion`: no peel at all —
pages change as pages turn in a bound volume: instantly.

**Accessibility.** The layer is `aria-hidden` and never traps focus;
during an SPA transition the old page is `inert` until the swap. The
title announcement (above) is the transition's accessible content. No
information crosses only via the peel. Keyboard users triggering a
link get the identical sequence — the press does not ask how the
treadle was driven.

**Tokens.** `--cream`, `--ink` (ghost at 6%), `--ease-peel`,
`--peel-duration` (450ms travelling / 300ms entry).

**Content-merge.** The ghost on the sheet is the reader's own outgoing
page, and the date line on the held slip is the Day's Forme date — the
transition is printed from the pages it connects, not branded with a
logo splash.

**Failure fallback & watchdog.** A 1,500ms watchdog removes the layer
unconditionally. If JS fails mid-transition in an SPA, the router's
fallback is a plain document navigation — the press's oldest technology:
turn the page.

**Reduced motion.** No peel, no slip: instant page change; loads show
§6.16 skeletons only if content genuinely isn't ready.

**Performance & mobile.** One composited layer, clip-path only, ≤450ms;
the ghost clone is a single low-ink snapshot (no live DOM mirror).
Mobile: plain sheet variant (above).

---

### 6.16 Un-inked standing type — the skeleton

**What & why.** When content genuinely isn't ready — a fetched table, a
slow archive drawer — the loading state is standing type not yet inked:
the forme's shapes present as pale sorts and rules in `--paper-shadow`
and `--ink-40`, the exact geometry of the coming content, awaiting
impression. A skeleton in this shop is not grey boxes; it is the page's
own type standing in the forme before the ink roller passes. The reader
sees *what is coming, shaped like itself*.

**Structure.** Per-forme skeleton mirrors: the table forme's skeleton is
7 ruled rows with figure-length blocks; the index's skeleton is its
card grid in pale sheets; a text forme's skeleton is ruled lines at the
body's own measure and line-height (29.45px — the skeleton is set on
the same body, §4). Blocks are `--paper-shadow` with `--ink-40`
hairlines; the moon disc's skeleton is an unfilled circle. One class,
`.standing`, swaps real content for its mirror (server-rendered when
the route is known-slow; client-inserted by §6.15's handoff).

**Motion spec.** Standing type does not shimmer — shimmering is a
screen habit, and ink does not shimmer on standing type. The single
licensed motion: a slow ink pass — a `--ink-40`→`--ink-70` darkening
sweep across the forme over 1,600ms `--ease-treadle`, repeating while
the content is outstanding (the roller crossing the forme, again, not
yet printing). When content arrives, the real forme replaces the
skeleton in one frame and locks (§6.3) if it hasn't — the impression
lands whole; content never trickles into a skeleton piecemeal.

**Choreography timeline.** Forme's content outstanding at t=0 →
skeleton present (it was rendered with the page or inserted by §6.15 at
its 1,200ms handoff) → ink passes at 1,600ms cycles → content arrives →
one-frame swap → §6.3 lock (300ms travelling variant) → forme at rest.
Maximum skeleton dwell before the errata-line (below): 4,000ms.

**State matrix.** *Standing:* as spec. *Arrived:* swapped whole.
*Failed (>4,000ms):* the skeleton is replaced by the forme's errata
state — a printed slip in the forme (§6.18's language) saying what
didn't arrive and offering the retry as a sort to press; the reader is
never left watching type that will never be inked. *Partial arrival:*
formes resolve independently; one standing forme among printed ones is
a true picture of a shop mid-work. *Focus:* skeletons are not focusable;
the forme's heading (real, printed above the skeleton) remains the
focus landmark. *Touch:* identical.

**Breakpoints.** Identical structure at all sizes; the skeleton mirrors
each breakpoint's own layout (it is generated from the same boxes), so a
resize while standing re-mirrors without a flash of wrong geometry.

**Edge cases & failure modes.** Content arrives before the skeleton's
first ink pass completes: swap immediately; a half-crossed roller is
forgotten. Content arrives as an error: the errata state (above), not
an endless retry loop — one retry press is offered; a second failure
prints the slip permanently for this visit ("the table could not be
set — the day's sheet is at the counter", §12, directing to the
colophon). Skeleton for a forme whose content is already in the DOM
(a false alarm): never inserted — skeletons are for absence, not for
theatre.

**Accessibility.** The standing forme carries `aria-busy="true"` on the
forme and a visually hidden status ("Setting the day's table…") that
resolves to the content's arrival announcement. The skeleton's blocks
are `aria-hidden`. When the errata state replaces it, the slip is real
text with a real button. Nothing about the wait is conveyed by the ink
pass alone.

**Tokens.** `--paper-shadow`, `--ink-40`, `--ink-70`, `--ease-treadle`,
`--ink-pass` (1600ms).

**Content-merge.** Each skeleton is its own forme's mirror — the table's
skeleton has the table's rows, the drawer's has the drawer's cards. It
is drawn from the content's shape, so the reader learns the page's
structure from its absence: the forme is visible before the impression.

**Failure fallback & watchdog.** The 4,000ms errata handoff *is* the
watchdog — no skeleton may stand longer. If the skeleton mechanism
itself fails, the forme is simply empty with its heading printed, which
is a lesser failure than a lying skeleton, and §10's gate tests the
handoff explicitly.

**Reduced motion.** No ink pass: the standing type stands still (which
is, literally, what standing type does). The swap on arrival is
instant.

**Performance & mobile.** Static boxes + one opacity/colour sweep per
standing forme; ≤0.1ms/frame. Mobile: identical mirrors of the mobile
layout.

### 6.17 The Day's Forme — the declared record

**What & why.** The record every figure on the page traces to: the
press's computed table for the date, held as one declared object and
printed in full in the table forme (§6.9). This element is the spec's
consistency machine — the reason the hero, the arc, the colophon, the
back numbers and the subscription forme can be audited against each
other. In build terms it is a data block (JSON in the page, or the
CMS's day record) plus the forme that renders it; in the theme's terms
it is the copy from which the compositor sets, kept on the stone where
anyone can check it.

**Structure.** A `<script type="application/json" id="days-forme">` (or
the framework's equivalent data island) carrying the record, and — this
is the discipline — *no other element on the page carries a figure as a
literal*. Figures in the DOM are rendered from the record at build/SSR
time (preferred: the record is the CMS entry; the page is its print) or,
for client-rendered figures, set from the record by the same code path
that renders the table. The record for the worked day:

```json
{
  "date": "2026-04-14",
  "dateLine": "Tuesday the Fourteenth of April",
  "press": "The Ephemeris Press",
  "sunrise": "06:04", "transit": "12:58", "sunset": "19:52",
  "dayLength": "13h 48m",
  "moonrise": "05:12", "moonset": "15:36",
  "moonIllumination": 18, "moonPhase": "waning crescent",
  "eveningPlanet": { "name": "Venus", "sets": "21:47", "elongation": "24° E" },
  "correction": { "field": "moonrise", "from": "05:21", "to": "05:12" },
  "price": { "monthly": "£6", "yearly": "£60" },
  "subscribers": 214,
  "backNumbers": [
    { "date": "2026-04-13", "sunrise": "06:06", "sunset": "19:50", "moon": 27 },
    { "date": "2026-04-12", "sunrise": "06:08", "sunset": "19:48", "moon": 36 },
    { "date": "2026-04-11", "sunrise": "06:11", "sunset": "19:46", "moon": 45 }
  ]
}
```

**Motion spec.** None of its own — the record does not move; everything
else moves *from* it. Its rendering (the table, §6.9) carries the
motion. The record's one behaviour is the correction: when a figure is
corrected after first setting, the correction is appended to the record
(`correction` above) and every rendering of that figure gains §6.13's
tick — the record remembers being wrong, in public.

**Choreography timeline.** n/a as an element; its timeline is the day's:
computed before dawn → set in the morning's page → corrected if the
proofreader catches an error (§6.13) → archived at midnight into the
back numbers (§6.12), where its figures freeze forever (a back number
is never re-set; yesterday's sheet said what it said, errata slips
notwithstanding — the slip is *attached* to the archive copy, §6.18).

**State matrix.** *Current day:* live record, correctable (with the
correction shown). *Archived:* frozen; corrections arrive only as
attached errata. *Missing (a date with no issue):* the record's absence
is itself data — the back-numbers drawer prints its slip (§6.12).
*Focus/disabled/hover:* n/a (data, not a control).

**Breakpoints.** n/a — but its *renderings* obey theirs (§6.9, §6.7,
§6.18's colophon). The record's figures are identical at every width:
the day does not change size with the screen.

**Edge cases & failure modes.** The arithmetic must reconcile, and the
worked record demonstrates the checks §10 enforces: sunset − sunrise =
19:52 − 06:04 = 13h 48m = `dayLength` ✓; transit = the midpoint
(06:04 + 19:52)/2 = 12:58 ✓; the arc's crown tick (§6.7) sits at the
transit; moonrise 05:12 precedes sunrise (a waning crescent rises
before the sun) and moonset 15:36 falls in the afternoon ✓; back
numbers walk 2 minutes per day toward today's times ✓; the
subscription's next number is 214 + 1 = 215 (§6.14) ✓; the moon
illumination falls day by day in the back numbers (45 → 36 → 27 → 18)
toward the new moon ✓. A record failing any derivable check does not
publish — the gate (§10) computes them.

**Accessibility.** The record's renderings are the accessible content
(§6.9's table above all). The JSON island is not itself announced. The
correction, when present, is rendered as text (§6.13), never as data
alone.

**Tokens.** None — the record consumes no styling. (Its figures' tokens
live with their elements.)

**Content-merge.** Total: the record *is* the content, declared once.
Every other element in this section names the field it prints. A
builder who types a time anywhere else has committed the theme's one
unforgivable misprint (§9, §10).

**Failure fallback & watchdog.** If the record fails to load on a
client-rendered page, no figure renders at all and the table forme
shows §6.16 then §6.18's slip — the press prints nothing rather than
something unchecked. A page with half its figures is worse than a page
with none, and the theme chooses none.

**Reduced motion.** n/a.

**Performance & mobile.** One small JSON block (~600 bytes for the
worked record); SSR rendering preferred so the record costs the client
nothing.

### 6.18 The errata slip — 404 & empty states

**What & why.** Every print shop keeps errata slips: small printed
corrections tipped into a finished book. The theme's error states are
errata slips — a small forme, set apart, in which the Pressman admits
the fault in plain words and prints the way back. A 404 here is not a
dead end; it is the shop owning a misprint, which is the most on-brand
thing an error page can do.

**Structure.** A single small forme centred in the chase: the slip's
head in Playfair ("Errata"), the fault stated in Garamond ("The page
you asked for was not in today's forme — it may have been set under
another date, or not set at all."), the day's date line, and the ways
back set as sorts: *Today's sheet* (home), *The back numbers* (the
archive, §6.12), and a search line ruled like §6.14's fields ("Ask the
compositor" — the search input, whose results are returned as a list of
formes). The slip carries one proof-red annotation: a circled "?" in
the margin, drawn, still. The colophon forme (§ below) still closes the
page — an error page is still a page of the paper.

**Motion spec.** The slip locks in as §6.3 (it is a forme). The circled
"?" draws once, 450ms `--ease-peel`, after the lock — the proofreader
marking the fault. Nothing else moves; an error page that performs is a
shop that isn't sorry. Search results, when they come, set as a
miniature index (§6.12's stagger at half length).

**Choreography timeline.** Page arrives (via §6.15's peel if in-app) →
slip locks t=0–520 → t=700 "?" draws → slip at rest. The reader's next
action is the content: the three ways back are pressable sorts (§6.8)
from the first frame.

**State matrix.** *404:* as spec. *Empty search:* the slip's variant —
"Nothing in the case answers to that name" + the nearest formes (the
day's table, the current month's back numbers) offered as sorts.
*Empty archive month:* §6.12's miniature slip, same voice. *Server
error (500):* the slip in its plainest form — fault admitted, no
decoration beyond the lock, the colophon present (a 500 page in this
theme still signs itself). *Focus:* on arrival via navigation, focus
lands on the slip's heading (the SPA rule, §6.15). *Touch:* identical.

**Breakpoints.** ≥1200px: slip in the 7-column measure. 768–1199px:
9 columns. <768px: full measure; the three way-back sorts stack as a
small case (§6.10's mobile treatment in miniature).

**Edge cases & failure modes.** A URL that names a real but *future*
date: the slip says so — "That day has not been set yet — the press
prints at dawn" — and offers today's sheet: the error knows the
difference between missing and unborn. A URL for a date in the gap (the
press's repaired March, §6.12): the slip names the gap. The slip never
prints a figure that isn't in a record: its date line is today's
record date or, if even that failed, no date line at all — an errata
slip with a wrong date would be a second erratum.

**Accessibility.** Real heading, real text, real links and a real
search form with a labelled input. The "?" annotation is `aria-hidden`.
HTTP status is correct (404/500) — the theme's honesty extends to the
protocol. Contrast throughout is the page standard (ink on cream).

**Tokens.** `--ink`, `--proof` (the "?"), `--paper-shadow`,
`--ease-clunk`, `--ease-peel`.

**Content-merge.** The slip's ways back are the site's real sections,
its date is the real record's, and its voice is the Pressman's (§12) —
the error page is made of the site, not of a generic apology template
with the logo swapped in (the exact failure §9 names).

**Failure fallback & watchdog.** The slip is server-rendered static
HTML — it *is* the fallback, for the whole site. If even the slip's
assets fail, its text remains: a bare errata slip in browser-default
type still admits the fault and links home, which is more than most
error pages manage fully dressed.

**Reduced motion.** The slip stands printed, "?" drawn. Nothing moves.

**Performance & mobile.** Static; the lightest page on the site, as an
error page should be. Mobile: stacked sorts (above).

**The colophon forme (closing note).** The original entry's ninth
element — the honest colophon — closes every page including this one,
and its build spec lives here because it is the page's foot: a full
final forme printing the typefaces used (Playfair Display, EB Garamond
— named, never "our fonts"), the credit "Set by hand at the Ephemeris
Press", and the reader's hemisphere's actual sunrise and moonrise for
today, set as figures (§6.6) from §6.17's record (on the worked day:
sunrise 06:04, moonrise 05:12 — the same figures the hero peeled and
the table set; a colophon disagreeing with its own page is §9's first
misprint). It locks last, its gold-on-ink band (§2's one licensed gold
lettering) carries the press's name, and the treadle ornament (§6.5)
stands in its margin on mobile, where the hero had no room for it. Its
watchdog, fallback and reduced-motion behaviour are §6.3's and §6.6's —
it is a forme with figures, and it obeys their rules.

---

## 7. Page application map

| Page | How the theme plays |
|---|---|
| **Home / today's sheet** | The full ceremony: job-case nav (§6.10), headline set sort by sort (§6.1), proof pull (§6.2) over the key figures, the day's table forme (§6.9), the proofreader's forme (§6.13), back numbers (§6.12), subscription forme (§6.14), colophon (§6.18). The solar arc (§6.7) runs the margin. |
| **A day page (detail)** | The same formes for one date, arrived at via §6.15's re-proof (no re-setting of the headline — the date line stands printed; the ceremony is for the front door). Archived days are frozen (§6.17) and carry any errata slip attached at the head of their table forme. |
| **Back numbers (listing)** | Month formes, each a drawer (§6.12); pagination by §6.15; the stick rule (§6.11) counts formes by month ("APRIL — FORME II OF III"). |
| **About / the method** | The proofreader's forme (§6.13) promoted to the page's centre; the treadle ornament (§6.5) at full size in the first forme; a forme of the shop's own history set as a forme like any other — no hero image, the press is the picture. |
| **Subscribe (conversion)** | §6.14 alone in the chase with the day's table forme above it — the reader decides with today's sky in front of them. |
| **Search** | "Ask the compositor" (§6.18's line) at the head; results as a miniature index (§6.12); no-results as the empty slip. |
| **Checkout / payment** | **Routed out of the theme.** The subscription forme takes the order slip; payment itself happens on the payment provider's own sheet, and the reader returns to an errata-free confirmation forme ("Your name is on the list — № 215") set in the theme. A press does not take card payments at the bed, and the theme does not pretend otherwise. |
| **404 / error** | §6.18's errata slip, colophon and all. |

---

## 8. Worked examples

### 8.1 The hero — the day's front door (worked day: Tuesday 14 April 2026)

**What the visitor sees.** The chase frames the page. At its head, the
job case (§6.10): compartments for *Today's Sheet · Back Numbers · The
Method · Subscribe*, with *Today's Sheet* held in the stick. Below, in
the hero forme, the treadle press rocks in the right margin among the
furniture. The date line sets itself sort by sort — "THE SKY FOR
TUESDAY THE FOURTEENTH OF APRIL" — 43 sorts; being over §6.1's 34-sort
threshold, the stagger compresses to 33ms and the line sets in ≈1.8s,
each sort landing with its squash (the compositor hurries, as §6.1
allows). The stick rule snaps beneath the line. Then the proof pull: the key-figures
panel peels over 1,200ms to reveal the printed impression — SUNRISE
06:04 · TRANSIT 12:58 · SUNSET 19:52 · MOONRISE 05:12 — and the four
figures set, digits snapping, as the peel clears them. In the right
margin the solar arc stands at its dawn foot: disc at 06:04, the arc
ahead of it empty gold-to-be.

**Scroll timeline.** 0–15% of the page: hero ceremony (above), furniture
of the hero forme packing as it settles. 15%: the stick rule takes up
"THE DAY'S TABLE — FORME II OF VII" as the table forme's head crosses
the reading line; the table locks with its clunk and sets row by row
(§8.2's neighbour). The reader has been in the shop for one screen and
has watched a headline made, a proof pulled, and a table begin to set —
the theme's whole argument, made before any persuasion is attempted.

### 8.2 Mid-page — the proofreader's forme

**What the visitor sees.** Forme IV of VII. Left: the miniature proof —
the day's first three rows (Sunrise 06:04 · Transit 12:58 · Moonrise
05:21) on a pale sheet. Right: the method, in three numbered paragraphs:
how the figures are computed, how they are read, how they are corrected.
As the forme's second third crosses the reading line, the strike draws
through 05:21 in proof red (300ms), the caret rises, and 05:12 sets
above the line in red — then inks, over 600ms, from red to ink: the
correction accepted. The marginal word fades in: *"read against the
almanac, 6.40 a.m."* The paragraph beside it (❷) says in prose what the
proof shows: the moonrise was first set as 05:21 and corrected to 05:12
before printing — the same 05:12 the hero peeled, the table set, and
the colophon will print (§6.17's correction record, shown at work).

**Scroll timeline.** Forme locks (520ms) → ❶ draws (the circled sunrise,
450ms) as the first third passes → strike + correction (~900ms) at the
second third → ❸ (the transit tick, "agrees") at the final third →
forme at rest, fully marked. A reader who scrolls fast gets the
watchdogs' version: the finished proof, all marks drawn — the story
survives its own performance being skipped.

### 8.3 The conversion — setting a name on the list

**What the visitor sees.** Forme VI of VII: the subscription forme
(§6.14), with the day's table forme directly above it in the chase — the
sky they would receive is on the page they decide on. The offer is set
plainly: "The Daily Impression — one sheet, posted each morning. £6 per
month · £60 per year." The reader writes their name and postal address
on the ruled lines (the forme says why: "The sheet is posted; the
postman needs the address, the press needs nothing else."), picks the
Monthly sort, and presses SET MY NAME. The forme impresses (200ms), the
stamp falls — RECEIVED & SET, red, −3° — and the number sets beneath
it: "№ 215 on the list." A final line, in the Pressman's italic: "Your
first sheet is tomorrow's forme — the sky for Wednesday the Fifteenth
of April."

**Scroll/submit timeline.** Forme locks on arrival → fields fill at the
reader's pace (no timer anywhere — a press does not hurry a customer) →
submit press t=0 → stamp t=250 → number set t=450 → receipt complete,
focus on the receipt heading, the same words announced. Every figure in
the exchange — £6, £60, № 215, the Fifteenth of April — derives from
§6.17's record (214 subscribers + 1; the record's date + 1 day), and
§10's gate re-derives them before the page may ship.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **The disagreeing colophon.** The colophon prints a sunrise that
   differs from the hero's by a minute. *Cure:* every figure renders
   from §6.17's record; §10's figure audit greps the built page for
   time literals outside the record. There is no second source.
2. **The decorative moon.** A crescent icon at a cheerful angle while
   the table prints 18% waning. *Cure:* every phase disc is computed
   from the record's illumination (§6.9); a disc drawn freehand is a
   misprint, removed at the gate.
3. **Gold headlines.** Gold size lettering on cream (2.7:1) because it
   "looks premium". *Cure:* §2's pairing law — gold letters live only
   on ink. A gold headline is the fastest way to make this theme look
   like a wedding invitation template.
4. **The fade-in forme.** Sections fading and rising softly like every
   SaaS page. *Cure:* the clunk (§6.3) — travel, hard stop, settle,
   marks ink. If it fades, it isn't this theme.
5. **Red everywhere.** Proof red used as a general accent — buttons,
   links, headings. *Cure:* the ration (§2): one red element per forme,
   and red means *correction*. A page shouting in red is a proof that
   failed.
6. **The spinning loader.** Any spinner, anywhere. *Cure:* standing
   type (§6.16). A shop with a spinner has admitted it is a website.
7. **Furniture as decoration.** Wood-texture backgrounds, clip-art
   blocks scattered for "vintage feel". *Cure:* furniture exists only
   in forme margins, sized to the space the content leaves (§6.4) —
   it is computed, not sprinkled.
8. **Invented figures.** A "daily" table whose times are static, or a
   subscriber count typed by hand. *Cure:* the record (§6.17) and its
   derivable checks; a figure that cannot be re-derived does not print.
9. **The grunge filter.** Distressed textures, coffee stains, torn
   edges — heritage as dirt. *Cure:* this shop is *clean*; its age
   shows in process (setting, locking, correcting), never in decay.
   Misregistration is 0.4px, not a smear.
10. **The mascot pressman.** A cartoon compositor waving from the
    footer. *Cure:* the press's characters are voices (§12), not
    mascots; the treadle ornament (§6.5) is a machine, drawn straight.
11. **Bold body text and sans labels.** A builder's habits leaking in.
    *Cure:* §3's laws — Garamond italic emphasises; caps labels label;
    there is no sans in the building.
12. **The endless archive.** Infinite scroll on the back numbers.
    *Cure:* drawers and pages (§6.12) — a drawer is finite, and its
    finitude is the browsing pleasure.

---

## 10. Quality gate

Blocking checks — the theme may not ship on a page that fails any:

1. **Figure audit.** Every time/count on the built page matches
   §6.17's record exactly; the record's derivable checks pass (sunset
   − sunrise = day length; transit = midpoint; back numbers walk
   consistently; next subscriber № = count + 1).
2. **One-record grep.** No time literal (regex `\d{2}:\d{2}`) exists in
   templates outside the record and its renderings.
3. **Print test.** The page prints legibly and completely — formes,
   table, colophon — with all enhancement disabled. (It is a newspaper;
   this test is the theme's home turf and it must be perfect.)
4. **No-JS test.** Full content, full navigation, working form (§6.14),
   correct figures, colophon present.
5. **Watchdog drill.** With rAF forcibly stalled: headline set, peel
   resolved, formes printed, figures at value, transition layer gone —
   all within their elements' watchdog times.
6. **Law test.** No gold text on cream anywhere (automated contrast
   scan of rendered text); no red element beyond one per forme; no
   spinner in the codebase's component tree.
7. **Clunk test.** Every section locks with the §6.3 timing (travel,
   stop, settle, marks) — no fade-based reveal survives review.
8. **Reduced-motion pass.** With `prefers-reduced-motion`: the whole
   page is the printed sheet — no setting, peeling, rocking, drawing;
   all content present; the hidden progressbar twin still updates.
9. **Correction honesty.** If the record carries a correction, §6.13's
   forme shows it with the original legible under its strike; a silent
   figure swap anywhere is a release-blocking fault.
10. **Disc audit.** Every moon disc's filled fraction equals its
    printed illumination within 1%.
11. **Focus pass.** Every interactive element reaches §6.8's proof-red
    ring; the subscription forme's error flow (§6.14) is fully
    keyboard-completable; focus order = reading order on every page
    type in §7.
12. **Performance pass.** §14's budgets measured on a mid-tier Android
    device over a throttled connection: LCP ≤ 2.5s, shared loop
    ≤1.2ms/frame, no long task > 50ms after load.

The gate is signed by a non-builder (the proofreader's role, §12) —
the person who set the page does not pass their own proof.

---

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components the theme refuses are listed with their in-theme replacement
— a refusal without a replacement is a gap, not a stance.

| Component | Treatment in this theme |
|---|---|
| **Buttons (primary)** | A large sort: ink face, Playfair small caps, §6.8 impression on press, proof-red focus ring. Label is a verb from the shop ("SET MY NAME", "PULL THE PROOF"). |
| **Buttons (secondary)** | An un-inked sort: `--paper-shadow` face, ink label, same press. |
| **Links (in text)** | Garamond, ink, underlined with a hairline rule that thickens on hover (the pencil under the line); §6.8 press on activation. Visited links ink to `--ink-70` — a read line is a lighter line. |
| **Text inputs** | Ruled lines (§6.14): transparent field over a rule, caption-cap label above; focus thickens the rule; error turns it proof red with the proofreader's note beneath. |
| **Textareas** | The slip grows downward (§6.14) — ruled lines multiply; never a boxed box. |
| **Radio / checkbox** | Small sorts in a row; the chosen sort is inked full and pressed 1px into its line; the unchosen stand at `--ink-70`. |
| **Selects** | Refused as native dropdowns in formes; replaced by a row of sorts for ≤5 options, or a ruled line opening the job case (§6.10's tray, repurposed as a picker) for more. |
| **Tables** | §6.9 is the law: caption as running title, hairline rules, figures right-aligned to the colon, set row by row. |
| **Cards** | Back-number proof cards (§6.12): pale sheets, seeded rotation, miniature marks. No other card exists in the theme. |
| **Badges / tags** | A proof tick: small proof-red marginal mark + caps label. Used for "CORRECTED" and "NEW NUMBER" only — badges are corrections or they are noise. |
| **Alerts** | An errata slip in miniature (§6.18's language at forme scale): fault or news stated plainly, in the Pressman's voice, dismissible by a sort marked "FILED". Never a coloured toast. |
| **Toasts** | **Refused.** News in a print shop is printed in place (an alert slip in the forme it concerns), never floated over the page. |
| **Modals** | **Refused.** A modal is a page pretending not to be one; the theme uses a forme on its own page (via §6.15) or an expanding forme section. The one exception — none. |
| **Tabs** | A row of standing sorts along a forme's head; the active tab's sort is inked and its forme-section shows. Used for the back numbers' months when drawers multiply. |
| **Accordions** | Formes that lock open: the head stays, the body sets line by line (§6.9's row stagger). Used in the method page's particulars. |
| **Pagination** | "Next drawer / Previous drawer" sorts at the index foot (§6.12), with the drawer count set as figures ("DRAWER II OF IX"). |
| **Search** | "Ask the compositor" (§6.18): a ruled line + results as a miniature index. |
| **Breadcrumbs** | The stick rule (§6.11) carries wayfinding; a breadcrumb trail is a second instrument playing the same note — refused in favour of the rule + the case. |
| **Progress bars** | The solar arc (§6.7) is the only one. Linear bars are refused. |
| **Spinners** | **Refused** — standing type (§6.16). |
| **Tooltips** | A compositor's marginal note: Garamond italic, ink, on a `--paper-shadow` slip, appearing on hover/focus after 400ms. Carries only what a margin can carry (one line). |
| **Images / plates** | Admitted rarely, as *plates*: a photograph pasted into the forme under a printed plate mark ("PLATE I") with a caption in the compositor's caps; no scale-in, no parallax (§5). The shop's own drawings (treadle, discs, arc) are inline SVG in ink. |
| **Dividers** | A furniture course (§6.4) or a centred fleuron line — a hairline with a single ❦-equivalent drawn mark (an SVG lozenge, not an emoji) — between formes only. |
| **Footer** | The colophon forme (§6.18's closing note) — there is no other footer. |

---

## 12. Content & copywriting voice

Two voices, as §1 establishes, and the page never confuses them.

**The Compositor** sets and labels. Headlines, table heads, captions,
navigation: measured, tabular, in the trade's terms, never lyrical.
Headline style: the thing itself, dated and named — "The Sky for
Tuesday the Fourteenth of April", not "Your daily dose of wonder!".
Labels are caps Garamond: SUNRISE · SOLAR TRANSIT · MOONRISE. Numbers
are always figures, never words, in data; always words, never figures,
in dates in prose ("the Fourteenth of April").

**The Pressman** speaks in the colophon, the errata slip, the margins
and the error lines. Dry, plain, first person plural of the shop
("we"), admits faults without varnish. He never sells. The offer in
§6.14 is the Compositor's setting; the receipt's last line is the
Pressman's.

**Fixed strings (verbatim, do not paraphrase):**

- Colophon credit: *"Set by hand at the Ephemeris Press."*
- Errata head: *"Errata — the page you asked for was not in today's forme."*
- Subscription promise: *"Your first sheet is tomorrow's forme."*
- Empty compartment: *"NOT YET SET."*
- Clean proof: *"Read and passed, no corrections."*

**Error voice (the proofreader corrects, never scolds).** Errors are
correction notes, in italic, keyed to the line: ✓ "The address line
needs a town — the sheet is posted, and the postman is good but not
psychic." ✗ "Invalid address." ✓ "A name is wanted here — the list is
kept by name." ✗ "This field is required." The accessible announcement
states the correction plainly first; the wit is the printed form of the
same fact (§6.14).

**Empty-state voice.** Absence is stated as a shop fact: ✓ "No numbers
were pulled in March — the press was being repaired." ✗ "Nothing here
yet!" ✓ (search) "Nothing in the case answers to that name." ✗ "0
results found."

**Headline ✓/✗.** ✓ "The Sky for Tuesday the Fourteenth of April" ✗
"Unlock the Secrets of the Heavens". ✓ (method) "How the Figures Are
Read" ✗ "Our Rigorous Quality Assurance Process". The shop's grandeur
is in its exactness; any headline that reaches for wonder instead of a
fact has left the building.

---

## 13. Full-page scroll choreography map

The home page (today's sheet), top to foot. Beats key to the reading
line (62% viewport height, §4); the shared loop (§5) carries all
scrubbed values.

| # | Beat | What the visitor sees & feels |
|---|---|---|
| 1 | First paint | The sheet, printed: case, date line, key figures, treadle already rocking. Nothing is missing; everything that follows is the shop *re-making* what is already there. |
| 2 | The setting | The date line's 43 sorts travel and squash into the stick (≈1.8s); the stick rule snaps beneath. The reader watches the headline being made. |
| 3 | The pull | The proof peel lifts over the key-figures panel (1,200ms); the four figures set as it clears them. The day's data is *published* in front of the reader. |
| 4 | Forme II — the table | The table forme locks (clunk, marks ink); rows set line by line; the phase disc fills to 18%. The stick rule takes up "THE DAY'S TABLE — FORME II OF VII". The sun begins its arc in the margin. |
| 5 | Forme III — the day in prose | A text forme locks; its furniture packs as it settles. The day's events written out (Venus sets 21:47, elongation 24° E — the record's figures in sentences). |
| 6 | Forme IV — the proof | §8.2: annotations draw; the moonrise strike and correction; red becomes ink. Trust, performed. The arc's disc crosses the crown tick (transit, 12:58) as the forme passes mid-page. |
| 7 | Forme V — back numbers | The drawer sets card by card; yesterday walks toward today in 2-minute steps. |
| 8 | Forme VI — the subscription | §8.3's forme locks; the offer read against the table still in view above. The press waits — no beat fires until the reader acts. |
| 9 | The colophon | The final forme locks; the gold-on-ink band; the day's sunrise and moonrise printed again, agreeing. The sun disc reaches the arc's sunset foot (19:52) exactly as the colophon locks — the reader has read the whole day, and the margin says so. |
| — | Reverse pass | Scrolling up: nothing un-prints. Formes stay locked, figures stay set, the proof stays marked. Only the sun retreats along its arc — position is honest in both directions. |
| — | Jump scroll | A reader who jumps (scrollbar drag, End key) finds every crossed forme locked and set by the watchdogs — the press catches up by having printed, not by performing late. |

---

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Total page weight (home, first load) | ≤ 640KB — of which fonts ≤ 150KB (two families, subset to Latin + figures, `font-display: swap` with the §3 fallbacks), inline SVG ≤ 30KB, JS ≤ 90KB gz, CSS ≤ 45KB; the page carries almost no imagery by design (§11's plates are the exception and are lazy and rationed) |
| LCP | ≤ 2.5s on mid-tier Android, throttled 4G — the hero is text; LCP is the date line in its printed state, which never waits for the setting |
| Shared loop | ≤ 1.2ms/frame, all scrubbed values (furniture, arc, stick-rule tracking) in the one loop (§5); elements leave the active set when settled |
| Discrete animations | ≤ 0.5ms/frame each, transform/opacity/clip-path only; no layout animation anywhere (the squash is a transform; the peel is a clip-path) |
| Long tasks | None > 50ms after load; the setting's measurement pass is one read, one write phase |
| INP | ≤ 200ms; the impression (§6.8) is class-and-transform only |

**Cut order when the budget is exceeded** (in this order — the
ceremony is cut before the content, always): 1) the hero peel's curl
shadow gradient; 2) furniture blocks per forme 9 → 5; 3) the treadle
period doubles, then stills (§6.5's own degradation); 4) the headline
setting's blur settle; 5) the ghost layer on impressions. **Never
cut:** the watchdogs, the printed fallbacks, the table, the colophon,
the record — a page that drops its honesty to keep its decoration has
failed §9, not met §14.

---

## 15. Build-order checklist

1. **The record first.** §6.17's Day's Forme as data, with its
   derivable checks as unit tests (day length, midpoint, back-number
   walk, subscriber arithmetic). Nothing renders until the record
   reconciles.
2. **The printed page.** The whole home page as static HTML/CSS —
   formes, table, colophon — passing §10's print and no-JS tests
   before a line of motion code exists. This is the sheet; everything
   after is the shop performing it.
3. **Tokens & type.** §2's palette as CSS variables, §3's scale and
   bite; the pairing law enforced by a lint rule (gold-on-cream text
   fails the build).
4. **The chase & formes.** §4's layout: chase frame, registration
   marks, furniture margins as static packed blocks.
5. **The shared loop.** One rAF loop, lerp 0.12, per-forme settle
   values; the reading-line observer.
6. **The clunk.** §6.3's lock + watchdogs; verify the watchdog drill.
7. **Figures.** §6.6's set + the table's row stagger (§6.9).
8. **The hero ceremony.** Sorts (§6.1), peel (§6.2), stick rule
   (§6.11) — in that dependency order.
9. **Furniture & arc.** §6.4's scrub, §6.7's arc + hidden progressbar.
10. **The treadle & sheen.** The two licensed ambient loops, with
    pause rules.
11. **Impressions.** §6.8's delegated press on all controls.
12. **The case.** §6.10's navigation with its stick.
13. **The proof forme.** §6.13's drawn corrections + the record's
    correction rendering.
14. **The subscription forme.** §6.14 complete: fields, errors,
    stamp, receipt, network-failure line; prices and numbers bound
    to the record.
15. **Transitions & skeletons.** §6.15's re-proof, §6.16's standing
    type with its 4,000ms errata handoff.
16. **The errata slip & remaining pages.** §6.18 (404, empty, 500),
    then §7's other page types from the same formes.
17. **The gate.** §10, all twelve checks, signed by a non-builder.
    Only then may the press print for the public.
