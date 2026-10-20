# Scite

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://scite.ai/
- Docs: https://api.scite.ai/
- Probe endpoint: `https://api.scite.ai/tallies/10.1038/nature12373`
- llms.txt: https://scite.ai/llms.txt

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: papers and tallies endpoints are public; everything else needs a key
- Authentication: free key
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

Citation statements (supporting / contradicting). Two endpoints are explicitly public, which is enough for lookups by DOI without an account.

## Evidence

> Papers and Tallies are public and don't require an API key.

Source: https://docs.scite.ai/authentication.md  
Snapshot: `data/snapshots/scite/auth.txt`  

## Live probe

- Request: `GET https://api.scite.ai/tallies/10.1038/nature12373`
- Result: HTTP 200 in 228 ms — **200 JSON**
- Rate-limit headers: `{"RateLimit-Limit": "60", "RateLimit-Remaining": "59", "RateLimit-Reset": "12", "X-RateLimit-Limit-Minute": "60", "X-RateLimit-Remaining-Minute": "59"}`
- Body starts: `{"total":1930,"supporting":22,"contradicting":1,"mentioning":1898,"unclassified":9,"doi":"10.1038/nature12373","citingPublications":2153}`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
