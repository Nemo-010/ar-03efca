# iDigBio

- Category: `data-api` — Life / physical science data APIs
- Home: https://www.idigbio.org/
- Docs: https://github.com/iDigBio/idigbio-search-api/wiki — HTTP 200 at capture
- Probe endpoint: `https://search.idigbio.org/v2/search/records/?q=openalex&limit=1&fields=uuid`
- llms.txt: none verified — belongs to github.com, not the provider

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: anonymous calls allowed; authenticating raises the limit
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Natural-history specimens. The wiki documents the v2 search API and asks users to join a mailing list so changes can be announced; no call rate is published, and the loading/limits page could not be captured as text.

## Evidence

> It uses technology and patterns common in other parts of iDigBio to build a wrapper around the full Elasticsearch API, exposing a minimal subset.

Source: https://github.com/iDigBio/idigbio-search-api/wiki  
Snapshot: `data/snapshots/idigbio/docs.txt`  

## Live probe

- Request: `GET https://search.idigbio.org/v2/search/records/?q=openalex&limit=1&fields=uuid`
- Result: HTTP 200 in 2357 ms — **200 JSON**
- Body starts: `{"itemCount":150902163,"lastModified":"2026-04-23T18:06:26.502Z","items":[{"uuid":"7f61e2b6-5524-40a3-a7f2-c32374f2b1b7","type":"records","data":{},"indexTerms":{"uuid":"7f61e2b6-5`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
