# Example 1 — Green page, broken checkout

## Before

```text
Status page (live, unchanged since launch):
  "All systems operational"
  Sign-in: Operational · Dashboard: Operational
  API: Operational · Checkout: Operational

Reality, same 40 minutes:
  Checkout success rate near zero; monitoring alert firing;
  support has confirmed the outage with three customers.
  Nobody owns updating the status page, so it stays green.
```

The page contradicts the measured reality customers are experiencing: it claims full health during a confirmed outage, which is worse than having no status page at all.

## After

```text
Status page (14:06, six minutes after impact confirmed):
  Incident: "Checkout unavailable"
  State: Investigating
  Checkout: Major outage · Sign-in: Operational
  Dashboard: Operational · API: Operational

First post (14:06):
  "Known: customers cannot complete checkout; orders already
   placed are unaffected. Not yet known: the cause.
   Next update by 14:36."

Subscribers notified; the same status is embedded in the app
and the help center. G-CX-081 diff: displayed states match the
monitoring source for every component.
```

## Note

Corrected under CX-167 and CX-163 (BAN-CX-081): the page reflects measured reality, and the first post goes out on confirmed impact — within the operator's stated target — not when someone gets around to it.
