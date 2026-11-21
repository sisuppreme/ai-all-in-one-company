# Example 3 — A kickoff-fossil progress.md re-verified entry by entry

## Before

progress.md has not been touched since project kickoff. It reads:

"In progress: project scaffolding.
Next: pick a stack."

The repository is three releases in. The stack was picked months ago, the
scaffolding is long finished, and two features have shipped that the file
never mentions. Anyone trusting this file — a new contributor, a receiving
owner at handover — plans from a state that stopped being true at week one.

## After

Every entry is re-verified against the repository before anything new is
written:

1. "Project scaffolding" is checked against the repo: the scaffold exists,
   its setup gate result is recorded with its original completion date, and
   the entry moves to done naming the repository structure as its artifact.
2. "Pick a stack" is deleted — the decision was made long ago and lives in
   DECISIONS.md, which the entry now links instead of restating.
3. The shipped features are added as done entries, each with its gate
   result and artifact link; genuinely current work is written as in
   progress with today's date.
4. Next is rebuilt from the actual backlog, one owner per item.

The file is shorter than a fresh rewrite would have been, and every line in
it can now be checked against something real.

Note: corrects PM-152 — stale entries are re-verified against the deliverable, then corrected or deleted, never silently carried forward.
