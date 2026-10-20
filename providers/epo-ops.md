# EPO Open Patent Services

- Category: `publisher` — Publisher & patent TDM endpoints
- Home: https://www.epo.org/
- Docs: https://developers.epo.org/ — HTTP 200 at capture
- Probe endpoint: `https://ops.epo.org/3.2/rest-services/published-data/search?q=openalex`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: OAuth credentials required; published free quota is per-registered-user and was not captured
- Authentication: key on application
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

European Patent Office Open Patent Services. Answers 403 without credentials; the developer portal is free to register but no call quota survived capture.

## Live probe

- Request: `GET https://ops.epo.org/3.2/rest-services/published-data/search?q=openalex`
- Result: HTTP 403 in 1096 ms — **needs key**
- Body starts: `<error><code>403</code><message>This request has been rejected due to the violation of Fair Use policy</message><moreInfo>https://www.epo.org/service-support/ordering/fair-use.html`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
