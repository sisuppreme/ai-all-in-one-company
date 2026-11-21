# Example 2 — The snippet that measured nothing

## Before

At launch, a GA4 snippet is pasted into the site template and the checklist
marks "analytics: done". Nobody writes a tracking-plan entry, nobody marks
the signup conversion, and nobody opens DebugView. For three months the
team reports pageviews from the realtime view and assumes conversions are
"in there somewhere". When a landing-page decision finally needs the signup
number, the property shows zero conversions — the event never fired under
any name.

## After

The shared tracking plan gains an entry for every tag and event the team
relies on, with the signup event's name and parameters taken from D12's
taxonomy. A G-CO-122 debug session walks the flow in a fresh profile:
nothing collects before consent, consent is granted, the signup completes,
and DebugView shows the conversion event firing exactly once under its plan
name. Only then does reporting resume — and the launch checklist's
"analytics done" claim is re-earned instead of assumed.

Note: corrects CO-244 — a pasted snippet proves nothing; configuration is verified by observing events fire in a debug session, and claiming otherwise fails BAN-CO-122.
