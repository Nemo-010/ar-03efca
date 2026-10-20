# Wikipedia / MediaWiki API

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://www.mediawiki.org/wiki/API:Main_page
- Docs: https://www.mediawiki.org/wiki/API:Etiquette — HTTP 200 at capture
- Probe endpoint: `https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=openalex&format=json&srlimit=1`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no hard speed limit on reads; write and state-changing calls are limited
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

MediaWiki action API. Read traffic is governed by etiquette rather than a published quota.

## Evidence

> There is no hard speed limit on read requests, but be considerate and try not to take a site down.

Source: https://www.mediawiki.org/wiki/API:Etiquette  
Snapshot: `data/snapshots/wikipedia-api/docs.txt`  

## Live probe

- Request: `GET https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=openalex&format=json&srlimit=1`
- Result: HTTP 200 in 432 ms — **200 JSON**
- Body starts: `{"batchcomplete":"","continue":{"sroffset":1,"continue":"-||"},"query":{"searchinfo":{"totalhits":40,"suggestion":"openable","suggestionsnippet":"openable"},"search":[{"ns":0,"titl`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
