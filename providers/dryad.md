# Dryad

- Category: `repository` — Repositories & research-data archives
- Home: https://datadryad.org/
- Docs: https://datadryad.org/api/v2/docs/
- Probe endpoint: `https://datadryad.org/api/v2/search?q=openalex&per_page=1`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Research-data repository. The API docs URL captured returns a redirect stub.

## Live probe

- Request: `GET https://datadryad.org/api/v2/search?q=openalex&per_page=1`
- Result: HTTP 200 in 455 ms — **200 JSON**
- Body starts: `{"_links":{"self":{"href":"/api/v2/search?q=openalex\u0026per_page=1"},"first":{"href":"/api/v2/search?per_page=1\u0026q=openalex"},"last":{"href":"/api/v2/search?page=1\u0026per_p`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
