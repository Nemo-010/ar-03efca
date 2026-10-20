# OBIS

- Category: `data-api` — Life / physical science data APIs
- Home: https://obis.org/
- Docs: https://api.obis.org/
- Probe endpoint: `https://api.obis.org/v3/occurrence?size=1`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Ocean biodiversity. The v3 API answers keyless; the captured landing page is a stub.

## Live probe

- Request: `GET https://api.obis.org/v3/occurrence?size=1`
- Result: HTTP 200 in 885 ms — **200 JSON**
- Body starts: `{"total":228719495,"results":[{"basisOfRecord":"MaterialSample","bibliographicCitation":"Brown, M. V. et al. Continental scale monitoring of marine microbiota by the Australian Mar`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
