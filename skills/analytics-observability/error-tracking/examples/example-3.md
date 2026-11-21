# Example 3 — The error event that carried a password

## Before

A login error is captured with the full request attached, exactly as submitted:

```js
tracker.captureException(err, {
  request: req, // headers, cookies, and parsed body included
});
```

The event stored in the tracker — a third-party system — now contains the user's submitted password in the body and a live session token in the headers, searchable by anyone with tracker access. The debugging aid became a credential leak.

## After

A before-send scrubber, configured by the denylist in the repo, strips sensitive fields from every event before transmission:

```js
tracker.init({
  beforeSend(event) {
    scrub(event, DENYLIST); // password, token, authorization, cookie, card_number, ...
    return event;
  },
});
```

The event keeps its stack, release tag, correlation ID, and non-sensitive context (route, status, error code), and the canary gate (G-AN-083) proves in staging that a request carrying `CANARY-PASSWORD-EXAMPLE` produces an event containing no trace of it.

Note: the Before violates AN-163 (context is scrubbed before it leaves); the After corrects it.
