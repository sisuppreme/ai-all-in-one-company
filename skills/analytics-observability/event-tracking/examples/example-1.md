# Example 1 — One signup, three event names

## Before

The web app emits `Signup Completed`. The mobile web redesign adds its own handler and emits `signed_up`; a landing-page experiment emits `SignUp Completed`. The activation funnel, built on the original name, silently reports half the real signups, and the team debates a conversion drop that never happened.

## After

The plan declares one canonical event, `Signup Completed`, and all three surfaces emit it through the shared wrapper. The two variants are removed from code, the plan lint (G-AN-011) fails the build if either reappears, and the funnel reads one continuous series.

_Rule: AN-022 — one naming convention, enforced mechanically; duplicate or variant names are defects (BAN-AN-011)._
