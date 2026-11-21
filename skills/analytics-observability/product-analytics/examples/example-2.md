# Example 2 — Pageviews-only "analytics" becomes a measurement plan

## Before

The analytics snippet is pasted into the site template on day one. Auto-collected pageviews accumulate. There is no tracking plan, no event for signup or for the product's core action, and no definition of "active user". When the team asks "where do signups drop off?", the only answer available is a pageview list.

## After

A tracking plan is committed to the repo before any instrumentation is added:

```markdown
# Tracking plan v1.0
Identity: anonymous_id = first-party cookie set on first visit;
identify on login; pre-login events stitch by anonymous_id.

Metric: signup_conversion
  = signup_completed / landing_viewed (same session)
  Events: landing_viewed {referrer}, signup_completed {plan}
  Owner: product-analytics. Review: weekly.

Metric: activation_7d
  = users with core_action_completed within 7 days of signup_completed
  Events: signup_completed, core_action_completed {action_type}
  Owner: product-analytics. Review: weekly.
```

Only the listed events are implemented, and a scripted test session diffs captured events against this plan before release (gate G-AN-001).

Note: the Before violates AN-001 (tracking plan before instrumentation); the After corrects it.
