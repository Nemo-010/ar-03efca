# CORE

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://core.ac.uk/
- Docs: https://core.ac.uk/services/api
- Probe endpoint: `https://api.core.ac.uk/v3/search/works/?q=openalex&limit=1`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **1,296,000 calls/month**
- Derivation: 5 per 10 s = 30/min x 1,440 x 30 = 1,296,000 calls/month ceiling
- Published rate: one batch request or five single requests per 10 seconds, without registration
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

Open-access aggregator. Free and keyless; registered organisations get a faster rate that is typically paid.

## Evidence

> CORE API is free and does not require registration, subject to our rate limits .

Source: https://core.ac.uk/services/api  
Snapshot: `data/snapshots/core/docs.txt`  

## Live probe

- Request: `GET https://api.core.ac.uk/v3/search/works/?q=openalex&limit=1`
- Result: HTTP 200 in 919 ms — **200 JSON**
- Rate-limit headers: `{"x-ratelimit-limit": "10", "x-ratelimit-remaining": "9", "x-ratelimit-retry-after": "2026-10-20T02:48:32+0000"}`
- Body starts: `{"totalHits":1311,"limit":1,"offset":0,"results":[{"acceptedDate":"","arxivId":null,"authors":[{"name":"Johansen, Marit"},{"name":"Larsen, Martin Sm\u00e5dal"},{"name":"Hval, Gyri"`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
