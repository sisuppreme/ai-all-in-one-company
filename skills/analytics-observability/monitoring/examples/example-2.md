# Example 2 — The 180 ms average hiding a 4.2-second tail

## Before

The service dashboard leads with a single panel: "Average response time: 180 ms", computed across all endpoints and all responses for the last 24 hours. The number looks healthy in every review. Meanwhile the checkout endpoint's slowest 1% of requests take over 4 seconds — a payment-gateway call with no timeout, failing slowly — and error responses take longer still, but both effects vanish into the mean, diluted by thousands of fast static-page hits. Support tickets about "the payment page hanging" are closed as user connection problems.

## After

The panel is replaced by latency percentile bands — p50, p95, p99 — charted per endpoint, with success latency and error latency as separate series. The checkout p99 of 4.2 s is immediately visible, the error-latency series shows the failing gateway calls taking the full timeout, and the latency SLI (share of responses under the stated threshold) is computed from the same histogram. The fix (a timeout plus a circuit breaker on the gateway call) is verified by watching the p99 fall, not by a slightly smaller average.

Note: corrects AN-104 — latency is percentiles with success and error series separated; the average hid exactly the tail users felt (BAN-AN-052).
