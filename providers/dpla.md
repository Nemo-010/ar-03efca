# Digital Public Library of America

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://dp.la/
- Docs: https://pro.dp.la/developers/api-codex — HTTP 403 at capture (see Notes)
- Probe endpoint: `https://api.dp.la/v2/items?q=openalex`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: not established (API key required; docs are behind a 403 for this client)
- Authentication: free key
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Digital Public Library of America. Every documentation URL tried returned 403 to this client, so the free tier is recorded as unverified rather than guessed.

## Live probe

- Request: `GET https://api.dp.la/v2/items?q=openalex`
- Result: HTTP 403 in 446 ms — **needs key**
- Body starts: `{"error":"invalid_api_key","message":"Invalid or inactive API key.","documentation":"https://pro.dp.la/developers/responses#errors"}`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
