# Example 2 — Build once, promote the digest

## Before

```yaml
# Deploy job rebuilds from the branch and pulls whatever is newest
deploy-prod:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
      with:
        ref: main
    - run: docker build -t app:latest .
    - run: docker push app:latest
    - run: ssh prod "docker pull app:latest && docker compose up -d"
```

Production runs a fresh build of branch HEAD that was never the artifact staging tested; `latest` also makes every restart a silent upgrade.

## After

```yaml
# Build job publishes one immutable artifact and records its digest
build:
  runs-on: ubuntu-latest
  outputs:
    digest: ${{ steps.publish.outputs.digest }}
  steps:
    - uses: actions/checkout@v4
    - id: publish
      run: |
        docker build -t registry.example.com/app:${{ github.sha }} .
        docker push registry.example.com/app:${{ github.sha }}
        echo "digest=$(docker inspect --format='{{index .RepoDigests 0}}' registry.example.com/app:${{ github.sha }})" >> "$GITHUB_OUTPUT"

deploy-staging:
  needs: build
  runs-on: ubuntu-latest
  steps:
    - run: ./deploy.sh staging "${{ needs.build.outputs.digest }}"

deploy-prod:
  needs: [build, deploy-staging]
  runs-on: ubuntu-latest
  environment: production
  steps:
    - run: ./deploy.sh production "${{ needs.build.outputs.digest }}"
```

Both environments deploy the same digest that was built and tested once; each deploy writes its digest, commit SHA, actor, and timestamp to the deploy record.

Note: Demonstrates DO-005 — the artifact promoted to production is bit-identical to the one tested in staging.
