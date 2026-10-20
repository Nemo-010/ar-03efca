# Smithsonian Open Access

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://www.si.edu/openaccess
- Docs: https://edan.si.edu/openaccess/apidocs/
- Probe endpoint: `https://api.si.edu/openaccess/api/v1.0/search?q=openalex`
- llms.txt: none verified — HTTP 403

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: api_key required; no call quota captured
- Authentication: free key
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Open Access collection metadata and images. The content itself is released for reuse without asking; the API wants a key.

## Evidence

> Welcome to Smithsonian Open Access, where you can download, share, and reuse millions of the Smithsonian’s images—right now, without asking.

Source: https://www.si.edu/openaccess  
Snapshot: `data/snapshots/smithsonian/home.txt`  

## Live probe

- Request: `GET https://api.si.edu/openaccess/api/v1.0/search?q=openalex`
- Result: HTTP 403 in 626 ms — **needs key**
- Body starts: `{ "error": { "code": "API_KEY_MISSING", "message": "No api_key was supplied. Get one at https://api.si.edu:443" } }`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
