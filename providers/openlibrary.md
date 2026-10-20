# Open Library

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://openlibrary.org/
- Docs: https://openlibrary.org/developers/api
- Probe endpoint: `https://openlibrary.org/search.json?q=openalex&limit=1`
- llms.txt: https://docs.openlibrary.org/llms.txt

## Free access

- Documented volume: **2,592,000 calls/month**
- Derivation: 1/s x 2,592,000 s/month = 2,592,000 calls/month ceiling
- Published rate: 1 request/second unidentified; 3 requests/second with a User-Agent carrying an email
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

Internet Archive's book catalogue. Identifies callers by User-Agent and gives them 3x.

## Evidence

> Default (non-identified requests): 1 request per second

Source: https://openlibrary.org/developers/api  
Snapshot: `data/snapshots/openlibrary/docs.txt`  

## Live probe

- Request: `GET https://openlibrary.org/search.json?q=openalex&limit=1`
- Result: HTTP 200 in 580 ms — **200 JSON**
- Body starts: `{"numFound":0,"start":0,"numFoundExact":true,"num_found":0,"documentation_url":"https://openlibrary.org/dev/docs/api/search","q":"openalex","offset":null,"docs":[]}`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
