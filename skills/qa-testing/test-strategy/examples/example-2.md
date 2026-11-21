# Example 2 — Numbered budgets replace "small and fast"

## Before

TESTING.md says: "Keep the e2e suite small and the unit suite fast." Nothing defines small or fast, so the e2e suite grows to 300 journeys and a 2-hour runtime without ever breaching the strategy, and the layer census has nothing to check against.

## After

TESTING.md states: "Unit: no count ceiling, runtime ≤ 5 min in CI. Integration: runtime ≤ 15 min. E2E: ≤ 25 journeys, runtime ≤ 20 min, each admitted per QA-205. Flake ceiling: 2% per suite." The census gate (G-QA-102) now fails the build the week a budget is breached.

Note: demonstrates QA-202 — pyramid allocation and budgets stated as numbers, not adjectives.
