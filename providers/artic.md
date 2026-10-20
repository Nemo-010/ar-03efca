# Art Institute of Chicago API

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://api.artic.edu/docs/
- Docs: https://api.artic.edu/docs/
- Probe endpoint: `https://api.artic.edu/api/v1/artworks?limit=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **2,592,000 calls/month**
- Derivation: 60/min x 1,440 x 30 = 2,592,000 calls/month ceiling
- Published rate: anonymous callers throttled to 60 requests/minute; each IP is one user
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

Art Institute of Chicago. Says outright that the API works without authentication and publishes the anonymous throttle.

## Evidence

> You may access our API without authentication.

Source: https://api.artic.edu/docs/  
Snapshot: `data/snapshots/artic/docs.txt`  

## Live probe

- Request: `GET https://api.artic.edu/api/v1/artworks?limit=1`
- Result: HTTP 200 in 318 ms — **200 JSON**
- Body starts: `{"pagination":{"total":133170,"limit":1,"offset":0,"total_pages":133170,"current_page":1,"next_url":"https:\/\/api.artic.edu\/api\/v1\/artworks?page=2&limit=1"},"data":[{"id":65344`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
