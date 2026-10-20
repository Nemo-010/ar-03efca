# OAPEN REST API

- Category: `repository` — Repositories & research-data archives
- Home: https://www.oapen.org/
- Docs: https://api.oapen.org/
- Probe endpoint: `https://api.oapen.org/search?query=openalex`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota; the API returns an HTML page rather than JSON
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Recorded honestly: this endpoint answered 200 but with HTML, so it is not a working JSON API as configured here.

## Evidence

> OAPEN connects libraries , publishers , researchers , and funders with a global infrastructure for peer-reviewed open access books

Source: https://api.oapen.org/  
Snapshot: `data/snapshots/oapen-api/home.txt`  

## Live probe

- Request: `GET https://api.oapen.org/search?query=openalex`
- Result: HTTP 200 in 864 ms — **200 HTML**
- Body starts: `<!doctype html> <html lang="en" data-bulma-theme="light"> <head> <meta charset="utf-8"/> <meta content="text/html; charset=UTF-8" http-equiv="Content-Type"> <meta name="viewport" c`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
