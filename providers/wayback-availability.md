# Wayback Availability API

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://archive.org/
- Docs: https://archive.org/developers/wayback-cdx-server.html
- Probe endpoint: `https://archive.org/wayback/available?url=openalex.org`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Single-URL availability check: returns the closest capture and its URL. Answered 200 in the live probe with no key.

## Evidence

> Internet Archive: Digital Library of Free & Borrowable Texts, Movies, Music & Wayback Machine

Source: https://archive.org/  
Snapshot: `data/snapshots/wayback-availability/home.txt`  

## Live probe

- Request: `GET https://archive.org/wayback/available?url=openalex.org`
- Result: HTTP 200 in 464 ms — **200 JSON**
- Body starts: `{"url": "openalex.org", "archived_snapshots": {"closest": {"status": "200", "available": true, "url": "http://web.archive.org/web/20261019015148/https://openalex.org/", "timestamp"`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
