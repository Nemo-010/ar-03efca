# DataCite REST API

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://datacite.org/
- Docs: https://support.datacite.org/docs/api
- Probe endpoint: `https://api.datacite.org/dois?query=openalex&page%5Bsize%5D=1`
- llms.txt: https://support.datacite.org/llms.txt

## Free access

- Documented volume: **4,320,000 calls/month**
- Derivation: 500 per 5 min = 100/min x 1,440 x 30 = 4,320,000 calls/month ceiling
- Published rate: 500 requests/5min unidentified, 1,000 identified (mailto), 3,000 authenticated
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

DOI metadata for research data. Three tiers keyed on how the caller identifies itself; the lowest tier needs nothing at all.

## Evidence

> | 500 requests per 5 minutes per IP address |

Source: https://support.datacite.org/docs/rate-limit.md  
Snapshot: `data/snapshots/datacite/ratelimits.txt`  

## Live probe

- Request: `GET https://api.datacite.org/dois?query=openalex&page%5Bsize%5D=1`
- Result: HTTP 200 in 1083 ms — **200 JSON**
- Body starts: `{"data":[{"id":"10.17605/osf.io/25c4a","type":"dois","attributes":{"doi":"10.17605/osf.io/25c4a","identifiers":[{"identifier":"https://osf.io/25c4a","identifierType":"URL"}],"creat`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
