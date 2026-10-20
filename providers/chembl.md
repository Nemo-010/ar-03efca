# ChEMBL

- Category: `data-api` — Life / physical science data APIs
- Home: https://www.ebi.ac.uk/chembl/
- Docs: https://chembl.gitbook.io/chembl-interface-documentation/web-services — HTTP 200 at capture
- Probe endpoint: `https://www.ebi.ac.uk/chembl/api/data/target.json?limit=1`
- llms.txt: https://chembl.gitbook.io/llms.txt

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Bioactivity database. Answers keyless with JSON or XML; the captured pages document parameters rather than rates.

## Evidence

> Because there is a limitation of how long a URL can be it's often more convenient to use POST requests instead.

Source: https://chembl.gitbook.io/chembl-interface-documentation/web-services  
Snapshot: `data/snapshots/chembl/r1.txt`  

## Live probe

- Request: `GET https://www.ebi.ac.uk/chembl/api/data/target.json?limit=1`
- Result: HTTP 200 in 2416 ms — **200 JSON**
- Body starts: `{"page_meta": {"limit": 1, "next": "/chembl/api/data/target.json?limit=1&offset=1", "offset": 0, "previous": null, "total_count": 18552}, "targets": [{"cross_references": [], "orga`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
