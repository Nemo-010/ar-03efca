# Gallica (BnF)

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://gallica.bnf.fr/
- Docs: https://api.bnf.fr/api-gallica-de-recherche
- Probe endpoint: `https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&query=gallica%20all%20%22openalex%22&maximumRecords=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: SRU service; no call quota published in the captured pages
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

BnF's digital library. Exposes an SRU endpoint with the standard maximumRecords paging parameter; the documentation is in French and states no rate.

## Evidence

> maximumRecords : il s'agit du nombre de résultats retournés par le service SRU.

Source: https://api.bnf.fr/api-gallica-de-recherche  
Snapshot: `data/snapshots/gallica/docs.txt`  

## Live probe

- Request: `GET https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&query=gallica%20all%20%22openalex%22&maximumRecords=1`
- Result: HTTP 403 in 368 ms — **bot wall**
- Body starts: `<!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content`
- Earlier attempts (kept, not overwritten): HTTP 200 200 JSON at 2026-10-20T02:48:15

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
