# Example 2 — "By using this site you agree"

## Before

```markdown
<!-- footer of every page -->
By using this site you agree to our Terms of Service and Privacy Policy.
Terms last updated: March 1.
```

That sentence is the entire acceptance system. No record exists of which user accepted which version, or when; the "last updated" date is edited by hand and has survived three substantive changes to the terms. In a dispute, the product cannot show what any given user agreed to.

## After

```markdown
## Signup flow and acceptance store

Signup step 3 shows: "I agree to the Terms of Service (v1.4) and the
Privacy Policy (v2.3)" with an unticked checkbox and links to both
documents. Submitting writes one row per document:

| user_id | document | version | accepted_at (UTC) | mechanism |
|---|---|---|---|---|
| u_88112 | terms | 1.4 | 2026-11-21T09:14:03Z | signup checkbox |
| u_88112 | privacy-notice | 2.3 | 2026-11-21T09:14:03Z | signup checkbox |

Full text of terms v1.4 and privacy notice v2.3 is archived at
publication (LG-063). The footer sentence is removed; the acceptance
test (G-LG-033) creates a staging account and asserts these rows exist.
```

Acceptance is now evidence: the exact version each user accepted, the moment, and the mechanism are stored, and the archived text behind each version can be produced on demand.

## Note

Corrected under LG-064: acceptance is a stored event — user, document version, timestamp, mechanism — never a sentence claiming agreement happened.
