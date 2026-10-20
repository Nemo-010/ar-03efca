# OpenAIRE Search API

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://www.openaire.eu/
- Docs: https://api.openaire.eu/
- Probe endpoint: `https://api.openaire.eu/search/publications?title=openalex&size=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no call quota published
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

The older publications search endpoint. Still answers unauthenticated; superseded by the Graph API for structured queries.

## Evidence

> Imagine a vast collection of research products all linked together, contextualised and openly available.

Source: https://api.openaire.eu/  
Snapshot: `data/snapshots/openaire-search/docs.txt`  

## Live probe

- Request: `GET https://api.openaire.eu/search/publications?title=openalex&size=1`
- Result: HTTP 200 in 830 ms — **200 JSON**
- Rate-limit headers: `{"x-ratelimit-limit": "7199", "x-ratelimit-used": "17"}`
- Body starts: `<?xml version="1.0" encoding="UTF-8"?> <response> <header> <query>(oaftype exact result) and (resulttypeid exact publication) and (resulttitle exact "openalex")</query> <locale>en_`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
