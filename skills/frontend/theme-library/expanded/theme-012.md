# Theme 12 — Microfilm Reader (Expanded, v1 + v2 standard)

## 1. Concept & world

The site is a reel of microfilm threaded through a reader in a dark library
basement, and the visit is a screening. The visitor does not scroll a page;
they wind film. A fixed reader housing — gate mask, reel labels, sprocket
rails down both edges, a take-up reel, a mono frame counter — stays pinned
for the whole visit while the film streams through it. Every section is a
frame of the reel, separated by frame lines. Every seventh frame is a
**damaged frame**: scratched, light-leaked, and used as a chapter divider,
carrying a librarian's note about the damage in mono. The damage is not
decoration; it is catalogued, the way a real archive catalogues the flood
of March 1953 that took frames 041–048 of the Halstead Gazette reel.

The motion language is the machine's mechanics, and the machine does not
glide. Film advances in **ratcheted detents** — stepped moves with a 1px
overshoot-and-catch — because that is how a sprocket drive moves. Fast
winding blurs. Slow winding resolves. The reader zooms mechanically, with
detent pauses, the way a focusing knob clicks through magnifications. Dust
is in the light path. Grain crawls. The room is dark because the film is
the light.

**Mood.** Lamplight scholarship at midnight: quiet, mechanical, faintly
ceremonial. The visitor should feel they have been trusted with something
fragile and old, and that the machine between them and it is honest about
its own wear.

**Best fit.** Archives and special collections, genealogy and family-history
services, newspaper and periodical archives, documentary film production
companies (especially those working from archival footage), local-history
societies, records-retention and digitisation services, museum collection
portals. The theme earns its keep wherever the content genuinely is — or is
honestly presented as — a sequence of preserved frames with a catalogue.

**Audiences.** Researchers and genealogists (patient, detail-hungry,
desktop-leaning, often older — hence the large filmed-text sizes in §3);
documentary researchers scouting footage; local-history hobbyists arriving
from search with one name or one date in mind. All three read long and
scroll slowly, which is exactly the pace the detents reward.

**When NOT to use it.** E-commerce or anything with rapid comparison
shopping — detents fight scanning behaviour. Bright, cheerful consumer
brands — the reader room is dark by physics, not by mood-board. Data-dense
dashboards — the gate shows one frame at a time and will starve a table.
Any site whose content is not sequential: if the material has no honest
order, the reel is a lie and the visitor will feel it within two frames.
And never for content that must be skimmed under time pressure (checkout,
booking, support triage) — a machine that makes you wind is wrong there.

**The one law.** Every number the machine shows — frame counts, reel
totals, archive statistics — is computed from the reel's actual frames in
the DOM. The counter never displays a figure the catalogue cannot back.
(See §5, law 5.)

## 2. Palette

Four anchor colours, all of them physical: the dark of the room, the amber
of aged film under the lamp, the phosphor white of the reader screen, the
blue of celluloid edge-printing.

| Token | Hex | Role | Ratio | Pairing & contrast |
|---|---|---|---|---|
| `--room` | `#0E0F11` | Reader-room black — page ground, housing body | 62% | The darkness everything sits in. Never used as text on lighter grounds except mono labels on amber. |
| `--amber` | `#D9A441` | Film amber — the lit film itself: frame grounds, skeleton frames, the counter's digits, damaged-frame notes | 18% | On `--room`: 7.6:1 — passes AA for all text, AAA for large. On `--room` it is the primary reading accent. |
| `--phosphor` | `#E8E6DF` | Phosphor white — all filmed content text (Newsreader), frame titles | 16% | On `--room`: 15.2:1 — AAA at every size. The only colour body text is ever set in. |
| `--celluloid` | `#3D5A73` | Celluloid blue — edge-printing, frame numbers on the film edge, links' rest state, the gate's cool shadow | 4% | On `--room`: 2.8:1 — **graphic and large-label use only, never body text**. On `--phosphor` grounds (the rare printed-slip surfaces): 5.4:1, AA for text. |

Derived tokens (labelled derived; computed from the anchors, never new hues):

| Token | Hex | Derivation & role |
|---|---|---|
| `--gate` | `#08090A` | `--room` taken darker — the inside of the gate mask and the vignette corners. |
| `--amber-wound` | `#8A6A2B` | Amber at winding density — film already wound on the take-up reel, counter digits for frames already read. On `--room`: 4.1:1, large/mono only. |
| `--phosphor-aged` | `#9B978C` | Phosphor greyed by age — secondary filmed text: captions, catalogue notes, frame metadata. On `--room`: 6.9:1, AA. |
| `--scratch` | `#F5F3EC` | Near-white of a scratch catching the lamp — scratch lines, dust highlights. Graphic only. |

**Contrast law.** Body text is phosphor on room (15.2:1) or it does not
ship. Amber carries headings, counters and notes (7.6:1). Celluloid blue
never carries a sentence: it is edge-printing — frame numbers, reel codes,
the thin blue rule under a frame title — where its job is to be *located*,
not read at length. Any builder tempted to set a paragraph in blue has
misread the film: edge-printing was never the article.

**Dark-mode behaviour.** There is no light mode and no inversion to
specify: the reader room is dark because a projector lamp in a lit room
washes the film out. `prefers-color-scheme: light` is answered with the
same room — the theme's fiction is a basement, and basements do not have
windows. What *does* adapt is brightness discipline: on OLED the gate
vignette (`--gate`) does the work of keeping blacks true, and the amber is
never raised above its token value to "pop" — the lamp is the lamp.

**Usage discipline.** A frame is mostly room-black and phosphor. Amber is
rationed to the film's own lit areas: the frame ground glow, the counter,
damaged-frame furniture, skeleton frames. If amber exceeds roughly a fifth
of the viewport, the room stops feeling dark and the film stops feeling
lit — check at the gate (§10).

## 3. Typography

Two faces, and the split between them is the split between the film and
the machine.

**Newsreader** (variable, opsz) sets everything that is *on the film*:
headlines, body, captions, catalogue prose. It is a serif with a
photographic softness at large optical sizes — the filmed page. **IBM Plex
Mono** sets everything that is *on the machine*: reel labels, frame
counters, edge-printing, librarian's notes, button labels on the housing.
If a string would be printed on the film stock or typed by the cataloguer,
it is mono; if it would be photographed from the original page, it is
Newsreader. There is no third case.

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Reel title (hero frame headline) | Newsreader 72pt opsz | 64px / 1.04 | −0.01em | The filmed masthead. Never uppercase; the original page wasn't. |
| Frame headline (H2) | Newsreader 48pt opsz | 40px / 1.1 | −0.005em | One per frame, top-left of the gate, under its frame line. |
| Frame subhead (H3) | Newsreader italic | 26px / 1.25 | 0 | Italics are the film's own emphasis — the original editor's, not ours. |
| Body (filmed text) | Newsreader 18pt opsz | 19px / 1.55 | 0 | Filmed text reads large: 19px minimum, measure 58–66ch. Never below 17px at any breakpoint. |
| Caption / catalogue note | Newsreader | 15px / 1.5 | 0 | Set in `--phosphor-aged`. |
| Frame counter | IBM Plex Mono | 13px | 0.08em | Tabular figures; format `FRAME 012 / 340`; the current frame's digits in `--amber`, the total in `--amber-wound`. |
| Reel label / edge-printing | IBM Plex Mono | 11px, uppercase | 0.14em | Reel codes (`REEL 07 · HALSTEAD GAZETTE 1911–1968`), frame numbers on the film edge. Celluloid blue or amber-wound, never phosphor — machine print is never the content's colour. |
| Librarian's note | IBM Plex Mono | 13px / 1.6 | 0.02em | On damaged frames only, in `--amber`, prefixed `NOTE —`. The only voice allowed to comment on the film. |
| Housing button label | IBM Plex Mono | 12px, uppercase | 0.12em | Advance, rewind, request — the machine's verbs. |

**Laws.** (1) Mono never sets a headline; Newsreader never sets a counter.
(2) Frame numbers are always three digits, zero-padded — `FRAME 007`, never
`FRAME 7` — because the counter wheel has three drums. (3) All figures in
mono are tabular; a counting digit must never change the counter's width.
(4) Underlines are film scratches, not link styling: links in filmed text
carry a 1px celluloid rule that brightens to amber on hover (§6.13); no
browser-default blue exists anywhere on the reel.

## 4. Layout language

**The housing.** A fixed frame around the viewport for the entire visit:
top bar (reel label left, frame counter right, 44px tall), bottom bar
(reading-room status line: current frame title + detent indicator, 36px),
and the two sprocket rails. The housing is `--room` with a 1px `--gate`
inner shadow; it never moves, never fades, and is the only permanently
visible chrome. Content scrolls *through* it — the film moves, the machine
doesn't.

**Sprocket rails.** 34px wide at ≥1200px, running both viewport edges,
inside the housing. Sprocket holes: 10×14px rounded rects (2px radius),
`--gate` fill with a 1px top highlight in `#232529`, pitched every 26px.
The rails are part of the film layer, not the housing: they translate with
the film in detents (§6.2) while the housing bars stay fixed — the visitor
sees film move *through* a still machine, which is the whole illusion.
Below 1200px the rails narrow to 22px (holes 7×10px, pitch 26px); below
768px they leave the edges and become a single 12px perforated strip along
the top of the gate — a phone is a smaller reader, not a different machine.

**The gate.** The visible frame window: aspect 1.37:1 (the 16mm frame
proportion) for image-led frames, free height for text frames, but always
delimited by **frame lines** — 2px `--amber-wound` rules with the frame
number edge-printed in celluloid at the left end (`№ 012`). Text frames sit
on a very low amber ground-glow (radial, `--amber` at 4% over `--room`,
centred) — the lamp's pool. The glow belongs to the frame, never to the
housing.

**Frame rhythm.** One frame, one idea. A frame's content is vertically
centred in at least 92vh of travel so the detent has somewhere to land;
dense catalogue material is split across frames rather than shrunk. The
damaged frame (every 7th) is shorter — 60vh — a held breath between
chapters, carrying only its damage, its note, and the next chapter's title
edge-printed at its foot.

**Spacing.** The unit is the sprocket pitch: 26px. Vertical rhythm inside
a frame is 13px (half-pitch) and 26px; frame padding is 52px (two pitches)
at ≥1200px, 26px below. Nothing in the theme is spaced in numbers that are
not pitch multiples — the film's perforations are the grid, and a builder
measuring in arbitrary pixels will feel the reel wobble.

**Density.** Deliberately sparse. A microfilm frame holds one newspaper
page, not a dashboard. If a frame needs a scrollbar of its own, it is two
frames. Whitespace here is unexposed film — black, quiet, and part of the
record.

## 5. Full motion system

The machine has five named easings and six laws. Every element in §6 draws
from these and only these.

**Easing & duration tokens.**

| Token | Value | Used by |
|---|---|---|
| `--ease-detent` | `cubic-bezier(0.25, 1.3, 0.35, 1)` | The sprocket step: fast advance, 1px overshoot, mechanical catch. |
| `--ease-magnify` | `steps(24)` over the duration, with three 90ms holds | The zoom (§6.1): a focusing knob clicking through detents at scale 0.35 / 0.62 / 0.85. |
| `--ease-lamp` | `cubic-bezier(0.4, 0, 0.2, 1)` | Light behaviour: blooms, glow pools, lamp fades — light never snaps. |
| `--ease-drift` | `linear` | Dust, grain, wound-reel rotation — constant-speed machine processes. |
| `--ease-whip` | `cubic-bezier(0.7, 0, 0.84, 0.4)` | Fast-forward blur and the navigation whip (§6.12). |
| `--dur-detent` | `120ms` | One sprocket step. Never varies; the machine's heartbeat. |
| `--dur-catch` | `60ms` | The overshoot settle after a step. |
| `--dur-zoom` | `1400ms` | The entrance magnification (§6.1). |
| `--dur-settle` | `500ms` | Dust & scratches settling after the zoom locks. |
| `--dur-scratch` | `700ms` | A damaged frame's scratch-line draw (§6.5). |
| `--dur-bloom` | `2500ms` | One light-leak pulse (§6.7). |
| `--dur-whip` | `400ms` | Route-change fast-forward (§6.12). |
| `--lerp-film` | `0.18` | rAF smoothing factor for the film layer. |
| `--lerp-lens` | `0.09` | rAF smoothing for the magnifier/dust layer — it lags the film, and the lag is the depth. |

**The motion vocabulary, in the machine's language.**

- **Scroll-triggered reveals** — a frame reveals *through the gate*: a
  rectangular clip (the gate aperture) opens over the frame as its detent
  locks, 240ms `--ease-detent`. Content is never faded up from nothing;
  it is *exposed*, the way the lamp exposes the frame in the gate.
- **Detented scroll (the theme's scroll behaviour)** — film position is
  quantised to frame boundaries (§6.2). The browser scrolls freely; the
  film layer renders only at detent positions, stepping 120ms at a time.
- **Parallax layers** — three depths: the film (lerp 0.18), the dust/grain
  layer in the light path (lerp 0.09 — it lags, so it reads as nearer the
  lamp), and the housing (fixed). Sprocket rails travel with the film;
  frame-edge numbers travel at 0.92× film speed, a hair of mechanical slip.
- **Pinned scenes** — the housing pins for the whole visit; within the
  film, a damaged frame pins for its 60vh while its scratch draws (§6.5).
- **Masked reveals** — the gate aperture is the mask; the hero zoom (§6.1)
  is a magnification through it, and frame entrances are gate exposures.
- **Blur-to-sharp** — reserved for winding: fast scroll blurs the film
  (§6.3); as velocity drops the frame resolves. Nothing else blurs, ever —
  blur is speed in this world, not a reveal style.
- **Counters** — the frame counter ticks one detent per frame passed
  (§6.11); archive statistics count once, in mono, when their frame locks.
- **Progress** — the take-up reel's wound diameter, scrubbed (§6.4), plus
  the counter. There is no progress *bar* anywhere: bars are software;
  reels are machines.
- **Marquees** — refused. Film does not loop sideways. The reel index
  (§6.13) is the navigation, and it is still.
- **Ambient loops** — grain crawl (0.9s, 8-step loop) and dust drift
  (§6.6), light-leak blooms on damaged frames (§6.7). All ambient motion
  lives in the light path, over the current frame only.
- **Micro-interactions** — magnifier swell on hover (§6.8), the clunk on
  click (§6.9), the projector-jitter title lock (§6.10). All mechanical,
  all ≤250ms except the jitter's 1s settle.
- **Page transitions** — the fast-forward whip (§6.12): 400ms of blurred
  frames streaking to the next section, then a detent lock.
- **Image treatments** — images are frames of film: they scale-in-frame
  (1.06→1.0, `--ease-magnify` shortened to 600ms) inside their gate as
  they centre, with grain over them, never under. No image is ever shown
  un-gated; a photograph outside a frame is a photograph outside the
  archive.

**The six laws.**

1. **Film never glides.** Any film movement that renders as a smooth
   continuous slide is a defect. Steps, catches, or stillness — nothing
   between.
2. **The gate promise (1s).** Every gated reveal carries a 1000ms watchdog:
   if the reveal has not completed 1s after its trigger, the gate is forced
   open by class. Content never waits on choreography.
3. **Damage is catalogued, not decorative.** Scratches, leaks and the
   librarian's notes exist only on damaged frames, and each damaged frame's
   note describes *its* damage. Random distress anywhere else is slop (§9).
4. **The counter counts the reel.** Frame totals, current frame, and
   statistics are computed from the DOM's actual frames (§1's one law).
   A hard-coded `340` that the page cannot back is a failed gate.
5. **One rAF loop.** Film, dust, reel and counter render from a single
   requestAnimationFrame loop with the two lerp factors above. No element
   runs its own scroll listener.
6. **Stillness is a state, not an absence.** When nothing moves, the film
   sits locked in its detent with grain crawling — the machine idling.
   A frozen, grainless frame reads as a broken projector.


## 6. Signature elements

### 6.1 Mechanical zoom-in entrance

**What & why.** The visit begins the way a reading session begins: the
first frame is already threaded, tiny in the gate, and the reader focuses
it. The hero starts at scale 0.12 at the gate's centre and magnifies to
full frame with a stepped mechanical ease — the focusing knob clicking
through detent pauses at 0.35, 0.62 and 0.85 — over 1400ms. It belongs
because magnification is the reader's first act, and because it teaches
the visitor, before a single scroll, that this machine moves in steps.

**Structure.** The hero is a normal `.frame` (frame 001) inside the film
layer. A wrapper `.gate-zoom` carries the transform; the frame's content is
complete DOM from first paint, unscaled in the accessibility tree. The
dust/scratch settle layer (§6.6) sits above it in the light path. The zoom
is armed by JS adding `.is-focusing` to the housing; without JS the class
never lands and the frame simply sits at scale 1.

**Motion spec.** Trigger: load, after first paint + 100ms. Scale
0.12→1.0 over `--dur-zoom` (1400ms) in 24 steps (`--ease-magnify`) with
90ms holds at 0.35 / 0.62 / 0.85 — the holds are where the knob clicks.
Simultaneously the gate vignette contracts from 38% inset to its resting
6%. At lock, dust and scratches settle over `--dur-settle` (500ms): grain
opacity 0→0.5, the hero frame's two hairline scratches fade to their rest
opacity 0.35. The frame counter (§6.11) reads `FRAME 001` throughout —
the zoom is focus, not travel.

**Choreography timeline (v2).**
- t=0 — First paint. Frame visible tiny in the gate (JS-armed only).
- t=100 — `.is-focusing` added; zoom begins.
- t=100–520 — Steps 1–8: scale 0.12→0.35. Hold 90ms (knob click 1).
- t=610–940 — Steps 9–16: scale 0.35→0.62. Hold 90ms (click 2).
- t=1030–1330 — Steps 17–21: scale 0.62→0.85. Hold 90ms (click 3).
- t=1420–1500 — Steps 22–24: scale 0.85→1.0; 1px overshoot at t=1480,
  catch by t=1500 — the zoom ends in a detent, like everything here.
- t=1500–2000 — Settle: dust fades in, scratches resolve, title jitter
  (§6.10) runs its 1s concurrently from t=1500.
- t=2000 — `.is-focused`. The machine is ready; scroll is live.

**State matrix (v2).**

| State | Frame | Vignette | Notes |
|---|---|---|---|
| Pre-focus (JS armed, t<100) | Scale 0.12, centred in gate | 38% inset | Lasts ≤100ms; never a reading state. |
| Focusing | Stepping 0.12→1.0 with holds | Contracting | Scroll input is buffered, not honoured mid-zoom (see edge cases). |
| Focused (rest) | Scale 1.0, locked in detent | 6% rest | The normal hero. |
| Scrolled-past | Scale 1.0; film has advanced | 6% | The zoom never replays on scroll-back. |
| Hover/focus-within | Per §6.8 swell only | — | Zoom is a load ceremony, not an interaction. |
| Disabled / no-JS | Scale 1.0 from first paint | 6% | The class is never added; nothing is hidden. |

**Breakpoint behaviour (v2).** ≥1200px: full ceremony as specced.
768–1199px: 18 steps, holds 70ms, total 1150ms — a smaller reader focuses
faster. <768px: 12 steps, one hold at 0.62, total 900ms, vignette from 30%
— phone visitors get the meaning (a machine focusing) without the wait.

**Edge cases (v2).** Slow network: the zoom waits for the hero frame's own
content, not for below-fold assets; if fonts are late, the zoom runs on the
fallback serif and the swap happens at lock, never mid-step (a mid-zoom
font swap shifts the frame's centre and reads as a slipped sprocket).
Scroll during zoom: input is buffered and applied as a single detent after
lock — the visitor's intent is honoured, the ceremony is not interrupted.
Tab hidden mid-zoom: on return, the zoom completes instantly to scale 1
(rAF timestamps jump; the state machine checks elapsed > duration and
locks). Very short hero content: the frame still fills the gate — the zoom
magnifies the frame, not the text block, so short content zooms as a
sparsely-filled frame, which is correct: some filmed pages are half blank.

**Accessibility (v2).** The zoom is a transform on a wrapper: reading
order, focus order and screen-reader output are the unscaled DOM
throughout. Focus is never placed inside the hero until `.is-focused`, so
a keyboard visitor's first Tab lands after the ceremony (≤2s) — and the
skip-link (§6.13) bypasses the hero entirely regardless. The zoom is not
announced. Contrast is unaffected: phosphor on room at every scale.

**Content merge.** The zoom magnifies the actual first frame — the reel
title and the opening content the visitor is about to read. It is not a
logo sting before the site; it is the reader focusing the page itself.

**Failure fallback.** JS off, or the 1s gate promise (§5 law 2) tripped by
a stalled load: frame at scale 1, vignette at rest, dust layer absent.
The hero reads as a still first frame.

**Reduced motion.** No zoom. The frame sits at scale 1 from first paint;
dust and grain are present but static (§6.6's reduced variant); the title
does not jitter (§6.10). The session starts already focused.

**Performance & mobile variant.** One transform on one wrapper, composited;
zero layout cost after lock (transform removed, `will-change` dropped at
`.is-focused`). Budget ≤1ms script. Mobile variant is the breakpoint spec
above.

**Tokens.** `--dur-zoom`, `--dur-settle`, `--ease-magnify`, `--ease-detent`,
`--room`, `--gate`, `--amber`.

### 6.2 Ratcheted frame advance

**What & why.** The theme's engine. Scrolling does not glide the film; it
winds it. The film layer's rendered position is quantised to frame
boundaries, and crossing a boundary is a 120ms sprocket step with a 1px
overshoot-and-catch. It belongs because the detent is what a microfilm
reader *does* — and because the slight mechanical resistance makes visitors
read at the machine's pace instead of skimming at theirs.

**Structure.** The film layer (`.film`) holds all `.frame` elements in
normal document flow inside a tall scroll body. A single rAF loop (§5 law
5) reads `scrollY`, maps it to the nearest detent (frame boundary), and
renders the film's `translateY` at detent positions only, stepping between
them with `--ease-detent`. Sprocket rails are children of the film layer
and step with it; the housing bars are outside it and never move. Frame
boundaries are measured from the DOM (each frame's offset), never assumed
from a fixed height — variable frame heights detent correctly.

**Motion spec.** Trigger: scroll position crossing a frame boundary.
Step: 120ms (`--dur-detent`, `--ease-detent`), travelling the inter-frame
distance (frame-line gap, 26px + the incoming frame's exposure). Overshoot:
1px past the boundary at ~100ms, caught back over `--dur-catch` (60ms).
Within a frame's own travel, the film still renders at the frame's internal
detent sub-positions every 26px (one sprocket pitch) — long frames step
their internal scroll in pitch increments, so the ratchet is felt
continuously, not only at boundaries. The magnifier/dust layer follows at
`--lerp-lens` (0.09), lagging each step by ~2 frames of render — the depth
cue.

**Choreography timeline (v2).** (One boundary crossing, desktop.)
- t=0 — Loop detects scrollY past boundary +8px (the engagement tooth).
- t=0–120 — Film steps to the boundary: translateY animates the gap
  distance with `--ease-detent`; rails step in sync; the incoming frame's
  gate exposure (§5) runs concurrently, opening at t=30.
- t=100 — Film is 1px past the boundary (overshoot).
- t=120–180 — Catch: film settles back the 1px; a 1-frame grain surge
  (opacity +0.15) sells the mechanical contact.
- t=180 — Detent locked. Counter tick (§6.11) fires. The frame is now
  the current frame.

**State matrix (v2).**

| State | Film | Rails | Counter | Notes |
|---|---|---|---|---|
| Locked in detent (rest) | At boundary, still | Still | Current frame shown | Grain crawls; machine idles (§5 law 6). |
| Stepping | 120ms step + 60ms catch | Step with film | Ticks at lock | The only motion state. |
| Fast winding | §6.3 blur takes over above velocity threshold | Streak with film | Ticks per frame passed, batched | Detents resume as velocity drops. |
| Scrolled-back (upward) | Steps in reverse, same 120ms | Same | Ticks down | Reverse is identical mechanics — a reader rewinds one detent at a time. |
| Hover | No change | — | — | Scroll mechanics ignore the pointer. |
| Disabled (reduced motion / no-JS) | Native scroll, no quantisation | Static with page | Counter updates on IO, no step | §6.2's fallback is ordinary scrolling. |

**Breakpoint behaviour (v2).** ≥1200px: full detents as specced, rails at
both edges. 768–1199px: detent step 110ms, internal sub-detents every 26px
kept; rails narrow (§4). <768px: boundary detents only — internal
sub-detents are cut (phone scroll is thumb-driven and fast; a ratchet
inside the frame fights the thumb), step 100ms, overshoot still 1px. The
boundary step is never cut at any size: it is the theme.

**Edge cases (v2).** Keyboard / find-in-page jumps: the loop detects a
position change > 2 frame heights between frames of the loop and snaps —
no step animation, film placed at the target detent, gate pre-opened; the
machine does not wind theatrically to catch up with a Page-Down.
Scrollbar drags: same snap rule. Scrolling back up rapidly: §6.3's blur
engages symmetrically (rewind blur), resolving into the landed frame.
Frames taller than 2.5× viewport: internal sub-detents carry the travel;
the boundary logic is unchanged. A frame shorter than the gate (damaged
frames, 60vh): the detent still lands on its boundary; the next step is
proportionally sooner — correct, dividers are short. Low-power device:
if the loop's frame budget exceeds 24ms sustained, sub-detents are cut
first, then the grain surge; boundary steps are last to go and never go
entirely (§14 cut order).

**Accessibility (v2).** Detents are a visual rendering of scroll position;
the underlying scroll is the browser's own, so keyboard, switch and
screen-reader navigation move through real document flow in real order.
Focus moving to an element in another frame scrolls natively; the loop
snaps (edge case above) rather than animating focus away. The step is
never accompanied by sound or by aria-live announcements — the counter is
`aria-hidden` (§6.11) and the current frame is conveyed by the document's
own heading structure.

**Content merge.** The steps act on the content frames themselves — the
sprocket holes driving the film are printed on the same stock as the
articles. Remove the content and there is nothing to advance.

**Failure fallback.** JS off or loop failure: ordinary continuous
scrolling of a dark, well-typeset page with frame lines and numbers as
static furniture. Every frame fully readable. The theme degrades to a
printed reel transcript, not to a broken page.

**Reduced motion.** No quantisation, no steps, no catch: native scroll,
frames separated by their lines, counter updated by IntersectionObserver.
The visitor reads a still strip (§6.12's reduced variant is the same
philosophy at load).

**Performance & mobile variant.** One rAF loop, ≤2ms script per frame of
render; transform-only writes on the film layer; detent state kept as two
numbers (current detent, target detent). Mobile variant is the breakpoint
spec above.

**Tokens.** `--dur-detent`, `--dur-catch`, `--ease-detent`, `--lerp-film`,
`--lerp-lens`.

### 6.3 Velocity fast-forward blur

**What & why.** When the visitor winds fast — a long fling toward a later
chapter — the film does what film does: it blurs. Intermediate frames
streak vertically as motion-blurred clones, in proportion to scroll
velocity, and resolve into the landed frame as the winding slows. It
belongs because it makes distance *felt*: travelling twelve frames costs
a visible whip of twelve frames, and the visitor learns the reel's length
in their hands.

**Structure.** A `.ff-layer` above the film, below the dust layer, holding
up to 6 clone strips (recycled DOM nodes) of the frames being passed. The
rAF loop computes scroll velocity each tick; above the engage threshold
the film layer itself gets a `filter: blur()` scaled to velocity plus a
vertical streak gradient, and the clone strips populate with the passed
frames' edge-numbers and title lines (cheap stand-ins: clones carry the
frame's edge-printing and headline only, not full content — at 14px of
blur, that is all the eye can take anyway, and the spec says so honestly).

**Motion spec.** Engage: velocity > 2400px/s sustained over 2 loop ticks.
Film blur: `min(14px, velocity / 400)` vertical only (via a stretched
clone + `blur()` on the film layer's wrapper — the blur is directional in
effect because the streak overlay masks horizontal softness). Clone
streaks: passed frames' strips translate through the gate at the scroll
velocity, opacity 0.5, each visible for the duration of its own passing.
Resolve: as velocity falls below 900px/s, blur eases to 0 over 180ms
(`--ease-whip`), clones clear, and the landed frame detent-locks (§6.2)
with its gate exposure. The counter (§6.11) free-runs during the blur —
digits spinning through frame numbers — and locks on landing.

**Choreography timeline (v2).** (A fling from frame 3 to frame 9.)
- t=0 — Velocity crosses 2400px/s. Detent stepping suspends.
- t=0–80 — Blur ramps to velocity-scaled value; first clone strips enter.
- t=80–(fling duration) — Streak state: clones whip through, counter
  free-runs, rails streak (their holes smear into dashed lines via the
  same blur — the perforations elongate, a detail the eye reads instantly).
- Velocity < 900px/s — Resolve begins: blur 180ms to 0.
- Landing — Final detent step (120ms) + catch; gate exposure on the landed
  frame; counter locks on its true number.
- Total added ceremony beyond the scroll itself: ≤260ms.

**State matrix (v2).**

| State | Film | Clones | Counter | Notes |
|---|---|---|---|---|
| Below threshold (rest/slow) | Sharp, detented | Absent | Locked | §6.2 governs. |
| Engaged (fast wind) | Blurred ∝ velocity | Streaking | Free-running | No frame is readable — correctly; you cannot read film at speed. |
| Resolving | Blur → 0 over 180ms | Clearing | Decelerating spin | The landed frame sharpens into its detent. |
| Scrolled-past / landed | Sharp, locked | Absent | True number | — |
| Hover/focus during wind | Unchanged | — | — | Focus inside a passed frame forces an immediate resolve at that frame (see accessibility). |
| Disabled | Never engages | — | — | Reduced motion: velocity is ignored entirely. |

**Breakpoint behaviour (v2).** ≥1200px: as specced, 6 clone strips.
768–1199px: 4 clones, blur cap 10px. <768px: the blur engages (phone flings
are the fastest winds of all) but clones are cut to 2 and the blur cap is
8px — GPU-filter cost on phones is the budget that matters (§14); the
counter free-run is kept, because it is cheap and it is the tell.

**Edge cases (v2).** Short hops (2–3 frames at high velocity): the blur
engages and resolves within ~300ms; if the hop is under 2 frames the
threshold's 2-tick sustain requirement prevents engagement entirely — a
quick single-frame flick stays a clean detent. Scrolling to the very end:
the take-up reel (§6.4) is full as the last frame locks; the blur resolves
into the end-of-reel frame (§6.17) whose counter reads the true total.
Browser without `filter` support on transformed elements: clones and the
streak gradient still render (they are opacity/transform only); the film
stays sharp but streaked — a lesser whip, still honest. Velocity spikes
from scrollbar drags: treated as jumps (§6.2 snap), not winds — no blur,
because a drag is the visitor carrying the film, not the machine winding it.

**Accessibility (v2).** The blur is presentational: the DOM is never
blurred for assistive tech, and no content is removed during a wind.
Keyboard focus landing mid-wind forces an immediate resolve at the focused
frame (blur cut, detent snap) — focus must never sit inside a blurred
frame. `prefers-reduced-motion`: the element does not exist (§6.3 disabled
row is the whole story).

**Content merge.** The streaking clones are the reel's own intermediate
frames — their real edge-numbers and headlines whip past. A visitor who
winds from the 1911 frame to the 1953 frame *sees* 1914, 1920, 1931 pass.
The blur is the archive's table of contents at speed.

**Failure fallback.** If the loop or filters fail, fast scrolling is just
fast scrolling: detents snap per §6.2's jump rule. Nothing is hidden at
any velocity in the fallback.

**Reduced motion.** Fully disabled. Fast scroll = ordinary scroll; frames
are read as a still strip.

**Performance & mobile variant.** The blur filter is the theme's most
expensive effect: it is applied to one wrapper, only while engaged, and
released the tick velocity drops. Clone pool is fixed at build (6 nodes),
recycled — zero allocation during a wind. Budget: filter cost only,
≤4ms/frame while engaged on desktop; mobile caps above.

**Tokens.** `--ease-whip`, `--dur-whip`, `--lerp-film`, `--amber-wound`,
`--celluloid`.

### 6.4 Take-up reel progress

**What & why.** Progress in a reader is not a bar filling; it is film
accumulating on the take-up reel. A reel at the housing's top-right
visibly winds: its wound diameter grows, scrubbed to reading progress,
beside the mono counter (`FRAME 012 / 340`). It belongs because it makes
progress *physical and honest* — the reel holds exactly the film you have
read, and an unread reel is visibly empty. Beside §6.11's counter, it is
the theme's entire progress system.

**Structure.** An SVG/canvas disc in the top housing bar: a core (46px
diameter) with three reel spokes, and a wound-film annulus whose outer
diameter is computed from progress — diameter grows with the *square root*
of progress (film winds in area, not in radius: `d = 46 + 72 × √p`, 46px
empty → 118px at p=1, clipped by the housing at the largest sizes and
scaled to fit the 44px bar via a viewport transform — the reel is drawn
at instrument scale, roughly 0.38×, so its drawn diameter runs 18px→45px
in the bar). The annulus is `--amber-wound`; the unwound supply side is
implied by a matching shrinking disc at the top-left on wide screens
(≥1200px only). Rotation: the reel turns as film passes, scrubbed — one
full rotation per 3 frames wound.

**Motion spec.** Trigger: scroll (scrubbed, rendered in the shared loop).
Diameter and rotation are pure functions of detent position — no
independent animation, no easing of their own; they inherit the detent's
step (the reel visibly *ticks* larger at each lock, 120ms steps, which is
the point: winding is mechanical). Between detents the reel is still.

**Choreography timeline (v2).** (Per detent lock.)
- t=0 — Detent step begins (§6.2).
- t=0–120 — Reel rotates ⅓ turn stepped with the film; annulus diameter
  interpolates to the new detent's value.
- t=120–180 — Catch: a 0.5px diameter settle (the new wrap of film
  compressing) mirrors the film's 1px catch at instrument scale.
- Continuous — At p=1 the reel is full: annulus at max, spokes barely
  visible; the counter (§6.11) reads the total. The footer (§6.17) is the
  only thing left to read.

**State matrix (v2).**

| State | Reel | Supply reel (≥1200px) | Notes |
|---|---|---|---|
| Start (frame 1) | Core only, 46px wound diameter (drawn ~18px) | Full | The visit begins with an empty take-up — true, and felt. |
| Mid-reel | Annulus ∝ √progress | Shrinking ∝ √(1−p) | The two reels together always hold the whole film — conservation of film. |
| End (last frame) | Full, 118px (drawn ~45px) | Core only | End-of-reel frame (§6.17) confirms in mono: `END OF REEL`. |
| Scrolled-back | Unwinds symmetrically | Refills | Rewinding is real: progress honestly decreases. |
| Hover | No change | — | The reel is an instrument, not a control. (Its click target is §6.13's index, not the reel.) |
| Disabled / no-JS | Static half-wound illustration in the bar | Static | A decorative still; the counter (§6.11) carries progress in the fallback via IO. |

**Breakpoint behaviour (v2).** ≥1200px: both reels, full spec.
768–1199px: take-up reel only (supply reel cut — the bar is narrower and
one instrument is enough), drawn scale 0.34×. <768px: the reel shrinks to
a 22px disc in the top bar beside the counter; the √ growth is preserved
(it is the information), the spokes are cut (at 22px they are noise).

**Edge cases (v2).** Very short pages (a 3-frame reel): growth per frame
is large and visibly stepped — correct, and the counter agrees. Very long
reels (300+ frames): per-detent growth is sub-pixel for long stretches;
the rotation (⅓ turn per 3 frames) carries the sense of winding when the
diameter cannot. Tab refocus after a jump: reel snaps to the true
progress — instruments do not animate to catch up. Print: the reel is
hidden (`@media print`); paper has no progress.

**Accessibility (v2).** The reel is `aria-hidden` — it is a picture of the
counter's number. Progress is available to assistive tech as real text:
the counter (§6.11) is in the accessibility tree as visually-hidden text
updated per frame (`Frame 12 of 340`), and each frame's heading carries
its own number. The reel itself is never focusable and never a control.

**Content merge.** The film on the reel is the film the visitor has read —
its diameter is computed from the same detent state as the counter and
the film layer. It cannot disagree with the page, because it *is* the
page's position, wound up.

**Failure fallback.** A static half-wound reel glyph in the housing bar.
Progress remains available from the counter and the frame numbers.

**Reduced motion.** The reel still updates (it is information, not
ornament) but discretely: diameter and rotation set instantly at each
frame change via IO, no stepped interpolation.

**Performance & mobile variant.** One SVG with two attribute writes per
detent (diameter via `r`, rotation via transform) inside the shared loop.
Negligible cost at every breakpoint; mobile variant is the size spec above.

**Tokens.** `--amber-wound`, `--amber`, `--room`, `--dur-detent`.

### 6.5 Damaged divider frames

**What & why.** Every seventh frame is damaged: scratched, light-leaked at
one edge, its emulsion bubbled in a corner — and it works as the reel's
chapter divider. As it arrives, a scratch-line draws itself down the frame
in SVG over 700ms, and beneath the damage sits the librarian's note in
mono, describing *this* frame's injury and what it cost the record. It
belongs because real archives are wounded, and because the divider gives
the reel a chapter rhythm no styled `<hr>` could: you do not decorate a
transition here, you pass through the damage the collection actually
suffered.

**Structure.** A `.frame.frame--damaged`, 60vh, containing: an SVG scratch
layer (2–4 paths per frame, each frame's paths unique — drawn from that
frame's own note: the flood frame's scratches run horizontal with a tide
line; the torn frame's run diagonal to a perforated edge), a light-leak
gradient at one edge (§6.7's home ground), the note block (`NOTE — …` in
`--amber` mono), and the incoming chapter's title edge-printed at the
frame's foot in celluloid. The scratch paths ship with
`stroke-dasharray` set but *undrawn* only when JS arms them; the no-JS
render shows the scratches fully drawn (see fallback).

**Motion spec.** Trigger: the damaged frame's detent lock (§6.2). The
frame pins for its 60vh of travel (`position: sticky` inside its slot).
Scratch draw: each path `stroke-dashoffset` → 0 over `--dur-scratch`
(700ms), `--ease-lamp`, staggered 90ms per path, longest path first — the
eye follows the worst injury first. Simultaneously the leak blooms once
(§6.7, `--dur-bloom` 2500ms, to its rest leak opacity 0.5). The note
exposes through the gate (§5) as the first scratch completes. After the
draw, the frame is still: damage does not animate twice.

**Choreography timeline (v2).**
- t=0 — Detent locks on the damaged frame; pin engages.
- t=0–700 — Scratch 1 (longest) draws, top to bottom.
- t=90–790 — Scratch 2 draws; t=180–880 scratch 3 if present.
- t=350 — Leak bloom begins its single pass (2500ms, peaking t≈1400).
- t=700 — Note gate-exposes (240ms); chapter title at the foot is already
  legible — it was never hidden.
- t≈1600 — All drawing done. The remaining pin travel is stillness: the
  visitor sits with the damage for the rest of the 60vh.
- Scroll on — Pin releases at the slot's end; the next chapter's first
  frame detents in.

**State matrix (v2).**

| State | Scratches | Leak | Note | Notes |
|---|---|---|---|---|
| Approaching (below gate) | Undrawn (JS-armed) | Rest 0.5 | Present in DOM, gate-closed visually | Content is never removed — only the draw is pending. |
| Arriving (locked, drawing) | Drawing per timeline | Blooming once | Exposes at t=700 | The ceremony. |
| Rest (read) | Fully drawn | Rest 0.5, §6.7's irregular pulses | Fully visible | The divider's working state. |
| Scrolled-past | Fully drawn | Rest | Visible in transcript order | Scrolling back shows the damage as found — no redraw. |
| Hover | No change | — | — | Damage is not interactive. |
| Disabled / no-JS | Fully drawn from first paint | Static gradient at 0.5 | Fully visible | The fallback is the archive's own catalogue photograph of the damage. |

**Breakpoint behaviour (v2).** ≥1200px: full spec, pin engaged.
768–1199px: pin kept; scratch count per frame capped at 3. <768px: the pin
is **cut** — a pinned 60vh divider on a phone traps the thumb; the frame
becomes a normal short frame, scratches pre-drawn at 80% with the final
20% drawing on entry (300ms) so the gesture survives without the trap.
The note is never cut at any size: the note is the point.

**Edge cases (v2).** A reel whose frame count is not a multiple of 7: the
last partial chapter gets no damaged frame unless the catalogue says the
reel's tail is damaged — the rhythm yields to the record. Two damaged
frames must never be adjacent (a build error the gate in §10 checks: if
the content model produces adjacent damage, one is reclassified as a
normal frame with a note in its caption instead). Scrolling fast through
a damaged frame: §6.3's wind carries the visitor past; the draw is skipped
and the frame is left fully drawn — the ceremony is for arrivals, not
drive-bys. Very long notes: the note wraps inside the frame; if it exceeds
4 lines the frame grows (frame heights are measured, §6.2) rather than
truncating the librarian.

**Accessibility (v2).** The scratch SVG is `aria-hidden`; the damage is
conveyed by the note's text, which is real content in reading order —
a screen-reader visitor learns "frames 041–048 water-damaged, March 1953"
exactly where a sighted visitor sees the tide line. The pinned frame never
traps focus: it is a visual pin of a normal-flow element, and focus moves
through it in DOM order. Note contrast: amber on room, 7.6:1, at 13px —
AA-pass and the theme's most important small text is also its most legible
accent.

**Content merge.** The damage is *in* this reel's film and the note is the
archive's own cataloguing of it; the divider divides because the record
itself is broken there. Remove the archive's real history of damage and
the element has nothing to show — which is precisely the test.

**Failure fallback.** Scratches fully drawn, leak static, note visible —
the frame as a catalogue photograph. No JS is required for the divider to
divide: it is a short frame with a note, and that already works.

**Reduced motion.** Scratches pre-drawn, no pin at any breakpoint, leak
static at rest opacity, note visible. The divider remains a divider.

**Performance & mobile variant.** One SVG per damaged frame, paths drawn
with composited dash-offset animation; only the in-gate damaged frame's
SVG is live. Cost negligible. Mobile variant is the breakpoint spec above.

**Tokens.** `--dur-scratch`, `--dur-bloom`, `--ease-lamp`, `--amber`,
`--scratch`, `--celluloid`.

### 6.6 Projector dust and grain

**What & why.** The room is in the projection. Film grain crawls
continuously over the current frame, and dust motes drift slowly through
the projector's light cone — denser near the frame edges, where the light
falls off and the eye forgives them. It belongs because a microfilm reader
screen is never clean: the grain is the film's own texture and the dust is
the basement's air, and together they are what makes the phosphor glow
read as *projected* rather than merely *displayed*.

**Structure.** Two layers in the light path, both `pointer-events: none`,
both clipped to the gate: `.grain` — a tiled noise background (SVG
feTurbulence data-URI, 180×180px tile, monochrome) at opacity 0.5,
animated by stepping its background-position through 8 offsets in a 0.9s
`steps(1)` loop; `.dust` — a canvas (or, on low-power devices, 10 DOM
dots) holding 14–22 motes, each a 1–2px `--scratch`-white radial dot at
0.12–0.4 opacity, drifting on individual slow linear paths (6–14px over
9–14s, looping with wrap). Both layers sit above the film, below the
housing chrome, and both render only for the frame currently in the gate —
the layers are gate-sized, not page-sized.

**Motion spec.** Trigger: time (ambient), from the hero's settle (§6.1)
onward. Grain: continuous crawl, 8 steps / 0.9s, `--ease-drift`. Dust:
continuous drift; motes within 12% of a frame edge are 1.6× denser and
0.1 more opaque (edge falloff). The whole light path follows the film at
`--lerp-lens` (0.09) — lagging the film's detents by ~2 render frames, so
on each step the dust visibly *settles after* the film: the room reacts to
the machine. During §6.3's fast-forward, grain crawl rate scales with
velocity (up to 3×) and motes streak 4px vertically — dust in a fast light
path smears.

**Choreography timeline (v2).** (Steady state, per detent.)
- t=0 — Detent step begins (§6.2); film moves.
- t=0–120 — Dust layer follows at lerp 0.09, trailing the film by ~22ms
  of rendered position.
- t=120–180 — Film catches; dust continues settling for a further ~80ms —
  the lag made visible.
- Continuous — Grain steps every 112ms; each mote completes its drift
  loop in 9–14s and respawns at a cone edge (never centre-frame: the
  middle of the page stays clean for reading).
- On frame change — The incoming frame's edges attract the mote density
  field over ~1s (`--ease-lamp` on the density gradient).

**State matrix (v2).**

| State | Grain | Dust | Notes |
|---|---|---|---|
| Rest (locked frame) | Crawling 0.9s loop | Drifting, edge-dense | The idling machine (§5 law 6). |
| Stepping | Crawl continues; 1-frame surge at catch (§6.2) | Lagging, then settling | The surge is the contact tell. |
| Fast-forward | Up to 3× crawl | Streaked 4px | §6.3 owns the film; dust obeys the same wind. |
| Scrolled-past frames | Not rendered | Not rendered | Only the in-gate frame has a light path. Off-gate frames are clean in the transcript. |
| Hover | No change | No change | The room ignores the pointer. |
| Disabled / no-JS | Absent | Absent | The fallback page is a clean transcript (§6.2). Grain is an enhancement, never a carrier. |

**Breakpoint behaviour (v2).** ≥1200px: 22 motes, full grain.
768–1199px: 16 motes, grain tile 150px. <768px: 10 motes as DOM dots (no
canvas — one less surface to composite on a phone GPU), grain opacity
0.35, crawl 1.2s. The *effect* survives at every size; only its budget
shrinks.

**Edge cases (v2).** Low-power / battery-saver (loop frame budget >24ms
sustained, §14): dust is cut first (it is the most expendable beauty),
grain drops to a static tile at opacity 0.3 — the frame still reads as
film, the room stops breathing. `prefers-reduced-transparency`-style
environments: grain opacity halves. Long sessions: mote count and grain
are constant-cost; nothing accumulates. If the canvas context is lost,
the dust layer removes itself silently and grain carries the room alone.

**Accessibility (v2).** Both layers are `aria-hidden`, `pointer-events:
none`, and — critically — contrast-neutral: grain at 0.5 monochrome over
phosphor text measured at worst-case 13.9:1 effective (from 15.2:1) —
still AAA; the grain tile's luminance variance is capped at build time so
no tile position can drop a glyph below 12:1. Motes never exceed 0.4
opacity and never cross the central reading measure at full opacity.
Motion sensitivity: see reduced-motion variant — this element is the
first thing the reduced theme stills.

**Content merge.** The grain is the film's grain — it lives only over
frames, textured like the stock the content is printed on; the dust is in
the light that reveals the content. Neither exists over the housing, the
footer's printed slip, or anywhere the fiction says there is no projection.

**Failure fallback.** No layers. The frames read clean — a freshly
digitised transcript. Nothing about the content depends on the room.

**Reduced motion.** Grain rendered as a *static* tile at 0.3 opacity (the
film's texture without the crawl); dust absent. The frame still reads as
film, the room holds its breath — which is what reduced motion means here.

**Performance & mobile variant.** Grain: one background-position step per
112ms — near-zero cost. Dust canvas: ≤22 particles, one 2D context,
gate-sized (≤ ~900×650px), updated in the shared loop; hard budget 1.5ms.
Mobile variant is the breakpoint spec above.

**Tokens.** `--lerp-lens`, `--ease-drift`, `--ease-lamp`, `--scratch`,
`--amber`.

### 6.7 Light-leak blooms

**What & why.** Old film leaks light where its canister seal failed, and
the leak lives in specific frames forever. On damaged frames (§6.5) and on
the reel's first and last frames, a soft amber bloom occasionally swells
in from one edge — a 2.5s opacity pulse at irregular intervals of roughly
17 seconds — then subsides to the leak's rest stain. It belongs because it
is the archive's damage made temporal: the flaw you can set a watch by,
almost, but not quite — the irregularity is what makes it feel like a
physical thing rather than a looping animation.

**Structure.** A radial-gradient layer inside the affected frame, anchored
at the leaking edge (each leaking frame declares its edge in the content
model: `data-leak="left|right|top"`), gradient from `--amber` at 0.55
through 0.18 to transparent across 45% of the frame's width. The layer is
part of the frame (it scrolls and detents with the film), clipped by the
gate, `aria-hidden`, `pointer-events: none`. The scheduler lives in the
shared rAF loop: a per-frame next-bloom timestamp drawn from a randomised
14–23s interval, active only while that frame is in the gate.

**Motion spec.** Trigger: time, irregular (14–23s randomised, seeded per
frame so two leaking frames never bloom in sync). Pulse: opacity of the
bloom layer 0.5 (rest stain) → 0.85 peak → 0.5 over `--dur-bloom` (2500ms),
`--ease-lamp`, with the gradient's radius swelling 45%→52% at the peak —
light spreading as it strengthens. Only one bloom per frame per interval;
a frame leaving the gate mid-bloom completes its pulse in the transcript
(it belongs to the frame, not the viewport).

**Choreography timeline (v2).** (One pulse.)
- t=0 — Scheduler fires for the in-gate leaking frame.
- t=0–900 — Bloom swells: opacity 0.5→0.85, radius 45%→52%.
- t=900–1400 — Peak hold, ±0.03 opacity breathing (the lamp's mains hum,
  in light).
- t=1400–2500 — Subsides to rest stain.
- t=2500 — Next interval drawn (14–23s). The frame returns to §6.5's rest
  state until then.

**State matrix (v2).**

| State | Bloom layer | Notes |
|---|---|---|
| Rest (between pulses) | Static stain at 0.5 | The leak is always *there*; the pulse is it breathing. |
| Pulsing | Per timeline | Only while the frame is in the gate (except a pulse already running, which completes). |
| Frame off-gate | Static stain | No scheduler runs for unread frames. |
| Hover | No change | Light does not care about pointers. |
| Scrolled-past | Static stain in the transcript | — |
| Disabled / reduced motion | Static stain at 0.5, forever | The leak as a catalogue photograph. |

**Breakpoint behaviour (v2).** Identical at all sizes except <768px, where
the peak opacity is 0.75 (a small screen is closer to the eye; the same
bloom reads stronger) and the radius swell is cut — opacity alone breathes.

**Edge cases (v2).** A frame whose leak edge carries text: the content
model forbids it — leaks anchor to the edge *opposite* the frame's text
block, and §10's gate checks the pairing, because a bloom under a paragraph
drops its contrast mid-pulse (measured worst case at peak under text:
9.8:1 — still AA, but the theme does not spend contrast it doesn't have
to). Multiple leaking frames in one gate view: impossible by layout (one
frame fills the gate), except damaged-frame + edge-frame adjacency at a
detent boundary — the scheduler serialises them, never simultaneous.
Battery-saver: pulses suspended, stain remains.

**Accessibility (v2).** Purely decorative and `aria-hidden`; the damage it
visualises is described in words by §6.5's librarian's note. Contrast:
the bloom never sits under body text (edge-case rule above); under
headlines at peak, phosphor-on-bloom measures ≥8.5:1. The pulse is slow
(2.5s) and low-amplitude — no flash risk; it never exceeds one pulse per
14s per frame, far outside photosensitivity ranges.

**Content merge.** The leak is a property of *this frame of this reel*,
declared in its catalogue entry and anchored to its edge. It is not a
page-wide ambience effect: frames that were never leaked on do not bloom,
and the housing never blooms.

**Failure fallback.** The static stain — a gradient at rest opacity,
present in the CSS with no JS. The frame still reads as light-damaged.

**Reduced motion.** Static stain only; the scheduler never runs.

**Performance & mobile variant.** One gradient layer's opacity animated
inside the shared loop; zero cost between pulses. Mobile variant is the
breakpoint spec above.

**Tokens.** `--dur-bloom`, `--ease-lamp`, `--amber`, `--amber-wound`.

### 6.8 Magnifier swell hover

**What & why.** Hovering a frame leans the reader's lens in: the frame's
content swells to scale 1.03 *inside its gate* — the gate does not grow,
the magnification does — and the frame tilts a hair, 0.4°, the way a
curling film frame lifts at one corner. It belongs because it is the one
interaction a reader offers a browsing hand: *look closer at this one*.
It is also the theme's only hover gesture, which is why it can afford to
be this considered.

**Structure.** The frame's inner content wrapper (`.frame__lens`) carries
the transform; the gate (`.frame`) clips it (`overflow: hidden`), so the
swell magnifies within the frame's own borders. The tilt is on the same
wrapper (`rotate(0.4deg)`, alternating sign by frame parity — odd frames
lift left, even frames lift right, the way film curls consistently per
winding direction). Transform origin is the pointer's entry quadrant,
so the swell leans *toward* the reader's hand.

**Motion spec.** Trigger: hover (pointer fine) or focus-within. Swell:
scale 1→1.03 over 250ms, `--ease-detent` (the machine's easing — even the
lens moves like a mechanism, with the faintest catch at the end). Tilt:
0→0.4° across the same 250ms. Release: 200ms back, same easing, no
overshoot on exit (the lens withdraws cleanly). The dust layer (§6.6)
does not swell — it is in the light path, in front of the lens, and its
staying put while the film swells is exactly the parallax that sells the
depth.

**Choreography timeline (v2).**
- t=0 — Pointer enters the frame (or focus lands within it).
- t=0–250 — Lens wrapper scales to 1.03 and tilts to 0.4°, origin at the
  entry quadrant; the frame's edge-printing (frame number) does *not*
  scale — it is on the film's edge, outside the lens's field, and its
  stillness frames the swell.
- t=250 — Rest at swell. Grain continues; nothing else changes.
- Pointer leaves — t=0–200 return to 1.0 / 0°.
- Rapid re-entry mid-release — the swell resumes from its current scale
  (no jump): the transform is stateful, driven by a target value in the
  shared loop.

**State matrix (v2).**

| State | Lens scale | Tilt | Notes |
|---|---|---|---|
| Rest | 1.0 | 0° | — |
| Hover (fine pointer) | 1.03 | 0.4° (sign by parity) | The full gesture. |
| Focus-within (keyboard) | 1.03 | 0° | Focus gets the magnification without the curl — the tilt is a pointer pleasure, not a focus signal. Focus outline (§6.13) also draws. |
| Active (press) | 1.03 held | 0.4° held | The click itself is §6.9's clunk; the swell does not dip — pressing a reader's frame doesn't push the film. |
| Scrolled-past | 1.0 | 0° | Hover states are cleared when a frame leaves the gate. |
| Touch | No hover swell | — | Touch uses §6.9's tap-clunk instead. A tap must never first swell-then-clunk (that reads as a double action). |
| Disabled | 1.0 always | — | Reduced motion: no swell, no tilt. |

**Breakpoint behaviour (v2).** ≥1200px: full spec. 768–1199px: scale
1.025, tilt 0.3°. <768px: hover does not exist on the primary input; the
element is inert (focus-within via external keyboard still gets 1.02, no
tilt).

**Edge cases (v2).** Text frames: the swell magnifies text — at 1.03 a
19px body becomes ~19.6px, no reflow (transform, not layout), no clipping
of the measure because the gate clips symmetrically and the frame's
padding (52px) exceeds the swell's reach (~9px at frame width). Image
frames: the image scales within its own inner gate too (§5 image
treatment) — the two magnifications compose to 1.06 at most, checked at
the gate so portraits don't crop faces at the combined swell. Pointer
crossing many frames quickly (a sweep down the reel): swell targets
update per frame; the loop's lerp prevents any frame from snapping.

**Accessibility (v2).** The swell is decorative magnification of content
that is fully legible at 1.0 — nothing is revealed by hovering that isn't
already readable (a hard rule: hover never unlocks content in this theme).
Focus-within parity ensures keyboard visitors get the same lean-in.
Contrast unchanged (transform only). Touch targets are the frames
themselves — far above 44px.

**Content merge.** The swell magnifies the frame's own content in its own
gate, pivoting toward the visitor's hand. It is the reader's lens doing
its one job on the actual page being read.

**Failure fallback.** No transform. Frames sit at 1.0 — the still reader.

**Reduced motion.** No swell, no tilt, at any input. Focus is shown by
§6.13's outline alone.

**Performance & mobile variant.** One transform on one wrapper per hovered
frame, driven by the shared loop; `will-change` applied on hover-start,
removed on release. Mobile: inert per breakpoint spec.

**Tokens.** `--ease-detent`, `--lerp-film`.

### 6.9 Clunk-advance click

**What & why.** Clicking a frame works the reader's advance lever: a
mechanical clunk — the film steps exactly one detent to centre that frame,
with the step-and-catch of §6.2, and the frame's edge gives a 1-frame
brightness knock as the sprocket engages. It belongs because a reader is
operated, not browsed: the click is the visitor's hand on the machine, and
it should feel like the machine answered.

**Structure.** Frames are click targets (the whole gate) with
`cursor: pointer` — the *normal system pointer*, per standing rules; the
theme adds no custom cursor. The clunk is rendered by the shared loop: on
click, the loop sets the target detent to the clicked frame's centre and
runs the standard step (120ms) + catch (60ms), plus a `brightness(1.12)`
knock on the frame's edge-printing for exactly 1 rendered frame (~16ms) at
the moment of engagement. A visually-hidden button inside each frame
("Advance to frame 012") gives the action a keyboard/AT name — the gate
itself is a `div` with a click handler, never the only path.

**Motion spec.** Trigger: click/tap on a frame not currently centred, or
Enter/Space on its advance button. If the clicked frame is the *next*
frame: one detent step (120ms + 60ms catch). If it is further: the film
winds at §6.3's mechanics but *without* blur for ≤3 frames (a lever throw
is deliberate, not a fling), and with blur beyond 3. If the clicked frame
is already centred: no travel — just the engagement knock and the counter
re-tick (§6.11), the machine acknowledging the hand. Scroll position is
driven by the loop to match (the detent is the truth; the scrollbar
follows).

**Choreography timeline (v2).** (Click on the next frame.)
- t=0 — Click lands. Edge-printing knock: brightness 1.12 for 1 frame.
- t=16 — Step begins (§6.2's step, identical numbers).
- t=136 — Overshoot point; t=136–196 catch.
- t=196 — Detent locked; counter ticks; clicked frame is current.
- Total: under 200ms — a clunk is fast, or it is a whirr.

**State matrix (v2).**

| State | Frame | Notes |
|---|---|---|
| Rest (current frame) | Click → knock + re-tick only | No travel. |
| Rest (other frame) | Click → wind to centre | Per motion spec distances. |
| Hover | §6.8's swell | The swell is the invitation; the clunk is the act. |
| Focus (advance button) | §6.13 outline on the button; Enter/Space = click | Keyboard parity is exact: same timeline. |
| Active (during wind) | Further clicks queue one deep | A second click mid-wind retargets; a third is ignored until lock (the lever can't be thrown twice at once). |
| Scrolled-past | Clickable when it re-enters the gate area | Frames outside the gate are not targets (they're wound film). |
| Disabled | Click = native anchor behaviour | No-JS: frames carry real fragment links (`#frame-012`) and the browser jumps. The clunk is an enhancement of a link, never a replacement for one. |

**Breakpoint behaviour (v2).** Identical mechanics at all sizes; <768px
the tap target is the full frame (≥ 200px tall — no precision needed) and
the knock is cut (small screens, small tells).

**Edge cases (v2).** Clicking a damaged frame: it centres and its §6.5
ceremony runs — the lever delivers you to the damage and the damage
performs. Clicking during §6.3's fling: the fling is cancelled into the
click's target (visitor intent outranks momentum). Double-click: treated
as one throw (the queue rule above). Click with a text selection active:
if the visitor has selected filmed text, the click is a deselection, not
an advance — the handler checks `getSelection()` and stands down; readers
must never be punished for selecting a name to copy.

**Accessibility (v2).** Every frame's advance is a real button with a real
name in the accessibility tree; the gate click is a pointer convenience
layered over it. Focus order follows the reel. The action's result —
"now on frame 012" — is the document's own heading coming into view; no
aria-live chatter (a clunk per frame would be unbearable announced).
Targets: whole frames. Contrast: the knock is a 16ms brightness tick on
edge-printing only, never on content.

**Content merge.** The click advances the actual film to the actual frame
clicked. The mechanism and the content are the same object.

**Failure fallback.** Fragment links + native jump. The reel is a
document with anchors; the machine is an enhancement.

**Reduced motion.** Click = instant jump (native anchor), no step, no
knock. The button still works; the machine is still.

**Performance & mobile variant.** Reuses §6.2/§6.3 machinery entirely;
the only new cost is one brightness filter for one frame. Mobile variant
is the breakpoint spec above.

**Tokens.** `--dur-detent`, `--dur-catch`, `--ease-detent`, `--celluloid`.

### 6.10 Projector-jitter title lock

**What & why.** When the reel loads, its title — the filmed masthead on
frame 001 — judders with projector jitter for one second: ±1px at roughly
8Hz, irregular, the way a freshly-threaded projector hunts for its gate —
then locks dead steady and never moves again. It belongs because it is
the machine's handshake: a brief, honest imperfection that proves the
projection is live, and whose *ending* is the signal that the reader is
ready. A title that jittered forever would be a defect; a title that
locks is a promise.

**Structure.** The hero frame's title element carries a `.jitter` class
from the zoom's lock (§6.1, t=1500) for 1000ms. The jitter is a transform
driven by the shared loop from a pre-generated irregular offset table (16
values, ±1px in x, ±0.6px in y, no two adjacent equal — generated at build
from a fixed seed so every visit jitters identically; a *random* jitter
would differ per visitor and the archive does not improvise). Only the
title jitters — never the frame, never the housing: the slip is in the
projected image, not the machine's body.

**Motion spec.** Trigger: §6.1's zoom lock. Duration 1000ms. Offsets step
at ~8Hz (every 125ms a new offset from the table, with two 60ms
double-steps mid-second for the hunting feel). Amplitude decays: first
500ms at full ±1px, second 500ms at ±0.5px — the hunt converging. At
t=1000 the transform is removed entirely (not set to 0 — removed, so no
composited layer lingers) and `.is-locked` is set. Once only: returning to
the hero by scroll never re-jitters; the projector is threaded now.

**Choreography timeline (v2).**
- t=0 (= §6.1 t=1500) — Zoom locks; jitter begins at full amplitude.
- t=0–500 — Offsets at ±1px, ~8Hz, irregular table order.
- t=500 — Amplitude halves (±0.5px); two quick double-steps at t=560, 620.
- t=880 — Last offset (±0.5px, y only).
- t=1000 — Transform removed; `.is-locked`; the title is still for the
  rest of the visit.

**State matrix (v2).**

| State | Title | Notes |
|---|---|---|
| Pre-lock (during zoom) | Steady, scaling with the frame | The jitter waits for focus — out-of-focus jitter would be mud. |
| Jittering (1s) | Per timeline | The only jittering object on the page. |
| Locked (rest of visit) | Dead steady | Scrolling away and back changes nothing. |
| Hover | No effect | The title is not a control. |
| Scrolled-past | Locked | — |
| Disabled / reduced motion | Never jitters | Locked from first paint (§6.1's reduced variant starts here). |

**Breakpoint behaviour (v2).** Identical at ≥768px. <768px: amplitude
±0.7px, duration 800ms — a phone's smaller gate hunts less, and its
visitor waits less.

**Edge cases (v2).** If §6.1's zoom is skipped (deep link to `#frame-012`,
returning visitor with the session flag): the title is simply locked —
the jitter belongs to the entrance ceremony and is not replayed for a
mid-reel arrival. If the tab is backgrounded during the jitter second,
rAF pauses and the jitter resumes on return for its remaining time (it is
elapsed-time driven, not frame-count driven, so it cannot overrun).
Font swap during jitter: the title's box is fixed by the frame's layout;
a swap may change glyph shapes but not the jitter's offsets.

**Accessibility (v2).** A 1s, ±1px transform on a headline: no content is
obscured (the offsets are sub-letterform), reading order untouched, not
announced. It is the theme's most motion-sensitive moment and its most
bounded: 1 second, 1 pixel, once. Reduced motion removes it entirely.
Vestibular note: sub-pixel-scale translation at 8Hz for 1s is far below
any threshold of concern, and the spec still cuts it for reduced-motion
visitors without argument.

**Content merge.** The jitter is in the projected title itself — the
masthead of the actual reel being read, settling into the gate. It is not
a loading spinner wearing a costume; when it locks, the content is what
remains.

**Failure fallback.** No class, no jitter: a steady title. The fallback
is indistinguishable from the locked state, which is the point.

**Reduced motion.** Never jitters (see matrix).

**Performance & mobile variant.** Sixteen transform writes over 1s inside
the shared loop; the layer is dropped at lock. Mobile variant is the
breakpoint spec above.

**Tokens.** `--dur-settle`, `--phosphor`.

### 6.11 Frame-counter data ticks

**What & why.** The machine counts what passes through it. The frame
counter in the housing (`FRAME 012 / 340`) ticks exactly one detent per
frame, at the moment that frame locks; and when a frame carrying archive
statistics arrives — reels held, frames preserved, years covered — those
figures count up in mono, one digit drum at a time, and stop at the true
numbers. It belongs because counting is the archive's love language: every
figure on the counter is a thing that exists, in a frame, in the DOM (§5
law 4).

**Structure.** The counter is a mono readout in the top housing bar:
current-frame drum (3 digits, zero-padded), separator, total drum. The
total is computed at build/runtime from the actual `.frame` count of the
reel — a page with 23 frames reads `/ 023`. Statistics live inside their
frames as `.stat` elements with `data-count-to` carrying the true figure
from the content (the catalogue's numbers, written by the archivist, not
the theme). Counting renders each digit as a translating drum strip
(0–9 stacked, mono tabular) — the counter is a set of wheels, and the
wheels turn.

**Motion spec.** Frame counter: on each detent lock (§6.2 t=180), the
current-frame drum steps to the new number — units drum rotates one step
(120ms, `--ease-detent`), tens/hundreds step only when they change, each
with the same catch. During §6.3's wind the drums free-run (continuous
rotation ∝ velocity) and lock on landing. Statistics: when a stat frame
locks, each figure counts from 0 (or from the figure's documented start —
a "years covered" figure counts from its earliest year, 1911, because the
archive's clock starts at its first frame) to its true value over 1200ms,
drums stepping in mono, staggered 120ms per figure; once counted, a stat
never recounts on revisit — the catalogue does not re-perform itself.

**Choreography timeline (v2).** (Stat frame locking.)
- t=0 — Detent locks; counter drum steps to the frame's number.
- t=180 — Catch settles; stat count begins.
- t=180–1380 — Figures count: reels (0→38) fastest, frames (0→526,700)
  longest, each drum stepping; figures finish in reading order, left to
  right, last at t=1380.
- t=1380 — All figures at true values, still. They remain at value for
  every later visit to the frame.

**State matrix (v2).**

| State | Counter drum | Stat figures | Notes |
|---|---|---|---|
| Rest | Current frame, still | True values (if counted) or pre-count (if not yet visited) | Pre-count figures render as `—` drums, not zeros: an uncounted stat is unknown, not zero. |
| Detent lock | Steps + catch | — | The tick is the lock's sound, made visible. |
| Fast-forward | Free-running | — | §6.3. |
| Stat frame arriving | Steps | Counting per timeline | Once per figure per visit-session. |
| Scrolled-past | Shows current frame (the one in the gate) | Counted figures stay at value | The counter always describes the gate, not the scroll position's history. |
| Hover/focus | No change | No change | Instruments, not controls. |
| Disabled / no-JS | Static text `FRAME — / 023`, updated by IO where JS allows | Figures at true values in the HTML | The numbers ship in the content; counting is presentation. |

**Breakpoint behaviour (v2).** ≥1200px: full drums. 768–1199px: drums kept
(they are 13px mono — cheap). <768px: the counter compresses to `012/023`
in the top bar (separator tightened, the word FRAME moves to the bottom
status bar) — the numbers survive, the label relocates.

**Edge cases (v2).** A reel with >999 frames: the drum gains a fourth
digit (the format is computed, not fixed at 3 — §3's law is zero-padding
to the total's width). Stats with decimals or ranges ("1911–1968"): ranges
do not count — both years render statically, because a range is a fact,
not a quantity; the counting rule applies to quantities only, and §10's
gate checks that no `data-count-to` sits on a range. A stat figure edited
in the CMS: the count target is the content's value, so the animation can
never disagree with the catalogue — the theme counts what it is told, and
what it is told is the archivist's number. Scroll-back: the counter ticks
down with the same mechanics; it is a position readout, not a high-water
mark.

**Accessibility (v2).** The visible counter is `aria-hidden` (its drums
are a picture of a number); a visually-hidden text twin — "Frame 12 of
340" — updates once per lock, *not* via aria-live (position is available
on demand, never announced over the reading). Stat figures: the true
value is the element's text content from the start for AT (the count is a
visual overlay of drum strips); screen readers meet the real numbers
immediately. Tabular mono keeps every drum's width constant — no layout
shift at any count state (CLS 0 from this element, always).

**Content merge.** The counter counts this reel's frames and the stats
are this archive's holdings, set in the frames where the catalogue states
them. The numbers are the content; the drums are just how the machine
says them.

**Failure fallback.** Static true values everywhere (they are in the
HTML). A visitor without JS reads the same numbers, uncounted.

**Reduced motion.** No counting, no drum rotation: counter text updates
per frame via IO; stats at true values from first paint.

**Performance & mobile variant.** Drum transforms inside the shared loop;
a stat count is ≤4 figures × 1200ms per frame-visit. Negligible. Mobile
variant is the breakpoint spec above.

**Tokens.** `--dur-detent`, `--ease-detent`, `--amber`, `--amber-wound`.

### 6.12 Blank-frame skeleton + fast-forward transition

**What & why.** The theme's two state-changes, both kept inside the
fiction. Loading: blank amber skeleton frames — unexposed film with
sprocket holes — that expose in as content arrives. Navigation: a
fast-forward whip, 400ms of blurred frames streaking to the next section,
then a detent lock. It belongs because a reader has no blank white void
and no spinner: it has unexposed film, and it has a wind knob. Every state
the software enters, the machine already had a word for.

**Structure.** Skeleton: `.frame.frame--blank` placeholders in the film
layer at the true frames' positions (same measured heights, so the reel's
detents are correct before content lands), ground `--amber` at 8% over
`--room`, sprocket holes along both edges, one mono line edge-printed:
`UNEXPOSED — AWAITING FILM`. Exposure: as each frame's content resolves,
the blank cross-fades to the real frame over 300ms (`--ease-lamp`) with a
single gate exposure (§5). Transition: route/section navigation reuses
§6.3's blur machinery at fixed ceremony length — a `.ff-layer` whip of the
intermediate frames between here and the target, 400ms, then the target
frame detent-locks and gate-exposes.

**Motion spec.** Skeleton exposure trigger: content ready per frame
(each frame exposes independently; the reel never waits for its slowest
frame). Whip trigger: navigation via §6.13's index or in-page section
links. Whip: blur ramps to 10px over 120ms, holds 160ms while the loop
drives scroll to the target, resolves over 120ms (`--ease-whip`), detent
lock + catch (the standard 120+60 runs inside the final 180ms — the
400ms budget contains the lock).

**Choreography timeline (v2).** (Whip.)
- t=0 — Navigation fires. Current frame's title streaks first (it is the
  last readable thing).
- t=0–120 — Blur to 10px; clone strips of intermediate frames enter.
- t=120–280 — Travel: scroll driven to target; counter free-runs.
- t=280–400 — Resolve: blur out, target frame's gate exposes, detent
  catches at t≈340–400.
- t=400 — Locked on target. Focus moves to the target frame's heading
  (see accessibility).

**State matrix (v2).**

| State | Skeleton | Whip | Notes |
|---|---|---|---|
| Loading (per frame) | Blank amber frame at true size | — | Detents already correct against blanks. |
| Exposing | Cross-fading 300ms | — | One frame at a time, in arrival order. |
| Loaded | Absent (real frames) | — | Blanks never return within a session. |
| Navigating | — | Per timeline | 400ms, then lock. |
| Hover/focus | No effect | Focus triggers per §6.13 | — |
| Disabled / no-JS | No blanks: content server-renders in place | Native anchor jump | The states are enhancements of a complete document. |

**Breakpoint behaviour (v2).** ≥1200px: full spec. 768–1199px: whip blur
cap 8px. <768px: whip shortened to 300ms (blur 6px, travel compressed) —
a phone navigation must feel instant first and mechanical second; skeleton
blanks keep full height (layout stability matters more on small screens,
not less).

**Edge cases (v2).** A frame whose content fails (network error): its
blank does not spin forever — after 4s it exposes to an error frame in the
fiction: a mono note in the frame, `FRAME DAMAGED IN TRANSIT — NOTE —
This frame did not arrive. [Retry]`, styled as a damaged frame (§6.5)
without the ceremony. Retry re-exposes. Navigation to a frame still
blank: the whip lands, the blank sits, exposure completes the arrival —
the visitor watches their frame develop, which is honest and rather
beautiful. Browser back/forward: no whip (history navigation is the
visitor's own hand on a different machine); the reel snaps to the
restored position per §6.2's jump rule.

**Accessibility (v2).** Skeletons are `aria-hidden` with the region's
`aria-busy` set until exposure; AT users meet content when it exists, not
a description of unexposed film. The whip moves focus to the target
heading on completion (focus is never left on a frame that has wound
away). Skeleton blanks cause zero CLS — heights are reserved by the
content model before load.

**Content merge.** The blank is the film before exposure; the whip is the
film running fast. Both states are the reel's own material in its own
states — the theme never steps outside the machine to say "loading…".

**Failure fallback.** No JS: no blanks, no whip — the document is simply
there, and links are anchors. The fallback is the theme with the machine's
motor removed and its film intact.

**Reduced motion.** Blanks expose instantly (no cross-fade); navigation is
an instant jump with focus moved. `aria-busy` behaviour unchanged.

**Performance & mobile variant.** Blanks are pure CSS. The whip reuses
§6.3's clone pool and filter — no new machinery. Mobile variant is the
breakpoint spec above.

**Tokens.** `--dur-whip`, `--ease-whip`, `--ease-lamp`, `--amber`,
`--amber-wound`, `--celluloid`.

### 6.13 Housing navigation — the reel index

**What & why.** A reader's navigation is its reel box: the label that says
what film this is and where its sections sit. The housing's top bar
carries the reel label; opening the **reel index** slides a drawer from
the housing's left side listing every chapter as a frame range
(`FRAMES 001–006 · THE FOUNDRY YEARS`), damaged dividers marked with
their note's first words. It belongs because visitors navigate a reel by
its catalogue, not by a menu of marketing nouns — and because the index
is the one place the theme lets you see the whole film at once, laid out
like a contact sheet.

**Structure.** Top bar: reel label (mono, §3) left; counter (§6.11) and
take-up reel (§6.4) right; an `INDEX` housing button. The index drawer is
a panel in the housing layer (not the film layer — it is machine, not
film), 320px wide, `--room` with a celluloid left rule, listing chapters
as mono rows: frame range, chapter title in Newsreader 17px, damaged
markers in amber. Each row is a real link to its first frame's fragment.
A skip-link ("Skip to frame content") is the first focusable element of
the page, styled as a housing label when focused.

**Motion spec.** Drawer: slides from the left edge over 260ms
(`--ease-detent` — the housing's parts move like the machine's parts,
with the catch), the film layer dims to 40% behind it (the lamp drops
while you consult the box). Row hover: the row's frame range brightens
from `--amber-wound` to `--amber` (120ms) and a 2px amber rule draws at
its left (160ms). Selecting a row: drawer closes (200ms), §6.12's whip
runs to the chapter. Current chapter's row carries a celluloid `▸ IN
GATE` marker, updated per detent.

**Choreography timeline (v2).**
- t=0 — INDEX activated (click/Enter).
- t=0–260 — Drawer steps in (detent easing, catch at t≈240); film dims
  concurrently (`--ease-lamp`, 260ms).
- t=260 — Focus moves to the current chapter's row.
- Selection — t=0–200 drawer closes; t=200 whip begins (§6.12 timeline
  from there); focus lands on the target frame's heading at whip end.
- Esc / outside click — drawer closes 200ms, focus returns to the INDEX
  button, no travel.

**State matrix (v2).**

| State | Drawer | Film | Notes |
|---|---|---|---|
| Closed (rest) | Off-canvas left | Full lamp | The visit's default. |
| Open | In, rows listed | Dimmed 40% | Focus trapped in the drawer while open. |
| Row hover/focus | Range brightens, rule draws | — | Focus and hover are the same state visually — parity by design. |
| Current chapter row | `IN GATE` marker in celluloid | — | Updated per detent lock, silently. |
| Disabled / no-JS | Rendered as a static index section at the page top | — | The links work; the drawer is an enhancement of a list. |

**Breakpoint behaviour (v2).** ≥1200px: 320px drawer. 768–1199px: 280px.
<768px: the drawer is full-width (the phone's reader has a small box);
rows are 52px tall (touch), the reel label in the top bar truncates to
the reel code (`REEL 07`) with the full label as the drawer's first row.

**Edge cases (v2).** A reel with one chapter: the index button is not
rendered — a one-chapter reel needs no index, and the housing stays
honest. Very many chapters (>40): the drawer scrolls (its own thin
scrollbar styled as a film edge) with chapter decades grouped under mono
subheads. Deep-link arrival (`#frame-012`): drawer closed, current-row
marker already correct. Print: the index prints as the transcript's table
of contents (§6.17's print rule).

**Accessibility (v2).** The drawer is a `nav` landmark with
`aria-label="Reel index"`; opening moves focus in, Esc returns it, focus
is trapped while open. Rows are links with descriptive text (`Frames
1–6, The Foundry Years`). The `IN GATE` marker is text, not colour alone.
INDEX button target: 44×44px minimum, in the bar's 44px height exactly.
Visible focus: a 2px `--amber` outline offset 2px — the theme's focus
ring everywhere (§6.8's parity rule uses the same).

**Content merge.** The index *is* the reel's catalogue — frame ranges and
chapter titles computed from the same DOM as the counter (law 4). It
cannot list a chapter the film doesn't have.

**Failure fallback.** A static contents list at the top of the document
with fragment links. Fully functional, unanimated.

**Reduced motion.** Drawer appears/disappears without sliding (opacity
0ms — instant), film does not dim (the dim is a lamp effect; instant
state changes keep full brightness), selection = instant jump.

**Performance & mobile variant.** One transform on the drawer; rows are
plain DOM. Mobile variant is the breakpoint spec above.

**Tokens.** `--ease-detent`, `--ease-lamp`, `--amber`, `--amber-wound`,
`--celluloid`, `--room`.

### 6.14 The gate hero — first frame composition

**What & why.** Frame 001 is the reel's title frame, and it is composed
like one: the filmed masthead (reel title in Newsreader 64px), the
catalogue line in mono beneath it (reel code, date range, holding
archive), and the first content the visitor came for — never a marketing
hero with a stock sky. The composition exists to be magnified by §6.1:
every element in it is placed where the zoom's steps will reveal it in
order — edge-printing first (visible even at 0.12 scale, because mono at
the frame's edge is the largest contrast at small size), masthead at the
0.35 hold, catalogue line at 0.62, opening content at lock.

**Structure.** A `.frame.frame--title`: top edge-printing strip (reel
code left, `FRAME 001` right, celluloid); masthead block centred-left at
58ch measure; catalogue line in mono `--amber`; a hairline scratch pair
(the hero's own light wear, §6.1's settle); the opening section's first
paragraph or image in the frame's lower half; at the frame's foot, the
advance hint — a mono line, `WIND TO FRAME 002 ↓`, with the down-detent
glyph drawn as two sprocket holes and a rule. The hint is part of the
film (edge-printed), not a floating UI pill.

**Motion spec.** The hero's motion *is* §6.1 + §6.10: zoom 1400ms, settle
500ms, jitter 1000ms, then stillness. After lock, the only motion in the
hero is ambient (§6.6) and the advance hint's glyph: the two sprocket
holes fill with amber in alternation every 1600ms (`--ease-lamp`) — the
machine idling, suggesting the wind direction without bouncing anything.
Scroll from the hero is §6.2's first detent, which the visitor has been
watching the machine prepare for.

**Choreography timeline (v2).** (= §6.1's and §6.10's, composed.)
- t=0–100 — Frame tiny in gate; edge-printing legible as texture.
- t=100–1500 — Zoom steps; masthead readable from the 0.35 hold (t≈520);
  catalogue line from 0.62 (t≈940).
- t=1500–2000 — Settle: scratches resolve; opening content fully lit.
- t=1500–2500 — Title jitter, decaying; locks at t=2500.
- t=2500 — Hero at rest. Advance hint begins its 1600ms idle alternation.
- First scroll — First detent step (§6.2) carries the hero out of the
  gate; its edge-printing is the last thing seen leaving — correct: the
  frame's number leaves last, like a page's folio.

**State matrix (v2).**

| State | Composition | Notes |
|---|---|---|
| Loading | §6.12 blank at frame 001's position | The reel threads before it focuses. |
| Focusing | Per §6.1 | — |
| Rest (locked) | Full composition, ambient only | The working hero. |
| Hover | §6.8 swell on the whole frame | The lens leans over the title frame like any other. |
| Scrolled-past | Static in the transcript | Returning shows it locked, no re-zoom (§6.1). |
| Disabled / reduced | Static composition, hint glyphs still | Fully readable from first paint. |

**Breakpoint behaviour (v2).** ≥1200px: masthead 64px. 768–1199px: 52px,
catalogue line wraps under the reel code. <768px: masthead 40px/1.08,
the opening content moves to frame 002 (a phone gate is small; the title
frame carries title + catalogue + hint only, and the reel says so in its
frame count — the counter's total is computed, so the composition change
is honest arithmetic, not a hidden cut).

**Edge cases (v2).** A reel with a very long title (a full newspaper name
plus subtitle): the masthead wraps to two lines and the catalogue line
drops a pitch (26px) — the frame grows by measurement (§6.2), the zoom's
steps are scale-based and unaffected. A reel whose first content is an
image: the image sits in the lower half in its own gate (§5 image
treatment) and scale-in-frames as the zoom locks — two magnifications
composing, capped per §6.8's rule. No opening content at all (a pure
title reel): the frame is title + catalogue + hint, and it is *shorter* —
the reel's honesty about its own sparseness.

**Accessibility (v2).** The masthead is the page's single `<h1>`. The
catalogue line is a `<p>` in mono — read as text, not decoration. The
advance hint is `aria-hidden` (scrolling needs no instruction for AT;
the document order teaches it). Focus order: skip-link → INDEX → first
content link in the hero — nothing in the ceremony intercepts focus.

**Content merge.** The hero is the reel's actual title frame — its real
name, its real catalogue data, its real first content. There is no hero
*about* the archive separate from the archive's first frame.

**Failure fallback.** A static title frame: masthead, catalogue, content,
hint. Indistinguishable from the locked state.

**Reduced motion.** The locked state from first paint (§6.1/§6.10 reduced
variants compose here).

**Performance & mobile variant.** No machinery of its own beyond §6.1,
§6.6, §6.10. Mobile variant is the breakpoint spec above.

**Tokens.** `--phosphor`, `--amber`, `--celluloid`, `--ease-lamp`.

### 6.15 Frame cards — catalogue entries

**What & why.** Where the reel lists its holdings — a chapter's frames, a
collection's reels, search results — each entry is a **frame card**: a
small gate containing the frame's image or opening lines, its frame
number edge-printed at the top, its catalogue line beneath. Cards are
laid in a grid like a contact sheet on the light table. It belongs
because the archive's unit is the frame, so the archive's card is a
frame — a visitor who has read three cards has already learned to read
the reel.

**Structure.** `article.frame-card`: gate area (aspect 1.37:1) holding
either the frame's image (gated, §5 treatment) or, for text frames, its
first two lines in Newsreader 17px on the amber ground-glow; top
edge-strip with `№ 012` (celluloid) and the reel code; below the gate:
title (Newsreader 20px), catalogue line (mono 12px, `--phosphor-aged`:
date, frames, condition — `CONDITION: GOOD / WATER DAMAGE AT 041`). The
whole card is one link to the frame. Damaged entries carry §6.5's scratch
motif at miniature scale on their gate's edge — drawn, static, honest.

**Motion spec.** Entry: cards expose through their gates in grid order
(§5 gate exposure, 240ms) staggered 60ms per card as their row detents
into view — a contact sheet being laid down row by row. Hover: §6.8's
swell applies inside the card's gate (1.03, 250ms) and the card's
edge-strip brightens celluloid→amber-wound. Click: §6.9's clunk, then
§6.12's whip to the frame itself. No card ever flips, lifts, or shadows —
film lies flat on the light table.

**Choreography timeline (v2).** (A row of three entering.)
- t=0 — Row's detent approaches; card 1's gate begins exposing.
- t=0/60/120 — Cards 1/2/3 begin exposing, staggered.
- t=240/300/360 — Gates fully open; catalogue lines were never hidden
  (they sit below the gate, in the clear).
- Hover — Swell per §6.8's timeline, scoped to the card's gate.
- Click — Knock (16ms), whip (§6.12), arrival at the real frame.

**State matrix (v2).**

| State | Gate | Edge-strip | Notes |
|---|---|---|---|
| Pre-entry | Gate closed (content present beneath) | Visible | §5's gate promise covers the row: 1s watchdog per card. |
| Rest | Open, image/lines at 1.0 | Celluloid | — |
| Hover/focus | Swell 1.03 in-gate | Brightens to amber-wound | Focus = hover, exactly (§6.8 parity). |
| Active | Knock + whip away | — | The card is a departure, not a destination. |
| Scrolled-past | Open, static | Celluloid | Cards never re-expose on scroll-back. |
| Disabled / no-JS | Open, static | Celluloid | A printed contact sheet. Fully functional links. |

**Breakpoint behaviour (v2).** ≥1200px: 3-up grid, gates 1.37:1.
768–1199px: 2-up. <768px: 1-up, gate aspect 16:10 (a phone's light table
shows one wide frame at a time), stagger cut to 30ms, swell still applies
on focus only.

**Edge cases (v2).** A frame with no image and a one-line opening: the
gate shows the line plus its frame's damaged/wear furniture if any —
never a placeholder graphic; an empty gate with edge-printing is a
truthful card for a sparse frame. Very long titles: two lines max, then
the catalogue line; truncation is by the content model (the archivist
writes a short title), never by CSS ellipsis on the card's face — the
full title lives on the frame itself, one click away. A reel with 200
entries: the grid paginates by chapter (§6.13's ranges), it does not
infinite-scroll — film ends, and so do lists (§11's pagination treatment).

**Accessibility (v2).** One link per card, named by the frame's title +
number ("Frame 012, The Foundry Opens, 1911"). The gate's image carries
the frame image's own alt. Focus outline is §6.13's amber ring on the
card. Touch targets: the whole card (≥180px tall at every breakpoint).

**Content merge.** The card *is* a miniature of the frame it links to —
same gate, same edge-printing, same condition line the catalogue keeps.
It is not a teaser invented for the listing; it is the frame, small.

**Failure fallback.** Static contact sheet: gates open, links live.

**Reduced motion.** Gates pre-open, no stagger, no swell; cards are a
printed contact sheet.

**Performance & mobile variant.** Gate exposures are clip-path animations
on in-view rows only; off-screen rows cost nothing. Images inside gates
are lazy and sized to the gate. Mobile variant is the breakpoint spec
above.

**Tokens.** `--ease-detent`, `--celluloid`, `--amber-wound`,
`--phosphor-aged`.

### 6.16 The request form — reading-room request slip

**What & why.** The reel's conversion moment is a request: a visitor asks
the archive for the thing — a frame scan, a reel booking, a research
enquiry. The form is a **reading-room request slip**: the paper form a
librarian hands you, rendered in the machine's language — mono labels,
ruled lines instead of boxes, and on submission, the slip is stamped with
a request number and filed. It belongs because archives convert by
request, not by checkout, and the slip keeps the transaction inside the
fiction while doing real work: it is a form first and a theme second, in
that order, always.

**Structure.** A frame (its own frame number in the reel — the request
frame is *in* the film, reached by winding like everything else) holding
a `<form>`: fields for name, email, reel/frame requested (pre-filled from
the frame the visitor was reading when they chose "Request this frame" —
the slip knows which frame you mean), and a note field ("What are you
researching?"). Labels are mono 11px uppercase above ruled inputs
(transparent ground, 1px `--amber-wound` bottom rule, Newsreader 19px
entry text — the visitor writes on the film in the film's face). The
submit is a housing-style button: `SUBMIT REQUEST` in mono on a bordered
plate. Errors render as librarian's notes (§3's voice) beneath their
fields, in `--amber`.

**Motion spec.** Focus: the field's rule brightens `--amber-wound`→
`--amber` (160ms `--ease-lamp`) and the label steps up one weight — the
lamp leaning over the line you're writing on. Field completion (blur with
a valid value): a small mono tick `✓ FILED` fades in at the rule's right
end (200ms) — the slip acknowledging each line. Submit: the button gives
§6.9's knock; the form frame detents once (a 120ms step in place — the
machine registering the slip); on success the whole slip is overlaid by
its stamped copy: a rotated (−3°) mono stamp `REQUEST № 214 — RECEIVED`
in `--amber` draws in like §6.5's scratch (500ms), and the counter in the
housing ticks +1 (requests are counted by the same machine). Error: the
offending field's rule turns to a scratch line (§6.5's SVG at field
scale) and the note exposes beneath — never a shake; paper doesn't shake.

**Choreography timeline (v2).** (Submission, success path.)
- t=0 — Submit activated. Knock (16ms edge brightness on the button).
- t=16–136 — Form frame detents in place (120ms step, 1px catch).
- t=136 — Request sent (async). Button label → `FILING…` with the §6.12
  blank-frame pulse on its plate (opacity 0.6↔1, 800ms loop, max 3 loops
  before the timeout note).
- Response — Stamp draws (500ms), counter ticks, success note exposes:
  `NOTE — Your request is in the reading-room tray. We answer within two
  working days.` Focus moves to the success heading.
- Error path — At response: field scratch + note per above; focus moves
  to the first error's field; the rest of the slip's entries are
  untouched. Paper remembers what you wrote.

**State matrix (v2).**

| State | Field rule | Label/note | Notes |
|---|---|---|---|
| Rest (empty) | `--amber-wound` | Mono label | — |
| Focus | Brightens to `--amber` 160ms | Label weight steps up | One field lit at a time — the lamp is small. |
| Filled & valid | `--amber-wound`, `✓ FILED` at right | — | The tick is mono, 11px, never green: the archive has no green. |
| Error | Scratch line drawn | Librarian's note beneath in amber | Persistent until corrected; never timed-out. |
| Submitting | Rules hold | Button `FILING…` | Fields disabled but legible (opacity 1, `aria-disabled` pattern per §11). |
| Success | Whole slip under its stamp | Success note + request number | The form becomes the record of itself. |
| Disabled / no-JS | Standard ruled form | Server-rendered notes | Posts natively; the stamp is a server-rendered confirmation page state. |

**Breakpoint behaviour (v2).** ≥1200px: slip at 58ch centred in its frame,
two-column for name/email. 768–1199px: single column, 52ch. <768px: the
slip fills the gate (frame padding 26px), inputs at 19px (also preventing
iOS zoom), the stamp scales to the slip's width, `✓ FILED` moves below
the rule's left end (the right end is where thumbs live).

**Edge cases (v2).** Arriving without a frame context (nav → Request
directly): the reel/frame field is an empty ruled select listing the
catalogue — the slip asks, it doesn't assume. Validation is on blur per
field + full pass on submit; a visitor who never blurs still meets every
note on submit, in field order. Network failure on submit: the slip's
note reads `NOTE — The tray is unreachable. Your entries are kept above.
[Try again]` — entries persist (they were never cleared), retry is one
activation. Double-submit: the button disables at t=0 of the timeline;
the detent-in-place is the lock's theatre and its truth. Autocomplete:
encouraged (`autocomplete` attributes correct); an autofilled field shows
its `✓ FILED` only after its first blur — the archive acknowledges what
it has *seen*.

**Accessibility (v2).** Real `<label>`s (the mono labels are labels, not
decoration), `aria-describedby` wiring each field to its note, errors
announced via a single `role="alert"` summary at submit (not per-field
shouting). Focus visible: §6.13's amber ring. The stamp is `aria-hidden`;
the success is conveyed by the success heading + note text. All targets
≥44px; the form is fully operable by keyboard in DOM order, and the
detent-in-place never moves focus. Contrast: entry text phosphor 15.2:1;
notes amber 7.6:1; rules are decoration and exempt, but the *label* of
every state is text at AA or better.

**Content merge.** The slip requests the archive's real holdings, is
pre-filled from the real frame being read, and its confirmation is
numbered by the same counter that numbers the frames. The fiction and
the function are one object: a request slip, in a reading room, for this
reel.

**Failure fallback.** A plain ruled form posting to the server, with
server-rendered notes and confirmation. Every enhancement is layered on
a form that already works.

**Reduced motion.** No detent, no stamp draw (stamp present, static), no
pulse; state changes are instant. The success note still appears and
focus still moves.

**Performance & mobile variant.** The form's motion reuses §6.2, §6.5 and
§6.9 machinery; its own cost is a few class toggles. Mobile variant is
the breakpoint spec above.

**Tokens.** `--ease-lamp`, `--ease-detent`, `--amber`, `--amber-wound`,
`--phosphor`.

### 6.17 End-of-reel footer

**What & why.** Film ends, and it says so. The footer is the reel's tail:
a length of blank leader, the `END OF REEL` edge-printing, the archive's
colophon set as the last frame's catalogue entry — what this reel was,
who holds it, what else they hold — and the reading-room's practical
lines (hours, requests, contact) in mono. It belongs because a visitor
who has wound the whole film has earned a proper ending, and because the
tail of a reel is where archives write their truth: the colophon is the
one frame the archivist authors outright.

**Structure.** Final frame (number = total, computed): 30vh of leader
(blank frame, ground-glow only, one hairline scratch — the tail is always
a little worn), then the colophon frame: `END OF REEL — REEL 07` edge-
printed in celluloid; colophon prose in Newsreader (the holding archive,
the digitisation note, the catalogue credit — "Catalogued by E. W.,
revised 2024"); three mono columns of practical links (Visit / Request /
About the archive) as real lists; the take-up statement — the counter's
total repeated as text: `YOU HAVE READ 340 FRAMES`. A `REWIND TO FRAME
001` housing button closes the visit (§6.12's whip, run in reverse at
600ms — rewinding a full reel takes a beat longer than advancing a
section, and the machine is honest about that too).

**Motion spec.** Arrival: the leader frame detents in like any frame; the
colophon's gate exposure is the standard 240ms. The `YOU HAVE READ` line
counts nothing — it *states* (the counting was §6.11's job, done along
the way; the tail is a signature, not an instrument). Rewind: §6.12 whip
reversed — blur builds over 200ms, travel 250ms, resolve 150ms into
frame 001 *without* replaying §6.1's zoom (the projector is threaded;
rewinding does not re-thread it) — the hero sits locked, and the counter
ticks down through the whip to 001.

**Choreography timeline (v2).** (Arrival at the tail.)
- t=0 — Last content frame's detent releases; leader frame steps in
  (120ms + catch).
- Leader travel (30vh) — Near-stillness: grain only. The pause is the
  point — the film runs out before the credits speak.
- Colophon detent — Gate exposes (240ms); `END OF REEL` was edge-printed
  and legible throughout the approach.
- Rest — The tail is still. §6.7 does not bloom here unless the tail
  frame is catalogued as leaked (§6.7 includes last frames — if this
  reel's tail leaks, it blooms on its irregular schedule, the archive's
  last word).

**State matrix (v2).**

| State | Leader | Colophon | Notes |
|---|---|---|---|
| Approaching | In gate, blank, glowing | Below | — |
| Rest (arrived) | Scrolled past | Exposed, still | The visit's end state. |
| Rewinding | Whip reversed (600ms total) | — | Counter ticks down through the blur. |
| Hover | §6.8 on the colophon frame | — | The tail is a frame and gets the lens like any other. |
| Print | Leader omitted | Colophon prints as the transcript's last page | `@media print`: the whole reel prints as a transcript — frames in order, notes included, housing hidden, footer as colophon. The theme's print stylesheet is a feature, not an afterthought: archives get printed. |
| Disabled / no-JS | Static last section | Static, complete | The document simply ends properly. |

**Breakpoint behaviour (v2).** ≥1200px: three mono columns. 768–1199px:
two columns. <768px: one column, leader shortened to 18vh (a phone's
patience for blank film is shorter, and the spec respects it), rewind
button full-width at 52px tall.

**Edge cases (v2).** A one-frame reel: leader + colophon still render —
even the shortest film has a tail. A visitor who jumps straight to the
footer via the index: the `YOU HAVE READ` line computes from the reel's
total, and the copy is written to be true regardless of path ("THIS REEL
HOLDS 340 FRAMES" is the fallback phrasing the content model uses when
the session's read-state is incomplete — the line never claims a reading
that didn't happen; §12's voice rules govern the two phrasings).

**Accessibility (v2).** The footer is a real `<footer>` with the colophon
as prose and the columns as labelled nav lists. `END OF REEL` is text.
The rewind button is a button, 44px+, named "Rewind to frame 1". Print
transcript: headings and notes in order, mono furniture converted to
plain text — a screen-reader and a printer both get the archive, not the
machine.

**Content merge.** The colophon is the archive writing about its own
reel — the catalogue's last entry, authored by the cataloguer whose notes
have accompanied the whole visit. The footer is not chrome appended to
the theme; it is the film's own tail.

**Failure fallback.** A static, complete footer. The document ends well
with no machinery at all.

**Reduced motion.** Leader and colophon static; rewind is an instant
jump to frame 001 with focus to the masthead.

**Performance & mobile variant.** No new machinery. Mobile variant is the
breakpoint spec above.

**Tokens.** `--celluloid`, `--amber-wound`, `--phosphor-aged`,
`--ease-whip`.

### 6.18 Frame finder — jump-to-frame search

**What & why.** Researchers arrive with a name, a date, a headline. The
frame finder is the reading room's catalogue drawer: a housing tool that
takes a query and returns frames — not "results pages", frames — each
result a §6.15 card with the matched line shown *in its gate*, the match
itself lit amber the way a librarian pencils a margin. It belongs because
search is how this audience actually enters an archive, and because the
finder keeps search inside the fiction without weakening it: the query
is typed on a catalogue card, the answer is a set of frames you then wind
to.

**Structure.** Opened from the housing (`FIND` button beside `INDEX`):
a panel in the housing layer, top-anchored, holding a ruled input (§6.16's
field treatment) labelled `SEARCH THE CATALOGUE`, and below it the
result strip: §6.15 cards in a horizontal contact-sheet row (desktop) or
vertical list (mobile). Each result card's gate shows the frame's matched
line with the matched term wrapped in `<mark>` styled as an amber
pencil underline (background `--amber` at 18%, 2px bottom rule in
`--amber`). The strip's head is a mono count: `7 FRAMES MATCH "HALSTEAD,
W."` — computed, like every number here.

**Motion spec.** Open: panel steps down from the housing over 220ms
(`--ease-detent`). Typing: results do not stream per keystroke — the
catalogue is consulted on a 300ms debounce, and the strip cross-fades
(160ms, `--ease-lamp`) between result sets; a machine that answered
mid-word would be showing off. Match lighting: when a result set lands,
the `<mark>` underlines draw left-to-right over 300ms, staggered 40ms
per card — the librarian's pencil moving down the drawer. Selecting a
result: panel closes, §6.12's whip to the frame, and on arrival the
matched line in the real frame carries the same pencil underline, drawn
once (400ms) — the visitor lands on the exact line they came for.

**Choreography timeline (v2).**
- t=0 — FIND activated; panel steps down (220ms); focus to the input.
- Typing + 300ms debounce — Strip fades out (160ms).
- Results ready — Strip fades in; underlines draw staggered (300ms +
  40ms × cards).
- Selection — Panel closes (180ms); whip (§6.12); on lock, the in-frame
  underline draws (400ms); focus to the frame's heading.
- Esc — Panel closes; focus returns to FIND; the reel is where it was.

**State matrix (v2).**

| State | Panel | Strip | Notes |
|---|---|---|---|
| Closed (rest) | Hidden | — | — |
| Open, empty query | Down | Shows the reel's chapter cards (§6.15) | An empty drawer still shows the catalogue's shape — never a blank void. |
| Open, typing | Down | Previous results at 40% until debounce lands | The strip never flickers per keystroke. |
| Results | Down | Cards + drawn underlines | Count line in mono, computed. |
| No results | Down | One card: the empty-state frame (§12's voice) | `NO FRAME MATCHES — NOTE — Try the surname alone…` — a librarian's suggestion, not an error. |
| Disabled / no-JS | A search page (GET form → results page of §6.15 cards) | Server-rendered | Search works without the panel; the panel is the drawer, the page is the catalogue. |

**Breakpoint behaviour (v2).** ≥1200px: horizontal strip, up to 5 cards
visible, strip scrolls in detents (of course). 768–1199px: 3 visible.
<768px: panel is full-screen (the phone's drawer is the whole desk);
results vertical, one card per row; the in-frame underline draw is kept —
it is the finder's whole payoff.

**Edge cases (v2).** A query matching a damaged frame: its card carries
§6.5's furniture and the match line may sit under a scratch — the
underline still draws, over the scratch: the librarian pencils over
damage without pretending it isn't there. A query matching 200 frames:
the strip caps at the first 20 by catalogue order with a mono tail line
(`+ 180 FURTHER FRAMES — REFINE THE SEARCH`) — the drawer shows a
drawerful. Zero-length query submit: treated as empty state, no error.
Very long queries wrap in the input (it is a ruled field, it grows a
second line — paper does).

**Accessibility (v2).** The input is a real `role="search"` form with a
real label; results are a list of links (§6.15's naming); the count line
is `aria-live="polite"` — the one live region in the theme, because a
search count is information the visitor cannot see coming, unlike frame
positions (§6.11's silence rule stands elsewhere). Marks are `<mark>`
elements — AT conveys them where supported, and the underline is never
the only signal (the card's catalogue line also names the match type:
`MATCH: HEADLINE / TEXT / NOTE`).

**Content merge.** The finder searches the reel's actual frames and
returns the frames themselves, with the visitor's own term pencilled into
the actual line. It is the catalogue drawer of this archive, not a
search widget pasted onto it.

**Failure fallback.** The GET search page: form, results as §6.15 cards,
marks as static underlines. Complete without JS.

**Reduced motion.** Panel appears instantly; no cross-fades; underlines
present, undrawn; whip replaced by the jump (§6.12's reduced variant).

**Performance & mobile variant.** Debounced queries; result cards reuse
§6.15's machinery; underline draws are composited border animations on
≤5 visible cards. Mobile variant is the breakpoint spec above.

**Tokens.** `--ease-detent`, `--ease-lamp`, `--amber`, `--amber-wound`,
`--phosphor-aged`.

## 7. Page application map

**Home (the reel's first winding).** Frame 001 title (§6.14) → chapter
frames in catalogue order, damaged dividers at every 7th (§6.5) → a
holdings frame (§6.11's statistics live here, mid-reel, where the
catalogue states them) → the request frame (§6.16) as the penultimate
frame → end-of-reel (§6.17). The home page *is* the featured reel; there
is no separate marketing layer above the film.

**Listing (a shelf of reels).** A contact-sheet page: §6.15 cards grouped
by collection, each card a reel (not a frame — at this level the unit is
the reel, and the card's gate shows the reel's title frame). The housing
is present but the film layer holds the *shelf*: cards detent by row
(§6.2's mechanics at row scale). Selecting a reel loads its film — a
§6.12 whip into frame 001 with §6.1's zoom, because threading a new reel
is a new session's beginning.

**Detail (a single frame, deep-linked).** Arriving at `#frame-012` places
the film at that detent with gates pre-opened, no zoom, no jitter (§6.10's
edge rule). The frame's neighbours are one detent away in each direction;
the index (§6.13) shows `IN GATE` on its chapter. The detail page and the
home page are the same document — a frame's URL is a position in the
reel, never a separate template.

**About (the archive's own frame).** The archive's history is a chapter
of frames like any other — including, usually, its own damaged divider:
every real archive has a flood, a fire, or a funding gap, and the about
chapter is where its note belongs. Staff are catalogue entries (§6.15
cards, portrait frames), not team-grid avatars.

**Request / contact.** §6.16's slip, reachable from any frame's "Request
this frame" (pre-filled) or as its own frame (blank context). There is
no separate contact page with a map and a chat widget; the reading room
takes requests on slips.

**Search results.** §6.18's server-rendered twin: a page of §6.15 cards
with pencilled marks, headed by the mono count. It is a drawer emptied
onto the light table.

**404 (a frame that was never shot).** A single damaged-style frame —
without §6.5's ceremony — carrying one mono note: `NOTE — No frame
answers to this number. The reel you want may be in the index.` plus the
index itself (§6.13's static form). The 404 is a catalogue answer, not a
mascot.

## 8. Worked examples (v2: hero, mid-page, conversion — end-to-end)

### Example A — The hero: "REEL 07 — THE HALSTEAD GAZETTE, 1911–1968"

A genealogy service's featured reel. Frame 001 per §6.14. Content:
edge-printing `REEL 07 · HALSTEAD GAZETTE` / `FRAME 001`; masthead
(Newsreader 64px) "The Halstead Gazette"; catalogue line: `REEL 07 ·
1911–1968 · 340 FRAMES · HELD BY THE HALSTEAD COUNTY ARCHIVE`; opening
content: the first paragraph of the archive's introduction, plus the
advance hint.

- **t=0** — Blank frame (§6.12) at frame 001's position exposes as the
  reel's data lands (≤300ms cross-fade).
- **t=100** — §6.1 zoom begins: scale 0.12. At this size only the
  edge-printing reads — deliberately: the visitor first learns *what film
  this is*.
- **t≈520** — First hold (0.35): the masthead's first line is legible.
- **t≈940** — Second hold (0.62): catalogue line legible — 340 frames,
  the promise of the visit's size, made in mono.
- **t=1500** — Lock + catch. Settle begins: the hero's two hairline
  scratches fade to 0.35; dust fades in over 500ms.
- **t=1500–2500** — §6.10 jitter on the masthead, decaying ±1px → ±0.5px.
- **t=2500** — Stillness. Grain crawls; dust drifts; the advance hint's
  sprocket holes begin their 1600ms alternation.
- **First scroll** — §6.2 detent: frame 002 (the 1911 chapter opener)
  steps in over 120ms + catch; counter ticks `FRAME 002 / 340`; the
  take-up reel (§6.4) rotates its first third-turn and grows its first
  sub-pixel of wound film. The visitor has wound the machine once and
  understands it entirely.

### Example B — Mid-page: the damaged divider into "The Flood Years"

Frame 014 (the second damaged divider) into frame 015, the Flood Years
chapter opener, on the same reel.

- **Approach** — Frame 013 (a 1952 front page) is in the gate. The
  visitor scrolls; §6.2's detent engages.
- **t=0** — Detent locks on frame 014. Pin engages (60vh slot).
- **t=0–700** — The flood frame's scratches draw: three paths, the
  longest a horizontal tide line at the frame's lower third, staggered
  90ms (§6.5 timeline).
- **t=350** — The left-edge leak begins its one arrival bloom (2500ms).
- **t=700** — The note gate-exposes: `NOTE — Frames 041–048 of the
  original Gazette were water-damaged in the flood of March 1953. This
  divider stands where they would have been. What survives is listed in
  the next chapter.` — the note explains an *absence in the numbering*:
  the reel's frame numbers skip, and the skip is the history.
- **Pin travel** — The visitor sits with the damage for the remaining
  pin distance; grain and dust continue; nothing else moves. The
  chapter title is edge-printed at the frame's foot: `THE FLOOD YEARS —
  WHAT SURVIVES`.
- **Release** — Frame 015 steps in: a §6.15-style chapter opener frame —
  headline "The Flood Years", and a grid of six frame cards (the
  surviving frames), exposing in stagger (§6.15 timeline). The counter
  reads `FRAME 015 / 340`. The take-up reel has visibly grown.
- **Scroll-back check** — Winding back up: frame 014 shows its damage
  fully drawn, no redraw (§6.5 matrix); the note is simply there, like
  damage is.

### Example C — Conversion: requesting a scan of frame 233

From frame 233 (a 1938 photograph frame), the visitor chooses "Request
this frame" (a housing-styled link in the frame's catalogue line).

- **t=0** — §6.12 whip (400ms): blur, counter free-run 233 → the request
  frame's number, lock + catch. Focus lands on the request frame's
  heading: "Request a frame".
- **The slip** (§6.16) — Pre-filled: `REEL 07 — FRAME 233 — "Mill
  Cottages, 1938"`. The visitor adds name, email, and a note: "Looking
  for my grandmother's house — I think it's the third cottage." Focus
  lights each rule in turn (§6.16); `✓ FILED` ticks appear on blur.
- **A mistake, handled in voice** — The email lacks its domain. On submit:
  that field's rule becomes a scratch line; beneath it, the librarian's
  note: `NOTE — The address line is incomplete: a domain is missing, the
  way a house number might be. Nothing else on the slip is disturbed.`
  Focus moves to the email field. The rest of the slip — including the
  grandmother sentence — is untouched.
- **Resubmit** — Knock (16ms), detent-in-place (120ms), `FILING…` (one
  800ms pulse), then the stamp draws over 500ms: `REQUEST № 214 —
  RECEIVED`, rotated −3°, in amber. The housing counter ticks. Success
  note: `NOTE — Your request is in the reading-room tray. We answer
  within two working days, and frame 233 will be held for you meanwhile.`
- **The merge, stated plainly** — the request is numbered by the same
  machine that numbered the frames, the confirmation speaks in the same
  voice that annotated the flood, and the frame the visitor asked for is
  *held* — the fiction's promise and the archive's actual workflow are
  the same sentence.

## 9. Anti-slop — how THIS theme goes cheap, and the cure

1. **Smooth scrolling left on.** The film glides like a normal website in
   a film costume. *Cure:* §5 law 1 — detents or nothing; the gate (§10)
   tests the step at three scroll speeds.
2. **Damage everywhere.** Scratches and leaks sprinkled over every frame
   "for vibe". *Cure:* law 3 — damage exists only on catalogued damaged
   frames, each with its note. Undocumented damage is deleted, not
   debated.
3. **Invented numbers.** A counter reading `/ 340` on a 23-frame page, or
   statistics typed by the designer. *Cure:* law 4 — every number computed
   from the DOM or written by the archivist in the content. The gate
   counts the frames and compares.
4. **Amber flood.** Amber backgrounds, amber buttons, amber everything —
   the lamp becomes a brand colour and the room stops being dark. *Cure:*
   §2's ratio discipline (≈18% and falling); if a screenshot's amber
   exceeds a fifth of the viewport, the build fails review.
5. **Blue body text.** Celluloid blue set as paragraphs because it "looks
   archival". *Cure:* §2's contrast law — blue is edge-printing, 2.8:1,
   graphic only. The gate measures it.
6. **A spinner in a trench coat.** Loading states that are generic
   progress bars renamed "winding". *Cure:* §6.12 — blanks are unexposed
   frames at true size, or the state doesn't ship.
7. **Jitter as a personality.** The title jitter applied to every heading,
   or left running. *Cure:* §6.10 — one object, one second, once.
8. **Hover-reveal content.** Text that only appears when hovered or when
   the swell engages. *Cure:* §6.8's hard rule — hover magnifies, it
   never reveals. Everything readable at rest, at 1.0, with the pointer
   elsewhere.
9. **Generic sans creeping in.** A system-ui label "for clarity" in the
   housing. *Cure:* §3's two-face law — machine text is mono, film text
   is Newsreader; there is no third case, and "clarity" is what the
   15.2:1 phosphor is for.
10. **The reel that lies about length.** A take-up reel that fills by
    scroll percentage of a *different* total than the counter shows.
    *Cure:* §6.4 and §6.11 share one detent state; the gate scrolls the
    full page and checks reel, counter and read-line against each other.

## 10. Quality gate

Blocking — every item must pass before a build in this theme ships:

1. Film never glides: at slow, medium and fling scroll speeds, film
   movement renders as detent steps (or §6.3's blur) — zero frames of
   continuous slide.
2. Gate promise: with JS throttled and animations stalled, every gated
   reveal is open within 1s of its trigger; with JS disabled, the full
   document is readable as a transcript.
3. Numbers audit: frame total in the counter = actual `.frame` count;
   take-up reel at p=1 = full; §6.17's stated total matches both; every
   `data-count-to` sits on a quantity, never a range.
4. Damage audit: scratches/leaks/notes exist only on damaged frames;
   damaged frames are never adjacent; every damaged frame's note
   describes its own damage.
5. Contrast audit: body text phosphor-on-room only; no body text in
   celluloid blue anywhere; amber text ≥13px mono or ≥18px Newsreader.
6. Reduced-motion pass: with `prefers-reduced-motion`, the visit is a
   still strip — no zoom, jitter, detents, blooms, counting or whip —
   and loses zero content.
7. Focus pass: full keyboard traversal — skip-link, INDEX, FIND, every
   frame's advance button, the form — with the amber ring visible at
   every stop and no focus ever inside a blurred or gated-shut frame.
8. Performance pass: §14's budgets measured on a mid-tier Android over
   4G: LCP ≤ 2.5s, CLS ≤ 0.05, INP ≤ 200ms, shared loop ≤ 2ms/frame
   idle.
9. Print pass: the reel prints as a clean transcript — frames in order,
   notes as text, housing and ambient layers absent.
10. Amber ratio check: three screenshots (hero, mid-reel, footer) each
    measure ≤ ~20% amber coverage.

## 11. Component inventory (v2)

Every component a real archive site needs, in the machine's treatment.
Anything not listed does not get invented ad hoc — it is built from the
nearest listed relative.

- **Buttons (housing)** — Mono uppercase label on a 1px `--amber-wound`
  bordered plate, `--room` ground; hover: border → `--amber`, label →
  `--amber` (160ms `--ease-lamp`); active: §6.9's knock; primary (submit,
  request) plates carry a filled `--amber` ground with `--room` text
  (7.6:1) — the one filled thing the machine owns.
- **Buttons (in-film links)** — Newsreader text with a 1px celluloid
  rule; hover: rule → amber and thickens to 2px (120ms); never a filled
  box — the film doesn't have buttons, it has references.
- **Inputs** — §6.16's ruled fields: mono label above, transparent
  ground, `--amber-wound` rule, Newsreader entry text; focus and error
  per §6.16's matrix.
- **Selects** — Ruled like inputs; the open list is a catalogue drawer
  (mono rows, `--room` ground, celluloid left rule), never the OS
  default chrome inside the fiction — but the underlying element is a
  real `<select>` where the platform allows, styled, not replaced.
- **Checkboxes / radios** — Small sprocket squares: a 14px square with a
  perforated border; checked = the hole fills with `--amber` (a punched
  frame, filled). Radio = circular gate aperture, filled centre when
  chosen. Focus ring per §6.13.
- **Tables (catalogue tables)** — Mono, ruled with `--amber-wound`
  hairlines every row, header row edge-printed in celluloid; numbers
  right-aligned tabular; row hover = §6.6's ground-glow at 2% — the lamp
  leaning over the ledger.
- **Badges (condition / status)** — Mono 11px stamps, bordered, rotated
  0° (stamps on *records* are straight; only §6.16's receipt stamp
  rotates, because it is struck by hand): `CONDITION: GOOD`,
  `WATER DAMAGE`, `RESTRICTED — READING ROOM ONLY` (celluloid border,
  amber text for damage states).
- **Alerts** — Librarian's notes (§3's voice): a mono block with a
  `NOTE —` prefix and a celluloid left rule, on the frame ground. There
  are no red alerts in an archive; there are notes, and urgency is
  carried by wording, not colour.
- **Pagination** — Frame ranges, mono: `FRAMES 001–050 · 051–100 · …`
  with the current range in amber; it is §6.13's index in miniature.
  Infinite scroll does not exist (§6.15's ruling).
- **Modals** — One only: the frame viewer for a single frame's
  high-magnification view — the gate expands (scale via `--ease-magnify`,
  600ms, three holds) over the dimmed film, with the frame's full
  catalogue entry beneath it. Esc/click-out collapses it back into its
  detent. No other modal exists in the theme; confirmations are notes,
  not dialogs.
- **Toasts** — Refused. A reader has no toasts. Transient confirmations
  are written into the nearest frame's catalogue line as a note, or, for
  the form, are §6.16's stamp. If a platform pattern demands a toast,
  the demand is refused in the build notes with this paragraph cited.
- **Tabs** — Reel switchers on the shelf page: edge-printed mono labels
  along a frame line; the active tab's label in amber with its frame
  line drawn double (two rules, 3px apart — the tab is a frame boundary,
  marked twice).
- **Accordions** — Catalogue groups that open like a drawer being pulled:
  the group's frames list steps down in detents (each row 120ms, §6.2's
  easing), never a smooth height glide.
- **Search** — §6.18, whole and entire.
- **Tooltips** — Catalogue glosses: mono 12px on `--room`, celluloid
  border, appearing after 600ms hover/focus, positioned like an
  edge-print — always at a frame's edge, never floating mid-text.
- **Breadcrumbs** — The position line in the bottom housing bar: `REEL 07
  › THE FLOOD YEARS › FRAME 015`, mono, celluloid separators, current
  frame in amber. It updates per detent; it is the counter's prose twin.
- **Progress** — §6.4 + §6.11 only. No bars, no percentages, no rings.
- **Skeleton** — §6.12's blanks, for every loading surface including
  cards (§6.15 gates at blank) and the viewer modal.
- **Empty states** — A blank frame with a librarian's note (§12's
  voice): the archive explaining the empty shelf in its own words.

## 12. Content & copywriting voice (v2)

Two voices, matching the two typefaces. **The film's voice** (Newsreader)
is the original material's own — headlines and prose are the archive's
content, written as the source wrote them or as a respectful cataloguer
summarises them: plain, dated, specific. **The machine's voice** (mono)
is the reading room speaking: terse, procedural, kind. It labels, counts,
and notes. It never sells.

- **Headlines (film voice).** The frame's own title, set as found.
  ✓ "The Flood Years" · ✗ "Discover Our Amazing Flood Collection!" —
  the archive does not discover its own holdings at you.
- **Labels (machine voice).** Noun + number, uppercase, no verbs of
  excitement. ✓ `FRAME 233 · MILL COTTAGES, 1938` · ✗ `Check Out This
  Frame!`
- **Buttons.** The machine's verbs: `WIND`, `REQUEST THIS FRAME`,
  `SUBMIT REQUEST`, `REWIND`. ✓ `REQUEST THIS FRAME` · ✗ `Get Instant
  Access Now`.
- **Errors (machine voice, as librarian's notes).** State what is wrong,
  where, and what survives — in the metaphor of the record, never the
  software. ✓ `NOTE — The address line is incomplete: a domain is
  missing, the way a house number might be. Nothing else on the slip is
  disturbed.` · ✗ `Error: invalid email!!!`
- **Empty states.** ✓ `NOTE — No frame in this reel answers to that
  name. Try the surname alone, or the decade — the catalogue is patient.`
  · ✗ `Oops! Nothing here.`
- **Success.** ✓ `NOTE — Your request is in the reading-room tray. We
  answer within two working days.` (A promise with a number in it —
  §5 law 4 applies to words too: never state a turnaround the archive
  doesn't keep.) · ✗ `Awesome! You're all set! 🎉`
- **Loading.** ✓ edge-printed on the blank: `UNEXPOSED — AWAITING FILM`.
  · ✗ `Loading… please wait` (and never, ever, a percentage).
- **Banned words.** "Seamless", "cutting-edge", "discover", "unlock",
  "instant access", exclamation marks in machine voice, and the word
  "content" anywhere a visitor can see it — the archive holds *frames*,
  *reels*, and *records*.

## 13. Full-page scroll choreography map (v2)

The canonical home reel, top to tail. Every beat, in order:

1. **Threading (load).** Blank frame 001 exposes (§6.12); zoom steps to
   focus (§6.1, 1400ms); settle (500ms); title jitter locks (§6.10).
   The visitor has watched the machine prepare the film.
2. **First wind.** First detent (§6.2): counter ticks to 002, take-up
   reel's first turn (§6.4). The visitor learns the pace.
3. **Chapter frames.** Gate exposures per frame (§5); §6.8's swell
   available on each; grain and dust continuous in the gate (§6.6).
   The reading rhythm: step, read, step, read.
4. **First damaged divider (frame 7).** Pin, scratch draw, note (§6.5);
   first leak bloom (§6.7). The reel's wound, and its honesty, arrive
   early enough to set expectations.
5. **Holdings frame.** Statistics count once (§6.11) — the archive's
   size, stated in its own frame, in mono.
6. **Mid-reel chapters.** The rhythm deepens: longer text frames
   (internal sub-detents), image frames scale-in-frame, damaged
   dividers at 14, 21… each with a different injury and a different
   note. No new mechanics are introduced after this point — mastery,
   not novelty, is the mid-reel's pleasure.
7. **A long wind (visitor flings toward the request frame).** §6.3's
   blur: the decades streak past, counter free-running; resolve and
   lock. Distance felt in the hand.
8. **The request frame.** §6.16's slip; focus lamp per field; on
   success, the stamp and the counter's +1. The visit's purpose,
   transacted in the fiction.
9. **The tail.** Leader's held blank (§6.17), then the colophon: `END
   OF REEL`, the totals as text, the practical columns. Stillness.
10. **Rewind (optional).** The 600ms reverse whip to frame 001 — which
    sits locked and steady, threaded, ready to be read again.

Emotional arc: ceremony → competence → trust (the damage, honestly
shown) → purpose (the request) → rest (the tail). If a build's arc reads
as novelty → more novelty → most novelty, it has failed this map even if
every element passes alone.

## 14. Whole-page performance budget (v2)

**Assets.** Total initial load ≤ 480KB (fonts: Newsreader variable subset
≤ 90KB + IBM Plex Mono ≤ 60KB; JS ≤ 38KB gz — the loop, detents, and
observers are small because the theme refuses frameworks for its motion;
CSS ≤ 30KB gz). Frame images: gated, lazy beyond the second frame, each
≤ 120KB (they are film frames — grain forgives compression, and the spec
exploits that honestly: quality 72 WebP under the grain reads as stock,
not as compression).

**Runtime.** The shared rAF loop: ≤ 2ms script per frame idle, ≤ 4ms
during §6.3's wind (filter active). Detent steps are transform-only.
Grain: background-position steps, no repaint of content. Dust canvas:
≤ 1.5ms. No long task > 50ms after load; the zoom's steps are CSS/steps-
driven, not JS-intervalled. INP ≤ 200ms (the clunk's response is one
class + a target detent). CLS ≤ 0.05 — frames are height-measured before
content lands (§6.12's blanks reserve true space).

**Cut order** (when the budget is exceeded, cut in this order, and log
the cut in the build notes):
1. Dust motes (§6.6) — the most expendable beauty.
2. Grain crawl → static grain (§6.6's reduced treatment).
3. Light-leak pulses (§6.7) → static stains.
4. Fast-forward clone strips (§6.3) → blur alone.
5. Magnifier swell (§6.8) — hover becomes outline-only.
6. Internal sub-detents (§6.2) → boundary detents only.
**Never cut:** boundary detents, the gate promise/watchdogs, reveal
fallbacks, the counter's correctness, reduced-motion variants, the
form's function. A build that cuts from the never list to keep the dust
has misunderstood the archive's priorities, and the gate (§10.8) is
measured with the cut order applied, not before.

## 15. Build-order checklist (v2)

1. **Tokens & type.** Palette (§2), type scale (§3), easing/duration
   tokens (§5) as CSS variables. The two-face law wired as utilities.
2. **Static transcript.** The whole reel as a readable no-JS document:
   frames, lines, numbers, notes, form. This version must already pass
   §10 items 2, 3, 5 on its own — it is the fallback and the foundation.
3. **Housing.** Bars, rails, counter (static text), index (§6.13 static
   form). Print stylesheet (§6.17) with the transcript.
4. **The loop & detents.** Shared rAF loop; §6.2's quantisation; counter
   ticks (§6.11); take-up reel (§6.4) — all driven from one detent state.
5. **Gate exposures.** §5's reveal + the 1s watchdog (law 2) on every
   gated element, tested with animations stalled.
6. **Entrance.** §6.12 blanks → §6.1 zoom → §6.10 jitter, in that order,
   with the deep-link and return-visit suppressions.
7. **Damage.** §6.5 dividers + §6.7 leaks, with the adjacency and
   note-pairing checks (§10.4) run against the real content.
8. **Ambient.** §6.6 grain + dust, gate-clipped, with the low-power
   degradation path (§14 cut order) wired to the loop's frame budget.
9. **Wind.** §6.3's velocity blur + clone pool; §6.12's whip on top of
   it; §6.9's clunk and §6.8's swell.
10. **Finder & form.** §6.18 (panel over the working GET search), then
    §6.16's slip with its full state matrix, server fallback first.
11. **Reduced motion & a11y passes.** The still-strip variant end-to-end;
    focus traversal (§10.7); the counter's hidden text twin.
12. **Budgets & gates.** §14 measured on device; §10 run in full, in
    order, with the numbers audit (item 3) executed by script against
    the DOM — a human counting frames by eye is how `/ 340` happens.
