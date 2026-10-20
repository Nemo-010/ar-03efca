# Perma.cc

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://perma.cc/
- Docs: https://perma.cc/docs/developer
- Probe endpoint: `https://api.perma.cc/v1/public/archives/?limit=1`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: public-archive endpoints need no key; the rest need an API key
- Authentication: key on application
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Library-run link permanence service. The public-archives listing is readable without a key; creating links needs an account.

## Evidence

> You do not need an API Key to use this portion of the API.

Source: https://perma.cc/docs/developer  
Snapshot: `data/snapshots/perma/docs.txt`  

## Live probe

- Request: `GET https://api.perma.cc/v1/public/archives/?limit=1`
- Result: HTTP 200 in 450 ms — **200 JSON**
- Body starts: `{"meta":{"limit":1,"next":"https://api.perma.cc/v1/public/archives/?limit=1&offset=1","offset":0,"previous":null},"objects":[{"guid":"M4DC-LKJ2","creation_timestamp":"2026-10-20T02`
- Earlier attempts (kept, not overwritten): HTTP 403 bot wall at 2026-10-20T02:48:13

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
