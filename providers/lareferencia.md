# LA Referencia

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://www.lareferencia.info/
- Docs: https://api.lareferencia.info/v1/
- Probe endpoint: `https://api.lareferencia.info/v1/search?query=openalex`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: not established — the API host did not resolve
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Regional aggregator. Recorded as unverified: DNS for api.lareferencia.info did not resolve.

## Live probe

- Request: `GET https://api.lareferencia.info/v1/search?query=openalex`
- Result: HTTP 0 in 27 ms — **no answer**
- Body starts: `<urlopen error [Errno -2] Name or service not known>`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
