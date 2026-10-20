# Library of Congress JSON API

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://www.loc.gov/
- Docs: https://www.loc.gov/apis/
- Probe endpoint: `https://www.loc.gov/books/?q=openalex&fo=json`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **864,000 calls/month**
- Derivation: 20/min x 1,440 min/day x 30 = 864,000 calls/month ceiling
- Published rate: 20 requests/minute for the JSON/YAML API; 150/min for text and image services
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

Library of Congress. Publishes a per-service rate table and the block duration for exceeding it, which is unusually precise for a public API.

## Evidence

> The API is accessible to the public with no API key or authentication required.

Source: https://www.loc.gov/apis/json-and-yaml/working-within-limits/  
Snapshot: `data/snapshots/loc/loclimits.txt`  

## Live probe

- Request: `GET https://www.loc.gov/books/?q=openalex&fo=json`
- Result: HTTP 403 in 96 ms — **bot wall**
- Body starts: `<!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
