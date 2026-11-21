# Example 3 — Fixture graph vs. measured steady state

## Before

The experiment record's "steady state" section is a tidy latency graph copied from a template — flat, plausible, and identical across every run. During the actual dependency-loss injection the real p95 latency triples, but the record's fixture graph never moves, so the experiment is signed off as "steady state held."

## After

The record names the steady-state metrics and the exact monitoring queries that measure them (p95 latency, error rate, successful checkouts per minute). Readings are pulled from those queries before, during, and after injection and filed with the run. When latency deviates past the pre-set abort criteria, the run aborts, the hypothesis is recorded as disproven, and a defect with an owner is filed the same day.

*Demonstrates QA-141 and QA-147, and corrects BAN-QA-072: steady state is measured from the real monitoring pipeline, never drawn from a fixture.*
