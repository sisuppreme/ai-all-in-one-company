# Example 3 — Making a tracking embed wait for consent and fail soft

## Before

A recommendations widget that also reports analytics is pasted into the
page head, where it loads for every visitor immediately and takes the
page down with it when its CDN stumbles:

```html
<head>
  <script src="https://sdk.example.com/recs.js"></script>  <!-- loads pre-consent, render-blocking -->
</head>
```

The script sets its cookies and fires its beacons before the consent
banner is even answered. When the provider has an outage, the blocking
script stalls the host page's first render, and the widget area sits
blank with no explanation.

## After

The embed loads only after consent, loads async with a timeout, and
degrades to an honest state when the provider is unreachable:

```html
<div id="recs-widget">
  <p class="embed-unavailable" hidden>
    Recommendations are unavailable right now — the rest of the page works as usual.
  </p>
</div>
```

```text
Consent → the loader runs only when the visitor's consent state
          allows tracking; before that, zero requests to the SDK's
          origins (checked by the consent-gate test).
Load    → async with a timeout; the host page renders and functions
          whether or not the SDK arrives.
Failure → on timeout or error, the widget area shows the unavailable
          message instead of a blank hole or a fake static copy.
```

Visitors who decline are never tracked, a provider outage costs the
host nothing but the widget itself, and what the page shows always
matches what the system is actually doing.

Note: corrects IN-227 — an SDK that tracks does not load, and makes no network request, before the visitor's consent state allows it.
