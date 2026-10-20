# PMC ID Converter

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://www.ncbi.nlm.nih.gov/pmc/tools/id-converter-api/
- Docs: https://www.ncbi.nlm.nih.gov/pmc/tools/id-converter-api/
- Probe endpoint: `https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids=PMC13900&format=json`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: up to 200 IDs per request; no call quota published
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Batches identifier conversions, which is the cheap way to normalise a reading list.

## Evidence

> The API service allows for up to 200 IDs in a single request.

Source: https://www.ncbi.nlm.nih.gov/pmc/tools/id-converter-api/  
Snapshot: `data/snapshots/pmc-idconv/docs.txt`  

## Live probe

- Request: `GET https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids=PMC13900&format=json`
- Result: HTTP 200 in 737 ms — **200 JSON**
- Body starts: `{"status":"ok","response-date":"2026-10-19 22:48:45","request":{"warnings":["query param `email` is missing.","query param `tool` is missing."],"format":"json","ids":["PMC13900"],"`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
