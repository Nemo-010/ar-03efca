# OAPEN Library

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://www.oapen.org/
- Docs: https://library.oapen.org/rest/
- Probe endpoint: `https://library.oapen.org/rest/search?query=openalex&expand=metadata&limit=1`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published call quota captured
- Authentication: free key
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Open-access book library. The REST search answered 403 to this client and the site API returns an HTML shell, so nothing is claimed.

## Evidence

> OAPEN connects libraries , publishers , researchers , and funders with a global infrastructure for peer-reviewed open access books

Source: https://www.oapen.org/  
Snapshot: `data/snapshots/oapen/home.txt`  

## Live probe

- Request: `GET https://library.oapen.org/rest/search?query=openalex&expand=metadata&limit=1`
- Result: HTTP 403 in 538 ms — **needs key**
- Body starts: `You address is not allowed to access this API.`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
