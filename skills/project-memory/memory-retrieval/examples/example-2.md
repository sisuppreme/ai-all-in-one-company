# Example 2 — The deployment guide that vanished

## Before

The project replaces its deployment process. The author writes `docs/deployment.md` with the new procedure and deletes the old `docs/deploy-guide.md` in the same commit, "to avoid confusion."

A month later, a contractor finds the old guide in a downloaded archive of the repo and follows it: it points at a decommissioned server and a credentials path that no longer exists. Nothing in the file says it is stale, and nothing in the current repo mentions it ever existed. The deletion removed the only evidence that the old procedure was replaced — and why.

## After

The old guide stays in the repo, clearly marked, and the new guide takes over as the canonical home:

`docs/deploy-guide.md` now opens with:

> **SUPERSEDED — 2026-11-21.** This procedure is no longer used. Use [deployment.md](deployment.md) instead. Kept for history; do not follow these steps.

The docs index links `deployment.md` as the current procedure and lists `deploy-guide.md` under "Superseded documents." Anyone who finds the old file — in the repo, an archive, or a search result — can see in one line that it is old and where its replacement lives.

Note: corrects PM-166 — superseded documents are marked and linked to their replacement, never silently deleted.
