# Example 3 — A matrix that decided nothing

## Before

The competitive analysis ends with the matrix itself: 24 capability rows across four products, all cells evidenced. It was presented in one meeting, filed, and never opened again. The next quarter's roadmap was assembled from stakeholder requests, and two features were built that the matrix had already shown to be table stakes with no differentiation value — while the one verified gap (offline mode, present in no competitor) was never discussed.

## After

The same analysis closes with a decisions section:

```markdown
## Decisions (2026-11-12, product lead)

1. BUILD: Offline mode for the field app. Basis: matrix rows "Offline
   editing" and "Sync on reconnect" — absent in all three competitors
   trialed (cells verified 2026-11-10/11); our support tickets cite
   connectivity loss 31 times in Q3. → feeds roadmapping, Next horizon.
2. SKIP: Built-in chat. Basis: row "In-app chat" — present in all three
   competitors with low task-test usage scores; table stakes we can meet
   later via integration. Revisit at the 2027-02-10 refresh.
3. POSITION AGAINST: TaskPilot on guest access. Basis: row "Guest
   access" — TaskPilot charges guests as seats (trial checkout,
   2026-11-11); our guests are free. Claim approved for copy with the
   comparison set named.
```

## Note

Corrected under PR-167: analysis ends in recorded decisions — build / skip / position against — each citing the matrix cells it rests on (PR-170). A matrix with no decisions is unfinished.
