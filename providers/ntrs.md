# NASA NTRS

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://ntrs.nasa.gov/
- Docs: https://sti.nasa.gov/ntrs-api/ — HTTP 404 at capture (see Notes)
- Probe endpoint: `https://ntrs.nasa.gov/api/citations/search?q=openalex&page.size=1`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

NASA technical reports. The site states the content is publicly available; the API answers keyless.

## Evidence

> The NASA Technical Reports Server (NTRS) provides access to NASA metadata records, full-text online documents, images, and videos.

Source: https://ntrs.nasa.gov/  
Snapshot: `data/snapshots/ntrs/home.txt`  

## Live probe

- Request: `GET https://ntrs.nasa.gov/api/citations/search?q=openalex&page.size=1`
- Result: HTTP 200 in 708 ms — **200 JSON**
- Rate-limit headers: `{"X-RateLimit-Limit": "500", "X-RateLimit-Remaining": "499", "X-RateLimit-Reset": "1792464778"}`
- Body starts: `{"stats":{"took":39,"total":0,"estimate":false,"maxScore":null},"results":[],"aggregations":{"created":{"buckets":[]},"author":{"doc_count_error_upper_bound":0,"sum_other_doc_count`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
