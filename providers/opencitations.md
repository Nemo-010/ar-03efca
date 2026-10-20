# OpenCitations Index

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://opencitations.net/
- Docs: https://opencitations.net/index/api/v2
- Probe endpoint: `https://opencitations.net/index/api/v2/citations/doi:10.1038/nature12373`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **7,776,000 calls/month**
- Derivation: 180/min x 1,440 x 30 = 7,776,000 calls/month ceiling
- Published rate: 180 requests/minute per IP address
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

Citation index. CC0 data, no key, published rate.

## Evidence

> API calls are rate-limited to 180 requests/minute per IP address to ensure fair usage and service availability.

Source: https://opencitations.net/index/api/v2  
Snapshot: `data/snapshots/opencitations/docs.txt`  

## Live probe

- Request: `GET https://opencitations.net/index/api/v2/citations/doi:10.1038/nature12373`
- Result: HTTP 200 in 2149 ms — **200 JSON**
- Body starts: `[ { "oci": "06010048871-06120344846", "citing": "omid:br/06010048871 openalex:W4409995113 doi:10.1063/5.0251893", "cited": "omid:br/06120344846 doi:10.1038/nature12373 pmid:2390374`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
