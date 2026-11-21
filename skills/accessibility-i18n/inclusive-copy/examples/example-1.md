# Example 1 — Context-free links and buttons rewritten to stand alone

## Before

```html
<nav aria-label="Account">
  <a href="/invoices">Click here</a>
  <a href="/plan">Learn more</a>
  <a href="/security">Click here</a>
</nav>
<button>OK</button>
```

A screen-reader user pulling up the link list hears "click here, learn more, click here" — three entries, no destinations. A voice-control user cannot say any of them with confidence, because two are identical. The "OK" button confirms something the user has to re-read the dialog to identify.

## After

```html
<nav aria-label="Account">
  <a href="/invoices">Download invoices</a>
  <a href="/plan">Compare plans and prices</a>
  <a href="/security">Change password and sign-in settings</a>
</nav>
<button>Delete project</button>
```

Each text names its destination or action, so the link list is a usable table of contents on its own, the spoken label matches the visible label (WCAG 2.5.3), and the confirm button repeats the destructive action it performs.

Note: corrects AC-183 — link and button text stands alone, naming the destination or action out of context.
