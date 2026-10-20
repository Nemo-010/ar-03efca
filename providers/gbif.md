# GBIF

- Category: `data-api` — Life / physical science data APIs
- Home: https://www.gbif.org/
- Docs: https://techdocs.gbif.org/en/openapi/
- Probe endpoint: `https://api.gbif.org/v1/occurrence/search?q=openalex&limit=1`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no fixed rate; the docs say the maximum changes with server load
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Biodiversity occurrences. Most of the API needs no authentication, and the docs are explicit that the tolerated rate moves with load, so no number is quoted.

## Evidence

> Most use of the GBIF API does not require authentication.

Source: https://techdocs.gbif.org/en/openapi/  
Snapshot: `data/snapshots/gbif/docs.txt`  

## Live probe

- Request: `GET https://api.gbif.org/v1/occurrence/search?q=openalex&limit=1`
- Result: HTTP 200 in 1292 ms — **200 JSON**
- Body starts: `{"offset":0,"limit":1,"endOfRecords":true,"count":0,"results":[],"facets":[]}`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
