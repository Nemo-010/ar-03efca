# DOAB

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://www.doabooks.org/
- Docs: https://directory.doabooks.org/rest/
- Probe endpoint: `https://directory.doabooks.org/rest/search?query=openalex`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: all services free of charge; no call quota published
- Authentication: free key
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

Directory of Open Access Books. The site says the services and the data are free; the REST endpoint needs a key in the probe.

## Evidence

> All DOAB services are free of charge and all data is freely available.

Source: https://www.doabooks.org/  
Snapshot: `data/snapshots/doab/home.txt`  

## Live probe

- Request: `GET https://directory.doabooks.org/rest/search?query=openalex`
- Result: HTTP 403 in 509 ms — **needs key**
- Body starts: `You address is not allowed to access this API.`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
