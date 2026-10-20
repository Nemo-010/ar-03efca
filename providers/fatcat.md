# Internet Archive Scholar / fatcat

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://scholar.archive.org/
- Docs: https://api.fatcat.wiki/ — not captured (see Notes)
- Probe endpoint: `https://api.fatcat.wiki/v0/release/lookup?doi=10.1038/nature12373`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

IA Scholar's bibliographic API. DNS for api.fatcat.wiki did not resolve from this machine during the probe, so the endpoint could not be exercised.

## Evidence

> This service provides fulltext searching for research publications archived in Internet Archive's various collections.

Source: https://scholar.archive.org/help  
Snapshot: `data/snapshots/fatcat/policy2.txt`  

## Live probe

- Request: `GET https://api.fatcat.wiki/v0/release/lookup?doi=10.1038/nature12373`
- Result: HTTP 0 in 25356 ms — **no answer**
- Body starts: `<urlopen error timed out>`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
