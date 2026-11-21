# Example 3 — Issuing a customer API key: shown once, stored hashed

## Before

Your own API stores customer keys in plain text and re-displays them:

```text
api_keys table
  id: 41, user: 108, key: "mk_live_EXAMPLE_FULL_VALUE", created: 2026-11-01

Settings page → "Your API key" field shows the full value on every visit.
Support can read any customer's key out of the database; a database
leak is a leak of every customer's credential at once.
```

## After

The full value exists once — in the creation response — and only a hash
plus a display prefix is stored:

```text
POST /api-keys
  → generate value: mk_live_EXAMPLE_FULL_VALUE
  → store: prefix "mk_live_9f3", hash = HMAC(server_pepper, value),
           scope "read:reports", created 2026-11-21
  → respond with the full value exactly once, with a copy warning

api_keys table
  id: 41, user: 108, prefix: "mk_live_9f3", key_hash: "…", scope: "read:reports"

Authentication: hash the presented key and compare against key_hash.
Settings page → shows "mk_live_9f3…" and a Revoke button — never the value.
```

A database leak now yields hashes, not credentials, and each key revokes
individually (G-IN-105) without disturbing the customer's other keys.

Note: corrects IN-205 — keys you issue are shown once at creation and stored only as a hash plus a non-secret identifying prefix.
