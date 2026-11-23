# 44. Hammam — Expanded (v1 + v2)

> Expansion of theme #44 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same two typefaces, the same ten signature elements —
> deepened, never redesigned — plus eight page-family elements.

## 1. Concept & world

Most websites are read at one temperature. This one is **bathed
through**. The page is a bathing ritual in five chambers: the visitor
enters through steam, passes through warm marble rooms, rests in a
middle chamber where almost nothing is asked of them, rinses in cool
water, and ends — if they mean to book — in the cold plunge. The
scroll is the ritual's procession. Colour temperature, text density,
scroll resistance and even the sharpness of the rendering all follow
the chamber the visitor is standing in: languid and vapour-soft in the
steam room, spare and silent in the tepid room, hard-edged and instant
in the plunge. Sections are not stacked cards; they are **chambers**,
each announced by an attendant's label carrying its temperature and a
ritual instruction, each entered through an arch, each with its own
air.

The world is the bathhouse, treated as a complete interface vocabulary
rather than a spa mood-board. The page has **chambers** (the five
sections, in fixed ritual order), **the slab** (the göbek taşı, the
heated central marble of the hero, on which the headline rests),
**attendants** (the labels, instructions and navigation that announce
each room and never hurry), **the thermometer** (the margin instrument
with five notches that measures the visitor's own progress through
the ritual), **steam** (the threshold substance — every transition,
entrance and reveal passes through it, and it always clears), and
**the plunge** (the final chamber, where the booking lives, rendered
with a crispness the warm rooms never attempt). Nothing on the page is
fog clip-art or turquoise spa stock. The bathhouse is the information
architecture: **temperature is the page's argument about pace**, and
the argument is performed by the scroll itself — warm content is
lingered over, the middle is rested in, and the ask, when it comes,
is cold, clear and quick.

**The theme's one law: steam is a threshold, never a wall.** Every
vapour layer on the page — the hero's emergence (§6.1), the chamber
wipes (§6.2), the condensation on a card (§6.8) — is an overlay above
content that is fully rendered beneath it from first paint, and every
vapour layer carries a hard clear time: **no steam may hide content
for longer than 3000ms**, enforced by watchdog, not by hope. The
corollary is the temperature rule: **every temperature printed on the
page is the chamber's own declared temperature**, taken from the
ritual object (§6.4) that also drives the thermometer, the chamber
labels and the footer record — one set of five numbers, printed three
ways, never decorated, never rounded for effect, never invented for a
page that has no chamber to belong to. A Hammam build whose steam
lingers, or whose "42°" appears beside content that is not the steam
room, has not bent the theme — it has fogged a corridor and called it
a bathhouse, and the quality gate (§10) fails it on sight. Everything
else in this theme is craft. That one is house discipline.

**The ritual is the interaction model.** The visitor's acts are a
bather's acts: they are announced into each room (§6.11), they clear
the condensation from a treatment to read it (§6.8), they warm what
they choose with a pour (§6.9), they rest where resting is the content
(the tepid chamber, §8.2), and when they finally commit, they plunge
(§6.10, §6.14) — no fade, no ceremony, cold water. The site does not
have users converting through a funnel; it has bathers completing a
ritual whose last step happens to be a booking. That is why the theme
fits services that are genuinely sequential and sensory — bathing,
treatment, retreat, tasting, therapy, any offering whose value is in
the order and the pacing — and why it curdles around anything that
must be scanned, compared in a table, or bought in a hurry.

**Best-fit sites and audiences.**

- Bathhouses, hammams, onsen, spas and thermal resorts — the literal
  world: a real sequence of rooms at real temperatures, bookable at
  the end.
- Treatment and therapy practices with a genuine session arc:
  massage, float tanks, sauna circuits, breathwork, physiotherapy —
  where the service is a progression and the first visit needs
  explaining as a ritual, not a price list.
- Retreats and slow hospitality: ryokan, riads, bath-hotels, silent
  retreats — stays sold as a sequence of states rather than a list of
  amenities.
- Tasting and ceremony: tea houses, hammam-style coffee rituals,
  omakase and tasting-menu restaurants with a fixed procession of
  courses — chambers become courses, temperatures become serves.
- Wellness products with a ritual protocol: bathing salts, sauna
  goods, cold-plunge equipment — where the product page can walk the
  protocol the product is used in.

**When NOT to use it.**

- For comparison content. Five pinned chambers are a procession, not a
  grid; a visitor who needs to compare twelve prices side by side is
  being walked through steam to reach a spreadsheet. Choose another
  theme.
- For urgent transactions. The ritual is paced — chambers pin, steam
  takes its 3 seconds at the door, the plunge must be reached. A
  visitor renewing insurance should not bathe first.
- Where the sequence is invented. If the business has no real ordered
  ritual — no rooms, no courses, no protocol — the chambers are
  theatre and the temperatures are lies (§1's law). A single-page
  portfolio in five "chambers" is a corridor with delusions.
- For audiences who must not be asked to scroll far. The plunge is the
  point; a page whose readers will only ever stand in the steam room
  has spent its whole design on a doorway.
- For content that changes daily. Chambers are architecture: moving
  the booking out of the plunge or adding a sixth room is a rebuild,
  and the build should treat it as one.

## 2. Palette

Five anchors, inherited unchanged. The palette is a bathhouse read in
section: vapour, marble, stone, slate, deep water — in the order the
bather meets them. Nothing else is admitted; every other colour on
the page is one of these five, tinted, shaded, or set at an opacity
over its own chamber.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--steam` | `#EFE9E1` | Steam white: the vapour layers, the steam room's ground, the page's lightest air | ~26% of pixels | Plunge on it: **10.06:1** (AAA). Ink on it 11.80:1. It is the only ground the steam layers themselves may be built from — steam is this colour at opacity, never a grey. |
| `--marble` | `#D8CFC2` | Warm marble: the warm and tepid chambers' ground, card grounds, the slab | ~30% of pixels | Ink on it **9.23:1** (AAA); plunge on it 7.87:1. Stone on it is 2.15:1 — stone never letters marble (see pairing law). |
| `--stone` | `#9A8B76` | Stone: arch keystones, thermometer body, vein branching, apparatus rules, disabled marks | ~10% of pixels | On steam 2.75:1, on plunge 3.66:1 — **graphical and ≥24px display only, never text** on any ground. Its darkened derivative `--stone-deep` carries small text on light grounds. |
| `--slate` | `#4E5A5A` | Cool slate: the cool chamber's ground, secondary apparatus in cold rooms | ~14% of pixels | On steam **5.93:1** (AA) — slate may letter light grounds; steam on it 5.93:1 — it may carry steam-white body text at ≥16px. On plunge 1.70:1 — slate and plunge never pair as text/ground. |
| `--plunge` | `#1F3A3D` | Plunge deep: the cold chamber's ground, the footer, display type on light grounds | ~20% of pixels | Steam on it **10.06:1** (AAA); steam-dim on it 8.11:1. The darkest water on the page; nothing darker is admitted except `--plunge-ink` for the footer's floor. |

**Derived tokens (closed list — no others may be introduced).**

| Token | Hex / value | Derivation & use |
|---|---|---|
| `--ink` | `#2E2A26` | Plunge deep warmed toward stone and darkened: body text on steam and marble. On steam **11.80:1**, on marble 9.23:1. |
| `--stone-deep` | `#6B5B45` | Stone darkened for lettering: captions, apparatus and secondary text on light grounds. On steam **5.43:1** (AA); on marble 4.25:1 — ≥14px bold or ≥18px only on marble. |
| `--steam-dim` | `#DCD2C2` | Steam shaded: secondary text and captions on plunge. On plunge **8.11:1** (AA). |
| `--plunge-ink` | `#152A2D` | Plunge darkened: the footer floor and the plunge chamber's deepest band. Steam on it ≈12.4:1. |
| `--ember` | `#C79A5F` | Stone warmed toward lamplight: the warm pour's glow (§6.9) and the one licensed warm accent in cold rooms. On plunge 4.75:1 — may letter the plunge at ≥18px; on steam 2.12:1 — never text on light grounds, glow only. |
| `--vapour` | `rgba(239,233,225,.88)` | Steam white at 88%: every steam layer (§6.1, §6.2, §6.16). Decorative-threshold only; content beneath must meet contrast with the vapour removed — and removed is its guaranteed state (§1's law). |
| `--mist` | `rgba(78,90,90,.28)` | Slate at 28%: the cool chamber's thin haze and the plunge's surface breath. Graphical only; the plunge's text never sits under it (§6.10). |

**Dark-mode behaviour: the bathhouse does not invert — it is read by
lamplight.** The chambers already run from light vapour to deep
water; there is no light scheme to flip to. Under
`prefers-color-scheme: dark`, the two light chambers change their
hour, not their nature: the steam room and warm room grounds deepen
one step — `--steam` → `#E4DCCC`, `--marble` → `#C9BCA6` — as if the
same rooms were visited in the evening, ink text holds (contrast
rises), and the steam layers take `--vapour` at .92 so the vapour
still reads against the deeper ground. The tepid, cool and plunge
chambers are unchanged: slate at dusk is slate. A build that inverts
the plunge chamber to a pale ground has drained the pool, and §10
fails it.

**Pairing law.** Body text is ink on steam and marble; steam on
plunge and plunge-ink; steam on slate at ≥16px; slate on steam.
Display type is plunge on light grounds, steam on dark. Stone is
never text. Ember letters only the plunge, at size. Any other pairing
is a build error, not a variation.

## 3. Typography

Two typefaces, inherited unchanged. **Cormorant** is the house's
ceremonial voice — tall, fine, unhurried — and sets chamber names,
headlines, ritual instructions and the plunge's confirmation. It is a
delicate face and the theme treats it as one: Cormorant never sets
below 20px, never sets body copy, and never sets a paragraph — it
announces, it does not explain. **Alegreya Sans** is the working
voice and sets body text, labels, form fields, errors and all prose.
Temperatures, durations and prices are set in Alegreya Sans 600 with
`font-variant-numeric: tabular-nums` — the attendant's ledger figures,
read off an instrument, not carved on a slab. There is no third
typeface; emphasis inside Cormorant is size, inside Alegreya Sans is
weight or italic.

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Chamber name | Cormorant 500 | 44–68px / 1.04, `clamp(2.75rem, 6vw, 4.25rem)` | +0.01em | Set with its temperature and instruction as one announcement (§6.11's grammar): name, then "38°", then the instruction in Alegreya italic. A chamber name without its temperature is an unannounced room. |
| Display / hero headline | Cormorant 500 | 56–92px / 1.0 | starts −0.005em, condenses to −0.04em (§6.1) | The condensing headline. Never more than 2 lines; a headline that needs 3 lines is two headlines. |
| Treatment title | Cormorant 500 | 26–32px / 1.12 | 0 | The treatment's name as the attendant gives it: the rite, then its duration in the ledger figures. |
| Heading (in-chamber) | Cormorant 500 | 28–36px / 1.1 | 0 | One per chamber region; headings do not cross chamber boundaries. |
| Body | Alegreya Sans 400 | 17–19px / 1.65 | 0 | Measure 56–64ch. In the tepid chamber, body text is rationed to the §4 emptiness law. On slate, 17px minimum — the 5.93:1 pairing earns AA at size. |
| Ritual instruction | Alegreya Sans 400 italic | 16–18px / 1.5 | 0 | The attendant's spoken line under each chamber name ("Stay here a while."). Italic is the house's spoken register — it is never used for emphasis in body copy. |
| Apparatus (temperatures, labels, thermometer) | Alegreya Sans 600 | 11–13px, uppercase | +0.16em | Chamber labels, notch names, durations. Uppercase is rationed to apparatus only. Temperatures always carry the degree mark and always come from the ritual object (§6.4). |
| Price (plunge) | Alegreya Sans 600 | 20–24px / 1.2, tabular | 0 | Set in steam on plunge; the price is stated in the cold, plainly, like the temperature. |

**Type laws.**

1. **Every chamber is announced before it is read.** Name,
   temperature, instruction — in that order, before any prose. A
   chamber that begins with a paragraph has let the bather wander in
   unannounced.
2. **Cormorant announces; Alegreya explains.** If a line must be read
   twice to be understood, it is prose wearing ceremonial dress —
   demote it. If a label must be scanned at arm's length, it is
   apparatus wearing prose — promote it.
3. **The warmer the chamber, the looser the type.** Line-height and
   letter-spacing ease with heat: steam room body 1.7, warm 1.65,
   tepid 1.6, cool 1.55, plunge 1.5 with tracking at 0. Reading itself
   cools and tightens as the ritual descends.
4. **Figures are readings.** Any number the page asserts (temperature,
   duration, capacity, price) is set in Alegreya Sans tabular and is
   subject to §1's law: taken from the ritual object or traceable to
   the house's real published data.
5. **No centred body text.** The slab may centre its headline; chamber
   prose is left-aligned like a attendant's list on a door. Centred
   paragraphs in the plunge are a gate failure.


## 4. Layout language

**The section is a chamber.** The page is one bathhouse: five
full-bleed chambers in fixed ritual order — steam (42°), warm (38°),
tepid (34°), cool (28°), plunge (14°) — each a pinned scene on desktop
(§5), each entered through its arch. Chambers meet at **thresholds**:
a full-width arch band, 96–144px tall, in the *next* chamber's ground,
its arch cut showing the room beyond — never a straight colour break,
never a wave divider borrowed from a beach theme. The threshold
profile is one authored SVG arch path reused at every boundary and
every breakpoint; architecture does not redraw itself per screen
size.

**Ritual order is content order.** Chambers appear in the order the
ritual descends: the welcome and the story in the steam, the offerings
in the warmth, the rest in the tepid, the practicalities in the cool,
the booking in the plunge. The DOM order is the chamber order is the
reading order — a screen reader bathes through the same rooms.
Reordering chambers for visual variety is forbidden; if the ritual
changes, the house is re-plumbed and the change is recorded in the
footer record (§6.15).

**The arch is the frame.** Every image on the page sits inside a
mihrab arch mask: a pointed-arch clip-path whose apex is at top
centre, whose springing line sits at 58% of the frame's height, and
whose curve radius is 50% of the frame's width. One arch geometry,
defined once as an SVG path, used at every size — a tall arch for
portraits and chamber thresholds, a squat arch (springing at 44%) for
cards. Rectangular images are refused: a rectangle in this house is a
door left unbuilt. Avatars and staff portraits take the arch too —
people in this house are framed by its architecture, not excused from
it.

**The attendant's margin.** On ≥1200px, the left 72px of every chamber
is the margin: a vertical zone holding the thermometer (§6.4) and,
rotated −90°, the current chamber's name and temperature. Content
begins at 72px and reads in a 1060px-max column. The margin is the
page's instrument panel; nothing decorative is placed there, and no
content may stray into it. Below 1200px the thermometer moves to a
fixed bottom-left chip (§6.4) and the margin closes.

**Density follows temperature.** Density is the theme's second
thermometer. The steam room is soft and sparse (one headline, one
image, the announcement). The warm room is the fullest — the
treatments, the story, the detail live where the bather lingers. The
**tepid chamber is the emptiness law: at most 40 words of text, one
image, one instruction** — it is the ritual's rest, and filling it
"for SEO" or "for balance" is the theme's defining failure (§9). The
cool room is practical and compact (times, prices, what to bring).
The plunge holds exactly the booking and nothing else: form, price,
confirmation. A plunge chamber as busy as the warm room has not
understood what cold water is for.

**The plunge does not drift.** The final chamber has no parallax, no
wisps, no ambient motion except the booking's own states (§6.14). Its
edges are sharp, its rendering instant. After four rooms of vapour,
stillness and clarity are the plunge's content statement.

## 5. Full motion system

Five named easings, used by every element and no others:

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-steam` | `cubic-bezier(.35,.55,.45,1)` | Vapour thinning: a quick bloom, then a long clear | Steam emergence (§6.1), chamber wipes (§6.2), steam pass (§6.16) |
| `--ease-pour` | `cubic-bezier(.6,0,.2,1)` | Water poured: fast spread across the surface, slow settle | Warm pour (§6.9), arch openings (§6.5), condensation wipe (§6.8) |
| `--ease-drift` | `cubic-bezier(.45,0,.55,1)` | The languid glide: even, unhurried, no arrival accent | Wisps (§6.6), arch parallax (§6.3), thermometer fill (§6.4) |
| `--ease-vein` | `cubic-bezier(.4,0,.3,1)` | A line drawn by a steady hand: the vein, the rules, the draws | Marble vein (§6.7), footer draw (§6.15) |
| `--ease-plunge` | `cubic-bezier(.85,0,.15,1)` | The cold snap: near-instant, hard stop, no settle tail | Plunge snap (§6.10), plunge states (§6.14) |

**Every motion term, translated into the bathhouse's language:**

- **Scroll-triggered reveals** are arch openings (§6.5): content is
  entered through a doorway, not faded up out of the floor. Nothing on
  this page rises like a SaaS landing section.
- **Scroll scrub** is temperature itself: the colour-temperature scrub
  (§6.3), the thermometer's fill (§6.4) and the arch parallax are pure
  functions of scroll position, driven by the shared loop.
- **Parallax** is architectural: the arch layer drifts at 0.94×, the
  text at 1.0×, the wisps rise at 1.06× (§6.3, §6.6). There is no
  decorative background parallax; the building is the content.
- **Pinned scenes:** exactly five — the chambers. Pinning is the
  architecture of this theme, and it is rationed to it: each chamber
  pins for 140vh of scroll on desktop, and no element inside a chamber
  pins again. A build that pins a sixth scene has added a room the
  ritual doesn't have.
- **Masked reveals** are steam and arches: the vapour that thins
  (§6.1) and the clip-path that opens (§6.5) — both are the house's
  own substances, both carry the §1 clear-time law.
- **Blur-to-sharp is licensed only as steam.** The hero headline's
  blur is vapour — a named material with a 3000ms hard clear — not a
  camera effect. Any other blur reveal (blurred cards, blurred
  images sharpening on entry) is refused: there is no lens in the
  bathhouse, only air.
- **Kinetic typography is refused** except the condensing headline
  (§6.1): its tracking draws together by −0.04em once, as the steam
  clears — droplets merging. Type does not perform in the rooms.
- **Counters** are ritual figures (§6.17): temperatures and durations
  count to their ritual-object values when their chamber is announced.
- **Progress** is the thermometer (§6.4): five notches, filled in
  ritual order, the current temperature printed beside it. There is
  no progress bar.
- **Marquee is refused.** Nothing in a bathhouse runs sideways
  forever. The house's announcements stand still and are read.
- **Ambient loops:** exactly one family — the steam wisps (§6.6),
  rationed per chamber (present in steam and warm, sparse in tepid,
  absent in cool and plunge), plus the condensation's slow re-fog
  (§6.8). Both pause off-screen; both are cut first by the
  performance ladder (§14).
- **Micro-interactions:** the condensation wipe (§6.8), the warm pour
  (§6.9), the plunge snap (§6.10). Every interaction is something a
  bather does to a surface: clear it, warm it, plunge into it.
- **Hover physics:** no magnetic pull, no tilt stages. Marble does
  not lean toward the visitor. A surface under the hand is cleared of
  steam or warmed — that is all, and it is enough.
- **Page transitions** are a steam pass (§6.16): the visitor passes
  through vapour between rooms of the site, ≤900ms, watchdog-guarded.
- **Smooth scrolling — the scroll itself has a temperature.** The
  shared loop lerps scrubbed values at `--lerp-warm` 0.09 while the
  visitor is in the steam, warm or tepid chambers — languid, heavy,
  warm — and at `--lerp-cold` 0.18 in the cool room and plunge: crisp,
  immediate, cold. The switch happens at the cool chamber's threshold
  and is itself eased over 600ms so the hand feels the water change,
  not a settings change. Native scroll is never hijacked; the house
  smooths its instruments, not the visitor's hand.
- **The shared loop law.** One `requestAnimationFrame` loop owns every
  scrubbed value (temperature scrub, thermometer, arch parallax, wisp
  rise, condensation re-fog). It writes only transform / opacity /
  custom properties, switches its lerp factor by chamber (§5 above),
  and stops writing a value when it settles within 0.1% of target.

**Watchdog law.** Every vapour has a timer: the hero's steam clears
by 3000ms after load whatever the loop is doing (§6.1); a chamber
wipe completes by 1200ms after its pin boundary is crossed (§6.2);
condensation never survives 5000ms of pointer absence (§6.8). The DOM
ships clear — every steam layer exists only under a JS-armed root
class. No-JS is not a degraded mode; it is the bathhouse with the air
already clear, which is most of what the steam was for.


## 6. Signature elements

### 6.1 Steam emergence

- **What & why.** The hero headline begins behind steam: a soft white
  vapour layer over the slab, the headline blurred beneath it, and
  over 3000ms the layer thins and lifts while the headline's letters
  condense — tracking drawing from −0.005em to −0.04em, droplets
  merging as the air clears. It belongs because the title is the first
  bather: it emerges from the steam the visitor is about to walk
  through, and the emergence teaches the page's whole grammar — vapour
  is a threshold you pass, and what is behind it was there all along.
- **Structure.** A `<header class="slab">` (§6.12) carrying the
  headline in real DOM at full contrast, a `::after` vapour layer
  (`--vapour`, backdrop-blur 6px at arm time, pointer-events none),
  and the headline's own `filter: blur(3px)` start state. Both blurred
  states exist only under the JS-armed root class `.house-armed`; the
  shipped DOM is clear, sharp and fully tracked-out.
- **Motion spec.** Trigger: load, gated on `document.fonts.ready`
  raced against a 500ms timer — steam must not wait for a slow font to
  start clearing. t=0–600ms: the vapour blooms slightly (opacity .88 →
  .96, blur 6px → 7px) — the door has just closed behind the visitor.
  t=600–3000ms: the layer thins on `--ease-steam` (opacity → 0, blur →
  0, translateY 0 → −24px as it lifts), the headline's blur resolves
  3px → 0 across the same window, and its tracking condenses
  −0.005em → −0.04em, letters arriving at their final spacing in the
  last 800ms. Total ceremony exactly 3000ms — §1's hard limit, not a
  target to drift past. A click, a keypress or the first scroll
  completes it instantly.
- **States.** Steamed (armed, ≤3000ms) → clearing → clear (permanent;
  the vapour layer is removed from the DOM at completion, not merely
  faded). It runs once per session; a return visit within the session
  loads clear.
- **Content merge.** The steam is *over the headline itself*, and the
  headline is the content — the animation is the act of the title
  becoming readable, performed by the room it names. Remove the steam
  and the page loses nothing but the doorway.
- **Failure fallback.** No JS: no vapour layer exists; the headline
  stands clear. Watchdog: a 3000ms `setTimeout` from arm time forces
  the clear state and removes the layer even if the loop never runs —
  `transitionend` is never trusted. If fonts fail, the race starts the
  clear in the fallback face; the tracking condense absorbs the
  letterfit shift because the headline's box is fixed-height.
- **Reduced-motion variant.** No steam, no condense: the headline
  stands at final tracking, sharp, at first paint. The information
  (the title) is identical; only the doorway rests.
- **Performance budget & mobile variant.** One backdrop-blur layer and
  two property animations; backdrop-blur is the most expensive line in
  this theme and is rationed to this element and §6.2. Mobile
  (<768px): the ceremony shortens to 2000ms, blur peaks at 4px, and
  the lift is −12px — a phone's steam room is smaller and its air
  clears faster.
- **Choreography timeline (v2).** t=0 fonts ready (or 500ms race lost)
  → t=0–600 bloom → t=600 thinning begins, headline blur 3px → 1.5px
  by t=1800 → t=2200 tracking condense begins → t=3000 vapour at 0,
  layer removed, headline at −0.04em, sharp → the chamber label's
  attendants (§6.11) have announced the room inside this window at
  their own trigger.
- **State matrix (v2).** *Rest:* clear headline, no layer. *Hover:*
  none — the emergence is not a control. *Focus:* focus landing on the
  headline's chamber link completes the clear instantly. *Active:*
  n/a. *Scrolled-past:* clear; never re-steams. *Disabled:* the
  ceremony is session-flagged; disabled = already run = clear.
  *Touch:* identical; a tap anywhere completes it.
- **Breakpoints (v2).** ≥1200px: 3000ms, blur 6→7px, lift −24px.
  768–1199px: 2600ms, blur 5px, lift −18px. <768px: 2000ms, blur 4px,
  lift −12px, tracking condense halved (−0.02em — small type must not
  crowd).
- **Edge cases & failure modes (v2).** *Slow network, hero image late:*
  the emergence runs on the slab regardless; the arch image (§6.12)
  fades in beneath cleared air when it arrives — steam never re-arms
  for an image. *Tab hidden mid-ceremony:* the watchdog is wall-clock,
  so a returning visitor finds the room clear, never a ceremony
  resumed mid-bloom. *Headline longer than 2 lines:* the build refuses
  it (§3); if content forces 3 lines, the condense is cut and only
  the vapour runs — crowding three lines is worse than skipping the
  droplets.
- **Accessibility spec (v2).** The headline is in the accessibility
  tree at full text from first paint — the vapour is `aria-hidden`
  and purely visual; screen readers never wait for steam. The blur
  never applies to focused content. Contrast is specified in the
  clear state (§2) because the steamed state is transient by law.
- **Tokens consumed (v2).** `--steam`, `--vapour`, `--ease-steam`,
  `--dur-emerge` (3000ms), `--dur-clear-law` (3000ms), `--blur-steam`
  (6px), `--track-condensed` (−0.04em).

### 6.2 Chamber steam-wipes

- **What & why.** Moving between chambers crossfades through steam:
  as one chamber's pin releases and the next chamber's threshold
  crosses, vapour density peaks mid-transition and thins onto the new
  room. It belongs because it is the ritual's doorway made literal —
  in a real bathhouse you pass through steam to reach the next
  temperature, and the wipe makes the scroll feel that passage instead
  of merely arriving. It is also the discipline that keeps the page's
  transitions uniform: one doorway, everywhere, always vapour.
- **Structure.** Each chamber boundary carries a threshold band (§4)
  with a vapour layer: an absolutely positioned div in `--vapour`,
  `pointer-events: none`, whose opacity is a pure function of the
  shared loop's boundary progress q (0 at the threshold's approach, 1
  at its centre, 0 as the new chamber settles). Both chambers' content
  is fully rendered at all times; the vapour is the only thing that
  moves.
- **Motion spec.** Trigger: scroll through a chamber pin boundary.
  The wipe's full pass is 1200ms of scroll travel: density rises
  0 → .92 across the first 45% on `--ease-steam`, peaks as the
  threshold arch is centred, and thins .92 → 0 across the final 55%.
  At the peak, the outgoing chamber is fully veiled for no more than
  ~250ms of travel — a held breath, not a whiteout. On fast scroll
  the wipe compresses proportionally; below 300ms of boundary travel
  it is skipped entirely and the chambers simply meet.
- **States.** Clear → steaming (rising) → peak (≤250ms) → thinning →
  clear in the new chamber. Scrolling back up runs the same doorway in
  reverse; the ritual may be walked backward and the steam does not
  care which way the bather passes.
- **Content merge.** The vapour lives in the threshold — the
  architectural element that already separates the rooms — and both
  rooms' content is present beneath it throughout. The wipe *is* the
  boundary being crossed; remove it and the threshold remains, merely
  unsteamed.
- **Failure fallback.** The 1200ms law: any wipe still veiling content
  1200ms after the visitor stops scrolling is cleared instantly by
  watchdog. No JS: no vapour layers exist; chambers meet at their
  thresholds. If the loop stalls, a per-boundary `setTimeout` performs
  the same clear.
- **Reduced-motion variant.** No wipes. Chambers meet at their
  threshold arches; the boundary is marked by the arch and the
  attendant's label only.
- **Performance budget & mobile variant.** One opacity animation per
  boundary, compositor-only; at most one boundary is steaming at any
  moment (boundaries are 140vh apart by construction). Backdrop-blur
  is NOT used here on mobile — opacity only. Mobile (<768px): chambers
  do not pin (§5), so the wipe becomes a short 600ms vapour pass as
  the threshold crosses 60% viewport height, peak opacity .7.
- **Choreography timeline (v2).** q=0 threshold enters lower viewport
  → q=0–.45 density 0 → .92, outgoing chamber veiling → q=.5 peak,
  arch centred, incoming chamber's label ghosting through → q=.45–1
  density → 0, incoming chamber sharp by q=.9 → q=1 the new chamber's
  announcement (§6.11) begins.
- **State matrix (v2).** *Rest:* clear. *Hover:* none. *Focus:* focus
  crossing into the next chamber (keyboard) clears the wipe instantly
  and places the reader in the new room — focus never travels through
  fog. *Active:* n/a. *Scrolled-past:* clear. *Disabled / no-JS:*
  clear. *Touch:* identical at the mobile values.
- **Breakpoints (v2).** ≥1200px: pinned pass, 1200ms, peak .92.
  768–1199px: pinned pass, 1000ms, peak .85. <768px: unpinned 600ms
  pass, peak .7, opacity only.
- **Edge cases & failure modes (v2).** *Fling through two chambers:*
  intermediate wipes are skipped (the <300ms rule compounds: a chamber
  passed entirely in one fling never steams) and the landing chamber
  stands clear. *Anchor jump into a chamber:* no wipe; the visitor
  arrives by the door the link names, and §6.11 announces the room.
  *Resize mid-wipe:* density is a function of boundary progress, not
  time, so the wipe re-derives instantly against the new geometry —
  no stuck veil.
- **Accessibility spec (v2).** The vapour is `aria-hidden`; both
  chambers are complete in the tree at all times, in ritual order.
  The wipe is never announced. A `prefers-reduced-transparency`
  visitor gets the reduced treatment (no vapour) even with motion
  allowed — the house respects both preferences independently.
- **Tokens consumed (v2).** `--vapour`, `--ease-steam`,
  `--dur-wipe` (1200ms), `--wipe-peak` (.92), `--dur-clear-law`
  (3000ms — the outer bound no combination of wipes may exceed at one
  boundary).

### 6.3 Temperature scrub

- **What & why.** The page's colour temperature shifts cooler scrubbed
  across the whole ritual: grounds, accents and the light itself move
  from warm ivory in the steam room toward plunge-deep accents in the
  cold, while text density loosens in the warm middle and tightens in
  the cold. It belongs because it makes the scroll position a climate:
  the visitor does not just read about descending temperatures, the
  page they are holding cools in their hands. It is the theme's
  background argument, running under every chamber.
- **Structure.** A single custom property, `--temp` (1.00 in the steam
  room → 0.00 in the plunge), written by the shared loop from ritual
  progress and consumed by chamber grounds and accents via
  `color-mix()`: each chamber declares its ground as a mix between its
  warm pole and its cool pole, so the scrub tints *within* the chamber
  rather than repainting it — the steam room cools toward marble, the
  warm room toward slate, the plunge is already at its floor and does
  not move. Text colours are never mixed (§2's pairing law is checked
  at both poles).
- **Motion spec.** Trigger: scroll scrub, continuous. `--temp` is a
  piecewise function of chamber position: within a chamber it drifts
  by at most 0.12 (the room's own cooling as you cross it); at each
  threshold it steps by the chamber gap (steam .12, warm .18, tepid
  .18, cool .22, plunge the remainder) eased over the threshold's
  1200ms travel on `--ease-drift`. Arch layers parallax at 0.94×
  against the text's 1.0× throughout (§5). The lerp factor is the
  chamber's own: 0.09 warm, 0.18 cold (§5's scroll-temperature rule).
- **States.** The scrub is stateless — a climate, not a component. At
  rest at any scroll position it holds that position's temperature
  exactly; it has no rest state of its own.
- **Content merge.** The scrub tints the chambers' own grounds and the
  threshold arches — the building cools, not an overlay. Every surface
  it touches is a surface the content sits on; there is no separate
  "effect layer" to remove.
- **Failure fallback.** No JS or loop failure: `--temp` holds its
  per-chamber CSS default (each chamber declares its mid-ritual value
  statically), so every chamber stands at a fixed, contrast-checked
  temperature. The page loses the cooling, never its legibility.
- **Reduced-motion variant.** The scrub steps discretely at thresholds
  (each chamber at its declared fixed temperature, no drift within).
  The climate is still communicated — by chamber, not by gradient.
- **Performance budget & mobile variant.** One custom property written
  per frame; `color-mix()` grounds are computed by the compositor for
  the ≤5 chamber surfaces. Mobile: the within-chamber drift is cut
  (threshold steps only) — small screens cross chambers too fast for a
  0.12 drift to read as anything but noise.
- **Choreography timeline (v2).** Continuous: `--temp` 1.00 at the
  slab → .88 leaving the steam room → .70 leaving the warm → .52
  leaving the tepid → .30 leaving the cool → 0.00 at the plunge's
  centre, where it locks; the footer (§6.15) sits at 0.00 — the record
  is written in cold water.
- **State matrix (v2).** *Rest:* holds position temperature. *Hover /
  focus / active:* unaffected — climate does not respond to the hand.
  *Scrolled-past:* chambers above hold their exit values when
  revisited; scrolling up re-warms exactly (the function is pure).
  *Disabled:* per-chamber static defaults. *Touch:* identical values,
  threshold steps only.
- **Breakpoints (v2).** ≥1200px: full drift + steps. 768–1199px: drift
  halved (0.06). <768px: steps only, as above.
- **Edge cases & failure modes (v2).** *A page with three chambers*
  (a short ritual): the function renormalises over the chambers
  present — `--temp` still spans 1.00 → 0.00 across the ritual that
  exists; the thermometer (§6.4) renormalises with it from the same
  object. *`color-mix()` unsupported:* the build ships per-chamber
  static grounds (the reduced treatment) — detected by `@supports`,
  never by sniffing. *Contrast at the poles:* every text pairing is
  audited at `--temp` 1.00 and 0.00 (§10, gate 6); a pairing that only
  passes mid-scrub fails.
- **Accessibility spec (v2).** The scrub never carries information
  alone: chamber identity is always also in the label, the temperature
  figure and the thermometer. Visitors who cannot perceive the cooling
  lose atmosphere, not content.
- **Tokens consumed (v2).** `--temp`, `--steam`, `--marble`, `--stone`,
  `--slate`, `--plunge`, `--ease-drift`, `--lerp-warm` (0.09),
  `--lerp-cold` (0.18).


### 6.4 Thermometer progress

- **What & why.** In the attendant's margin stands a thermometer: a
  slender stone column with five notches — steam, warm, tepid, cool,
  plunge — that fills notch by notch as the visitor passes each
  chamber, with the current chamber's temperature printed beside it
  in ledger figures. It belongs because progress in this house is body
  temperature: the gauge measures the visitor's own ritual state, and
  its five notches are the five rooms they have been announced into.
  It is also the ritual object made visible — the same data object
  that prints the chamber labels and the footer record (§6.15), so the
  instrument cannot disagree with the rooms.
- **Structure.** A `<nav class="thermometer" aria-label="The ritual">`
  in the left margin (§4): an SVG column 8px wide, five notch ticks,
  a fill line that rises as chambers complete, and beside each notch a
  link lettered with the chamber's name and temperature ("STEAM ·
  42°"). The current temperature is a live `<output>` in Alegreya Sans
  tabular beside the active notch. All five notches are real links to
  their chambers from first paint.
- **Motion spec.** Trigger: scroll. The fill rises on `--ease-drift`
  as a pure function of ritual progress (the shared loop writes one
  scaleY): a notch lights (its tick fills stone → its chamber's pole
  colour, 300ms) as its chamber's midpoint passes viewport centre, and
  the printed temperature crossfades to the new chamber's figure over
  200ms. Notches fill in ritual order only — the instrument has no way
  to show plunge before cool, because the page has no way to be read
  in that order (§4).
- **States.** *Rest:* filled to the current chamber, current
  temperature printed. *Hover (notch):* the notch's chamber name warms
  (stone-deep → ink, 150ms) — desktop only. *Focus:* identical to
  hover, with the §11 focus ring. *Scrolled-past chambers:* their
  notches stay filled when the visitor scrolls back up — the
  instrument remembers the deepest point of the ritual reached, while
  the printed temperature always reports the chamber currently stood
  in. The two facts are never confused: fill = furthest, figure =
  current.
- **Content merge.** The thermometer *is* the chamber index and the
  progress gauge in one instrument: its notches are the sections, its
  figures are §1's temperatures, its fill is the reading. Remove the
  animation and it remains the page's table of contents.
- **Failure fallback.** No JS: all five notches stand printed with
  their temperatures, the fill drawn to the first notch (the visitor
  is, statically, at the door). Loop failure: the fill freezes at its
  last true value — an instrument that stops is honest; one that
  guesses is not.
- **Reduced-motion variant.** The fill steps notch to notch (no rising
  animation); the temperature figure swaps instantly. The instrument
  reads identically.
- **Performance budget & mobile variant.** One SVG, one transform per
  frame. Mobile (<1200px): the margin column closes and the
  thermometer becomes a fixed chip at bottom-left — five dots and the
  current temperature ("WARM · 38°") — 44px tall, tapping it opens the
  chamber list (§6.11's grammar). Below 768px the dots lose their
  labels; the figure remains.
- **Choreography timeline (v2).** Continuous with §6.3: fill 0 at the
  slab → notch 1 lights as the steam room's midpoint passes centre →
  notches 2–4 at their midpoints, figure crossfading 42° → 38° → 34°
  → 28° → notch 5 and 14° as the plunge is entered → fill complete at
  the plunge's centre, where it locks beside §6.10's snap.
- **State matrix (v2).** *Rest:* as above. *Hover:* notch warms
  (desktop). *Focus:* hover parity + ring. *Active:* the link's
  chamber is jumped to (no wipe, §6.2's anchor rule). *Scrolled-past:*
  fill remembers furthest; figure reports current. *Disabled:* a
  chamber with no section is absent from the instrument — the gauge
  never promises a room the house doesn't have. *Touch:* the chip;
  tap targets ≥44px.
- **Breakpoints (v2).** ≥1200px: full margin instrument, names +
  figures. 768–1199px: bottom-left chip with dots + figure.
  <768px: chip, dots unlabelled, figure only.
- **Edge cases & failure modes (v2).** *Three-chamber page:* the
  instrument draws three notches and renormalises its fill from the
  same ritual object as §6.3 — instrument and page can never disagree
  about how many rooms exist. *Very fast scroll to the plunge:* all
  notches light in order within one frame batch — the fill catches up
  in ritual order, never out of it. *Print:* the thermometer prints
  as the chamber list with temperatures (the ritual on paper).
- **Accessibility spec (v2).** A real `<nav>` with five links named
  "The Warm Room — 38 degrees". The current chamber carries
  `aria-current="true"`, migrating with scroll. The fill and dots are
  `aria-hidden` decoration over the links. The `<output>` temperature
  is `aria-live="off"` — the figure is readable on demand, never
  announced over the prose.
- **Tokens consumed (v2).** `--stone`, `--stone-deep`, `--ink`,
  `--ease-drift`, `--dur-notch` (300ms), the five chamber pole colours,
  `--lerp-warm` / `--lerp-cold` via the shared loop.

### 6.5 Arch openings

- **What & why.** Every section inside a chamber — and every chamber
  itself at smaller breakpoints — opens through its arch: the mihrab
  clip-path expands from its apex over 900ms, the content standing
  complete behind the opening arch. It belongs because the doorway
  shape is the architecture the content sits inside: entering a
  section is entering a room, and the arch is how this house says a
  room has begun. It is the theme's reveal grammar, as the spade-wipe
  is the trench's — one reveal, everywhere, always the same doorway.
- **Structure.** Each arch-framed block carries the §4 arch as a
  `clip-path: path()` on a wrapper, with the content fully rendered
  inside at all times. The closed state — the arch path scaled to 12%
  about its apex — exists only under the JS-armed root class; the
  shipped DOM is open. The arch geometry is the single authored path
  from §4, scaled by transform, never redrawn per element.
- **Motion spec.** Trigger: the block's top crosses 75% of viewport
  height. The clip scales 12% → 100% about the apex over 900ms
  `--ease-pour`, the apex leading, the springing line (58%) reached at
  ≈t=520, the feet landing last. One arch opens at a time per chamber;
  a second block entering during an opening queues at +250ms overlap.
  Blocks already >50% visible at load are never closed.
- **States.** Closed (armed only) → opening (900ms) → open
  (permanent; scrolling back up never re-closes an arch — a room once
  entered stays entered). Focus entering a closed block opens it
  instantly.
- **Content merge.** The arch is the frame the content already lives
  in (§4): the opening animates the frame, and the content's arrival
  and the doorway's opening are the same event. An arch that framed
  nothing would be a hole in a wall; here every arch frames its room's
  actual content.
- **Failure fallback.** The 1000ms law: any block still closed 1000ms
  after entering the viewport is opened instantly, clip removed. No
  JS: no closed states exist. A per-block `setTimeout` watchdog
  performs the same opening if the loop stalls.
- **Reduced-motion variant.** No opening. Arches stand open; the
  doorway is present as architecture, not as event.
- **Performance budget & mobile variant.** One clip-path animation per
  block, compositor-only; clips are removed after opening so the
  resting page carries no clip overhead. Mobile: opening shortens to
  650ms and starts from 22% — phone scrolling is fast, and a doorway
  that lags the thumb feels like a locked door.
- **Choreography timeline (v2).** t=0 block top crosses 75% line →
  t=0–300 apex descends, arch at 40% → t=520 springing line reached,
  arch at 78%, content's upper half readable → t=900 feet land, clip
  removed → queued next block began at t=650 per the overlap rule.
- **State matrix (v2).** *Rest (open):* framed content, still. *Hover:*
  none — the arch is not a control. *Focus:* focus inside a closed
  block opens it instantly. *Active:* n/a. *Scrolled-past:* open.
  *Disabled / no-JS:* open. *Touch:* identical at mobile values.
- **Breakpoints (v2).** ≥1200px: 900ms from 12%. 768–1199px: 800ms
  from 16%. <768px: 650ms from 22%, as above.
- **Edge cases & failure modes (v2).** *Block taller than 250vh:* the
  arch opens its first viewport-height and the remainder is simply
  present — the doorway opens the room; it does not perform the whole
  room. *Anchor jump into a closed block:* target and everything above
  it open instantly on arrival. *Resize mid-opening:* the clip is
  percentage/path-based against the element box, so it completes
  against the new size without a jump.
- **Accessibility spec (v2).** The clip is visual only; content is in
  the tree, in order, regardless of the arch's state — a screen reader
  enters every room immediately. Openings are never announced. Focus
  is never moved by an opening.
- **Tokens consumed (v2).** `--ease-pour`, `--dur-arch` (900ms),
  `--arch-springing` (58%), `--dur-fallback` (1000ms).

### 6.6 Steam wisps

- **What & why.** In the warm chambers, wisps of steam drift upward
  continuously — slow, sparse, thinning per chamber and absent in the
  plunge. It belongs because it is the air of each room behaving at
  its stated temperature: the steam room's air is visibly thick, the
  tepid room's barely moves, and the plunge's stillness (§4) is
  defined against the wisps' absence. It is the theme's only ambient
  loop, and it is rationed like one.
- **Structure.** A `pointer-events: none` canvas (or ≤14 DOM divs on
  low-power devices) pinned inside each warm chamber, `aria-hidden`,
  rendering soft radial-gradient sprites in `--vapour` that rise,
  expand and dissolve. Wisps spawn only within the chamber currently
  in view, from the chamber's lower third — steam rises from the
  water and the slab, not from the text.
- **Motion spec.** Ambient, per-chamber density from the ritual
  object: steam room 12 concurrent wisps, warm room 8, tepid 3, cool
  0, plunge 0. Each wisp: rise 140px over 6000–9000ms on `--ease-drift`
  (staggered phases), horizontal sway ±10px on a 7000ms sine, scale
  0.6 → 1.4, opacity peaking at .35 mid-life and dissolving to 0. The
  field thins *within* each chamber as the visitor descends through it
  (density × (1 − chamber progress × 0.5)) — the air settles as the
  bather does.
- **States.** Drifting (chamber in view) → paused (chamber off-screen,
  tab hidden, or budget cut) → absent (cool and plunge chambers, by
  law). Wisps never respond to hover, focus or click — weather does
  not perform for the hand.
- **Content merge.** The wisps rise through the chamber's own air,
  behind its text layer and above its ground: they are the room's
  atmosphere, spatially tied to the chamber they belong to, and they
  stop at its threshold. A wisp crossing into the next chamber is a
  leak, and the build clips them at chamber bounds.
- **Failure fallback.** No canvas/WebGL: DOM-div fallback with the
  same timings; no JS at all: no wisps — the chambers stand in clear
  air, which the theme explicitly accepts (§5's watchdog law). A wisp
  failure can never touch content: the layer is decorative and
  removable without consequence.
- **Reduced-motion variant.** No wisps, anywhere. The chambers' air is
  still and clear; temperature is carried by §6.3 and §6.4 alone.
- **Performance budget & mobile variant.** ≤12 sprites, one canvas per
  chamber, rAF-shared with the main loop; the field is the first cut
  in §14's ladder. Mobile: counts halve (6/4/2), rise shortens to
  90px, and on `save-data` or low-power signals the wisps are cut
  entirely.
- **Choreography timeline (v2).** Continuous while a warm chamber is
  in view: spawn at the chamber's lower third every ~700ms (steam
  room) to ~2400ms (tepid), each wisp living 6–9s; on chamber exit the
  field drains over 1200ms (no new spawns; living wisps finish their
  rise) so thresholds never pop.
- **State matrix (v2).** *Rest:* drifting per density law. *Hover /
  focus / active:* unaffected. *Scrolled-past:* drained and paused.
  *Disabled:* cool/plunge absence is a state of the ritual, not a
  disable; a globally disabled field (budget) leaves all chambers in
  clear air. *Touch:* identical counts at mobile values.
- **Breakpoints (v2).** ≥1200px: full densities. 768–1199px: densities
  × 0.75, rounded down. <768px: halved as above; canvas replaced by
  DOM divs if the device reports ≤4GB RAM or a low-power GPU.
- **Edge cases & failure modes (v2).** *Long chamber, long dwell:*
  the density cap is absolute — a visitor who rests ten minutes in
  the warm room gets the same 8 wisps, never an accumulation. *Wisps
  over text:* sprites render behind the text layer (z-order fixed in
  §4) and peak at .35 opacity, so a wisp behind a paragraph is
  weather behind glass; contrast is audited with wisps at peak (§10).
  *Battery saver / reduced data:* field cut, silently.
- **Accessibility spec (v2).** `aria-hidden`, no focusable content, no
  information carried. Under `prefers-reduced-motion` or
  `prefers-reduced-transparency` the field never arms.
- **Tokens consumed (v2).** `--vapour`, `--ease-drift`,
  `--wisp-peak` (.35), `--wisp-rise` (140px), the ritual object's
  per-chamber densities.


### 6.7 Marble vein draw

- **What & why.** A marble vein SVG-draws itself across the hero slab
  — one main vein travelling the slab's width over 1600ms, branching
  once, in stone at 60% — while the headline emerges above it (§6.1).
  It belongs because the slab the headline rests on is the house's
  central object, and the vein forming under the title says the
  material itself is alive in this house: the marble is not a texture
  pasted behind type, it is a stone being veined in front of the
  reader. It is also the theme's one drawn line, rationed to the slab
  the way the trench rations its surveyor's line.
- **Structure.** An inline SVG inside the slab (§6.12), behind the
  headline, `aria-hidden`: one main path (authored per build, a
  surveyed non-repeating profile crossing the slab diagonally) and one
  branch path leaving it at ~62% of its length. Drawn state is the CSS
  default; the undrawn state (`stroke-dasharray` offset) is JS-armed
  only.
- **Motion spec.** Trigger: load, beginning at t=900ms inside §6.1's
  emergence window — the vein starts once the steam has thinned
  enough to see the slab. Main vein draws over 1600ms `--ease-vein`;
  at t≈1900 (62% drawn) the branch begins, drawing over 700ms. Both
  complete by t=2600, inside the emergence's 3000ms, so the slab is
  finished as the air clears. It draws once per session.
- **States.** Undrawn (armed only) → drawing → veined (permanent). It
  never redraws, never responds to hover or scroll; a stone does not
  re-vein because it was looked at again.
- **Content merge.** The vein is *in* the slab the headline rests on —
  the hero's ground acquiring its material while its title emerges.
  The two ceremonies (§6.1, §6.7) share one window and one surface;
  neither is an overlay on the other.
- **Failure fallback.** No JS: the vein stands drawn. Watchdog: if the
  draw has not started by 1400ms it is drawn instantly; if it stalls
  mid-path, a 2600ms timer completes it.
- **Reduced-motion variant.** Drawn at first paint. The slab is marble
  before it is theatre.
- **Performance budget & mobile variant.** Two path animations, no
  images. Mobile: the branch is cut (main vein only, 1200ms) — a
  small slab carries one vein honestly.
- **Choreography timeline (v2).** t=900 draw begins under thinning
  steam → t=1900 branch forks → t=2500 main vein lands → t=2600 branch
  lands → t=3000 §6.1's clear completes over a finished slab.
- **State matrix (v2).** *Rest:* veined. *Hover / focus / active:*
  none. *Scrolled-past:* veined. *Disabled:* session-already-drawn =
  veined. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full draw with branch. 768–1199px:
  full draw, branch shortened (500ms). <768px: main vein only, 1200ms.
- **Edge cases & failure modes (v2).** *Slab narrower than the path:*
  the path is authored against the slab's aspect box with
  `preserveAspectRatio="none"` refused — instead the path is defined
  in a 1200×400 viewBox and scales uniformly, cropping at the slab's
  edges like a real cut stone. *Dark scheme:* the vein takes stone at
  45% (the evening slab is less veined to the eye — §2's lamplight
  ruling).
- **Accessibility spec (v2).** Purely decorative and `aria-hidden`;
  the slab's meaning is in its headline and announcement, which are
  text.
- **Tokens consumed (v2).** `--stone`, `--ease-vein`, `--dur-vein`
  (1600ms), `--vein-opacity` (.6).

### 6.8 Condensation wipe hover

- **What & why.** Treatment cards in the warm chambers carry a thin
  condensation layer; hovering (or focusing) wipes a clear radial
  patch in it that follows the pointer, so the treatment is read
  through a cleared circle of its own steam, and when the hand leaves,
  the patch fogs back over ~5000ms. It belongs because reading a
  treatment in a bathhouse means clearing its steam — the gesture is
  done on the card's own surface, with the hand, the way a bather
  wipes a mirror. It is the theme's examination tool, as the brush is
  the trench's.
- **Structure.** Each card (§6.13) carries a condensation layer: a div
  in `--vapour` at .55 opacity with a radial-gradient mask whose clear
  centre (radius 90px) is positioned by custom properties written from
  pointer position through the shared loop. The card's content is
  fully rendered beneath at all times; the condensation never applies
  to the card's title or price line, which sit above the layer in
  clear air — the attendant keeps the name readable.
- **Motion spec.** Trigger: pointerenter / focus. The clear patch
  opens over 250ms `--ease-pour` (radius 0 → 90px) and follows the
  pointer with the loop's warm lerp (0.09 — the wipe trails the hand
  slightly, like a real palm on glass). On leave, re-fog begins after
  an 800ms grace and completes over 5000ms linear-ish on
  `--ease-steam`, the patch shrinking as it clouds. Keyboard focus
  clears a patch centred on the card and holds it while focus remains.
- **States.** *Fogged* (rest, .55) → *clearing* → *clear patch under
  the hand* → *re-fogging* (800ms grace + 5000ms) → *fogged*. A card
  that has been read keeps a faint permanent clearing at its centre
  (.55 → .42) for the session — the mirror remembers being wiped.
- **Content merge.** The condensation is on the treatment's own card
  and the reading happens through the cleared patch on that card — the
  interaction and the content are the same surface. A build that fogs
  a card with no treatment beneath it has steamed an empty mirror.
- **Failure fallback.** No JS / no pointer: cards stand at a light
  .25 condensation that never obscures (contrast audited at that
  level) — or, if the loop fails, the layer is removed entirely by
  watchdog within 1000ms of the failure. Condensation is a courtesy,
  never a lock.
- **Reduced-motion variant.** No condensation layer. Cards stand clear;
  hover gets §6.9's warmth only.
- **Performance budget & mobile variant.** One masked layer per card,
  mask position written by the shared loop; ≤6 condensed cards per
  viewport by the density law (§4). Mobile/touch: there is no hover —
  the first tap on a card clears its whole face over 400ms (and does
  not activate the card's action); the second tap acts. Re-fog on
  touch is 3000ms.
- **Choreography timeline (v2).** t=0 pointer enters → t=0–250 patch
  opens to 90px → tracking while the pointer moves (lerp 0.09) →
  t=leave +800ms grace → +800–5800 re-fog to .55 (or .42 if previously
  read) → rest.
- **State matrix (v2).** *Rest:* fogged .55. *Hover:* patch clear,
  following. *Focus:* patch centred and held; focus ring (§11)
  visible above the layer. *Active (click):* §6.9's pour fires through
  the cleared patch. *Scrolled-past:* fogged; the session's .42 memory
  persists. *Disabled:* a sold-out treatment's card stands clear and
  unsteamed — no wiping a treatment that cannot be booked. *Touch:*
  two-tap grammar as above.
- **Breakpoints (v2).** ≥1200px: 90px patch, 5000ms re-fog.
  768–1199px: 75px patch, 4500ms re-fog. <768px: whole-face clear on
  first tap, 3000ms re-fog.
- **Edge cases & failure modes (v2).** *Pointer leaves the window
  mid-wipe:* the patch holds at its last position and re-fogs on the
  normal schedule — no orphan clear spot. *Many cards wiped in
  succession:* each card keeps its own layer and timer; the loop
  writes at most 6 masks per frame. *Text selection attempt:* the
  layer is `pointer-events: none` and `user-select` is never touched —
  the steam never eats a selection.
- **Accessibility spec (v2).** The layer is `aria-hidden` and
  pointer-events none; card content is fully in the tree at all times.
  Focus clears the patch (above), so keyboard readers get the same
  clear view as pointer readers. Contrast is audited in the fogged
  state for the title/price (which sit above the layer) and in the
  cleared state for the body.
- **Tokens consumed (v2).** `--vapour`, `--ease-pour`, `--ease-steam`,
  `--dur-wipe-clear` (250ms), `--dur-refog` (5000ms), `--patch-radius`
  (90px), `--lerp-warm` (0.09).

### 6.9 Warm pour click

- **What & why.** Clicking a treatment pours a warm glow across its
  card from the click point: a radial spread of `--ember` at low
  opacity, expanding over 600ms, holding 1000ms, then cooling over
  1200ms. It belongs because selection feedback in this house is
  temperature — the treatment warms under the hand that chose it, the
  way water poured over the slab warms the stone it crosses. It
  replaces the ripple, the checkmark-pop and the colour-flash with the
  house's own physics.
- **Structure.** A glow layer inside the card (§6.13), beneath its
  text, `pointer-events: none`: a radial gradient centred on custom
  properties set from the click coordinates, its radius and opacity
  animated by the shared loop. The pour also sets the card's chosen
  state (§6.13): a stone-deep rule under the title warms to `--ember`
  for as long as the treatment is selected.
- **Motion spec.** Trigger: click / tap / Enter / Space on the card's
  select control. Spread: radius 0 → 120% of the card's diagonal over
  600ms `--ease-pour`, opacity 0 → .28. Hold: 1000ms at .28. Cool:
  → .10 over 1200ms `--ease-steam`, where it rests while the treatment
  remains selected; deselecting cools it to 0 over 600ms. Keyboard
  activation pours from the card's centre.
- **States.** *Unchosen:* no glow. *Pouring* (600ms) → *warm* (hold
  1000ms) → *resting warmth* (.10, while selected) → *cooling* on
  deselect. Re-clicking a selected card re-pours from the new click
  point — the hand warms it again.
- **Content merge.** The glow spreads across the treatment's own card,
  from the point the visitor touched it, and its resting warmth *is*
  the card's selected state — feedback and state are one substance.
  A pour on a non-treatment surface is refused by construction: only
  treatment cards carry the layer.
- **Failure fallback.** No JS: selection is shown by the rule and a
  printed "CHOSEN" apparatus line (§6.13) — the pour is the flourish,
  never the only signal. Loop failure mid-pour: the glow freezes at
  its current opacity and is removed by the 1000ms watchdog; the
  selected rule remains.
- **Reduced-motion variant.** No spread: the resting warmth (.10) and
  the ember rule apply instantly on selection. State is identical;
  only the pouring rests.
- **Performance budget & mobile variant.** One gradient layer per
  card, transform/opacity only; at most 2 pours animate concurrently
  (a third click queues its spread to the next frame batch). Mobile:
  the pour spreads from the tap point identically; hold shortens to
  700ms.
- **Choreography timeline (v2).** t=0 click → t=0–600 spread to 120%
  at .28 → t=600–1600 hold → t=1600–2800 cool to .10 → rest (selected)
  → on deselect t=0–600 cool to 0, ember rule returns to stone-deep at
  t=300.
- **State matrix (v2).** *Rest:* unchosen, no glow. *Hover:* §6.8's
  wipe only — warmth is earned by choosing, not by passing over.
  *Focus:* no glow (focus is shown by the ring); *active/activation:*
  the pour. *Scrolled-past:* selected cards keep their .10 warmth and
  ember rule. *Disabled:* a sold-out treatment cannot be poured on —
  its card stands clear, cool and unsteamed (§6.8). *Touch:* pour from
  the tap point on the second tap (the first tap clears, §6.8).
- **Breakpoints (v2).** ≥1200px: as specified. 768–1199px: spread
  capped at 100% diagonal. <768px: hold 700ms, cool 900ms.
- **Edge cases & failure modes (v2).** *Rapid re-clicks:* the pour
  restarts from the newest point; opacities never stack beyond .28
  (the layer is single, values clamp). *Pour during re-fog (§6.8):*
  the pour fires through the condensation — the patch clears
  instantly at the click point as the glow spreads, the two layers
  composited in the loop's fixed z-order. *Card removed while warm
  (list re-render):* the glow dies with the card; the selection
  persists in the booking summary (§6.14) — state outlives surface.
- **Accessibility spec (v2).** The glow is `aria-hidden` decoration;
  selection is conveyed by the control's `aria-pressed` / radio state
  and the printed CHOSEN line, never by warmth alone. Ember at .28
  over marble never sits behind text at less than §2's audited
  pairings (text stays ink; the glow is beneath it and contrast is
  checked in the warm state, §10 gate 6).
- **Tokens consumed (v2).** `--ember`, `--ease-pour`, `--ease-steam`,
  `--dur-pour` (600ms), `--pour-peak` (.28), `--pour-rest` (.10).

### 6.10 Cold plunge snap

- **What & why.** The final chamber arrives with a snap: as the plunge
  threshold is crossed, steam is instantly absent, edges sharpen, and
  the booking chamber settles in 150ms — a clarity settle instead of a
  fade. It belongs because it is the ritual's climax performed by the
  rendering itself: after four rooms of vapour and drift, the cold
  water does not fade in, it *hits*. Every prior element has been
  teaching the visitor to feel this one.
- **Structure.** The plunge chamber (§6.14's home) carries a
  `data-climate="plunge"` state set by the shared loop at its
  threshold: under it, the chamber's entrance transforms are disabled,
  `--temp` locks to 0.00 (§6.3), the loop's lerp switches to
  `--lerp-cold` 0.18 (§5), and a one-time 150ms `--ease-plunge` settle
  (scale 1.004 → 1, no opacity change — cold sharpens, it does not
  fade) marks the arrival. The chamber's DOM is, as everywhere,
  complete from first paint.
- **Motion spec.** Trigger: the plunge threshold crossing viewport
  centre. t=0: any residual vapour from §6.2's wipe is cut, not faded
  (the doorway into the plunge is a duck under cold water, not a
  thinning). t=0–150ms: the settle runs. From t=150: the chamber is
  still (§4) — no wisps, no drift, no parallax — and every interaction
  inside it answers at plunge timings (≤150ms, §6.14).
- **States.** *Approaching* (cool chamber, lerp easing toward cold
  across the threshold's 600ms, §5) → *plunged* (locked, still, crisp)
  → scrolling back up releases the lock at the same threshold: the
  cool room re-warms the loop over 600ms. The snap itself fires once
  per entry, not continuously while the chamber is in view.
- **Content merge.** The snap is a property of the booking chamber's
  own rendering — the cold is in how the content presents itself, not
  in an effect laid over it. The form (§6.14) inherits the snap's
  timings; the chamber and its ask are one temperature.
- **Failure fallback.** No JS: the plunge chamber stands in its final
  state — deep ground, sharp edges, still — which is precisely the
  snap's end state. The ceremony is the arrival, not the room.
- **Reduced-motion variant.** Identical end state with no settle: the
  chamber is simply present, cold and clear. (Reduced motion changes
  almost nothing here — the plunge was already the stillest room.)
- **Performance budget & mobile variant.** The cheapest element in the
  theme: one class toggle and a 150ms transform. Mobile: identical;
  the snap is the one ceremony the phone keeps at full strength,
  because it costs nothing and means everything.
- **Choreography timeline (v2).** q=threshold approach: lerp easing
  0.09 → 0.18 over 600ms → q=centre: vapour cut, `--temp` locks 0.00 →
  t=0–150 settle → t=150 stillness; §6.4's fifth notch lights and
  14° prints in the same beat.
- **State matrix (v2).** *Rest (in plunge):* locked, still. *Hover /
  focus:* plunge timings (hover states ≤150ms, §6.14). *Active:*
  instant. *Scrolled-past (above):* lock released, loop re-warmed.
  *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** All breakpoints: identical. The plunge does
  not simplify; it is already simple.
- **Edge cases & failure modes (v2).** *Direct anchor arrival in the
  plunge* (a booking link from another page): the chamber loads
  already plunged — lock set, no snap performed; a bather who enters
  by the side door is simply already in the water. *Plunge as the
  first chamber* (a booking-only page): the whole page sits at
  `--lerp-cold`; §7's booking map covers this. *Oscillating scroll at
  the threshold:* the lock has 4% hysteresis so the climate cannot
  flicker.
- **Accessibility spec (v2).** The snap changes no content, order or
  focus. The settle is transform-only and disabled under reduced
  motion. The chamber's arrival is conveyed to assistive tech by its
  heading and `aria-current` on §6.4, as every chamber's is.
- **Tokens consumed (v2).** `--plunge`, `--ease-plunge`,
  `--dur-snap` (150ms), `--lerp-cold` (0.18), `--temp`.


### Page-family elements

### 6.11 The attendant's announcements (page family: navigation)

- **What & why.** Navigation in this house is an attendant who
  announces rooms. The header is a slim marble bar carrying the
  house's name and the five chamber links in ritual order, each
  lettered with its temperature; and at the head of every chamber, the
  announcement itself: the chamber name in Cormorant, its temperature
  in ledger figures, and its ritual instruction in italic — announced
  by a stagger in which the name settles first, the temperature counts
  up (§6.17), and the instruction fades in last, like an attendant
  speaking after the door opens. It belongs because a bather is never
  left to guess which room they are in or how hot it is.
- **Structure.** Header: `<nav class="attendant-bar">`, house name
  left, chamber links right, each link "THE WARM ROOM · 38°" in
  apparatus. Announcement: a `<header class="announcement">` at each
  chamber's head — `<h2>` name, `<output>` temperature, `<p>`
  instruction — in DOM order, complete from first paint; the stagger
  is JS-armed transforms only. The current chamber's header link
  carries a stone-deep rule and `aria-current`.
- **Motion spec.** Trigger: chamber entry (its announcement crossing
  60% viewport height). Name: settles 8px over 500ms `--ease-drift`.
  Temperature: counts from the previous chamber's figure to this one
  over 700ms (§6.17's stepped count). Instruction: opacity 0 → 1 over
  600ms beginning at t=350. The header bar's current-link rule slides
  between links over 400ms `--ease-vein` as chambers change. The whole
  announcement completes within 1050ms and never repeats within a
  chamber visit.
- **States.** *Rest:* announced, still. *Hover (link):* the link's
  temperature warms stone-deep → ink (150ms). *Focus:* hover parity +
  §11 ring. *Active:* jump to the chamber (anchor; no wipe, §6.2's
  rule). *Scrolled-past:* announcements stay announced. *Disabled:* a
  chamber with no section is absent from the bar. *Touch:* the bar
  compresses to the house name + the thermometer chip (§6.4); chamber
  links live in the chip's list.
- **Content merge.** The announcement is the chamber's own heading —
  navigation and content share one utterance. The header links are
  the same names, temperatures and order as the announcements and the
  thermometer: three printings of the ritual object, audited in §10.
- **Failure fallback.** No JS: announcements stand complete, the
  header's first link carries the static current rule (the steam
  room — where a static visitor stands). The count stands at the true
  figure.
- **Reduced-motion variant.** Announcements appear whole; temperatures
  print at value; the header rule jumps.
- **Performance budget & mobile variant.** Trivial: three small
  animations per chamber, one sliding rule. Mobile: header compresses
  as above; announcement type scales per §3's clamps; the stagger
  tightens (name 350ms, instruction at t=200).
- **Choreography timeline (v2).** t=0 announcement crosses 60% →
  t=0–500 name settles → t=100–800 temperature counts → t=350–950
  instruction fades → t≈600 header rule begins its slide → t=1050 the
  room is announced and still.
- **State matrix (v2).** As States above; *scrolled-past:* the header
  rule stays on the deepest chamber reached until the visitor scrolls
  back into an earlier one, when it migrates — current means stood-in,
  not furthest (contrast §6.4's fill, which remembers furthest; the
  two instruments answer different questions and §10 audits that they
  are not confused).
- **Breakpoints (v2).** ≥1200px: full bar + margin announcements.
  768–1199px: bar without the margin (announcements in-flow).
  <768px: compressed bar + chip; announcements in-flow, stagger
  tightened.
- **Edge cases & failure modes (v2).** *Chamber names too long for
  the bar:* names shorten to their apparatus form ("WARM · 38°") —
  the temperature is never the part dropped; a link that loses its
  figure has lost its announcement. *Mid-page load (refresh at the
  tepid chamber):* that chamber announces on load; earlier chambers
  stand announced.
- **Accessibility spec (v2).** Header is a `<nav aria-label="Chambers">`;
  links named "The Warm Room, 38 degrees". Announcements are the
  chambers' real headings (`<h2>`), so the heading outline is the
  ritual outline. `aria-current="true"` on the stood-in chamber only.
- **Tokens consumed (v2).** `--marble`, `--stone-deep`, `--ink`,
  `--ease-drift`, `--ease-vein`, `--dur-announce` (500ms).

### 6.12 The slab hero composition (page family: hero)

- **What & why.** The first screen is the göbek taşı: a great warm
  marble slab, centred, filling the viewport's middle, on which the
  headline rests (§6.1) and across which the vein draws (§6.7). Around
  it, the steam room's ground; above it, the attendant's bar (§6.11);
  beneath its lower edge, the first chamber's announcement beginning.
  It belongs because every bathhouse is organised around its slab —
  the hero is not a banner with a picture, it is the house's central
  stone, and the visitor's first act is to lie the headline down on
  it.
- **Structure.** A `<section class="steam-room">` (chamber 1) whose
  centre is `<div class="slab">`: marble ground, the arch (§4) as its
  top edge profile, the vein SVG (§6.7), the headline, and beneath the
  headline one line of apparatus — "FIVE CHAMBERS · 42° TO 14° · THE
  PLUNGE LASTS THREE MINUTES" — the ritual's whole span, generated
  from the ritual object, not typed. The slab occupies 62vh; the
  chamber pins for its 140vh (§5) with the slab centred through the
  first 60vh of the pin.
- **Motion spec.** The slab itself does not move — heated stone is
  still; its ceremonies are §6.1 (steam) and §6.7 (vein). Its parallax
  is the arch rate (0.94×, §6.3) applied to the chamber ground around
  it, so the room breathes past the stone. On pin release, the slab
  exits with the chamber through §6.2's wipe.
- **States.** *Rest:* steamed-then-clear (§6.1), veined (§6.7).
  *Hover / focus:* none of its own. *Scrolled-past:* the slab is gone
  with its chamber; returning re-enters through the wipe with the
  steam already clear (session rule, §6.1).
- **Content merge.** The slab carries the headline, the vein and the
  ritual's span line — it is the hero's content surface, not a
  backdrop. The apparatus line is real information (the five
  temperatures' range), generated from the same object as §6.4.
- **Failure fallback.** No JS: a marble slab, a headline, a drawn
  vein, a true line of apparatus. The hero loses its doorway and
  keeps everything else.
- **Reduced-motion variant.** Clear, veined, still — the printed
  slab.
- **Performance budget & mobile variant.** The slab is flat colour +
  one SVG; no photographic marble is permitted (§9 — a marble photo
  texture is a confession the drawing didn't happen). Mobile: slab
  54vh, apparatus line wraps to two lines, vein per §6.7's mobile
  rule.
- **Choreography timeline (v2).** t=0 load → §6.1's emergence runs
  0–3000 → §6.7's vein draws 900–2600 → pin holds the slab centred
  through 60vh of scroll → chamber exit through §6.2.
- **State matrix (v2).** *Rest:* as above. *Hover:* none. *Focus:* the
  headline's chamber link (§6.1) may sit in the slab's apparatus line;
  its focus completes the emergence. *Active:* n/a. *Disabled:* n/a.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: slab 62vh, margin thermometer
  visible. 768–1199px: slab 58vh. <768px: slab 54vh, no pin (chamber
  scrolls naturally), apparatus wraps.
- **Edge cases & failure modes (v2).** *Very short viewport
  (landscape phone):* the slab's min-height is 420px and the chamber
  unpins — the ritual yields to the device rather than trapping the
  bather. *Headline at maximum length:* two lines (§3) still fit the
  slab at 62vh; if not, the slab grows — the stone is cut to the
  title, never the title cropped to the stone.
- **Accessibility spec (v2).** The slab is a `<section>` labelled by
  its headline (`<h1>`). The vein is `aria-hidden`. The apparatus
  line is real text, read in order.
- **Tokens consumed (v2).** `--marble`, `--steam`, `--stone`,
  `--ease-drift`, the arch path (§4).

### 6.13 Treatment cards (page family: cards / listing)

- **What & why.** In the warm room, the treatments are cards of
  marble: each carries its name in Cormorant, its duration and
  temperature in ledger figures, two lines of the house's prose, its
  condensation (§6.8), its pour (§6.9), and a select control lettered
  like an attendant's offer — "TAKE THIS TREATMENT". Cards are cut
  into the chamber wall in a grid with marble showing between them;
  there are no floating rounded rectangles in the bathhouse. It
  belongs because the warm room is where the bather lingers and
  chooses, and the choosing is done by hand, on warm stone.
- **Structure.** A `<ul class="treatments">` of `<li><article
  class="treatment">`: title, apparatus line (duration · temperature
  · capacity), prose, condensation layer (§6.8), glow layer (§6.9),
  and a real `<button aria-pressed>` select control. The card's arch
  (§4, squat form) caps its top edge. Cards are generated from the
  house's treatment data; a treatment's printed temperature is its
  room's temperature from the ritual object (§1's law).
- **Motion spec.** Entry: each card's arch opens per §6.5 as the grid
  crosses; cards in a row stagger by 120ms. Hover/focus: §6.8's wipe.
  Activation: §6.9's pour + the chosen rule. Nothing else moves on a
  card — marble with two weathers (steam, warmth) is enough.
- **States.** *Rest:* condensed (§6.8), unchosen. *Hover:* wiping.
  *Focus:* wiped + ring. *Active/selected:* poured, resting warmth,
  ember rule, CHOSEN line printed. *Scrolled-past:* session states
  persist (wipe memory, selection). *Disabled:* a fully booked
  treatment — card clear, cool, control disabled, apparatus line
  amended "FULL TODAY" in the attendant's voice (§12), never greyed
  into illegibility (contrast holds at §2 pairings).
- **Content merge.** Every animated layer on the card belongs to the
  card's own treatment: the condensation is its room's air, the pour
  is its selection, the figures are its real duration and temperature.
  A card animation that could be moved to another card unchanged
  would fail §1's spirit; the pour's origin point and the wipe's patch
  are this card's, under this hand.
- **Failure fallback.** No JS: cards stand clear (condensation layer
  absent), select buttons work as toggles with the CHOSEN line
  printed by the server state or not at all — the list is fully
  readable and operable as plain HTML with the booking form (§6.14)
  carrying selection by radio if scripting is absent.
- **Reduced-motion variant.** No condensation, no pour spread; hover
  lifts nothing; selection shows by rule + CHOSEN line instantly.
- **Performance budget & mobile variant.** ≤6 cards per viewport
  (§4); layers are gradient/mask only. Mobile: one column; the arch
  cap flattens (springing 38%); the two-tap grammar (§6.8) applies.
- **Choreography timeline (v2).** Grid entry: arches open staggered
  120ms per card → rest condensed → visitor's wipe/pour per §6.8/§6.9
  timelines → on chamber exit, cards keep their session states.
- **State matrix (v2).** As States above, with touch: first tap
  clears, second tap selects/pours; focus parity via the button.
- **Breakpoints (v2).** ≥1200px: 3 columns, 90px wipe patch.
  768–1199px: 2 columns, 75px patch. <768px: 1 column, whole-face
  clear.
- **Edge cases & failure modes (v2).** *A treatment with no
  temperature* (a dry treatment — a haircut in the cool room): its
  apparatus line prints duration and capacity only; the build never
  invents a degree to fill the line (§1). *Very long treatment name:*
  Cormorant wraps to two lines and the arch cap grows; the figures
  line never wraps. *Grid re-flow on filter:* surviving cards keep
  their session states by treatment id, not by position.
- **Accessibility spec (v2).** List semantics; each card's button is
  labelled "Take the Kese Scrub, 25 minutes" (name + duration, not
  "select"). Chosen state via `aria-pressed` and the printed line.
  Touch targets ≥44px. The condensation and glow layers are
  `aria-hidden`.
- **Tokens consumed (v2).** `--marble`, `--ink`, `--stone-deep`,
  `--ember`, `--vapour`, `--ease-pour`, plus §6.8's and §6.9's tokens.

### 6.14 The plunge booking form (page family: forms / conversion)

- **What & why.** The booking lives in the plunge and behaves like
  cold water: fields are inscription lines on the deep ground, errors
  are stated plainly and instantly, and submission is a plunge — one
  decisive press, a 150ms snap, and the confirmation stands in the
  cold, lettered like a temperature. It belongs because the ritual has
  been cooling toward this ask for five chambers; a warm, lingering,
  multi-step checkout here would betray the whole descent. One form,
  one press, no steps, no upsell — the plunge is not a funnel.
- **Structure.** A `<form class="plunge-form">` on `--plunge`: fields
  for name, contact direction (email or phone), chamber-visit choices
  as ruled radio lines (the treatments chosen in §6.13 arrive
  pre-marked, editable), date and hour as native inputs restyled to
  the inscription grammar, and one submit block lettered "PLUNGE —
  BOOK THE RITUAL". Labels are apparatus above each line; the price
  total is printed above the submit, computed from the chosen
  treatments' real prices, in ledger figures.
- **Motion spec.** All timings are plunge timings (§6.10): focus
  lights the field's rule steam-white over 120ms `--ease-plunge`;
  validation on blur answers within 150ms; the submit press is a 2px
  press over 120ms `--ease-plunge` with the block's ember edge
  flashing once. On submit, the form does not spinner (§11 refuses
  spinners): the block letters "—" for the duration of the request,
  capped by a 4000ms watchdog that restores it with the failure note.
  On success, the form is replaced over 150ms (a cut, not a fade) by
  the confirmation (§12's voice) with its reference.
- **States.** *Rest:* lines at slate 40%. *Focus:* rule lit, label
  steam. *Error:* rule in ember, note beneath in the house's error
  voice, persistent until corrected — errors in the cold are not
  timed away. *Submitting:* block lettered "—", fields locked but
  readable. *Success:* confirmation. *Failed submit:* nothing cleared;
  the note above the form reads §12's fixed failure string; the block
  un-presses.
- **Content merge.** The form is the plunge's content — there is
  nothing else in the chamber competing with it (§4's density law),
  and its choices are the very treatments the visitor warmed in §6.13.
  The confirmation's reference and details are the booking itself,
  printed in the footer record's grammar (§6.15).
- **Failure fallback.** No JS: the form posts natively and the server
  returns the confirmation as a page — the plunge works with the
  plumbing off. Failed network: §12's failure note, fields kept
  verbatim (rehearsed in §10, gate 7).
- **Reduced-motion variant.** Identical, minus the press travel: the
  plunge was already nearly still (§6.10).
- **Performance budget & mobile variant.** No animation budget beyond
  rule colour and the press; the form must answer within one frame on
  a low-power phone. Mobile: single column, native date/time inputs
  keep their platform pickers (the house does not rebuild a calendar
  in marble), submit block full-width ≥52px tall.
- **Choreography timeline (v2).** Entry: the chamber's snap (§6.10)
  → form stands → visitor's focus lights rules at 120ms → submit
  press 120ms → request (≤4000ms watchdog) → success cut 150ms →
  confirmation stands with reference, and §6.15's record gains its
  line when the visitor scrolls on.
- **State matrix (v2).** *Rest / hover:* hover on the submit warms its
  ember edge (150ms) — the one warm thing in the cold room, rationed
  to the ask. *Focus:* rule lit + §11 ring. *Active:* the press.
  *Disabled:* the submit is disabled only while submitting; fields are
  never disabled at rest. *Touch:* identical timings; targets ≥48px.
- **Breakpoints (v2).** ≥1200px: two-column fields (name/direction,
  date/hour), choices full-width. 768–1199px: two columns for the
  short fields only. <768px: one column throughout.
- **Edge cases & failure modes (v2).** *Arrival with nothing chosen
  in §6.13* (direct link to booking): the choices stand unmarked and
  the form's head line says, in the attendant's voice, "No treatment
  chosen yet — the rooms are above, or choose here." — the form never
  pre-selects on the visitor's behalf. *Price change mid-session:*
  the total recomputes and the change is printed beside it ("The
  Kese Scrub is now 900 — the house changed its list at noon.") —
  totals never change silently in the cold. *Double submit:* the
  block locks on first press; a second press is impossible, not
  merely ignored.
- **Accessibility spec (v2).** Real `<label>`s, `aria-describedby`
  for error notes, errors announced via a polite live region once —
  in the cold, once is enough. Focus order is field order. Contrast:
  steam on plunge 10.06:1, steam-dim 8.11:1, ember rule graphical
  only (errors are also text, never colour alone).
- **Tokens consumed (v2).** `--plunge`, `--plunge-ink`, `--steam`,
  `--steam-dim`, `--slate`, `--ember`, `--ease-plunge`, `--dur-snap`
  (150ms).


### 6.15 The cooling-room footer (page family: footer)

- **What & why.** After the plunge, the bather rests in the cooling
  room — and so does the page. The footer sits on `--plunge-ink`, the
  deepest ground, and keeps the house's record: the five chambers with
  their temperatures (the ritual object, printed a third time), the
  house's facts (address, hours, the water's source), and — if a
  booking was made — the session's own line: "You entered at 42° and
  booked the plunge at 14°." It belongs because a ritual ends with a
  record, and because §10's three-records audit needs a third printing
  of the temperatures to check the other two against.
- **Structure.** A `<footer class="cooling-room">`: a drawn rule
  (§6.7's grammar, one line, `--ease-vein`), then three columns — the
  ritual (five chamber links with temperatures), the house (facts in
  prose), the record (the session line, present only when true) — and
  a colophon line in apparatus. All links are real; the record line is
  generated from session state, never typed.
- **Motion spec.** Trigger: footer entry. The rule draws over 900ms
  `--ease-vein`. Nothing else moves — the cooling room is stiller even
  than the plunge (§4); columns stand. The record line, when it
  exists, is simply present.
- **States.** *Rest:* drawn, still. *Hover:* links warm steam-dim →
  steam (150ms, plunge timing — the footer is a cold room). *Focus:*
  parity + ring. *Scrolled-past:* still. *Disabled:* n/a. *Touch:*
  links stack, targets ≥44px.
- **Content merge.** The footer is the ritual's record, not its
  sitemap-with-widgets: every column is the house's own facts, and the
  session line is the visitor's own visit, honestly reported — the
  theme's confession, as the indigo footer confesses its dips.
- **Failure fallback.** No JS: the rule stands drawn, the record line
  is absent (a static visit keeps no session — the footer does not
  pretend otherwise), all facts and links present.
- **Reduced-motion variant.** Rule drawn at first paint; all else
  identical.
- **Performance budget & mobile variant.** One path draw. Mobile:
  columns stack in ritual order — ritual, record, house — because the
  record of the visit outranks the house's facts on a small screen.
- **Choreography timeline (v2).** t=0 footer top enters → t=0–900
  rule draws → rest. If a booking completed above, the record line is
  already in the DOM when the footer is reached — records are written
  when the act happens, not when they are read.
- **State matrix (v2).** *Rest / hover / focus:* as above. *Active:*
  links navigate (§6.16's steam pass). *Scrolled-past:* still.
  *Disabled:* a chamber link to a section the page doesn't have is
  absent (§6.4's rule, applied here too). *Touch:* as above.
- **Breakpoints (v2).** ≥1200px: three columns. 768–1199px: two
  columns (ritual + record, house below). <768px: stacked, ritual
  first.
- **Edge cases & failure modes (v2).** *No booking made:* the record
  column holds the house's standing line instead — "The plunge is
  taken at 14°. The water keeps." (§12's fixed string) — never an
  empty column, never a fabricated visit. *Visitor who only visited
  two chambers:* the record line, if printed at all, reports only
  what happened ("You rested in the warm room.") — the record does
  not round a visit up to a ritual.
- **Accessibility spec (v2).** A `<footer>` with labelled `<nav>` for
  the ritual column; the record line is plain text in reading order.
  Contrast: steam on plunge-ink ≈12.4:1; steam-dim on plunge-ink
  audited ≥7:1.
- **Tokens consumed (v2).** `--plunge-ink`, `--steam`, `--steam-dim`,
  `--stone`, `--ease-vein`, `--dur-rule` (900ms).

### 6.16 Steam skeleton + steam-pass transition (page family: loader / transition)

- **What & why.** Waiting in this house is standing in steam, briefly:
  a loading section shows its chamber's ground with a soft vapour veil
  and its announcement printed (name and temperature — the room is
  known before its contents arrive), and navigation between pages is
  a steam pass — vapour rises, the page changes beneath it, the vapour
  thins on the new room. It belongs because the theme's threshold
  substance is the honest way to mark an in-between state: the visitor
  is between rooms, and the house says so with its own air.
- **Structure.** Skeleton: the loading chamber's real `<section>` with
  its announcement (§6.11) complete, its content region veiled by a
  `--vapour` layer at .5 with the content's block shapes (marble
  blocks in the content's real layout) beneath. Transition: a
  full-viewport vapour layer, `pointer-events: none`, armed only
  during a same-site navigation.
- **Motion spec.** Skeleton: the veil breathes once (opacity .5 → .65
  → .5 over 2400ms `--ease-steam`) and clears the moment content
  lands, over 400ms; a 6000ms watchdog clears it regardless — a room
  that never fills is shown empty with its §6.18 dry-room line rather
  than steamed forever. Transition: vapour rises 0 → .9 over 300ms
  `--ease-steam`, the navigation swaps beneath the peak, and the new
  page thins 0 over 600ms — total ≤900ms, and the new page's own §6.1
  (if it is a home page) does not re-run: the pass *is* its doorway.
- **States.** *Veiling → clearing → clear* (skeleton); *rising →
  peak → thinning → clear* (transition). A navigation that fails
  mid-pass thins the vapour back onto the original page with its
  state intact — the visitor is returned to the room they were in,
  never left in the corridor.
- **Content merge.** The skeleton veils the actual section in its
  actual layout, announced by its actual name and temperature; the
  pass joins two actual rooms of the same house. Neither is a generic
  loading screen wearing the theme's colours.
- **Failure fallback.** No JS: no skeleton (content is server-rendered
  or the section stands with its announcement and a plain "The room
  is being prepared." line), and navigation is a plain page load.
  Watchdogs as above; `transitionend` never trusted.
- **Reduced-motion variant.** No veil, no pass: sections appear when
  ready; navigation is instant. The announcements still identify every
  room.
- **Performance budget & mobile variant.** One layer, opacity only.
  Mobile: the pass shortens to 600ms total; skeletons veil at .4.
- **Choreography timeline (v2).** Skeleton: t=0 announcement printed,
  veil at .5 → breath cycle 2400ms → content lands → 400ms clear →
  §6.5's arch opens the arrived content. Transition: t=0 click →
  t=0–300 rise → swap at peak → t=300–900 thin → new room announced.
- **State matrix (v2).** *Rest:* clear. *Hover:* none. *Focus:* focus
  is never held inside a veiled region; on transition, focus moves to
  the new page's heading at the swap. *Active:* n/a. *Disabled:* a
  section whose content failed stands as §6.18. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: as specified. 768–1199px: pass 800ms.
  <768px: pass 600ms, skeleton veil .4.
- **Edge cases & failure modes (v2).** *Slow content in one chamber
  only:* only that chamber veils; the ritual around it stands clear —
  steam is local weather, never a site-wide outage costume. *Back
  button during a pass:* the pass cancels, vapour thins onto the
  restored page. *Prefetch making navigation instant:* the pass is
  skipped below 150ms of actual wait — steam is not performed for a
  door that is already open.
- **Accessibility spec (v2).** The veiled region is `aria-busy="true"`
  with its announcement readable; the pass is `aria-hidden` and the
  new page's heading receives focus at the swap (the one licensed
  focus move in the theme, because the page itself changed).
- **Tokens consumed (v2).** `--vapour`, `--marble`, `--ease-steam`,
  `--dur-pass` (900ms), `--dur-skeleton-law` (6000ms).

### 6.17 Ritual figures — temperatures & durations (page family: data)

- **What & why.** The house's numbers — chamber temperatures,
  treatment durations, capacities, the plunge's three minutes — count
  to their values when their chamber is announced, in Alegreya Sans
  tabular, stepped like an instrument settling. It belongs because in
  this house a figure is a reading taken at a moment, not a digit
  printed on a wall: the thermometer's mercury and the attendant's
  announcement both *arrive* at the number. And every figure obeys
  §1's law — it counts to the ritual object's value or the house's
  real published datum, never to a number chosen for its shape.
- **Structure.** Each figure is an `<output class="figure">` (or a
  tabular `<span>` inside prose) carrying its final value in the DOM;
  the count is a JS-armed text replacement across stepped frames,
  generated from the ritual object (temperatures, durations) or the
  page's data (capacities, counts of treatments).
- **Motion spec.** Trigger: the figure's chamber announcement (§6.11)
  or the figure entering at 70% viewport height. Temperatures count
  from the previous chamber's temperature (the instrument's last
  reading — 42 → 38 descends, as the bather cools) over 700ms in
  1° steps at ~35ms intervals, `--ease-drift` applied to the step
  timing (steps quicken slightly as the value nears). Durations and
  capacities count from 0 over 600ms in whole units. A figure counts
  once per session.
- **States.** *Printed* (DOM default, final value) → *counting*
  (armed only) → *read* (final value, permanent). Hover/focus: none —
  readings do not respond to hands. Scrolled-past: read.
- **Content merge.** The figures are the chambers' and treatments' own
  data, printed where the data belongs (announcements, apparatus
  lines, the thermometer). The count's start value is itself a true
  reading (the previous chamber's temperature) — even the animation's
  path is honest.
- **Failure fallback.** No JS: figures stand at value. Watchdog: any
  count not finished by 900ms snaps to its value — an instrument that
  sticks is corrected, not watched.
- **Reduced-motion variant.** Figures print at value. Readings are
  information; only their settling rests.
- **Performance budget & mobile variant.** Text updates ≤30 per
  figure, ≤4 figures counting concurrently; trivially cheap. Mobile:
  identical (figures are small; the phone's bathhouse keeps its
  instruments).
- **Choreography timeline (v2).** With §6.11: t=100 count begins →
  steps at ~35ms, easing → t=800 value lands exactly and holds → the
  instruction fades in over it (t=350–950, §6.11).
- **State matrix (v2).** *Rest:* read. *Hover / focus / active:* none.
  *Scrolled-past:* read. *Disabled:* a figure with no source in the
  ritual object or house data is not printed at all (§1) — absence,
  not a placeholder zero. *Touch:* identical.
- **Breakpoints (v2).** All breakpoints identical values and timings;
  figure size follows §3's apparatus scale.
- **Edge cases & failure modes (v2).** *Temperature counting up*
  (scrolling back to a warmer chamber): counts 14 → 28 → … from the
  current reading to the chamber's — the instrument re-reads honestly
  in both directions. *A figure whose value changes mid-session* (a
  treatment sells out, capacity 6 → 0): it re-counts once to the new
  true value with its apparatus line amended (§6.13's FULL TODAY) —
  figures track the house, not the first paint. *Rounding:* degrees
  are whole by the ritual object's definition; durations in whole
  minutes; a figure that needs decimals (a 22.5° pool) declares them
  in the object and counts in 0.5 steps — the object's precision is
  the page's precision.
- **Accessibility spec (v2).** Figures carry their final value to
  assistive tech throughout (the counting span is `aria-hidden`, with
  a visually-hidden final value beside it). Counts are never announced
  live.
- **Tokens consumed (v2).** `--ease-drift`, `--dur-count-temp`
  (700ms), `--dur-count-fig` (600ms), the ritual object.

### 6.18 The dry room (page family: 404 / empty state)

- **What & why.** Every bathhouse has a room the water never reached.
  The 404 is the dry room: a chamber with no steam, no arch opening,
  no temperature — its announcement line prints the name and, where
  the temperature belongs, a dash. One image arch stands empty, and
  the house's line is §12's fixed string: "This room is dry." Beneath
  it, the attendant's list of the rooms that do have water. It belongs
  because an error page in this theme should be a place in the house,
  not an apology from the web — and its dryness is only legible
  because every other room is wet.
- **Structure.** A single unchambered `<main class="dry-room">` on
  `--marble`: announcement grammar (§6.11) with the temperature
  replaced by "—°", one empty arch frame (the §4 path, unfilled), the
  fixed line in Cormorant, and the five chamber links with their true
  temperatures — the way back is lettered with the water's warmth.
- **Motion spec.** None, by law: no steam (§6.6's absence, total), no
  arch opening (the arch stands open and empty), no count (there is
  no temperature to count to). The only motion available is the
  links' hover warmth at plunge timing. The stillness is the message.
- **States.** *Rest:* dry, still. *Hover / focus:* link warmth + ring.
  *Active:* navigation (§6.16's pass — the one steam the dry room is
  allowed is the steam of leaving it). *Disabled:* n/a. *Touch:*
  identical.
- **Content merge.** The dry room is the house's own missing room: its
  announcement follows the house grammar with the one honest absence,
  and its links are the real chambers. It carries the error as
  content, not as a skinned 404 template.
- **Failure fallback.** The dry room is itself a fallback; it must
  render with no JS, no fonts and no images — text, the arch path and
  links only. If even the arch path fails, the room is a marble page
  with true words on it, which suffices.
- **Reduced-motion variant.** Identical — there is nothing to reduce.
- **Performance budget & mobile variant.** The lightest page on the
  site; it must load faster than any chamber. Mobile: the empty arch
  shrinks to 40vh; links stack full-width.
- **Choreography timeline (v2).** None — and that is specified, not
  omitted: t=0 the room stands dry. Any build that adds an entrance
  ceremony here has misunderstood the room.
- **State matrix (v2).** As States above; *scrolled-past:* the page
  rarely scrolls; if it does, nothing arms.
- **Breakpoints (v2).** ≥1200px: arch 56vh centred, links in a row.
  768–1199px: arch 48vh. <768px: arch 40vh, links stacked.
- **Edge cases & failure modes (v2).** *A sought treatment that
  exists but is fully booked:* that is not this room — it is §6.13's
  FULL TODAY state in the warm room; the dry room is only for what
  does not exist. *Search with no results:* the results area takes
  the dry room's grammar at section scale (dash temperature, fixed
  line, nearest chambers offered) rather than a generic empty state.
- **Accessibility spec (v2).** The heading is the announcement; the
  dash temperature is read as "no temperature" via a visually-hidden
  span (a screen reader must not be told "dash degrees"). HTTP status
  is a real 404.
- **Tokens consumed (v2).** `--marble`, `--ink`, `--stone-deep`,
  `--ease-plunge` (link timings), the arch path (§4).

## 7. Page application map

**Home — the full ritual.** All five chambers in order: steam (the
slab, §6.12, the house's welcome), warm (the treatments, §6.13, the
story), tepid (the rest — one image, ≤40 words, §8.2), cool (the
practicalities: hours, prices, what to bring, questions answered
plainly), plunge (the booking, §6.14). The footer record (§6.15)
closes the visit. This is the only page type that must have all five
chambers; it is the ritual the other pages abbreviate.

**Listing (treatments) — the warm room, extended.** A listing page is
the warm chamber at greater length: its own announcement (the
temperature is the warm room's 38° — the listing *is in* that room),
the full treatment grid (§6.13) with its condensation and pours, and
the plunge one link away at all times (the attendant's bar carries
"PLUNGE · 14°" — a ready bather is never made to re-walk the ritual
to book). Listing pages do not re-run the steam room; a returning
bather enters at the warmth.

**Detail (one treatment) — a side room off the warm chamber.** The
treatment at full size in its arch, its figures (§6.17), its rite
described in the house's prose, its neighbours at the foot ("Also in
the warm room"), and its select control pouring (§6.9) straight into
the plunge form (§6.14). The detail page's temperature is its room's;
a treatment is never promoted into the steam room for display.

**About — the house's history, told in the tepid room's quiet.** The
people, the water's source, the building's age — set sparely, one
image per idea, the emptiness law relaxed to 120 words per section
but the spirit kept: the about page is where the house rests its
voice. The ritual-object declaration (how temperatures are set, when
they are reviewed) lives here in long form — the methodology is
deliberately deep; casual visitors don't need it, committed ones
rest with it.

**Booking — the plunge only.** §6.14's form on its own page, reached
by the ritual or directly: a direct arrival lands already plunged
(§6.10's side-door rule) with the warm rooms one link up. The booking
page has no steam room and no warm room — depth is the home page's
argument, not a toll gate on every route.

**The dry room (404).** §6.18, everywhere, unchanged.


## 8. Worked examples

### 8.1 The hero — entering the steam

*The commission: a working hammam and bathhouse, "The Marble House";
the home page's ritual runs steam (the welcome) → warm (treatments) →
tepid (the rest) → cool (practicalities) → plunge (booking). Ritual
object: 42° / 38° / 34° / 28° / 14°, declared once, printed by §6.4,
§6.11 and §6.15.*

- **The composition (§6.12).** First screen: steam-room ground. The
  attendant's bar across the top — THE MARBLE HOUSE, and the five
  chambers with their temperatures. Centre: the slab, 62vh of warm
  marble under its arch, the headline "Bathe in order." in Cormorant
  at 84px, and beneath it the apparatus: "FIVE CHAMBERS · 42° TO 14° ·
  THE PLUNGE LASTS THREE MINUTES" — five, 42 and 14 generated from the
  ritual object; three minutes the house's real plunge guidance.
- **The ceremony.** Fonts ready at t≈110ms: the steam blooms to t=600,
  thins across 600–3000 (§6.1); the vein begins under the thinning
  vapour at t=900 and lands its branch by t=2600 (§6.7); the headline
  sharpens and its letters condense into their final spacing by
  t=3000. A visitor who never scrolls has still received the whole
  contract: the house's name, its method ("in order"), its span of
  temperatures, and a finished slab of veined marble.
- **Scroll timeline.** 0–40px: nothing moves but the thermometer
  (§6.4) waking in the margin. 40–200px: the chamber ground cools a
  breath (§6.3's within-chamber drift) and the wisps (§6.6) rise at
  full density around the slab. At the pin's release the doorway
  steams (§6.2) and the warm room is announced.

### 8.2 Mid-page — the tepid rest

*The same page, mid-ritual: the tepid chamber, 34°, holding the
house's single resting image — the empty warm room at opening time —
and almost nothing else.*

- **Entry.** The warm room's treatments fall behind through the wipe
  (§6.2, density peaking as the threshold arch centres). The tepid
  announcement (§6.11) settles: "THE TEPID ROOM", the count descending
  38 → 34 (§6.17 — the instrument cooling between rooms), and the
  instruction: "Nothing is asked of you here." (§12's fixed string.)
- **The chamber itself.** One arch image, 70vh, parallaxing at the
  arch rate against the chamber ground (§6.3). Text, counted and
  within the law (§4): the announcement (9 words), the instruction
  (6), and one line of the house's prose beneath the image — "The
  marble keeps the morning's warmth until noon." (8) — 23 words in
  the whole room. Three wisps (§6.6) cross the chamber in the time it
  takes to scroll it. There is no button. There is nothing to click.
  The absence is the content, and the visitor who rests here arrives
  at the cool room actually rested — the theme's whole argument in
  one quiet screen.
- **What the visitor feels.** The page has stopped selling. After two
  chambers of vapour, treatments and choosing, a room that asks
  nothing is the most luxurious thing on the site — and the build's
  discipline (the word count, the missing CTA) is exactly what §10
  gate 5 protects.

### 8.3 Conversion — the plunge

*The same page's end: the cool room has given the hours and prices
plainly; the threshold to the plunge crosses.*

- **Arrival.** At the threshold's centre the wipe's vapour is cut, not
  thinned (§6.10); the loop's lerp snaps cold; `--temp` locks to 0;
  the chamber settles in 150ms and stands still: deep ground, the
  announcement "THE COLD PLUNGE · 14°" and its instruction — "Plunge.
  Do not hesitate." — and the form (§6.14), the treatments the visitor
  warmed in the warm room already marked among its choices, the total
  printed in ledger figures above the block.
- **The booking.** The visitor checks the hour: the rule lights in
  120ms. They mistype the direction (no @): on blur, within 150ms,
  the rule turns ember and the note stands beneath in the house's
  voice: "This direction will not carry — check the address before
  you plunge." (§12's error voice: a fact about water and addresses,
  not a scolding.) They correct it; the note clears. They press
  PLUNGE — BOOK THE RITUAL: the block presses 2px, the request runs,
  and the form is cut — not faded — to the confirmation: "BOOKED —
  THE PLUNGE, SATURDAY, 09:00. REFERENCE MH-2214. Your towel is kept
  at the desk." Scrolling on, the footer's record (§6.15) already
  holds the line: "You entered at 42° and booked the plunge at 14°."
- **Failure rehearsed.** If the post fails, nothing they wrote is
  cleared; the note above the form reads "NOT BOOKED — THE WATER
  REFUSED. YOUR WORDS ARE KEPT ABOVE." and the block un-presses. A
  visitor who bathed through five chambers for this form is never
  sent back to the steam room by a network blink (§10, gate 7).

## 9. Anti-slop — what makes THIS theme look cheap

1. **Stock-photo steam.** Photographic fog overlays, mist PNGs and
   spa-stock vapour pasted over sections. *Cure:* steam in this house
   is one substance — `--vapour`, a flat layer with a hard clear time
   (§6.1, §6.2, §6.16). If it has a photograph's texture, it is clip
   art wearing the theme.
2. **Steam that never clears.** A hero still fogged at ten seconds
   because the reveal "looked atmospheric". *Cure:* §1's law and the
   watchdogs — 3000ms is a hard limit measured by timer, and §10
   gate 1 measures it, not vibes it.
3. **Temperatures as decoration.** "42°" sprinkled beside content that
   is not the steam room; a contact page at "38°" because it felt
   warm. *Cure:* the ritual object and §10's temperature-truth audit —
   every degree on the page belongs to a chamber.
4. **The arch on everything, meaning nothing.** Arch masks applied to
   logos, avatars in a footer grid, map embeds — until the doorway is
   a sticker. *Cure:* §4 — the arch frames rooms and the images that
   live in them; small furniture (links, chips, the thermometer)
   stays unarched, and its rarity is what makes a threshold read as a
   threshold.
5. **Five pins as a scroll trap.** Chambers pinned so long the visitor
   is wading, or a sixth and seventh "chamber" added until the ritual
   is a corridor. *Cure:* §5 — five pins at 140vh, no more rooms than
   the ritual has, unpinning on short viewports (§6.12).
6. **Blur reveals everywhere.** Every card and image sharpening from
   blur on entry because the hero did it. *Cure:* §5's licence — blur
   exists only as steam (§6.1), with its clear-time law. A build that
   blurs a treatment card has put a camera in the bathhouse.
7. **Spa teal.** The palette drifting toward turquoise-and-white
   wellness stock because "spa = teal". *Cure:* §2's closed token
   list — the cold in this house is slate and plunge-deep, green-grey
   and near-black, never a swimming-pool turquoise.
8. **The middle chamber, filled.** A tepid room stuffed with
   testimonials "for balance" or SEO paragraphs. *Cure:* §4's
   emptiness law (≤40 words, counted) and §10 gate 5. The rest is the
   theme's signature; filling it is deleting the theme.
9. **A thermometer that lies.** Notches that fill by percentage, a
   figure that shows the scroll depth instead of the chamber, a gauge
   promising rooms the page doesn't have. *Cure:* one ritual object
   generating §6.4, §6.11 and §6.15, and §10's three-records audit.
10. **The pour on everything.** Warm glows on nav links, footer links,
    every button — until choosing means nothing. *Cure:* §6.9's
    construction law: only treatment cards carry the layer; the one
    other warmth is the plunge submit's edge (§6.14), rationed to the
    ask.
11. **Cormorant at caption size.** The ceremonial face set at 13px
    "for elegance", disintegrating into hairlines. *Cure:* §3's floor
    — Cormorant never below 20px; apparatus and captions are Alegreya
    Sans, always.
12. **A plunge that fades in.** The booking chamber arriving on a soft
    800ms fade like every other section. *Cure:* §6.10 — the plunge
    cuts and snaps at 150ms; a gentle plunge is a contradiction the
    gate (§10, gate 8) rejects.


## 10. Quality gate

**Blocking (any failure stops the build):**

1. **Steam-clear audit.** Every vapour layer on the page — hero
   (§6.1), wipes (§6.2), skeleton (§6.16) — is timed with the loop
   killed and with it running: no layer may veil content past 3000ms
   from its trigger, and the DOM with JS disabled contains no vapour
   at all. A layer that can outlive its watchdog fails.
2. **Temperature-truth audit.** Every temperature printed anywhere
   (announcements, thermometer, cards, footer, meta copy) traces to
   the ritual object's five declared values or is absent. A degree
   that belongs to no chamber fails.
3. **Three-records agreement.** The thermometer (§6.4), the chamber
   announcements and header (§6.11) and the footer record (§6.15)
   state identical chamber names, orders and temperatures — generated
   from one ritual object and verified by reading all three.
4. **No stranded content.** With JS disabled, the whole ritual reads:
   chambers announced, treatments legible, prices printed, form
   working. With JS on and the loop killed, every watchdog (§6.1's
   3000ms, §6.2's 1200ms, §6.5's 1000ms, §6.16's 6000ms) fires and
   clears its layer.
5. **Tepid emptiness.** The tepid chamber contains ≤40 words of text,
   one image, no call to action. Counted, not estimated.
6. **Contrast audit.** Text pairings only from §2's law, verified in
   the cleared state, in the fogged state for above-layer text
   (§6.8), in the warm state (§6.9), and at both poles of the
   temperature scrub (§6.3). Stone as text anywhere: fail.
7. **Form-keeping.** A failed submit (simulated network error) leaves
   every field exactly as written, with §12's failure note. Any build
   that clears the plunge form on error fails.
8. **Plunge crispness.** The plunge chamber contains no fade longer
   than 150ms, no wisps, no parallax, and its vapour (if any from the
   doorway) is cut, not thinned (§6.10). Softness in the cold fails.

**Standard (must pass, fixable in review):**

9. Density follows temperature (§4): warm room fullest, cool room
   compact, plunge holding only the booking.
10. Exactly five pins at 140vh (desktop); the refusal list (§5) is
    honoured — no marquee, no blur beyond steam, no kinetic type
    beyond §6.1's condense.
11. Ambient ration: wisp densities at or below the ritual object's
    caps (12/8/3/0/0), paused off-screen, absent under reduced motion.
12. The emergence and the vein run once per session and never re-run;
    the slab's apparatus figures match the generated counts.
13. Every interactive element is ≥44px, focus shows §6.8's cleared
    patch or §11's ring, and focus never travels through a wipe
    (§6.2).
14. Mobile: pins released, thermometer as chip, condensation by the
    two-tap grammar, plunge timings unchanged.

## 11. Component inventory

Every component a real Hammam site needs, with its themed treatment.
Components the theme refuses are listed with their in-house
replacement — a refusal without a replacement is a gap, not a stance.

| Component | Themed treatment |
|---|---|
| Primary button | The plunge block (§6.14): plunge ground, steam label in apparatus, ember edge on hover, 2px press on `--ease-plunge`. On light chambers, a marble block with ink label and stone-deep rule. |
| Secondary button | Ruled-line button: transparent, 2px bottom rule in the chamber's text colour; hover warms the rule toward `--ember` in warm chambers, lights it steam in cold ones. |
| Text input | Inscription line (§6.14): apparatus label above, 2px rule below, no box — on marble in warm chambers, on plunge in the cold. |
| Textarea | Ruled sheet: lines every 33px (the body line unit), Alegreya Sans 18px — a note left for the attendant. |
| Select | Refused as a dropdown. Choices are the attendant's list: ruled radio lines, the chosen one's rule warmed (§6.14's grammar generalised). Native `<select>` survives only inside the plunge form's date/hour, where the platform picker is the honest tool. |
| Checkbox | Towel mark: an unfilled square in stone-deep; filled = the square warms to `--ember` with a ground-colour tick. |
| Radio | Attendant's line: the chosen line's rule inks in the chamber's accent; the dot is a small filled circle of stone-deep. |
| Toggle / switch | Refused. The house has states of water, not switches; use two attendant's lines (With the ritual / The plunge only) as radios. |
| Card | Treatment card (§6.13): arch-capped, condensed, wipeable, pourable. |
| Table | The hours-and-prices table (cool room): real table, apparatus headers, no zebra striping — a marble rule every 6 rows at most. Plain, compact, cold-room honest. |
| Tabs | Refused. Rooms are not tabbed; chambers are walked (§6.11) or indexed (§6.4). A build needing tabs has two rooms arguing — separate them into chambers. |
| Accordion | The cubicle door: a treatment's detail expands downward like a door opening into a private cubicle — the row below gives way over 300ms `--ease-drift`; the heading gains a small arch glyph. |
| Modal / dialog | The private cubicle: a full-chamber overlay in the current chamber's ground, entered through its arch (§6.5), dismissed by its attendant's line ("Return to the warm room"). One at a time; the plunge form never lives in one. |
| Toast | Refused. News in this house is recorded, not toasted: transient confirmations appear as a one-line record entry at the chamber's foot, in the house's voice, and remain until the chamber is left. |
| Tooltip | Refused. Explanation lives in ritual instructions and context lines (§12); a treatment that needs a tooltip needs a better instruction. |
| Badge | Temperature chip: apparatus text on the chamber's ground — "38° · WARM ROOM" — the badge states where a thing is bathed, never a marketing claim ("POPULAR" is a steam-room word and is banned, §12). |
| Alert | The attendant's notice: a band in the current chamber, ember rule in the plunge / stone-deep rule elsewhere, message in §12's error voice, persistent until resolved. |
| Pagination | Room pagination: "The next room" / "The room before" links lettered with the chamber's name and temperature — never numbered pages; a ritual is continuous. |
| Progress bar | Refused. Progress is the thermometer (§6.4). |
| Spinner | Refused. Waiting is steam (§6.16). |
| Skeleton | §6.16's veiled chamber with its announcement printed. |
| Search | The attendant's enquiry: a single inscription line in the bar; results are returned as a chamber list — findings grouped by the room they live in, temperatures stated — a guided walk, not a result dump. |
| Breadcrumbs | Replaced by the thermometer's visited notches (§6.4) plus the bar's current rule (§6.11): the visitor's path is a temperature, not a trail of pages. |
| Skip link | "Skip to the plunge" / "Skip to the treatments" as a plain ink link appearing on first focus in the steam room. |
| Focus ring | 2px stone-deep outline on light chambers, 2px steam outline on plunge, offset 3px, on every interactive element; on treatment cards, focus also clears the condensation (§6.8). |
| Divider | A threshold (§4's arch band) or, within a chamber, a 2px rule in the chamber's text colour at 30%. Wavy SVG dividers are refused — that is a different theme's water. |


## 12. Content & copywriting voice

Two voices, cast like the type. **The Attendant** announces:
chamber names, temperatures, instructions, labels — brief, courteous,
certain, the voice of someone who has opened this door ten thousand
times and still opens it properly. **The House** writes prose:
treatment descriptions, the story, errors, confirmations — Alegreya
Sans, sentence case, unhurried and plain, the voice of the building
itself when the attendant is not speaking. The voices never swap: the
attendant never explains, the house never announces.

**Headline style.** Short, declarative, about the ritual — never
about the brand's greatness. ✓ "Bathe in order." / "The water is
ready at seven." ✗ "Indulge in the ultimate luxury wellness
experience!" (three banned moves in one line: indulge, ultimate,
exclamation). Exclamation marks are banned from the whole theme — a
bathhouse does not shout through steam.

**Label style.** Apparatus: room + temperature. ✓ "THE WARM ROOM ·
38°", "PLUNGE · 14°". ✗ "Section 2", "Step 4 of 5" (the ritual is
walked in rooms, not processed in steps — the thermometer counts
temperatures, not percentages).

**Instruction style.** One calm imperative or permission per chamber,
spoken by the attendant. ✓ "Enter slowly." / "Stay here a while." /
"Nothing is asked of you here." ✗ "Get ready for an amazing soak!!"
The instruction tells the bather how to be in the room, never what to
buy in it.

**Error voice.** A fact about the house, stated plainly, with the way
back. ✓ "This direction will not carry — check the address before
you plunge." ✓ "NOT BOOKED — THE WATER REFUSED. YOUR WORDS ARE KEPT
ABOVE." ✗ "Oops! Something went wrong 😞" (the house has no "oops",
and no emoji survives steam).

**Empty-state voice.** ✓ "This room is dry." / "No treatment is
taken at this hour — the warm room keeps its list above." ✗ "Nothing
found! Try again?" — the house does not blame the bather for the
house's empty room.

**Confirmation voice.** ✓ "BOOKED — THE PLUNGE, SATURDAY, 09:00.
REFERENCE MH-2214. Your towel is kept at the desk." ✗ "Success! 🎉
You're all set for your pamper session!" — a confirmation is a record
entry spoken by the attendant, not a celebration.

**Banned words:** indulge, pamper, detox, oasis, ultimate, luxury
experience, rejuvenate, wellness journey, oops, POPULAR (as a badge).
**Owned words:** chamber, steam, marble, slab, plunge, attend, rest,
rinse, stay, in order, the water, kept (for things the house holds
for you).

**Fixed strings (verbatim, do not paraphrase):** the tepid
instruction — "Nothing is asked of you here."; the plunge instruction
— "Plunge. Do not hesitate."; the dry-room line — "This room is
dry."; the form failure note — "NOT BOOKED — THE WATER REFUSED. YOUR
WORDS ARE KEPT ABOVE."; the footer's standing line — "The plunge is
taken at 14°. The water keeps."

## 13. Full-page scroll choreography map

The home ritual, top to bottom. Every beat in order; instruments run
continuously beneath the beats (temperature scrub §6.3 drifting,
thermometer §6.4 filling, wisps §6.6 rising in the warm rooms).

| Beat | Scroll zone | What happens | What the visitor feels |
|---|---|---|---|
| 1 | Load | Steam blooms and thins (§6.1); vein draws (§6.7); slab stands (§6.12) | Arriving through the door |
| 2 | 0–40px | Thermometer wakes in the margin (§6.4) | The instrument is live |
| 3 | Steam room in view | Wisps at full density (12); the ground cools a breath (§6.3) | Being in the steam |
| 4 | Warm threshold centres | Steam wipe peaks and thins (§6.2); warm room announced (§6.11) | Passing to the warmth |
| 5 | Warm room in view | Treatments condensed (§6.13); wipes and pours available (§6.8/§6.9); wisps at 8 | Lingering, choosing |
| 6 | Tepid threshold centres | Wipe; the count descends 38 → 34 (§6.17) | The house quietening |
| 7 | Tepid room in view | One image, 23 words, 3 wisps; nothing to click (§8.2) | Rest, actually given |
| 8 | Cool threshold centres | Wipe, thinner (the air is cooling); lerp begins easing cold (§5) | Rinsing; practicalities |
| 9 | Cool room in view | Hours and prices table; no wisps; type tightens (§3 law 3) | Clarity returning |
| 10 | Plunge threshold centres | Vapour cut, not thinned (§6.10); `--temp` locks 0; fifth notch lights, 14° prints (§6.4) | The cold, arriving |
| 11 | Plunge in view | Stillness; the form at plunge timings (§6.14) | The ask, in cold water |
| 12 | Footer enters | Rule draws (§6.15); the session's record line stands | The cooling room; the visit, recorded |

**Reverse pass.** Scrolling up: the ritual re-warms exactly — the
temperature scrub is a pure function (§6.3), wipes run in reverse
(§6.2), announcements stay announced, selections stay poured, the
thermometer's fill remembers the furthest depth while its figure
reports the room stood in (§6.4). The plunge's lock releases at its
threshold and the loop warms over 600ms. The only things that do not
reverse are the session's facts: what was chosen, what was booked.

**Jump-scroll catch-up.** Anchor jumps and flings: no wipes are owed
to a teleport (§6.2), chambers landed in stand announced and clear,
figures stand read, the thermometer snaps to the room stood in, and
the plunge — if landed in — is already locked (§6.10's side-door
rule).

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Total page weight (home) | ≤ 700KB, of which images ≤ 420KB (arch-cropped, one per chamber by the density law) |
| Fonts | Cormorant (1 weight) + Alegreya Sans (2 weights + italic) ≤ 110KB, `font-display: swap` |
| JS | ≤ 55KB gzipped (one loop, observers, wipe/pour state, form) |
| Shared-loop cost | ≤ 1.6ms/frame average; writes only transform / opacity / custom properties |
| Long tasks | None > 50ms after load; the emergence's timers are sliced per beat |
| Steam-clear latency | Any vapour cleared ≤ 3000ms from trigger (watchdog law, §1) |
| Active wisps | ≤ 12 page-wide, one chamber at a time (§6.6) |
| Backdrop-blur layers | ≤ 1 at any moment (§6.1 only; §6.2 uses opacity) |

**Cut order when the budget is exceeded** (cut in this order, record
each cut in the build notes):

1. Steam wisps (§6.6) — gone entirely; the air is clear, the ritual
   intact.
2. The vein's branch (§6.7) — the main vein still draws.
3. Within-chamber temperature drift (§6.3) — threshold steps only,
   the mobile treatment for all.
4. The steam-pass transition (§6.16) — navigation becomes instant
   with the announcement flash.
5. Condensation persistence (§6.8's .42 memory) — cards fog fully
   again; the wipe itself stays.
6. Arch parallax (§6.3's 0.94 layer) — arches move with their text;
   the scrub and thermometer stay.

**Never cut:** any watchdog, the thermometer, the temperature scrub's
threshold steps, the plunge snap, the form's error-keeping, any
reduced-motion variant. A build that cuts the honesty to keep the
atmosphere has inverted the theme.

## 15. Build-order checklist

1. Declare the ritual first: fix the five chambers, their order, each
   chamber's temperature, instruction and content assignment. Write
   the ritual object; everything else is generated from it.
2. Build the static bathhouse: all chambers, all content, figures
   printed, prices legible, form working — with no JS and no steam.
   This is the site; the rest is weather.
3. Set the palette tokens and pairing law (§2); audit contrast in
   every chamber before any motion exists, including the lamplight
   scheme.
4. Set the type scale, the Cormorant floor (§3 law: never below
   20px) and the per-chamber line-heights (§3 law 3).
5. Author the arch path (§4) — one geometry, reused at thresholds,
   cards and the dry room, at all breakpoints.
6. Build the instruments from the ritual object: thermometer (§6.4),
   attendant's bar and announcements (§6.11), footer record (§6.15).
   Verify the three-records agreement by reading all three.
7. Add the shared loop; wire the temperature scrub (§6.3) and the
   chamber-lerp switch (§5); calibrate: each threshold must cross as
   its chamber boundary crosses viewport centre.
8. Add the chambers' pins (desktop) and the steam wipes (§6.2) with
   their 1200ms watchdog and the fling/anchor rules; test with the
   loop killed.
9. Add the entrance ceremony: steam emergence (§6.1) with its 3000ms
   watchdog, vein draw (§6.7), slab composition (§6.12), session
   rules.
10. Add the arch openings (§6.5) with the 1000ms law.
11. Add the treatment weather: condensation (§6.8), pours (§6.9),
    cards (§6.13) with their session persistence and FULL TODAY
    states.
12. Build the cold end: plunge snap (§6.10) with its hysteresis,
    booking form (§6.14) with error-keeping rehearsed against a
    simulated network failure, footer (§6.15).
13. Count the tepid chamber's words (§4's law) and remove until it
    passes — this step is a deletion step, scheduled on purpose.
14. Add figures (§6.17), skeleton/transition (§6.16), the dry room
    (§6.18), and last — only if the budget survives — the wisps
    (§6.6).
15. Run §10 in full: steam-clear audit with the loop killed,
    temperature-truth audit, three-records agreement, no-JS read,
    tepid word count, contrast at both scrub poles, form-keeping
    rehearsal, plunge crispness. Gate signed by someone who did not
    build the page.
