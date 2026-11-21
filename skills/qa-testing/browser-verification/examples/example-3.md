# Example 3 — A route nobody clicked that was broken

## Before

The verifier manually clicks through the five pages the builder mentioned —
home, dashboard, pricing, login, checkout — and reports "all pages fine".
The release ships.

The settings page, which nobody opened, loads with a failed 500 request and
a console error, and renders its form disabled. Users find it first.

## After

The pass runs the scripted route smoke test instead (G-QA-031):

1. `npx playwright test smoke/routes.spec.ts` loads every route in the
   project's route list — 23 routes, not the 5 suggested ones (QA-071).
2. The script exits non-zero: /settings returns a 500 on its profile
   request and logs a console error; the failure is filed as a finding with
   the captured console output and response (QA-063).
3. The release is blocked until the endpoint is fixed; the re-run exits 0
   across all 23 routes, and both runs are recorded in progress.md.

Note: corrects QA-063 and QA-071 — every route is loaded, and console errors and failed requests are findings by default.
