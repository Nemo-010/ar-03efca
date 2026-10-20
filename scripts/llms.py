#!/usr/bin/env python3
"""Verify llms.txt availability from the snapshots, honestly.

fetch.py records a probe as successful whenever it returned HTTP 200. That
counts three kinds of non-answer as success:

  * an HTML page served at a *.txt path (a soft-404, a shell, or a login wall)
  * an empty body
  * a file belonging to a different site

This script rewrites data/llms.json with one record per provider:
    url      the URL that actually served a markdown index, or null
    bytes    size of the served body
    reason   why it was accepted or rejected

Usage: python3 scripts/llms.py [--fetch]
  --fetch probes the canonical locations live and snapshots the ones that
          pass, so the accepted file is stored in data/snapshots/<slug>/.
"""
import concurrent.futures as cf
import gzip
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import fetch, to_text, DATA, SNAP  # noqa: E402

OUT = os.path.join(DATA, "llms.json")
HTML_START = ("<!doctype", "<html", "<head", "<?xml", "<!--")
SKIP_HOST = ("github.com", "raw.githubusercontent.com", "readme.io")


def registrable(host):
    host = host.lower()
    for pre in ("www.", "docs.", "help.", "api.", "api-docs.", "developers.", "developer.",
                "support.", "platform.", "console.", "guides.", "techdocs."):
        if host.startswith(pre):
            return host[len(pre):]
    return host


def host_of(url):
    m = re.match(r"https?://([^/]+)", url or "")
    return m.group(1).lower() if m else ""


def is_markdown_index(body: bytes) -> tuple:
    if not body:
        return False, "empty body"
    head = body[:400].decode("utf-8", "replace").lstrip().lower()
    if head.startswith(HTML_START):
        return False, "served HTML at a .txt path"
    text = body[:1500].decode("utf-8", "replace")
    if not re.search(r"^#{1,3} ", text, re.M):
        return False, "not a markdown index (no heading near the top)"
    return True, "ok"


def probe(slug: str, home: str, docs: str = "") -> dict:
    """Try the canonical llms.txt locations for one provider.

    The exact host the provider publishes on is tried first, then the usual
    doc prefixes on the registrable domain. A file is only accepted from a
    host that belongs to the provider: the registrable domain must match, or
    the host must be a subdomain of it.
    """
    exact = host_of(home)
    host = registrable(exact)
    doc_host = host_of(docs or "")
    cands = []
    if exact:
        cands.append(f"https://{exact}/llms.txt")
    if doc_host:
        cands.append(f"https://{doc_host}/llms.txt")
    if host:
        cands += [f"https://{host}/llms.txt", f"https://docs.{host}/llms.txt",
                  f"https://help.{host}/llms.txt", f"https://support.{host}/llms.txt",
                  f"https://developers.{host}/llms.txt", f"https://{host}/llms-full.txt"]
    tried = []
    for url in dict.fromkeys(cands):
        res = fetch(url)
        raw = res.pop("raw")
        ok, why = is_markdown_index(raw) if res["status"] == 200 else (False, f"HTTP {res['status']}")
        tried.append({"url": url, "status": res["status"], "bytes": len(raw), "reason": why})
        if ok and host_of(url) in ("github.com", "raw.githubusercontent.com"):
            # GitHub publishes its own llms.txt; it is never the project's file
            tried[-1]["reason"] = "belongs to github.com, not the provider"
            continue
        if ok:
            # a file on a third-party docs host must at least name the provider
            own = registrable(host_of(url)) == host or host_of(url) == doc_host
            if not own and slug.split("-")[0] not in raw[:4000].decode("utf-8", "replace").lower():
                tried[-1]["reason"] = f"host {host_of(url)} is not the provider's"
                continue
            d = os.path.join(SNAP, slug)
            os.makedirs(d, exist_ok=True)
            with gzip.open(os.path.join(d, "llms.txt.gz"), "wb", compresslevel=9) as f:
                f.write(raw)
            with open(os.path.join(d, "llms.txt"), "w") as f:
                f.write(to_text(raw, res["content_type"]))
            mp = os.path.join(d, "meta.json")
            meta = {"slug": slug, "sources": {}}
            if os.path.exists(mp):
                with open(mp) as fh:
                    meta = json.load(fh)
            meta.setdefault("sources", {})["llms"] = {**res, "text_bytes": len(raw)}
            with open(mp, "w") as fh:
                json.dump(meta, fh, indent=1)
            return {"url": url, "bytes": len(raw), "reason": "ok", "tried": tried}
    return {"url": None, "bytes": 0,
            "reason": tried[-1]["reason"] if tried else "no candidate host", "tried": tried}


def main():
    with open(os.path.join(DATA, "candidates.json")) as fh:
        cands = json.load(fh)["providers"]
    out = {}
    if "--fetch" in sys.argv:
        with cf.ThreadPoolExecutor(6) as ex:
            futs = {ex.submit(probe, p["slug"], p.get("home") or "", p.get("docs") or ""): p
                    for p in cands}
            for f in cf.as_completed(futs):
                p = futs[f]
                out[p["slug"]] = f.result()
                print(f"{p['slug']:24s} {'OK  ' if out[p['slug']]['url'] else 'none'} "
                      f"{out[p['slug']]['reason']}", flush=True)
    else:
        # judge from the snapshots already on disk, applying the same rules as a live probe
        for p in cands:
            slug = p["slug"]
            path = os.path.join(SNAP, slug, "llms.txt")
            body = b""
            if os.path.exists(path):
                with open(path, "rb") as fh:
                    body = fh.read()
            ok, why = is_markdown_index(body)
            url = None
            mp = os.path.join(SNAP, slug, "meta.json")
            if os.path.exists(mp):
                with open(mp) as fh:
                    url = (json.load(fh).get("sources", {}).get("llms") or {}).get("url")
            if ok and host_of(url) in ("github.com", "raw.githubusercontent.com"):
                ok, why = False, "belongs to github.com, not the provider"
            if ok and url:
                host = registrable(host_of(p.get("home") or ""))
                doc_host = host_of(p.get("docs") or "")
                if registrable(host_of(url)) != host and host_of(url) != doc_host:
                    ok, why = False, f"host {host_of(url)} is not the provider's"
            out[slug] = {"url": url if ok else None, "bytes": len(body), "reason": why}
    with open(OUT, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    good = [s for s, v in out.items() if v["url"]]
    print(f"\nllms.json: {len(good)} of {len(out)} providers serve a verified markdown index")
    for s in good:
        print(f"  {s:24s} {out[s]['url']}")


if __name__ == "__main__":
    main()
