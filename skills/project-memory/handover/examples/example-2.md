# Example 2 — Secrets pasted into handover.md, replaced by a credentials path

## Before

handover.md's "Access" section reads:

"Database: postgres://app:S3cret-Prod-Pw@db.internal:5432/app
Payments: Stripe secret key sk_live_… (full value pasted)
Server: SSH in as deploy, password on the wiki page."

The intent is helpful — the new owner can log in immediately. The effect is
that production secrets now live in a Markdown file in git history, readable
by everyone who will ever clone the repo, and un-rotatable without rewriting
history.

## After

The section is rewritten as a credentials path, and the exposed values are
rotated because they were committed:

| System | Secrets live in | Access is granted by |
|---|---|---|
| Production database | Team vault, "prod-db" entry | Vault admin adds the receiver and confirms in handover.md |
| Stripe (payments) | Stripe dashboard, team members | Account owner invites the receiver with the developer role |
| Hosting / deploy | Provider console, SSO group "deployers" | Group owner adds the receiver; deploy keys are per-person |

1. Each row names the system, where the secret lives, and the grant
   procedure — no values.
2. The secrets scan (G-PM-092) runs over the handover materials and returns
   zero matches.
3. The grants themselves are executed through those procedures, and
   handover.md records that they were completed, with dates.

The receiver ends with the same access — obtained through the path, leaving
no secret behind in the document.

Note: corrects PM-185 — handover materials name systems, secret locations, and grant procedures; secret values never appear.
