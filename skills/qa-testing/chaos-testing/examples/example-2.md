# Example 2 — Production-first breakage vs. graduated staging run

## Before

To "test resilience for real," an engineer severs the payment dependency directly in production during business hours, with no staging run, no scheduled window, and an abort procedure nobody has ever executed. Checkouts fail for real customers, support learns about it from complaints, and the abort takes twenty improvised minutes.

## After

The same dependency-loss experiment runs first in staging at a one-service blast radius, with the abort switch test-fired before injection and steady state measured throughout; it passes and the record is filed. Only then is a production game day scheduled in an announced low-traffic window per D18, with a named person watching the abort switch — and the run starts at the same small radius that passed in staging.

*Demonstrates QA-145, QA-146, and QA-151: abort tested first, staging before production, and customer-impacting windows scheduled and announced.*
