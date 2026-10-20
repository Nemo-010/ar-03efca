# Software Heritage

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://www.softwareheritage.org/
- Docs: https://archive.softwareheritage.org/api/
- Probe endpoint: `https://archive.softwareheritage.org/api/1/origin/search/openalex/?limit=1`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota; the API documents only its routes
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Source-code archive. The API root answered 200 unauthenticated in the probe; the captured documentation is a machine-readable route list with no rate statement.

## Evidence

> Get information about a content (aka a \"blob\") object

Source: https://archive.softwareheritage.org/api/1/  
Snapshot: `data/snapshots/softwareheritage/limits.txt`  

## Live probe

- Request: `GET https://archive.softwareheritage.org/api/1/origin/search/openalex/?limit=1`
- Result: HTTP 200 in 785 ms — **200 JSON**
- Rate-limit headers: `{"X-Ratelimit-Limit": "10", "X-Ratelimit-Remaining": "8", "X-Ratelimit-Reset": "1792464519"}`
- Body starts: `[{"url":"https://github.com/waterfirst/openalexR","visit_types":["git"],"has_visits":true,"nb_visits":1,"snapshot_id":"140bc59d1402ffd16d8d115977f34911c9f1fea4","last_visit_date":"`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
