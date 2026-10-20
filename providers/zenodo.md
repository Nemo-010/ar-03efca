# Zenodo

- Category: `repository` — Repositories & research-data archives
- Home: https://zenodo.org/
- Docs: https://developers.zenodo.org/
- Probe endpoint: `https://zenodo.org/api/records?q=openalex&size=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **2,592,000 calls/month**
- Derivation: 60/min x 1,440 x 30 = 2,592,000 calls/month ceiling for guests
- Published rate: guest 60 requests/minute and 2,000/hour; authenticated 100/minute and 5,000/hour
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

CERN's repository. The clearest guest-versus-authenticated rate table in this set, and it names the per-endpoint limits that bite first (search 30/min).

## Evidence

> Global limit for guest users 60 requests per minute, 2000 requests per hour

Source: https://developers.zenodo.org/#rate-limiting  
Snapshot: `data/snapshots/zenodo/limits.txt`  

## Live probe

- Request: `GET https://zenodo.org/api/records?q=openalex&size=1`
- Result: HTTP 200 in 1266 ms — **200 JSON**
- Rate-limit headers: `{"retry-after": "11", "x-ratelimit-limit": "30", "x-ratelimit-remaining": "28", "x-ratelimit-reset": "1792464529"}`
- Body starts: `{"hits": {"hits": [{"created": "2024-11-11T20:38:41.722044+00:00", "modified": "2024-11-11T20:38:41.917679+00:00", "id": 13941458, "conceptrecid": "13941457", "doi": "10.5281/zenod`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
