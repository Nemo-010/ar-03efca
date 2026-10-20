# Semantic Scholar Graph API

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://www.semanticscholar.org/
- Docs: https://www.semanticscholar.org/product/api
- Probe endpoint: `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1038/nature12373?fields=title`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: 1,000 requests/second shared by ALL unauthenticated callers; 1 req/s per key
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

The headline rate is a shared pool, not a per-caller allowance, so it is deliberately not converted into a monthly figure. In practice the pool is often exhausted: the probe got a 429.

## Evidence

> Most Semantic Scholar endpoints are available to the public without authentication, but they are rate-limited to 1000 requests per second shared among all unauthenticated users.

Source: https://www.semanticscholar.org/product/api  
Snapshot: `data/snapshots/semanticscholar/docs.txt`  

## Live probe

- Request: `GET https://api.semanticscholar.org/graph/v1/paper/DOI:10.1038/nature12373?fields=title`
- Result: HTTP 200 in 266 ms — **200 JSON**
- Body starts: `{"paperId": "a5de30adc5c22bc86e8cfabe7fbd07c052d196a8", "title": "Nanometer scale thermometry in a living cell"} `

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
