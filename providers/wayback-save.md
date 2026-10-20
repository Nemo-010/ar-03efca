# Wayback Save Page Now

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://web.archive.org/save
- Docs: https://archive.org/developers/
- Probe endpoint: `https://web.archive.org/save/status/https://example.com`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: Save Page Now is rate-limited per account in practice; no number captured
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Write endpoint. The status endpoint answered 200 unauthenticated in the probe, but no documented allowance survived capture.

## Evidence

> All of these are in digital form and freely available to anyone with an internet connection.

Source: https://archive.org/developers/  
Snapshot: `data/snapshots/wayback-save/docs.txt`  

## Live probe

- Request: `GET https://web.archive.org/save/status/https://example.com`
- Result: HTTP 200 in 426 ms — **200 JSON**
- Body starts: `{"status":"error","status_ext":"error:404","message":"The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.","exc`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
