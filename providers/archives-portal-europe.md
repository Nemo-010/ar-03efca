# Archives Portal Europe

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://www.archivesportaleurope.net/
- Docs: https://www.archivesportaleurope.net/information/api — HTTP 404 at capture (see Notes)
- Probe endpoint: `https://www.archivesportaleurope.net/OAI-PMH/?verb=Identify`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: OAI-PMH endpoint answered 404 at the documented path
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Aggregates European archive catalogues. The OAI-PMH path in the probe returned 404, so the endpoint recorded here is unverified.

## Evidence

> This object is made available under the Creative Commons CC0 1.0 Public Domain Dedication .

Source: https://www.archivesportaleurope.net/  
Snapshot: `data/snapshots/archives-portal-europe/home.txt`  

## Live probe

- Request: `GET https://www.archivesportaleurope.net/OAI-PMH/?verb=Identify`
- Result: HTTP 404 in 2169 ms — **404**
- Body starts: `<!DOCTYPE html> <html lang="en"> <head> <script type="application/ld+json"> { "@context" : "https://schema.org", "@type" : "WebSite", "name" : "Archives Portal Europe", "alternateN`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
