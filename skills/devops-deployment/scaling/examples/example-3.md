# Example 3 — Load test before a launch event

Demonstrates: DO-247 (load-test before the traffic event; the tested ceiling is a recorded number).

## Before

Launch plan note, written the week before a product launch:

> Expect around 10,000 visitors on launch day. Run 20 replicas of the web tier to be safe.

No load test backs either number: nobody knows what one replica sustains, whether 20 replicas help (the database may saturate at 4), or what the service does past its ceiling. The first real load test is the launch itself.

## After

Load test report filed in the project docs before the launch (k6 against staging, production-shaped data):

> - Ramp: 0 → 400 concurrent users over 10 minutes, hold 15 minutes.
> - Result: p95 latency stayed under the 800 ms target up to 260 requests/second; errors began at 310 requests/second with database connections exhausted.
> - Tested ceiling: **260 requests/second sustained**, reached at 5 web replicas; a 6th replica added nothing (database-bound — read replica work handed to D5).
> - Launch configuration: 6 replicas, autoscaler ceiling 10, saturation alerts on connection-pool usage at 70%.

Capacity is now a measured number with a named bottleneck, replica counts are sized from it, and the remaining constraint has an owner instead of a launch-day surprise.
