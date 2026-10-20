#!/usr/bin/env python3
"""Generate the report set from data/facts.json, data/probes.json and data/llms.json.

Outputs:
  reports/00-methodology.md      how every figure was produced and checked
  reports/01-inventory.md        ranked inventory + per-category catalogue
  reports/02-deep-reviews.md     eight providers reviewed in depth
  reports/03-post-analysis.md    five analyses
  reports/04-probes.md           what each endpoint actually answered
  providers/<slug>.md            one page per provider
  README.md
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
REP = os.path.join(ROOT, "reports")
PROV = os.path.join(ROOT, "providers")
TODAY = "2026-10-20"

def load(name):
    with open(os.path.join(DATA, name)) as fh:
        return json.load(fh)


facts = load("facts.json")
probes = load("probes.json")
llms = load("llms.json")
cats = load("candidates.json")["categories"]
BY = {r["slug"]: r for r in facts}

SEC = 2592000  # seconds in a 30-day month


def fmt(n):
    return f"{n:,}" if isinstance(n, int) else "—"


def ranked():
    """Providers with a documented figure, largest first, then the rest by confidence."""
    with_num = sorted([r for r in facts if r["monthly_calls"]], key=lambda r: -r["monthly_calls"])
    order = {"high": 0, "medium": 1, "low": 2, "none": 3}
    rest = sorted([r for r in facts if not r["monthly_calls"]],
                  key=lambda r: (order[r["confidence"]], r["name"]))
    return with_num + rest


def verdict_label(r):
    p = r.get("probe") or {}
    v = p.get("verdict")
    return {"ok": "200 JSON", "ok-html": "200 HTML", "auth": "needs key", "payment": "402",
            "bot-wall": "bot wall", "blocked": "429/503", "not-found": "404",
            "error": "no answer", "none": "not probed"}.get(v, "not probed")


def key_label(r):
    return {"none": "none", "free": "free key", "apply": "key on application",
            "paid": "paid only", None: "?"}[r["key"]]


# ------------------------------------------------------------------ per provider
def prov_md(r):
    L = [f"# {r['name']}", ""]
    L.append(f"- Category: `{r['category']}` — {cats.get(r['category'], '')}")
    L.append(f"- Home: {r['home'] or '—'}")
    L.append(f"- Docs: {r['docs'] or '—'}")
    L.append(f"- Probe endpoint: `{r['api'] or '—'}`")
    if r["llms"]:
        L.append(f"- llms.txt: {r['llms']}")
    else:
        L.append(f"- llms.txt: none verified — {r.get('llms_reason') or 'not found'}")
    L.append("")
    L.append("## Free access")
    L.append("")
    if r["monthly_calls"]:
        L.append(f"- Documented volume: **{fmt(r['monthly_calls'])} calls/month**")
        if r["derivation"]:
            L.append(f"- Derivation: {r['derivation']}")
    else:
        L.append("- Documented volume: **no call quota published** in the captured sources")
    L.append(f"- Published rate: {r['rate']}")
    if r["one_time"]:
        L.append(f"- One-time grant: {r['one_time']}")
    L.append(f"- Authentication: {key_label(r)}")
    L.append(f"- Payment card for the free tier: "
             f"{ {True: 'yes', False: 'no', None: 'not stated'}[r['card']] }")
    L.append(f"- Evidence confidence: **{r['confidence']}**")
    L.append("")
    L.append("## Notes")
    L.append("")
    L.append(r["note"])
    L.append("")
    if r["evidence"]:
        L.append("## Evidence")
        L.append("")
        for e in r["evidence"]:
            if e.get("quote"):
                L.append("> " + e["quote"].strip())
                L.append("")
            if e.get("url"):
                L.append(f"Source: {e['url']}  ")
            if e.get("snapshot"):
                L.append(f"Snapshot: `{e['snapshot']}`  ")
            L.append("")
    p = r.get("probe") or {}
    L.append("## Live probe")
    L.append("")
    if p.get("url"):
        L.append(f"- Request: `GET {p['url']}`")
        L.append(f"- Result: HTTP {p.get('status')} in {p.get('ms')} ms — **{verdict_label(r)}**")
        if p.get("rate_headers"):
            L.append(f"- Rate-limit headers: `{json.dumps(p['rate_headers'])}`")
        if p.get("body_head"):
            L.append(f"- Body starts: `{p['body_head'][:180]}`")
        if p.get("history"):
            L.append("- Earlier attempts (kept, not overwritten): " + "; ".join(
                f"HTTP {h.get('status')} {verdict_label({'probe': h})} "
                f"at {h.get('probed_at', '')[:19]}" for h in p["history"]))
    else:
        L.append("- Not probed.")
    L.append("")
    L.append("## Measurement note")
    L.append("")
    L.append(f"Generated from `data/facts.json` on {TODAY}. The probe is one unauthenticated "
             "request from one machine: it shows whether the endpoint answers at all, not what "
             "the quota is. Re-run `make fetch probe` to refresh.")
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------- methodology
def build_methodology():
    n = len(facts)
    hi = sum(1 for r in facts if r["confidence"] == "high")
    md = sum(1 for r in facts if r["confidence"] == "medium")
    lo = sum(1 for r in facts if r["confidence"] == "low")
    nums = [r for r in facts if r["monthly_calls"]]
    ok = sum(1 for r in facts if str((r.get("probe") or {}).get("verdict", "")).startswith("ok"))
    L = ["# Methodology and verification", ""]
    L.append(f"Compiled {TODAY}. Scope: academic and archival services that expose a documented "
             "HTTP API — web archives, national archive catalogues, library and museum "
             "aggregators, scholarly graphs, bibliographic indexes, research-data repositories, "
             "life-science data services, and publisher/patent text-and-data-mining endpoints. "
             f"{n} providers are catalogued.")
    L.append("")
    L.append("One provider is one API surface. Where a service publishes two distinct APIs "
             "(bioRxiv/medRxiv share a host but serve different corpora; OAPEN's library REST "
             "search and its api host were tried and are reported as one row) the row names the "
             "surface that was probed, so the count is of endpoints, not of companies.")
    L.append("")
    L.append("## Where the method comes from")
    L.append("")
    L.append("The discipline is adopted from two earlier inventories, and both debts are specific:")
    L.append("")
    L.append("| Borrowed | From | Applied here |")
    L.append("|---|---|---|")
    L.append("| snapshot → facts → reports pipeline, with gzip + text + `meta.json` per page and "
             "sha256 on every capture | `Nemo-010/w-search-3f9a2c` | `scripts/fetch.py`, "
             "`scripts/facts.py`, `scripts/build_reports.py` |")
    L.append(f"| integrity test that re-checks every quote verbatim and every figure against its "
             "source, and refuses to generate a report citing a provider it does not have | "
             f"`Nemo-010/w-search-3f9a2c` | `scripts/test_integrity.py` |")
    L.append("| `llms.txt` verification that rejects an HTML soft-404, an empty body, and a file "
             "belonging to another site | `Nemo-010/w-search-3f9a2c` | `scripts/llms.py` |")
    L.append("| per-row evidence index (url, http code, bytes, sha256, capture time) so one number "
             "can be traced to one artefact | `talaria0101/w-search-7b668b35` | `meta.json` per "
             "provider, plus `data/probes.json` |")
    L.append("| keeping two independent passes and saying when they disagree instead of "
             "reconciling them silently | `talaria0101/w-search-7b668b35` | documentation snapshot "
             "vs live probe, reported separately everywhere |")
    L.append("")
    L.append(f"What is different here: this inventory is academic and archival, so the "
             "commercial-API apparatus (signup bonuses, credit-card requirements, anti-bot "
             "rankings) mostly does not apply. Three of "
             f"{n} providers publish a quota; "
             f"{sum(1 for r in facts if r['card'] is True)} ask for a card; "
             f"{sum(1 for r in facts if r['one_time'])} offer a trial credit. The work that "
             "mattered instead was distinguishing a published rate from a quota, a missing "
             "credential from a bot wall, and a live page from a dead host.")
    L.append("")
    L.append("## Two evidence classes, never mixed")
    L.append("")
    L.append("| class | what it proves | where it lives |")
    L.append("|---|---|---|")
    L.append("| **Documentation snapshot** | what the provider *says* the allowance is | "
             "`data/snapshots/<slug>/*.txt` + `meta.json` |")
    L.append("| **Live probe** | what the endpoint *did* for one unauthenticated caller today | "
             "`data/probes.json` |")
    L.append("")
    L.append("A provider can have a generous documented allowance and still refuse this caller "
             "(Semantic Scholar documents 1,000 req/s and answered a 429 on the first probe run). "
             "A provider can answer happily and publish no number at all (Wayback CDX). The "
             "reports keep the two apart and never infer one from the other.")
    L.append("")
    L.append("Two endpoints even changed their answer between attempts, and both results are kept "
             "in the probe history rather than the last one winning: Gallica answered XML on the "
             "first run and a Cloudflare challenge on the second; Perma.cc did the reverse. That "
             "is the honest state of a public API reached from a datacentre IP, and collapsing it "
             "to a single verdict would misrepresent it.")
    L.append("")
    L.append("## Pipeline")
    L.append("")
    L.append("```sh")
    L.append("make fetch     # snapshot home/docs/policy pages per provider (gzip + text + sha256)")
    L.append("make probe     # one live unauthenticated request per API endpoint")
    L.append("make llms      # verify which providers really serve a markdown llms.txt")
    L.append("make facts     # build data/facts.json from the curated table + probe results")
    L.append("make reports   # rebuild every report from data/facts.json")
    L.append("make test      # integrity: every quote verbatim, every figure recomputes")
    L.append("make check     # re-fetch every recorded source, compare sha256 (non-destructive)")
    L.append("```")
    L.append("")
    L.append("## How a number gets into the inventory")
    L.append("")
    L.append("1. The provider publishes a rate or a monthly figure on a page that was captured.")
    L.append("2. The exact sentence is copied into `scripts/facts.py` as `quote`, with the page's "
             "URL and snapshot path.")
    L.append("3. If the figure is derived from a rate, `derivation` states the arithmetic: "
             "`rate × seconds in a 30-day month` (2,592,000) for per-second rates, "
             "`rate × 1,440 × 30` for per-minute rates.")
    L.append("4. `scripts/test_integrity.py` re-checks that the quote is verbatim in the snapshot "
             "and that the arithmetic reproduces the published number.")
    L.append("")
    L.append("A derived number is a **ceiling**: it is what the published rate permits if you call "
             "continuously for a month. It is not a quota the provider promises to serve, and no "
             "real workload calls at the ceiling. The ranking therefore shows both the rate and "
             "the derived monthly ceiling, and says which is which.")
    L.append("")
    L.append("## What the confidence column means")
    L.append("")
    L.append(f"- **high** ({hi} providers) — an explicit number, or an explicit statement that "
             "access is free and keyless, in official documentation that was captured.")
    L.append(f"- **medium** ({md}) — an official statement that access is free or needs a key, "
             "without a number that can be converted to a call count.")
    L.append(f"- **low** ({lo}) — nothing usable survived capture: a login wall, a JavaScript "
             "shell, a 403 challenge, a bot check, a dead host, or a documentation page that "
             "documents endpoints but never states an allowance.")
    L.append("")
    L.append("`low` is not a verdict that the provider is bad. It means this run could not verify "
             "the allowance, and the report says so rather than guessing. Of the "
             f"{n} providers, {ok} answered an unauthenticated call during the probe, which is a "
             "different and independent fact.")
    L.append("")
    L.append("## Why some well-known services are marked low")
    L.append("")
    L.append("The failure modes are worth naming, because they are the reason the number is "
             "missing and not a judgement about the service:")
    L.append("")
    L.append("- **Cloudflare / bot interstitial.** `europepmc.org`, `dblp.org`, `base-search.net`, "
             "`cds.cern.ch` and `pubchem.ncbi.nlm.nih.gov` serve a JavaScript challenge to a "
             "plain HTTP client. The API hosts themselves (`www.ebi.ac.uk/europepmc/webservices`, "
             "`dblp.org/search/publ/api`) do answer, so the API works even when the docs site "
             "does not.")
    L.append("- **Application shell.** `patentsview.org`, `uspto` developer pages and "
             "`clinicaltrials.gov/data-api` return a single-page app that renders text only in a "
             "browser. Status 200, no readable words.")
    L.append("- **Dead or moved documentation.** `europeana`'s Confluence page is a 404, "
             "`info.orcid.org` returns 404 for every reference path tried, "
             "`chroniclingamerica`'s legacy API is retired in favour of the loc.gov API.")
    L.append("- **Host does not resolve.** `api.fatcat.wiki`, `api.lareferencia.info`, "
             "`api.dimensions.ai`, `search.patentsview.org`, `timetravel.mementoweb.org`, "
             "`api.isidore.science` and `api.constellate.org` did not resolve from this machine. "
             "That is a fact about this network, not about the provider.")
    L.append("")
    L.append("## Limits of this inventory")
    L.append("")
    L.append("- Free tiers change without notice. Every number is as of the capture date in the "
             "snapshot's `meta.json`.")
    L.append("- A rate is not a quota. Converting `5 requests/second` into `12,960,000/month` is "
             "arithmetic, not a promise; it is labelled a ceiling everywhere it appears.")
    L.append("- Where a provider publishes several rates (guest vs authenticated, per endpoint), "
             "the lowest published rate is the one converted, because it is the one a caller "
             "without an account can rely on.")
    L.append("- Where a rate is shared among all callers (Semantic Scholar), or is CPU time rather "
             "than calls (Wikidata), it is deliberately **not** converted, and the report says why.")
    L.append("- One probe per endpoint, from one IP, at one moment. It is evidence that the "
             "endpoint answers unauthenticated callers at all; it is not a load test.")
    L.append("- No terms-of-service analysis is included. This is a technical inventory of "
             "documented allowances; it makes no claim that any particular use is permitted.")
    L.append("- Licences are noted where a page states one, but licence of the *data* and the "
             "terms of the *API* are different things and only the captured text is reported.")
    L.append("")
    L.append("## Re-verifying one number")
    L.append("")
    L.append("```sh")
    L.append("python3 -c \"import json;d={r['slug']:r for r in json.load(open('data/facts.json'))};"
             "print(json.dumps(d['crossref'],indent=1))\"")
    L.append("```")
    L.append("")
    L.append("That prints the quote, the URL and the snapshot path. Open the snapshot and read the "
             "sentence; `make check` re-fetches the URL and reports whether the bytes changed.")
    L.append("")
    L.append("Licence: 0BSD (see `LICENSE`).")
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------- inventory
def build_inventory():
    rows = ranked()
    numbered = [r for r in rows if r["monthly_calls"]]
    L = ["# Academic and archival APIs by documented free allowance", ""]
    L.append(f"Compiled {TODAY}. {len(facts)} providers, {len(numbered)} with a documented "
             "call figure. Ranked by the documented recurring free volume, largest first; "
             "providers that publish no number follow, ordered by evidence confidence.")
    L.append("")
    L.append("**Read the volume column as a ceiling, not a quota.** Seventeen of the twenty "
             "figures are a published rate (`5 requests/second`, `500 per 5 minutes`) multiplied by "
             "the seconds in a 30-day month. Nobody calls at that rate for a month; the column "
             "exists so that rates of different shapes can be compared at all. Only NARA (10,000/"
             "month), ADS (5,000/day) and OpenAlex (a $1/day budget with a published price list) "
             "state a quota a caller can plan against without assuming saturation. The `Basis` "
             "column always says which kind of number it is.")
    L.append("")
    L.append("Columns: **Calls/mo** documented recurring free volume; **Basis** the published "
             "figure or the arithmetic; **Key** whether an API key or account is needed; "
             "**Card** whether a payment card is demanded; **Probe** what one unauthenticated "
             "request returned; **Conf** evidence confidence.")
    L.append("")
    L.append("| # | Provider | Category | Calls/mo | Basis | Key | Card | Probe | Conf | Links |")
    L.append("|---|----------|----------|--------:|-------|-----|:----:|-------|:----:|-------|")
    for i, r in enumerate(rows, 1):
        basis = (r["derivation"] or r["rate"]).replace("|", "/")[:96]
        links = " · ".join(x for x in [
            f"[home]({r['home']})" if r["home"] else "",
            f"[docs]({r['docs']})" if r["docs"] else "",
            f"[llms]({r['llms']})" if r["llms"] else "",
            f"[report](../providers/{r['slug']}.md)"] if x)
        card = {True: "yes", False: "no", None: "?"}[r["card"]]
        L.append(f"| {i} | **{r['name']}** | {r['category']} | {fmt(r['monthly_calls'])} | "
                 f"{basis} | {key_label(r)} | {card} | {verdict_label(r)} | "
                 f"{r['confidence']} | {links} |")
    L.append("")
    L.append("## The ranking is not the dataset")
    L.append("")
    L.append(f"Every one of the {len(facts)} providers has a full report under `providers/` and a "
             "row in the category catalogue below, including the ones with no published figure. "
             "A provider absent from the ranked top of the table is not absent from the work.")
    L.append("")
    for cat, label in cats.items():
        rows = [r for r in facts if r["category"] == cat]
        if not rows:
            continue
        L.append(f"## {label}")
        L.append("")
        for r in sorted(rows, key=lambda x: (-(x["monthly_calls"] or 0), x["name"])):
            vol = fmt(r["monthly_calls"]) + " calls/mo" if r["monthly_calls"] else "no published number"
            L.append(f"### {r['name']}")
            L.append("")
            L.append(f"- Free access: {vol} — {r['rate']}")
            L.append(f"- Authentication: {key_label(r)} · confidence {r['confidence']} · "
                     f"probe {verdict_label(r)}")
            L.append(f"- Links: home {r['home'] or '—'} · docs {r['docs'] or '—'} · "
                     f"llms.txt {r['llms'] or '—'} · [full report](../providers/{r['slug']}.md)")
            L.append("")
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ deep reviews
REVIEWS = ["openalex", "wayback-cdx", "crossref", "loc", "zenodo", "uniprot",
           "met-museum", "nara"]


def build_reviews():
    L = ["# Deep reviews", ""]
    L.append("Eight providers reviewed against the same questions: what is the documented "
             "allowance, what does the API actually do, what is the failure mode, and what is it "
             "good for in an archival or academic pipeline. Every figure here is also in "
             "`data/facts.json`; nothing is added in prose.")
    L.append("")
    for slug in REVIEWS:
        r = BY[slug]
        p = r.get("probe") or {}
        L.append(f"## {r['name']}")
        L.append("")
        L.append(f"`{r['category']}` · confidence **{r['confidence']}** · "
                 f"key: {key_label(r)} · card: "
                 f"{ {True: 'yes', False: 'no', None: 'not stated'}[r['card']] }")
        L.append("")
        L.append("**Documented allowance.** " +
                 (f"{fmt(r['monthly_calls'])} calls/month. {r['derivation']}. "
                  if r["monthly_calls"] else "No call quota is published. ") +
                 r["rate"] + ".")
        L.append("")
        L.append("**Live probe.** " + (
            f"`GET {p['url']}` returned HTTP {p.get('status')} in {p.get('ms')} ms "
            f"({verdict_label(r)})." if p.get("url") else "Not probed."))
        L.append("")
        L.append("**What it is.** " + r["note"])
        L.append("")
        if r["evidence"]:
            e = r["evidence"][0]
            L.append("> " + e["quote"].strip())
            L.append("")
            L.append(f"Source: {e['url']} · snapshot `{e['snapshot']}`")
            L.append("")
        L.append("**In a pipeline.** " + PIPELINE.get(slug, ""))
        L.append("")
    return "\n".join(L) + "\n"


PIPELINE = {
 "openalex": "The best default for scholarly metadata because the price list is public: a DOI "
             "lookup is free, a filtered list costs a tenth of a cent per call, a full-text "
             "search costs a cent per call. That means a pipeline can budget in dollars instead "
             "of guessing at a quota. Use single-entity lookups for citation checking (free, "
             "unlimited) and reserve searches for discovery.",
 "wayback-cdx": "The index of record for 'what did this page say in 2019'. One call per URL "
                "returns the capture list with status codes and digests; `collapse=digest` "
                "deduplicates, and `limit` bounds the response. There is no published quota, so "
                "pace yourself rather than relying on a header to tell you when to stop.",
 "crossref": "The cheapest way to turn a DOI into publisher-deposited metadata, and the only one "
             "here that publishes both a rate and a concurrency allowance. Add a `mailto` and you "
             "move from 5 to 10 requests/second for free, which is the single easiest performance "
             "win in this inventory.",
 "loc": "The Library of Congress API is the model public-sector API: a per-service rate table "
        "(20/minute for JSON, 150/minute for text and image), the block duration when you exceed "
        "it, and a 100,000-item paging ceiling. For newspaper and print collections it replaces "
        "the retired Chronicling America API. The caveat is the probe: a datacentre IP gets a "
        "Cloudflare challenge before the rate table ever applies, so budget for identifying your "
        "client properly rather than assuming the documented rate is reachable.",
 "zenodo": "CERN's repository is where a lot of European research data lands, and its rate table "
           "distinguishes guest from authenticated per endpoint — search is 30/minute, not the "
           "60/minute headline. A DOI-to-record lookup is one call; do not walk the whole corpus.",
 "uniprot": "The highest published rate in this inventory (200 requests/second/user) on a "
            "protein knowledge base. Realistic use is per-accession lookup during annotation, "
            "not bulk scanning; bulk belongs in the FTP download, not the API.",
 "met-museum": "80 requests/second with no key and no registration, over a collection whose "
               "images are openly licensed. For art and object metadata this is the least "
               "friction of any source here — and it also publishes the full dataset for "
               "download, which sidesteps the API entirely.",
 "nara": "The only provider in this set that publishes a plain monthly call quota: 10,000 "
         "queries/month per key by default, with named tiers to 1.5M for partners. That makes it "
         "easy to plan and hard to scale without an application — the key is free but gated, and "
         "a keyless call gets the single-page application shell rather than JSON.",
}


# ------------------------------------------------------------------ post-analysis
def build_post_analysis():
    numbered = sorted([r for r in facts if r["monthly_calls"]], key=lambda r: -r["monthly_calls"])
    quotas = [r for r in numbered if r["basis_kind"] in (
        "published-monthly", "published-daily", "daily-budget")]
    ceilings = [r for r in numbered if r["basis_kind"] == "rate-ceiling"]
    total = sum(r["monthly_calls"] for r in numbered)
    L = ["# Post-analysis", ""]
    L.append(f"All figures derive from `data/facts.json` (captured {TODAY}). Nothing here is an "
             "estimate unless the sentence says so.")
    L.append("")

    # ---- 1. totals
    L.append("## 1. Total documented volume, one account and five")
    L.append("")
    L.append("Of the providers with a number, **three publish a quota** — one monthly, one daily, "
             "and one as a daily dollar budget with a published price list. The other "
             f"{len(ceilings)} publish a *rate* (requests per second or minute), and their monthly "
             "figure is arithmetic on that rate, not a promise. The two groups are kept apart "
             "because they mean different things.")
    L.append("")
    L.append("### 1a. Published quotas")
    L.append("")
    L.append("| Provider | Per account /mo | ×5 | What the provider actually publishes |")
    L.append("|----------|---:|---:|-------|")
    for r in quotas:
        L.append(f"| {r['name']} | {fmt(r['monthly_calls'])} | **{fmt(r['monthly_calls']*5)}** | "
                 f"{(r['derivation'] or '').replace('|','/')[:96]} |")
    L.append(f"| **Subtotal** | **{fmt(sum(r['monthly_calls'] for r in quotas))}** | "
             f"**{fmt(sum(r['monthly_calls'] for r in quotas)*5)}** | |")
    L.append("")
    L.append("These three are the only numbers in this inventory that a caller can plan against "
             "without assuming saturation. NARA and ADS state the quota outright; OpenAlex "
             "publishes a daily dollar budget and a price per operation, so the call count follows "
             "from two published facts.")
    L.append("")
    L.append("### 1b. Rate ceilings")
    L.append("")
    L.append("| Provider | Rate published | Ceiling /mo | ×5 |")
    L.append("|----------|----------------|---:|---:|")
    for r in ceilings:
        L.append(f"| {r['name']} | {r['rate'].replace('|','/')[:84]} | {fmt(r['monthly_calls'])} | "
                 f"**{fmt(r['monthly_calls']*5)}** |")
    L.append(f"| **Subtotal** | | **{fmt(sum(r['monthly_calls'] for r in ceilings))}** | "
             f"**{fmt(sum(r['monthly_calls'] for r in ceilings)*5)}** |")
    L.append("")
    L.append("A ceiling is what the published rate permits if a client called continuously for 30 "
             "days. No real client does that, and several of these docs ask callers not to.")
    L.append("")
    L.append("### 1c. The headline number, and why it is nearly meaningless")
    L.append("")
    L.append(f"Adding the two groups gives **{fmt(total)} calls/month** for one account each and "
             f"**{fmt(total*5)}** for five. That total is dominated by two rows:")
    L.append("")
    for r in numbered[:2]:
        L.append(f"- {r['name']}: {fmt(r['monthly_calls'])} ({r['monthly_calls']/total*100:.1f}% "
                 f"of the total) — {r['derivation']}")
    L.append("")
    L.append("Both are per-second rates on scientific data APIs. Dropping them leaves "
             f"**{fmt(total - sum(r['monthly_calls'] for r in numbered[:2]))} calls/month**, and "
             "that figure is the one worth remembering. Three reasons the total overstates what a "
             "real pipeline gets:")
    L.append("")
    L.append("1. **A rate is not a quota.** Nothing obliges a provider to serve a client that "
             "saturates its published rate for a month, and several of these docs say so.")
    L.append("2. **Shared pools.** Semantic Scholar's 1,000 requests/second is shared by every "
             "unauthenticated caller in the world, so it is excluded from the sum entirely rather "
             "than counted as one caller's allowance.")
    L.append("3. **Per-key gates.** NARA's quota and Dimensions' eligibility rule mean a second "
             "account needs a second approval, so the ×5 column is arithmetic rather than access.")
    L.append("")
    L.append("### 1d. Ceiling by category")
    L.append("")
    L.append("| Category | With a figure | Ceiling /mo, 1 account | ×5 |")
    L.append("|---|---:|---:|---:|")
    for cat in cats:
        rows = [r for r in numbered if r["category"] == cat]
        if not rows:
            continue
        s2 = sum(r["monthly_calls"] for r in rows)
        L.append(f"| {cat} | {len(rows)} | {fmt(s2)} | {fmt(s2*5)} |")
    L.append("")
    L.append("### 1e. One-time grants")
    L.append("")
    ot = [r for r in facts if r["one_time"]]
    if ot:
        for r in ot:
            L.append(f"- {r['name']}: {r['one_time']}")
    else:
        L.append("None of the captured pages in this set offer a one-time credit grant. That is a "
                 "real difference from commercial scraping APIs: public and academic "
                 "infrastructure publishes a standing rate instead of a trial.")
    L.append("")

    # ---- 2. auth friction
    L.append("## 2. Friction: what it takes to make the first call")
    L.append("")
    buckets = {"none": [], "free": [], "apply": [], "paid": [], None: []}
    for r in facts:
        buckets[r["key"]].append(r)
    L.append("| Friction | Count | Meaning | Examples |")
    L.append("|---|---:|---|---|")
    L.append(f"| keyless | {len(buckets['none'])} | works with no key at all | "
             + ", ".join(r["name"] for r in buckets["none"][:6]) + " |")
    L.append(f"| free key | {len(buckets['free'])} | sign-up, no payment | "
             + ", ".join(r["name"] for r in buckets["free"][:6]) + " |")
    L.append(f"| key on application | {len(buckets['apply'])} | a human approves the key | "
             + ", ".join(r["name"] for r in buckets["apply"][:6]) + " |")
    L.append(f"| paid only | {len(buckets['paid'])} | no free API tier found | "
             + ", ".join(r["name"] for r in buckets["paid"]) + " |")
    L.append(f"| not established | {len(buckets[None])} | capture did not settle it | "
             + ", ".join(r["name"] for r in buckets[None][:8]) + " |")
    L.append("")
    cards = [r["name"] for r in facts if r["card"] is True]
    L.append(f"**Payment cards demanded for the free tier: {len(cards)}.** "
             + ("None of the captured pages requires a card to reach a free academic or archival "
                "API." if not cards else ", ".join(cards) + "."))
    L.append("")
    L.append("The gated ones matter more than the count suggests. "
             + ", ".join(r["name"] for r in buckets["apply"])
             + " all require an application or an institutional entitlement, which means they "
             "cannot be added to a pipeline by a script — a human has to ask. "
             + ("Two of them publish a call figure beyond the gate ("
                + ", ".join(r["name"] for r in buckets["apply"] if r["monthly_calls"])
                + "), which is what makes filing the application worthwhile; the rest publish "
                "none." if any(r["monthly_calls"] for r in buckets["apply"]) else
                "None of them publishes a call figure beyond the gate."))
    L.append("")

    # ---- 3. probe results
    L.append("## 3. What the endpoints actually answered")
    L.append("")
    vs = {}
    for r in facts:
        v = (r.get("probe") or {}).get("verdict") or "none"
        vs[v] = vs.get(v, 0) + 1
    L.append("| Verdict | Count | What it means |")
    L.append("|---|---:|---|")
    for v, label in [("ok", "200 with a machine-readable body"),
                     ("ok-html", "200 but an HTML page, not the API"),
                     ("auth", "401/403 with a JSON or plain refusal — a key is required"),
                     ("bot-wall", "403/503 carrying a Cloudflare/Anubis/reCAPTCHA challenge"),
                     ("blocked", "429/503 — refused at probe time"),
                     ("not-found", "404 — the documented path is gone"),
                     ("error", "no answer: DNS, TLS or timeout"),
                     ("none", "not probed")]:
        if vs.get(v):
            L.append(f"| {v} | {vs[v]} | {label} |")
    L.append("")
    answered = vs.get("ok", 0) + vs.get("ok-html", 0)
    L.append(f"{answered} of {len(facts)} endpoints answered an unauthenticated call. The most "
             "common failure is not a paywall: it is a bot interstitial or an application shell, "
             "which returns 200 with no usable body. That is why the probe records "
             "`ok-html` separately from `ok`.")
    L.append("")
    L.append("Slowest endpoints in the probe (one request each, so this is a floor, not a "
             "benchmark):")
    L.append("")
    slow = sorted([r for r in facts if (r.get("probe") or {}).get("ms")],
                  key=lambda r: -r["probe"]["ms"])[:8]
    L.append("| Provider | ms | Verdict |")
    L.append("|---|---:|---|")
    for r in slow:
        L.append(f"| {r['name']} | {r['probe']['ms']:,} | {verdict_label(r)} |")
    L.append("")

    # ---- 4. maturity / coverage
    L.append("## 4. Where the free capacity actually is")
    L.append("")
    L.append("Counting only providers with a published figure, by category:")
    L.append("")
    L.append("| Category | With a figure | Total in category | Share |")
    L.append("|---|---:|---:|---:|")
    for cat in cats:
        rows = [r for r in facts if r["category"] == cat]
        if not rows:
            continue
        w = sum(1 for r in rows if r["monthly_calls"])
        L.append(f"| {cat} | {w} | {len(rows)} | {w/len(rows)*100:.0f}% |")
    L.append("")
    L.append("Web archives are the least quantified category in this inventory: the Wayback CDX "
             "server, the single largest index of the web's past, publishes no call quota at all. "
             "The well-quantified categories are bibliographic indexes and life-science data, "
             "where the funder pays for the infrastructure and the API is the product.")
    L.append("")
    L.append("llms.txt is barely used in this space: "
             f"{sum(1 for r in facts if r['llms'])} of {len(facts)} providers serve a verified "
             "markdown index at a canonical path ("
             + ", ".join(r["name"] for r in facts if r["llms"]) + "). "
             "Academic and archival infrastructure predates that convention, and several hosts "
             "that do return 200 at `/llms.txt` serve an HTML shell there, which the verifier "
             "rejects.")
    L.append("")

    # ---- 5. recommended stack
    L.append("## 5. A stack built only from verified figures")
    L.append("")
    L.append("If the requirement is 'documented allowance, no card, works today', the subset is "
             "small and specific:")
    L.append("")
    L.append("| Need | Provider | Why this one |")
    L.append("|---|---|---|")
    picks = [("openalex", "scholarly metadata and citation graph",
              "published price list, free single-entity lookups, $1/day budget"),
             ("crossref", "DOI metadata",
              "5/s public, 10/s with a mailto, no key needed"),
             ("datacite", "research-data DOIs", "500 per 5 min unidentified, keyless"),
             ("wayback-cdx", "historical page state", "the index of record; no quota to exceed"),
             ("loc", "newspapers and print collections",
              "explicit 20/min rate table with the block duration — note the probe hit a "
              "Cloudflare wall, so expect to identify the client properly"),
             ("openlibrary", "book metadata", "1/s unidentified, 3/s with a contact header"),
             ("doaj", "open-access journal articles", "2/s published, keyless"),
             ("pubmed", "biomedical literature", "3/s keyless, 10/s with a free NCBI key"),
             ("zenodo", "research data deposits", "guest 60/min published per endpoint"),
             ("met-museum", "museum objects and images", "80/s, no key, no registration")]
    for slug, need, why in picks:
        L.append(f"| {need} | {BY[slug]['name']} | {why} |")
    L.append("")
    L.append("The honest summary: **an archival pipeline can be built entirely from keyless, "
             "rate-published public APIs**, and the binding constraint is not quota but "
             "politeness — arXiv's one request every three seconds is the slowest published rate "
             "in the set, and it is slow on purpose.")
    L.append("")
    L.append("Two caveats on that table, both measured: the Library of Congress API publishes the "
             "cleanest rate table here but answered the probe with a Cloudflare challenge, and "
             "OpenAlex's free tier is a dollar a day rather than an unlimited keyless pool. Both "
             "are still the right choice for their job; neither is frictionless.")
    L.append("")
    pub = [r for r in facts if r["category"] == "publisher"]
    L.append(f"What is *not* in the table is just as informative: none of the {len(facts)} providers "
             f"needs a payment card, none offers a one-time trial credit, and the "
             f"{len(pub)} publisher and patent endpoints are the only group where no free call "
             "figure exists at all.")
    return "\n".join(L) + "\n"


# ----------------------------------------------------------------------- probes
def build_probes():
    L = ["# Live probe results", ""]
    L.append("One unauthenticated `GET` per documented endpoint, from one machine, on "
             f"{TODAY}. This is a different evidence class from the documentation snapshots: it "
             "shows whether the endpoint answers a caller with no key, not what the allowance is.")
    L.append("")
    L.append("Verdicts: `ok` = 2xx with a machine-readable body; `ok-html` = 2xx but an HTML page "
             "rather than the API; `auth` = 401/403 with a plain refusal; `bot-wall` = 403/503 "
             "carrying a Cloudflare, Anubis or reCAPTCHA challenge; `blocked` = 429/503; "
             "`not-found` = 404; `error` = no answer (DNS, TLS, timeout). The `auth` / `bot-wall` "
             "split matters: the first needs a credential, the second needs a browser.")
    L.append("")
    L.append("| Provider | Status | Verdict | ms | Rate-limit headers | URL |")
    L.append("|---|---:|---|---:|---|---|")
    for r in sorted(facts, key=lambda x: x["name"].lower()):
        p = r.get("probe") or {}
        rh = p.get("rate_headers") or {}
        rh_s = ", ".join(f"`{k}: {v}`" for k, v in list(rh.items())[:3]) if rh else "—"
        L.append(f"| {r['name']} | {p.get('status', '—')} | {verdict_label(r)} | "
                 f"{p.get('ms', '—')} | {rh_s} | `{(p.get('url') or '—')[:88]}` |")
    L.append("")
    hist = [r for r in facts if (r.get("probe") or {}).get("history")]
    if hist:
        L.append("## Endpoints that changed their answer between attempts")
        L.append("")
        L.append("The probe keeps earlier results instead of overwriting them, so a throttle or a "
                 "transient failure stays visible:")
        L.append("")
        for r in hist:
            p = r["probe"]
            seq = [f"HTTP {h.get('status')}" for h in p["history"]] + [f"HTTP {p.get('status')}"]
            L.append(f"- **{r['name']}** — " + " → ".join(seq) + f" (final: {verdict_label(r)})")
        L.append("")
    L.append("## Rate-limit headers seen in the wild")
    L.append("")
    L.append("These are the only endpoints that told the probe its budget in the response "
             "headers, which is what a gateway would use to pace itself automatically:")
    L.append("")
    for r in facts:
        rh = (r.get("probe") or {}).get("rate_headers") or {}
        if rh:
            L.append(f"- **{r['name']}** — " + ", ".join(f"`{k}: {v}`" for k, v in rh.items()))
    L.append("")
    L.append("Everything else publishes its allowance in prose or not at all. That is the single "
             "biggest practical difference from the commercial scraping market, where rate-limit "
             "headers and per-call prices are standard.")
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------------ README
def build_readme():
    numbered = [r for r in facts if r["monthly_calls"]]
    ok = sum(1 for r in facts if str((r.get("probe") or {}).get("verdict", "")).startswith("ok"))
    lo = sum(1 for r in facts if r["confidence"] == "low")
    L = ["# Academic and archival APIs: documented free allowances", ""]
    L.append(f"An inventory of **{len(facts)} academic and archival services that expose an HTTP "
             f"API** — web archives, national archive catalogues, library and museum aggregators, "
             f"scholarly graphs, bibliographic indexes, research-data repositories, life-science "
             f"data services and publisher TDM endpoints. Compiled {TODAY}.")
    L.append("")
    L.append("Each provider gets a page with its documented rate, the verbatim sentence that "
             "states it, a link to the captured snapshot, and the result of one live "
             "unauthenticated request against its API.")
    L.append("")
    L.append("| Metric | Value |")
    L.append("|---|---|")
    L.append(f"| Providers catalogued | {len(facts)} |")
    L.append(f"| With a documented call figure | {len(numbered)} |")
    L.append(f"| Documented volume, 1 account each | {fmt(sum(r['monthly_calls'] for r in numbered))} calls/month |")
    L.append(f"| Documented volume, 5 accounts each | {fmt(sum(r['monthly_calls'] for r in numbered)*5)} calls/month |")
    L.append(f"| Answered an unauthenticated probe | {ok} of {len(facts)} |")
    L.append(f"| Serve a verified llms.txt | {sum(1 for r in facts if r['llms'])} |")
    L.append(f"| Require a payment card for the free tier | {sum(1 for r in facts if r['card'] is True)} |")
    L.append("")
    L.append("The two volume figures are **ceilings**: only three providers publish a quota "
             "(monthly, daily, or a daily dollar budget with a price list); for the rest the "
             "monthly number is the published rate times the seconds in a 30-day month. "
             "`reports/03-post-analysis.md` splits the three published quotas from the rate "
             "ceilings and shows that two rows account for 89% of the total.")
    L.append("")
    L.append("## Reports")
    L.append("")
    L.append("| File | Contents |")
    L.append("|---|---|")
    L.append("| `reports/00-methodology.md` | how every number was produced, and what it does not mean |")
    L.append("| `reports/01-inventory.md` | the ranked table plus a per-category catalogue of all providers |")
    L.append("| `reports/02-deep-reviews.md` | eight providers reviewed in depth |")
    L.append("| `reports/03-post-analysis.md` | totals, friction, probe results, coverage, a verified stack |")
    L.append("| `reports/04-probes.md` | what each endpoint answered, with its rate-limit headers |")
    L.append("| `providers/<slug>.md` | one page per provider |")
    L.append("")
    L.append("## Data")
    L.append("")
    L.append("| File | Contents |")
    L.append("|---|---|")
    L.append("| `data/candidates.json` | the working set: slug, name, category, home, docs, probe URL |")
    L.append("| `data/facts.json` | the curated table: figure, derivation, quote, URL, snapshot, probe |")
    L.append("| `data/probes.json` | one live request per endpoint: status, latency, headers, body head |")
    L.append("| `data/llms.json` | per-provider llms.txt verdict, with the rejection reason |")
    L.append("| `data/snapshots/<slug>/` | gzip + plain text + `meta.json` (URL, status, sha256) |")
    L.append("")
    L.append("## Reproduce")
    L.append("")
    L.append("```sh")
    L.append("make all       # fetch, probe, llms, facts, reports, test")
    L.append("make test      # integrity: quotes verbatim, figures recompute, reports consistent")
    L.append("make check     # re-fetch every recorded source and compare sha256")
    L.append("```")
    L.append("")
    L.append("`make test` is the guarantee: it fails if any quote in `data/facts.json` is not "
             "present verbatim in the snapshot it cites, or if any derived monthly figure does not "
             "reproduce from the rate named in its derivation.")
    L.append("")
    L.append("## Limits")
    L.append("")
    L.append("- A rate is not a quota. Ceilings are labelled as ceilings wherever they appear.")
    L.append("- Shared pools (Semantic Scholar) and CPU-time limits (Wikidata) are deliberately not "
             "converted to call counts.")
    L.append(f"- `low` confidence means this run could not verify the allowance — a bot "
             f"interstitial, an application shell, a login wall or a dead host — not that the "
             f"service is bad. {lo} providers are in that state and each page says why.")
    L.append("- One probe per endpoint from one IP is evidence that an endpoint answers, not a "
             "load test.")
    L.append("- Free tiers change without notice; every number is as of its snapshot.")
    L.append("- No terms-of-service analysis. This is a technical inventory of documented "
             "allowances and makes no claim that any particular use is permitted.")
    L.append("")
    L.append("Licence: 0BSD (see `LICENSE`).")
    return "\n".join(L) + "\n"


def main():
    os.makedirs(REP, exist_ok=True)
    os.makedirs(PROV, exist_ok=True)
    def put(path, text):
        with open(path, "w") as fh:
            fh.write(text)

    for r in facts:
        put(os.path.join(PROV, r["slug"] + ".md"), prov_md(r))
    put(os.path.join(REP, "00-methodology.md"), build_methodology())
    put(os.path.join(REP, "01-inventory.md"), build_inventory())
    put(os.path.join(REP, "02-deep-reviews.md"), build_reviews())
    put(os.path.join(REP, "03-post-analysis.md"), build_post_analysis())
    put(os.path.join(REP, "04-probes.md"), build_probes())
    put(os.path.join(ROOT, "README.md"), build_readme())
    print(f"wrote 5 reports, {len(facts)} provider pages and README.md")


if __name__ == "__main__":
    main()
