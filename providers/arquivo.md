# Arquivo.pt

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://arquivo.pt/
- Docs: https://arquivo.pt/api
- Probe endpoint: `https://arquivo.pt/wayback/cdx?url=openalex.org&output=json&limit=2`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **10,800,000 calls/month**
- Derivation: 250/60s x 2,592,000 s/month = 10,800,000 calls/month ceiling
- Published rate: 250 requests/60s (full-text & URL search); 400 requests/60s (image, Memento)
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

Portuguese web archive. Publishes per-endpoint limits and the 429 it returns above them.

## Evidence

> If a client exceeds the following maximum usage limits, it will receive an error "HTTP 429 Too many requests" and must decrease its access rate:

Source: https://arquivo.pt/api  
Snapshot: `data/snapshots/arquivo/limits.txt`  

## Live probe

- Request: `GET https://arquivo.pt/wayback/cdx?url=openalex.org&output=json&limit=2`
- Result: HTTP 200 in 717 ms — **200 JSON**
- Rate-limit headers: `{"RateLimit-Limit": "250", "RateLimit-Reset": "60", "X-RateLimit-Limit": "250", "X-RateLimit-Policy": "250;w=60", "X-RateLimit-Reset": "t=1792464508520004", "X-RateLimit-Scope": "ip"}`
- Body starts: `{"urlkey": "org,openalex)/", "timestamp": "20220425034858", "url": "http://openalex.org/", "mime": "text/html", "status": "200", "digest": "2W23FXGBNESHQHKM425VJSLWTBC5NUSS", "leng`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
