# Example 3 — Emergency live edit back-ported to Git

Note: demonstrates DO-091 — live-object edits are emergency-only and are back-ported into the committed manifests the same day.

## Before

During an incident, an engineer runs `kubectl edit deployment web` and raises replicas from 3 to 6 directly on the live object. The committed manifest in Git still says 3. Two days later the next pipeline apply silently scales the tier back to 3 mid-traffic, and nobody can reconstruct what the cluster was actually running during the incident.

## After

The same emergency edit is made live to stop the incident, and the same day the engineer updates the committed manifest (`replicas: 6`), commits it with a note linking the incident, and `kubectl diff -f k8s/` confirms live state and Git agree. The next pipeline apply changes nothing, and the incident review can read exactly what ran and when.
