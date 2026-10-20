# J-STAGE

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://www.jstage.jst.go.jp/
- Docs: https://www.jstage.jst.go.jp/static/pages/JstageServices/TAB3/-char/en
- Probe endpoint: `https://api.jstage.jst.go.jp/searchapi/do?service=3&q=openalex&count=1`
- llms.txt: none verified — HTTP 0

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Japanese science and technology journals. WebAPI returns XML metadata keyless.

## Evidence

> J-STAGE WebAPI is an application programming interface (API) that enables users to retrieve metadata for J-STAGE content in XML format.

Source: https://www.jstage.jst.go.jp/static/pages/JstageServices/TAB3/-char/en  
Snapshot: `data/snapshots/jstage/docs.txt`  

## Live probe

- Request: `GET https://api.jstage.jst.go.jp/searchapi/do?service=3&q=openalex&count=1`
- Result: HTTP 200 in 968 ms — **200 JSON**
- Body starts: `<?xml version="1.0" encoding="UTF-8"?> <feed xmlns="http://www.w3.org/2005/Atom" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns:opensearch="http://a9.com/-/spec`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
