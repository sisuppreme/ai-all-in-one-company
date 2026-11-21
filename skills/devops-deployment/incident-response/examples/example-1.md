# Example 1 — Declaring and commanding an incident

## Before

Checkout errors spike at 14:05. Three engineers pile into a chat channel: one restarts servers, another starts reverting a config change "just in case," a third answers angry user emails with a personal theory of the cause. Nobody declares anything, nobody knows who is deciding, and at 15:00 two different fixes collide and extend the outage.

## After

The on-call primary declares SEV-1 at 14:07 under the written severity definitions and takes the Incident Commander role. The IC assigns one responder to mitigation, one scribe to the timeline, and a liaison to status updates every 15 minutes — and fixes nothing personally. Responders act only on IC assignments, so no two fixes collide, and the channel has exactly one source of truth.

Note: Demonstrates DO-282 and DO-283 — severity and declaration rights defined in advance, and exactly one Incident Commander who coordinates instead of fixing.
