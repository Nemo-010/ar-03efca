# ClinicalTrials.gov

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://clinicaltrials.gov/
- Docs: https://clinicaltrials.gov/data-api/api — HTTP 200 at capture
- Probe endpoint: `https://clinicaltrials.gov/api/v2/studies?pageSize=1`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published call quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Trial registry. The v2 API answers keyless with JSON; the captured 'about the API' page rendered as an application shell with no readable text.

## Live probe

- Request: `GET https://clinicaltrials.gov/api/v2/studies?pageSize=1`
- Result: HTTP 200 in 461 ms — **200 JSON**
- Body starts: `{"studies":[ {"protocolSection":{"identificationModule":{"nctId":"NCT02684435","orgStudyIdInfo":{"id":"15-1866"},"organization":{"fullName":"University of North Carolina, Chapel Hi`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
