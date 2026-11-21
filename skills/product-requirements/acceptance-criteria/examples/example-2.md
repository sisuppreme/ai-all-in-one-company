# Example 2 — Boundary and failure scenarios for a seat limit

## Before

Business rule in the story: "A workspace includes 5 seats."

Scenario set: one scenario — a workspace with 4 seats used invites a fifth
member successfully.

The boundary and the refusal were never specified, so the code decided them:
in the first build, the sixth invite also succeeded, and billing never knew.

## After

Scenario: Last seat can be filled
  Given a workspace with 4 of 5 seats used
  When the owner invites a new member
  Then the invitation is sent and the seat count shows 5 of 5.

Scenario: Sixth seat is refused
  Given a workspace with 5 of 5 seats used
  When the owner invites a new member
  Then the invitation is not sent,
  and the owner sees a message stating the plan limit of 5 seats
  and the upgrade option.

Scenario: Duplicate invite does not consume a seat
  Given a workspace with 4 of 5 seats used
  When the owner invites an email that already holds a seat
  Then no new seat is consumed and the owner is told the person is already a
  member.

Note: corrects PR-104 — every business rule gets scenarios for its boundary and failure cases, not only its happy path.
