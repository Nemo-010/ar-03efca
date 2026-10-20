# UK Web Archive

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://www.webarchive.org.uk/
- Docs: https://www.webarchive.org.uk/en/ukwa/info/api
- Probe endpoint: `https://www.webarchive.org.uk/wayback/archive/cdx?url=openalex.org&limit=2`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: not established
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

UK Web Archive. Neither the documentation page nor its archived copy could be fetched from this machine; no allowance is claimed.

## Live probe

- Request: `GET https://www.webarchive.org.uk/wayback/archive/cdx?url=openalex.org&limit=2`
- Result: HTTP 0 in 353 ms — **no answer**
- Body starts: `<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1082)>`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
