# Example 2 — Silent save toast vs. polite live region

## Before

```js
saveProfile(data).then(() => {
  toast.style.background = '#1a7f37';
  toast.textContent = 'Saved';
  toast.classList.add('show');      // visible for 3 seconds, then fades
  setTimeout(() => toast.classList.remove('show'), 3000);
});
```

```html
<div id="toast" class="toast"></div>
```

The confirmation exists only as a visual event. A screen-reader user who clicks "Save profile" hears nothing, gets no confirmation the save happened, and may submit again or abandon the task unsure.

## After

```html
<div id="toast" class="toast" role="status" aria-live="polite"></div>
```

```js
saveProfile(data).then(() => {
  toast.textContent = 'Profile saved.';   // announced by the live region; focus stays on the button
}).catch(() => {
  errorRegion.textContent = 'Profile could not be saved. Check your connection and try again.';
});
```

`role="status"` makes the container a polite live region: the confirmation is announced without moving focus, and a failure is announced as an error message that says what happened and what to do — not silence, and not a color change.

*Demonstrates AC-047 — dynamic changes are announced by live regions, politely by default.*
