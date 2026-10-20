# Lens.org Scholarly API

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://www.lens.org/
- Docs: https://docs.api.lens.org/
- Probe endpoint: `https://api.lens.org/scholarly/search`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: API key required; no free allowance published
- Authentication: paid only
- Payment card for the free tier: not stated
- Evidence confidence: **medium**

## Notes

Scholarly and patent records. The API root answers 401 without a key; the site markets a publicly available database but not a free API tier.

## Evidence

> This is the world’s largest publicly available database with internal transparency metrics.

Source: https://www.lens.org/  
Snapshot: `data/snapshots/lens/home.txt`  

## Live probe

- Request: `GET https://api.lens.org/scholarly/search`
- Result: HTTP 401 in 382 ms — **needs key**
- Body starts: `{"reference":"6732ea8f-7821-4f53-8440-809652538174","message":"Missing/Incorrect Authorization Header","code":401}`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
