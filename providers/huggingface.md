# Hugging Face Hub

- Category: `repository` — Repositories & research-data archives
- Home: https://huggingface.co/
- Docs: https://huggingface.co/docs/hub/api
- Probe endpoint: `https://huggingface.co/api/datasets?limit=1`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: limits are per request class and published through RateLimit headers, not as one table; the docs use '100 requests per 5 minutes' only as an example of the header format
- Authentication: free key
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Model and dataset hub. Deliberately not converted into a monthly figure: the only number on the page is an illustration of header syntax, and treating it as a quota would invent an allowance the docs do not state.

## Evidence

> All API calls are subject to the HF-wide Rate limits .

Source: https://huggingface.co/docs/hub/rate-limits  
Snapshot: `data/snapshots/huggingface/docs.txt`  

## Live probe

- Request: `GET https://huggingface.co/api/datasets?limit=1`
- Result: HTTP 200 in 186 ms — **200 JSON**
- Rate-limit headers: `{"RateLimit": "\"api\";r=498;t=123", "RateLimit-Policy": "\"fixed window\";\"api\";q=500;w=300"}`
- Body starts: `[{"_id":"6ac0e39df4f1ce50a992796a","id":"datasocial/tiktok-5.6B-videos","author":"datasocial","disabled":false,"gated":false,"lastModified":"2026-10-07T18:55:25.000Z","likes":369,"`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
