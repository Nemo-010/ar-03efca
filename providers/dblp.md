# dblp computer science bibliography

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://dblp.org/
- Docs: https://dblp.org/faq/How+to+use+the+dblp+search+API.html
- Probe endpoint: `https://dblp.org/search/publ/api?q=openalex&format=json&h=1`
- llms.txt: none verified — HTTP 202

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota; the site answers a JS challenge to non-browser clients
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Computer-science bibliography. The live probe returned 202 with an interstitial, so the JSON API is reachable only through a client that runs the challenge; the archived copy of the FAQ is what is quoted here.

## Evidence

> Part of the search API is still in flux.

Source: https://web.archive.org/web/20260723200605/https://dblp.org/faq/How+to+use+the+dblp+search+API.html  
Snapshot: `data/snapshots/dblp/docs.txt`  

## Live probe

- Request: `GET https://dblp.org/search/publ/api?q=openalex&format=json&h=1`
- Result: HTTP 202 in 519 ms — **200 HTML**
- Body starts: `<!doctype html><html lang="en"><head><title>Making sure you&#39;re not a bot!</title><link rel="stylesheet" href="/.within.website/x/xess/xess.min.css?cachebuster=v1.27.0"><meta na`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
