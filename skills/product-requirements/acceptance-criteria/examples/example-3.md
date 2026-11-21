# Example 3 — Rewriting an imperative scenario declaratively

## Before

Scenario: User resets password
  Given I am on the login page
  When I click "Forgot password", type my email in the second input field,
  and press the blue submit button
  Then I see a green toast in the top-right corner.

A redesign that moves the link or restyles the button breaks this scenario
even though the password-reset rule never changed.

## After

Scenario: Password reset is offered for a registered email
  Given an account exists for the email
  When the account holder requests a password reset
  Then a reset link is sent to that email,
  and the requester is told to check their inbox,
  and the link expires after 60 minutes.

Scenario: No account is revealed for an unknown email
  Given no account exists for the email
  When a password reset is requested for it
  Then the requester sees the same "check your inbox" message,
  and no email is sent.

The scenarios now state the rules — including the security rule — and survive
any redesign of the page.

Note: corrects PR-105 — scenarios describe behavior and rules, not UI mechanics.
