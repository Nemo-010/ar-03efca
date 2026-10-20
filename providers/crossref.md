# Crossref REST API

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://www.crossref.org/
- Docs: https://www.crossref.org/documentation/retrieve-metadata/rest-api/tips-for-using-the-crossref-rest-api/
- Probe endpoint: `https://api.crossref.org/works/10.1038/nature12373`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **12,960,000 calls/month**
- Derivation: 5/s x 2,592,000 s/month = 12,960,000 calls/month ceiling
- Published rate: 5 requests/second (public pool), 10/s polite pool with a mailto, 150/s with a Plus key
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

DOI metadata. No account needed for the public pool; adding a mailto moves you to the polite pool with double the rate and a concurrency allowance.

## Evidence

> The following limits apply: Pool Rate limit Concurrency limit Public 5 1 Polite 10 3 Plus 150 None

Source: https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/  
Snapshot: `data/snapshots/crossref/limits.txt`  

## Live probe

- Request: `GET https://api.crossref.org/works/10.1038/nature12373`
- Result: HTTP 200 in 224 ms — **200 JSON**
- Rate-limit headers: `{"x-rate-limit-interval": "1s", "x-rate-limit-limit": "5"}`
- Body starts: `{"status":"ok","message-type":"work","message-version":"1.0.0","message":{"indexed":{"date-parts":[[2026,10,18]],"date-time":"2026-10-18T15:24:20Z","timestamp":1792337060791,"versi`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
