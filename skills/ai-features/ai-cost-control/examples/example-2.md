# Example 2 — The retry loop that billed all weekend

## Before

```text
Agent task runner (paraphrased):
  while not task_complete:
      result = call_model(plan + history)
      if result.error or result.needs_more_steps:
          continue        # retry / re-plan, no counter, no spend check

Friday 18:40 — a malformed tool response makes every plan "need more steps."
The loop runs until Monday 08:15, when someone notices the usage graph.
Every iteration was a full-price call with the full accumulated history.
```

No iteration cap, no per-task spend cap, no maximum context — a single stuck task consumed the feature's whole monthly budget in one weekend.

## After

```text
Recorded bounds in the task config: max_retries = 3 (exponential backoff),
max_iterations = 25, max_spend_per_task = <budget value>, input context
capped at the feature's per-request token budget (AI-187).

Same fault injected in staging (G-AI-092): the stub returns a retryable
error indefinitely. The runner stops at the recorded bound, returns a
typed TASK_BUDGET_EXCEEDED error, the user sees "this task could not be
completed automatically," and total tokens consumed stay under the
bound's ceiling. The failure is a support ticket, not an invoice.
```

## Note

Violates AI-184: retries and agent loops with no hard iteration or spend bound. Corrected by recording the bounds in configuration, terminating with a typed error, and proving termination with the runaway-loop fault-injection test.
