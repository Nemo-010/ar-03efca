# Project Gutenberg (Gutendex)

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://www.gutenberg.org/
- Docs: https://gutendex.com/
- Probe endpoint: `https://gutendex.com/books/?search=openalex`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no fees and no registration; the mirror is a static file service
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

Project Gutenberg's catalogue, reached here through the Gutendex JSON wrapper. The wrapper is a third-party service, so its own uptime is not Gutenberg's.

## Evidence

> ✓ 100% Free - No fees, no registration, completely free

Source: https://www.gutenberg.org/  
Snapshot: `data/snapshots/gutenberg/home.txt`  

## Live probe

- Request: `GET https://gutendex.com/books/?search=openalex`
- Result: HTTP 200 in 312 ms — **200 JSON**
- Body starts: `{"count":0,"next":null,"previous":null,"results":[]}`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
