# DataverseNL

- Category: `repository` — Repositories & research-data archives
- Home: https://dataverse.nl/
- Docs: https://guides.dataverse.org/en/latest/api/ — HTTP 200 at capture
- Probe endpoint: `https://dataverse.nl/api/search?q=openalex`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published call quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Dutch Dataverse instance; same software, same per-installation rate limiting as the Harvard row, so its allowance is whatever that installation configured.

## Evidence

> Rate limiting can be configured on a tier level with tier 0 being reserved for guest users and tiers 1-any for authenticated users.

Source: https://guides.dataverse.org/en/latest/installation/config.html  
Snapshot: `data/snapshots/dataverse-nl/ratelimits.txt`  

## Live probe

- Request: `GET https://dataverse.nl/api/search?q=openalex`
- Result: HTTP 200 in 831 ms — **200 JSON**
- Body starts: `{"status":"OK","data":{"q":"openalex","total_count":205,"start":0,"spelling_alternatives":{},"items":[{"name":"SYNERGY+","type":"dataset","url":"https://doi.org/10.34894/DDCVCV","i`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
