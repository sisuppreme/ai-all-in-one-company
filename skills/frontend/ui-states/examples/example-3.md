# Example 3 — Hover-only card actions made reachable

## Before

```css
.card .actions { opacity: 0; }
.card:hover .actions { opacity: 1; }
```

```html
<article class="card">
  <h3>Q3 launch plan</h3>
  <div class="actions">
    <button>Edit</button>
    <button>Delete</button>
  </div>
</article>
```

Edit and Delete exist only while a mouse hovers. On touch there is no hover;
by keyboard the buttons are focusable but invisible until focused by luck —
in practice, unreachable for both groups.

## After

```css
.card .actions { opacity: 1; }
@media (hover: hover) {
  .card .actions { opacity: 0.55; }
  .card:hover .actions,
  .card:focus-within .actions { opacity: 1; }
}
```

The actions are always visible at reduced emphasis; hover or keyboard focus
on the card raises them to full emphasis. The enhancement still rewards the
mouse, but touch users see the buttons and keyboard users reveal them by
focusing the card or tabbing to the buttons themselves.

Note: corrects FE-165 — hover enhances but never gates; every reveal has a tap and keyboard-focus equivalent.
