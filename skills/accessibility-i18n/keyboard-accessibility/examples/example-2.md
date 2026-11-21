# Example 2 — Focus-stranding dialog vs. managed dialog

## Before

```js
function openConfirm() {
  confirmBox.style.display = 'block';   // focus stays on the page behind it
}
function closeConfirm() {
  confirmBox.style.display = 'none';    // focus was on a button inside the
}                                       // now-hidden box: it resets to <body>
```

The dialog opens without moving focus, Tab keeps cycling through the page behind it, Esc does nothing, and on close the focused button disappears — focus resets to the top of the document, so the keyboard user must tab through the entire header and navigation again to resume the task.

## After

```js
let invoker = null;
function openConfirm(btn) {
  invoker = btn;
  confirmBox.showModal();               // native <dialog>: focus moves inside,
}                                       // Tab cycles within it, Esc closes it
confirmBox.addEventListener('close', () => {
  if (invoker) invoker.focus();        // focus returns to the invoking element
});
```

Using the native `<dialog>` element with `showModal()` gives the trap-while-open, Esc-to-close behavior built in, and the `close` handler restores focus to the "Delete item" button that opened it — the user lands exactly where they left off.

*Demonstrates AC-088 — dialogs move focus in on open, hold it while open, and return it to the invoker on close.*
