# OpenReview

- Category: `repository` — Repositories & research-data archives
- Home: https://openreview.net/
- Docs: https://docs.openreview.net/reference/api-v2 — HTTP 200 at capture
- Probe endpoint: `https://api2.openreview.net/notes?limit=1`
- llms.txt: https://docs.openreview.net/llms.txt

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published call quota captured
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Peer-review platform. The v2 notes endpoint needs an invitation parameter and answers 403 to a bare call, so nothing is claimed about an allowance.

## Evidence

> API V2 | OpenReview

Source: https://docs.openreview.net/reference/api-v2  
Snapshot: `data/snapshots/openreview/docs.txt`  

## Live probe

- Request: `GET https://api2.openreview.net/notes?limit=1`
- Result: HTTP 200 in 644 ms — **200 HTML**
- Body starts: `<!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1" /> <link href="https://fonts.gstatic.com" rel="`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
