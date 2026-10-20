# id.loc.gov (LC Linked Data)

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://id.loc.gov/
- Docs: https://id.loc.gov/
- Probe endpoint: `https://id.loc.gov/search/?q=openalex&format=json`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: not established — the search endpoint returned 403
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Library of Congress linked-data service. Recorded as unverified.

## Live probe

- Request: `GET https://id.loc.gov/search/?q=openalex&format=json`
- Result: HTTP 403 in 76 ms — **bot wall**
- Body starts: `<!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
