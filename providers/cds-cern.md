# CERN Document Server

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://cds.cern.ch/
- Docs: https://cds.cern.ch/help/hacking
- Probe endpoint: `https://cds.cern.ch/search?p=openalex&of=recjson&rg=1`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured; the site now runs an Anubis proof-of-work check
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

CERN Document Server. The search endpoint answered after a delay, but the captured pages are the Anubis interstitial, so the practical route is the API rather than the HTML site.

## Evidence

> You are seeing this because the administrator of this website has set up Anubis to protect the server

Source: https://cds.cern.ch/help/hacking  
Snapshot: `data/snapshots/cds-cern/docs.txt`  

## Live probe

- Request: `GET https://cds.cern.ch/search?p=openalex&of=recjson&rg=1`
- Result: HTTP 200 in 514 ms — **200 HTML**
- Body starts: `<!doctype html><html lang="en"><head><title>Making sure you&#39;re not a bot!</title><link rel="stylesheet" href="/.within.website/x/xess/xess.min.css?cachebuster=v1.27.0"><meta na`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
