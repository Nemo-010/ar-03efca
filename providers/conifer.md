# Conifer (Rhizome)

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://conifer.rhizome.org/
- Docs: https://conifer.rhizome.org/api/docs
- Probe endpoint: `https://conifer.rhizome.org/api/v1/`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: free accounts get 5GB of storage; no call quota published
- Authentication: free key
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Rhizome's web-archiving service. The free tier is measured in stored bytes, not calls.

## Evidence

> Free accounts with 5GB of storage.

Source: https://conifer.rhizome.org/  
Snapshot: `data/snapshots/conifer/home.txt`  

## Live probe

- Request: `GET https://conifer.rhizome.org/api/v1/`
- Result: HTTP 200 in 265 ms — **200 JSON**

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
