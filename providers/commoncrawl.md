# Common Crawl Index

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://commoncrawl.org/
- Docs: https://commoncrawl.org/cc-index-table
- Probe endpoint: `https://index.commoncrawl.org/collinfo.json`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published call quota; the index is a static file service
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

Crawl corpora and the CDXJ index are free to read. There is no account and no per-call price; volume is bounded by the index's own throughput.

## Evidence

> Common Crawl is a 501(c)(3) non-profit organization dedicated to providing a copy of the Internet to Internet researchers, companies and individuals at no cost for the purpose of research and analysis.

Source: https://commoncrawl.org/faq  
Snapshot: `data/snapshots/commoncrawl/limits.txt`  

## Live probe

- Request: `GET https://index.commoncrawl.org/collinfo.json`
- Result: HTTP 200 in 286 ms — **200 JSON**
- Body starts: `[ { "id": "CC-MAIN-2026-39", "name": "September 2026 Index", "timegate": "https://index.commoncrawl.org/CC-MAIN-2026-39/", "cdx-api": "https://index.commoncrawl.org/CC-MAIN-2026-39`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
