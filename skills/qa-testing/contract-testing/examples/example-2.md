# Example 2 — Green pipeline, unread verdict

## Before

Contracts are written and the provider publishes verification results, but nothing in the delivery path ever reads them. The deploy job promotes unconditionally:

```yaml
deploy:
  steps:
    - run: ./deploy.sh production   # no can-i-deploy step anywhere
```

A provider release retypes a field the web app depends on. Verification in the provider's own CI goes red, nobody is notified, the release deploys, and the web app breaks in production — with a "verified contracts" badge on the repo the whole time.

## After

The deploy job asks the broker for the verdict for the exact version and environment, and its exit code gates promotion:

```yaml
deploy:
  steps:
    - name: Contract deploy gate
      run: >
        pact-broker can-i-deploy
        --pacticipant billing-api
        --version ${{ github.sha }}
        --to-environment production
    - run: ./deploy.sh production   # runs only if the gate exited 0
```

The step carries no `|| true` and no `continue-on-error`; a red verdict stops the promotion exactly like a failing test.

Note: corrects QA-167 (deployment reads the verdict).
