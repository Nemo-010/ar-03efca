# K10plus SRU

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://k10plus.de/
- Docs: https://projekt.mvb10plus.de/ — not captured (see Notes)
- Probe endpoint: `https://sru.k10plus.de/gvk?version=1.1&operation=searchRetrieve&query=pica.all%3Dopenalex&maximumRecords=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: SRU service; no published call quota
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

K10plus union catalogue. The SRU endpoint answers; the captured page is a short index.

## Live probe

- Request: `GET https://sru.k10plus.de/gvk?version=1.1&operation=searchRetrieve&query=pica.all%3Dopenalex&maximumRecords=1`
- Result: HTTP 200 in 834 ms — **200 JSON**
- Body starts: `<?xml version="1.0" encoding="UTF-8"?> <zs:searchRetrieveResponse xmlns:zs="http://www.loc.gov/zing/srw/"><zs:version>1.1</zs:version><zs:numberOfRecords>23</zs:numberOfRecords><zs`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
