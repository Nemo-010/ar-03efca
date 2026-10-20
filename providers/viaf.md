# VIAF

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://viaf.org/
- Docs: https://viaf.org/viaf/data/
- Probe endpoint: `https://viaf.org/viaf/AutoSuggest?query=openalex`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: not established; the data page returned 403
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Virtual International Authority File. The AutoSuggest endpoint answered keyless; OCLC's developer page documents the API but states no rate in the captured text.

## Evidence

> With the VIAF API, you can: Search for authority data by keyword, local name, preferred name form, title, source, or control number of source records

Source: https://www.oclc.org/developer/api/oclc-apis/viaf.en.html  
Snapshot: `data/snapshots/viaf/docs.txt`  

## Live probe

- Request: `GET https://viaf.org/viaf/AutoSuggest?query=openalex`
- Result: HTTP 200 in 203 ms — **200 JSON**
- Rate-limit headers: `{"Ratelimit-Limit": "1003", "Ratelimit-Remaining": "999", "Ratelimit-Reset": "76279", "X-Ratelimit-Limit-Day": "1003", "X-Ratelimit-Remaining-Day": "999"}`
- Body starts: `{"query":"openalex","result":null} `

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
