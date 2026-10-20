# re3data

- Category: `repository` — Repositories & research-data archives
- Home: https://www.re3data.org/
- Docs: https://www.re3data.org/api/doc
- Probe endpoint: `https://www.re3data.org/api/v1/repositories?query=openalex`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota; the API is a plain REST interface
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Registry of research-data repositories — useful for finding a repository, not for content.

## Evidence

> re3data.org supports the retrievial of its content via API.

Source: https://www.re3data.org/api/doc  
Snapshot: `data/snapshots/re3data/docs.txt`  

## Live probe

- Request: `GET https://www.re3data.org/api/v1/repositories?query=openalex`
- Result: HTTP 200 in 2810 ms — **200 JSON**
- Body starts: `<?xml version="1.0" encoding="UTF-8"?> <list> <repository> <id>r3d100000001</id> <doi>https://doi.org/10.17616/R31NJCHT</doi> <name>Odum Institute Archive Dataverse</name> <link hr`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
