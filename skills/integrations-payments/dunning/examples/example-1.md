# Example 1 — The two silent weeks

## Before

A renewal charge declines. The provider's retry machinery runs on its
default schedule, but no failed-payment email was ever configured and the
app shows nothing — the subscription row just sits at `past_due`, visible
only in an admin panel nobody opens. Fourteen days later the retries run
out, the subscription is canceled, and the customer's first contact from
the product is a "your account has been closed" email. The card on file
had been reissued by their bank; a working update link on day one would
have recovered the account in minutes.

## After

The sequence is configured before the first failure:

1. The first decline fires a failed-payment email the same day: the
   amount, the reason in plain language, and a hosted payment-update
   link.
2. Smart retries run across the configured two-week window, spaced so
   each reminder lands near an attempt, and an in-app banner shows
   while the subscription is past due.
3. Card-updater is enabled, so when the customer's bank reissues the
   card, a retry succeeds against the new credentials without the
   customer doing anything — and contact stops at that moment.
4. Had nothing succeeded, the sequence would have ended in the one
   configured state — pause — with a closing notice saying exactly
   what that means.

Note: corrects IN-082 — the first failure notifies the customer the same day; silent retrying is banned (BAN-IN-041).
