# BASE (Bielefeld)

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://www.base-search.net/
- Docs: https://api.base-search.net/ — HTTP 200 at capture
- Probe endpoint: `https://api.base-search.net/cgi-bin/BaseHttpSearchInterface.fcgi?func=PerformSearch&query=openalex&format=json`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: API key granted on application; no call quota published
- Authentication: key on application
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Bielefeld Academic Search Engine. The key is free but must be applied for, which puts it out of reach of a gateway that wants to start today.

## Evidence

> Before you can start testing and using the interface, you need to apply for an API key via this form .

Source: https://api.base-search.net/  
Snapshot: `data/snapshots/base/docs.txt`  

## Live probe

- Request: `GET https://api.base-search.net/cgi-bin/BaseHttpSearchInterface.fcgi?func=PerformSearch&query=openalex&format=json`
- Result: HTTP 200 in 1910 ms — **200 JSON**
- Body starts: `{"error": "Access denied for IP address 38.25.151.89 and user agent ar-research/0.1 (public API documentation inventory; +https://github.com/Nemo-010/ar-03efca)."}`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
