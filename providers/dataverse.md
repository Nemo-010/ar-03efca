# Harvard Dataverse

- Category: `repository` — Repositories & research-data archives
- Home: https://dataverse.harvard.edu/
- Docs: https://guides.dataverse.org/en/latest/api/
- Probe endpoint: `https://dataverse.harvard.edu/api/search?q=openalex&per_page=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published call quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Harvard Dataverse. The rate limit is a per-installation setting, not a hosted allowance: an operator sets calls-per-hour per tier, and if the setting is absent there is no limit. So there is no number to publish for dataverse.harvard.edu from the docs alone.

## Evidence

> Rate limiting can be configured on a tier level with tier 0 being reserved for guest users and tiers 1-any for authenticated users.

Source: https://guides.dataverse.org/en/latest/installation/config.html  
Snapshot: `data/snapshots/dataverse/ratelimits.txt`  

## Live probe

- Request: `GET https://dataverse.harvard.edu/api/search?q=openalex&per_page=1`
- Result: HTTP 200 in 388 ms — **200 JSON**
- Body starts: `{"status":"OK","data":{"q":"openalex","total_count":53,"start":0,"spelling_alternatives":{},"items":[{"name":"OpenAlex D-index","type":"dataverse","url":"https://dataverse.harvard.`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
