# Example 2 — Raw error replaced by plain language with retry

## Before

```html
<div class="panel">
  <p>Error 500: NullReferenceException at OrdersController.cs:118
     (stack: GetOrders → Authorize → …)</p>
</div>
```

The user learns the framework, a file name, and a line number — and nothing
about what happened to their orders or what to do next.

## After

```html
<div class="error-state" role="alert">
  <h2>We couldn't load your orders</h2>
  <p>Something went wrong on our side. Your orders are safe —
     this is a loading problem, not a problem with your account.</p>
  <button class="btn-primary" data-action="retry-load">
    Try again
  </button>
  <p class="error-state-alt">
    Still failing? <a href="/support">Contact support</a> and mention
    reference <code>req-8f3ka</code>.
  </p>
</div>
```

The copy names the problem in the user's terms, reassures where reassurance is
true, and gives two next steps: retry, then support with a reference the user
can quote. The exception detail goes to the error log, where it belongs.

Note: corrects FE-163 — error copy names the problem and the next step; raw codes and stack text never reach the UI.
