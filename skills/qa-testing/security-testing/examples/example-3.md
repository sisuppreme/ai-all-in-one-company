# Example 3 — Password reset proven end to end

## Before

The reset test requests a password reset for a staging account, asserts the reset email arrived in the test inbox, and passes. It never follows the link — so it never notices that the reset endpoint accepts the token but writes nothing: after "resetting," the old password still logs in and the new one does not. The flow is a facade that the test certified as working.

## After

The test follows the reset link, submits a new password, and then asserts both halves of the contract: login with the old password is rejected, and login with the new password succeeds. Against the broken endpoint the test fails; after the endpoint is fixed to persist the new credential and invalidate existing sessions, the same test passes.

*Demonstrates QA-189: a reset is proven by logging in with the new password while the old one fails — the email alone is not a pass.*
