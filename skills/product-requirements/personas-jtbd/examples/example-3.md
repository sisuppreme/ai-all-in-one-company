# Example 3 — Forces of progress before a feature proposal

## Before

Proposal: "Dispatchers need automated rebalancing — one click and late orders
redistribute themselves. Build it."

The proposal jumps from persona to feature. It never asks why dispatchers
still rebalance by hand, so it cannot know what would stop them adopting the
automation.

## After

Forces for the dispatch-lead job (from F-09, F-11, F-14):

- Push: month-end rebalancing by spreadsheet took about an hour and still
  produced totals finance rejected.
- Pull: a single late-orders view promises the rebalance decision in minutes.
- Anxiety: an automated change the dispatcher cannot inspect or undo could
  send the wrong driver across town; participants said they would not trust
  it on day one.
- Habit: the spreadsheet export is a known ritual; it works, slowly, every
  time.

Proposal after forces: build the late-orders view first, with any automated
rebalancing arriving later as a preview the dispatcher approves or discards —
the anxiety force, not the feature list, set the order.

Note: corrects PR-046 — push, pull, anxiety, and habit are analyzed before any feature is proposed from a persona.
