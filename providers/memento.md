# Memento TimeTravel aggregator

- Category: `web-archive` — Web archives & national archive catalogs
- Home: http://timetravel.mementoweb.org/
- Docs: http://timetravel.mementoweb.org/guide/api/
- Probe endpoint: `http://timetravel.mementoweb.org/api/json/2020/https://openalex.org`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: not established
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Aggregator over many archives' Memento endpoints. The host did not resolve from this machine during the probe.

## Live probe

- Request: `GET http://timetravel.mementoweb.org/api/json/2020/https://openalex.org`
- Result: HTTP 0 in 76 ms — **no answer**
- Body starts: `<urlopen error [Errno -2] Name or service not known>`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
