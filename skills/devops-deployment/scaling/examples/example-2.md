# Example 2 — Autoscaler with a ceiling and a stabilization window

Demonstrates: DO-245 (the autoscaling ceiling is a deliberate number) and DO-248 (scale-down is designed, not accidental).

## Before

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web
  minReplicas: 2
  maxReplicas: 500
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

The ceiling of 500 was copied from a template: the load test showed 6 replicas sustain peak traffic, so a spike or retry storm can scale the service — and its bill — far past any tested or budgeted level, and with no stabilization window the replica count flaps as load jitters.

## After

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web
  minReplicas: 2
  # Ceiling: load test (2026-11-21) — 6 replicas sustain the tested peak;
  # 10 gives headroom and caps worst-case hourly cost per the cloud-costs record.
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Pods
          value: 1
          periodSeconds: 60
```

The ceiling is set from the load-test result and the recorded cost decision, and scale-down waits five minutes and removes one pod per minute, so replicas drain gracefully instead of oscillating.
