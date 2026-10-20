# NASA ADS

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://ui.adsabs.harvard.edu/
- Docs: https://ui.adsabs.harvard.edu/help/api/
- Probe endpoint: `https://api.adsabs.harvard.edu/v1/search/query?q=openalex`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **150,000 calls/month**
- Derivation: 5,000/day x 30 = 150,000 calls/month (published daily quota)
- Published rate: 5,000 regular requests/day for most request types, with a token; higher limits by email request
- Authentication: free key
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

NASA Astrophysics Data System. Publishes a daily figure and an explicit process for raising it; the token is generated from the user profile page.

## Evidence

> All users, including API users, are subject to the same rate limit (currently 5000 regular requests/day for most request types).

Source: https://adsabs.github.io/help/policies/rate-limits  
Snapshot: `data/snapshots/ads/ratelimits.txt`  

## Live probe

- Request: `GET https://api.adsabs.harvard.edu/v1/search/query?q=openalex`
- Result: HTTP 401 in 339 ms — **needs key**
- Body starts: `{"message": "Missing \"Authorization\" in headers."}`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
