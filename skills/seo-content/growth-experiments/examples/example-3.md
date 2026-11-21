# Example 3 — The variant with an unbacked promise

## Before

For a support-page experiment, variant B's headline read: "Get an answer within one hour — guaranteed." The support team was staffed for next-business-day replies, no one-hour process existed, and no policy page mentioned a guarantee. The variant was ready to launch on the argument that the test itself would show whether the promise was worth building the process for.

## After

The variant fails the pre-launch real-content pass (G-CO-133): the promise has no backing process, so it cannot be tested — an experiment never measures whether a false claim converts. The hypothesis is rewritten around a true, checkable difference: variant B states the actual service level from the fact sheet — "Every message answered by a support engineer within one business day" — with a clearer contact form as the tested change, against the control's generic "Contact us" page. The promise the team wished it could make is logged separately as an operations proposal; if the one-hour process is ever built and documented, a later registered experiment may test announcing it.

Note: corrects CO-268 (variants pass the same real-content gates as any page — no promise without a backing process, per DET-CON-028).
