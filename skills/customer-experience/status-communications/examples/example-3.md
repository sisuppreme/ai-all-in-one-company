# Example 3 — "Issue fixed," nothing more

## Before

```text
Resolution post, closing a major incident:
  "The issue has been fixed. Everything is back to normal.
   The outage was caused by a brief server glitch.
   We apologize for the inconvenience."

No affected components named. No duration. And the "server
glitch" was never established — the real cause was found two
days later and was something else entirely.
The incident entry flips to Resolved and the page returns
to all-green, as if the outage never happened.
```

A resolution post with no cause and no duration erases the incident: customers cannot tell what was affected, how long it lasted, or whether it will happen again.

## After

```text
Resolution post:
  "Resolved — Sign-in and API.
   Duration: 09:12–10:44 (1 hour 32 minutes from first
   confirmed impact to verified recovery).
   Cause: the identity-provider certificate used for sign-in
   expired, which also broke API token validation.
   Dashboard and Checkout were not affected.
   Postmortem: [link] — published 3 days later, covering the
   timeline, why the expiry was missed, and the new automated
   certificate-expiry alert now in place."

G-CX-084 audit: resolution states components and duration;
major incident has a linked postmortem inside the stated window.
```

## Note

Corrected under CX-170 and CX-171 (BAN-CX-083): the resolution states affected components, honest duration, and the cause at the level actually established — and a major incident closes only with its postmortem published and linked, not with a bare "fixed."
