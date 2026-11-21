# Example 3 — Reset and privilege-change flow made real

## Before

```text
POST /reset-password { email }
→ "No account for that email" when unregistered (enumeration).
→ Otherwise emails a reset link valid for 7 days, reusable any
  number of times; old sessions stay valid after the reset.

POST /admin/grant-role { userId, isAdmin: true }
→ Trusts the isAdmin flag in the request body; no re-authentication,
  no notification to the account holder.
```

## After

```text
POST /reset-password { email }
→ Always responds: "If an account exists for that email, a reset
  link is on its way." A single-use token with a 60-minute expiry
  is stored hashed; first use expires it, invalidates all existing
  sessions, and notifies the account holder.

POST /admin/grant-role { userId, role }
→ Role is read from the server-side account record, never the
  request. The acting admin re-authenticates (password or MFA)
  before the change applies; the affected holder is notified
  out-of-band and the change is written to the auth event log.
```

## Note

Corrects SE-070 (recovery as strong as login) and SE-071 (re-authentication and notification for privilege changes); the trusted-flag pattern is banned outright by BAN-SE-033.
