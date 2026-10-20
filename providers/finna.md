# Finna (Finnish libraries)

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://www.finna.fi/
- Docs: https://api.finna.fi/
- Probe endpoint: `https://api.finna.fi/v1/search?lookfor=openalex&limit=1`
- llms.txt: none verified — no llms.txt found; the probe returned HTTP 403

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: not established — the API returned 403 to this client
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Finnish library search. Recorded as unverified.

## Live probe

- Request: `GET https://api.finna.fi/v1/search?lookfor=openalex&limit=1`
- Result: HTTP 403 in 79 ms — **bot wall**
- Body starts: `<!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
