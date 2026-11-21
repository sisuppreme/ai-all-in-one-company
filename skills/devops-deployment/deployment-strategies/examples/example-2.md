# Example 2 — Abort-free canary given metrics gates

Demonstrates: DO-046 (abort condition named before promotion) and DO-052 (metrics-gated canary promotion).

## Before

Release plan: "Canary the new checkout service at 10% for an hour, keep an eye on the dashboard, roll back if it looks bad." No baseline is captured, no threshold exists, and "looks bad" is decided under pressure by whoever is awake.

## After

Before promotion, the plan records the baseline (error rate 0.3%, p95 latency 420 ms over the prior 24 hours) and the abort condition: error rate above 1.3% or p95 above 800 ms, sustained 5 minutes, sends all traffic back to the stable version. Steps run 5% → 25% → 50% → 100%, each held until the comparison stays inside thresholds; the abort action is the named traffic-switch command, rehearsed in staging.
