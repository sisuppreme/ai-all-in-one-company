# Example 1 — Replacing "TODO: document errors" with the error catalog

## Before

The generated reference for `POST /v1/orders` documents the 201 response and stops. The errors section reads "TODO: document errors". An integrator's first failed order in production is their first sight of the error format.

## After

The operation documents each error response in the shared Problem Details format, and the human-written error catalog explains each `type`:

```text
422  https://api.example.com/problems/validation-failed
     A field failed validation; `detail` names the field and the rule.
401  https://api.example.com/problems/unauthenticated
     The credential is missing or expired; see the authentication walkthrough.
409  https://api.example.com/problems/idempotency-conflict
     The idempotency key was already used with a different payload.
```

The documentation lint (G-AR-052) now fails the build if any operation lacks an error response or the string "TODO" appears in the spec.

## Note

Corrects AR-103 (every endpoint documents its error responses in the shared Problem Details format; a shipped TODO is a blocking defect).
