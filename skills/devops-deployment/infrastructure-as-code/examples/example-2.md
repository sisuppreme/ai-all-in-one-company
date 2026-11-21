# Example 2 — Drift found and back-ported

## Before

The nightly read-only plan starts reporting a difference: an extra ingress rule on the application security group that appears in no pull request. The team is busy, so the finding sits in the CI log for two weeks while everyone assumes someone else added it "temporarily." The code and the real environment quietly stop being the same thing, and the next legitimate plan buries the unexplained rule inside a larger diff where nobody notices it.

## After

The non-empty unscheduled plan fails the drift check the first night it appears. The plan diff identifies the exact rule and when it appeared; it traces to a debugging session where an engineer opened a port in the console and forgot to close it. The rule is removed through code the same day, the drift finding is closed in progress.md, and the incident is the reminder that console changes are emergencies that get back-ported or reverted — never left as silent drift.

Note: demonstrates DO-105 — a plan against live state that reports unproposed changes is a failed check, not a curiosity.
