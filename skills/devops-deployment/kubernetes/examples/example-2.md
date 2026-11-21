# Example 2 — Resources and replicas on a stateless tier

Note: demonstrates DO-083 and DO-088 — every container sets requests and limits, and stateless tiers run at least two replicas.

## Before

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 1
  template:
    spec:
      containers:
        - name: web
          image: registry.example.com/web:latest
          # no resources block: BestEffort pod, evicted first under pressure
```

One pod, no resource guarantees, unpinned image: a node failure or a memory crunch takes the only copy down.

## After

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 3
  template:
    spec:
      topologySpreadConstraints:
        - maxSkew: 1
          topologyKey: topology.kubernetes.io/zone
          whenUnsatisfiable: DoNotSchedule
      containers:
        - name: web
          image: registry.example.com/web@sha256:9f2c1a4b8d3e5f60718293a4b5c6d7e8f90a1b2c3d4e5f60718293a4b5c6d7e8f9
          resources:
            requests:
              cpu: "250m"
              memory: "256Mi"
            limits:
              cpu: "500m"
              memory: "512Mi"
```

Three replicas spread across zones, requests and limits sized from observed staging usage, and the image pinned by digest.
