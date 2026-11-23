# 27. The Society Pages — Expanded (v1 + v2)

*Expansion of theme #27 from `themes-026-050.md`, written directly to the
full standard: the 10-part v1 structure plus the v2 deepening layers
(EXPANSION-STANDARD.md). Identity preserved exactly — the Edwardian social
register as an interface: engagements, arrivals and at-homes announced on
calling cards and engraved invitations. The same four palette anchors
(Card white `#FAF6EC`, Engraving black `#26241F`, Calling-card gold
`#A8853B`, Debutante blush `#D9A7A0`), the same two typefaces (Cormorant
Garamond italic display, Libre Franklin announcements), and all 9 original
signature elements deepened, not redesigned — joined by 3 further
signature-grade elements drawn from the original motion system and 6
page-family elements, 18 in all.*

---

## 1. Concept & world

The page is a morning's calling hour, typeset. The visitor does not browse
a website; they pay a call. On the tea table in front of them sits a stack
of calling cards beside a silver salver, and the visit proceeds exactly as
a call proceeded in 1908: the top card is received first and placed on the
salver, each announcement is presented in its turn, invitations are
uncovered from under their tissue, replies are sent in the correct form of
words, and when the last card has been presented the stack is empty and
the visit is complete. Every mechanism on the page is an act of etiquette
performed on the content itself — the card that turns over *is* the
section heading, the salver that fills *is* the record of what the visitor
has attended, the thinning stack in the header *is* the progress
indicator. There is no chrome in this theme that is not also furniture.

The emotional register is poise. Nothing hurries, nothing shouts, nothing
begs. Announcements are made the way the society pages made them: a name,
an occasion, a date, a place — stated once, in full, in the correct order,
and never repeated with an exclamation mark. The design's luxury is not
ornament; it is the visible certainty that everything on the page knows
its place and its turn.

**The one law.** Precedence is the page's physics. Every card,
announcement and section is presented in precedence order — the hostess's
own announcements first, then engagements by wedding date, then marriages,
then at-homes by date, then arrivals and departures by date — and nothing
may be presented before its turn or out of it. Stagger sequences, card
turns, the calendar stream and even the entrance choreography obey the
order; DOM order *is* precedence order, so the law is auditable in source
(§10, blocking). The corollary: a card has two faces and both are real.
The name side is a true presentation, not a teaser; the details side
carries the complete announcement. Nothing in this theme is ever hidden
behind a gesture — the turn reveals, it never withholds.

**Best fits.** Event and wedding businesses whose product is occasions
(venues, planners, stationers, florists, caterers); members' clubs,
societies and alumni associations publishing arrivals, engagements and
at-homes; cultural institutions with a season of receptions, private views
and patron evenings; luxury hospitality announcing residencies and
salon evenings; a personal site for a host, celebrant or toastmaster. The
theme earns its keep wherever the content genuinely arrives as
announcements about named people on dated occasions, and where the reply
— the RSVP — is the conversion.

**When NOT to use it.** Never for high-frequency content: a register that
announces forty items a day is a feed wearing a costume, and precedence
collapses into a queue. Never for urgent or transactional content
(tickets on sale in ten minutes, delivery tracking, incident status) —
manners are the opposite of urgency and the mismatch reads as parody.
Never for content about unnamed crowds: the register names people or it
is not a register. Never for a brand whose voice is loud, ironic or
discount-driven — a card that says "50% OFF!!" in engraved italic is the
theme's fastest route to §9. And never where replies are not genuinely
collected: the RSVP buttons must work (§6.6, §6.15); decorative etiquette
is worse than none.

**The visit's shape.** A page in this theme is one call: the receiving of
the top card (the hero), a small number of announced sections each
presented by its turning card, the engagement calendar pinned while its
announcements stream beneath in precedence order, the RSVP ledger and
reply card, and a footer that is the salver at the end of the hour —
every card received, the stack beside it empty. Longer registers live on
listing pages (§7), one visit per page.

---

## 2. Palette

Four anchors, inherited exactly. Two derived tokens are admitted —
`--gold-deep` and `--blush-deep` — because the anchors' gold (3.20:1 on
card) and blush (1.95:1 on card) cannot carry text, and a register that
cannot print its names in gold-toned ink still needs a text-grade
relative. Everything else is an anchor at a stated opacity, or the
salver's silver, which is a material, never a colour of type.

| Token | Hex | Role | Usage ratio | Pairing & contrast (measured) |
|---|---|---|---|---|
| `--card` | `#FAF6EC` | Card white — every card face, the table's lit ground, body ground | ~62% of pixels | Ground for `--ink` (14.37:1) and `--gold-deep` (5.39:1) |
| `--ink` | `#26241F` | Engraving black — all engraved lines, names, body text, plate-marks | ~24% | On `--card` 14.37:1; on `--blush` 7.37:1; the only body-text colour |
| `--gold` | `#A8853B` | Calling-card gold — crests, rules, plate-mark accents, the light-catch gradient | ~8% | On `--card` 3.20:1 — display ≥24px, rules and metal only, **never body text**; on `--ink` 4.49:1 |
| `--blush` | `#D9A7A0` | Debutante blush — tissue tint, debutante announcements' wash, hover warmth | ~6% | On `--card` 1.95:1 — grounds and washes only, **never text, never a border that must be seen** |
| `--gold-deep` | `#7D6125` | Derived — text-grade gold for kickers, folios, ledger labels | as needed | On `--card` 5.39:1 — the only gold permitted below 24px |
| `--blush-deep` | `#A96A61` | Derived — display-italic accents, the debutante name line at ≥24px | as needed | On `--card` 3.95:1 — display only, never below 24px, never body |
| `--card-deep` | `#EFE6D0` | Derived — the table surface beyond the cards, salver zone ground, card backs' shade | as needed | `--ink` on it 12.48:1 |
| `--silver` | `#B3AC9C` | Derived material — the salver and its reflection gradient only | salver only | On `--card` 2.09:1 — a metal, never text, never an outline that carries meaning |

**Pairing laws.** (1) Names are always `--ink`; the engraving is black or
it is not engraving. (2) Gold appears on a card only as crest, rule or
light — if a sentence is set in `--gold` below 24px, the build is wrong;
use `--gold-deep`. (3) Blush is a temperature, not a colour of
information: it may warm a ground, tint a tissue, wash a debutante's card;
it may never be the only signal of anything. (4) The salver is the page's
only metal and its only gradient besides the light-catch; silver never
appears in type, buttons or borders. (5) One card, one accent: a card
carries gold *or* blush emphasis, never both — a card dressed in both
reads as a confectionery box (§9.4).

**Dark behaviour — candlelight, not inversion.** The cards do not invert;
the room darkens. Under `prefers-color-scheme: dark` the table surface
falls to `--ink` warmed 6% toward gold (`#2B2620`), the salver zone to
`#211E19`, and every card remains `--card` — paper does not change colour
because the lamps are lit; it is simply the brightest thing in the room.
Gold warms one step (`#B8944A` in dark only, display roles unchanged);
blush deepens to `#C08D85` as a wash. Text contrast is unchanged because
text never leaves the card. A build that inverts the cards to black has
printed the register on coal (§9.9).

---

## 3. Typography

Two typefaces, two duties, never exchanged. **Cormorant Garamond** is the
engraver's hand: italic for names, occasions and display — the lettering
on the card. **Libre Franklin** is the register's clerk: announcements,
dates, ledger figures, labels — everything that must be *recorded* rather
than *admired*. A name set in Franklin is a clerical error; a date set in
Cormorant italic is a affectation. The gate checks the casting (§10).

| Role | Face | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| The name (card face) | Cormorant Garamond italic 500 | 40px / 1.05 (hero 56px) | −0.01em | The person or house presented; always `--ink` |
| Occasion line | Cormorant Garamond italic 500 | 24px / 1.2 | 0 | "requests the honour of your presence" register |
| Display headline | Cormorant Garamond 500 (upright) | 56px / 1.02 ≥1200px; 40px <768px | −0.015em | Reserved for the visit's title; italic only for names within it |
| Section announcement | Libre Franklin 600 | 13px / 1.4 | +0.14em, uppercase | The clerk announces; the card then turns (§6.2) |
| Body / announcement text | Libre Franklin 400 | 16.5px / 1.65 | 0 | The details side; measure 34–52ch on cards |
| Particulars (date, place) | Libre Franklin 500 | 15px / 1.5 | +0.02em | Dates are always spelled or figured in full — "Saturday, the fourteenth of June" in display contexts, `14 June` in the ledger; never `6/14` |
| Ledger figures | Libre Franklin 500, tabular | 15px / 1.5 | 0 | RSVP counts, presentations "n of N"; tabular so the ledger never jitters |
| Kicker / folio | Libre Franklin 600 | 11px / 1.4 | +0.18em, uppercase | `--gold-deep` only |
| The form of words | Cormorant Garamond italic 500 | 19px / 1.4 | 0 | Fixed etiquette strings — "Accepts with pleasure", "Declines with regret" — always in the engraver's hand, never in Franklin |

**Type laws.** (1) Italic is the voice of persons; upright Franklin is
the voice of record. A sentence spoken *by* the house is italic; a fact
*about* the house is Franklin. (2) No exclamation marks anywhere in the
theme — the register has never once been surprised. (3) Names are never
set in all caps; caps are for the clerk's labels only. (4) Numerals in
prose are spelled out below twenty ("fourteen guests"), figured in the
ledger and calendar where they are data. (5) The ampersand is permitted
in names of houses and couples ("Mr. & Mrs. Ashworth") and nowhere else.
(6) Line-height on card faces never drops below 1.4 — engraved lettering
needs air the way it needs the plate-mark's margin.

---

## 4. Layout language

**The table.** The page is a tea table seen from the visitor's side. Its
surface is `--card-deep`; everything the visitor handles sits on it as
paper: cards, invitations, the salver. The reading column is 1120px at
≥1200px, but content rarely fills it — cards are sized as cards, not as
banners. A calling card is 340×190px at desktop (the real 3.5″×2″ ratio,
1.79:1, held at every breakpoint by scaling, never by re-flowing its
face). An invitation card is 520px wide. A full-width announcement card —
the section presenter — spans the column but keeps a card's proportions
of margin: its plate-mark sits 14px inside its edge, its text measure
inside that.

**The salver zone.** A fixed region of the hero and, in reduced form, of
the footer: an ellipse of `--silver` gradient (radial, 2.09:1 against the
table at its brightest — a sheen, not a shape with an outline) on which
received cards accumulate (§6.3). The salver never scrolls away from the
hero; its footer counterpart closes the visit (§6.16).

**The plate-mark.** Every card carries the embossed border left by the
engraver's plate: a 1px `--ink` line at 22% opacity inset 14px, with a
second hairline at 8% inset 17px — the double impression of a real plate.
It is drawn, not printed, on presentation (§6.8). Text never crosses it;
the plate-mark is the card's margin law, and content that would breach it
is set smaller or the card is made larger.

**Rhythm and density.** The table breathes in visiting intervals:
sections are separated by 120px of bare table at ≥1200px (88px at
768–1199px, 64px below) — the pause while the next card is brought in.
Within a section, cards sit 24px apart. Density is deliberately low: a
page presents at most 9 announcements (the morning's post of a
well-run house); a tenth belongs on the next page of the register (§7).
Whitespace here is not emptiness, it is the table's polish — bare
`--card-deep` with nothing on it is a designed state, and filling it with
decoration is §9.6.

**The pinned calendar.** One pin per page is permitted: the engagement
calendar (§6.10), pinned at the top of its chapter while its
announcements stream beneath in precedence order. Nothing else pins —
a table does not follow the visitor around the room.

**Grid.** A loose 12-column grid underlies the table for the calendar
and listing pages, but cards are placed as objects, not cells: slight
rotations are rationed to received cards on the salver (−2° to +2°,
deterministic by index, never random per load) and forbidden on cards
awaiting presentation, which sit square — an unpresented card is never
askew; only a handled one may be.

---

## 5. Full motion system

Five named easings — the house's manners, as curves:

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-present` | `cubic-bezier(.25,.8,.25,1)` | The turn and the presentation: unhurried, exact | §6.2, §6.8, §6.13 |
| `--ease-bow` | `cubic-bezier(.34,1.3,.4,1)` | A small deferential overshoot (≤4%) on settles | §6.1 settle, §6.7 stamp release, §6.11 |
| `--ease-glance` | `cubic-bezier(.4,0,.2,1)` | Light moving across a surface; no overshoot, ever | §6.5, §6.11 sheen, §6.12 |
| `--ease-file` | `cubic-bezier(.5,0,.15,1)` | A card sliding away into a stack: slow start, decisive end | §6.7 filing, §6.9 thinning |
| `--ease-lift` | `cubic-bezier(.2,.7,.3,1)` | Tissue and paper lifting from one edge | §6.4, §6.14 |

Every motion term of the library, in this theme's language:

- **Scroll-triggered reveals** — cards turn (§6.2), tissues lift (§6.4),
  plate-marks draw (§6.8). All are armed by an IntersectionObserver at
  35% visibility and fire **once**: a presented card is never
  un-presented by scrolling away.
- **Scroll-scrubbed motion** — the salver slide (§6.3) and the tea-table
  parallax (§6.12) only. Both read from the single shared rAF loop
  (lerp 0.12); nothing else in the theme is scrubbed, because manners
  are events, not sliders.
- **Pinned scenes** — exactly one: the engagement calendar (§6.10).
- **Masked reveals** — details are uncovered by the lifting tissue
  (a physical mask), never by clip-path wipes or gradient masks; the
  light-catch (§6.5) is the sole gradient-mask effect and it reveals
  nothing — it only polishes what is already legible.
- **Blur-to-sharp** — refused. Engraving is sharp or it is a smudge;
  no element in this theme ever resolves from blur (§9.8).
- **Kinetic typography** — refused. Names do not slide, bounce or
  assemble; a name is *presented*, whole, on its card. The single
  exception is the ledger's figures (§6.6), which count because they
  are data arriving, not lettering performing.
- **Counters** — the RSVP ledger (§6.6) and the header's "presentations
  n of N" (§6.9). Both count real DOM state; an invented figure is a
  gate failure.
- **Progress indicators** — the thinning header stack (§6.9). There is
  no progress bar in this theme; a bar is a machine's furniture.
- **Marquees** — refused. Nothing on a tea table scrolls sideways
  begging attention. The calendar stream (§6.10) moves vertically, at
  reading speed, under the visitor's own scroll.
- **Ambient loops** — one only: the tissue sheen idling over the
  current invitation (§6.12), 9s cycle, ±5% opacity. A second ambient
  loop would make the table fidget.
- **Micro-interactions** — the crest stamp (§6.7), tilt-to-light
  (§6.11), the reply card's ruled fields (§6.15). Each is a gesture
  from the etiquette book, performed on the content object.
- **Hover physics** — tilt-to-light (§6.11): maximum 4°, spring return
  300ms `--ease-bow`, driven by the shared loop; the engraved lines
  brighten as the angle finds the light. No magnetic pull, no lift —
  a card is steadied, not snatched.
- **Page transitions** — the card-receipt transition (§6.18's sibling,
  specced in §6.14's family set as part of the index leaf): navigation
  presents the destination's first card turning; 600ms, same grammar
  as §6.2, never a fade-to-white.
- **Skeleton loading** — an unengraved card: the card's outline and
  plate-mark printed, its face blank card-white with the name's line
  shown as a hairline rule (§6.14). No shimmer — blank paper does not
  sparkle.
- **Reduced motion** — every element carries its own variant (§6);
  globally: all cards rest details-side up, the salver is already
  across the table, counters show final figures, the calendar does
  not pin.

**The fallback law.** Every pre-state (turned card, covered invitation,
undrawn plate-mark) is armed by JS only, after the DOM is readable, and
every armed state carries a 1000ms watchdog: if its trigger has not
fired within 1000ms of the element entering the viewport — or if the
observer itself fails — the element settles to its presented state.
No card may wait forever to be presented; a guest kept standing is a
hostess's failure, and it is a gate item (§10).

---

## 6. Signature elements

### 6.1 The receiving of the top card

- **What & why.** The hero is a visit beginning. A stack of calling cards
  sits on the table beside the salver; 400ms after load the top card is
  received: it lifts, tilts so the light crosses its engraving, travels
  to the salver and settles — and its details side, turned uppermost on
  arrival, carries the visit's headline and first announcement. It
  exists because this theme has no banner and no headline block: the
  first piece of content is *handed to* the visitor, and the receiving
  is the hero.
- **Structure.** `.hero-table` containing `.card-stack` (3 card backs
  visible beneath the top card, offset 3px each — real DOM cards, the
  next announcements in precedence order, not decoration) and
  `.salver-zone` (§4). The top card is `.card.is-top` with `.face-name`
  and `.face-details` as two absolutely stacked faces of one element;
  the details face is rotated 180° on Y in the card's local frame so
  the arrival turn presents it. Headline and CTA live on the details
  face as ordinary DOM.
- **Motion spec.** Trigger: load, gated on `document.fonts.ready` with
  a 300ms cap (Cormorant must be the hand that is received). Beat 1 —
  lift: translateY −24px, 260ms `--ease-bow`. Beat 2 — tilt to light:
  rotateY −14°, rotateX 6°, 380ms `--ease-glance`, carrying the §6.5
  light sweep across the engraved name. Beat 3 — travel: the card
  translates to the salver (40vw at ≥1200px; measured FLIP to the
  salver zone's slot at smaller sizes), 640ms `--ease-present`, turning
  to details-side during the middle 300ms of the travel. Beat 4 —
  settle: shadow contracts from 24px/18% to 10px/12%, rotation comes
  to rest at the salver's deterministic −1.5°, 220ms `--ease-bow`.
  Total 1500ms; the visitor may scroll at any point — the card is in
  flow on the hero table and simply completes.
- **States.** *Rest (pre-load):* the top card lies on the stack,
  name side up, fully legible. *Receiving:* the four beats. *Received:*
  at rest on the salver, details up, interactive. There is no hover
  state on the stack itself; the received card takes §6.11 tilt.
- **Content merge.** The card is the hero content — headline, standfirst
  and the primary reply action are printed on it. Remove the motion and
  the hero is a card on a salver beside a stack: complete, quieter.
- **Failure fallback.** No JS → the top card ships already on the
  salver, details up (server-rendered in its received state; JS arms
  the stacked pre-state only when it can run the receiving). Watchdog:
  if fonts stall past the 300ms cap, the receiving proceeds in the
  fallback face rather than waiting.
- **Reduced-motion variant.** The card is on the salver, details up, at
  first paint. The stack beside it shows the next cards' names.
- **Performance budget & mobile variant.** One FLIP transform on one
  element plus one gradient sweep; zero layout thrash (the salver slot
  reserves the card's box). Mobile (<768px): the table stacks — stack
  above, salver below; travel is vertical, 34vh, beats unchanged;
  the tilt reduces to rotateY −8° (a small card in a small hand).

**v2 — Choreography timeline** (t = fonts-ready or 300ms cap):

| Beat | Time | What happens |
|---|---|---|
| Arm | t −∞ (head script) | JS places the top card on the stack, name up; no-JS leaves it received on the salver |
| Pause | t + 0–400ms | The table is still; the visitor sees the stack and the empty salver |
| Lift | t + 400–660ms | Card rises 24px, shadow deepens |
| Tilt | t + 660–1040ms | Card tilts to the light; §6.5 sweep crosses the engraved name |
| Travel & turn | t + 1040–1680ms | Card crosses to the salver, turning to its details face mid-travel |
| Settle | t + 1680–1900ms | Shadow contracts; card rests at −1.5°; headline is read |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (stacked) | Name side up on the stack, legible | Same |
| Receiving | Four beats as specced | Same, tilt reduced |
| Received | Details up on salver; §6.11 tilt on hover | Details up; no tilt |
| Focus | Focus lands on the details face's reply link only after settle; the card never moves for focus | Same |
| Scrolled-past | Received state persists; never replays | Same |
| Disabled | n/a — the card is content, not a control | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: full spec, 40vw travel.
768–1199px: salver zone narrows; travel measured by FLIP (typically
~30vw). <768px: vertical table, travel 34vh, tilt −8°, stack shows 2
card backs.

**v2 — Edge cases & failure modes.** *Long headline on the details
face:* the face's measure is fixed; headlines are capped at 9 words by
the copy rules (§12) — a longer one is set at 32px and the card grows
to invitation size (520px wide) rather than shrinking the name below
40px on the name face. *Visitor scrolls during travel:* the hero is
in flow; the FLIP target is the salver slot in the same flow, so the
card arrives correctly wherever the page has scrolled to. *Return
visit:* the receiving replays — a call is paid afresh each time; only
the RSVP state (§6.7) persists.

**v2 — Accessibility spec.** Both faces are in the DOM in reading
order (name face first, details second, the second `aria-hidden` until
the turn completes, then swapped — a screen reader meets a card, then
its announcement, never both at once). No focus is moved on load. The
motion is decorative: with it removed, nothing is lost. Name contrast
14.37:1 at every frame (colours never change; only position and the
light sweep's gradient, which peaks at 12% white and cannot drop the
name below 7:1 mid-sweep).

**v2 — Tokens consumed.** `--card`, `--card-deep`, `--ink`, `--gold`,
`--ease-bow`, `--ease-glance`, `--ease-present`, `--dur-receive`,
`--dur-fallback`.

### 6.2 Card-turn announcements

- **What & why.** Every section is announced the way a visitor was
  announced: by a card that turns over. A full-width card at the head
  of each section shows the engraved name of the occasion on its face;
  as the section enters, the card turns — rotateY 600ms — and its
  details side, carrying the section's heading, standfirst and first
  item, becomes the section's true head. There is no other heading
  treatment in the theme; the turn *is* the announcement mechanism.
- **Structure.** `.announce-card` per section: `.face-name` (engraved
  name, plate-mark, §6.8 border) and `.face-details`, both in the DOM,
  the card a `transform-style: preserve-3d` element with
  `backface-visibility: hidden` faces. The card's height is set by the
  taller face (measured once at build or by CSS grid stack — both
  faces in one grid cell, card height = max), so the turn never
  changes layout.
- **Motion spec.** Trigger: IntersectionObserver, card 35% visible,
  once. rotateY 0→180° over 600ms `--ease-present`; at 300ms (the
  edge-on instant) the plate-mark draw (§6.8) completes on the details
  face so the card arrives *finished*. A 60ms pre-beat: the card's
  shadow tightens 2px as if steadied by a hand before turning.
  Sections entering in the same scroll frame turn in precedence order
  with 120ms staggers — never simultaneously, never out of order
  (§1, the one law).
- **States.** *Unpresented:* name side up, square, fully legible —
  a complete state, not a locked one. *Turning:* 600ms. *Presented:*
  details side up, permanent; scrolling away and back never re-turns.
  *Hover/focus:* the presented card takes §6.11 tilt; the unpresented
  card does not tilt — it has not been handed over yet.
- **Content merge.** The details face carries the section's actual
  heading and opening content; the name face carries its true title.
  Neither face is a teaser. Removing the turn leaves a page of
  details-side cards with engraved heads — the reduced-motion page.
- **Failure fallback.** Both faces live in the DOM; without JS the
  details face is shown (server renders details-up; JS arms the
  name-up pre-state only when it can run turns). The 1000ms watchdog
  (§5) flips any card whose observer failed. A card whose section is
  jumped to by anchor turns instantly on arrival (no 600ms wait at
  the destination).
- **Reduced-motion variant.** All cards details-side up at first
  paint; the name survives as the section's kicker line above the
  heading, so no content from either face is lost.
- **Performance budget & mobile variant.** One rotateY per card, ≤2
  turning concurrently (the stagger enforces it); transform-only, no
  repaints beyond the card. Mobile: identical; the turn axis stays Y
  (a card turns the same way in a small hand), duration 520ms.

**v2 — Choreography timeline** (t₀ = card 35% visible):

| Beat | Time | What happens |
|---|---|---|
| Steady | t₀ + 0–60ms | Shadow tightens 2px; the hand is on the card |
| Turn | t₀ + 60–660ms | rotateY 0→180° `--ease-present` |
| Edge-on | t₀ + 360ms | Details face's plate-mark finishes drawing (§6.8) |
| Presented | t₀ + 660ms | Card at rest, details up; section content beneath begins its own entrances |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Unpresented | Name up, square, legible | Same |
| Turning | 600ms rotateY | 520ms |
| Presented | Details up; §6.11 tilt available | Details up; no tilt |
| Hover | Tilt on presented only | n/a |
| Focus | A focusable element on the details face takes the standard ring; an unpresented card turns instantly when focus would land inside it | Same |
| Scrolled-past | Presented, static | Same |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: full-width card, faces at full
measure. 768–1199px: card narrows to the column; name 32px. <768px:
card full-bleed at 20px table margins; name 28px; details measure
full width inside the plate-mark.

**v2 — Edge cases & failure modes.** *Details face much taller than
name face:* the grid-stack height rule means the name face floats in
a tall card — correct and intended; the surplus is card, with the
plate-mark holding the composition. *Many sections entering at once
(fast scroll to foot):* turns queue in precedence order at 120ms
staggers, and any card still unpresented when it leaves the viewport
top is presented instantly — no card may be skipped standing.
*Anchor jump:* instant presentation at the target (§ above). *Print:*
cards print details-side; the name face prints as the section's
running head.

**v2 — Accessibility spec.** The turn is presentational: in DOM order
the section reads kicker (the name, as text) → heading → content,
regardless of which face is visual. The hidden face is `aria-hidden`
and `inert` until presented; on presentation the swap is announced
only by the content becoming available in order — no live-region
noise for a visual courtesy. Keyboard: if focus enters an unpresented
card's details (possible via find-in-page or sequential nav after JS
state changes), the card turns instantly. Contrast on both faces:
ink on card 14.37:1.

**v2 — Tokens consumed.** `--card`, `--ink`, `--gold-deep`,
`--ease-present`, `--dur-turn`, `--dur-fallback`.

### 6.3 Salver slide

- **What & why.** The silver salver — with the cards received so far
  stacked on it — travels across the table, scrubbed to the first
  chapter's scroll. It is the theme's one piece of moving furniture,
  and it earns its motion honestly: the salver is where the visit's
  record accumulates, and its slow crossing of the table is the first
  chapter's timeline made visible. As later cards are received (the
  RSVP filing of §6.7), their destination is wherever the salver has
  reached.
- **Structure.** `.salver` — an ellipse 560×150px at desktop, radial
  `--silver` gradient (brightest 30% off-centre toward the light),
  holding `.salver-stack` of received-card miniatures (the real cards'
  filed copies, §6.7). The salver lives in a `.salver-track` spanning
  the first chapter's width; its reflection is a second, flipped
  gradient ellipse beneath at 18% opacity, moving with it (the fastest
  layer of §6.12's parallax, because a reflection travels with its
  object and reads as speed).
- **Motion spec.** Scrubbed, not triggered: salver translateX maps the
  first chapter's scroll progress (chapter top at 80% viewport →
  chapter bottom at 20%) to 0 → 38vw at ≥1200px (0 → 24vw at
  768–1199px; static below 768px). Driven by the shared rAF loop,
  lerp 0.12 — the salver glides with a heavy object's lag, never
  locked 1:1 to the scrollbar. The reflection streaks: its gradient
  position shifts an additional 12% across the same range. At the
  chapter's end the salver parks; it does not follow the visitor
  further (the footer's salver, §6.16, is a separate, still object).
- **States.** *At rest (chapter start):* salver at the table's left,
  holding only the hero card (§6.1). *Crossing:* scrubbed glide.
  *Parked:* chapter end; §6.7 filings now travel to the parked
  position. *Scrolled-past:* parked forever; scrolling back reverses
  the scrub exactly (it is a pure function of scroll position).
- **Content merge.** The salver carries the received cards — the
  visit's actual record. Its motion moves content the visitor has
  already handled, never content they are trying to read; the reading
  column is never under the salver's path.
- **Failure fallback.** No JS → the salver sits parked at the
  chapter's end position with its stack complete. Loop stall → the
  shared watchdog freezes it wherever it is; a salver mid-table is a
  correct state, not a broken one.
- **Reduced-motion variant.** The salver is parked at its end position
  from first paint; filings (§6.7) appear on it without travel.
- **Performance budget & mobile variant.** One transform + one
  gradient-position shift per frame, on one element; the reflection
  is a background, not a second DOM node of content. Mobile: the
  slide is cut entirely below 768px — the salver sits centred under
  the hero stack (a small table has no crossing to make), reflection
  omitted.

**v2 — Choreography timeline** (spatial; s = first-chapter scroll progress 0→1):

| Beat | s | What happens |
|---|---|---|
| Rest | 0 | Salver at left, hero card aboard, reflection aligned |
| Glide | 0–0.85 | translateX lerps toward 38vw·s; reflection gradient streaks +12%·s |
| Approach | 0.85–1 | Lerp settles; salver decelerates into its park |
| Parked | 1 | Salver still; §6.7 filings target this position |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Left of table, hero card aboard | Centred, static |
| Crossing | Scrubbed glide, lerp 0.12 | n/a (cut) |
| Parked | End position; receives filings | Static; receives filings |
| Hover | None — furniture is not handled | n/a |
| Focus | The filed cards on it are not focusable duplicates (the originals live in their sections) | Same |
| Scrolled-past | Parked; scrub reverses on scroll-back | Static |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: 38vw crossing, reflection on.
768–1199px: 24vw crossing, reflection at 12% opacity. <768px: no
crossing, no reflection; salver centred, 320×96px.

**v2 — Edge cases & failure modes.** *Short first chapter* (less than
100vh of scroll): the mapping compresses; if the chapter offers under
40vh of travel the slide is disabled and the salver parks at centre —
a glide of 80px reads as a twitch, not a crossing. *Cards filed while
the salver is mid-crossing:* §6.7's filing path targets the salver's
*current* rendered position (read from the loop's state, not from
scroll math), so a card never flies to where the salver was.
*Resize mid-chapter:* the loop recomputes endpoints on resize;
the salver's progress fraction is preserved.

**v2 — Accessibility spec.** The salver and its stack are
`aria-hidden` duplicates: every card on it exists accessibly in its
own section, and the salver is the visual record only. Its motion is
scroll-scrubbed ambient furniture movement; it never carries text
that exists nowhere else. Under reduced motion it is static (§
above). No contrast surface: silver carries no type (§2, law 4).

**v2 — Tokens consumed.** `--silver`, `--card-deep`, `--loop-lerp`,
`--salver-travel`, `--ease-glance`.

---

### 6.4 Tissue lift reveal

- **What & why.** An engraved invitation arrived protected by a sheet of
  tissue, and the details were read by lifting it. Invitation-detail
  blocks in this theme — the particulars of an at-home, the programme of
  a reception — rest under a translucent tissue sheet that lifts from
  its top edge as the block enters, uncovering the text beneath. The
  reveal is the object's own covering being removed; nothing is wiped,
  faded or clipped by an invisible mask.
- **Structure.** `.invitation` block: the details content in normal flow,
  overlaid by `.tissue` — an absolutely positioned sheet, `--card` at
  82% opacity with a `--blush` tint at 6% and a printed tissue line (the
  occasion's name in Cormorant italic 19px at 55% `--ink`, the only
  thing on the tissue). The tissue's transform-origin is its top edge.
  The content beneath is fully in the DOM and fully styled; the tissue
  is an overlay with `pointer-events: none` at all times.
- **Motion spec.** Trigger: block 40% visible, once. The tissue lifts:
  rotateX 0→78° over 700ms `--ease-lift`, its opacity falling to 0 in
  the final 180ms as it comes edge-on and "is taken away"; a soft
  shadow under its free edge deepens to 14% at mid-lift and clears.
  At rest the tissue element is `visibility: hidden` — removed, not
  parked over the content. If the block enters already half-scrolled
  (fast scroll), the lift compresses to 350ms; if it enters at the
  viewport's top edge by anchor jump, there is no lift — the tissue
  is simply gone.
- **States.** *Covered:* tissue flat, its printed line legible, the
  particulars beneath dimmed to ~35% legibility through the sheet —
  a true state: the visitor can almost read, and knows what the
  sheet protects. *Lifting:* 700ms. *Uncovered:* permanent.
  *Hover/focus:* no interaction; the tissue never re-covers.
- **Content merge.** The tissue belongs to the invitation object; its
  printed line is the invitation's own title. The reveal uncovers the
  block's real particulars — date, place, programme — printed on the
  invitation itself, not on a layer beneath the page.
- **Failure fallback.** Without JS the tissue is never rendered over
  the content (server renders uncovered; JS inserts and arms the
  tissue only when it can lift it). Watchdog 1000ms from arming: an
  unlifted tissue is removed. Screen-reader and find-in-page users
  never meet the tissue at all (below).
- **Reduced-motion variant.** No tissue. The particulars stand printed,
  with the tissue's line as their heading — the line is content, so
  it survives the variant as a heading.
- **Performance budget & mobile variant.** One rotateX + opacity on
  one overlay; the content beneath does not repaint (the tissue is
  composited above it). Mobile: identical, lift angle 70° (a smaller
  sheet reads fully at a lower lift), duration 600ms.

**v2 — Choreography timeline** (t₀ = block 40% visible):

| Beat | Time | What happens |
|---|---|---|
| Covered rest | before t₀ | Tissue flat; printed line legible; particulars dimmed beneath |
| Lift | t₀ + 0–520ms | rotateX 0→78° `--ease-lift`; free-edge shadow deepens then clears |
| Removal | t₀ + 520–700ms | Tissue fades to 0 as it comes edge-on; `visibility: hidden` at 700ms |
| Read | t₀ + 700ms | Particulars at full contrast; the block is an open invitation |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Covered | Tissue flat, line legible | Same |
| Lifting | 700ms rotateX | 600ms, 70° |
| Uncovered | Permanent; tissue removed | Same |
| Hover | No change | n/a |
| Focus | If focus lands inside a covered block, the tissue lifts instantly (0ms) | Same |
| Scrolled-past | Uncovered | Same |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: full spec. 768–1199px: lift
650ms. <768px: lift 600ms at 70°, tissue line 17px.

**v2 — Edge cases & failure modes.** *Very tall invitation* (programme
longer than 60vh): the tissue covers only the first 420px — the head
of the invitation, where its title and date live; the tail was never
under tissue on a real card either. The lift triggers on the head.
*Two invitations entering together:* lifts stagger 150ms in reading
order. *The visitor scrolls the block away mid-lift:* the lift
completes off-screen (it is 700ms and one-shot); returning, the block
is uncovered. *Transparency unsupported (forced-colors mode):* the
tissue is not rendered at all (§ a11y).

**v2 — Accessibility spec.** The tissue is `aria-hidden` and the
content beneath is **never** `aria-hidden`, inert or
contrast-reduced for assistive technology — the dimming is a purely
visual overlay on a fully available text. Keyboard focus entering
the block removes the tissue instantly. In `forced-colors` mode the
tissue element is `display: none` (translucency is meaningless
there). At rest-covered, the visible dimmed text sits at ~3.4:1 —
acceptable only because the state is transient (≤ the time to scroll
40% of the block into view) and the same text is simultaneously
available at 14.37:1 to AT; a block that cannot lift (JS failed)
never shows the dimmed state at all.

**v2 — Tokens consumed.** `--card`, `--blush`, `--ink`,
`--ease-lift`, `--dur-tissue`, `--dur-fallback`.

### 6.5 Engraving light-catch

- **What & why.** Engraved lettering is incised; it reads by the light
  it catches. When a name is presented — the hostess's name in the
  hero, each card title on its turn — one specular sweep crosses its
  strokes, a gradient mask travelling left to right, and for 900ms the
  name is not merely printed but *engraved*. It is the theme's proof
  of material, performed on the very type the visitor is reading.
- **Structure.** Applied to `.engraved-name` elements: the name set
  twice in one grid cell — the base in `--ink`, and above it an
  identical copy in a `--gold`→white→`--gold` gradient clipped to the
  text (`background-clip: text`), its background-position animated.
  The overlay copy is `aria-hidden`, `pointer-events: none`. No
  wrapper, no canvas; the effect is one background-position tween on
  one element per name.
- **Motion spec.** Trigger: the name's presentation event — §6.1's
  tilt beat for the hero name, §6.2's edge-on instant for card
  titles, §6.10's stream arrival for calendar names. One sweep:
  background-position −150% → 150% over 900ms `--ease-glance`, the
  gradient band 28% of the text width. It fires **once per
  presentation** and never on hover, never on a loop — light crosses
  a name when it is announced, not when it is poked. A name
  re-presented (its card re-entering after an anchor jump) does not
  re-sweep.
- **States.** *Rest:* base ink only; the overlay sits parked at
  −150%, invisible. *Sweeping:* 900ms. *After:* parked at 150%,
  invisible; the name is ink again. There are no interactive states.
- **Content merge.** The sweep is on the name itself — the content is
  the surface. It reveals nothing and hides nothing: at the sweep's
  peak the name's contrast dips locally to ~7:1 (measured, §6.1) and
  returns; legibility is never the price of the polish.
- **Failure fallback.** If `background-clip: text` is unsupported,
  the overlay copy is not rendered (feature-detected at build of the
  class) and the name is simply engraved ink — the theme's rest
  state is complete without the effect.
- **Reduced-motion variant.** No sweep. Names are ink. (The variant
  loses an ornament, not a meaning.)
- **Performance budget & mobile variant.** One background-position
  animation per presented name, ≤2 concurrent; composited, no
  repaint of the text itself. Mobile: identical — the sweep is
  cheap; band widens to 36% on short names so it reads at small
  sizes.

**v2 — Choreography timeline** (t₀ = the name's presentation event):

| Beat | Time | What happens |
|---|---|---|
| Parked | before t₀ | Overlay at −150%; name is plain ink |
| Sweep | t₀ + 0–900ms | Gradient band crosses left→right `--ease-glance` |
| Parked | t₀ + 900ms | Overlay at 150%, invisible; name is ink; never repeats |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Ink name, overlay parked | Same |
| Sweeping | 900ms, once | Same |
| Hover | No re-sweep, ever | n/a |
| Focus | No sweep on focus; the name is not a control | Same |
| Scrolled-past | Ink; a name presented above the fold on load sweeps on load, not on scroll-back | Same |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: band 28%. 768–1199px: band
32%. <768px: band 36%, duration 800ms (shorter names, quicker light).

**v2 — Edge cases & failure modes.** *Very long names* (a house name
of 40+ characters): the sweep stays 900ms — the band travels faster,
which is correct; light does not slow for long names. *Name wrapping
to two lines:* the gradient is per-element, so the band crosses both
lines together, reading as one light — acceptable and intended.
*Names inside the turning card:* the sweep is timed to the edge-on
instant (§6.2) so it plays on the arriving face, never on the
departing one. *Dark mode:* the gradient's white point warms to
`#F3E3BC`; sweep unchanged.

**v2 — Accessibility spec.** Purely decorative and `aria-hidden`;
the accessible name is the base copy, present and unobscured at all
times. The effect never runs under reduced motion. Contrast floor
during the sweep ≈7:1 (the gradient is capped at 12% white over
ink), so even mid-sweep the name exceeds AA for its 24px+ sizes.

**v2 — Tokens consumed.** `--ink`, `--gold`, `--ease-glance`,
`--dur-glance`.

### 6.6 RSVP ledger counters

- **What & why.** At the head of the RSVP section sits the hostess's
  ledger line: "Accepts with pleasure 128 · Declines with regret 14".
  The figures count up when the section is presented, and — the point
  of the element — they increment live, by one, in the correct column,
  when the visitor replies (§6.15/§6.7). The counters are the section's
  real data rendered as a kept book; a count that decorates rather
  than records would be a lie in tabular figures.
- **Structure.** `.ledger` line in Libre Franklin 500 tabular: two
  labelled figures, each a `<data>` element whose value is the count.
  The counts are rendered server-side at their true values; JS rewinds
  them to a stated starting offset (accepts from true−24, declines
  from true−6, or from 0 if the true value is smaller) only when it
  can run the count, and only for figures the server marks
  `data-countable` (a real tally from the reply store — never a
  number invented for the page).
- **Motion spec.** Trigger: ledger 50% visible, once. Count-up: 1100ms
  `--ease-present`, figures stepping in whole integers at ~40ms
  intervals (a clerk's hand, not an odometer's blur — values are
  legible at every step). A visitor's own reply increments the
  relevant figure by 1 over 300ms with a single gold rule flashing
  beneath the figure (120ms) — the entry being made in the book.
  Changing one's reply (§6.15) moves the figure: one column −1, the
  other +1, each 300ms, in that order.
- **States.** *Unpresented:* true figures, static (the no-JS state).
  *Counting:* 1100ms. *At rest:* true figures. *Own reply pending:*
  figures unchanged until the reply is confirmed (§6.15) — the ledger
  records what has been received, not what is being written.
- **Content merge.** The figures are the section's data, printed where
  the data belongs: at the head of the replies. The visitor's own act
  enters the same book they have been reading — the merge is the
  meaning.
- **Failure fallback.** No JS → true figures, statically. A count-up
  interrupted (tab hidden) completes instantly on return — the book
  is never left mid-entry. If the reply store is unreachable, the
  ledger shows the last true figures and §6.15's form carries the
  failure; the ledger never estimates.
- **Reduced-motion variant.** True figures at first paint; a reply
  updates the figure instantly with the gold rule held for 600ms
  (emphasis by line, not by counting).
- **Performance budget & mobile variant.** One interval-free rAF
  count on two figures; negligible. Mobile: identical; the ledger
  line wraps to two lines with the rule between them.

**v2 — Choreography timeline** (t₀ = ledger 50% visible):

| Beat | Time | What happens |
|---|---|---|
| Rest | before t₀ | True figures (server-rendered) |
| Count | t₀ + 0–1100ms | Both figures count from their offsets, whole steps ~40ms |
| Kept | t₀ + 1100ms | Figures rest at truth; the book is open |
| Own entry | reply confirmed + 0–300ms | Relevant figure +1; gold rule flashes beneath it at +120ms for 120ms |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | True figures | Same |
| Counting | 1100ms whole-step count | Same |
| Hover | None — a ledger is read, not handled | n/a |
| Focus | Figures are text; the reply buttons (§6.15) take focus, not the ledger | Same |
| Scrolled-past | True figures; count never replays | Same |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: one line, centred. 768–1199px:
one line, left-aligned to the section measure. <768px: two lines,
accepts above declines, gold hairline between.

**v2 — Edge cases & failure modes.** *Zero replies yet:* the ledger
reads "Accepts with pleasure 0 · Declines with regret 0" — a new book,
stated plainly; the count-up is skipped (nothing to count) and the
first reply's +1 becomes the section's event. *Large tallies*
(>999): figures use tabular Franklin with a thin space thousands
separator ("1 240"); the count-up offset caps at 40 so a large book
still counts in 1100ms. *Reply changed twice:* each change moves the
figures in order; rapid changes queue and settle at truth — the
ledger's displayed value is always the store's value at rest.

**v2 — Accessibility spec.** The ledger is plain text in reading
order. During the count-up the figures are `aria-hidden` and a
visually-hidden static copy carries the true values, swapped at
completion — a screen reader is never read a rising number. A
visitor's own reply update is announced politely ("Your reply has
been entered: accepts with pleasure, 129 in all") via §6.15's live
region, once. Figures in `--ink` at 14.37:1; labels `--gold-deep`
5.39:1.

**v2 — Tokens consumed.** `--ink`, `--gold-deep`, `--gold`,
`--ease-present`, `--dur-count`.

---

### 6.7 Gold crest stamp

- **What & why.** To accept is to seal. Clicking "Accepts with
  pleasure" (§6.15) stamps a gold crest onto the corner of the
  visitor's own reply card — the crest arrives rotated, strikes, and
  settles — and the card then files itself, sliding across the table
  into the salver's stack. Reply, confirmation and filing are one
  physical gesture on the content card; there is no toast, no banner,
  no "success!" — the stamped, filed card *is* the confirmation, and
  it stays on the salver where the visitor can see it for the rest of
  the visit.
- **Structure.** The crest is an inline SVG (a shield-and-initial
  monogram drawn in `--gold` strokes, 44×44px) absolutely positioned
  at the reply card's top-right corner, initially unrendered. The
  filing is a FLIP: the card's clone travels to the salver stack's
  next slot (§6.3's current position) while the original collapses
  to a "filed" line in the form (§6.15) — the card in the salver is
  a miniature (120×68px) bearing the name and the crest.
- **Motion spec.** Trigger: the accept control's activation, after
  the reply validates (§6.15). Stamp: crest scales 1.6→1 and rotates
  −14°→−8° over 180ms `--ease-bow`, with a 60ms contact beat — the
  card's shadow pulses 10px→14px→10px as the seal strikes. Rest
  240ms (the visitor sees the crest on their card). Filing: the
  miniature travels 700ms `--ease-file` to the salver, shrinking to
  slot size, landing with a 120ms settle at the stack's next
  deterministic rotation. Declining stamps nothing: the reply card
  is simply placed, crestless, at the salver's edge — a regret is
  filed without a seal, which is the correct etiquette and the
  theme's small, exact sadness.
- **States.** *Unstamped:* no crest. *Striking:* 180ms. *Stamped:*
  crest at rest, −8°, permanent for the visit. *Filing:* 700ms.
  *Filed:* miniature on the salver; the form shows its filed line
  with a "Change one's reply" link that unstamps (crest fades 200ms)
  and returns the card. *Disabled:* while a reply is submitting, the
  accept control is disabled and crestless — a seal is never struck
  twice.
- **Content merge.** The crest is struck on the visitor's own reply —
  their name, their answer — and filed among the visit's received
  cards. It decorates nothing; it *executes* the reply.
- **Failure fallback.** If the reply submission fails, no stamp: the
  card stays in the form with §6.15's error line, unstamped — a seal
  on an unsent reply would be a false record. No-JS: the form posts
  classically and the returned page shows the card already filed on
  the salver with its crest printed (server-rendered state).
- **Reduced-motion variant.** The crest appears on the card at rest
  angle (no strike); the filing is instant — the miniature is simply
  on the salver, and the form's filed line states it.
- **Performance budget & mobile variant.** One SVG scale/rotate +
  one FLIP flight; trivial. Mobile: the filing flight shortens to
  the static salver's position (§6.3 mobile) — distance ~40vh,
  duration 560ms.

**v2 — Choreography timeline** (t₀ = reply confirmed by the store):

| Beat | Time | What happens |
|---|---|---|
| Strike | t₀ + 0–180ms | Crest scales 1.6→1, rotates to −8°, shadow pulse at contact |
| Regard | t₀ + 180–420ms | The stamped card rests; the visitor reads their sealed reply |
| Filing | t₀ + 420–1120ms | Miniature flies `--ease-file` to the salver's current slot |
| Filed | t₀ + 1120ms | Miniature settles on the stack; §6.6 ledger entry completes |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Unstamped | Crest absent | Same |
| Striking | 180ms strike + shadow pulse | Same |
| Stamped | Crest at −8°, permanent | Same |
| Filing | 700ms FLIP to salver | 560ms to static salver |
| Filed | Miniature on salver; filed line in form | Same |
| Disabled (submitting) | Accept control disabled, no crest | Same |

**v2 — Breakpoint behaviour.** ≥1200px: full spec. 768–1199px:
filing targets the narrowed salver's position (§6.3). <768px:
filing to the centred static salver; crest 38px.

**v2 — Edge cases & failure modes.** *Reply changed after filing:*
"Change one's reply" fades the crest (200ms), lifts the miniature
off the salver (fade 200ms — a filed card is withdrawn, not flown
back), restores the form; §6.6's figures move accordingly. *Salver
off-screen at filing time:* the flight still runs (it crosses the
visitor's view toward the salver's direction) — or, if the salver
is more than 2 viewports away, the miniature fades at the form and
appears on the salver; flying a card through three sections is
theatre, not filing. *Double activation:* the disabled state and a
submission token make a second strike impossible.

**v2 — Accessibility spec.** The stamp and flight are decorative
confirmations of a state change that is announced properly: the
form's polite live region states "Your reply has been received and
filed" (§6.15). The crest SVG is `aria-hidden` (the reply's state
is in the filed line's text: "Filed — accepts with pleasure"). The
miniature on the salver is `aria-hidden` (§6.3 — the accessible
original lives in the form's filed line). Focus stays on the filed
line's heading after submission; it is never sent chasing the card.

**v2 — Tokens consumed.** `--gold`, `--ink`, `--card`,
`--ease-bow`, `--ease-file`, `--dur-stamp`, `--dur-file`.

### 6.8 Plate-mark draw

- **What & why.** An engraved card is known by its plate-mark — the
  faint embossed rectangle the printing plate leaves around the
  lettering. In this theme the plate-mark is every card's border, and
  when a card is presented the mark *draws itself*: the plate is
  being pressed in front of the reader, and the card arrives
  manufactured, not rendered. The drawn line is not a frame added to
  the card; it is the card's own edge, the thing that makes the paper
  a card at all.
- **Structure.** Each card carries an SVG rect (or four CSS-border
  segments where SVG is impractical) inset 14px, stroke `--ink` at
  22%, width 1px, plus the second hairline at 17px/8% (§4). The draw
  uses stroke-dasharray on the rect's perimeter; the hairline does
  not draw — it fades in at the draw's end (120ms), the plate's
  second, lighter impression.
- **Motion spec.** Trigger: the card's presentation event (§6.2's
  turn — timed to complete at the edge-on instant; §6.1's settle;
  §6.14 card entry). Duration 900ms `--ease-present`, drawn clockwise
  from the top-left corner — the order a plate is inked. Perimeter
  speed is constant, so a full-width announcement card and a calling
  card draw in the same 900ms at different speeds: the press takes
  the same time for every impression.
- **States.** *Undrawn:* no border visible; the card is paper with
  lettering — legible, unfinished. *Drawing:* 900ms. *Drawn:*
  permanent; a presented card's mark never redraws. *Hover/focus:*
  no change — the mark is the card's manufacture, not its mood.
- **Content merge.** The mark bounds the card's content — text is
  set inside it by the layout law (§4). The draw literally traces
  the boundary of the content it will hold.
- **Failure fallback.** Without JS, marks are printed (server renders
  the full border; JS arms the dash pre-state only when it can draw
  it). Watchdog 1000ms: an undrawn mark on a presented card snaps to
  drawn — a card may not stand borderless because a script stalled.
- **Reduced-motion variant.** Marks are printed in full at first
  paint. (The reduced-motion page is a box of finished cards.)
- **Performance budget & mobile variant.** One dashoffset tween per
  card, ≤3 drawing concurrently (presentation staggers enforce it);
  no layout impact. Mobile: identical; inset tightens to 10px on
  cards under 300px wide so the mark keeps its proportion.

**v2 — Choreography timeline** (t₀ = presentation event):

| Beat | Time | What happens |
|---|---|---|
| Armed | before t₀ | Dash offset at full perimeter (JS-armed only) |
| Draw | t₀ + 0–900ms | Rect draws clockwise from top-left, constant 900ms |
| Second impression | t₀ + 900–1020ms | Hairline fades in at 8% |
| Finished | t₀ + 1020ms | The card is manufactured; mark static forever |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Undrawn | Borderless card, content legible | Same |
| Drawing | 900ms clockwise draw | Same |
| Drawn | Permanent | Same |
| Hover | No change | n/a |
| Focus | No change; focus ring (§6.13/§6.14) sits outside the mark | Same |
| Scrolled-past | Drawn | Same |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: inset 14px. 768–1199px:
inset 12px. <768px: inset 10px on narrow cards, 12px on full-width;
duration unchanged (900ms is the press's time, not the card's).

**v2 — Edge cases & failure modes.** *Card presented by anchor jump:*
mark drawn instantly (the destination must be finished). *Card
re-presented in a listing (§6.14) after filtering:* marks of
already-presented cards stay drawn; only genuinely new cards draw.
*SVG rect in a card that resizes (responsive reflow mid-draw):* the
rect is in the card's own coordinate box (`preserveAspectRatio=
none` on a viewBox-less rect via CSS inset borders fallback) — the
build uses four border segments whose dash lengths are recomputed
on resize; a resize mid-draw restarts the draw from the corner
rather than leaving a broken perimeter.

**v2 — Accessibility spec.** The mark is decoration (`aria-hidden`
SVG / CSS borders) carrying no information — a card's boundary is
also expressed by its grouping and heading. Contrast of the mark
(22% ink) is deliberately sub-text: it is an emboss, perceived by
its shadow side in print; nothing depends on seeing it. Focus
indicators never rely on the mark.

**v2 — Tokens consumed.** `--ink`, `--ease-present`, `--dur-draw`,
`--dur-fallback`.

### 6.9 Header stack thinning

- **What & why.** Progress, told in the theme's own objects. The
  header carries a miniature stack of calling cards — one for each
  presentation the page will make — and beside it the register's own
  wording: "Presentations 3 of 9". As each section is presented
  (§6.2), the stack's top miniature slides off and fades, and the
  figure advances. At the footer the stack is empty: the visit is
  complete, and the empty stack beside the full salver (§6.16) is
  the page's closing sentence.
- **Structure.** `.header-stack` in the pinned header (§6.13): a
  54×30px stack glyph built from the same card DOM pattern at
  miniature scale (backs only — miniatures carry no text), plus the
  figure line in Libre Franklin tabular 13px, `--gold-deep`. The
  count N is the number of `.announce-card` presentations on the
  page, counted from the DOM at build — never a hand-written number.
- **Motion spec.** Trigger: each §6.2 presentation completing. The
  top miniature slides 18px right and fades over 380ms
  `--ease-file`; the figure crossfades to n+1 (150ms) at the slide's
  midpoint. If two presentations complete within 380ms (fast
  scroll), the thinnings queue at 200ms intervals — the stack never
  drops two cards in one gesture. Scroll-back does not restack:
  presentations are permanent (§6.2), so progress never retreats.
- **States.** *Full:* n = 0 presented, stack complete. *Thinning:*
  per presentation. *Empty:* n = N; the stack glyph shows only its
  shadow line and the figure reads "Presentations 9 of 9 — the
  visit is complete" in the footer's vicinity (§6.16 states it in
  full; the header figure simply rests at N of N). *Rest:* between
  presentations, static.
- **Content merge.** The stack counts the page's own presentations —
  the figure is derived from the same events that turn the cards.
  It is not a scroll bar wearing a costume: a page scrolled without
  presenting (sections skipped by anchor) shows the truth, cards
  presented instantly at their destinations (§6.2) and counted.
- **Failure fallback.** No JS → the header shows the stack full and
  the figure as "Nine presentations" (the count as a statement of
  contents, not of progress) — or the stack is omitted and §6.13's
  navigation stands alone; it never shows a wrong progress. Observer
  failure falls back to scroll-position estimation only for the
  figure, and the stack glyph is removed rather than miscounted.
- **Reduced-motion variant.** Miniatures do not slide; the stack
  glyph's height steps down per presentation and the figure updates
  instantly.
- **Performance budget & mobile variant.** One 380ms transform on a
  54px glyph per presentation; nothing per frame. Mobile: the stack
  glyph is dropped below 768px (the header is small); the figure
  line remains — the count is the content, the glyph is its portrait.

**v2 — Choreography timeline** (t₀ = a §6.2 turn completing):

| Beat | Time | What happens |
|---|---|---|
| Slide | t₀ + 0–380ms | Top miniature slides 18px right, fading `--ease-file` |
| Recount | t₀ + 190ms | Figure crossfades to n+1 of N |
| Rest | t₀ + 380ms | Stack sits one card thinner; queue advances if pending |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Full | Stack complete, "0 of N" | Figure only |
| Thinning | 380ms slide + recount | Figure updates |
| Empty | Shadow line only, "N of N" | Figure "N of N" |
| Hover | None | n/a |
| Focus | The figure is text; the glyph is `aria-hidden` | Same |
| Scrolled-past | Count reflects presentations, not position | Same |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: glyph + figure. 768–1199px:
glyph at 44×24px + figure. <768px: figure only, 12px.

**v2 — Edge cases & failure modes.** *A page with one presentation:*
the stack is a single card; thinning empties it at the hero's
receipt — correct, and the header thereafter rests at "1 of 1".
*Presentations added dynamically (calendar stream, §6.10):* the
calendar's announcements are **not** counted — N counts section
presentations only, stated in §6.10 so the two systems never
double-count a card. *Print:* the header stack does not print; the
figure prints as the contents count on the register's first leaf.

**v2 — Accessibility spec.** The figure is real text, updated
without a live region (progress of reading is not an announcement);
its final state is reachable in the footer (§6.16) as a sentence.
The glyph is `aria-hidden`. Figure contrast: `--gold-deep` on the
header's `--card` ground, 5.39:1 at 13px semibold — the smallest
text permitted in the theme, and the reason the figure is never set
in `--gold` (3.20:1 would fail).

**v2 — Tokens consumed.** `--gold-deep`, `--ink`, `--card`,
`--ease-file`, `--dur-thin`.

---

### 6.10 The pinned engagement calendar

- **What & why.** The season's engagements are kept on one calendar, and
  the calendar does not leave the table while its announcements are
  read. The calendar card pins at the head of its chapter; beneath it,
  announcement cards stream past in strict precedence order (§1) —
  engagements by wedding date, then marriages, then at-homes, then
  arrivals — each announced by the calendar's own marker moving to its
  date as it passes. The pin is the theme's one act of insistence: the
  season is a whole, and the visitor reads it whole.
- **Structure.** `.calendar-card` (invitation size, 520px): a month
  grid in Libre Franklin tabular, engagement dates ringed in `--gold`
  hairlines, the current announcement's date filled `--gold` at 18%.
  Beneath, `.announcement-stream`: the chapter's announcement cards
  (the §6.14 card at reading size) in DOM order = precedence order =
  stream order. The pin is `position: sticky` within the chapter —
  no JS pinning, no spacer hacks; the chapter's height is the stream's.
- **Motion spec.** The pin itself has no entrance: the calendar is
  *placed* (a §6.8 plate-mark draw on entry, then stillness). As each
  announcement card crosses the chapter's reading line (45% viewport),
  the calendar's marker moves to that announcement's date: the gold
  fill fades from the old date (200ms) and into the new (200ms,
  overlapping by 60ms — one date is never unmarked mid-chapter), and
  the announcement's own card receives its §6.5 light-catch if it
  carries a name. Scroll-scrubbed nothing; the marker changes are
  events, fired by the observer, eased `--ease-present`. The stream
  cards enter with §6.2's grammar at card scale (plate-mark draw +
  a 12px rise, 400ms `--ease-present`, staggered 90ms in precedence
  order when several arrive together).
- **States.** *Placed:* calendar pinned, first date marked.
  *Streaming:* marker advancing as announcements pass. *Released:*
  the chapter's last announcement passes; the calendar unpins with
  the chapter's end and scrolls away — it does not chase the visitor
  into the next chapter. *Empty season:* the calendar shows the month
  unringed and the stream holds §6.17's not-at-home card.
- **Content merge.** The calendar is the stream's own index: every
  ringed date is an announcement below, every announcement below has
  its date ringed. The marker moving is the visitor's place being
  kept in the season they are reading — apparatus, not ornament.
- **Failure fallback.** No JS → the calendar is a static card at the
  chapter's head, all engagement dates ringed, the current-date fill
  omitted (there is no "current" without reading), and the stream
  reads beneath it in order. Sticky unsupported → the calendar simply
  heads the chapter unpinned; nothing else changes.
- **Reduced-motion variant.** No pin (the calendar heads the chapter
  and scrolls away — a pinned card is a motion commitment some
  visitors decline), no marker animation: the fill is present on the
  announcement nearest the reading line, changing instantly.
- **Performance budget & mobile variant.** Sticky is compositor-cheap;
  the marker is two 200ms opacity fades on small fills. Mobile
  (<768px): the calendar does not pin (a 520px card pinned on a phone
  is a wall); it heads the chapter at full width, its month grid
  compresses to a list of engagement dates in Franklin, and the
  stream follows — precedence intact, furniture reduced.

**v2 — Choreography timeline** (per announcement; t₀ = card crosses the reading line):

| Beat | Time | What happens |
|---|---|---|
| Unmark | t₀ + 0–200ms | Previous date's gold fill fades out |
| Mark | t₀ + 140–340ms | New date's fill fades in (60ms overlap) |
| Announce | t₀ + 0–400ms | The card itself completes its entry (rise + plate-mark) |
| Read | after t₀ + 400ms | Marker rests; the visitor reads the announcement under its date |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Placed | Pinned at chapter head, first date marked | Heads chapter, unpinned |
| Streaming | Marker advances per announcement | Marker advances (calendar scrolls away; marker state persists in its DOM) |
| Released | Unpins at chapter end | n/a |
| Hover | A ringed date brightens its hairline to full `--gold` (200ms) — the date is inspectable | n/a |
| Focus | Ringed dates are not links; the announcements' own links take focus in stream order | Same |
| Scrolled-past | Calendar gone with its chapter; stream cards presented | Same |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: pinned calendar 520px at the
chapter's left, stream in the right column (calendar and stream side
by side — the visitor reads the announcement beside its date).
768–1199px: calendar pinned above the stream (full width, month grid
compact), stream below. <768px: no pin, date-list calendar, stream
below.

**v2 — Edge cases & failure modes.** *Two announcements on one date:*
both ring the same date; the marker rests there for both, and the
date's fill deepens 18%→26% while the second is read — the calendar
admits the coincidence rather than choosing. *An announcement with
no date yet ("a date in September to be announced"):* it streams in
its precedence place with its card's date line set as words, and the
calendar marks nothing — the marker rests on the previous date; an
unfixed engagement is not pinned to a guessed day (§9.5). *Stream
longer than 9:* the chapter paginates to the next leaf of the
register (§7) — the calendar chapter never holds more than a
season's morning. *Month boundary mid-stream:* the calendar turns
its leaf — the month grid crossfades (300ms) to the next month as
the first announcement of that month is marked; the pin survives
the turn.

**v2 — Accessibility spec.** The calendar is a real `<table>` (or
grid with table semantics) whose ringed dates are also listed in
each announcement's own particulars — no information exists only as
a gold ring. The marker's movement is not announced. The stream's
reading order is DOM order = precedence order; the pinned visual
never reorders anything for AT. Date fills at 18% gold under ink
figures keep figures at ≥11:1.

**v2 — Tokens consumed.** `--card`, `--gold`, `--ink`,
`--ease-present`, `--dur-mark`, `--dur-draw`.

### 6.11 Card tilt-to-light (hover)

- **What & why.** A card in the hand is turned to the light to read its
  engraving. Hovering (or focusing) a presented card tilts it a few
  degrees toward the pointer, and the engraved lines brighten as the
  angle finds the light — the card's specular sheen tracks the tilt,
  so the visitor *feels* the incised lettering they are looking at.
  It is the theme's only hover physics, and it is deliberately small:
  a card is steadied and angled, never lifted, flipped or chased.
- **Structure.** Applied to presented `.card` and `.announce-card`
  elements. The tilt is a transform on the card driven by pointer
  position over it (rotateX/rotateY from centre offset); the sheen is
  the §6.5 gradient technique as a soft overlay (`::after`, radial
  gradient at 10% white, position following the tilt's light angle),
  `pointer-events: none`, clipped to the card. Both run in the shared
  rAF loop: pointer target vs current tilt, lerp 0.18.
- **Motion spec.** Tilt range: ±4° on each axis at the card's edges,
  proportional to pointer offset. Engage: the tilt follows within
  one frame of the loop (≤16ms lag at lerp 0.18, settling fully in
  ~300ms). Release (pointer leaves): spring return to flat over
  300ms `--ease-bow` with a ≤1° overshoot — the card settles back
  onto the table. The sheen's opacity peaks at 0.10 at full tilt and
  is 0 at flat: brightness is earned by angle, exactly as with a
  real engraving. Focus (keyboard) applies a fixed −3°/2° tilt and
  the sheen at 0.06 — the card angles itself to the reader who
  cannot point.
- **States.** *Flat:* rest, and the state of every unpresented card
  (they do not tilt — §6.2). *Tilting:* pointer over, loop-driven.
  *Returning:* 300ms spring. *Focused:* fixed courtesy tilt.
  *Scrolled-past:* flat; the loop stops writing to off-screen cards
  (observer-gated).
- **Content merge.** The tilt acts on the card the visitor is
  reading, and the sheen brightens that card's own engraved lines.
  Nothing is revealed or moved but the object itself; text remains
  fully legible at ±4° (the plate-mark and measure are sized with
  the tilt's perspective in reserve).
- **Failure fallback.** No JS or no fine pointer → cards are flat,
  which is their designed rest state; nothing is missing. Loop
  failure mid-tilt: the watchdog returns the card to flat (transform
  removed) — a card may not be left leaning.
- **Reduced-motion variant.** No tilt, no sheen. Hover/focus instead
  deepens the card's plate-mark from 22% to 34% ink (150ms) — the
  card is *attended to*, shown by its border, not its angle.
- **Performance budget & mobile variant.** Loop cost per tilted card
  ≤0.4ms/frame; only the hovered card tilts (one at a time by
  construction). Touch: no tilt — a finger covers the engraving it
  would angle; tap targets are the card's own controls. The sheen
  never runs on touch.

**v2 — Choreography timeline** (pointer over a presented card):

| Beat | Time | What happens |
|---|---|---|
| Engage | t₀ + 0–16ms | Loop begins lerping tilt toward the pointer's angle |
| Angle | t₀ + ~120ms | Tilt at working angle; sheen fading in with it |
| Track | continuous | Tilt and sheen follow the pointer, lerp 0.18 |
| Release | leave + 0–300ms | Spring return `--ease-bow`, ≤1° overshoot, sheen to 0 |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (flat) | No transform, no sheen | Same |
| Hover | Tilt ±4°, sheen ≤0.10 | n/a |
| Focus | Fixed −3°/2° courtesy tilt, sheen 0.06 | Same (external keyboard) |
| Active (press on a card control) | Tilt holds; the control's own state (§6.15) governs | Tilt n/a; control state governs |
| Scrolled-past | Flat; loop writes stop | Flat |
| Disabled | A card for a cancelled occasion (§6.14) does not tilt | Same |

**v2 — Breakpoint behaviour.** ≥1200px: ±4°. 768–1199px: ±3° (cards
sit closer; a smaller angle reads the same). <768px: tilt disabled
(touch-first), plate-mark deepening serves hover/focus instead.

**v2 — Edge cases & failure modes.** *Pointer crossing a card
corner at speed:* the lerp smooths the target; the card never snaps.
*Card near the viewport edge, perspective clipping:* tilt origin is
the card's centre and the table has no overflow constraints on cards,
so nothing clips. *Two cards overlapped on the salver:* miniatures
never tilt (§6.3) — only full cards in sections. *Tilt during the
card's §6.2 turn:* impossible — unpresented cards do not tilt, and
the turn disables tilt until presented.

**v2 — Accessibility spec.** The tilt is decorative and never the
only sign of focus: the standard focus ring (2px `--gold-deep`
outline, offset 3px, outside the plate-mark) accompanies the
courtesy tilt. Motion is pointer-driven and stops the instant the
pointer leaves; it is fully absent under reduced motion. Text
contrast is unchanged by the sheen (≤0.10 white overlay keeps ink
≥9:1 at peak tilt).

**v2 — Tokens consumed.** `--ink`, `--gold-deep`, `--ease-bow`,
`--loop-lerp`, `--tilt-max`, `--dur-return`.

### 6.12 Tea-table parallax & the tissue sheen

- **What & why.** The table has depth, and the theme's ambient life
  lives in it. Three strata move at three rates as the visitor
  scrolls: the tissue overlays slowest, the cards at reading speed,
  the salver's reflection fastest — so the table reads as a surface
  with objects *on* it, not a flat page with pictures. And over the
  current invitation, a tissue sheen idles: the translucent sheet's
  light breathing ±5% on a 9s cycle, the one ambient loop the theme
  permits itself. Together they are the room's air; separately each
  would be an effect.
- **Structure.** Parallax applies to decorative strata only:
  `.tissue` sheets (still covering un-presented invitations, §6.4)
  translate at 0.96× scroll; card *backgrounds* never move (cards
  are read — § below); the salver reflection (§6.3) streaks at the
  rate specced there. Implementation: the shared rAF loop writes a
  `--strata` custom property per stratum element from cached
  positions; transforms are translate3d only. The sheen is a CSS
  animation on the covering tissue's opacity (0.80↔0.85 effective),
  phase-offset per invitation by index so two tissues never breathe
  together.
- **Motion spec.** Parallax offsets are capped: tissue ±10px across
  its whole passage through the viewport; reflection per §6.3.
  Lerp 0.12 via the shared loop. The sheen: 9s ease-in-out infinite,
  opacity amplitude ±5% around the tissue's 82% base, pausing when
  the invitation is off-screen (observer toggles
  `animation-play-state`) and permanently once its tissue has lifted
  (§6.4 removes the element). The sheen never applies to text,
  cards' faces, or the calendar.
- **States.** *Rest:* strata aligned (the no-JS state — parallax is
  an offset applied by the loop, never a pre-state). *Scrolling:*
  offsets live. *Idle:* parallax settled; sheen breathing on the
  covered invitation nearest the reading line. *Scrolled-past:*
  offsets are a pure function of position; scroll-back restores
  them exactly.
- **Content merge.** The strata are the table's own materials —
  tissue on invitations, light on the salver. The cards' *contents*
  never parallax against their own faces; a paragraph that drifts
  inside its card would be a haunting, not a depth cue (§9.7).
- **Failure fallback.** No JS → no offsets; the table is flat and
  complete. Loop stall → offsets freeze where they are (a tissue
  6px adrift is invisible as an error). Sheen is CSS-only and its
  absence is undetectable.
- **Reduced-motion variant.** No parallax, no sheen. The table is
  still, as a table in a quiet room is still.
- **Performance budget & mobile variant.** Loop writes: ≤6 stratum
  elements per frame, transform-only; sheen is one composited
  opacity animation. Mobile: parallax halved (tissue ±5px) and the
  reflection stratum omitted with §6.3's slide; sheen kept (it is
  the cheaper life).

**v2 — Choreography timeline** (continuous; per element):

| Beat | Time | What happens |
|---|---|---|
| Enter | element enters viewport | Loop begins writing its offset; sheen resumes if it is the reading-line tissue |
| Passage | while visible | Tissue offset lerps toward ±10px by position; sheen breathes 9s |
| Exit | element leaves viewport | Writes stop; sheen pauses; offset holds |
| Lift | §6.4 fires | The tissue and its sheen are removed together |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Strata aligned | Same |
| Scrolling | Offsets live, lerp 0.12 | Offsets halved |
| Idle | Sheen breathing on one tissue | Same |
| Hover | No change (the sheen is weather, not response) | n/a |
| Focus | Sheen pauses on the focused invitation's tissue — reading stills the air | Same |
| Scrolled-past | Offsets positional; sheen paused off-screen | Same |
| Disabled / no-JS | Aligned, no sheen | Same |

**v2 — Breakpoint behaviour.** ≥1200px: full offsets. 768–1199px:
tissue ±7px. <768px: tissue ±5px, reflection stratum off, sheen on.

**v2 — Edge cases & failure modes.** *Many covered invitations at
once (a listing page):* sheen applies to at most one tissue (the
nearest the reading line); parallax caps at 6 written elements —
a table of twenty breathing tissues is a séance (§9.7). *Tissue
lifted mid-breath:* §6.4's removal wins; the animation is discarded
with the element. *Battery/low-power:* the loop's frame budget
(§14) cuts parallax before any content motion; the sheen is the
second cut.

**v2 — Accessibility spec.** Both effects are decorative, carry no
information, and are invisible to AT (tissues are already
`aria-hidden`, §6.4). Neither runs under reduced motion. The sheen's
amplitude (±5% on an 82% overlay) cannot produce luminance flashes;
its 9s period is far outside any photosensitivity range.

**v2 — Tokens consumed.** `--card`, `--blush`, `--loop-lerp`,
`--strata-max`, `--sheen-cycle`.

---

### 6.13 The visiting-list navigation (page family: navigation)

- **What & why.** One did not navigate a house; one was announced, and
  one's calls for the day were kept on a list. The navigation is the
  visiting list: the house's name engraved at the head, the day's
  calls set as a row of small card-tabs — each the name of a room of
  the site (The Season, Engagements, At-Homes, The Register) — and, at
  the list's right, the thinning stack of §6.9 keeping the visit's
  count. The current room's tab is the one turned face-up in gold-deep;
  the rest lie face-down in ink. It belongs at the top because a call
  begins with the list, and it never becomes a hamburger: on a small
  table the list folds to two columns, it does not hide.
- **Structure.** `<header class="visiting-list">`: the house name
  (Cormorant italic 28px), `<nav>` of card-tabs — each an `<a>` styled
  as a 150×44px card with plate-mark inset 6px — and the §6.9 stack +
  figure. The header is sticky (the list stays at hand during the
  call) with the table's `--card` ground at 96% and a hairline gold
  rule beneath; its height is 76px desktop, 64px mobile.
- **Motion spec.** Tab hover/focus: the tab lifts 2px and its
  plate-mark deepens (150ms `--ease-present`) — a card being touched,
  not turned. The current tab is marked on scroll by the section
  observer: its label crossfades ink→`--gold-deep` over 200ms as its
  section becomes current — ink changing, never a sliding pill. On
  navigation (§ page transition), the destination's first card turns
  (§6.2 grammar, 600ms) — the header itself does not animate.
- **States.** *Rest:* tabs flat, current in gold-deep. *Hover/focus:*
  lift + deepened mark. *Active:* the pressed tab settles back 1px
  (120ms). *Scrolled:* the header's shadow deepens 4% once the hero
  leaves — the list is on the table's edge now, and the light says so.
- **Content merge.** The tabs are the site's real rooms, named as the
  register names them; the stack counts the page's real presentations
  (§6.9). Nothing in the header is a control without a room behind it.
- **Failure fallback.** Plain header with text links; the stack figure
  degrades per §6.9. No JS is required for any navigation.
- **Reduced-motion variant.** No lift; hover/focus deepens the mark
  only. Current-tab changes are instant.
- **Performance budget & mobile variant.** Static but for 150ms
  transitions; sticky is composited. Mobile: the list wraps to two
  rows inside the 64px→(auto) header — tabs at 44px touch height,
  house name 24px; the §6.9 figure remains, its glyph dropped (§6.9).

**v2 — Choreography timeline** (hover, t₀ = pointer enter a tab):

| Beat | Time | What happens |
|---|---|---|
| Touch | t₀ + 0–150ms | Tab lifts 2px; plate-mark deepens 22%→34% |
| Rest | t₀ + 150ms | Tab held, ready |
| Release | leave + 0–200ms | Tab settles flat; mark relaxes |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Flat tabs; current in `--gold-deep` | Same, wrapped |
| Hover | Lift 2px + mark deepens | n/a |
| Focus | Same as hover + focus ring outside the mark | Same |
| Active | Settles 1px while pressed | Same |
| Scrolled-past (hero gone) | Header shadow +4% | Same |
| Disabled | A room not yet open is absent from the list, never greyed | Same |

**v2 — Breakpoint behaviour.** ≥1200px: one row, 76px. 768–1199px:
one row, tabs 132px wide, house name 24px. <768px: two-row wrap,
tabs ≥44px tall, header height auto (max 128px, beyond which the
list becomes a "Calls" disclosure in the same card style — never a
hamburger glyph).

**v2 — Edge cases & failure modes.** *More rooms than the row holds
(>6):* the list shows the six principal rooms; the remainder live in
the register index (§6.18) — a visiting list with eleven calls is an
itinerary, not a list. *Very long room names:* tabs size to content
up to 180px; beyond that the name is set at 12px Franklin — the name
is never truncated on its own card. *Sticky failure (overflow
ancestor):* the header scrolls away with the hero; navigation
remains reachable in the footer (§6.16) — the visit is never
stranded.

**v2 — Accessibility spec.** A real `<nav aria-label="The visiting
list">`; current room carries `aria-current="page"`, updated by the
scrollspy on section change only. Focus order = list order. Focus
ring: 2px `--gold-deep` at 3px offset. Tab text: ink 14.37:1;
current tab `--gold-deep` 5.39:1 at 13px semibold — permitted, and
the reason current is shown by colour *and* by the turned-card
position (the current tab's mark is double-ruled), never colour
alone.

**v2 — Tokens consumed.** `--card`, `--ink`, `--gold-deep`,
`--gold`, `--ease-present`, `--dur-thin`.

### 6.14 Announcement cards (page family: cards)

- **What & why.** The register's unit of content, outside the calendar
  stream: a card that carries one announcement whole — the name
  engraved, the occasion, the particulars, and its one permitted
  action (Read the announcement / Send a reply). Listing pages,
  related announcements and the season index are all laid from these
  cards on the table. A card in this theme is never a thumbnail with
  a headline pasted on: it is the announcement itself, at card size,
  and clicking through is done only when the announcement genuinely
  continues on its own leaf (§7).
- **Structure.** `<article class="announce-card-sm">` at 340×~230px:
  plate-mark (§6.8), kicker (occasion class, `--gold-deep`), the name
  (Cormorant italic 28px), occasion line, particulars in Franklin
  (date spelled per §3, place), and a footer line: the card's action
  as a Franklin link with a hairline gold rule. A debutante's card
  carries the blush wash (§2) at its head — the one card class
  permitted the wash. Cancelled occasions are printed as cards too:
  the name struck through with a single ink hairline and "Postponed"
  in the kicker — the register records the change, it does not delete
  the card.
- **Motion spec.** Entry: plate-mark draw (§6.8) + the card rises
  12px over 400ms `--ease-present`, staggered 90ms in precedence
  order within a table of cards. Hover: §6.11 tilt. The footer
  link's rule draws in left→right (180ms) on hover/focus. A
  postponed card does not rise and does not tilt — it lies flat, as
  a card one does not pick up.
- **States.** *Unpresented:* flat, mark undrawn, fully legible.
  *Presented:* mark drawn, at rest. *Hover/focus:* tilt + rule draw.
  *Postponed:* flat forever, struck name, no tilt. *Loading:* the
  unengraved skeleton (§5) — outline + hairline where the name will
  be, resolving by the mark drawing and the name printing at once
  (no fade) when content lands; a card still unengraved at 1200ms
  shows its name plainly (the standing rule: paper first).
- **Content merge.** Everything on the card is the announcement:
  name, occasion, date, place. The wash on a debutante's card is her
  card's stock, not a decoration applied to it. Remove all motion
  and the table of cards is the listing, complete.
- **Failure fallback.** Static cards, marks printed, names ink. The
  listing is server-rendered; JS adds rises and draws only.
- **Reduced-motion variant.** Cards printed and still; the footer
  rule is fully drawn at rest.
- **Performance budget & mobile variant.** Entry transforms on ≤9
  cards per table; tilt per §6.11. Mobile: cards stack one per row
  at full table width (the card face scales, its ratio held by
  padding, text never below the §3 floors); the rise is 8px.

**v2 — Choreography timeline** (t₀ = card 30% visible):

| Beat | Time | What happens |
|---|---|---|
| Rise | t₀ + 0–400ms | Card rises 12px `--ease-present` (90ms stagger by precedence) |
| Manufacture | t₀ + 0–900ms | Plate-mark draws (§6.8) concurrently |
| Rest | t₀ + 900ms | Card presented; tilt available |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Unpresented | Flat, legible, mark undrawn | Same |
| Entering | Rise + draw | Rise 8px + draw |
| Presented | At rest; tilt on hover | At rest |
| Hover | §6.11 tilt; footer rule draws | n/a |
| Focus | Courtesy tilt + rule + ring on the action | Same |
| Scrolled-past | Presented, still | Same |
| Disabled (postponed) | Flat, struck, no tilt, no rise | Same |

**v2 — Breakpoint behaviour.** ≥1200px: cards laid 3-across on the
table with 24px gaps, mixed with one wide card per table permitted
(a marriage announcement at invitation size). 768–1199px: 2-across.
<768px: 1-across, full width, name 26px floor.

**v2 — Edge cases & failure modes.** *Name too long for one line:*
names wrap to two lines and the card grows in height — cards in a
row keep their own heights (a table of real cards is not a grid of
identical boxes; rows align at their tops). *Missing particulars
(date to be announced):* the particulars line prints the words
("A date in September, to be announced") — never a blank, never a
guessed date (§9.5). *Image on a card:* the register does not
photograph its announcements; a card that needs an image uses an
engraved-style SVG ornament drawn per §6.8's grammar — or the build
is in the wrong theme.

**v2 — Accessibility spec.** One action per card, named by the
announcement ("Read the announcement of Miss Eleanor Vane's
engagement"); the whole card is not a link (the register's cards
are read, not leaned on). Name 28px italic ink at 14.37:1; kicker
`--gold-deep` 5.39:1. Postponed state is conveyed by the kicker's
word, never by the strikethrough alone.

**v2 — Tokens consumed.** `--card`, `--ink`, `--gold-deep`,
`--blush`, `--ease-present`, `--dur-draw`, `--tilt-max`.

### 6.15 The reply card (page family: forms / conversion)

- **What & why.** The conversion of this theme is a reply, and it is
  made on a card, in the correct form of words. The reply card offers
  the two period answers as the primary choice — "Accepts with
  pleasure" / "Declines with regret", set in the engraver's italic —
  then the particulars a hostess actually needs: the name(s) replying,
  the number of the party, and a line for a note. Submission is §6.7's
  stamp and filing. A reply form with a "Submit" button would be a
  clerk's error; here the button *is* the answer, and sending it is
  the etiquette performed.
- **Structure.** `<form class="reply-card">` at invitation size:
  plate-mark, the occasion's name as its head, the two answer
  controls as a radio pair styled as two half-cards side by side
  (each 248×64px, the chosen one gaining a gold hairline and its
  crest miniature), ruled-line fields (transparent ground, 1px ink
  bottom rule at 40%, Franklin 16px input text, labels above in
  kicker style), the party number as a stepper of printed figures
  (1–8, "and three more by arrangement" beyond), and the send
  control: a full-width card strip reading "Send this reply" in
  Franklin caps. Errors print beneath their field in the hostess's
  voice (§12) in `--blush-deep` at display size or `--gold-deep` —
  never in a red the palette does not contain.
- **Motion spec.** Choosing an answer: the chosen half-card's gold
  hairline draws (240ms, §6.8 grammar at small scale) and its crest
  fades in at rest angle (200ms); the other half dims its italic to
  70% — a decision, shown as one card being taken up and the other
  set down. Field focus: the rule thickens 1px→2px and warms to
  `--gold-deep` (150ms). Send: the control settles 1px (120ms), then
  §6.7's sequence runs on confirmation. Error: the field's rule
  turns `--blush-deep` and the message prints beneath in 45ms/word
  caption grammar — written, not popped.
- **States.** *Unanswered:* both half-cards equal; send disabled
  until an answer is chosen (a reply without an answer is an
  envelope without a card). *Answered:* one half taken up. *Sending:*
  controls disabled, the send strip reads "Sending…" in the clerk's
  hand — the theme permits itself exactly one ellipsis, here.
  *Filed:* the form is replaced by its filed line (§6.7) with the
  reply restated in full and "Change one's reply". *Error:* fields
  keep their values; the reply is never lost to a failed send.
- **Content merge.** The form is a reply card for this occasion; its
  head is the occasion's own name, its answers are the ledger's own
  words (§6.6), and its confirmation is filed onto the visit's
  salver. Nothing about it is a generic form in costume.
- **Failure fallback.** No JS → a classical form posting to the
  reply endpoint; the returned page shows the filed state
  server-rendered. A failed send preserves every field and states
  the failure in the hostess's voice with a "Send again" strip.
- **Reduced-motion variant.** No draws or fades: the chosen half
  shows its hairline and crest at once; errors print whole.
- **Performance budget & mobile variant.** Transitions only; no loop.
  Mobile: the two half-cards stack (each full width, 56px), fields
  full width, party stepper figures at 44px targets.

**v2 — Choreography timeline** (send, t₀ = send activated):

| Beat | Time | What happens |
|---|---|---|
| Settle | t₀ + 0–120ms | Send strip settles 1px; controls disable |
| Sending | t₀ + 120ms → store reply | Strip reads "Sending…"; the card waits, values intact |
| Confirmation | store replies | §6.7 stamp (180ms) → regard (240ms) → filing (700ms) |
| Filed | +1120ms from confirmation | Filed line in place; §6.6 ledger entry made; focus on the filed heading |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Unanswered | Both halves equal; send disabled | Stacked halves; send disabled |
| Answered | Chosen half hairlined + crest; other at 70% | Same |
| Focus | Field rule thickens/warms; half-cards take ring + hairline | Same |
| Sending | Disabled; "Sending…" | Same |
| Filed | Filed line + change link | Same |
| Error | Rule `--blush-deep`; message prints beneath; values kept | Same |
| Disabled | Send, until an answer is chosen | Same |

**v2 — Breakpoint behaviour.** ≥1200px: form at 520px in the
section's centre column. 768–1199px: 480px. <768px: full table
width; half-cards stacked; note field 3 rows.

**v2 — Edge cases & failure modes.** *Party larger than 8:* the
stepper's last figure is "8+" and the note field's label becomes
"Names of the party, if more than eight" — the hostess is told, not
surprised. *A reply for a postponed occasion (§6.14):* the form is
replaced by the postponement card and a line offering a reply when
the new date is announced; no reply is collected for a date that
does not exist. *Name field empty on send:* the error is the
hostess's own sentence (§12) and focus moves to the field — the
only field the theme will ever insist on, because a reply without
a name cannot be entered in the book. *Duplicate reply (same name,
same occasion):* the filed line offers the change path instead of
entering a second reply; the ledger never counts a guest twice.

**v2 — Accessibility spec.** Real `<form>`, real radio inputs
(visually styled, natively focusable, arrow-key operation intact),
labels bound to every field, errors linked by `aria-describedby`
and announced in the polite live region once. The send strip is a
`<button type="submit">`. Touch targets ≥44px (half-cards 64px,
stepper figures 44px). Error colour is never the only signal: the
message's words carry it. Contrast: input text ink 14.37:1; labels
`--gold-deep` 5.39:1; the disabled send strip is ink at 55% with
its reason stated in the unanswered state's line ("An answer is
required before the reply can be sent") — a disabled control that
explains itself.

**v2 — Tokens consumed.** `--card`, `--ink`, `--gold`,
`--gold-deep`, `--blush-deep`, `--ease-present`, `--dur-stamp`,
`--dur-file`.

---

### 6.16 The salver footer (page family: footer)

- **What & why.** A call ends as it began, at the salver. The footer is
  the table at the end of the hour: the salver — still, at rest —
  holding every card received during the visit (the hero's card, the
  visitor's own filed reply if one was made, miniatured in the order
  they were received), the visiting list repeated as plain links, and
  the visit's closing sentence set in the engraver's italic:
  "Nine presentations were made; the salver holds them all." The
  footer proves the visit happened, in the visit's own objects.
- **Structure.** `.footer-table` on `--card-deep`: the still salver
  (a static instance of §6.3's object, reflection omitted — the hour
  is over and the light has gone), its stack of miniatures in receipt
  order, the closing sentence (with the true count, DOM-derived), the
  house's particulars in Franklin (address of the house, the
  hostess's at-home day — "At home on Thursdays" — the register's
  colophon line), and §6.13's rooms as a plain list.
- **Motion spec.** One motion only: as the footer enters, the salver's
  top miniature — the most recently received card — settles the final
  4px onto the stack (300ms `--ease-bow`), the visit's last physical
  act. Nothing else in the footer moves, ever. If no card was filed
  by the visitor, the hero's miniature performs the settle.
- **States.** *Approaching:* salver still, stack complete but for the
  last 4px. *Closed:* settled; the sentence readable. There are no
  interactive states beyond the footer's links.
- **Content merge.** The miniatures are the visit's real receipts;
  the count in the sentence is the same N the header kept (§6.9).
  A footer that showed cards the visitor never received would be a
  servant's invention (§9.10).
- **Failure fallback.** Static footer; the sentence prints the count
  from the server where known, or omits the number ("The salver
  holds them all") rather than guessing.
- **Reduced-motion variant.** The settle is omitted; the stack is
  complete at first paint.
- **Performance budget & mobile variant.** One 300ms transform, once.
  Mobile: the salver scales to 300px wide above the sentence; the
  particulars stack.

**v2 — Choreography timeline** (t₀ = footer 30% visible):

| Beat | Time | What happens |
|---|---|---|
| Approach | before t₀ | Salver still; top miniature 4px proud |
| Settle | t₀ + 0–300ms | Top miniature settles onto the stack `--ease-bow` |
| Closed | t₀ + 300ms | The visit is complete; the sentence is read |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Approaching | Stack one card proud | Same |
| Closed | Settled; links live | Same |
| Hover | Links take §6.13's treatment; the salver does not respond | n/a |
| Focus | Standard rings on links | Same |
| Scrolled-past | n/a — the footer is the end | n/a |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: salver left, sentence and
particulars right in two columns. 768–1199px: salver above, columns
below. <768px: single column, salver 300px.

**v2 — Edge cases & failure modes.** *A visit with no reply filed:*
the salver holds the hero's card alone and the sentence reads for
the presentations only — the footer does not pretend a reply exists.
*Very long visits (register leaves, §7):* the footer salver holds
the *leaf's* receipts; the closing sentence counts the leaf and
names the whole ("Leaf two of the season's register; …"). *Print:*
the footer prints as the register leaf's colophon — sentence,
particulars, no salver image.

**v2 — Accessibility spec.** The salver stack is `aria-hidden` (its
cards' accessible originals are in their sections and in §6.15's
filed line); the closing sentence is real text carrying the count.
Footer links are a labelled `<nav aria-label="The house">`. The
settle is decorative.

**v2 — Tokens consumed.** `--card-deep`, `--silver`, `--ink`,
`--ease-bow`, `--dur-settle`.

### 6.17 Not at home (page family: empty states & 404)

- **What & why.** The period's perfect empty state already exists: a
  caller who came on the wrong day was told the mistress was "not at
  home" — a courteous fiction that covered absence without admitting
  disorder. Every empty state in this theme is that card: the season
  with no engagements yet, the register leaf with no announcements,
  and the 404 — a card left on the salver reading "Not at home" in
  the engraver's italic, the occasion's particulars beneath, and the
  way back to the rooms that *are* receiving. An error page that
  breaks character to say "404!!" has forgotten whose house it is in.
- **Structure.** `.not-at-home`: a single invitation card centred on
  the bare table (the table around it is genuinely bare — §4's
  designed emptiness), plate-mark printed (not drawn — nobody is
  being presented), the words "Not at home" (Cormorant italic 40px),
  one Franklin sentence of particulars ("The engagement you seek is
  not in this season's register." / for 404: "No card has been left
  under this name."), and the visiting list as the way onward. For
  empty listings the card sits at the head of the empty table with
  the season's other rooms offered beneath.
- **Motion spec.** None on arrival — an empty room is still. The one
  permitted motion: if the state resolves while the visitor waits
  (a live register gaining its first announcement), the not-at-home
  card is *taken away* — lifted 12px and faded over 300ms
  `--ease-file` — and the first announcement card is presented in
  its place (§6.14 grammar). Absence leaves politely; it does not
  pop.
- **States.** *At rest:* the card, the sentence, the way onward.
  *Resolving:* the 300ms removal above. There is no loading spinner
  in this theme; a pending state is the bare table with the card's
  outline (the unengraved skeleton) and the sentence "The register
  is being brought in" — stated, not spun.
- **Content merge.** The card is the message: the absence is
  announced in the register's own form, on the register's own card.
  The onward links are the house's real rooms.
- **Failure fallback.** The card is server-rendered for 404 and
  empty states; no JS is involved in its existence.
- **Reduced-motion variant.** Identical (the state has no motion to
  reduce); the resolving removal becomes an instant exchange.
- **Performance budget & mobile variant.** Static. Mobile: the card
  is full table width; "Not at home" at 32px.

**v2 — Choreography timeline** (resolving case only; t₀ = first content arrives):

| Beat | Time | What happens |
|---|---|---|
| Rest | before t₀ | The not-at-home card on the bare table |
| Removal | t₀ + 0–300ms | Card lifts 12px, fades `--ease-file` |
| Presentation | t₀ + 300–1200ms | First announcement presented (§6.14: rise + draw) |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Card centred, still | Full-width card |
| Pending | Outline card + stated sentence | Same |
| Resolving | 300ms removal, then presentation | Same |
| Hover | Onward links only; the card does not tilt | n/a |
| Focus | Onward links take rings in list order | Same |
| Scrolled-past | n/a | n/a |
| Disabled | n/a | n/a |

**v2 — Breakpoint behaviour.** ≥1200px: card 520px centred, table
bare for a full viewport. 768–1199px: card 460px. <768px: card full
width at 20px margins.

**v2 — Edge cases & failure modes.** *A search with no results
(§6.18):* the card's sentence names the search ("No card has been
left under the name 'Ashworth' this season") — the fiction stays
specific, never generic. *An empty RSVP ledger (§6.6 at zero):* no
card — the ledger simply reads its zeroes; the not-at-home card is
for absent *content*, not for small numbers. *A genuinely broken
page (500):* the card's sentence is the hostess's apology (§12) and
the onward list is the house's front door only — the theme does not
dress a failure as a fiction beyond one courteous card.

**v2 — Accessibility spec.** For 404 the card's heading is the
page's `<h1>` ("Not at home") with the particulars sentence naming
the situation plainly enough for AT ("No card has been left under
this name — the page you sought is not in this register"). Status
is never carried by the fiction alone: the HTTP status is real, and
empty listings expose their state in the heading hierarchy.

**v2 — Tokens consumed.** `--card`, `--card-deep`, `--ink`,
`--ease-file`, `--dur-file`.

### 6.18 The season index (page family: search & index)

- **What & why.** A register is consulted by name. The index leaf is
  the season's book: every name announced this season, in alphabetical
  order, each entry a line — name in the engraver's italic, the
  occasions it was announced for in Franklin, the leaf where each
  announcement stands — joined by the dotted leader rule of every
  printed index. A search field at its head, styled as a card, finds
  a name by its first letters; the index *turns to* the letter rather
  than filtering to a fragment, because a book is not a database
  view: the visitor sees the name among its neighbours, as in any
  register they have ever used.
- **Structure.** `.index-leaf`: the search card (one ruled field,
  §6.15 grammar, label "Find a name in the register"), the alphabet
  as a row of letter-tabs (letters with no names are printed at 40%
  — the book admits its gaps), and the entries in alphabetical
  groups under engraved letter heads. Each entry line: name,
  leader dots (a dotted bottom border on a flexible span), occasion
  + leaf reference as a link to the announcement (§6.14's card on
  its leaf).
- **Motion spec.** Typing in the search: after 2+ letters and a
  250ms pause, the leaf scrolls to the matching letter group
  (smooth, 500ms `--ease-present`, or instant under reduced motion)
  and the first matching name receives a §6.5 light-catch — the
  name is *found*, and the light says so. Selecting a letter-tab
  does the same without the catch. No filtering, no result counts,
  no "no results" panel: a name with no entry scrolls to where it
  would stand and §6.17's sentence appears as a line in the index
  ("No card has been left under this name this season") — the book
  shows the empty place.
- **States.** *Rest:* the full index, alphabetical. *Seeking:*
  field focused, rule warmed (§6.15). *Found:* scrolled, the name
  lit once. *Not found:* scrolled to the empty place, the sentence
  printed there. *Returning:* clearing the field leaves the leaf
  where it lies — a book does not snap shut.
- **Content merge.** The index is generated from the season's actual
  announcements — every entry resolves to a real card on a real
  leaf; an entry pointing nowhere is a gate failure (§10).
- **Failure fallback.** No JS → the full index stands with its
  letter heads as anchor links (the tabs are `<a href="#letter-M">`
  regardless); the search field degrades to a server query that
  returns the leaf at the letter. Nothing about the book requires
  the light-catch.
- **Reduced-motion variant.** Jumps are instant; the found name is
  marked by a gold hairline beneath it held for 1200ms instead of
  the sweep.
- **Performance budget & mobile variant.** One smooth scroll + one
  sweep per search; the index is server-rendered whole (a season is
  ≤ 300 names — beyond that, the register is published in volumes,
  §7). Mobile: letter-tabs wrap to two rows at 40px targets; leader
  dots shorten to a minimum 18px before the occasion wraps under
  the name.

**v2 — Choreography timeline** (t₀ = search pause at 250ms with a match):

| Beat | Time | What happens |
|---|---|---|
| Turn | t₀ + 0–500ms | Leaf scrolls to the letter group `--ease-present` |
| Arrival | t₀ + 500ms | The matched name rests in view |
| Light | t₀ + 500–1400ms | §6.5 sweep crosses the found name, once |

**v2 — State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Full index, alphabetical | Same |
| Seeking | Field rule warmed; tabs live | Same |
| Found | Scrolled; name swept once | Scrolled; hairline under reduced motion only |
| Not found | Scrolled to the empty place; sentence printed there | Same |
| Hover | Entry links: leader dots ink to full weight (150ms) | n/a |
| Focus | Entries are links in alphabetical order; the found name is not force-focused | Same |
| Scrolled-past | The leaf lies where it was left | Same |
| Disabled | Letters with no names are text at 40%, never links | Same |

**v2 — Breakpoint behaviour.** ≥1200px: index in two columns
(groups flow), leader dots full. 768–1199px: one column, dots full.
<768px: one column, dots ≥18px, occasion wraps beneath the name,
letter-tabs 40px.

**v2 — Edge cases & failure modes.** *Duplicate names* (two Miss
Vanes): entries are distinguished by their occasions in the entry
line itself — the index never merges two people into one line.
*Names beginning with particles or titles* ("de la Mare", "Lady
Mary"): filed under the substantive name (M, L) with a cross-entry
at the particle ("de la Mare — see Mare") printed as an entry with
no occasion: the book's own convention, stated in the leaf's head
note. *A name sought that exists only in a past season:* the empty
place sentence gains "— in this season"; past seasons are separate
volumes (§7), linked from the leaf's foot.

**v2 — Accessibility spec.** The index is a list of links in
alphabetical order with letter-group headings — fully navigable by
heading and link lists. The search field has a real `<label>`; the
"found" light is decorative and the found state is also expressed
by the scroll position and, for AT, by an `aria-describedby` note
on the field naming the match ("Eleanor Vane — two announcements").
Leader dots are CSS, invisible to AT. Empty letters at 40% are
text, announced as letters with no entries only if focused — they
are not links.

**v2 — Tokens consumed.** `--ink`, `--gold-deep`, `--gold`,
`--ease-present`, `--dur-glance`, `--ease-file`.

---

## 7. Page application map

- **Home — the call.** The full visit as specced: §6.1 hero, announced
  sections, §6.10 calendar chapter, §6.15 reply, §6.16 footer. One
  page, one call, ≤9 presentations.
- **Listing — a leaf of the register.** A table of §6.14 cards in
  precedence order under one §6.2 announcement card naming the leaf
  ("Engagements of the Season — Leaf Two"). Pagination is by leaves,
  named as leaves, with the previous and next leaf's first name
  printed on the turning link — a visitor turns to a name, not a
  number. Filters, where the register is large, are by occasion class
  only, styled as the index's letter-tabs (§6.18).
- **Detail — the announcement's own leaf.** One announcement at
  invitation size: its card presented on entry (§6.2 at full width),
  its particulars under §6.4's tissue, its reply card (§6.15) as the
  leaf's second half, and beneath, "Other announcements of the
  season" as §6.14 cards — never more than three; a register does not
  shout recommendations.
- **About — the house.** The hostess's own card, presented first by
  precedence (§1): her name receives the page's only §6.5 sweep on
  load; the house's history is set as announcements of past seasons,
  each a §6.14 card lying flat (the past is presented already).
- **Contact — leaving a card.** The contact page *is* §6.15's grammar
  generalised: a card on which the visitor leaves their name, their
  direction, and a line — sent with the filing gesture (§6.7) to the
  house's salver, confirmed by the filed line. No map, no office
  hours grid; the house's at-home day is stated in the particulars
  ("At home on Thursdays, between three and six").
- **Search/index — the season's book.** §6.18 whole. Past seasons are
  separate volumes, each its own index leaf, linked as volumes.
- **404 / empty — not at home.** §6.17 whole.

## 8. Worked examples

### 8.1 The hero — a wedding venue's first call

*Setting.* "Hartfield House" — a venue whose season opens. The hero
table (§4): on `--card-deep`, left, the stack of three cards (backs of
the next announcements: the June engagement, the Thursday at-home, the
arrival of the new chef — in precedence order); right, the empty
salver. The header (§6.13) shows the house name, four rooms, and the
stack at "Presentations 0 of 7".

*Timeline.* Fonts ready at ~220ms (under the 300ms cap). At t+400ms
the top card lifts 24px; at 660ms it tilts −14° and the light crosses
"Mr. & Mrs. Ashworth" — the house's own announcement, first by
precedence; at 1040ms it travels 40vw to the salver, turning mid-way;
at 1680ms it settles at −1.5°, details up: the headline "The Season at
Hartfield opens on the fourteenth of June", the standfirst in
Franklin, and the reply strip. The visitor has been *handed* the
season. Beneath the table, the first section's announcement card
waits name-up: "Engagements".

*What the builder checks.* The details face was in the DOM from first
paint; with JS off, the same card sits on the salver details-up and
the hero is complete. The stack's second card is a real announcement,
reachable later in its section — not a prop.

### 8.2 Mid-page — the calendar chapter

*Setting.* The same page, third chapter. The calendar card (June,
520px) is placed at the chapter's head; its plate-mark draws in
900ms as it enters. Ringed dates: 14, 21, 28. Beneath/beside it the
stream: Miss Eleanor Vane's engagement (wedding 14 June), the
Ashworths' marriage (21 June), the Thursday at-home (28 June) — in
that order, because precedence says engagements before marriages
before at-homes, whatever the dates.

*Timeline.* The visitor scrolls; at ≥1200px the calendar pins at the
chapter's left while the first announcement crosses the reading line:
its date (14) fills gold over 200ms. The engagement card completes
its rise and its name takes the light-catch. Two cards later the
at-home crosses: the fill leaves 21 (fading from t₀) and settles on
28 by t₀+340ms. The chapter ends; the calendar unpins and is gone —
the next chapter's announcement card turns as it enters, and the
header stack thins to "Presentations 4 of 7".

*What the builder checks.* DOM order = stream order = precedence
order (engagement, marriage, at-home), even though the at-home's
date is the latest; the calendar's marker never marked a date whose
announcement the visitor had not reached.

### 8.3 Conversion — a reply to the at-home

*Setting.* The at-home's own leaf (§7 detail). The tissue over the
particulars lifted as the visitor entered (700ms, §6.4): "Thursdays,
between three and six; music from four." Below, the reply card:
its head is the occasion's name, "The Thursday At-Home", and beneath
it the two half-cards: *Accepts with pleasure* / *Declines with
regret*.

*Timeline.* The visitor takes up "Accepts with pleasure": its gold
hairline draws in 240ms, the regret half dims to 70%. Name field:
"Miss Clara Hartley" — the rule warms on focus; party: two. She
sends. The strip settles; "Sending…"; the store confirms; the crest
strikes her card's corner (180ms, shadow pulse); a beat of regard;
the miniature flies 700ms to the salver at the foot of the leaf —
wait: the salver lives in the hero and footer; on a detail leaf the
filing target is the leaf's own salver strip at its foot (the
§6.16 object at leaf scale), and the miniature lands as its second
card. The filed line stands in the form's place: "Filed — Miss Clara
Hartley accepts with pleasure, a party of two", with "Change one's
reply". In the header of the *next* page she visits, nothing changes
(the ledger is per-occasion); on this leaf, the occasion's ledger
line (§6.6 pattern, at the reply card's head on return) has gained
one accept.

*What the builder checks.* With JS off, the same reply posts
classically and the returned leaf shows the filed line and the
miniature, server-rendered. A failed send leaves every field as she
left it, with the hostess's sentence beneath the strip.

## 9. Anti-slop — what makes THIS theme look cheap

1. **RSVP buttons renamed by a developer.** "RSVP Now", "Count me
   in!", "Submit" — the theme's whole credibility is in the form of
   words. Cure: the strings are fixed (§3, §12); a build that changes
   them has left the theme.
2. **A card that turns to reveal a teaser.** Details face carrying
   "Read more…" and three dots instead of the announcement. Cure:
   both faces carry complete content (§1 corollary); the turn
   presents, it never gates.
3. **Precedence violated for layout convenience.** Announcements
   reordered so the grid looks balanced, or the hostess's card placed
   third because the hero needed a photograph. Cure: DOM order is
   precedence order (§10, blocking); balance is achieved by card
   sizing, never by re-ranking people.
4. **Gold and blush on the same card.** The confectionery box. Cure:
   §2 law 5 — one accent per card; the debutante wash excludes gold
   rules on that card.
5. **Invented dates and tallies.** A calendar ringing dates with no
   announcements, a ledger counting replies nobody made, a
   "date to be announced" quietly given a day. Cure: every figure
   traces to the DOM or the store (§6.6, §6.10); the gate audits it.
6. **Filling the bare table.** Stock flourishes, scattered petals,
   a repeating damask pattern itching to cover the `--card-deep`.
   Cure: the bare table is a designed state (§4); emptiness is the
   polish.
7. **Parallax on the lettering.** Text drifting inside its card at a
   different rate from the card. Cure: strata move materials only
   (§6.12); a card and its words are one object.
8. **Blur-to-sharp reveals "for elegance".** A name resolving from a
   smudge reads as a printing error in an engraving theme. Cure:
   refused in §5; names are presented whole or not at all.
9. **Dark mode by inversion.** Cards turned black with white italic.
   Cure: candlelight (§2) — the room darkens, the paper does not.
10. **The salver as clip-art.** A stock silver tray image, cards
    "on" it that were never received, a reflection that ignores the
    cards. Cure: the salver is built from the theme's gradient and
    holds only receipts (§6.3, §6.16); if it cannot be built so, the
    build omits it and keeps the stack.

## 10. Quality gate

**Blocking — the build may not ship with any of these failed:**

1. **Precedence audit.** DOM order of every announcement sequence
   equals the precedence order of §1 (hostess → engagements by
   wedding date → marriages → at-homes → arrivals). Checked in
   source, not by eye.
2. **Two-face truth.** Every turning card's both faces contain
   complete, real content; no face is a teaser, a spinner or a
   "read more".
3. **The form of words.** "Accepts with pleasure" / "Declines with
   regret" appear verbatim wherever replies are offered; no
   exclamation mark exists anywhere in the theme's UI copy.
4. **Figure truth.** Ledger counts, "presentations n of N", calendar
   rings and the footer's closing count each trace to DOM content or
   the reply store. One invented figure fails the build.
5. **JS-off visit.** With JavaScript disabled: the hero card is
   received on the salver, all cards details-up, all particulars
   uncovered, all marks printed, the reply form posts and returns a
   filed page. The visit is complete.
6. **No stranded presentation.** Every armed pre-state settles within
   its watchdog (1000ms) in a throttled-CPU pass; no card stands
   unpresented, covered or undrawn at any scroll position.
7. **Contrast floors.** Body text only in `--ink` on `--card`
   (14.37:1) or `--card-deep` (12.48:1); `--gold` never below 24px;
   small gold-toned text only in `--gold-deep` (5.39:1); blush never
   text.
8. **Reduced-motion visit.** With `prefers-reduced-motion`: no turns,
   lifts, tilts, parallax, sheen or pins; every card details-up; the
   visit loses no content, including card name-faces (as kickers,
   §6.2).

**Standard — required unless a noted exception applies:**

9. One pin per page (§6.10); one ambient loop (§6.12); ≤9
   presentations per leaf.
10. The light-catch fires once per name, on presentation only —
    never on hover, never looping (§6.5).
11. Tilt ≤4°, presented cards only, absent on touch (§6.11).
12. The salver holds only cards actually received during the visit
    (§6.3, §6.16).
13. Dates in display contexts spelled or fully figured per §3;
    no locale-ambiguous date strings anywhere.
14. Every card's plate-mark inset and ratio held at all breakpoints
    (§4, §6.8).

---

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components the theme refuses are listed with their in-world
replacement — a refusal without a replacement is a gap, and this
theme has none.

| Component | Treatment in this theme |
|---|---|
| Primary button | A card strip: `--card` ground, plate-mark inset 6px, Franklin caps label ("Send this reply", "Leave your card"). Settles 1px on press (120ms). Never a filled pill. |
| Secondary button | A hairline-ruled Franklin link with the §6.14 rule-draw on hover. |
| Answer choice (radio pair) | §6.15's two half-cards; native radios beneath the styling. |
| Text input | Ruled-line field (§6.15): transparent ground, ink bottom rule, label above in kicker style. |
| Textarea | The reply card's note field: three ruled lines, line-height matched to the rules (26px) so writing sits on the lines. |
| Stepper (party number) | Printed figures 1–8(+), the chosen figure in `--gold-deep` with a hairline beneath; 44px targets. |
| Select / dropdown | **Refused.** A register does not drop down. Replacement: a short list of card-tabs (§6.13 grammar) or, for long lists, the index leaf (§6.18). |
| Tabs | Card-tabs (§6.13): small cards, the current turned to `--gold-deep`. |
| Accordion | **Refused** — content is never folded away in a house that presents things. Replacement: the announcement continues on its own leaf (§7 detail), announced by its card. |
| Modal / dialog | **Refused.** Nothing interrupts a call. Replacement: the matter gets its own card on the table (a postponement, a correction) presented in precedence position. |
| Toast / snackbar | **Refused.** Confirmation is a filed card on the salver (§6.7), which stays where it was put. |
| Tooltip | **Refused.** If a thing needs explaining, the explanation is printed on its card in Franklin. |
| Badge / chip | **Refused.** Status is stated in the kicker's words ("Postponed", "By invitation") — never a coloured dot or pill. |
| Alert / notice | A card, presented in place: plate-mark, the notice in the hostess's voice (§12), no icon, no colour the palette lacks. Errors in forms per §6.15. |
| Pagination | By leaves (§7): "Leaf Two" links carrying the first name of each leaf. Numbered pagination is refused — one does not number a hostess's callers. |
| Breadcrumbs | **Refused.** The visiting list (§6.13) and the index (§6.18) are the house's whole geography; a caller is never lost enough to need crumbs. |
| Progress indicator | The thinning stack (§6.9). A progress bar is refused (§5). |
| Skeleton loader | The unengraved card (§5, §6.14): outline, plate-mark, hairline for the name. No shimmer. |
| Table (data) | The ledger table: Franklin tabular, hairline rules between rows, figures right-aligned, no zebra striping (a ledger is ruled, not striped). Used for tallies and the calendar's date list on mobile. |
| Calendar | §6.10 whole. |
| Search | §6.18 whole — the index leaf, turning to letters. |
| Image treatment | Engraved-style SVG ornament only, drawn per §6.8's grammar; photographs are refused (§6.14) — the register announces, it does not illustrate. |
| Divider | A hairline gold rule, or the plate-mark of the next card. Never a gradient fade rule. |
| Footer | §6.16 whole. |
| 404 / empty | §6.17 whole. |

## 12. Content & copywriting voice

Two voices, cast like the type (§3). **The engraver's voice**
(Cormorant italic) speaks for persons and the house: names, occasions,
the form of words, the closing sentence. **The clerk's voice**
(Libre Franklin) records: announcements' particulars, ledger labels,
errors, instructions. A sentence is cast by who is speaking, and the
two never swap.

**Headline style.** A statement of occasion, never a pitch.
✓ "The Season at Hartfield opens on the fourteenth of June."
✗ "Don't miss our AMAZING season launch!!" (three failures: the
exclamation, the caps, the selling).

**Announcement style.** Name, occasion, date, place — in that order,
once.
✓ "Miss Eleanor Vane, to Mr. Thomas Okafor — the fourteenth of June,
at St. Swithin's, followed by a reception at Hartfield House."
✗ "Big news! Eleanor & Thomas are tying the knot 🎉 Join us!" (the
register does not do big news, emoji, or exclamation).

**The form of words (fixed strings, verbatim).** "Accepts with
pleasure" · "Declines with regret" · "requests the honour of your
presence" · "At home on Thursdays" · "Not at home" · "Change one's
reply" · "The visit is complete". These are not copy to be edited;
they are the theme's liturgy (§10, blocking).

**Labels.** Clerk's caps, short, factual: "PRESENTATIONS 3 OF 9",
"THE SEASON", "LEAF TWO". ✗ "You're 33% through your journey!" —
no percentages, no journey, no "you're".

**Error voice — the hostess, correcting without embarrassment.**
✓ "The reply cannot be entered without a name — the book must know
whose answer it keeps." ✗ "Error: name is a required field." /
"Oops! Something went wrong 🙁". A failed send: ✓ "Your reply has
not been sent; the card is as you left it. Send again when ready."

**Empty voice.** §6.17's sentences: "Not at home." / "No card has
been left under this name." ✗ "Nothing here yet — check back soon!"
(the register never begs a return visit).

**Confirmation voice.** The filed line, past tense, complete:
✓ "Filed — Miss Clara Hartley accepts with pleasure, a party of
two." ✗ "Success! You're on the list 🎉".

**Banned words & marks.** Exclamation marks (everywhere); "amazing",
"stunning", "don't miss", "hurry", "limited time"; percentages as
progress; emoji; "Oops"; "journey"; "community" as a noun for
guests. **Owned words.** Presentation, register, leaf, season,
at-home, salver, filed, entered (in the book), received.

## 13. Full-page scroll choreography map

The home visit, top to footer, in order. (Detail and listing leaves
run the same beats with their own cards.)

| # | Beat | What the visitor sees & feels |
|---|---|---|
| 1 | Arrival | The table set: stack, empty salver, header list with the stack full. Stillness for 400ms — the room is composed. |
| 2 | The receiving (§6.1) | The top card lifts, catches the light, travels and turns on the salver. The season's headline is in the visitor's hand. |
| 3 | First announcement (§6.2) | Scrolling begins; the first section's card turns at its entrance, plate-mark completing at the edge-on instant. |
| 4 | The salver crossing (§6.3) | Through the first chapter the salver glides rightward with its one card; the table itself seems to be served. |
| 5 | An invitation uncovered (§6.4) | A tissue lifts from the at-home's particulars; beneath, the current invitation's sheen had been breathing (§6.12). |
| 6 | Names in the light (§6.5) | Each presented name takes its one sweep as it arrives — never twice, never on hover. |
| 7 | The calendar chapter (§6.10) | The calendar pins; announcements stream in precedence order; the gold marker keeps the visitor's place by date. |
| 8 | The thinning (§6.9) | In the header, miniatures slide away one by one; the figure climbs. The visit is measurably proceeding. |
| 9 | The ledger (§6.6) | The RSVP section is announced by its card; the ledger counts up to its true figures as it is presented. |
| 10 | The reply (§6.15, §6.7) | The visitor takes up a half-card, writes on ruled lines, sends; the crest strikes; the miniature flies to the salver. Their card is in the visit now. |
| 11 | The close (§6.16) | The footer's salver: every receipt in order, the last miniature settling its final 4px; the closing sentence. The stack in the header is empty. The visit is complete. |

Reverse pass: scrolling back up, nothing un-presents, un-counts or
un-files. Presented cards rest; the salver's scrub (§6.3) alone
reverses, because it is a position, not an event. Jump-scroll
(anchor, scrollbar drag): every card between here and there is
presented instantly in precedence order, the stack recounts without
sliding, and the destination is finished when the visitor arrives.

## 14. Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight (home) | ≤ 420KB compressed | Fonts dominate: Cormorant Garamond (italic + 500, subset to Latin + the season's names' glyphs where built per-site) ≈ 68KB; Libre Franklin (400/500/600 + tabular) ≈ 74KB |
| Hero critical path | The receiving (§6.1) must be runnable by fonts-ready + 300ms cap | No image blocks it; the salver is a gradient, the cards are DOM |
| Images | 0 photographs; SVG crests/ornaments ≤ 12KB total inline | §6.14's no-photograph law is also the performance law |
| Animation frame budget | ≤ 2.5ms of JS per frame, all loops combined | The shared rAF loop drives: salver scrub, parallax strata (≤6 writes), one tilt, counters when active. Everything else is CSS transitions on transform/opacity |
| Concurrent animations | ≤ 3 presentation events (turns/draws/lifts staggered to enforce) | §5's staggers are the enforcement |
| Long tasks | None > 50ms after load | Counting and FLIP measurements are the only JS of size; both are bounded per element |
| Layout shift | CLS = 0 from all motion | Card heights reserved by the grid-stack rule (§6.2); salver slot reserved (§6.1); tissue is an overlay (§6.4) |

**Cut order when the budget is exceeded** (cut in this order; the
visit's meaning is cut last): 1) the tissue sheen (§6.12) — 2) the
tea-table parallax strata (§6.12) — 3) the salver slide becomes a
parked salver (§6.3 reduced pattern) — 4) tilt-to-light (§6.11) —
5) the light-catch sweep (§6.5). **Never cut:** card turns (§6.2),
plate-mark draws (§6.8), the ledger's truth (§6.6), the stamp and
filing (§6.7), any fallback or watchdog. A page that keeps those
five is still this theme on a slow connection; a page that cuts
them and keeps the sheen is a screensaver at a tea party.

## 15. Build-order checklist

1. **The static visit first.** Build the complete page with every
   card details-up, marks printed, tissues absent, salver parked,
   ledger at truth. This is the no-JS, reduced-motion and print
   page, and it must be finished before any motion exists.
2. **Tokens & type.** Palette (§2) with the derived gold/blush
   grades; the two faces with §3's casting; measure the contrasts
   in the built CSS, not from this document.
3. **The table & cards.** Layout (§4): card ratios, plate-mark
   insets, salver zone, the 120px visiting intervals.
4. **Precedence pass.** Order all content in the DOM by §1 before
   styling any sequence; the choreography inherits the order.
5. **The header & stack.** §6.13 with §6.9's counter wired to the
   DOM's presentation count.
6. **Presentation grammar.** The observer + watchdog framework
   (§5's fallback law) as one shared utility; §6.2 turns and §6.8
   draws on top of it.
7. **The receiving.** §6.1's FLIP and settle, with the server
   rendering the received state by default.
8. **Covers & light.** §6.4 tissue, §6.5 light-catch, §6.12 strata
   and sheen — in that order, each behind the shared loop.
9. **The calendar.** §6.10's sticky, marker events, month-leaf turn.
10. **The reply.** §6.15's form (native first, classical post
    working), then §6.6's live ledger, then §6.7's stamp & filing.
11. **Index & emptiness.** §6.18's leaf, §6.17's card, §6.16's
    footer with its DOM-derived count.
12. **Tilt.** §6.11 last of the motions — it is the theme's one
    luxury and the first thing the cut order (§14) may take.
13. **Variants.** Reduced-motion pass over every element; candlelight
    dark pass (§2); forced-colors pass (tissue and sheen removed).
14. **The gate.** §10 in full, blocking items first, on a
    throttled CPU and with JS disabled, before the theme is used.
