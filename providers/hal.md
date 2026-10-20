# HAL Open Archive

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://hal.science/
- Docs: https://api.archives-ouvertes.fr/docs
- Probe endpoint: `https://api.archives-ouvertes.fr/search/?q=openalex&rows=1&wt=json`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published call quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

French national open archive. The search endpoint answered 200 unauthenticated; the documentation captured is an index page with no rate statement.

## Evidence

> Cette page vous donne accès à la documentation des APIs de HAL v3.0.

Source: https://api.archives-ouvertes.fr/docs  
Snapshot: `data/snapshots/hal/limits.txt`  

## Live probe

- Request: `GET https://api.archives-ouvertes.fr/search/?q=openalex&rows=1&wt=json`
- Result: HTTP 200 in 540 ms — **200 JSON**
- Body starts: `{ "response":{ "numFound":77, "start":0, "maxScore":10.245265, "numFoundExact":true, "docs":[{ "docid":"4572223", "label_s":"Frédérique Bordignon. OpenAlex : évolution ou défi pour`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
