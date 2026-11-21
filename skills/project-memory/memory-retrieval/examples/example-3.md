# Example 3 — The template's retrieval test

## Before

The project's retrieval gate runs the query list that shipped with its template:

| Query | Expected file |
|---|---|
| "which framework" | stack.md |
| "how to run locally" | README.md |
| "coding conventions" | CONTRIBUTING.md |

All three pass. The gate is green — but it only proves the template's facts are findable. The questions this project's newcomers actually ask — which database, what is the current release, who is paged when payments fail — are never tested. Two of them, it turns out, cannot be answered from the repo at all: the escalation path lives only in a chat thread. The gate tested the template, not the project, and certified a memory that does not work.

## After

The project maintains its own `retrieval-queries.md`, written from the questions its newcomers and on-call engineers really ask, each naming its canonical file:

| # | Question | Search term | Canonical file |
|---|---|---|---|
| 1 | Which database and version do we run? | PostgreSQL | stack.md |
| 2 | What is the current released version? | version | CHANGELOG.md |
| 3 | Who is paged when payments fail, and how? | escalation | docs/runbook.md |
| 4 | How is a production deploy performed? | deploy | docs/deployment.md |
| 5 | Why was the queue replaced last spring? | queue | DECISIONS.md |
| … | (at least 10 rows, extended as new fact classes appear) | | |

The scripted search runs this list: every query must return its named canonical file. Row 3 initially fails — the escalation path is not in the runbook — which is the gate doing its job: the fact is written into its canonical home, and the test passes on the project's real memory, not the template's.

Note: corrects PM-169 — the scripted known-fact search runs the project's own query list, maintained as a required project artifact.
