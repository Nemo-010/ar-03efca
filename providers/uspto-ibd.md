# USPTO Open Data Portal (IBD)

- Category: `publisher` — Publisher & patent TDM endpoints
- Home: https://developer.uspto.gov/
- Docs: https://developer.uspto.gov/api-catalog
- Probe endpoint: `https://developer.uspto.gov/ibd-api/v1/application/publications?publicationTitleText=engine`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured; the API answered HTML rather than JSON
- Authentication: ?
- Payment card for the free tier: not stated
- Evidence confidence: **low**

## Notes

USPTO Open Data Portal. Recorded as unverified: the endpoint returned a single-page application shell.

## Live probe

- Request: `GET https://developer.uspto.gov/ibd-api/v1/application/publications?publicationTitleText=engine`
- Result: HTTP 200 in 1733 ms — **200 HTML**
- Body starts: `<!doctype html> <html lang="en" data-beasties-container> <head><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> <meta charset="utf-8"> <base href="/"> <meta nam`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
