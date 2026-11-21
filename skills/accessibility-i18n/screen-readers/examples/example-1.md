# Example 1 — Div tab bar vs. native buttons with names

## Before

```html
<div class="tabs">
  <div class="tab active" onclick="showPanel(1)">Profile</div>
  <div class="tab" onclick="showPanel(2)">Billing</div>
  <div class="tab" onclick="showPanel(3)"><img src="gear.png"></div>
</div>
```

Keyboard focus never reaches any "tab", a screen reader announces nothing for them, and the third control is an unlabeled image. With a mouse it looks like a tab bar; to assistive technology it does not exist.

## After

```html
<div class="tabs">
  <button type="button" class="tab" aria-pressed="true" onclick="showPanel(1)">Profile</button>
  <button type="button" class="tab" aria-pressed="false" onclick="showPanel(2)">Billing</button>
  <button type="button" class="tab" aria-pressed="false" aria-label="Settings" onclick="showPanel(3)">
    <img src="gear.png" alt="">
  </button>
</div>
```

Native `<button>` elements bring focusability, keyboard activation, and the button role for free; each has an accessible name ("Profile", "Billing", "Settings"), the pressed state is programmatic, and the decorative gear icon is skipped with `alt=""`. (A true tab interface with panels would implement the full APG tabs pattern instead.)

*Demonstrates AC-041 — native semantics first; ARIA only where native HTML cannot express the widget.*
