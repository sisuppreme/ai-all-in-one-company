# Example 2 — Waiting for the root cause

## Before

```text
Timeline of a sign-in outage:
  09:12  Monitoring confirms users cannot sign in.
  09:15  Team starts diagnosing. Status page: untouched.
  10:40  Root cause found (expired identity-provider certificate).
  11:05  Fix deployed; sign-in restored.
  11:20  First and only public post: "Earlier today a certificate
         issue prevented sign-in. It has been resolved."

Customers spent two hours with a green status page and no word,
then received a summary of an incident they were never told
was happening.
```

Silence until the cause is known leaves customers to discover the outage themselves and assume the worst about everything else.

## After

```text
Timeline of the same outage:
  09:12  Monitoring confirms users cannot sign in.
  09:18  First post — State: Investigating.
         "Known: sign-in is failing for all users; signed-in
          sessions are unaffected. Not yet known: the cause.
          Next update by 09:48."
  09:47  Update — State: Identified.
         "Cause identified: an expired identity-provider
          certificate. A replacement is being deployed.
          Next update by 10:17."
  10:15  Update — State: Monitoring.
         "Sign-in is succeeding again; we are watching error
          rates before declaring resolution. Next update by 10:45."
  10:44  Resolution post (see Example 3 for its required content).
```

## Note

Corrected under CX-163 and CX-164 (BAN-CX-082): the first post goes out on confirmed impact with what is known, what is not yet known, and the next update time — the cause is communicated when it is actually identified, not before and not as a precondition.
