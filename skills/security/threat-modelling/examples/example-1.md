# Example 1 — No model, then a model

## Before

> Feature: "Password reset by email link." Implementation starts Monday. Design note in the ticket: "Standard reset flow, same as every site. Security: link expires eventually, probably 24h. No threat model — it's a solved problem."

No diagram, no enumerated threats, no abuse cases. The shipped flow accepts reset requests for any email without rate limiting (account enumeration and inbox flooding), tokens never expire server-side, and a used token stays valid for replay.

## After

> `docs/threat-models/password-reset.md` — Last reviewed: 2026-11-21.
> Assets: account credentials; reset tokens (store: `password_resets`).
> Crossings:
>
> | Crossing | Threat | Control |
> |---|---|---|
> | C1: anonymous user → reset request endpoint | T1 (Spoofing/Info disclosure): enumeration reveals which emails have accounts | Identical response text and timing for known and unknown emails; rate limit per IP and per email |
> | C2: email link → token redemption | T2 (Tampering/Replay): token reused after a successful reset | Token is single-use, hashed at rest, expires in 30 minutes; redemption invalidates all sessions |
> | C3: anonymous user → reset request endpoint | T3 (Denial of service): flooding a victim's inbox | Max 3 reset emails per account per hour; CAPTCHA after the second request |
>
> Dispositions: T1 control + test `reset_response_is_uniform`; T2 control + test `reset_token_single_use`; T3 control. ASVS selected: V2 authentication, V3 session management.

*Note: corrects SE-181 (model written before build) and SE-185 (every trust-boundary crossing carries a named threat and a named control).*
