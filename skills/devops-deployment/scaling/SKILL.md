# scaling

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://sre.google/sre-book/monitoring-distributed-systems/
- **Depends on:** containers, kubernetes
- **Feeds into:** reliability, cloud-costs

## When to use / Do NOT use

- **Use when:** a production workload needs defined scaling behavior — resource sizing, autoscaling, saturation alerting, or a documented capacity ceiling — before a launch, a traffic event, or in response to observed saturation.
- **Do NOT use when:** the service has no production traffic yet and no launch is scheduled — record the single-instance ceiling under the hosting or servers-vps skill and revisit at launch; speculative autoscaling for an unused service is ceremony, not capacity.

## Rules

1. **DO-241 — Scale from measurements, not forecasts.** Every scaling decision cites a golden-signal measurement (latency, traffic, errors, saturation) from the monitoring dashboards; a change justified only by an expected traffic guess is not approved.
2. **DO-242 — Requests and limits on every workload.** Every production container declares CPU and memory requests and limits, sized from observed p95 usage in staging or production metrics, never copied from a tutorial or left unset.
3. **DO-243 — Saturation alerts fire before exhaustion.** Alerts exist for each resource that can saturate the service — CPU, memory, disk, connection pools, queue depth — with thresholds set below the exhaustion point, so the page arrives while headroom remains.
4. **DO-244 — Stateless tiers scale horizontally.** Stateless workloads scale by adding replicas behind a load balancer or an autoscaler (HPA or platform equivalent) that measures utilization against the declared requests; no request means no autoscaling signal.
5. **DO-245 — The autoscaling ceiling is a deliberate number.** Every autoscaler sets a maximum replica count, recorded with the cost reasoning behind it; the ceiling is a budget decision owned with the cloud-costs skill, not a default left at the platform maximum.
6. **DO-246 — Stateful tiers scale on their own path.** Databases and stateful services scale by managed replication, read replicas, or connection management chosen with D5; adding stateless app replicas against a saturated single database is not a scaling action.
7. **DO-247 — Load-test before the traffic event.** Before any launch, campaign, or seasonal peak, a load test runs in staging and the tested ceiling — sustained throughput with p95 latency inside the service's target — is recorded as a number in the project docs.
8. **DO-248 — Scale-down is designed, not accidental.** Autoscalers declare a stabilization window and connections drain gracefully on replica removal; replica counts oscillating up and down within minutes are treated as a defect and fixed before production reliance.
9. **DO-249 — Sizing is reviewed after change.** Requests, limits, and ceilings are re-checked against observed usage after every load test and after any material traffic-pattern change; the review and its outcome are recorded.
10. **DO-250 — A single server still states its ceiling.** A workload on one VPS or a non-autoscaling platform documents its capacity ceiling (the load-test number or the measured saturation point) and carries saturation monitoring; having neither an autoscaler nor a stated ceiling is a fail.
11. **DO-251 — Every scaling change leaves a record.** Each change to replica counts, ceilings, requests, or limits is logged with the date and the measurement that motivated it, so capacity history is auditable.
12. **DO-252 — Autoscaler behavior is proven end to end.** Before production relies on an autoscaler, a staging run drives load up and down and observes scale-up to the ceiling and scale-down without flapping; unobserved autoscaler configuration is untested configuration.

## BAN list

- **BAN-DO-121 — Workload with no resources declared.** Banned: a production container with no CPU or memory requests or limits. Defeats: DET-INF-027. Bad: a Deployment manifest with no `resources:` block, sized by whatever the node happens to have left. Instead: declare requests and limits sized from observed p95 usage on every container before the workload ships. Severity: BLOCK.
- **BAN-DO-122 — Unbounded autoscaler.** Banned: an autoscaler with no maximum replica count, or a maximum left at the platform default without a recorded cost decision. Defeats: DET-INF-027. Bad: an HPA with `maxReplicas: 500` copied from a template on a service whose tested ceiling needs 6 replicas, turning a traffic spike or a retry storm into an unbounded bill. Instead: set the ceiling from the load-test result and the budget, and record the reasoning with the cloud-costs skill. Severity: BLOCK.
- **BAN-DO-123 — Capacity by forecast.** Banned: provisioning or promising capacity for a launch or traffic event from an estimate alone, with no load test behind the number. Defeats: DET-INF-027. Bad: "Expect 10,000 launch-day users, so run 20 replicas" with no staging test showing what one replica sustains. Instead: load-test in staging, record the tested ceiling, and size replica counts from that number. Severity: BLOCK.
- **BAN-DO-124 — CPU-only saturation view.** Banned: judging scaling need from CPU alone while the service's real bottleneck — memory, disk, connection pool, or queue depth — is unmonitored. Defeats: DET-INF-011. Bad: a dashboard charting CPU at 40% while the database connection pool sits exhausted and requests queue. Instead: monitor all four golden signals with saturation tracked for the resource that actually limits the service. Severity: WARN.

## Gates

- **G-DO-121 — Resource and ceiling audit.** Verifies: DO-242, DO-245. Check: script over the production manifests or platform config confirms every container carries a `resources:` block and every autoscaler declares both a minimum and a maximum replica count. Pass: 100% of workloads have resources and no autoscaler is unbounded. Fail: block shipment. Recorded in: progress.md.
- **G-DO-122 — Load test report on file.** Verifies: DO-247, DO-252. Check: a load test report (k6, Locust, or platform equivalent) from staging is filed in the project docs, stating sustained throughput, p95 latency at that throughput, and the tested ceiling. Pass: the report exists and the ceiling is a recorded number. Fail: block the launch or traffic event. Recorded in: progress.md.
- **G-DO-123 — Autoscaler end-to-end observation.** Verifies: DO-244, DO-248. Check: in staging, drive load until the autoscaler adds replicas, hold, then remove load and watch scale-down. Pass: replicas rise to at most the ceiling under load and drain without oscillation after load stops. Fail: block production reliance on the autoscaler. Recorded in: progress.md.
- **G-DO-124 — Saturation alert coverage.** Verifies: DO-243, DO-250. Check: list the alerting rules for the service and confirm CPU, memory, disk, and the service's bottleneck resource (connections or queue depth) each have a threshold below exhaustion; fire one test alert. Pass: every listed resource alerts and the test alert reaches the on-call path. Fail: warn and fix before the next traffic event. Recorded in: progress.md.

## Anti-patterns

- **Bigger-box reflex.** Answering every slowdown by moving to a larger instance without identifying which resource saturates; the bottleneck moves with the box and the bill arrives first — find the saturating signal (DO-241) before spending.
- **Average-based sizing.** Requests sized from mean CPU or memory, so ordinary peaks exceed them and pods throttle or OOM at the busiest moment — size from p95 and compare against staging metrics at review.
- **Replicas in front of a saturated database.** Doubling the web tier while the single-writer database is the constraint; latency gets worse as contention grows — check stateful saturation (DO-246) before touching stateless counts.
- **Set-and-forget autoscaler.** An HPA shipped once and never re-observed after traffic patterns, instance types, or the app itself changed — the DO-249 review exists because last year's ceiling is a stale number.

## Examples

- [Example 1 — Requests and limits sized from p95 usage](examples/example-1.md) — violates/corrects DO-242.
- [Example 2 — Autoscaler with a ceiling and a stabilization window](examples/example-2.md) — violates/corrects DO-245, DO-248.
- [Example 3 — Load test before a launch event](examples/example-3.md) — violates/corrects DO-247.

## Recall anchors

- Scale from measurements, never from forecasts.
- No requests, no autoscaling — and no headroom.
- Every autoscaler has a ceiling, and the ceiling is a cost decision.
- Load-test before the event; the tested ceiling is a recorded number.
- Scale-down is designed: stabilize, drain, never flap.

## Checklist

- [ ] Golden-signal dashboards reviewed and the motivating measurement cited for this scaling change (DO-241).
- [ ] Every production container sets requests and limits from observed p95 usage (DO-242).
- [ ] Saturation alerts exist below exhaustion for CPU, memory, disk, and the bottleneck resource (DO-243).
- [ ] Autoscalers declare a maximum replica count with the cost reasoning recorded (DO-245, G-DO-121).
- [ ] Stateful saturation checked with D5 before stateless replica counts change (DO-246).
- [ ] Load test report filed with the tested ceiling as a recorded number (DO-247, G-DO-122).
- [ ] Autoscaler observed end to end in staging: scale-up to the ceiling, scale-down without flapping (DO-248, DO-252, G-DO-123).
- [ ] Single-server workloads state a documented capacity ceiling with saturation monitoring (DO-250).
