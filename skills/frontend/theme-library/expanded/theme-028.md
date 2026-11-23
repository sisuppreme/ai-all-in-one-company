# 28. Errata Slip — Expanded (v1 + v2)

The tiny tipped-in slip that corrects a whole print run, made into a
complete interface language. Identity preserved exactly from the
library entry: the same concept (every claim is provisional; the
design language is the slip itself — small, pasted, slightly crooked,
absolutely authoritative), the same four palette anchors (Book cloth
blue `#31435C`, Slip paper `#F6EFDB`, Paste shadow `#C9BFA5`, Errata
red `#B23A2E`), the same two typefaces (EB Garamond for the "book",
IBM Plex Mono for the slips), and all nine original signature
elements deepened — never redesigned — plus three further signatures
drawn out of the original motion system and six page-family elements,
eighteen in all.

## 1. Concept & world

An errata slip is the most honest object in publishing. A book goes
out into the world carrying a mistake; the publisher cannot recall
the print run, so it prints a small slip — *tipped in* by hand at the
front of the book — that says, in the trade's fixed formula, *for
"1,200" read "12,000."* The slip is small because paper is money. It
is pasted because it arrived after binding. It is crooked because a
human pasted it, quickly, thousands of times. And it outranks the
page it sits on: wherever slip and book disagree, the slip is right.
This theme builds a website out of that object and that hierarchy.

The world of the theme is the publisher's back office at the moment
of correction: a calm, well-set book page (EB Garamond, generous
measure, nothing hurried) lying open on its own cloth-blue binding,
and over it a population of small mono slips, each one pasted at a
slight angle over the exact value it corrects. The page does not
pretend to have been right all along. Its corrections are visible,
numbered, cumulative and auditable — a numbered errata index closes
the page, and the index and the slips correspond one-to-one. The
visitor's experience is not "a page with decorations" but "a document
whose provenance I can check": hover a slip and its corner lifts to
show the superseded value printed beneath; scroll and the margin
carries the current erratum beside the passage it corrects; reach the
foot and the index holds every correction the page has made, in
order, like the back matter of a corrected edition.

**The theme's one law: the slip annotates the datum; it never
carries it.** The corrected value is the text content of the page
itself, set in the book's own type, present in the DOM, readable with
JavaScript disabled, findable by search engines and screen readers.
The slip is a pasted annotation layer that points at the correction,
dates it and numbers it. Any build in which removing the slip removes
the corrected value has broken the law and fails the gate (§10) —
that inversion is the difference between this theme and a sticker
pack.

**The second law: no slip is ever straight.** Every slip sits at a
rotation between 0.5° and 1.5°, its angle derived deterministically
from its erratum number (§4), because a straight slip is a lie about
how it got there — and because the visitor's eye reads the slight
crookedness as *pasted by hand*, which is the theme's entire claim to
authority. A slip at 0.0° is a build defect, caught at the gate.

**The third law: every slip is numbered, and the numbers are the
page's count of itself.** Slips are numbered in reading order —
Erratum No. 1, No. 2, … — and the header counter, the margin pin and
the closing index all read from the same DOM population. A page that
shows "Erratum No. 14" in the header must contain exactly fourteen
slips above the fold of the index, and the index must list fourteen
rows. Invented numbering — a decorative "No. 14" on a page with six
slips — is the theme's cardinal fabrication and a blocking gate
failure.

**Best-fit sites and audiences.** Anywhere the content's credibility
depends on showing its corrections: a pricing page for a product
whose prices genuinely changed (and whose publisher wants the change
seen, not silently swapped); documentation and changelogs for
software, standards or datasets, where "what changed and when" is the
product; journalism corrections pages and updated explainers; academic
and reference publishing; financial or scientific figures that were
republished after review; a museum or archive catalogue whose records
are amended as research lands. The audience is the sceptical reader —
the one who checks. The theme rewards checking: every gesture in it
(corner-lift, index, margin pin) is an audit affordance.

**When NOT to use it.** (1) When there are no real corrections to
show. A page with nothing to correct that pastes slips on itself
anyway is wearing a costume, and the audience this theme attracts
will lift a corner, find nothing beneath, and leave. If the content
has never been wrong, use another theme. (2) For content where a
visible correction history would be dangerous or unlawful to display
— live medical dosing, real-time safety instructions — where the
superseded value must not remain legible anywhere, even beneath a
lifted corner. The theme's honesty requires the old value to survive
under the slip; where survival itself is the hazard, do not build
here. (3) For high-frequency data (prices ticking by the second,
live availability): slips paste at editorial speed, and a page that
needs forty corrections a minute is a feed, not a corrected edition.
(4) For pure brand theatre with no data on the page at all — the
slips need values to sit on; a hero with nothing to correct gives the
flutter (§6.1) nothing honest to do.

## 2. Palette

Four anchors from the library entry, plus a closed list of derived
tokens. Contrast figures below are measured, not estimated.

| Token | Hex | Role | Usage |
|---|---|---|---|
| `--cloth` | `#31435C` | Book cloth blue — the ground the open book lies on; header band, footer field, the margin rail's ground | ~18% of viewport (the surround) |
| `--slip` | `#F6EFDB` | Slip paper — every slip's ground; the colour of correction itself | ~6% (slips only; never a section background) |
| `--paste` | `#C9BFA5` | Paste shadow — the offset shadow/glue tone under every slip; brush strokes; slip edge shading | ~2% (shadows and strokes only, never text: 1.74:1 on page, decorative by law) |
| `--red` | `#B23A2E` | Errata red — stamps, erratum numbers on slips, the correction formula's verb, error states | ≤3% (rationed; see pairing rules) |
| `--page` | `#FCF9F0` | Derived: the book's leaf — page ground, card ground | ~70% (the reading surface) |
| `--ink` | `#26231C` | Derived: book ink — all Garamond text, slip mono text | body text everywhere |
| `--red-deep` | `#8E2B21` | Derived: red for small text (≤13px) where `--red` alone is insufficient on slip paper | small red text only |
| `--note` | `#5C564A` | Derived: the pencil-grey of apparatus — captions, index folios, superseded values | secondary text |
| `--cloth-light` | `#7E97B5` | Derived: cloth's lightened step for text and hairlines *on* cloth grounds | on-cloth text only |

**Measured contrast (WCAG ratios).** `--ink` on `--page` 14.89:1;
`--ink` on `--slip` 13.65:1; `--red` on `--slip` 5.17:1 (passes AA
for text ≥12px, and is the slip's stamp colour); `--red` on `--page`
5.64:1; `--red-deep` on `--slip` 7.26:1 (AAA — mandatory for red text
under 13px, e.g. the index's fine rows); `--slip` on `--cloth`
8.76:1 (slips pasted onto cloth-coloured furniture stay legible);
`--cloth` on `--page` 9.55:1; `--note` on `--page` 6.91:1, on
`--slip` 6.34:1; `--paste` on `--page` 1.74:1 — `--paste` is a shadow
and a glue tone and is **banned from carrying text, icons or
meaning** at any size.

**Pairing rules.** (1) A slip is always `--slip` paper with `--ink`
mono text, a `--paste` offset shadow, and at most one red element
(its number or its stamp — never both, never a red slip). (2) Red
never appears on the book page except inside a slip, a stamp, or an
error state; red loose on the page is clip-art urgency and breaks the
fiction that red is the corrector's pencil. (3) `--cloth` grounds
never carry `--ink` text; on cloth, text is `--slip` (8.76:1) or
`--cloth-light` (4.81:1 on the darkened cloth, large/apparatus only).
(4) The superseded value beneath a slip is set in `--note` with a
Garamond italic strikethrough — present, legible (6.34:1), and
visibly demoted.

**Dark-mode behaviour — the lamplight ruling.** The theme does not
invert; it is *read by lamplight*. Under `prefers-color-scheme:
dark`: the cloth deepens to `--cloth-deep #1E2A3C`, the leaf warms
and dims to `--page-lamp #EFE6CC`, slip paper dims one step to
`--slip-lamp #EDE3C8`, and `--ink` is unchanged (12.59:1 on the lamp
leaf). Errata red is held at `#B23A2E` — on the dimmed slip it
measures 4.64:1, lawful for stamps and slip numbers at ≥12px — while
small red text drops to `--red-deep` (6.52:1 on lamp slip). The glue
sheen (§6.7) warms from white 10% to amber 12%: lamplight is the one
place the sheen is allowed a colour. Paste shadow deepens to
`#8E8265` so slips still lift off the dimmed leaf. Nothing about the
slips' rotation, numbering or order changes after dark; only the
light does.

## 3. Typography

Two families, never swapped — the casting law of this theme: **EB
Garamond is the book; IBM Plex Mono is the slip.** Garamond speaks
for the published text (claims, prose, values); mono speaks for the
correction layer (slips, numbers, stamps, the index's data columns).
A slip set in Garamond is a paragraph pretending; a headline set in
mono is a database pretending. The gate checks the casting.

**EB Garamond** (book voice): display 54px/1.04, −0.01em tracking,
for the title page's book title (§6.13); H1 38px/1.12; H2 29px/1.18;
H3 22px/1.25; body 19px/1.58 — books are set large and this theme
keeps the courtesy; values (prices, statistics, dates as they appear
in prose) are body-size Garamond with `font-variant-numeric:
lining-nums` so a corrected figure sits on the same baseline as the
sentence around it; captions and apparatus 15px/1.5 italic in
`--note`; the superseded value beneath a slip is 17px italic
`--note` with a 1px strikethrough. Garamond's old-style figures are
used in prose; lining figures are mandatory inside tables (§6.15) and
beside slips, where old-style numerals would misalign against the
mono.

**IBM Plex Mono** (slip voice): slip text 12.5px/1.45 — small,
because a slip is small, but never below the 12px floor at any
breakpoint (a correction you cannot read is a correction withheld);
slip headline formula ("for … read …") 12.5px medium; erratum
numbers 11px, uppercase, letter-spacing 0.09em, in `--red` (or
`--red-deep` under 13px contexts per §2); stamps 11px uppercase,
0.14em tracking; the header counter and index numerals in mono
tabular figures (`font-variant-numeric: tabular-nums` is mandatory
on every counter in the theme — a rolling counter that changes width
is a counter that shakes the page). Mono is never used for prose
longer than a slip's ~90 characters; a correction that needs a
paragraph gets a footnote in Garamond and a slip that points to it.

**Type laws.** (1) The correction formula is fixed and verbatim:
`for "X" read "Y"` — the trade's wording since the nineteenth
century; paraphrases ("X should be Y", "update: Y") are banned in
slip text (the voice section, §12, gives the full formula set).
(2) Every slip carries, in order: its number, the location it
corrects ("p.2 · Prices"), the formula, and its stamp date. A slip
missing any of the four is a sticker, not an erratum. (3) Garamond
headings are never corrected *in* Garamond: when a heading is
corrected, the corrected heading is the DOM text and a slip pasted at
its end carries the formula pointing back at the superseded wording
in the index. (4) Numerals in slips are always the exact values —
"for 1,200 read 12,000", never "for a small number read a bigger
one".

## 4. Layout language

**The open book on its cloth.** The page is a leaf of `--page`
(max-width 1240px, centred) lying on a full-viewport `--cloth`
ground visible at the edges — the visitor is looking down at an open
book on a table, and the cloth surround is what makes the slips'
paste shadows read as shadows. The leaf carries a 1px `--paste`-tone
edge and a soft ambient shadow (24px blur, cloth-darkened) so it sits
*on* the cloth rather than floating in a void. On <768px the leaf
goes full-bleed (the book fills the phone; the cloth survives as the
header and footer bands only).

**Grid and measure.** Book prose sets in a 62ch measure inside a
12-column leaf grid; the right-hand margin column (columns 10–12,
min 220px at ≥1200px) is the **working margin** — the home of the
margin pin (§6.3), folio notes and slip overflow. Slips are sized to
their content (mono 12.5px, padding 8px 10px, max-width 300px) and
positioned over the value they correct, anchored to the value's
inline box, never placed by absolute page coordinates — a slip must
follow its datum through reflow, zoom and font substitution, because
a slip that drifts off its value is a false claim.

**The rotation law, made deterministic.** Slip *n*'s rotation is
`0.5 + ((n × 37) mod 100) / 100` degrees — a value in [0.5°, 1.49°] —
with sign positive (clockwise) for odd *n*, negative for even *n*.
Two builders given the same page produce the same crookedness; the
angles look hand-scattered because 37 and 100 are coprime, and no two
adjacent slips share an angle. Rotations are applied to the slip
element only, never to its text layout (the mono block inside stays
axis-aligned to the slip, which is itself the rotated frame).

**Density rules.** Slips are rationed like the paper they imitate:
at most **one slip per viewport-height of reading** in body sections,
and at most **three slips visible in any single viewport** anywhere
on the page. A page with more corrections than that has a density
problem the index (§6.17) exists to solve — overflow corrections live
as index rows with margin markers, not as a blizzard of paper. The
hero is the single exception: three slips by design (§6.1). Paste
shadows offset 3px down / 2px right at rest (the light is from the
upper left everywhere in the theme; a shadow in any other direction
is a different room).

**Whitespace.** The book's calm is the theme's luxury and the slips'
contrast: sections breathe at 96px vertical rhythm on the leaf, and
the working margin is kept empty except when the pin is resident —
an always-full margin would make the pin invisible. Whitespace in
this theme is the uncorrected page: the larger it is, the more the
few corrections matter.

## 5. Full motion system

Every motion term, translated into the theme's own materials — paste,
paper, the corrector's hand. One shared `requestAnimationFrame` loop
drives all scroll-scrubbed values with lerp **0.12**; nothing in the
theme runs its own scroll listener.

**Named easings.** `--ease-paste: cubic-bezier(0.22, 1, 0.36, 1)` —
a slip settling onto wet paste: fast approach, long soft landing.
`--ease-flutter: cubic-bezier(0.3, 1.35, 0.5, 1)` — paper falling:
descent with a rotational overshoot as the slip finds its angle.
`--ease-press: cubic-bezier(0.65, 0, 0.35, 1)` — the flat of a hand
pressing: symmetric, firm, no bounce. `--ease-brush: cubic-bezier(0.4,
0, 0.2, 1)` — a loaded brush pulled at constant speed.
`--ease-peel: cubic-bezier(0.7, 0, 0.25, 1)` — a corner lifting
against paste resistance, then giving.

**Scroll-triggered reveals.** Corrections paste over as their
sections enter (§6.2): the slip arrives from its glued edge in 460ms
`--ease-paste` as the datum crosses 78% viewport height. Book prose
itself does not reveal-animate — a book page is printed, not
performed; only the correction layer moves, which is why its motion
reads as an event. **Parallax.** Slips travel at 0.94× the book's
scroll rate (§6.11) — a 6% lag, sold by their paste shadows widening
to 5px at mid-lag — because pasted paper sits *on* the page, not in
it. **Pinned scenes.** The margin pin (§6.3): the current erratum
held in the working margin, scrubbed by the shared loop, swapping by
crossfade as new corrections pass. No other pinning exists in the
theme; a corrected book does not do set pieces. **Masked reveals.**
Slip text reveals through its pasted edge (§6.10): a clip mask wipes
from the glued edge across the slip in 380ms as the paste lands, so a
slip is read in the order it was pasted. **Blur-to-sharp** is refused
in this theme, with a reason: a correction must never be illegible,
even for a frame — the corrector's pencil does not do soft focus.
**Counters.** Figures roll to their corrected values (§6.5), 800ms,
timed to land as their slip pastes; the header's "Erratum No. n"
advances by step, not roll (§6.14). **Progress.** The header erratum
counter plus the accumulating index (§6.8) — progress in this theme
is a count of corrections witnessed, because that is the page's real
through-line. **Marquee** is refused: nothing in a corrected edition
loops sideways; the refusal is recorded here so no builder adds one.
**Ambient loops.** One only: the glue sheen (§6.7), a specular edge
highlight cycling slip to slip at 4s each, the theme's breathing.
**Micro-interactions.** Corner-lift on hover (§6.4), press-flat and
re-stamp on click (§6.12), slip-miniature hover states in the index
(§6.17). **Hover physics.** The corner lift is a true 3D rotate on
the slip's free corner axis with shadow deepening — paper physics,
small and exact; no magnetic buttons exist here, the corrector's hand
does not wobble. **Page transitions.** The full-page slip (§6.9):
navigation pastes a leaf-sized slip over the viewport and peels it
from its free corner. **Image treatments.** Images in the book are
printed plates: they arrive already on the page (no treatment), but a
corrected *caption* gets a slip like any other value, and a replaced
image wears its predecessor's outline as a `--paste` hairline frame
for one edition — the ghost of the old plate, kept honest.

**Global motion rules.** Every animation is armed by JS only: the
DOM ships in the finished, corrected, fully readable state, and JS
adds pre-states (un-pasted slips, un-rolled counters) only when it
can guarantee the animation will run. A global 900ms watchdog —
inherited from the library entry ("900ms fallback presses all slips
flat") — forces every slip to its final state if any trigger misfires.
`prefers-reduced-motion` collapses the theme to its printed state:
slips present and flat, corrections footnoted inline (§6 variants
specify each element's ruling).

## 6. Signature elements

### 6.1 Title correction flutter

- **What & why.** The theme's thesis performed on its own title
  before the visitor reads a word of body copy. The title page opens
  calm — the book's original, wrong title set large in Garamond — a
  beat of stillness, and then three small mono slips flutter down and
  paste over it, correcting it into the real title. The page's first
  act is to correct itself, in public, with numbered slips. It
  belongs here because errata slips were tipped in at the front of
  the book: the correction is quite literally the first thing a
  reader of a corrected edition meets, and a hero that performs the
  theme's law ("every claim is provisional, including ours") earns
  the visitor's trust for every correction that follows.
- **Structure.** A `<header class="title-page">` (§6.13) holding the
  real, corrected `<h1>` as the DOM text — search engines, screen
  readers and no-JS visitors meet the true title. Above it, an
  aria-hidden stage layer holds the *superseded* title set in
  identical Garamond (the "first printing" of the heading), and three
  `.slip` elements anchored to the words they correct within that
  stage. Each slip carries the full slip anatomy (§3): number,
  location ("Title page"), formula (`for "…" read "…"`), stamp date.
  The stage layer is inserted by JS only; without JS it never exists
  and the h1 simply stands.
- **Motion spec.** Trigger: load, after fonts settle or 600ms,
  whichever is sooner — the flutter must not begin over a FOUT
  reflow. A held beat of **500ms** of stillness first (the calm is
  part of the spec; a correction that arrives instantly reads as a
  gimmick, one that arrives after a breath reads as a decision). Then
  the three slips flutter in erratum-number order, staggered 160ms:
  each falls `translateY −30px → 0` while its rotation travels from
  ±4° of overshoot to its lawful angle (§4: No. 1 → +0.87°, No. 2 →
  −1.24°, No. 3 → +0.61°), **500ms `--ease-flutter`**, landing with a
  60ms paste-shadow bloom (shadow offset 2px→3px, blur 0→2px). As the
  third slip lands, the superseded title beneath the slips crossfades
  its uncorrected words to `--note` italic (300ms) — the wrong title
  is demoted, not deleted, exactly as a real first printing survives
  under its tipped-in correction.
- **Choreography timeline (v2).** t₀ = stage armed (fonts settled) →
  t₀+0–500ms: stillness, the wrong title alone → t₀+500ms: slip No. 1
  begins its fall → t₀+660ms: No. 2 → t₀+820ms: No. 3 → t₀+1000ms:
  No. 1 landed, shadow bloomed → t₀+1320ms: No. 3 landed → t₀+1320–
  1620ms: uncorrected words demote to `--note` italic beneath the
  slips → t₀+1620ms: the header counter (§6.14) steps to "Erratum
  No. 3" and the index (§6.8) shows its first three rows — the hero
  and the apparatus agree from the first screen.
- **State matrix (v2).** *Rest (pre-trigger):* the corrected h1
  alone; the stage layer does not exist until armed. *Hover:* slips
  in the hero accept the corner-lift (§6.4) like any slip — the
  visitor can lift No. 2 and read the wrong word beneath within the
  first screen. *Focus:* slips are not focusable in the hero (their
  content is duplicated in the index, §6.17, which is the keyboard
  route to every correction). *Active:* n/a. *Scrolled-past:* the
  stage remains, static, slips flat — the flutter never replays on
  scroll-back; a correction is made once. *Disabled (no JS):* the
  corrected h1 with a Garamond footnote line beneath it — "This title
  was corrected by Errata Nos. 1–3; see the index" — the designed
  state, complete.
- **Content merge.** The slips correct the page's actual title, word
  by word; the superseded wording under them is the genuine earlier
  title (the content team supplies it — it is a content requirement,
  not a visual effect: §10 gates on the superseded title being a real
  prior title, not placeholder text). Remove the stage and the hero
  is a title page with a footnote: poorer, complete.
- **Failure fallback.** The 900ms global watchdog applies per slip:
  any slip whose flutter has not completed by trigger+900ms is
  pressed flat instantly at its lawful angle. If the stage layer
  fails to build (missing superseded title in content), the flutter
  is skipped entirely and the hero ships as the no-JS state — a
  correction performance with nothing real to correct is never faked.
- **Reduced-motion variant.** No fall, no demote crossfade. The stage
  appears already assembled — wrong title demoted, three slips flat
  at their angles — or, at the visitor's stricter setting, the slips
  are omitted and the footnote line carries the corrections inline,
  per the library entry's ruling ("corrections as footnoted inline
  values with static slips" is the floor, not the ceiling).
- **Breakpoints (v2).** ≥1200px: as specced; slips up to 300px wide
  over a 54px title. 768–1199px: title 44px, slip max-width 260px,
  stagger tightens to 130ms. <768px: the stage stacks — superseded
  title at 34px, slips land beneath the words they correct rather
  than over them if the title wraps past two lines (a slip covering a
  wrapped line it does not correct is a false claim), fall distance
  shortens to −18px, stagger 110ms.
- **Edge cases & failure modes (v2).** *Title shorter than three
  correctable words:* the flutter uses as many slips as there are
  real corrections — one or two — and the numbering continues from
  there; a third slip is never invented to complete the choreography.
  *Very long real title:* the stage caps at three slips; further
  title corrections live only in the index. *Font swap mid-flutter:*
  arming waits for `document.fonts.ready` or the 600ms cap, so slips
  never land on a title that then changes font beneath them. *Return
  visit in the same session:* the flutter replays (it is the page's
  greeting), but a `sessionStorage` flag shortens the held beat to
  150ms for repeat views — courtesy, not concealment.
- **Accessibility spec (v2).** The stage layer is `aria-hidden` in
  full: its text duplicates the h1's correction history, which the
  index (§6.17) exposes accessibly with real links and text. The h1
  is the corrected title, always. The demote crossfade never takes
  the superseded title below `--note` on `--page` (6.91:1) even in
  its aria-hidden state — visual visitors with low vision still read
  the fiction correctly. No focusable element exists in the hero
  stage; keyboard order passes from the running head (§6.14) to the
  first body link undisturbed.
- **Performance budget & mobile variant.** Three small absolutely
  positioned elements, transform/opacity only, ≤0.3ms/frame in the
  shared loop's accounting; the stage layer is ≤6KB of DOM. Mobile:
  same three elements, shortened falls as above; the stage is the
  cheapest signature in the theme and is never cut.
- **Tokens consumed (v2).** `--page`, `--ink`, `--note`, `--slip`,
  `--paste`, `--red`, `--ease-flutter`, `--ease-paste`, `--lerp`.

### 6.2 Value paste-overs

- **What & why.** The theme's workhorse: wherever a figure on the
  page has changed — a price, a statistic, a date, a name — a slip
  pastes over the old value's position as the section enters,
  announcing the correction at the exact datum it corrects. It
  belongs here because an errata slip's whole geometry is *on top of
  the error*: the correction's authority comes from its position, and
  a change log detached from the values it changes is precisely the
  silent-swap behaviour this theme exists to refuse.
- **Structure.** Each corrected datum is a `<span class="datum">`
  containing the corrected value as its text (the law, §1), wrapped
  in a `<span class="corrected">` anchor that also holds the slip:
  an `<aside class="slip">` positioned over the datum's inline box,
  offset so its glued (top) edge sits 2px above the value's cap
  height, rotated per §4. The superseded value is present in the
  anchor as a visually-hidden-until-lift layer printed *beneath* the
  slip's footprint (§6.4 reveals it). Slips annotate; the datum's own
  text is always the corrected value, slip or no slip.
- **Motion spec.** Trigger: the datum crossing 78% viewport height,
  once. The brush stroke draws first (§6.6, 300ms `--ease-brush`),
  then the slip scales in from its glued edge — `transform: scale(0.82,
  0.6) → 1` with `transform-origin` at the glued edge's midpoint,
  rotation travelling from its lawful angle ±1.2° to its lawful
  angle — **460ms `--ease-paste`**. The datum's own figure rolls to
  its corrected value in synchrony (§6.5) so number and slip land as
  one event. Paste shadow fades in across the final 120ms.
- **Choreography timeline (v2).** t₀ = datum crosses 78% vh →
  t₀+0ms: brush stroke begins under the slip's footprint → t₀+300ms:
  stroke complete; slip begins scaling from its glued edge → t₀+460ms:
  counter roll (§6.5) begins on the datum → t₀+760ms: slip fully
  pasted, shadow set → t₀+880ms: the margin pin (§6.3) swaps to this
  erratum and the header counter steps — the apparatus acknowledges
  the correction 120ms after it lands, like a clerk initialling a
  ledger line after the paste dries.
- **State matrix (v2).** *Rest (pre-trigger, JS-armed only):* slip
  held at scale 0.82/0.6, opacity 0 — a state that exists for at most
  the scroll into view; the no-JS and watchdog states are the pasted
  slip. *Hover:* corner-lift (§6.4). *Focus:* a slip whose datum is a
  link inherits the link's focus — the slip lifts its corner on
  `:focus-visible` of the datum, so keyboard visitors get the
  provenance gesture too. *Active:* press-flat (§6.12). *Scrolled-past:*
  pasted, permanent; paste-overs never un-paste on scroll-back — the
  historical record does not rewind. *Disabled (no JS):* slip present,
  flat, at its angle, beside a datum already showing the corrected
  value; the superseded value is listed in the index row.
- **Content merge.** The slip sits on the datum it corrects and says
  what changed (`for "£42" read "£48"`); the datum beneath is the
  page's real, current figure. The animation is the act of correction
  applied to live content — detach the slip and the figure is still
  correct, merely unprovenanced.
- **Failure fallback.** Watchdog at trigger+900ms presses the slip
  flat at final state. If the datum's content changes after arming
  (live region update), the slip re-anchors to the new inline box and
  its formula is re-read from data attributes — a slip pointing at a
  value it no longer matches is withdrawn (display:none) and its
  index row is struck, never left lying.
- **Reduced-motion variant.** The slip is present and flat from first
  paint of the section; the counter does not roll (the corrected
  figure simply stands); the brush stroke is drawn complete. The
  correction's information content is identical; only the pasting is
  omitted.
- **Breakpoints (v2).** ≥1200px: slips overlay the datum in place,
  max-width 300px. 768–1199px: max-width 260px; a slip whose datum
  sits in the measure's last 15% anchors from its right edge instead
  so it never crosses the working margin's boundary. <768px: slips
  stop overlaying — each corrected datum gains its slip *beneath* it,
  full-measure width up to 340px, still rotated (the angle survives;
  the overlay does not, because a 300px slip over a 340px measure
  would bury the sentence it corrects). Rotation, numbering and
  formula are unchanged at every size.
- **Edge cases & failure modes (v2).** *Two corrected data in one
  line:* their slips stagger 120ms apart in reading order and the
  second slip's footprint is checked against the first's — if they
  would overlap, the second drops to the below-datum position even on
  desktop (overlap rule: slips never cover another slip's formula).
  *Datum inside a table:* §6.15's table ruling applies (slip in the
  cell's correction gutter, not over the figure). *Datum longer than
  the slip (a corrected name):* the slip covers the name's first
  line-box only and its formula carries the full old and new names.
  *Correction of a correction:* a datum corrected twice wears one
  slip — the latest — whose formula reads `for "£42" read "£48"`
  against the *current* predecessor, and the index keeps both rows,
  the earlier struck. Slips never stack two-deep on one datum; paste
  is not geology.
- **Accessibility spec (v2).** The slip is an `<aside>` with
  `aria-label="Erratum No. 7: for £42 read £48, corrected 12 March"`,
  placed immediately after its datum in DOM order, so a screen reader
  meets value, then provenance, in reading order. The corrected value
  itself is plain text — never an image, never split across spans.
  Slip text contrast: `--ink` on `--slip` 13.65:1; the red number
  5.17:1 at 11px is the theme's one deliberate AA-large-style
  exception — it is duplicated in the aria-label and the index, and
  `--red-deep` (7.26:1) is used wherever the number stands alone
  (index rows). Touch: the slip's tap target is its full box, min
  height 36px via padding, and tap performs the press-flat (§6.12)
  rather than the hover lift.
- **Performance budget & mobile variant.** One transform animation
  per datum, ≤0.2ms/frame; slips are DOM text, no assets. Cap: at
  most 3 paste-overs animating concurrently (the density rule, §4,
  makes this natural); further triggers queue at 120ms intervals.
  Mobile: below-datum placement as above; scale-in shortens to 380ms.
- **Tokens consumed (v2).** `--slip`, `--paste`, `--ink`, `--red`,
  `--red-deep`, `--ease-paste`, `--ease-brush`, `--lerp`.

### 6.3 Margin pin erratum

- **What & why.** The current correction, held beside the passage it
  corrects. As the visitor scrolls, the most recently passed slip
  pins in the working margin and travels with the reading position
  until the next correction replaces it — the margin becomes a live
  provenance rail, so at any moment the visitor can glance sideways
  and see *the state of the page's honesty right here*. It belongs
  here because real corrected books were read with the errata leaf
  held open beside the text; the pin is that held-open leaf, doing
  the oldest job in scholarly reading: keeping the correction and the
  passage in the same field of vision.
- **Structure.** A `<div class="margin-pin">` in the leaf's working
  margin (columns 10–12), `position: sticky; top: 96px`, holding a
  miniature of the current slip (`.slip.is-mini`: same paper, same
  rotation law at half scale of presence — rotation unchanged, type
  at 11.5px floor via a scaled duplicate, never below legibility) plus
  a hairline leader rule in `--paste` tone pointing from the pin to
  the margin edge of the passage it corrects. The pin's content is a
  live duplicate of the source slip's data (number, formula, date),
  rendered from the same content source, not a second hand-written
  copy.
- **Motion spec.** The pin is scrubbed by the shared rAF loop (lerp
  0.12) only in that its *swap* is smoothed: when a new correction's
  datum crosses 50% viewport height, the resident pin crossfades —
  old mini-slip fades and sinks 6px over 200ms, new one rises and
  fades in over 240ms `--ease-paste`, the leader rule redraws
  (scaleX 0→1, 180ms). Between swaps the pin is still: sticky
  positioning does the travelling, and any additional bobbing would
  be a leaf trembling in a still room. The swap fires 120ms after the
  source slip's paste completes (§6.2's timeline), never before —
  the margin reports corrections that have happened, not ones about
  to.
- **Choreography timeline (v2).** t₀ = new datum's paste completes →
  t₀+120ms: swap begins; resident mini-slip fades to 0, sinks 6px
  (200ms) → t₀+200ms: leader rule collapses → t₀+240ms: new mini-slip
  at final angle, opacity 1, leader redrawn → t₀+320ms: swap settled;
  the pin's erratum number is now the header counter's number (§6.14
  steps at the same beat — the two apparatuses never disagree in
  view).
- **State matrix (v2).** *Rest:* the pin shows Erratum No. 1's
  miniature from page load (the first correction is the standing
  context until a later one passes). *Hover:* the mini-slip lifts
  its corner exactly as its source slip does (§6.4), revealing the
  superseded value — the pin is a working slip, not a picture of one.
  *Focus:* the pin contains one link, "See in the index", focusable,
  with the theme's focus ring (2px `--red` outline offset 2px — red
  is lawful here, inside the correction apparatus). *Active:* click
  on the mini-slip scrolls the source datum into view and flashes
  its slip's corner lift once — the pin can take you to its passage.
  *Scrolled-past:* after the final correction, the pin remains
  resident showing the last erratum until the index (§6.17) enters,
  where it un-pins and docks as the index's header row — the rail
  hands over to the full record. *Disabled (no JS):* no pin (sticky
  duplication without swap logic would strand a random correction in
  the margin); the margin carries a static Garamond note instead:
  "Corrections are listed in the index at the foot of this page."
- **Content merge.** The pin *is* the current correction — the same
  number, formula and date as the slip on the datum — relocated to
  where the reader's eye rests. It adds no information and removes
  none; it is the index's data worn at reading distance.
- **Failure fallback.** If the swap logic fails, the pin freezes on
  its current erratum rather than blanking — a stale pin is a
  clerical error, an empty margin is a missing leaf. If the working
  margin is unavailable (viewport <1200px), the pin does not render
  in the margin at all; see breakpoints.
- **Reduced-motion variant.** Swaps are instant (no crossfade, no
  sink); the leader rule is drawn complete. The pin's information
  rhythm — current correction beside current passage — is unchanged.
- **Breakpoints (v2).** ≥1200px: full spec, margin rail resident.
  768–1199px: the margin is too narrow for a legible mini-slip, so
  the pin becomes a slim correction tab fixed to the leaf's right
  edge: erratum number + a 24px slip-paper tab; tapping it opens the
  current correction as a below-datum slip (§6.2's mobile position)
  under the passage in view. <768px: no pin and no tab — the header
  counter (§6.14) alone carries the running provenance, and each
  slip's below-datum placement keeps corrections adjacent to their
  data. The pin is the first element cut on small screens, by design:
  adjacency beats apparatus.
- **Edge cases & failure modes (v2).** *Long gaps between
  corrections:* the pin simply remains — a margin holding one
  correction for three screens is correct behaviour, not a stall; the
  pin never invents filler content. *Two corrections within one
  viewport:* the pin shows the later (the one nearest the reading
  line at 50% vh) and the earlier remains available via its own slip.
  *The datum is inside the pinned region itself (a corrected figure
  in a sticky table head):* the pin yields — it fades to 40% while
  the sticky head is resident, rather than duplicating a correction
  already in view. *Print:* the pin is hidden in print; the index
  prints in full (print is the theme's home medium and the index is
  its print-native apparatus).
- **Accessibility spec (v2).** The pin is `aria-hidden` as a duplicate
  (its content exists accessibly at the slip and in the index),
  *except* its "See in the index" link, which is a real, labelled
  navigation aid and remains in the tab order. Swap changes are never
  announced — a live region chirping every correction would make the
  page unreadable by ear; the index is the accessible record, reached
  by the link. Focus ring as above; the tab variant's tap target is
  44×44px minimum.
- **Performance budget & mobile variant.** One sticky element, one
  crossfade per correction, ≤0.2ms/frame; the leader rule is a
  transform. Mobile: cut entirely (see breakpoints) — its budget is
  spent on the below-datum slips instead.
- **Tokens consumed (v2).** `--slip`, `--paste`, `--ink`, `--red`,
  `--note`, `--ease-paste`, `--lerp`.

### 6.4 Corner-lift provenance

- **What & why.** The audit gesture. Hovering (or focusing, or
  long-pressing) a slip lifts its free corner — the corner away from
  the glued edge — rotating up in 3D so the superseded value printed
  beneath shows in the revealed wedge. Old and new coexist on the
  page; this gesture is how the visitor checks one against the other.
  It belongs here because provenance you cannot inspect is just a
  claim: the theme's authority rests on the old value genuinely being
  *there*, under the paper, one gesture away, exactly as a reader can
  lift a real tipped-in slip and read the printed error beneath it.
- **Structure.** The slip is two layers: the slip face (`.slip-face`,
  the mono annotation) hinged along its glued edge via a wrapper with
  `perspective: 600px` and `transform-origin` on the glued edge; and
  beneath its footprint, printed on the page in the anchor's flow, the
  superseded value in 17px Garamond italic `--note` with
  strikethrough (§2's pairing rule), positioned to occupy the datum's
  box. At rest the slip covers it exactly; the lift rotates the face
  around the glued edge so the free corner rises and the old value
  shows beneath the raised wedge.
- **Motion spec.** Trigger: hover (pointer fine), `:focus-visible` of
  the slip or its datum, or a 450ms long-press on touch. The face
  rotates `rotateX/rotateY` (axis = the glued edge; for a top-glued
  slip, `rotateX(0 → −24°)` about the top edge) over **320ms
  `--ease-peel`** — slow at first against the paste, then giving. The
  paste shadow beneath deepens and stretches as the corner rises
  (offset 3px→7px, blur 2px→6px, opacity 0.55→0.8), and a glue-sheen
  line (§6.7's material) brightens along the hinge. Release reverses
  over 260ms `--ease-press` — the corner settles back onto its paste
  with the press easing, never a snap. Maximum lift 24°: enough to
  read the old value's line, never so much the slip appears detached;
  a slip floating free of its page is a sticker again.
- **Choreography timeline (v2).** t₀ = hover/focus/long-press →
  t₀+0–80ms: paste resistance — the corner strains 0→4° (the ease's
  flat head) → t₀+80–260ms: the give — 4°→22°, shadow stretching in
  step → t₀+320ms: rest at 24°, hinge sheen at full → held: the old
  value is readable for as long as the gesture holds → release: 260ms
  press back to flat, shadow relaxing over the final 100ms.
- **State matrix (v2).** *Rest:* flat, old value covered. *Hover:*
  lift as specced. *Focus:* identical lift (keyboard parity is a law
  in this theme — every hover behaviour has a focus twin). *Active
  (pressing):* the lift yields to the press-flat (§6.12) — pointer
  down mid-lift presses the slip flat over 160ms and the click's
  re-stamp follows. *Scrolled-past:* flat; lifts never persist across
  scroll (a slip left lifted while its section leaves is reset by the
  shared loop when the anchor exits the viewport). *Disabled:*
  a slip whose datum has been withdrawn (§6.2) cannot lift — there is
  nothing honest beneath it; its corner stays pasted and its index
  row shows the withdrawal.
- **Content merge.** What the lift reveals is the page's own history:
  the actual superseded value, in the book's type, in the datum's own
  box. The gesture adds no tooltip, no popover, no detached UI — the
  evidence was printed on the page all along, under the correction,
  which is the theme's whole epistemology in one interaction.
- **Failure fallback.** If 3D transforms are unavailable, the lift
  degrades to a 2D equivalent: the slip translates 4px toward its
  glued edge and fades to 88% opacity, uncovering the old value's
  first line — less theatrical, same information. If the superseded
  value is missing from content, the lift is disabled for that slip
  and the slip is flagged at the gate (§10): a lift over nothing is
  the theme's emptiest possible gesture.
- **Reduced-motion variant.** No rotation. On hover/focus, the slip
  fades to 12% opacity over 120ms (a "hold it to the light" ruling),
  revealing the old value printed beneath; release restores opacity.
  The audit remains fully possible; only the paper physics is
  omitted.
- **Breakpoints (v2).** ≥1200px and 768–1199px: full 3D lift as
  specced. <768px: slips sit below their data (§6.2), so the lift
  becomes a disclosure — tapping the slip's corner zone expands the
  superseded value as a printed line directly beneath the slip
  (height animation 200ms `--ease-press`, or instant under reduced
  motion); hover does nothing on touch, by design.
- **Edge cases & failure modes (v2).** *Slip glued on its left edge*
  (margin-adjacent data, §6.2's right-edge anchoring): the hinge axis
  follows the glued edge — the lift is always away from the glue,
  never a fixed direction. *Very small slips (single-figure
  corrections):* the lift angle reduces to 18° and the revealed old
  value is also carried in the slip's `aria-label`, because a 40px
  wedge cannot legibly frame a number. *Pointer leaves mid-lift then
  re-enters:* the press-back and lift are interruptible from current
  angle (the loop reads the live transform), never restarting from 0
  or 24. *Two slips hovered in quick succession:* each behaves
  independently; there is no global "one lift at a time" rule —
  paper does not coordinate.
- **Accessibility spec (v2).** The superseded value is real DOM text,
  reachable by screen reader in place (it is visually covered, never
  `display:none` or `aria-hidden` — a screen reader meets datum,
  correction and superseded value in order). The lift itself is
  decorative and unannounced. Focus-visible lift parity as above;
  the slip's focus ring is drawn on the slip's rotated frame so the
  visitor sees focus on the object they are auditing. Touch target:
  the whole slip, ≥36px tall.
- **Performance budget & mobile variant.** One element's transform +
  one shadow, GPU-composited, ≤0.2ms/frame; perspective is set on the
  wrapper only while a lift is active or armed in the viewport. Mobile:
  the disclosure variant above — cheaper and more legible than a 3D
  lift at phone scale.
- **Tokens consumed (v2).** `--slip`, `--paste`, `--note`, `--ink`,
  `--ease-peel`, `--ease-press`.

### 6.5 Roll-to-corrected counters

- **What & why.** A corrected figure does not simply appear at its
  new value: as its slip pastes (§6.2), the number itself rolls from
  the superseded value to the corrected one, digit by digit in
  tabular mono, landing exactly as the paste lands. Number and
  correction are one event — the visitor never sees an uncorrected
  figure settle, and never sees a corrected figure arrive without its
  provenance arriving with it. It belongs here because in the trade,
  the erratum and the figure it governs are a single fact; a counter
  that rolls on its own schedule, detached from its slip, is a
  slot machine wearing a slip's clothes.
- **Structure.** The datum (§6.2) carries `data-from` (superseded
  numeric value) and its text content is the corrected value
  (`data-to` is the same number, parsed). The roll renders into the
  datum's own text node via the shared loop: intermediate values are
  computed, formatted with the datum's own locale, grouping and
  unit/currency affixes (affixes are static text around the rolling
  span — only the digits roll). Non-numeric corrections (names,
  dates with month names) do not roll; they use §6.2's paste alone,
  with the old value available under the corner-lift. The roll is a
  JS enhancement layered on a datum whose static text is already the
  corrected value.
- **Motion spec.** Duration **800ms**, linear digit progression eased
  by `--ease-paste` applied to the *value* (fast early travel, soft
  arrival — a hand spinning a counter wheel and letting it settle).
  Start is locked to §6.2's timeline: the roll begins 160ms after the
  slip begins scaling, so the figure is mid-travel as the paper
  lands, and both complete within the same 40ms window. Figures roll
  through their true intermediate values (1,200 → 12,000 passes
  through 4,318, 8,904…), formatted at every frame — no digit-strip
  tricks, no blur. Integer data roll as integers; decimal data roll
  at their printed precision (a corrected 4.2 does not visit 4.1837).
- **Choreography timeline (v2).** t₀ = datum crosses 78% vh (shared
  with §6.2) → t₀+300ms: brush stroke done, slip begins → t₀+460ms:
  roll begins from `data-from` → t₀+900ms: roll at ~78% of travel,
  decelerating → t₀+1260ms: roll lands on the corrected value within
  40ms of the slip's shadow setting (§6.2 t₀+760ms relative to its own
  trigger — the two timelines are authored to coincide; the gate
  spot-checks the synchrony) → the datum's `aria-label` (which has
  carried the corrected value throughout) is untouched: assistive
  tech never hears the travel, only the destination.
- **State matrix (v2).** *Rest (pre-trigger):* the datum shows the
  corrected value — the roll's from-state is applied by JS at arming,
  milliseconds before the trigger, never as a shipped default.
  *Hover/focus:* the roll is unaffected; the corner-lift (§6.4) may
  proceed over a rolling figure without conflict (different layers).
  *Active:* n/a. *Scrolled-past:* corrected value, static; rolls
  never replay on scroll-back — the figure was corrected once, in
  view or not. *Disabled (no JS):* the corrected value, printed.
  The superseded value lives under the slip and in the index, not in
  the datum.
- **Content merge.** The rolling digits are the datum itself changing
  from its published error to its corrected truth, inside its own
  sentence or cell. The counter is not a widget beside the content;
  it is the content, caught in the act of being corrected.
- **Failure fallback.** If the loop stalls mid-roll, the 900ms
  watchdog sets the datum's text to the corrected value outright —
  a figure frozen between values is the one state this theme forbids
  absolutely (it is a value nobody ever published). If `data-from`
  is absent or non-numeric, no roll is armed and §6.2 proceeds alone.
- **Reduced-motion variant.** No roll. The corrected value stands
  from first paint; the slip pastes statically (§6.2's variant). The
  provenance is complete; the travel is omitted.
- **Breakpoints (v2).** Identical behaviour at all sizes — digits are
  digits. On <768px the roll duration shortens to 650ms (smaller
  figures, held closer, read sooner); formatting and synchrony with
  the slip are unchanged.
- **Edge cases & failure modes (v2).** *Huge ranges* (1,200 →
  1,200,000): the roll stays 800ms; intermediate formatting must
  never overflow the datum's box — the box is sized to the wider of
  from/to at build time, so the layout never shifts mid-roll.
  *Negative or sign-changing corrections* (−4 → 6): the roll passes
  through zero honestly; the minus sign is part of the rolling span.
  *Percentages and decimals with trailing zeros:* printed precision
  is law — 12.0% rolls as 12.0%, never 12%. *A datum corrected while
  already in view* (live data update): no roll; the slip re-pastes
  (§6.2's withdrawal-and-replace path) and the figure crossfades
  200ms — a roll is for first meetings.
- **Accessibility spec (v2).** The datum carries
  `aria-label="£48 (corrected from £42)"` from the start, and the
  rolling text is `aria-hidden` during travel, so screen readers
  announce the destination once, never a stream of intermediates.
  Tabular figures guarantee the roll never moves surrounding text —
  a screen-magnifier user tracking the sentence is not thrown by
  shifting line breaks.
- **Performance budget & mobile variant.** Text writes on one node,
  throttled to animation frames, ≤0.3ms/frame; at most 3 rolls
  concurrent (the §4 density cap). Mobile: the 650ms duration above;
  no other change — the roll is already the cheapest motion in the
  theme.
- **Tokens consumed (v2).** `--ink`, `--ease-paste`, `--lerp`.

### 6.6 Paste-brush stroke

- **What & why.** Before a slip can paste, the paste must be laid.
  An SVG brush stroke — a soft-edged band of `--paste` tone, slightly
  wider than the slip it will hold — draws itself across the slip's
  footprint in the moment before the slip arrives. It belongs here
  because it is the visible cause of everything else in the theme:
  the sheen, the shadow, the lift's resistance all claim there is
  glue under this paper, and the brush stroke is where the theme
  proves it, once per slip, in the open. Without it the slips merely
  appear; with it they are *pasted*, by a hand the visitor almost
  sees.
- **Structure.** An inline SVG per corrected anchor, sized to the
  slip's footprint +8px width, holding one path: a filled,
  slightly irregular band shape (authored with 2px of edge wobble —
  a brush edge, not a rectangle) with a `clipPath` rect whose width
  animates. The band's fill is `--paste` at 55% opacity with a
  feTurbulence-free, hand-authored second inner path at 30% for the
  wet centre. The SVG sits beneath the slip in the anchor's stacking
  order, above the page. After the slip lands, the stroke remains
  visible only as a 2–3px halo at the slip's glued edge — the squeeze-
  out of paste that real pasting leaves.
- **Motion spec.** Trigger: §6.2's paste-over, 300ms before the slip
  moves. The clip wipes left→right (or along the glued edge for
  side-glued slips) over **300ms `--ease-brush`** — constant-speed,
  like a pulled brush. As the slip lands (§6.2), the band's exposed
  body is covered; its halo contracts from full band to the 2–3px
  squeeze-out line over the slip's final 120ms, so the finished state
  reads as a slip with paste at its edges, not a slip on a sticker of
  glue.
- **Choreography timeline (v2).** t₀ = §6.2 trigger → t₀+0ms: clip
  wipe begins → t₀+300ms: band complete, fully exposed for one frame
  of honesty → t₀+300–760ms: the slip scales in over it (§6.2) →
  t₀+640–760ms: exposed band contracts to the squeeze-out halo →
  t₀+760ms: finished — slip, halo, shadow, in that order from the
  page up.
- **State matrix (v2).** *Rest (pre-trigger):* no band — paste is
  laid at the moment of pasting, never pre-drawn (a page pre-striped
  with glue bands would be a page waiting for corrections, which is
  the wrong tense). *Hover:* the halo is the hinge line that brightens
  during the corner-lift (§6.4) — its one later job. *Focus:* same
  brightening via the lift's focus twin. *Active:* n/a. *Scrolled-past:*
  the halo persists, static, for the life of the page. *Disabled (no
  JS):* the halo is present (it is part of the finished slip's print),
  the full band never shows — without the pasting event there is no
  stroke to perform.
- **Content merge.** The stroke occupies exactly the footprint of the
  correction it enables and ends as that correction's edge detail.
  It is the physical link between page and slip — the theme's claim
  that these two layers were joined by an act, drawn at the join.
- **Failure fallback.** If SVG is unavailable, the stroke is skipped
  and the slip pastes directly (§6.2 proceeds 300ms earlier); the
  halo is then faked by the slip's own `--paste` border-edge on the
  glued side. If the stroke's animation stalls, the watchdog clears
  the band at trigger+900ms so no naked glue band is ever left
  exposed without its slip.
- **Reduced-motion variant.** No wipe. The halo is simply present
  with the statically-pasted slip — the stroke's information (this
  was pasted, here) survives as the edge line; the performance is
  omitted.
- **Breakpoints (v2).** All sizes: identical, scaled to the slip's
  footprint. On <768px, where slips sit below their data, the stroke
  draws along the slip's top edge only (the visible glue line of a
  slip pasted by its head) and the band phase is shortened to 200ms.
- **Edge cases & failure modes (v2).** *Slip re-pasted after a data
  update* (§6.2's replace path): the stroke redraws — new paste for a
  new slip; the old halo is removed with the old slip so halos never
  accumulate into a frame. *Very small slips* (<60px wide): the band
  is a single 180ms dab (a brush dot), because a 60px wipe reads as a
  glitch, not a stroke. *Table cells* (§6.15): the stroke draws in
  the cell's correction gutter, vertically, top→bottom, 240ms.
- **Accessibility spec (v2).** Purely decorative and `aria-hidden`;
  it carries no information the slip's own label does not state. Its
  contrast is deliberately sub-textual (`--paste` at 55% on `--page`)
  — it must never be mistaken for content by low-vision visitors,
  and its halo state sits beneath the slip, outside the text path.
- **Performance budget & mobile variant.** One clip-path animation
  per correction, ≤0.15ms/frame; the path is static geometry. Mobile:
  the shortened edge-stroke above. The stroke is the second element
  cut under performance pressure (§14) — the slip still pastes
  honestly without its brush.
- **Tokens consumed (v2).** `--paste`, `--ease-brush`.

### 6.7 Glue-sheen rotation

- **What & why.** The theme's single ambient loop, and its quietest:
  a faint specular highlight — the light catching wet-look glue at a
  slip's edge — slowly cycles across the page's slips, one at a time,
  four seconds each, in reading order. It belongs here because pasted
  paper is not quite matte: the glue line at a slip's edge holds a
  slight gloss the page lacks, and a page whose corrections catch the
  light in turn feels *handled*, recently worked on, alive in the
  way a desk is alive. It also does real work: it walks the visitor's
  eye through the page's corrections in order, without moving a
  single element.
- **Structure.** Each slip carries a `::after` sheen layer: a linear
  gradient (transparent → white 10% → transparent; amber 12% in
  lamplight, §2) clipped to the slip's glued-edge 6px band, offset so
  it rests off-edge. The shared loop grants one slip at a time the
  `.is-sheened` class; the sheen's `background-position` sweeps
  across the band. No slip carries its own timer — the rotation is a
  single page-level scheduler walking the DOM's slip list in reading
  order, skipping slips outside the viewport ±1 screen.
- **Motion spec.** Per slip: the highlight sweeps the glued edge over
  **1200ms** (ease-in-out sine), then rests; the scheduler dwells
  **4000ms per slip** total (sweep + 2800ms of stillness) before
  advancing. The loop is unhurried by design — at any moment at most
  one slip on the page is lit, at 10–12% opacity, on a 6px band. The
  sheen never runs during a paste-over, lift or roll on the same
  slip; the scheduler skips an occupied slip and returns next cycle.
- **Choreography timeline (v2).** Continuous: slip *k* sheens (sweep
  1200ms) → 2800ms rest → slip *k+1* (next in reading order within
  the active viewport band) sheens → … → after the last slip in the
  band, the cycle restarts from the first; slips entering the band
  join the rotation at their reading-order position, never by
  jumping the queue.
- **State matrix (v2).** *Rest:* sheen parked off-edge, invisible.
  *Sheening:* the 1200ms sweep. *Hover:* a hovered slip's sheen
  pauses wherever it is (the corner-lift's hinge brightening, §6.4,
  is a separate, stronger effect and takes the edge over). *Focus:*
  same pause. *Active/scrolled-past:* slips outside the active band
  are never sheened. *Disabled (no JS):* no sheen — the slips are
  matte paper, which is their honest default.
- **Content merge.** The sheen lives on the slips' own glue lines —
  it is a property of the corrections' material, not a light effect
  sprayed over the page. It touches no book text, no image, nothing
  but the edges of the pasted paper.
- **Failure fallback.** The sheen is enhancement-only: its absence is
  undetectable as a defect. If the scheduler fails, nothing is left
  mid-state (the class is removed on any error path), and no watchdog
  is needed because no content state depends on it.
- **Reduced-motion variant.** **None — the sheen does not run.** It
  is the theme's only purely ambient motion, and ambient motion is
  precisely what reduced-motion exists to still. This is the
  strictest ruling in the theme and it is not negotiable at build
  time.
- **Breakpoints (v2).** ≥1200px and 768–1199px: full rotation.
  <768px: the rotation runs only over slips currently on screen
  (band = the viewport itself), dwell shortens to 3000ms; the sheen
  band narrows to 4px to match the smaller slips.
- **Edge cases & failure modes (v2).** *A page with one slip:* the
  sheen visits it every 4000ms — a single correction breathing; if
  the content team finds that melancholy, the cure is more honesty
  elsewhere, not a faster loop. *Many slips in one band (>8):* the
  scheduler still walks in order; a full cycle may take 30s+, which
  is correct — the sheen is weather, not a feature tour.
  *Photosensitivity:* a 10% opacity edge highlight sweeping over
  1200ms is orders below any flash threshold; its slowness is a
  safety property, and "enlivening" it is a gate failure.
  *Battery:* the scheduler pauses entirely when the tab is hidden
  and when the page has been idle (no scroll/interaction) for 60s,
  resuming on activity.
- **Accessibility spec (v2).** Decorative, `aria-hidden` via the
  pseudo-element's nature; it announces nothing, signifies nothing,
  and is fully absent under reduced motion. It never overlays text —
  the band is the slip's edge, outside its text box.
- **Performance budget & mobile variant.** One gradient position
  animation on one small element at a time; ≤0.1ms/frame — the
  cheapest loop in the theme, and still the **first element cut**
  under any performance pressure (§14): ambience is always the first
  sacrifice. Mobile: narrowed band and shortened dwell as above.
- **Tokens consumed (v2).** `--paste`, `--slip`, `--lerp`.

### 6.8 Index accumulation

- **What & why.** The closing errata index is not written in advance
  and revealed; it *accumulates*. Each time the visitor passes a
  correction, the index at the foot of the page gains that
  correction's numbered row — by the time the visitor arrives, the
  index is the record of the corrections they personally witnessed,
  complete and in order. It belongs here because it fuses the theme's
  two apparatuses — progress and provenance — into one object: the
  index is both the page's table of corrections and the receipt for
  the visitor's reading. A progress bar tells you how much page is
  left; this tells you how much *honesty* you have passed.
- **Structure.** The index (§6.17 is its full page-family treatment;
  this element is its accumulation behaviour) is an ordered list in
  the footer leaf: each row = erratum number (mono, `--red-deep`),
  location ("p.2 · Prices, line 4"), the formula (`for "£42" read
  "£48"`), the stamp date, and a 28px slip miniature (a tiny rotated
  slip-paper chip carrying the number). Rows exist in the DOM from
  the start in their final state — accumulation is a JS-armed
  pre-state (row held at opacity 0, miniature parked 12px left)
  applied only to rows whose corrections the visitor has not yet
  passed.
- **Motion spec.** Trigger: the source slip's paste completing
  (§6.2), wherever the index physically sits. The row fades in over
  **300ms `--ease-paste`** while its miniature slides in from the left
  and settles at the row's lawful rotation (the same §4 formula —
  the miniature is the slip, at index scale), 380ms `--ease-flutter`
  without overshoot beyond 1°. Simultaneously the header counter
  (§6.14) steps to this erratum's number. Rows accumulate strictly in
  number order; a visitor who jump-scrolls to the foot triggers all
  intervening pastes' rows in one ordered cascade, 60ms apart — the
  index catches up like a clerk who was handed a stack of slips at
  once.
- **Choreography timeline (v2).** t₀ = source paste completes →
  t₀+0ms: row fade begins → t₀+80ms: miniature begins its slide →
  t₀+380ms: miniature settled at angle → t₀+300ms: row at full
  opacity → the header counter steps at t₀+120ms (§6.3's beat) so the
  three apparatuses (pin, counter, index) settle within one 400ms
  window and never visibly disagree.
- **State matrix (v2).** *Rest (pre-trigger, JS-armed):* row held
  invisible — the one pre-state in the theme that hides content, and
  it is lawful only because the same row's content is simultaneously
  present at its slip, in view, at the moment of arming; the index is
  a duplicate record, never the sole carrier. The watchdog (below)
  bounds the state absolutely. *Hover:* the row's miniature lifts
  (§6.4 at miniature scale: 14° for 240ms) and the row's location
  underlines — hovering a row highlights its source slip if it is on
  screen (a 600ms sheen pulse, §6.7's material, on demand).
  *Focus:* rows are links to their data (focus scrolls the datum into
  view and fires its corner-lift once); focus ring on the row.
  *Active:* the jump executes. *Scrolled-past:* rows for passed
  corrections are simply present — accumulation is permanent.
  *Disabled (no JS):* the complete index, printed, every row — the
  designed state.
- **Content merge.** The index's rows are the corrections themselves,
  restated in the trade's format; accumulation makes the footer a
  log of the page's own events. Nothing in the index exists that is
  not also a slip on the page (the 1:1 law, §1) — the accumulation is
  the law being visibly kept, one row at a time.
- **Failure fallback.** A global index watchdog: any row still
  un-accumulated 1500ms after its source slip's paste (or at the
  moment the index itself enters the viewport, whichever is sooner)
  is set to final state instantly. The index the visitor reaches is
  therefore always complete and correct, even if every intermediate
  trigger failed — the record outranks the performance.
- **Reduced-motion variant.** Rows are present from the start (no
  accumulation); the miniature sits at its angle; the counter still
  steps (it is information, rendered instantly). The index reads as
  the printed back matter it imitates.
- **Breakpoints (v2).** ≥1200px: rows in two columns (numbers run
  down the left column, then the right — book index order, not
  across). 768–1199px: one column, full measure. <768px: one column;
  the miniature shrinks to 22px and the formula wraps to two lines
  rather than truncating — a truncated formula is a withheld
  correction.
- **Edge cases & failure modes (v2).** *A page with 30+ corrections:*
  the density law (§4) should have prevented it, but if content
  demands it, the index paginates by section ("Errata for Prices",
  "Errata for Specifications") with rows accumulating within their
  groups; the numbering stays global and unbroken. *Visitor arrives
  via an anchor at the page foot:* all rows are final (the index
  watchdog's viewport clause) — nobody meets a half-written index.
  *A correction withdrawn (§6.2):* its row is struck through in
  `--note` and annotated "withdrawn" with the date — the index never
  deletes a row, because an index that deletes is a memory hole with
  good typography.
- **Accessibility spec (v2).** The index is a real `<ol>` with real
  links; each row's link text is the full formula ("Erratum No. 7 —
  Prices: for £42 read £48"), so the index is fully usable by ear.
  Accumulation is never announced (it duplicates in-view events).
  Row contrast: number in `--red-deep` on `--page` (≥7:1 class),
  formula in `--ink` 14.89:1. Focus order follows number order.
- **Performance budget & mobile variant.** One fade + one small
  transform per correction; negligible. The cascade cap: at most 8
  rows animating at once, further rows snap to final — catching up
  is clerical, not theatrical. Mobile: as breakpoints above.
- **Tokens consumed (v2).** `--page`, `--ink`, `--note`, `--red-deep`,
  `--slip`, `--paste`, `--ease-paste`, `--ease-flutter`.

### 6.9 Full-page slip transition

- **What & why.** Leaving the page is also an act of correction.
  When the visitor follows an internal link, a full-page slip —
  leaf-sized, slip paper, rotated a lawful 0.8°, carrying the
  destination's name and the formula "continued overleaf" in mono —
  pastes over the viewport; the route swaps beneath it; then the
  slip peels away from its free corner, revealing the new page
  already printed and corrected. It belongs here because the theme's
  material is paper pasted on paper, and a navigation that fades or
  slides would be a foreign substance between two corrected editions.
  The transition also performs the theme's promise: you are never
  shown a half-loaded page, only a covered one and then a finished
  one.
- **Structure.** A fixed `.page-slip` element (100vw × 100vh, slip
  paper with the theme's paste-shadow edge and a mono footer line:
  destination title + "Errata Slip — continued overleaf"), parked
  above the viewport translated −104%. It carries one brush-stroke
  band (§6.6's material) along its leading edge. The element exists
  in the DOM from load, inert and `aria-hidden`; it enhances internal
  `<a>` clicks only — it never intercepts modified clicks, new-tab
  opens, external links or form submissions.
- **Motion spec.** Trigger: activation of an interceptable internal
  link. Cover: the slip translates down into place over **380ms
  `--ease-paste`**, rotation settling 2.2° → 0.8°, its brush band
  drawing in its first 200ms. At full coverage (380ms) the route
  swaps and scroll resets beneath the slip. Peel: after the new page
  is ready (or 500ms, whichever is later, capped at 2.5s), the slip
  lifts from its free (bottom-right) corner — a 3D peel, corner
  rising to 65° while the slip translates up-right — over **520ms
  `--ease-peel`**, exiting the viewport and revealing the new page
  printed beneath. Total ritual: ~0.9–1.4s.
- **Choreography timeline (v2).** t₀ = link activation → t₀+0ms:
  slip begins its descent, outgoing page `inert` → t₀+200ms: brush
  band complete → t₀+380ms: full coverage; route swaps; focus is
  parked on the slip's (aria-hidden, tabindex −1) shell → new page
  ready or t₀+880ms: peel begins from the free corner → t₀+1400ms:
  slip clear; focus moves to the new page's `<h1>`; a polite
  announcement "Continued: [page name]" fires → t₀+1900ms: watchdog
  confirms the slip is parked and inert.
- **State matrix (v2).** *Rest:* parked, invisible, inert. *Covering:*
  pointer locked out (the slip is the page's surface). *Covered:*
  waiting state — if the destination stalls past 2.5s, the slip's
  footer line gains a second mono line, "the next leaf is being
  pasted in", and at 4s the transition aborts: the slip peels back
  and the browser's native navigation proceeds (the theme never traps
  a visitor under paper). *Peeling:* as specced. *Scrolled-past:*
  n/a. *Disabled (no JS):* ordinary navigation; the slip never
  renders.
- **Content merge.** The slip that covers the viewport is the theme's
  own object at page scale, and its printed line names the actual
  destination — it is a title slip for the leaf you are turning to,
  not a loading spinner in fancy dress. The new page arrives already
  corrected (its slips pre-pasted in final state after a transition —
  a turned-to page does not re-perform its corrections; §6.2's
  paste-overs fire only on first manufacture, not on arrival).
- **Failure fallback.** Any error in the transition path (router
  failure, peel stall) tears the slip down instantly and shows the
  destination plainly; the 1900ms watchdog enforces this. Browser
  back/forward bypass the slip entirely — history gestures belong to
  the browser, and a corrected book does not argue with its reader
  about how they turn back.
- **Reduced-motion variant.** No cover, no peel. Navigation is
  instant, marked by a 120ms slip-paper flash on the running head
  (§6.14) — the change of leaf is acknowledged in the theme's paper
  without the paper moving.
- **Breakpoints (v2).** ≥1200px: full spec. 768–1199px: cover 340ms,
  peel 460ms. <768px: the peel becomes a lift — the slip translates
  up and fades over its last 120ms (a full 3D corner peel on a phone
  reads as a card trick, not a page turn); cover stays 320ms. The
  footer line's text size never drops below 11px.
- **Edge cases & failure modes (v2).** *Same-page anchors:* no slip —
  anchors scroll within the leaf. *Downloads and mailto:* untouched.
  *A link inside a slip (an index row):* the transition fires
  normally; the clicked slip is not itself animated (it stays in the
  covered page). *Prefetched destination:* the full ritual still
  runs — the paste is the point, not the wait — but the covered wait
  collapses to the 500ms floor. *Slow destination:* the stall lines
  and abort path in the state matrix.
- **Accessibility spec (v2).** The outgoing page is `inert` from t₀;
  at peel completion focus lands on the destination's `<h1>`
  (tabindex −1) with the polite announcement above — standard SPA
  focus law executed in the theme's grammar. The slip itself is
  `aria-hidden` throughout (its destination line duplicates the
  announcement). Reduced-motion and screen-reader-driven navigation
  skip the ritual per the variant.
- **Performance budget & mobile variant.** One fixed element, one
  transform sequence; the peel's 3D is the theme's most expensive
  single effect (≤1.2ms/frame for 520ms) and is spent once per
  navigation. Mobile: the lift variant above, ≤0.6ms/frame.
- **Tokens consumed (v2).** `--slip`, `--paste`, `--ink`, `--red`,
  `--ease-paste`, `--ease-peel`, `--ease-brush`.

### 6.10 Slip-edge text reveal

- **What & why.** A slip is read in the order it was pasted. When a
  slip lands (§6.2), its own text does not appear all at once: a clip
  mask wipes across the slip from its glued edge, revealing the
  number first, then the location, then the formula, in the 380ms
  after the paper settles — the eye is led down the slip exactly as
  the corrector's eye travelled when writing it. It belongs here
  because the slip's internal order is its rhetoric (number →
  location → formula → date, §3's law), and a reveal that honoured
  any other order would argue with the text it reveals.
- **Structure.** The slip's text block carries a CSS mask
  (`mask-image: linear-gradient`) whose gradient stop is animated via
  a registered `@property` custom property, or — where `@property`
  is unsupported — a `clip-path: inset()` wipe on an inner wrapper.
  The mask direction follows the glued edge: top-glued slips reveal
  top→bottom (the usual case: number line first), left-glued slips
  reveal left→right by line. The text itself is fully in the DOM, in
  reading order, from the start; the mask is a JS-armed pre-state.
- **Motion spec.** Trigger: the parent slip's paste landing (§6.2's
  t₀+640ms — as the shadow sets). The wipe runs **380ms
  `--ease-paste`** across the slip's text block. Lines are revealed
  continuously, not word-staggered: the mask is a soft 6px gradient
  edge, so a line is uncovered as a band of print, the way ink takes
  on paper. For the hero's three slips (§6.1), the reveal chains:
  each slip's text wipe begins as its own landing completes, so the
  title page's corrections become readable in number order.
- **Choreography timeline (v2).** t₀ = slip lands → t₀+0ms: mask at
  0%, text covered by the slip's own paper (the slip reads blank for
  one beat — pasted, not yet written on, the correct fiction) →
  t₀+120ms: number line uncovered → t₀+240ms: location + formula
  uncovered → t₀+380ms: stamp date uncovered; mask removed entirely
  (the finished slip carries no mask — the reveal deletes itself).
- **State matrix (v2).** *Rest (pre-trigger):* text covered by mask —
  a JS-armed state bounded by the same 900ms watchdog; the no-JS
  slip is fully lettered. *Revealing:* as specced. *Revealed:*
  terminal; the mask never returns, including on scroll-back and on
  re-paste (a replacement slip's text reveals again — new slip, new
  writing). *Hover/focus:* no interaction with the mask; the
  corner-lift (§6.4) operates on the lettered slip. *Disabled:*
  lettered from the start.
- **Content merge.** The reveal is the slip's own text arriving in
  its own rhetorical order — the animation is the act of writing the
  correction, performed on the correction itself. It decorates
  nothing outside the slip's border.
- **Failure fallback.** The watchdog clears any mask at trigger+900ms.
  If neither mask nor clip-path animation is supported, the text is
  simply present (the enhancement detects support before arming —
  an unsupported browser never sees a blank slip). A blank slip that
  persists is a blocking gate failure (§10): it is the theme's
  version of invisible content.
- **Reduced-motion variant.** No wipe; the slip arrives lettered.
  The number→formula order survives as pure typography, which is
  where it primarily lives anyway.
- **Breakpoints (v2).** Identical at all sizes; on <768px the wipe
  shortens to 300ms (shorter slips, held closer). Side-glued slips
  reveal left→right at every size.
- **Edge cases & failure modes (v2).** *Long formulas* (a corrected
  sentence, slip at max-width with 4 lines): the wipe stays 380ms —
  the band moves faster across more text; lines never wait for a
  per-line stagger, because a slip is one utterance. *The visitor
  lifts the corner mid-reveal:* the lift proceeds; the mask is on
  the text layer, the lift on the face layer — they compose without
  conflict, and the reveal completes beneath the raised corner.
  *Print:* masks do not print; slips print lettered.
- **Accessibility spec (v2).** The mask is visual only; the text is
  in the accessibility tree in full from the start (a screen reader
  is never asked to wait for ink). No announcement is made — the
  slip's arrival is already carried by its position after the datum
  (§6.2's a11y). Contrast is the slip's own (§6.2).
- **Performance budget & mobile variant.** One mask/clip animation
  on a small element per correction, ≤0.15ms/frame. Mobile: the
  300ms duration above. This element is cut third under performance
  pressure (§14) — lettered-on-arrival is an honourable slip.
- **Tokens consumed (v2).** `--slip`, `--ink`, `--ease-paste`.

### 6.11 Slip-lag parallax

- **What & why.** Pasted paper sits *on* the page, not in it — and
  the scroll proves it. As the visitor scrolls, every pasted slip
  travels at 0.94× the rate of the book text beneath it: a 6% lag,
  scrubbed through the shared loop, so slips drift a few pixels
  against their data as the page moves and settle back into register
  when the scroll stops. Their paste shadows widen as the lag grows
  and narrow as it closes, selling the physics: the slip is sliding
  minutely on its paste, the way a real tipped-in slip shifts under a
  thumb. It belongs here because it is the theme's depth cue — the
  one place the two layers (book and correction) are allowed to be
  seen as two layers.
- **Structure.** Slips live in the anchor's flow (§6.2); the loop
  applies a `translateY` delta to each armed slip equal to
  `(scrollVelocity smoothed) × lagFactor`, clamped to ±7px, where the
  slip's target offset is `−(pageScrollDelta since settle) × 0.06`
  integrated by the lerp — in practice: the slip's rendered position
  chases its anchored position with the shared lerp (0.12) applied to
  the slip layer only, while book text scrolls natively. The paste
  shadow's offset is a CSS variable on the slip, driven by the same
  delta (3px at rest → 5px at full lag).
- **Motion spec.** Continuous, scroll-driven, no trigger. Lag factor
  **0.06** (slips move at 94% of scroll); maximum displacement ±7px;
  settle: when scroll velocity reaches 0, the lerp returns every
  slip to exact register within ~300ms. The drift is symmetric —
  scrolling up lags slips the other way — because paste does not know
  which way the page is moving. A slip mid-paste-over, mid-lift or
  mid-reveal is exempt: its own animation owns its transform until it
  settles, then the lag adopts it.
- **Choreography timeline (v2).** Spatial, per scroll gesture: scroll
  begins → within one frame the loop begins displacing slips against
  travel → steady scroll: displacement holds at the clamp
  proportional to velocity (≤7px) → scroll ends → 300ms settle: slips
  ease back to 0 offset, shadows narrowing 5px→3px in step → rest:
  register exact, auditable — a screenshot at rest must show every
  slip precisely on its datum.
- **State matrix (v2).** *Rest:* offset 0, register exact. *Scrolling:*
  offset per velocity, shadow widened. *Settling:* the 300ms return.
  *Hover/focus:* a hovered slip's lag freezes at its current offset
  (the corner-lift, §6.4, takes over its transform) and resumes
  settling on release. *Scrolled-past:* slips outside the viewport
  are not driven (the loop tracks ±1 viewport only). *Disabled (no
  JS):* slips are in register, always — the static truth of the page.
- **Content merge.** The lag acts on the correction layer only, and
  its entire meaning is the relationship between that layer and the
  book: the slips are *on* the content, and the scroll lets the
  visitor feel the "on". At rest — the state in which anything is
  read — the merge is exact.
- **Failure fallback.** If the loop stalls, offsets freeze wherever
  they are for at most one watchdog cycle (900ms), after which a
  settle sweep forces every slip to 0 offset — a page whose slips sit
  permanently 7px off their data has failed the theme's first law in
  spirit, and the fallback exists to make that state impossible to
  keep. Transform support is universal enough that no other fallback
  is specified; without JS there is no lag at all.
- **Reduced-motion variant.** **No lag.** Slips scroll in perfect
  register with the book at all times. Parallax of any kind is the
  canonical reduced-motion exclusion, and this theme — whose whole
  ethic is that the correction must sit exactly on its datum — gives
  it up without argument.
- **Breakpoints (v2).** ≥1200px: full 0.06 factor, ±7px clamp.
  768–1199px: factor 0.05, clamp ±5px. <768px: slips sit below their
  data in flow (§6.2), where a vertical lag would collide with the
  following text — the lag is **cut entirely** on phones, and the
  layer separation is carried by the paste shadow alone. This is the
  theme's clearest mobile simplification: the physics yields to the
  reading.
- **Edge cases & failure modes (v2).** *Fast fling scroll:* the clamp
  holds at 7px; slips never detach visually from their data (7px is
  chosen as the largest displacement at which a slip still unmistakably
  belongs to its value). *Anchor reflow mid-scroll* (an image loads
  and pushes a datum down): the slip follows its anchor's layout
  position; the lag delta is computed against the new position from
  the next frame — no jump, because the lerp absorbs the step.
  *A slip at the viewport's edge:* displacement may carry it ±7px
  across the fold; it is never clipped by an ancestor (anchors do not
  set `overflow: hidden` — a build rule, checked at the gate).
- **Accessibility spec (v2).** The lag is pure visual physics; it
  moves no focus, changes no order, and is absent under reduced
  motion. Because slips return to exact register at rest, no reading
  state ever presents a slip misaligned with its datum to a magnifier
  user tracking a line.
- **Performance budget & mobile variant.** The loop writes one
  transform per in-band slip per frame: ≤0.5ms/frame for a full
  viewport of slips (the density cap keeps this ≤3). Mobile: cut, as
  above — its budget is returned to the scroll itself.
- **Tokens consumed (v2).** `--paste`, `--lerp`, `--ease-paste`.

### 6.12 Press-flat re-stamp

- **What & why.** The click. Pressing a slip — click, tap, or Enter
  on a focused slip — presses it flat against the page with the flat
  of an invisible hand, and as it settles, its stamp is re-struck:
  the slip's date stamp fades and re-imprints with a fresh strike,
  acknowledging the touch. It belongs here because every other gesture
  in the theme is the visitor *reading* the corrections; this is the
  one where they handle the paper — and handling it should feel like
  handling it: the corner that lifts on hover (§6.4) presses down
  under a click, the shadow squeezes out, and the stamp — the
  corrector's mark of "seen, verified" — is struck again, now with
  the visitor as witness. On slips that carry an action (a corrected
  price linking to its product), the press *is* the click feedback,
  and navigation follows the stamp.
- **Structure.** The slip face (§6.4's layer) plus a `.stamp` element
  in its footer line: the date in mono 11px uppercase, `--red`,
  struck inside a 1px `--red` rounded-rect impression border at −2°
  (the stamp has its own small crookedness, independent of the slip's
  angle — hands stamp at their own angle). The re-strike animates the
  stamp's opacity/scale; the press animates the face's rotation (any
  lift collapses) and the paste shadow's squeeze (offset 3px→1px,
  blur 2px→0, then rebound).
- **Motion spec.** Trigger: click/tap/Enter/Space on the slip.
  Press: **160ms `--ease-press`** — face rotation → 0 (from lifted or
  rest), shadow squeezing to 1px. Hold at flat for 60ms. Re-stamp at
  release (or at 220ms for keyboard): the stamp scales 1.25→1 with
  opacity 0→1 over **140ms `--ease-press`**, its impression border
  darkening from 40% to full `--red` across the same beat — a stamp
  hitting paper. The slip then rebounds: shadow relaxes to its rest
  3px over 240ms. If the slip carries a link, navigation (or the
  §6.9 transition) begins at the re-stamp's completion, 360ms after
  the press — the visitor sees the stamp strike before the page
  answers.
- **Choreography timeline (v2).** t₀ = press → t₀+0–160ms: face
  flattens, shadow squeezes → t₀+160–220ms: held flat (the hand is
  on it) → t₀+220ms: stamp re-strikes (140ms) → t₀+360ms: stamp
  settled at full impression; link action fires if any → t₀+360–600ms:
  shadow rebounds to rest; the slip is exactly as it was, except its
  stamp is fresh — and, if the build tracks it, the index row's
  miniature pulses once in sympathy (§6.8's material) when both are
  on screen.
- **State matrix (v2).** *Rest:* stamp at rest impression (85%
  opacity — a stamp struck some time ago). *Hover:* corner-lift
  (§6.4) — the press's opposite, and the two never fight: pointer
  down converts lift to press from the current angle. *Focus:*
  corner-lift (focus twin) plus the focus ring; Enter/Space fires
  the press. *Active:* the press sequence above. *Scrolled-past:*
  rest. *Disabled:* a slip with no action and no datum (withdrawn,
  §6.2) does not press — it is pasted down for good; its cursor and
  behaviour say so (no pointer affordance, no ring).
- **Content merge.** The press acts on the correction itself and its
  stamp is the correction's own date — the feedback is the content's
  material responding, not a button ripple imported from another
  design language. Where the slip carries the page's real action
  (following a corrected value to its source), the press is that
  action's entire ceremony.
- **Failure fallback.** The press is feedback, never a gate: if the
  animation is unavailable, the click still performs its action
  instantly. A slip whose action fails (dead link) keeps its stamp
  un-struck and the error surfaces in the page's own voice (§12) —
  the stamp never certifies a journey that did not happen.
- **Reduced-motion variant.** No press, no re-strike animation. On
  activation, the stamp's impression border darkens instantly to full
  `--red` for 600ms — acknowledgement by ink, not by motion.
- **Breakpoints (v2).** Identical at all sizes. On <768px the press
  replaces the corner-lift disclosure (§6.4's mobile ruling) as the
  slip's primary tap behaviour only where the slip carries an action;
  pure-annotation slips on mobile disclose on tap and press on
  long-press — the two gestures are kept distinct so a reader
  auditing a value never triggers a navigation by accident.
- **Edge cases & failure modes (v2).** *Rapid repeat presses:* the
  sequence restarts from current state; the stamp re-strikes each
  time (a stamp struck twice is darker — the impression opacity caps
  at 100%, it does not compound into a blob). *Press during the
  paste-over:* the paste completes first (its 460ms owns the
  transform); the press queues and fires on the settled slip — paper
  is not pressed while it is still falling. *Press on the hero's
  slips:* identical behaviour; the hero's corrections are working
  slips, not stage props.
- **Accessibility spec (v2).** Actionable slips are real `<button>`s
  or links with labels that state the action and the correction
  ("Corrected price £48 — see the edition it belongs to"), never
  "click here". Non-actionable slips are not focusable and present
  as the `<aside>` of §6.2. The re-stamp is decorative; state changes
  it accompanies (navigation, confirmation) are announced by their
  own mechanisms. Press target: the full slip, ≥36px tall, ≥44px on
  touch via the below-datum mobile layout.
- **Performance budget & mobile variant.** One small transform +
  shadow + opacity sequence, ≤0.2ms/frame, once per press. Mobile:
  as the breakpoints above; no cost change.
- **Tokens consumed (v2).** `--slip`, `--paste`, `--red`, `--ink`,
  `--ease-press`.

### 6.13 The title page (page family: hero)

- **What & why.** Every corrected edition opens with its title page,
  and so does this theme: a calm, centred Garamond composition —
  the book's title, its author/publisher line, its edition statement
  ("Second edition, corrected") — with the correction flutter (§6.1)
  performing over it and three slips as its only ornament. It belongs
  here because the hero's job in this theme is not to sell but to
  *establish the document*: what this is, whose it is, and the fact —
  performed, not claimed — that it has already corrected itself once
  before asking for trust.
- **Structure.** A `<header>` on the leaf (§4), centred measure
  34ch: publisher's line (mono 11px uppercase, `--note`), the title
  (Garamond 54px) with §6.1's stage layer, the edition statement
  (Garamond italic 19px) carrying the edition's real data — edition
  number, correction count to date, last-corrected date — and a
  single Garamond link downward ("Begin at the first page") styled
  as a contents entry with a dotted leader to its folio (§6.14's
  material). No image. A corrected book's title page has no picture;
  the slips are the illustration.
- **Motion spec.** The flutter (§6.1) is the hero's only entrance.
  The composition itself never animates in — a title page is
  *opened to*, not loaded. The downward link's leader dots draw on
  hover (background-position sweep, 200ms `--ease-paste`). The
  edition statement's correction count is a datum like any other: if
  it was itself corrected, it wears a slip and rolls (§6.5) — the
  hero obeys the theme's laws on its own furniture first.
- **Choreography timeline (v2).** Page load → the title page stands
  complete (wrong title staged per §6.1) → §6.1's timeline runs
  (500ms beat, three slips by t₀+1620ms) → the header counter settles
  at "Erratum No. 3" → stillness. Nothing else moves until the
  visitor scrolls, at which point the working margin's pin (§6.3)
  takes up its residence.
- **State matrix (v2).** *Rest:* the composed title page. *Hover:*
  slips lift (§6.4); the contents link draws its leader. *Focus:*
  the link's ring (2px `--cloth` outline — on the leaf, cloth is the
  furniture colour and red stays inside corrections). *Active:* the
  link scrolls to the first section (no page slip; it is an anchor).
  *Scrolled-past:* the title page scrolls away entirely — it is never
  pinned; books do not keep their title page hovering over chapter
  one. *Disabled (no JS):* title page with §6.1's footnote line.
- **Content merge.** Every line of the hero is the document's real
  front matter — title, publisher, edition, count. The edition
  statement's numbers are data (counted from the page's own slips by
  the build), so the hero's calmest line is also its most checkable.
- **Failure fallback.** The hero is static HTML; its only dynamic
  part is §6.1, whose fallbacks apply. If the edition count cannot
  be computed at build time, the statement prints without the count
  ("Second edition, corrected") rather than with an invented one.
- **Reduced-motion variant.** §6.1's variant; the rest of the hero
  has no motion to reduce.
- **Breakpoints (v2).** ≥1200px: 54px title, 34ch measure.
  768–1199px: 44px. <768px: 34px, measure full-width with 20px leaf
  padding; the publisher's line wraps above the title rather than
  shrinking below 11px.
- **Edge cases & failure modes (v2).** *A one-correction page:* the
  flutter uses its one real slip (§6.1) and the edition statement
  says so; the hero's stillness grows, which suits it. *No
  corrections at all:* the theme should not have been chosen (§1) —
  the hero degrades to a plain title page and the gate fails the
  build on theme-fit, not on craft. *Very long titles:* the stage
  caps at three slips (§6.1); the title wraps in the centred measure
  and slips anchor to their words through the wrap.
- **Accessibility spec (v2).** One `<h1>`, the corrected title (§6.1).
  The publisher's line and edition statement are plain text in
  reading order. The contents link's text names its destination
  ("Begin at the first page — Contents"). Contrast: `--note` on
  `--page` 6.91:1 for the small mono lines (mono at 11px uppercase in
  `--note` is apparatus, duplicated by the edition statement in
  Garamond — the pairing is deliberate).
- **Performance budget & mobile variant.** Static but for §6.1.
  Mobile: the type steps above; nothing is cut — the title page is
  the theme's cheapest page.
- **Tokens consumed (v2).** `--page`, `--ink`, `--note`, `--cloth`,
  `--ease-paste`.

### 6.14 The running head & erratum counter (page family: navigation)

- **What & why.** A corrected book carries its identity at the head
  of every page: title on the left, and — this theme's addition —
  the running count of corrections witnessed, "Erratum No. n", on
  the right. The running head is the page's navigation furniture
  (book title → home; a contents link → the index) and its progress
  instrument in one strip, because in this theme progress *is* the
  erratum count (§5). It belongs here because a reader deep in a long
  corrected document needs exactly two things from the header: where
  they are in the book, and how much of its honesty they have seen.
- **Structure.** A `<header class="running-head">` band across the
  leaf's top (and onto the cloth on full-bleed mobile): left, the
  book's short title in Garamond 17px small-caps as the home link;
  centre (≥1200px only), the section name of the passage in view,
  Garamond italic `--note`, updated by the scrollspy; right, the
  counter — a 22px slip-paper chip, rotated −0.8° (a miniature slip
  doing header duty), carrying "ERRATUM No." in mono 10px and the
  current number in mono tabular 15px — plus the contents link,
  drawn as a Garamond contents entry. The band is sticky at the
  leaf's top on ≥768px, with a `--paste` hairline beneath.
- **Motion spec.** The counter **steps**, never rolls: when a
  correction is passed (§6.2/§6.8's beat, t₀+120ms), the number
  changes in one frame while the chip performs a 140ms `--ease-press`
  settle (scale 1.06→1, shadow squeezing and releasing) — a stamp
  acknowledging the step. The section name crossfades 160ms on
  scrollspy change. The band itself gains its hairline shadow as the
  page first scrolls (opacity over the first 40px of scroll, scrubbed
  by the shared loop). No other motion: a running head that performs
  is a banner ad in a book's clothing.
- **Choreography timeline (v2).** Per correction passed: source paste
  completes → +120ms: chip settles (140ms) with the new number already
  in place at the settle's first frame — the number changes *as* the
  stamp lands, not after → pin swap (§6.3) and index row (§6.8)
  complete inside the same 400ms window. Per scrollspy change: old
  section name fades 80ms → new name fades 80ms.
- **State matrix (v2).** *Rest (top of page):* counter at "Erratum
  No. 3" after the hero (or No. 0 → the chip reads "ERRATA — none
  yet" on a page whose corrections all sit below; the chip never
  shows a number for a correction not yet passed). *Hover:* the chip
  lifts its corner 10° (§6.4 at miniature scale) — it is a slip, and
  behaves like one; the title and contents links underline via leader
  draw (§6.13). *Focus:* rings on both links; the chip is not
  focusable (it is a status, and its information is the index's).
  *Active:* links navigate (home via §6.9's transition; contents
  scrolls to the index). *Scrolled-past:* n/a — the head is the
  persistent state. *Disabled (no JS):* the chip shows the page's
  total ("ERRATA — 14 in this edition") since no live count exists;
  the section name is absent (no scrollspy) and the band is a plain
  title strip.
- **Content merge.** The counter counts the page's real slips, in
  step with the pin and the index — three views of one DOM fact. The
  section name is the actual heading in view. Nothing in the head is
  decoration: remove the corrections from the page and the counter
  has nothing to say, which is the correct relationship.
- **Failure fallback.** If the counting logic fails, the chip falls
  back to the no-JS total form rather than freezing on a wrong live
  number — a static true total outranks a live false one. Scrollspy
  failure leaves the last true section name, never a blank.
- **Reduced-motion variant.** The number steps without the chip
  settle; the section name swaps without crossfade; the hairline is
  present from the first pixel of scroll. The 120ms flash of §6.9's
  variant lands on this band.
- **Breakpoints (v2).** ≥1200px: full three-part head. 768–1199px:
  the centre section name is dropped (the pin's tab, §6.3, carries
  location at this size); title and chip remain. <768px: the band
  sits on the cloth (full-bleed), title truncates at 18ch with the
  full title in its link's accessible name; the chip keeps its full
  size — the counter is the last thing the theme would shrink,
  because on mobile it is the *only* running apparatus (§6.3's
  ruling).
- **Edge cases & failure modes (v2).** *Anchor arrival mid-page:*
  the counter initialises to the number of corrections above the
  arrival point (counted from the DOM at load) — a visitor who lands
  at section four is told the truth about what they have "passed" in
  document order, and the chip's settle does not fire for the
  initialisation. *A correction above the fold after the hero:* the
  count includes the hero's three from the start (§6.1). *Print:*
  the running head prints as a true running head (title + total
  errata) on each printed page via `@page` margins where supported,
  and the sticky band itself is hidden.
- **Accessibility spec (v2).** The counter is a `role="status"` with
  `aria-live="off"` — deliberately: its changes are *not* announced
  (a page announcing every passed correction would be unusable by
  ear); its accessible form is the static total in its `aria-label`
  ("14 errata in this edition; the index at the foot lists them
  all"). Links are real links with full names. Chip contrast: mono
  `--ink` on `--slip` 13.65:1; the red label uses `--red-deep` at
  10px (7.26:1 class on slip).
- **Performance budget & mobile variant.** One sticky band; the
  scrollspy is an IntersectionObserver; ≤0.1ms/frame. Mobile: the
  cloth-band form above, same budget.
- **Tokens consumed (v2).** `--page`, `--cloth`, `--slip`, `--paste`,
  `--ink`, `--note`, `--red-deep`, `--ease-press`, `--lerp`.

### 6.15 The corrected table (page family: cards / listing / data)

- **What & why.** The theme's sternest test: a long data table —
  prices, specifications, results — that accumulates corrections as
  it is scrolled, row by row, until the table the visitor finishes
  is demonstrably not the table that was first published. Tables are
  where silent swaps do their worst damage in real publishing, so the
  table is where this theme must be most itself: corrected cells
  marked, superseded values kept, the accumulation visible. It
  belongs here because the original library entry names it ("a long
  data table accumulates corrections scrubbed in proportion to
  scroll") — the deepening turns that sentence into a buildable
  instrument.
- **Structure.** A real `<table>` — caption, `th` row and column
  headers, lining-figure Garamond numerals in cells (§3) — with one
  addition: a narrow **correction gutter** column at the table's
  right edge (36px), headed "Errata". A corrected cell carries its
  slip *in the gutter*, aligned to the row, numbered, with a hairline
  `--paste` leader from the gutter slip to the corrected cell. The
  cell's text is the corrected value (the law); the superseded value
  is in the gutter slip's formula and revealed in place by §6.4's
  disclosure variant (below). Cards and listing items elsewhere on
  the page follow the same law at lower density: a corrected card
  value wears its slip per §6.2, and a listing's corrected entries
  carry a gutter-equivalent — a right-aligned slip chip in the item's
  footer line.
- **Motion spec.** As each corrected row crosses 65% viewport height,
  its gutter slip pastes: the brush stroke draws vertically in the
  gutter (240ms, §6.6's table ruling), the slip scales in from its
  top edge (380ms `--ease-paste`), the leader rule draws (scaleX,
  200ms), and the cell's figure rolls (§6.5, 650ms at table scale) —
  one row's correction is a 900ms event, and rows trigger in reading
  order with at most two in flight. The accumulation is scrubbed in
  proportion to scroll in the library entry's sense: rows correct as
  the reading reaches them, neither before (an unseen correction is
  a spoiler of the audit) nor in a batch at load.
- **Choreography timeline (v2).** Per row, t₀ = row crosses 65% vh →
  t₀+0ms: gutter stroke begins → t₀+240ms: slip scales in →
  t₀+300ms: leader draws → t₀+350ms: cell figure begins its roll →
  t₀+620ms: slip settled → t₀+1000ms: roll lands; the header counter
  and pin acknowledge per §6.14/§6.3 (the pin shows the table's
  latest erratum while the table is in view).
- **State matrix (v2).** *Rest:* uncorrected rows are plain print;
  corrected rows wear gutter slips once passed. *Hover:* the gutter
  slip lifts its corner (§6.4) — and because a table cell cannot be
  overlaid, the superseded value appears as a printed line in a
  full-width sub-row that expands beneath the row (200ms
  `--ease-press`): "As first published: £42 — corrected by Erratum
  No. 7, 12 March." *Focus:* the gutter slip is focusable (it is the
  row's provenance control); focus opens the same sub-row. *Active:*
  press-flat (§6.12) on the gutter slip. *Scrolled-past:* corrected,
  static; sub-rows closed. *Disabled (no JS):* every corrected row
  ships with its gutter slip present and its sub-row content carried
  in the index; the sub-row itself is a JS disclosure, and its facts
  are never exclusive to it.
- **Content merge.** The gutter is part of the table — a column the
  table grew because it needed one — and every mark in it points at a
  cell in its own row. The corrections are the table's data about its
  data; remove them and the table still computes, but it no longer
  testifies.
- **Failure fallback.** The 900ms watchdog pastes any stalled gutter
  slip. If the table is re-sorted or filtered by the visitor (where
  the build offers it), gutter slips travel with their rows (they are
  row content, not overlays) and the accumulation state persists by
  erratum number, not by row position — provenance survives
  rearrangement.
- **Reduced-motion variant.** Gutter slips present statically; no
  rolls; sub-rows open instantly. The table's testimony is complete.
- **Breakpoints (v2).** ≥1200px: full gutter table. 768–1199px: the
  gutter narrows to 28px and the slip becomes a numbered chip (number
  only, full slip in the sub-row disclosure). <768px: the table
  linearises into row-cards (the theme's listing form), each carrying
  its corrected values with below-value slips per §6.2's mobile
  ruling — a corrected table on a phone is a list of corrected
  records, and pretending otherwise would bury the figures.
- **Edge cases & failure modes (v2).** *A row with two corrected
  cells:* one gutter slip per row, its formula covering the primary
  (leftmost) correction and "+1 more" counted in the sub-row, where
  both formulas print in full — the gutter rations paper, the
  sub-row keeps the record. *Corrections denser than one per three
  rows:* the §4 density law yields to the table's nature — tables are
  the theme's high-density habitat — but the two-in-flight cap still
  holds, queuing the rest at 150ms intervals. *Sticky table headers:*
  the header row may stick; gutter slips never stick with it (a slip
  belongs to its row, not to the furniture).
- **Accessibility spec (v2).** The table is a true table with
  `scope`d headers; a corrected cell carries `aria-describedby`
  pointing at its sub-row text ("corrected from £42 by Erratum
  No. 7"), so the provenance is in the table's accessible structure,
  not only in the gutter's visuals. The gutter column's header is
  "Errata" and its slips' labels follow §6.2. Sub-row expansion is a
  `button` with `aria-expanded` where it is interactive. Numerals
  remain text at all times.
- **Performance budget & mobile variant.** Per-row events are small
  transforms; the table's cost is DOM size, capped by build guidance
  at 120 rows per page (longer tables paginate by section, with the
  errata numbering continuous across pages of the table). Mobile:
  the linearised form above.
- **Tokens consumed (v2).** `--page`, `--ink`, `--note`, `--slip`,
  `--paste`, `--red-deep`, `--ease-paste`, `--ease-brush`,
  `--ease-press`.

### 6.16 Report an erratum (page family: form / conversion)

- **What & why.** The theme's conversion point, and its most
  characteristic: the form through which a reader reports an error
  they have found. A corrected edition that cannot receive new
  corrections is a finished fiction; this form is how the page's
  honesty stays alive after publication. It belongs here because the
  form is set as the thing it produces — the reader's submission is
  composed *as an errata slip* while they write it, and submitting it
  pastes their slip, provisionally, at the form's foot: "Received —
  to be verified." The conversion is not a signup; it is an act of
  readership, and the theme treats it with the full ceremony of its
  material.
- **Structure.** A `<form class="erratum-form">` on the leaf, set as
  a printed form from the book's world: fields for the location
  (page/section — a select of the page's real sections), the printed
  error (text input), the correction (text input), and the reader's
  name for the acknowledgment (optional). Labels are Garamond; inputs
  are ruled-line fields (transparent ground, 1px `--note` bottom
  rule, Garamond 19px input text — the reader writes in the book's
  hand). Beside/below the fields sits the **live slip**: a slip-paper
  element, rotated per §4 using the *next* erratum number (the count
  + 1, computed from the DOM), whose formula line updates as the
  reader types: `for "…" read "…"` composed from their two fields.
  The submit button is a stamp: mono uppercase in a `--red`
  impression border, "Submit this erratum".
- **Motion spec.** Typing in either value field updates the live
  slip's formula with a 120ms mono caret-blink-free refresh (text
  swaps instantly; a typewriter effect here would be theatre over
  someone's real correction). Field focus: the rule thickens to 2px
  and a `--cloth` plate slides beneath it (200ms `--ease-paste`) —
  the line being written on is underlined by the book. Submit: the
  stamp button presses (§6.12's stamp grammar at button scale,
  160ms); on success the live slip *pastes* — brush stroke (300ms),
  slip settling at its angle (460ms `--ease-paste`) into the form's
  "received" zone — and the confirmation prints beneath it in
  Garamond: the provisional number, and the honest sentence "This
  slip is tipped in provisionally. It joins the index when the
  editors have verified it." The provisional slip does **not** enter
  the numbered index (§6.17) — it wears its number with a "prov."
  suffix, because the index's 1:1 law admits only verified
  corrections.
- **Choreography timeline (v2).** t₀ = submit → t₀+0–160ms: stamp
  presses → server round-trip (the form is inert, the stamp held at
  90% impression) → success: t₁+0ms brush stroke → t₁+300ms slip
  settles → t₁+460ms confirmation line fades in (300ms) → the form's
  fields clear to a printed "received" state (values retained in the
  pasted slip, which is the receipt). Error path: the offending
  field's rule turns `--red`, its ground washes `--red` at 6%, and
  the error prints *as a slip* pasted at the field's end (380ms) in
  the corrector's voice (§12): the form corrects the reader the way
  the reader corrects the book — the theme's symmetry, and its best
  joke, played completely straight.
- **State matrix (v2).** *Rest:* ruled fields empty, live slip
  showing its formula with em-dash placeholders (`for "—" read "—"`).
  *Hover:* the stamp button's impression border deepens 40%→70%.
  *Focus:* the ruled-line treatment above; the stamp's focus ring is
  the impression border at full `--red` plus a 2px offset outline.
  *Active:* the press. *Submitting:* fields inert, stamp held.
  *Success:* the pasted provisional slip + confirmation; the form
  offers "Report another" as a Garamond link that resets it.
  *Disabled (no JS):* the form still submits (it is a real form);
  the live slip is absent and the confirmation is the server's page —
  the ceremony is an enhancement, the channel is not.
- **Content merge.** The form's output is a slip because a slip is
  what the form produces in the theme's world; the live preview is
  the reader's own words taking the correction's shape as they type.
  Nothing about the interaction decorates the task — it *is* the
  task, wearing the theme's material because the material is the
  meaning.
- **Failure fallback.** A submission that fails (network, server
  500) never loses the reader's text: fields retain their values,
  the live slip keeps its formula, and the error prints in the
  corrector's voice with a plain retry. A duplicate submission (same
  location + formula as a verified erratum) is answered honestly:
  "This correction is already in the index as Erratum No. 7" — with
  the index row linked.
- **Reduced-motion variant.** No paste ceremony: on success the
  provisional slip appears statically with its confirmation; errors
  print instantly. The live formula still updates as the reader
  types (it is content, not motion).
- **Breakpoints (v2).** ≥1200px: fields and live slip side by side
  (the slip in the working margin, where slips live). 768–1199px:
  stacked, slip beneath the fields. <768px: stacked; the stamp
  button is full-width, 48px tall; the live slip sticks at the form's
  foot while typing so the reader sees their correction take shape
  without scrolling.
- **Edge cases & failure modes (v2).** *Very long corrections* (a
  whole sentence): the live slip grows to its max-width and the
  formula wraps; past ~280 characters the form gently rules the
  submission a "note for the editors" instead — a text field replaces
  the slip preview, because a slip has a size and a paragraph is not
  one (§3's law, enforced by the form itself). *Spam/abuse:* the
  provisional state is the defence — nothing enters the index
  unverified, and the form says so, which is both honest and
  discouraging to vandals. *The reader corrects the form's own copy:*
  allowed and welcomed — the section select includes "This form".
- **Accessibility spec (v2).** Real `<label>`s, real validation with
  `aria-describedby` error slips (the error slip's text is the
  description target), focus moves to the first error on submit and
  to the confirmation (tabindex −1) on success. The live slip is
  `aria-hidden` (it duplicates the fields' values); the provisional
  number and verification status are in the confirmation text, which
  is a `role="status"`. Stamp contrast: `--red` on `--page` 5.64:1
  at 11px uppercase — the button's text is also carried by its size
  and border; `--red-deep` is used for the button text at <768px.
- **Performance budget & mobile variant.** The form is DOM and text;
  the live slip updates are ≤1 text write per keystroke debounce
  (120ms). Mobile: the sticky-slip layout above.
- **Tokens consumed (v2).** `--page`, `--ink`, `--note`, `--cloth`,
  `--slip`, `--paste`, `--red`, `--red-deep`, `--ease-paste`,
  `--ease-press`, `--ease-brush`.

### 6.17 The errata index (page family: footer / colophon)

- **What & why.** The foot of the page, and the theme's court of
  record: the complete numbered index of every correction on the
  page, set as back matter on the cloth ground, closing with the
  colophon line of the edition. §6.8 specifies its accumulation
  behaviour; this element is its full composition as the page's
  footer. It belongs here because errata slips were *listed* — the
  slip at the front of the book ended with the index of all of them —
  and because the footer's job in this theme is not links and logos
  but testimony: everything above this line has been corrected
  exactly thus, and here is the proof, in order, checkable against
  every slip.
- **Structure.** A `<footer>` on `--cloth` (the leaf ends; the book
  closes onto its binding): the index as an `<ol>` (§6.8's rows —
  number, location, formula, date, miniature), grouped by section
  where the page has distinct parts; beneath it, the colophon in
  slip-paper-toned text on cloth (`--slip` on `--cloth`, 8.76:1):
  edition statement, publisher line, "Set in EB Garamond and IBM Plex
  Mono", the count of errata in this edition (computed, §6.14's
  total), and the standing invitation linking to §6.16's form ("Found
  an error we have not? Report it — the index is not closed.").
  Ordinary footer furniture (legal links, contact) sits in a final
  quiet row in `--cloth-light`, visually demoted below the testimony.
- **Motion spec.** The accumulation (§6.8) is the index's motion;
  the footer itself, when it first enters, performs one small act:
  its heading rule — a brush stroke the width of the measure — draws
  once (600ms `--ease-brush`), the last paste laid on the page,
  beneath which the record sits. The margin pin docks as the index's
  header row as it arrives (§6.3). Nothing else moves; a court of
  record does not fidget.
- **Choreography timeline (v2).** Index enters → heading stroke
  draws (600ms) → the pin docks (its mini-slip settling into the
  header row over 240ms) → any rows still un-accumulated cascade per
  §6.8 (60ms apart) → the footer stands complete, and the header
  counter's number, the pin's number and the index's last row agree
  — the page's closing audit, performed in view.
- **State matrix (v2).** *Rest:* the complete index (no-JS and
  reduced-motion states are this). *Hover/focus:* §6.8's row
  behaviours. *Active:* row links jump to their data (§6.8).
  *Scrolled-past:* n/a — the footer is the end. *Disabled:* the
  printed index, complete — the state every other state is an
  enhancement of.
- **Content merge.** The footer *is* content — the page's back
  matter, as integral as its first section. The colophon's count is
  the page's own count of itself; the invitation is the page's real
  conversion path. A visitor who reads only the footer has read the
  page's whole history of error and repair, which in this theme is a
  legitimate way to read the page.
- **Failure fallback.** §6.8's index watchdog guarantees completeness
  on arrival. If grouping data is missing, the index prints as one
  ungrouped list — order by number is never sacrificed to grouping.
- **Reduced-motion variant.** §6.8's variant; the heading stroke is
  drawn complete; the pin does not dock (it simply is not present,
  and the header row stands without it).
- **Breakpoints (v2).** ≥1200px: index in two columns (§6.8).
  768–1199px and <768px: one column; the colophon stacks; the legal
  row wraps. On cloth grounds at all sizes, text is `--slip` or
  `--cloth-light` only (§2's pairing rule).
- **Edge cases & failure modes (v2).** *A page whose corrections were
  all withdrawn:* the index prints its struck rows and the colophon
  count reads "14 errata, all withdrawn" — the record of a perfect
  retraction is still a record. *Multi-page documents:* each page's
  footer carries its own index; the edition's master index lives on
  the contents page, numbered continuously — the build must carry
  the numbering offset as content data, never recompute it per page
  (two pages both claiming Erratum No. 1 is the theme's version of a
  duplicate key).
- **Accessibility spec (v2).** §6.8's row spec; the footer is a
  contentinfo landmark containing a navigation-labelled list
  ("Index of errata"). Colophon contrast on cloth as measured above.
  The invitation link's text states its purpose in full.
- **Performance budget & mobile variant.** Static but for §6.8's
  accumulation and one 600ms stroke. Mobile: single column, as
  above.
- **Tokens consumed (v2).** `--cloth`, `--cloth-light`, `--slip`,
  `--paste`, `--ink`, `--red-deep`, `--ease-brush`, `--ease-paste`.

### 6.18 The unissued page (page family: 404 / empty state)

- **What & why.** The 404 of a corrected edition is a bibliographic
  event, and the theme treats it as one: the requested leaf was
  never issued. The page shows a blank leaf on the cloth — a leaf
  with a title-page composition (§6.13) whose title is the honest
  statement "This page has not been issued" — and, pasted over it,
  one slip: the only correction that can be made to a page that does
  not exist, redirecting the reader to the nearest issued pages.
  Empty states (no results, an empty listing) use the same grammar:
  the leaf is blank, and a slip pasted on it carries the one true
  sentence about the emptiness and the way back.
- **Structure.** The leaf, mostly empty: a Garamond statement of the
  situation, the pasted slip (numbered "Erratum No. —" with the
  number left blank in mono, the theme's one lawful blank: a
  correction cannot be numbered against a page that is not in the
  edition), its formula reading `for this address read one of the
  following`, and a short contents list of real destinations set as
  a contents page (leaders + folios, §6.14's material). For search
  empty states, the slip's formula quotes the reader's own query:
  `for "…" — nothing in this edition answers to it`, with the
  nearest sections listed.
- **Motion spec.** The slip flutters in once, on load, exactly as
  §6.1's slips do (500ms `--ease-flutter` after a 500ms beat) — the
  single most eloquent entrance in the theme, because it is the only
  page where the correction is the *entire* content. The contents
  leaders draw on hover per §6.14. Nothing else moves, ever; an
  empty page with ambient motion is a waiting room, and this is a
  library.
- **Choreography timeline (v2).** Load → the blank leaf stands →
  500ms beat → the slip flutters and pastes (500ms) → its text
  reveals (§6.10) → stillness, and the contents list waits. The
  header counter (§6.14) reads "ERRATA — none", the only page where
  it does: there is nothing here to correct, and the apparatus says
  so rather than inventing a count.
- **State matrix (v2).** *Rest:* as specced. *Hover:* the slip lifts
  its corner (§6.4) — beneath it is blank leaf, which is the point:
  there is nothing under this correction because there was never
  anything here. *Focus:* the contents links take focus in order.
  *Active:* links navigate via §6.9. *Disabled (no JS):* the slip is
  present statically; the statement and contents stand.
- **Content merge.** The 404's slip corrects the only datum the page
  has — the address the visitor asked for — and the contents list is
  the book's real contents. The emptiness is the content, and the
  theme's discipline (a slip needs a datum) is honoured by making
  the request itself the datum.
- **Failure fallback.** The page is static HTML with one flutter; its
  fallback is itself. If the nearest-pages data is unavailable, the
  contents list falls back to the edition's top-level sections —
  never to a generic "go home" alone.
- **Reduced-motion variant.** The slip is present, pasted, static.
  The blank number stays blank.
- **Breakpoints (v2).** ≥1200px: the leaf at reading measure, the
  slip at full size. <768px: the leaf full-bleed, the slip below the
  statement per §6.2's mobile placement; the contents list full
  width with 44px rows.
- **Edge cases & failure modes (v2).** *Soft 404s* (a listing with
  filters that match nothing): the slip quotes the filter state, not
  a query, and offers the single action "Clear the filters" as a
  contents entry — the correction is to the reader's own slip of
  instructions, which is exactly an erratum. *A page withdrawn after
  publication* (a true retraction): a different, graver variant —
  the leaf carries the original title struck through in Garamond and
  a slip reading "This page is withdrawn by the editors" with the
  date and the reason in the index; the theme distinguishes *never
  issued* from *withdrawn* because bibliography does, and conflating
  them is a small dishonesty the audience for this theme will catch.
- **Accessibility spec (v2).** The statement is the `<h1>`. The blank
  number is rendered as text ("Erratum, unnumbered") in the slip's
  accessible label — a screen reader is told the joke plainly,
  because the joke is information. Contents links are fully named.
  The HTTP status remains a true 404; the theme decorates the
  response, never its semantics.
- **Performance budget & mobile variant.** The lightest page in the
  theme: one slip, one flutter. Mobile: as breakpoints above.
- **Tokens consumed (v2).** `--page`, `--cloth`, `--ink`, `--note`,
  `--slip`, `--paste`, `--red-deep`, `--ease-flutter`, `--ease-paste`.

## 7. Page application map

**Home / title page.** §6.13's composition: the flutter (§6.1), the
edition statement with its counted corrections, then the book's
sections in reading order with paste-overs (§6.2) at the §4 density.
The home page is the edition's front matter and first chapter in
one; its index (§6.17) is the full record.

**Listing / catalogue.** Entries as corrected records: each entry a
Garamond title, its data, and — where a datum was corrected — a slip
per §6.2 (desktop) or the below-datum placement (mobile). A listing
may carry a head slip of its own: the listing's title corrected
("for *Complete Works* read *Works in Progress*") is the theme's
honest way to head an imperfect catalogue. Sorting and filtering
never renumber errata; numbers belong to the edition, not to the
view.

**Detail / article.** The theme's natural home. Long prose, worked
margin, pin resident (§6.3), corrections at datum density, the table
ruling (§6.15) where data tables occur, and the index closing the
leaf. The detail page's corrections are its credibility, displayed
at the exact points of doubt.

**About / the edition page.** The story of the corrections
themselves: why this edition exists, what the first printing got
wrong, the editors' policy (every correction numbered, nothing
silently swapped — the policy *is* §1's laws, published). This page
carries the fewest slips and the most Garamond: it is the one place
the book speaks about its slips rather than through them.

**Contact / conversion.** §6.16's form is the conversion pattern for
every form in the theme (report, subscribe, order): ruled Garamond
fields, a live slip composing the submission's essence, a stamp for
a button, errors delivered as slips in the corrector's voice. A
checkout in this theme confirms with a pasted receipt slip carrying
the order's real number as its erratum-style reference — the
receipt is tipped into the reader's copy of the page.

**Contents / index page.** For multi-page editions: the contents set
as a book's contents (leaders, folios) and the master errata index
numbered continuously across pages (§6.17's rule). This page is the
apparatus entire — it carries no slips of its own except one: its
own title, corrected, because the theme's first law applies to the
apparatus too.

**404 / empty.** §6.18, in its never-issued and withdrawn variants.

## 8. Worked examples

### 8.1 The hero — a pricing page corrects its own title

A software product's pricing page, second edition. The book title as
first published was "Honest pricing, fixed forever" — a claim the
publisher had to withdraw when prices rose. The corrected title,
which is the DOM `<h1>`, reads "Honest pricing, corrected in the
open." Build sequence: the title page (§6.13) stands with the staged
superseded title; at fonts-ready the 500ms beat holds; slip No. 1
flutters onto "fixed forever" carrying `Title page — for "fixed
forever" read "corrected in the open"`, stamped with the real date
of the price change; Nos. 2 and 3 follow onto the publisher's line
(the company's former name) and the edition statement (the old
edition number). The header chip settles at "Erratum No. 3"; the
visitor who lifts No. 1's corner reads the withdrawn claim beneath,
in demoted italic. Scroll timeline: hero still → three pastes by
1.6s → first pricing section enters → §6.2 pastes the corrected
monthly figure as its slip (No. 4) lands and the figure rolls
£42 → £48 in the same beat (§6.5) → the pin takes up No. 4 in the
margin. The visitor has been on the page twenty seconds and has
already watched it correct itself four times, each time on the
record.

### 8.2 Mid-page — the specifications table accumulates

Halfway down the same page, the specifications table (§6.15): forty
rows, of which six carry corrections from a supplier's revised
datasheet. As the reader scrolls the table, row 7's gutter slip
(No. 9) pastes — stroke, slip, leader, and the cell's weight figure
rolling 1,200 g → 1,020 g; the sub-row stands ready under §6.4 to
show "As first published: 1,200 g". Rows 12, 19, 19 (second cell,
counted in the sub-row), 28 and 33 follow, never more than two in
flight. The pin in the margin walks Nos. 9 → 14 as the table passes;
the header chip steps in the same beats; a reader who jumps straight
to the footer finds the index already holding rows 1–14 in order,
the table's six among them, each linking back to its row. Emotional
arc: the table begins as the driest object on the page and ends as
the most trusted, because it is the one that showed its working.

### 8.3 Conversion — a reader reports the seventh error

The report form (§6.16) at the foot of a documentation page. A
reader has found a wrong version number in a tutorial. They choose
the section ("Installing — step 3"), type the printed error
("v2.4.1") and the correction ("v2.4.3"); in the margin, the live
slip — rotated 1.13°, numbered "No. 15 prov." — composes itself:
`Installing, step 3 — for "v2.4.1" read "v2.4.3"`. They press the
stamp. The slip pastes into the received zone with its brush stroke;
the confirmation prints the provisional number and the verification
sentence; the index does not change (its law holds), and the reader
leaves with a receipt that is itself a small, crooked, honest piece
of paper. Two days later, verified, the correction appears on the
tutorial as Erratum No. 15 — no "prov." — and the reader who returns
finds their slip in the index, in order, among the others.

## 9. Anti-slop — what makes THIS theme look cheap

1. **Straight slips.** A slip at 0.0° reads as a UI card with a
   paper texture. Cure: the §4 rotation formula, enforced at the
   gate; angles are computed from erratum numbers, never eyeballed
   and never randomised per load (a slip whose angle changes between
   visits was never pasted by anyone).
2. **Slips carrying the data.** The corrected value hidden inside
   the slip, the datum beneath showing the old figure (or a
   placeholder). This inverts §1's law and destroys the theme's
   accessibility and SEO in one move. Cure: the datum's text is the
   corrected value; the slip annotates; the gate tests by disabling
   the slip layer and re-reading the page.
3. **Invented numbering.** "Erratum No. 14" as a decorative flourish
   on a page with six slips. Cure: numbers are DOM-counted; header,
   pin and index are three views of one count; the gate recounts.
4. **Red everywhere.** Red headings, red links, red buttons — the
   corrector's pencil diluted into a brand colour. Cure: §2's
   ration; red lives inside slips, stamps and errors only.
5. **Sticker physics.** Slips that bounce, spring or wobble on
   jelly easings; drop shadows like floating cards (large blur,
   vertical lift). Cure: the theme's easings are paste, press and
   peel; shadows are 3px offsets in `--paste`, because the slip is
   *on* the page, not above it.
6. **The blizzard.** Thirty slips on one page because "the theme is
   slips". Cure: §4's density law; overflow corrections go to the
   index with margin markers. A page that is all corrections has no
   book left to correct.
7. **Fake superseded values.** "Lorem ipsum" or a generic "old
   price" beneath the corner-lift. Cure: the superseded value is a
   content requirement (§6.4); a slip without a real predecessor is
   flagged and cannot ship.
8. **Mono prose.** Whole paragraphs in IBM Plex Mono because it
   "looks like documentation". Cure: §3's casting law; mono is for
   slips, numbers and stamps, capped at slip length.
9. **Silent index.** An index that lists fewer corrections than the
   page carries, or deletes withdrawn rows. Cure: the 1:1 law and
   §6.8's struck-row rule; the gate diffs index rows against slip
   elements.
10. **The costume site.** Slips pasted over content that was never
    wrong — a marketing page wearing corrections as texture. Cure:
    §1's when-NOT-to-use; the theme lead must name the real
    corrections a page carries before the theme is approved for it.

## 10. Quality gate

**Blocking (any failure stops the build):**

1. **The law test.** Disable the slip layer (CSS + JS off): every
   corrected value on the page still reads correctly, in place.
2. **The count test.** Slip elements in the DOM = highest erratum
   number shown = index rows listed (withdrawn rows included,
   struck). All three numbers equal, verified by script.
3. **The rotation test.** Every slip's computed rotation is within
   [0.5°, 1.5°] and matches the §4 formula for its number.
4. **The predecessor test.** Every slip has a real superseded value
   in its anchor and its index row; no placeholder text anywhere in
   the correction layer.
5. **No invisible content.** With JS enabled but all triggers
   suppressed, the 900ms watchdog leaves every slip pasted, lettered
   and legible; the index is complete.
6. **Reduced-motion completeness.** With `prefers-reduced-motion`,
   every correction is present and auditable (slips static or
   footnoted inline); no information exists only in an animation.
7. **Contrast.** Slip text ≥ 4.5:1 in all states (measured: ink on
   slip 13.65:1; red numbers per §2's rules, `--red-deep` wherever a
   number stands alone); superseded values ≥ 4.5:1 (`--note` 6.34:1
   on slip, 6.91:1 on page).
8. **Casting.** No Garamond inside a slip; no mono prose beyond slip
   length; formulas verbatim per §12.

**Standard (fix before ship unless waived in writing):**

9. Density within §4's law (≤1 slip per viewport-height in body
   sections; ≤3 visible per viewport outside the hero).
10. Paste synchrony: each §6.5 roll lands within 40ms of its slip's
    shadow setting.
11. The sheen (§6.7) is the only ambient loop; it is absent under
    reduced motion and pauses off-screen.
12. Print: the page prints as a corrected book — slips rendered at
    their angles with formulas legible, index complete, pin and
    running head per §6.3/§6.14's print rulings.
13. Five-second test: a first-time visitor can say, within five
    seconds of the hero, "this page corrects itself, and the
    corrections are numbered" — if they say "sticky notes", the
    rotations or the formulas have failed.

## 11. Component inventory

Every component a real site in this theme needs, with its themed
treatment. The governing idea: the book's furniture is printed; the
correction layer's furniture is pasted.

- **Buttons.** Primary actions are **stamps** (§6.16): mono
  uppercase text in a `--red` impression border at −2°, press per
  §6.12. Secondary actions are Garamond links with dotted leaders
  (contents style). There are no filled pill buttons in this theme;
  a filled button is a sticker that forgot its formula.
- **Inputs.** Ruled-line fields (§6.16): transparent ground, `--note`
  bottom rule thickening on focus with a `--cloth` plate beneath,
  Garamond 19px input text. Textareas are ruled *pages* (repeating
  31px line rules). Selects open as contents lists.
- **Tables.** §6.15 entire: real tables, lining figures, correction
  gutter, sub-row provenance.
- **Cards.** A card is a leaf fragment: `--page` ground, `--paste`
  hairline, Garamond title; a corrected value on the card wears its
  slip per §6.2; the card never rotates (only slips do — a rotated
  card is a slip that ate the page).
- **Badges.** A badge is a **slip chip**: 22px slip-paper chip at the
  §4 angle for its position, mono 10px — used for "Corrected",
  edition markers, the header counter (§6.14). Badges never carry
  marketing claims ("New!", "Hot!") — a chip that is not a
  correction is refused.
- **Alerts.** An alert is a slip pasted at the head of the section it
  concerns, in the corrector's voice (§12), numbered if it corrects
  anything, unnumbered only if it is pure notice ("This edition is
  still being corrected"). Dismissing an alert presses it flat
  (§6.12) and files it — dismissed alerts are listed, struck, in the
  index's appendix; they are never vaporised.
- **Pagination.** Contents-style: "Leaf 3 of 9" in Garamond with
  leader-linked leaf numbers; the current leaf is the one whose
  number wears a slip chip if that leaf carries corrections.
- **Modals.** **Refused.** A modal is a page pasted over the book
  that admits no correction; the theme's replacement is the
  **tipped-in leaf**: a full-leaf overlay in the book's own layout
  (same measure, same furniture) that enters via §6.9's slip
  transition and can itself carry slips. Confirmations happen inline
  (§6.16's pasted receipt), never in a dialog.
- **Toasts.** **Refused.** A toast is an unnumbered, unindexed,
  self-deleting claim — everything the theme exists to oppose. The
  replacement is the **margin note**: a Garamond italic line in the
  working margin (or a below-datum line on mobile) that persists
  until the visitor passes it, and is summarised in the index
  appendix if it reported a change.
- **Tabs.** Contents tabs: Garamond labels with leader rules; the
  active tab's label is underlined by a brush stroke (§6.6's
  material, drawn once on activation, 300ms). Tab panels are leaves;
  switching leaves does not re-run corrections (they were made once).
- **Accordions.** "Folded leaves": Garamond summary lines with a
  slip-chip showing the count of corrections inside a closed section
  — the one place a number on a closed door is honest, because it
  counts what the door hides and the index lists them.
- **Tooltips.** **Refused as tooltips.** The theme's answer to "what
  was here before" is §6.4's corner-lift (the evidence, in place),
  and to "what does this mean" is a Garamond footnote. A floating
  tooltip is a slip with no paste, no number and no index entry.
- **Loaders.** The coarse state is a leaf with ruled blank lines and
  slip-shaped `--paste` placeholders at the positions corrections
  will occupy — the page *in proof*. Skeletons resolve per §6.2's
  watchdog; a spinner exists nowhere in the theme.
- **Progress bars.** **Refused as bars.** Progress is the erratum
  counter (§6.14) and the accumulating index (§6.8). A determinate
  task (upload, generation) shows its progress as a brush stroke
  drawing across a ruled line, with the figure in mono — paste being
  laid for a slip the visitor is waiting to read.

## 12. Content & copywriting voice

Two voices, cast by §3's law, and a third for the apparatus.

**The book's voice (Garamond)** is the publisher's: calm, complete
sentences, no urgency, no exclamation. It makes claims plainly
because it knows they will be corrected plainly if wrong. ✓ "The
pump weighs 1,020 grams and draws 340 watts at full load." ✗ "A
featherweight powerhouse that sips power!!" Headlines state; they do
not shout. Empty states in the book's voice are bibliographic
(§6.18): ✓ "Nothing in this edition answers to 'gasket'." ✗ "Oops!
No results found 😢"

**The corrector's voice (mono, on slips)** is the trade's formula
language — terse, located, dated. The fixed forms, verbatim:
`for "X" read "Y"` · `line 4: for "X" read "Y"` · `the figure on
p.2 is withdrawn` · `this slip is tipped in provisionally` ·
`already corrected as Erratum No. n`. ✓ `p.2 · Prices — for "£42"
read "£48"` ✗ `price update!! now £48` ✗ `we've made some changes
to this value`. The corrector never apologises at length and never
celebrates; the longest sentence a slip may carry is the withdrawal
notice. Error messages (in forms, §6.16) are corrector's-voice
slips: ✓ `for the date given read a date in the future` ✗ `Invalid
input`. Confirmation voice: ✓ "Received as Erratum No. 15, prov. It
joins the index when the editors have verified it." ✗ "Thanks!!
Your feedback means the world to us."

**The apparatus voice** (index, colophon, running head) is the
librarian's: pure record. Index rows are formulas, not sentences.
The colophon states materials and counts. The standing invitation is
the apparatus's one warm line: "Found an error we have not? Report
it — the index is not closed."

**Banned words** in the correction layer: *oops, sorry, just,
simply, update (as a noun for a correction), tweak, fix (as a verb
for a published error — the word is "correct"), new-and-improved*.
**Owned words**: *erratum/errata, for … read …, tipped in, as first
published, withdrawn, verified, edition, leaf, in the open*.

## 13. Full-page scroll choreography map

A standard detail page (title page, three prose sections, one table,
the form, the index), top to foot. The emotional arc: **confidence,
tested and re-earned** — the page begins by correcting itself,
spends its middle keeping that promise at datum level, and ends by
handing the visitor the complete record and an invitation to extend
it.

1. **The title page stands.** Calm Garamond; the wrong title staged.
   *Feel: a book, opened.*
2. **The flutter** (§6.1): three slips correct the title by 1.6s;
   the chip settles at No. 3. *Feel: it corrects itself first — before
   asking anything of me.*
3. **First prose section.** One paste-over (§6.2 + §6.5 roll) as the
   corrected figure enters; the pin takes residence in the margin.
   *Feel: the promise is kept at the level of a single number.*
4. **The sheen passes** (§6.7) across the first slip as reading
   continues. *Feel: the page is recently worked on; someone cares
   for it.*
5. **Second section, a corrected name.** Paste-over with the
   corner-lift invited by proximity; most visitors lift here for the
   first time and meet the superseded name. *Feel: the evidence is
   really there, under the paper.*
6. **The table** (§6.15): six corrections accumulate down the rows,
   the pin walking the numbers, the counter stepping in sympathy.
   *Feel: the driest object becomes the most trusted.*
7. **A quiet stretch** — a full section with no corrections. The pin
   rests; the margin is empty; nothing performs. *Feel: the book is
   mostly right, and says so by silence.*
8. **The form** (§6.16): the visitor composes a correction; the live
   slip takes shape; the stamp; the provisional paste. *Feel: my
   readership is material here — I can leave a slip of my own.*
9. **The index arrives** (§6.17/§6.8): the heading stroke draws, the
   pin docks, the count agrees everywhere. *Feel: a record, closed
   and checkable.*
10. **The colophon and the invitation.** "The index is not closed."
    *Feel: honesty as an ongoing practice, not a launch feature.*

Reverse pass: scrolling back up, nothing replays, nothing un-pastes;
the slips sit in register (§6.11 settles), the pin swaps backward to
the correction nearest the reading line, and the page reads as a
corrected book being re-read — which is the correct tense for a
second pass. Jump-scroll catch-up: index rows cascade at 60ms (§6.8),
paste-overs land instantly in final state for sections skipped
entirely (a correction nobody watched still happened; its slip is
pasted when you arrive, not performed for an empty room).

## 14. Whole-page performance budget

- **Assets.** Fonts: EB Garamond (2 weights + italic) and IBM Plex
  Mono (2 weights), subset, ≤120KB total. Images: the theme needs
  none for its system; content plates ≤150KB each, lazy below the
  fold. JS for the full correction system ≤28KB gz (one loop, one
  observer, the slip scheduler). CSS ≤18KB gz. No canvas, no WebGL,
  no libraries beyond the shared loop utilities.
- **Frame budget.** The shared loop's total write cost ≤1.6ms/frame
  with a full viewport of slips (lag §6.11 ≤0.5ms, sheen §6.7
  ≤0.1ms, rolls §6.5 ≤0.3ms×3, pin/counter ≈0.2ms). Long tasks: none
  over 50ms; slip arming is staggered by the observer, never batched
  at load beyond the hero's three.
- **Cut order** (when the budget is exceeded, cut in this order and
  never skip a step): 1. Glue sheen (§6.7) — ambience first, always.
  2. Paste-brush stroke (§6.6) — slips paste without their brush.
  3. Slip-edge text reveal (§6.10) — slips arrive lettered.
  4. Slip-lag parallax (§6.11) — slips scroll in register.
  5. Corner-lift 3D → the opacity variant (§6.4). 6. The page-slip
  peel → the lift variant (§6.9). **Never cut:** the paste-overs
  themselves, the rolls' synchrony, the index accumulation's
  completeness, any fallback or watchdog, the reduced-motion
  variants. The never-cut list is the theme's honesty machinery;
  cutting it to save frames is precisely backwards.

## 15. Build-order checklist

1. Set the static corrected book first: leaf, cloth, Garamond
   composition, all data at corrected values, all slips present and
   flat at their §4 angles, index complete. Verify with JS off —
   this is the page; everything after is weather on it.
2. Add the superseded values beneath every slip and the index's 1:1
   correspondence; run gate tests 1–4 (§10) on the static build.
3. Token layer: palette (§2 incl. lamplight), type casting (§3),
   easings (§5).
4. The shared rAF loop (lerp 0.12) and the IntersectionObserver
   arming system; the 900ms watchdog before any animation.
5. Paste-overs (§6.2) with brush strokes (§6.6) and text reveals
   (§6.10); then the rolls (§6.5) and their synchrony check.
6. The apparatus: header counter (§6.14), margin pin (§6.3), index
   accumulation (§6.8) — wired to the same DOM count, verified by
   gate test 2.
7. The audit gestures: corner-lift (§6.4), press-flat re-stamp
   (§6.12), with focus twins for both.
8. The hero flutter (§6.1) and title page (§6.13); the table ruling
   (§6.15); the form with its live slip (§6.16).
9. The footer index composition (§6.17), the unissued page (§6.18),
   the page-slip transition (§6.9).
10. Ambience last: slip-lag (§6.11), then the sheen (§6.7) — in that
    order, and each behind the §14 cut order.
11. Reduced-motion pass: walk every element's variant; verify gate
    test 6 by reading the page with motion off and auditing a
    correction by keyboard alone.
12. Lamplight pass: `prefers-color-scheme: dark` values per §2;
    re-measure the red pairings on the dimmed papers.
13. Print stylesheet: slips at angles, index complete, pin/head per
    their print rulings.
14. Full gate (§10), blocking items first; the five-second test with
    a reader who has never seen the theme.
