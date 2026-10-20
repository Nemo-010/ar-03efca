# INSPIRE-HEP

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://inspirehep.net/
- Docs: https://github.com/inspirehep/rest-api-doc
- Probe endpoint: `https://inspirehep.net/api/literature?q=openalex&size=1`
- llms.txt: none verified — served HTML at a .txt path

## Free access

- Documented volume: **7,776,000 calls/month**
- Derivation: 15 per 5 s = 180/min x 1,440 x 30 = 7,776,000 calls/month ceiling
- Published rate: 15 requests per 5-second window per IP address
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

High-energy-physics literature. Blocked requests still count against the window, which the docs warn about explicitly.

## Evidence

> every IP address is allowed 15 requests in a 5s window.

Source: https://github.com/inspirehep/rest-api-doc  
Snapshot: `data/snapshots/inspirehep/docs.txt`  

## Live probe

- Request: `GET https://inspirehep.net/api/literature?q=openalex&size=1`
- Result: HTTP 200 in 547 ms — **200 JSON**
- Body starts: `{"hits":{"hits":[{"links":{"bibtex":"https://inspirehep.net/api/literature/3066924?format=bibtex","latex-eu":"https://inspirehep.net/api/literature/3066924?format=latex-eu","latex-`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
