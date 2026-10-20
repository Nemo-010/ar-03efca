# Wayback Machine CDX

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://web.archive.org/
- Docs: https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server — HTTP 200 at capture
- Probe endpoint: `https://web.archive.org/cdx/search/cdx?url=openalex.org&limit=2&output=json`
- llms.txt: none verified — belongs to github.com, not the provider

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published call quota; the CDX endpoint answers unauthenticated callers
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

The CDX server is the Wayback index API: one call returns capture rows for a URL, filterable and pageable, so a caller controls its own volume. No rate or quota is stated on the captured pages.

## Evidence

> However, the cdx server is freely available with the rest of the open-source wayback machine software in this repository.

Source: https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server  
Snapshot: `data/snapshots/wayback-cdx/docs.txt`  

## Live probe

- Request: `GET https://web.archive.org/cdx/search/cdx?url=openalex.org&limit=2&output=json`
- Result: HTTP 200 in 696 ms — **200 JSON**
- Body starts: `[["urlkey","timestamp","original","mimetype","statuscode","digest","length"], ["org,openalex)/","20130711171335","http://openalex.org","text/html","200","OAHU5W462BNTDE2DKBTUEQD2KC`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
