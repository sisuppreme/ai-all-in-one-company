# D3 Example — A Landing Page Hero, Rebuilt from Template Slop

## Scenario

Marketing needs a landing page hero for the SaaS: headline, subcopy, email
signup form, and a product visual. D3 builds it with the design-token system
and the UI-state matrix, and D9 will write the final copy later — the
structure, states, and visual system are D3's job now.

## Before

```html
<section style="background: linear-gradient(135deg,#7c3aed,#2563eb);
                padding: 96px 24px; text-align: center">
  <h1 style="font-size: 53px; background: linear-gradient(90deg,#f0abfc,#93c5fd);
             -webkit-background-clip: text; color: transparent">
    🚀 Supercharge Your Workflow ✨</h1>
  <p style="font-size: 19px">Join 10,000+ happy teams. 99.9% uptime. Zero setup.</p>
  <div class="logo-row">[ Acme ] [ Globex ] [ Initech ] [ Umbrella ]</div>
  <img src="dashboard.png">
  <div onclick="signup()" style="box-shadow: 0 8px 30px rgba(0,0,0,.35);
       border-radius: 8px; padding: 13px 22px">Get Started</div>
  <form onsubmit="return subscribed()"><input placeholder="Email address"></form>
</section>
```

Every card and button on the page reuses the same shadow and a different
radius (8px, 12px, 24px, pill). The form shows nothing while submitting,
nothing on error, and a fake progress bar that fills on a timer.

## What the skills caught

- **BAN-FE-022 — The violet-blue gradient as default** (**DET-VIS-017 —
  Purple-blue gradient signature**) and **BAN-FE-071 — Gradient headline
  text** (**DET-VIS-018**). **FE-048**: gradients exist only as named
  tokens with a brand reason.
- **BAN-FE-073 — Emoji as iconography** (**DET-VIS-016**), violating
  **FE-150 — Emoji are never structural**.
- **BAN-FE-005 — The unsourced stat band**: "10,000+ happy teams, 99.9%
  uptime" traces to nothing — **DET-VIS-035 — Stat band with round
  numbers**, **DET-CON-011 — Fabricated or unsourced statistics**.
- **BAN-FE-004 — The invented logo cloud** (**DET-VIS-034**): four company
  marks for customers that do not exist.
- **BAN-FE-002 — The clickable div**, violating **FE-002**; the hero image
  has no reserved dimensions (**FE-003**), so the page shifts on load.
- **BAN-FE-021 — Raw values in component styles** and **BAN-FE-072 —
  Off-scale font sizes** (53px, 19px): **FE-043 — Semantic only in
  components**, **FE-141 — Sizes come only from the type scale**
  (**DET-VIS-012 — Flat type scale**). **BAN-FE-024 — One shadow for
  everything** (**DET-VIS-021**) plus radius scatter (**DET-VIS-043**).
- The form has no state matrix at all — **FE-161**, **BAN-FE-084 — Fake
  progress or sync state** (**DET-VIS-032 — Missing or fake UI states**,
  **DET-FAKE-022 — Progress and sync states that lie**).

## After

```html
<section class="hero">
  <h1 class="hero__title">Plan the week before it plans you</h1>
  <p class="hero__sub">Fieldnotes turns a team's scattered tasks into one
    shared plan. Free for teams up to five — no card required.</p>
  <img src="/product/board.png" width="1120" height="700"
       alt="The Fieldnotes planning board with this week's tasks by owner">
  <form class="signup" data-state="idle">
    <label for="email">Work email</label>
    <input id="email" type="email" required autocomplete="email">
    <button type="submit">Get started</button>
    <p class="signup__status" role="status"></p>
  </form>
</section>
```

```css
.hero { background: var(--surface-page); padding: var(--space-section) var(--space-gutter); }
.hero__title { font-size: var(--text-display); color: var(--color-text-primary); }
.signup button { border-radius: var(--radius-control); box-shadow: var(--elevation-raised); }
```

The stat band and logo cloud are deleted, not softened — there is nothing
true to replace them with yet. The form implements the state matrix from
**FE-161**: idle, submitting (button disabled, status text), error (plain
message naming the fix, **FE-163**), success (confirmation with the next
step, **FE-164**). Contrast for every text/surface pair was computed before
the tokens were named (**FE-046**, gate **G-FE-023**).

## Skills used

- [frontend-core](../skills/frontend/frontend-core/SKILL.md)
- [design-tokens](../skills/frontend/design-tokens/SKILL.md)
- [typography](../skills/frontend/typography/SKILL.md)
- [ui-states](../skills/frontend/ui-states/SKILL.md)
