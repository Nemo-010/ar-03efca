# Trove (National Library of Australia)

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://trove.nla.gov.au/
- Docs: https://trove.nla.gov.au/about/create-something/using-api
- Probe endpoint: `https://api.trove.nla.gov.au/v3/result?q=openalex&category=book&n=1`
- llms.txt: none verified — served HTML at a .txt path

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: call rate is set per application level; the table lists 200m for each level
- Authentication: key on application
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

National Library of Australia. Access needs an approved key and the published table lists a call rate per review level; the unit of '200m' is not spelled out, so it is not converted into a monthly figure here.

## Evidence

> Access and Terms of Use On-going use of the Trove API will require an active API key.

Source: https://trove.nla.gov.au/about/create-something/using-api  
Snapshot: `data/snapshots/trove/docs.txt`  

## Live probe

- Request: `GET https://api.trove.nla.gov.au/v3/result?q=openalex&category=book&n=1`
- Result: HTTP 401 in 1074 ms — **needs key**
- Body starts: `{ "message":"No API key found in request", "request_id":"e5d580325a15e071379d716c1c12030d" }`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
