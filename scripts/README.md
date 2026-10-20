# scripts

| file | role |
|---|---|
| `_build_candidates.py` | writes `data/candidates.json` — the provider working set |
| `fetch.py` | snapshots home/docs/policy pages per provider (gzip + text + `meta.json`) |
| `fetch_url.py` | adds one extra URL to a provider's snapshot dir |
| `policy.py` | the URL map used to reach each provider's rate-limit or terms page |
| `probe.py` | one live unauthenticated request per API endpoint → `data/probes.json` |
| `llms.py` | verifies which providers really serve a markdown `llms.txt` → `data/llms.json` |
| `facts.py` | the curated table; builds `data/facts.json` |
| `build_reports.py` | generates `reports/`, `providers/` and `README.md` from `facts.json` |
| `test_integrity.py` | the guarantee: quotes verbatim, figures recompute, reports consistent |
| `check.py` | re-fetches every recorded source and compares sha256 (non-destructive) |
| `grab.py` | helper: print sentences matching a regex from one provider's snapshots |

`grab.py` is how every quote in `facts.py` was found and checked by eye before it
was pasted in:

```sh
python3 scripts/grab.py crossref 'Pool Rate limit' 3
```
