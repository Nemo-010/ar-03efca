# SNAC API

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://snaccooperative.org/
- Docs: https://api.snaccooperative.org/
- Probe endpoint: `https://api.snaccooperative.org/`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: not established
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Social Networks and Archival Context. The API root answers 400 to a bare GET (it wants a query), so the probe proves the host answers but not the allowance.

## Live probe

- Request: `GET https://api.snaccooperative.org/`
- Result: HTTP 400 in 328 ms — **no answer**
- Body starts: `{ "error": { "type": "Input Error", "message": "No input given to the server" }, "timing": 1.89 }`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
