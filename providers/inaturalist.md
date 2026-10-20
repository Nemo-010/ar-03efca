# iNaturalist

- Category: `data-api` — Life / physical science data APIs
- Home: https://www.inaturalist.org/
- Docs: https://api.inaturalist.org/v1/docs/ — HTTP 200 at capture
- Probe endpoint: `https://api.inaturalist.org/v1/observations?per_page=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured; the recommendations page returned 403
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Citizen-science observations. The API answers keyless; the recommended-practices page could not be captured from this client.

## Evidence

> All iNaturalist observations are open and freely available

Source: https://www.inaturalist.org/  
Snapshot: `data/snapshots/inaturalist/home.txt`  

## Live probe

- Request: `GET https://api.inaturalist.org/v1/observations?per_page=1`
- Result: HTTP 200 in 617 ms — **200 JSON**
- Body starts: `{"total_results":395088120,"page":1,"per_page":1,"results":[{"quality_grade":"casual","time_observed_at":"2026-10-19T22:49:23-03:00","taxon_geoprivacy":null,"annotations":[],"uuid"`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
