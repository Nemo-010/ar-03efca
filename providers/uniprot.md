# UniProt

- Category: `data-api` — Life / physical science data APIs
- Home: https://www.uniprot.org/
- Docs: https://www.uniprot.org/help/api
- Probe endpoint: `https://rest.uniprot.org/uniprotkb/search?query=openalex&size=1&format=json`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **518,400,000 calls/month**
- Derivation: 200/s x 2,592,000 s/month = 518,400,000 calls/month ceiling
- Published rate: 200 requests/second/user
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

Protein knowledge base. The highest published rate in this set; the number comes from the Proteins API documentation page.

## Evidence

> We limit your requests to 200 requests/second/user.

Source: https://www.ebi.ac.uk/proteins/api/doc/  
Snapshot: `data/snapshots/uniprot/r2.txt`  

## Live probe

- Request: `GET https://rest.uniprot.org/uniprotkb/search?query=openalex&size=1&format=json`
- Result: HTTP 200 in 1016 ms — **200 JSON**
- Body starts: `{"results":[],"suggestions":[{"query":"openase","hits":2}]}`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
