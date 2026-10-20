# ORCID Public API

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://orcid.org/
- Docs: https://info.orcid.org/documentation/api-reference/
- Probe endpoint: `https://pub.orcid.org/v3.0/expanded-search/?q=openalex&rows=1`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: public API; the rate-limit page was not captured
- Authentication: free key
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Researcher identifiers. The public API answered 200 unauthenticated; the documentation site returned 404 for every path tried, so no number is claimed.

## Live probe

- Request: `GET https://pub.orcid.org/v3.0/expanded-search/?q=openalex&rows=1`
- Result: HTTP 200 in 251 ms — **200 JSON**
- Body starts: `{"expanded-result":[{"orcid-id":"0000-0003-0245-6063","given-names":"Okan","family-names":"Arslan","credit-name":null,"other-name":[],"email":["okan@westga.edu"],"institution-name"`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
