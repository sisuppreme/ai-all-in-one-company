# Example 2 — Reject in the basement

## Before

The banner's first layer offers one large button:

```html
<div class="cookie-banner">
  <p>We use cookies to improve your experience.</p>
  <button class="btn-primary btn-large">Accept all cookies</button>
  <a href="/cookie-settings">Manage settings</a>
</div>
```

Rejecting requires opening "Manage settings", finding the per-purpose toggles on the second layer, switching each one off, and saving — four interactions against the accept path's one. The design steers every hurried visitor into accept-all.

## After

Accept, reject, and granular choice sit on the same layer, at the same weight:

```html
<div class="cookie-banner">
  <p>We use cookies to improve your experience. Non-essential cookies
     stay off unless you allow them.</p>
  <button class="btn-primary">Accept all</button>
  <button class="btn-primary">Reject all</button>
  <button class="btn-primary">Choose purposes</button>
</div>
```

Each button is one click, the same size and styling, and each records its outcome as a consent event (LG-088). "Choose purposes" opens the granular layer for visitors who want it — it is no longer the only road to "no."

*Violates/corrects LG-084 (symmetric first layer); see also BAN-LG-042.*
