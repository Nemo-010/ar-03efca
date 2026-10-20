# Europe PMC

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://europepmc.org/
- Docs: https://europepmc.org/RestfulWebService
- Probe endpoint: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=openalex&format=json&pageSize=1`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no call quota captured; the REST service answers unauthenticated
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Life-sciences literature, including full text for the open-access subset. The documentation site returned 403 to this client and the captured reference PDF is a binary that could not be read here, so no number is claimed.

## Evidence

> Comprehensive search Search life sciences literature from trusted sources around the globe, all in one search, accessible by anyone anywhere, for free.

Source: https://europepmc.org/  
Snapshot: `data/snapshots/europepmc/home.txt`  

## Live probe

- Request: `GET https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=openalex&format=json&pageSize=1`
- Result: HTTP 200 in 794 ms — **200 JSON**
- Body starts: `{"version":"6.9","hitCount":604,"nextCursorMark":"AoIIQKFopSg1NjU2ODEzNw==","nextPageUrl":"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=openalex&cursorMark=AoIIQKF`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
