# NDLTD Union Catalog

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://search.ndltd.org/
- Docs: https://union.ndltd.org/OAI-PMH
- Probe endpoint: `https://union.ndltd.org/OAI-PMH?verb=Identify`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: not established — the OAI endpoint returned 503
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Theses and dissertations. Recorded as unverified: the OAI-PMH endpoint answered 503.

## Live probe

- Request: `GET https://union.ndltd.org/OAI-PMH?verb=Identify`
- Result: HTTP 503 in 734 ms — **429/503**
- Rate-limit headers: `{"Retry-After": "86400"}`
- Body starts: `<!DOCTYPE html> <html> <head> <title>503 Service Unavailable</title> <style> body { width: 35em; margin: 0 auto; font-family: Tahoma, Verdana, Arial, sans-serif; } </style> </head>`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
