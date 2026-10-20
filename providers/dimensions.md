# Dimensions

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://www.dimensions.ai/
- Docs: https://docs.dimensions.ai/dsl/api.html
- Probe endpoint: `https://api.dimensions.ai/v2/publications?search_text=openalex`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **1,296,000 calls/month**
- Derivation: 30/min x 1,440 x 30 = 1,296,000 calls/month ceiling, but eligibility is restricted
- Published rate: 30 requests/minute per IP; free access only for eligible research projects
- Authentication: key on application
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

The rate is published, but free access is granted to eligible scientometric research projects rather than to anyone who signs up, so the ceiling is not generally available.

## Evidence

> The Analytics API and the CRIS API are limited to 30 requests per IP address per minute.

Source: https://docs.dimensions.ai/dsl/api.html  
Snapshot: `data/snapshots/dimensions/docs.txt`  

## Live probe

- Request: `GET https://api.dimensions.ai/v2/publications?search_text=openalex`
- Result: HTTP 0 in 27 ms — **no answer**
- Body starts: `<urlopen error [Errno -2] Name or service not known>`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
