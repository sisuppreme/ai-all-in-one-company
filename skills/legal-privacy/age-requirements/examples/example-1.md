# Example 1 — The checkbox that gated nothing

## Before

A drawing app aimed at children adds an age step to signup:

```text
[✓] I confirm I am 13 or older        [ Continue ]
```

The box renders pre-ticked. Unchecking it and continuing still creates the account; checking it creates the account; the answer is never stored anywhere. A 9-year-old who can read the sentence — or who simply taps the only button on the screen — is in, and the product holds no record that a gate ever existed. The privacy notice nevertheless states "users must be 13 or older."

## After

The same signup, rebuilt:

```text
Before any account fields are shown:

  When were you born?  [ DD ] / [ MM ] / [ YYYY ]     [ Continue ]

- No default or pre-filled value; the determination is computed server-side
  against the market row for the user's market (regime, threshold, method).
- Under threshold → the signup stops here and offers the parental-consent
  flow (method per the market row) or a clear refusal where no consent
  path exists. Changing the date after a failed determination is locked
  for the session and the attempt is logged.
- Stored on the account: determination = under/over threshold, market row
  used, date of determination. The raw date of birth is not retained.
```

## Note

Corrected under LG-142 and LG-143: the gate runs before any personal data is collected, and the screen is neutral — it asks for a date and computes an answer instead of inviting a self-declaration that nothing checks and nothing records (the cosmetic gate banned as BAN-LG-071).
