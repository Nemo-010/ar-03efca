# Wiley TDM API

- Category: `publisher` — Publisher & patent TDM endpoints
- Home: https://www.wiley.com/
- Docs: https://onlinelibrary.wiley.com/library-info/resources/text-and-datamining — HTTP 403 at capture (see Notes)
- Probe endpoint: `https://api.wiley.com/onlinelibrary/tdm/v1/articles/10.1002%2Fadvs.201900001`
- llms.txt: none verified — no llms.txt found; the probe returned HTTP 403

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: TDM API token required; no free allowance captured
- Authentication: paid only
- Payment card for the free tier: not stated
- Evidence confidence: **low**

## Notes

Text and data mining endpoint. Answers 400 without a token; the captured pages are marketing copy.

## Live probe

- Request: `GET https://api.wiley.com/onlinelibrary/tdm/v1/articles/10.1002%2Fadvs.201900001`
- Result: HTTP 400 in 339 ms — **no answer**

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
