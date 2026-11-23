# 74. Lagrange Post — Expanded (v1 + v2)

A postal service for the five Lagrange points. The site is a mail
route through orbital space: content arrives as letters, parcels
and postcards posted between gravitational harbours, and delay is
the aesthetic — deep space is far away, and this theme never
pretends otherwise. Every figure on the page — every transit day,
every light-minute, every denomination — traces to one declared
route record (§6.13), printed on the page itself, so a visitor can
re-derive any number the Post prints. Written directly to the
v1 + v2 standard: fifteen sections, eighteen elements, every
element carrying all eight v1 fields and all six v2 layers.

## 1. Concept & world

The Lagrange Post carries mail between Earth and the five
Lagrange points — the gravitational harbours where a letter can
be parked, relayed and forwarded without drifting away. The
company's whole proposition is unfashionable: it is slow, it is
honest about being slow, and it prices distance in the only
currency distance actually charges — time. A letter to L4 takes
twenty-two days. The site says so on its own hero, in a postmark,
before it says anything else.

The world of the theme is the airmail age rebuilt for orbit.
Paper is cream, edges are chevroned red and blue, postmarks are
inked at an angle because a hand pressed them, and the route is a
drawn chart of five node circles joined by one line — because a
postal network is a chart before it is anything else. Nothing on
the page is instant. Letters arrive; they do not appear. Parcels
are in transit; one of them is always still in transit, and the
page keeps it that way on purpose (§6.6). The visitor's role is
the recipient's and then the sender's: first you receive the
hero letter from L4, then you travel the outbound route node by
node, and at the end you are handed a telegram form and charged
by the word, exactly as the warning says.

**The theme's one law: the delay is printed, never hidden.**
Every transit figure, rate and distance on the page is read from
the route record (§6.13), which is itself printed as a page
element; the transit counter (§6.4) may only ever display a
number that exists in that record; and no element may imply a
faster service than the record allows. A build that shows "22
DAYS" in the hero and "fast delivery" in a footer has broken the
law even if every animation is perfect.

Best fit: space logistics and satellite-services companies with
long, honest sales cycles; deep-space mission and advocacy
organisations; slow-tech and correspondence-first products
(letter-writing services, archival print, pen-pal and epistolary
platforms); museums and exhibitions about the postal or space
ages; any brand whose truth is "this takes time and is worth
it." The theme flatters patience and punishes hype, so it suits
organisations that keep schedules measured in weeks.

When NOT to use it: anything whose promise is immediacy —
same-day delivery, live chat, real-time dashboards, breaking
news. A trading interface in Lagrange Post is a lie in both
directions. Also avoid it for content with no journey in it: a
single-page price list with nothing that travels gains nothing
from a route. And never use it where transit figures would be
decorative — if the client will not commit to one declared set
of numbers, the theme's law cannot be kept and another theme
should be chosen.

How the Post actually works, because the theme's details all
hang from it: mail leaves Earth on scheduled freight windows,
not on demand — a letter posted on Tuesday waits for the
window like a ship waits for a tide, and the record's transit
figures include the wait, which is why they are honest. L1 and
L2 are near harbours (the signal is five seconds; the freight
is two and three days because windows are weekly). L3 is
reached only by the relay arc around the Sun — nothing travels
the straight line through it — which is why the far side of
the Sun is fourteen days away on a 301M km road. L4 and L5 sit
at the same distance and the same eight-minute signal, but L5
runs against the orbital grain, so its freight takes
twenty-four days to L4's twenty-two; the record prints both,
and the theme never averages them into a "typical" figure. A
build that needs a reason for any number on the page will find
it in this paragraph or in the record — nowhere else.

The emotional register is unhurried confidence. The page moves
the way freight moves: long decelerations, arrivals that settle,
nothing that snaps. Typography does the class work — Franklin's
postal authority for anything the Post itself prints, Newsreader's
letterpress warmth for anything a person wrote, Special Elite's
typewriter face for anything a machine stamped. If a visitor
remembers one thing, it should be the postmark: RECEIVED — L4 —
22 DAYS IN TRANSIT. The brand arrived from far away and said so.

## 2. Palette

Five anchors from the original entry, unchanged. Derived tokens
are shades and working colours computed from the anchors; every
contrast figure below was measured from the hex values for this
expansion, not borrowed.

| Token | Hex | Role | Usage ratio | Pairing / contrast |
|---|---|---|---|---|
| `--paper` | `#F3EDE0` | Airmail cream — the page ground, letter stock | ~62% of surfaces | Ink on paper 7.65:1 (body-safe); blue on paper 5.79:1 |
| `--ink` | `#4A4A44` | Postmark ink — body text, postmarks, rules | ~18% | On paper 7.65:1; cream on ink 7.65:1 (footer stock) |
| `--blue` | `#2C5F8A` | Par-avion blue — route line, links, secondary text, chevrons | ~8% | On paper 5.79:1 (text-safe); on ink 1.32:1 — forbidden pairing |
| `--red` | `#C44536` | Par-avion red — chevrons, stamp accents, the one alert colour | ~6% | On paper 4.23:1 — large print and stamps only, never body text |
| `--gold` | `#C29B40` | Orbital gold — denominations, node rings, foil rules | ~3% | On paper 2.23:1 — never text on paper; on `--night` 5.24:1 — may letter on the chart only |
| `--paper-deep` | `#E9E0CC` | Derived — envelope stock, sheet shadows, table bands | ~2% | Ink on paper-deep 6.9:1 |
| `--onion` | `#FBF7EC` | Derived — onion-skin sheets, translucent overlays at 72% | ~1% | Always over `--paper` or `--night`; never a text ground alone |
| `--ink-soft` | `#6E6A5E` | Derived — captions, form hints, postmark dates at rest | sparing | On paper 4.63:1 — captions and labels ≥12px only, never body |
| `--night` | `#2E2E29` | Derived — the five-node chart panel, the one dark surface | one panel | Cream on night 11.70:1; gold on night 5.24:1 (chart lettering licensed) |
| `--postmark` | ink at 82% | Postmark impressions — ink is pressed, never solid | — | Rendered as `--ink` at 82% opacity with a 0.4px blur edge |

Rules that follow from the measurements:

- **Body text is ink on paper, full stop.** 7.65:1 is the
  theme's working contrast; letters are read at length and are
  never set in blue, red or gold.
- **Red never carries information alone.** At 4.23:1 it is a
  stamp colour: chevron stripes, the denomination corner's
  frame, one alert postmark. Any meaning red carries is also
  carried in words.
- **Gold is metal, not ink.** On paper it foils rules, rings
  and denomination numerals set large (≥24px) as *objects*, not
  text. Its single lettering licence is on the `--night` chart
  panel, where node designations stamp in gold at 5.24:1.
- **Forbidden pairings:** blue on ink (1.32:1), red on ink
  (1.81:1), gold on paper as text (2.23:1), gold on red in any
  role. A build containing any of these fails §10.
- **The chevron edge** is the only place red and blue meet:
  alternating 12px diagonal bands, always at a sheet's top or
  foot edge, never as a background fill behind text.

Dark-mode behaviour: the theme has no inverted scheme, by
ruling. Letters are physical objects; a letter does not turn
black at night. Under `prefers-color-scheme: dark` the page
keeps its paper (the reading lamp is assumed), and the `--night`
chart panel stays as it is — it was already the dark room the
chart is drawn in. What changes is only the page's outer frame
(the browser chrome surround, if the host site supplies one),
never the mail.

## 3. Typography

Three families, exactly as the original entry specifies — no
fourth voice is admitted.

- **Libre Franklin** (700/800) — postal display. Headlines,
  section titles, the masthead, rate-card headings: anything
  the Post prints officially. Set tight (−0.01em), uppercase
  only for labels and the masthead; headlines are sentence case
  because the Post is confident, not shouting.
- **Newsreader** (400/500, optical sizes on) — letter bodies.
  The voice of a person writing. 17–19px, line-height 1.55,
  measure 34–38em. Italic is the hand's emphasis; bold does not
  exist inside a letter.
- **Special Elite** — postmarks, the transit counter, form
  labels, denominations, dates. The typewriter that works in
  the sorting office. Never above 1rem except the hero postmark
  (1.25rem), never set in lowercase for postmark text, and its
  digits are placed on a fixed 0.62em-per-digit grid so the
  counter's figures do not jitter as they count — the machine's
  own carriage spacing, designed in rather than apologised for.

Type scale (desktop): display `clamp(2.5rem, 5.2vw, 4rem)`
Franklin 800; section title 2rem Franklin 700; letter title
1.375rem Franklin 700; body 1.125rem Newsreader; caption
0.8125rem Newsreader italic or Franklin 600 uppercase at
0.11em tracking; postmark 0.875rem Special Elite uppercase at
0.06em tracking; counter 1.5rem Special Elite on the digit grid.

Five type laws:

1. **Franklin never sets a letter body.** If a paragraph is
   correspondence, it is Newsreader; if Franklin appears inside
   a letter sheet, the sheet has been contaminated by the
   office and the build fails §10.
2. **Special Elite never sets prose.** Two lines maximum,
   anywhere. It stamps, labels and counts; it does not explain.
3. **Every figure is set from the route record (§6.13).** A
   number that does not exist in the record — a transit day, a
   rate, a distance — does not appear on the page in any face.
4. **Postmarks are never level.** Every postmark impression
   prints at a seeded angle between −7° and −3° (hero: exactly
   −6°). A level postmark reads as a forgery in this world.
5. **Letters never shout.** No uppercase, no bold, no red
   inside a letter body. Urgency in a letter is expressed by
   what it says, as it was in 1911 and as it is at L4.

## 4. Layout language

The page is a route, and the layout is its chart. One shared
route line — a 2px `--blue` SVG path — threads the whole page
from the masthead to the footer, passing through five node
stations, one per letter section. On wide screens the line runs
in a fixed left rail (a 120px chart margin) and the letters sit
to its right like sheets pinned along a route board; on narrow
screens the line folds to the top of each section as a horizontal
leg with its node circle at the left.

- **Grid.** 12 columns at ≥1200px with the route rail occupying
  columns 1–2; letter sheets span columns 3–11. 768–1199px:
  8 columns, rail narrows to 72px. <768px: single column, the
  route becomes a horizontal leg above each letter.
- **Sheets.** Every content section is a sheet: `--paper` (or
  `--onion` for overlays) with a chevron edge at its head, a
  perforated stamp frame for its image, and its postmark —
  node, date, days in transit — printed in the top-right
  corner at its seeded angle. Sheets are separated by 96–128px
  of open ground: the space between letters is transit, and it
  is left empty on purpose. Density is low and stays low; a
  Lagrange page that feels crowded has mistaken itself for a
  news site.
- **The chart panel.** The five-node chart (§6.5) is the one
  full-bleed, `--night` element — the dark room where the route
  is drawn in gold and cream. It is placed mid-page, after the
  second letter, so the visitor has received mail before being
  shown the network that carried it.
- **Spacing rhythm.** Base 8px; sheet padding 32px (24px
  mobile); the transit gaps between sheets are the rhythm —
  96px minimum, growing to 160px before the chart panel, the
  longest leg on the page, because L3 is far.
- **Anatomy of a letter sheet** (every letter, every page, in
  this order): chevron head edge; the postmark corner
  (top-right, seeded angle, node + date + days); the stamp
  frame (§6.7) where the letter carries a plate; the Franklin
  headline; the Newsreader body at the §3 measure; and the
  reply-slip foot — a ruled line carrying the letter's one
  onward act (reply, book, read the next letter). A sheet
  missing its postmark corner or its reply-slip is not a
  letter in this theme, whatever its content says.
- **Alignment.** Letters align to a shared left text edge;
  postmarks deliberately break it (they land where a hand
  landed). Nothing else breaks the grid. The one licensed
  irregularity is the postmark, and its licence is not
  transferable to headlines, images or buttons.

## 5. Full motion system

One shared requestAnimationFrame loop drives every scrubbed
value on the page — the route line's draw, the letters' travel,
the transit counter — at a lerp of **0.085**: deliberately heavy,
because the theme's scroll feel is *orbital patience*, long
smooth decelerations in which the page settles into each arrival
the way a ferry settles into a harbour. Named easings:

- `--ease-orbit` — `cubic-bezier(0.22, 0.61, 0.21, 1)`: the
  long deceleration; envelope travel, letter arrivals, the
  counter's settle.
- `--ease-stamp` — `cubic-bezier(0.55, 0, 0.85, 0.36)` down,
  60ms level settle: the postmark press. Fast, hard, final.
- `--ease-fold` — `cubic-bezier(0.37, 0, 0.21, 1)`: paper
  mechanics; the envelope flap, the frank-and-fold transition.
- `--ease-drift` — `linear` with a sinusoidal precession
  overlay: the tumbling parcel (§6.6) only.
- `--ease-post` — `cubic-bezier(0.25, 0.8, 0.3, 1)`: small
  settles — stamp frames landing, cards lifting from the rack.

Every motion term, in this theme's own language:

- **Scroll-triggered reveals** are *arrivals*: a letter enters
  along the route line and settles at its node (§6.3). Nothing
  fades up in place; on this page, things come from somewhere.
- **Scroll-driven/scrub** is the route itself: scroll position
  is distance along the line, and the transit counter (§6.4)
  is its readout.
- **Parallax** runs at postal depths: chevron edges at 0.92,
  onion-skin sheets at 0.96, postmark layers at 1.04 — three
  shallow layers, the depth of a small stack of mail on a desk.
  Nothing parallaxes further; deep parallax is for falling
  through space, and mail does not fall.
- **Pinned scenes:** the route chart pins (§6.5) while its five
  nodes draw and stamp; nothing else pins. One pin per page is
  the ration — a pinned page is a held letter, and the Post
  holds only the chart.
- **Masked reveals:** the opening letter (§6.2) slides from its
  envelope — the envelope is the mask. No other masks.
- **Blur-to-sharp is refused.** A blurred letter is a smudged
  letter; mail arrives legible or it has been damaged, and the
  theme does not perform damage. Type prints sharp, always.
- **Kinetic typography is refused** except the postmark: words
  in letters do not move. The one moving text is the counter,
  whose digits change because the route is being travelled.
- **Marquee is refused.** Mail does not hurry past a window.
  The route index (§6.11) is a printed list, still by law.
- **Counters:** the transit counter (§6.4) is the page's only
  counter family, and its figures come from the record.
- **Progress indicator:** the transit counter itself, beside
  the route — progress is days in transit, accumulated. There
  is no progress bar; a bar would measure the page, and this
  page measures the journey.
- **Ambient loops — exactly two licensed:** the tumbling parcel
  (§6.6) and the postmark dates' idle cycle on the chart
  (§6.5). Everything else is still when the visitor is still.
- **Hover physics:** the ghost postmark (§6.8) and the rack
  tilt (§6.3, max 3°) — the weight of handled paper, nothing
  springier.
- **Micro-interactions:** the stamp-down click (§6.9), the
  telegram's per-word counter (§6.10), the franking send
  (§6.10, §6.15). Each is a postal act, not a UI twitch.
- **Page transitions:** frank, fold, envelope wipe (§6.16).
- **Skeleton loading:** blank onion-skin gaining handwriting
  (§6.17).
- **Custom cursor: refused.** The system pointer is the
  visitor's hand; the Post does not lend them a novelty one.

Loop mechanics, stated once for the whole theme: scroll
position is sampled passively; each scrubbed value keeps a
current and a target, and the loop writes only values whose
delta exceeds 0.01 (positions) or one whole unit (counter
figures), so a still page costs still frames. Station
geometry is measured on load and on debounced resize, never
per frame. When the tab hides, the loop stops and every
phase-based element (the envelope's travel, the chart's draw)
recomputes from elapsed time on return — nothing fast-forwards
and nothing restarts. If the loop fails to start at all, the
page is already in its delivered state (§15, step 2) and each
element's watchdog simply confirms it.

Reduced motion, globally: all mail is delivered and open on
arrival — letters printed at their nodes, the counter showing
the final node's figures, the parcel parked, the chart drawn.
The page reads identically; only the travelling is removed.

## 6. Signature elements

### 6.1 The arriving envelope

- **What & why.** On load, a dotted orbital trajectory strokes
  itself across the hero, and an envelope travels it —
  decelerating over a long orbital ease — into a parking orbit
  beside the headline, where a postmark stamps down at exactly
  −6°: "RECEIVED — L4 — 22 DAYS IN TRANSIT." It belongs because
  the headline is mail that has travelled: the brand's promise
  (distance, honestly priced in time) is performed on its own
  name before a single claim is read.
- **Structure.** One inline SVG (viewBox 1200×520) layered over
  the hero: a dashed trajectory path (stroke `--blue`, dash
  2/7), the envelope as an SVG group (rect `--paper-deep`,
  chevron strip, flap polygon), and the postmark as an HTML
  overlay (double-ring border, Special Elite text, rotated
  −6°) so its text stays selectable and crisp. The trajectory's
  geometry is fixed at build; only the envelope's position
  along it is animated, via `getPointAtLength` in the shared
  loop.
- **Motion spec.** Trigger: load, once. Trajectory strokes in
  over 1600ms `--ease-orbit`. Envelope follows the path over
  2400ms `--ease-orbit` (the same curve, so it visibly slows
  into its orbit), ending parked at the path's final point,
  tilted 4° — parked, not landed. At t=2500ms the postmark
  presses: scale 1.6→1 over 120ms `--ease-stamp`, opacity
  0→0.82 (the `--postmark` value), then a 60ms level settle.
  The envelope then holds its parking orbit with a ±3px,
  9s-period drift — parked objects in a Lagrange harbour do
  drift, slightly, forever.
- **States.** Travelling / parked (drift only) / stamped
  (postmark down, §6.2 begins) / delivered-static (reduced
  motion, no-JS, or watchdog-fired: envelope printed parked,
  postmark printed, no trajectory motion).
- **Content merge.** The envelope carries the hero's own
  headline letter (§6.2) — it is not decoration around the
  hero, it is the hero's container. Its postmark states the
  true origin and transit of the page's first content, read
  from the route record (§6.13): L4, 22 days. Remove the
  letter and the envelope is empty; the element cannot be
  pasted onto a page that has no mail.
- **Failure fallback.** Watchdog at 2600ms: if the shared loop
  has not advanced the envelope past 90% of the path (blocked
  script, starved frames), the envelope snaps to parked, the
  postmark prints, and §6.2's letter is shown open. No-JS: the
  envelope is server-rendered parked with the postmark
  printed and the letter open beneath it — the delivered
  state is the DOM state; animation only performs the journey
  *toward* it.
- **Reduced-motion variant.** No travel, no stamp press: the
  hero opens delivered — envelope parked, postmark printed at
  −6°, letter open. The drift is off; a parked envelope under
  reduced motion is a still photograph of one.
- **Performance budget & mobile variant.** One SVG path lookup
  per frame plus a transform write: ≤0.3ms/frame, hero only,
  loop idles once parked (drift is a CSS animation on the
  parked group, not loop work). Mobile (<768px): trajectory
  shortened to a single arc across the hero's top third,
  travel 1800ms, drift amplitude ±2px.
- **Choreography timeline (v2).** t=0 first paint (hero text
  printed, envelope absent, letter open in DOM) → JS arms →
  letter folds away into the envelope's start position over
  200ms (only if JS armed before first paint + 300ms;
  otherwise the sequence is skipped and the delivered state
  stands) → trajectory strokes 0–1600ms → envelope travels
  300–2700ms → postmark presses at 2800ms (120ms + 60ms
  settle) → flap opens (§6.2) at 3000ms → drift begins 3400ms
  → watchdog deadline 2600ms for the travel leg passes unused
  or fires the snap.
- **State matrix (v2).** *Rest:* parked, drifting, postmark
  down. *Hover:* the drift pauses and the envelope straightens
  to 0° over 300ms — held up to the light. *Focus:* the
  envelope is not focusable (it is a scene, not a control);
  the letter inside it is the focusable content, in DOM order.
  *Active:* n/a. *Scrolled-past:* drift continues (it is
  ambient and cheap) but the loop stops sampling the path.
  *Disabled:* n/a. *Touch:* no hover straighten; tap does
  nothing — the envelope is not a button and never pretends.
- **Breakpoints (v2).** ≥1200px: full 1200×520 trajectory,
  envelope 300px wide. 768–1199px: trajectory compressed
  vertically (viewBox 1200×380), envelope 240px. <768px:
  single-arc trajectory across the hero top, envelope 180px,
  postmark 1rem.
- **Edge cases & failure modes (v2).** *Slow network:* the
  scene is inline SVG/HTML — no asset waits; fonts arriving
  late reflow the postmark text inside its fixed ring, which
  is sized for Special Elite's metrics with 12% slack.
  *Return visit:* a session flag skips the travel (the letter
  has already arrived once today) and opens delivered — the
  Post does not re-perform arrivals for regulars. *Tab hidden
  mid-travel:* the loop is phase-based on elapsed time, so on
  return the envelope is wherever the clock says, or the
  watchdog has delivered it. *Very fast scroll away:* nothing
  depends on the hero being watched.
- **Accessibility spec (v2).** The SVG is `aria-hidden`; the
  postmark text is real HTML with an accessible reading
  ("Received at L4, twenty-two days in transit") via
  `aria-label` on the postmark element, its visible text
  `aria-hidden` to avoid a double read. The hero's heading
  order is untouched by the scene. No focusable elements are
  added by this element.
- **Tokens consumed (v2).** `--paper-deep`, `--blue`, `--ink`,
  `--postmark`, `--red`, `--ease-orbit`, `--ease-stamp`,
  `--loop-lerp` (0.085), `--dur-trajectory` (1600ms),
  `--dur-travel` (2400ms).

### 6.2 The opening letter

- **What & why.** After the postmark lands, the envelope's flap
  folds open (500ms) and the headline letter slides out and
  unfolds beneath it — the hero copy is correspondence, and you
  read it because it was sent to you, from L4. It belongs
  because the theme's first content act is *receiving*: the
  visitor does not land on a headline, they open one.
- **Structure.** The letter is a DOM sheet (`--paper`, chevron
  head edge, perforated stamp frame at its top-right carrying
  denomination 55 — the L4 letter rate from §6.13) containing
  the real hero: an eyebrow line ("FROM THE L4 HARBOUR OFFICE"),
  the Franklin display headline, and the Newsreader letter body
  (212 words in the reference build, §13). The envelope (§6.1)
  is its mask: the sheet's wrapper clips to the envelope's
  mouth during the slide, then unclips at rest.
- **Motion spec.** Trigger: §6.1's stamp, at t≈3000ms. Flap
  rotates open (rotateX 0→160°) over 500ms `--ease-fold`. The
  sheet translates out 46% of its height over 700ms
  `--ease-orbit`, pauses 120ms (a hand adjusting its grip),
  then unfolds to full height over 600ms `--ease-fold` as the
  wrapper's clip releases. The headline is fully legible from
  the first unfold frame — the slide reveals, it never types
  or blurs.
- **States.** Sealed (pre-arrival, JS-armed only) / opening /
  open (rest state for the whole visit) / delivered (no-JS,
  reduced motion, watchdog: open from first paint).
- **Content merge.** This *is* the hero content — headline,
  standfirst and primary CTA (set as a printed reply-slip at
  the letter's foot, §6.11's navigation notwithstanding). The
  opening performance is the content's own delivery, not an
  intro played before it; there is no skip button because
  there is nothing to skip to — the letter is the page.
- **Failure fallback.** Watchdog at 4000ms from load: any
  state other than open is forced open (clip removed, flap
  hidden behind the sheet). No-JS: the letter ships open; the
  flap is a JS-inserted element and simply never exists.
- **Reduced-motion variant.** The letter is open on arrival,
  flap folded flat behind it, printed as delivered. Nothing
  in the hero moves.
- **Performance budget & mobile variant.** Transforms and one
  clip-path animation on a single sheet: ≤0.2ms/frame for
  ~1.8s, then zero. Mobile (<768px): the slide distance is
  34% (shorter sheet travel), unfold 450ms; the stamp frame
  shrinks to 72px wide.
- **Choreography timeline (v2).** Postmark down (t=0 for this
  element) → flap fold 0–500ms → sheet slide 500–1200ms →
  grip pause 1200–1320ms → unfold 1320–1920ms → reply-slip
  CTA settles (translateY 6px→0, 240ms `--ease-post`) →
  rest. Watchdog deadline 4000ms from load stands behind the
  whole sequence.
- **State matrix (v2).** *Rest:* open letter. *Hover:* the
  sheet lifts 2px and its shadow deepens one step — paper
  picked up, §6.3's rack tilt does not apply to the hero.
  *Focus:* focus entering the letter (headline link, CTA)
  shows the standard 2px `--blue` ring; the sheet itself is
  not a focus target. *Active:* n/a. *Scrolled-past:*
  unchanged — an opened letter stays open. *Disabled:* n/a.
  *Touch:* no lift; the letter is read, not handled.
- **Breakpoints (v2).** ≥1200px: sheet 720px wide, stamp
  frame 120px. 768–1199px: sheet spans the content columns,
  stamp 96px. <768px: sheet full-width minus 32px gutters,
  stamp 72px, headline at the scale's floor (2.5rem).
- **Edge cases & failure modes (v2).** *Long headline:* the
  sheet grows; the unfold duration is fixed, so a long letter
  unfolds faster per line — acceptable, paper is like that;
  beyond 3 headline lines the slide leg is dropped and only
  the unfold plays. *Short letter:* minimum sheet height
  340px keeps the stamp frame and postmark from colliding.
  *Fonts late:* the sheet's height is content-driven, so a
  reflow mid-unfold extends the clip rather than cropping
  text — the clip is released on a timer AND on a
  transitionend, whichever is later, capped by the watchdog.
- **Accessibility spec (v2).** Heading hierarchy starts here
  (the letter's headline is the page `h1`). The envelope and
  flap are `aria-hidden`. The unfolding is never the only way
  content appears — DOM order is reading order throughout.
  The reply-slip CTA is a real link, 48px tall.
- **Tokens consumed (v2).** `--paper`, `--paper-deep`, `--ink`,
  `--blue`, `--gold`, `--ease-fold`, `--ease-orbit`,
  `--ease-post`, `--dur-flap` (500ms), `--dur-unfold` (600ms).

### 6.3 Route-line letters

- **What & why.** Each section of the page is a letter that
  travels the shared route line, scrubbed to scroll, and
  arrives at its node (L1–L5) with a small orbital settle
  before it can be read in place. It belongs because chapters
  here are deliveries: the sitemap is a mail route, and
  reading is receiving. This is the theme's core scroll
  mechanic — the one every other element hangs from.
- **Structure.** A fixed SVG route path runs the page's full
  height in the left rail (≥768px) with five node circles at
  the letter sections' stations. Each letter is a DOM sheet
  (§4) whose station progress is computed in the shared loop:
  `p = clamp01((viewportCentre − stationStart) / legLength)`.
  The sheet's translateX (rail side) and its postmark opacity
  are functions of p; the route path's drawn length is the
  maximum p across stations, so the line is drawn exactly as
  far as the furthest letter has travelled — never ahead of
  the mail.
- **Motion spec.** Trigger: scroll, scrubbed through the
  shared loop at lerp 0.085. A letter begins its leg 40vh
  before its station centres, travels 24px (desktop) from the
  rail toward its reading position under `--ease-orbit`'s
  character, and settles with a 180ms, 2px overshoot-and-rest
  as p crosses 0.92 — the orbital settle. Its postmark fades
  to full `--postmark` opacity across p 0.85→1. Letters above
  the viewport rest fully arrived; the motion is a ratchet —
  scrolling back up does not un-deliver a letter (its p holds
  its maximum), because received mail stays received.
- **States.** In transit (p<0.85) / settling (0.85–1) /
  arrived (rest) / read (its stamp-down, §6.9, has been
  pressed by the visitor — a separate, persistent mark).
- **Content merge.** The letters *are* the page's sections —
  services, story, evidence, invitations — each written as
  correspondence from its node ("From L2, where the light is
  always leaving…"). The travel is not an entrance effect
  applied to neutral content; the content's fiction and the
  mechanic are the same fact.
- **Failure fallback.** Watchdog per letter at first
  intersection + 2000ms: if p has not reached 1 (loop stalled,
  path geometry failed), the letter is set arrived — transform
  cleared, postmark printed. No-JS: all letters ship arrived
  in reading position; the route line ships fully drawn.
- **Reduced-motion variant.** Letters are printed at their
  stations, arrived, postmarks down. The route line is fully
  drawn. Scrolling is just scrolling.
- **Performance budget & mobile variant.** Per frame: one path
  length write + ≤5 sheet transforms, ≤0.5ms/frame. Mobile
  (<768px): the rail folds away; each letter's leg is a short
  horizontal SVG segment above the sheet that draws as the
  sheet centres; travel distance 12px, settle overshoot 1px.
- **Choreography timeline (v2).** Station approaches (p 0→
  0.6: sheet still at rail offset, postmark at 0 opacity) →
  p 0.6–0.85: travel leg, sheet gliding the 24px → p 0.85:
  postmark begins to ink → p 0.92: settle overshoot 2px,
  180ms → p 1: arrived; the transit counter (§6.4) ticks to
  this node's figures; the node circle on the rail stamps its
  designation (§6.5's grammar, miniaturised).
- **State matrix (v2).** *Rest:* arrived sheet. *Hover:* the
  sheet tilts like a card lifted from a sorting rack — max
  3°, pivot at its bottom-left, 300ms `--ease-post` — and
  §6.8's ghost postmark appears. *Focus:* focus within the
  letter holds the tilt at 1.5° (a steadier hand for keyboard
  readers) and shows the focus ring on the focused element.
  *Active:* n/a for the sheet. *Scrolled-past:* arrived,
  unchanged; its node stays stamped on the rail.
  *Disabled:* n/a. *Touch:* no tilt; arrival is scroll-driven
  only.
- **Breakpoints (v2).** ≥1200px: rail 120px, travel 24px.
  768–1199px: rail 72px, travel 16px, node circles 28px.
  <768px: horizontal legs, travel 12px, node circle 22px at
  the leg's left end.
- **Edge cases & failure modes (v2).** *Jump scroll / anchor
  link:* letters above the landing point arrive instantly
  (ratchet), the landed letter plays its settle once — the
  Post does not make you re-travel a route you teleported
  across. *Very long letter:* its station leg lengthens
  (legLength scales with sheet height, capped at 120vh) so
  the settle never happens mid-reading. *Short page:* with
  fewer than three letters the route still draws; the theme
  is not licensed below three letters (§1) and the gate
  checks it. *Resize:* station geometry is re-measured on a
  debounced resize; p values are ratios, so nothing jumps.
- **Accessibility spec (v2).** Letters are `<article>`s with
  labelled headings in order; the route SVG is `aria-hidden`
  (it duplicates the reading order, which is the accessible
  route). Arrival never moves focus or changes DOM order.
  Tilt is disabled for any user with reduced motion or a
  coarse pointer who has scrolled — tilt is hover-only.
  Touch targets inside letters follow §11 (≥44px).
- **Tokens consumed (v2).** `--blue`, `--paper`, `--ink`,
  `--postmark`, `--ease-orbit`, `--ease-post`, `--loop-lerp`
  (0.085), `--dur-settle` (180ms), `--rail-w` (120px).

### 6.4 Transit-time counter

- **What & why.** Beside the route, a Special Elite counter
  accumulates days in transit true to the route record —
  minutes of signal near Earth, days of freight by L4 —
  updating as letters travel. It belongs because progress in
  this theme is delay: the counter makes the service's one
  truth (distance takes time) into the page's clock, and it
  replaces the progress bar the theme refuses (§5).
- **Structure.** A small printed plate fixed to the route rail
  (desktop) or docked above the current letter (mobile):
  three lines — `DAYS IN TRANSIT: n`, `SIGNAL: x`, `CARGO:
  n WORDS` — set in Special Elite on the 0.62em digit grid
  (§3), stamped onto a `--paper-deep` plate with a double
  rule. All three figures are read from the route record
  (§6.13) and the choreography map (§13): days and signal are
  the current node's row; cargo is the cumulative word count
  of letters arrived so far (hero 212 → 360 → 536 → 739 →
  970 → 1,159 across the reference page).
- **Motion spec.** Trigger: scroll, via the shared loop. As a
  letter's p (§6.3) crosses its leg, the days figure scrubs
  through the integers between the previous node's days and
  this node's (2 → 3 → 14 → 22 → 24 across the route) at the
  loop's lerp, landing exactly on the record's figure at
  arrival — the counter never displays a day count that is
  not either a record figure or a whole day between two
  record figures on the same leg. Signal switches discretely
  at arrival (5 SEC → 5 SEC → 17 MIN → 8 MIN → 8 MIN). Cargo
  counts up by the arriving letter's word count over 600ms
  `--ease-orbit`. The counter ratchets: scrolling up holds
  the furthest figures reached.
- **States.** At origin (before L1: days 0, signal "—",
  cargo = hero's 212 once §6.2 opens, else 0) / in transit
  (scrubbing) / at node (record figures, still) / complete
  (L5 arrived: 24 days, 8 MIN, 1,159 words).
- **Content merge.** The counter is the route's own
  instrument, printed on the rail the letters travel — it
  measures the content's journey, not the page's length. Its
  cargo figure literally counts the words of the letters on
  this page; a page with different letters shows a different,
  true, number.
- **Failure fallback.** Watchdog: if the loop stalls, the
  counter prints the figures of the furthest station the
  visitor has scrolled to (computed from scroll position
  directly, no loop). No-JS: the counter ships in its complete
  state (24 / 8 MIN / total cargo) — the delivered summary.
- **Reduced-motion variant.** The counter updates discretely
  at each arrival (no scrub, no count-up), figures identical.
- **Performance budget & mobile variant.** Three text writes
  per frame at most, only while a leg is in progress:
  ≤0.1ms/frame. Mobile: the plate docks as a slim bar above
  the current letter showing days and signal only; cargo
  moves to the footer (§6.18) where it is printed in full.
- **Choreography timeline (v2).** Hero opens → cargo ticks
  0→212 over 600ms → L1 leg: days scrub 0→2, at arrival
  signal prints 5 SEC, cargo 212→360 → L2 leg: days 2→3,
  cargo →536 → chart interlude (counter holds; the chart has
  its own figures, §6.5) → L3 leg: days 3→14, signal 17 MIN,
  cargo →739 → L4 leg: days 14→22, signal 8 MIN, cargo →970
  → L5 leg: days 22→24, cargo →1,159 → complete state; the
  footer's third printing (§6.18) agrees.
- **State matrix (v2).** *Rest:* current node's figures,
  still. *Hover:* the plate lifts 1px (it is an object on the
  rail) — no data changes. *Focus:* the counter is not
  focusable; it is `aria-hidden` from the tab order and read
  only via its live-region rules below. *Active:* n/a.
  *Scrolled-past:* ratcheted figures hold. *Disabled:* n/a.
  *Touch:* identical figures; the docked bar is not
  interactive.
- **Breakpoints (v2).** ≥1200px: full three-line plate on the
  rail, 1.5rem figures. 768–1199px: plate narrows, cargo line
  drops to the footer. <768px: docked two-figure bar.
- **Edge cases & failure modes (v2).** *A leg skipped by jump
  scroll:* figures jump to the landed node's row (ratchet) —
  the counter never pretends a journey took longer than the
  record says, nor shorter. *Record edited:* the counter
  reads the record from the DOM table (§6.13), so a corrected
  figure corrects everywhere; a missing row fails the build
  at §10, not at runtime. *Long dwell mid-leg:* scrub is
  position-based, so dwelling changes nothing.
- **Accessibility spec (v2).** The counter is decorative
  instrumentation of visible content; it is wrapped in
  `aria-hidden="true"` with a visually-hidden static summary
  ("Route: five nodes; longest transit twenty-four days")
  read once in rail order. Its changes are never announced —
  a screen reader user reads the letters, which carry the
  same facts in prose.
- **Tokens consumed (v2).** `--paper-deep`, `--ink`,
  `--ink-soft`, `--blue`, `--ease-orbit`, `--loop-lerp`
  (0.085), `--dur-cargo` (600ms).

### 6.5 Five node chart

- **What & why.** The route chart itself: five node circles
  (L1–L5) and their connecting arcs SVG-draw themselves as the
  chart centres, each node stamping its designation as drawn,
  with its record figures printed beneath — distance, signal,
  transit. It belongs because the map is the network: drawn as
  a postal chart on the page's one dark panel, because that is
  what the company operates.
- **Structure.** A full-bleed `--night` section containing one
  inline SVG (viewBox 1200×560): five circles (r 34, stroke
  `--gold` 2px, fill `--night`), four connecting arcs (stroke
  `--paper` at 40%, dash-drawn), a small Earth disc at the
  origin end, and HTML figure captions under each node (cream,
  with the designation in gold — the palette's one licensed
  gold lettering, 5.24:1 on night). The chart is the visual
  printing of the route record (§6.13); its numbers are the
  same numbers, in the same order.
- **Motion spec.** Trigger: scroll into view; the section pins
  for 140vh while the draw plays (the page's one pin, §5).
  Arcs draw sequentially over 1800ms total `--ease-orbit`
  (each arc ~450ms, overlapping by 90ms); as each arc lands,
  its node circle strokes in over 300ms and its designation
  stamps (scale 1.5→1, 110ms `--ease-stamp`, gold on night)
  with the figure caption fading to full over 240ms. Postmark
  dates on the chart idle through their cycle — the chart's
  small printed date line under the title advances one day per
  4s through the current node's transit figure and back (the
  second licensed ambient loop, §5) — a clerk idly turning a
  date stamp, never a data change: the record figures do not
  move.
- **States.** Undrawn (pre-centre; JS-armed only) / drawing /
  drawn (rest) / delivered (no-JS, reduced motion, watchdog:
  fully drawn with all designations printed).
- **Content merge.** The chart is not an illustration of the
  network; it is the network's own document, and §6.13's
  table is its second printing. A visitor who reads only the
  chart has the whole route's truth; a visitor who reads only
  the table has the same truth in rows.
- **Failure fallback.** Watchdog at 3000ms from first
  intersection: any undrawn arc or unstamped node is set to
  its drawn state. No-JS: the SVG ships with all strokes at
  full length and captions printed — the draw is a performance
  of a chart that exists complete in the DOM.
- **Reduced-motion variant.** No pin, no draw: the chart is
  printed complete as the section arrives. The date line is
  still (set to the L4 figure, the hero's node).
- **Performance budget & mobile variant.** Stroke-dash writes
  on 9 paths + 5 stamp transforms during a 1.8s window:
  ≤0.4ms/frame, then zero (date cycle is a 4s text write).
  Mobile (<768px): the chart turns vertical — nodes stacked
  down the panel, arcs as short vertical legs; pin shortens
  to 100vh; captions sit right of each node.
- **Choreography timeline (v2).** Panel centres → pin begins
  → arc 1 draws 0–450ms, node L1 stamps at 420ms → arc 2
  360–810ms, L2 stamps → arc 3 720–1170ms, L3 stamps → arc 4
  1080–1530ms, L4 stamps → L5 (terminus, no onward arc)
  stamps at 1560ms → all captions full by 1800ms → pin
  releases at 140vh scroll → date idle cycle begins.
- **State matrix (v2).** *Rest:* drawn chart, date idling.
  *Hover:* a node brightens its ring to full gold and its
  caption's figures bolden (weight, not colour) — the chart
  answers a pointing finger. *Focus:* nodes are links to
  their letters (the chart is the page's second navigation);
  focus shows a 2px cream ring offset 3px and the same
  brighten. *Active:* following a node link scrolls to its
  letter (which arrives instantly by ratchet, §6.3).
  *Scrolled-past:* drawn, date still idling (it is cheap and
  it is the chart's clerk). *Disabled:* n/a. *Touch:* tap =
  the link; no hover brighten.
- **Breakpoints (v2).** ≥1200px: horizontal chart as
  described. 768–1199px: horizontal, circles r 28, captions
  two-line. <768px: vertical chart, pin 100vh, draw total
  1400ms.
- **Edge cases & failure modes (v2).** *Pin unsupported /
  JS off:* the chart is a normal section, printed drawn.
  *Visitor scrolls fast through the pin:* the draw is
  scroll-scrubbed within the pin range, so fast scroll draws
  fast; at pin exit everything is drawn regardless (ratchet).
  *Figure dispute:* if §6.13's record and the chart disagree,
  that is a build failure caught by §10's figure audit — the
  chart generates its captions from the same source data as
  the table, so disagreement means the source was edited in
  one place only.
- **Accessibility spec (v2).** The SVG is `aria-hidden`; the
  captions are real HTML in reading order, and each node link
  is labelled "L3 letter — fourteen days in transit" so the
  chart is fully usable without the drawing. Contrast: cream
  on night 11.70:1, gold designations 5.24:1 at 1rem+ bold —
  the one place gold letters, licensed by §2.
- **Tokens consumed (v2).** `--night`, `--paper`, `--gold`,
  `--ink-soft`, `--ease-orbit`, `--ease-stamp`, `--dur-chart`
  (1800ms), `--pin-chart` (140vh).

### 6.6 Tumbling parcel

- **What & why.** A small parcel tumbles slowly along a margin
  orbit for the whole page — rotation ~12s per revolution with
  a slight precession — and never arrives. It belongs because
  some mail is still in transit: the page keeps one parcel
  permanently en route as the honest emblem of the service,
  and as the counterweight to every arrival the page performs.
- **Structure.** A 54px SVG parcel (kraft `--paper-deep` box,
  string cross, one small red/blue chevron edge, a printed
  label "L5 — IN TRANSIT") positioned in the right margin on
  desktop, following a tall, narrow elliptical orbit path
  whose height is the page's full scroll length. Its position
  is a function of scroll progress (it travels as you travel)
  plus its own time-based tumble — it is en route *with* you,
  never delivered *to* you.
- **Motion spec.** Trigger: time + scroll, continuous. Tumble:
  rotate 360° over 12s `--ease-drift` with a ±6° precession
  wobble on a 17s period. Orbit: the parcel's vertical
  position lerps (shared loop, 0.085) toward scroll progress
  mapped onto the margin ellipse; it drifts ±10px horizontally
  on the ellipse's curve. It never docks, never stamps, never
  opens. If the visitor reaches the footer, the parcel is
  still mid-orbit beside §6.18 — which prints its status in
  words: "ONE PARCEL STILL IN TRANSIT."
- **States.** En route (the only state) / parked (reduced
  motion: printed still in the margin at the hero's level,
  label legible) / absent (mobile <768px: the margin does not
  exist; the parcel appears once, parked, inside the footer
  beside its status line).
- **Content merge.** The parcel's label is a real route fact
  (L5, the longest letter transit at 24 days, §6.13) and the
  footer's status line is its second printing. It is the one
  element whose content is a *non*-arrival — remove it and
  the page claims everything arrives, which is precisely the
  lie the theme exists to refuse.
- **Failure fallback.** The parcel is pure enhancement: if
  the loop never runs, it renders parked at its first orbit
  position with its label readable. No-JS: parked, as in
  reduced motion. Nothing is hidden behind it, ever — it
  floats in margin space the layout reserves and content
  never enters.
- **Reduced-motion variant.** Parked, still, printed. The
  footer status line stands.
- **Performance budget & mobile variant.** One transform write
  per frame: ≤0.1ms/frame. Mobile: no orbit (see States) —
  the cost and the distraction both go to zero.
- **Choreography timeline (v2).** Page load: parcel fades in
  at orbit start over 600ms as the hero's envelope parks →
  scroll: travels the margin ellipse at the loop's lerp,
  tumbling throughout → chart pin: holds its orbit position
  (the pin is not travel) → footer: still en route beside the
  status line → end of page: nothing. It does not arrive.
  That is the timeline, and the gate (§10) checks that no
  build has quietly delivered it.
- **State matrix (v2).** *Rest:* tumbling en route. *Hover:*
  the tumble pauses and the label tips toward the reader
  (rotate to 0° over 300ms) — a parcel held up for
  inspection; it does not open. *Focus:* not focusable; it is
  `aria-hidden` atmosphere with its fact duplicated in the
  footer text. *Active:* n/a. *Scrolled-past:* it travels
  with the scroll, so it is never past. *Disabled:* n/a.
  *Touch:* no hover; it tumbles on.
- **Breakpoints (v2).** ≥1200px: right-margin orbit, parcel
  54px. 768–1199px: orbit narrows to the gutter, parcel 44px.
  <768px: parked footer instance only.
- **Edge cases & failure modes (v2).** *Short page:* the
  ellipse compresses; below three letters the theme is not
  licensed anyway (§6.3). *Margin collision:* the orbit's
  horizontal band is reserved in layout (§4); stamp frames
  (§6.7) never enter it. *Prefers-reduced-transparency or
  low-power mode:* parked variant, same as reduced motion.
- **Accessibility spec (v2).** `aria-hidden="true"`; its one
  fact ("one parcel still in transit to L5") is printed as
  real text in §6.18's footer. It never overlaps content, so
  it can never reduce anyone's contrast or hit area.
- **Tokens consumed (v2).** `--paper-deep`, `--red`, `--blue`,
  `--ink`, `--ease-drift`, `--loop-lerp` (0.085),
  `--dur-tumble` (12s).

### 6.7 Perforated stamp frames

- **What & why.** Postcards and images sit in stamp frames
  with true perforated edges — the frame's border is a
  radial-gradient dot mask, not a dashed line — and each
  carries a denomination corner that prints last. It belongs
  because pictures here are postage: valued, denominated and
  sent, like everything the company touches. An image in this
  theme has been *paid for* and the frame shows the price.
- **Structure.** A figure element: the image inside a `--paper`
  mat whose edge is perforated by a mask of radial-gradient
  dots (10px pitch, 3px holes) on all four sides; the
  denomination sits in the frame's top-right corner in Special
  Elite (gold numerals as objects ≥24px, §2's licence — or ink
  at smaller sizes); the caption prints beneath in Newsreader
  italic as the postcard's message line. Denominations are not
  decorative: a letter's stamp carries its node's letter rate
  from §6.13 (hero 55 for L4; L1 12, L2 14, L3 38, L5 58).
- **Motion spec.** Trigger: scroll into view. The stamp scales
  1.04 → 1.0 over 500ms `--ease-post` as it centres — a stamp
  pressed flat onto the page — and the denomination corner
  prints last: opacity 0→1 with a 90ms `--ease-stamp` press at
  the scale's end. No other motion; a stamp at rest is at rest.
- **States.** Incoming (pre-centre, JS-armed) / pressed (rest)
  / handled (hover: §6.8's ghost postmark may overlay it) /
  printed (no-JS, reduced motion, watchdog).
- **Content merge.** The denomination is the image's actual
  carriage cost from the record, and the caption is written
  as the postcard's message from that node ("The harbour at
  L3 holds station through the long night — wish you were
  in range."). The frame is how this theme publishes
  photography; there is no unframed image anywhere on the
  page, and §10 checks it.
- **Failure fallback.** Watchdog at 1800ms from first
  intersection: scale set to 1, denomination printed. No-JS:
  stamps ship pressed with denominations printed — the mask
  is CSS, so the perforation exists without any script.
- **Reduced-motion variant.** Stamps are printed pressed,
  denominations showing. Nothing scales.
- **Performance budget & mobile variant.** One transform +
  one opacity per stamp, ≤0.15ms/frame during its 500ms.
  The perforation mask is a composited background — no layout
  cost. Mobile: pitch tightens to 8px, denomination moves to
  the caption line (ink, 0.875rem) to keep the corner clear
  at small sizes.
- **Choreography timeline (v2).** Stamp enters viewport →
  scale begins at 30% visibility → 1.04→1.0 over 500ms →
  denomination presses at 480ms (90ms) → caption (already
  printed; it never animates) → rest. If the stamp is inside
  a §6.3 letter, its press waits for the letter's arrival
  settle (+180ms) — mail is opened before its enclosures are
  examined.
- **State matrix (v2).** *Rest:* pressed stamp. *Hover:*
  ghost postmark (§6.8) + the mat lifts 1px. *Focus:* if the
  image is a link, the frame's outer mat takes the 2px
  `--blue` ring; the perforation is never the focus style.
  *Active:* n/a. *Scrolled-past:* pressed, unchanged.
  *Disabled:* n/a. *Touch:* no lift; the press plays on
  scroll only.
- **Breakpoints (v2).** ≥1200px: full mat, denomination in
  corner. 768–1199px: mat padding −25%. <768px: mat padding
  10px, denomination in caption line.
- **Edge cases & failure modes (v2).** *Image fails to load:*
  the frame holds its shape with the caption and a printed
  "PLATE NOT RECEIVED" line in Special Elite — a missing
  plate is admitted in the theme's own language, never a
  broken-image icon. *Very tall image:* the mat crops to a
  4:3 maximum with the full plate one click away (the click
  is §6.9's stamp-down on the frame's corner). *Mask
  unsupported:* a solid 1px `--ink-soft` border replaces the
  perforation — plainer, still a frame.
- **Accessibility spec (v2).** Images carry real alt text
  written as descriptions, not captions (the caption is
  visible text and is not repeated into alt). Denomination is
  real text, read as "postage, fifty-five" via `aria-label`
  on the denomination element. Focus ring contrast: blue on
  paper 5.79:1.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--ink-soft`,
  `--gold`, `--blue`, `--ease-post`, `--ease-stamp`,
  `--dur-press` (500ms), `--perf-pitch` (10px).

### 6.8 Ghost-postmark hover

- **What & why.** Hovering a letter ghosts a faint circular
  postmark over it — opacity 0 → 0.18 over a slow 400ms fade —
  showing the node's mark. It belongs because handling mail
  leaves the route's mark on it: attention is franked,
  lightly, on the letter itself, and 0.18 is the whole point —
  a ghost is a handling mark, not a stamp.
- **Structure.** Each letter (§6.3) and stamp frame (§6.7)
  carries a pre-rendered postmark overlay (the same double-ring
  + Special Elite construction as §6.1's, at the element's
  seeded angle) positioned at its top-right, `pointer-events:
  none`, opacity 0. Hover/focus toggles a class; the fade is a
  CSS transition — the only element in the theme that does not
  need the shared loop.
- **Motion spec.** Trigger: hover or focus-within. Fade in
  400ms `--ease-post` to 0.18; hold while hovered; fade out
  300ms on leave. No movement — the ghost does not press, slide
  or rotate in; it *develops*, like a mark coming up under a
  thumb's warmth.
- **States.** Absent / ghosting (0.18) / superseded (if §6.9's
  real stamp-down lands, the ghost is replaced by the full
  impression at 0.82 and never returns for that element).
- **Content merge.** The ghost shows the element's own node's
  mark and the current transit day from §6.4's counter — it is
  the route's data, worn lightly. An element without a node
  (footer text, the rate card's fine print) grows no ghost;
  the mark only exists where mail exists.
- **Failure fallback.** If CSS transitions are unavailable the
  ghost simply does not appear — it is the one element whose
  total failure costs nothing, because it carries no unique
  information. No watchdog is needed and none is faked.
- **Reduced-motion variant.** The ghost appears and disappears
  without the fade (instant at 0.18) — or, on touch, never.
  The mark is still available via §6.9's deliberate stamp.
- **Performance budget & mobile variant.** One opacity
  transition: ≤0.05ms/frame. Mobile/touch: disabled entirely —
  there is no hover on a sorting table you touch with gloves;
  §6.9 covers the intent.
- **Choreography timeline (v2).** Pointer enters → 400ms fade
  to 0.18 → hold (postmark's date line shows the counter's
  current day, sampled at entry) → pointer leaves → 300ms
  fade out → absent. Focus-within follows the same beats so
  keyboard handling is franked too.
- **State matrix (v2).** *Rest:* absent. *Hover:* ghosting.
  *Focus:* ghosting at 0.22 (slightly deeper — the keyboard
  hand presses a little harder, and the difference keeps the
  two input modes distinguishable in testing). *Active:* the
  press becomes §6.9. *Scrolled-past:* absent (hover state
  clears on scroll). *Disabled:* n/a. *Touch:* absent by
  design.
- **Breakpoints (v2).** ≥1200px and 768–1199px: as described.
  <768px: disabled (touch-first assumption), §6.9 remains.
- **Edge cases & failure modes (v2).** *Rapid hover sweeping
  across letters:* each ghost fades independently; the 400ms
  in / 300ms out asymmetry means a sweep leaves no comet
  trail of half-faded marks. *Element already stamped (§6.9):*
  ghost never renders (see States). *Overlay above a link:*
  `pointer-events: none` is load-bearing and §10 tests a
  click through the ghost.
- **Accessibility spec (v2).** The ghost is `aria-hidden` and
  adds no focusable surface. Its information (node, day) is
  printed statically in each letter's own postmark corner
  (§4), so nothing is hover-gated. Focus-triggered ghosting
  gives keyboard users the same handling feedback sighted
  pointer users get.
- **Tokens consumed (v2).** `--postmark`, `--ink`, `--ease-post`,
  `--dur-ghost` (400ms), `--ghost-o` (0.18).

### 6.9 Stamp-down click

- **What & why.** Clicking a letter brings the postmark down
  hard: a dated postmark inks onto the element at a slight
  angle with a 120ms press and stays — the element is marked
  received, with the current transit day. It belongs because
  receipt is the reader's act: you stamp your own mail when
  you have read it, closing the loop the hero's arrival opened.
- **Structure.** The full-strength sibling of §6.8's ghost:
  the same overlay construction, rendered at `--postmark`
  opacity (0.82), its date line filled from §6.4's counter at
  the moment of the press ("DAY 22" on the hero's node). The
  stamped state persists for the session (a class + session
  storage flag keyed by letter ID) — a received letter does
  not un-receive itself on the next visit today.
- **Motion spec.** Trigger: click/tap, or Enter/Space on the
  letter's "mark received" control (see Accessibility). Press:
  scale 1.6→1 over 120ms `--ease-stamp` with opacity 0→0.82 in
  the first 60ms, a 2px downward settle over 60ms, and a 1%
  ink-spread (a 0.4px blur that sharpens) across 90ms — the
  physical sequence of a stamp landing. The letter itself
  dips 1px under the blow and recovers over 200ms
  `--ease-post`. Second clicks do nothing (already received);
  the mark cannot be double-struck.
- **States.** Unstamped / pressing / received (rest, permanent
  for the session) / printed-received (a returning session
  shows the mark already down, no press animation).
- **Content merge.** The stamp certifies the element's own
  content as read, with the route's true current day — it is
  a reading receipt written in the theme's grammar, not a
  like button in fancy dress. The footer's tally (§6.18)
  counts received letters from the same flags: "RECEIVED BY
  YOU: n OF 5."
- **Failure fallback.** If the press animation cannot run, the
  mark appears at full opacity instantly — the state matters,
  the theatre is optional. No-JS: letters ship unstamped and
  the "mark received" control is absent; nothing is lost,
  because the letters themselves are complete (§6.3).
- **Reduced-motion variant.** The mark prints instantly at
  full opacity; no press, no dip, no spread.
- **Performance budget & mobile variant.** One transform +
  opacity on one overlay: ≤0.1ms/frame for ~380ms. Mobile:
  identical (tap is the natural gesture — stamping is a
  thumb's work), press scale starts at 1.4 to keep the mark
  inside small sheets.
- **Choreography timeline (v2).** Click → ghost (§6.8, if
  present) clears in 60ms → press 0–120ms (opacity full by
  60ms) → letter dip 60–260ms → ink spread sharpens by
  210ms → settle complete 320ms → footer tally updates
  (text write, no animation) → rest: received.
- **State matrix (v2).** *Rest:* unstamped or received.
  *Hover:* §6.8 ghost (unstamped only). *Focus:* the mark-
  received control (a real button printed at the letter's
  foot as a reply-slip line, "MARK RECEIVED") shows the blue
  ring; the sheet itself is not the control. *Active:* the
  press. *Scrolled-past:* state persists. *Disabled:* the
  button disables once stamped (it has done its work), with
  its label changing to "RECEIVED — DAY n". *Touch:* tap on
  the button only — tapping the sheet body does not stamp,
  because reading is not receipt.
- **Breakpoints (v2).** All breakpoints: same press; the
  mark's size scales with the sheet (hero 132px, letters
  104px, mobile 88px).
- **Edge cases & failure modes (v2).** *Session storage
  blocked:* the mark lasts for the page view only — noted in
  §10 as an acceptable degradation, never an error shown to
  the visitor. *Stamp lands over text:* the mark's position
  is the sheet's reserved postmark corner (§4), never over
  the body measure. *Rapid double-click:* the second is
  absorbed by the state check; no double impression.
- **Accessibility spec (v2).** Stamping is done from a real
  `<button>` with a text label; the visual press is
  `aria-hidden`. The button's state is exposed via
  `aria-pressed` and its label update. The mark itself is
  decorative over content that remains fully readable beneath
  it (0.82 ink over the reserved corner only).
- **Tokens consumed (v2).** `--postmark`, `--ink`, `--blue`,
  `--ease-stamp`, `--ease-post`, `--dur-press-stamp` (120ms).

### 6.10 Telegram contact form

- **What & why.** The contact form is a telegram: a live
  per-word counter, a running delay line, and a send button
  that is a franking stamp — beneath the printed warning,
  verbatim from the original entry: "CHARGED BY THE WORD.
  LIGHT-TIME DELAY: 22 DAYS. CHOOSE WORDS AS CARGO." It
  belongs because the form enforces the service's economics:
  words are cargo, and the interface charges attention by the
  word, as the warning promises.
- **Structure.** A telegram sheet (`--onion` over `--paper`,
  chevron foot edge): destination node selector (five radio
  "offices", L1–L5), a Newsreader textarea ruled like a
  telegram blank, and a Special Elite tally line that recomputes
  on every input event: `WORDS: n — POSTAGE: n × rate — LIGHT-TIME
  DELAY: d DAYS`, where rate and d are read from the selected
  node's row in §6.13 (L4: 5 per word, 22 days — the warning's
  own figures, because the form's default destination is L4).
  The send control is a franked stamp button (denomination
  corner updates with the postage total).
- **Motion spec.** Trigger: input events. Each word boundary
  crossed ticks the counter with a 90ms `--ease-stamp`
  mini-press on the tally (scale 1→0.97→1) — the office
  machine counting. The delay line never animates; delays do
  not perform. On send: the frank presses (140ms
  `--ease-stamp`), the sheet folds (§6.16's fold, 500ms
  `--ease-fold`) and slides into an envelope wipe, and the
  confirmation arrives as a received telegram slip (§6.17's
  grammar in reverse) bearing the same word count and a
  delivery date computed from the record: today + d days,
  printed in full.
- **States.** Blank (tally at 0, frank greyed but visible) /
  drafting (tally live) / over-length (past 60 words the
  tally prints "OVER THE WIRE LIMIT — SEND AS TWO TELEGRAMS"
  and the frank refuses until split or trimmed — the limit
  is the theme's, stated on the sheet) / sending (fold) /
  sent (confirmation slip; the form reprints blank beneath
  it) / error (undeliverable — see §12's voice).
- **Content merge.** This is the page's conversion act, and
  its mechanics are the product: a visitor who has written
  fourteen careful words has already understood the Lagrange
  Post better than any headline could teach them. The
  postage they "pay" is attention, counted honestly.
- **Failure fallback.** No-JS: the form is a plain working
  form (real `action`, real submit); the tally line prints
  the L4 default figures statically and the server recomputes
  — the counter is an enhancement of a form that never
  depends on it. Watchdog: if input handlers fail to attach
  by 2000ms, the tally is replaced by the static default line
  so no stale figure can mislead.
- **Reduced-motion variant.** No tally tick, no fold: send
  swaps directly to the confirmation slip. The counting is
  identical — arithmetic is not motion.
- **Performance budget & mobile variant.** Input handler does
  one word-count + one text write per event: negligible.
  Mobile: the node selector becomes a horizontal office strip;
  the tally wraps to two lines with the postage figure kept
  whole (figures never break mid-number).
- **Choreography timeline (v2).** Sheet arrives (§6.3's leg,
  as the page's final letter) → visitor selects office (tally
  delay line updates instantly to that node's days) → typing:
  per-word ticks → send: frank press 140ms → fold 500ms →
  wipe 400ms → confirmation slip settles 300ms `--ease-post`
  with its delivery date printed → tally in the footer
  (§6.18) unchanged (telegrams are not letters; the received
  count is letters only — the record keeps its categories
  clean).
- **State matrix (v2).** *Rest:* blank telegram, warning
  printed, tally at the L4 default. *Hover:* the frank lifts
  1px. *Focus:* fields take the 2px `--blue` ring; the tally
  is a live region at `aria-live="off"` (it would chatter) —
  instead the postage total is summarised on blur and on
  send. *Active:* frank press. *Scrolled-past:* a drafted
  telegram persists (its text is the visitor's cargo; the
  page never discards cargo). *Disabled:* the frank disables
  only in the over-length and sending states, with the
  reason printed beside it. *Touch:* identical; the tally
  tick is visual only.
- **Breakpoints (v2).** ≥1200px: sheet 680px, tally one line.
  768–1199px: sheet full measure. <768px: office strip
  scrolls horizontally; textarea 5 rows; tally two lines.
- **Edge cases & failure modes (v2).** *Pasted 400 words:*
  the count lands whole, the over-limit state engages, no
  tick animation storm (ticks are capped at one per 90ms and
  skipped entirely for jumps >5 words). *Empty send:* the
  frank shakes once — no: shaking is refused in this theme;
  the sheet prints "A TELEGRAM OF NO WORDS CARRIES NOTHING"
  under the blank and stays. *Destination switched mid-draft:*
  tally recomputes from the same text; the visitor's words
  are never touched. *Network failure on send:* the slip
  prints the §12 error line and the draft is restored intact.
- **Accessibility spec (v2).** Real `<form>`, real labels
  ("Destination office", "Your telegram"), the warning is
  visible text, not a tooltip. The word count is available
  to AT via a visually-hidden status updated on blur.
  Postage figures are text, never colour-coded. Send button
  minimum 48px. Error text is ink on paper (7.65:1); the red
  frank outline is never the only error signal.
- **Tokens consumed (v2).** `--onion`, `--paper`, `--ink`,
  `--red`, `--blue`, `--gold`, `--ease-stamp`, `--ease-fold`,
  `--ease-post`, `--dur-tick` (90ms).

### 6.11 Postmark masthead & route navigation

- **What & why.** The page's header is the Post's masthead: the
  wordmark set as a franked postmark block, and the navigation
  is the route index — the five nodes listed as printed
  offices with their transit days beside them. It belongs
  because in this theme you do not navigate a site, you choose
  a destination; the nav is the route table's first, smallest
  printing.
- **Structure.** A `--paper` header band: left, the wordmark
  (Franklin 800, "LAGRANGE POST") with a small circular
  postmark device (ink, −4°) overlapping its corner; right,
  the route index as an inline list — `L1 · 2D — L2 · 3D —
  L3 · 14D — L4 · 22D — L5 · 24D` in Special Elite, each a
  link to its letter. Beneath, a 2px rule from which the
  route line (§6.3) descends. Figures are §6.13's transit
  column, unrounded and unabbreviated beyond the D.
- **Motion spec.** Trigger: load + scroll. On load the
  postmark device presses once (120ms `--ease-stamp`) after
  the hero trajectory begins — the office franked this page
  before the mail moved. On scroll the masthead does not
  shrink, chase or hide: it scrolls away like the top of a
  letter. A slim route-index strip (the five nodes only)
  docks at the viewport top once the masthead passes, fading
  in over 240ms — the index card pulled from the file, not a
  sticky nav in costume.
- **States.** Full masthead / docked index (scrolled) /
  current-node (the docked strip underlines the node whose
  letter is centred, in `--blue`, weight change only) /
  printed (no-JS: masthead only, no docked strip).
- **Content merge.** The nav's labels are the record's data;
  choosing L3 from the header and reading "14 days" beside it
  is the theme's whole argument in one line of Special Elite.
  A generic "Services / About / Contact" nav is forbidden
  here — destinations, not departments.
- **Failure fallback.** The docked strip is JS-enhanced; its
  absence costs nothing (the masthead's index remains at the
  top, and §6.5's chart is the second navigation). Watchdog:
  if the dock logic has not initialised by 2000ms the strip
  never appears rather than appearing late over content.
- **Reduced-motion variant.** The docked strip appears
  without the fade; the postmark device is printed, unpressed.
- **Performance budget & mobile variant.** One intersection
  check + one opacity transition: negligible. Mobile: the
  route index wraps under the wordmark (two lines, figures
  kept with their nodes); the docked strip shows nodes only,
  days dropped to keep the strip one line — the letters
  themselves still print their full figures.
- **Choreography timeline (v2).** t=0 masthead printed →
  hero trajectory starts → postmark device presses at 400ms
  → scroll: masthead leaves → docked strip fades in 240ms at
  the masthead's exit → node underlines track §6.3 arrivals
  → footer reached: strip fades out (the route is complete;
  the index goes back in the file).
- **State matrix (v2).** *Rest:* masthead or docked strip.
  *Hover:* a node link's underline draws in 160ms
  `--ease-post` (a ruled line, postal and plain). *Focus:*
  blue ring on the link; the underline also draws (keyboard
  parity). *Active:* link follows to its letter (ratchet
  arrival, §6.3). *Scrolled-past:* docked state. *Disabled:*
  n/a. *Touch:* tap targets are the full node cells, 44px.
- **Breakpoints (v2).** ≥1200px: one-line index. 768–1199px:
  index wraps to two lines right-aligned. <768px: index
  under wordmark; docked strip nodes-only.
- **Edge cases & failure modes (v2).** *Longer wordmark (a
  sub-brand):* the postmark device keeps its corner; the
  index drops below rather than compressing figures.
  *Current node ambiguity mid-leg:* the underline stays on
  the last arrived node — the index reports arrivals, not
  intentions. *Print stylesheet:* the masthead prints as a
  letterhead, docked strip suppressed.
- **Accessibility spec (v2).** A real `<nav>` with an
  aria-label "Route index"; the current node carries
  `aria-current="location"` in the docked strip. The postmark
  device is `aria-hidden` (the wordmark is the name). Link
  text includes the days ("L3, fourteen days") via
  visually-hidden expansion of the D.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--blue`,
  `--postmark`, `--ease-stamp`, `--ease-post`, `--dur-dock`
  (240ms).

### 6.12 The mail index

- **What & why.** The listing element: an index of letters and
  parcels presented as sorting-office index cards — each card
  a row with its node's postmark tab, its headline as the
  letter's first line, its word count as cargo, and its
  transit figure. It belongs because a postal service's
  catalogue is a mail index; visitors browse what is in
  transit and what has been received, not "content cards."
- **Structure.** A ruled index table (real `<table>` semantics
  via list markup with row groups): each row is a card on
  `--paper` with a left postmark tab (node + days, Special
  Elite), the headline (Franklin 700), a one-line Newsreader
  standfirst, and a right-aligned cargo figure (`212 WORDS`,
  from the letter's true count). Rows separate with hairline
  ink rules; every fifth row takes a `--paper-deep` band, the
  sorting office's ruled ledger rhythm.
- **Motion spec.** Trigger: scroll. Rows arrive like §6.3's
  letters in miniature: each slides 12px from the rail side
  and settles (180ms `--ease-post`) as it crosses the 70%
  line, staggered 60ms per row within a viewport batch —
  mail sorted into pigeonholes, the original system's own
  image. No row animates twice; the index is a ratchet like
  everything else here.
- **States.** Unsorted (pre-arrival, JS-armed) / arriving /
  filed (rest) / received (a row whose letter was stamped
  §6.9 shows a small received mark in its tab).
- **Content merge.** The index's rows are the page's (or the
  archive's) actual letters with their actual figures —
  headline, node, days, words all true. Filtering the index
  (by node, via §6.11's grammar) files and re-files real
  mail; there is no demo content in the drawers.
- **Failure fallback.** Watchdog per batch at 1800ms: unfiled
  rows snap to filed. No-JS: the index ships filed, complete,
  in order.
- **Reduced-motion variant.** Rows are filed on arrival; no
  slide, no stagger.
- **Performance budget & mobile variant.** ≤8 row transforms
  per batch, ≤0.2ms/frame. Mobile: the cargo figure moves
  under the headline (rows grow taller rather than figures
  shrinking); the postmark tab stays — it is the row's
  identity.
- **Choreography timeline (v2).** Index section's letter
  arrives (§6.3) → first batch of rows files 60ms apart →
  subsequent batches as scrolled → a row stamped elsewhere
  (§6.9) shows its received mark on next view of the index
  (state read at render, no live patching theatrics).
- **State matrix (v2).** *Rest:* filed row. *Hover:* the row
  lifts from the rack — 3° tilt is reserved for letters; the
  index row lifts 2px straight, a card pulled halfway from
  its drawer. *Focus:* the row's link takes the blue ring;
  the lift applies. *Active:* follows to the letter.
  *Scrolled-past:* filed. *Disabled:* n/a. *Touch:* no lift;
  tap follows.
- **Breakpoints (v2).** ≥1200px: full row (tab, headline,
  standfirst, cargo). 768–1199px: standfirst truncates to
  one line. <768px: cargo under headline; tab becomes a top
  strip on the card.
- **Edge cases & failure modes (v2).** *Empty drawer (a node
  with no letters):* the index prints the §12 empty line —
  "NO MAIL FOR L3 THIS SEASON — THE ROUTE STILL RUNS." —
  never a blank gap. *Very long archive:* pagination is by
  season (§11), printed as index dividers, not infinite
  scroll — a drawer you can empty is the theme's honesty
  about volume. *Duplicate headlines:* cargo figures and
  dates distinguish rows; the office files by more than
  titles.
- **Accessibility spec (v2).** The index is a list of links
  with full accessible names ("Letter from L3 — The Long
  Night — fourteen days in transit, two hundred and three
  words"). Row lift is visual only. Banding is never the
  only distinction between rows.
- **Tokens consumed (v2).** `--paper`, `--paper-deep`, `--ink`,
  `--ink-soft`, `--blue`, `--ease-post`, `--dur-file` (180ms).

### 6.13 The route record

- **What & why.** The theme's declared data anchor: one printed
  table holding every figure the page is allowed to use — per
  node, its distance from Earth, its signal (light-time), its
  letter transit in days, its telegram rate per word, its
  letter postage and its parcel rate per kilogram. It belongs
  because the theme's law (§1) — the delay is printed, never
  hidden — needs a single source of truth that is itself part
  of the page, auditable by any visitor with a pencil.
- **Structure.** A real `<table>` on a `--paper-deep` sheet,
  ruled like a ledger, Franklin headings, Special Elite
  figures on the digit grid. The record for the reference
  build, printed identically here and everywhere it is used:

  | Node | Distance | Signal | Letter transit | Telegram /word | Letter postage | Parcel /kg |
  |---|---|---|---|---|---|---|
  | L1 | 1.5M km | 5 sec | 2 days | 1 | 12 | 90 |
  | L2 | 1.5M km | 5 sec | 3 days | 1 | 14 | 95 |
  | L3 | 301M km (relay arc) | 17 min | 14 days | 3 | 38 | 210 |
  | L4 | 150M km | 8 min | 22 days | 5 | 55 | 260 |
  | L5 | 150M km | 8 min | 24 days | 5 | 58 | 275 |

  The DOM table is the runtime source: §6.4's counter, §6.10's
  tally and §6.14's card all read their figures from these
  cells (or from the same build-time data that prints them —
  never from a second hand-typed copy).
- **Motion spec.** Trigger: scroll into view. The table is
  printed, not performed: rows take a 120ms `--ease-post`
  settle in sequence (40ms apart) as the sheet arrives — a
  ledger laid on the counter. Figures never count, scrub or
  animate; the record is the thing other elements' motion is
  measured against, and it holds still.
- **States.** Printed (the only state) / referenced (when
  another element is mid-animation, the record is visually
  unchanged — it does not highlight itself; the truth does
  not wave).
- **Content merge.** The record is the page's constitution
  printed as a page element: §6.1's postmark (22 days), §6.4's
  counter, §6.5's chart captions, §6.7's denominations (55 on
  the hero stamp), §6.10's warning (22 days, 5 per word at
  L4) and §6.15's waybill arithmetic are all this table,
  quoted. A build whose figures disagree with its own record
  has not made a typo; it has broken the theme.
- **Failure fallback.** The table is static HTML: it cannot
  fail to appear. If JS is absent, dependent elements fall
  back to their printed defaults, which are this table's
  values typed once in the static markup and audited against
  it at §10.
- **Reduced-motion variant.** Identical, minus the row
  settles.
- **Performance budget & mobile variant.** Zero animation
  cost. Mobile: the table scrolls horizontally inside its
  sheet with the Node column sticky — figures are never
  shrunk below 0.875rem, because a rate you cannot read is a
  rate you are hiding.
- **Choreography timeline (v2).** The record's sheet arrives
  (§6.3) after the L2 letter and before the chart (§13) →
  rows settle 40ms apart → rest, permanently. Its position
  in the page order is deliberate: the visitor has received
  two letters and felt the delay before being shown the
  table that prices it.
- **State matrix (v2).** *Rest:* printed. *Hover:* a row
  takes the `--paper` lift (the ledger's page under a
  thumb). *Focus:* rows are not focusable; cell text is
  selectable. *Active:* n/a. *Scrolled-past:* printed.
  *Disabled:* n/a. *Touch:* horizontal scroll of the sheet,
  with the sticky node column.
- **Breakpoints (v2).** ≥1200px: full seven-column table.
  768–1199px: distance column abbreviates (1.5M km → 1.5M).
  <768px: horizontal scroll, sticky first column.
- **Edge cases & failure modes (v2).** *A route with a node
  added or retired:* the record gains or loses a row and
  every dependent element follows from the same source — but
  the theme licenses exactly five nodes (§1); a sixth row is
  a different theme. *Figure corrected post-launch:* correct
  the source once; §10's audit greps the built page for every
  other printing of the old figure. *Rounding:* forbidden —
  the record prints 1.5M km because the Post publishes 1.5M
  km; a build that prints 1,500,000 km or "about a week" for
  5 days fails the gate.
- **Accessibility spec (v2).** A genuine `<table>` with
  `<th scope="col">` headings and a caption ("The route
  record — all figures used on this page"). Figures are
  text. Contrast: ink on paper-deep 6.9:1.
- **Tokens consumed (v2).** `--paper-deep`, `--paper`, `--ink`,
  `--ink-soft`, `--blue`, `--ease-post`, `--dur-ledger`
  (120ms).

### 6.14 Rate card

- **What & why.** The pricing element: the Post's services
  laid out as a printed rate card — letters, telegrams,
  parcels, each with its per-node rates quoted from §6.13 and
  its conditions in letterpress small print. It belongs
  because a postal service publishes its rates on a card at
  the counter; pricing here is a public document, not a
  marketing grid with a "most popular" ribbon.
- **Structure.** A `--paper` card, chevron head edge, three
  service blocks. Each block: the service name (Franklin),
  a one-line Newsreader description written as a clerk would
  ("A letter is one sheet, sealed, carried the whole route"),
  and its rate row per node in Special Elite, quoted from the
  record (letter postage 12 / 14 / 38 / 55 / 58; telegram per
  word 1 / 1 / 3 / 5 / 5; parcel per kg 90 / 95 / 210 / 260 /
  275). The card's foot carries the conditions in 0.8125rem:
  what a sheet is, what a word is, when the clock starts.
- **Motion spec.** Trigger: scroll into view. The card arrives
  as a letter (§6.3's settle, shared with its section). Inside,
  nothing animates except one thing: hovering a service block
  ghosts that block's total for the worked example printed
  beside it (§6.8's grammar at 0.12 — a pencil total, lightly
  shown). Rates never count up; a price that performs is a
  price that is lying about being fixed.
- **States.** Printed / example-ghosted (hover) / printed
  (no-JS, reduced motion).
- **Content merge.** The rate card is §6.13 read as a customer
  document; §8.2's worked example is priced from it in front
  of the visitor (a letter and a 2 kg parcel to L4: 55 +
  2 × 260 = 575, printed in the example). Pricing pages in
  this theme do not have tiers, toggles or annual discounts —
  the Post charges by distance and weight, and the card says
  so.
- **Failure fallback.** Fully static; the ghost is the only
  enhancement and its absence costs nothing (§6.8's ruling
  applies).
- **Reduced-motion variant.** Identical; the ghost appears
  without its fade.
- **Performance budget & mobile variant.** Zero loop cost.
  Mobile: service blocks stack; rate rows wrap as five
  node chips per service with figures kept whole.
- **Choreography timeline (v2).** Card arrives with its
  section (§6.3 settle) → conditions print (always visible)
  → hover ghosts the example total → the section's own worked
  example (§8.2) sits immediately below, so the eye travels
  card → arithmetic → total without a scroll.
- **State matrix (v2).** *Rest:* printed card. *Hover:* the
  example-total ghost on the hovered block. *Focus:* blocks
  are not links; the example total is also printed statically
  in §8.2, so focus users lose nothing. *Active:* n/a.
  *Scrolled-past:* printed. *Disabled:* n/a. *Touch:* no
  ghost; the static example stands.
- **Breakpoints (v2).** ≥1200px: three blocks side by side.
  768–1199px: blocks in a 2+1 arrangement. <768px: stacked,
  node chips wrap.
- **Edge cases & failure modes (v2).** *A rate changes:* the
  record (§6.13) changes and the card follows from the same
  source; a card edited alone fails §10. *A service is
  withdrawn:* its block is struck through with a printed
  "SERVICE SUSPENDED — THE ROUTE REMAINS" line (the strike
  never deletes, §12) rather than vanishing — the Post's
  history stays on the card. *Currency:* the record's units
  are the Post's own; a build that converts them into a
  visitor's local currency has invented figures and fails.
- **Accessibility spec (v2).** Rates are text in a list, not
  a graphic; each block's heading names the service before
  its figures. The ghost total is `aria-hidden` and
  duplicated statically in §8.2.
- **Tokens consumed (v2).** `--paper`, `--ink`, `--ink-soft`,
  `--red`, `--blue`, `--ease-post`, `--ghost-o` (0.18, ghost
  at 0.12 here).

### 6.15 Waybill booking form

- **What & why.** The parcel conversion: a waybill — the
  printed form that travels with freight — for booking a
  parcel to a node, with weight stepped in kilograms, the
  rate per kilogram quoted from §6.13, and a total that is
  arithmetic the visitor can check. It belongs because
  freight in this world is documented, not checked out; the
  booking is a form you fill in by hand at the counter.
- **Structure.** A waybill sheet (doubled chevron edge — the
  freight form is heavier paper): sender and recipient fields
  ruled as waybill lines, a node selector (the five offices),
  a weight stepper (0.5 kg steps, 0.5–20 kg), and the tally
  line in Special Elite: `PARCEL TO L4 — 2.0 KG × 260 = 520 —
  TRANSIT 22 DAYS`. The submit control is a heavy frank
  ("FRANK & DISPATCH"). A carbon copy of the completed waybill
  is the confirmation (§6.6's carbon grammar, here as a
  document): the same form, ghosted one line down, stamped
  "COPY — CARRIES WITH THE PARCEL."
- **Motion spec.** Trigger: input + submit. Weight steps tick
  the tally with §6.10's 90ms mini-press; the total recomputes
  per step from the record. On submit: the frank presses
  (140ms `--ease-stamp`), the sheet's carbon copy fades up
  beneath it offset by one line (400ms `--ease-post`), and
  the copy is stamped over 120ms. No wipe — freight paperwork
  is duplicated, not sent away; the original stays on the
  counter in front of you.
- **States.** Blank / drafting (tally live) / invalid (a
  field empty: the waybill prints "INCOMPLETE — THE PARCEL
  CANNOT TRAVEL WITHOUT AN ADDRESS" beneath the field, in
  ink, never red alone) / dispatching (frank pressed, 600ms)
  / dispatched (carbon copy stamped; the waybill number
  printed — sequential from the office's book, in the
  reference build № 041, being the forty-first waybill in a
  book whose count the confirmation itself states).
- **Content merge.** The waybill is the service, transacted:
  its rates are the record's, its transit figure is the
  record's, and its confirmation is the theme's own document
  type. A visitor who books a 2 kg parcel to L5 reads
  `2.0 × 275 = 550 — TRANSIT 24 DAYS` and has been told the
  whole truth of the purchase before paying anything.
- **Failure fallback.** No-JS: a plain form posting to a real
  endpoint; the tally prints the L4/1 kg default statically
  (260, 22 days) and the server confirms. Watchdog at 2000ms
  replaces a dead live-tally with the static default line, as
  §6.10 rules.
- **Reduced-motion variant.** No tick, no fade: the carbon
  copy appears printed beneath the original on dispatch.
- **Performance budget & mobile variant.** Input handlers
  only; negligible. Mobile: the waybill's two columns stack;
  the tally stays one unbroken line (it scrolls with the
  sheet if it must — figures never wrap mid-number).
- **Choreography timeline (v2).** Sheet arrives (§6.3) →
  fields filled (tally ticks per weight step; node change
  recomputes instantly) → frank press 140ms → 600ms dispatch
  hold (the clerk checks the form — a printed "CHECKING…"
  is refused; the hold is silent) → carbon copy fades 400ms
  → copy stamped 120ms → waybill number prints → rest:
  dispatched, with a "BOOK ANOTHER PARCEL" reply-slip that
  reprints the blank form below.
- **State matrix (v2).** *Rest:* blank waybill, default tally
  (L4, 1.0 kg, 260, 22 days — the hero's node as the office
  default). *Hover:* frank lifts 1px. *Focus:* blue rings on
  fields; the tally summarised for AT on blur, as §6.10.
  *Active:* frank press. *Scrolled-past:* a drafted waybill
  persists (cargo is never discarded). *Disabled:* the frank
  disables in the invalid and dispatching states, reason
  printed. *Touch:* the weight stepper's targets are 48px.
- **Breakpoints (v2).** ≥1200px: two-column waybill.
  768–1199px: two columns narrow. <768px: single column,
  office strip horizontal.
- **Edge cases & failure modes (v2).** *Over 20 kg:* the
  stepper stops and the sheet prints "OVER THE COUNTER LIMIT
  — FREIGHT OVER 20 KG TRAVELS BY ARRANGEMENT" (the Post has
  a heavier service; this form is not it). *Fractional
  weights:* steps are 0.5 kg and the tally always shows one
  decimal, so 1.5 × 260 = 390 prints exactly. *Node changed
  after dispatch:* impossible — the dispatched waybill locks
  its fields (a form that has travelled cannot be edited);
  booking another is the path.
- **Accessibility spec (v2).** Real form, real labels, the
  stepper is a native number input with step buttons as
  enhancement. Totals are text. The carbon copy is
  `aria-hidden` duplication; the confirmation's facts are
  announced once via a polite live region.
- **Tokens consumed (v2).** `--paper`, `--paper-deep`, `--ink`,
  `--blue`, `--red`, `--ease-stamp`, `--ease-post`,
  `--dur-tick` (90ms).

### 6.16 Frank-and-fold page transition

- **What & why.** Moving between pages franks, folds and
  slides the current page into an envelope wipe: the page is
  stamped with the destination's postmark, folds along its
  third, and slides away as the new page's letter slides out.
  It belongs because leaving a page here is posting it —
  every departure is franked with where you are going.
- **Structure.** A transition layer (an envelope graphic built
  from `--paper-deep` panels + a destination postmark overlay)
  inserted above the outgoing page. The fold is a CSS 3D fold
  on a wrapper (two panels, rotateX along the horizontal
  third) — the page itself is never transformed in a way that
  reflows its content; a static snapshot panel carries the
  visual while the real DOM swaps beneath.
- **Motion spec.** Trigger: navigation click on an internal
  link. Frank: destination postmark presses at the click
  point's nearest postmark corner (140ms `--ease-stamp`).
  Fold: panels close over 500ms `--ease-fold`. Wipe: the
  folded page slides down-out over 400ms `--ease-orbit` as
  the incoming page's masthead (§6.11) is revealed already
  printed. Total budget 1040ms; beyond 1200ms the transition
  is cut to a plain swap by the watchdog below.
- **States.** Idle / franking / folding / wiping / done /
  bypassed (external links, form posts, reduced motion,
  no-JS: normal navigation, untouched).
- **Content merge.** The frank names the actual destination
  node or page ("FOR L3 — 14 DAYS" on a route link; the
  page's own postmark on others) — the transition carries
  routing information, not branding confetti. A transition
  that says nothing about where you are going is decoration
  and is cut by §14 before anything else.
- **Failure fallback.** Watchdog at 1200ms from the click: if
  the incoming page has not committed, the layer is removed
  and the browser's own navigation proceeds — the transition
  can delay a departure by at most 1.2s and can never strand
  a visitor on a folded page. History/back bypasses the fold
  entirely (you do not re-frank a return).
- **Reduced-motion variant.** No transition: plain navigation.
  The destination postmark appears on arrival as part of the
  new page's own furniture instead.
- **Performance budget & mobile variant.** Snapshot panels
  are composited transforms: ≤0.5ms/frame for ~1s. Mobile:
  the fold is dropped; frank (140ms) + a 300ms envelope-edge
  slide only — small screens get the stamp, not the origami.
- **Choreography timeline (v2).** Click → frank presses
  0–140ms → fold 140–640ms → wipe 640–1040ms (new page
  commits beneath at ~700ms) → layer removes itself →
  incoming page's own arrivals (§6.3 ratchets already-read
  letters instantly) → rest. Watchdog deadline 1200ms.
- **State matrix (v2).** *Rest:* idle, layer absent. *Hover:*
  no pre-transition (hovering a link franks nothing — mail
  is franked when posted, not when considered). *Focus:*
  keyboard navigation triggers the same sequence on
  activation. *Active:* the sequence. *Scrolled-past:* n/a.
  *Disabled:* links mid-transition are inert (the layer
  captures clicks) for at most the watchdog's 1200ms.
  *Touch:* same as click.
- **Breakpoints (v2).** ≥1200px and 768–1199px: full
  frank-fold-wipe. <768px: frank + slide (see mobile variant).
- **Edge cases & failure modes (v2).** *Slow incoming page:*
  the fold completes and holds as a closed envelope with the
  destination postmark — a held letter, honest about waiting —
  until commit or the 1200ms watchdog forces plain
  navigation with the envelope removed. *Prefetch available:*
  the wipe shortens to 250ms. *Anchor links within the page:*
  no transition (you have not left the letter).
- **Accessibility spec (v2).** The layer is `aria-hidden`;
  focus moves to the incoming page's `h1` on commit as in
  normal SPA practice; the transition never traps focus and
  never hides the destination from AT — the link's own text
  already named it.
- **Tokens consumed (v2).** `--paper-deep`, `--ink`,
  `--postmark`, `--ease-stamp`, `--ease-fold`, `--ease-orbit`,
  `--dur-fold-page` (500ms).

### 6.17 Onion-skin handwriting loader

- **What & why.** Loading shows blank onion-skin gaining its
  handwriting in shimmer: a translucent sheet on which the
  coming content's letter-shapes ghost up gradually, as if
  written from the other side of thin paper. It belongs
  because in this theme content is correspondence — a page
  that has not arrived yet is a letter still being written,
  and the skeleton is that letter's other side.
- **Structure.** Skeleton sheets in the exact geometry of the
  content they precede (letter sheets, index rows, the
  waybill): `--onion` panels with line-shaped shimmer bands
  (a moving 8% ink gradient, 1600ms period) laid where the
  real text lines will sit, counted from the content's own
  structure — a letter skeleton has as many line bands as the
  letter has paragraphs' approximate lines, capped at 12.
- **Motion spec.** Trigger: any content fetch or route commit
  that takes >150ms. Shimmer sweeps at 1600ms per pass,
  `--ease-post` character (a gradient translation, nothing
  pulsing). Content replaces skeleton sheet-by-sheet as it
  commits — each sheet's real content arrives with §6.3's
  settle (180ms) — never a whole-page swap at once.
  Hard ceiling: 3000ms; at 3000ms whatever has not arrived is
  replaced by its §12 empty/error line, printed, and the
  skeleton retires.
- **States.** Unneeded (<150ms loads: never shown) / writing
  (shimmering) / arriving (per-sheet replacement) / retired
  (complete or ceiling-hit).
- **Content merge.** The skeleton is shaped by the actual
  incoming content's structure — it is the letter's reverse
  side, not a generic grey template. A skeleton that could
  belong to any page fails the anti-filler law even as a
  loading state.
- **Failure fallback.** The skeleton is itself the fallback's
  face; its own failure mode is staying too long, governed
  by the 3000ms ceiling and a 4000ms watchdog that force-
  prints the error line. No-JS loads show no skeleton (the
  server delivers content or an error, as it should).
- **Reduced-motion variant.** A still onion-skin sheet with
  the printed line "IN TRANSIT —" and the node's transit
  figure where known. No shimmer.
- **Performance budget & mobile variant.** Gradient
  translation on ≤3 sheets: ≤0.2ms/frame. Mobile: one sheet
  maximum in the skeleton (the first), the rest arrive as
  they commit.
- **Choreography timeline (v2).** t=0 request → 150ms grace
  (no skeleton for fast loads) → skeleton writes in (fade
  200ms) → shimmer passes 1600ms → sheets replace as content
  commits (180ms settles) → last sheet → skeleton retires →
  3000ms ceiling / 4000ms watchdog stand behind the whole
  sequence.
- **State matrix (v2).** *Rest:* absent. *Hover/focus:* the
  skeleton is inert and unfocusable. *Active:* n/a.
  *Scrolled-past:* skeletons below the fold are cancelled —
  the Post does not write letters nobody is waiting for.
  *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** All breakpoints: geometry mirrors the
  content's own breakpoint layout.
- **Edge cases & failure modes (v2).** *Partial failure (one
  sheet's fetch fails):* that sheet alone takes the error
  line; its neighbours arrive normally — a route with one
  lost letter is still a route. *Repeat visit (cached):*
  loads land under the grace period and no skeleton appears.
  *Very slow but alive:* the ceiling still applies — at
  3000ms the visitor gets the honest line and a retry
  reply-slip, not an eternal shimmer.
- **Accessibility spec (v2).** The skeleton region carries
  `aria-busy="true"` and a visually-hidden "Loading — mail in
  transit" status; shimmer is `aria-hidden`. Focus is never
  placed inside a skeleton.
- **Tokens consumed (v2).** `--onion`, `--paper`, `--ink-soft`,
  `--ease-post`, `--dur-shimmer` (1600ms).

### 6.18 Dead-letter footer & undeliverable 404

- **What & why.** The footer is the dead-letter office: the
  place undeliverable things end up, kept in good order —
  the route's third printing (all five nodes with their
  transit figures), the cargo total, the received tally, the
  parcel's status line, and the office's own small print. The
  404 is its sibling: a letter that could not be delivered,
  returned to sender with the reason stamped on it. It
  belongs because a postal theme's footer is not a sitemap
  with a newsletter box; it is where the route accounts for
  everything, including what never arrived.
- **Structure.** An `--ink` footer (cream text, 7.65:1) in
  three columns: the route reprinted (nodes + days, Special
  Elite); the page's account — `WORDS CARRIED ON THIS PAGE:
  1,159` (the §13 total), `RECEIVED BY YOU: n OF 5` (from
  §6.9's flags), `ONE PARCEL STILL IN TRANSIT — L5, DAY n OF
  24` (the day read from §6.4's counter); and the office
  column (the Post's address written as a routing instruction,
  the §11 small print links). The 404 page is a single
  returned envelope: the requested address struck through
  (the strike never deletes, §12), a red-ink stamp
  "UNDELIVERABLE AS ADDRESSED", and the three likeliest
  destinations offered as a reply-slip.
- **Motion spec.** Trigger: scroll into view. The footer's
  route reprint draws its rule line over 600ms `--ease-orbit`
  as the footer centres; the tallies are printed, not counted
  (the counting happened on the journey, §6.4). The 404's
  stamp presses once on load (120ms `--ease-stamp`) — the
  office has already handled this letter before you arrived.
  Footer choreography is specified as nearly none beyond the
  rule: accounts are stated, not performed.
- **States.** Footer: printed / accounted (tallies filled
  from session state) / fresh (no letters stamped yet:
  `RECEIVED BY YOU: 0 OF 5` — printed honestly, never hidden).
  404: returned (the only state).
- **Content merge.** Every footer figure is a second or third
  printing of a number already established above — the route
  (record §6.13, chart §6.5, footer here), the cargo (§6.4,
  §13), the parcel (§6.6). The footer is where the page's
  arithmetic is audited by the visitor, and §10 audits it
  first.
- **Failure fallback.** Static HTML; session-derived tallies
  fall back to their fresh-state printings if storage is
  unavailable. The 404 works with no JS at all (its stamp is
  printed in the markup; the press is enhancement).
- **Reduced-motion variant.** The rule prints undrawn; the
  404 stamp is printed, unpressed.
- **Performance budget & mobile variant.** One 600ms line
  draw; zero thereafter. Mobile: columns stack — route,
  account, office — in that order; the account never drops
  below the office column (the numbers outrank the address).
- **Choreography timeline (v2).** Footer centres → rule
  draws 600ms → tallies already printed → the parcel (§6.6)
  is beside the footer in its margin orbit, still tumbling →
  end of page. 404: load → stamp presses at 300ms → the
  reply-slip destinations rest → nothing else moves.
- **State matrix (v2).** *Rest:* printed footer / returned
  404. *Hover:* footer links underline (ruled line, §6.11's
  grammar). *Focus:* blue ring — on ink, the ring is cream
  (blue on ink is a forbidden pairing, §2). *Active:* links
  follow (§6.16 transition). *Scrolled-past:* n/a (it is the
  end). *Disabled:* n/a. *Touch:* tap targets 44px.
- **Breakpoints (v2).** ≥1200px: three columns. 768–1199px:
  two columns (account merges under route). <768px: stacked,
  order preserved.
- **Edge cases & failure modes (v2).** *A page with different
  letters:* the cargo total is computed from that page's own
  letters (§13's method) — a footer that prints 1,159 on a
  page carrying 800 words fails §10. *Zero letters received:*
  printed as 0 OF 5 (see States) — the account does not
  flatter. *The 404 for a retired node:* the reply-slip
  offers the surviving route and says the office closed —
  the strike-never-deletes rule applies to destinations too.
- **Accessibility spec (v2).** Footer is a real `<footer>`
  with labelled columns; cream on ink 7.65:1 throughout; the
  404's stamp text is real text (not an image), its heading
  is the plain fact ("This address could not be delivered")
  with the postal theatre as styling around it.
- **Tokens consumed (v2).** `--ink`, `--paper`, `--red`,
  `--blue`, `--ease-orbit`, `--ease-stamp`, `--dur-rule`
  (600ms).

## 7. Page application map

- **Home.** The full route as specified: hero letter from L4
  (§6.1–6.2), letters L1–L5 (§6.3) carrying services, story
  and evidence in that order, the record (§6.13) after L2,
  the chart (§6.5) after the record, rate card (§6.14) after
  L4, telegram (§6.10) as the final letter, dead-letter
  footer (§6.18). The counter (§6.4) rides the rail
  throughout; the parcel (§6.6) rides the margin.
- **Listing / archive.** The mail index (§6.12) is the page:
  drawers by node and season, each row a letter with true
  figures; the masthead's route index (§6.11) filters by
  node. No hero envelope — archives are entered, not
  delivered to.
- **Detail (a single letter).** The letter at full measure
  with its stamp frame plates (§6.7), its own postmark, and a
  reply-slip at its foot linking the next letter on the route
  (the route order is the reading order). The counter shows
  this letter's node figures only.
- **About / the office.** Written as the Post's own letter to
  the visitor (Newsreader throughout, Franklin only for the
  office's printed headings) with the record (§6.13) embedded
  as the office's charter — the numbers the office holds
  itself to.
- **Contact.** The telegram (§6.10), alone on the page with
  the warning. Nothing else competes with it.
- **Booking / freight.** The waybill (§6.15) with the rate
  card (§6.14) printed above it — price before paperwork,
  always.
- **Checkout equivalents.** There is no cart. Payment, where a
  build needs it, happens off-theme at the franked boundary
  (§6.16 carries the visitor out stamped "FOR THE COUNTER"),
  because the Post's forms end at dispatch; pretending a
  payment gateway is a waybill would break the law's spirit.
- **404.** The returned envelope (§6.18).

## 8. Worked examples

### 8.1 The hero — a letter from L4 (load timeline)

The visitor arrives. First paint shows the masthead printed
(§6.11) and the hero letter open in the DOM — nothing is
hidden. JS arms within 300ms: the letter folds into the
envelope's start, the dotted trajectory strokes across the
hero over 1600ms, and the envelope travels it over 2400ms
`--ease-orbit`, slowing visibly as it nears the headline, and
parks at a 4° tilt beside it. At 2800ms the postmark presses
at exactly −6° — "RECEIVED — L4 — 22 DAYS IN TRANSIT" — the
22 read from §6.13's L4 row. The flap folds (500ms), the
letter slides out, pauses, unfolds: Franklin headline "The
far harbour writes home.", Newsreader body of 212 words from
the L4 harbour office, the stamp frame in its corner carrying
denomination 55 (L4 letter postage). The transit counter
ticks its cargo figure 0 → 212. The reply-slip at the letter's
foot reads "REPLY BY TELEGRAM —" and routes to §6.10. Total
performance: ~3.4s, every millisecond of it skippable by
simply scrolling — the letter is open in the DOM either way,
and a visitor who scrolls at t=1s finds it open below.

### 8.2 Mid-page — the chart and the price of going (scroll timeline)

The visitor has received the L1 letter (148 words; counter:
2 days, 5 SEC, cargo 360) and the L2 letter (176 words; 3
days, cargo 536). The record's sheet arrives (§6.13) — the
whole route priced in one table. Then the `--night` chart
panel centres and pins (140vh): arcs draw over 1800ms, nodes
stamp in gold, L3's caption printing "301M KM — SIGNAL 17 MIN
— 14 DAYS." Below the chart, the L3 letter arrives ("The Long
Night," 203 words; counter scrubs 3 → 14 days, cargo 739).
Further down, the rate card (§6.14) prints its worked example
in full view: "ONE LETTER AND ONE PARCEL, 2 KG, TO L4 —
LETTER 55 + PARCEL 2 × 260 = 575 — IN TRANSIT 22 DAYS." Every
figure in that line is §6.13's L4 row and one multiplication a
visitor can check against the table they scrolled past a
minute earlier. That checkability is the section's design.

### 8.3 Conversion — fourteen words to L4 (submit timeline)

The final letter is the telegram sheet (§6.10), warning
printed at its head: "CHARGED BY THE WORD. LIGHT-TIME DELAY:
22 DAYS. CHOOSE WORDS AS CARGO." The destination office is L4
by default. The visitor writes: "ARRIVING HARBOUR WINDOW
OPENS MARCH NINTH HOLD TWO BERTHS CONFIRM BY RETURN POST"
— fourteen words. The tally ticks per word and settles:
`WORDS: 14 — POSTAGE: 14 × 5 = 70 — LIGHT-TIME DELAY: 22
DAYS`. The frank's denomination corner shows 70. On send, the
frank presses (140ms), the sheet folds and wipes (§6.16's
grammar, 900ms total), and the confirmation slip arrives
printed with the same fourteen words, the same 70, and the
delivery line computed from the record: "TO BE DELIVERED AT
L4 — 22 DAYS FROM POSTING." Nothing in the confirmation
introduces a number the form did not already show. The
visitor has been charged attention by the word, warned in
advance, and quoted exactly — the theme's conversion is a
kept promise, performed.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The instant arrival.** Letters that fade up in place like
   web cards. Cure: everything arrives along the route
   (§6.3) or is printed delivered; there is no third state.
2. **The rounded delay.** "About three weeks" for L4. Cure:
   the record says 22 days; the page says 22 days, everywhere,
   in every printing (§6.13's audit).
3. **Gold body text.** Denomination gold set as prose at
   2.23:1. Cure: gold is metal — foil, rings, large numerals;
   its one lettering licence is the night chart (§2).
4. **The level postmark.** A postmark set straight reads as a
   UI badge. Cure: seeded angles −7° to −3°, hero exactly −6°
   (type law 4).
5. **Dashed-border perforations.** A stamp frame with a CSS
   dashed border is a coupon. Cure: true radial-gradient dot
   masks (§6.7) or the plain fallback border — never dashes.
6. **Clip-art space.** Rockets, planets and starfields pasted
   behind the mail. Cure: the theme's space is a chart —
   nodes, arcs, one route line (§6.5). The sky is a document.
7. **The delivered parcel.** A build that lands §6.6's parcel
   at the footer "for delight." Cure: it never arrives; the
   footer prints its status instead (§6.18). The gate checks.
8. **Invented nodes.** An L6 added for a sixth section. Cure:
   there are five Lagrange points; a page needing six
   sections writes two letters from one node (§7) or chooses
   another theme.
9. **Live-tracking cosplay.** A map with a moving dot and an
   ETA countdown. Cure: this Post publishes transit days, not
   tracking; the counter (§6.4) counts the journey you are
   reading, not a vehicle's telemetry.
10. **Franklin in a letter.** Office type inside correspondence.
    Cure: type law 1 — letters are Newsreader, whole and only.
11. **The hidden delay.** Transit figures in fine print while
    the hero promises the stars. Cure: the hero's own postmark
    carries the 22 days (§6.1); the law (§1) is structural.
12. **Stock-photo stamps.** Generic landscape photos in the
    stamp frames with random denominations. Cure: plates are
    the node's own postcards, captioned as messages, priced
    from the record (§6.7).
13. **The chat bubble.** A floating "usually replies in
    minutes" widget in the corner of a 22-day postal service.
    Cure: contact is the telegram (§6.10), with its delay
    printed on it. If a build needs support, the support
    answer arrives by post and says so.
14. **The averaged route.** "Delivery in 2–24 days" in a
    summary line. Cure: the Post publishes per-node figures
    or none (§6.13); a range that hides L5's twenty-four
    behind L1's two is the rounded delay (§9.2) wearing a
    table's clothes.

## 10. Quality gate

Blocking checks — all must pass before this theme ships in a
build:

1. **Figure audit.** Every number on the page (postmarks,
   counter, chart captions, denominations, tallies, rate card,
   worked examples, footer) is grepped and matched against
   §6.13's record. One unmatched figure fails the build.
2. **Three-printings test.** The route's figures agree in the
   record, the chart and the footer; the cargo total agrees
   in §6.4, §13 and §6.18.
3. **Delivered-by-default test.** With JS disabled, every
   letter is open, every figure printed, the chart drawn, the
   forms submittable. Nothing is in transit on screen.
4. **Watchdog drill.** With the shared loop artificially
   stalled, each element reaches its delivered state inside
   its stated deadline (envelope 2600ms, letter 4000ms, chart
   3000ms, letters 2000ms, transition 1200ms, skeleton
   4000ms).
5. **Reduced-motion pass.** The full page with
   `prefers-reduced-motion`: all mail delivered and open, no
   pin, no tumble, no shimmer, figures identical.
6. **Postmark audit.** Every postmark on the page sits between
   −7° and −3° (hero −6° exactly); none is level; none
   overlaps body text.
7. **Contrast audit.** Body ink on paper (7.65:1); no text in
   gold on paper; no blue or red on ink; gold lettering only
   on `--night`; red never the sole carrier of a meaning.
8. **Parcel check.** §6.6's parcel is en route at the footer;
   the footer's status line prints its node and day; no build
   artefact delivers it.
9. **Perforation check.** Stamp frames use the dot mask (or
   the plain fallback); a dashed border anywhere fails.
10. **Cursor check.** The system cursor is unchanged
    everywhere; no element substitutes a pointer.
11. **Cargo arithmetic.** Each letter's printed word count is
    its true count (script-verified against the DOM text);
    the cumulative figures in §6.4/§13 follow.
12. **Form honesty.** The telegram and waybill tallies
    recompute from the record for every node and a sample of
    inputs (14 words to L4 = 70; 2 kg to L5 = 550; 1.5 kg to
    L4 = 390), and their no-JS fallbacks post successfully.

## 11. Component inventory

Every component a real Lagrange Post site needs, with its
themed treatment. Anything not listed does not get invented
in another theme's clothes.

- **Buttons.** Primary: the frank — a `--paper-deep` stamp
  block, Franklin label, denomination corner where a cost
  exists; presses per §6.9. Secondary: the reply-slip — a
  ruled line with a Franklin label, underline draws on hover.
  There is no third button style.
- **Links.** Inline: ink with a `--blue` underline. In the
  route index and footer: ruled-line hover (§6.11).
- **Inputs.** Ruled waybill lines — bottom rule only, ink;
  focus thickens the rule and adds the blue ring at the
  field's start. Labels in Special Elite above the line.
- **Textarea.** The telegram blank (§6.10): ruled lines at
  the body's line-height, Newsreader text.
- **Selects / radios.** Office selectors: the five nodes as
  radio postmark tabs (§6.10, §6.15). Native `<select>` is
  refused — a destination is chosen from the chart, not a
  dropdown.
- **Tables.** The record (§6.13) and the mail index (§6.12):
  ledger rules, Special Elite figures, sticky first column
  on small screens.
- **Cards.** Index cards (§6.12) and stamp frames (§6.7) are
  the only card forms. Generic content cards do not exist.
- **Badges.** One only: the received mark (§6.9). Status
  badges in colours are refused — status is printed in words.
- **Alerts.** A postmark-style notice block (ink ring,
  Special Elite line, Newsreader explanation). Errors per
  §12's voice. No toast — see below.
- **Pagination.** By season, as printed index dividers in
  §6.12 ("SEASON OF THE LONG NIGHT — 14 LETTERS"). Infinite
  scroll is refused: a drawer can be emptied.
- **Modals.** Refused. Anything that would be a modal is a
  letter overlay on onion-skin (§6.17's material) that
  arrives as its own sheet — or, more often, its own page.
- **Toasts.** Refused, with replacement: confirmations are
  documents (the telegram slip §6.10, the carbon copy §6.15)
  that stay where they were issued.
- **Tabs.** Refused, with replacement: the route index
  (§6.11) — destinations are places, and places are not tabs.
- **Accordions.** The office's small print (§6.14's
  conditions, §6.18's office column) may fold as a letter
  folds — a printed "CONDITIONS —" line expanding the sheet.
  Nothing else accordions.
- **Progress.** The transit counter (§6.4). Progress bars and
  spinners are refused (§5, §6.17).
- **Search.** The archive's search is a sorting-office query
  slip in the index header (§6.12): one ruled input, results
  re-filed beneath it. No overlay search.
- **Breadcrumbs.** The route itself: "EARTH — L2 — THIS
  LETTER" in Special Elite at a letter's head. On a route
  theme, the breadcrumb is the journey so far.
- **Footer.** The dead-letter office (§6.18).
- **404.** The returned envelope (§6.18).

## 12. Content & copywriting voice

Two registers, kept apart as strictly as the type laws:

- **The Office** (Franklin / Special Elite; terse, printed,
  uppercase for labels): anything the Post states officially —
  postmarks, rates, warnings, tallies. The Office does not
  persuade; it publishes. Headline style for office surfaces:
  short declaratives — "THE ROUTE RUNS IN ALL SEASONS." —
  never a question, never an exclamation.
- **The Correspondence** (Newsreader; warm, specific, first
  person from the node): the letters. A letter's headline is
  a line from the letter, not a marketing claim — "The far
  harbour writes home." Letters mention weather, work and
  waiting; they never mention the website.

Fixed strings (verbatim, never paraphrased):
- "CHARGED BY THE WORD. LIGHT-TIME DELAY: 22 DAYS. CHOOSE
  WORDS AS CARGO."
- "RECEIVED — L4 — 22 DAYS IN TRANSIT"
- "ONE PARCEL STILL IN TRANSIT."
- "UNDELIVERABLE AS ADDRESSED"
- "NO MAIL FOR L3 THIS SEASON — THE ROUTE STILL RUNS."

Error voice — the Office, honest, with the remedy:
✓ "UNDELIVERABLE AS ADDRESSED — CHECK THE NODE AND TRY AGAIN."
✗ "Oops! Something went wrong."
✓ "A TELEGRAM OF NO WORDS CARRIES NOTHING."
✗ "This field is required."
Label style: labels name the postal object, never the UI
object — "DESTINATION OFFICE", not "Select destination";
"WORDS", not "Character count" (words are the unit of cargo;
characters are free and the form does not pretend otherwise).
Headline pairs, for calibration:
✓ (Office) "THE ROUTE RUNS IN ALL SEASONS."
✗ (Office) "Blast off to savings with our stellar plans!"
✓ (Correspondence) "The harbour holds station through the
long night, and the garden you asked about has taken."
✗ (Correspondence) "We're super excited to share our journey
with you!!"
The second ✗ fails on three counts the gate can name: the
Office's exclamation in a letter's register, the banned
excitement, and news about the website inside correspondence.

Empty states are printed facts, not apologies (the L3 line
above). Numbers in copy follow the record exactly; the words
"fast", "instant", "real-time" and "seamless" are banned from
the theme's vocabulary in either register — the Post's whole
voice is that some things take twenty-two days and are worth
them.

## 13. Full-page scroll choreography map

The reference home page, beat by beat. Cargo figures are the
letters' true word counts, cumulative, as §6.4 displays them.

1. **Load.** Masthead prints; masthead postmark presses at
   400ms; hero trajectory strokes (1600ms); envelope travels
   and parks (2400ms); postmark stamps −6° (2800ms); flap
   folds, letter opens (3000–4900ms). Cargo 212.
2. **Hero rest.** Envelope drifts ±3px; parcel fades into its
   margin orbit; counter plate shows L4's figures from the
   hero's own arrival (22 days — the hero came the long way).
3. **L1 leg.** Route line draws into the rail; the L1 letter
   travels and settles; counter scrubs to 2 days / 5 SEC;
   cargo 360. The journey out begins at the bottom of the
   counter's range — patience is being taught by arithmetic.
4. **L2 letter.** Settles; 3 days; cargo 536.
5. **The record.** Its sheet settles; rows file 40ms apart.
   The visitor now owns the table every later figure quotes.
6. **The chart.** `--night` panel pins (140vh); arcs draw
   (1800ms); five nodes stamp in gold; date line begins its
   idle cycle. The counter holds — the chart is a room, not
   a leg.
7. **L3 letter.** The long leg: counter scrubs 3 → 14 days,
   signal 17 MIN; cargo 739. The transit gap before this
   sheet is the page's widest (§4).
8. **L4 letter.** 22 days; 8 MIN; cargo 970. The hero's
   postmark figure returns as a destination — the route has
   come full circle.
9. **Rate card.** Arrives with its section; its worked
   example (55 + 2 × 260 = 575) printed under the L4 letter
   it prices.
10. **L5 letter.** The far terminus: 24 days; cargo 1,159 —
    the counter's complete state.
11. **Telegram.** The final letter is the form; the visitor
    writes, the tally ticks, the frank waits.
12. **Footer.** The dead-letter office: rule draws (600ms);
    route reprinted; account printed (1,159 words; received
    n of 5; parcel still in transit, L5). The parcel tumbles
    beside it. End of route.

Reverse pass: scrolling up, everything holds its arrived
state (ratchets in §6.3, §6.4); the only motion is the
parcel's tumble and the envelope's drift — the two licensed
ambient loops. Jump scroll: letters above the landing point
arrive instantly, the counter jumps to the landed node's row,
and the landed letter plays its settle once.

## 14. Whole-page performance budget

- **Page weight:** ≤780KB total for the home page (plates and
  the chart are inline SVG; the three font families subset to
  the page's glyphs, ≤180KB combined; no framework, no image
  library — stamp plates are the only raster assets, ≤90KB
  each, ≤4 per page).
- **Frame budget:** the shared loop's worst frame (chart draw
  + a letter settling + counter scrub) ≤1.6ms; steady-state
  frames ≤0.6ms (parcel + drift only). Long tasks: none over
  50ms; the trajectory's path lookups are precomputed at arm
  time.
- **Loop discipline:** one rAF loop, lerp 0.085, idling when
  nothing is scrubbing and the hero/chart are off-screen;
  ambient loops are CSS where possible (drift, shimmer) so
  the loop can sleep.
- **Measurement:** the budget is checked on a mid-range
  Android over throttled 4G, not on the build machine: first
  paint of the delivered page (step 2 of §15) under 1.8s, the
  hero sequence armed by 300ms after first paint, and the
  loop's frame cost sampled across the chart pin — the page's
  busiest 140vh — rather than at rest, where everything is
  cheap and nothing is proven.
- **Cut order when over budget:** (1) §6.16's fold (keep the
  frank); (2) chart pin (draw without pinning); (3) stamp
  scale-press (print denominations only); (4) parcel
  precession (keep the tumble); (5) parallax depths (letters
  still arrive). **Never cut:** the watchdogs, the delivered
  DOM states, the record's printing, the reduced-motion
  variants, the counter's figures. A Lagrange page that is
  fast because its mail can be lost has cut the wrong thing.

## 15. Build-order checklist

1. Print the route record (§6.13) as data + table; freeze the
   figures. Nothing else is built on unfrozen numbers.
2. Build the static, delivered page: masthead, all letters
   open, chart drawn, footer accounted — fully readable with
   no JS. This is the product; everything after is travel.
3. Stamp frames (§6.7) and postmark construction (angle seeds,
   `--postmark` rendering) as shared primitives.
4. The route line + letters' arrived geometry (§6.3), then
   the shared loop and the scrub.
5. Transit counter (§6.4) reading the record from the DOM.
6. Hero sequence: trajectory, envelope, postmark, opening
   letter (§6.1–6.2) with watchdogs armed before the
   animation is allowed to hide anything.
7. Chart draw + pin (§6.5).
8. Parcel (§6.6) and ghost postmark (§6.8) — the two light
   touches, after the heavy mechanics stand.
9. Stamp-down (§6.9) + footer tallies (§6.18) sharing the
   received-state store.
10. Mail index (§6.12), rate card (§6.14).
11. Telegram (§6.10) and waybill (§6.15) with live tallies,
    then their no-JS fallbacks tested by disabling JS.
12. Transition (§6.16) and skeleton (§6.17).
13. Reduced-motion pass across every element; delivered
    states compared side-by-side with the step-2 static page.
14. §10 gate, run by someone who did not build the page;
    figure audit by grep, watchdog drill by loop-stall.
15. Sign-off recorded with the record's figures printed on
    the sign-off itself — the gate signs the numbers, not
    just the look.
