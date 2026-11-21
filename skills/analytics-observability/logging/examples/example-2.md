# Example 2 — The login handler that logged passwords

## Before

A login handler logs the whole submitted object "to help debugging":

```js
logger.info("login attempt", { form: req.body });
// stores: {"email":"user@example.com","password":"<the user's actual password>"}
```

Every login writes the user's password into the log store in searchable plain text, where it is retained, backed up, and visible to anyone with log access. The developer meant no harm; the logger let it happen.

## After

The logger's denylist redacts credential fields before any line is written, and the handler logs identifiers and outcomes instead of values:

```js
logger.info("login_attempt", { trace_id, request_id, user_id, outcome: "success" });
logger.warn("login_attempt", { trace_id, request_id, user_id, outcome: "bad_password", attempts: 3 });
// denylist in logger config: password, token, authorization, session_id, card_number → "[REDACTED]"
```

The canary gate (G-AN-042) proves it: a staging login with `CANARY-PASSWORD-EXAMPLE` returns zero hits when the store is searched for that string.

Note: the Before violates AN-085 (secrets and personal data are never logged); the After corrects it.
