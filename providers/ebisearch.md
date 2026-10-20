# EBI Search

- Category: `data-api` — Life / physical science data APIs
- Home: https://www.ebi.ac.uk/ebisearch/
- Docs: https://www.ebi.ac.uk/ebisearch/swagger.ebi — HTTP 200 at capture
- Probe endpoint: `https://www.ebi.ac.uk/ebisearch/ws/rest?query=openalex&format=json`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

EBI-wide search. The REST endpoint returns a large JSON domain catalogue keyless.

## Live probe

- Request: `GET https://www.ebi.ac.uk/ebisearch/ws/rest?query=openalex&format=json`
- Result: HTTP 200 in 731 ms — **200 JSON**
- Body starts: `{"hitCount":337,"domains":[{"id":"allebi","hitCount":337,"subdomains":[{"id":"genomes","hitCount":0,"subdomains":[{"id":"dgva","hitCount":0},{"id":"ega","hitCount":0},{"id":"hgnc",`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
