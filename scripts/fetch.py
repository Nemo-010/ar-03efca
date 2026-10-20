#!/usr/bin/env python3
"""Fetch public documentation pages for every candidate provider.

Snapshots are stored gzip-compressed under data/snapshots/<slug>/ as
<kind>.gz plus a plain-text rendering <kind>.txt (HTML stripped) for
grepping. Every fetch is recorded in meta.json with URL, HTTP status,
final URL, byte size, sha256 and fetch time.

Usage: python3 scripts/fetch.py [slug ...]
"""
import concurrent.futures as cf
import datetime
import gzip
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
SNAP = os.path.join(DATA, "snapshots")
UA = ("ar-research/0.1 (public API documentation inventory; "
      "+https://github.com/Nemo-010/ar-03efca)")
MAX_BYTES = 3_000_000
TIMEOUT = 25
WORKERS = 12

TAG_RE = re.compile(r"<(script|style|svg|noscript)\b.*?</\1>", re.S | re.I)
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
ANY_TAG = re.compile(r"<[^>]+>")


def to_text(raw: bytes, ctype: str) -> str:
    if "html" in ctype or raw[:200].lstrip().lower().startswith((b"<!doctype", b"<html")):
        s = raw.decode("utf-8", "replace")
        s = COMMENT_RE.sub(" ", s)
        s = TAG_RE.sub(" ", s)
        s = ANY_TAG.sub(" ", s)
        s = html.unescape(s)
        s = re.sub(r"[ \t\r\f\v]+", " ", s)
        s = re.sub(r"\n\s*\n+", "\n", s)
        return s.strip()
    return raw.decode("utf-8", "replace")


def fetch(url: str, accept: str = "text/html,text/plain,application/json,*/*") -> dict:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": accept,
        "Accept-Language": "en",
    })
    started = datetime.datetime.now(datetime.timezone.utc)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            raw = r.read(MAX_BYTES + 1)
            status = r.status
            ctype = r.headers.get("Content-Type", "")
            final = r.geturl()
            headers = dict(r.headers)
    except urllib.error.HTTPError as e:
        try:
            raw = e.read(MAX_BYTES)
        except Exception:
            raw = b""
        status = e.code
        ctype = e.headers.get("Content-Type", "") if e.headers else ""
        headers = dict(e.headers) if e.headers else {}
        final = url
    except Exception as e:  # noqa: BLE001
        status = 0
        ctype = ""
        final = url
        headers = {}
        raw = str(e).encode()
    truncated = len(raw) > MAX_BYTES
    raw = raw[:MAX_BYTES]
    return {"url": url, "status": status, "final_url": final, "content_type": ctype,
            "bytes": len(raw), "truncated": truncated,
            "sha256": hashlib.sha256(raw).hexdigest(),
            "fetched_at": started.isoformat(timespec="seconds"),
            "rate_headers": {k: v for k, v in headers.items()
                             if k.lower().startswith(("x-ratelimit", "ratelimit",
                                                      "retry-after", "x-rate"))},
            "raw": raw}


def save(slug: str, kind: str, res: dict) -> dict:
    d = os.path.join(SNAP, slug)
    os.makedirs(d, exist_ok=True)
    with gzip.open(os.path.join(d, kind + ".gz"), "wb", compresslevel=9) as f:
        f.write(res.pop("raw"))
    with gzip.open(os.path.join(d, kind + ".gz"), "rb") as gz:
        txt = to_text(gz.read(), res["content_type"])
    with open(os.path.join(d, kind + ".txt"), "w") as f:
        f.write(txt)
    res["text_bytes"] = len(txt)
    return res


def work(p: dict) -> str:
    slug = p["slug"]
    meta_path = os.path.join(SNAP, slug, "meta.json")
    meta = {"slug": slug, "name": p["name"], "category": p["category"],
            "fetched_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
            "sources": {}}

    jobs = []
    for kind in ("docs", "pricing", "home"):
        if p.get(kind):
            jobs.append((kind, p[kind]))

    probes = []
    if p.get("llms"):
        probes.append(("llms", p["llms"]))
    for u in (p.get("docs"), p.get("home")):
        if not u:
            continue
        probes.append(("llms", u.rstrip("/") + "/llms.txt"))
    for u in (p.get("docs"), p.get("home")):
        m = re.match(r"https?://([^/]+)", u or "")
        if not m:
            continue
        host = m.group(1)
        if host.startswith(("www.", "docs.", "api.")):
            host = re.sub(r"^(www|docs|api)\.", "", host)
        probes.append(("llms", f"https://docs.{host}/llms.txt"))
        break

    seen = set()
    for kind, url in jobs + probes:
        if url in seen:
            continue
        seen.add(url)
        res = fetch(url)
        key = kind if kind not in meta["sources"] else f"{kind}-{hashlib.sha1(url.encode()).hexdigest()[:6]}"
        if res["status"] == 200:
            meta["sources"][key] = save(slug, kind if key == kind else key, res)
        else:
            res.pop("raw")
            meta["sources"][key + "-err"] = res
        time.sleep(0.05)

    os.makedirs(os.path.dirname(meta_path), exist_ok=True)
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=1)
    ok = sum(1 for v in meta["sources"].values() if v.get("status") == 200)
    return f"{slug:24s} ok={ok:2d} / {len(meta['sources'])}"


def main():
    with open(os.path.join(DATA, "candidates.json")) as f:
        doc = json.load(f)
    provs = doc["providers"]
    want = set(sys.argv[1:])
    if want:
        provs = [p for p in provs if p["slug"] in want]
    os.makedirs(SNAP, exist_ok=True)
    t0 = time.time()
    with cf.ThreadPoolExecutor(WORKERS) as ex:
        futs = {ex.submit(work, p): p["slug"] for p in provs}
        for f in cf.as_completed(futs):
            try:
                print(f.result(), flush=True)
            except Exception as e:  # noqa: BLE001
                print(f"FAIL {futs[f]}: {e}", flush=True)
    print(f"done in {time.time()-t0:.0f}s, {len(provs)} providers")


if __name__ == "__main__":
    main()
