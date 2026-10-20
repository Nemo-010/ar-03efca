# Springer Nature API

- Category: `publisher` — Publisher & patent TDM endpoints
- Home: https://www.springernature.com/
- Docs: https://dev.springernature.com/ — HTTP 200 at capture
- Probe endpoint: `https://api.springernature.com/meta/v2/json?q=openalex`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: API key required; higher rate limits are a paid feature
- Authentication: paid only
- Payment card for the free tier: not stated
- Evidence confidence: **medium**

## Notes

Springer Nature. Has a separate Open Access API that is free for open-access content; the general metadata API needs a key.

## Evidence

> Open Access API Retrieve full-text content from our open access publications, empowering your research with unrestricted access to valuable insights.

Source: https://dev.springernature.com/  
Snapshot: `data/snapshots/springer/docs.txt`  

## Live probe

- Request: `GET https://api.springernature.com/meta/v2/json?q=openalex`
- Result: HTTP 401 in 792 ms — **needs key**
- Body starts: `{"status": "Fail","message": "Authentication failed. API key is invalid or missing","error": {"error": "Unauthorized", "error_description": "API key is invalid or missing. Ensure t`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
