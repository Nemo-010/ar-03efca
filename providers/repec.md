# RePEc / IDEAS

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://ideas.repec.org/
- Docs: https://ideas.repec.org/ — HTTP 200 at capture
- Probe endpoint: `https://ideas.repec.org/cgi-bin/htsearch?q=openalex`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Economics bibliography. The IDEAS search page answers HTML, not JSON, so it is not a clean gateway target.

## Evidence

> IDEAS is the largest bibliographic database dedicated to Economics and available freely on the Internet.

Source: https://ideas.repec.org/  
Snapshot: `data/snapshots/repec/docs.txt`  

## Live probe

- Request: `GET https://ideas.repec.org/cgi-bin/htsearch?q=openalex`
- Result: HTTP 200 in 10570 ms — **200 HTML**
- Body starts: `<!DOCTYPE html> <head><title>IDEAS/RePEc search</title> <meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-wid`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
