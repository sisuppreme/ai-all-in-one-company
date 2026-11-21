# Example 3 — Analytics firing before the consent answer

## Before

The analytics snippet is inlined in the page head:

```html
<head>
  <script src="https://analytics.example.com/tracker.js"></script>
  <script>tracker.pageview();</script>
  <!-- consent banner renders later, in the body -->
</head>
```

Every visitor — including those who press "Reject" — has already sent a pageview with a persistent identifier. The privacy notice states that analytics runs only with consent.

## After

The tracker initializes only after consent resolves, and the consent state is recorded:

```js
onConsentResolved((state) => {
  recordConsentState(state);            // stored with the session record
  if (state.analytics === 'granted') {
    tracker.init({ anonymousId: getAnonymousId() });
    tracker.pageview();
  }
  // denied: no tracker load, no requests, nothing queued to send later
});
```

A fresh consent-denied session is then exercised with the network log open: zero analytics requests (gate G-AN-002).

Note: the Before violates AN-004 (consent before collection); the After corrects it.
