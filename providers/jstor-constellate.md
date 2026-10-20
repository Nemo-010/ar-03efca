# JSTOR / Constellate

- Category: `publisher` — Publisher & patent TDM endpoints
- Home: https://www.jstor.org/
- Docs: https://constellate.org/docs/
- Probe endpoint: `https://api.constellate.org/`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: not established; the API host did not resolve
- Authentication: ?
- Payment card for the free tier: not stated
- Evidence confidence: **low**

## Notes

JSTOR's text-analysis service. Recorded as unverified.

## Live probe

- Request: `GET https://api.constellate.org/`
- Result: HTTP 0 in 126 ms — **no answer**
- Body starts: `<urlopen error [Errno -2] Name or service not known>`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
