# Example 1 — Paper experiment vs. written record

## Before

The team kills an app instance during a quiet afternoon, watches the dashboard for a minute, sees nothing break, and writes up the experiment record afterward from memory: "Killed an instance; system stayed up; resilience confirmed." The record names no steady-state metric, no hypothesis, no blast radius, and no abort criteria — and no injection log is attached, so nothing proves the kill even ran.

## After

Before anyone touches the infrastructure, the record is written: steady state is successful checkouts per minute and error rate from the production monitoring queries; the hypothesis is that both hold when one of three app instances is killed; blast radius is exactly one instance; abort criteria are error rate above 2% for 3 minutes; the abort switch (stop injection, restore the instance) is test-fired first. The run executes, the injection tool's log is attached, before/during/after measurements are filed, and the verdict is recorded against them.

*Demonstrates QA-142, QA-144, and QA-152: the record, hypothesis, and measurements exist before injection, not reconstructed after it.*
