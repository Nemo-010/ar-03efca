# archive.today

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://archive.ph/
- Docs: https://archive.ph/
- Probe endpoint: `https://archive.ph/timemap/https://openalex.org`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota; the site throttles bursty callers with 429
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Readable via its timemap and newest endpoints. The probe got a 200 on the timemap and a 429 on the newest lookup, which is the site's own throttle rather than a documented tier.

## Evidence

> Archive.today is a time capsule for web pages!

Source: https://archive.ph/  
Snapshot: `data/snapshots/archive-today/docs.txt`  

## Live probe

- Request: `GET https://archive.ph/timemap/https://openalex.org`
- Result: HTTP 200 in 679 ms — **200 JSON**
- Body starts: `<https://openalex.org/>; rel="original", <http://archive.md/timegate/https://openalex.org/>; rel="timegate", <http://archive.md/20240116021934/https://openalex.org/>; rel="first me`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
