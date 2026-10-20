# DOAJ

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://doaj.org/
- Docs: https://doaj.org/api/v4/docs
- Probe endpoint: `https://doaj.org/api/search/articles/openalex?pageSize=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **5,184,000 calls/month**
- Derivation: 2/s x 2,592,000 s/month = 5,184,000 calls/month ceiling
- Published rate: 2 requests/second on all API routes, with a 5-request burst queue
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

Directory of Open Access Journals. Publishes the rate and the burst behaviour.

## Evidence

> There is a rate limit of two requests per second on all API routes.

Source: https://doaj.org/api/v4/docs  
Snapshot: `data/snapshots/doaj/docs.txt`  

## Live probe

- Request: `GET https://doaj.org/api/search/articles/openalex?pageSize=1`
- Result: HTTP 200 in 369 ms — **200 JSON**
- Body starts: `{"total": 252, "page": 1, "pageSize": 1, "timestamp": "2026-10-20T02:48:34.239941Z", "query": "openalex", "results": [{"last_updated": "2025-08-19T21:34:10Z", "bibjson": {"identifi`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
