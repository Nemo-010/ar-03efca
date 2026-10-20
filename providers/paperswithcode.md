# Papers with Code

- Category: `repository` — Repositories & research-data archives
- Home: https://paperswithcode.com/
- Docs: https://paperswithcode.com/api/v1/docs/
- Probe endpoint: `https://paperswithcode.com/api/v1/papers/?items_per_page=1`
- llms.txt: none verified — served HTML at a .txt path

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Papers with code links. The API answers, but the captured docs page is a 1.4MB HTML shell.

## Live probe

- Request: `GET https://paperswithcode.com/api/v1/papers/?items_per_page=1`
- Result: HTTP 200 in 1130 ms — **200 HTML**
- Rate-limit headers: `{"RateLimit": "\"pages\";r=98;t=122", "RateLimit-Policy": "\"fixed window\";\"pages\";q=100;w=300"}`
- Body starts: `<!doctype html> <html class=""> <head> <meta charset="utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" /> <meta name="description" `

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
