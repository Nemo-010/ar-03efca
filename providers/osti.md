# OSTI.gov

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://www.osti.gov/
- Docs: https://www.osti.gov/api/v1/docs — HTTP 200 at capture
- Probe endpoint: `https://www.osti.gov/api/v1/records?q=openalex&rows=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

US DOE science and technical reports. The API documents its resources but no rate.

## Evidence

> The API is built on a REST architecture, providing predictable URLs that make writing applications easy.

Source: https://www.osti.gov/api/v1/docs  
Snapshot: `data/snapshots/osti/docs.txt`  

## Live probe

- Request: `GET https://www.osti.gov/api/v1/records?q=openalex&rows=1`
- Result: HTTP 200 in 353 ms — **200 JSON**
- Body starts: `[ {"language":"English","entry_date":"2026-09-23T07:42:21Z","report_number":"LA-UR-26-27683","identifier":"89233218CNA000001","country_publication":"United States","doi":"10.2172/3`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
