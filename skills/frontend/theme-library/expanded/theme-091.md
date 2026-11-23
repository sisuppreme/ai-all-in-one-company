# 91. The Projectionist's Booth — Expanded (v1 + v2)

> Identity preserved exactly from the original entry: a silent-film cinema seen
> from behind the projector — the whole page is a reel of 1920s film, complete
> with sprocket holes, frame lines and the warm flicker of a carbon-arc lamp.
> The visitor sits in the booth, not the audience. Same four palette anchors —
> Booth black `#0E0C0A`, aged silver-screen cream `#E8DCC3`, arc-lamp amber
> `#C98A2D`, dusty grey-brown `#6E6257`. Same two fonts — **Limelight** (display)
> and **Special Elite** (captions, intertitles, body). All 11 original signature
> elements deepened, not redesigned, plus 7 page-family elements = **18 elements**,
> each with a full v1 build spec and every v2 deepening layer.

**The theme's one law — the strip is the record.** Every figure on the page —
feet of footage, frame counts, running time, showtimes, seats remaining — is
read off the strip itself: one declared **changeover sheet** (§6.17) prints the
reel count, the footage per reel and the projection speed, and every counter,
table and form on the page is a second printing of that one record. The footage
counter may only ever display footage the frames on the page actually contain;
a runtime may only be the arithmetic of the sheet (feet × 16 frames ÷ speed).
And the booth's second law, inherited from the original entry: **damage is
admitted, never hidden** — the burnt frame (§6.5) carries its wound in the open
with a caption that names it, and the splice (§6.6) shows the repair. A page in
this theme never airbrushes its own strip.

---

## 1. Concept & world

The visitor is not in the stalls. They are up the narrow stairs, behind the
small square window, standing next to a 1920s projector that is older than the
building's wiring. Everything they see arrives the way the projectionist sees
it: as film. The page is one vertical strip of 35mm — sprocket holes down both
edges, frame lines between sections, emulsion grain in the light, dust drifting
through the beam. Sections are not "sections"; they are frames on the strip,
and scrolling is the hand-crank: the strip advances under the visitor's hand
with the subtle mechanical catch of a gate pulling film down, frame by frame.

The mood is warm darkness and ritual. The page opens the way a programme
opened in 1924: countdown leader, an iris-in, a title card rising through
carbon-arc flicker. It admits its age proudly — one frame is burnt, one is
spliced, a hair occasionally gets into the gate — because in this world those
are not defects, they are provenance. A restoration studio's print is valuable
*because* its history is visible on the strip.

**The world in one paragraph, for the builder.** Booth black is the room.
Cream is the screen and the paper (cue sheets, intertitles, the changeover
sheet). Amber is the lamp — the only warm light source, and the only colour
allowed to mean "live, running, now". Dusty grey-brown is everything worn:
the gate, the reel cans, the booth's woodwork, captions that have faded with
handling. Nothing in this world is glossy, nothing is new, and nothing moves
smoothly — the machine's mechanics (steps, catches, jolts, flicker) are the
motion language, and a buttery digital glide anywhere on the page is a world
error, not a style choice.

**Best-fit sites and audiences.**

- **Film festivals with a repertory / revival strand** — the programme is
  literally a strip of films; each screening is a frame.
- **Restoration studios and archives** — the damage-and-repair grammar (§6.5,
  §6.6) is their daily work made visible; provenance is the product.
- **Vintage cinema venues and picture palaces** — a single-screen house whose
  whole offer is the ritual: leader, iris, intertitles, changeovers.
- **Silent-film societies, accompanist collectives, cinematheques** — audiences
  who know what a changeover cue is and will check the arithmetic.
- **Museum exhibitions on early cinema** — the booth is the exhibit; the page
  is a working demonstration, not a brochure.

**When NOT to use this theme.**

- **Multiplex / mainstream cinema chains.** A 14-screen booking funnel needs
  speed and seat-map density; the crank-stepped scroll (§6.3) would fight the
  transaction. Route checkout-density pages out (see §7).
- **Video-streaming products.** The theme's whole claim is physical film,
  projected once, in a room. A play-button grid betrays it instantly.
- **Bright, family-first entertainment brands.** The palette is a dark room
  and a warm lamp; it cannot do cheerful daylight without lying.
- **Content that must update at news speed.** The strip is printed; figures
  trace to one sheet (§6.17). A page whose numbers change hourly needs a
  different record-keeping metaphor.
- **Accessibility-critical public services.** Flicker-adjacent texture and a
  typewriter body face are wrong tools where the legal duty is maximal
  plainness — even with the reduced-motion variant, choose a plainer theme.

**The emotional promise.** *You are trusted with the machine.* The audience
sits in the dark and believes; the visitor to this page is shown the booth,
the cue sheet, the burnt frame and the splice — the whole apparatus — and the
page trusts them to find that more beautiful than the illusion alone.

---

## 2. Palette

Four anchors, exactly as the original entry specifies. No fifth colour may be
introduced; warmth, wear and damage are all rendered *inside* these four
(opacity, grain and texture do the work that extra hues do in other themes).

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--booth` | `#0E0C0A` | Booth black — the room, the strip's base, all ground | ~62% | Ground for everything. Cream on booth: **13.6:1** — the page's reading pair. Amber on booth: **6.1:1** — passes for large text and signals; never body copy under 14px. |
| `--screen` | `#E8DCC3` | Silver-screen cream — frames, intertitle cards, paper, body text | ~26% | The light surface. Booth ink on cream: **13.6:1**. Amber on cream: **2.5:1 — FORBIDDEN pairing** (lamp colour washes out on the screen; amber never sits on cream). Dust on cream: **4.9:1** — captions on cards only, ≥13px. |
| `--arc` | `#C98A2D` | Arc-lamp amber — the live colour: progress fill, record light, hover bloom, the one CTA family | ~7% | Signal-only discipline: amber always means *running / live / act now*. On booth 6.1:1. Never a background wash over text; never decorative borders at rest. |
| `--dust` | `#6E6257` | Dusty grey-brown — gate metal, reel cans, frame lines, faded captions, disabled states | ~5% | On booth: **3.3:1 — never text under 18px**, captions and rules only. On cream 4.9:1 (see above). The colour of everything worn by handling. |

**Derived tokens** (computed from the anchors; no new hues):

| Token | Value | Use |
|---|---|---|
| `--booth-raise` | `#171310` | Frame stock lifted one step from the room — card stock inside frames, the booth-window nav bar |
| `--screen-dim` | `#CBBd9F` | Cream at rest in secondary print — table rules, inactive intertitle cards in the pinned cycle |
| `--arc-hot` | `#E3A94B` | The lamp at full strike — hover bloom core, the record light's lit centre; used inside gradients only, never as flat text colour |
| `--arc-deep` | `#8F5E1B` | Amber in shadow — pressed button state, sprocket fill on the far rail |
| `--burnt` | `#3A2415` | The burnt frame's emulsion — a booth/arc midpoint, texture only, never text |
| `--gate-line` | `rgba(232,220,195,.16)` | Frame lines and hairlines on booth black |

**Dark-mode behaviour.** This theme *is* a dark room; there is no light-mode
inversion and none may be improvised. Under `prefers-color-scheme: light` the
page does **not** invert — a cinema booth at noon is still a booth. Instead the
"house lights half" ruling applies: `--booth` lifts to `#1B1712`, cream stays,
flicker amplitude (§5) halves, and the burnt frame's patch lightens one step so
it survives the brighter room. Under forced-colors mode, all texture, grain and
flicker are dropped, sprocket rails become 1px solid borders in CanvasText,
and the amber signal colour is replaced by the system's Highlight for the
progress fill and focus outline — the strip must remain legible as pure
structure.

**The flicker ruling.** Carbon-arc flicker (§5) is a *light* effect: it may
modulate a radial gradient's opacity over frames, never the opacity or colour
of text itself. The reading line — any glyph the visitor is meant to read —
sits outside the flicker layer at all times. If a build flickers the words,
it has failed the theme's first law test in §10.

---

## 3. Typography

Two families only, as the original entry specifies. **Limelight** is the
deco-cinema display face — it sets titles the way a 1924 title card was
lettered. **Special Elite** is the typewriter face of the booth's paperwork —
cue sheets, captions, intertitles and body text are all typed, because in the
booth everything that isn't lettered is typed.

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Programme title (hero) | Limelight | clamp(44px, 9vw, 96px) / 1.02 | +0.01em | Title-card setting: centred, cream on booth, never more than 3 lines; the title is lettered, so it never animates letter-by-letter (cards rise whole, §6.2) |
| Frame headline | Limelight | clamp(28px, 4.5vw, 44px) / 1.1 | +0.015em | One per frame; may carry the keyword swell (§6.7) only inside intertitle cards, never in headlines |
| Intertitle | Special Elite | 20–24px / 1.5 | +0.02em | Centred on its card, sentence case as typed; the key word swells (§6.7) — emphasis is acted, never bolded (Special Elite has no true bold; faux-bold is forbidden) |
| Body | Special Elite | 16.5px / 1.65 | +0.005em | Max measure 62ch inside a frame; typewriter face at small sizes tires — never under 15px for prose |
| Caption / cue note | Special Elite | 13.5px / 1.45 | +0.03em | Dust on booth or booth on cream; the booth's marginalia voice (§12) |
| Data (counter, tables) | Special Elite | 15–18px, tabular figures where the face allows; odometer digits are drawn as digit wheels (§6.4), not font tricks | +0.04em | All figures come from the changeover sheet (§6.17); numerals are never styled decoratively — a number is a reading from the machine |

**Five type laws.**

1. **Lettered or typed — nothing else.** No third family, no system-font
   fallback visible in the design (fallbacks: `Georgia, serif` for Limelight,
   `Courier New, monospace` for Special Elite, used only while loading).
2. **Emphasis is acted, not weighted.** The swell (§6.7), the amber underline
   of a cue mark, the strike-through of a corrected figure — never bold,
   never italic-synthetic.
3. **Numerals are readings.** Every number traces to §6.17. A decorative
   numeral (a giant "01" section marker) is forbidden — the strip already has
   frame numbers, and they are real: they count the frames on the page.
4. **Intertitles are centred; paperwork is left.** Cards centre their text
   like the screen did; tables, forms and the cue sheet align left like the
   typewriter did. The two alignments never mix inside one element.
5. **Type never flickers, jitters or burns.** Motion applies to cards, light
   and the strip — glyphs stay printed. The hair-in-the-gate (§6.11) moves
   the *strip* by 1px; the words ride it as print on film, which is the
   world's own logic.

---

## 4. Layout language

**The strip.** The page is one vertical strip of 35mm film, centred, maximum
content width **1120px** at ≥1200px viewport, flanked by the two sprocket
rails. Each section is a **frame**: a cream or booth-raise rectangle with a
4px frame line (`--gate-line` on booth, booth at 18% on cream) and a printed
frame number in its top-left corner (`FR. 04` — real ordinal of the frame in
the DOM, set by the build, never by script decoration). Frames are separated
by **splice gaps** of 56px of booth black carrying a single frame line — the
strip's breathing room is black, never cream.

**The rails.** Each sprocket rail is 44px wide at desktop: a column of
sprocket holes (14×18px rounded rectangles, booth-raise on booth, inset
shadow) pitched at 64px. The left rail is also the progress device (§6.4):
its holes fill amber as footage passes. The right rail is plain — one working
rail, one resting rail; symmetry would be decoration.

**Spacing rhythm.** The strip's unit is the **frame pitch**: vertical rhythm
in multiples of 16px inside frames, 56px splice gaps between them, 96px of
leader black before the first frame and after the last. Inside a frame,
padding is 40px desktop / 20px mobile. Nothing sits on the rails; content
never bleeds across a frame line — the frame is a hard border in this world,
unlike themes where elements overflow their sections.

**Density rules.** One idea per frame. A frame holds a headline *or* an
intertitle cycle *or* a table — never two competing centres. Dense content
(programme listings) is broken across consecutive frames (§6.13) rather than
shrunk. The booth is a small room: the layout is deliberately unhurried, with
black doing the separating that other themes do with whitespace.

**The booth window.** A fixed header styled as the booth's rear wall: the
venue name lettered small in Limelight, the frame-index navigation (§6.12),
and the footage counter (§6.4) pinned at the right — the projectionist's
instruments, always in reach, never scrolling away.

**Whitespace as material.** Black is this theme's whitespace and it is spent
like film stock: leader before the programme (the countdown needs darkness to
read against), splice gaps between frames, and a long black tail after the
final frame where the strip runs out into the footer (§6.18's territory). A
frame that touches the next frame with no splice gap has been edited wrong.

**Anatomy of one frame (build reference).** Every frame, whatever it carries,
is assembled from the same six parts, in this order: (1) the **frame line** —
a 4px rule, `--gate-line` on booth stock or booth at 18% on cream stock;
(2) the **frame number** — "FR. 04" typed at 12px in the top-left, 14px from
the corner, in `--dust` on booth or booth-ink on cream; (3) the **head room** —
28px of empty stock beneath the top line, where a real frame's image has not
yet begun; (4) the **picture area** — the still or card, inset 24px from the
frame's sides on desktop, 12px on mobile; (5) the **caption band** — a typed
line or two beneath the picture, separated by a hairline, where the booth
says what the picture is; (6) the **foot room** — 20px of stock before the
bottom frame line. A frame missing its number or its caption band is not a
variant; it is unfinished stock, and §10's frame census counts parts, not
intentions. Cream frames and booth frames share the anatomy exactly — the
stock changes, the cutting doesn't.

---

## 5. Full motion system

Motion in the booth is **mechanical**: the gate steps, the lamp flickers
irregularly, splices draw, irises open. Nothing eases like a digital
interface; everything moves like a machine with mass, a catch and a lamp.

**Named easings** (the only five; defined once, consumed by token name):

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-crank` | `cubic-bezier(.3,.7,.3,1)` + JS quantisation to frame steps | The gate pull: fast catch, brief settle | Frame advance (§6.3), rail fill, counter wheels |
| `--ease-iris` | `cubic-bezier(.65,0,.25,1)` | The iris diaphragm: slow open, decisive close | Iris wipe (§6.2), page transitions (§6.16) |
| `--ease-draw` | `cubic-bezier(.55,.06,.25,1)` | A line drawn by a steady hand | Splice line (§6.6), cue-mark underlines |
| `--ease-settle` | `cubic-bezier(.2,.9,.25,1.15)` | A reel can set down with one small overshoot | Cards landing, form confirmation, button press recovery |
| `--ease-flash` | `steps(2, end)` | The frame-line flash: two hard steps, no blend | Click flash (§6.10), record-light blink |

**The shared loop.** One `requestAnimationFrame` loop, lerp factor **0.12**,
drives every scrubbed value: crank position (§6.3), rail fill and counter
(§6.4), pinned intertitle cycle (§6.8), lamp bloom intensity (§6.9), parallax
of the scratch/dust layers. No scroll handler writes styles. The loop sleeps
when the tab is hidden or when nothing is in motion (dirty-flag), and it
quantises the crank channel to whole frame steps before writing.

**Motion terms, in this theme's language:**

- **Scroll-triggered reveals** — frames are *projected* as they enter: a
  frame's still scales 1.08→1 inside its sprocketed border over 700ms
  `--ease-crank` as the frame crosses centre; its caption types in by lines
  (not characters — typewriter lines land whole, 90ms stagger). Trigger:
  frame's top crossing 78% viewport height. Fallback per §6.
- **Scroll-driven / scrubbed animation** — the crank itself (§6.3): scroll
  position is footage; the strip's translateY is the lerped, quantised
  reading of it. The splice line (§6.6) draws scrubbed to its frame's
  progress through the viewport centre band.
- **Parallax** — two texture layers only: scratches at 0.96× scroll rate,
  dust-in-beam at 1.04× — a 4% differential each way, enough to feel depth in
  the gate, never enough to misalign a frame line. Text and frames never
  parallax against each other.
- **Pinned sections** — one only: the feature frame (§6.8) pins for 220vh
  while its three intertitles cycle. A second pin on a page is refused — the
  booth runs one feature at a time.
- **Smooth scrolling** — refused as a default; the crank (§6.3) *is* the
  scroll feel. Anchor jumps (§6.12) travel by fast crank (900ms quantised)
  rather than browser smooth-scroll.
- **Progress indicator** — the sprocket rail + footage counter (§6.4),
  measured in feet from the changeover sheet.
- **Staggered + masked reveals** — entrance sequence (§6.1, §6.2): leader →
  iris → title card rise with a flicker pass → rails slide in → captions
  stagger line by line.
- **Kinetic typography** — the intertitle keyword swell (§6.7) and the
  odometer digit wheels (§6.4). Nothing else moves type.
- **Marquee** — refused. Film does not scroll sideways on this page; the
  programme's names live in frames. (A venue that needs a ticker has left
  the booth.)
- **Counters** — footage counter (§6.4), runtime and seats in the programme
  frames (§6.13) — all readings from §6.17, counted in digit-wheel steps,
  never a smooth numeric tween.
- **SVG line-draw** — the splice (§6.6) and the changeover cue marks (the
  small circles-and-crosses the projectionist pencils on the film, drawn in
  §6.14's table rows as they are passed).
- **Image scale-in-frame** — stills scale 1.08→1 *inside* their sprocketed
  frames; the frame border never moves and the image never escapes it.
- **Hover / magnetic / tilt micro-interactions** — lamp bloom (§6.9) and the
  reel-can magnetic pull (§6.10, ≤6px). Tilt is refused: frames are flat in
  the gate; a tilted frame is a jammed frame.
- **Custom cursor** — refused (standing rule). The pointer is the visitor's
  hand; the booth does not dress it.
- **Skeleton loading** — unexposed frames (§6.16): cream stock with printed
  frame lines and the words "UNEXPOSED — AWAITING THE PRINT" typed once; no
  shimmer (shimmer is a lamp effect and the lamp is off on unexposed stock).
- **Page transitions** — the reel change (§6.16): iris-out 350ms, leader
  black with the next reel's number, iris-in 450ms; 2400ms hard ceiling.
- **Ambient loops** — exactly two licensed: carbon-arc flicker (irregular,
  seeded random walk on a gradient's opacity, 4–11Hz micro-variation, never
  periodic) and dust drift in the beam (slow, 26s traverse). The hair-in-the-
  gate (§6.11) is *not* a loop — it is a rare event, 1–2 times per session.
- **Reduced motion** — §10 and per element: flicker off, jitter off, crank
  becomes direct 1:1 scroll, iris becomes a cut, the leader is skipped to a
  printed "3 · 2 · 1" still. The page rests as a printed strip.

**The flicker, specified exactly.** "Irregular, lamp-like" is a build
requirement, not a mood, so it is specified as an algorithm. The flicker
layer is a radial gradient centred on the current frame's still (or the
hero frame before any scroll), and the loop drives its opacity with a
**seeded random walk**: every 90ms the target opacity steps by a random
amount in ±0.05, clamped to the band 0.82–1.00 of the layer's base opacity;
the rendered value lerps toward the target at 0.35 per frame (faster than
the crank channel — light responds quicker than film). The seed is fixed
per page (derived from the print's total footage, §6.17 — tonight: 4860),
so every visitor's lamp behaves the same way, the way the same projector
would. Three hard bounds: the walk never drops the layer below 0.82 (the
lamp never threatens to go out — a lamp that dies is a breakdown, not an
atmosphere); the walk pauses entirely while the visitor is reading a form
(§6.15 focus state) or while any text field has focus anywhere on the page;
and the layer's gradient is clipped to the picture area of the frame it
lights, so its light can never reach the caption band or body text (§2's
ruling, enforced geometrically, not by discipline). A build whose flicker
is a sine wave, a CSS keyframe loop, or an unseeded `Math.random` shimmer
fails §10: all three read as *effects*; the walk reads as a lamp. On the
pinned scene (§6.8) the walk's band widens slightly (0.78–1.00) and its
step rate doubles to every 45ms — the feature is running, the lamp works
harder — and the intertitle transitions borrow three steps of the same walk
for their dips, so the whole page's light has one source and one behaviour.

---

## 6. Signature elements

The 11 originals (§6.1–§6.11) are deepened, never redesigned. The 7
page-family elements (§6.12–§6.18) complete the page: navigation, programme
cards, the showtime table, the box-office form, the loader/transition, the
record itself, and the dark booth of the 404. Every figure any element shows
traces to §6.17, the changeover sheet.

### 6.1 The countdown leader

**What & why.** Real film-leader circles count 3…2…1 — crosshair, concentric
circle, the number lettered large — each held ~600ms with gate jitter, before
the programme starts. The page begins the way its films do; the ritual is the
brand's native ceremony, and skipping it would be like entering the cinema
after the lights are already down.

**Structure.** A full-viewport booth-black overlay (`<div class="leader">`)
containing one inline SVG (two concentric circles, crosshair lines, a sweep
wedge) and a Limelight numeral. The leader is **inserted by JS only** — the
DOM ships with the first frame fully visible beneath it, so a no-JS visit
never sees a leader at all. An actual printed "3 · 2 · 1" still (the three
circles in a row, static) is the reduced-motion / skip state, living in the
hero frame as a caption strip.

**Motion spec.** Each number: SVG circle draws in 180ms `--ease-draw`, numeral
settles 120ms `--ease-settle`, hold 320ms with ±1px gate jitter at 90ms steps,
sweep wedge rotates one quarter-turn per number. Total per number 620ms;
full leader 1,860ms + 240ms iris handoff into §6.2. Skippable on first scroll
input, first keypress, or click (the projectionist starts the show when the
house is ready).

**Choreography timeline.** t=0 overlay fades to full booth black (80ms) →
t=80 "3" circle draws → t=260 numeral settles → t=380–580 jitter hold →
t=620 "2" (same beats) → t=1240 "1" → t=1860 final circle holds 240ms while
the iris (§6.2) begins beneath it → t=2100 leader overlay is removed from the
DOM (not merely hidden).

**State matrix.** *Rest (pre-load):* absent from DOM. *Running:* as timeline.
*Skipped:* any input → jump to the "1" still for 120ms, then iris. *Scrolled-
past:* cannot recur — session flag `booth.leaderSeen` suppresses replay on
in-page navigation (§6.16 re-entry shows only the reel-number card).
*Disabled:* JS off → never inserted. *Touch:* identical; skip on first touch.

**Breakpoints.** ≥1200px: circles 340px diameter, numeral 150px. 768–1199px:
circles 280px, numeral 124px. <768px: circles 210px, numeral 96px; hold times
unchanged (the ritual is not shortened for small rooms).

**Edge cases & failure modes.** Slow network: the leader is inline SVG + one
webfont; if Limelight has not loaded by t=0, the numeral renders in the
Georgia fallback — the count never waits for a font. Tab hidden mid-count:
the timeline is timestamp-driven, so it completes silently and removes
itself. Visitor with `prefers-reduced-motion`: leader replaced by the static
printed still, no overlay. Repeat visit in session: suppressed (see states).

**Accessibility.** The overlay is `aria-hidden` decoration over already-
available content; it never traps focus and never moves it. A visually hidden
live region announces "Programme starting" once when the iris opens. The skip
affordance is any input — documented in §12's fixed strings, since a hidden
button would be a web convention the booth doesn't use; keyboard users skip
with any key, including Tab, without losing their place (focus is untouched).

**Tokens.** `--booth`, `--screen`, `--gate-line`, `--leader-size`,
`--ease-draw`, `--ease-settle`.

**Content-merge.** The leader's numbers are the programme's own — on a
festival page the leader can carry the strand name typed beneath the circles
("REPERTORY STRAND — NIGHT THREE"), set from the page's record (§6.17), so
the ceremony announces the actual show, not a generic cinema.

**Failure fallback & watchdog.** A 2,600ms watchdog removes the overlay
unconditionally if the timeline stalls (rAF paused, font hang). Because the
overlay is JS-inserted over complete content, every failure mode ends with
the page simply *there*.

**Reduced motion.** No overlay; the printed three-circle still appears as a
caption strip at the head of the hero frame.

**Performance & mobile.** Inline SVG ~1.2KB; zero assets. Mobile variant:
smaller circles (see breakpoints); jitter steps reduced to ±0.5px to avoid
visible layout shimmer on low-refresh screens.

### 6.2 The iris-wipe opening

**What & why.** After the leader, a circular clip-path expands from the
centre of the first frame — a 1920s iris-in — revealing the hero frame: the
programme title card, the feature still, the first showtime. The reveal
grammar belongs to the films, not to web conventions.

**Structure.** The hero frame is complete in the DOM. JS arms the effect by
setting `clip-path: circle(0% at 50% 42%)` on a wrapper, then animates the
radius via the shared loop; the wrapper's clip is removed at completion so
no clip can strand the frame. The iris edge carries a 2px `--arc` ring at
40% opacity — the lamp catching the diaphragm.

**Motion spec.** Radius 0% → 112% (enough to clear the corners) over 900ms
`--ease-iris`, beginning 240ms after the leader's last beat (or at t=120ms
when the leader was skipped/absent). The title card inside rises 14px and
fades its last 8% of opacity during the iris's final 300ms — a card rising
through the opening light, not a fade-in pasted on top.

**Choreography timeline.** t=0 clip armed at 0% → t=0–900 radius lerps to
112% (loop-driven, `--ease-iris` applied to progress) → t=600–900 title card
rise → t=900 clip-path removed, ring fades 160ms → t=1060 hero at rest; the
flicker layer (§5) fades up over the following 800ms.

**State matrix.** *Rest:* no clip, frame fully visible (the DOM default).
*Armed:* clip at 0% for exactly one frame of paint before the loop starts —
JS arms and starts in the same task, so a painted 0% state is never seen
without motion following. *Running:* as timeline. *Scrolled-past:* if the
visitor scrolls during the iris, it completes instantly (jump to end state).
*Disabled:* JS off or reduced-motion → never armed. *Touch:* identical.

**Breakpoints.** ≥1200px: iris centre at 50% / 42% of the hero frame.
768–1199px: centre 50% / 40%. <768px: centre 50% / 36% (the title sits
higher); duration 750ms — a smaller room opens faster.

**Edge cases & failure modes.** If the hero image (the feature still) has
not loaded, the iris still runs — the frame's printed caption and title are
the content; the still fades in inside its sprocketed border when it arrives
(§5 image rule). If the loop is busy (long task), the iris degrades to a
CSS transition on the same property — same duration, same end state.

**Accessibility.** Purely visual reveal of content that is already in the
accessibility tree; no aria state changes. Focus is never placed inside a
clipped region before the clip clears (the hero's first link becomes
focusable in DOM order regardless — clipping is visual only, and keyboard
focus scrolls the frame into view, which triggers the instant-complete rule).

**Tokens.** `--arc`, `--booth`, `--ease-iris`, `--iris-ms` (900).

**Content-merge.** The iris reveals *the programme*: title, still, first
showtime — the frame a 1924 audience saw first. It is never used on inner
pages' content frames (only §6.16's transition borrows the diaphragm, at
half duration, for reel changes).

**Failure fallback & watchdog.** A 1,400ms watchdog clears any clip-path on
the hero wrapper. Default state is unclipped; every failure ends open.

**Reduced motion.** A plain cut: the frame is simply there, with the printed
leader still as its caption (§6.1).

**Performance & mobile.** clip-path animation on one wrapper only, composited;
cost negligible. Mobile: 750ms duration, ring at 30% opacity (thinner lamp).

### 6.3 The hand-cranked frame advance

**What & why.** Scrolling advances the film frame by frame: the strip's
position is quantised to frame steps with a tiny mechanical catch, so reading
feels cranked, not glided. The reader's hand is on the crank — this is the
theme's core interaction and the one visitors will describe afterwards.

**Structure.** Native scroll is never hijacked: the document scrolls
normally, and the crank is a *rendering* layer — the strip container's inner
wrapper receives a `transform: translateY()` offset equal to the difference
between the lerped scroll reading and the true scroll position, quantised
to the frame pitch (64px at desktop = one sprocket pitch). In practice the
offset is small (±32px max) and reads as the film's mechanical settle after
each pull. A 1px gate-line flash line at the viewport's top frame boundary
marks each caught step.

**Motion spec.** Shared loop, lerp 0.12 per frame toward the quantised
target; a step "catches" when the lerped value crosses a pitch boundary —
at the catch, a 40ms `--ease-flash` frame-line pulse and, at most once per
300ms, a 1px vertical settle overshoot (`--ease-settle`, 90ms). Fast scroll
(velocity > 2400px/s) suspends quantisation — the projectionist cranks fast
to reach a reel change; nobody reads at that speed, and stepping would
judder. Quantisation resumes 160ms after velocity falls.

**Choreography timeline.** Per scroll gesture: t=0 scroll input → loop
target updates → t≈90ms first catch pulse as the first boundary crosses →
subsequent catches at each pitch crossing while lerping → gesture end →
final settle overshoot 90ms → loop sleeps.

**State matrix.** *Rest:* offset 0, strip aligned to true scroll.
*Cranking:* catches as above. *Fast-crank:* quantisation suspended, offset
decays to 0 at lerp 0.2. *Scrolled-past / scroll-up:* fully symmetric — the
crank runs backwards with the same catches (the projectionist can rewind).
*Disabled:* JS off → no wrapper offset exists; plain native scroll.
*Touch:* identical rendering layer; touch scroll velocity is read from the
same scroll events — no touch-specific handlers.

**Breakpoints.** ≥1200px: pitch 64px, max offset ±32px. 768–1199px: pitch
56px, max offset ±28px. <768px: pitch 48px, catch pulse removed (the frame
lines are closer together; the pulse would strobe), max offset ±20px.

**Edge cases & failure modes.** Low-power device: if the loop's frame time
exceeds 24ms sustained over 60 frames, quantisation halves (pitch ×2) and
the catch pulse is dropped — the crank gets heavier, never broken. Content
longer than expected: the mechanism is position-based, not content-based;
it cannot run out. Browser find-in-page jump: a >2000px instantaneous jump
snaps the offset to 0 (no catch theatre for a teleport).

**Accessibility.** The offset never exceeds ±32px and never changes layout,
scroll position, or focus — it is a visual settle only. Screen-reader and
keyboard scrolling are unaffected. `prefers-reduced-motion` disables the
layer entirely (below).

**Tokens.** `--pitch` (64px), `--ease-flash`, `--ease-settle`,
`--crank-lerp` (0.12).

**Content-merge.** The step the scroll catches on is the strip's own pitch —
the same 64px as the sprocket holes (§4). The visitor isn't watching an
effect applied to the page; the page's physical unit is what their hand
feels.

**Failure fallback & watchdog.** The wrapper transform is written only by
the loop; a 500ms inactivity check zeroes it if the loop dies, and the
no-JS state has no transform at all. Content can never be left offset.

**Reduced motion.** Layer off. Scroll is direct 1:1; the strip is a printed
page.

**Performance & mobile.** One transform on one wrapper, composited; the
quantisation math is trivial. Mobile variant: smaller pitch and no pulse
(see breakpoints); the settle overshoot is kept — it is the crank's signature
and costs nothing.

**The quantisation, worked once so it is never improvised.** At desktop
pitch (64px), suppose the visitor has scrolled to a true position of
1,530px and is still moving. The quantised target is the nearest pitch
boundary below the reading: floor(1530 ÷ 64) × 64 = 1,472px. The loop lerps
the *rendered* position from its current value toward 1,472 + (the
fractional remainder the visitor has pulled past the boundary, capped at
one pitch) — in effect the film is pulled down in 64px pulls, each pull
completing with the catch. The wrapper offset written each frame is
`rendered − true`, which is why it can never exceed ±32px (half a pitch):
at the moment of the catch the rendered position snaps its last few pixels
onto the boundary the visitor's scroll has already passed. If the visitor
reverses direction mid-pull, the target recomputes from the new true
position on the next frame — the crank has no memory and no momentum of its
own beyond the 0.12 lerp, so a reversal feels like a real gate: a catch,
then the film runs back. Builders must not add inertia curves, velocity
smoothing or spring overshoot to this channel; the settle overshoot at
gesture end (§6.3's motion spec) is the single licensed flourish, and it
belongs to the gesture, not to the scroll.

### 6.4 The sprocket progress rail & footage counter

**What & why.** Progress measured in the medium's own unit — feet of film.
The left sprocket rail's holes fill amber as footage passes, and a footage
counter in the booth window (§4) ticks its digit wheels like a nitrate
odometer. The counter may only show footage the page's frames contain: its
maximum is the strip's total printed footage from §6.17, never a generic
100%.

**Structure.** The rail: a fixed column of hole elements generated from the
frame count (one hole per frame on the page + leader holes), each a
`<span class="hole">` filled by toggling a class as its frame is passed. The
counter: five digit wheels (feet to 99,999) built as vertical digit strips
inside a clipped window, translated by the loop; the wheels are `aria-hidden`
with a visually hidden text reading ("Footage: 2,431 of 4,860 feet") updated
at most once per second.

**Motion spec.** As the lerped scroll reading (§6.3) passes each frame's
footage boundary (cumulative feet from §6.17), the corresponding hole fills:
background `--arc-deep` → `--arc` over 160ms `--ease-crank`, one hole at a
time, in order — never a percentage sweep. Digit wheels step per foot with
the crank quantisation: each foot = one wheel step of 10% of a digit height,
90ms `--ease-crank`; tens/hundreds wheels move only on their carries,
exactly like the machine.

**Choreography timeline.** Continuous with scroll: frame boundary crossed →
hole fill begins (160ms) → counter wheels step to the new footage (90ms per
foot, queued carries resolve within 240ms) → hidden text reading updates at
the next 1s tick. At the final frame: last hole fills, counter rests at the
sheet's total, and the counter's rim light (§6.9's lamp, at 20%) warms for
600ms — the print is finished.

**State matrix.** *Rest (top):* holes empty (booth-raise), counter at 00000
with the leader's 24 ft pre-roll already counted — the counter starts at the
leader footage printed on §6.17, an honest machine detail. *Running:* as
above. *Scrolled-past:* holes above the current frame stay filled (footage
once run stays run — scrolling up *unfills* them in reverse order, because
the film is being rewound; the counter counts down). *Disabled:* JS off →
holes printed empty, counter printed at the sheet's total with the caption
"THE PRINT RUNS 4,860 FT" — the record without the machine. *Touch:*
identical.

**Breakpoints.** ≥1200px: rail 44px, counter in the booth window at 18px
digits. 768–1199px: rail 36px, counter 16px. <768px: rail 24px with holes
10×14px; counter moves into the frame-index bar (§6.12) at 14px digits and
the booth window keeps only the venue name — the instrument shrinks, it
does not vanish.

**Edge cases & failure modes.** A page with more frames than the rail can
hold at pitch: holes compress to a minimum 40px pitch and the excess frames
share holes by footage proportion (the fill is footage-true, not frame-
true). If §6.17's data is missing, the counter prints "——— FT" and the rail
stays empty — the machine refuses to invent a reading (§10 gate blocks this
in production).

**Accessibility.** The rail is decorative (`aria-hidden`); progress is
conveyed by the hidden text reading and by the frame numbers themselves.
The counter's visible wheels are `aria-hidden`; the text equivalent updates
at 1Hz maximum to avoid chatter. Contrast: filled hole (amber on booth)
6.1:1 as a signal, empty hole is a shape, not information.

**Tokens.** `--arc`, `--arc-deep`, `--booth-raise`, `--pitch`,
`--ease-crank`, `--counter-feet-total` (from §6.17).

**Content-merge.** The holes are the strip's real sprocket holes (§4) — the
progress device is the page's own anatomy, and the footage it counts is the
sum of the frames the visitor has actually passed.

**Failure fallback & watchdog.** Fill states are classes toggled by the
loop; if the loop dies, holes simply stop mid-strip — content is untouched
and the printed total (no-JS caption pattern) is present in the DOM as the
hidden reading. No watchdog needed beyond the loop's own health check
(§6.3), because no state of this element can hide content.

**Reduced motion.** Holes fill instantly (no 160ms), wheels snap to the
reading with no stepping, rim-light beat removed.

**Performance & mobile.** Hole fills are class toggles on ≤40 spans; wheels
are transforms on 5 strips. Mobile: smaller rail (above); wheel digit height
14px; the 1s text update unchanged.

**The page's own footage map.** The counter counts the *page's* strip, so
the page must have a footage map of its own, derived from the sheet at
build time: each frame is assigned footage in proportion to its rendered
height, scaled so the frames sum exactly to the print's total — the last
frame's boundary is 4,860 ft by construction, never by rounding luck (the
final frame absorbs the rounding remainder, and the map is printed in the
build's audit output). Tonight's home page, for reference:

| Frame | Content | Cumulative feet at its foot |
|---|---|---|
| FR. 01 | Title card / hero | 380 |
| FR. 02 | Tonight at the Orpheum (standfirst) | 760 |
| FR. 03 | The pinned scene (§6.8) | 1,540 |
| FR. 04 | Programme frames I (§6.13) | 2,320 |
| FR. 05 | Programme frames II | 3,050 |
| FR. 06 | The burnt frame (§6.5) | 3,610 |
| FR. 07 | The changeover table (§6.14) | 4,300 |
| FR. 08 | The box-office slip (§6.15) + run-out | 4,860 |

Two consequences builders must honour. First, the rail's holes are pitched
by *footage*, not by frame count — a long frame (the pinned scene) owns
more holes than a short one, which is why §4's rail is generated from this
map and not from the DOM's frame count alone. Second, if an editor adds or
removes a frame, the map is regenerated and every boundary changes — the
counter is never reprogrammed by hand, because it was never programmed by
hand in the first place: it reads the map the way the machine reads the
film. A page whose map sums to anything but the sheet's total fails §10
before a single hole is drawn.

### 6.5 The burnt frame

**What & why.** One frame mid-page carries a burnt, bubbling emulsion patch
— animated blister shimmer — that the visitor must scroll past, exactly like
a nitrate splice in a real print. Its caption admits the damage in the
booth's voice. The archive shows its wounds: authenticity as a designed
obstacle, not a filter. This is the original entry's named anti-slop detail,
promoted to a full element.

**Structure.** A normal content frame (it carries real content — in the
worked example, the restoration notes for Reel 3) whose top-right quadrant
holds the burn: layered radial gradients in `--burnt`/`--booth` with a
canvas-free CSS blister field (12 small blurred circles at fixed seeded
positions) inside a blob-shaped clip. The patch never covers the frame's
text column — it eats the frame's *margin and its still*, the way real burns
eat the picture first. The still beneath the patch is printed torn: its
corner is the patch.

**Motion spec.** Blister shimmer: the blister circles breathe — scale
1↔1.06 and opacity ±8% — on a seeded irregular pattern (each blister its own
duration, 2.4–4.1s, `--ease-settle` reversed), never synchronised (a uniform
pulse reads as a lava lamp, not as damage). As the frame crosses the
viewport centre, the patch's edge glow (`--arc` at 12%) warms for 900ms —
the lamp behind the burn — then cools. That is all: the burn does not grow,
spread or animate theatrically. Damage is still; only light moves.

**Choreography timeline.** Frame enters → t=0 blisters at rest pattern
(already running, ambient-class but element-local) → frame centre crossing
→ edge glow warms 900ms `--ease-crank` → frame passes → glow cools 1400ms →
blisters continue their seeded pattern (they are texture, not a beat).

**State matrix.** *Rest:* patch present, blisters breathing, caption
printed. *Hover:* nothing — you do not interact with a burn; the lamp bloom
(§6.9) is refused on this frame (the lamp does not warm a wound for
inspection; the caption explains). *Scrolled-past:* unchanged — the burn is
behind you, still on the strip. *Disabled:* JS off → patch is a static
gradient, caption identical. *Touch:* identical to rest.

**Breakpoints.** ≥1200px: patch ~340×260px in the still's corner.
768–1199px: ~260×200px. <768px: the still stacks above the text and the
patch sits on the still only, ~180×140px — on small screens the burn must
never approach the text column, so it shrinks to the picture it ate.

**Edge cases & failure modes.** If the frame's still fails to load, the
patch remains over the printed empty frame border — the caption still reads
correctly ("the burn took the corner of this frame in 1962"), because the
caption describes the *frame*, not the image file. Long content: the text
column is layout-protected (patch is absolutely positioned within the
still's box only).

**Accessibility.** The patch is `aria-hidden` texture. The caption is real
text, adjacent, and is the accessible description of the damage — a screen
reader visitor gets the same honesty a sighted one does. Contrast of the
caption (cream on booth) is the standard 13.6:1.

**Tokens.** `--burnt`, `--booth`, `--arc`, `--screen`, `--ease-settle`.

**Content-merge.** The burnt frame is not a decoration break — it carries
the restoration-notes content, and its damage is *about* that content (the
reel that burnt is the reel the notes discuss). The §10 gate requires every
build to name, in the caption, which reel burnt and when — a generic burn
on unrelated content fails the gate.

**Failure fallback & watchdog.** None required: the element is static-first.
With CSS only, the patch renders; the shimmer is the only JS/CSS-animation
layer and its absence changes nothing's legibility.

**Reduced motion.** Blisters still (single static pattern), edge glow
removed. The burn remains — reduced motion removes movement, not history.

**Performance & mobile.** Twelve blurred circles is the cheapest texture on
the page; blur radius capped at 8px, and the layer is `will-change`-free
(opacity/transform only). Mobile: blister count halves to 6, patch per
breakpoints.

### 6.6 The splice-line repair

**What & why.** Across the frame immediately after the burnt one, an SVG
splice line draws itself diagonally as the frame enters — the repair made
visible. Damage (§6.5) and repair are both content; the strip's history is
the story the archive tells about itself.

**Structure.** An inline SVG spanning the frame's full width, one diagonal
path (the splice tape edge) plus two short perpendicular ticks (the
splicer's marks), drawn over the frame line between the burnt frame and
this one — the line lives *on the join*, in the splice gap (§4), not inside
either frame's content. Below it, a typed caption: "SPLICED AT THE BOOTH —
REEL 3 TO REEL 4, CEMENT SPLICER, 1987." set from §6.17's repair record.

**Motion spec.** Path draws via `stroke-dashoffset`, scrubbed to the join's
progress through the viewport's centre band (enters at 65% height, complete
at 45%): total draw length covered over ~340px of scroll, `--ease-draw`
applied to the scrub value in the shared loop. The two ticks draw after the
main line, 120ms each, when the scrub passes 85%. Once drawn, the line
stays drawn — scrolling back up does not un-repair the film (the scrub is
ratcheted: `max(previous, current)`).

**Choreography timeline.** Join enters centre band → line draws
proportionally (scroll-scrubbed) → 85%: tick 1 (120ms) → tick 2 (120ms) →
100%: caption's underline (the splicer's pencil line) draws 200ms
`--ease-draw` → rest: a printed diagonal on the strip.

**State matrix.** *Rest (pre-trigger):* line printed at 18% opacity in dust
(the splice exists on the film whether or not you've watched it being made
— the draw is a demonstration, not the repair itself). *Drawing:* scrubbed
as above. *Scrolled-past:* fully drawn, full opacity. *Scroll-up:* stays
drawn (ratchet). *Disabled:* JS off → line printed at full opacity with its
caption; nothing hidden. *Touch:* identical scrub.

**Breakpoints.** All sizes: the line spans the join; on <768px the diagonal
flattens (rise 18px instead of 34px) so it fits the narrower strip; ticks
and caption unchanged.

**Edge cases & failure modes.** If the burnt frame (§6.5) is omitted in a
build, the splice must also be omitted — a repair with no damage is a lie
the §10 gate rejects. If the visitor jump-scrolls past the join (anchor
navigation), the ratchet completes it instantly on arrival.

**Accessibility.** Decorative SVG (`aria-hidden`); the caption is real text
and carries the information. The draw is scrubbed to scroll, so it cannot
flash or strobe.

**Tokens.** `--dust`, `--screen`, `--ease-draw`, `--gate-line`.

**Content-merge.** The line sits on the actual join between the two frames
it names, and its caption cites the actual reels from §6.17 — it is the
strip's own repair record, printed where the repair is.

**Failure fallback & watchdog.** The pre-state is 18% opacity, not 0 — a
dead loop leaves a faint but complete splice with its caption. No watchdog
needed; nothing can be stranded.

**Reduced motion.** Line printed at full opacity from the start; no draw.

**Performance & mobile.** One path, dash-offset writes from the shared
loop; negligible. Mobile: flattened diagonal (above).

---

### 6.7 The intertitle keyword swell

**What & why.** In intertitle cards, one key word swells mid-sentence —
scale and letterspacing, ~500ms — as the card centres: silent-film
over-enunciation, the actor mouthing the word too clearly. Emphasis in this
cinema is acted, not bolded (Type law 2).

**Structure.** The intertitle is a cream card centred in its frame; the key
word is a `<strong class="swell">` — semantic emphasis, styled without
weight change: `display:inline-block` so transform applies, transform-origin
at the word's baseline centre. The word is chosen by the author in the
content, one per card, marked in the source — never auto-detected by script
(a script cannot know which word the actor would mouth).

**Motion spec.** As the card's centre crosses the viewport's centre band
(±8% of viewport height): the word scales 1 → 1.18 and letter-spacing
0.02em → 0.09em over 500ms `--ease-settle`, holds 700ms, then relaxes over
600ms `--ease-crank`. One swell per card per pass; scrolling the card out
and back re-arms it (the scene replays when you rewind to it).

**Choreography timeline.** Card enters band → t=0 swell begins → t=500 full
swell → t=1200 hold ends → t=1800 relaxed → card leaves band; state resets
for the next pass.

**State matrix.** *Rest:* word at natural size — the sentence reads
perfectly without the swell. *Swelling/held/relaxing:* as timeline.
*Hover:* no change (you do not hover an actor's line). *Scrolled-past:*
relaxed state. *Disabled:* JS off → no swell; the word is still a
`<strong>`, carrying its emphasis semantically. *Touch:* identical
(scroll-driven, no touch handlers).

**Breakpoints.** All sizes: same timing; on <768px the scale caps at 1.12
and spacing at 0.06em — a small card must not burst its frame line.

**Edge cases & failure modes.** A card whose key word is long (≥14
characters): the swell is capped so the word's swollen width ≤ 92% of the
card's measure — the build computes the cap from the word's rendered width
at authoring time and sets it as a per-card token (`--swell-max`). Two cards
in the band simultaneously: both may swell — they are two scenes, not one.

**Accessibility.** Transform only — the text, its order and its semantics
never change; screen readers read the sentence once, unswollen. The swell
is slow (500ms) and small (≤1.18×): safe under vestibular guidelines, and
removed entirely under reduced motion.

**Tokens.** `--screen`, `--booth`, `--ease-settle`, `--ease-crank`,
`--swell-max` (per card).

**Content-merge.** The swollen word is the sentence's actual pivot — in the
worked example, "tonight" in "The print returns to the vault TONIGHT" — the
word the whole card exists to say. A swell on a filler word fails §9.

**Failure fallback & watchdog.** The rest state is the complete sentence;
the effect is a transform applied by the loop and cleared on band exit. A
dead loop leaves an unswollen, fully readable card. No watchdog needed.

**Reduced motion.** No swell. The word carries a printed amber underline
(the cue-pencil mark) instead — emphasis by annotation, the booth's other
native grammar.

**Performance & mobile.** One transform on one word per card; negligible.
Mobile caps per breakpoints.

### 6.8 The pinned feature frame — cycling intertitles

**What & why.** One feature frame pins while scroll cycles its three
intertitle cards — crossfading through flicker — like a scene playing while
you hold the reel. A scene screens inside the page: cinema within the
strip. This is the page's single licensed pin (§5).

**Structure.** A frame of 100vh containing the feature still (sprocketed,
§5) and an intertitle card slot beneath it. The three intertitles are three
real cards in the DOM, stacked; the pin container is 220vh tall with the
frame sticky at its centre. All three cards are in the accessibility tree
in order — the cycle is a visual performance over complete content (and
with JS off, the three cards simply stack and read as a three-card scene).

**Motion spec.** Pin range 220vh. Scroll progress through the range is
divided in thirds; at each third boundary, the current card crossfades to
the next through a flicker pass: outgoing card's opacity dips in the arc
pattern (three irregular dips over 240ms), incoming card rises 8px and
settles (`--ease-settle`, 320ms). The still's scale scrubs 1.08→1 across
the whole pin (§5 image rule). The lamp flicker layer (§5) is at its
strongest here — this frame is the screening.

**Choreography timeline.** Pin begins → card 1 at rest (it was the frame's
printed state) → 33% boundary: flicker-dip 240ms + card 2 settles (320ms)
→ 66%: same to card 3 → pin ends: card 3 remains as the frame's resting
print, frame unpins and scrolls away whole. Scroll-up reverses the cycle
exactly (the scene rewinds).

**State matrix.** *Rest (before pin):* card 1 shown, cards 2–3 stacked
beneath at 0 opacity but present (JS-armed state only; no-JS shows all
three stacked visibly). *Pinned:* cycle as timeline. *Scrolled-past:* card
3 resting. *Disabled:* no pin — the frame is a normal frame, cards stacked
and readable. *Touch:* identical; the pin is scroll geometry, not gesture.

**Breakpoints.** ≥1200px: pin 220vh, still 16:9-ish frame with card below.
768–1199px: pin 200vh. <768px: pin abolished — the three cards stack in one
tall frame and crossfade is replaced by the §6.7 swell on each card's key
word as it centres; a pinned scene on a phone traps the visitor in the
booth's smallest room.

**Edge cases & failure modes.** Very tall viewports (>1100px): pin range
caps at 200vh so the scene cannot overstay. If the still fails to load, the
cards cycle over the printed empty frame — the scene is the words. If the
visitor uses find-in-page to jump beyond the pin, the frame lands in its
scrolled-past state (card 3), consistent with the ratchet logic in §6.6.

**Accessibility.** All three intertitles are readable in DOM order at all
times (opacity is visual only); a screen reader experiences the scene as
three consecutive cards — correct. The flicker-dip is opacity on the *card
stock*, capped at a 35% dip, never a full flash, and within photosensitivity
limits (no more than 3 dips per transition, transitions ≥600ms apart by
scroll geometry). Reduced motion removes the pin entirely (below).

**Tokens.** `--screen`, `--screen-dim`, `--arc`, `--ease-settle`,
`--ease-crank`, `--pin-range` (220vh).

**Content-merge.** The three cards are one scene's actual dialogue — in the
worked example, Caligari's three title cards — and the still is that scene.
The pin is not a slideshow of unrelated marketing lines; §9 names that as
slop.

**Failure fallback & watchdog.** The sticky frame can never trap scroll
(the container's height is CSS, not JS). If the loop dies mid-pin, the
visible card freezes but remains fully readable, and scrolling on unpins
normally. Watchdog: none needed beyond geometry.

**Reduced motion.** No pin, no cycle: the three cards print in sequence in
one frame, each with its §6.7 underline. The scene reads as a storyboard —
the booth's paper form of the same content.

**Performance & mobile.** One sticky element, opacity/transform only.
Mobile: pin abolished (above) — the cheapest variant is the honest one.

**The three cards, written out (worked example).** Tonight's pinned scene
carries the feature's own intertitles, in the print's order, each with its
one authored key word (§6.7's swell applies when the same card grammar is
used outside the pin; inside the pin the cycle itself is the emphasis, so
the swell is not doubled here): Card 1 — "IN THE TOWN OF HOLSTENWALL,
THERE CAME A STRANGER WITH A CABINET." Card 2 — "WHAT THE CABINET HOLDS,
NO LIVING MAN MAY SAY." Card 3 — "TONIGHT, THE CABINET OPENS." The cards
are the scene's actual dialogue, not marketing lines written for the page:
a build that pins three promotional slogans ("BOOK NOW — UNMISSABLE —
RESTORED") over a still has made a carousel in a costume, and §9's census
rejects it. Where a print's real intertitles cannot be licensed or read
(common with fragmentary survivals), the cards carry the booth's typed
scene notes instead — "SCENE: THE FAIRGROUND. THE PRINT IS SILENT HERE
FOR NINE FEET." — typed, not lettered, because they are the projectionist's
notes and not the film's words; the lettered/typed distinction (Type law 1)
is how the page never passes its own commentary off as the film's.

### 6.9 The arc-lamp hover bloom

**What & why.** Hovering a frame blooms warm amber light beneath it and the
frame's still sharpens slightly — as if the projectionist turned the lamp
up for a closer look. Inspection is the hand on the lamp.

**Structure.** A radial-gradient layer (`--arc-hot` core → transparent)
positioned under the frame's still, opacity 0 at rest, plus a `filter:
contrast(1.04) saturate(1.05)` nudge on the still itself. The gradient sits
on a pseudo-element so it can never overlay text (standing rule: animated
layers are pointer-events-none and never cover the content they belong to).

**Motion spec.** Pointer enter: bloom opacity 0 → 0.55 over 420ms
`--ease-crank` (the lamp strikes — slightly uneven: the loop adds a single
120ms dip at 40% progress, the arc catching). Pointer leave: decay over
700ms `--ease-crank` (lamps cool slower than they strike). Still filter
transitions with the same curves. Focus-within triggers the identical bloom
at 0.4 opacity — keyboard inspection gets the same lamp.

**Choreography timeline.** Enter → t=0 strike begins → t≈170 the catch dip
→ t=420 full bloom → hold while hovered (flicker layer modulates the bloom
±4% — the lamp is alive) → leave → 700ms cool → rest.

**State matrix.** *Rest:* no bloom. *Hover:* as timeline. *Focus-within:*
bloom at 0.4, no catch dip (a steadier lamp for readers). *Active (press):*
bloom peaks 0.7 for the press duration — the lamp flares as the machine
answers (pairs with §6.10). *Scrolled-past:* unchanged. *Disabled:* the
bloom is a hover nicety; touch has no hover — on touch, a frame's first tap
blooms it for 900ms before any link follows only where the frame itself is
the link target; otherwise touch simply has no bloom state, by design.
*JS off:* no bloom; frames are complete without it.

**Breakpoints.** All sizes identical; <768px bloom radius shrinks to the
still's box only (no under-glow beyond the frame on a narrow strip).

**Edge cases & failure modes.** Refused on the burnt frame (§6.5) — the
lamp does not warm a wound. Refused inside the box-office form (§6.15)
while a field is being edited (the lamp would distract the paperwork);
focus bloom there is replaced by the field's own amber rule (§6.15).

**Accessibility.** The bloom is decorative light, `aria-hidden` by
construction (pseudo-element). Focus bloom ensures the effect is not
hover-only for meaning — though it carries no meaning beyond "you are
here", which the focus outline also states (2px `--arc` outline, offset
3px, on booth). Contrast at bloom peak: text over the warmed still area is
never text — copy never sits on the still.

**Tokens.** `--arc`, `--arc-hot`, `--ease-crank`.

**Content-merge.** The bloom lives under *this frame's still* — it is the
lamp turned on the very picture being inspected, positioned by the still's
own box, not a generic glow following the pointer around the page.

**Failure fallback & watchdog.** Rest state is no bloom; a dead loop leaves
frames unlit and complete. No watchdog needed.

**Reduced motion.** Bloom becomes instant-on/instant-off at 0.35 opacity
(a switched lamp, no strike or cool), flicker modulation removed.

**Performance & mobile.** One gradient opacity per hovered frame; the
filter nudge is on the still only. Mobile: no hover bloom (above); the
focus variant remains for switch/keyboard users.

### 6.10 Clunk-and-flash — the reel-can buttons

**What & why.** Buttons are reel cans: squat cylinders in dust metal with
the label typed on the lid. They pull magnetically toward the pointer
(≤6px — a can nudged on the bench), and a click lands with a mechanical
clunk: a 2-frame jolt of the whole strip and a frame-line flash. The
machine answers through its own mechanics.

**Structure.** `<button class="reel-can">` — a rounded rect with a lid line
(a 1px rule at 22% height) and the label in Special Elite, centred (paperwork
alignment does not apply to objects). The magnetic pull is a transform on
the button only, driven by pointer proximity within a 48px halo, lerped in
the shared loop at 0.18 (snappier than the crank — small metal, small mass).

**Motion spec.** Halo enter: pull toward pointer, max 6px, lerp 0.18.
Click: strip jolt — the strip wrapper translates 2px down and back over
90ms `--ease-flash` (2 hard steps); simultaneously a frame-line flash: a
1px `--screen` line at 60% opacity sweeps the clicked frame's top border,
120ms `--ease-flash`. Button itself: lid presses (translateY 1px, shadow
collapses) 60ms, recovers `--ease-settle` 180ms. The click's *action* (link
follow, form submit) is never delayed by the theatre — the clunk is
concurrent, not a gate.

**Choreography timeline.** t=0 pointerdown → lid press (60ms) + jolt step 1
→ t=45 jolt step 2 (back) → t=60 flash line sweeps (120ms) → t=180 lid
recovered → rest. Pointerup/click event fires on its normal schedule
throughout.

**State matrix.** *Rest:* can on the bench, label flat. *Hover:* pull
(≤6px) + §6.9 bloom refused here — cans get a lid sheen instead (a 12%
`--screen` gradient angle shift), because the lamp bloom belongs to frames.
*Focus:* 2px amber outline (the standard) + pull disabled (keyboard users
get a steady can). *Active:* clunk sequence. *Disabled:* can in `--dust` at
50%, no pull, no clunk, label gains the typed suffix "(NOT TONIGHT)" only
where the record says so (§6.13's sold-out shows) — a disabled reason is
always printed, never a bare grey button. *Touch:* no pull; the clunk fires
on tap identically.

**Breakpoints.** All sizes: min target 48×48px. <768px: halo shrinks to the
button's own box (pull ≤4px) — on a narrow bench, cans are not chased.

**Edge cases & failure modes.** Two cans adjacent: pulls are independent
and capped so neighbours never overlap (max combined displacement checked
against the gap token `--can-gap`, 12px). If the loop is dead, cans are
ordinary buttons — the pull and clunk are garnish on a working control.

**Accessibility.** Real `<button>`s with real labels; the jolt/flash are
visual only and never move the hit area (transform on the wrapper is 2px
for 90ms and pointer events are not intercepted). Focus outline per §6.9.
Reduced motion: no pull, no jolt, no flash — a plain press state (lid line
darkens).

**Tokens.** `--dust`, `--screen`, `--arc`, `--ease-flash`, `--ease-settle`,
`--can-gap`.

**Content-merge.** The can's label is the action in the booth's words —
"BOOK FOR THE 19:45" (§6.15), "READ THE RESTORATION NOTES" — and the can for
a sold-out show is physically absent, replaced by its typed notice (§6.13):
the object system and the record agree.

**Failure fallback & watchdog.** Buttons work with JS off, CSS off, loop
dead. No watchdog applicable — nothing here can strand content or function.

**Reduced motion.** Plain press state only (above).

**Performance & mobile.** Pull math is one distance check per can in the
halo (≤ a handful on screen). Mobile: tap clunk kept (it is the theme's
handshake), pull reduced (above).

### 6.11 Hair-in-the-gate jitter

**What & why.** At rare, irregular intervals the whole strip jitters by 1px
for a few frames — a hair has got into the gate — then settles. Imperfection
as proof of medium: the page is projected, not rendered.

**Structure.** A transform on the strip wrapper (the same wrapper §6.3
uses), applied by the loop from a seeded event scheduler: after a random
45–110s of *projected* time (tab visible, page in use), a 3-frame event:
offsets +1px, −1px, 0 over 3 consecutive rAF frames (~50ms total), followed
by a 400ms calm. Maximum 2 events per session, never within the first 20s,
never during the pinned scene's intertitle transitions (§6.8) or while the
visitor is typing in the form (§6.15).

**Motion spec.** As structure: 3 frames, 1px amplitude, no easing (a hair
does not ease). The event is logged to a session counter; after 2 events
the scheduler retires for the session — a booth that jitters constantly is
broken, not charming.

**Choreography timeline.** Scheduler fires → frame 1: +1px → frame 2: −1px
→ frame 3: 0 → 400ms calm → scheduler re-arms (if events remain).

**State matrix.** *Rest:* no offset (99% of the session). *Event:* 50ms as
above. *Suppressed:* during form entry, during §6.8 transitions, when the
tab is hidden, under reduced motion (never fires), after 2 events.
*Disabled:* JS off → never exists. *Touch:* identical (it is time-based,
not input-based).

**Breakpoints.** All sizes: 1px. On <768px the amplitude stays 1px — the
gate does not know the screen is small.

**Edge cases & failure modes.** If the visitor is mid-scroll at high
velocity, the event waits for velocity < 400px/s (a hair during a fast
crank would be invisible anyway and risks reading as a bug). If the loop's
health check (§6.3) has degraded the crank, the hair is disabled — a
struggling machine does not get extra faults.

**Accessibility.** 1px for 50ms, at most twice a session: far inside
vestibular safety margins, and fully removed by reduced motion. It never
moves focus, layout or hit areas (transform only). This is the element most
likely to be cut by a nervous builder — §10's gate instead requires it be
*bounded exactly as specified*, because unbounded it is a defect and absent
it the medium loses its proof.

**Tokens.** `--ease-flash` (character only; the event itself is un-eased).

**Content-merge.** The jitter moves the *strip* — print, frames and all —
because on real film the hair is in the gate and the whole image shakes.
It is not applied to any single element, which would read as a glitch
effect pasted on.

**Failure fallback & watchdog.** The wrapper offset is written and cleared
by the same scheduler; a finaliser in the loop guarantees offset 0 within
100ms of any event end, even if the scheduler throws. Default state is 0.

**Reduced motion.** Never fires. The gate is clean all evening.

**Performance & mobile.** Three transform writes per event, twice a
session. No mobile variant — identical, and equally rare.

**The projectionist's log.** In a real booth, a hair in the gate is noted
on the cue sheet — it is how the next projectionist knows the gate needs
cleaning. The page honours this: after the session's second (final) hair
event, a typed line is appended to the footer's run-out (§11): "THE GATE
TOOK A HAIR TWICE TONIGHT — IT HAS BEEN NOTED." The line is session-only
(never persisted, never shown to anyone but the visitor who sat through
it), and it is the theme's smallest proof that the booth is *run*, not
rendered: the machine keeps a log of its own faults. If only one hair
occurred, no line is printed — the log records the pattern, not the
incident, exactly as a real cue sheet would. Builders sometimes propose
making the hair clickable or acknowledged ("dismiss"); refuse it — you do
not click a hair out of a gate; you note it and clean the gate after the
show.

### 6.12 The booth-window navigation

**What & why.** The fixed header is the booth's rear wall, and its
navigation is the frame index: a typed list of the strip's frames ("FR. 01
PROGRAMME · FR. 04 THE PRINT · FR. 07 SHOWTIMES") that the projectionist
cranks to. Navigation by frame number is the booth's native filing system.

**Structure.** `<nav class="booth-window">` fixed at the top: venue name
(Limelight, small), the index (horizontal on desktop, a typed disclosure
list on mobile), and the footage counter (§6.4) at the right. Each index
entry is an anchor to its frame's `id`; the entry for the frame currently
in view carries the amber cue dot (a 6px circle — the pencil mark the
projectionist makes against the running order).

**Motion spec.** Clicking an entry cranks the strip to the frame: a 900ms
quantised fast-crank (the §6.3 mechanism at high velocity, quantisation
suspended, landing settle 90ms `--ease-settle`). The cue dot moves with a
160ms `--ease-draw` slide as frames pass (scroll-spy driven by the loop's
frame-boundary readings, the same data as §6.4's rail). The nav bar itself
never hides, shrinks or transforms — the booth wall does not move.

**Choreography timeline.** Click → t=0 crank begins → t≈820 arrival, settle
→ t=900 cue dot slides to the frame (if it hasn't already) → rest. Scrolling
manually: dot updates at each frame boundary, 160ms slide each.

**State matrix.** *Rest:* dot against the current frame. *Hover (entry):*
the entry's frame number warms to `--arc` (120ms). *Focus:* standard
outline; the dot does not move for focus alone (the dot reports position,
not attention). *Active:* the crank. *Scrolled-past:* dot tracks.
*Disabled:* JS off → entries are plain anchors; the browser jumps; the dot
is printed against FR. 01 and the entries still work. *Touch:* the mobile
disclosure list opens with a 240ms `--ease-crank` unroll (typed lines
appearing line by line, 40ms stagger — a cue sheet unrolling).

**Breakpoints.** ≥1200px: full index inline, up to 8 frames listed (a
longer strip groups frames under "REELS" sub-entries — see §7). 768–1199px:
index inline but frame titles shorten to their nouns (typed abbreviations
are in-voice). <768px: disclosure list; counter (§6.4) joins this bar.

**Edge cases & failure modes.** A page with 12+ frames: the index lists
frames in strip order with the current frame's neighbours always visible;
overflow entries live in the disclosure at all sizes (the wall is only so
wide). Anchor targets account for the fixed bar (scroll-margin-top = bar
height + 16px) at every size.

**Accessibility.** A real `<nav>` with a list of links; the cue dot is
`aria-hidden` and current position is stated with `aria-current="true"` on
the entry. The mobile disclosure is a `<button>` with `aria-expanded`,
closing on Esc and on selection. All entries ≥44px tall on touch sizes.

**Tokens.** `--booth-raise`, `--arc`, `--screen`, `--ease-draw`,
`--ease-crank`.

**Content-merge.** The index entries are the frames' real printed numbers
and titles — generated from the strip's own DOM order at build time, so the
index cannot drift from the page it indexes.

**Failure fallback & watchdog.** Plain anchors with no JS dependency; the
crank is an enhancement over a working jump. No watchdog needed.

**Reduced motion.** Crank becomes an instant jump; dot moves instantly;
mobile list opens without the unroll.

**Performance & mobile.** Scroll-spy reads the loop's existing frame data —
no extra observers. Mobile variant per breakpoints.

---

### 6.13 Programme frames — the show cards

**What & why.** Each screening is a card the size of a film frame: the
still, the title lettered, the typed facts (reels, footage, runtime,
showtime), and its reel-can button (§6.10) or its sold-out notice. The
programme is a strip of frames because that is what a programme *is* here —
and every fact on the card is a reading from §6.17, never copy written for
the card.

**Structure.** `<article class="prog-frame">` inside a frame (§4): still in
a sprocketed sub-border (a miniature of the page's own frame grammar), title
in Limelight, facts as a typed definition list, action row. Cards stack one
per frame on listing pages (§7); on the home page, the next screening's card
is the hero's companion frame.

**Motion spec.** Entry: the §5 reveal — still scales 1.08→1 (700ms
`--ease-crank`) as the card centres; fact lines type in line-by-line (90ms
stagger). Hover: §6.9 bloom under the still. The seats-remaining figure, if
shown, is a digit-wheel reading (§6.4's mechanism, one wheel set per card)
that steps only when the record changes (a booking elsewhere) — it never
animates for decoration.

**Choreography timeline.** Card enters → still scale (700ms) → facts stagger
(3–5 lines × 90ms) → action row settles (`--ease-settle` 180ms) → rest.

**State matrix.** *Rest:* complete card. *Hover/focus:* bloom + can sheen.
*Sold out:* the can is absent; in its place a typed notice on a dust strip:
"SOLD OUT — THE PRINT RETURNS TO THE VAULT" (the exact string from §12);
the still dims to 70% and its frame number is struck with a pencil line —
the projectionist has crossed this one off the running order. *Disabled:*
not applicable to the card itself (only its button has states, §6.10).
*Scrolled-past:* unchanged. *JS off:* cards complete; sold-out state is
printed by the server/record, not by script. *Touch:* tap = focus bloom
(§6.9 rule), second tap follows the can.

**Breakpoints.** ≥1200px: card frame full strip width, still left (46%),
facts right. 768–1199px: still 40%. <768px: still stacks above facts; fact
lines full width; the can goes full-width (a can you can hit with a thumb).

**Edge cases & failure modes.** A screening with no still (common for
archive one-offs): the card prints its frame with the typed words "NO STILL
SURVIVES" centred in the empty frame — the archive's honesty again, never a
placeholder image. A title longer than two Limelight lines: the card grows;
frame lines are per-card, so the strip absorbs it. Seats figure missing
from the record: the line is omitted entirely (the strip prints nothing it
does not know, §6.17's law).

**Accessibility.** The card is an `<article>` with the title as its heading;
facts are a real `<dl>`; the sold-out notice is text, not just a dimmed
image (the dim is `aria-hidden` styling on the still's wrapper). The can is
a real button/link per §6.10.

**Tokens.** `--screen`, `--dust`, `--arc`, `--booth-raise`, `--ease-crank`,
`--ease-settle`.

**Content-merge.** The card's facts are the screening: reels and footage
from the sheet, runtime computed from them, showtime from the sheet. A card
cannot display a runtime the sheet doesn't produce — the build renders
cards *from* §6.17's data.

**Failure fallback & watchdog.** Static-first in full; the entry reveal is
loop garnish with the standard frame fallback (§5: frames render visible by
default). No watchdog beyond the loop health check.

**Reduced motion.** No scale, no stagger — the card is printed. Sold-out
strike and notices unchanged (they are print, not motion).

**Performance & mobile.** Stills are the page's main weight: each card still
≤90KB (see §14), `loading="lazy"` below the second card. Mobile stacking
per breakpoints; the digit wheels for seats are dropped <768px in favour of
a printed figure (wheels are machinery; small rooms read the number).

**A second card, worked (the matinee short).** The same element under the
sheet's other print shows the grammar holding at the record's edges:
*The Doll's Revenge* (1908), matinee only. Its card prints the empty frame
— "NO STILL SURVIVES" centred in the sprocketed border — because the sheet
says no still survives, and the card may not borrow the feature's still or
a stock image to fill the hole. Its facts line reads "1 REEL · 640 FT ·
11 MIN AT 16 FPS · ONE REEL — NO CHANGEOVER" — the absence of cues stated
as a fact of the print (§6.17's two-speed ruling), not left as a blank the
visitor might read as an omission. Its can reads "BOOK FOR THE 14:30" and,
the matinee being the family show, its caption band carries the booth's
one concession to the audience's world: "CHILDREN AT THE DOOR PRICE —
THE SHEET AT THE OFFICE HAS IT." The card does not print a child price,
because the sheet (§6.17) does not carry one: it points to where the true
figure lives rather than inventing a plausible one. That refusal — a card
visibly declining to complete itself — is this element's honesty test, and
§10's figure audit passes the card precisely because the number is absent.

### 6.14 The changeover table — showtimes & runtimes

**What & why.** The evening's running order as a typed table: showtime,
print, reels, footage, runtime, changeover cues, seats. It is the
projectionist's own sheet pinned inside the booth — and the visitor reads
the same sheet the booth runs on. Tables in this theme are paperwork, and
paperwork is typed, ruled and left-aligned (Type law 4).

**Structure.** A real `<table>` on a cream card (the sheet is paper, so it
is cream in the booth's black room) with booth-ink text: caption ("TONIGHT'S
RUNNING ORDER — FROM THE CHANGEOVER SHEET"), column heads in small
Limelight, rows in Special Elite, hairline rules in booth at 25%. Each row's
changeover cell lists cue footages (e.g. "990 · 1,965 · 2,950 · 3,910 FT").
One row per screening; the next screening's row carries the amber cue mark
in its margin.

**Motion spec.** Rows are print: no entry animation beyond the frame's own
reveal (§5). As the visitor scrolls the table, a pencil cue-mark — a small
SVG circle-and-cross, the mark a projectionist pencils on film at a cue —
draws itself (`--ease-draw`, 260ms) beside each row as that row crosses the
viewport centre, marking "you have read this far down the sheet". The marks
ratchet like §6.6 (they stay drawn; the sheet remembers being read).

**Choreography timeline.** Row crosses centre → cue mark draws 260ms →
next row. Table fully passed → all marks drawn; the sheet is read.

**State matrix.** *Rest:* full table printed, marks undrawn (18% dust
pre-print, as §6.6). *Reading:* marks draw per row. *Scrolled-past:* all
drawn. *Hover (row):* the row's paper warms — cream → `--screen` full from
`--screen-dim` at 150ms (a hand resting on the sheet). *Disabled:* JS off →
marks printed fully in dust; table complete. *Touch:* identical; marks are
scroll-driven.

**Breakpoints.** ≥1200px: all 7 columns. 768–1199px: changeover cues move
to a second line inside the print cell (the sheet is re-ruled, not shrunk).
<768px: the table becomes a stack of typed blocks per screening (time,
print, facts as lines) — a table that needs horizontal scrolling in the
booth is a sheet that doesn't fit the wall; §10 fails any build that
scrolls it sideways.

**Edge cases & failure modes.** A day with one screening: the table has one
row and that is correct — no padding rows, no "more coming" filler. A print
with an unusual speed (16fps silents): the runtime column shows the
computed figure with the speed noted ("72 MIN AT 18 FPS") — the sheet
always shows its working. Numbers are rendered from §6.17; a hand-typed
runtime in the table's HTML that disagrees with the sheet fails §10's
figure audit.

**Accessibility.** Real table semantics with `<th scope>` and a caption;
the cue marks are `aria-hidden` decoration. Row hover warmth is never the
only state signal. Cream card contrast: booth on cream 13.6:1 throughout,
including the dim pre-print rows (`--booth` at full strength — dimming
paperwork text is forbidden).

**Tokens.** `--screen`, `--screen-dim`, `--booth`, `--dust`, `--arc`,
`--ease-draw`.

**Content-merge.** The table *is* §6.17 printed for reading — same figures,
same order. It merges by identity, not by styling: there is one record and
this is its public face.

**Failure fallback & watchdog.** Static print; the marks' pre-state is
visible. No watchdog needed.

**Reduced motion.** Marks printed fully; row warmth instant.

**Performance & mobile.** One table, a handful of small SVG marks. Mobile
stacked blocks per breakpoints (the marks draw beside each block instead).

### 6.15 The box-office form — booking in the booth

**What & why.** The conversion moment, kept in the world: booking seats for
a screening is filling in the booth's own booking slip — typed fields on a
cream slip, a reel-can submit (§6.10), and a confirmation that arrives as a
ticket stub torn from the strip. The form's screening, showtime, price and
remaining seats all come from §6.17; the form can no more invent a price
than the counter can invent footage.

**Structure.** A `<form>` on a cream slip inside a frame: screening summary
line (printed from the record), name, email, seats (a stepper built from
two small cans and a digit reading), a typed total that recomputes from the
sheet's price × seats, submit can ("BOOK FOR THE 19:45" — the actual
showtime). Confirmation replaces the slip's lower half with a ticket stub:
perforated edge (a row of sprocket holes — the strip's own perforation),
the booking reference typed large, and the cue line "ARRIVE BY THE LEADER —
DOORS AT 19:15" computed from the showtime (doors 30 min prior, per §6.17).

**Motion spec.** Field focus: the field's bottom rule draws amber
(`--ease-draw`, 220ms) — the pencil underlining the line being written.
Seats stepper: the digit steps with the §6.4 wheel mechanism (90ms/step);
the total reprints (no tween — a new typed figure replaces the old, with a
120ms `--ease-flash` frame-line blink on the total's rule). Submit: the
§6.10 clunk, then the stub tears in: it translates 12px down from behind
the slip's perforation line with `--ease-settle` 380ms and a 60ms 0.4°
rotation settle (paper finding its lie) — the only rotation on the page,
because paper, unlike frames, can sit crooked. Errors: the error strip
(§11) slides from the slip's top, 200ms `--ease-crank`, and the offending
field's rule goes `--arc` full with the message typed beneath it in the
booth's voice (§12).

**Choreography timeline.** Focus → rule draws 220ms. Stepper click → wheel
step 90ms → total blink 120ms. Submit → clunk (90ms, §6.10) → validation:
clean → stub tears in 380ms + perforation shadow settles 200ms → focus
moves to the stub's heading (the one deliberate focus move on the page,
announced by the live region: "Booked — reference …"). Error → strip slides
200ms, focus to the first error field, message typed.

**State matrix.** *Rest:* slip printed, total showing the 1-seat figure.
*Focus:* rule draw. *Filled:* completed fields carry a small typed tick in
dust at their right (the clerk's mark). *Submitting:* can pressed-flat,
label "THREADING THE PROJECTOR…" (the booth's honest wait), form inert but
fully visible. *Success:* stub state as above; the form's data remains
readable above the stub (nothing is wiped). *Error:* per-field messages +
strip; no data is ever cleared by an error. *Disabled (screening sold
out):* the form is replaced by the §6.13 sold-out notice and the vault
line — a form for a show that cannot be booked is never rendered.
*JS off:* the form is a working form (server round-trip); stepper becomes a
plain number input; total prints the 1-seat figure with "TOTAL PER SEAT —
THE SLIP SHOWS ONE; THE OFFICE CONFIRMS" honesty line. *Touch:* stepper
targets 48px; the tear-in identical.

**Breakpoints.** ≥1200px: slip 560px wide, two-column name/email row.
768–1199px: slip full frame width, fields stack. <768px: slip full width,
stepper full-width row, submit can full width at the slip's foot.

**Edge cases & failure modes.** Seats requested > remaining: the stepper
caps at the record's figure and the cap is explained in type ("ONLY 6 LEFT
ON THE SHEET") — never a silent clamp. Price or seats missing from §6.17:
the form does not render; the frame prints the §11 alert in the booth's
voice and §10's gate blocks the build. Network failure on submit: the slip
stays filled, the error strip says the office couldn't be reached and to
keep the slip — data loss on failure is the one unforgivable sin here.

**Accessibility.** Real labels, `aria-describedby` for errors, error summary
in a live region, focus management as choreographed. The perforation and
stub are visual; the confirmation's information is plain text in reading
order. Contrast: booth on cream 13.6:1; the amber focus rule is paired with
a 2px weight change so it is not colour-alone.

**Tokens.** `--screen`, `--booth`, `--arc`, `--dust`, `--ease-draw`,
`--ease-flash`, `--ease-settle`, `--ease-crank`.

**Content-merge.** Every figure on the slip — price, seats, showtime, doors
time — is the record's. The stub's reference is the booking's own (server-
issued), and the perforation is the strip's sprocket grammar: the ticket is
torn from the same film the page is made of.

**Failure fallback & watchdog.** Submission is a real form post; the JS
enhancements (stepper wheels, tear-in) degrade to the printed slip. A
submission watchdog at 6s returns the can from "THREADING…" to its label
with the keep-your-slip error if the request hangs — the visitor is never
left watching a stuck machine.

**Reduced motion.** No tear-in (the stub prints), no blink on the total, no
clunk jolt; rules draw instantly. The information sequence is unchanged.

**Performance & mobile.** The form is DOM-light; the only animation is
transform/opacity on the stub. Mobile per breakpoints; the digit wheel for
seats is kept (it is small) but the total's blink is dropped <768px.

### 6.16 Reel change — loader & page transition

**What & why.** Moving between pages is a reel change: the lamp dims, the
iris closes, a leader card names the incoming reel, the iris opens on the
new strip. Loading states are unexposed frames (§5). The booth never shows
a spinner — a projector is either threaded or it is not.

**Structure.** Transition overlay (JS-inserted, like §6.1): booth black with
a printed reel card — "REEL 2 — THE PROGRAMME" in Limelight with the typed
frame title beneath — and an iris diaphragm (§6.2's mechanism in reverse).
Skeleton state for slow content: the incoming frame printed as unexposed
stock — cream, frame lines, the typed line "UNEXPOSED — AWAITING THE
PRINT", and the frame's real headline already set in Limelight (headlines
are print, they do not wait for pictures).

**Motion spec.** Exit: iris closes 350ms `--ease-iris` + lamp dim (flicker
layer to 0 over 200ms). Card: reel card holds 300–700ms (as long as the
navigation actually takes, min 300 so the card can be read, max 700 before
the new page is shown regardless — the show does not wait for ceremony).
Enter: §6.2's iris at 450ms. Hard ceiling: 2,400ms total; a watchdog forces
the enter state at the ceiling. Same-page anchors use §6.12's crank instead
— the reel change is for page changes only.

**Choreography timeline.** Click → t=0 dim + iris close (350ms) → card
(min 300ms, overlapped with load) → new page ready → iris open 450ms →
flicker layer fades up 800ms → rest. Leader (§6.1) does NOT replay; the
reel card carries the new page's frame title, so the ceremony informs.

**State matrix.** *Rest:* no overlay. *Exiting / holding / entering:* as
timeline. *Failed navigation:* iris reopens on the same page (450ms) with
the §11 alert typed on the reel card's line 2 — the visitor is told the
reel would not thread, in the booth's voice. *Disabled:* JS off → ordinary
navigation, no overlay exists. *Touch:* identical.

**Breakpoints.** All sizes: card scales per §6.1's leader sizes at −20%.

**Edge cases & failure modes.** Prefetched/instant navigation: the card's
300ms minimum is waived if the browser reports the page ready before the
iris has closed (the ceremony never delays a ready show by more than the
close itself). Back/forward cache restores: no transition — the strip is
simply there, mid-reel, as a returned-to film would be.

**Accessibility.** The overlay is `aria-hidden`; a live region announces
the new page's title on arrival (standard SPA practice, in the booth's
words: "Reel 2 — The Programme"). Focus moves to the new page's first
heading on enter — the one place the theme manages focus, because a reel
change is a place change.

**Tokens.** `--booth`, `--screen`, `--arc`, `--ease-iris`.

**Content-merge.** The card names the actual incoming page from its own
title and frame count ("REEL 2" = the page's ordinal in the site's running
order, from the site record) — the ceremony is the site's table of contents
performed.

**Failure fallback & watchdog.** The 2,400ms ceiling watchdog plus the
overlay's JS-inserted nature: any failure — exception, hang, bfcache
weirdness — ends with the overlay removed and a page showing.

**Reduced motion.** No iris, no card hold: a plain cut with the reel card
shown only if loading genuinely exceeds 700ms (as a static notice).

**Performance & mobile.** Overlay is two elements and one clip animation.
Mobile: identical, card smaller (above).

**Where the reel number comes from.** The card's "REEL n" is not the
destination's position in a menu — it is the page's ordinal in the site's
declared running order, a small site-level record kept beside §6.17's
sheet: home is Reel 1 (the feature), the programme listing Reel 2, each
screening detail takes the next numbers in programme order, and the
paperwork pages (about, contact, membership) are the final reel,
collectively — the booth's paperwork is one reel of many pages, which is
why moving between two paperwork pages uses a plain cut with no card at
all (you do not change reels to turn a page of the same ledger). If the
running order record is absent, the card prints the page's title alone
with no reel number — the ceremony degrades to honesty rather than
inventing an ordinal. The 404 (§6.18) has no reel number and never
receives a transition card inbound: there is no reel to change *to*, and
the dark booth must be reachable without theatre when something has
already gone wrong.

### 6.17 The changeover sheet — the reel record

**What & why.** The theme's one declared record, from which every figure on
the page is printed: for each screening — print title, year, reels with
footage per reel, projection speed, computed runtime, changeover cue
footages, showtimes, doors times, price, seats, and the repair log (burns,
splices, missing stills). If a number is not derivable from this sheet, it
does not appear on the page. This element is the theme's law (§1) made into
a buildable object.

**Structure.** A single data object (JSON in the build, or a typed table in
the CMS) — in the worked example: *The Orpheum Revival House, tonight:*
"The Cabinet of Dr. Caligari" (1920), restoration print of 1962/1987;
reels R1 990 ft, R2 975 ft, R3 985 ft, R4 960 ft, R5 950 ft — **total
4,860 ft**; leader pre-roll 24 ft; speed **18 fps**; runtime = 4,860 × 16 ÷
18 = 4,320 s = **72 min**; changeover cues at cumulative **990 · 1,965 ·
2,950 · 3,910 ft**; showtimes **14:30** and **19:45**, doors 30 min prior;
price **£9.50**; house **212 seats**; repair log: Reel 3 burnt (1962, corner
of one frame), splice R3→R4 cement (1987), no still survives for the
matinee's supporting short. The sheet also prints, as a page element, in
§6.14's table and as a typed card in the footer area of archive pages — the
record is shown to the visitor, not hidden in code.

**Motion spec.** The sheet itself does not move — paper doesn't. Its
*readings* move elsewhere (counter §6.4, wheels §6.13, form §6.15). As an
element its only behaviour: when printed on the page, its rows receive the
§6.14 cue-mark treatment.

**Choreography timeline.** None (paper). Build-time: the sheet is validated
(footages sum, runtime arithmetic, cue cumulatives) before any element
renders — a sheet that doesn't sum doesn't ship (§10).

**State matrix.** *Rest:* the record, printed where the page shows it.
*Stale (a screening has passed):* its showtime rows are struck with the
pencil line (the day's sheet is annotated, never silently edited — at
day's end the sheet is re-typed for tomorrow). *Missing data:* the affected
figure is absent everywhere (§6.13's rule) and §10 blocks the build.
*Disabled:* not applicable — data has no JS state. *Touch:* n/a.

**Breakpoints.** As printed matter it follows §6.14's table breakpoints
when shown as the table, and §6.13's card rules when shown as a card.

**Edge cases & failure modes.** A print at a non-standard speed: the sheet
carries the speed per print, and every runtime derived from it shows its
working (§6.14). Two prints sharing a title (different years): the sheet
keys screenings by print + year, and cards must show the year — the booth
never lets two prints share a label. A repair after the sheet is typed
(tonight's print tears): the sheet is amended by a typed correction slip
pasted over the row — visibly amended, in the world's grammar, with the
original still legible beneath.

**Accessibility.** As a printed table/card it inherits §6.14/§6.13's specs.
As data it has no interface; its accessibility duty is that everything
derived from it is real text somewhere (§6.4's hidden reading, §6.14's
table).

**Tokens.** Consumed by: `--counter-feet-total`, and every figure-bearing
element (§6.4, §6.13, §6.14, §6.15). The sheet itself consumes the palette's
paper tokens when printed.

**Content-merge.** Total: the sheet is not merged *with* the content, it
*is* the content's source. §10's figure audit greps the built page for
every numeral and traces each to this sheet.

**Failure fallback & watchdog.** Build-time validation is the watchdog: sum
checks (reels = total), runtime recomputation, cue cumulatives, and a
render-time assertion that the counter's maximum equals the sheet's total.

**Reduced motion.** Paper has no motion to reduce.

**Performance & mobile.** One small JSON object (<2KB for a full evening).
No mobile variant — arithmetic is the same in every room.

**The sheet, printed in full (worked record).** So two builders produce the
same record, the sheet's canonical form is a table with one row per reel
plus a header block per screening:

| Field | Tonight's entry |
|---|---|
| House | The Orpheum Revival House |
| Print | *The Cabinet of Dr. Caligari* (1920), restoration print |
| Leader pre-roll | 24 ft (counted by §6.4, never hidden) |
| Speed | 18 fps (this print; see the 16 fps ruling below) |
| Reel 1 | 990 ft — cue out at 990 ft |
| Reel 2 | 975 ft — cue out at 1,965 ft |
| Reel 3 | 985 ft — cue out at 2,950 ft · *burnt 1962, corner of one frame* |
| Reel 4 | 960 ft — cue out at 3,910 ft · *splice in, cement, 1987* |
| Reel 5 | 950 ft — print ends at 4,860 ft |
| Total footage | **4,860 ft** (990+975+985+960+950 — the sum is printed, not asserted) |
| Runtime | 4,860 × 16 ÷ 18 = 4,320 s = **72 min** |
| Showtimes | 14:30 · 19:45 — doors 30 min prior (14:00 · 19:15) |
| Price / house | £9.50 · 212 seats |
| Supporting short (matinee only) | *The Doll's Revenge* (1908), 1 reel, 640 ft at 16 fps = 640 × 16 ÷ 16 = 640 s ≈ **11 min**; no still survives (§6.13 prints the empty frame) |

**The two-speed ruling.** Speeds are per print, never per venue: the
matinee short runs at 16 fps, the feature at 18 fps, and every runtime on
the page shows which speed produced it ("11 MIN AT 16 FPS" / "72 MIN AT
18 FPS"). A build that stores one global speed and derives both runtimes
from it fails §10's audit on arithmetic, not on taste. Changeover cues
exist only between reels of the same print — the short has one reel and
therefore no cues, and its card (§6.13) prints "ONE REEL — NO CHANGEOVER"
rather than an empty cue cell: the sheet states absences, it does not
leave blanks.

### 6.18 The dark booth — 404 & empty states

**What & why.** A missing page is the booth with the projector off: the
strip runs out into black leader, one frame is printed with the typed
notice, and the way back is the frame index. The 404 does not pretend the
film exists; it shows the empty booth and the door.

**Structure.** A black page: the rails continue (the strip's edges persist)
but the frames stop — after the last real frame, 40vh of plain black
leader, then one cream frame, printed (not animated): "NO SUCH REEL — THE
BOOTH HOLDS NO PRINT BY THAT NAME." Beneath, the typed next actions: the
frame index (§6.12's list, printed statically) and the evening's sheet
(§6.14) — the two things a person in a dark booth actually needs. Empty
states elsewhere (no screenings today, no results for a festival strand)
use the same grammar at frame scale: an unexposed frame (§6.16) with the
typed reason and the nearest real alternative from the record.

**Motion spec.** None, by specification. The dark booth is the one page
where the lamp is off: no flicker, no iris, no crank theatre — a single
exception: the frame-index links carry §6.10's cans, whose clunk still
answers (the machine is off, but the bench is real). Choreography: there
is none, and §10 checks that none was added.

**Choreography timeline.** None — specified as *none*. The page is a
printed notice in a dark room.

**State matrix.** *Rest:* the printed notice and the ways back. *Hover/
focus:* can sheen and outlines only. *Disabled:* identical (nothing here
needs JS). *Touch:* identical.

**Breakpoints.** ≥1200px: notice frame centred at strip width. <768px: the
black leader shortens to 24vh (a small room reaches the notice faster);
rails persist at mobile width (§6.4).

**Edge cases & failure modes.** A 404 for a *screening that existed* (past
date): the notice names it from the record if the build can ("THAT PRINT
PLAYED ON 14 NOV AND HAS RETURNED TO THE VAULT") with the next screening of
the same print if one exists — the booth remembers its programme. A true
unknown URL gets the generic notice. Neither version invents a screening.

**Accessibility.** The notice is the page's `<h1>`; the index list is a
real nav; contrast is the standard pair. No motion means no motion risk —
the safest page on the site is the lost one, which is correct.

**Tokens.** `--booth`, `--screen`, `--dust`, `--gate-line`.

**Content-merge.** The 404's content is the site's real index and the real
evening sheet — the way back is made of the site's actual material, not a
generic "go home" button.

**Failure fallback & watchdog.** The page is the fallback. Nothing to watch.

**Reduced motion.** Identical — there was no motion to reduce.

**Performance & mobile.** The lightest page on the site (<15KB total).
Mobile per breakpoints.

---

## 7. Page application map

| Page type | How the theme plays |
|---|---|
| **Home** | The full ceremony: leader (§6.1), iris (§6.2), hero title card for tonight's feature, the pinned scene (§6.8), programme frames (§6.13) for the week's screenings, the burnt frame + splice (§6.5/§6.6) carrying the restoration story, the changeover table (§6.14) as tonight's sheet, footer as run-out leader (§6.18 grammar). One pin, one burn, one splice — never two. |
| **Programme / listing** (festival strand, season) | No leader (the ceremony is for arrivals, not for browsing); frames are §6.13 cards in strip order, grouped by reel (day) with typed reel dividers; the index (§6.12) lists days, not frames. Filters are typed slips pasted over the strip's margin — results re-deal as frames, never as a grid. |
| **Screening detail** | The print's own page: its sheet (§6.17) printed in full as the §6.14 table, its three intertitles as the pinned scene (§6.8) if stills exist, its repair log as a burnt/splice pair only if the record actually lists damage — a pristine print gets no fake wounds (§9). Booking is §6.15 on the same page. |
| **About / the venue** | The booth itself: frames of typed history, the projector's plate (maker, year — from the venue's real record), staff as the booth's crew list. The hair-in-the-gate (§6.11) is licensed here at its full rarity; the leader is not (you don't count down to a history page). |
| **Archive / restoration notes** | The damage grammar leads: burnt frames and splices carry case notes, each tied to a named print and date from the repair log. Before/after stills sit in sprocketed frames with the §6.9 lamp for inspection. |
| **Contact / membership** | Paperwork pages: cream slips, typed fields (§6.15's grammar without the booking figures), cans for actions. No pins, no burns — the office is not the booth floor. |
| **Checkout (dense seat maps, payment)** | **Routed out of the theme.** Seat-picking grids and payment forms leave the strip: a plain, fast, high-contrast surface in the venue's name, entered from §6.15's slip ("THE OFFICE HANDLES SEATS AND CARDS — STEP THROUGH"). The booth sells the ritual; the office takes the money. §10 fails any build that themes a payment form. |

## 8. Worked examples

The venue throughout: **The Orpheum Revival House**, tonight's feature the
restoration print of *The Cabinet of Dr. Caligari* (1920) — all figures from
§6.17's sheet: 5 reels, 4,860 ft, 18 fps, 72 min, cues at 990 · 1,965 ·
2,950 · 3,910 ft, shows 14:30 & 19:45, £9.50, 212 seats.

### 8.1 The hero (home) — the programme begins

The visitor arrives in darkness. The leader (§6.1) counts 3…2…1 in drawn
circles, "REPERTORY — NIGHT THREE" typed beneath from the site's record.
The iris (§6.2) opens on FR. 01: the title card — "THE CABINET OF DR.
CALIGARI" in Limelight at 96px, beneath it the typed line "RESTORED PRINT ·
5 REELS · 4,860 FT · TONIGHT 19:45", and the feature still in its sprocketed
frame, scaling 1.08→1 as the iris clears. The booth window (§6.12) is
already in place above; the footage counter (§6.4) reads 00024 — the
leader's pre-roll, honestly counted. Scroll timeline: first crank catches
(§6.3) as FR. 01 leaves; the left rail's first holes fill as the hero's
frames pass; at 40% scroll the pinned scene (§6.8) approaches with its
first intertitle already printed. Nothing on this hero is decorative: the
title is the show, the figures are the sheet, the counter is the machine.

### 8.2 Mid-page: the burnt reel (restoration notes)

FR. 06 carries the restoration notes for Reel 3. Its still — a frame from
the reel — has its top-right corner eaten by the burn (§6.5): blister field
breathing at its seeded rates, edge warming as the frame centres. The
caption, typed in the margin: "REEL 3 TOOK THE LAMP'S HEAT IN 1962. THE
CORNER IS GONE; THE REST IS THE RESTORATION'S." The notes themselves —
what was done in 1987, what the cement splice cost in frames — run in the
protected text column. In the splice gap below, the line draws (§6.6) as
the join crosses centre: "SPLICED AT THE BOOTH — REEL 3 TO REEL 4, CEMENT
SPLICER, 1987." Scroll timeline: burn frame centres (glow beat) → notes
read at crank pace → splice draws across ~340px of scroll → FR. 07 (the
programme's next card) enters with its still scaling in. The visitor has
been told, in order: what was damaged, what it cost, how it was mended —
the archive's whole argument in three frames.

### 8.3 Conversion: booking the 19:45

FR. 09 is the box-office slip (§6.15). Its summary line is printed from the
sheet: "THE CABINET OF DR. CALIGARI — TONIGHT 19:45 — £9.50 A SEAT — 212 IN
THE HOUSE, 41 LEFT ON THE SHEET." (The 41 is the record's live figure; if
the record has no live figure, the line omits it — §6.13's rule.) The
visitor types name and email (amber rules drawing under each field), steps
seats to 2 (wheel steps, total reprinting £19.00 with its rule blink), and
presses the can: "BOOK FOR THE 19:45". Clunk — 90ms — and the stub tears
in below the perforation: reference typed large, "ARRIVE BY THE LEADER —
DOORS AT 19:15", focus announced. If instead the sheet said sold out, FR.
09 would never have carried the form at all: the §6.13 notice would stand
in its place, and no visitor would fill a slip for a show that cannot seat
them.

## 9. Anti-slop — what makes THIS theme look cheap

1. **Smooth, buttery scrolling.** The crank (§6.3) is the theme's handshake;
   a build that glides has removed the machine and kept the wallpaper.
   *Cure:* quantised crank, always, with the fast-crank suspension as the
   only relief.
2. **Flicker on the words.** A global opacity flicker over text is the
   fastest route to "haunted website". *Cure:* flicker lives on the light
   layer only (§2's ruling); §10 tests it.
3. **A percentage progress bar.** Feet or nothing. *Cure:* §6.4's rail and
   counter, fed by §6.17.
4. **Fake damage everywhere.** Burns and splices on every frame turn
   provenance into a filter pack. *Cure:* one burn, one splice, each named
   to a real print in the record (§6.5, §6.6 gates).
5. **A pristine print given fake wounds.** The inverse sin: §7 forbids
   damage grammar on prints whose log is clean.
6. **Intertitle swells on every line.** If every word is mouthed, none is.
   *Cure:* one authored key word per card (§6.7).
7. **Numbers that don't sum.** A runtime typed by hand that disagrees with
   the footage is the booth's cardinal sin. *Cure:* §6.17 + §10's figure
   audit — every numeral traced.
8. **Sepia photo filters as "vintage".** The palette is four exact colours;
   a sepia wash over stock photos is a costume, not the booth. *Cure:*
   stills sit in sprocketed frames under the lamp (§6.9), unfiltered.
9. **A spinner.** Projectors thread or they don't. *Cure:* §6.16's
   unexposed frames and reel card.
10. **Curtain/iris reveals on every section.** The iris is the programme's
    opening, not a scroll effect. *Cure:* iris at §6.2 and §6.16 only;
    frames reveal by the §5 scale-and-type grammar.
11. **The jitter as a glitch loop.** §6.11 unbounded is a broken site.
    *Cure:* the exact bounds — 1px, 3 frames, twice a session.
12. **Limelight everywhere.** Lettered type is for titles; a page of it is
    a poster, not a booth. *Cure:* Type law — paperwork is typed (Special
    Elite), and §10 checks the ratio.
13. **A themed payment form.** *Cure:* §7's routing rule — the office takes
    the money, plainly.
14. **The leader on every page.** The countdown is an arrival ceremony;
    replaying it on inner pages turns ritual into toll. *Cure:* §6.1 runs
    on the home arrival only (session-suppressed), §6.16's reel card —
    shorter, named, informative — handles every later change, and §7's map
    states per page type which ceremony, if any, it earns. A visitor who
    has been counted in three times has been welcomed once and delayed
    twice.

## 10. Quality gate

Blocking checks — all must pass before this theme ships in a build:

1. **Figure audit.** Every numeral on the page is grepped and traced to
   §6.17's sheet; reels sum to the total; runtime recomputes from feet ×
   16 ÷ speed; cue footages are the true cumulatives.
2. **No-JS pass.** With scripts disabled: no leader, no iris clip, all
   frames fully visible, counter printed as the sheet's total, form
   functional, 404 grammar intact.
3. **Reduced-motion pass.** `prefers-reduced-motion` yields the printed
   strip: no flicker, no jitter, no pin, no crank offset, leader as still.
4. **Flicker test.** Text contrast is measured at flicker extremes — since
   text is never in the flicker layer, readings are identical; any variance
   fails the build.
5. **Watchdog drill.** Kill the rAF loop mid-load: leader gone by 2,600ms,
   iris cleared by 1,400ms, crank offset zeroed, content complete.
6. **Damage census.** Exactly one burnt frame and one splice, each captioned
   with a named print and date from the repair log; zero damage grammar on
   clean prints.
7. **Crank check.** Scroll is quantised to the pitch at reading speeds,
   suspends above 2,400px/s, and the offset never exceeds ±½ pitch.
8. **Pin census.** Exactly one pinned frame (§6.8); on <768px, none.
9. **Counter truth.** The counter's maximum equals the sheet's total
   footage, and it starts at the leader's printed pre-roll.
10. **Form honesty.** Sold-out screenings render no form; seat caps are
    explained in type; a failed submission preserves all entered data.
11. **Table fit.** The changeover table never scrolls sideways at any
    breakpoint (stacked blocks <768px).
12. **Type ratio.** Limelight appears only in titles, card heads and the
    reel card; body and data are Special Elite throughout.

## 11. Component inventory

| Component | Booth treatment |
|---|---|
| Primary button | Reel can (§6.10) — dust metal, typed label, clunk |
| Secondary button | Flat typed link with amber cue underline (`--ease-draw` on hover) |
| Text input | Cream slip field, booth ink, amber rule draws on focus (§6.15) |
| Number stepper | Two small cans + digit-wheel reading (§6.15) |
| Select (screening) | A typed slip list — choosing a show reprints the slip from the record |
| Checkbox / radio | Pencil tick boxes: a square rule the visitor's click fills with a typed ✕ |
| Table | The changeover sheet (§6.14) |
| Card | Programme frame (§6.13) |
| Badge / tag | A pasted typed slip (strand name, "RESTORED", "WITH LIVE ACCOMPANIMENT") — pasted at a seeded 1–2° tilt, the page's only other rotation |
| Alert | A typed strip pasted across the frame's top, in the booth's voice (§12); errors in `--arc` rule + typed message |
| Toast | Refused — the booth does not whisper from corners; confirmations are stubs and strips in place |
| Modal | Refused — a modal is a second booth; confirmations happen on the slip (§6.15) |
| Tabs | Reel dividers: switching reels re-deals frames (§7 listing grammar) |
| Accordion | Cue-sheet folds: a frame's notes unfold with a 240ms `--ease-crank` unroll, one fold open at a time |
| Pagination | "THE STRIP CONTINUES — REEL 2" can at the foot; page numbers are reel numbers |
| Breadcrumbs | The frame index path (FR. numbers) printed above the frame, static |
| Progress | §6.4 rail + counter — no other progress UI exists |
| Skeleton | Unexposed frame (§6.16) |
| Tooltip | A typed caption slip appearing above the element, 150ms, plain words only |
| Focus outline | 2px `--arc`, offset 3px, everywhere, no exceptions |
| Footer | Run-out leader: black, the sheet reprinted small, the booth's address typed, "THE STRIP ENDS — THE HOUSE LIGHTS COME UP" as the final line |
| 404 / empty | The dark booth (§6.18) |

## 12. Content & copywriting voice

Two registers, as the booth has two hands. **The Lettered voice** (Limelight)
is the show: titles, programme names, ceremony — it speaks in short,
ceremonial lines and never explains. **The Typed voice** (Special Elite) is
the paperwork: captions, facts, errors, notices — it speaks plainly, in the
first person of the house ("we", the booth), and it admits everything.

- **Headlines:** the print's real title, lettered. Never a marketing line
  where a title belongs.
- **Labels:** typed, terse, factual — "REELS", "FOOTAGE", "AT 18 FPS".
- **Buttons:** the action with its object — "BOOK FOR THE 19:45", never
  "Submit" or "Go".
- **Error voice:** the booth admits and instructs. ✓ "THE OFFICE COULDN'T
  BE REACHED — YOUR SLIP IS KEPT; TRY AGAIN." ✗ "Oops! Something went
  wrong." ✓ "THAT SEAT COUNT IS MORE THAN THE SHEET HOLDS — ONLY 6 LEFT."
  ✗ "Invalid quantity."
- **Empty voice:** ✓ "NO SUCH REEL — THE BOOTH HOLDS NO PRINT BY THAT
  NAME." ✗ "404 — page not found."
- **Fixed strings (verbatim, do not paraphrase):** the sold-out line "SOLD
  OUT — THE PRINT RETURNS TO THE VAULT"; the leader caption pattern
  "REPERTORY — NIGHT THREE"; the splice caption pattern "SPLICED AT THE
  BOOTH — REEL n TO REEL n+1, CEMENT SPLICER, YEAR."; the closing line "THE
  STRIP ENDS — THE HOUSE LIGHTS COME UP."
- **Numbers:** always with their unit and, where computed, their working —
  "72 MIN AT 18 FPS". A bare number is a number hiding something.

## 13. Full-page scroll choreography map

Nine beats, top to footer (home page):

1. **Leader & iris** (§6.1, §6.2) — the ceremony; counter at the pre-roll.
2. **Title card at rest** — flicker layer fades up; the house is lit.
3. **First crank** — FR. 01 leaves with catches; rail holes begin to fill;
   the counter starts its honest climb.
4. **Programme frames** (§6.13) — stills scale in one by one; facts type in
   line by line; the visitor is reading the week's strip.
5. **The pinned scene** (§6.8) — three intertitles cycle through flicker
   dips; the screening inside the page.
6. **The burn** (§6.5) — the strip's wound; the lamp warms its edge as it
   centres; the pace of the crank seems to slow (it doesn't — attention
   does).
7. **The splice** (§6.6) — the repair draws across the join; the strip is
   whole again and says so.
8. **The sheet & the slip** (§6.14, §6.15) — paperwork: cue marks draw down
   the running order; the booking slip waits with its figures already true.
9. **Run-out** — the last frame passes, the counter rests at the sheet's
   total, the footer runs out into black leader and the closing line.

Reverse pass: the crank rewinds symmetrically (§6.3); intertitle cycles
reverse (§6.8); cue marks, the splice and filled holes *unfill/undraw only
where specified* — holes unfill (footage rewinds), the splice stays drawn
(a repair is permanent), cue marks stay (a read sheet stays read).
Jump-scroll (anchors, find-in-page): ratchets complete instantly (§6.6,
§6.12) — the strip never performs a journey the visitor skipped.

**The short-page variant (screening detail, five beats).** A detail page
runs a shorter strip and its choreography compresses, it does not merely
truncate: (1) no leader — arrival is a plain frame with the reel card's
title line as its head; (2) the print's own card (§6.13) opens, still
scaling in; (3) the pinned scene (§6.8) if the print has stills — the one
pin, kept; (4) the sheet (§6.14) with its cue marks, followed immediately
by the slip (§6.15) — on a detail page paperwork follows the scene without
programme frames intervening; (5) run-out: the repair log as a final typed
frame (damage pair only if the log lists damage), then the closing line.
Total frames on a detail page: 5–7. A detail page that pads itself with
programme cards from other screenings to reach home-page length has
misunderstood the strip: a short reel is a complete reel.

## 14. Whole-page performance budget

- **Total page weight:** ≤ 850KB home (stills dominate: hero still ≤ 160KB,
  programme stills ≤ 90KB each, lazy below the second card).
- **Fonts:** Limelight + Special Elite, subset to Latin + figures, ≤ 38KB
  total woff2; `font-display: swap` with the §3 fallbacks.
- **JS:** ≤ 30KB — one loop, the leader/iris arming, the form enhancements.
  No framework; the booth predates them and the budget enforces the joke.
- **Frame budget:** the shared loop's per-frame work ≤ 2.5ms on a mid
  phone; all animated properties are transform/opacity/clip-path.
- **Long tasks:** none > 50ms after load; the figure audit is build-time,
  never runtime.
- **Cut order when over budget:** (1) dust layer, (2) scratch parallax,
  (3) blister count on §6.5, (4) catch pulse on §6.3, (5) bloom filter
  nudge (keep the gradient). **Never cut:** the crank quantisation, the
  counter/rail, the watchdogs, the reduced-motion variant, the figure
  audit.

## 15. Build-order checklist

1. Type the changeover sheet (§6.17) and validate its arithmetic — before
   any markup.
2. Build the static strip: frames, rails, printed counter caption, all
   content visible with no JS and no CSS animation.
3. Print the table (§6.14) and cards (§6.13) *from* the sheet data.
4. Add the booth window + frame index (§6.12) with plain anchors.
5. Add the form (§6.15) as a working form; test the no-JS round trip.
6. Add the shared rAF loop; wire the crank (§6.3) and rail/counter (§6.4).
7. Add frame reveals (§5) and the lamp bloom (§6.9).
8. Add the burn and splice (§6.5, §6.6) with their captions from the log.
9. Add the pinned scene (§6.8) and the swell (§6.7).
10. Add the leader + iris (§6.1, §6.2) with watchdogs; add the reel change
    (§6.16).
11. Add the hair (§6.11) last, at its exact bounds — it is the easiest
    element to overdo and the last one the machine earns.
12. Reduced-motion variant pass over every element.
13. Run §10's gate: figure audit, no-JS pass, watchdog drill, damage
    census. Gate signed by a non-builder.
14. Re-run the figure audit after *any* later change to the sheet — a new
    showtime, a re-typed reel, a corrected price. The sheet is a living
    record in a working booth, and the audit is cheap precisely so that it
    can be run every time the record moves; a page whose figures were true
    at launch and drifted by the second week has failed the theme more
    quietly, and more completely, than one that never passed at all.
