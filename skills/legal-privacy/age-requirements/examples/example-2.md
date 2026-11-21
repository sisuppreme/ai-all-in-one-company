# Example 2 — One age for the whole world

## Before

```ts
// config.ts
export const MIN_AGE = 13; // COPPA
```

One constant, chosen from the US rule the developer knew, silently governs every market the product serves. German users are admitted at 13 although Germany's GDPR Article 8 age is 16; French users at 13 although France sets 15. The help page repeats "you must be 13 or older" in every locale. Nothing in the code or copy records where 13 came from or when it was last checked.

## After

Thresholds live in the project legal file as dated, sourced configuration; code reads the row for the user's market and contains no age numbers of its own:

```markdown
## Age table (excerpt) — project legal file

| Market | Regime | Minimum age | Verification method | Source | Verified | Review |
|---|---|---|---|---|---|---|
| DE | GDPR Art. 8 (national age) | 16 | Neutral DOB screen; parental authorisation flow below threshold | GDPR Art. 8, EUR-Lex | 2026-11-21 | 2027-05-21 |
| FR | GDPR Art. 8 (national age) | 15 | Neutral DOB screen; parental authorisation flow below threshold | GDPR Art. 8, EUR-Lex | 2026-11-21 | 2027-05-21 |
| ES | GDPR Art. 8 (national age) | 14 | Neutral DOB screen; parental authorisation flow below threshold | GDPR Art. 8, EUR-Lex | 2026-11-21 | 2027-05-21 |
| GB | UK GDPR / DPA 2018 s.9 | 13 | Neutral DOB screen; parental authorisation flow below threshold | GDPR Art. 8, EUR-Lex | 2026-11-21 | 2027-05-21 |
| US | COPPA | Under 13 gated | Verifiable parental consent (FTC-accepted method) before collection | FTC Children's Privacy guidance | 2026-11-21 | 2027-05-21 |
```

The age-flow test suite (G-LG-071) runs one scripted signup per row: a 14-year-old test user is routed to the parental flow under the DE row and proceeds under the GB row — from the same build.

## Note

Corrected under LG-141: the threshold is per-market configuration in a dated, sourced table — never a hardcoded constant (the pattern banned as BAN-LG-072).
