# SciELO ArticleMeta

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://scielo.org/
- Docs: https://articlemeta.scielo.org/api/v1/
- Probe endpoint: `https://articlemeta.scielo.org/api/v1/article/identifiers/?limit=1`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: not established
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Latin American open-access collection. The ArticleMeta endpoint answered 200 keyless; no documentation page could be captured.

## Evidence

> Read our Open Access Statement

Source: https://scielo.org/  
Snapshot: `data/snapshots/scielo/home.txt`  

## Live probe

- Request: `GET https://articlemeta.scielo.org/api/v1/article/identifiers/?limit=1`
- Result: HTTP 200 in 1580 ms — **200 JSON**
- Body starts: `{ "meta": { "limit": 1, "offset": 0, "filter": { "processing_date": { "$gte": "1900-01-01", "$lte": "2026-10-19" } }, "total": 1436787 }, "objects": [ { "code": "S0100-879X19980008`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
