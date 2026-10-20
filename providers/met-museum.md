# The Met Collection API

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://www.metmuseum.org/
- Docs: https://metmuseum.github.io/
- Probe endpoint: `https://collectionapi.metmuseum.org/public/collection/v1/objects/436535`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **207,360,000 calls/month**
- Derivation: 80/s x 2,592,000 s/month = 207,360,000 calls/month ceiling
- Published rate: 80 requests/second; no registration or API key
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

The Met's collection API. Publishes the highest per-second rate of any museum API here and explicitly needs no key.

## Evidence

> At this time, we do not require API users to register or obtain an API key to use the service.

Source: https://metmuseum.github.io/  
Snapshot: `data/snapshots/met-museum/docs.txt`  

## Live probe

- Request: `GET https://collectionapi.metmuseum.org/public/collection/v1/objects/436535`
- Result: HTTP 200 in 691 ms — **200 JSON**
- Body starts: `{"objectID":436535,"isHighlight":true,"accessionNumber":"1993.132","accessionYear":"1993","isPublicDomain":true,"primaryImage":"https://images.metmuseum.org/CRDImages/ep/original/D`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
