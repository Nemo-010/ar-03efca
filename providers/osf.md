# OSF (Open Science Framework)

- Category: `repository` — Repositories & research-data archives
- Home: https://osf.io/
- Docs: https://developer.osf.io/ — HTTP 200 at capture
- Probe endpoint: `https://api.osf.io/v2/nodes/?page%5Bsize%5D=1`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Open Science Framework. The API root answers with a JSON welcome document but the docs site captured is a stub.

## Live probe

- Request: `GET https://api.osf.io/v2/nodes/?page%5Bsize%5D=1`
- Result: HTTP 200 in 761 ms — **200 JSON**
- Body starts: `{"data":[{"id":"mdyxj","type":"nodes","attributes":{"title":"Assessing the Potential of Music-Induced Flow as an Alternative to Mindfulness Meditation","description":"This review e`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
