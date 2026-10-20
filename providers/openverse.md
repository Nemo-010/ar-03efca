# Openverse

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://openverse.org/
- Docs: https://api.openverse.org/v1/
- Probe endpoint: `https://api.openverse.org/v1/images/?q=openalex&page_size=1`
- llms.txt: none verified — no llms.txt found; the probe returned HTTP 404

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: anonymous calls allowed; the API publishes no quota in the captured pages
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Openly licensed images and audio, aggregated across sources. Answers keyless.

## Live probe

- Request: `GET https://api.openverse.org/v1/images/?q=openalex&page_size=1`
- Result: HTTP 200 in 97 ms — **200 JSON**
- Rate-limit headers: `{"x-ratelimit-available-anon_burst": "19", "x-ratelimit-available-anon_sustained": "199", "x-ratelimit-limit-anon_burst": "20/min", "x-ratelimit-limit-anon_sustained": "200/day"}`
- Body starts: `{"result_count":36,"page_count":36,"page_size":1,"page":1,"results":[{"id":"9d30ab5f-ab06-4db7-90ea-4f81196951e8","title":"Academic works by discipline over time (visualization of `

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
