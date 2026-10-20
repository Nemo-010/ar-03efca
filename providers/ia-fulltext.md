# Internet Archive Full-Text Search

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://archive.org/search
- Docs: https://archive.org/developers/search_inside.html
- Probe endpoint: `https://ia-fts.archive.org/api/v1/search/hits?q=openalex&size=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Full-text search inside archived books. The endpoint refused connections from this machine during the probe, so nothing is claimed about it.

## Evidence

> Internet Archive: Digital Library of Free & Borrowable Texts, Movies, Music & Wayback Machine

Source: https://archive.org/search  
Snapshot: `data/snapshots/ia-fulltext/home.txt`  

## Live probe

- Request: `GET https://ia-fts.archive.org/api/v1/search/hits?q=openalex&size=1`
- Result: HTTP 0 in 165 ms — **no answer**
- Body starts: `<urlopen error [Errno -2] Name or service not known>`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
