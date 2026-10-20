# OpenAlex

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://openalex.org/
- Docs: https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication — HTTP 200 at capture
- Probe endpoint: `https://api.openalex.org/works?filter=doi:10.1038/nature12373`
- llms.txt: https://docs.openalex.org/llms.txt

## Free access

- Documented volume: **300,000 calls/month**
- Derivation: 10,000 list+filter calls per $1 of daily budget x 30 = 300,000 calls/month; a search costs 10x a list call, so 1,000 searches/day = 30,000/month
- Published rate: 10 req/s without a key, 30 req/s with a free key; $0.10/day keyless, $1/day with a key
- Authentication: free key
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

The clearest published free budget in this set: a dollar a day, with a published price per operation, so the call count follows from the price list. Single-entity lookups are free.

## Evidence

> Every account gets **$1 of usage per day** for free.

Source: https://help.openalex.org/access/example-costs.md  
Snapshot: `data/snapshots/openalex/costs.txt`  

## Live probe

- Request: `GET https://api.openalex.org/works?filter=doi:10.1038/nature12373`
- Result: HTTP 200 in 595 ms — **200 JSON**
- Rate-limit headers: `{"X-RateLimit-Cost-USD": "0.0001", "X-RateLimit-Credits-Used": "1", "X-RateLimit-Limit": "1000", "X-RateLimit-Limit-USD": "0.1", "X-RateLimit-Onetime-Remaining": "0", "X-RateLimit-Prepaid-Remaining-USD": "0", "X-RateLimit-Remaining": "942", "X-RateLimit-Remaining-USD": "0.0942", "X-RateLimit-Reset": "76289"}`
- Body starts: `{"meta": {"notice": "No API key, so this request shares one free daily budget ($0.10) with everyone on your network's IP address. Get a free key with its own $1/day at https://open`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
