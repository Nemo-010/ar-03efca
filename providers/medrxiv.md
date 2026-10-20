# medRxiv API

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://www.medrxiv.org/
- Docs: https://api.biorxiv.org/
- Probe endpoint: `https://api.biorxiv.org/details/medrxiv/10.1101/2020.09.09.20191205`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: same service as bioRxiv; no published quota
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Health-sciences preprints, served by the same API host as bioRxiv.

## Evidence

> Results are paginated with 100 articles served in a call.

Source: https://api.biorxiv.org/  
Snapshot: `data/snapshots/medrxiv/docs.txt`  

## Live probe

- Request: `GET https://api.biorxiv.org/details/medrxiv/10.1101/2020.09.09.20191205`
- Result: HTTP 200 in 657 ms — **200 JSON**
- Body starts: `{"messages":[{"status":"ok","category":"all"}], "collection":[{"title":"Evolution of immunity to SARS-CoV-2","authors":"Wheatley, A. K.; Juno, J. A.; Wang, J. J.; Selva, K. J.; Rey`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
