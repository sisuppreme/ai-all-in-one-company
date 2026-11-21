# Example 3 — Orphan risk acceptance

## Before

> Risk acceptance: "Session tokens are stored in localStorage. XSS would expose them, but our CSP is strict, so the risk is accepted."
> — filed in the threat model with no owner, no date, and no expiry.

Eight months later the CSP has been loosened twice for third-party widgets, nobody remembers the acceptance exists, and the threat it closed is silently live again.

## After

> Risk acceptance RA-3 — Threat T-9 (token theft via XSS).
> Decision: session tokens stored in localStorage for the single-page app.
> Compensating controls: strict CSP (`script-src 'self'`, no inline scripts), all user content rendered through the escaping template layer, dependency pinning with weekly audit.
> Owner: auth-hardening skill owner (D7).
> Accepted: 2026-11-21. Expires: 2027-02-21 — on expiry this threat reopens and the httpOnly-cookie migration is re-evaluated against the current CSP.

*Note: corrects SE-188 (every risk acceptance names an owner and an expiry date; an undated, unowned acceptance counts as an open threat).*
