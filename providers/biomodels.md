# BioModels

- Category: `data-api` — Life / physical science data APIs
- Home: https://www.ebi.ac.uk/biomodels/
- Docs: https://www.ebi.ac.uk/biomodels/docs/
- Probe endpoint: `https://www.ebi.ac.uk/biomodels/search?query=openalex&format=json`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Systems-biology models. The site states the mission is freely accessible models; the API answers keyless.

## Evidence

> Our mission is to provide the systems modelling community with reproducible, high-quality, freely accessible models published in the scientific literature.

Source: https://www.ebi.ac.uk/biomodels/  
Snapshot: `data/snapshots/biomodels/home.txt`  

## Live probe

- Request: `GET https://www.ebi.ac.uk/biomodels/search?query=openalex&format=json`
- Result: HTTP 200 in 1456 ms — **200 JSON**
- Body starts: `{"facetStats":"[]","facets":[],"matches":0,"models":[],"queryParameters":{"numResults":10,"offset":0,"sortBy":"relevance","sortDirection":"desc"}}`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
