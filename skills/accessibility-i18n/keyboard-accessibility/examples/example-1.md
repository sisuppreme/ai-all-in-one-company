# Example 1 — Clickable div card vs. native button

## Before

```html
<div class="plan-card" onclick="selectPlan('pro')">
  <h3>Pro plan</h3>
  <p>$12 / month</p>
  <span class="fake-button">Choose Pro</span>
</div>
```

The card looks interactive and works with a mouse, but it has no role, no accessible name as a control, and no keyboard path: Tab skips straight past it, Enter and Space do nothing, and the primary conversion action of the page is unreachable for keyboard users.

## After

```html
<article class="plan-card">
  <h3>Pro plan</h3>
  <p>$12 / month</p>
  <button type="button" onclick="selectPlan('pro')">Choose Pro</button>
</article>
```

The card is now static content, and the action is a native `<button>`: it is in the Tab order automatically, activates with Enter and Space, exposes its name and role to assistive technology, and shows the standard focus indicator — no custom key handling needed.

*Demonstrates AC-081 / AC-082 — native interactive elements first; everything operable by pointer is operable by keyboard alone.*
