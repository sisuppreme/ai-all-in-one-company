# Example 3 — Replacing a reusable, logged OTP with a hashed, expiring, rate-limited one

## Before

The verification flow keeps codes reusable and visible:

```text
POST /otp/send
  → code = 6-digit random, stored in plaintext on the user row
  → log.info("Sending OTP 482916 to +1 555 010 2030")
  → code valid until the next login, however long that takes

POST /otp/verify { "code": "482916" }
  → compares against the stored value; succeeds any number of times
  → no attempt limit: an attacker can guess against the endpoint all day
```

The code sits in log files, never expires, and can be replayed.

## After

The code is hashed, short-lived, single-use, and capped:

```text
POST /otp/send
  → send-cap check for the number (3 per hour) — pass
  → code = 6-digit random; store SHA-256 hash + expiry (10 minutes)
  → enqueue via provider; log records number and SID, never the code

POST /otp/verify { "code": "482916" }
  → hash the submission, compare to the stored hash
  → expired or already used → fail
  → wrong code → attempts += 1; at 5 attempts the code is locked
  → correct code → mark used, issue the session; replay now fails
```

Verification is proven by the G-IN-073 test flow: expiry, single use,
attempt lockout, and resend cap are all exercised before launch.

Note: corrects IN-147 — OTP codes are stored hashed, expire within minutes, and are invalidated on first successful use.
