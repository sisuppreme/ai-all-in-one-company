# Example 3 — Automatic teardown

## Before

Previews were created per PR but nothing ever removed them. After two months the platform lists dozens of live previews from merged and closed PRs; several still serve old builds on guessable subdomains, and the workspace is near its preview quota, slowing new deploys.

## After

The pipeline owns the full lifecycle. A close/merge event runs the teardown job, and a weekly sweep enforces the configured caps (max 10 live previews, max age 7 days):

```yaml
teardown-preview:
  if: github.event.action == 'closed'
  steps:
    - run: ./scripts/teardown-preview.sh "$PR_NUMBER"
      # destroys the preview deploy, its database, and its subdomain

# scheduled sweep (weekly cron in the pipeline)
# ./scripts/sweep-previews.sh --max-count 10 --max-age-days 7
```

Closing the test PR makes its preview URL return 404 within the documented teardown window, verified by G-DO-013.

Note: corrects DO-026 — teardown is automatic on merge/close.
