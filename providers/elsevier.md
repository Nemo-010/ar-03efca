# Elsevier Scopus / ScienceDirect API

- Category: `publisher` — Publisher & patent TDM endpoints
- Home: https://www.elsevier.com/
- Docs: https://dev.elsevier.com/ — HTTP 200 at capture
- Probe endpoint: `https://api.elsevier.com/content/search/scopus?query=openalex`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: API key plus an entitlement per product; no free allowance published
- Authentication: paid only
- Payment card for the free tier: not stated
- Evidence confidence: **medium**

## Notes

Scopus and ScienceDirect. The docs say plainly that holding a key does not grant access to content, which is the key distinction from the open APIs above.

## Evidence

> Registering for or holding an API key does not by itself grant access to Elsevier data or content.

Source: https://dev.elsevier.com/  
Snapshot: `data/snapshots/elsevier/docs.txt`  

## Live probe

- Request: `GET https://api.elsevier.com/content/search/scopus?query=openalex`
- Result: HTTP 401 in 331 ms — **needs key**
- Body starts: `{"service-error":{"status":{"statusCode":"AUTHENTICATION_ERROR","statusText":"Invalid API Key"}}}`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
