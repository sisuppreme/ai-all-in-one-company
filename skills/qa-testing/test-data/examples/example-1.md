# Example 1 — Factory data instead of a production copy

## Before

The checkout test suite runs against a staging database restored nightly from the production backup, because "real data catches real bugs." Tests read whichever customer rows happen to exist, two tests update the same popular account, and the suite passes or fails depending on what real customers did that day. Real names, emails, and order histories sit in staging and in CI logs.

## After

The suite builds its own database from migrations and creates every record it needs through factories: `create(:user)`, `create(:order, user: user, items: 3)`. Volumes and shapes mirror production (a 10,000-row fixture set exists for the pagination tests), but every person is invented and every address is on `example.com`. The suite passes in any order, and staging holds no production rows at all.

Note: corrects QA-241 (manufactured, never harvested) and QA-248 (no production data in test environments).
