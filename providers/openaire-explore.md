# OpenAIRE Explore

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://explore.openaire.eu/
- Docs: https://graph.openaire.eu/docs/
- Probe endpoint: `https://api.openaire.eu/search/publications?keywords=openalex&size=1`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: a web UI over the Graph API; no separate allowance
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Counted separately from the Graph API because it is a different surface, but its quota is the Graph's.

## Evidence

> A comprehensive and open dataset of research information covering 239 M publications

Source: https://explore.openaire.eu/  
Snapshot: `data/snapshots/openaire-explore/home.txt`  

## Live probe

- Request: `GET https://api.openaire.eu/search/publications?keywords=openalex&size=1`
- Result: HTTP 200 in 707 ms — **200 JSON**
- Rate-limit headers: `{"x-ratelimit-limit": "7199", "x-ratelimit-used": "18"}`
- Body starts: `<?xml version="1.0" encoding="UTF-8"?> <response> <header> <query>(oaftype exact result) and (resulttypeid exact publication) and ( openalex)</query> <locale>en_US</locale> <size>1`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
