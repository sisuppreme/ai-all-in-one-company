# 17. The Classifieds — Expanded (v1 + v2)

The site is the back page of the paper, promoted to the whole paper:
hundreds of tiny, dense, ruled advertisements, and the entire site is
discoverable the way a classifieds page is discoverable — by browsing
small print. Nothing on the page is large except the masthead. Nothing is
decorative except the reader's own highlighter. This document is the
complete build specification. Where it disagrees with the short library
entry, this document is the build target.

---

## 1. Concept & world

**The story.** Every newspaper ends the same way: page after page of
agate type, ruled into columns, where a bicycle, a job, a lost dog and a
bridge for sale all get exactly the same typographic dignity — a bold
two-word head, three lines of compressed copy, a price. The Classifieds
takes that page seriously as an interface. The site's listings are not
cards styled to *look* like ads; they are ads, set in agate, ruled into
real columns, flowing down one column and continuing at the top of the
next exactly as newsprint does. The visitor does not navigate this site.
They *read* it, the way a reader reads the back page at breakfast — and
the page remembers being read: a translucent marker band follows the
reading position down the columns, and every ad it passes keeps a faint
yellow wash forever, marked as seen. Attention is the site's only
currency and the highlighter is how it is spent, visibly.

**The mood.** Dense, dry, faintly comic, completely unhurried. The paper
is warm newsprint, the ink is ordinary rule black, and the single accent
is marker yellow — not a brand colour but a reader's tool, the
highlighter pen someone brought to the page. Density is the aesthetic:
white space is rationed like column inches, because on a real classifieds
page space costs money and nobody wastes it. The page should feel
*full* — full of other people's small, urgent, specific needs — and the
visitor's own listing, when they post one, joins that crowd at exactly
the same size. There are no heroes here. There is a masthead, an index,
and the small print.

**Best-fit sites and audiences.** Marketplaces and resale boards (where
every listing is genuinely the same shape: head, three lines, price);
job boards, especially local and trade boards; local directories and
community notice boards; rental listings; event and gig boards; any
catalogue whose items are numerous, comparable and text-first. The
audience is the browser-as-reader: people who enjoy scanning, who trust
density as a signal of abundance, who would rather read forty real ads
than admire four large ones.

**When NOT to use it.** Not for image-led commerce (fashion, food,
travel) — the theme rations photographs to thumbnail size inside ruled
boxes and will starve any product that sells by looking good. Not for
luxury or low-volume brands: three listings in this theme look like a
failed newspaper, not an exclusive one; the theme needs a crowd
(≥ 60 listings per page to hold the fiction; below that, use a different
theme). Not for content that needs emotional pacing — long-form stories,
manifestos, anything whose argument depends on whitespace and pause.
Not for dashboards or data tools: agate type is for reading, not for
monitoring. Not where listings differ wildly in shape (a marketplace
mixing jobs, houses and personals is fine — that *is* the classifieds;
a SaaS pricing page is not).

**The one law.** Every element on the page must be something that could
physically exist on the back page of a printed newspaper, or in the hand
of its reader. The columns, the rules, the index, the dog-ear, the
clippings tray: print. The highlighter, the wash, the lifted slip: the
reader's hand. Anything that is neither paper nor hand — a floating
glassmorphic panel, a gradient hero, a modal that fades in from nowhere
— breaks the world and is refused (§9).

---

## 2. Palette

Three anchors from the library entry, unchanged. Derived tokens are
labelled DERIVED and exist only to do jobs the anchors cannot (depth
under a lifted slip, the tray's shade, a fainter rule for skeleton
lines). No other colour may be introduced — in particular no second
accent: if something needs emphasis, it gets the marker, a rule, or
bold type, never a new hue.

| Token | Hex | Role | Usage ratio | Pairing & contrast |
|---|---|---|---|---|
| `--newsprint` | `#F0EBDD` | The sheet itself: page ground, ad ground, tray ground | ~78% of pixels | Ground for `--ink` text (≈14.1:1, AAA at agate sizes) |
| `--ink` | `#1F1E1A` | Rule black: all text, all column rules, masthead, index | ~19% of pixels | On `--newsprint` ≈14.1:1; on `--marker` ≈9.6:1 (AAA) |
| `--marker` | `#F2C230` | Marker yellow: highlighter band, washes, featured lift tint, the one accent | ~3% of pixels, hard cap | Decorative only — ≈1.5:1 against newsprint, so it never carries text alone; text over a full-strength marker fill stays `--ink` (≈9.6:1) |
| `--newsprint-deep` (DERIVED) | `#E3DCC8` | The sheet beneath: pinned-stage floor visible between gliding columns, tray interior, dog-ear underside | ~6% (inside the newsprint share) | Under `--ink` ≈11.8:1; used as ground, never as a text colour |
| `--newsprint-shade` (DERIVED) | `#D8D0B8` | Slip shadows' paper tone, skeleton block fill, disabled ad ground | ~2% | Ground only |
| `--ink-soft` (DERIVED) | `#55534A` | Secondary agate: datelines, "ads seen" line, photo captions, legal small print | ~2% of text | On `--newsprint` ≈6.9:1 (AA at all sizes, AAA at ≥14px) |
| `--rule-faint` (DERIVED) | `#B9B198` | Skeleton agate lines, un-drawn rule ghosts, hairlines inside the tray | <1% | Decorative structure only; never text, never an interactive boundary on its own |
| `--marker-wash` (DERIVED) | `rgba(242,194,48,.16)` | The permanent read-wash an ad keeps after the band passes (§6.3) | grows with reading | A tint over `--newsprint`; `--ink` text over it stays ≈13.4:1 |
| `--marker-hover` (DERIVED) | `rgba(242,194,48,.28)` | Hover wash (§6.7) | transient | Same pairing as `--marker-wash` |

**Pairing rules (hard).** (1) Text is `--ink` or `--ink-soft`, on
`--newsprint`, `--newsprint-deep`, a marker wash, or a full `--marker`
fill — no other text pairing exists. (2) `--marker` at full strength is
a *fill and a band*, never a text colour and never a border colour for
interactive elements (1.5:1 cannot signal a boundary). (3) Rules are
`--ink` at 1px (column rules), 2px (section/category rules) or 3px
(masthead rule); `--rule-faint` is only for skeleton ghosts. (4) The
marker ration: at any scroll position, full-strength `--marker` may
cover at most the band (§6.3), one shimmering ad (§6.10) and the three
lifted featured ads' tint (§6.1) — if a design needs more yellow, the
design is wrong, not the ration.

**Dark-mode behaviour.** There is no dark mode, and that is a ruling,
not an omission: newsprint does not invert. A "lamplight" variant is
permitted for night reading — `--newsprint` warms to `#E8E0CB`,
`--newsprint-deep` to `#D9D0B2`, ink and marker unchanged — applied by
an explicit reader toggle labelled "Lamplight" in the index, never by
`prefers-color-scheme` alone, because the sheet's identity is its paper
colour and an OS setting must not re-paper the page. Contrast figures
above hold within ±0.4 under lamplight.

---

## 3. Typography

Two faces, both from the library entry, no third face for any reason.

- **Libre Franklin** — the heads: masthead, category heads, ad heads,
  index entries, buttons, the progress line. Always set in tiny caps
  (uppercase, letterspaced) — the classifieds head voice. Weights: 600
  (ad heads), 800 (category heads, buttons), 900 (masthead only).
- **Newsreader** — the reading matter: ad body copy, descriptions,
  datelines, form help, legal lines. Its optical sizing is used
  (`opsz` auto): agate settings take the small optical cut, which is
  what makes 11–12px body type stay legible instead of turning to mush.

**The type scale.** The page's unit is the agate line: 1 agate =
14px of vertical rhythm (the traditional agate ≈ 5.5pt; here it is the
grid unit, §4). Sizes are few and rationed — a classifieds page has
never needed a display size.

| Role | Face / weight | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Masthead | Franklin 900, caps | 44px / 44px (28px <768px) | +0.01em | Once per page. Never any other 900 on the page |
| Sheet title / H1 | Franklin 800, caps | 20px / 24px | +0.04em | The page's name ("Situations Vacant", "The Whole Sheet") — set like a section banner, not a hero |
| Category head | Franklin 800, caps | 13px / 16px | +0.09em | Always paired with its 2px rule (§6.5 draws it); count follows in Newsreader italic |
| Ad head | Franklin 600, caps | 11.5px / 14px | +0.05em | Max 2 lines; the ad's whole pitch lives here — if it needs a third line it is two ads |
| Ad body (agate) | Newsreader 400 | 11.5px / 14px | 0 | Max 4 lines, then the ad ends — classifieds copy is cut, never scrolled-within |
| Dateline / meta | Newsreader 400 italic | 10.5px / 14px | 0 | `--ink-soft`; place + date, e.g. *Leeds, Tue.* |
| Index entry | Franklin 600, caps | 11px / 20px | +0.07em | One per line, count right-aligned in Newsreader tabular |
| Progress line | Newsreader 400 | 10.5px / 14px | 0 | `--ink-soft`; exact wording fixed by §6.4 |
| Button / action | Franklin 800, caps | 11px / 14px | +0.08em | Set as a classified head — a button is a tiny ad for the action |
| Form label | Franklin 600, caps | 10.5px / 14px | +0.07em | Above the field, never floating, never placeholder-only |
| Price / figure | Newsreader 600, tabular | 11.5px / 14px | 0 | Prices sit in the ad's last line, bold, never in marker yellow |

**Per-role rules.** *Display:* there is none, deliberately — the
largest thing after the masthead is a 20px banner; any design reaching
for a 40px headline inside the sheet has left the theme. *Heads:* caps
always, sentence case never; a head that wraps past its ration is
rewritten, not shrunk. *Body:* agate is the default size of the world;
body copy at 16px+ appears only on the post-an-ad form's help text and
the 404 page, where the reader has stopped browsing and started doing.
*Data:* all counts, prices and figures are tabular and set in
Newsreader, never Franklin — figures in a newspaper are read, not
shouted. *Italics* are Newsreader's own, reserved for datelines and the
index's asides; Franklin is never italicised (it has no true italic in
this system and synthetic oblique is a §9 failure).

**Density law.** Line-height inside the sheet is always 14px or a
multiple of it (the agate grid). An ad is 5–9 agate lines tall
(70–126px): head (1–2), body (2–4), meta + price (1), rule gaps (1).
Ads taller than 9 lines are split or cut. This law is what makes the
columns flow (§6.2) computable: the stage can fold a column of
known-height blocks without measuring surprises.

---

## 4. Layout language

**The sheet.** The page is one sheet of newsprint. On desktop it is set
in **three ruled columns** (each 300–340px, 1px `--ink` rules between
and around, 14px gutters inside the rules); the masthead spans the
sheet's full width above the columns; the category index is a fourth,
narrower column (200–220px) pinned at the sheet's left on ≥1200px, or a
pinned horizontal strip above the columns below that (§6.13). The
clippings tray is the sheet's foot: a full-width ruled band beneath the
columns where clipped ads accumulate (§6.17).

**The pinned stage.** The three content columns live on a pinned
multi-column stage (§6.2): the stage pins for ~300vh of scroll while
the reading position travels down column 1, folds to the top of
column 2, then column 3 — the physical path of reading a broadsheet
column layout, mechanised. The stage floor is `--newsprint-deep`, so
the gliding columns read as paper sliding over the sheet beneath.
Above and below the stage, the page is an ordinary document: masthead
and intro sheet first, then the stage, then post-an-ad and the tray.
The stage is an enhancement of that document, never a replacement for
it (§6.2 fallback).

**Spacing rhythm.** Everything is measured in agate (14px). Section
gaps are 3 agate (42px) with a 2px rule; category gaps inside a column
are 2 agate (28px); ad-to-ad gaps are 1 agate (14px) closed by the
next ad's head — there are no empty lines inside a column that are not
accounted for. Margins are rationed: the sheet's outer margin is 28px
on desktop, 14px on mobile — a newspaper's margin, not a website's.

**Density rules.** (1) A viewport of the sheet at any scroll position
shows at least 9 ads on desktop, at least 4 on mobile — if it shows
fewer, the layout has wasted column inches. (2) Photographs are
rationed to one per ad, ≤ 84×63px, inside a ruled box (§6.11); most
ads have none, as on a real back page. (3) No element may span two
columns except the masthead, category banners *within* the stage's
fold logic (§6.2), the tray, and the form. (4) The dog-ear: the sheet's
top-right corner carries a folded dog-ear (a 34px triangle of
`--newsprint-deep` with a 1px rule edge) — the page has been handled.
It is static, structural, and is the sheet's only ornament; it
parallaxes 4px against the columns as the fixed layer beneath (§5),
the single permitted piece of pure print character.

**Whitespace as material.** Whitespace in this theme is not emptiness,
it is *unsold column inches* — and it is therefore always framed: an
empty region appears only as a ruled blank (the skeleton, §6.12), a
house ad ("THIS SPACE TO LET — your ad here, 3 lines, from £4"), or
the tray waiting for clippings. Unframed white space is a §9 failure:
the reader must always be able to tell whether a gap is intentional
print or a loading error, and in this theme intentional print is
ruled and labelled.

---

## 5. Full motion system

One shared `requestAnimationFrame` loop drives everything scroll-linked
(the column fold, the highlighter band, the dog-ear parallax, the photo
scale-ins). Scroll position is lerped toward the target at **0.14** per
frame; all scrubbed values derive from the lerped position, never from
raw scroll events, so the sheet glides and never judders. Nothing in
this theme bounces, springs past its rest, or loops decoratively except
the two sanctioned ambient motions (§6.10).

**Named easings (the press sheet).**

| Token | Curve | Used by |
|---|---|---|
| `--ease-sweep` | `cubic-bezier(.6,.05,.2,1)` | The highlighter sweep (§6.1) — a hand accelerating across, easing onto the page |
| `--ease-lift` | `cubic-bezier(.2,.9,.25,1.15)` | Featured lift-off, slip lifts (§6.1, §6.9) — paper rising, one 15% overshoot, no more |
| `--ease-glide` | `cubic-bezier(.45,.05,.35,1)` | Column fold travel (§6.2) — the sheet sliding under the reader's eye |
| `--ease-rule` | `cubic-bezier(.7,0,.3,1)` | SVG rule draws (§6.5) — a ruler pulled steadily down the column |
| `--ease-snip` | `cubic-bezier(.85,0,.15,1)` | The clip flash (§6.8) — scissors: fast close, hard stop |
| `--ease-settle` | `cubic-bezier(.3,.7,.3,1)` | Washes, shimmers, counters' final digit — ink soaking in |

**Duration tokens.** `--dur-sweep` 1100ms · `--dur-lift` 450ms ·
`--dur-rule` 600ms · `--dur-tick` 700ms · `--dur-wash` 180ms ·
`--dur-snip` 250ms · `--dur-turn` 450ms · `--dur-fold` (per-column
travel, computed: 380ms per 100vh of stage, clamped 500–1400ms).

**Every motion term, in classified language.**

- **Scroll-triggered reveals** — ads do not "reveal"; they are *already
  printed*. What triggers on entry is the ruling (§6.5: rules draw as a
  column region enters) and the counters (§6.6). Content is never
  hidden awaiting a trigger — the sheet is printed before it is read.
- **Scroll-driven / scrubbed animation** — the theme's core: the column
  fold (§6.2) and the highlighter band (§6.3) are scrubbed 1:1 to
  lerped scroll across the pinned stage; reverse scroll reverses both,
  exactly.
- **Parallax** — two layers only: the dog-ear and stage floor
  (`--newsprint-deep`) sit beneath; the columns glide above at full
  rate; the ear drifts 4px against them. No ad ever parallaxes against
  another ad — small print must stay in register.
- **Pinned sections** — the stage (§6.2), and above it the masthead +
  index (§6.13). Two pins maximum, never nested.
- **Masked line reveals** — refused for text (agate copy is never
  masked; a reader must be able to read an ad the instant it exists).
  The one mask in the theme is the featured ads' marker-swath clip-path
  (§6.1): a clip shaped like a highlighter stroke, revealing the *wash*,
  not the words.
- **Blur-to-sharp reveals** — refused. Newsprint is never out of focus;
  blur reads as a misprint. (The single exception is none.)
- **Staggered reveals** — the entrance only: category heads rule-in
  staggered 60ms apart in reading order (§6.1), and skeleton lines fill
  line by line (§6.12). Nothing staggers on scroll — the page is
  printed, not performed.
- **Kinetic typography** — refused inside the sheet. Type does not move
  in a newspaper. The masthead is static; the only moving text is the
  progress line's changing figures (§6.4), which is data, not display.
- **Marquee** — one, and it is print-honest: the index strip on narrow
  screens scrolls its category names horizontally *only while being
  dragged or while the stage is idle > 6s*, at 24px/s, pausing on any
  touch. A decorative infinite marquee is a §9 failure.
- **Animated counters** — agate counters (§6.6): figures tick up in
  Newsreader tabular over `--dur-tick`, once, when the index enters.
- **Progress indicators** — the highlighter band itself (§6.3) plus the
  index progress line (§6.4). There is no progress bar; a bar would be
  furniture from another world (§1 law).
- **Image scale-in-frame** — ad photos (§6.11): scale 1.1→1 inside
  their ruled boxes, scrubbed to the band's approach.
- **Hover / magnetic / tilt micro-interactions** — hover is the wash
  (§6.7); tilt is the cut-out slip's ≤3° paper tilt (§6.9); magnetic
  effects are refused (paper does not attract the hand; the hand moves).
- **Custom cursor** — refused, standing rule. The system cursor is the
  reader's fingertip; nothing is drawn over it.
- **Skeleton loading** — ruled agate-line blanks (§6.12): the sheet
  before the ads are set.
- **Page transitions** — the sheet-turn (§6.12): the page turns over to
  a fresh classifieds sheet, rules redrawing, 450ms.
- **Ambient loops** — exactly two: the idle marker shimmer on the
  last-marked ad and the faint newsprint grain crawl (§6.10). Both are
  opacity-only, both pause off-screen and under `save-data`.
- **Reduced motion** — §6 variants per element; globally: no pin, one
  standard scrolling column, highlighter rendered as a static wash on
  the first screenful, counters at final figures, no shimmer, no grain.

---

## 6. Signature elements

Eighteen elements: the twelve signature elements of the library entry
(§6.1–§6.12) and six page-family elements (§6.13–§6.18). Every element
carries its full build spec and its v2 layers. Shared tokens (easings,
durations) are defined once in §5; colour tokens in §2.

### 6.1 Highlighter sweep + featured lift-off

- **What & why.** The page's entrance is the reader arriving: the full
  sheet lands printed, a marker band sweeps across it once, and the
  three ads the band marks lift off the page as cut-out featured
  stories. It teaches the theme's whole grammar in 1.6 seconds — the
  marker means *chosen*, a lift means *in the hand* — and then never
  happens again. The featured ads are not an editorial module bolted
  on; they are three ordinary listings the reader's hand has picked out
  of the small print, and they stay marked all session.
- **Structure.** The sheet is a normal document (§4). The band is a
  single absolutely-positioned `<div class="sweep-band">` (height 34px,
  `--marker` at 0.55 alpha, soft 6px feathered edges via linear-gradient,
  `pointer-events:none`, `aria-hidden`) inside the stage's coordinate
  space. Featured ads are ordinary `<article class="ad">` elements
  carrying `data-featured`; lifting adds `.is-lifted` (transform +
  `--shadow-slip`: `0 1px 2px rgba(31,30,26,.18), 0 10px 22px
  rgba(31,30,26,.16)`) and a marker-swath underlay (an `::after` at
  full `--marker`, clipped by the swath clip-path, z-below the text).
- **Motion spec.** Sheet lands (no fade — print is simply *there*).
  At t=250ms the band sweeps left→right across the first screenful over
  `--dur-sweep` (1100ms, `--ease-sweep`). Each featured ad lifts as the
  band's leading edge crosses its left edge: scale 1→1.03, shadow from
  none to `--shadow-slip`, over `--dur-lift` (450ms, `--ease-lift`),
  staggered by crossing order (≈150ms apart for the standard layout);
  the swath clip-path opens left→right in the same 450ms. Category
  heads rule-in (§6.5) staggered 60ms apart during the sweep.
- **Choreography timeline (v2).** t=0 sheet painted complete →
  t=250ms band enters at sheet left → t≈480ms band crosses featured
  ad 1 → ad 1 lifts (450ms) → t≈700ms ad 2 lifts → t≈920ms ad 3 lifts →
  t=1350ms band exits right, fades 150ms → t=1500ms band removed from
  DOM; featured ads remain lifted. Total ≈1.5s, once per page load,
  never on scroll, never on return visits within the session
  (`sessionStorage` flag — the reader has already arrived).
- **State matrix (v2).** *Rest (pre-sweep):* all ads flat, printed —
  desktop and touch identical. *Hover:* a lifted ad takes §6.9 slip
  tilt; a flat ad takes §6.7 wash. *Focus:* a featured ad's link shows
  the §11 focus rule (2px `--ink` outline offset 2px); focus never
  lifts or re-lifts. *Active:* §6.8 clip. *Scrolled-past:* featured
  ads keep their lift and swath permanently (state, not animation).
  *Disabled:* JS off or fallback fired → featured ads render flat with
  the swath printed statically at 0.35 alpha — marked, not lifted; that
  *is* the designed disabled state.
- **Content merge.** The three featured ads are real listings from the
  page's own data, chosen by the same "featured" flag the index count
  uses; the sweep marks the actual ads in place. Remove the motion and
  the page still says, in print, which three are featured.
- **Failure fallback.** A 1600ms watchdog from first paint: if the
  sweep has not completed (JS error, hidden tab, jank), the band is
  removed and featured ads snap to the disabled state above. No ad is
  ever left mid-lift.
- **Reduced-motion variant.** No sweep, no lift. Featured ads render
  with the static swath (0.35 alpha) and a 1px dashed `--ink` "clipped"
  edge on two sides — the print signal for *featured* without motion.
- **Breakpoints (v2).** ≥1200px: as specced, band crosses the full
  three-column screenful. 768–1199px: two columns; the band crosses
  both, featured ads are the first three in reading order regardless
  of column. <768px: one column; the sweep becomes vertical — the band
  travels down the first screenful (900ms) and lifts the three featured
  ads stacked in it; if fewer than three featured ads fit the first
  screenful, only those in view lift, the rest render with the static
  swath.
- **Edge cases & failure modes (v2).** *Slow network / late fonts:*
  the sweep waits for `document.fonts.ready` or 600ms, whichever first,
  so it never crosses text that then reflows. *Fewer than 3 featured
  ads:* the sweep still runs and lifts what exists; zero featured ads
  → no sweep at all (a band marking nothing is a lie). *Tab hidden
  mid-sweep:* the watchdog completes the state statically on return.
  *Scroll during sweep:* the sweep is confined to the first screenful
  and finishes regardless; scroll is never locked.
- **Accessibility spec (v2).** The band is `aria-hidden`; featured ads
  carry the word "Featured" in their meta line (*Featured · Leeds,
  Tue.*) so the distinction exists in text, not only in lift and
  colour. The sweep moves no focus and announces nothing. Contrast: ad
  text over the swath is `--ink` on `--marker` ≈9.6:1. Touch targets:
  featured ads' links are the same agate links as all ads (§6.15) —
  the lift does not change target geometry.
- **Performance budget & mobile variant.** One transform on the band +
  three transforms/box-shadows: ≤0.4ms/frame. Box-shadow animation is
  confined to the 450ms lifts; shadows are pre-rendered as a static
  layer toggled by class where the engine allows. Mobile variant: the
  vertical sweep above; shadow blur halved (11px) for GPU cost.
- **Tokens consumed (v2).** `--newsprint`, `--ink`, `--marker`,
  `--shadow-slip`, `--ease-sweep`, `--ease-lift`, `--dur-sweep`,
  `--dur-lift`.

### 6.2 Columnar scroll flow

- **What & why.** The theme's engine. Reading a broadsheet means
  travelling down one column and continuing at the top of the next;
  the stage mechanises exactly that path. Scrolling does not move the
  page up — it moves the *reading position* through folded columns,
  so the visitor experiences the listings as one continuous column of
  small print that happens to be folded twice across the sheet. This
  is what makes the theme a place rather than a list: you are always
  somewhere *in* the paper, and the index (§6.4) can say where.
- **Structure.** `<section class="stage">` with a scroll length of
  ~300vh containing a sticky stage frame (100vh). Inside, a
  `.columns-track` holds the three columns side by side on the
  `--newsprint-deep` floor. The track's translate is a function of
  lerped stage progress (§5): progress 0→⅓ reads column 1 (track
  shifts the reading window down column 1's length), ⅓→⅔ folds to
  column 2's top and reads down it, ⅔→1 column 3. Implementation is a
  single transform on the track plus a per-column inner translate;
  the DOM order is strictly column 1 → 2 → 3, which is also the
  reading order, the tab order, and the no-JS order.
- **Motion spec.** Continuous scrub, 1:1 with lerped scroll
  (lerp 0.14). The fold itself — the jump from a column's foot to the
  next column's head — is eased over the middle 12% of each third
  (`--ease-glide`), so the eye is carried across the fold rather than
  teleported; within a column, movement is linear with scroll (the
  reader's eye moves at reading speed). Column rules and the dog-ear
  parallax against the track at 4px total drift (§4).
- **Choreography timeline (v2).** Stage progress p (lerped): p=0
  masthead of stage + column 1 head at the reading line → p=0.29
  column 1 foot approaches → p=0.29–0.375 fold window: track eases to
  column 2 head → p=0.375–0.62 column 2 reads → p=0.62–0.71 fold to
  column 3 → p=0.71–1 column 3 reads to its foot, where the stage
  unpins and the document continues to the form and tray. The
  highlighter band (§6.3) and progress line (§6.4) read the same p.
- **State matrix (v2).** *Rest:* p=0, column 1 head at the line.
  *Hover/focus:* unaffected by the flow — an ad under the pointer keeps
  its §6.7/§6.9 states wherever the fold has carried it; focus on an
  ad outside the current reading window scrolls the stage to it
  (native `scrollIntoView` is intercepted and mapped to stage
  progress, never fought). *Active:* §6.8. *Scrolled-past:* columns
  already read keep their §6.3 washes; the flow does not reset them.
  *Disabled:* pin unsupported or fallback fired → the stage unpins
  into the ordinary three-column document (§4), read top-to-bottom.
  Touch: identical mapping; the fold is driven by the same lerp, and a
  fast flick decays through the fold window without skipping a column
  head (progress clamps at fold boundaries until velocity < 0.4).
- **Content merge.** The columns are the layout, not a viewport onto
  other content: the ads, category heads and rules that fold are the
  page's actual listings in their actual order. The stage adds a
  reading path to a document that remains complete without it.
- **Failure fallback.** The library entry's law, made mechanical: a
  1000ms watchdog after stage entry — if the pin has not engaged
  (unsupported `position: sticky` in the required form, JS error,
  `prefers-reduced-motion`, or an iframe/embed context), the stage
  unpins permanently for the session and the document reads as a
  normal three-column page. No ad can be stranded off-stage: the
  unpinned document contains every ad in reading order.
- **Reduced-motion variant.** No pin, no fold. One standard scrolling
  column on <1200px, the static three-column document on ≥1200px;
  reading is ordinary vertical scroll; the highlighter is §6.3's
  static variant.
- **Breakpoints (v2).** ≥1200px: three columns + index column, stage
  300vh. 768–1199px: two columns, stage 260vh, folds recomputed as
  halves (p windows scale: fold windows at 0.44–0.56). <768px: one
  column — **the fold is not performed**; a single column folded onto
  itself is just scrolling with extra machinery, so the stage becomes
  a normal document column and §§6.3–6.4 degrade to their mobile
  variants. This is a designed absence, stated here so no builder
  "fixes" it.
- **Edge cases & failure modes (v2).** *Content shorter than the
  stage:* if total column content is < 2.2× viewport height, the stage
  length shrinks proportionally (min 160vh) — a stage that scrolls
  past its own content is a §10 failure. *Content much longer:*
  columns are balanced to within one ad of each other at build time;
  an unbalanced feed is rebalanced by moving whole ads, never by
  splitting one. *Scroll back up:* the fold reverses exactly; washes
  (§6.3) persist, positions restore — there is no "unreading".
  *Resize mid-stage:* progress p is preserved, geometry recomputed
  from p, never from pixel offsets. *Find-in-page:* matches in folded
  columns trigger the same progress-mapping as focus.
- **Accessibility spec (v2).** The stage is a `<section
  aria-label="Classified listings">`; columns are three `<div
  role="group" aria-label="Column 1 of 3">` etc. in DOM reading order.
  Keyboard: tab order follows the DOM (column 1 fully, then 2, then
  3) — the fold follows focus, so a keyboard reader experiences the
  same path as a scroller. The stage never traps scroll: at p=1 the
  document continues natively. A visually-hidden status line mirrors
  §6.4's progress text for screen readers, updated at fold crossings
  only (not per frame).
- **Performance budget & mobile variant.** One transform per frame on
  the track + one on the band (§6.3): the cheapest pinned stage in the
  library. No per-ad transforms during the fold (ads ride the track).
  Frame budget ≤0.6ms of theme code. Mobile variant: no stage at all
  (above) — zero cost.
- **Tokens consumed (v2).** `--newsprint`, `--newsprint-deep`,
  `--ink`, `--ease-glide`, `--dur-fold`, stage length token
  `--stage-h` (300vh / 260vh by breakpoint).

### 6.3 Scrubbing highlighter band

- **What & why.** The reader's hand, made visible. A translucent
  marker band rides at the reading position inside the columns, and
  every ad it fully passes keeps a permanent faint wash — *marked as
  read*. The page accumulates the visitor's attention the way a real
  back page accumulates pencil ticks and coffee rings, and the
  accumulation is the theme's memory: come back to a section and you
  can see what you have already read. It is also the progress
  indicator (§5): where the band is, is where you are.
- **Structure.** `<div class="hl-band">` (height 30px ≈ 2 agate lines +
  headroom, `--marker` at 0.38 alpha, feathered top/bottom edges,
  `pointer-events:none`, `aria-hidden`) positioned inside the stage
  frame, its vertical position driven by the same lerped progress as
  §6.2. The permanent wash is a class on the ad (`.is-read`) applying
  `--marker-wash` background via a background-size transition so the
  wash soaks downward, never a layout change.
- **Motion spec.** The band scrubs 1:1 with lerped progress within
  the current column, and crosses folds with the track (§6.2 fold
  windows). An ad gains `.is-read` when the band's lower edge passes
  the ad's foot; the wash soaks in over 300ms (`--ease-settle`). The
  band never moves under its own power — no auto-scroll, no idle
  drift; it is exactly where reading has reached.
- **Choreography timeline (v2).** Continuous: band top = reading line
  for current p → ad foot crosses band bottom → t+0 wash begins →
  t+300ms wash at full `--marker-wash` → §6.4's "ads seen" increments
  at t+150ms (mid-soak, so the count and the colour agree to the eye).
  On a fold, the band rides the track across (same 12% window) and
  resumes at the next column's head.
- **State matrix (v2).** *Rest:* band at column 1 head, no washes.
  *Hover:* §6.7's stronger wash supersedes on the hovered ad only.
  *Focus:* focusing an unread ad does not mark it read (focus is not
  reading); focusing does move the band if the focus-mapping of §6.2
  scrolls to it — the band follows position, and position is what
  marks. *Active:* §6.8. *Scrolled-past:* washes persist for the
  session; they are the state. *Disabled:* JS off → no band, no
  washes; the page is simply an unread newspaper, complete.
  Touch: identical; there is no touch-specific band behaviour.
- **Content merge.** The wash is applied to the ad element itself and
  the band sits inside the column it is reading. Nothing floats above
  unrelated content: the band is 30px tall, inside the ruled column,
  over the ad currently being read.
- **Failure fallback.** If the stage is unpinned (§6.2 fallback), the
  band degrades to document flow: an `IntersectionObserver` marks ads
  read as they pass the viewport's middle third, same wash, same
  counter. If IO is unavailable, no band and no washes — content
  untouched.
- **Reduced-motion variant.** No travelling band. The first screenful
  of ads renders pre-washed (the reader has "started" the page) and
  further ads wash instantly (no soak) as they enter the viewport's
  middle third. The read/unread distinction survives; the hand does
  not move.
- **Breakpoints (v2).** ≥1200px and 768–1199px: as specced, band
  width = current column width − 8px (it stays inside the rules).
  <768px: no stage (§6.2), so the band is IO-driven in the single
  column, width = column − 8px; the soak shortens to 200ms (smaller
  screens, quicker eye).
- **Edge cases & failure modes (v2).** *Fast scroll to the foot:*
  every passed ad still washes — the band travels the whole path in
  the lerp, and wash application is batched per frame (≤ 12 ads per
  frame) so a jump cannot jank. *Scroll back up:* washes never
  un-wash; the band returns to the reading line. *Very tall ads:*
  an ad is read when its foot passes, however long it is (ads are
  capped at 9 lines by §3, so this is bounded). *Session restore:*
  washes are session-only; a new visit starts with a clean page —
  yesterday's newspaper is not today's.
- **Accessibility spec (v2).** `aria-hidden` band; read state is not
  conveyed by colour alone — read ads gain a 3px marker tick in their
  left rule (a small filled notch, part of `.is-read`) and the index
  line (§6.4) states the count in text. Screen readers get the count,
  not the colour. The wash keeps text contrast ≥13.4:1 (§2).
- **Performance budget & mobile variant.** One transform + batched
  class changes; ≤0.3ms/frame. The wash transition is background-only.
  Mobile: IO variant above; no continuous transform at all.
- **Tokens consumed (v2).** `--marker`, `--marker-wash`, `--ink`,
  `--ease-settle`, lerp shared with §6.2.

---

### 6.4 Index progress line

- **What & why.** The pinned category index carries one tiny line of
  Newsreader — *"column 2 of 3 · ads seen 47"* — that updates as the
  band crosses columns and ads. It is the theme's entire progress UI:
  no bar, no percentage, no spinner, just the finding aid reporting
  on its own page in the page's own type. It exists because the folded
  stage (§6.2) removes the scrollbar's usual story, and a reader of
  small print deserves to know where in the paper they are.
- **Structure.** A `<p class="index-progress">` inside the pinned
  index (§6.13), 10.5px Newsreader `--ink-soft`, tabular figures. The
  two numbers are `<output>` elements updated by the shared loop at
  most once per 120ms (throttled — the line is read, not watched).
  Column count in the string is the live column count (3 / 2 / 1 by
  breakpoint), never hardcoded.
- **Motion spec.** No motion of its own: figures change discretely.
  The "ads seen" figure changes in step with §6.3's wash (mid-soak,
  §6.3 timeline). The column figure changes at fold crossings. A
  120ms `--ease-settle` opacity settle (1→0.55→1) on the changed
  figure only — a blink of fresh ink, nothing more.
- **Choreography timeline (v2).** Band crosses ad foot → t+150ms
  count +1 with the 120ms settle → fold window opens → at fold
  midpoint the column figure changes with the same settle → line is
  never more than 300ms behind the eye.
- **State matrix (v2).** *Rest:* "column 1 of 3 · ads seen 0".
  *Hover/focus:* none (the line is not interactive). *Active:* n/a.
  *Scrolled-past (stage exited):* the line freezes at its final
  figures — "column 3 of 3 · ads seen 212" — a completed reading,
  left on the index like a pencilled total. *Disabled:* JS off → the
  line renders its static form: "212 ads on this sheet" (the total,
  known at build time). Touch: identical.
- **Content merge.** The line lives inside the index it describes and
  counts the index's own listings. It is the page counting itself, in
  the margin where a reader would pencil the same tally.
- **Failure fallback.** Static total (above). If the stage unpins,
  the line counts via the §6.3 IO fallback with identical wording.
- **Reduced-motion variant.** Identical, minus the 120ms settle —
  figures simply change. (The line was never the motion.)
- **Breakpoints (v2).** ≥1200px: in the index column. 768–1199px:
  "column n of 2". <768px: the stage is gone; the line moves into the
  pinned index strip (§6.13) and reads "ads seen n" only — a single
  column has no column number worth printing.
- **Edge cases & failure modes (v2).** *Ads clipped mid-reading
  (§6.8):* a clipped ad still counts as seen if it was washed; the
  total on the sheet decrements only in the static total on reload —
  the line never runs backwards within a session. *Duplicate IDs /
  re-rendered lists:* the counter counts DOM ads, not data rows, so
  what is counted is what is printed. *Zero ads:* the line reads
  "no ads today" (the §12 empty voice) and the stage does not pin.
- **Accessibility spec (v2).** The visible line is `aria-hidden`
  (it changes too often to announce); the §6.2 visually-hidden status
  line announces column changes and every 25th ad ("Column 2 of 3.
  50 ads seen.") — progress at a reader's pace, not a ticker's.
- **Performance budget & mobile variant.** Two text writes ≤ 8×/s:
  negligible. Mobile: the shortened form above.
- **Tokens consumed (v2).** `--ink-soft`, `--ease-settle`.

### 6.5 Self-ruling columns

- **What & why.** The column rules are the sheet's skeleton, and they
  are drawn, not placed: as each column region enters, its rules
  stroke themselves down the page in 600ms, top to bottom, the way a
  compositor rules a page before setting the type. It is the theme's
  one structural flourish, and it earns its place because the rules
  *are* the layout — watching them draw is watching the page become a
  page. Category heads' 2px rules draw with them.
- **Structure.** Rules are SVG: one `<svg class="rules">` per column
  region, absolutely positioned over the column box, containing the
  vertical rules as `<line>`/`<path>` with `pathLength=100` and
  dash-offset animation, plus the category rules as horizontal paths.
  The printed (final) state is dash-offset 0. Without JS the SVG is
  rendered fully drawn — the draw is an enhancement layered on a
  complete page.
- **Motion spec.** Trigger: column region's head crosses 85% viewport
  height (or stage progress reaches it). Vertical rules draw over
  `--dur-rule` (600ms, `--ease-rule`), both rules of a column
  simultaneously (they are one gesture); the category 2px rule draws
  left→right in 300ms as its head lands. Once drawn, a rule never
  redraws within the session.
- **Choreography timeline (v2).** Region enters → t=0 verticals begin
  → t=600ms verticals complete → category heads inside the region
  draw their rules at their own entry beats (300ms each, staggered
  60ms if several enter together, §6.1). On the pinned stage, draws
  are keyed to stage progress so a fold never shows an undrawn rule:
  columns 2 and 3 pre-draw during the fold window that reveals them.
- **State matrix (v2).** *Rest:* undrawn ghost (`--rule-faint` at
  40%) — visible structure, so layout never shifts. *Drawing:* the
  600ms stroke. *Drawn:* full `--ink` 1px, permanent. *Hover/focus:*
  none. *Scrolled-past:* drawn, static. *Disabled:* fully drawn from
  first paint (the ghost *is* replaced by the real rule in the no-JS
  render). Touch: identical.
- **Content merge.** The rules drawn are the actual column boundaries
  the ads sit between. The animation decorates nothing; it constructs
  the grid in view of the reader.
- **Failure fallback.** Ghost rules are real borders' understudies:
  if the SVG fails or JS is off, columns carry ordinary CSS 1px
  `--ink` borders — identical final geometry. A 900ms watchdog
  force-completes any draw interrupted mid-stroke.
- **Reduced-motion variant.** Rules render drawn. No ghost, no stroke.
- **Breakpoints (v2).** ≥1200px: three columns + index rule set.
  768–1199px: two columns. <768px: one column — the draw becomes a
  single left rule per category region (the column's outer rules are
  the screen edge's business), 400ms.
- **Edge cases & failure modes (v2).** *Long columns:* the draw is
  per *region* (a category block, ~1–2 viewports), never one 600ms
  stroke down a 9-viewport column — the stroke speed stays a ruler's
  speed, not a zipper's. *Reflow on resize:* drawn rules stay drawn;
  geometry recomputed, dash state preserved. *Print:* `@media print`
  renders all rules solid (the theme's final proof, §10).
- **Accessibility spec (v2).** Purely decorative structure:
  `aria-hidden`, no role, no focus. Contrast of the drawn rule
  (≈14.1:1) far exceeds the 3:1 non-text minimum; the ghost state is
  never the only carrier of structure because ads are grouped by
  headed categories in the DOM regardless.
- **Performance budget & mobile variant.** SVG strokes on ≤ 8 paths
  per region, transform/dash only: ≤0.3ms/frame during a draw, zero
  at rest. Mobile: the single-rule variant above.
- **Tokens consumed (v2).** `--ink`, `--rule-faint`, `--ease-rule`,
  `--dur-rule`.

### 6.6 Agate counters

- **What & why.** "ADS TODAY 212" in the masthead's dateline row, and
  a count beside every category in the index — the paper enumerating
  itself. When the index first enters, the figures tick up in tiny
  agate numerals over 700ms, the way a mechanical counter settles.
  They exist because abundance is this theme's argument (§1) and the
  argument should be countable, in the paper's own type size — not a
  marketing number in display type, which would break the world.
- **Structure.** `<span class="count" data-count="212">` in Newsreader
  tabular 600. Category counts sit right-aligned on the index entry's
  line (§3). All figures are rendered server-side at final value in
  the HTML; the tick-up is a JS recount starting from the *previous
  edition's* count where the data provides one, else from the final
  figure minus 12% (rounded) — the point is the settle, not a count
  from zero, which would fabricate a moment when the paper had no ads.
- **Motion spec.** Trigger: the index (or masthead row) enters at 80%
  viewport. Figures step in 8–12 discrete tabular steps over
  `--dur-tick` (700ms, `--ease-settle` on the last step only), upward
  only, landing exactly on the true figure. Once per session per
  counter.
- **Choreography timeline (v2).** Index enters → t=0 all its counts
  begin together (a counter bank settling, not a cascade) → steps at
  ~70ms intervals → t=700ms all landed. The masthead "ads today"
  counter runs with the entrance (§6.1), offset +200ms.
- **State matrix (v2).** *Rest:* final figures (the no-JS truth).
  *Counting:* the 700ms settle. *Hover/focus:* none — counts are
  text. *Scrolled-past:* final figures, static. *Disabled:* final
  figures from first paint. Touch: identical.
- **Content merge.** Every figure counts listings actually on the
  sheet (or, for "ads today", actually in today's edition feed) —
  the §10 truth audit applies: one invented figure fails the build.
- **Failure fallback.** Final figures are the HTML default; any JS
  failure leaves the truth on the page. A counter interrupted
  mid-tick snaps to final (watchdog 900ms).
- **Reduced-motion variant.** Final figures, no tick.
- **Breakpoints (v2).** All sizes identical; on <768px the masthead
  counter moves under the masthead rule (the dateline row wraps), same
  behaviour.
- **Edge cases & failure modes (v2).** *Count of 0:* no tick; the
  category shows "—" and the §12 empty line. *Live updates mid-
  session* (a new ad posted): the affected category count +1s with a
  single 120ms settle (§6.4's gesture), never a re-tick. *Huge
  counts:* tabular figures, thin-space thousands separators
  ("1 204"), never rounded — a classifieds count is exact or absent.
- **Accessibility spec (v2).** Counters are plain text in reading
  order; the tick is `aria-hidden` on a duplicate span with the final
  figure in the accessible text — screen readers hear the truth once,
  not twelve stepping numbers. Contrast: `--ink` on `--newsprint`.
- **Performance budget & mobile variant.** ≤ 20 counters × 12 text
  writes, once: negligible. No mobile difference.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--ease-settle`,
  `--dur-tick`.

---

### 6.7 Highlighter-wash hover

- **What & why.** Hovering an ad washes it with the marker at hover
  strength — the reader's hand hovering over a listing, interested.
  It is the theme's only hover language for un-lifted ads, and its
  restraint is the point: no lift, no border change, no shadow — just
  the wash deepening, because on paper, interest is a highlighter
  pausing, not the ad jumping up.
- **Structure.** The ad's background transitions between its read
  state (transparent or `--marker-wash` if §6.3 has passed) and
  `--marker-hover` (0.28 alpha). Implemented as a background-color
  transition on the `<article class="ad">` itself; the wash sits
  behind the text (z-0), text unchanged.
- **Motion spec.** Wash in over `--dur-wash` (180ms, `--ease-settle`)
  on pointerenter; wash out over 240ms on leave (ink lingers a beat
  longer leaving than arriving — a marker lifts slowly). On a read ad,
  hover deepens from 0.16 to 0.28; on an unread ad, from 0 to 0.28.
- **Choreography timeline (v2).** Pointer enters → t=0 wash begins →
  t=180ms full hover strength → pointer leaves → t=240ms back to base
  state. No other element participates.
- **State matrix (v2).** *Rest:* base wash state. *Hover:* as specced.
  *Focus:* keyboard focus applies the same wash **plus** the §11
  focus outline (wash alone is not a focus indicator — 1.5:1 cannot
  be). *Active:* the wash holds through the click; §6.8's flash
  follows. *Scrolled-past:* unchanged. *Disabled:* n/a — hover is an
  enhancement; the ad is fully usable without it. *Touch:* no hover;
  the first tap on an ad's body applies the wash and the second tap
  follows the ad's link (the standard two-step for hover-dependent
  print), except the clip button (§6.8), which acts on first tap.
- **Content merge.** The wash is on the ad, in the reader's colour,
  at the reader's initiative. It is the same substance as §6.3's read
  wash, one strength up — a single material for attention at two
  intensities.
- **Failure fallback.** None needed: no wash, no loss. The ad's head,
  body and link are untouched by the mechanism.
- **Reduced-motion variant.** The wash applies instantly (no 180ms
  soak) — a state, not a motion.
- **Breakpoints (v2).** Identical at all sizes; on <768px the touch
  two-step above replaces hover entirely.
- **Edge cases & failure modes (v2).** *Pointer sweeping down a
  column:* washes trail the pointer by design; enter/leave are
  debounced 40ms so a fast pass doesn't flicker the column like a
  strobe. *Hover during the fold (§6.2):* the hovered ad keeps its
  wash while riding the track — hover state belongs to the ad, not
  the viewport. *Sticky hover on touch browsers:* cleared on
  scroll-start.
- **Accessibility spec (v2).** Hover conveys nothing exclusively —
  every hovered ad's content and link are identical unhovered. Focus
  visible: 2px `--ink` outline, offset 2px, on the ad's link, plus
  the wash. Contrast of text over `--marker-hover`: ≈12.6:1.
- **Performance budget & mobile variant.** One background transition;
  zero loop cost. Mobile: the two-step tap above.
- **Tokens consumed (v2).** `--marker-hover`, `--marker-wash`,
  `--dur-wash`, `--ease-settle`.

### 6.8 Clip-the-ad click

- **What & why.** Readers cut ads out of newspapers. Clicking an ad's
  clip control runs a scissors-snip flash around its border and lifts
  the ad out of the column into the clippings tray at the page foot
  (§6.17), where the reader's clippings accumulate. It is the theme's
  save/bookmark, and it is honest about what saving *is* here: the ad
  leaves the page (its column space closes up with a house-ad slip,
  §4) and lives in the tray as a cut-out slip (§6.9). A real state
  change in the layout, not a heart icon filling in.
- **Structure.** Every ad carries a `<button class="clip-btn">` —
  a small caps Franklin label "CLIP" with a scissors glyph (SVG,
  10px) in its meta line. On clip: an SVG dashed rect (`.snip-edge`)
  draws around the ad's border; the ad becomes a `.slip` (§6.9),
  animates to the tray; a `<aside class="house-ad">` ("THIS SPACE TO
  LET") of identical height takes its column place so the column
  never collapses mid-read. The tray (§6.17) is the single source of
  truth: clipped IDs persist in `sessionStorage`; unclipping from the
  tray reverses the whole path.
- **Motion spec.** Snip: dashed line draws around the border over
  `--dur-snip` (250ms, `--ease-snip`), dash 6px/4px, `--ink`. Lift:
  the slip scales 1.02, gains `--shadow-slip`, rotates −0.6°, over
  200ms (`--ease-lift`). Travel: the slip translates to the tray's
  position over 550ms (`--ease-glide`), shrinking to tray scale
  (0.92), then settles with a 120ms paper settle (rotate → its tray
  rotation, §6.9). The house-ad slip fades its print in over 300ms
  behind the departing slip. Total ≈950ms; the column is never
  scroll-jacked — the reader's place is held by the house ad.
- **Choreography timeline (v2).** Click → t=0 snip begins →
  t=250ms snip completes, lift begins → t=450ms slip free, house ad
  printing beneath → t=450–1000ms travel to tray → t=1000ms settle,
  tray count +1 with §6.4's 120ms settle → the tray's tab pulses
  once (opacity, 300ms) if the tray is off-screen.
- **State matrix (v2).** *Rest:* "CLIP" button at rest weight.
  *Hover:* the button's label takes the §6.7 wash; the ad does not
  pre-lift. *Focus:* §11 focus outline on the button. *Active:*
  the snip (above). *Clipped (resting state in tray):* the slip
  shows "UNCLIP" on its tray hover/focus. *Disabled:* the button is
  a real `<button>`; with JS off it submits a form fallback
  (server-side save list) — clipping works without the theatre.
  *Touch:* first-tap acts (no two-step; the button is unambiguous).
- **Content merge.** Clipping operates on the ad itself and moves
  the ad itself. The tray at the foot holds the reader's actual
  clippings, in clip order, readable in full — the feature *is* the
  content, rearranged by hand.
- **Failure fallback.** If the travel animation is interrupted (tab
  switch, reduced data), the state change completes instantly: the
  slip is in the tray, the house ad is in the column. State first,
  theatre second — a 900ms watchdog enforces the end state.
- **Reduced-motion variant.** No snip draw, no travel: the ad is
  replaced by the house ad and appears in the tray, both instantly,
  with the tray count updated. The scissors glyph remains as the
  button's print mark.
- **Breakpoints (v2).** ≥1200px / 768–1199px: as specced; the tray is
  at the sheet foot, so travel distance varies — travel duration
  scales 450–700ms by distance, capped. <768px: the tray is a pinned
  bottom strip (§6.17); the slip travels the shorter distance
  (350ms) and the strip's count updates in place.
- **Edge cases & failure modes (v2).** *Clipping a featured (lifted)
  ad:* it clips from its lifted state; its featured place in the
  column is taken by the house ad and the featured count in the index
  decrements (§6.6 live-update rule). *Clipping everything:* the
  column becomes house ads — permitted, and the tray footer (§6.17)
  offers "Return all clippings" — the reader has taken the page home.
  *Double-click:* the second click lands on the house ad, which has
  no clip button; no race. *Tray full:* the tray holds all clippings
  in a wrapped slip row; beyond 24, slips stack in a neat pile
  (offset 2px each) with a "+n more in the tray" line — never a
  scroll-trap.
- **Accessibility spec (v2).** The button's accessible name is
  "Clip this ad: [ad head]" — never bare "CLIP". A polite live region
  announces "Clipped: [head]. 3 clippings in the tray." Focus moves
  to the house ad's "clipped — in tray" note after a clip (the
  reader's place is preserved, §4), and to the slip on unclip.
  Touch target: the button is 28px tall within the ad's meta line —
  below the 44px ideal, so the *whole meta line* is the button's hit
  area (44px effective via padding into the ad's own box, never
  overlapping the next ad).
- **Performance budget & mobile variant.** One ad's transform +
  one SVG draw per clip; nothing loops. Mobile: shorter travel
  (above); shadow blur halved.
- **Tokens consumed (v2).** `--ink`, `--marker`, `--shadow-slip`,
  `--ease-snip`, `--ease-lift`, `--ease-glide`, `--dur-snip`.

### 6.9 Cut-out slip tilt

- **What & why.** A lifted ad — featured (§6.1) or clipped (§6.8) —
  is a piece of cut paper in the reader's hand, and it behaves like
  one: hovering tilts it up to 3° toward the pointer's quadrant, its
  shadow softening as it rises. The tilt is the theme's only
  pointer-physics, rationed to slips because only slips are *held*;
  flat ads in the column never tilt (paper still in the sheet does
  not lean).
- **Structure.** `.slip` elements carry a pointer handler writing
  `--tilt-x`/`--tilt-y` custom properties; the transform is
  `perspective(700px) rotateX(var) rotateY(var)` composed with the
  slip's resting rotation (`--slip-rot`, set per slip between −1.2°
  and +1.2° at clip time — no two clippings in the tray sit at the
  same angle, like real cuttings on a corkboard). Shadow scales with
  tilt magnitude via the same properties.
- **Motion spec.** Tilt follows the pointer with the shared lerp
  (0.18 for slips — slightly looser than scroll, paper lags the hand
  a fraction). Max 3° per axis by pointer quadrant within the slip.
  On leave, the slip settles back to `--slip-rot` over 350ms
  (`--ease-settle`) with a 4% overshoot of rotation only — paper
  rocking once on the board.
- **Choreography timeline (v2).** Pointer moves → each frame, target
  tilt recomputed from quadrant → lerped tilt approaches (63% in
  ~90ms) → pointer leaves → t=0 settle begins → t=350ms at rest
  rotation, shadow at rest depth.
- **State matrix (v2).** *Rest:* `--slip-rot`, rest shadow.
  *Hover:* tilt as specced. *Focus:* a focused slip straightens to
  0° and takes the §11 outline — focus is reading, not holding.
  *Active:* §6.8's press (scale 0.99, 100ms) if the slip's button is
  pressed. *Scrolled-past:* slips in the tray are below the stage;
  their state is rest. *Disabled:* no pointer handler (touch, JS
  off) → slips sit at `--slip-rot`, complete. *Touch:* tilt is not
  offered; a slip's tap is its button or link, first-tap (§6.7's
  two-step does not apply to slips — they are already "in hand").
- **Content merge.** Only ads the reader (or the entrance sweep) has
  physically lifted can tilt. The physics is a property of the
  object's state in the fiction, not a site-wide hover effect.
- **Failure fallback.** No handler → static slips at their resting
  rotations. Nothing is hidden or moved by the fallback.
- **Reduced-motion variant.** No tilt, no settle: slips sit at
  `--slip-rot` (rotation is a state, not a motion, and a corkboard of
  clippings at slight angles is the tray's printed look).
- **Breakpoints (v2).** ≥1200px / 768–1199px: as specced. <768px:
  tilt disabled (touch-first context; a slip under a thumb must not
  squirm) — resting rotations remain.
- **Edge cases & failure modes (v2).** *Pointer crossing slips
  quickly:* each slip's lerp is independent; a slip left mid-tilt
  always completes its 350ms settle — no slip is ever abandoned at
  an angle it didn't choose. *Tray pile (>24 clips, §6.8):* piled
  slips don't tilt (they're under other paper). *Device orientation
  / gyro:* never used — tilt is pointer-only, by rule.
- **Accessibility spec (v2).** Tilt is decorative and `aria-hidden`
  in effect (transform only); it never moves a focus outline away
  from its element (outline follows the element's box). Slips remain
  fully readable at 3° — the cap exists precisely so agate text
  never becomes hard to read.
- **Performance budget & mobile variant.** ≤ 6 slips tilting
  concurrently in practice; one transform each, ≤0.2ms/frame total.
  Mobile: disabled (above), zero cost.
- **Tokens consumed (v2).** `--shadow-slip`, `--slip-rot` (per-slip),
  `--ease-settle`, `--ease-lift`.

---

### 6.10 Idle marker shimmer + newsprint grain

- **What & why.** The page's two ambient motions, and its only ones.
  The marker shimmer: a soft pulse of yellow light idling on the ad
  the reader last marked — attention lingering where the hand
  stopped. The grain: newsprint fibre texture crawling almost
  imperceptibly across the sheet, so the paper feels like paper and
  not like a screenshot of paper. Both are opacity-only, both are
  quieter than anything else on the page, and both exist to keep the
  sheet *material* during long reads.
- **Structure.** Shimmer: an `::after` on the `.is-current` ad (the
  last ad the band passed or the pointer last washed), a radial
  `--marker` gradient at 0→0.18 alpha, animated opacity 0.6→1→0.6.
  Grain: a fixed full-sheet layer with an SVG feTurbulence noise
  texture (tile 180×180px, opacity 0.05), translated 1px steps in a
  slow loop — a crawl, not a drift; `mix-blend-mode: multiply`.
- **Motion spec.** Shimmer period 4s (sine in/out), running only
  while the current ad is in the viewport. Grain crawl: 1px per
  900ms in a 6-step loop (5.4s), effectively subliminal; it halts
  entirely when the tab is hidden, under `save-data`, and on
  low-power signals (`navigator.hardwareConcurrency ≤ 2` or battery
  saver), because ambience is the first budget cut (§14).
- **Choreography timeline (v2).** Band marks ad → ad becomes
  `.is-current`, previous current ad's shimmer fades 400ms → shimmer
  loops at 4s → pointer washes another ad → currency transfers on
  pointer leaving it. Grain runs from first paint, unchoreographed.
- **State matrix (v2).** *Rest:* shimmer on the current ad only —
  never more than one shimmering ad (§10 audit). *Hover:* the
  hovered ad's §6.7 wash supersedes; shimmer resumes on leave if
  that ad is current. *Focus:* no change. *Scrolled-past:* shimmer
  pauses off-screen (IntersectionObserver), grain continues only
  in view. *Disabled:* JS off → grain renders as a static texture
  (it is a background, complete without motion); no shimmer.
  *Touch:* shimmer follows the last tapped/washed ad; grain same.
- **Content merge.** The shimmer sits on an actual ad the reader
  actually marked; the grain is the sheet's own material. Neither is
  a layer over unrelated content — the grain is *under* the ink in
  blend terms (multiply), the shimmer behind the ad's text.
- **Failure fallback.** Both are pure enhancement; their absence is
  indistinguishable from a still moment of the same page.
- **Reduced-motion variant.** Both off. The grain texture remains
  static (paper is still paper); no shimmer — the current ad keeps
  only its read wash and tick (§6.3).
- **Breakpoints (v2).** Identical at all sizes; grain tile shrinks to
  120×120 on <768px for memory.
- **Edge cases & failure modes (v2).** *Long sessions:* the grain
  loop is transform-only on a composited layer — no repaint, no
  battery crime; it still yields to the §14 frame budget and pauses
  if frame time exceeds budget for 60 consecutive frames. *Shimmer
  on a clipped ad:* currency transfers to the next read ad when the
  current one is clipped (§6.8).
- **Accessibility spec (v2).** Both `aria-hidden`, neither flashes
  (4s period, ≤0.18 alpha delta — far below any photosensitivity
  threshold), neither is the sole carrier of the "current" state
  (the progress line, §6.4, carries it in text).
- **Performance budget & mobile variant.** Grain: one composited
  transform step per 900ms — ~0. Shimmer: one opacity animation.
  Mobile: grain static under `save-data`, shimmer retained (it is
  one element).
- **Tokens consumed (v2).** `--marker`, `--newsprint`, `--ease-settle`.

### 6.11 Ruled-box ad photos

- **What & why.** Some classified ads carry a photograph — a car, a
  house, a dog — and on the back page it sits in a ruled box at
  thumbnail size, halftone-coarse, beside the copy. As the reading
  band approaches, the photo scales-in-frame (1.1→1) inside its box:
  the one image treatment in the theme, rationed to one photo per ad
  and a minority of ads, because a classifieds page where every ad
  has a photo is a catalogue, not a newspaper.
- **Structure.** `<figure class="ad-photo">` (84×63px desktop, 72×54px
  mobile) floated inside the ad's box with a 1px `--ink` rule border
  and a 3px inner offset — the photo is *pasted into* the ad. The
  `<img>` is `object-fit: cover`, filtered `grayscale(1) contrast(1.06)`
  with a halftone dot overlay (`::after`, radial-gradient dots at
  3px pitch, opacity 0.12) — every photo is printed, none is glossy.
  The scale transform applies to the img inside the clipped figure.
- **Motion spec.** Scrubbed, not triggered: as the band (§6.3) comes
  within 2 agate lines of the ad, the img scales 1.1→1 across that
  approach (driven by the shared lerp value, no separate observer).
  Scrolling back reverses it exactly. An ad already read holds scale
  1 — the photo has been *seen*.
- **Choreography timeline (v2).** Band at ad-head −2 lines → scale
  1.1 → band at ad head → scale ≈1.04 → band passes ad foot → scale
  1, held. The whole travel is ~1 viewport-third of scroll: slow,
  print-like, never a pop.
- **State matrix (v2).** *Rest (unapproached):* scale 1.1, cropped
  slightly tight — the photo before the eye lands. *Approaching:*
  scrubbed. *Read:* scale 1, permanent. *Hover:* no photo-specific
  state (§6.7 wash covers the ad). *Focus:* the figure is not
  focusable; an ad link's focus is §6.7's. *Disabled:* JS off →
  scale 1 (the CSS default is the finished state; JS arms the 1.1).
  *Touch:* same scrub via the §6.3 IO fallback positions.
- **Content merge.** The photo is inside the ad's own ruled box,
  beside its own copy, at the size the fiction allows. It illustrates
  the listing; it never illustrates the page.
- **Failure fallback.** Broken or slow images: the box holds its
  ruled frame with the ad's initial letter set as a Franklin
  monogram (a printed placeholder, not a broken-image icon); layout
  is fixed by the box's aspect, CLS 0. Alt text is the listing's own
  ("2019 Fiesta, red, pictured") — written per §12.
- **Reduced-motion variant.** Scale 1 always; the photo is simply
  printed. Halftone and grayscale remain (they are print, not motion).
- **Breakpoints (v2).** ≥1200px: 84×63px, float right in the ad.
  768–1199px: 76×57px. <768px: 72×54px, float right; on ads narrower
  than 300px the photo sits above the body copy instead of floating
  (a float in a narrow column strangles agate lines below 4 words).
- **Edge cases & failure modes (v2).** *Portrait photos:* the box is
  landscape; `object-position` honours the listing's focal hint,
  defaulting to top (faces and rooflines survive). *No photo:* most
  ads — the box simply does not exist; no empty frames are printed.
  *Many photos in view:* ≤ 12 figures transform per frame batch
  (they share the band's value, so cost is one calculation).
- **Accessibility spec (v2).** Alt text mandatory and specific (§12
  bans "image of"); the halftone overlay is decorative and never
  reduces the photo's own contrast below recognisability — photos
  are content, not texture. Figure is `aria-hidden` only when the
  photo is purely decorative (rare; a seller's photo almost never is).
- **Performance budget & mobile variant.** Images ≤ 18KB each
  (84px-wide thumbnails, WebP), lazy below the first screenful,
  `content-visibility: auto` on off-stage ads. Transform is
  compositor-only.
- **Tokens consumed (v2).** `--ink`, `--newsprint`, shared lerp (§5).

### 6.12 Agate skeleton + sheet-turn transition

- **What & why.** The theme's two state changes. Loading: before the
  ads are set, the sheet shows ruled blank columns — agate-line
  skeletons, grey rules and empty line-blocks where ads will stand —
  which fill with real ads line by line, top to bottom, the way a
  page comes off the press already ruled. Navigation: moving to
  another sheet (another category's page, page 2 of a listing) turns
  the sheet over — the old page lifts and turns, a fresh classifieds
  page lands beneath, its rules redrawing. Both states are the
  newsprint itself in two conditions: blank, then printed; turned,
  then fresh.
- **Structure.** Skeleton: the real column DOM with `.ad--skeleton`
  placeholders — each a ruled box containing 4–7 `--rule-faint`
  agate lines (divs at 60–100% widths, the last line always short,
  like a real ad's). Sheet-turn: a `.sheet-turn` overlay cloning the
  outgoing sheet's first screenful (screenshot-cloned via a cloned
  node, never a canvas capture), rotating on the sheet's left edge
  (rotateY 0→−88°, perspective 1600px) over the incoming page, whose
  rules redraw per §6.5 as it is revealed.
- **Motion spec.** Skeleton fill: as each ad's data lands, its lines
  are replaced by the printed ad with a 120ms print-in (opacity +
  1px settle); fills proceed in reading order with ≤ 40ms stagger —
  a press run, not a cascade. Sheet-turn: `--dur-turn` (450ms,
  `--ease-glide`), outgoing sheet's turn + incoming rules' redraw
  (300ms, §6.5) overlapping the last 200ms. Trigger: route change
  within the classifieds section only — leaving to the form or tray
  views uses a plain document change (you don't turn the sheet to
  read its own foot).
- **Choreography timeline (v2).** Load: t=0 ruled blanks painted
  (they are the server's first paint — no white flash, no spinner)
  → data lands per region → lines print-in in reading order →
  region complete → §6.5 draws its rules → §6.1's sweep may then
  run. Turn: click → t=0 outgoing clone lifts (shadow grows) →
  t=250ms past vertical, incoming visible, its rules drawing →
  t=450ms clone gone, incoming sheet live, focus to its H1.
- **State matrix (v2).** *Rest (loading):* skeleton. *Filling:*
  per-ad print-in. *Loaded:* the sheet. *Turning:* as above.
  *Disabled:* JS off / SPA off → ordinary full-page navigation,
  skeleton only as long as the server takes (it is server-rendered,
  so a no-JS page still lands ruled, then printed). *Touch:*
  identical; the turn's perspective flattens to a 2D slide-over
  (rotateY on small GPUs reads as tearing; the slide keeps the
  fiction — a sheet pulled across).
- **Content merge.** The skeleton occupies the exact boxes the ads
  will occupy; the turn turns the actual page. Neither state invents
  a surface that isn't the sheet.
- **Failure fallback.** Skeleton ads that fail to load become the
  §12 empty ad in place ("NOTHING FILED — this space to let") after
  a 4s timeout — a ruled, labelled blank, never an eternal shimmer.
  A failed turn falls back to an instant navigation. Watchdog: any
  skeleton visible at 6s is force-resolved to content or the empty
  ad.
- **Reduced-motion variant.** Skeleton fills instantly per ad (no
  print-in); navigation is an instant change with the incoming
  rules pre-drawn. The states remain distinguishable (blank vs
  printed) without motion.
- **Breakpoints (v2).** Skeleton mirrors the live column count
  (3 / 2 / 1). The turn's clone is the first screenful at every size;
  <768px uses the slide-over variant above.
- **Edge cases & failure modes (v2).** *Partial data (one category
  slow):* regions fill independently; the sweep (§6.1) waits for the
  first screenful only. *Back button mid-turn:* the turn cancels to
  the destination state instantly — history is never animated
  against. *Slow connection:* §14's cut order removes the turn first,
  then the sweep; the skeleton is never cut (it *is* the slow-state
  design). *Prefers-reduced-data:* photos (§6.11) load last, after
  all text is printed.
- **Accessibility spec (v2).** Skeleton region carries
  `aria-busy="true"` and a visually-hidden "Listings are being set"
  line; completion announces once ("212 ads on this sheet") via the
  §6.4 status line. The turn moves focus to the new sheet's H1 at
  completion and the new page's title is the document title — a
  screen-reader user experiences an ordinary navigation.
- **Performance budget & mobile variant.** Skeleton: pure CSS boxes,
  zero animation cost (no shimmer loop — a *shimmering* skeleton is
  a §9 failure; blanks are still). Turn: one cloned node, one
  transform, 450ms; clone discarded immediately. Mobile: slide-over
  variant, shadow removed.
- **Tokens consumed (v2).** `--newsprint`, `--newsprint-deep`,
  `--rule-faint`, `--ink`, `--ease-glide`, `--ease-rule`,
  `--dur-turn`, `--dur-rule`.

---

### 6.13 Masthead + category index (page family: navigation)

- **What & why.** Navigation in a newspaper is the masthead and the
  index of what's inside — so here it is literally that. The masthead
  (sheet name, dateline row with the §6.6 "ads today" count, the 3px
  rule) pins at the sheet's top; the category index pins beneath it
  or beside the columns, listing every category with its count, in
  caps, one per line. The visitor navigates by reading the table of
  contents of the paper they are holding. There is no hamburger, no
  dropdown, no mega-menu: the index is short because the paper is
  one section deep.
- **Structure.** `<header class="masthead">`: name (Franklin 900),
  dateline row (Newsreader italic: place, date, "ads today" count),
  3px rule. `<nav class="index" aria-label="Categories">`: a list of
  category links (Franklin caps 11px, count right-aligned Newsreader
  tabular), the §6.4 progress line at its foot, and the "Post an ad"
  action set as the index's last, ruled entry — an ad for the action,
  in the index's own voice. Both pin via `position: sticky` (masthead
  top:0; index top: masthead height) — sticky, never fixed, so the
  document's flow is the fallback.
- **Motion spec.** The masthead does not animate on load (it is the
  paper's name; names don't perform). On stage entry (§6.2), the
  masthead compresses: its name steps 44px→26px and the dateline row
  collapses, over 300ms (`--ease-settle`) scrubbed to the first 8% of
  stage progress, freeing the stage's full height for columns; it
  re-expands symmetrically above the stage. Index entries take the
  §6.7 wash on hover; the current category's entry carries a marker
  block (full `--marker` square bullet) — print's way of saying *you
  are here*.
- **Choreography timeline (v2).** Stage approaches → p 0→0.08
  masthead compresses, index locks under it → stage runs → p
  0.92→1.0 masthead re-expands as the stage exits → document
  continues. Category click: §6.12's turn (within-sheet) or a stage
  progress jump to that category's fold position (600ms
  `--ease-glide`) when the category lives on the same sheet.
- **State matrix (v2).** *Rest:* full masthead, index listed.
  *Compressed (in-stage):* as above. *Hover:* entry wash. *Focus:*
  §11 outline on entries. *Active/current:* marker block bullet +
  `aria-current="page"`. *Scrolled-past:* masthead unpins naturally
  after the tray (it is sticky within the sheet wrapper, not the
  document). *Disabled:* JS off → both render statically, fully
  linked; compression never happens. *Touch:* the index strip
  variant (below); entries are 44px targets.
- **Content merge.** The nav *is* the paper's furniture — masthead
  and contents index are content a reader uses, typeset as
  themselves. The counts beside categories are §6.6's real figures.
- **Failure fallback.** Sticky unsupported → both sit at the document
  top as a normal header and index; every link still works; the
  stage's progress line (§6.4) relocates into the index wherever it
  sits.
- **Reduced-motion variant.** No compression: the masthead stays at
  its compact 26px form throughout the stage (chosen at stage entry,
  instantly), index identical.
- **Breakpoints (v2).** ≥1200px: index is the pinned left column
  (200–220px) beside the stage. 768–1199px: index becomes a pinned
  horizontal strip under the masthead — entries inline, counts
  attached, horizontally scrollable by drag/wheel with the §5
  marquee exception when idle. <768px: same strip, entries at 44px
  height, progress line inside it (§6.4 mobile form); masthead name
  28px.
- **Edge cases & failure modes (v2).** *Many categories (>14):* the
  index column lists all (it is a newspaper index; length is
  honesty), grouped under two sub-heads ("THE SHEET", "THE SMALL
  PRINT") if it exceeds one screenful — never a "more" menu.
  *Long category names:* one line, ellipsis in Franklin caps with
  the full name in the link's accessible label. *Sticky + stage
  pin interaction:* the masthead/index pin and the stage pin are
  sequenced (masthead sticky ends where the stage's wrapper ends)
  — nested-pin fighting is a §10 check.
- **Accessibility spec (v2).** Landmarks: `banner`, `nav` with
  `aria-label="Categories"`. `aria-current` on the live category.
  The compression is visual only; the dateline's content stays in
  the accessibility tree. Index links' targets are ≥28px in the
  column (text-dense exception documented) and 44px in the strip.
- **Performance budget & mobile variant.** Sticky + one scrubbed
  height step: ≤0.2ms/frame. Mobile: strip variant, no compression
  transform (height steps are instant under the strip's own rule).
- **Tokens consumed (v2).** `--ink`, `--newsprint`, `--marker`,
  `--ink-soft`, `--ease-settle`, `--ease-glide`.

### 6.14 The front sheet (page family: hero)

- **What & why.** A classifieds site has no hero image and no
  headline pitch; its front is the top of the sheet itself: masthead,
  a one-line standfirst set as a banner ("Every ad on this sheet was
  filed by a neighbour. 212 today."), the category banner row, and
  the columns beginning immediately — the first screenful *is* the
  product, dense with real ads (§4 density law: ≥9 visible). The
  "hero" composition is the discipline of making the top of a
  newspaper do the persuading: abundance, order, and the reader's
  hand already moving (§6.1's sweep crosses this screenful).
- **Structure.** Masthead (§6.13) → standfirst banner (Franklin 800
  20px, one line, between 2px rules) → the stage's head: the first
  category banner + columns 1–3 first screenful, including the three
  featured ads (§6.1) placed in reading order among the ordinary ads
  (never corralled into a featured rail — they were *found* in the
  print). The dog-ear (§4) sits on this screenful's corner.
- **Motion spec.** The entrance is §6.1's (sweep + lift-off +
  rule-ins staggered). The standfirst does not animate. As the stage
  engages, the standfirst scrolls away with the document (it is
  above the stage, not pinned) — the paper's pitch is read once, at
  the top, like a newspaper's.
- **Choreography timeline (v2).** t=0 sheet lands → §6.1 timeline
  runs across this screenful → first scroll: standfirst exits,
  masthead compresses (§6.13), stage progress begins. Nothing else
  is choreographed here — density is the show.
- **State matrix (v2).** *Rest:* printed front sheet. *Hover/focus:*
  per-ad states (§§6.7–6.9). *Scrolled-past:* the front sheet is
  above the stage; returning to it shows featured ads still lifted,
  washes as left. *Disabled:* the static front sheet — which, by the
  density law, is already the complete pitch. *Touch:* identical,
  one column.
- **Content merge.** Total: there is no hero *section* distinct from
  content. The standfirst's figures are §6.6's real counts; the
  screenful is listings.
- **Failure fallback.** The static sheet (above). If featured data
  is missing, the sweep is skipped (§6.1) and the front sheet is
  still complete.
- **Reduced-motion variant.** Static front sheet with statically
  swathed featured ads (§6.1 variant).
- **Breakpoints (v2).** ≥1200px: 3 columns, ≥9 ads in view.
  768–1199px: 2 columns, ≥6 in view. <768px: 1 column, ≥4 in view,
  standfirst wraps to two lines at 17px (the only place the banner
  size changes — a wrapped 20px banner crowds a phone's first
  screenful below the density law).
- **Edge cases & failure modes (v2).** *Thin day (<60 listings):*
  the theme's own rule (§1) says the fiction strains; the front
  sheet holds by adding the two joke ads and the house ads (§4) —
  a real back page pads with house ads, never with fake listings.
  *Standfirst figures stale:* counts render from the same data as
  §6.6; a mismatch is a §10 truth-audit failure.
- **Accessibility spec (v2).** The standfirst is the page's `<h1>`
  (the sheet's name in the masthead is a `<p>`-styled brand, so the
  heading order starts at the promise, not the logo). Reading order:
  masthead → standfirst → index → columns.
- **Performance budget & mobile variant.** The front sheet is the
  LCP: masthead + standfirst + first ads must paint from server HTML
  with fonts subset (§14); no JS is required for its completeness.
- **Tokens consumed (v2).** `--ink`, `--newsprint`, `--marker`,
  `--newsprint-deep`.

### 6.15 The ad block (page family: cards)

- **What & why.** The card of this theme is the ad itself — a ruled
  block of agate: caps head, up to four lines of body, a meta line
  (place, date, price) and the CLIP button (§6.8). There is no other
  card species: category banners, house ads and the empty ad are the
  same block in different copy. Uniformity is the design — a reader
  scans a column of identical shapes at reading speed, and any ad
  that breaks the block shape (bigger, bordered, coloured) is an
  advertiser buying prominence the theme does not sell.
- **Structure.** `<article class="ad">`: `<h3 class="ad-head">`
  (Franklin caps, ≤2 lines), `<p class="ad-body">` (Newsreader agate,
  ≤4 lines), optional `<figure class="ad-photo">` (§6.11),
  `<footer class="ad-meta">` (dateline italic + price tabular + clip
  button). Height 5–9 agate lines (§3 density law); ads are separated
  by 1 agate of rule-space, the next head closing the gap. Category
  changes inside a column insert a banner block (2px rules + caps
  head + count, §6.5 draws its rule).
- **Motion spec.** The ad has no entrance motion of its own — it is
  printed. Its motions are the system's: wash (§6.7), read wash
  (§6.3), photo scale (§6.11), clip (§6.8), tilt when lifted (§6.9),
  skeleton print-in when loading (§6.12). A builder who adds a
  fade-up to ads has left the theme (§9).
- **Choreography timeline (v2).** Per the owning elements above; the
  ad block itself contributes one beat: when its category banner's
  rule draws (§6.5), the ads beneath it are already fully printed —
  the rule arrives last, ruling off a section that exists.
- **State matrix (v2).** *Rest:* printed. *Read:* §6.3 wash + tick.
  *Hover:* §6.7. *Focus-within:* §6.7 wash + outline on the focused
  control. *Featured:* §6.1 lift + swath. *Clipped:* replaced by the
  house ad (§6.8). *Expired/house:* house ads set in the same block,
  head "THIS SPACE TO LET", body in the §12 house voice — visually
  identical weight, so a column of house ads still reads as a
  newspaper, not as errors. *Disabled (JS off):* the printed block,
  clip as form submit (§6.8). *Touch:* two-step wash (§6.7), clip
  first-tap.
- **Content merge.** Definitionally total — the card is the content.
- **Failure fallback.** The block is plain HTML in reading order;
  every enhancement is a class on it. There is no state in which an
  ad exists but cannot be read.
- **Reduced-motion variant.** The printed block with instant state
  changes (per owning elements).
- **Breakpoints (v2).** The block is column-width at every size; on
  <768px the photo un-floats on narrow ads (§6.11) and the meta line
  wraps price under dateline if the column is < 300px.
- **Edge cases & failure modes (v2).** *Over-length copy:* heads
  clamp at 2 lines, body at 4, with the ad's detail view (listing
  page) carrying the full text — the sheet never truncates mid-word
  and never hides copy behind "read more" inside the column (the
  detail link is the ad head itself). *Missing price:* the meta line
  prints "POA" or "Offers" — the classifieds have always had a word
  for it; never a blank. *Duplicate ads:* the data layer's problem,
  but the block renders a "Also filed under Motors" cross-line
  rather than repeating the block (§12 voice).
- **Accessibility spec (v2).** Article with its head as heading
  (heading order: category banner `h2` → ad `h3`). The whole head
  is the detail link (one link per ad, plus the clip button — two
  tab stops per ad maximum, or scanning by keyboard becomes a
  census). Meta line is text, not an image of text. Contrast per §2
  at every state (wash states verified in §6.3/§6.7).
- **Performance budget & mobile variant.** Zero per-ad JS; states are
  classes. `content-visibility: auto` below the stage's fold.
  Mobile: the same block, one column.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--newsprint`,
  `--marker-wash`, `--marker-hover`.

### 6.16 Post-an-ad form (page family: forms / conversion)

- **What & why.** The conversion is filing an ad, and the form is a
  classified order form — the coupon at the bottom of the page that
  you fill in and post. It is typeset as part of the sheet (it lives
  below the stage, in a single ruled column, 58ch), its fields are
  agate-ruled lines, its cost is computed in column inches as you
  write, and its success state is your ad, printed, in a proof block
  exactly as it will appear in the sheet. The reader becomes a filer
  without leaving the paper.
- **Structure.** `<form class="file-form">`: category `<select>`
  (set as an index list, §11), head field (60 characters, live agate
  count), body field (4 lines, line counter drawn as agate rules),
  place + price fields on one ruled row, photo upload (§6.11's box
  as the preview), and the submit button set as a classified head:
  "FILE THIS AD — £6 FOR 3 DAYS". The price line updates from the
  real rate card (lines × days × category rate) in tabular
  Newsreader. A live proof `<article class="ad ad--proof">` beside
  (≥1200px) or above (<1200px) the fields renders the ad exactly as
  §6.15, updating per keystroke (debounced 120ms).
- **Motion spec.** Field focus: the field's rule inks from
  `--rule-faint` to `--ink` (200ms) and a marker tick appears in the
  left margin beside the active field (the reader's place). Proof
  updates print-in (120ms, §6.12's gesture at form scale). Error:
  the field's rule takes a double-rule (print's correction mark) and
  the error line appears in Newsreader italic beneath — never red
  (there is no red in this world), never an icon. Submit: the proof
  block lifts (§6.9, 200ms) and a snip flash (§6.8) runs its border —
  your ad is clipped *into* the paper — then the success block (§12
  voice) replaces the form: the ad as filed, its reference number in
  tabular figures, when it will appear.
- **Choreography timeline (v2).** Focus field → rule inks (200ms),
  tick lands → typing → proof reprints ≤120ms after pause → submit
  → proof lifts (200ms) → snip (250ms) → success block prints in
  (300ms) → the sheet above gains the ad on next view (and §6.6's
  category count +1s with its settle when the filer returns to the
  sheet).
- **State matrix (v2).** *Rest:* faint rules, empty proof frame
  (ruled, labelled "YOUR AD AS IT WILL APPEAR"). *Focus:* inked
  rule + tick. *Filled:* rule stays inked at 60%. *Error:*
  double-rule + italic note, persistent until corrected (forms in
  print do not time out). *Submitting:* button text "FILING…",
  fields disabled, proof lifted. *Success:* the filed block.
  *Disabled:* JS off → the form is a plain HTML form posting to the
  server; the proof is absent and the rate is computed on the
  server's confirmation page — the transaction survives without the
  theatre. *Touch:* fields at 16px input text (iOS zoom law) while
  labels stay agate.
- **Content merge.** The form is a document of the paper — the order
  coupon — and its proof is the actual ad object the filer is
  buying. The price is computed from the sheet's real rate card,
  displayed in the sheet's own figures.
- **Failure fallback.** Plain form (above). A failed submit keeps
  every field's value and prints the §12 error voice at the form's
  head — a filer never loses a written ad to a network error
  (values persist in `sessionStorage` across an accidental reload).
- **Reduced-motion variant.** States apply instantly; submit skips
  lift and snip, success prints without motion.
- **Breakpoints (v2).** ≥1200px: form column + proof column side by
  side (the filer sees the ad while writing it — the theme's one
  two-column moment outside the stage). 768–1199px: proof above the
  fields, sticky while the form is in view. <768px: proof collapses
  to a "Preview as printed" toggle block above the submit button,
  expanded state showing the §6.15 block.
- **Edge cases & failure modes (v2).** *Head over 60 chars:* the
  counter prints "61 — one word too many" and the field refuses the
  extra character (classifieds heads are cut, §3) — with the cut
  word offered as the body's first word, not silently eaten.
  *Body over 4 lines:* the rate line shows the 5-line price and the
  proof shows the ad at 5 lines with a note — over-length is a
  price, not an error, on a real order form. *Photo too large:*
  client-side downscale to the §6.11 box spec before upload.
  *Category with moderation:* the success block says so in §12
  voice ("held for the editor's eye — appears by 6pm") — never a
  fake instant-live promise.
- **Accessibility spec (v2).** Labels always visible (§3); errors
  linked via `aria-describedby`, summarised at the form head with
  anchor links to fields; focus moves to the success block's heading
  on completion. The live proof is `aria-hidden` (it duplicates the
  fields); the rate line is a polite live region updating on pause,
  not per keystroke. Touch targets: fields ≥44px tall.
- **Performance budget & mobile variant.** Proof reprint is one
  block's text write per debounce — trivial. No animation loops.
  Mobile: single column, proof toggle (above).
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--rule-faint`,
  `--marker`, `--newsprint`, `--shadow-slip`, `--ease-settle`,
  `--ease-snip`.

### 6.17 Clippings tray + page foot (page family: footer)

- **What & why.** The sheet's foot is where the reader's clippings
  live: a full-width ruled band — the tray — holding every clipped
  ad as a cut-out slip (§6.9), in clip order, plus the paper's
  colophon line (who publishes this sheet, the edition, the legal
  small print in agate). The footer is not a sitemap farm; a
  newspaper's foot is its imprint and, here, the reader's own
  collection. The tray makes the session's reading tangible: scroll
  to the foot and your clippings are waiting, slightly crooked, like
  cuttings on a corkboard.
- **Structure.** `<footer class="sheet-foot">`: the tray
  (`<section class="tray" aria-label="Your clippings">`) — a
  `--newsprint-deep` band with a 2px top rule, a tray head ("YOUR
  CLIPPINGS — n" in Franklin caps with §6.6-style count), the slips
  in a wrapped row (each the full §6.15 block at 92% scale with its
  `--slip-rot`), an "UNCLIP" control per slip, and tray actions:
  "Return all clippings", "Print clippings" (a real print stylesheet
  — clippings print as clippings, §10). Below: the colophon line —
  publisher, edition number, "Set in Libre Franklin & Newsreader",
  legal links as agate text links.
- **Motion spec.** The tray itself is still. Slips arrive per §6.8.
  The tray head's count settles (§6.4's 120ms) on change. Unclip:
  the slip lifts and travels back to its column place (the house ad
  yields), 550ms `--ease-glide`, or — if the sheet above has been
  turned since (§6.12) — fades from the tray and the ad is restored
  on next sheet view (state is truth; travel is theatre, and theatre
  never blocks state).
- **Choreography timeline (v2).** Clip lands (§6.8) → tray count
  settles → if tray off-screen, its tab in the index (§6.13, "Tray —
  n") pulses once. Unclip → slip travels or fades (above) → count
  settles → focus returns to the restored ad's place (§6.8's focus
  rule, mirrored).
- **State matrix (v2).** *Empty:* the tray prints its empty state in
  §12 voice ("NO CLIPPINGS YET — clip an ad and it will wait for you
  here") inside its ruled band — a framed blank, per §4's whitespace
  law. *Holding:* slips at rest rotations. *Hover:* §6.9 tilt
  (un-piled slips). *Focus:* slip straightens + outline (§6.9).
  *Disabled:* JS off → clippings saved server-side (§6.8) render as
  a static slip list, unclip as form buttons. *Touch:* slips don't
  tilt (§6.9); unclip is a 44px button.
- **Content merge.** The tray holds the reader's actual clippings —
  the session's own content, collected. The colophon is the paper's
  real imprint. Nothing in the foot is decorative furniture.
- **Failure fallback.** Static slip list (above). Print stylesheet
  renders the tray's slips in a clean ruled grid — the one place the
  theme *wants* to be printed.
- **Reduced-motion variant.** Arrivals and returns are instant state
  changes; rotations remain (state, not motion, §6.9).
- **Breakpoints (v2).** ≥1200px / 768–1199px: slips wrap in rows of
  the tray's full width. <768px: the tray is additionally mirrored
  as a pinned bottom strip while reading ("CLIPPINGS — n ▸" tapping
  to the tray) — on a phone the foot is far away, and the reader's
  clippings should not be. The strip is 44px, `--newsprint-deep`,
  ruled top; it never covers an ad's clip button (the sheet's bottom
  padding reserves its height).
- **Edge cases & failure modes (v2).** *Tray pile (>24, §6.8):*
  piled slips show head + meta only, stacked at 2px offsets, with
  "and n more in the tray" expanding the pile in place. *Session
  end:* clippings are session-scoped (like §6.3's washes) unless the
  site accounts save them — the tray head says which ("kept for this
  visit" / "kept in your account") in §12 voice. *Printing with an
  empty tray:* the tray prints its empty line — an honest foot.
- **Accessibility spec (v2).** Tray is a labelled section; each slip
  keeps its article semantics and head; unclip buttons named
  "Return [head] to the sheet". The pinned strip is a link, 44px,
  with the count in text. Colophon links are ordinary links at agate
  size with 28px line spacing.
- **Performance budget & mobile variant.** Static band; arrivals are
  §6.8's budget. The strip is one sticky element.
- **Tokens consumed (v2).** `--newsprint-deep`, `--newsprint`,
  `--ink`, `--ink-soft`, `--shadow-slip`, `--slip-rot` (per-slip),
  `--ease-glide`.

### 6.18 The empty column (page family: 404 / no results)

- **What & why.** A category with no ads, a search with no matches,
  a wrong URL — in this theme they are the same printed thing: a
  column with nothing filed in it. The page prints the column anyway
  — rules drawn, category head set — and inside it, the empty ad in
  §12 voice: what was looked for, that nothing is filed under it
  today, and the two things a reader can do (browse the index, file
  the first ad). A classifieds paper never shows a broken page; it
  shows white space with a rule around it and a house ad in it.
- **Structure.** The sheet frame (masthead, index) intact; the stage
  replaced by a single ruled column containing: the sought head set
  as a category banner ("SOUGHT: 'BICYCLE, TANDEM'"), the empty ad
  block (§6.15 shape: head "NOTHING FILED", body in §12 voice), a
  house ad ("THIS SPACE TO LET — file the first ad under this head,
  from £4"), and the three nearest live categories as ordinary ad-
  shaped links. A true 404 (no such sheet) adds the line "This page
  was not in today's edition" and the sheet's own index as the way
  back — never a generic error illustration.
- **Motion spec.** The column's rules draw (§6.5) as usual; the
  empty ad prints in (§6.12's 120ms). Nothing else moves — an empty
  page that performs is worse than an empty page.
- **Choreography timeline (v2).** Land → rules draw 600ms → empty
  ad printed → done. Total < 1s.
- **State matrix (v2).** *Rest:* as specced. *Hover/focus:* the
  category links take §6.7/§11 states. *Disabled:* identical (the
  page is static by design). *Touch:* identical.
- **Content merge.** The emptiness is reported in the paper's own
  forms — the sought term is printed, the nearest categories are
  real listings' categories with real counts (§6.6).
- **Failure fallback.** This *is* the fallback page; its own
  fallback is that it is plain HTML requiring nothing.
- **Reduced-motion variant.** Rules pre-drawn; otherwise identical.
- **Breakpoints (v2).** One column at every size (an empty page does
  not need the stage); index per §6.13's breakpoint behaviour.
- **Edge cases & failure modes (v2).** *Search with results in
  another category:* the empty ad says so and names it ("Nothing
  under Motors — but 3 filed under Cycles") — cross-references are a
  newspaper habit (§6.15's cross-line). *Typo'd category:* the
  nearest-head suggestion is computed from the real index, never a
  hardcoded list.
- **Accessibility spec (v2).** The empty ad's head is the page `h1`
  for search-empties ("Nothing filed under 'tandem bicycle'"); for
  404s the `h1` is "This page was not in today's edition". Status
  code is a real 404; search-empties are 200.
- **Performance budget & mobile variant.** The lightest page in the
  theme; no stage, no loop beyond the shared one idling.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--newsprint`,
  `--rule-faint`, `--ease-rule`.

---

## 7. Page application map

**Home (the whole sheet).** The full composition: masthead, standfirst,
pinned stage with all categories folded through the three columns,
index pinned, post-an-ad form below the stage, tray at the foot.
Featured ads (§6.1) are drawn from across categories. This is the
reference build; every other page type is a subset or a single column
of it.

**Category page (one section of the sheet).** The sheet frame with a
single category in the stage: columns carry only that category's ads,
the stage shortens to the content (min 160vh, §6.2), the index marks
the category current (§6.13). Sub-category banners rule off inside
the columns. The standfirst is replaced by the category's own banner
line with its true count ("MOTORS — 47 filed today").

**Listing detail (the ad, enlarged).** One ad leaves the small print:
a single ruled column (58ch) where the ad's full text is set at body
size (Newsreader 15px/22px — the theme's one concession to length),
its photo at 100% column width in its ruled box (§6.11's treatment,
larger frame), the filer's other ads as ordinary agate blocks beneath
("ALSO FILED BY THIS SELLER"), and the clip button keeping §6.8's
behaviour — clipping from detail returns the slip to the tray and the
reader to the sheet position they came from. Breadcrumb is an index
line: "The Sheet › Motors › Fiesta, 2019" set as agate, not chevrons.

**Search results.** The sheet with the stage carrying matched ads
across categories, each keeping its category banner as a cross-line
above it (§6.18's habit); the sought term is the standfirst ("SOUGHT:
'TANDEM' — 3 FILED"). No matches → §6.18. Result counts are §6.6
figures. Sorting, where offered, is an index-style line of text links
("by date · by price · by place") — never a dropdown widget.

**About / the paper itself.** A single-column sheet: the paper's own
story set as a long classified ("ABOUT THIS SHEET: est. 2019…") in
agate with category-style banners for sections, the rate card as a
ruled table (§11), and the masthead's history as datelines. No stage;
about pages are read, not browsed.

**Contact / file-a-problem.** The §6.16 form pattern re-skinned: a
ruled coupon ("WRITE TO THE SHEET") with the same field, error and
success voices. Checkout equivalents (paying to boost an ad, where
the product has them) use §6.16's rate-line pattern — price computed
in the open, in tabular figures, on the coupon — never a separate
checkout universe.

**Account / your filings.** The reader's own filed ads as a personal
column: their ads as §6.15 blocks with status lines in the meta
("LIVE — day 2 of 3", "HELD FOR THE EDITOR"), their clippings tray
(§6.17) promoted to the page's head. Same blocks, same rules — the
account page is a page of the paper the reader has written in.

---

## 8. Worked examples

### 8.1 The hero — a job board's front sheet

*The build.* "The Gazette Jobs Sheet": masthead "THE GAZETTE — JOBS"
(Franklin 900), dateline "*Leeds · Tuesday · Ads today 212*", 3px
rule. Standfirst (the `h1`): "Every job on this sheet was filed by an
employer within twenty miles. 212 today." Index column at left:
FULL-TIME 86, PART-TIME 41, SHIFTS & NIGHTS 33, APPRENTICESHIPS 18,
WORK FROM HOME 22, SHORT NOTICE 12 — each with §6.6 counters — then
the progress line, then "POST A JOB" as the index's last ruled entry.
The stage: three columns folding 212 ads in category order; three
featured ads (a bakery's night-shift baker, a canal trust's lock
keeper, a school cook) sit in reading order in column 1's first
screenful. The dog-ear sits top-right. Among the ordinary ads, per
the library entry's anti-slop law, two joke ads in perfect voice:
"FOR SALE: one bridge, barely used. Buyer collects. — Box 114" (in
SHORT NOTICE, filed by the paper itself as a house joke) and "WANTED:
hen's teeth. Any condition considered." — both clipped-able, both
counted in the 212 (they are filed ads; the truth audit counts what
is printed).

*Scroll timeline.* t=0 sheet lands printed → t=250ms sweep begins →
featured ads lift at ≈480/700/920ms → t=1500ms sweep done, masthead
counter settled at 212 → reader scrolls → masthead compresses over
stage p 0–0.08 → band rides column 1, washes accumulating, index line
counting → p 0.29–0.375 fold to column 2 (the eye lands on
APPRENTICESHIPS' banner as its rule draws) → p 0.62–0.71 fold to
column 3 → p=1 stage releases into the post-a-job form. A reader who
clips the lock keeper at p≈0.2 watches the snip, the lift, the slip's
travel to the tray, and finds "YOUR CLIPPINGS — 1" waiting at the
foot.

### 8.2 Mid-page — the Motors section, read deeply

*The build.* Inside the same sheet, the MOTORS category: banner
("MOTORS — 47 FILED") with its drawn 2px rule, then 47 ads folded
across the stage's middle. Ads carry §6.11 photos on roughly one in
three (the Fiesta, the narrowboat — Motors includes boats, as any
local paper's does — the Transit with "one careful owner, one
careless"). Cross-lines appear where a seller filed twice ("Also
filed under Cycles: same seller"). One ad is a house ad where a
listing expired that morning: "THIS SPACE TO LET — this space held a
2018 Astra until 9am today."

*Scroll timeline.* Fold from column 1 lands the reader at Motors'
banner (rule draws 300ms as it lands) → band descends: each ad's
photo scales 1.1→1 as the band nears, washes soak at each foot, the
index line ticks "ads seen 88… 96… 104" → the reader hovers the
narrowboat (wash deepens to 0.28), clicks CLIP (snip 250ms, lift,
travel; a house ad prints into the gap) → band crosses into column
3's Motors tail → the shimmer (§6.10) idles on the last washed ad,
the Transit, while the reader pauses. Nothing else on the page is
moving. That stillness is the section's premium note: density at
rest.

### 8.3 Conversion — filing a job ad

*The build.* Below the stage, the coupon (§6.16): "FILE A JOB —
£6 FOR 3 DAYS, 3 LINES" as the section banner. Category select set
as an index list; head field ("NIGHT BAKER — 4 NIGHTS, SAT OFF" typed
live, counter "38 OF 60"); body field filling its four ruled lines;
place "Leeds LS9", wage "£13.20/HR" on the ruled row; the rate line
recomputing in tabular figures as days are set to 5 ("5 DAYS × 3
LINES — £10"); the proof block at the right rendering the ad exactly
as §6.15 — caps head, agate body, meta line — updating 120ms after
each pause in typing.

*Scroll/interaction timeline.* Reader scrolls past the stage's end →
form region enters, its column rules draw (§6.5) → focus head field:
rule inks, marker tick lands in the margin → typing: proof reprints
per pause → an error is made (wage left blank): on submit attempt,
the wage field takes its double rule and the italic note "A job with
no wage filed is a rumour. Give the rate, or write 'Offers'." →
corrected → submit: proof lifts, snip runs its border, success block
prints: the ad as filed, "REF GZ-2214", "Appears in tomorrow's sheet
by 6am. Held for the editor's eye until then." → the filer scrolls
up: the index's FULL-TIME count has settled 86 → 87.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **Ads styled as cards.** Rounded corners, drop shadows at rest,
   gaps of white between floating tiles — the instant the blocks
   stop sharing rules and rhythm, it is a generic listing grid in a
   serif font. *Cure:* shared 1px rules, agate rhythm, no rest
   shadows anywhere (§6.15); shadows exist only on lifted paper.
2. **A big hero.** A 48px headline and a stock photo above the
   columns "for conversion" destroys the fiction and the density
   law. *Cure:* §6.14 — the first screenful is ≥9 real ads; the
   standfirst is one line at 20px.
3. **Yellow everywhere.** Marker as button colour, link colour,
   price colour, background tint on alternate sections. The ration
   (§2) is the design: yellow is a reader's tool, and a page the
   reader has "marked" entirely is a page marked nowhere. *Cure:*
   the §2 cap, audited in §10.
4. **Fake density.** Lorem-ipsum ads, duplicated listings with names
   swapped, counts that don't match the listings. Density is only
   premium when it is *true*. *Cure:* §10 truth audit; joke ads and
   house ads are labelled by their nature in copy, never passed off
   as listings.
5. **Fade-up ads.** Listings that fade/slide in on scroll read as a
   website performing a newspaper. *Cure:* ads are printed from
   first paint (§6.15); motion belongs to rules, band, hand and
   paper — never to the type's existence.
6. **A generic save heart.** A bookmark icon row on each ad imports
   another product's language. *Cure:* §6.8 — clipping, with the
   tray; the state change is spatial and total.
7. **Dropdowns and modals.** A filter modal floating over the sheet
   breaks the §1 law (neither paper nor hand). *Cure:* filtering is
   the index (§6.13) and cross-lines (§6.15); anything that must
   overlay is a slip on the sheet (the proof, the tray pile), never
   a dimmed world behind glass.
8. **Comfortable whitespace.** 24px card padding, 96px section gaps
   "to let it breathe" — breathing is rationed here; air is unsold
   inches and must be framed (§4). *Cure:* agate spacing only; gaps
   are ruled and labelled.
9. **A shimmering skeleton.** Pulsing grey blocks are a loader from
   another world. *Cure:* §6.12 — still, ruled blanks that print in;
   stillness is the loading state.
10. **Cute copy.** "Oops! Nothing here 😢" in the empty column, or
    "Yay, clipped!" toasts. The paper's voice is dry (§12); cuteness
    is the fastest way to make small print feel like a toy. *Cure:*
    §12's voices, verbatim where specified.

---

## 10. Quality gate

A build may not ship in this theme until every **blocking** item
passes and at least 9 of the 11 **standard** items pass. The reviewer
checks evidence (a JS-off load, a full-page screenshot, a slow-scroll
pass), not intentions.

**Blocking — all must pass.**

1. **JS-off test:** with JavaScript disabled, every ad is readable
   in reading order, the index and clip forms work, counts show
   final figures, featured ads show their static swath.
2. **Fallback test:** with the pin deliberately broken, the stage
   unpins within 1s and no ad is stranded off-stage (§6.2); with IO
   broken, washes simply never appear and nothing else changes.
3. **Reduced-motion test:** no pin, no fold, no sweep, no shimmer;
   one standard column (or static columns ≥1200px); all states
   reachable; the page is complete.
4. **Truth audit:** every count on the page (masthead, index,
   progress line, tray) equals the number of matching ads in the
   DOM/data; every price in a proof equals the rate card's
   computation. One invented figure fails the build.
5. **Marker ration:** on a full-page screenshot at three scroll
   positions, full-strength `--marker` covers only the band, ≤1
   shimmering ad, and the featured swaths; yellow never carries text
   alone and never colours a price.
6. **Density audit:** first screenful shows ≥9 ads (desktop) / ≥4
   (mobile); no unframed whitespace region larger than one ad block
   exists anywhere on the sheet (gaps are skeleton, house ad, or
   labelled blank).
7. **Register audit:** at rest, all columns and rules measure 0px
   offset from the agate grid; the only resting rotations are slips
   (`--slip-rot` within ±1.2°) and the dog-ear's fold.
8. **Cursor & cover audit:** system cursor unchanged everywhere; no
   animated element overlaps text it does not belong to at 5 scroll
   depths; the band never covers the index or masthead.
9. **Print test:** `@media print` renders the sheet as clean ruled
   columns with solid rules and no band/shimmer/grain motion
   artefacts; the tray prints as a ruled grid of clippings.

**Standard — at least 9 of 11.**

10. Sweep completes ≤1.6s and never replays within a session.
11. Fold travel is lerp-smooth (0.14) with no frame over 20ms of
    theme code during a full stage scroll on a mid-range Android.
12. Counters tick once, upward only, landing on true figures.
13. Washes persist per session and never un-wash on reverse scroll.
14. Clip round-trip (clip → tray → unclip → restored place) works
    by mouse, touch, and keyboard, with focus preserved.
15. Photos are ≤18KB, halftone-treated, and never more than one per
    ad.
16. The two joke ads are present, in perfect classified voice, and
    counted honestly.
17. Type scale unmodified: no size outside §3's table appears in the
    sheet; Franklin is never faux-italicised.
18. The five-second test: a first-time viewer describes the page as
    *the back page of a newspaper, being read* — not "a retro
    listing site", not "a card grid with rules".
19. Skeleton blanks resolve to ads or the labelled empty ad within
    6s on a throttled connection.
20. The lamplight variant (§2), if offered, is a reader's toggle —
    never an OS-forced re-papering.

**Minimum bar, in one line:** a build that passes the blocking nine
has earned the right to be judged on premiumness; a build that also
clears the standard list *and* makes a reviewer slow down and actually
read the small print is a Classifieds page. Anything less is a listing
grid in costume, and it goes back to the compositor.

---

## 11. Component inventory

Every component a real site in this theme needs, with its themed
treatment. Anything not listed here does not get invented ad hoc; if
a build needs a component the inventory lacks, it is built as the
nearest listed relative and the inventory is amended.

| Component | Themed treatment |
|---|---|
| Primary button | A classified head as a button: Franklin 800 caps on `--newsprint`, 2px `--ink` rule box, press = ink fills the box and text goes `--newsprint` (150ms). Label is a verb in classified voice ("FILE THIS AD", "CLIP") |
| Secondary button | Same box at 1px rule, no fill on press; wash (§6.7) on hover |
| Text link | Newsreader, underline = a drawn rule (background-size trick, 1px `--ink`), hover deepens to 2px. Links inside agate copy are never coloured — there is no link colour in this world |
| Ad block | §6.15 — the card species of the theme |
| Category banner | 2px rules above/below, Franklin 800 caps head + Newsreader italic count (§6.5 draws the top rule) |
| Index entry | §6.13 — caps name, tabular count, marker block when current |
| Input (text) | A ruled line, not a box: transparent ground, 1px bottom rule (`--rule-faint` → `--ink` on focus, §6.16), Newsreader 15px entry text, Franklin caps label above |
| Textarea | A ruled sheet: repeating-linear-gradient agate lines at 14px pitch, entry text on the lines, line counter in the margin |
| Select | Set as an index list (radio-style ruled rows) when ≤8 options; a native `<select>` restyled as a ruled line when more — never a custom dropdown panel (§9.7) |
| Checkbox / radio | A small ruled box the reader ticks: the tick is a hand-drawn-style SVG stroke (draws 120ms) — the reader marks paper, in ink (`--ink`, never marker: a tick is a decision, not a highlight) |
| Toggle | **Refused.** Print has no toggles. A binary choice is two ruled options side by side, the chosen one washed (§6.7 strength) — e.g. lamplight on/off (§2) |
| Table (rate card, terms) | A ruled table: column rules like the sheet's, heads in Franklin caps, figures tabular Newsreader, row rules 1px; the table is a small classifieds page of numbers |
| Badge / tag | A marker swath behind caps text (the §6.1 swath at label scale) — used only for "FEATURED" and "NEW TODAY"; any other badge need is met with bold caps in the meta line |
| Alert / notice | A house-ad block (§6.15 shape) with head "NOTICE" — inline in the column flow, never a banner across the top, never a toast |
| Toast | **Refused.** Feedback lives where the action happened (tray count, success block, live region). Nothing floats |
| Modal | **Refused** (§9.7). Detail content is a page (§7 listing detail); confirmations are slips on the sheet |
| Pagination | A sheet line: "CONTINUED ON SHEET 2 ›" set as a category banner at the column foot — page 2 is another sheet (§6.12 turns to it). Numbered pages, if needed, are agate figures in the same line |
| Tabs | Category banners (§6.13 index strip on mobile) — the index *is* the tab set; no separate tab component exists |
| Accordion | An index expansion: the entry's sub-entries rule-in beneath it (§6.5 draw, 300ms) in the same column — used for index groups (§6.13) and FAQ-as-classifieds on about pages |
| Search field | A sought-line: the index's head carries "SEEK:" + a ruled input; submitting turns the sheet (§6.12) to the results sheet (§7) |
| Breadcrumb | An agate index line with "›" separators (§7), Newsreader italic |
| Progress | §6.3 band + §6.4 line. No other progress UI exists |
| Skeleton | §6.12 ruled blanks |
| Empty state | §6.18 the empty column / empty ad |
| Error state (form) | §6.16 double rule + italic note; page errors are §6.18 |
| Price / rate line | Tabular Newsreader, computed in the open (§6.16), never styled as a badge |
| Photo | §6.11 ruled box, halftone, rationed |
| Footer | §6.17 tray + colophon |
| Focus indicator (global) | 2px `--ink` outline, 2px offset, on the interactive element; in dense agate the outline is doubled by the §6.7 wash where the element is an ad |

---

## 12. Content & copywriting voice

The paper writes like a classifieds page: compressed, factual, dry,
with the comedy coming from specificity, never from the writing
trying to be funny. Two voices: the **paper's** (Franklin caps heads,
terse) and the **reader's margin** (Newsreader italic asides — the
datelines, the progress line, the error notes, which speak like a
person annotating, in lower case).

**Headline rules (paper's voice).** Caps, ≤ 60 characters, noun-first,
no verbs where a noun does the job, no adjectives of enthusiasm.
✓ "NIGHT BAKER — 4 NIGHTS, SAT OFF" · ✓ "TANDEM BICYCLE, STEEL,
ONE OWNER" · ✗ "Amazing Opportunity for a Passionate Baker!!!" ·
✗ "You Won't Believe This Bicycle". Prices and facts outrank flair:
if a head can carry the price, it does.

**Label rules.** Buttons and labels are classified heads for actions:
verb + object, caps, ≤ 4 words. ✓ "FILE THIS AD" · ✓ "CLIP" ·
✓ "RETURN ALL CLIPPINGS" · ✗ "Submit" · ✗ "Save to favourites" ·
✗ "OK". The empty button ("OK", "Yes") is banned — a newspaper
button says what it does.

**Error voice (reader's margin).** Italic, sentence case, states the
fact and the remedy in one breath, never apologises, never blames.
✓ "A job with no wage filed is a rumour. Give the rate, or write
'Offers'." · ✓ "That head is one word too long — the sheet cuts at
sixty." · ✗ "Oops! Something went wrong." · ✗ "Invalid input".

**Empty-state voice.** States what was sought, what is filed
(nothing), and the nearest true thing. ✓ "NOTHING FILED under
'tandem bicycle' today. Three filed under Cycles — or file the
first, from £4." · ✗ "No results found 😢".

**Success voice.** The paper confirms like a receipt: what was
filed, its reference, when it appears. ✓ "Filed. REF GZ-2214.
Appears in tomorrow's sheet by 6am, held for the editor's eye until
then." · ✗ "Awesome! Your ad is live!"

**Fixed strings (verbatim, do not paraphrase).** Progress line:
"column {n} of {m} · ads seen {k}" (§6.4). Tray empty: "NO CLIPPINGS
YET — clip an ad and it will wait for you here". House ad head:
"THIS SPACE TO LET". Skeleton-resolved empty: "NOTHING FILED — this
space to let". Masthead counter label: "ADS TODAY".

**Banned words.** "Oops", "awesome", "amazing", "curated",
"seamless", "delightful", "favourites", "dashboard", "content"
(as a noun for listings — they are *ads*), exclamation marks in the
paper's voice (the reader's margin may have one per page, and the
joke ads may have none — their comedy is deadpan).

**The joke ads.** Exactly two per sheet (§8.1), written in perfect
classified voice, deadpan, plausible at a glance, absurd at a read.
They are the paper's signature and its proof that a human edits it.
They rotate per edition from a kept list; they are never labelled
as jokes (§9.4's labelling law applies to *listings passed off as
real* — the jokes are house ads by nature, filed by the paper, and
the §10 audit counts them as what they are).

**Photo alt text.** Specific and commercial, like the ad itself:
✓ "2019 Fiesta, red, nearside pictured" · ✗ "image of car" ·
✗ "" (a seller's photo is never decorative, §6.11).

---

## 13. Full-page scroll choreography map

The home sheet, top to foot, in order. Every beat names what the
visitor sees and what moves; beats not listed do not move.

1. **Landing.** The printed sheet, whole (§6.14). Nothing fades in.
2. **The sweep (t=250–1500ms).** §6.1: band crosses, three featured
   ads lift, category rules draw staggered, masthead counter settles
   at the true "ads today".
3. **First scroll — the pitch leaves.** The standfirst scrolls away;
   the masthead compresses (§6.13, stage p 0–0.08); the index locks
   in place with its progress line at "column 1 of 3 · ads seen 0".
4. **Column 1 descends.** The band rides the reading line (§6.3);
   ads wash as they are passed; photos settle 1.1→1 (§6.11); the
   progress count climbs. The dog-ear drifts its 4px. Nothing else
   moves — the reader is reading.
5. **First fold (p 0.29–0.375).** The track glides to column 2's
   head (§6.2); column 2's region rules are already drawn as it
   lands (§6.5's pre-draw); the progress line's column figure
   settles to 2 at the fold's midpoint.
6. **Column 2 descends.** As beat 4, in the second column's
   categories. The shimmer (§6.10) idles on the last-washed ad
   whenever reading pauses > 1.2s.
7. **Second fold (p 0.62–0.71).** As beat 5, to column 3.
8. **Column 3 descends to the sheet's foot.** The last category's
   banner, the last ads wash; the progress line reaches the final
   figures and freezes (§6.4 scrolled-past state).
9. **Stage release (p=1).** The masthead re-expands; the document
   resumes ordinary scroll. The post-an-ad section's rules draw as
   it enters (§6.5).
10. **The coupon.** §8.3's interaction choreography — a working
    section, not a scroll show.
11. **The tray.** Still. The session's clippings at their rotations;
    the count in the tray head agrees with §6.4's world (it counts
    clippings, not ads seen — two tallies, two labels, never mixed).
12. **The colophon.** Static. The last thing on the sheet is the
    paper stating what it is. End of page.

**Reverse scroll** retraces beats 9→3 exactly (§6.2), with washes and
counts persisting — the paper remembers being read in both
directions. **Jump scroll** (scrollbar drag, Home/End) lands the
stage at the mapped progress with all intermediate washes applied in
one batched pass (§6.3) — the reader who skips to the end has, in the
fiction, skimmed: the page shows it.

---

## 14. Whole-page performance budget

**Asset budget (home sheet, first load).**

| Item | Ceiling |
|---|---|
| HTML (server-rendered sheet, first screenful + stage data) | ≤ 90KB gz |
| CSS | ≤ 28KB gz (the whole theme is rules, type and washes) |
| JS | ≤ 34KB gz (one loop, IO, clip/tray state, form proof) |
| Fonts | Libre Franklin (600/800/900) + Newsreader (400/600 + italic) subsets ≤ 110KB total, `font-display: swap` with the §6.1 font gate |
| Images | Photos ≤ 18KB each, ≤ 12 on the first stage pass; total page images ≤ 400KB with lazy loading below the fold |
| Total first load | ≤ 700KB — a dense page that loads like a light one is the theme's technical signature |

**Frame budget.** The shared loop's theme code ≤ 1.2ms per frame
(track transform, band transform, ≤ 12 batched wash/photo updates).
No long task > 50ms during scroll; the fold must hold 60fps on a
mid-range Android (the §10 standard check). Transforms and opacity
only — box-shadow animation is confined to §6.1/§6.8's brief lifts
and pre-rendered where possible.

**Cut order (when the budget is exceeded, cut in this order, never
reorder).** 1. Grain crawl (§6.10) → static grain. 2. Shimmer
(§6.10) → off. 3. Sheet-turn (§6.12) → instant navigation. 4. The
sweep (§6.1) → static swaths. 5. Slip tilt (§6.9) → static rotations.
6. Photo scale scrub (§6.11) → photos printed at scale 1. **Never
cut:** the fold (§6.2), the band and washes (§6.3), the progress line
(§6.4), the clip round-trip (§6.8), any fallback, any reduced-motion
variant. The theme without its cuts is still the theme; the theme
without its never-cuts is a listing grid.

**Data discipline.** Counts are computed from the rendered data
(§10 truth audit); no counter may be a marketing figure. Ads beyond
the stage's first pass may hydrate progressively, but the skeleton
(§6.12) — not a spinner — is the only waiting state, and the stage's
geometry is computed from real ad heights (§3's law makes them
predictable before hydration).

---

## 15. Build-order checklist

Build in this order; each step passes before the next begins. The
order is static-first, because in this theme the static page is not
a fallback for the experience — it *is* the experience, enhanced.

1. **Tokens & type.** §2 palette (with derived tokens flagged), §3
   scale and agate rhythm (14px base grid), font loading with the
   swap gate. *Gate:* the type table renders a specimen column
   indistinguishable in rhythm from a printed back page.
2. **The static sheet.** Masthead, standfirst, index, three-column
   document, ad blocks (§6.15), form (§6.16 static), tray + colophon
   (§6.17 static), empty page (§6.18). No JS. *Gate:* §10 blocking
   items 1, 4, 5, 6, 7 pass on this build alone.
3. **Rules & skeleton.** §6.5 SVG ruling (with CSS-border fallback),
   §6.12 skeleton + print-in. *Gate:* slow-throttle load shows ruled
   blanks resolving in reading order within 6s.
4. **The stage.** §6.2 pin + fold + the 1s unpin watchdog; §6.13
   masthead compression + index pinning. *Gate:* blocking items 2
   and 8; focus-mapping verified by keyboarding through all three
   columns.
5. **The hand.** §6.3 band + washes (with IO fallback), §6.4
   progress line + status announcements. *Gate:* jump-scroll and
   reverse-scroll passes; counts agree with washes at every depth.
6. **Counters.** §6.6 tick-up + live-update settle. *Gate:* truth
   audit against the DOM.
7. **The entrance.** §6.1 sweep + lift-off + session flag + 1600ms
   watchdog. *Gate:* sweep never replays in-session; hidden-tab
   load lands in the disabled state.
8. **Clipping.** §6.8 round-trip, §6.9 tilt, §6.17 tray dynamics +
   mobile strip. *Gate:* blocking-adjacent round-trip test by
   mouse, touch, keyboard; focus preserved both ways.
9. **Photos & ambience.** §6.11 scrub, §6.10 shimmer + grain with
   their pause conditions. *Gate:* §14 frame budget measured on a
   mid-range Android; cut order implemented and tested by forcing
   each cut.
10. **The form's life.** §6.16 proof, rate computation, error and
    success choreography. *Gate:* no-JS submit path verified
    end-to-end on the server.
11. **Transitions.** §6.12 sheet-turn for in-section navigation.
    *Gate:* back-button mid-turn cancels cleanly.
12. **Reduced-motion & lamplight passes.** Every §6 variant
    implemented and toggled-tested; lamplight as the reader's toggle
    (§2). *Gate:* blocking item 3.
13. **Print stylesheet.** §10 item 9. *Gate:* a printed sheet a
    reader could pin to a corkboard.
14. **Full quality gate.** §10 run end-to-end with evidence
    (screenshots at three depths, JS-off load, throttled load,
    screen-reader pass of the index and one column). Any blocking
    failure returns the build to the step that owns it.

---
