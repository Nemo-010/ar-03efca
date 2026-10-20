# bioRxiv API

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://www.biorxiv.org/
- Docs: https://api.biorxiv.org/ — HTTP 200 at capture
- Probe endpoint: `https://api.biorxiv.org/details/biorxiv/10.1101/2020.09.09.20191205`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published call quota; 100 results per page, cursor paging
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Preprint metadata by DOI or date window. Keyless and unthrottled in the probe.

## Evidence

> Results are paginated with 100 articles served in a call.

Source: https://api.biorxiv.org/  
Snapshot: `data/snapshots/biorxiv/docs.txt`  

## Live probe

- Request: `GET https://api.biorxiv.org/details/biorxiv/10.1101/2020.09.09.20191205`
- Result: HTTP 200 in 692 ms — **200 JSON**
- Body starts: `{"messages":[{"status":"no posts found"}], "collection":[]} `

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
