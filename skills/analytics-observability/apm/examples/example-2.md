# Example 2 — The default sampler that threw away the incident

## Before

Nobody ever chose a sampling strategy, so the library default — a low fixed head-based rate — is what production runs. A rare checkout failure starts occurring: real users hit it roughly a dozen times a week, always on the same downstream call. The error rate chart shows the bump, but the sampler keeps almost none of the failing traces, and not one of the slow ones. The team spends days adding temporary logging to reproduce a failure that their own telemetry was discarding on purpose — by accident.

## After

The sampling decision is written in the repo: a stated baseline rate for routine traffic, with errors and slow outliers always kept via tail sampling at the collector, and the blind spot (most successful routine traces are dropped) named as an accepted cost. The next occurrence of the failure leaves a complete trace — the downstream span shows exactly which call stalls — and the always-kept gate (G-AN-094) proves the configuration behaves this way in staging before it is trusted in production.

Note: corrects AN-183 — sampling is a written decision with errors and slow requests always kept; the default is not a strategy (BAN-AN-093).
