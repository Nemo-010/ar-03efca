# Cleveland Museum of Art Open Access API

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://www.clevelandart.org/
- Docs: https://openaccess-api.clevelandart.org/
- Probe endpoint: `https://openaccess-api.clevelandart.org/api/artworks/?q=openalex&limit=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Cleveland Museum of Art open-access API. Answers keyless, and the whole dataset is also offered as a download, which sidesteps rate limits entirely.

## Evidence

> If you do not wish to use our API, you can obtain the complete and current dataset in JSON or CSV format from our GitHub repository .

Source: https://openaccess-api.clevelandart.org/  
Snapshot: `data/snapshots/cleveland-art/docs.txt`  

## Live probe

- Request: `GET https://openaccess-api.clevelandart.org/api/artworks/?q=openalex&limit=1`
- Result: HTTP 200 in 212 ms — **200 JSON**
- Body starts: `{"info": {"total": 0, "parameters": {"skip": 0, "limit": 1, "q": "openalex", "select": "accession_number,accession_number_sortable,cover_accession_number,department,collection,gall`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
