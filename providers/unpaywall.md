# Unpaywall

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://unpaywall.org/
- Docs: https://help.openalex.org/access/unpaywall.md — HTTP 200 at capture
- Probe endpoint: `https://api.unpaywall.org/v2/10.1038/nature12373?email=research@example.org`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: legacy-compatible surface over the OpenAlex database; the OpenAlex $1/day budget is the allowance that applies
- Authentication: free key
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Unpaywall no longer has its own allowance: its docs say it runs on the OpenAlex database and that there is no separate Unpaywall list. The old 100k/day figure is not in any captured page, so it is not claimed.

## Evidence

> Since then there has been one set of data. Unpaywall is a legacy-compatible format over it, kept stable for the thousands of tools built on it.

Source: https://help.openalex.org/access/unpaywall.md  
Snapshot: `data/snapshots/unpaywall/docs.txt`  

## Live probe

- Request: `GET https://api.unpaywall.org/v2/10.1038/nature12373?email=research@example.org`
- Result: HTTP 200 in 360 ms — **200 JSON**
- Body starts: `{"best_oa_location":{"endpoint_id":null,"evidence":"deprecated","host_type":"publisher","is_best":true,"license":null,"oa_date":"2013-07-30","pmh_id":null,"repository_institution":`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
