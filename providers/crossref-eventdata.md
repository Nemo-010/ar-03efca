# Crossref Event Data

- Category: `scholarly-graph` — Scholarly graphs, metadata & citation APIs
- Home: https://www.eventdata.crossref.org/
- Docs: https://www.eventdata.crossref.org/guide/ — not captured (see Notes)
- Probe endpoint: `https://api.eventdata.crossref.org/v1/events?obj-id=10.1038/nature12373&rows=1`
- llms.txt: none verified — no llms.txt found; the probe host did not resolve or refused the connection

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: not established — the host did not resolve from this machine
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Event data (mentions, citations) over Crossref DOIs. Recorded as unverified.

## Live probe

- Request: `GET https://api.eventdata.crossref.org/v1/events?obj-id=10.1038/nature12373&rows=1`
- Result: HTTP 0 in 25058 ms — **no answer**
- Body starts: `<urlopen error timed out>`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
