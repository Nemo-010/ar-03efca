# National Library of Norway API

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://www.nb.no/
- Docs: https://api.nb.no/catalog/swagger-ui.html — HTTP 404 at capture (see Notes)
- Probe endpoint: `https://api.nb.no/catalog/v1/items?q=openalex&size=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

National Library of Norway. The catalogue API answers keyless; the captured root is a link stub.

## Live probe

- Request: `GET https://api.nb.no/catalog/v1/items?q=openalex&size=1`
- Result: HTTP 200 in 1067 ms — **200 JSON**
- Body starts: `{"_embedded":{"items":[{"id":"d622715ec3ce0bf5e25f79f3f580d0e6","_links":{"self":{"href":"https://api.nb.no:443/catalog/v1/items/d622715ec3ce0bf5e25f79f3f580d0e6"},"mods":{"href":"`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
