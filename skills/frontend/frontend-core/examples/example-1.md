# Example 1 — A clickable card becomes a real button

## Before

```html
<div class="plan-card" onclick="selectPlan('pro')">
  <h3>Pro</h3>
  <p>For growing teams</p>
  <span class="fake-btn">Choose Pro</span>
</div>
```

The whole card is a `div` with a click handler and the "button" is a styled
`span`. Keyboard users cannot reach it, screen readers announce nothing
actionable, there is no focus state, and Enter/Space do nothing. It renders
fine in a screenshot and fails every real user who does not use a mouse.

## After

```html
<article class="plan-card">
  <h3>Pro</h3>
  <p>For growing teams</p>
  <button type="button" class="btn btn-primary" onclick="selectPlan('pro')">
    Choose Pro
  </button>
</article>
```

The action is a native `<button>`: focusable, announced as a button,
operable with Enter and Space, and styled by the same class the design
system uses everywhere. If the whole card surface must be clickable, the
button is stretched over the card with CSS (`position: absolute; inset: 0`
on the button inside a positioned card) — the semantics stay native.

Note: corrects FE-002 — anything that responds to a click is a real `<button>` or `<a>`, keyboard-operable and focusable.
