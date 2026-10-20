# Figshare

- Category: `repository` — Repositories & research-data archives
- Home: https://figshare.com/
- Docs: https://docs.figshare.com/
- Probe endpoint: `https://api.figshare.com/v2/articles?page_size=1`
- llms.txt: none verified — no llms.txt found; the probe returned HTTP 202

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no automatic rate limiting in place for API requests
- Authentication: free key
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

The strongest free statement here — and the least useful one: no rate limiting is published, so there is no ceiling to plan against, and no promise it stays that way.

## Evidence

> We do not have automatic rate limiting in place for API requests.

Source: https://docs.figshare.com/  
Snapshot: `data/snapshots/figshare/docs.txt`  

## Live probe

- Request: `GET https://api.figshare.com/v2/articles?page_size=1`
- Result: HTTP 200 in 737 ms — **200 JSON**
- Body starts: `[{"id": 34704930, "title": "Food neophobia is associated with lower self-reported physical and mental health", "doi": "", "handle": "", "url": "https://api.figshare.com/v2/articles`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
