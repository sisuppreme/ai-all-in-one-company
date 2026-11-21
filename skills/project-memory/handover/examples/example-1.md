# Example 1 — A link-and-cheer transfer corrected to a recorded acceptance

## Before

The giver's final message on the project channel reads:

"Repo's all yours — everything's in there. Good luck! 🚀"

There is no handover.md. Nobody has been named as the receiver, no
walkthrough happened, and nothing records a transfer. Three weeks later the
site goes down at night; the person who happens to be on call has never
agreed to own the project, does not know a runbook exists, and cannot tell
whether the giver still considers it theirs.

## After

The transfer is re-run as a handover:

1. A receiving owner is named — a person, in a stated role — and agrees to
   take the project on.
2. handover.md is created from the project's records: mandated-file
   manifest, landmines list, credentials path, and the runbooks,
   postmortems, and DECISIONS.md listed as transferred items.
3. The giver walks the receiver through the architecture and the known
   failure modes; the walkthrough's date and participants are recorded.
4. The receiver performs the cold run unaided: deploys the project, finds
   the runbook for a named incident class, names the top open risks, and
   states who accepted the transfer and when.
5. handover.md closes with the acceptance block: accepting owner, role,
   ISO 8601 date, and the scope accepted. progress.md records the gate
   results and marks the transfer complete.

The difference is not the paperwork — it is that ownership now has a name, a
date, and a test the receiver actually passed.

Note: corrects PM-183 — acceptance is recorded in handover.md with the accepting owner, a date, and the scope accepted.
