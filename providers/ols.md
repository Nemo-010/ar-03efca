# EMBL-EBI Ontology Lookup Service

- Category: `data-api` — Life / physical science data APIs
- Home: https://www.ebi.ac.uk/ols4/
- Docs: https://www.ebi.ac.uk/ols4/help — HTTP 200 at capture
- Probe endpoint: `https://www.ebi.ac.uk/ols4/api/search?q=openalex&rows=1`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Ontology lookup. Answers keyless; the captured help page is a short landing page.

## Live probe

- Request: `GET https://www.ebi.ac.uk/ols4/api/search?q=openalex&rows=1`
- Result: HTTP 200 in 644 ms — **200 JSON**
- Body starts: `{"response":{"docs":[{"iri":"https://ror.org/02nr0ka47","ontology_name":"ror","related_synonyms":["Impactstory","OurResearch"],"ontology_prefix":"ror","short_form":"ror_02nr0ka47",`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
