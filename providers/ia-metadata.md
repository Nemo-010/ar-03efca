# Internet Archive Metadata API

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://archive.org/
- Docs: https://archive.org/developers/md-read.html
- Probe endpoint: `https://archive.org/metadata/wikipedia`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Item metadata read API. Answers a bare GET per identifier and is the cheapest way to turn an archive.org identifier into structured metadata.

## Evidence

> An item’s metadata may be fetched by making an HTTP GET request to

Source: https://archive.org/developers/md-read.html  
Snapshot: `data/snapshots/ia-metadata/docs.txt`  

## Live probe

- Request: `GET https://archive.org/metadata/wikipedia`
- Result: HTTP 200 in 3299 ms — **200 JSON**
- Body starts: `{}`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
