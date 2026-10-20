# zbMATH Open

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://zbmath.org/
- Docs: https://api.zbmath.org/v1/
- Probe endpoint: `https://api.zbmath.org/v1/document/_structured_search_query?search_string=openalex&results_per_page=1`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Mathematics bibliography. The structured-search endpoint answers keyless; the documentation page captured is a stub.

## Live probe

- Request: `GET https://api.zbmath.org/v1/document/_structured_search_query?search_string=openalex&results_per_page=1`
- Result: HTTP 200 in 645 ms — **200 JSON**
- Body starts: `{"result":null,"status":{"execution":"Entry not found!...","execution_bool":false,"internal_code":"Entry not found! internal code: id does not exist!","last_id":null,"nr_total_resu`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
