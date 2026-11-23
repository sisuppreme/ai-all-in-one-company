# 99. The Grand Tour Ledger — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never
redesigned).** A travel house run like a 19th-century expedition
ledger — every journey is an account opened in a great book,
stamped, ruled and balanced; luxury travel presented as the
bookkeeping of wonders. Palette anchors: ledger paper `#F3ECDC`,
iron-gall ink navy `#26324B`, wax-seal red `#9C2B2B`, baize green
`#6B7F5E`, gilt rule `#B08D4F`. Type: Cinzel (display — engraved
capitals) + EB Garamond (entries), tabular lining figures
throughout so columns of figures align like accounts. Layout: a
great book — red-ruled ledger lines, folios, ribbon markers;
journeys are entries, each ruled under as completed; destination
stamps slam at a slight rotation; the foot of the page strikes a
balance. The original entry's honesty detail is kept verbatim as
the theme's conscience: the ledger includes a *"Disbursements &
Disappointments"* column — one entry reads *"Day 9: rain. Charged
to experience."*

## 1. Concept & world

The Grand Tour Ledger is the website of a house that keeps
books the way other houses keep brochures. Its founding fiction
is precise: sometime in the age of the grand tour, a travel
house decided that a journey was not a product but an *account*
— opened when a traveller walked in, posted entry by entry as
the journey was planned and then lived, and balanced at the end
against what the world actually delivered. The great book never
closed. This page is that book, still open on the desk: its
paper is the page ground, its ink is the text colour, its red
ruling is the grid, its wax seal is the only authority mark, and
every journey the house sells appears not as a card in a feed
but as an entry — dated, itemised, stamped on arrival, and ruled
under when it is complete. Luxury here is not marble or gold
leaf; it is *procedure performed beautifully*. Any clerk can
post an entry. This house posts it with a swelling pen, blots it
before it dries, stamps it slightly crooked because a hand did
it, and strikes the balance in public at the foot of the page.

The world the page performs is the desk of that book: warm
lamplight on gilt edges (§5, §6.8), the ribbon that keeps the
reader's place sliding from folio to folio (§6.10), the seal
coming down before a word is read (§6.1), the headline engrossed
— written out fair, in the house's best hand — rather than set
(§6.2). Nothing arrives on this page by appearing. It arrives by
being *posted*: written, dried, ruled, stamped. That verb is the
theme's whole motion grammar, and every element in §6 is a tense
of it. The reader is not a user; the reader is a traveller whose
account is being kept, and the page's politeness is the
politeness of a clerk who has all day and intends to use it on
you.

**The theme's one law: the book balances, or the book says
why.** Two clauses, both audited by the gate (§10). (1) *Every
figure is a posting.* Every number the page prints — miles,
nights, wonders, prices, the great balance itself — is either an
entry on the page (a line in a journey's account, a row in the
disbursements table) or a sum of entries printed on the page,
with the addition performable by the reader from what is
visible. The struck balance (§6.5) totals the entries above it
and nothing else; a journey card's "from £4,850" is the sum of
its own itemised lines or it is not printed. A figure that
cannot be traced to a posting is a smuggled number, and a
smuggled number in a ledger is not a rounding error — it is the
one fraud this house cannot survive, because the entire fiction
is that the book can be trusted. (2) *The disappointments are
posted too.* Every journey account carries its disbursements and
its disappointments in the same ink as its wonders (§6.13): the
rain day, the closed pass, the extra night bought at full price.
A Grand Tour page in which nothing ever went wrong is a
brochure wearing a ledger's clothes, and it fails the gate on
sight. The law's corollary governs motion as much as figures:
an entry may be *performed* (written, blotted, stamped) only
over its complete printed text (§6.3) — the performance is the
house's ceremony, never a condition of the content existing.

**Best-fit sites and audiences.** Luxury and bespoke travel
first, literally: private tour ateliers, expedition and polar
cruise operators, rail-journey houses, safari planners,
concierge and relocation services, heritage hotels that sell a
stay as a chapter. Then any business whose truth is *a long
engagement, itemised honestly*: bespoke tailors and
cabinet-makers with commission books, private banks and family
offices (the ledger is their native furniture), expedition
outfitters, rare-book and map dealers, restoration ateliers,
schools selling a multi-year course of study as an account of
terms. The audience it suits keeps receipts and distrusts
gloss: travellers who read an itinerary the way auditors read
accounts, who find a struck balance more persuasive than a
superlative, and who will forgive a house almost anything
except a number that appears from nowhere. Conversion on such
sites is an account opened — an enquiry posted, a consultation
booked, a deposit entered — acts performed in the book's own
ritual (§6.14), never a checkout bolted onto the side of it.

**When NOT to use it.** Not for anything sold by urgency:
flash sales, last-seat countdowns, dynamic-pricing flight
search — the house does not hurry, and a countdown timer in
Cinzel is a forgery. Not for high-volume inventory (four hundred
hotel rooms cannot be entries; the book holds dozens of
accounts, not thousands). Not for apps, dashboards or anything
the reader operates rather than reads — a ledger is consulted,
not driven. Not where the client cannot itemise: §6.12's cards
and §6.5's balance require real component figures, and a house
that will only print a single glossy total cannot keep this
book. Not for brands whose voice is irreverent or minimal — the
theme's courtesy is load-bearing, and stripping it leaves a
spreadsheet in a serif font (§9, failure 8).

## 2. Palette

Five anchors, inherited exactly. Derived tokens form a closed
list: a token not in this table does not exist in the theme, and
the gate greps built CSS for undeclared hex values. Contrast
ratios below were computed for this expansion from the hex
values (WCAG relative-luminance formula).

| Token | Hex | Role | Usage ratio | Pairing & contrast (computed) |
|---|---|---|---|---|
| `--paper` | `#F3ECDC` | Ledger paper — the page ground, entry leaves, card stock | ~52% of viewport area | Carries `--ink` at **10.88:1**, `--ink-deep` at 13.62:1, `--seal-deep` at 8.61:1, `--baize-deep` at 6.63:1. The ground everything is posted on; never a text colour on any other token except `--ink` and `--baize-deep` grounds. |
| `--ink` | `#26324B` | Iron-gall ink navy — body text, entry text, figures, the engrossed headline | ~26% | On paper 10.88:1 — the reading pairing. On `--paper-shade` 9.40:1. Carries `--paper` at 10.88:1 and `--gilt-pale` at 6.98:1 when it is itself the ground (the closing leaf, §6.17). Never carries `--seal` (1.70:1 — **forbidden**: red ink is never written on the navy leaf). |
| `--seal` | `#9C2B2B` | Wax-seal red — the seal, destination stamps, stamp ink, the one warm authority mark | ≤3% (rationed, §5) | On paper **6.39:1** — stamps and ≥14px stamp text only; small red text uses `--seal-deep` (8.61:1). On ink forbidden (above). A page where red exceeds the ration has confused a seal with a colour scheme (§9, failure 4). |
| `--baize` | `#6B7F5E` | Baize green — the desk cloth: section grounds for the disbursements leaf, ribbon-adjacent panels, graphical fields | ~10% | On paper **3.70:1** — graphical and large display only, never body text; text in the green register is `--baize-deep` (6.63:1 on paper, and paper on baize-deep 6.63:1). |
| `--gilt` | `#B08D4F` | Gilt rule — the fore-edge, rules that are ornaments, folio furniture, the balance's double rule | ~6% | On paper **2.64:1** — a metal, never text. Text in the gilt register is `--gilt-deep` (4.87:1, ≥14px only). On ink grounds the gilt voice is `--gilt-pale` (6.98:1). A gilt rule is drawn, not typed. |
| `--ink-deep` (derived) | `#182136` | Dried iron-gall — the headline at full strength, footer ground, the closed-book leaf | — | On paper 13.62:1. The ink after a century in the book: darker than the writing ink because it has finished drying forever. |
| `--ink-soft` (derived) | `#4A5872` | Pencil navy — captions, apparatus, source lines, the clerk's marginal hand | — | On paper 6.09:1. Never body text; the apparatus voice (§12). |
| `--paper-shade` (derived) | `#E7DCC2` | The shaded leaf — alternate entry grounds, card stock, the blotting paper's tone | — | Carries ink at 9.40:1 and seal-deep at 7.44:1. The page turned toward the lamp's edge. |
| `--seal-deep` (derived) | `#7C1F1F` | Old wax, in shadow — small red text, stamp captions, error ink | — | On paper 8.61:1; on paper-shade 7.44:1. The only red licensed below 14px. |
| `--baize-deep` (derived) | `#46573D` | Baize in shadow — green text, the disbursements leaf ground, ribbon deep tone | — | On paper 6.63:1; carries paper at 6.63:1. The desk cloth where the lamp does not reach. |
| `--gilt-deep` (derived) | `#7D6230` | Tarnished gilt — gilt-register text ≥14px, folio numerals on paper | — | On paper 4.87:1 — labels and numerals only, never body. |
| `--gilt-pale` (derived) | `#D9BC7F` | Gilt under lamplight — gilt-register text on ink grounds | — | On ink 6.98:1. The fore-edge catching the lamp on the closing leaf (§6.17). |
| `--ruling` (derived) | `#B98A8A` | The red ruling — ledger lines, entry rules, table hairlines | — | On paper 2.53:1 — a line, never text, never a border thicker than 1px. The ruling is printed on the paper before the house writes a word; it is furniture, not emphasis. |

**Usage discipline.** Half the page is paper, a quarter is ink
(as text mass, not area), a tenth is baize field, gilt is a
rule's width everywhere and a field almost nowhere, and wax red
is a rounding error with authority. The ratio is audited in the
gate (§10) by screenshot sampling: seal-red pixels above 4% of
any viewport means the stamps have become branding. Gilt is
rationed by geometry rather than area — it may run the full
fore-edge (§6.8) because an edge is a line, but it may never
fill a panel, a button or a background; the moment gilt is a
surface, the book has been gilded shut and cannot be read
(§9, failure 5).

**Dark behaviour — the book is read by lamplight, or it is not
read at all.** The Grand Tour Ledger is a light theme by
physics: ledgers are paper, and paper in the dark is a rumour.
The theme therefore has **no dark mode and no inversion**. Under
`prefers-color-scheme: dark`, the page does not pretend the
ledger went navy; instead the lamp narrows: `--paper` grounds
hold exactly as printed, the candle-warm light field (§5) tightens
its radius by 20% and warms by one step, the baize sections
deepen toward `--baize-deep` as their ground (paper text on it
holds at 6.63:1), and the closing leaf (§6.17) — already ink —
becomes the page's natural resting state rather than a contrast.
Every text pairing in the table keeps its class: no ratio moves,
because no ground that carries text changes value class. A build
that ships a "dark ledger" by inverting paper to charcoal has
made the book out of the desk and fails §9.

## 3. Typography

**Faces.** Cinzel (display — engraved capitals, used the way a
title is engrossed on a book's opening leaf: sparingly, largely,
and never for anything the clerk would simply write) + EB
Garamond (everything else — entries, body, figures, forms,
apparatus). Two faces is the whole library: the engraved hand
and the writing hand. A third face — a sans for UI, a mono for
data — is a foreign clerk in the office and is refused (§11
carries the full refusals list). EB Garamond is chosen because
its old-style figures are beautiful and its **tabular lining
figures** are the theme's accounting instrument: with
`font-feature-settings: "tnum" 1, "lnum" 1` set as law on every
figure-bearing element, columns of miles and pounds align to the
pen stroke, which is the entire visual argument of §6.5.

**The scale** (desktop; §6 breakpoint tables carry the smaller
sizes):

| Role | Face | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Hero display | Cinzel 600 | 56px / 1.08 | +0.04em | The engrossed headline (§6.2); max 7 words (§12) |
| Section display | Cinzel 600 | 34px / 1.15 | +0.05em | Leaf titles; one per leaf, at its head |
| Entry head | EB Garamond 600 | 24px / 1.25 | 0 | Journey names inside accounts (§6.3) |
| Calligraphic name | EB Garamond 500 italic, SVG-stroked | 40–64px | — | Destination names (§6.7); drawn, not set |
| Body / entry text | EB Garamond 400 | 18px / 1.55 | 0 | Measure 60–68ch (§4) |
| Body small | EB Garamond 400 | 16px / 1.5 | 0 | Card lines, table cells |
| Caption / apparatus | EB Garamond 500 | 13.5px / 1.45 | +0.02em | `--ink-soft`; source lines, folio furniture |
| Data numerals | EB Garamond 500, tnum+lnum | 30px (balance) / 18px (inline) | 0 | The accounts' figures (§6.5, §6.12); never Cinzel |
| Stamp text | Cinzel 700 | 13–15px | +0.12em | Inside stamp rings (§6.4); the only letterspaced small text |
| Form labels | EB Garamond 600 | 14px / 1.4 | +0.03em | `--ink`; the form is a leaf of the book (§6.14) |

**Five type laws.**
1. **Figures are tabular, or they are not printed.** Every
   numeral that participates in an account — prices, miles,
   nights, dates in tables, the balance — sets in EB Garamond
   with `tnum` and `lnum` forced on. A proportional figure in a
   column is a lie about addition: the eye cannot sum what does
   not align. Decorative numerals (folio numbers, §6.11) are
   also tabular, because on this page there are no decorative
   numerals — only postings and furniture from the same hand.
2. **Cinzel is engraved, never written.** Cinzel appears in
   exactly four places: leaf titles, the hero headline, stamp
   rings, and the book's name on the closing leaf. Body copy,
   buttons, labels and prices in Cinzel are a title case
   accident, not a style (§9, failure 8). If a string would be
   spoken by the clerk, it is Garamond; if it would be cut into
   the cover, it is Cinzel.
3. **The handwriting is a performance, never the text.** The
   engrossing (§6.2), the writing-in (§6.3) and the calligraphic
   names (§6.7) are stroke performances laid *over* complete,
   typeset text that is present from first paint. No build may
   make the reader wait for a letter to exist: the performance
   reveals, the print *is*. This is §1's corollary in the type
   layer, and the gate tests it with JavaScript disabled.
4. **Italics are the traveller's voice.** EB Garamond italic is
   reserved for what the traveller said or lived — journal lines
   inside entries, the disappointments column's confessions
   (§6.13), testimonial letters (§6.15). The house itself never
   writes italic: apparatus, errors, prices and rules are
   upright, because the clerk does not murmur over the accounts.
5. **No letterspaced lowercase, ever.** Tracking exists only on
   Cinzel capitals and stamp text. Letterspaced Garamond
   lowercase is a wedding invitation that wandered into a
   counting house (§9, failure 8).


## 4. Layout language

**The great book.** The page is one volume, read top to bottom
the way a ledger is kept: opening leaf (hero), contents leaf
(§6.11), the accounts themselves (entries, §6.3; journey cards,
§6.12), the honesty leaf (disbursements, §6.13), the
account-opening leaf (the form, §6.14), the letters leaf
(§6.15), and the closing leaf where the balance is struck and
the book is signed (§6.17). Each major section is a *leaf*: a
paper field bounded above by a gilt head-rule and below by the
rule its last entry draws (§6.3), with its folio numeral printed
in the outer margin in `--gilt-deep`. Leaves are never cards on
a background — the paper *is* the background, continuous from
the first leaf to the last, and the only ground changes licensed
are the baize desk showing at the disbursements leaf (§6.13) and
the ink closing leaf (§6.17), the desk and the book's cover
making their two appearances.

**Grid and ruling.** One content column at 60–68ch, centred,
ruled throughout: horizontal `--ruling` hairlines every 28px
(the ledger's line rhythm, `--rule-unit`) run behind entry
leaves only — never behind display type, never behind the form's
fields, where the ruling becomes the field's own underline
(§6.14). The vertical margin rule — the ledger's red margin
line — runs at the column's left edge on entry leaves, and the
folio furniture (numerals, ribbon, stamps' resting place) lives
outside it, in a 72px margin rail at ≥1200px. Figures right-align
to a shared decimal axis at the column's right edge; the balance
(§6.5) is set on that same axis, so the eye that has read a
hundred entry figures arrives at the total already aligned.

**Density law.** Entries are rationed: a leaf holds at most 5
full entries or 6 journey cards, and at any scroll position at
most one performance may be running — one entry writing, one
stamp falling, one name being lettered — because a desk where
three clerks perform at once is a theatre, not a counting house
(§9, failure 7). Vertical rhythm is the ruling's: leaf padding
is always a whole number of `--rule-unit`s (4 units = 112px
desktop), so entry baselines land on the printed lines the way
handwriting lands on a ruled page — the single most convincing
detail in the theme, and the cheapest.

**Section choreography.** Grounds follow a declared order —
paper, paper, paper-shade, baize (disbursements only), paper,
ink (closing only) — never two shaded leaves in a row (the book
would feel thumbed) and never a baize leaf anywhere but under
the accounts' honesty table, where the desk is the right ground
for bad news. Each leaf's Cinzel title sits directly under its
gilt head-rule; the first entry's head sits exactly 2 rule-units
below it, so every leaf opens with the same held breath.

**The reading line and the ribbon.** Progress in this book is
not a bar: it is the ribbon (§6.10) resting in the margin at the
reader's current leaf, and the gilt fore-edge (§6.8) darkening
down the page's right edge. The internal measurement both are
keyed to is the reading line at 55% of viewport height — the
line an entry crosses to be posted (§6.3), a stamp crosses to
fall (§6.4), a figure crosses to join the balance (§6.5). It is
never drawn. A build that renders it has mistaken the clerk's
straightedge for furniture.

## 5. Full motion system

One shared `requestAnimationFrame` loop drives every scrubbed
value in the theme — the balance's digit wheels, the gilt edge,
the ribbon's slide, the lamp's breath — reading a single lerped
scroll progress (`lerp 0.12`) and writing only transform,
opacity and registered custom properties. No scroll handler
writes styles. Named easings, a closed list — an easing not in
this table does not exist in the theme:

| Easing token | Curve | Used by |
|---|---|---|
| `--ease-seal` | `cubic-bezier(.2,1.6,.35,1)` with a squash beat | The wax seal (§6.1), stamp falls (§6.4) |
| `--ease-engross` | `cubic-bezier(.45,0,.2,1)` | Engrossing strokes (§6.2), calligraphic names (§6.7) |
| `--ease-rule` | `cubic-bezier(.6,0,.3,1)` | Rules drawing (§6.3, §6.5), gilt head-rules |
| `--ease-blot` | `cubic-bezier(.3,.7,.3,1)` | Blotting masks lifting (§6.6) |
| `--ease-post` | `cubic-bezier(.25,.8,.3,1)` | Entries settling (§6.3), cards (§6.12), the bill of leaves |
| `--ease-ribbon` | `cubic-bezier(.5,0,.2,1)` | Ribbon slides (§6.10), page turns (§6.10) |
| `--ease-lamp` | `cubic-bezier(.4,0,.6,1)` | The lamp breath, ink warming (§6.9), candle-warm light |
| `--ease-wheel` | `cubic-bezier(.3,.9,.3,1)` | Digit wheels (§6.5) |

**Scroll-triggered reveals** are postings: an entry crosses the
reading line, writes in over its printed text (§6.3), is blotted
(§6.6) and ruled under; a section's destination stamp falls as
its leaf locks (§6.4). Nothing fades up from below — paper does
not rise; ink dries. **Scroll-driven scrub** carries three
values only: the struck balance's wheels (§6.5), the gilt edge's
patina (§6.8), and the lamp field's slow travel down the book
(§6.9's ambient half). **Pinned scene:** the hero leaf pins for
120vh while its first three entries are written in sequence —
the only pin in the theme, because a book opened flat on a desk
is the one honest pin this world owns. **Masked reveals** are
the blotting masks (§6.6): a paper-textured mask that lifts off
drying ink, never a clip-path wipe borrowed from a video theme.
**Blur-to-sharp** is refused as a reveal — ink is never out of
focus on paper; the one softness licensed is wet-ink sheen
(§6.6), a specular gradient, not a blur. **Counters** are the
digit wheels (§6.5) and the tallies inside journey cards
(§6.12) — odometer wheels in tabular Garamond, never a
count-up in a sans. **Progress indicator** is the ribbon
(§6.10) plus the fore-edge (§6.8): two instruments, both
objects in the world. **Marquee** is refused — a ledger does not
shout along a ticker; the contents leaf (§6.11) is the theme's
answer to navigation anxiety. **Kinetic typography** is the
engrossed headline (§6.2) and the lettered destination names
(§6.7) — type that moves by being *written*, stroke by stroke.
**Ambient loop:** exactly one — the candle-warm lamp breath
across the gilt edges, a ±4% luminance swell on a 7s
`--ease-lamp` cycle, plus the paper grain's faint shift inside
it. A second ambient loop would make the desk fidget (§9,
failure 6). **Micro-interactions:** ink-deepening hover (§6.9),
stamp-slam clicks (§6.4), the seal's press on the form's submit
(§6.14), ribbon grabs (§6.10) — all under 400ms except the
ceremonies the theme exists for. **Page transitions** are
ribbon-marked leaf turns (§6.10): 700ms, heavy, with the ribbon
sliding to the new folio. **Image treatment:** photographs are
entered as *plates* — pasted into the book on paper-shade mounts
with a gilt hairline, scaling 1.03→1 inside the mount as the
leaf is posted (§6.12); an image that fills its frame edge to
edge is a screen habit, not a book habit. **Skeleton loading**
is the unposted leaf (§6.16): ruled lines and a pencilled folio,
written over within 900ms or left honestly blank-ruled.
**Reduced motion:** the ledger shown fully written and ruled,
seal static, balance printed at its struck totals, ribbon at
rest — §6 carries the per-element variant, and §13 maps the
whole page in that state.

## 6. Signature elements

### 6.1 The wax seal

- **What & why.** On load, before any other motion, a wax seal
  — 84px disc of `--seal` with the house's engraved device (a
  Cinzel "G·T" monogram inside a double ring) — falls onto the
  hero leaf's head, overshoots, squashes, and holds, while a
  thin ink ring spreads from beneath its edge across the paper.
  It belongs because the book is *opened under seal*: the house
  warrants the accounts that follow before it asks to be read,
  and the seal is the only element in the theme allowed to be
  pure ceremony — its content is the warranty itself.
- **Structure.** An inline SVG disc (two concentric rings, the
  monogram as Cinzel text on a path, an irregular wax edge path
  with 7 lobes so it reads as poured, not machined) inside a
  `<figure class="seal" aria-hidden="true">`, positioned over
  the hero leaf's gilt head-rule, right of the title. The ink
  ring is a separate SVG ellipse stroke beneath it. The DOM
  ships the seal at rest, fully formed; the fall is a transform
  performance armed by JS only.
- **Motion spec.** Trigger: load, once per session
  (`sessionStorage` — a returning traveller finds the book
  already open and sealed). t=0 (gated on
  `document.fonts.ready` raced against 700ms; the monogram must
  fall in Cinzel or not at all — race lost, seal ships at rest):
  seal drops from translateY(−26px) scale(1.06) over 260ms
  `--ease-seal`; impact squash scaleY(0.88) scaleX(1.07) at
  260–340ms; settle to rest by 520ms. Ink ring: stroke draws
  and fades to 55% opacity 300–900ms `--ease-rule`. Total
  ceremony 900ms, then §6.2 arms. Watchdog 1400ms (§ below).
- **States.** Unsealed (JS-armed pre-state, seal held above the
  leaf) → falling → sealed (rest). Hover: none — the seal is
  not a control. Focus: none. Scrolled-past: sealed; the seal
  never re-falls on scroll return. Disabled/no-JS: printed
  sealed at first paint.
- **Content merge.** The seal lands on the hero leaf's own
  head-rule and its monogram is the house's mark that recurs on
  the closing leaf's signature (§6.17) and the form's
  confirmation (§6.14) — one device, three postings, so the
  warranty given at the opening is the warranty honoured at the
  close.
- **Failure fallback.** Watchdog at 1400ms from DOMContentLoaded:
  if the fall has not completed, transforms are cleared and the
  seal stands at rest. No JS: never armed. Slow network: the
  seal is inline SVG in the HTML; the ceremony script is
  deferred and the watchdog runs regardless.
- **Reduced-motion variant.** No fall, no ring spread. The seal
  stands printed; the ink ring is present at its resting 55%.
- **Performance budget & mobile variant.** One SVG ≤3KB, one
  transform animation, no filters. Mobile (<768px): seal 64px,
  drop distance −18px, ceremony 700ms — a smaller book, the same
  wax.
- **Choreography timeline (v2).** t=0 fonts ready (or race lost
  → rest) → t=0–260 fall → t=260–340 squash → t=300–900 ink ring
  draws → t=520 seal at rest → t=900 ring at rest, §6.2 arms →
  watchdog ceiling 1400ms.
- **State matrix (v2).** *Rest:* sealed, ring at 55%. *Hover:*
  none. *Focus:* n/a (not focusable). *Active:* n/a.
  *Scrolled-past:* sealed; unchanged. *Disabled:* printed.
  *Touch:* identical; no tap behaviour — a seal is not pressed
  twice.
- **Breakpoints (v2).** ≥1200px: 84px disc, drop −26px, 900ms.
  768–1199px: 76px, −22px, 850ms. <768px: 64px, −18px, 700ms,
  positioned above the title rather than right of it (the leaf
  is narrower than the ceremony).
- **Edge cases & failure modes (v2).** *Tab hidden mid-fall:*
  rAF pauses; on return, wall-clock past 1400ms fires the
  watchdog and the seal rests. *Hero title edited in a CMS:*
  the seal's anchor is the head-rule, not the title's geometry —
  it survives edits. *Second visit:* session flag ships it
  sealed; the book does not re-warrant itself hourly.
- **Accessibility spec (v2).** The seal is decorative ceremony
  over a complete page: `aria-hidden`, never focusable, never
  announced. The house's name and warranty exist as real text in
  the hero standfirst (§12), so nothing the seal "says" is lost
  to a screen reader.
- **Tokens consumed (v2).** `--seal`, `--seal-deep` (monogram
  shadow ring), `--gilt` (inner ring hairline), `--paper`,
  `--ease-seal`, `--ease-rule`, `--dur-seal` (900ms),
  `--dur-watchdog-seal` (1400ms).

### 6.2 The engrossed headline

- **What & why.** The hero headline — Cinzel capitals, ≤7 words
  (§12) — is engrossed: each letter's strokes swell thick-thin
  in calligraphic order, as a fair hand writes a title out in
  full before the book's work begins. It belongs because the
  title of a ledger is not set by a machine; it is the one line
  the house writes *beautifully on purpose*, and its slow
  arrival (after the seal, §6.1) is the house clearing its
  throat. The performance is stroke work over print (§3 law 3):
  the headline exists, typeset and complete, from first paint.
- **Structure.** A real `<h1>` in Cinzel at full contrast. Above
  it, an `aria-hidden` SVG layer holds one stroked path per
  letter-group (3–5 paths for a 7-word headline, grouped by word
  so the hand "lifts" between words), each path drawn with a
  variable-width stroke technique: two overlaid paths — a 1px
  hairline full draw plus a swelling path whose stroke-width is
  animated via a mask — producing the thick-thin of a nib. The
  overlay is removed from the DOM at completion.
- **Motion spec.** Trigger: load, armed at §6.1's t=900 (or
  immediately if the seal shipped at rest). Per word: hairline
  draws 240ms `--ease-engross`; swell follows 120ms behind,
  300ms; word gap 90ms. A 4-word headline completes in ~1900ms;
  ceiling for 7 words 2600ms. The standfirst (Garamond) posts
  beneath at completion +150ms via §6.3's settle. Watchdog
  3200ms.
- **States.** Printed (DOM state, always) → engrossing (overlay
  performing) → engrossed (overlay removed). Hover/focus: none.
  Focus entering the hero mid-performance completes it instantly
  — a keyboard traveller is never asked to watch a pen before
  reading. Scrolled away mid-performance: it completes on its
  own clock; the headline is whole on return.
- **Content merge.** The headline is the page's actual title and
  the book's name for the season's journeys — the performance
  writes the content, not an intro sting; there is no separate
  "hero copy" beneath it waiting to be the real one.
- **Failure fallback.** Watchdog 3200ms removes the overlay
  mid-stroke if anything stalls. No JS: no overlay is inserted;
  the headline is simply engraved print. Fonts race lost
  (Cinzel late): overlay never arms — strokes drawn in a fallback
  face would be a forged hand.
- **Reduced-motion variant.** No overlay. The headline stands in
  Cinzel, and the gilt head-rule above it (§6.1's leaf) carries
  the ceremony instead, drawn once at rest at full length.
- **Performance budget & mobile variant.** ≤5 SVG paths, stroke
  animation on the compositor via `stroke-dashoffset`; overlay
  ≤6KB. Mobile: headline 34px, per-word draw 180ms, ceiling
  1800ms — the hand writes smaller and slightly faster, as hands
  do in smaller books.
- **Choreography timeline (v2).** t=0 armed → per word: t+0
  hairline 240ms → t+120 swell 300ms → t+510 next word (90ms
  lift) → final word +150ms standfirst posts → overlay removed
  at completion → watchdog ceiling 3200ms.
- **State matrix (v2).** *Rest:* printed, overlay absent.
  *Hover:* none. *Focus:* focus-within completes instantly.
  *Active:* n/a. *Scrolled-past:* completed. *Disabled:* printed.
  *Touch:* identical; first touch inside the hero completes it.
- **Breakpoints (v2).** ≥1200px: 56px, ceiling 2600ms.
  768–1199px: 44px, ceiling 2200ms. <768px: 34px, per-word 180ms,
  ceiling 1800ms; headlines over 5 words wrap to two lines and
  engross line by line, never letter by letter across the break.
- **Edge cases & failure modes (v2).** *Headline over 7 words:*
  refused at build (§12) — a title that needs 8 words is two
  titles. *CMS edit:* the overlay is generated from the printed
  text at build time; an edit without regeneration ships print
  only (the safe failure). *Very long single word:* grouped as
  one path; swell mask scales; ceiling still enforced by the
  watchdog.
- **Accessibility spec (v2).** The `<h1>` is complete in the
  accessibility tree from first paint; the overlay is
  `aria-hidden`. Contrast is the print's at all times — ink-deep
  on paper 13.62:1 — because the readable layer never leaves.
- **Tokens consumed (v2).** `--ink-deep`, `--ink`, `--paper`,
  `--gilt`, `--ease-engross`, `--dur-engross-word` (510ms),
  `--dur-watchdog-engross` (3200ms).

### 6.3 Entries written and ruled

- **What & why.** The theme's core element. Each journey entry —
  head (Garamond 600 name + dates), itemised lines (legs, stays,
  guides, each with its figure), and a closing line — is posted
  as it crosses the reading line: the printed entry settles from
  a faint wet-ink sheen to matte while a ruling line draws itself
  beneath it in `--ruling`, left to right, the clerk's
  straightedge finishing the account. It belongs because posting
  *is* the site's verb: content does not appear on this page, it
  is entered, and the drawn rule is the full stop of bookkeeping —
  this account is complete and the next may begin.
- **Structure.** A `<section class="entry">` per journey: real
  semantic HTML — `<h3>`, a `<table>` or definition list for the
  itemised lines (figures in tabular Garamond, right-aligned to
  the shared decimal axis, §4), a journal line in italic (§3 law
  4). The rule is an SVG line (or a scaled `<hr>` with a gilt
  end-cap) beneath the entry, `scaleX` 0→1 armed by JS. The wet
  sheen is a specular gradient layer over the entry's text block,
  removed at dry time by §6.6's blot.
- **Motion spec.** Trigger: entry's head crosses the reading
  line (55% vh), once. Settle: sheen fades 600ms `--ease-post`;
  rule draws 500ms `--ease-rule` beginning at +200ms; the entry's
  stamp (§6.4) falls at +650ms if the leaf carries one. Entries
  stagger only by scroll — two entries crossing in one frame post
  140ms apart, never simultaneously (§4 density law). Watchdog
  1600ms per entry.
- **States.** Printed (DOM) → posting (sheen + rule drawing) →
  posted (ruled, matte). Hover: §6.9's ink-deepening. Focus:
  an entry receiving focus posts instantly (rule at full length)
  — the clerk turns to the page you asked for. Scrolled-past:
  posted; scrolling back up never un-posts an entry (the book
  does not unwite itself).
- **Content merge.** The element *is* the content unit of the
  whole theme: a journey's real itinerary and real figures,
  itemised so §6.5 can sum them and §6.12 can card them. An
  "entry" containing marketing copy instead of an itemised
  account is a poster in the book and fails §10.
- **Failure fallback.** Watchdog 1600ms: rule snaps to full,
  sheen removed. No JS: entries stand printed and *unruled* —
  the build ships a CSS default rule at 30% ruling tone so the
  leaf still reads as a ledger without the ceremony. Slow
  content (CMS entries arriving late): the observer arms on
  insertion; an entry inserted above the reading line posts
  instantly.
- **Reduced-motion variant.** Entries stand printed, rules drawn
  at full length in resting ruling tone, no sheen. The leaf
  reads as a finished page of the book — which is the point.
- **Performance budget & mobile variant.** Per entry: one
  gradient layer + one line transform; ≤12 entries perform per
  page. Mobile: rule draw 380ms, sheen skipped below 768px if
  the device reports `save-data` or a 2-core CPU (the entry
  posts by its rule alone).
- **Choreography timeline (v2).** t=0 head crosses reading line
  → t=0–600 sheen settles → t=200–700 rule draws → t=650 stamp
  arms (§6.4) → t=700 entry posted → §6.6 blot completes the dry
  by t≈1100 → watchdog ceiling 1600ms.
- **State matrix (v2).** *Rest (posted):* ruled, matte, figures
  aligned. *Hover:* ink deepens (§6.9). *Focus:* instant post if
  unposted. *Active:* n/a. *Scrolled-past:* posted, permanent.
  *Disabled:* printed with default rule. *Touch:* identical;
  no tap behaviour on the entry body (its links and stamp keep
  theirs).
- **Breakpoints (v2).** ≥1200px: full itemisation, margin rail
  carries folio + stamp. 768–1199px: itemised lines compress to
  two columns (item, figure), journal line full width. <768px:
  lines stack item-over-figure left-aligned — the decimal axis
  is surrendered below 768px and figures left-align in tabular
  Garamond rather than pretending to a column that no longer
  fits; rule draw 380ms.
- **Edge cases & failure modes (v2).** *Entry longer than the
  design expects (12+ lines):* posts in two beats — head + first
  6 lines, rule withheld until the entry's foot crosses the
  reading line, then the rule draws: an account is ruled when it
  *ends*, not when it starts. *Entry with no figures* (a pure
  journal entry): licensed once per leaf, marked in the margin
  "no charge" in the clerk's hand — the book admits a free entry
  rather than inventing a figure (§1). *Rapid scroll fling:*
  entries above the line post instantly in bulk (catch-up rule,
  §13) — the reader never arrives at an unposted account.
- **Accessibility spec (v2).** Entries are landmarks by heading;
  figures are real table text, summed by AT from the same DOM
  §6.5 sums visually. The rule and sheen are `aria-hidden`.
  Focus order follows the book: head, lines, journal, next
  entry. Contrast: ink on paper 10.88:1 at rest and during the
  sheen (the sheen is a specular layer *over* print, never a
  lightening of it).
- **Tokens consumed (v2).** `--paper`, `--paper-shade`, `--ink`,
  `--ink-soft`, `--ruling`, `--gilt`, `--ease-post`, `--ease-rule`,
  `--dur-post` (600ms), `--dur-rule` (500ms), `--dur-watchdog-entry`
  (1600ms), `--rule-unit` (28px).

### 6.4 Destination stamps

- **What & why.** As each itinerary leaf locks — its last entry
  posted — its destination stamp falls: a circular double-ring
  stamp in `--seal`, the destination's name in letterspaced
  Cinzel around the ring, its date in tabular Garamond at the
  centre, landing at a slight rotation (2–4°, seeded per stamp,
  § below) with an ink-ring pulse spreading from the contact
  edge. It belongs because a ledger of journeys needs its
  arrivals *certified*, and certification by hand is never quite
  straight: the rotation is the fingerprint of the clerk, and a
  page of perfectly aligned stamps would be a print shop, not a
  passport desk. Stamps also answer clicks anywhere the theme
  invites commitment (cards §6.12, the form §6.14) — one gesture
  of assent across the whole book.
- **Structure.** Inline SVG per stamp: outer ring 2px, inner
  ring 1px, name on a circular text path (Cinzel 700, +0.12em),
  date centred (Garamond tabular), a faint ink-texture mask so
  the impression is uneven — heavier at the contact edge, lighter
  opposite, like a real pad running dry on one side. Rotation is
  a custom property `--stamp-rot` set from a seeded value
  (destination name hashed to 2.0–4.0°, sign alternating by leaf
  order) — *seeded, never random at runtime*, so the book stamps
  the same way on every visit and two builders produce the same
  page. The stamp is `aria-hidden` decoration over a printed
  "Arrived" line in the entry itself (see Accessibility).
- **Motion spec.** Trigger: leaf lock (last entry posted) or
  click on a stampable control. Fall: from translateY(−14px)
  scale(1.12) opacity 0 → contact in 180ms `--ease-seal`;
  squash scaleY(0.94) 180–240ms; ink pulse ring expands 14→46px
  fading 240–700ms `--ease-rule`; stamp settles at its rotation
  by 260ms. Total 700ms. A stamp falls once per leaf per session;
  click-stamps on controls repeat the pulse but not the fall.
- **States.** Unstamped (armed, invisible — the only element in
  the theme permitted an invisible pre-state, because its
  content twin is printed, below) → falling → stamped (rest,
  ink at 92% with texture). Hover on a stamped leaf: the stamp
  warms — `--seal` → a 6% lighter mix — with §6.9's lamp ease.
  Focus: a leaf reached by keyboard stamps instantly at rest.
  Scrolled-past: stamped. Disabled/no-JS: the printed "Arrived ·
  {destination} · {date}" line stands alone, complete.
- **Content merge.** The stamp certifies the leaf's real
  destination and the real date the itinerary's last entry
  carries — it is the entry's own metadata performed, and the
  closing leaf's totals (§6.17) count stamped leaves as
  "journeys on the books." A stamp over a section that is not an
  itinerary is a seal on an empty envelope (§9, failure 4).
- **Failure fallback.** Watchdog 1100ms from leaf lock: stamp
  snaps to rest at its seeded rotation. The printed Arrived line
  is the permanent fallback — with JS dead, the page loses the
  slam and keeps the fact.
- **Reduced-motion variant.** The stamp stands printed at its
  rotation, full texture, no fall, no pulse. The rotation is
  kept — stillness is not the same as straightness.
- **Performance budget & mobile variant.** One SVG ≤4KB per
  stamp, ≤6 stamps per page; texture is a static mask, never an
  animated filter. Mobile: stamp 72px (from 92px), fall distance
  −10px, pulse capped at 34px.
- **Choreography timeline (v2).** t=0 leaf locks (or click) →
  t=0–180 fall → t=180–240 squash → t=240–700 ink pulse →
  t=260 stamp at rest rotation → watchdog ceiling 1100ms.
- **State matrix (v2).** *Rest:* stamped, textured, rotated.
  *Hover:* warms 6% (leaf-level). *Focus:* instant stamp.
  *Active (click-stamp controls):* pulse repeats, fall does not.
  *Scrolled-past:* stamped. *Disabled:* printed Arrived line
  only. *Touch:* identical; tap targets that stamp are ≥44px.
- **Breakpoints (v2).** ≥1200px: 92px stamp in the margin rail,
  overlapping the entry's last line by 12px. 768–1199px: 84px,
  inside the leaf's top-right. <768px: 72px, below the entry head
  right-aligned — never over body text at any size (a stamp that
  covers a word has certified nothing but carelessness).
- **Edge cases & failure modes (v2).** *Two leaves locking in
  one frame:* stamps stagger 160ms (§4 density law). *Destination
  name too long for the ring (>16 chars):* the name sets on two
  arcs (upper/lower) rather than shrinking below 11px — stamp
  text has a floor size because certification you cannot read is
  decoration. *Date absent:* the stamp is refused; the leaf
  prints its Arrived line unstamped and the gate fails the build
  — an undated arrival is exactly the fraud §1 exists to catch.
- **Accessibility spec (v2).** Stamp SVG `aria-hidden`; the
  information lives in the printed Arrived line (real text,
  seal-deep on paper 8.61:1). Stamp motion is never the only
  signal of completion: the leaf's rule (§6.3) has already drawn.
  Touch targets on stampable controls ≥44×44px.
- **Tokens consumed (v2).** `--seal`, `--seal-deep`, `--paper`,
  `--ease-seal`, `--ease-rule`, `--dur-stamp` (700ms),
  `--stamp-rot` (seeded 2.0–4.0°), `--dur-watchdog-stamp`
  (1100ms).

### 6.5 The struck balance

- **What & why.** At the foot of the accounts, the page adds
  itself up. Three totals — miles travelled, nights lodged,
  wonders entered — stand in tabular Garamond on digit wheels
  (odometer-style vertical digit strips), scrubbed to scroll:
  as the reader descends the accounts, the wheels turn toward
  the running totals of the entries passed; at the closing leaf
  the wheels settle on the final sums and a double gilt rule
  draws beneath them — the account *struck*. It belongs because
  §1's law needs a visible audit: the balance is the theme's
  proof, performed in public, that every figure on the page was
  a posting and the postings sum. It is the conclusion of the
  argument the whole page has been making.
- **Structure.** A `<footer class="balance">` inside the accounts
  leaves (a running version) and its final form on the closing
  leaf (§6.17). Each total: a label (Garamond 500 small caps
  effect via letterspaced uppercase Garamond — §3 law 5 permits
  this only as the balance's furniture, set in Cinzel instead:
  labels are Cinzel 13px, one of its four licensed homes) and a
  wheel group — one clipped digit strip per digit, tabular
  Garamond 30px, translating on the shared lerp loop. The sums
  are computed at build time from the entries' printed figures
  and also printed as a static total in a `<noscript>`-safe
  default: the DOM ships the wheels at their final values with
  JS-armed offsets only.
- **Motion spec.** Trigger: scroll (scrubbed, shared loop, lerp
  0.12). Each wheel's target = the sum of figures in entries
  whose feet have crossed the reading line; wheels ease toward
  targets at ≤1 digit-step per 90ms `--ease-wheel` so a fast
  scroll shows turning, not teleporting, and a fling settles
  within 900ms of arrival. At the closing leaf, when all three
  targets equal the final sums for 400ms continuously, the
  double rule draws: two gilt lines 3px apart, 700ms
  `--ease-rule`, and the word "Balanced." posts beneath in the
  clerk's apparatus hand. Watchdog: the rule also draws if the
  reader reaches the closing leaf's foot by any means (keyboard,
  anchor, find-in-page) — arrival is arrival.
- **States.** Turning (targets changing) → settled (targets
  stable <400ms) → struck (rule drawn, final). Hover: none.
  Focus: the balance is a region with an aria-label (below);
  focus does not alter it. Scrolled back up: wheels turn back
  down the sums — the running balance is honest in both
  directions; the struck rule, once drawn on the closing leaf,
  never undraws.
- **Content merge.** The totals are the entries' own figures —
  miles from the legs, nights from the stays, wonders from the
  journal lines' count — and §6.13's disbursements carry their
  own sub-balance in the same instrument. The balance invents
  nothing; a build whose wheel targets are typed by hand instead
  of summed from the DOM fails §10's figure audit.
- **Failure fallback.** No JS: wheels stand at final sums,
  double rule printed, "Balanced." printed — the closing leaf is
  complete as a static account. Loop stall: a 2000ms watchdog
  per wheel snaps it to its current target.
- **Reduced-motion variant.** No wheels: totals print at the
  running value for the section in view (updated stepwise at
  leaf boundaries, no animation), and the closing leaf prints
  the final struck balance with its rule. The audit survives;
  the odometer does not.
- **Performance budget & mobile variant.** ≤15 digit strips
  total across three wheels; transforms only; repaint of digit
  text never occurs (strips are pre-rendered 0–9). Mobile: wheel
  digits 24px, labels stack above totals, the running balance
  appears only at leaf feet (not pinned) — a small book keeps
  its balance at the foot of each account, not in a floating bar.
- **Choreography timeline (v2).** Continuous: reading-line
  crossings add postings → wheels step ≤1 digit/90ms → at
  closing leaf, targets = finals → 400ms stability → t=0–700
  double rule draws → t=700 "Balanced." posts → struck (final).
- **State matrix (v2).** *Rest (mid-page):* wheels at running
  sums. *Hover:* none. *Focus:* unchanged; region labelled.
  *Active:* n/a. *Scrolled-past (closing):* struck, permanent.
  *Disabled:* printed finals. *Touch:* identical; no pinning on
  touch devices below 768px.
- **Breakpoints (v2).** ≥1200px: three totals in a row on the
  decimal axis, 30px digits. 768–1199px: three in a row, 26px.
  <768px: totals stack as three ruled lines (label left, wheel
  right), 24px; the double rule spans the column.
- **Edge cases & failure modes (v2).** *An entry's figures
  edited in a CMS:* wheels re-sum from the DOM on load — the
  balance follows the book, never a cached total. *A journey
  with a "no charge" entry (§6.3):* contributes 0 and is counted
  in the wonders only if its journal line exists — the rule is
  printed in §6.13's footnote so the audit is reproducible.
  *Totals exceeding wheel width (miles > 999,999):* a sixth
  strip is added at build; wheels never clip a digit — a clipped
  total is an unstruck balance.
- **Accessibility spec (v2).** The wheel display is
  `aria-hidden`; a visually-hidden live-off text twin prints the
  current totals ("Running balance: 4,120 miles, 38 nights, 11
  wonders") updated at leaf boundaries only — never per digit,
  so AT is told the account, not the odometer. Closing leaf's
  struck totals are real text. Contrast: ink on paper 10.88:1;
  the gilt rule is furniture, not information.
- **Tokens consumed (v2).** `--ink`, `--ink-soft`, `--gilt`,
  `--gilt-deep`, `--ruling`, `--paper`, `--ease-wheel`,
  `--ease-rule`, `--dur-wheel-step` (90ms), `--dur-strike`
  (700ms), `--dur-watchdog-wheel` (2000ms).

### 6.6 Blotting-paper dry

- **What & why.** Each posted entry is briefly covered by a
  blotting-paper mask — a paper-shade, faintly fibrous panel
  exactly the entry's size — which lifts away as the ink "dries":
  beneath it, the entry's wet sheen (a soft specular gradient
  across the text) fades to matte. It belongs because it is the
  theme's theory of haste: even drying time is respected in this
  house, and the half-second an entry spends under the blotter
  is the page teaching the reader its tempo without a word of
  copy. It is also §6.3's completion beat — the blot lifting is
  how the eye knows an account is finished and may be trusted.
- **Structure.** A `<div class="blot" aria-hidden>` per entry,
  absolutely positioned over the entry's text block (never over
  its figures' column — figures are read first and never blotted,
  a rule with an audit in §10), background `--paper-shade` with
  an inline SVG fibre texture (feTurbulence, static, ≤2KB,
  shared across blots via one `<defs>`). The sheen is a gradient
  layer on the entry itself. DOM ships neither armed: no blot,
  no sheen, matte print.
- **Motion spec.** Trigger: §6.3's settle, per entry. Blot is
  present from the entry's first paint *if JS armed it before
  first frame* (it is inserted by the same script that arms the
  posting, never after the reader has seen the entry — a blot
  arriving late is a cover-up). Lift: translateY(0→−6px) +
  opacity 1→0 over 550ms `--ease-blot`, beginning at +350ms
  after the rule starts drawing; sheen fades in parallel
  350–950ms. Total dry ≈950ms. Watchdog 1500ms removes blot and
  sheen unconditionally.
- **States.** Wet (blot on, sheen live) → drying (lifting) →
  dry (rest; both layers absent from DOM). Hover/focus during
  wet: the blot lifts instantly — no reader is made to wait for
  paper to dry before reading what they have pointed at.
  Scrolled-past: dry. Disabled: never wet.
- **Content merge.** The blot covers the entry's own prose and
  lifts off it; the entry's figures stand outside the mask and
  are legible throughout, so the account's numbers are never
  hidden by its ceremony — the merge rule that keeps this
  element honest (§9, failure 3, is its violation).
- **Failure fallback.** Watchdog 1500ms. If the fibre texture
  fails to load (it is inline; failure means a broken build),
  the blot renders flat paper-shade and still lifts on schedule.
  No JS: no blot exists.
- **Reduced-motion variant.** No blot, no sheen: entries post by
  rule alone (§6.3's variant). The drying is described, not
  performed — the entry's apparatus line may carry "entered and
  dried" in the clerk's hand (§12).
- **Performance budget & mobile variant.** One shared texture;
  per-entry cost is two composited layers for <1s. Mobile: blot
  lift 420ms, sheen omitted on low-power devices (the rule +
  stamp carry the posting).
- **Choreography timeline (v2).** t=0 entry posts (§6.3) →
  t=350 blot begins lift → t=350–950 sheen fades → t=900 blot
  gone → t=950 entry matte, posted → watchdog ceiling 1500ms.
- **State matrix (v2).** *Rest:* dry, layers absent. *Hover:*
  instant lift if wet. *Focus:* instant lift. *Active:* n/a.
  *Scrolled-past:* dry. *Disabled:* never armed. *Touch:* first
  touch on a wet entry lifts its blot.
- **Breakpoints (v2).** ≥1200px: blot covers prose block only,
  figures exempt. 768–1199px: same geometry, lift 500ms.
  <768px: blot covers the full entry width (the figures column
  has stacked into the prose, §6.3) but the lift begins earlier
  (+250ms) so small-screen reading is never delayed past 700ms
  total.
- **Edge cases & failure modes (v2).** *Reader scrolls fast
  past a wet entry:* catch-up (§13) dries everything above the
  reading line instantly. *Entry re-posted after CMS edit:*
  the blot may perform once more — fresh ink is wet ink; the
  seal (§6.1) is the only once-per-session ceremony.
  *Print stylesheet:* blots and sheens are `display:none` in
  print — paper does not need to dry on paper.
- **Accessibility spec (v2).** Blot and sheen are `aria-hidden`
  and pointer-events-none; the entry's text is in the
  accessibility tree, unobscured, from first paint — the blot is
  a visual metaphor laid over print that AT never meets.
  Contrast during sheen: the sheen adds specular highlight
  *between* lines (gradient stops avoid text rows at the
  entry's line-height rhythm, §4) and never drops text contrast
  below 7:1 at any frame.
- **Tokens consumed (v2).** `--paper-shade`, `--paper`, `--ink`,
  `--ease-blot`, `--dur-blot` (550ms), `--dur-sheen` (600ms),
  `--dur-watchdog-blot` (1500ms), `--rule-unit`.


### 6.7 Calligraphic destination names

- **What & why.** A destination's name — "Samarkand",
  "Reykjavík", "The Empty Quarter" — is lettered, not typeset:
  an SVG stroke performance in Garamond italic forms whose stroke
  swells and thins like a nib under a practised hand, drawn as
  the itinerary leaf arrives, then resting as a gilt-underlined
  display name above the account it governs. It belongs because
  places are honoured by the hand that writes them: the house
  typesets its prices (anyone may print a figure) but it *writes*
  its places, and the difference between the two treatments is
  the brand in a single gesture. Each name is drawn once; the
  drawing is the leaf's overture.
- **Structure.** The name exists first as real text — an `<h2>`
  or entry head in EB Garamond italic 500 — complete in the DOM.
  The performance layer is an `aria-hidden` SVG above it holding
  the name as 1–3 stroked paths (per word), built at authoring
  time from the display font's outlines by the build pipeline
  (paths are assets, ≤9KB per name, never generated at runtime).
  Swell is produced by a moving mask over a filled duplicate:
  the fill is revealed behind a nib-shaped aperture travelling
  the path, so width variation reads as pressure, not as a
  stroke-width animation (which browsers render as uniform
  thickening and which §9, failure 2 names as the cheap version).
- **Motion spec.** Trigger: the name's leaf crossing the reading
  line, once per session. Per word: aperture travels the path
  over 620ms `--ease-engross`, with two pressure beats (swell at
  the word's stressed syllable, thin at its tail); word gap
  120ms. A two-word name completes in ~1400ms; ceiling 2000ms
  for three words. At completion the gilt underline draws
  300ms `--ease-rule` and the overlay is removed; the printed
  italic name remains, now underlined — the performance retires
  into the furniture. Watchdog 2600ms.
- **States.** Printed (always) → lettering (overlay performing)
  → lettered (overlay gone, underline drawn). Hover: none.
  Focus: focus entering the leaf completes the lettering
  instantly. Scrolled-past: lettered. Disabled: printed italic,
  underline printed at 40% gilt.
- **Content merge.** The name governs the account beneath it —
  it is that leaf's heading and its stamp's text (§6.4 draws its
  ring text from the same string). A lettered name over a
  section that is not a place's account (a pricing page, a form)
  is calligraphy spent on furniture and is refused (§11).
- **Failure fallback.** Watchdog 2600ms removes the overlay
  mid-word. If a name's path asset is missing at build, the leaf
  ships print-only — the pipeline fails the asset check, not the
  page.
- **Reduced-motion variant.** No overlay: the name stands in
  italic with its gilt underline printed. The honour is in the
  italic and the rule; the drawing was ceremony.
- **Performance budget & mobile variant.** ≤3 names perform per
  page (a page with six destinations letters its three principal
  names and prints the rest — honour rationed is honour kept).
  Mobile: names 32px, per-word 480ms, ceiling 1500ms.
- **Choreography timeline (v2).** t=0 leaf crosses line → per
  word: aperture 620ms with swells at ~35% and ~70% of travel →
  120ms lift → t≈1400 (2 words) underline draws 300ms → overlay
  removed → watchdog ceiling 2600ms.
- **State matrix (v2).** *Rest:* printed italic + gilt underline.
  *Hover:* none (the leaf's §6.9 warming applies to its entries,
  not the name). *Focus:* instant completion. *Active:* n/a.
  *Scrolled-past:* lettered. *Disabled:* print + pale underline.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: 56px names, ceiling 2000ms.
  768–1199px: 44px, ceiling 1800ms. <768px: 32px, per-word 480ms;
  names over 14 characters set on two lines and letter line by
  line — a nib never hurries across a break.
- **Edge cases & failure modes (v2).** *Diacritics and
  non-Latin names:* path assets must cover the name as the place
  spells itself — a name the pipeline cannot letter in its own
  orthography ships printed with honour (italic + underline) and
  the gap is logged; the house never letters a place's name
  wrong to keep the ceremony. *Name edited in CMS:* assets
  regenerate at build; an unregenerated edit ships print-only.
  *Aperture mask unsupported (very old engine):* the overlay is
  feature-detected off; print stands.
- **Accessibility spec (v2).** The heading is real text in the
  accessibility tree at all times; overlay `aria-hidden`.
  Contrast: ink on paper 10.88:1; the gilt underline is
  furniture. Heading order is untouched by the performance —
  the `<h2>` precedes its account in the tree exactly as printed.
- **Tokens consumed (v2).** `--ink`, `--ink-deep`, `--gilt`,
  `--paper`, `--ease-engross`, `--ease-rule`, `--dur-letter-word`
  (620ms), `--dur-watchdog-letter` (2600ms).

### 6.8 Gilt edge darkening

- **What & why.** The page's right fore-edge — a 10px gilt band
  running the full height of the book at ≥1200px — darkens and
  warms gradually with scroll depth, from bright fresh gilt to
  the deep, thumb-darkened tone of a volume opened a thousand
  times at this page. It belongs because it makes progress a
  *patina*: the book shows where it has been read, and the
  reader's place in it is visible as wear rather than as a
  percentage. It is the quietest element in the theme and the
  one returning visitors name first, because it makes the page
  feel *kept*.
- **Structure.** A fixed `<div class="fore-edge" aria-hidden>`
  at the viewport's right edge: a vertical gilt gradient whose
  two stops are custom properties (`--edge-top`, `--edge-base`)
  driven by the shared lerp loop from lerped scroll progress —
  top of page: `--gilt-pale`-bright; bottom: `--gilt-deep`
  warmth, with a soft thumb-darkened band centred on the current
  reading position (a radial highlight travelling with the
  reading line). No image assets; the grain is a repeating
  1px-line CSS gradient at 3% ink.
- **Motion spec.** Trigger: scroll (scrubbed, shared loop, lerp
  0.12). Edge tone = interpolate(gilt-pale → gilt-deep,
  progress^1.3) — the exponent makes the first half of the book
  darken slowly (a new book resists wear) and the last third
  deepen quickly. The travelling thumb band follows the reading
  line with an additional 0.06 lerp lag, so it trails the scroll
  like a thumb sliding down the edge. No other motion: the edge
  never pulses, flashes or completes.
- **States.** Bright (top) → darkening (mid) → deep (foot).
  Hover/focus/active: none — the edge is not a control and is
  never the only carrier of position (§6.10's ribbon repeats
  the information accessibly). Scrolled back up: the edge
  lightens again — wear here is a reading, not a scar; the book
  shows where you *are*, not where you have been. (The struck
  balance, §6.5, is the theme's permanent record; the edge is
  its present tense.)
- **Content merge.** The edge belongs to the book the page is;
  its darkening is keyed to the folios (§6.11), each leaf's entry
  darkening it by its share — the wear is the sum of the
  accounts read, not a scroll percentage wearing a costume.
- **Failure fallback.** No JS: the edge stands at its mid tone
  (a static gilt gradient, gilt → gilt-deep) — a kept book at
  rest. Loop stall: the edge freezes at its last tone; nothing
  is hidden by it at any tone.
- **Reduced-motion variant.** The edge is set stepwise at leaf
  boundaries to the tone of the leaf in view (no continuous
  scrub) — position still reads as patina, without the slide.
- **Performance budget & mobile variant.** One fixed layer, two
  custom properties per frame, zero repaints beyond the edge's
  own 10px strip. Mobile (<768px): the edge narrows to 5px and
  the thumb band is cut — a small book's edge is a line, not a
  landscape; below 480px the edge is a static gilt hairline.
- **Choreography timeline (v2).** Continuous with scroll:
  progress lerps 0.12 → edge tone interpolates (exp 1.3) →
  thumb band follows at 0.06 lag → at foot, edge rests at full
  depth as the closing leaf (§6.17) is read — the book is most
  worn where it ends.
- **State matrix (v2).** *Rest:* tone of current position.
  *Hover:* none. *Focus:* none. *Active:* n/a. *Scrolled-past:*
  n/a (position instrument). *Disabled:* static mid tone.
  *Touch:* identical values; no gesture is bound to the edge.
- **Breakpoints (v2).** ≥1200px: 10px edge + thumb band.
  768–1199px: 7px edge, thumb band at 60% strength. <768px: 5px,
  no band; <480px: static hairline.
- **Edge cases & failure modes (v2).** *Short page (one leaf):*
  progress saturates early; the exponent keeps the edge from
  reaching full depth on a page too short to have worn it —
  depth is capped by leaf count, not scroll alone. *Zoomed
  viewport:* the edge is viewport-fixed, not document-fixed, so
  zoom never detaches it from the fore-edge it represents.
  *Print:* the edge prints as a gilt hairline on the first page
  only (print CSS), or the book pretends to a binding it does
  not have.
- **Accessibility spec (v2).** `aria-hidden`, purely atmospheric;
  position information is duplicated by the ribbon's accessible
  name (§6.10) and by ordinary heading navigation. The edge
  never carries text and its contrast is never load-bearing.
- **Tokens consumed (v2).** `--gilt`, `--gilt-pale`, `--gilt-deep`,
  `--ink`, `--ease-lamp` (thumb-band lag curve), `--edge-w`
  (10px).

### 6.9 Ink-deepening hover

- **What & why.** Hovering an entry deepens its ink — text
  colour eases from `--ink` toward `--ink-deep`, its figures
  gain a step of weight (Garamond 500 overlay swap is refused;
  the deepening is colour and a 0.2px text-shadow in ink at 12%,
  never a font swap that would shift the columns) — and its
  stamp warms (§6.4), as if the clerk leaned closer with the
  lamp. It belongs because attention in this house is lamplight:
  the entry you regard is the entry better lit, and the effect
  teaches the page's fiction — a human is attending to this
  account — in 300ms, without a tooltip, a lift, or a shadow
  borrowed from a card UI.
- **Structure.** Pure CSS state on `.entry:hover` and
  `.entry:focus-within` (the two are one state in this theme —
  the lamp does not distinguish a pointer from a keyboard),
  driving colour transitions on the entry's text and a
  `--lamp` custom property (0→1) that the stamp's warmth and a
  soft radial paper highlight (positioned at the entry's head)
  consume. No JS. Touch: the state is bound to first tap via
  `:active` persistence rules below.
- **Motion spec.** Trigger: hover/focus-within. Deepen: 300ms
  `--ease-lamp` in; release: 450ms `--ease-lamp` out — the lamp
  withdraws more slowly than it leans in, the theme's small
  courtesy. The paper highlight swells from 0 to a 340px radial
  at 6% gilt warmth in parallel. No transform on the entry at
  any point: paper under a lamp does not jump.
- **States.** Rest (ink, lamp 0) → regarded (ink-deep, lamp 1,
  stamp warm) → rest. Active (click within entry): a brief lamp
  flare to 1.15 for 120ms — the clerk nodding — then back to
  regarded. Scrolled-past: no residue; an entry off-screen holds
  no lamp. Disabled: the state is CSS; it cannot fail to exist,
  only to be noticed.
- **Content merge.** The lamp lights the entry's own text and
  its own stamp; it is bound to the entry element, never a
  global spotlight — a page where the lamp wanders free of the
  accounts is §6.8's edge misused as a toy (§9, failure 6).
- **Failure fallback.** None needed and none faked: if CSS
  custom properties fail (ancient engine), the colour transition
  alone still deepens the ink. The content is untouched in every
  state.
- **Reduced-motion variant.** The deepening becomes instant
  (transition-duration 0.01ms via the reduced-motion query) but
  *remains* — regard is information (which entry am I on?), not
  decoration, and reduced motion in this theme removes travel,
  not light.
- **Performance budget & mobile variant.** Colour transitions on
  one entry's subtree; the radial highlight is a background on
  the entry, composited. Mobile/touch: hover does not exist —
  first tap on an entry sets regarded until another entry is
  tapped or the leaf is left; the deepening is the tap's
  acknowledgement, paired with the entry's own links remaining
  the actual targets (the entry body is never a link itself).
- **Choreography timeline (v2).** t=0 pointer/focus enters →
  t=0–300 ink deepens, lamp 0→1, stamp warms → (click) t=0–120
  flare 1.15 → release: t=0–450 lamp withdraws.
- **State matrix (v2).** *Rest:* ink, lamp 0. *Hover:* regarded.
  *Focus:* regarded (focus-within, identical). *Active:* flare
  120ms. *Scrolled-past:* rest. *Disabled:* n/a (CSS state).
  *Touch:* tap-to-regard, sticky per leaf.
- **Breakpoints (v2).** ≥1200px: highlight 340px radial.
  768–1199px: 280px. <768px: highlight cut (small leaves are
  wholly lit by regard); deepening and stamp warmth remain.
- **Edge cases & failure modes (v2).** *Pointer sweeping down a
  leaf:* entries deepen in sequence like a lamp passing — this
  is the intended reading and the 300/450 asymmetry keeps it
  calm, never flickery; a build that shortens the release below
  300ms makes the leaf strobe and fails §10. *Entry partially
  off-screen:* the lamp lights what is visible; the highlight is
  clipped by the entry, not the viewport. *Forced-colors mode:*
  deepening yields to system colours; the stamp warmth is
  disabled; regard is then shown by the system's focus/hover
  conventions alone.
- **Accessibility spec (v2).** Focus-within parity is the spec:
  every hover effect has an identical keyboard state, and the
  visible focus ring (2px `--seal-deep` outline, offset 3px —
  the house marks your place in red pencil) is separate from and
  additional to the lamp. Contrast in regarded state: ink-deep
  on paper 13.62:1 — regard *raises* contrast; an entry is never
  harder to read for being attended to.
- **Tokens consumed (v2).** `--ink`, `--ink-deep`, `--seal`,
  `--gilt`, `--paper`, `--ease-lamp`, `--dur-lamp-in` (300ms),
  `--dur-lamp-out` (450ms), `--lamp`.

### 6.10 Ribbon-marked page turns & the resting ribbon

- **What & why.** Two duties, one object. At rest, a baize-green
  ribbon — 22px wide, notched at its foot — hangs in the margin
  rail at the reader's current leaf, sliding to the new folio as
  leaves pass: the book keeps your place the way books do. On
  navigation (to another page of the site, or a contents-leaf
  jump, §6.11), the turn is performed: the current leaf lifts
  from its fore-edge, turns over 700ms with the ribbon sliding
  to the destination folio, and the new page settles as the next
  leaf of the same book. It belongs because movement through
  this site is movement through a volume — heavy, placed, and
  never a fade — and because the ribbon is the theme's progress
  indicator wearing its true shape (§5).
- **Structure.** Resting ribbon: a fixed-position element in the
  margin rail (`<div class="ribbon" role="img">` with an
  accessible name, below), its vertical position a custom
  property driven by the shared loop from the current leaf's
  folio offset; the notch is a clip-path triangle; a gilt folio
  numeral is printed on the ribbon at its head. Page turn: a
  full-leaf overlay (paper ground, the outgoing leaf's content
  cloned at 40% ink as a "show-through" — the print ghosting
  through the turning page, a real book's detail) rotating on
  the book's spine axis (left edge) with a deepening spine
  shadow; implemented as a view-transition enhancement with a
  plain navigation fallback.
- **Motion spec.** Resting: ribbon slides between folio stops
  over 600ms `--ease-ribbon`, triggered by leaf change on the
  shared loop (it rides the lerped progress, so it glides rather
  than jumps). Turn: t=0 navigation committed → leaf lifts
  (rotateY 0→−12°, shadow grows) 0–250ms → turns through
  −160° by 620ms `--ease-ribbon` → new leaf settles, ribbon
  arrives at the new folio at 700ms. Hard ceiling: navigation
  is never blocked past 700ms; if the turn cannot run, the
  browser navigates plainly at once. Watchdog 900ms forces
  completion/removal of the overlay.
- **States.** Resting (at current folio) → sliding (leaf change)
  → resting. Turning (overlay live) → settled (new page, ribbon
  placed). Focus: a contents-leaf jump (§6.11) triggered by
  keyboard performs a *short* turn (400ms) or none under reduced
  motion — the ribbon still arrives. Scrolled-past: n/a.
  Disabled/no-JS: no overlay ever; the ribbon stands printed at
  the first folio, and its information duty passes to the
  contents leaf and headings.
- **Content merge.** The ribbon rests *at a folio* — its stops
  are the leaves' real positions, generated from the page's
  leaf map (§6.11), so the indicator cannot drift from the
  contents it indexes. The turn's show-through is the outgoing
  page's own print: you leave a page by seeing it ghost through
  its successor, which is what leaving a page in a book is.
- **Failure fallback.** View-transitions unsupported: plain
  navigation, zero delay — the ceremony is an enhancement with
  a hard rule that it may never tax the journey. Overlay stall:
  900ms watchdog removes it and completes navigation.
- **Reduced-motion variant.** No turn: navigation is instant,
  and the ribbon on the new page stands already at its folio.
  The resting ribbon updates stepwise at leaf changes.
- **Performance budget & mobile variant.** The overlay clones
  text only (no images re-rendered), one rotate transform;
  turns are disabled on `save-data` connections. Mobile: the
  margin rail is gone, so the ribbon becomes a 14px ribbon at
  the top edge of the viewport, its folio numeral beside the
  book's name (§6.11's compact contents); turns shorten to
  500ms.
- **Choreography timeline (v2).** Rest: leaf change → ribbon
  glides 600ms to the new stop. Turn: t=0 commit → 0–250 lift →
  250–620 turn + spine shadow → 620–700 new leaf settles,
  ribbon placed → watchdog ceiling 900ms.
- **State matrix (v2).** *Rest:* at current folio. *Hover:* the
  ribbon is not a control; hovering it shows its folio's leaf
  title as a native-position tooltip card (§11) after 600ms.
  *Focus:* n/a (not focusable; its information is in the
  contents leaf). *Active:* n/a. *Scrolled-past:* n/a.
  *Disabled:* printed at first folio. *Touch:* identical;
  ribbon never intercepts touches (pointer-events none).
- **Breakpoints (v2).** ≥1200px: 22px margin ribbon, 700ms turns.
  768–1199px: 18px ribbon in a narrowed rail, 600ms turns.
  <768px: top-edge ribbon 14px, folio numeral in the header,
  500ms turns, show-through omitted (the clone is the cost).
- **Edge cases & failure modes (v2).** *Back button:* the turn
  reverses (leaf turns back, ribbon returns) only if the
  browser supplies the navigation type; otherwise plain — a
  book never argues with its reader about direction. *Anchor
  jump within the page:* no turn; the ribbon glides and §13's
  catch-up posts what was passed. *Two navigations in flight:*
  the second cancels the first's overlay instantly.
- **Accessibility spec (v2).** The ribbon carries
  `role="img"` and an accessible name updated at leaf changes —
  "You are at folio 3 of 6: The Accounts" — updated at most once
  per leaf (never per scroll frame). Turns never trap focus:
  focus moves to the new page's heading at settle, per standard
  navigation practice. Ribbon is pointer-events-none; nothing
  operable hides beneath it.
- **Tokens consumed (v2).** `--baize`, `--baize-deep`, `--gilt`,
  `--gilt-deep`, `--paper`, `--ink`, `--ease-ribbon`,
  `--dur-turn` (700ms), `--dur-ribbon` (600ms),
  `--dur-watchdog-turn` (900ms).

### 6.11 Folio navigation — the contents leaf

- **What & why.** The site's navigation is a leaf of the book:
  a contents list at the head of the home page (and a compact
  form in the header elsewhere) where each destination is an
  entry — leaf title in Garamond, its folio numeral, a leader
  of gilt dots to the page's figure (journeys: "6 accounts";
  the form leaf: "open an account") — and the reader's current
  leaf is marked by the ribbon (§6.10) resting against its line.
  It belongs because a book's navigation was solved centuries
  ago: a contents leaf, honest folios, and a kept place. A nav
  bar with a hamburger would be a ticket machine bolted to the
  counting-house door.
- **Structure.** A `<nav>` containing an ordered list mirroring
  the leaf map: each item a real link (Garamond 18px), folio
  numeral (tabular, `--gilt-deep`), dotted leader (CSS
  border-bottom dotted in `--gilt` at 40%, baseline-aligned),
  and the item's figure. The current item carries
  `aria-current="page"` (or `"location"` in-page) and the
  ribbon's stop. Header form: the same list compressed to a
  single row at ≥1200px, and to a "Contents" disclosure (a real
  `<details>`-equivalent button + region) below that.
- **Motion spec.** Posting: the contents leaf posts like an
  entry (§6.3) on load after the engrossing — lines settle
  staggered 60ms apart, leaders draw 300ms `--ease-rule` per
  line. Current-leaf marker: the ribbon's arrival (§6.10).
  Disclosure open/close: 320ms `--ease-post`, height + opacity,
  with the leaf's gilt head-rule redrawing beneath the opened
  list. No other motion — contents are consulted, not performed.
- **States.** Rest (posted). Hover on an item: §6.9's lamp at
  half strength + the leader dots deepen to full gilt — the
  clerk's finger running along the line. Focus: full lamp +
  red-pencil focus ring (§6.9). Active: the item stamps small —
  a 10px seal dot presses beside its folio (180ms, §6.4's ease)
  before navigation/turn begins. Current: ribbon resting +
  item in ink-deep.
- **Content merge.** The contents *is* the book's map of itself:
  folios are the leaves' real order, figures are real counts
  from the leaves (accounts on the page, wonders struck) — a
  contents figure that disagrees with its leaf is a §1 fraud in
  miniature and the gate checks them against the DOM.
- **Failure fallback.** No JS: the contents stands printed and
  complete, current item marked by ink-deep alone; the
  disclosure variant ships open below 768px (a closed contents
  that cannot open is a locked book). All links are ordinary
  anchors; nothing about navigation depends on the turn (§6.10).
- **Reduced-motion variant.** Contents printed, leaders drawn,
  disclosure instant. The current marker remains the ribbon at
  rest.
- **Performance budget & mobile variant.** Text and CSS only;
  ≤1KB of theme CSS beyond the entry system it reuses. Mobile:
  the header contents is the disclosure; the full contents leaf
  still opens the home page (books open with their contents at
  every size).
- **Choreography timeline (v2).** Load: seal (§6.1) → engross
  (§6.2) → contents lines settle 60ms stagger → leaders draw →
  ribbon glides to folio 1. Disclosure: t=0 tap → 0–320 leaf
  opens → rule redraws at 320.
- **State matrix (v2).** *Rest:* posted, current marked.
  *Hover:* half-lamp + leader deepens. *Focus:* full lamp +
  ring. *Active:* seal dot presses 180ms, then turn/navigation.
  *Scrolled-past:* n/a. *Disabled:* printed, disclosure open on
  small screens. *Touch:* items ≥44px tall; first tap regards
  (§6.9), second follows — no: links follow on first tap (a
  contents that makes you knock twice is a door, not a list);
  the regard state yields to navigation.
- **Breakpoints (v2).** ≥1200px: full contents leaf + one-row
  header form. 768–1199px: contents leaf full; header form is
  the disclosure. <768px: contents leaf full on home; disclosure
  header elsewhere, items 16px/44px rows, leaders retained
  (they are the line's grammar at every size).
- **Edge cases & failure modes (v2).** *More leaves than the
  contents expects (>9):* the contents leaf paginates as a
  two-column contents (the book grew) — never a scrollable nav
  box. *A leaf removed in CMS:* the contents regenerates from
  the leaf map at build; a hand-maintained contents is refused
  (§9, failure 9's cousin: furniture that can disagree with the
  book will). *Long titles:* wrap to two lines, leader drops to
  the second line's baseline; folio never wraps.
- **Accessibility spec (v2).** Landmark `<nav>` with
  aria-label "Contents of the book"; leaders and dots are
  decorative (`aria-hidden` spans); each link's accessible name
  is "Leaf title, folio N" — the figure is a separate visible
  span included in the name only where it aids choice ("6
  accounts"). Focus ring per §6.9. Contrast: ink 10.88:1,
  folio gilt-deep 4.87:1 at 14px+ (numerals are labels, §2).
- **Tokens consumed (v2).** `--ink`, `--ink-deep`, `--ink-soft`,
  `--gilt`, `--gilt-deep`, `--seal`, `--paper`, `--ease-post`,
  `--ease-rule`, `--dur-contents` (320ms).

### 6.12 Journey account cards

- **What & why.** Where journeys must be *listed* — the
  collection leaf, search results, a season's offerings — they
  appear as account cards: a paper-shade leaf fragment carrying
  the journey's plate (photograph on its mount, §5), its name
  (§6.7's italic, printed), its itemised skeleton (three lines:
  legs, nights, guide — each with its figure), its total ruled
  beneath, and its stamp (§6.4) once booked or featured. It
  belongs because listing is the one place a feed threatens the
  book, and the card answers it in the book's own grammar: not a
  tile with a hero image and a price badge, but a *summary
  account* — the full entry (§6.3) condensed, its figures still
  itemised, its total still a sum.
- **Structure.** An `<article class="account-card">`: plate
  figure (image in a paper mount with gilt hairline, caption in
  the clerk's hand), name, a 3-line item table (tabular figures,
  decimal axis shared across the grid so a column of cards reads
  as one account), a rule, the total line ("Entered at £4,850 —
  the sum of the lines above"), and a text link "Read the full
  account →" to the journey's entry leaf. Cards sit in a grid
  ruled like a leaf: the grid's rows share the `--rule-unit`
  rhythm.
- **Motion spec.** Posting: cards post as a group when the grid
  crosses the reading line — settle 500ms `--ease-post`,
  staggered 90ms in reading order, each card's rule drawing at
  its settle +150ms (350ms). Plate: image scales 1.03→1 inside
  its mount over the same 500ms. Hover: §6.9 lamp + the plate's
  mount shadow deepens (the card does not lift — paper on a desk
  is not picked up by a glance). Click on the card's link:
  §6.10's turn. Watchdog 1400ms for the group.
- **States.** Printed (DOM, complete) → posting → posted.
  Hover/focus-within: regarded (§6.9). Featured/booked: stamped
  (§6.4 at rest in the card's corner). Sold out — the house says
  "The account is closed": the card remains, its total line
  struck through with a ruling-red line and the clerk's note
  beneath; a closed account is still an account, never a
  vanished card (§1's honesty in the listing layer).
- **Content merge.** Every figure on the card is a line of the
  journey's real account and the total is their sum — the card
  is auditable against the full entry it links to, and §10
  checks card totals against entry totals across the site. The
  plate's caption names the place and the day ("Day 4 — the
  Karaouine at dawn"), drawn from the itinerary, not a stock
  alt-text.
- **Failure fallback.** No JS: cards stand printed, rules at
  resting tone, plates at scale 1. Images failing: the mount
  holds the caption and a pencilled "plate missing" note in the
  clerk's hand — the book admits the loss on the page (§9's
  honesty pattern), never a broken-image icon.
- **Reduced-motion variant.** Cards printed, rules drawn, plates
  still. Closed accounts still struck — that is content, not
  motion.
- **Performance budget & mobile variant.** Images: responsive
  `srcset`, the mount's aspect reserved (no CLS); ≤6 cards
  perform per leaf (§4). Mobile: grid → single column, cards
  full-leaf width, plate mount narrows to 40% beside the lines
  — the account stays an account, never a stacked tile.
- **Choreography timeline (v2).** t=0 grid crosses line → cards
  settle 90ms stagger, 500ms each → rules draw at settle+150 →
  plates settle with their cards → group posted by ~1200ms →
  watchdog ceiling 1400ms.
- **State matrix (v2).** *Rest:* posted, matte. *Hover:* lamp +
  mount shadow. *Focus:* lamp + ring on the link. *Active:*
  link press → turn. *Scrolled-past:* posted. *Disabled:*
  printed. *Touch:* tap regards; the link is the target (≥44px).
- **Breakpoints (v2).** ≥1200px: 3-across grid, shared decimal
  axis across the row. 768–1199px: 2-across, axis per row.
  <768px: 1 column, plate 40% left, lines right, total full
  width beneath its rule.
- **Edge cases & failure modes (v2).** *A journey with only two
  lines to itemise:* the third line prints "—" and the total
  sums two lines; a padded third line inventing a charge is a
  §1 fraud. *Very long names:* two lines, italic, never
  truncated with an ellipsis — the book does not abbreviate a
  place. *Grid of 1:* the single card sets at entry width
  (60–68ch), not stretched across the leaf.
- **Accessibility spec (v2).** Card is an article with its name
  as heading; the item table is a real table (or list with
  figure spans) readable linearly; the total's "sum of the lines
  above" is real text, not a tooltip. Image alt = the caption's
  fact. Contrast per §2; the struck total remains legible
  (strikethrough is a line, not a lightening).
- **Tokens consumed (v2).** `--paper-shade`, `--paper`, `--ink`,
  `--ink-soft`, `--ruling`, `--gilt`, `--seal`, `--ease-post`,
  `--ease-rule`, `--dur-card` (500ms), `--rule-unit`.


### 6.13 The Disbursements & Disappointments table

- **What & why.** The theme's conscience, given a leaf of its
  own. A ruled table on the baize ground — the desk showing
  through where bad news is kept — with three columns: the day,
  the disbursement or disappointment (in the traveller's italic
  where it is a confession, §3 law 4), and what it was charged
  to: a figure in pounds, or the words "to experience". The
  original entry's line stands as the table's exemplar and its
  second row in every worked example: *"Day 9: rain. Charged to
  experience."* It belongs because §1's second clause needs a
  home that is not a footnote: a house that posts its failures
  in the same ink, at the same size, in a table built like its
  accounts, has earned the right to be believed about its
  wonders. This leaf is the most persuasive page in the theme
  and the one competitors will not copy, which is the point.
- **Structure.** A real `<table>` on a `--baize-deep` leaf:
  caption in Cinzel ("Disbursements & Disappointments"), column
  heads in the clerk's apparatus hand (paper on baize-deep,
  6.63:1), rows ruled with paper hairlines at 30%, figures
  tabular right-aligned, confessions in Garamond italic paper.
  A sub-balance line closes the table in §6.5's manner: money
  disbursed summed; disappointments charged to experience
  *counted* (a number of days, never a price — experience is not
  invoiced, and pricing it would be the one vulgarity the table
  exists to refuse).
- **Motion spec.** Posting: the leaf posts as one entry (§6.3)
  — it is not staggered row by row (bad news is not drip-fed);
  its rule draws beneath the sub-balance. Rows regard under
  §6.9's lamp adapted to the dark ground (paper text brightens
  toward full paper from 92%). The sub-balance's money wheel
  (§6.5) turns as the leaf crosses. Watchdog 1600ms.
- **States.** Printed → posting → posted. Hover/focus-within a
  row: brightened (above). Closed/empty state: a season with no
  disappointments prints the table with one row — "Nothing to
  enter. The house is as surprised as you are." — because an
  empty honesty table would look like the leaf was forgotten;
  the book remarks on its own luck.
- **Content merge.** Every row is a real event from a real
  journey's account, cross-referenced by folio ("see the
  Samarkand account, Day 9") — the table is an index of the
  book's failures, and §10 spot-checks rows against entries.
  Rows are never written for colour: a disappointment the house
  did not actually absorb is a short story, and short stories
  live in §6.15's letters, attributed to their writers.
- **Failure fallback.** No JS: the table stands printed on its
  baize leaf, sub-balance printed. The leaf is content-first by
  design: its ceremony is the least of it.
- **Reduced-motion variant.** Printed; sub-balance printed;
  row-brightening instant. Nothing else changes — honesty has
  no choreography to reduce.
- **Performance budget & mobile variant.** A table and a leaf
  ground; the cheapest element in §6. Mobile: the table becomes
  stacked entries (day as head, confession beneath, charge
  right-aligned on its own line) below 560px — a three-column
  table at 360px would squeeze the confessions, and confessions
  are never squeezed (§9, failure 10).
- **Choreography timeline (v2).** t=0 leaf crosses line →
  t=0–600 leaf settles (§6.3) → sub-balance wheel turns to its
  sum → rule draws 500ms → posted → watchdog ceiling 1600ms.
- **State matrix (v2).** *Rest:* posted on baize. *Hover:* row
  brightens. *Focus:* row brightens + ring (paper outline on
  dark ground). *Active:* n/a. *Scrolled-past:* posted.
  *Disabled:* printed. *Touch:* rows ≥48px; tap brightens.
- **Breakpoints (v2).** ≥1200px: full table, confessions at
  18px italic. 768–1199px: full table, confessions 16.5px.
  <768px: table holds to 560px, then stacks as above.
- **Edge cases & failure modes (v2).** *A disappointment with a
  real cost AND a confession* (the flooded road that also cost a
  night's fare): two rows, linked — the money in Disbursements,
  the day in Disappointments, each cross-referencing the other;
  never merged into one row that hides either half. *Legal
  review asks to soften a row:* the house may remove a row
  (the book is the house's), but the sub-balance footnote then
  prints "entries removed at counsel's advice: n" — removal is
  itself posted, or the leaf's premise is void.
- **Accessibility spec (v2).** Real table semantics: caption,
  `th scope="col"`, row heads as the day cells. The italic
  confessions are text, not images. Contrast: paper on
  baize-deep 6.63:1; hairlines are furniture. The sub-balance's
  "charged to experience: 3 days" is real text.
- **Tokens consumed (v2).** `--baize-deep`, `--baize`, `--paper`,
  `--gilt-pale`, `--ink`, `--ease-post`, `--ease-rule`,
  `--ease-wheel`, `--dur-post` (600ms).

### 6.14 Opening an account — the booking form

- **What & why.** The conversion leaf, kept as a leaf of the
  book: a traveller opens an account by entering their name,
  their journey (chosen from the book's accounts), their dates
  and party, and their direction (email) — each field a ruled
  line in the ledger, filled in Garamond, and the submission is
  not a button press but a *posting*: the house's seal (§6.1's
  device, at form scale) stamps the entry, a folio number is
  assigned from the book's real sequence, and the confirmation
  is an entry the traveller can read back. It belongs because
  conversion is where themes go to die — a generic checkout
  dropped into a ledger would break the fiction at the exact
  moment money appears; here the ritual *is* the reassurance:
  your enquiry has been entered, numbered, and sealed, in a book
  that posts its disappointments.
- **Structure.** A `<form>` set as a leaf: fields are ruled
  lines (label above in the clerk's hand, input as Garamond
  18px on the ruling line, no boxes — the line is the field),
  the journey field a real `<select>` styled as an entry line
  (its options are the book's accounts with their totals, §6.12),
  dates as native inputs on ruled lines. The price summary is a
  small account at the form's foot: the chosen journey's lines
  re-posted, a deposit line, and the total — §1 applies in full:
  the total is the sum of the lines printed above it, recomputed
  in the DOM when the journey changes. Submit is a Garamond
  button styled as an entry line with the seal device beside it
  — never a filled pill (§11).
- **Motion spec.** Field focus: the field's ruling line deepens
  from `--ruling` to `--ink` (300ms `--ease-lamp`) and a red-
  pencil margin tick appears beside the label — the clerk's eye
  is on this line. Journey change: the summary account re-posts
  (§6.3's settle, 400ms) with the wheels (§6.5) turning to the
  new total. Submit: the form's entries settle, the seal falls
  at form scale (54px, 500ms `--ease-seal`), a folio number
  typesets (digit by digit is refused — folio numbers print,
  200ms fade of the printed number), and the form leaf is
  replaced by the confirmation entry (§ below) over 600ms
  `--ease-post`. Errors: the offending line's rule turns
  `--seal-deep` and the clerk's note appears in the margin
  (§12's error voice) — no shake, no red fill; a ledger does
  not shout or tremble.
- **States.** Rest (printed, lines at ruling tone) → focused
  (line deepened, tick shown) → valid/invalid per line (invalid:
  seal-deep rule + margin note, persisting until corrected) →
  submitting (seal falling; fields inert but readable) →
  confirmed (replaced by the entry). The confirmation entry:
  folio number, the traveller's name as entered, journey, dates,
  total — all as printed text — closing with the house's line
  (§12) and the seal at rest. A "post another entry" link
  restores the form.
- **Content merge.** The form's journeys, figures and folio
  sequence are the book's own: the select's totals are §6.12's
  card totals (one source, the entry DOM), and the folio number
  continues the sequence the contents leaf (§6.11) prints — if
  the contents ends at folio 6, the first confirmation of the
  session is № 7's entry. A form with its own prices is a second
  book, and the house keeps one book.
- **Failure fallback.** The form is a real form: with JS off it
  submits by ordinary POST to the house's endpoint, fields are
  native, labels are `<label>`s, and the summary account prints
  the default journey's lines with a note that totals are
  confirmed by return post. A stalled submission (no response
  in 6000ms) restores the form with its entries intact and a
  margin note in §12's voice — input is never eaten by this
  house (§9, failure 11).
- **Reduced-motion variant.** Focus deepening instant; summary
  re-posts without settle; submit confirms without the seal's
  fall (seal printed at rest on the confirmation). The folio
  number still prints.
- **Performance budget & mobile variant.** The form reuses the
  entry, seal and wheel systems — its own cost is CSS for ruled
  fields (≤3KB). Mobile: fields stack full-leaf; the summary
  account sits above the submit (never below the fold of the
  form's own leaf); tap targets ≥48px; the seal at confirmation
  is 44px.
- **Choreography timeline (v2).** Focus: line deepens 300ms.
  Journey change: summary re-posts 400ms, wheels turn ≤900ms.
  Submit: t=0 entries settle → t=100–600 seal falls → t=600
  folio prints → t=600–1200 confirmation entry replaces the
  form → watchdog: 6000ms stall restores the form intact.
- **State matrix (v2).** *Rest:* ruled, quiet. *Hover:* field
  line warms (§6.9 at half strength). *Focus:* deepened + tick
  + ring (§6.9's red-pencil ring on the field). *Active:*
  submit presses as an entry line (translateY 1px, the press
  of §11's button). *Scrolled-past:* n/a. *Disabled:* a
  submitting form's fields are `readonly`, never greyed into
  illegibility. *Touch:* labels remain above fields (never
  placeholder-only) at every size.
- **Breakpoints (v2).** ≥1200px: two-column leaf — fields left,
  summary account right on the decimal axis. 768–1199px: single
  column, summary above submit. <768px: single column, summary
  collapses to its total line + a "see the account" disclosure
  that opens the full lines in place (320ms, §6.11's ease).
- **Edge cases & failure modes (v2).** *Party size changes the
  price:* the summary gains a per-traveller line and re-sums —
  the arithmetic is printed, so a multiplier is a line, never a
  silent change to the total. *A journey closes while the form
  is open:* on submit, the house answers with the confirmation
  replaced by a clerk's note — the account closed at folio N;
  here are two open accounts of similar temper — and the
  traveller's entries are preserved in the form beneath it.
  *Duplicate submission:* the folio number is the idempotency
  key; a second submit with the same entries returns the same
  entry, printed again, never a twin account.
- **Accessibility spec (v2).** Native semantics throughout:
  `<label for>` on every field, errors linked by
  `aria-describedby` to the margin notes, `aria-invalid` on the
  line, the summary as a table with a caption, the confirmation
  as a region with `tabindex="-1"` receiving focus on arrival.
  Focus ring per §6.9. Contrast: labels ink-soft 6.09:1 at
  14px (apparatus, §2), input text ink 10.88:1, error notes
  seal-deep 8.61:1 — an error you cannot read is a second error.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--ink-soft`,
  `--ruling`, `--seal`, `--seal-deep`, `--gilt`, `--ease-lamp`,
  `--ease-seal`, `--ease-post`, `--dur-form-seal` (500ms),
  `--dur-stall` (6000ms).

### 6.15 Letters of recommendation — the guest-book leaf

- **What & why.** Testimonials are kept as letters entered in
  the book: each a Garamond italic account (§3 law 4 — the
  traveller's voice) of one journey, signed with the traveller's
  name, their folio (the account it refers to), and the season;
  a letter is never excerpted into a star-rated snippet, never
  given a score, and never printed without its journey's folio
  beside it, so any reader may turn to the account and check the
  letter against the book — including its disbursements
  (§6.13). It belongs because praise in a ledger is evidence,
  and evidence is filed, not framed. A letter that mentions the
  rain on Day 9 is worth six that mention only wonders, and the
  house prefers them (§12).
- **Structure.** A leaf of `<blockquote>` entries, each posted
  as an entry (§6.3): the letter's text (italic, 18px, measure
  58ch — letters are narrower than accounts), a signature line
  (name upright in the clerk's hand, folio link, season), and
  where the journey had a disappointments row, the letter's own
  reference to it is left standing — the build never edits a
  letter's weather out.
- **Motion spec.** Posting per §6.3 (settle + rule), staggered
  by scroll only. The folio link regards under §6.9. No
  rotation, no carousel: letters are read in the order the book
  received them, and a carousel of praise is a salesman cycling
  his references (§9, failure 12). Watchdog per §6.3.
- **States.** Printed → posting → posted. Hover/focus: §6.9 on
  the entry; the folio link carries the standard ring. Empty
  state: a new house with no letters prints the leaf with its
  head-rule and one clerk's line — "No letters yet. The book is
  young; its accounts are open above." — an honest empty leaf,
  never populated with invented correspondents.
- **Content merge.** Each letter's folio binds it to a real
  account on the site; §10 follows every folio link to its entry
  and checks the journey name matches. Letters are the only
  content in the theme the house did not write, and the merge
  rule is attribution: name, folio, season — a letter missing
  any of the three is not entered.
- **Failure fallback.** Per §6.3: printed, ruled at rest tone,
  complete without JS.
- **Reduced-motion variant.** Per §6.3: printed and ruled.
- **Performance budget & mobile variant.** Text only; the
  cheapest leaf after §6.13. Mobile: letters at 16.5px, measure
  full leaf, signature stacks beneath.
- **Choreography timeline (v2).** Per entry: §6.3's timeline
  (crossing → settle 600ms → rule 500ms → posted; watchdog
  1600ms).
- **State matrix (v2).** *Rest:* posted. *Hover:* lamp. *Focus:*
  lamp + ring on links. *Active:* folio link → §6.10 turn.
  *Scrolled-past:* posted. *Disabled:* printed. *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: letters at 58ch within the
  column, folio in the margin rail. 768–1199px: folio moves into
  the signature line. <768px: full-width letters, signature
  stacks.
- **Edge cases & failure modes (v2).** *A traveller withdraws a
  letter:* it is removed and the leaf's apparatus line notes
  "one letter withdrawn at its writer's request" — the count of
  letters, like every figure in the book, stays honest about its
  own history. *A letter longer than 180 words:* entered in full
  or not at all; the house asks the writer for a shorter letter
  rather than cutting one (§12).
- **Accessibility spec (v2).** `<blockquote>` with `<footer>`
  attribution; folio links have real names ("The Samarkand
  account, folio 3"). Italic at 18px Garamond holds contrast
  10.88:1 (ink on paper). No star graphics exist to be misread.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--ink-soft`,
  `--ruling`, `--gilt-deep`, `--ease-post`, `--ease-rule`,
  `--dur-post` (600ms).

### 6.16 The unposted leaf — skeleton & loading

- **What & why.** When a leaf's accounts are still being fetched
  (a season's journeys, a search through the book), the reader
  is shown the leaf itself, unposted: paper, red ruling, a
  pencilled folio numeral, and the *shape* of entries to come —
  ruled line-blocks in pencil-grey where entries will stand,
  each block the true height of its entry if known, or the
  house's standard entry height if not. It belongs because
  loading in a ledger is not a spinner — nothing in a counting
  house spins — it is a leaf prepared and waiting for its
  entries: the ruling is printed before the writing arrives, in
  the world exactly as on paper.
- **Structure.** A leaf skeleton mirroring §6.3's geometry
  (same column, same `--rule-unit` rhythm): head-rule in gilt at
  40%, entry blocks as ruling-toned rectangles with one
  pencil line (`--ink-soft` at 30%) per text line, figures
  column as a narrower block on the decimal axis. The skeleton
  is `aria-hidden` with a visually-hidden "The leaf is being
  entered…" status (below).
- **Motion spec.** No shimmer — shimmering paper is a screen
  pretending to be wet, and this house's wet is §6.6's, earned.
  The skeleton is still, except one licensed motion: a pencil
  line at the foot of the last block draws itself slowly
  (1200ms `--ease-rule`, once) — the clerk has begun. Entries
  arriving replace blocks one-for-one with §6.3's posting;
  a leaf not filled within 900ms keeps its skeleton without
  apology, and at 4000ms the skeleton's foot gains a clerk's
  note: "The post is slow today. What has arrived is above;
  the rest is coming." — the book narrates its own delay in its
  own voice (§12) rather than spinning about it.
- **States.** Prepared (skeleton) → posting (entries replacing
  blocks in order) → posted (skeleton gone). Partial arrival is
  a first-class state: arrived entries are fully posted and
  readable while later blocks wait — the leaf is never held
  hostage to its slowest entry.
- **Content merge.** The skeleton's blocks are the coming
  entries' true shapes — same count, same order, same folios —
  generated from the fetch's manifest, so the prepared leaf is
  already information: how much book is coming, and where.
- **Failure fallback.** Fetch failure: blocks are replaced by
  one clerk's note entry — "This leaf could not be fetched from
  the strong-room. [Try again] — the rest of the book is
  unaffected." — with a real retry button (§11). No JS: the
  leaf's content is server-rendered in the first place on all
  primary pages; the skeleton serves only client-side
  collections (search, season filters).
- **Reduced-motion variant.** Skeleton still, pencil line
  printed rather than drawn, the 4000ms note still arrives (it
  is information, not motion).
- **Performance budget & mobile variant.** CSS blocks only,
  zero assets. Mobile: identical geometry at the mobile entry
  rhythm; the figures-column block drops (figures stack, §6.3).
- **Choreography timeline (v2).** t=0 leaf prepared → t=0–1200
  pencil line draws once → entries replace blocks as they land
  (§6.3 each) → t=4000 (if incomplete) clerk's note posts →
  complete when the last block is replaced.
- **State matrix (v2).** *Rest:* n/a (transient). *Hover:* none.
  *Focus:* the status is reachable by AT; no focusable skeleton
  parts. *Active:* retry (on failure) is a real button.
  *Scrolled-past:* skeleton continues off-screen; arrival still
  posts. *Disabled:* server-rendered content, no skeleton.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full geometry with figures
  column. 768–1199px: full, narrower blocks. <768px: stacked
  blocks, no figures column.
- **Edge cases & failure modes (v2).** *Manifest lies (more
  entries arrive than blocks):* extra entries post beneath the
  prepared leaf with their own rule — the book adds a leaf
  rather than squeezing its ruling. *Zero results (a search
  through the book finds nothing):* the skeleton is replaced by
  the empty leaf of §12's voice — "No account answers to that
  name. The book suggests…" with the nearest folios — never a
  blank page with a magnifying glass.
- **Accessibility spec (v2).** A single `role="status"` line
  announces the leaf's arrival once ("Six accounts entered"),
  never per entry. Skeleton blocks are `aria-hidden`; focus is
  never placed inside a skeleton. The failure note and retry are
  real, reachable content.
- **Tokens consumed (v2).** `--paper`, `--ruling`, `--ink-soft`,
  `--gilt`, `--ease-rule`, `--dur-pencil` (1200ms),
  `--rule-unit`.

### 6.17 The closing leaf — footer & signature

- **What & why.** The book ends the way accounts end: on an ink
  leaf (`--ink-deep` ground — the book's cover, turned inward)
  the final balance is struck (§6.5's final form), the contents
  are re-entered in brief (folios in `--gilt-pale`), the house's
  direction is posted (address, post, wire — in the world's
  words, §12), and the clerk signs: the seal (§6.1's device)
  stands at rest beside a signature line, and beneath it the
  colophon — set in the book, by whom, in what faces. It belongs
  because a footer in this theme is not a sitemap with a
  copyright line; it is the closing of the account the page
  opened, and a reader who reaches it should feel the book shut
  with the same ceremony it opened with — seal, balance,
  signature.
- **Structure.** A `<footer>` leaf: struck balance (three totals
  as real text with their wheels' static twins), a two-column
  contents reprise (Garamond, paper on ink-deep 13.62:1-class —
  paper on `--ink-deep` is the table's pairing inverted and
  holds by the same computation class as §2's ink-on-paper),
  the house's direction block, the seal + signature rule, and
  the colophon in apparatus size. The gilt double rule of §6.5
  is the leaf's head.
- **Motion spec.** The leaf posts as the book's last entry
  (§6.3): its balance wheels settle to the final sums as it
  crosses (§6.5's strike), the seal — already present — receives
  one lamp swell (§6.9's ease, 600ms) as the signature line
  draws beneath it (500ms `--ease-rule`). Nothing else moves:
  the end of the book is the stillest place in it.
- **States.** Printed → posting → closed (final; the struck
  state is permanent for the session). Hover/focus on reprise
  links: gilt-pale brightens to paper + ring in gilt-pale.
  The seal does not re-fall — a book is sealed once (§6.1).
- **Content merge.** The closing balance is the same sums as
  §6.5's, struck finally; the reprise folios are §6.11's leaf
  map; the direction block is the house's real address — the
  leaf is the page's facts, closed and signed, and §10 audits
  its totals against the entries like any other figure.
- **Failure fallback.** No JS: printed struck balance, printed
  seal, printed signature rule — the closing leaf is complete
  as static print (it is the page's most important no-JS
  surface after the entries themselves).
- **Reduced-motion variant.** Printed; the signature rule drawn;
  no lamp swell.
- **Performance budget & mobile variant.** Reuses seal, wheel
  and entry systems; own cost is the ink leaf's CSS. Mobile:
  reprise stacks to one column, balance totals stack per §6.5's
  mobile rule, seal 56px beside the signature.
- **Choreography timeline (v2).** t=0 leaf crosses → wheels
  settle to finals → §6.5's 400ms stability → double rule
  (already the leaf's head) is struck by the "Balanced." posting
  → signature rule draws 500ms → lamp swell on the seal 600ms →
  closed.
- **State matrix (v2).** *Rest:* closed, struck. *Hover:* links
  brighten. *Focus:* ring in gilt-pale. *Active:* link press →
  §6.10 turn (the book reopens at the chosen folio). *Scrolled-
  past:* n/a (the foot). *Disabled:* printed closed.
  *Touch:* links ≥44px.
- **Breakpoints (v2).** ≥1200px: two-column reprise + balance
  row. 768–1199px: balance row, reprise one column. <768px:
  all stacked; colophon last, smallest, as colophons are.
- **Edge cases & failure modes (v2).** *A page too short to
  have earned a closing (a single-leaf page):* the closing leaf
  still strikes its balance — of one leaf — because a small
  account closed properly is the house's whole advertisement.
  *Legal lines (registration, terms):* entered in the colophon
  block in apparatus voice — the book files its legal existence
  where books do, at the back, in small print that is actually
  legible (13.5px minimum, paper on ink-deep).
- **Accessibility spec (v2).** Footer landmark; struck totals
  are real text (the wheels' twins, §6.5); reprise is a list of
  real links with folio names; contrast: paper on ink-deep —
  computed class 13.62:1 by symmetry with §2's ink-deep on
  paper; gilt-pale on ink 6.98:1 for labels ≥14px.
- **Tokens consumed (v2).** `--ink-deep`, `--ink`, `--paper`,
  `--gilt`, `--gilt-pale`, `--seal`, `--ease-rule`, `--ease-lamp`,
  `--dur-strike` (700ms).

### 6.18 The missing leaf — the 404 page

- **What & why.** A folio that does not exist is a leaf missing
  from the book, and the error page says so in the book's own
  terms: a paper leaf, ruled, bearing one entry in the clerk's
  hand — "Folio {n} is not in this book." — the torn stub of the
  missing leaf shown at the gutter (a gilt-edged paper fragment,
  slightly rotated like §6.4's stamps, because even the book's
  damage is physical), the nearest true folios entered beneath
  as "the book offers instead", and the contents leaf (§6.11) in
  full below. It belongs because an error page is where a
  theme's honesty is cheapest to fake and most valuable kept: a
  house that posts its disappointments (§6.13) does not meet a
  lost traveller with a cartoon mascot.
- **Structure.** A single leaf: head-rule, the clerk's entry
  (Garamond 20px, the requested folio in tabular figures), the
  stub (an SVG paper fragment with a torn edge path and gilt
  fore-edge, resting at −3°), an offers list (3 nearest leaves
  as §6.11 lines with folios and leaders), and the full contents
  leaf. The requested path is printed in the entry as entered —
  the book shows the traveller their own handwriting, as it
  were — sanitised to text, always.
- **Motion spec.** The leaf posts as an entry (§6.3) on load —
  settle 500ms, rule draws — and the stub settles at its
  rotation with a 300ms `--ease-seal` press (it was *placed*,
  not animated in). Nothing else moves; a missing leaf is a
  quiet room. The offers regard under §6.9. Watchdog per §6.3.
- **States.** Printed → posted. Hover/focus on offers: §6.9 +
  §6.11 states. There is no retry state — the leaf does not
  exist; the page does not pretend refresh will bind it in.
- **Content merge.** The offers are computed from the real leaf
  map (nearest by folio and by name-likeness to the requested
  path), and the contents below is §6.11's own — the error page
  is a leaf of the book, bound in the same volume, not a
  separate microsite with the logo pasted on.
- **Failure fallback.** The 404 is server-rendered static HTML
  with the theme's CSS — it must work when everything else has
  failed, so it depends on no JS, no fetch, and no webfont
  (system serif fallback stack is specified for it alone:
  Garamond, Georgia, serif — a missing leaf in a borrowed hand
  is still a leaf).
- **Reduced-motion variant.** Printed; the stub stands at its
  rotation; the rule drawn.
- **Performance budget & mobile variant.** The lightest page in
  the theme: ≤25KB total including CSS, no JS required. Mobile:
  stub shrinks to 72px and sits inline beside the entry's head;
  offers stack.
- **Choreography timeline (v2).** t=0 load → leaf settles 500ms
  → stub presses at t=200, 300ms → rule draws by 700ms → posted
  → watchdog ceiling 1600ms (§6.3's).
- **State matrix (v2).** *Rest:* posted. *Hover:* offers regard.
  *Focus:* ring per §6.9. *Active:* offer → §6.10 turn (or plain
  navigation — the turn is an enhancement, §6.10). *Scrolled-
  past:* n/a. *Disabled:* fully printed (the native state).
  *Touch:* offer rows ≥48px.
- **Breakpoints (v2).** ≥1200px: stub 120px in the margin rail.
  768–1199px: stub 96px, leaf's top-right. <768px: stub 72px
  inline; contents leaf full below.
- **Edge cases & failure modes (v2).** *Requested folio is a
  real leaf under a mistyped case or trailing slash:* the entry
  says so and offers the true leaf first, marked "entered under
  a slightly different hand" — the book corrects the traveller
  courteously, with the correction shown. *Hostile path strings:*
  printed as inert text, length-capped at 80 characters with
  the overflow noted ("…and further characters, which the clerk
  declines to copy out") — even sanitisation is done in voice.
- **Accessibility spec (v2).** The page's `<h1>` is the clerk's
  entry sentence itself (the error is the heading, in words);
  HTTP status is 404 (the page never soft-404s — a missing leaf
  reported as found would be the book lying about its own
  contents, §1's final form). Offers are a list of links with
  folio names. Contrast per §2.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--ink-soft`,
  `--gilt`, `--ruling`, `--seal-deep`, `--ease-post`,
  `--ease-seal`, `--dur-post` (600ms).

## 7. Page application map

**Home — the book opened.** Seal (§6.1), engrossed headline
(§6.2), contents leaf (§6.11), the season's three principal
accounts posted as entries (§6.3) with their names lettered
(§6.7) and stamps (§6.4), the running balance at the accounts'
foot (§6.5), one letter (§6.15) entered as evidence, the
disbursements leaf in brief (three rows, §6.13, linking to its
full leaf), the account-opening leaf (§6.14), closing leaf
(§6.17). The home page is the whole argument in one opening:
warranted, itemised, honest, open for accounts.

**Collection / listing — the season's accounts.** Journey cards
(§6.12) in ruled grids, filtered by season and temper via the
unposted leaf (§6.16) on change; the contents leaf compresses
to its header form; the balance on this page totals the
*collection's* figures and says so ("the balance of this leaf")
— a page may strike a sub-balance if it labels it, never if it
lets it pose as the book's.

**Journey detail — one account, full leaf.** The entry (§6.3)
at full itemisation (every leg, stay, guide and charge), its
name lettered (§6.7), its stamp (§6.4), its journal lines, its
own disbursements rows (§6.13's table scoped to this account
and cross-referenced both ways), letters referring to it
(§6.15, by folio), and the account-opening form (§6.14) with
this journey pre-entered — the summary account is the entry's
own lines, so detail and booking can never disagree.

**About — the house's own account.** The house's history posted
as entries (founded, the lean years entered as disbursements —
the about leaf carries the theme's bravest table), the clerks
presented as signatories (name, hand, since), the book itself
described: how accounts are kept, what the seal warrants, why
disappointments are posted. About pages in this theme are
audited like accounts: every claim a posting or a confession.

**Contact — a letter to the house.** Not a form with a map
widget: a letter leaf — the traveller writes (name, direction,
their matter) on ruled lines (§6.14's field system, without the
account summary), posts it with the small seal, and receives a
folio number for their letter. The house's direction (§6.17's
block) stands beside it for those who prefer the post.

**Checkout / deposit — the account's first posting.** Where a
deposit is taken, the payment step is entered as the account's
first disbursement: the summary account (§6.14) stands
unchanged beside the payment fields (the payment provider's own
furniture, admitted as a foreign leaf and labelled as such —
"the payment is taken by {provider}, entered here as a
disbursement" — §1's honesty applied to the seam every theme
tries to hide), and the confirmation is the account entry with
the deposit posted as its first line.

## 8. Worked examples

### 8.1 The hero (home) — the book opened under seal

**The build.** The opening leaf: paper ground, gilt head-rule,
the seal (§6.1) at the rule's right, the engrossed headline
(§6.2) — the worked example's house is a rail-journey atelier,
and its headline is "JOURNEYS, ENTERED AND BALANCED" (4 words,
Cinzel 56px). Beneath, the standfirst in Garamond: the house's
warranty in prose (name, since, what the seal means). Then the
contents leaf (§6.11) — six leaves with folios and figures —
and the first account already posting below the fold: the
Trans-Siberian entry, its head crossing the reading line as the
reader settles.

**Scroll timeline.** t=0 load → fonts race (700ms) → seal falls
(900ms ceremony) → engrossing arms at t=900, completes ~t=2800
(4 words) → standfirst posts → contents lines settle (60ms
stagger) and leaders draw → ribbon glides to folio 1 → the hero
leaf pins for 120vh while the first three entries (posted in
the leaf's lower half: the season's three principal journeys in
brief) write in sequence as the pin scrubs → pin releases into
the accounts leaf. Reduced motion: the leaf stands complete —
seal printed, headline engraved, contents posted, three entries
ruled — a finished opening, still.

### 8.2 Mid-page: the Samarkand account (journey detail)

**The build.** The leaf of one journey: name lettered (§6.7) —
"SAMARKAND" in Garamond italic at 56px, gilt underline — above
the full entry (§6.3): 11 itemised lines (the night train from
Tashkent, 4 nights at the registan-side house, the guide
Maqsud, the calligraphy masterclass…) each with its figure on
the decimal axis, summing to the entry's total ruled beneath.
The destination stamp (§6.4) rests in the margin at −3.1°
(seeded from the name). The journal lines run italic between
the lines' groups. Below the entry, its disbursements (§6.13
scoped): "Day 9: rain. Charged to experience." — the exemplar,
here in its true home — and the flooded-road fare as its money
row, cross-referenced. A letter (§6.15) from the traveller who
took it in October follows, folio-linked.

**Scroll timeline.** Name crosses the line → lettering 620ms +
underline → entry posts (settle 600ms, rule at +200) → blot
lifts (950ms dry) → stamp falls as the entry's foot locks
(700ms) → disbursements leaf settles as one (600ms), its
sub-balance wheel turns → the letter posts → the balance in the
margin (§6.5's running form) has been adding the entry's figures
wheel-step by wheel-step throughout. The reader has watched an
account be opened, kept, rained on, and balanced — the whole
theme in one leaf.

### 8.3 Conversion: opening the Samarkand account (booking)

**The build.** §6.14's leaf with the Samarkand journey
pre-entered from §8.2's entry: fields on ruled lines (name,
direction, dates, party of two), the summary account at the
right re-posting the entry's 11 lines condensed to 5 (legs,
stays, guide, masterclass, the house's fee — each a line, the
fee printed as a line because a fee hidden in a total is a
smuggled figure), a deposit line (20%, computed and printed as
arithmetic: "deposit, one fifth: £970"), and the total £4,850
— the sum, checkable against §8.2's entry and §6.12's card,
which carry the same total from the same lines.

**Scroll timeline.** The leaf posts on arrival (§6.3). Focus
moves line to line, each deepening with its margin tick. The
party field changes 2→3: a per-traveller line appears in the
summary, wheels turn, the total re-strikes at £6,140 with its
arithmetic printed. An error is made on purpose in the example:
the direction field is left empty on submit — the line's rule
turns seal-deep, the margin note appears in the clerk's voice
(§12): "The direction line is empty — the house cannot write
back to an address it has not been given." Nothing shakes;
nothing is cleared. Corrected, resubmitted: the seal falls
(500ms), folio № 7 prints (the contents ended at 6), and the
confirmation entry replaces the form — name, journey, dates,
party, total, deposit — closing with the house's line: "Your
account is opened. The book will write to you before the week
is out." The traveller screenshots confirmations; this one is
worth the screenshot.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The smuggled total.** A price or total that is not the sum
   of printed lines. *Cure:* §1's audit — every figure traces
   to a posting; §10 sums the DOM. This is the theme's mortal
   sin; all others are venial.
2. **Calligraphy as a font trick.** Destination names set in a
   script font, or "drawn" with uniform stroke-width animation.
   *Cure:* §6.7's aperture-mask swell over real italic Garamond
   print — or print alone, which is always respectable.
3. **The blot that hides the numbers.** Blotting masks (§6.6)
   wandering over figures, or sheens that lighten text. *Cure:*
   figures are exempt by structure; sheen contrast floor 7:1;
   §10 checks the mask's geometry.
4. **Stamp confetti.** Stamps as decoration — on every section,
   at random runtime rotations, in brand-red gradients. *Cure:*
   stamps certify itinerary leaves only, seeded rotations,
   rationed by §2's 4% pixel audit.
5. **Gilt as a surface.** Gold backgrounds, gold buttons, gold
   gradients on panels. *Cure:* gilt is a line and an edge
   (§2's geometry ration); the moment it fills, the book is
   gilded shut.
6. **The wandering lamp.** Hover glows and spotlights applied
   globally, cursor-follow light, a second ambient loop. *Cure:*
   one lamp, bound to entries (§6.9); one ambient breath (§5);
   no cursor effects of any kind, ever.
7. **Three clerks at once.** Simultaneous performances — an
   entry writing while a name letters while a stamp falls in
   the same viewport. *Cure:* §4's density law — one performance
   at a time, sequenced by the reading line (§13).
8. **Cinzel creep.** Display face leaking into buttons, labels,
   prices, body — or letterspaced lowercase anywhere. *Cure:*
   §3 law 2's four licensed homes for Cinzel; the gate greps
   computed styles on a sample of components.
9. **The contents that disagrees.** Hand-maintained nav whose
   folios, counts or order drift from the leaves. *Cure:* the
   contents generates from the leaf map at build (§6.11).
10. **Squeezed confessions.** The disappointments table crushed
    into narrow columns or shrunk type to fit a grid. *Cure:*
    §6.13's stacking rule — confessions get their full measure
    at every width.
11. **The eaten form.** A submission failure that clears the
    traveller's entries, or a spinner where the seal should be.
    *Cure:* §6.14's stall rule — entries preserved, note in the
    clerk's voice, seal or nothing.
12. **Curated praise.** Testimonial carousels, star ratings,
    letters excerpted to their happiest clause. *Cure:* §6.15 —
    letters filed whole, folio-bound, weather included.
13. **The brochure in the book.** An "entry" whose lines are
    marketing adjectives instead of itemised fact. *Cure:* an
    entry is lines with figures, or it is labelled a journal
    entry and charged "no charge" (§6.3) — the book always
    knows which it is holding.

## 10. Quality gate

Blocking — every item must pass before the theme may be used:

1. **Figure audit.** A script sums every entry's printed lines
   and compares: entry totals, card totals (§6.12), form totals
   (§6.14), the struck balance (§6.5/§6.17). Any mismatch, any
   hand-typed total, fails the build.
2. **Disappointments present.** Every journey account carries
   its disbursements rows, cross-referenced with §6.13; a book
   with no bad weather fails.
3. **Print test.** With JavaScript disabled, the whole page is
   readable: entries complete, totals printed, seal at rest,
   contents whole, form submittable.
4. **Watchdog drill.** With the rAF loop artificially stalled,
   every ceremony completes or cancels within its watchdog
   ceiling (§6 timings); no content is stranded mid-performance.
5. **Contrast census.** Every text pairing measures at or above
   §2's computed ratios; sage-class errors (baize or gilt used
   as small text) fail on sight.
6. **Stamp census.** Stamps only on itinerary leaves; rotations
   within the seeded 2.0–4.0°; seal-red ≤4% of any viewport
   screenshot.
7. **Performance census.** One performance at a time (§4) under
   a scripted scroll; long tasks ≤50ms during ceremonies; the
   shared loop is the only scroll-driven writer.
8. **Blot geometry.** §6.6 masks never intersect the figures
   column at ≥768px; sheen never drops text contrast below 7:1.
9. **Cinzel census.** Cinzel computed on leaf titles, hero,
   stamp rings and the closing name only (§3 law 2).
10. **Contents agreement.** §6.11's folios, order and figures
    match the DOM's leaf map exactly.
11. **Reduced-motion pass.** With `prefers-reduced-motion`, the
    page is the finished book: written, ruled, struck, sealed —
    and every figure still audits (gate 1 re-run in this state).
12. **Folio continuity.** The form's first confirmation folio
    continues the contents' sequence (§6.14); a folio used
    twice, anywhere, fails the book.

Minimum bar: 12/12 blocking. No partial pass ships — a ledger
that balances in 11 of 12 respects is a ledger that does not
balance.


## 11. Component inventory

Every component a real Grand Tour site needs, with its themed
treatment — or its refusal, which is also a treatment. The
refusals matter: a component admitted in its generic form is a
foreign clerk at the desk.

| Component | Treatment in this theme |
|---|---|
| Primary button | An entry line: Garamond 600 text on a ruled line with a gilt end-cap; press = translateY(1px) + the rule deepens (§6.9's lamp in miniature). Never a filled pill, never Cinzel. |
| Secondary button | A pencilled line: `--ink-soft` text, dotted ruling underline; regard (§6.9) inks it. |
| Text input | A ruled line (§6.14): label above in the clerk's hand, Garamond input on the line, line deepens on focus, seal-deep on error. No boxes. |
| Select | An entry line with a gilt folio-arrow; options are accounts with figures (§6.14). Native behaviour, themed dress. |
| Date input | Native input on a ruled line; its value sets in tabular Garamond — dates are figures here. |
| Checkbox / radio | A small square ruled box; the clerk's tick is an SVG stroke drawn 160ms `--ease-rule` when checked — a tick entered, not a state toggled. Radio = the seal dot (§6.11's press) at 10px. |
| Table | The ledger table (§6.13): ruled rows, tabular figures on the decimal axis, caption in Cinzel, sub-balance closing line. Zebra striping refused — the ruling *is* the stripe. |
| Badge | Refused as a pill. A badge's job is done by a margin note in the clerk's hand ("new this season") or by a stamp (§6.4) where certification is meant. |
| Alert / notice | A clerk's margin note: seal-deep rule at its left, apparatus voice (§12), posted like an entry (settle 400ms). Never a coloured banner; the book does not have banners. |
| Toast | Refused. News from the house arrives as an entry posted at the foot of the current leaf (§6.14's confirmation pattern) — a toast is a shout from another room. |
| Modal | A leaf laid over the book: paper panel, gilt head-rule, the underlying leaf dimmed by a baize shadow (not a black overlay — the desk, not a void). Opens by settling (350ms `--ease-post`), closes by lifting; focus trapped per standard practice; the seal stands at its head when it confirms anything. |
| Tabs | Folios: a row of folio numerals with leaf titles; the active tab is marked by the ribbon (§6.10) resting beneath it. Switching posts the new leaf (§6.3) — tabs here change the page you are on in the book, so they behave like it. |
| Accordion | A leaf folded: head-rule + title; opening draws the rule and settles the entries inside (320ms). Only one leaf open per group — a book open everywhere is a book dropped. |
| Pagination | Folio turns: "← Folio 2 of 5 →" in Garamond with the ribbon marking the current; numbered as folios, never as a row of boxed digits. |
| Breadcrumbs | A contents line (§6.11 compressed): "Contents · The Accounts · Samarkand" with gilt leaders — the path back through the book, in the book's grammar. |
| Progress bar | Refused as a bar. Progress is the ribbon (§6.10) + the fore-edge (§6.8); a determinate task (an upload to the house) uses the digit-wheel manner: a ruled line filling with ink strokes, one per tenth, labelled in figures. |
| Spinner | Refused (§6.16). Waiting is an unposted leaf. |
| Tooltip | A margin note card: paper-shade, clerk's hand, appears after 600ms regard, beside the margin it annotates — never above text it would cover. |
| Card | The account card (§6.12) — the only card in the theme. |
| Form errors | Margin notes in seal-deep (§6.14, §12). Summary errors are refused: the clerk speaks at the line that erred. |
| Empty state | An honest empty leaf (§6.15, §6.16): head-rule, one clerk's line in voice, the way onward offered as contents lines. |
| Search | A search through the book: an index leaf — the query entered on a ruled line, results posted as contents lines (§6.11) with folios; no-results per §6.16's empty leaf. |
| Price display | Always an account: lines + ruled total (§6.12/§6.14). A lone price is a smuggled figure (§9.1). |
| Image / plate | A pasted plate (§5, §6.12): paper mount, gilt hairline, caption with place and day. Edge-to-edge imagery refused. |
| Video | A plate that moves: same mount, a small seal-dot play mark; the house prefers the written account and says so in the caption when a film is offered instead of one. |

## 12. Content & copywriting voice

**Two voices, never blended.** *The Clerk* keeps the book:
upright Garamond, complete sentences, figures always in words
and numerals together at first use ("four nights (4)"), no
contractions in apparatus, courtesy without warmth — the clerk
is not your friend; the clerk is *accurate*, which is better.
*The Traveller* writes the journal lines and letters: italic,
contractions welcome, weather permitted, first person. A page
where the clerk jokes or the traveller itemises has mixed its
hands (§9's voice failure, policed like a figure error).

**Headline style.** Cinzel, ≤7 words, a statement of procedure
or place, never a promise: ✓ "JOURNEYS, ENTERED AND BALANCED" ·
✓ "THE SIBERIAN ACCOUNT" · ✗ "UNFORGETTABLE LUXURY ESCAPES
AWAIT" (a promise, three adjectives, no procedure). Section
titles name the leaf's contents as a contents leaf would:
"The Accounts", "Disbursements & Disappointments" — not
"Why travellers love us".

**Label style.** Apparatus labels are short nouns in the
clerk's hand: "Direction" (not "Email address" — the house
writes to a direction; the field's `type` is email and its
autocomplete is honest, but its label is the book's word),
"Party" (not "Guests"), "Entered at" (not "From"). Buttons are
verbs the book performs: "Open the account", "Post the letter",
"Strike the balance" — never "Submit", which is what one does
to a form, not to a house.

**Error voice.** The clerk states the fact, the consequence,
and the remedy, in that order, without apology or alarm:
✓ "The direction line is empty — the house cannot write back
to an address it has not been given. Enter it above, and post
again." · ✓ "Those dates fall in the closed season — the pass
is shut from November. The book suggests the October account,
folio 3." · ✗ "Oops! Something went wrong!!" (three failures
in five words: familiarity, vagueness, punctuation this house
does not own).

**Empty-state voice.** The book remarks on its own emptiness
and offers the way on: ✓ "No account answers to that name. The
book suggests the accounts nearest in temper, below." ·
✓ "No letters yet. The book is young; its accounts are open
above."

**Fixed strings (verbatim, do not paraphrase).** The
disappointments exemplar: *"Day 9: rain. Charged to
experience."* · The balance's closing word: *"Balanced."* ·
The confirmation's close: *"Your account is opened. The book
will write to you before the week is out."* · The slow-post
note (§6.16): *"The post is slow today."* · The 404 entry's
form: *"Folio {n} is not in this book."*

**Numbers style.** Miles with commas, tabular; money with the
currency before the figure and no decimals on whole pounds
("£4,850"); per-line figures always, totals always labelled as
sums ("the sum of the lines above"); dates written out in
entries ("the 9th of October") and tabular in tables. A figure
without its unit is an unposted figure.

## 13. Full-page scroll choreography map

Nine beats, home page, in order. One performance at a time
(§4); the shared loop (lerp 0.12) carries beats 5 and 8
continuously beneath the rest.

1. **The opening (load).** Seal falls (§6.1, 900ms) →
   engrossing (§6.2, ~1900ms) → standfirst posts → contents
   leaf settles line by line (§6.11) → ribbon glides to folio 1.
   The visitor feels: a book being opened *for* them, by a hand
   that is not hurrying.
2. **The pin (hero leaf, 120vh).** The leaf holds while its
   three brief accounts write in sequence (§6.3) as the pin
   scrubs — the season's offerings entered before the reader's
   eyes, each blotted dry (§6.6).
3. **The accounts.** Full entries post one by one at the
   reading line; names letter (§6.7) ahead of their entries;
   stamps fall as leaves lock (§6.4). The rhythm is the brand:
   write, dry, rule, stamp — write, dry, rule, stamp.
4. **The collection.** Cards post in reading order (§6.12);
   the leaf's sub-balance labels itself as a sub-balance.
5. **The running balance (continuous).** Wheels turn at the
   accounts' feet as figures cross the line (§6.5); the ribbon
   slides folio to folio (§6.10); the fore-edge darkens
   (§6.8). The visitor's peripheral sense: the book is keeping
   up with them, and keeping score honestly.
6. **The honesty leaf.** Disbursements settle as one (§6.13) —
   a tempo change the reader feels: after the ceremonies, plain
   dealing. Its sub-balance strikes quietly.
7. **The letter.** One letter posts (§6.15), italic, narrower —
   another tempo change: a human voice inside the procedure.
8. **The opening of an account.** The form leaf (§6.14) posts;
   from here the choreography is the visitor's own — focus
   deepening line by line, the summary re-posting at changes,
   and (on submit) the seal, the folio, the confirmation entry.
9. **The closing.** The ink leaf (§6.17): wheels settle to the
   finals, "Balanced." posts, the signature rule draws, the
   seal takes its one lamp swell. The book shuts. **Reverse
   pass:** scrolling back up, nothing un-posts, un-stamps or
   un-strikes; wheels turn back honestly (§6.5), the ribbon
   returns, the edge lightens — the book remembers forward and
   reports backward. **Jump scroll / anchor arrival:** catch-up
   posts everything above the landing line instantly (rules at
   rest, stamps at rest, wheels at their sums) — a traveller
   who opens the book at the middle finds it kept up to there,
   never a flurry of belated ceremony. **Reduced motion:** the
   same nine beats as a finished book — every beat's resting
   state, in the same order, with the same figures.

## 14. Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight (home, first load) | ≤ 880KB | Fonts are the largest single item; see below |
| Fonts | ≤ 120KB | Cinzel (1 weight, latin subset) + EB Garamond (regular/500/600 + italic, subset); `font-display: swap` with the §6.1/§6.2 font races as the behavioural budget |
| Inline SVG (seal, stamps, stub, plates' frames) | ≤ 40KB total | Seal ≤3KB, stamps ≤4KB each (≤6), textures shared via one `<defs>` |
| Calligraphic path assets (§6.7) | ≤ 9KB per name, ≤ 3 names per page | Build-time assets; a fourth name is an editorial decision to print, not a budget overrun |
| Images (plates) | ≤ 90KB per plate, responsive srcset | Mount aspect reserved; plates lazy-load below the second leaf |
| JS (theme systems) | ≤ 38KB gz | One shared loop, the posting observer, the wheel/balance module, the form module; no framework |
| CSS | ≤ 30KB gz | The ruling system and entry system shared by §6.3/6.11/6.12/6.15 |
| Animation frame budget | ≤ 1.6ms/frame main-thread | The loop writes transforms/opacity/registered properties only; wheel steps are text-free (pre-rendered strips) |
| Long tasks during ceremonies | ≤ 50ms | Gate 7 (§10) measures under scripted scroll |
| Simultaneous performances | 1 | §4's density law as a performance rule: sequencing is the budget's enforcement arm |

**Cut order when the budget is exceeded** (cut in this order,
never skip a step): (1) the thumb band on the fore-edge (§6.8);
(2) plate scale-in (plates rest at scale 1); (3) the blotting
sheen (blots lift without it, §6.6); (4) the hero pin (entries
post unpinned); (5) calligraphic lettering beyond the first
name (names print, §6.7's honour intact); (6) the ink ring on
the seal (the seal falls unringed). **Never cut:** the printed
completeness of any element, any watchdog, the figure audit's
DOM sums, the reduced-motion variants, focus states, or the
disappointments leaf. A page that balances its budget by
dropping its honesty has misread which ledger matters.

## 15. Build-order checklist

1. **The static book first.** Build the entire page as finished
   print — entries, totals (hand-verified once), contents,
   closing leaf — with no JS. This artefact is the fallback for
   every element and the gate's print test (§10.3) is run on it
   before any motion exists.
2. **Tokens & ruling system.** §2's closed token list, §3's
   type laws (tnum/lnum forced), §4's `--rule-unit` rhythm and
   decimal axis. Baselines land on the ruling before anything
   moves.
3. **The leaf map.** Generate the contents (§6.11), ribbon stops
   (§6.10) and folio sequence from one source; wire the form's
   folio continuation (§6.14) to the same sequence.
4. **The shared loop.** Lerp 0.12 progress, the reading line,
   the catch-up rule (§13) — before any element consumes them.
5. **Entries (§6.3) + blots (§6.6).** The posting system, its
   watchdogs, its focus-completion. Everything else in §6 hangs
   on this rhythm.
6. **Stamps (§6.4)** with seeded rotations, and the Arrived
   lines printed first (the stamp is the second posting of a
   fact, never the first).
7. **The balance (§6.5)** — DOM-summed wheels, text twins, the
   strike; then the closing leaf (§6.17) that inherits it.
8. **The opening ceremonies (§6.1, §6.2)** — seal, then
   engrossing, each with its font race and watchdog.
9. **Names (§6.7)** — path assets generated and checked against
   the places' own orthographies; unletterable names print with
   honour and are logged.
10. **Regard & ribbon (§6.9, §6.10, §6.8)** — lamp states with
    focus parity, ribbon stops, fore-edge; page turns last in
    this step and only as an enhancement over plain navigation.
11. **Cards & collections (§6.12, §6.16)** — the listing layer
    and its unposted leaf, with the figure audit (§10.1) wired
    across card/entry/form totals.
12. **The honesty leaf (§6.13) & letters (§6.15)** — content
    entered from real accounts; cross-references checked both
    ways.
13. **The form (§6.14)** — ruled fields, summary-as-account,
    seal confirmation, stall restoration, folio idempotency.
14. **The missing leaf (§6.18)** — static, dependency-free,
    verified by breaking things on purpose.
15. **The gate (§10)** — all 12 blocking checks, run in order,
    including the reduced-motion re-run of the figure audit;
    signed by someone who did not build the page. A gate signed
    by its own builder is a stamp the clerk gave himself, and
    this house does not honour those.
