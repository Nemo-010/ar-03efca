# BioStudies (EBI)

- Category: `data-api` — Life / physical science data APIs
- Home: https://www.ebi.ac.uk/biostudies/
- Docs: https://www.ebi.ac.uk/biostudies/api/v1/swagger-ui.html
- Probe endpoint: `https://www.ebi.ac.uk/biostudies/api/v1/search?query=openalex&pageSize=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

EBI study archive. Answers keyless; the captured help page is navigation chrome.

## Live probe

- Request: `GET https://www.ebi.ac.uk/biostudies/api/v1/search?query=openalex&pageSize=1`
- Result: HTTP 200 in 601 ms — **200 JSON**
- Body starts: `{"page":1,"pageSize":1,"totalHits":20,"isTotalHitsExact":true,"sortBy":"relevance","sortOrder":"descending","suggestion":[],"expandedEfoTerms":[],"expandedSynonyms":[],"query":"ope`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
