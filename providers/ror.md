# Research Organization Registry

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://ror.org/
- Docs: https://ror.readme.io/docs/rest-api
- Probe endpoint: `https://api.ror.org/v2/organizations?query=harvard`
- llms.txt: https://ror.readme.io/llms.txt

## Free access

- Documented volume: **17,280,000 calls/month**
- Derivation: 2,000 per 5 min = 400/min x 1,440 x 30 = 17,280,000 calls/month ceiling
- Published rate: 2,000 requests per 5 minutes per IP address; no registration
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

Research organisation registry. Publishes both the rate and the absence of registration.

## Evidence

> No registration is currently required to use the ROR API, but note that the rate limit is a maximum of 2000 requests in a 5-minute period per IP address

Source: https://ror.readme.io/docs/rest-api  
Snapshot: `data/snapshots/ror/docs.txt`  

## Live probe

- Request: `GET https://api.ror.org/v2/organizations?query=harvard`
- Result: HTTP 200 in 788 ms — **200 JSON**
- Body starts: `{"number_of_results":34,"time_taken":6,"items":[{"admin":{"created":{"date":"2021-04-06","schema_version":"1.0"},"last_modified":{"date":"2024-12-11","schema_version":"2.1"}},"doma`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
