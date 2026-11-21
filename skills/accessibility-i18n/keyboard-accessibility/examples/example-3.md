# Example 3 — Positive tabindex and removed outline vs. DOM order and visible focus

## Before

```css
*:focus { outline: none; }              /* "cleaner look" */
```

```html
<button tabindex="3">Help</button>
<button tabindex="1">Save</button>
<button tabindex="2">Cancel</button>
```

Two defects compound: the global CSS removes every focus indicator, so keyboard users cannot see where they are; and the positive `tabindex` values hijack the Tab order, so focus jumps Save → Cancel → Help regardless of the layout — and every element without a positive value tabs only after all of them, scrambling the order further on every page that copies the pattern.

## After

```css
:focus-visible {
  outline: 3px solid #1a73e8;
  outline-offset: 2px;
}
```

```html
<button type="submit">Save</button>
<button type="button">Cancel</button>
<button type="button">Help</button>
```

No `tabindex` attributes at all: the DOM is ordered Save, Cancel, Help to match the visual and logical order, Tab follows it naturally, and `:focus-visible` draws a thick, high-contrast indicator on whichever element holds keyboard focus.

*Demonstrates AC-084 / AC-085 — focus order comes from DOM order with positive tabindex forbidden, and the focus indicator is always visible.*
