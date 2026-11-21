# Example 2 — The export that wasn't

## Before

```python
@app.get("/account/download-my-data")
def download_my_data(user):
    # TODO: real export later — serve the sample for now
    return send_file("static/export-sample.json")
```

Every requester receives the same placeholder file. The button works, the download works, and no subject has ever received their data.

## After

```python
@app.post("/privacy-requests")
def create_request(user, type="access"):
    req = log_request(user, type, channel="in-product")   # clock starts here
    verify_identity(req, method="authenticated-session")
    return {"request_ref": req.ref, "deadline": req.deadline}

def fulfil_access(req):
    bundle = {
        "account":   db.account_records(req.subject),
        "content":   db.content_records(req.subject),
        "search":    index.documents_for(req.subject),
        "analytics": analytics.events_for(req.subject),
        "processors": [p.export_for(req.subject) for p in processor_register],
    }
    deliver(req, to_json(bundle), to_csv(bundle))          # real records, usable formats
    close(req, outcome="delivered")
```

## Note

Corrected under LG-048: the export is generated from the subject's actual records across every store at fulfilment time (G-LG-021 asserts completeness against a test subject); a fabricated or template file is BAN-LG-022 (DET-FAKE-019).
