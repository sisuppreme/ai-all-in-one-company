# Example 3 — The zero-error week that was a dead exporter

## Before

On Monday a deploy restarts the metrics exporter with a broken config and it never comes back. The scrape target is down, so no new series arrive. The error-rate panel, queried over the week, returns no errors — because it returns no data at all — and the flat line is read as a clean week. The weekly report states "zero errors in production". In reality the service threw errors all week; they were visible in the error tracker, which nobody cross-checked, and the monitoring gap itself went unnoticed for six days.

## After

The monitoring setup treats absence as a signal: an `up` series is tracked per scrape target, and alerting carries a dead-man's-switch rule — if a service's golden-signal series stop arriving for longer than the documented interval, an absence alert fires at the on-call channel, labeled "no data", distinct from any error-rate alert. Dashboards render data gaps as gaps, not as zero lines. The same exporter failure now pages within minutes as a monitoring outage, and the weekly report can only claim zero errors for windows where data was actually present.

Note: corrects AN-109 — missing data raises an absence alert and is reported as "no data", never read as zero errors (verified by the G-AN-055 drill).
