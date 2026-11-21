# Example 1 — Invented limits in a launch plan

## Before

Launch plan, hosting section: "We will host the API on Render's free tier, which gives 1,000 instance hours a month — more than enough. The database is free PostgreSQL with no expiry. CI is free and unlimited on our plan." No sources, no dates, and two of the three claims are wrong.

## After

Free-tier sheet rows, each read from the official page on the check date: Render free — 750 instance hours per workspace per month (shared across all services, not per service), checked 2026-11-21, https://render.com/docs/free. Render free PostgreSQL — expires 30 days after creation; expiry date recorded in the sheet with a reminder set before it. CI minutes recorded from the provider's own billing page with its check date; anything not yet verified is marked "placeholder — unverified," never stated as a limit.

Note: corrects DO-162 — no tier number appears in a plan without an official page URL and a check date.
