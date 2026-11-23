# 15. The Corrections Column — Expanded (v1 + v2)

The site is a corrections column that never closes: a brand leading with its
own mistakes, every claim on the page issued twice — once as it was
"originally published", struck through in the margin, and once as the
corrected statement, pasted over the error on a paper slip. This document is
the complete build specification. Where it disagrees with the short library
entry, this document is the build target.

---

## 1. Concept & world

**The story.** Every newspaper runs a corrections box; almost every brand
hides its own at the bottom of page two in 8pt type. The Corrections Column
inverts the shame: the errata *are* the front page. The site is typeset as a
standing corrections column in a broadsheet of record — a narrow statement
column, a wide margin carrying the struck-through originals, pasted paper
slips carrying the corrected readings, a red editor's line ruling the margin
from the first error to the last, and a ledger in the header that counts the
corrections as the visitor scrolls past them: *14 corrections and counting.*
The fiction is not decorative. The layout literally cannot present a claim
without also presenting its history: original and correction coexist in the
DOM, in the layout, and in the reading order, forever. Honesty is not the
tone of this theme; it is its grid.

**The mood.** Penitent, dry, faintly comic, and completely unembarrassed.
The paper is warm apology white, the ink is ordinary newsroom ink, the red
is the editor's pencil — used sparingly, only ever where something is being
corrected, dated, or counted. The editor's hand (Caveat) appears in the
margin the way a real editor's hand appears on a proof: briefly, personally,
and never in the reading text itself. The emotional arc of a page is fixed:
*we said this → it was wrong → here is the true statement → here is the date
we admitted it.* A visitor should leave trusting the brand more than if it
had never erred, because the page performs the admission instead of merely
claiming the virtue.

**Best-fit sites and audiences.**
- Journalism outlets and newsletters whose corrections policy is a selling
  point — the corrections index becomes the homepage.
- Transparency-first fintech: fee claims, rate claims, "no hidden charges"
  claims — each one issued, dated, and visibly amended when the lawyers or
  the facts change.
- Apology and rebrand campaigns: a company that mis-stated, mis-sold, or
  mis-shipped, rebuilding trust by publishing the full errata ledger.
- Public-sector and NGO transparency pages: amended figures, revised
  guidance, corrected reports.
- Any changelog-driven product that wants its "what we got wrong" page to
  carry the same weight as its marketing pages.

**When NOT to use it.**
- When there is nothing real to correct. The theme's entire authority comes
  from genuine, dated, cumulative errata. A brand that invents trivial
  "mistakes" ("we said our coffee was great; it is, in fact, excellent")
  turns the column into a joke at the reader's expense — §9 lists this as
  the theme's first slop mode. If the client cannot supply at least five
  real corrections with real dates, refuse the theme.
- For legal, medical, or safety corrections where an overlay interaction
  could delay comprehension: use the side-by-side static variant only
  (§6.2's reduced-motion layout as the permanent layout), never the
  slide-over ritual.
- For high-frequency transactional UI (checkout, banking flows) beyond a
  single framed statement — the margin ritual needs reading room; it
  collapses honestly below 768px (§4) but it does not belong inside a
  payment form.
- When the organisation's corrections are contested or under litigation:
  the theme publishes both versions permanently, side by side. That is the
  point, and it is a commitment, not a skin.

**The one law.** *No claim without its history.* Every corrected statement
on a page built in this theme ships with its original text, its correction
date, and its place in the running tally. A correction without a date is
set dressing; a tally that does not match the page's actual errata is a
lie the theme itself forbids (§10, blocking gate 1).

---

## 2. Palette

Four anchor inks, taken from the library entry unchanged. Derived tokens
are labelled **derived** and exist only to do jobs the anchors cannot do at
accessible contrast; no fifth hue is introduced. Red is rationed by law:
it appears only on strikes, the editor's line, date stamps, the tally, and
correction slips' edges — never as a generic accent, never as a button
colour, never in the reading text.

| Token | Hex | Role | Usage ratio | Pairing / contrast notes |
|---|---|---|---|---|
| `--paper` Apology white | `#FAF8F3` | The sheet: page ground, statement column, slip faces | ~78% of surface | Ground for `--ink` (≈15.0:1), `--red` (≈5.2:1), `--grey` (≈4.2:1) |
| `--ink` Ink | `#22201C` | Reading text, originals (at 78% for struck margin text), hairlines at 14% | ~16% | On `--paper` ≈15.0:1 — all body text, all sizes |
| `--red` Correction red | `#C22E2E` | Strikes, editor's line, date stamps, tally numerals, slip edge rule | ~3% | On `--paper` ≈5.2:1 — display and apparatus only; never body text below 18px |
| `--grey` Humble grey | `#7C766B` | Skeleton statements, secondary apparatus, the archive drawer's hush | ~3% | On `--paper` ≈4.2:1 — apparatus ≥14px semibold or non-essential text only |
| `--red-deep` (**derived**) | `#9E2424` | Small red text: slip meta lines, form error notes, the drawer's count | as needed | On `--paper` ≈7.2:1 — the only red permitted below 18px |
| `--ledger-grey` (**derived**) | `#5F594F` | Small apparatus text the reader must actually read: captions, ledger labels, form help | as needed | On `--paper` ≈6.4:1 — replaces `--grey` wherever text is essential |
| `--paper-shade` (**derived**) | `#F0EADD` | Slip undersides, the pasted edge strip, drawer interior, skeleton pulse base | as needed | A shadow of the paper, not a new colour; `--ink` on it ≈13.6:1 |
| `--hairline` (**derived**) | ink at 14% | Column rules, ledger rules, card borders | hairlines only | Never a text colour |
| `--shadow-paste` (**derived**) | `rgba(34,32,28,.25)` | The warm paste shadow under slips (§4) | — | Warm-neutral; never a cool grey-blue shadow |

**Dark-mode behaviour — the sheet under the desk lamp.** The theme does not
invert. A corrections column is a physical sheet; in dark mode the *desk*
darkens and the sheet stays a sheet. Concretely: the page background outside
the sheet (header bar surround, archive drawer exterior, footer ground)
becomes `#211F1B` (ink warmed 6% toward the red); every token *on* the sheet
— `--paper`, `--ink`, `--red`, all derived tokens — is mode-invariant, so
every contrast figure above holds in both modes and no element is re-specced
for dark. The sheet gains one addition: a lamp tint, a radial gradient of
`rgba(194,46,46,.03)` over `rgba(250,248,243,1)` centred at 30% 0%, felt
rather than seen. The archive drawer (§6.17) is dark in both modes — it is
the inside of a drawer, not a mode.

**Red rationing, stated as a build rule.** A page in this theme may not
contain red anywhere the design system has not licensed it: strikes (§6.9),
the editor's line (§6.3), date stamps (§6.5), the tally (§6.4), slip edge
rules (§6.1), error notes in `--red-deep` (§6.16), and the drawer's count
(§6.17). A red button, a red logo, a red sale badge — each is a §10 gate
failure, because red that means "sale" today cannot mean "we were wrong"
tomorrow.

---

## 3. Typography

Two faces only. **Source Serif 4** sets everything that is *published* —
statements, originals, stamps, apparatus. **Caveat** sets everything that is
*handwritten* — the editor's marginal notes, the "originally published"
labels, the apology's signature line. The hand never sets a statement; the
press never sets a note. That division is the theme's typographic law, and
§9 lists crossing it as a slop mode.

| Role | Face / settings | Size / line-height | Used by |
|---|---|---|---|
| Hero claim (wrong, then corrected) | Source Serif 4, 600 | 54px / 1.04, tracking −0.01em | §6.1, §6.14 |
| Page H1 | Source Serif 4, 600 | 40px / 1.1 | listing & record pages |
| Section statement lead | Source Serif 4, 600 | 30px / 1.22 | §6.2 corrected leads |
| Statement body (the reading text) | Source Serif 4, 400 | 20px / 1.6 | §6.2, articles |
| Slip claim line | Source Serif 4, 600 | 19px / 1.4 | correction slips |
| Margin original | Source Serif 4, 400 italic | 15px / 1.55, `--ink` at 78% | §6.2, §6.9 struck texts |
| Editor's note (the hand) | Caveat, 500 | 21px / 1.25, `--red-deep` or ink | margin notes, §6.10 signature |
| "Originally published" label | Caveat, 600 | 19px / 1.2, `--grey` → `--ledger-grey` at small sizes | §6.2 |
| Date stamp | Source Serif 4, 600, uppercase, `letter-spacing: .14em`, `font-variant-numeric: tabular-nums` | 12.5px / 1.3, `--red` | §6.5 |
| Ledger line & tally | Source Serif 4, 600, uppercase, tracking .12em; numerals tabular | 13px / 1.4 | §6.4 |
| Caption / apparatus | Source Serif 4, 400 | 13.5px / 1.5, `--ledger-grey` | captions, form help |
| Counter figures | Source Serif 4, 600, tabular-nums | 28px / 1.1 | §6.8 |

**Per-role rules.**
- *Statements* are never italic and never red. Italic is reserved for the
  struck originals — the typographic past tense. A corrected statement set
  in italic reads as doubt; the correction must read as fact.
- *Originals* are always set smaller than their corrections (15px against
  the correction's 19–20px). The eye must be able to tell, at a glance and
  without reading, which text is current law.
- *The hand* (Caveat) is rationed: at most one handwritten note per erratum,
  at most 12 words. An editor who writes essays in the margin is performing,
  not correcting. Caveat never appears below 19px — handwriting set small
  is illegible and precious.
- *Date stamps* are always full dates, always the date the correction was
  *published*, never the date of the original error, and never relative
  ("3 days ago" is banned — a ledger does not do relative time). Format:
  `14 MARCH 2026` in stamp caps.
- *Numerals* in the tally, the counters, and the drawer count are tabular
  and are computed from the DOM (§6.4), never typed by hand into the copy.
- Line length: statements 58–64ch (target 62ch); margin originals 24–30ch;
  slip claim lines ≤ 46ch — a slip longer than its claim is a paragraph
  wearing a costume (§9).

**Font loading.** Source Serif 4 (400, 600, italic 400) and Caveat (500,
600) — five files, ≤ 120KB total with `font-display: swap`. The layout is
fully readable in the fallback serif (Georgia); stamps and the tally are
positioned so a late font swap moves nothing by more than 1px (CLS budget,
§14).

---

## 4. Layout language

**The sheet and its two columns.** The page is one sheet, max width 1180px,
centred on the desk. Inside it, a two-track grid carries the whole fiction:

- **Margin track — 264px.** Carries the struck originals, the editor's
  notes, the date stamps, and (for the first three errata) the pinned
  standing apology. The margin is not a sidebar; nothing navigational,
  promotional, or decorative may be placed in it. If a component is not
  part of an erratum, it does not enter the margin.
- **Gutter — 48px.** Carries the editor's red line on a rail 24px from the
  margin track's right edge (§6.3). The gutter is otherwise empty: the
  line needs silence around it.
- **Statement track — minmax(auto, 62ch).** Carries the corrected reading
  text, slips, cards, and forms.

**The slip geometry.** A correction slip is a rectangle of `--paper` (never
white — a slip is cut from the same stock as the sheet) with: a 3px
`--red` edge rule on its glued (left) edge; padding 18px 22px; a paste
shadow `0 1px 2px rgba(34,32,28,.18), 0 10px 24px −8px var(--shadow-paste)`;
and an honest rotation. **Rotation law:** slips rotate 0.5–1.5°, sign
alternating by erratum index (odd entries −, even +), magnitude cycling
0.5° / 1.0° / 1.5° by index mod 3. The rotation is set in CSS from a
`--slip-rot` custom property per entry, so two builders produce the same
sheet, and so reduced-motion and print can zero it in one place. A slip
overlaps its claim by design: it is positioned over the struck claim's
position in the statement track, anchored to the glued edge, with the
original preserved beneath it in the DOM and in the margin (§6.1, §6.6).

**Section choreography.** The page reads as a sequence of errata, each one
a three-beat unit: (1) the margin shows the original and strikes it;
(2) the slip lands on the claim in the statement track; (3) the red line
draws through the gutter connecting them, and the tally ticks. Sections
that carry no correction (a plain about paragraph, a contact block) are
set in the statement track alone with an empty margin — the empty margin
is itself a statement: *nothing to correct here.* No page may run more
than two uncorrected sections consecutively; a corrections column that
goes quiet for a full screen has stopped being one (§10, gate 6).

**Density rules.** One erratum per section; never two slips on one claim;
never a slip on a heading alone (the slip corrects a sentence, and the
sentence ships with it). Vertical rhythm is an 8px base unit; errata are
separated by 96px of paper on desktop — the corrections need air around
them, because each one is an admission and admissions are not stacked like
banners. The archive drawer (§6.17) closes every page that carries three
or more errata; pages with fewer link to the drawer's home on the
corrections index instead.

**Whitespace as material.** The paper is the luxury. Margins stay empty
rather than useful; the gutter stays silent; the space between the struck
original and its correction is where the theme's meaning lives — the
distance between what was said and what is true. Any proposal to "use"
the margin for related links, ads, or social proof is refused in §9.

**Responsive geometry (summary; per-element detail in §6).**
- **≥1200px:** full two-track sheet as above; margin 264px, gutter 48px.
- **768–1199px:** margin narrows to 208px, gutter to 36px, statement
  measure caps at 58ch; slip rotation law unchanged; the apology pin
  (§6.10) still pins, for two errata instead of three.
- **<768px:** the sheet becomes one column and the fiction re-choreographs
  rather than squeezes: each erratum stacks as *original (struck, in a
  `--paper-shade` margin block) → red line becomes a 24px vertical rule
  between the two → slip below, rotation capped at 1°*. The red line's
  rail becomes a left border on the erratum unit. Nothing is hidden; the
  order — error first, correction second — is preserved at every width,
  because that order is the theme.

---

## 5. Full motion system

Motion in this theme is the physical life of a corrections desk: slips are
pasted, stamps thud, strikes are drawn by a hand, a red line is ruled down
a margin. Every duration below is a token; every easing is named; nothing
moves without a job in the fiction.

**Named easings (the desk's hand).**
- `--ease-paste: cubic-bezier(.22,1,.36,1)` — a slip sliding and settling
  onto paste: fast travel, long soft landing, no bounce (wet paper does
  not bounce).
- `--ease-strike: cubic-bezier(.65,0,.35,1)` — the strike draw: a steady
  hand, even speed, no flourish.
- `--ease-thud: cubic-bezier(.34,1.4,.64,1)` — the date stamp: overshoot
  on scale only, one beat, done.
- `--ease-peel: cubic-bezier(.7,0,.3,1)` — peels and corner lifts:
  reluctant start, accelerating release.
- `--ease-settle: cubic-bezier(.25,1,.5,1)` — tilts, sheens, and every
  small physical adjustment.

**Duration tokens.** `--dur-beat: 900ms` (the honest pause — a wrong claim
sits plainly before it is corrected); `--dur-slip: 500ms`;
`--dur-strike: 400ms` nominal (computed per claim, §6.9);
`--dur-stamp: 160ms`; `--dur-press: 130ms`; `--dur-peek: 240ms`;
`--dur-page: 400ms` (full-slip transition); `--dur-line: 0ms` — the red
line is scrubbed, never timed.

**Every motion term, in this theme's language.**
- **Scroll-triggered reveals** — the margin ritual (§6.2): sections do not
  "fade up"; they are *corrected* on entry, in reading order, once.
- **Parallax** — slips drift at a 0.92 scroll factor against the statement
  column (§6.2), paste shadows deepening with the lag; the only parallax
  on the page, and it is 8% — paper barely lags.
- **Pinned scenes** — the standing apology pins beside the first three
  errata (§6.10); nothing else pins. Pinning is the apology's privilege.
- **Masked line reveals** — slips reveal through a clip-path opening from
  the glued edge (§6.1): the glued side is down first, the free side
  lands last, exactly like paste.
- **Blur-to-sharp** — translated as *ink drying*: date stamps land at
  1.5px blur and dry sharp over 300ms (§6.5). Nothing else blurs; blur is
  wet ink, and the statements are always dry.
- **Animated counters** — the corrections tally (§6.4) and the days-since
  counter (§6.8), both counting real DOM facts, both landing on their true
  values with a 600ms count and no overshoot.
- **Progress indicators** — two, both diegetic: the editor's red line
  (§6.3) and the ledger fill under the header tally (§6.4). There is no
  third progress bar anywhere in the theme.
- **Marquees** — *refused, in-table, with reason:* a corrections column
  does not ticker. Breaking news belongs to the publications this column
  corrects. The ledger line (§6.4) occupies the header slot a marquee
  would want, and it moves only when a correction is passed.
- **Ambient loops** — two only: the paste-sheen shimmer crossing slips on
  a 9s cycle (§6.2), and the paper grain that breathes — opacity 0.5→0.65
  — only while the page is scrolling. Ambient motion that runs while the
  visitor is trying to read an apology is vandalism.
- **Micro-interactions** — corner-peek hover (§6.6), paste-press click
  (§6.7), pointer tilt on slips (≤ +1.5° beyond the rotation law, §6.6),
  stamp ink refresh (§6.7).
- **Page transitions** — the full-slip paste and peel (§6.12): the site's
  own unit, the slip, carries the visitor between pages.
- **Image treatments** — photographs are issued as corrections: they
  scale-in-frame (1.05→1) inside pasted slip frames (§6.11), and a
  photograph that replaces an earlier one carries the earlier one's
  caption, struck, in the margin like any other erratum.

**The one rAF loop.** All scrubbed and ambient motion — red line, slip
parallax, grain breath, sheen — runs in a single requestAnimationFrame
loop with lerp smoothing (factor 0.14 for the line, 0.10 for parallax).
The loop sleeps when the tab is hidden and when nothing is within 120vh
of the viewport. Triggered animations (strikes, stamps, slips) are CSS
transitions/animations fired by an IntersectionObserver at 30% entry —
never scroll-jacked, never scrubbed; a correction happens *to* the claim
when you arrive, it is not wound back and forth by your scrollbar. The
only scrubbed elements are the red line and the parallax lag, because
both are *positions*, not events.

---

## 6. Signature elements

Eighteen elements: the twelve signature elements of the library entry
(§6.1–§6.12) and six page-family elements (§6.13–§6.18). Every element
carries its full build spec and its v2 layers. Shared tokens (easings,
durations) are defined once in §5; colour tokens in §2.

### 6.1 The founding correction gesture

- **What & why.** The hero performs the brand's founding act on its own
  first sentence: the headline states the claim *wrong*, plainly, and sits
  there for a full honest beat; then a pasted correction slip slides over
  the wrong words carrying the true statement, and the struck hero word
  shudders once as it is covered. If a visitor sees nothing else, they have
  seen what the brand is. This is the theme's signature and its contract:
  the gesture must be exact, or the theme is a costume.
- **Structure.** An `<h1>` whose wrong claim is real text in the DOM
  (never an image, never split-letter spans that break reading). The
  correctable phrase is wrapped in `<span class="claim-wrong">`. The slip
  is an `<article class="slip slip--founding">` positioned over the claim,
  containing the corrected phrase in the same type size, a `--red` glued
  edge, and the correction's date stamp (§6.5). The struck original remains
  in the margin track as well, per §6.2 — the hero is erratum № 1 and is
  counted as such by the tally (§6.4).
- **Motion spec.** Beat: wrong claim plain for `--dur-beat` (900ms) after
  the hero is fully painted. Slip: `translateX(−108%) → 0` with
  `--ease-paste` over `--dur-slip` (500ms), clip-path inset opening from
  the glued (left) edge in the same 500ms; paste shadow grows from
  `0 1px 1px rgba(34,32,28,.12)` to the full §4 shadow across the slide.
  At the moment the slip's leading edge crosses the claim's midpoint
  (~300ms in), the struck word shudders: `translateX` 0→−1.5px→1px→0 over
  120ms, once. The strike across the hero word draws (§6.9) in the first
  200ms of the slip's travel, so the word is struck *as* it is covered.
- **Choreography timeline (v2).** t=0 hero painted, claim wrong and plain
  → t=900ms strike begins on the wrong word (200ms draw) → t=950ms slip
  starts sliding → t≈1250ms slip crosses claim midpoint, word shudders
  (120ms) → t=1450ms slip lands, shadow at full depth, date stamp thuds
  (§6.5, 160ms) → t=1610ms gesture complete; the tally (§6.4) ticks to
  include erratum № 1. Total: ≈1.61s, once, never repeated on the page.
- **State matrix (v2).** *Rest (pre-trigger):* claim plain, slip parked
  off-claim — desktop and touch identical. *Hover:* no hover state; the
  slip inherits §6.6 peek and §6.7 press once landed. *Focus:* the slip is
  focusable only if it contains a link; focus never re-triggers the
  gesture. *Active:* §6.7 press. *Scrolled-past:* landed state, static.
  *Disabled:* with JS disabled or the fallback fired (§6.1 fallback), the
  slip sits in its side-by-side position permanently — that is the
  disabled state, fully designed, not an error.
- **Content merge.** The slip covers the actual claim in the actual
  headline; the correction *is* the headline's final text. Remove the
  animation and the hero still reads: wrong claim struck in the margin,
  true claim in the column.
- **Failure fallback.** The 900ms law: if the slide has not completed
  900ms after its trigger (JS error, jank, interrupted tab), the slip
  snaps to the side-by-side fallback — positioned in the statement track
  directly beneath the claim, rotation kept, both texts fully readable.
  A watchdog timer, not the animation's `transitionend`, owns this
  decision. The true statement is never trapped under an unlanded slip.
- **Reduced-motion variant.** No beat, no slide, no shudder: the hero
  renders in the side-by-side state from first paint — struck original in
  the margin, corrected statement in the column, stamp present. Same
  information, same order, zero motion.
- **Breakpoints (v2).** ≥1200px: as specced, slip overlays the claim in
  place. 768–1199px: same, claim set at 44px. <768px: the slide-over is
  *not* performed — the stacked layout (§4) puts the struck claim in its
  shade block and the slip beneath it from first paint; a 500ms slide on a
  phone reads as a glitch, and the founding gesture's dignity matters
  more than its choreography. The beat and the stamp still occur (stamp
  thuds beside the slip).
- **Edge cases & failure modes (v2).** *Slow network / late fonts:* the
  beat timer starts at first contentful paint of the headline, not at
  `load`; if the serif swaps mid-beat, the beat extends by the swap
  duration so the wrong claim is never corrected before it has been read
  in final type. *Claim longer than the slip:* the slip grows to the
  claim's full box (slips are sized by content, §4) — a slip that covers
  only part of a wrong sentence is a §10 failure. *Scroll-away mid-
  gesture:* the gesture completes off-screen; it does not restart on
  return. *Repeat visits:* the gesture plays on every fresh page load —
  it is the brand's act, not a tutorial — but never twice within one
  page view.
- **Accessibility spec (v2).** Reading order in the DOM is: original claim
  (marked `<s>` semantics via `aria-label="Originally published, since
  corrected"` on the margin copy), then the corrected statement, then the
  date. The slip's corrected phrase is the `<h1>`'s accessible text — the
  parked wrong phrase inside the h1 is `aria-hidden` once the slip lands,
  and present (as history) in the margin copy, so a screen reader hears
  the correction as the headline and the original as its footnote, never
  the reverse. The shudder is decorative and `aria-hidden`. Focus order:
  headline → slip (if interactive) → ledger. No focus is moved by the
  gesture.
- **Performance budget & mobile variant.** One transform + one clip-path
  on one element, one SVG line: ≤ 0.5ms/frame in the shared loop, zero
  layout thrash (slip is absolutely positioned over reserved space, CLS
  contribution 0). Mobile variant: the stacked static form above — the
  cheapest element on the page.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--red`, `--paper-shade`,
  `--shadow-paste`, `--ease-paste`, `--ease-thud`, `--dur-beat`,
  `--dur-slip`, `--slip-rot` (set per entry, §4).

### 6.2 The margin ritual (per section)

- **What & why.** The theme's repeating unit and its heartbeat: every
  section is an erratum performed in three beats — the "originally
  published" version appears in the margin and is struck; the corrected
  version reads clean in the statement column; the red line (§6.3) links
  them. One ritual, repeated identically, is what makes a page feel like a
  column rather than a campaign.
- **Structure.** Each erratum is a `<section class="erratum">` containing:
  a margin block (`<aside class="erratum-original">`) with the Caveat
  label *"Originally published"*, the original text, and an inline SVG
  strike layer (§6.9); and a statement block (`<div
  class="erratum-corrected">`) with the corrected lead (30px), body
  (20px), and its slip where the correction replaces a specific claim
  inline (§6.1's slip pattern, at body scale). Both texts are full,
  ordinary, selectable DOM text.
- **Motion spec.** Trigger: section enters at 30% viewport. Beat 1
  (t=0): the original is simply *there* — originals never animate in;
  errors don't get entrances. Beat 2 (t=+120ms): the strike draws across
  the original (§6.9 timing). Beat 3 (t=+300ms): if the section carries an
  inline slip, the slip slides over its claim (`--dur-slip`,
  `--ease-paste`) and its stamp thuds (§6.5). Meanwhile the corrected
  column never moves at all — the truth is not animated; only the
  correction is. Slips parallax at the 0.92 factor (§5) with paste
  shadows deepening up to +20% alpha at maximum lag.
- **Choreography timeline (v2).** t=0 section crosses 30% → t=0 original
  static in margin, strike begins → t≈400ms strike completes → t=300ms
  (parallel) slip begins slide if present → t=800ms slip landed, stamp
  thudded → t≈960ms ritual complete; red line (§6.3) has scrubbed through
  the gutter alongside throughout. Rituals never overlap: if two sections
  enter within 300ms of each other (fast scroll), the second ritual is
  *skipped to its end state* — the column does not perform admissions in a
  blur; skipped rituals land instantly, fully readable.
- **State matrix (v2).** *Rest:* end state (original struck, correction
  clean) — this is also the no-JS state. *Hover:* margin original: none
  (history is not interactive); slip: §6.6/§6.7. *Focus:* corrected text
  is plain text; links inside it take the standard focus (2px `--ink`
  outline, offset 2px). *Active:* n/a for the section itself.
  *Scrolled-past:* end state, parallax released. *Disabled:* JS off =
  rest state permanently. Touch: identical, minus hover-dependent cues.
- **Content merge.** The ritual is not applied *to* the content; the
  ritual *is* the content's structure — original and correction are the
  section's two real texts, laid out in the grid the theme is built on.
- **Failure fallback.** Base CSS renders the end state: original visible
  and struck (the strike is an SVG overlay whose *final* path is the CSS
  default; JS rewinds it to draw the animation), corrected text clean.
  Any failure — no JS, observer failure, reduced data — leaves a fully
  readable erratum. The 900ms slip law (§6.1) applies to inline slips.
- **Reduced-motion variant.** End state from first paint: original struck
  (static SVG), correction clean, no parallax, no sheen. This variant is
  also the mandated permanent layout for legal/medical corrections (§1).
- **Breakpoints (v2).** ≥1200px: margin 264px, ritual as specced.
  768–1199px: margin 208px; strike timing unchanged; parallax factor
  0.95 (less room, less lag). <768px: stacked form (§4) — original in its
  `--paper-shade` block, 24px red rule segment, correction below; the
  strike still draws (it is cheap and it is the meaning), the slip does
  not slide (it is placed), parallax off entirely.
- **Edge cases & failure modes (v2).** *Original longer than the
  correction* (common — errors ramble): the margin block grows; the
  gutter line (§6.3) spans the taller of the two tracks. *Correction
  shorter than one line:* the slip is still a slip (min width 220px) —
  a three-word correction pasted properly reads as confidence, not
  emptiness. *Section with no original* (new content, nothing to
  correct): rendered as an uncorrected section (§4), no ritual, no fake
  erratum invented to fill the pattern. *Scroll back up:* rituals never
  reverse; the column's history, once performed, stays performed.
- **Accessibility spec (v2).** DOM order per erratum: original (with its
  "Originally published" label as a real heading-level-3 or
  `aria-label`), then corrected text. Screen-reader users therefore hear
  exactly what sighted users see, in the same order: error, then truth.
  The strike SVG is `aria-hidden`; the struck semantics are carried by
  the label and by `<s>` on the original's key phrase. Contrast: original
  at ink 78% on paper ≈ 9.4:1 — struck text is still *read*, so it is
  still held to a text contrast bar, deliberately.
- **Performance budget & mobile variant.** Per section: one SVG path
  animation + at most one slip transform; sections outside 120vh are
  fully inert. Page budget: ≤ 12 rituals armed at once (§14). Mobile:
  parallax and sheen cut; strike draw kept (one path, ≤ 0.2ms/frame).
- **Tokens consumed (v2).** `--paper`, `--paper-shade`, `--ink`, `--red`,
  `--ledger-grey`, `--ease-strike`, `--ease-paste`, `--dur-strike`,
  `--dur-slip`, `--slip-rot`.

### 6.3 The editor's red line

- **What & why.** A single red rule ruled down the gutter, drawn by
  scrolling, that physically passes through every erratum — touching each
  margin original and each correction slip in turn. It is the theme's
  progress indicator and its thesis in one stroke: follow the line and
  you have audited the page. It replaces every conventional scroll
  progress bar, and it is the only one permitted (§5).
- **Structure.** An SVG (or a `scaleY`-transformed div — SVG specified, so
  the line can step around slips) living in the gutter rail (§4): a 2px
  `--red` path whose route runs vertically, with a 14px horizontal tick
  into the margin at each original and a 14px tick into the statement
  track at each slip. Ticks are part of the path, drawn as the line
  reaches them. The path's total geometry is computed from the errata's
  DOM positions on load and on resize.
- **Motion spec.** Scrubbed, never timed: line length = page scroll
  progress mapped through the shared rAF loop with lerp factor 0.14, so
  the line trails the scrollbar by a few frames like a hand following a
  finger. Draw via `stroke-dashoffset`. When the line's head passes an
  erratum's midpoint, that erratum's tally event fires (§6.4) — the line
  is the counting mechanism, not a decoration beside it.
- **Choreography timeline (v2).** Continuous, beat-locked to scroll:
  head enters gutter at page top (tied to first erratum's original) →
  descends at lerped scroll pace → tick draws into margin as head passes
  each original's vertical centre (±40ms of draw at 60fps) → tick draws
  toward the slip as head passes the correction → line terminates at the
  archive drawer's rule (§6.17), where it stops dead — the audit ends at
  the drawer.
- **State matrix (v2).** *Rest (top of page):* line at zero length, head
  at the first erratum. *Hover/focus/active:* none — the line is not
  interactive on desktop or touch. *Scrolled-past (scrolling up):* the
  line *retreats* with scroll (it is a position, §5) but ticks, once
  drawn, stay drawn — the audit trail does not un-happen; only the head
  position is reversible. *Disabled:* JS off → the line renders fully
  drawn at 40% opacity (a static ruled margin), ticks included.
- **Content merge.** The line's route is generated from the errata
  themselves; move a section and the line re-routes. It connects nothing
  but this page's own mistakes to this page's own fixes.
- **Failure fallback.** If path computation fails or JS is off, the CSS
  default is the fully-drawn static line at 40% opacity. The margin reads
  as ruled paper; nothing is lost but the drawing.
- **Reduced-motion variant.** Fully drawn static line at 40% opacity from
  first paint; tally events fire from section entry instead (§6.4).
- **Breakpoints (v2).** ≥1200px: gutter rail as specced. 768–1199px:
  rail narrows with the gutter (36px); ticks shorten to 10px.
  <768px: the rail dissolves into per-erratum 24px vertical rules (§4) —
  each erratum carries its own segment of the line, drawn (scrubbed
  within its unit) as the unit passes; the continuous audit becomes a
  chain of admitted links, and the tally fires per unit as before.
- **Edge cases & failure modes (v2).** *Resize / late fonts:* path
  recomputed on a debounced resize and on `document.fonts.ready`; mid-
  scroll recompute preserves progress fraction, not pixel length.
  *Erratum added by client-side rendering:* the line re-routes and the
  tally denominator updates (§6.4) — a correction added live is added to
  the audit. *Very long pages (>40 errata):* the path is chunked into
  per-section segments to keep dash maths cheap; behaviour identical.
  *Print:* the line prints fully drawn at 40% — the audit trail is part
  of the document.
- **Accessibility spec (v2).** The line is decorative (`aria-hidden`); its
  information content — how many corrections you have passed — is carried
  accessibly by the ledger tally (§6.4), which is live-region polite and
  throttled. No meaning exists only in the line.
- **Performance budget & mobile variant.** One path, one dash-offset write
  per frame in the shared loop: ≤ 0.3ms/frame. Mobile: per-unit segments,
  same budget. No canvas, no WebGL, ever, for this element.
- **Tokens consumed (v2).** `--red`, `--ease-settle` (tick draw only),
  `--dur-line` (0ms — scrubbed).

---

### 6.4 The corrections-ledger header

- **What & why.** The header carries the column's running total as a dated
  ledger line: *"14 CORRECTIONS AND COUNTING"* above a hairline that fills
  as corrections are passed. It is the masthead of the fiction — a real
  corrections column prints its tally where other papers print their
  slogan — and it is the accessible carrier of the red line's information
  (§6.3). The count is this page's actual errata, counted from the DOM.
- **Structure.** A sticky header: left, the publication name (Source Serif
  4, 600, 20px); right, the ledger block — the tally line (13px caps,
  §3) with its numeral in tabular figures, and beneath it a 120px × 2px
  ledger rule (`--hairline` track, `--red` fill). On listing pages the
  ledger line reads the *site's* total ("212 CORRECTIONS SINCE 2019");
  on article pages it reads the *page's* count. The two denominators are
  never mixed on one line (§13 voice rules).
- **Motion spec.** The tally numeral counts up 600ms (`--ease-settle`,
  no overshoot — a ledger does not bounce) each time the red line passes
  an erratum (§6.3) or, in reduced/no-JS counting, when an erratum enters.
  The ledger fill's width = passed/total, lerped in the shared loop
  (factor 0.14, same as the line, so header and gutter never disagree).
  The header itself never animates on scroll (no shrink, no hide): a
  ledger you cannot see is a ledger you cannot audit.
- **Choreography timeline (v2).** Page load: tally starts at the count of
  errata already passed (0 on a fresh article) and the denominator is set
  from the DOM count → each line-pass event: numeral counts to the new
  value over 600ms, fill lerps alongside → at the final erratum: numeral
  lands, fill completes, and the ledger line's wording flips from
  "AND COUNTING" to the full stop form "14 CORRECTIONS. THAT IS ALL OF
  THEM." for exactly as long as the visitor remains below the last
  erratum — scroll back above it and "AND COUNTING" returns. The flip is
  a text swap, no animation; ledgers do not celebrate.
- **State matrix (v2).** *Rest:* current count, current fill. *Hover:*
  the ledger block is a link to the corrections index on listing pages
  (underline draws, §11) and plain text on article pages. *Focus:* as
  hover, with the standard focus outline. *Active:* press per §11
  buttons/links. *Scrolled-past:* n/a — the header is sticky, it has no
  scrolled-past state; that is the point. *Disabled:* JS off → the tally
  renders the page's total statically ("14 CORRECTIONS ON THIS PAGE")
  and the fill renders complete at 40% opacity. Touch: identical; the
  ledger block's tap target, when linked, is ≥ 44px tall.
- **Content merge.** The tally counts this page's real errata, in the
  header where a corrections column prints its running total. It is
  computed, never written (§10, blocking gate 1).
- **Failure fallback.** Static total, static complete fill at 40%, as in
  the disabled state. A header that shows a wrong *live* count is worse
  than a static one — if the counting script fails, the fallback is the
  honest static total, and the failure is invisible to the reader.
- **Reduced-motion variant.** Numeral swaps instantly at each pass event;
  fill jumps to its fraction. Wording flip unchanged (it is text, not
  motion).
- **Breakpoints (v2).** ≥1200px: full ledger block. 768–1199px: the
  ledger rule shortens to 80px; wording unchanged. <768px: the header
  stacks — name on line one, ledger line beneath it at 12px, fill full
  width of the header; the tally is never dropped at any width (dropping
  the count on mobile would exempt phone readers from the audit).
- **Edge cases & failure modes (v2).** *Zero errata on the page:* the
  ledger reads "NO CORRECTIONS ON THIS PAGE. YET." — the theme's driest
  line, and the only permitted joke in the header. *Errata added live:*
  denominator recomputed, fill re-fractioned, wording stays honest.
  *Count > 999:* tabular figures, no abbreviation — a ledger writes
  1,204, not 1.2k. *Sticky header + anchor jumps:* anchor targets offset
  by header height + 16px so a jumped-to erratum is never under the
  ledger it is about to increment.
- **Accessibility spec (v2).** The tally is `aria-live="polite"` but
  throttled by design: it announces only the *landing* value, at most
  once per erratum, and never mid-count. The fill is `aria-hidden`
  (the numeral carries the fact). Header landmark order: name → nav
  (§6.13) → ledger. Contrast: ledger text in `--ink` (≈15:1); the word
  "CORRECTIONS" may be `--red` only at ≥13px semibold caps (5.2:1,
  apparatus-grade, §2) — the numeral itself is always ink.
- **Performance budget & mobile variant.** One textContent write per
  count, one transform per frame for the fill: negligible. Mobile: as
  specced above; the count-up shortens to 300ms (smaller numbers,
  shorter patience — the value is identical).
- **Tokens consumed (v2).** `--paper`, `--ink`, `--red`, `--hairline`,
  `--ease-settle`.

### 6.5 Date-stamp thuds

- **What & why.** Every correction is dated, and the date arrives like a
  rubber stamp hitting the desk: fast, heavy, final. The stamp is the
  theme's proof of accountability — an undated correction is a rumour —
  and its little violence is the only slapstick the theme permits itself.
- **Structure.** A `<time class="stamp" datetime="2026-03-14">14 MARCH
  2026</time>` in stamp caps (§3), `--red`, rotated −2°, positioned at the
  slip's top-right corner overlapping its edge by 6px — stamped *onto*
  the slip, not typeset inside it. On margin originals without slips, the
  stamp sits at the margin block's top-right.
- **Motion spec.** On its erratum's ritual (§6.2, beat 3): scale
  1.25 → 1 with `--ease-thud` over `--dur-stamp` (160ms), rotation
  settling from −5° to its resting −2°, and the ink drying: filter blur
  1.5px → 0 over 300ms (§5's blur-to-sharp). Stamps stagger 90ms apart
  when two errata enter together. After landing: a 1px ink spread
  (text-shadow 0 0 0.5px currentColor) fades in over 200ms — the ink
  soaking into the paper.
- **Choreography timeline (v2).** Trigger (ritual beat 3, or §6.1 t=1450ms
  for the founding slip) → t=0 stamp at scale 1.25, −5°, blurred 1.5px,
  opacity 0 → t=40ms opacity 1 → t=160ms scale/rotation landed (thud) →
  t=300ms blur fully dried → t=360ms ink spread complete. The stamp is
  the last thing to happen in every ritual; the date seals the admission.
- **State matrix (v2).** *Rest:* stamped, dry, −2°. *Hover:* none on the
  stamp itself; when its slip is peeked (§6.6) the stamp rides the slip.
  *Focus:* stamps are not focusable (they are `<time>`, read in flow).
  *Active:* §6.7's press refreshes the stamp's ink (opacity pulse 1 →
  0.55 → 1, 260ms) — re-affirmed just now. *Scrolled-past:* rest.
  *Disabled:* JS off → stamp present, dry, at rest rotation from first
  paint. Touch: identical; no hover behaviours attach to the stamp.
- **Content merge.** The stamp dates the correction it physically sits
  on; its `datetime` is the correction's real publication date from the
  content system — never the build date, never "today" computed at
  runtime (§9: a stamp that always says today is a prop).
- **Failure fallback.** Static stamp, dry, present. The thud is theatre;
  the date is the content, and the content never depends on the theatre.
- **Reduced-motion variant.** Stamp present at rest from first paint; the
  §6.7 ink-refresh becomes an instant opacity swap (still a refresh, no
  pulse).
- **Breakpoints (v2).** ≥1200px and 768–1199px: as specced. <768px: the
  stamp sits at the stacked slip's top-right as before; thud scale range
  softens (1.15 → 1) — a smaller desk, a lighter stamp — duration
  unchanged.
- **Edge cases & failure modes (v2).** *Long dates / locales:* the stamp
  format is fixed `DD MONTH YYYY` in the publication's language; the box
  sizes to content, and a stamp wider than its slip right-aligns to the
  slip's edge rather than shrinking its type. *Same date on many
  corrections:* fine — a bad day at the publication is a historical fact,
  and the tally (§6.4) still counts each one. *Correction updated:* the
  stamp is *joined* by a second, smaller stamp ("AMENDED 02 MAY 2026")
  beneath it — stamps are never overwritten; the record accretes (§9).
- **Accessibility spec (v2).** `<time datetime>` gives machines the ISO
  date; the caps-and-tracking styling is visual only. The stamp is read
  in DOM order immediately after its correction. Contrast: `--red` at
  12.5px semibold caps on paper ≈ 5.2:1 — apparatus-grade per §2, and the
  same date is always repeated in `--ledger-grey` in the erratum's meta
  line for readers who need the higher-contrast copy.
- **Performance budget & mobile variant.** One transform + one filter on
  one small element per erratum; the blur is the only filter in the theme
  and it runs 300ms, once. Mobile: as above, cheaper by range, not by
  kind.
- **Tokens consumed (v2).** `--red`, `--ledger-grey`, `--ease-thud`,
  `--dur-stamp`.

### 6.6 Slip-corner peek hover

- **What & why.** A pasted slip invites one question: *what does it say
  underneath?* The peek answers it physically — hover lifts the slip's
  free corner and the visitor glimpses the original claim still sitting
  beneath its correction. Provenance you can lift. It is the theme's most
  tactile element and its most honest: the correction does not destroy
  the error; it covers it, and the cover can be raised.
- **Structure.** The slip (§6.1 structure) with `transform-origin` at its
  glued (left) edge. Beneath it, in the statement track at the identical
  position, the original claim set in margin-original style (15px italic,
  struck, §6.9) — present in the DOM always, visible only through the
  lifted corner's reveal (a clip-path wedge from the free corner,
  max 38% of the slip's width) and in the margin copy (§6.2). The lift is
  a `rotateY` tilt (6°) combined with a corner curl shadow gradient on
  the slip's underside (`--paper-shade`).
- **Motion spec.** Hover (or focus-within, or touch tap-toggle): corner
  lifts over `--dur-peek` (240ms, `--ease-peel`), rotation adds +2.5°
  from the glued edge per the source spec, shadow deepens +30%, the
  revealed wedge of original fades in at 120ms. Release: settles back
  over 200ms `--ease-settle`. Pointer-tracked tilt: while hovered, the
  slip's rotation follows the pointer's horizontal position by up to
  +1.5° beyond its lawful rotation (§4), lerped at 0.12 — the slip leans
  toward the hand that lifts it.
- **Choreography timeline (v2).** t=0 pointer enters → t=60ms shadow
  begins deepening → t=120ms wedge of original fully visible → t=240ms
  lift complete (2.5° + tilt) → held while hovered → pointer leaves →
  t=200ms settled flat. Focus-within runs the same timeline on focus
  events; the touch tap toggles between the two end states with the same
  durations.
- **State matrix (v2).** *Rest:* flat, pasted, original hidden beneath
  (and present in the margin). *Hover (desktop):* lifted as specced.
  *Focus:* focus-within lifts identically — keyboard users get the same
  provenance. *Active (touch):* first tap lifts and *holds* (the slip
  gains `aria-expanded` semantics via its toggle button behaviour when
  it carries one; a non-interactive slip on touch lifts on tap and
  releases on tap-elsewhere). *Scrolled-past:* flat. *Disabled:* no-JS →
  slips render in the side-by-side fallback (§6.1), where the original
  is simply *beside* the slip — the peek's information with no gesture
  required.
- **Content merge.** What is under the slip is the slip's own claim's
  original — the peek reveals content, not a tooltip, not a decoration.
- **Failure fallback.** Side-by-side state (§6.1 law): if transforms or
  clip-path fail, the slip never covers the claim in the first place.
- **Reduced-motion variant.** No lift. On hover/focus, the original
  appears in place beneath the slip as a static revealed block (the slip
  shifts down by its own height, layout reserved so nothing jumps) —
  provenance by disclosure, not by gesture.
- **Breakpoints (v2).** ≥1200px: full peek. 768–1199px: wedge narrows to
  30% (less room under a slip on a narrower sheet). <768px: no peek —
  the stacked layout (§4) already shows original and correction in
  sequence; a peek on mobile would reveal what is already on screen.
  Touch laptops (hover-capable) keep the hover behaviour.
- **Edge cases & failure modes (v2).** *Slip near the viewport edge:*
  the lift is transform-only; it never triggers scroll or reflow.
  *Rapid hover in/out:* transitions are interruptible and reverse from
  current value — no queue, no stuck corner (a stuck lifted corner is a
  §10 failure: it reads as damage, not interactivity). *Original longer
  than the wedge shows:* the wedge reveals the original's first lines;
  the full original is always one glance left, in the margin — the peek
  is a glimpse by design, and it never pretends to be the whole record.
- **Accessibility spec (v2).** The peek is an enhancement only: every
  fact under the slip exists in the margin copy in reading order, so no
  information is hover-gated. Where the slip is a link or button, its
  accessible name is the corrected claim, never "peek". Touch targets:
  interactive slips are ≥ 44px in their shortest dimension (slips are
  text blocks; this is inherent). Keyboard: focus-within lift, Esc
  releases the lift without moving focus.
- **Performance budget & mobile variant.** One transform + one gradient
  on one element; pointer tilt writes one CSS variable per frame, only
  while hovered. Mobile: cut entirely (see breakpoints) — the cheapest
  possible variant, because the layout already tells the truth.
- **Tokens consumed (v2).** `--paper`, `--paper-shade`, `--ink`,
  `--shadow-paste`, `--ease-peel`, `--ease-settle`, `--dur-peek`,
  `--slip-rot`.

---

### 6.7 Paste-press click

- **What & why.** Clicking a slip presses it flat into its paste — a small
  physical *yes, still true* — and its date stamp refreshes its ink, as if
  re-stamped in the moment. It is the theme's acknowledgement gesture: the
  reader doesn't "like" a correction; they press it, and the column
  confirms the correction stands as of now.
- **Structure.** The slip as a `<button>`-equivalent surface only when the
  product gives the press a function (e.g. "stand by this correction"
  counters in a transparency product); otherwise the slip is a plain
  article and the press is a pointer-only micro-interaction with no
  semantics. The stamp (§6.5) is a child of the slip so the refresh rides
  the press.
- **Motion spec.** Press: `scale .99` and paste shadow flattening to 40%
  depth over `--dur-press` (130ms, `--ease-settle`); release returns over
  180ms. Simultaneously the stamp's ink refreshes: opacity 1 → .55 → 1
  over 260ms, with the ink-spread text-shadow (§6.5) re-fading in — the
  stamp looks freshly wet for a quarter of a second. No sound, no haptic
  API, no confetti: a desk, not a game.
- **Choreography timeline (v2).** t=0 pointerdown → t=130ms fully pressed
  (scale .99, shadow flat) → t=130ms stamp opacity dips to .55 →
  t=260ms stamp back at full ink, spread re-set → pointerup → t=+180ms
  slip at rest scale and shadow. If the press carries a function, its
  result (e.g. a "stood by 41 readers" line in the slip's meta) updates
  at t=260ms, after the stamp has refreshed — cause, then record.
- **State matrix (v2).** *Rest:* pasted, stamp dry. *Hover:* §6.6 lift
  (the press composes with the lift: a lifted slip presses from its
  lifted angle). *Focus:* visible outline (§6.6); Enter/Space fire the
  press identically to pointerdown. *Active:* pressed state as specced.
  *Scrolled-past:* rest. *Disabled:* a slip whose function is unavailable
  (e.g. already pressed by this reader, in products that count presses)
  keeps its shape, loses its press (no scale), and its meta line says why
  in `--ledger-grey`: "You pressed this on 14 MARCH 2026." Touch: press
  on tap, with the §6.6 tap-lift taking precedence on first tap for
  peekable slips (first tap lifts, second tap presses — stated in the
  slip's `aria-label` where it matters).
- **Content merge.** The press acts on the slip itself, in place, and its
  only effect is on the slip's own record (stamp, meta line). It never
  opens, navigates, or decorates anything else.
- **Failure fallback.** Without JS the slip is a static article; if the
  press carries a function, the function is a real form submit / link
  underneath the enhancement (progressive enhancement, §6.16 pattern).
- **Reduced-motion variant.** No scale, no shadow change: the stamp's ink
  refresh becomes an instant opacity swap and the meta line updates. The
  acknowledgement remains; the squash goes.
- **Breakpoints (v2).** Identical at all widths; on <768px the stacked
  slips press with scale .995 (a smaller gesture on a smaller sheet) —
  the stamp refresh, the meaningful part, is unchanged.
- **Edge cases & failure modes (v2).** *Double-click / mash:* presses
  are idempotent within 600ms (debounced at the stamp, not the finger —
  the reader may press as often as they like; the record refreshes at
  most twice a second). *Press during the founding gesture (§6.1):*
  ignored until the slip has landed (t<1610ms) — you cannot affirm a
  correction that hasn't finished arriving. *Press on a slip whose
  correction was later amended:* the press affirms the *current* slip;
  amended slips (§6.5's second stamp) say so in their meta.
- **Accessibility spec (v2).** Interactive slips are real buttons with
  the corrected claim as their name and the press result announced via a
  visually-hidden `aria-live="polite"` line ("Correction of 14 March
  2026 re-affirmed"). Non-interactive slips expose no button role —
  theatre must not counterfeit function. Focus outline: 2px `--ink`
  offset 2px, visible against both paper and slip.
- **Performance budget & mobile variant.** Two property transitions on
  one element; the cheapest interaction in the theme. Mobile: as above.
- **Tokens consumed (v2).** `--paper-shade`, `--shadow-paste`, `--red`,
  `--ease-settle`, `--dur-press`.

### 6.8 The "days since last error" counter

- **What & why.** Beside the cumulative tally sits the column's other
  vital sign: how long the publication has now gone *without* erring.
  It counts up in the header stats — and, as the footer joke, it resets
  to 0 the moment the archive drawer (§6.17) opens, because opening the
  drawer means looking at an error, and the streak was only ever about
  not looking. It is the theme's one wink, and it is strictly rationed:
  this counter, and nothing else, is funny.
- **Structure.** A stat block in the header's right cluster (or the
  article's meta band on listing pages): label "DAYS SINCE LAST ERROR"
  (12px caps, `--ledger-grey`), figure in counter type (28px tabular,
  §3), computed from the most recent correction date in the site's
  errata data and *today's date at build/render time on the server* —
  never from the visitor's clock, which lies.
- **Motion spec.** On first entry into view: counts 0 → true value over
  900ms (`--ease-settle`), once. The reset: when the archive drawer
  opens, the figure swaps to 0 instantly (no count-down — a streak
  doesn't drain, it ends) and the label gains a Caveat marginal note,
  rotated −3°, reading *"you looked."* — the joke, delivered deadpan, in
  the editor's hand. Closing the drawer does not restore the number
  until the next page view; the column remembers being caught.
- **Choreography timeline (v2).** Page load: figure at true value if the
  header was never off-screen (no count-up for a number the reader may
  already have read — count-up runs only when the stat scrolls into view
  from below) → drawer opens (§6.17 timeline) → at drawer's t=+200ms the
  figure swaps to 0 and the Caveat note fades in over 200ms → drawer
  closes: figure stays 0, note stays, until navigation.
- **State matrix (v2).** *Rest:* true value (or 0 post-drawer). *Hover:*
  the stat is not interactive; hovering the drawer handle does not
  pre-reset it (the joke requires the act). *Focus:* the drawer handle's
  focus gives no preview of the reset. *Active:* the reset is bound to
  the drawer's open event only. *Scrolled-past:* rest. *Disabled:* JS
  off → the drawer is a static section (§6.17 fallback) and the counter
  shows its true value permanently — the joke is JS-enhanced, the fact
  is not. Touch: identical.
- **Content merge.** Both counters measure the column's own record: the
  tally counts corrections made; this counts days since the last one was
  needed. They are the same ledger read two ways.
- **Failure fallback.** Static true value, server-rendered. If the
  errata data is unavailable, the stat is omitted entirely — a missing
  stat is honest; a guessed one is a fabrication (§10, gate 1).
- **Reduced-motion variant.** No count-up: true value at first paint.
  The reset swap and note fade become instant. The joke survives
  reduced motion because it is timing, not movement.
- **Breakpoints (v2).** ≥1200px: header cluster as specced. 768–1199px:
  figure 24px. <768px: the stat moves to the meta band under the H1
  (the stacked header (§6.4) has no room for two stats and a ledger);
  the drawer reset still applies — the joke is layout-independent.
- **Edge cases & failure modes (v2).** *Last error was today:* the true
  value is 0 and no drawer is needed for the joke — the label's Caveat
  note reads *"today. sorry."* from first paint. *No errors ever:* the
  stat is not shown (a publication with no corrections has no business
  in this theme, §1). *Stale cached pages:* the figure is recomputed
  client-side from the server-stamped last-error date on load, so a
  cached page never claims a streak longer than the truth.
- **Accessibility spec (v2).** The figure's accessible text is the full
  sentence ("23 days since the last error") via visually-hidden text;
  the reset is *not* announced live — a joke whispered by a screen reader
  mid-read is an interruption, and the drawer's own heading (§6.17)
  carries the real information. Contrast: figure in `--ink` (≈15:1);
  label in `--ledger-grey` (≈6.4:1).
- **Performance budget & mobile variant.** One count-up, one text swap.
  Mobile: as above.
- **Tokens consumed (v2).** `--ink`, `--ledger-grey`, `--red-deep`
  (Caveat note), `--ease-settle`.

### 6.9 Self-drawing strike-throughs

- **What & why.** The strike is the theme's verb. It is never pre-drawn:
  when a section is entered, a red line draws itself across the wrong
  words at reading speed, in reading order — because a strike that simply
  *exists* is typography, but a strike that *happens* is an editor
  catching the error in front of you. This element is the engine inside
  §6.1 and §6.2; it is specced once, here, and referenced by both.
- **Structure.** Per struck phrase: an inline SVG overlaying the phrase's
  box, one path per line of wrapped text (multi-line phrases get one path
  per line, drawn in sequence), path drawn as a hand-ruled line — a
  gentle 1.5px vertical wobble via two mid control points, never a
  pixel-straight rule (a ruler-straight strike reads as CSS
  `line-through`, which is precisely the cheap reading this element
  exists to prevent; §9). The underlying text carries real `<s>`
  semantics in the DOM so the strike's meaning survives the SVG entirely.
- **Motion spec.** Draw: `stroke-dashoffset` from full to 0 with
  `--ease-strike`; duration computed per phrase:
  `clamp(300ms + 14ms × word count, 300ms, 500ms)` — a two-word error is
  struck briskly, a rambling one takes the hand longer. Multi-line:
  lines draw in reading order, 60ms gap between lines, total capped at
  700ms (beyond that, lines overlap their draws by up to 40%). The
  strike sits at 58% of the phrase's x-height — through the words'
  middles, like a pencil, not at the baseline like an underline.
- **Choreography timeline (v2).** Trigger (ritual beat 2, §6.2, or §6.1
  t=900ms) → t=0 dash offset full → draw proceeds at the computed
  duration → multi-line gaps at each line's completion +60ms → final
  line lands → t=+80ms a 0.5px settle (the path's opacity 0.92 → 1, the
  ink arriving). Strikes on one page fire in strict reading order; the
  observer queue (§6.2) enforces it even under fast scroll, skipping —
  never scrambling — rituals that were passed too quickly.
- **State matrix (v2).** *Rest:* fully drawn (the CSS default state; JS
  rewinds to animate). *Hover/focus/active:* none — a strike is not
  interactive on any device. *Scrolled-past:* drawn. *Disabled:* drawn,
  statically — the disabled state and the rest state are the same
  picture, by design. Touch: identical.
- **Content merge.** The line is drawn on the wrong words themselves, at
  their size, in their box. It is not a divider, a decoration, or a
  section ornament; remove a phrase and its strike goes with it.
- **Failure fallback.** The SVG's final path is the no-JS default: the
  strike is *present* unless JS successfully rewinds it for the draw.
  If SVG is unsupported (effectively never), `<s>`'s native line-through
  — suppressed only when the SVG layer is confirmed live — carries the
  meaning alone.
- **Reduced-motion variant.** Strike present statically from first
  paint. No exceptions, including the hero: the founding gesture (§6.1)
  keeps its beat and slide in standard motion, but under reduced motion
  even those go, and the strike — the meaning — remains.
- **Breakpoints (v2).** Identical at all widths; on <768px the stacked
  originals (§4) are narrower, so phrases wrap more and the multi-line
  rules do more work — durations recompute from the rendered line count,
  not the desktop one.
- **Edge cases & failure modes (v2).** *Font swap after measurement:*
  paths are recomputed on `document.fonts.ready` and on resize
  (debounced 150ms); a strike that no longer crosses its words is
  re-measured, never left floating (§10, gate 4). *Phrase edited in a
  CMS after build:* strikes are runtime-measured from the live DOM, so
  edited text re-strikes correctly with no rebuild. *Very long original
  (a whole paragraph struck):* permitted once per page maximum — a
  paragraph-long strike is a retraction (§7's retraction pattern), and
  the draw caps at 900ms with lines overlapping up to 60%.
- **Accessibility spec (v2).** The SVG is `aria-hidden="true"`; semantics
  live in `<s>` and the "Originally published" labelling (§6.2). The
  strike's red (≈5.2:1 on paper) is decoration-grade by design — the
  *meaning* (this text is superseded) is never carried by the line's
  visibility alone.
- **Performance budget & mobile variant.** One path per phrase, one
  dash-offset write per frame while drawing; a page's strikes never draw
  simultaneously (§6.2's queue). Mobile: identical engine, recomputed
  geometry.
- **Tokens consumed (v2).** `--red`, `--ease-strike`, `--dur-strike`
  (computed, §above).

---

### 6.10 The pinned standing apology

- **What & why.** Before the corrections begin, the column apologises —
  once, in writing, in the margin — and the apology *stays*: it pins
  beside the first three corrections, accompanying each admission like a
  chaperone, and then, its duty done, it releases and scrolls away with
  the fourth. A standing apology that scrolled off with the hero would be
  a banner; one that never left would be wallpaper. Three corrections is
  exactly long enough to mean it.
- **Structure.** An `<aside class="standing-apology">` in the margin
  track: a hairline-ruled block containing the apology text (Source Serif
  4, 17px/1.55 — the only margin text set in the press face at near-body
  size, because the apology is a statement, not a note), the publication's
  name, and a Caveat signature line. It is real content from the content
  system — the organisation's actual standing apology, versioned like any
  other statement (if the apology itself is ever corrected, it gets an
  erratum like everything else; §9 finds this delightful and mandatory).
- **Motion spec.** Pinning is `position: sticky` within a margin rail
  whose height spans errata 1–3 — no JS pinning, no scroll-jacking; the
  apology simply refuses to leave while its three charges are in view.
  On pin engage/disengage there is *no* animation (sticky is silent; a
  bounce would be grovelling). The only motion: when the fourth erratum's
  ritual begins, the apology's hairline rule draws out (a reverse strike,
  300ms, `--ease-strike`, in `--grey` — the editor quietly ruling the
  apology closed) as it releases.
- **Choreography timeline (v2).** Page load: apology in flow at the head
  of the margin → scroll: sticks at header-offset (header height + 24px)
  as erratum 1 enters → remains stuck through errata 1–3's full span →
  erratum 4 crosses 30%: rule draws out (300ms) → apology reaches its
  rail's end and scrolls away naturally with the page → it does not
  reappear; pages are read once, apologies are made once.
- **State matrix (v2).** *Rest:* in flow / stuck, per scroll position.
  *Hover/focus/active:* none — the apology contains no interactive
  elements except, optionally, its one link ("our corrections policy"),
  which takes standard link states. *Scrolled-past:* gone, by design.
  *Disabled:* no-JS → the apology is a static margin block at the top;
  sticky is CSS and still works, so the disabled state is nearly
  identical. Touch: identical.
- **Content merge.** The apology accompanies the corrections it apologises
  for — positioned by them, released by them. It is not a hero element
  and never appears in the statement track.
- **Failure fallback.** Static block at the margin's head. If the page
  has fewer than three errata, the rail spans what exists; with zero
  errata the apology does not render at all — apologising beside no
  corrections is theatre (§9).
- **Reduced-motion variant.** Identical (sticky is not motion); the
  rule-out draw becomes a static `--grey` rule from first paint.
- **Breakpoints (v2).** ≥1200px: pins for three errata. 768–1199px: pins
  for two (the narrower margin's rail is shorter; forcing three would
  crowd the originals it shares the track with). <768px: no pin — the
  apology becomes the stacked layout's opening block, full-width, above
  erratum 1, and scrolls away immediately; on a phone, an apology that
  follows you is a popup, and popups are beneath this theme.
- **Edge cases & failure modes (v2).** *Apology longer than the
  viewport:* it never sticks (a stuck element taller than the screen
  traps its own ending); it renders static — length is a copy problem,
  flagged in §12 (the standing apology is capped at 60 words by the
  voice rules). *Errata reordered in the CMS:* the rail is computed from
  the first three `.erratum` elements in DOM order at runtime; the
  apology follows the document, not a hardcoded section. *Sticky broken
  by a transformed ancestor:* the build-order (§15) forbids transforms
  on the sheet's ancestors; if it happens anyway, the apology degrades
  to a static block — silent, readable, unembarrassing.
- **Accessibility spec (v2).** The apology is a `complementary` landmark
  labelled "Standing apology", read once in DOM order before erratum 1.
  Sticky positioning does not change focus or reading order. Its text is
  `--ink` at 17px (≈15:1). The signature is Caveat at 21px (§3's floor
  for the hand).
- **Performance budget & mobile variant.** Pure CSS sticky: zero JS,
  zero per-frame cost — the cheapest element in the theme. Mobile:
  static block, as above.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--grey`, `--hairline`,
  `--ease-strike`.

### 6.11 Slip-frame images

- **What & why.** In a corrections column, even a photograph is a claim —
  and claims get corrected. Images therefore arrive the way corrections
  do: pasted, inside a slip frame, honestly tilted, scaling into their
  frame as they enter. A photograph that replaces an earlier photograph
  is a full erratum: the old caption sits struck in the margin, the new
  image is pasted in the column.
- **Structure.** A `<figure class="slip-frame">`: the slip's paper stock,
  padding, glued-edge rule, and rotation law (§4) applied to a frame; the
  `<img>` inside a clipped inner window; a `<figcaption>` in apparatus
  type (13.5px, `--ledger-grey`) naming what the image shows and — for
  replacement images — the Caveat note *"replaces the photograph of
  02 FEBRUARY 2026"*. The frame is a slip that happens to carry a
  photograph; it peeks (§6.6) and presses (§6.7) like any other slip
  where the product makes slips interactive.
- **Motion spec.** On entry (30%): the image scales 1.05 → 1 inside its
  window over 700ms `--ease-paste` (the paste settle, slowed for weight);
  the frame's paste shadow deepens across the same 700ms; the paste-sheen
  (§5) makes one pass as the scale lands. Thereafter the frame joins the
  slips' 0.92 parallax (§6.2) — photographs lag with the paper they're
  pasted on, never independently.
- **Choreography timeline (v2).** t=0 frame crosses 30% → scale begins
  1.05 → shadow at 60% → t=350ms scale 1.02, shadow 85% → t=700ms scale
  1.0, shadow full, sheen pass begins (1200ms traverse) → t=1900ms at
  rest. Replacement images run their margin ritual first (§6.2 beats:
  old caption struck at t=0–400ms) and the frame's entry begins at
  t=+300ms, in ritual order.
- **State matrix (v2).** *Rest:* framed, pasted, at scale 1. *Hover:*
  §6.6 peek (revealing, beneath the frame's free corner, a thumbnail
  strip of the replaced photograph where one exists — the provenance
  rule applied to images) and §6.7 press where interactive. *Focus:*
  the figure is focusable only if interactive; the image itself is
  ordinary content. *Active:* §6.7. *Scrolled-past:* rest.
  *Disabled:* JS off → image at scale 1 in its frame, caption complete.
  Touch: tap behaviours per §6.6/§6.7.
- **Content merge.** The frame's caption, its place in an erratum, and
  its replacement history are content; the pasted frame is how this
  publication *issues* photographs. A decorative stock photo in a slip
  frame is a §9 violation — if it corrects nothing, it is not pasted.
- **Failure fallback.** Broken or slow image: the frame renders with its
  caption and a `--paper-shade` window holding the image's alt text set
  as a statement (17px serif) — a missing photograph is itself reported,
  in the column's voice ("The photograph could not be printed. It showed:
  …"). The frame never collapses; its box is aspect-ratio reserved.
- **Reduced-motion variant.** Image at scale 1 from first paint; no
  sheen pass; parallax off. The frame, caption, and history remain.
- **Breakpoints (v2).** ≥1200px: frames may span the statement track's
  full width; replacement pairs (old caption in margin) as specced.
  768–1199px: same, max width 88% of the track. <768px: frames stack
  full-width in the column, rotation capped at 1° (§4), the replaced
  photograph's struck caption sits above the frame in the shade block.
- **Edge cases & failure modes (v2).** *Portrait vs landscape:* the
  window's aspect comes from the image; frames never crop a photograph
  to fit the paper (cropping a correction is a second error). *Image
  with no predecessor in a corrections context:* it is not framed — it
  runs as an ordinary figure in the statement track; the slip frame is
  earned by errata only. *Huge images:* `srcset` with the window's real
  sizes; the frame's paper and shadow are CSS, so a slow image never
  delays the text around it.
- **Accessibility spec (v2).** Alt text is written to the column's
  standard (§12): what the photograph shows, factually, plus — for
  replacements — what changed versus the previous photograph, since that
  difference is the news. Captions are associated via
  `aria-describedby`. The peek's replaced-photo thumbnail is decorative
  (`alt=""`) because the full record is the margin caption.
- **Performance budget & mobile variant.** Images lazy-load below the
  fold (`loading="lazy"`, decoding async); the scale transform is on the
  inner window, not the frame, so the shadow never repaints. Page image
  budget in §14. Mobile: scale range narrows to 1.03 → 1, sheen cut.
- **Tokens consumed (v2).** `--paper`, `--paper-shade`, `--ink`,
  `--ledger-grey`, `--red`, `--shadow-paste`, `--ease-paste`,
  `--slip-rot`.

### 6.12 Full-slip page transition + skeleton

- **What & why.** Leaving a page in this theme is done the way everything
  is done: with a slip. Navigation pastes a slip over the whole viewport;
  the new page is revealed by peeling that slip from its free corner.
  Loading, likewise, shows the column's skeleton — humble-grey statement
  shapes that receive their correction slips as real content arrives.
  Transitions and loading are not chrome around the fiction; they are
  two more of its rituals.
- **Structure.** A fixed full-viewport slip layer (`--paper`, glued-edge
  rule scaled to a 6px left rule, the destination's name set as a slip
  claim line in the corner, its date stamp pre-printed). The skeleton:
  statement-track blocks in `--paper-shade` with `--grey` text-bars,
  margin blocks empty, each skeleton erratum carrying an unlanded slip
  outline; content replaces skeleton errata one-for-one, in order, each
  landing with its §6.2 ritual compressed (strike 200ms, slip 300ms —
  loading is not the place for the full ceremony).
- **Motion spec.** Outgoing: the slip slides over the viewport from its
  glued (left) edge, `--dur-page` (400ms, `--ease-paste`), full paste
  shadow trailing. Hold: only as long as the route actually takes (no
  artificial minimum beyond the 400ms cover). Incoming: the slip peels
  from its free (bottom-right) corner — a clip-path polygon sweep plus a
  curl shadow — over 450ms `--ease-peel`, revealing the new page already
  painted beneath (the new page never animates in under the peel; it is
  simply *there*, the way the next sheet is there). Skeleton pulse:
  text-bars breathe opacity .55 → .8 on a 1400ms cycle — the only pulse
  in the theme, and it belongs to unfinished business.
- **Choreography timeline (v2).** t=0 navigation committed → t=400ms
  viewport covered, route change executes under cover → new page painted
  → peel begins → t=+450ms peel complete, slip layer removed from the
  DOM (never left as a fixed overlay) → the new page's own rituals arm.
  Skeleton: shown if content is not ready within 120ms of paint →
  errata replace in order, 90ms stagger → last skeleton replaced →
  layer removed. Hard law: skeleton never persists beyond 3000ms; at
  3000ms whatever content exists renders, and missing errata render as
  §6.11-style reported absences.
- **State matrix (v2).** *Rest:* no layer present. *Hover/focus/active:*
  the layer is never interactive. *Scrolled-past:* n/a. *Disabled:* JS
  off / no router → ordinary full-page navigation, no layer, no
  skeleton; the theme loses its transitions and keeps its entire
  meaning. Touch: identical.
- **Content merge.** The slip that carries the visitor is labelled with
  the destination's actual name and carries the publication's stamp; the
  skeleton is shaped like the page it is loading. Neither is a generic
  spinner wearing the theme's colours.
- **Failure fallback.** If the peel fails mid-route (JS error), the layer
  is force-removed by a 1200ms watchdog and the destination stands
  revealed — a stuck slip over a whole site is the one unforgivable
  state in this theme, and the watchdog exists because of it.
- **Reduced-motion variant.** No slide, no peel: a 120ms crossfade of
  the viewport (opacity only), or instant navigation where the router
  allows. Skeleton bars are static (no pulse).
- **Breakpoints (v2).** Identical mechanics at all widths; on <768px the
  peel's curl shadow is dropped (the clip sweep alone reads clearly at
  small size) and the cover slide shortens to 320ms.
- **Edge cases & failure modes (v2).** *Back/forward navigation:* the
  transition plays in reverse geography — the slip peels *back* (cover
  from the right, peel from the left) for history-back, so direction is
  legible. *Same-page anchors:* no transition; anchors are reading, not
  travel. *Slow route (>1200ms):* the cover slip's stamp "dries" (its
  ink blur cycle, §6.5, runs once) and the slip's claim line gains the
  Caveat note *"still pasting…"* at 1500ms — the theme admits delay in
  its own voice rather than spinning. *Prefetch:* destinations prefetch
  on link hover/focus where the router supports it, so the peel usually
  reveals an already-painted page.
- **Accessibility spec (v2).** Route changes move focus to the new page's
  H1 and announce the page title via the router's live region; the slip
  layer is `aria-hidden` and inert. Skeleton regions carry
  `aria-busy="true"` until replaced. The transition never traps focus —
  it contains no focusable elements.
- **Performance budget & mobile variant.** The layer is one element,
  transform + clip-path only; it exists in the DOM only during
  transitions. Skeleton: pure CSS shapes, no images. Mobile: as above.
- **Tokens consumed (v2).** `--paper`, `--paper-shade`, `--ink`, `--red`,
  `--grey`, `--shadow-paste`, `--ease-paste`, `--ease-peel`, `--dur-page`.

---

### 6.13 Column-head navigation (page family: navigation)

- **What & why.** Navigation in a corrections column is a ledger index:
  the sections of the publication listed as ruled entries, each carrying
  the count of corrections it currently holds. A reader navigates an
  honest publication by where the errors are. The nav never hides the
  tally, and the tally never decorates the nav — they are the same fact.
- **Structure.** Within the sticky header (§6.4), a horizontal ledger of
  4–6 entries (Source Serif 4, 15px, `--ink`), each entry a ruled line
  item: name, then a tabular count in `--ledger-grey` ("Finance · 41").
  The current section's entry carries a 2px `--red` underline — red is
  licensed here because the underline is the editor's line in miniature,
  marking where in the ledger you stand. A hairline rules the ledger's
  bottom edge.
- **Motion spec.** Entries do not animate on load. Hover: the entry's
  underline draws left-to-right over 180ms `--ease-strike` (a small
  ruling gesture). The current-page underline is static. Counts never
  tick, spin, or celebrate in the nav — the header tally (§6.4) is the
  only counting surface; nav counts are the standing record, updated on
  navigation.
- **Choreography timeline (v2).** Static, except: hover t=0 → underline
  drawn by t=180ms; on route change the red marker transfers instantly
  (no travelling dot — ledgers do not animate their index).
- **State matrix (v2).** *Rest:* entries plain, current marked. *Hover:*
  underline draw. *Focus:* underline draw + 2px outline offset 3px.
  *Active:* press — the entry's text deepens to `--red-deep` for 120ms
  (ink, pressed harder). *Scrolled-past:* n/a (sticky header). *Disabled:*
  an entry with no live page renders as plain text with its count — the
  ledger lists sections that exist as records even when unlinked.
  Touch: no hover; tap targets ≥ 44px tall via header padding.
- **Content merge.** The counts are the sections' real errata totals from
  the same data as §6.4 — the nav is the ledger's table of contents.
- **Failure fallback.** A plain list of links in a header. Everything
  else is enhancement.
- **Reduced-motion variant.** Underlines appear instantly on hover/focus.
- **Breakpoints (v2).** ≥1200px: full ledger row. 768–1199px: counts
  drop (names only) — the totals live on the index page; the marker and
  names remain. <768px: the ledger collapses to a "Sections" disclosure
  whose panel is a ruled list with counts restored (in the panel there
  is room, and in a list the counts are the content).
- **Edge cases & failure modes (v2).** *A section with zero corrections:*
  its count reads "Finance · 0" without apology or ornament — a clean
  section is a fact, not a failure. *Very long section names:* truncate
  with ellipsis at 18ch in the bar (never in the mobile panel); the
  ledger does not wrap to two lines and push the sheet down.
- **Accessibility spec (v2).** `<nav aria-label="Sections">`; current
  entry carries `aria-current="page"`; counts are read as part of the
  link name ("Finance, 41 corrections") via visually-hidden text, so the
  ledger is navigable by ear.
- **Performance budget & mobile variant.** One 180ms underline transition.
  Mobile: the disclosure panel is a static list, zero animation beyond
  its underline draws.
- **Tokens consumed (v2).** `--ink`, `--red`, `--red-deep`,
  `--ledger-grey`, `--hairline`, `--ease-strike`.

### 6.14 Front-page hero composition (page family: hero)

- **What & why.** The hero is the column's front page: masthead rule,
  the founding correction performed at full size (§6.1), the standing
  apology beginning in the margin (§6.10), and the day's ledger strip
  beneath. It is specced separately from §6.1 because the gesture needs a
  stage with exact proportions — a founding correction crammed into a
  marketing hero's split layout would read as a gimmick instead of a
  confession.
- **Structure.** Full sheet width. Top: a double hairline rule (the
  masthead rule) with the publication line ("THE DAILY LEDGER —
  CORRECTIONS DESK") in 12px caps between the rules. Centre: the claim
  block — the wrong claim set at 54px in the statement track, its margin
  original beside it (§6.2 geometry at hero scale), the founding slip
  (§6.1) sized to the claim. Beneath: the ledger strip — the day's three
  newest corrections as one-line entries (date stamp + corrected claim +
  link), ruled off by a hairline. The apology (§6.10) occupies the margin
  from the hero downward.
- **Motion spec.** Only §6.1's gesture and §6.5's stamp move in the hero.
  The ledger strip's entries are static on load (they are records, not
  teasers). The masthead rule draws once on first load (1200ms,
  `--ease-strike`, from centre outward — the desk ruling its sheet
  before the confession begins); on repeat views within a session it is
  pre-drawn.
- **Choreography timeline (v2).** t=0 masthead rule begins (1200ms) →
  t=0 hero claim painted wrong, beat running (§6.1) → t=900ms §6.1
  gesture fires → t=1610ms gesture complete, tally at 1 → hero at rest.
  Total ceremony ≈ 1.61s (the rule draws in parallel, finishing inside
  the beat).
- **State matrix (v2).** Inherited from §6.1 and §6.10 for its moving
  parts. The ledger strip's entries: *rest* plain; *hover* the entry's
  claim underlines (`--ease-strike` draw, 180ms); *focus* as hover +
  outline; *active* standard. Touch: entries are full-row tap targets
  ≥ 48px.
- **Content merge.** Every element of the hero is content: the claim, its
  correction, the apology, and today's real corrections in the strip. A
  hero image is permitted only as a §6.11 slip-frame (i.e., only as a
  corrected photograph).
- **Failure fallback.** The side-by-side hero (§6.1 fallback at page
  scale): struck claim in the margin block, corrected claim in the
  column, strip static. Fully composed with no JS.
- **Reduced-motion variant.** Side-by-side hero, masthead rule pre-drawn,
  stamp static (§6.1/§6.5 variants compose).
- **Breakpoints (v2).** ≥1200px: as specced. 768–1199px: claim 44px,
  strip entries stack their stamps above their claims. <768px: stacked
  per §4 — masthead rule, claim block (original in shade block, slip
  beneath), strip as a ruled list; the apology follows as its own block
  (§6.10 mobile ruling).
- **Edge cases & failure modes (v2).** *No correction today:* the strip
  reads "NO CORRECTIONS TODAY. THE DESK IS WATCHING." and the hero still
  performs the founding gesture (the founding error is historical, not
  daily). *Founding claim retired:* if the organisation corrects its
  founding claim's *correction*, the hero gains a second slip (§6.5's
  accretion rule) — the hero is erratum № 1 forever, however many layers
  it grows.
- **Accessibility spec (v2).** Landmark order: masthead line (banner) →
  H1 (the corrected claim, §6.1) → ledger strip as a list with an
  `aria-label` "Today's corrections". The wrong claim never becomes the
  H1's accessible name.
- **Performance budget & mobile variant.** The hero is text, two rules,
  and one slip: it is the page's LCP element and it is *type* — LCP
  target ≤ 1.6s on 4G (§14). Mobile: as above, gesture static.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--red`, `--hairline`,
  `--ledger-grey`, `--ease-strike`.

### 6.15 Erratum entry cards (page family: cards)

- **What & why.** On the corrections index and section listings, each
  correction is a card — and a card in this theme is a small erratum: the
  struck original on a shade ground, the correction pasted over its lower
  half as a slip, the date stamped on the corner. A grid of cards reads
  as a desk covered in pasted slips, which is exactly what a corrections
  index is.
- **Structure.** An `<article class="erratum-card">` (min height 190px):
  top zone in `--paper-shade` carrying the original claim (15px italic,
  struck statically — cards do not perform the draw; §6.9's engine is
  reserved for reading pages, and §9 explains why performing it 24 times
  in a grid is slop), the slip overlapping the zone boundary by 28px
  carrying the corrected claim (17px, 600), a meta line (section,
  `--ledger-grey`), and the date stamp (§6.5, static on cards) at the
  top-right. Whole card is one link to the correction's record page (§7).
- **Motion spec.** Entry: cards paste in as their row enters — slip zone
  settles `translateY(6px) → 0` with paste shadow growing, 380ms
  `--ease-paste`, staggered 70ms per card within the row, never more
  than one row animating. Hover: the card's slip lifts its corner (§6.6
  at card scale: +2°), revealing the original's next line beneath the
  overlap. The card itself never scales, glows, or floats — desks don't.
- **Choreography timeline (v2).** Row enters at 25% → t=0 first card
  settles → +70ms per subsequent card → row complete ≤ t=380+210ms.
  Hover: §6.6's timeline compressed (lift 200ms). Press (§6.7 pattern):
  the whole card presses at scale .995 for navigation feedback, 120ms.
- **State matrix (v2).** *Rest:* pasted, static strike. *Hover:* corner
  lift. *Focus:* lift + outline (the card is one link; focus-within
  drives the lift so keyboard users see the same provenance). *Active:*
  press. *Scrolled-past:* rest. *Disabled:* a card whose record page is
  unavailable renders without the link, meta line noting "Record in the
  archive drawer" — still fully readable. Touch: no hover; the overlap
  already shows both texts partially, and the full record is one tap
  away — nothing is touch-gated.
- **Content merge.** The card *is* the erratum in miniature: original,
  correction, date. No card exists for content that is not a correction.
- **Failure fallback.** Static cards, both texts visible, stamp present.
  The entry settle is the only motion and its absence costs nothing.
- **Reduced-motion variant.** Cards appear in place; hover lift becomes
  the static revealed-line disclosure (§6.6's variant at card scale).
- **Breakpoints (v2).** ≥1200px: 3 columns, gutter 28px. 768–1199px: 2
  columns. <768px: 1 column; the slip overlap reduces to 18px and card
  rotation is zeroed (a one-column desk is a tidy desk; §4's rotation
  law applies to reading pages, and cards carry a milder ±0.5°
  alternation at ≥768px only).
- **Edge cases & failure modes (v2).** *Original longer than the shade
  zone:* the zone truncates the original at 3 lines with the truncation
  marked by the editor's ellipsis "…" in Caveat — never a silent CSS
  clip of a *record*; the full original is on the record page, and the
  card says so by its link. *Correction amended later:* the card grows
  the second stamp (§6.5) and its meta line gains "Amended" in
  `--red-deep`. *Empty listing:* §12's empty-state voice, set as a
  single uncorrected section (§4) — no skeleton cards, no fake errata.
- **Accessibility spec (v2).** The card link's accessible name is the
  corrected claim + date ("Corrected 14 March 2026: …"), never the
  struck original. The static strike is `<s>` with the §6.9 aria
  treatment. Grid is a list (`<ul>` of `<li>`) so screen readers get
  count and position.
- **Performance budget & mobile variant.** Cards are text and shadow;
  24 per page maximum before pagination (§11) — a corrections index
  paginates like a newspaper, it does not infinitely scroll (§9).
  Mobile: settle animation kept (it is one transform), stagger removed.
- **Tokens consumed (v2).** `--paper`, `--paper-shade`, `--ink`, `--red`,
  `--red-deep`, `--ledger-grey`, `--shadow-paste`, `--ease-paste`,
  `--ease-settle`, `--dur-peek`.

---

### 6.16 File-a-correction form (page family: forms / conversion)

- **What & why.** The column's conversion point is not a sale; it is a
  reader filing an error they have spotted. The form is a printed
  correction slip the reader fills in: *what we published, what is true,
  how you know.* Its success state is not a thank-you page — it is the
  filed correction entering the ledger as "received, under review", with
  a reference number stamped on it. A corrections column that cannot
  receive corrections is a monologue.
- **Structure.** A single-column slip-form (max width 560px, §4 slip
  geometry at form scale, rotation 0 — forms are never tilted; play
  stops where a reader is typing): fields for the published claim (URL +
  the words as printed), the true statement, the evidence (source or
  link), and the reader's email (optional, for the outcome notice).
  Labels are apparatus (13px caps, `--ledger-grey`); inputs are ruled
  lines — transparent ground, 1px `--hairline` bottom rule, 18px Source
  Serif text. The submit control is the **filing plate**: a full-width
  block, `--ink` ground, paper text, labelled with the plain verb:
  "File this correction". Errors appear as editor's notes in the form's
  own margin strip: Caveat, `--red-deep`, with a drawn circle around the
  field's number (§12 voice).
- **Motion spec.** Focus: the field's rule inks from `--hairline` to
  full `--ink` over 200ms and the label takes a 40% impression (a
  shallow stamp-shadow). Error: the note is *drawn* — the Caveat text
  fades in over 200ms while its circle draws (SVG, 300ms,
  `--ease-strike`) — proof marks are struck, not faded. Submit: the
  plate presses (§6.7 pattern at form scale, 130ms), the form takes a
  full impression (its slip shadow deepens, 400ms) while submitting.
  Success: the form is replaced by the filed slip — the reader's own
  correction, typeset as an erratum card (§6.15) with its reference
  number stamped (§6.5 thud) and its status line: "Received. Under
  review. We publish our verdict either way."
- **Choreography timeline (v2).** Focus: t=0 rule inks → t=200ms label
  impressed. Error (on blur or submit): t=0 field rule turns
  `--red-deep` → t=0–300ms circle draws → t=200ms note fully present.
  Submit: t=0 plate press → t=130ms form impression full → request →
  success: form crossfades (150ms) to the filed slip → stamp thuds at
  +160ms → status line types in as a statement (no typewriter effect —
  statements are set, not typed; it simply appears).
- **State matrix (v2).** *Rest:* hairlines faint, labels flat. *Hover:*
  fields brighten their rule to 30% ink. *Focus:* as specced. *Filled:*
  a completed field's rule rests at 60% ink — a filled line on a form is
  darker than an untouched one. *Error:* red-deep rule + drawn note,
  persistent until corrected (form errors never time out; the desk does
  not forget what it flagged). *Submitting:* impression held, inputs
  disabled, plate label reads "Filing…". *Success:* the filed slip,
  permanent for the session. *Disabled (JS off):* a plain HTML form
  posting to the server, errors re-rendered server-side in the same
  margin-note layout as static text. Touch: inputs at 18px (also
  prevents iOS zoom), targets ≥ 48px.
- **Content merge.** The form is the column's intake document — its
  fields are the erratum's own fields (published / true / evidence), so
  a successful filing is already shaped like the correction it may
  become. The filed-slip success state is the same object as §6.15's
  card: the reader sees their correction enter the same record as the
  publication's own.
- **Failure fallback.** Plain form, server round-trip, same layout, same
  voice. Every enhancement is CSS/JS over a working form; a failed
  script loses the theatre and keeps the filing.
- **Reduced-motion variant.** Focus/error/submit states apply instantly;
  the success stamp appears statically. The circle around an error is
  pre-drawn.
- **Breakpoints (v2).** ≥1200px and 768–1199px: form in the statement
  track with its note strip in the margin track — the one place the
  margin carries something other than an original, licensed because the
  notes *are* corrections-in-progress. <768px: single column, notes
  appear beneath their fields (a phone form has no margin), circle drawn
  around the field number inline.
- **Edge cases & failure modes (v2).** *Duplicate filing* (same claim
  filed twice): the success slip notes "Seconded — this claim was also
  filed on [date]" instead of erroring; a correction with two witnesses
  is stronger, not invalid. *Server failure on submit:* the form keeps
  every entered value, the impression releases, and the error note is
  the desk's own: "The desk could not take this filing. Nothing you
  wrote was lost. Try again." (§12). *Spam/abuse filings:* handled
  server-side; the form never shows a CAPTCHA styled as anything but
  what it is — a plain apparatus block; the theme does not costume
  security as stationery.
- **Accessibility spec (v2).** Every field has a real `<label>`; errors
  are tied by `aria-describedby` and announced via `role="alert"` on the
  note strip, once, on appearance. Error identification is never
  colour-only: the drawn circle + note text + the field's number are
  three redundant channels. Focus order follows the slip top to bottom;
  the success state moves focus to the filed slip's heading.
- **Performance budget & mobile variant.** No animation loops; the form
  is the lightest page-family element after the apology. Mobile: notes
  below fields, impression reduced to the plate press only.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--red-deep`,
  `--ledger-grey`, `--hairline`, `--shadow-paste`, `--ease-strike`,
  `--ease-settle`, `--dur-press`.

### 6.17 The archive drawer + colophon footer (page family: footer)

- **What & why.** Every page of corrections closes with the drawer: the
  old errors, kept. A shallow drawer front at the foot of the sheet —
  pull it and the full archive of past errata slides out, oldest
  shame first-class and searchable. Beneath it, the colophon: what this
  column is set in, how many corrections it has published to date, and
  the standing line. The drawer is the theme's promise made physical:
  nothing is deleted, ever; errors are *filed*.
- **Structure.** The drawer front: a `--paper-shade` band, full sheet
  width, with a handle rule, the label "THE ARCHIVE OF ERRORS" (13px
  caps), the count ("212 ON FILE", tabular, `--red-deep`), and a Caveat
  note: *"nothing in here has been deleted."* Open, the drawer reveals
  the archive list: ruled entries by year, each a one-line erratum
  (stamp date, struck original in miniature, corrected claim, link to
  its record). The colophon below: centred apparatus text (13.5px) —
  type credits, the total corrections to date (computed, §6.4's site
  denominator), the corrections-policy link, and the legal line.
- **Motion spec.** Opening: the drawer front slides down and the archive
  list's container expands (`grid-template-rows` 0fr → 1fr technique or
  measured height) over 450ms `--ease-paste`; entries fade-settle in
  ruled order, 40ms stagger, capped at the first 12 (the rest are simply
  present — a drawer does not perform its whole contents). The red line
  (§6.3) terminates at the drawer's rule. Opening fires §6.8's reset —
  the streak ends because you looked. Closing reverses in 350ms.
- **Choreography timeline (v2).** t=0 handle activated → t=0 §6.8 counter
  swaps to 0 (the joke lands as the drawer moves) → t=450ms drawer fully
  open, first entries settled → focus moves to the drawer's heading only
  if activated by keyboard. Close: t=0 → t=350ms shut, handle's count
  unchanged (opening a drawer does not file new errors).
- **State matrix (v2).** *Rest:* closed, count visible. *Hover:* the
  handle rule deepens to `--ink` 30%. *Focus:* outline + rule deepens.
  *Active:* press (handle translates 1px down — a drawer pull begins).
  *Open:* entries at rest; the handle reads "CLOSE THE ARCHIVE".
  *Scrolled-past:* unchanged. *Disabled:* JS off → the drawer renders
  *open and static* as a page section (the archive is content; hiding it
  behind a dead toggle would be the theme's one unforgivable act).
  Touch: the whole front is the tap target (≥ 56px tall).
- **Content merge.** The drawer contains the publication's actual
  complete errata archive — the same records as the index (§6.15),
  unabridged. The colophon's total is the same computed number as the
  drawer's count and the site ledger (§6.4): one fact, three printings,
  never three numbers.
- **Failure fallback.** Open static section, as in the disabled state.
- **Reduced-motion variant.** The drawer opens instantly (height swap,
  no slide); entries static; §6.8's reset still fires (it is timing,
  not motion).
- **Breakpoints (v2).** ≥1200px: archive entries in two ruled columns
  inside the drawer. 768–1199px: one column, year groups stacked.
  <768px: the drawer front stacks its label, count, and note; entries
  one column; the drawer opens to a capped height with its own internal
  scroll only if the archive exceeds 60 entries (a page-scroll trap in a
  footer is a §9 offence; below 60, the drawer grows the page).
- **Edge cases & failure modes (v2).** *Enormous archives (1,000+):*
  the drawer shows years as sub-drawers (each year a ruled disclosure),
  all present in the DOM as links — the archive is never paginated away
  behind a "load more" that a crawler or a determined reader cannot
  follow. *An error expunged by law:* the entry remains as a struck line
  with the note "Removed by order of [court/policy], [date]" — even
  removal is recorded, in the column's own grammar. *Drawer opened from
  a deep link (#archive):* opens on load, §6.8 already at 0.
- **Accessibility spec (v2).** The handle is a real `<button>` with
  `aria-expanded` and `aria-controls`; the archive is a `<region>`
  labelled by its heading. Year groups are heading-structured. The
  count's accessible text: "212 corrections on file". Colophon links are
  ordinary links; the drawer's red line termination is decorative.
- **Performance budget & mobile variant.** The drawer ships closed with
  its entries as lightweight ruled text (no cards, no images): ≤ 30KB
  of HTML for 200 entries; beyond 200, year sub-drawers lazy-render
  their lists on first open (the *links* are always present). Mobile:
  as above.
- **Tokens consumed (v2).** `--paper`, `--paper-shade`, `--ink`, `--red`,
  `--red-deep`, `--ledger-grey`, `--hairline`, `--ease-paste`,
  `--ease-settle`.

### 6.18 The misprint page (page family: 404)

- **What & why.** A publication's 404 is a misprint: the page the reader
  wanted was never published. The theme's error page is set as a
  correction of a page that does not exist — the only erratum whose
  original is an absence — and it routes the reader back into the ledger
  with the publication's driest courtesy.
- **Structure.** A single uncorrected-format section (§4) in the
  statement track: the stamp "NEVER PUBLISHED" (§6.5 pattern, static),
  the statement (30px): "The page you asked for was never published. If
  we ever implied otherwise, that implication is withdrawn." — the
  requested URL set as the struck "original" in the margin block
  (verbatim, in mono-spaced apparatus type, struck by §6.9's static
  strike), and beneath, the three most-visited corrections as §6.15
  cards, plus a link to the archive (§6.17).
- **Motion spec.** Almost none, deliberately: the stamp is pre-struck,
  the strike pre-drawn. One gesture only: after 1200ms, a Caveat note
  fades in under the statement — *"the desk regrets the error. the desk
  always regrets the error."* (300ms fade). An error page that performs
  is showing off at the reader's expense.
- **Choreography timeline (v2).** t=0 page painted complete → t=1200ms
  Caveat note fades (300ms) → rest. That is the entire timeline.
- **State matrix (v2).** *Rest:* as painted. *Hover/focus/active:* only
  on its links and cards (§6.15 states). *Scrolled-past:* n/a (the page
  is one screen by design). *Disabled:* identical — the page uses no JS
  except the note fade, which is CSS-only in the fallback (note present
  statically). Touch: identical.
- **Content merge.** The requested URL is the erratum's original — the
  reader's own request, corrected. The recovery links are the site's
  real most-visited corrections, not a generic sitemap.
- **Failure fallback.** This page *is* a fallback; its own fallback is
  that it is static HTML servable by any error handler with zero assets
  beyond the two fonts.
- **Reduced-motion variant.** Identical, with the note present from
  first paint.
- **Breakpoints (v2).** All widths: single column; ≥1200px the margin
  block carries the struck URL beside the statement (§4 geometry);
  <768px stacked per §4.
- **Edge cases & failure modes (v2).** *URL contains markup or enormous
  length:* the URL is escaped, truncated at 80 characters with the
  editor's ellipsis (§6.15), and never executed — a 404 that echoes
  input is a security bug wearing a costume. *Genuinely removed legal
  content:* the statement swaps to §6.17's removal wording ("Removed by
  order of…"), served with a 410 where the platform supports it.
- **Accessibility spec (v2).** H1 is the statement's first sentence.
  The struck URL is `aria-hidden` decoration (its meaning — "you asked
  for this" — is in the statement); screen readers are not made to
  spell out a long URL. HTTP status is a real 404.
- **Performance budget & mobile variant.** The lightest page in the
  theme: ≤ 20KB total, no JS required.
- **Tokens consumed (v2).** `--paper`, `--paper-shade`, `--ink`, `--red`,
  `--red-deep`, `--ledger-grey`, `--ease-settle`.

---

## 7. Page application map

**Home (the front page).** Masthead + ledger header (§6.4, §6.13) → hero
(§6.14: founding gesture, apology rail begins) → the three newest errata
as full §6.2 rituals (the apology pins beside them, §6.10) → one
uncorrected section (what the publication does, stated plainly — §4's
two-section limit observed) → further errata as §6.15 cards linking to
their records ("continued in the index") → archive drawer + colophon
(§6.17). The home page performs the full ceremony exactly once; a
homepage that performs it nine times is a parade, not a column (§9).

**Corrections index (listing).** The ledger made browsable: filter ruled
as ledger tabs by section and year (counts on every tab, §6.13's rule),
errata as §6.15 cards, 24 per page, paginated with folio pagination
(§11) — never infinite scroll. The index's H1 is a statement, not a
label: "Everything we have got wrong, in order." Sorted newest-first by
default; a "most amended" sort exists for readers auditing repeat
offenders.

**Correction record (detail).** One erratum at full scale: the §6.2
ritual with room to breathe — full original (however long), the slip,
the evidence for the correction (sources cited as apparatus), the
amendment chain if any (§6.5's accreting stamps, each amendment its own
dated paragraph), and the reader filings that prompted it where
applicable (§6.16's provenance, anonymised). The record page is the
theme's unit of permanence: it is never edited silently, only amended
visibly.

**About (the apology page).** The standing apology at full length, the
corrections policy as plain statements (uncorrected sections), the
desk's process set as a ruled list (how an error is reported, verified,
published, amended), and the complete site tally with its first and
latest dates. No slips perform here except the policy's own historical
corrections, if it has any — an about page is where the column explains
itself, in statements.

**File a correction (contact/conversion).** §6.16's form as the whole
page: a short statement of what happens to a filing (the verdict is
published either way — that sentence is the page's conversion copy), the
form, and beneath it the three most recent *reader-filed* corrections
that were upheld, as §6.15 cards: proof that filing works.

**Article pages (the publication's ordinary content).** The theme steps
back: articles set in the statement track alone, margins empty — *until*
the article is corrected, whereupon its errata appear at the article's
head as §6.2 rituals before the text, and the corrected passages carry
their slips inline. An uncorrected article in this theme looks like a
clean newspaper page; that cleanliness is the reward the whole system
exists to make meaningful.

**Retraction pattern (special).** When a whole piece is withdrawn, its
page becomes a single erratum at maximum scale: the entire original in
the margin track (struck, §6.9's long-form ruling), the statement track
carrying only the retraction statement, its evidence, and the apology —
no slip, because there is no corrected version; a retraction is the one
correction that replaces text with an absence, and the layout says so.

**404.** §6.18.

---

## 8. Worked examples

### 8.1 The hero — a fintech's founding correction

*Setting.* "Northbeam Finance" (fictional), a transparency-first lender
whose launch claim was *"No fees. Ever."* — until its statements showed a
currency-conversion margin it had not counted as a fee. The hero must
perform that.

**Build.** §6.14's composition. Margin block: label *"Originally
published, 03 JUNE 2025"*, original: the claim's context line ("Our
launch announcement, in full:") and the struck phrase. Statement track:
the H1's wrong claim painted plain — "No fees. Ever." at 54px — with
`<span class="claim-wrong">` around "No fees." The founding slip carries:
"One fee, named." (the corrected claim, 54px-equivalent slip claim at
hero scale set 40px to fit the slip's measure) plus its second line in
statement body: "A 0.8% conversion margin, printed on every statement
since 14 MARCH 2026." Stamp: `14 MARCH 2026`. Ledger strip beneath:
today's three corrections from the rates desk.

**Scroll/load timeline.** t=0 masthead rule draws (1200ms, parallel) →
claim painted wrong → t=900ms strike draws across "No fees." (200ms —
two words at §6.9's formula: 300 + 14×2 ≈ 330ms, hero uses the ritual's
200ms strike since the phrase is also §6.1's, which specifies 200ms;
builders take §6.1's number for the hero) → t=950ms slip slides (500ms,
`--ease-paste`) → t≈1250ms "No fees." shudders (120ms) as the slip
crosses it → t=1450ms slip landed, stamp thuds (160ms) and dries (300ms)
→ t=1610ms tally reads "1" and the strip is at rest. The apology
(§6.10) sits in the margin from first paint, its rail spanning this and
the next two errata.

**What the visitor feels.** A lender that opens by striking its own
slogan. The 900ms beat is the whole brand: the wrong claim is given a
full, unhurried second of plain visibility — no rush to cover it —
before the correction arrives with physical weight.

### 8.2 Mid-page — the rates table that was wrong

*Setting.* Lower on Northbeam's home page, a section whose original
announcement overstated its savings rate: "Earn 4.1% on every pound,
from day one." The truth: 4.1% applied above £5,000; below that, 2.3%.

**Build.** A §6.2 ritual whose statement track carries not just the
corrected lead but a small data table (§11) — because the correction *is*
a table: two ruled rows (balance band / true rate), the corrected lead
above it: "Two rates, printed plainly." The margin original is the full
original sentence, struck by §6.9 (11 words → 300 + 14×11 = 454ms draw).
The slip lands on the lead's claim phrase "every pound" — no; the slip
lands on the corrected lead itself is wrong practice (§4: a slip
corrects a claim, and the lead *is* the correction). Instead the slip
pattern applies to the table's headline figure: the original table (in
the margin, miniature, struck as a block) showed one row; the corrected
table stands clean in the column. The erratum's slip is reserved for the
section's closing claim — "The rate we advertise is the rate you get."
— originally published as "The best rate on the market." (struck in the
margin; slip carries the true closing claim + stamp `02 MAY 2026`).

**Scroll timeline.** Section enters at 30% → t=0 margin original present,
strike begins → t=454ms strike complete → t=300ms (parallel) the
corrected table's rows rule themselves in (hairlines draw left-to-right,
120ms per row, §11) → t=800ms closing slip lands, stamp thuds → red line
(§6.3) ticks through the gutter throughout, tally increments as its head
passes the section's midpoint → ritual complete ≈ t=960ms. Scrolling
back up: nothing reverses (§6.2); the table stays corrected.

**What the visitor feels.** The correction is *checkable*: not a
softer adjective but a table with two rows and a date. The theme's
mid-page lesson — corrections in this column carry evidence, set in the
same type as the claims.

### 8.3 Conversion — filing the error in the wild

*Setting.* A reader of Northbeam's blog finds a post claiming the
conversion margin is "under 0.5%". It is 0.8%. She files it.

**Build.** The file-a-correction page (§7): the statement ("Tell us what
we got wrong. We publish our verdict either way — upheld or not, the
filing is answered in this column."), then §6.16's form. She pastes the
post's URL, quotes the printed words, writes the true statement, links
the rates page as evidence.

**Interaction timeline.** She focuses the first field: rule inks (200ms),
label impresses. She pastes a URL without a scheme: on blur, the field's
rule turns `--red-deep`, the circle draws around field № 1 (300ms), and
the Caveat note appears: *"this needs the full address — the desk can't
file a street with no number."* She fixes it; the note stays until the
field validates on the next blur (errors persist until corrected,
§6.16), then the circle is joined by a small Caveat *"ta — corrected."*
— the form corrects its own corrections, in miniature, because it could
not possibly do otherwise. Submit: plate press (130ms), form impression
(400ms), request. Success: the form is replaced by her filed slip
(§6.15 card format) — her quoted claim, her true statement, reference
"№ 1,208" stamped with today's date (§6.5 thud), status: "Received.
Under review. We publish our verdict either way." Three weeks later the
correction is upheld; the record page (§7) carries her filing,
anonymised, as its provenance: *"Filed by a reader, 02 MAY 2026.
Upheld."*

**What the visitor feels.** Filing an error is not shouting into a
support inbox; it is handing a slip to a desk that has publicly promised
to answer in print. The form's own error handling — patient, specific,
self-correcting — is the proof of the promise, encountered before the
promise is even tested.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **Invented mistakes.** Corrections for errors nobody made ("we said
   'great'; we meant 'brilliant'"). *Cure:* §1's law — five real, dated
   errata or the theme is refused. The column's authority is its archive;
   a fabricated archive is fraud with good typography.
2. **CSS `line-through` instead of the drawn strike.** A uniform,
   ruler-straight, instantly-present strike reads as a text style, not an
   editor's act. *Cure:* §6.9's SVG draw with its hand wobble and
   computed durations; `line-through` exists only as the no-SVG semantic
   floor.
3. **Red as decoration.** Red buttons, red logos, red sale badges, a red
   "new" flag. *Cure:* §2's rationing list is exhaustive; any other red
   fails §10.
4. **The tally that doesn't count.** A header reading "14 corrections"
   typed by a copywriter, drifting out of sync with the page. *Cure:*
   DOM-computed counts only (§6.4); §10 gate 1 blocks the build.
5. **Slips as generic cards.** White rectangles with drop shadows and
   rounded corners, rotated a uniform 2°, carrying marketing copy.
   *Cure:* §4's geometry — same paper stock, glued-edge rule, rotation
   law with alternating signs and cycling magnitudes, paste shadow in
   warm neutral, and a slip only ever carries a corrected claim.
6. **Performing the ritual in grids.** Twenty-four cards all drawing
   their strikes and sliding their slips on a listing page. *Cure:*
   §6.15 — cards are static miniatures; the full ritual is reserved for
   reading pages, once per section. Ceremony repeated becomes noise.
7. **The apology as hero copy.** A giant "SORRY." headline, a tearful
   brand video, grovelling as a launch campaign. *Cure:* §6.10 — the
   apology is 60 words of margin prose at 17px. Its power is that it
   *stays*, not that it shouts.
8. **Corrections without dates, or with relative dates.** "Recently
   updated." *Cure:* §3/§6.5 — full publication dates, stamped, with
   `datetime` attributes; undated errata cannot be built (§10).
9. **The margin used as a sidebar.** Related links, social proof, a
   newsletter box parked in the margin "because there's space". *Cure:*
   §4 — the margin carries originals, notes, stamps, and the apology.
   Nothing else. Ever.
10. **Silent edits.** Fixing the corrected text later without a trace
    (the theme's mortal sin — it is the behaviour the entire column
    exists to expose). *Cure:* amendments accrete (§6.5's second stamp,
    §7's amendment chain); the build's CMS workflow (§15) makes the
    corrected text append-only.
11. **Handwriting everywhere.** Caveat headlines, Caveat buttons, a
    Caveat "personality". *Cure:* §3's division of faces — the hand
    writes notes of ≤ 12 words in margins, and nothing else.
12. **The drawer as a dump.** An archive drawer stuffed with the site's
    leftover links. *Cure:* §6.17 — the drawer contains the errata
    archive, complete and only that; expunged entries remain as struck
    records.

---

## 10. Quality gate

Blocking items (★) must pass; the rest must pass or be explicitly waived
in the project's DECISIONS.md with a reason the desk would print.

1. ★ **The tally is computed.** Every count on the page (header, nav,
   drawer, colophon) is derived from the errata in the DOM/data at
   render; change the errata and every count changes. Hand-typed counts
   fail the build.
2. ★ **Both versions, always.** Every corrected claim's original exists
   in the DOM, in reading order before its correction, readable with JS
   disabled and with CSS disabled.
3. ★ **Every erratum is dated** with a full publication date and a valid
   `datetime`; no relative dates anywhere in the theme.
4. ★ **Strikes land on their words.** After fonts load and after any
   resize, every strike path crosses its phrase's rendered box (§6.9's
   re-measurement runs); a floating strike fails.
5. ★ **The 900ms law.** Kill JS mid-gesture on §6.1 and §6.2 slips: the
   side-by-side fallback engages; the true statement is reachable in
   ≤ 900ms in every failure mode tested.
6. **Section rhythm.** No more than two consecutive uncorrected sections
   on any page carrying errata (§4).
7. **Red audit.** Every red pixel on the page traces to §2's licensed
   list. (Automate: screenshot + colour-cluster review.)
8. **Rotation audit.** Slip rotations match §4's law (alternating sign,
   0.5/1.0/1.5 cycle) — no uniform angles, no slip beyond 1.5°.
9. **Reduced motion = side by side.** With `prefers-reduced-motion`,
   every erratum renders in the side-by-side state and all information
   survives; the §6.8 joke still lands.
10. **Contrast at every state.** Originals ≥ 9:1 (ink 78%), corrections
    15:1, small red text only in `--red-deep` (≥ 7:1), apparatus only in
    `--ledger-grey` (≥ 6.4:1) — measured on hover and focus states too,
    not just rest.
11. **The drawer is complete.** The archive drawer's count equals the
    index's total equals the colophon's total; expunged entries present
    as struck records.
12. **No silent-edit path.** The CMS/build workflow makes published
    corrected text append-only; an amendment produces a new stamp and a
    chain entry, never an overwrite (§9.10).
13. **Performance.** §14's budgets met on a mid-range Android over 4G:
    LCP ≤ 2.0s, CLS ≤ 0.02, INP ≤ 200ms, no long task > 50ms from theme
    code.
14. **The desk test.** A reader shown any page for five seconds can say
    what the theme is doing: "they show you what they got wrong, then
    the correction, with dates." If they say "it's a newspaper theme",
    the build has failed at being a *corrections* column.

---

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components not listed do not get invented ad hoc; additions follow §4's
geometry and §2's rationing.

- **Buttons.** Primary (the filing plate pattern, §6.16): `--ink` block,
  paper text, plain verb, press = §6.7 at block scale. Secondary: ruled
  text buttons — apparatus caps with a hairline rule beneath that inks
  on hover (§6.13's draw). No red buttons. No pill shapes anywhere in
  the theme; paper has corners.
- **Links.** In statements: ink, underline in `--hairline` deepening to
  ink on hover. In apparatus: `--ledger-grey` → ink. Visited links in
  the archive take a 60% ink — the ledger remembers being read.
- **Inputs.** §6.16's ruled-line fields (label above, hairline rule,
  ink-on-focus, filled = 60% rule). Selects and textareas follow the
  same ruling; checkboxes are *proof ticks* — a square hairline box the
  reader ticks with a drawn ✓ (SVG, 200ms, `--ease-strike`, in
  `--red-deep`: a tick is a proof mark, so it earns the editor's colour
  at apparatus size); radio buttons are *stamp choices* — circles that
  fill with a thud (§6.5 at 120ms) when chosen.
- **Tables.** Ruled ledger tables: hairline row rules that draw in on
  entry (120ms per row, §8.2), header row in apparatus caps, numerals
  tabular, no zebra striping (ledgers rule lines; they do not shade
  alternate facts), totals row under a double rule.
- **Badges.** One only: the *Amended* badge — a miniature stamp
  (§6.5 style, static, `--red-deep`) on cards and records. There is no
  "New" badge in a corrections column; newness is not the virtue here.
- **Alerts.** Set as *editor's notices*: a `--paper-shade` block with a
  glued-edge rule, the notice as a statement, dated. Error alerts use
  `--red-deep` apparatus text; the circle-draw (§6.16) is reserved for
  forms.
- **Pagination.** Folio pagination: "Leaf 3 of 9" in apparatus type,
  prev/next as ruled text buttons, page numbers as ledger entries. No
  infinite scroll anywhere (§9.6's cousin: a ledger has leaves).
- **Modals.** One pattern: the *pasted notice* — a centred slip
  (§4 geometry, rotation 0) over a dimmed desk (`rgba(34,32,28,.45)`),
  entering with the §6.12 cover motion at 300ms, leaving by peel.
  Reserved for confirmations that interrupt (a filing's duplicate
  warning, §6.16). Never for marketing.
- **Toasts.** Refused as a pattern; replaced by the *margin note*: a
  transient confirmation appears as a Caveat note in the margin beside
  what it concerns ("filed — № 1,208"), fading after 6s, and persists
  as a static apparatus line where the record lives. Toasts vanish;
  notes are filed.
- **Tabs.** Ledger tabs (§7's index filters): apparatus caps on a
  hairline, active tab marked by the editor's line segment (2px `--red`
  rule above the tab — the line, again, marks where you stand), counts
  on every tab.
- **Accordions.** *Index expansions*: ruled entries that open like
  §6.17's drawer in miniature (height animation 300ms `--ease-paste`),
  used for year groups and policy clauses. The chevron is a drawn
  editor's caret (^ rotated), never an icon font.
- **Search.** The archive search (§6.17's companion): a ruled input
  labelled "Search the errors", results as §6.15 cards, the result
  count announced as a ledger line ("7 ERRORS MATCH 'FEES'"). Empty
  results use §12's empty voice.
- **Progress.** Only §6.3 and §6.4 exist. A third progress indicator is
  a §10 discussion, not an addition.
- **Tooltips.** *Marginal glosses*: a dotted hairline underline on the
  term; the gloss appears as a Caveat note in the margin on hover/focus
  — the editor explaining a term in the margin, where explanations
  live. On mobile the gloss appears beneath the term in the stacked
  block.
- **Dividers.** The double masthead rule (§6.14) for page heads; the
  single hairline elsewhere; a section that needs emphasis gets the
  editor's line passing through it, not a thicker rule.
- **Avatars / bylines.** The desk has no faces; bylines are apparatus
  lines ("— THE RATES DESK"). A publication that wants author photos
  issues them as §6.11 slip-frames or not at all.

---

## 12. Content & copywriting voice

Two voices, matching §3's two faces. **The press voice** (Source Serif)
states facts: claims, corrections, policies. **The editor's voice**
(Caveat) comments briefly in margins: labels, asides, the one joke
(§6.8). Rules below bind both.

**Headlines (press voice).** A headline in this theme is a claim or a
corrected claim — declarative, specific, falsifiable. ✓ "One fee,
named." ✓ "Two rates, printed plainly." ✗ "Our journey toward radical
transparency" (unfalsifiable, undateable — it could never be corrected,
so it could never run here). If a headline could not conceivably be
struck through one day, it does not belong in the column.

**Statements.** Short sentences. Numbers in full ("0.8%", "£5,000"),
never rounded into fog ("under 1%" is how the original error happened).
Every statement that asserts a fact about the organisation carries, or
is carried by, a date.

**Labels & apparatus.** Ledger register: nouns and counts, caps, no
verbs of excitement. ✓ "212 CORRECTIONS ON FILE". ✗ "Wow — 212
corrections and counting!!" The tally's one licensed flourish is "AND
COUNTING"; its full-stop form is "THAT IS ALL OF THEM." (§6.4).

**Error messages (editor's voice, in forms).** Specific, blameless,
fixable, and written as the desk's note to one reader. ✓ "This needs
the full address — the desk can't file a street with no number."
✗ "Invalid URL." ✗ "Oops! Something went wrong." The desk does not say
oops; the desk files a note. Server errors apologise in the press voice
and state what was preserved (§6.16).

**Empty states.** An empty archive year: "No errors filed in 2019. The
desk was younger then." (press voice, one dry line, no illustration).
An empty search: "No errors match 'banana'. Either we never made that
one, or it is filed under another word." — and a link to file it
(§6.16), because an unmatched search might be an unfiled error.

**Success states.** Confirmations are records, not celebrations: the
filed slip, its number, its status, what happens next (§6.16). No
exclamation marks in the press voice anywhere on the site; the editor's
voice may use exactly one, ever, and §6.8's joke declined to use it.

**Banned words** (press voice): *oops, sorry-not-sorry, journey,
learnings, synergy, delighted, thrilled, mistake-free, perfect record,
minor error* (an error is an error; the desk does not grade its own
shame), and *recently* (dates are dates).

**The apology's rules.** The standing apology (§6.10) is ≤ 60 words,
names the *kind* of wrong (not a specific incident — those have their
own errata), contains no "but", and ends with the mechanism, not the
feeling: ✓ "…When we find one, we print the correction here, dated,
and we keep the original where you can read it." Feelings are the
reader's to have; the column supplies the record.

---

## 13. Full-page scroll choreography map

The canonical article/home page, beat by beat, top to footer. "Sees"
is what is on screen; "feels" is the intended register — the desk's
emotional arc runs *exposure → evidence → accountability → rest*.

1. **Load — the desk rules its sheet.** Masthead rule draws (1200ms,
   parallel with everything below). Sees: the publication line, the
   ledger header with its tally at 0. Feels: a newspaper, opening.
2. **The beat (0–900ms).** The hero claim sits wrong and plain (§6.1).
   Sees: a confident, false headline. Feels: a held breath — the reader
   who knows the theme waits for it; the reader who doesn't, simply
   reads a claim.
3. **The founding correction (900–1610ms).** Strike, slip, shudder,
   stamp (§6.1 timeline). Sees: the brand correct itself. Feels: the
   theme's whole argument, made once, at full size.
4. **The apology takes its seat.** §6.10 pins as erratum 1's section
   scrolls under it. Sees: the apology staying while errors pass.
   Feels: chaperoned — the admissions are supervised.
5. **Errata 1–3 — the ritual, three times.** Each: original struck
   (§6.9), slip lands, stamp thuds, red line ticks through, tally
   counts (§§6.2–6.5). Sees: the pattern become a column. Feels:
   rhythm — by the third, the reader trusts the mechanism and starts
   reading *for* the corrections.
6. **The apology is released.** Erratum 4 begins; the apology's rule
   draws out in grey and it scrolls away (§6.10). Sees: the chaperone
   leave. Feels: the column stands on its own now — the apology has
   done its work and does not linger for credit.
7. **Mid-page evidence.** A §8.2-style section: a corrected table, rows
   ruling in. Sees: a correction with receipts. Feels: the register
   shifts from confession to audit — this is the page's credibility
   peak, placed deliberately past the halfway mark.
8. **The quiet section.** One uncorrected statement block (§4). Sees:
   plain prose, empty margin. Feels: rest — and the empty margin reads,
   by now, as its own claim: *nothing to correct here.*
9. **Cards — the recent record.** §6.15 cards settle in rows. Sees:
   the desk covered in slips. Feels: abundance without performance;
   the ritual is over, the record continues.
10. **The drawer.** §6.17's front: label, count, the Caveat promise.
    If opened: the archive slides out, the days-since counter (§6.8)
    quietly becomes 0. Sees: everything, kept. Feels: the promise
    verified — and the joke, landing like a stamp.
11. **The colophon.** Type credits, the total, the policy link.
    Sees: the column signing its work. Feels: a document, finished —
    the page ends the way a printed column ends, with apparatus, not a
    newsletter blast.

**Reverse pass.** Scrolling up retraces positions only: the red line's
head retreats, parallax re-lags, nothing re-performs, nothing un-strikes.
The map is a ratchet, like the record it describes.

**Other page types** remove beats, never add new kinds: the index
starts at beat 9's register (cards) with its own ledger H1; the record
page is beats 5–7 expanded to fill the sheet; the form page is beat 8's
quiet with §6.16's interactions.

---

## 14. Whole-page performance budget

**Asset budget (first load, article page).**
- HTML ≤ 45KB (the archive drawer ships as links + ≤ 200 ruled entries,
  §6.17; beyond that, year lists lazy-render).
- CSS ≤ 28KB gz. JS ≤ 18KB gz — the theme's entire runtime is one rAF
  loop, one IntersectionObserver queue, the strike measurer, and the
  router hooks (§6.12). Any framework that ships more than the theme's
  own code to run it is a §15 build-order discussion.
- Fonts ≤ 120KB (five files, §3), `font-display: swap`, preloaded
  statement face only.
- Images: slip-frame photographs only (§6.11), `srcset` to their real
  windows, ≤ 160KB per above-fold image, lazy below.

**Runtime budget.**
- One rAF loop; ≤ 0.8ms of JS per frame at steady state (line dash
  write, ≤ 12 parallax transforms, grain opacity). Strike draws and
  counts are CSS/observer-driven, not loop-driven.
- No long task > 50ms from theme code; strike measurement batches via
  `requestIdleCallback` where available, capped at 8 phrases per task.
- Metrics on mid-range Android / 4G: LCP ≤ 2.0s (the LCP element is
  type, §6.14), CLS ≤ 0.02 (slips overlay reserved space; stamps are
  absolutely positioned; the tally's tabular figures prevent numeral
  jitter), INP ≤ 200ms.

**Cut order — what goes first when the budget is exceeded.**
1. The paste-sheen ambient pass (§5) — pure atmosphere.
2. Slip parallax (0.92 → 1.0) and the grain breath.
3. Pointer-tracked tilt (§6.6); the corner lift stays (it carries the
   provenance interaction).
4. Card entry settles on listing pages (§6.15).
5. The stamp's ink-dry blur (§6.5) — the thud stays, the drying goes.
**Never cut:** the drawn strikes, the slip landings, the fallbacks and
watchdogs (§6.1's 900ms law, §6.12's 1200ms law), the reduced-motion
variants, the tally's correctness, or the drawer's completeness. The
theme cuts theatre before it cuts record, every time, in this order.

---

## 15. Build-order checklist

Ordered so that each step only assumes verified earlier steps.

1. **Tokens & type.** Implement §2's tokens (anchors + derived, dark =
   desk-only ruling) and §3's scale; verify contrast figures with a
   checker before any layout exists.
2. **The static sheet.** Build §4's grid (margin / gutter / statement)
   and one complete erratum in its *end state* — struck original,
   landed slip, stamp, both texts in DOM order. Verify with JS and CSS
   disabled: the page must already be the theme, silent.
3. **The fallback laws.** Implement §6.1's 900ms watchdog and §6.12's
   1200ms watchdog against the static build; test by killing scripts
   mid-gesture.
4. **The strike engine.** §6.9's measurement (incl. fonts.ready and
   resize re-measurement) and the ritual queue (§6.2) — strikes in
   reading order, skipped-not-scrambled under fast scroll.
5. **The ritual.** §6.2's beats + §6.5's stamps + §6.1's founding
   gesture, on the observer triggers. Gate: §10 items 2–5 pass.
6. **The audit line.** §6.3's path computation and the shared rAF loop
   (lerp 0.14); §6.4's tally wired to line-pass events, DOM-counted.
   Gate: §10 item 1 (change an erratum; watch every count move).
7. **The apology rail.** §6.10's sticky rail (3 / 2 / static by
   breakpoint), rail computed from DOM order.
8. **Interactions.** §6.6 peek (with focus-within and touch toggle),
   §6.7 press, pointer tilt. Gate: no stuck corners; Esc releases.
9. **Images & cards.** §6.11 frames (with reported-absence fallback),
   §6.15 cards and the index's pagination.
10. **The form.** §6.16 as a working no-JS form first; then focus,
    error-draw, impression, and filed-slip success layered on. Gate:
    values survive a forced server error.
11. **The drawer & colophon.** §6.17 (open-static without JS), §6.8's
    counter and its reset wiring. Gate: §10 item 11 (three counts, one
    number).
12. **Transitions.** §6.12's cover/peel + skeleton with its 3000ms law;
    history-direction geography.
13. **The misprint page.** §6.18, served as real 404, input escaped.
14. **Reduced-motion & print passes.** Every element's variant verified
    against its §6 spec; print stylesheet (line fully drawn at 40%,
    slips in side-by-side positions, drawer open).
15. **Performance pass.** §14's budgets measured; cut order applied if
    needed — theatre first, record never.
16. **The desk test & full gate.** §10 run end to end, blocking items
    first; a five-second reader test (§10.14) with someone who has
    never seen the theme.

---

*End of the expanded specification for theme #15, The Corrections
Column. Companion files: the short library entry in
`themes-001-025.md` (identity source) and `EXPANSION-STANDARD.md`
(structure and laws applied throughout).*
