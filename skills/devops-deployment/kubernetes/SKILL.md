# kubernetes

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/ ; https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
- **Depends on:** containers, infrastructure-as-code
- **Feeds into:** deployment-strategies, scaling, reliability, rollback

## When to use / Do NOT use

- **Use when:** the workload has multiple services or a real scaling/failover requirement that justifies a cluster, and workloads are declared as manifests or Helm charts in Git and applied by the pipeline.
- **Do NOT use when:** the project is a single-service app with no scaling or failover need — use a managed platform or a VPS via the hosting or servers-vps skill instead; cluster ceremony for a one-service app is a finding, not an achievement.

## Rules

1. **DO-081 — Adoption test first.** Before any manifest is written, record in the project docs why Kubernetes is required (multiple services, real scaling, or failover need) and why a platform or VPS cannot meet it; no recorded justification, no cluster.
2. **DO-082 — Manifests are the source of truth.** Every workload is declared in manifests or Helm charts committed to Git and applied by the pipeline; no workload exists only in cluster state.
3. **DO-083 — Requests and limits on every container.** Every container in every workload sets CPU and memory requests and limits, sized from observed usage in staging or production metrics, not guessed.
4. **DO-084 — No BestEffort pods in production.** A pod with no requests and no limits is rejected at review; BestEffort pods are evicted first under pressure and are not a production posture.
5. **DO-085 — Readiness checks dependencies.** The readiness probe fails when a required dependency (database, cache, downstream API) is unreachable, so the pod leaves the Service endpoints until it can actually serve.
6. **DO-086 — Liveness checks only the process itself.** The liveness probe tests that the process is alive and able to make progress, never a downstream dependency; a dependency outage must drain pods via readiness, not restart-loop them via liveness.
7. **DO-087 — Slow starters get a startup probe.** A container that cannot answer its liveness probe during boot declares a startup probe, so liveness checks stay disabled until startup completes.
8. **DO-088 — Stateless tiers run at least two replicas.** Every stateless production workload sets `replicas: 2` or more, spread across nodes or zones with pod anti-affinity or topology spread constraints, behind a Service.
9. **DO-089 — State lives outside the pods.** Databases and durable state run in managed stores or replicated operators; a stateless tier never reads or writes state stored inside its own pods.
10. **DO-090 — Rollout history is retained.** Deployments keep enough revision history (`revisionHistoryLimit` ≥ 2) that `kubectl rollout undo` can return to the previous version at any time.
11. **DO-091 — No hand-edits to live objects.** `kubectl edit`, `kubectl patch`, and console changes to live objects are emergency-only and are back-ported into the committed manifests the same day.
12. **DO-092 — Images referenced by digest or pinned tag.** Workloads reference images by digest or a specific version tag, never `latest`, so the running version is identifiable and reproducible.

## BAN list

- **BAN-DO-041 — BestEffort production pod.** Banned: a production workload whose containers declare no resource requests or limits. Defeats: DET-INF-027. Bad: a Deployment manifest with no `resources:` block at all, relying on node leftovers. Instead: set requests and limits on every container, sized from observed usage, before the workload ships. Severity: BLOCK.
- **BAN-DO-042 — Dependency-checking liveness probe.** Banned: a liveness probe that calls a database, cache, or downstream API. Defeats: DET-INF-020. Bad: `livenessProbe` hitting `/healthz` that returns 500 whenever Postgres is down, restarting every pod during a database outage. Instead: make liveness check only the process itself and move the dependency check into the readiness probe. Severity: BLOCK.
- **BAN-DO-043 — Single-replica stateless tier.** Banned: a production stateless workload running one replica as its only copy behind the Service. Defeats: DET-INF-019. Bad: `replicas: 1` on the only web tier, so one pod kill or node failure takes the site down. Instead: run at least two replicas spread across failure domains behind the Service. Severity: BLOCK.
- **BAN-DO-044 — Cluster state edited by hand.** Banned: changing live objects with `kubectl edit` or a console and leaving the committed manifests unchanged. Defeats: DET-INF-024. Bad: an engineer raises a replica count live during an incident and the repo still says the old value, so the next pipeline apply silently reverts it. Instead: back-port every emergency live change into the manifests in Git the same day. Severity: WARN.

## Gates

- **G-DO-041 — Manifest validity and resource lint.** Verifies: DO-082, DO-083, DO-084, DO-092. Check: `kubectl apply --dry-run=server -f k8s/` succeeds, and a script over the manifests confirms every container has requests, limits, and a digest or pinned-tag image (no `latest`). Pass: dry-run clean and zero containers missing resources or using `latest`. Fail: block shipment. Recorded in: progress.md.
- **G-DO-042 — Probe behavior drill.** Verifies: DO-085, DO-086, DO-087. Check: in staging, stop a required dependency; the workload's readiness fails and pods drain from the Service, while liveness does not restart any pod. Pass: traffic stops, zero restarts during the outage, pods return when the dependency recovers. Fail: block shipment. Recorded in: progress.md.
- **G-DO-043 — Kill-one-pod drill.** Verifies: DO-088, DO-089. Check: `kubectl delete pod` on one replica of each stateless tier while sending requests; the Service keeps responding with no user-visible errors. Pass: no failed requests during the kill. Fail: block shipment. Recorded in: progress.md.
- **G-DO-044 — Drift and rollback check.** Verifies: DO-090, DO-091. Check: diff live objects against the committed manifests (`kubectl diff -f k8s/` shows no unexplained changes) and run `kubectl rollout undo` on one Deployment in staging to prove the previous revision restores. Pass: no unexplained drift and the undo succeeds. Fail: warn and reconcile before the next release. Recorded in: progress.md.

## Anti-patterns

- **Cluster for one container.** A full Kubernetes setup serving a single small app that a platform or VPS would host for a few dollars — catch it at the adoption test (DO-081) before any manifest exists.
- **Requests copied from a tutorial.** Resource values pasted from a blog post instead of measured usage; they pass the lint gate but starve or waste in production — compare against staging metrics at review.
- **Probes on a static path.** Readiness and liveness both hitting `/` and returning 200 while dependencies are dead; the homepage being up is not the service being able to serve — trace what the probe handler actually touches.
- **Helm values drift.** The chart is in Git but the real values live in a `--set` command in someone's shell history, so no one can reproduce the release — values belong in committed values files.

## Examples

- [Example 1 — Probes that drain instead of restart-loop](examples/example-1.md) — violates/corrects DO-085, DO-086.
- [Example 2 — Resources and replicas on a stateless tier](examples/example-2.md) — violates/corrects DO-083, DO-088.
- [Example 3 — Emergency live edit back-ported to Git](examples/example-3.md) — violates/corrects DO-091.

## Recall anchors

- No recorded need, no cluster.
- No requests, no autoscaling — and first to be evicted.
- Readiness checks dependencies; liveness never does.
- Two replicas minimum, state outside the pods.
- If it is not in Git, it does not exist.

## Checklist

- [ ] Adoption justification recorded, naming why a platform or VPS cannot meet the need (DO-081).
- [ ] Every container sets requests and limits from observed usage; no BestEffort pods (DO-083, DO-084).
- [ ] Readiness checks dependencies; liveness checks only the process; slow starters have startup probes (DO-085–DO-087).
- [ ] Stateless tiers run ≥2 replicas across failure domains; state lives outside the pods (DO-088, DO-089).
- [ ] Revision history retained and `kubectl rollout undo` proven in staging (DO-090).
- [ ] Live objects match committed manifests; any emergency edit back-ported same day (DO-091).
- [ ] All images referenced by digest or pinned tag, never `latest` (DO-092).
