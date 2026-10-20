# Europeana

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://www.europeana.eu/
- Docs: https://europeana.atlassian.net/wiki/spaces/EF/pages/2477260801/API+documentation — HTTP 200 at capture
- Probe endpoint: `https://api.europeana.eu/record/v2/search.json?query=openalex&wskey=api2demo&rows=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published call quota; a demo key (`wskey=api2demo`) works on the record API
- Authentication: free key
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Europeana's search API answers with the public demo key. The documented documentation URL moved; the captured page is a Confluence 'page not found', so nothing about quotas is claimed.

## Evidence

> You‘re viewing this with anonymous access, so some content might be blocked.

Source: https://europeana.atlassian.net/wiki/spaces/EF/pages/2477260801/API+documentation  
Snapshot: `data/snapshots/europeana/docs.txt`  

## Live probe

- Request: `GET https://api.europeana.eu/record/v2/search.json?query=openalex&wskey=api2demo&rows=1`
- Result: HTTP 200 in 386 ms — **200 JSON**
- Rate-limit headers: `{"ratelimit": "\"project\";r=993901;t=691", "ratelimit-policy": "\"project\";q=1000000;w=3600"}`
- Body starts: `{"apikey":"api2demo","success":true,"requestNumber":999,"itemsCount":0,"totalResults":0,"items":[]}`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
