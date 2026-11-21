# Example 3 — The terms that changed overnight

## Before

```markdown
## Terms of Service — Version 1.0, effective March 1

… (new section 14, inserted last night) …
14. Binding arbitration. All disputes arising from use of this service
shall be resolved by binding arbitration; you waive any right to a
court trial or class action.
```

The arbitration clause was edited into the live page in place. The version ID and effective date were left unchanged, no user was notified, and the previous text was overwritten — so the product cannot even show what the terms said before the change, let alone prove a user saw the new clause.

## After

```markdown
## Terms of Service — Version 1.1, effective 2026-12-01

What changed in v1.1: a new section 14 adds binding arbitration for
disputes. Version 1.0 remains in force until 2026-12-01 and its full
text stays in the archive.

Rollout record:
- 2026-11-21 — v1.1 published to the archive; change notice emailed to
  all account holders and shown as an in-product banner.
- On first login after 2026-12-01, each user sees the change summary
  with "I accept v1.1" / "Close my account" choices; acceptance writes
  an event row (user, terms, 1.1, timestamp, re-acceptance flow).
- Counsel review of v1.1 recorded 2026-11-20 (reviewer, date, version
  on file) before publication (G-LG-035).
```

The change is material, so it ships as a new version with a future effective date, a plain-language change notice, and a re-acceptance event per user — and v1.0's text survives in the archive for anyone whose dispute predates it.

## Note

Corrected under LG-065: a material change is published as a new version with an effective date and a change notice, and existing users re-accept before the new version binds them — a binding document is never edited silently in place.
