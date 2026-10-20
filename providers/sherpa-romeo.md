# Sherpa Romeo

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://v2.sherpa.ac.uk/
- Docs: https://v2.sherpa.ac.uk/api/ — HTTP 403 at capture (see Notes)
- Probe endpoint: `https://v2.sherpa.ac.uk/cgi/retrieve?item-type=publication`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: API key required; the docs site returned 403 to this client
- Authentication: key on application
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Journal open-access policies. Recorded as unverified: every documentation fetch returned a 403 challenge page.

## Live probe

- Request: `GET https://v2.sherpa.ac.uk/cgi/retrieve?item-type=publication`
- Result: HTTP 403 in 583 ms — **needs key**
- Body starts: `<!DOCTYPE html> <html lang="en-GB" style="height: 100%;"> <head> <meta charset="UTF-8" /> <meta name="viewport" content="width=device-width" /> <title>Jisc - Error 403 </title> <me`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
