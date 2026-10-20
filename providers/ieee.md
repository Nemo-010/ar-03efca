# IEEE Xplore API

- Category: `publisher` — Publisher & patent TDM endpoints
- Home: https://developer.ieee.org/
- Docs: https://developer.ieee.org/docs
- Probe endpoint: `https://ieeexploreapi.ieee.org/api/v1/search/articles?querytext=openalex`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: API key required; the docs page did not state a free quota
- Authentication: key on application
- Payment card for the free tier: not stated
- Evidence confidence: **medium**

## Notes

IEEE Xplore metadata API. Answers 403 without a key. Up to 25 DOIs per metadata call.

## Evidence

> Digital Object Identifier (DOI) API Query up to 25 DOI (Digital Object Identifier) numbers and retrieve metadata records including abstracts.

Source: https://developer.ieee.org/docs  
Snapshot: `data/snapshots/ieee/docs.txt`  

## Live probe

- Request: `GET https://ieeexploreapi.ieee.org/api/v1/search/articles?querytext=openalex`
- Result: HTTP 403 in 357 ms — **needs key**
- Body starts: `<h1>Developer Inactive</h1>`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
