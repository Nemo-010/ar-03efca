# Altmetric

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://www.altmetric.com/
- Docs: https://api.altmetric.com/
- Probe endpoint: `https://api.altmetric.com/v1/doi/10.1038/nature12373`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: API key required; no free allowance captured
- Authentication: key on application
- Payment card for the free tier: not stated
- Evidence confidence: **low**

## Notes

Attention scores for research outputs. The details API answered 403 without a key.

## Evidence

> Altmetric does all the heavy lifting involved in extracting, disambiguating and

Source: https://api.altmetric.com/  
Snapshot: `data/snapshots/altmetric/limits.txt`  

## Live probe

- Request: `GET https://api.altmetric.com/v1/doi/10.1038/nature12373`
- Result: HTTP 403 in 88 ms — **needs key**
- Body starts: `You must supply an API key in a parameter named 'key'. As of 10 November 2025, all users need an API key to access the Altmetric Details Page API. To obtain access, register for an`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
