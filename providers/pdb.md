# RCSB PDB Data API

- Category: `data-api` — Life / physical science data APIs
- Home: https://www.rcsb.org/
- Docs: https://data.rcsb.org/redoc/
- Probe endpoint: `https://data.rcsb.org/rest/v1/core/entry/4HHB`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Protein structures. The data API answers keyless per entry; no rate page was captured.

## Live probe

- Request: `GET https://data.rcsb.org/rest/v1/core/entry/4HHB`
- Result: HTTP 200 in 321 ms — **200 JSON**
- Body starts: `{"audit_author":[{"name":"Fermi, G.","pdbx_ordinal":1},{"name":"Perutz, M.F.","pdbx_ordinal":2}],"cell":{"Z_PDB":4,"angle_alpha":90.0,"angle_beta":99.34,"angle_gamma":90.0,"length_`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
