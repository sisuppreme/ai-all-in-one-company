# Example 1 — The purpose with no lawful basis

## Before

```markdown
## Obligations register (excerpt)

| Market | Processing | Notes |
|---|---|---|
| EU | Product analytics events | "Standard analytics, everyone does this" |
| EU | Email marketing | Covered by the privacy policy |
```

Analytics ships on the strength of "everyone does this" and marketing is waved through because a policy mentions it. No lawful basis is recorded for either purpose, so there is nothing to test the consent flow or the notice against.

## After

```markdown
## Obligations register (excerpt)

| Market | Regime | Purpose | Lawful basis | Requirement | Owner | Verified | Review |
|---|---|---|---|---|---|---|---|
| EU | GDPR | Product analytics events | Consent (Art. 6(1)(a)) | No analytics fires before consent; consent event recorded with banner version | D14 | 2026-11-21 | 2027-05-21 |
| EU | GDPR | Email marketing | Consent (Art. 6(1)(a)) | Separate opt-in at signup; withdrawal in one click, honored before next send | D14 | 2026-11-21 | 2027-05-21 |
| EU | GDPR | Contract performance data (account, billing) | Contract (Art. 6(1)(b)) | Collected only for account operation; retention per schedule row R-04 | D14 | 2026-11-21 | 2027-05-21 |
```

Each purpose carries its own basis, the requirement it creates, and an owner; the coverage check (G-LG-001) can now fail the build if a purpose appears without one.

## Note

Corrected under LG-003: a lawful basis is assigned per processing purpose, recorded before build — never inferred from "standard practice" or from a policy merely mentioning the activity.
