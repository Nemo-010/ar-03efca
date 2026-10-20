# Thoth Open Metadata

- Category: `repository` — Repositories & research-data archives
- Home: https://thoth.pub/
- Docs: https://api.thoth.pub/graphql
- Probe endpoint: `https://api.thoth.pub/`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota; GraphQL and export APIs
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Open-metadata service for book publishers. Metadata is CC0.

## Evidence

> Stay open with open APIs, no lock-in, and CC0-licensed metadata.

Source: https://thoth.pub/  
Snapshot: `data/snapshots/thoth/home.txt`  

## Live probe

- Request: `GET https://api.thoth.pub/`
- Result: HTTP 200 in 967 ms — **200 JSON**
- Body starts: `{"api_name":"Thoth Metadata GraphQL API","api_version":"1.8.0","api_schema":"","public_url":"https://api.thoth.pub/graphql","schema_explorer_url":"https://api.thoth.pub/graphiql"}`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
