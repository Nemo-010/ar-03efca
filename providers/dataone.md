# DataONE

- Category: `repository` — Repositories & research-data archives
- Home: https://www.dataone.org/
- Docs: https://purl.dataone.org/architecture/apis/MN-API.html
- Probe endpoint: `https://cn.dataone.org/cn/v2/query/solr/?q=openalex&rows=1&wt=json`
- llms.txt: none verified — HTTP 401

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: not established
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Earth-observation data network. The Solr query endpoint answered 200 keyless; the documentation URL captured is an authorisation error page.

## Live probe

- Request: `GET https://cn.dataone.org/cn/v2/query/solr/?q=openalex&rows=1&wt=json`
- Result: HTTP 200 in 693 ms — **200 JSON**
- Body starts: `{ "responseHeader":{ "zkConnected":true, "status":0, "QTime":0, "params":{ "q":"openalex", "rows":"1", "wt":"json" } }, "response":{ "numFound":19, "start":0, "numFoundExact":true,`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
