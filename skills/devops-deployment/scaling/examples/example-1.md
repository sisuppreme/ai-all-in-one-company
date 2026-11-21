# Example 1 — Requests and limits sized from p95 usage

Demonstrates: DO-242 (requests and limits on every workload, sized from observed p95 usage).

## Before

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 2
  template:
    spec:
      containers:
        - name: web
          image: registry.example.com/web@sha256:1a2b3c
          # no resources block — sized by whatever the node has left
```

The container declares no requests or limits: the scheduler cannot place it predictably, the autoscaler has no utilization signal, and under node pressure this pod is evicted first.

## After

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 2
  template:
    spec:
      containers:
        - name: web
          image: registry.example.com/web@sha256:1a2b3c
          resources:
            requests:
              cpu: "250m"     # staging p95 CPU over 7 days: 210m
              memory: "256Mi" # staging p95 memory over 7 days: 230Mi
            limits:
              cpu: "500m"
              memory: "512Mi"
```

Requests and limits are set from the measured p95 in staging, with the measurement noted alongside, so sizing is auditable and the autoscaler can compute utilization against the request.
