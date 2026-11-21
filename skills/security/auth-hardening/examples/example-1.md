# Example 1 — Password policy rewritten to NIST 800-63B

## Before

Registration validates passwords with a composition ritual and a rotation schedule:

```text
Password rules shown to the user:
- 8–20 characters
- Must contain an uppercase letter, a digit, and a symbol
- Cannot paste into the field (paste disabled "for security")
- Password expires every 30 days and must be changed
- No screening against known-breached passwords
```

Users respond predictably: `Password1!`, then `Password2!` at the next forced rotation.

## After

```text
Password rules shown to the user:
- At least 15 characters (at least 8 if you also enable MFA)
- Up to 128 characters accepted; spaces and paste are fine — a
  password manager is welcome
- Screened against a blocklist of breached and commonly used
  passwords; a match is rejected with an explanation
- No composition rules, no scheduled expiry; change is forced
  only on evidence of compromise
```

## Note

Corrects SE-061 (length policy), SE-062 (breached-password screening), and SE-063 (no scheduled rotation) — policy per NIST SP 800-63B Rev. 4.
