# Example 1 — Replacing the bare "user" with a named persona

## Before

"As a user, I want to export reports, so that I can share them."

Which user? Dispatchers export month-end totals; drivers must never see other
drivers' earnings. The bare role hides a permission rule that will be decided
silently at build time.

## After

"As a dispatch lead, I want to export the currently filtered order list as
CSV, so that I can send month-end totals to finance without re-typing them."

The role is the persona from the set (dispatch lead, v1.0), the capability is
specific, and the benefit is the persona's own outcome. The permission rule
(only this role exports) is now visible for acceptance-criteria to test.

Note: corrects PR-082 — the role is a named persona; bare "user" is allowed only when every segment is served identically, with the reason stated.
