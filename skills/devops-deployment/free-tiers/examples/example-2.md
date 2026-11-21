# Example 2 — Sleeping tier chosen for a production API

## Before

The production API — including the payment provider's webhook endpoint and a nightly scheduled job — is deployed on a free web service tier. The tier spins down after 15 minutes without inbound traffic and takes about a minute to spin back up, so overnight webhooks time out, the scheduled job fires late or not at all, and the first user each morning waits on a cold start.

## After

The free sleeping tier hosts only the public demo and the staging preview, where a cold start is harmless. Production runs on an always-on tier named in the free-tier sheet as the first paid step, with its trigger recorded in advance ("first paying customer"). The sheet's sleep/expiry field for the free tier reads "spins down after 15 idle minutes — validation use only," so the constraint is visible to anyone planning from it.

Note: corrects DO-166 — sleeping tiers host demos and validation, never services with real users, webhooks, or scheduled jobs.
