# US National Archives Catalog

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://www.archives.gov/research/catalog
- Docs: https://www.archives.gov/research/catalog/help/api
- Probe endpoint: `https://catalog.archives.gov/api/v2/records/search?q=openalex`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **10,000 calls/month**
- Derivation: published monthly figure, not a rate conversion
- Published rate: 10,000 queries/month per API key (default); higher tiers to 1.5M/month
- Authentication: key on application
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

US National Archives Catalog API. The only provider here that publishes a plain monthly call quota with named higher tiers. A keyless call gets the single-page application shell rather than JSON, which is what the probe recorded — the quota is real, but the endpoint is not open.

## Evidence

> NARA limits the number of Catalog API requests to a default rate of 10,000 queries per month per API key.

Source: https://www.archives.gov/research/catalog/help/api  
Snapshot: `data/snapshots/nara/docs.txt`  

## Live probe

- Request: `GET https://catalog.archives.gov/api/v2/records/search?q=openalex`
- Result: HTTP 200 in 293 ms — **200 HTML**
- Body starts: `<!doctype html><html lang="en"><head><script>var hostname=window.location.hostname,scriptSources="'self' 'unsafe-inline' https://www.google-analytics.com https://www.googletagmanag`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
