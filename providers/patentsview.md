# PatentsView

- Category: `publisher` — Publisher & patent TDM endpoints
- Home: https://patentsview.org/
- Docs: https://patentsview.org/apis/api-endpoints
- Probe endpoint: `https://api.patentsview.org/patents/query?q=%7B%22_gte%22%3A%7B%22patent_date%22%3A%222020-01-01%22%7D%7D`
- llms.txt: none verified — served HTML at a .txt path

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: API key required; the docs page rendered as an application shell
- Authentication: key on application
- Payment card for the free tier: not stated
- Evidence confidence: **low**

## Notes

US patent data. The endpoint answered HTML rather than JSON to the probe, so it is recorded as unverified.

## Live probe

- Request: `GET https://api.patentsview.org/patents/query?q=%7B%22_gte%22%3A%7B%22patent_date%22%3A%222020-01-01%22%7D%7D`
- Result: HTTP 200 in 1208 ms — **200 HTML**
- Body starts: `<!doctype html> <html lang="en" data-beasties-container> <head><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> <meta charset="utf-8"> <base href="/"> <meta nam`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
