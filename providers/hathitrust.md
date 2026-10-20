# HathiTrust Bibliographic API

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://www.hathitrust.org/
- Docs: https://www.hathitrust.org/bib_api
- Probe endpoint: `https://catalog.hathitrust.org/api/volumes/brief/json/oclc:424023`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published call quota; bulk work is steered to OAI and the hathifiles
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Bibliographic lookups by identifier only — it is explicitly not a keyword search API.

## Evidence

> The HathiTrust Bibliographic API is not a search API (e.g., where you use a keyword to search across the collection).

Source: https://www.hathitrust.org/bib_api  
Snapshot: `data/snapshots/hathitrust/limits.txt`  

## Live probe

- Request: `GET https://catalog.hathitrust.org/api/volumes/brief/json/oclc:424023`
- Result: HTTP 200 in 438 ms — **200 JSON**
- Body starts: `{"oclc:424023":{"records":{"000578050":{"recordURL":"https:\/\/catalog.hathitrust.org\/Record\/000578050","titles":["Infinite series"],"isbns":["9780030110405","9780030110405"],"is`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
