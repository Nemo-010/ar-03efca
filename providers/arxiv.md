# arXiv API

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://arxiv.org/
- Docs: https://info.arxiv.org/help/api/tou.html
- Probe endpoint: `https://export.arxiv.org/api/query?search_query=all:openalex&max_results=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **864,000 calls/month**
- Derivation: 1 per 3 s = 1,200/hour x 24 x 30 = 864,000 calls/month ceiling
- Published rate: no more than one request every three seconds, single connection
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

Preprint server. The slowest published rate in this set, and deliberately so; metadata is CC0 and bulk access is meant to come from the OAI-PMH service or the bulk data. The probe shows the throttle working: three attempts in a row returned 429, then a read timeout, then 200 — all recorded in the probe history rather than only the last one.

## Evidence

> When using the legacy APIs (including OAI-PMH, RSS, and the arXiv API), make no more than one request every three seconds, and limit requests to a single connection at a time.

Source: https://info.arxiv.org/help/api/tou.html  
Snapshot: `data/snapshots/arxiv/docs.txt`  

## Live probe

- Request: `GET https://export.arxiv.org/api/query?search_query=all:openalex&max_results=1`
- Result: HTTP 200 in 205 ms — **200 JSON**
- Body starts: `<?xml version='1.0' encoding='UTF-8'?> <feed xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:arxiv="http://arxiv.org/schemas/atom" xmlns="http://www.w3.org/2005/Atom"`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
