# DigitalNZ

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://digitalnz.org/
- Docs: https://digitalnz.org/developers/api — HTTP 202 at capture (see Notes)
- Probe endpoint: `https://api.digitalnz.org/v3/records.json?text=openalex`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: not established (key required; docs served a 202 challenge)
- Authentication: free key
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

The records endpoint answered 200 with a key-less call in the probe, but the documentation pages returned a 202 interstitial and no allowance was captured.

## Live probe

- Request: `GET https://api.digitalnz.org/v3/records.json?text=openalex`
- Result: HTTP 200 in 1314 ms — **200 JSON**
- Body starts: `{"search":{"page":1,"per_page":20,"result_count":3,"request_url":"https://api.digitalnz.org/v3/records.json?text=openalex","results":[{"id":52462072,"created_at":"2023-09-18T16:54:`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
