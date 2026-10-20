# Chronicling America

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://chroniclingamerica.loc.gov/
- Docs: https://chroniclingamerica.loc.gov/about/api/
- Probe endpoint: `https://chroniclingamerica.loc.gov/search/pages/results/?andtext=openalex&format=json`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: the legacy dedicated API is retired; the collection is served by the loc.gov API
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Historic US newspapers. The legacy endpoint now 404s; use the loc.gov API, whose limits are recorded on the Library of Congress row.

## Evidence

> Beginning in 2025, the Chronicling America collection is accessible exclusively via the loc.gov API.

Source: https://www.loc.gov/apis/additional-apis/chronicling-america-api/  
Snapshot: `data/snapshots/chroniclingamerica/policy.txt`  

## Live probe

- Request: `GET https://chroniclingamerica.loc.gov/search/pages/results/?andtext=openalex&format=json`
- Result: HTTP 404 in 322 ms — **404**
- Body starts: `<!DOCTYPE html> <html lang="en" class="no-js" prefix="lc: http://loc.gov/#"> <head> <title>Page Not Found -- 404 -- Library of Congress</title> <link href='https://www.loc.gov/stat`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
