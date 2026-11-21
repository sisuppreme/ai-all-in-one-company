# Example 3 — The field collected just in case

## Before

```markdown
## Signup form fields

- Email, password
- Full name
- Date of birth        ("might need it later")
- Phone number         ("for future 2FA, maybe")

## Privacy notice (excerpt)

"We take data minimisation seriously and only collect what we need."
```

Two fields have no purpose in the register — they are collected on speculation. The notice sentence claims the opposite of what the form does, so the product now holds extra personal data, extra breach exposure, and a published statement its own schema contradicts.

## After

```markdown
## Signup form fields

- Email, password
- Full name

## Register change (2026-11-21)

- Date of birth: removed from form and schema. No registered purpose.
  If age-gating is ever required, the age-requirements skill adds a
  threshold determination flow; a full date of birth is not the default.
- Phone number: removed. 2FA is not a shipped feature; when it ships,
  the field enters with its purpose and retention row first (LG-012).
```

The data map, the form, and the notice now agree, and the completeness check (G-LG-002) passes because every remaining field maps to a purpose.

## Note

Corrected under LG-005: minimisation is enforced at the form and schema level — a field with no registered purpose is removed, not policy-washed by a reassuring sentence in the notice.
