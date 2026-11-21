# Example 1 — "For scale" becomes a forcing-requirement test

## Before

Proposal: "Split the app into microservices with a saga for checkout, so it
can scale." Current load: 40 orders a day, one developer, one server at 5%
CPU. No bottleneck is named; the split multiplies deploy and debugging cost
immediately and buys nothing measurable.

## After

ADR records the test instead: the modular monolith stays. The forcing
requirement is written down in advance — "if sustained checkout traffic
exceeds 500 orders/hour or the payments team needs an independent deploy
cadence, revisit service extraction for payments only." The decision is
revisitable because its trigger is a number, not a mood.

Note: corrects AR-162 and AR-169 — no pattern without a stated problem, and the modular monolith is the default composition until a requirement forces distribution.
