# OpenAIRE Graph

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://graph.openaire.eu/
- Docs: https://graph.openaire.eu/docs/ — HTTP 200 at capture
- Probe endpoint: `https://api.openaire.eu/graph/v1/researchProducts?search=openalex&pageSize=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no call quota published; the graph is also downloadable in bulk
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

The Graph API answered 200 unauthenticated in the probe. Bulk download is the intended route for volume, and the licence is CC-BY or CC-0. The explore.openaire.eu web UI is a front end over this same API, so it is not counted as a separate provider.

## Evidence

> The Graph is freely available for download and re-use to all as CC-BY or CC-0.

Source: https://graph.openaire.eu/  
Snapshot: `data/snapshots/openaire-graph/home.txt`  

## Live probe

- Request: `GET https://api.openaire.eu/graph/v1/researchProducts?search=openalex&pageSize=1`
- Result: HTTP 200 in 678 ms — **200 JSON**
- Rate-limit headers: `{"x-ratelimit-limit": "7199", "x-ratelimit-used": "16"}`
- Body starts: `{"header":{"numFound":2955,"maxScore":10.416988,"queryTime":129,"page":1,"pageSize":1},"results":[{"authors":null,"openAccessColor":null,"publiclyFunded":null,"type":"software","la`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
