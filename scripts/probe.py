#!/usr/bin/env python3
"""Live-probe each provider's API endpoint and record what came back.

This is the second evidence class, kept strictly apart from the documentation
snapshots: the docs say what the allowance is, the probe says whether an
unauthenticated call worked from this machine right now.

For every provider it records: HTTP status, latency, response content-type,
rate-limit headers, the first 400 bytes of the body, and a verdict:

  ok            2xx with a body that parses (or is plainly text)
  auth          401/403 — an API key is required for this endpoint
  bot-wall      401/403/503 carrying a challenge page (Cloudflare, Anubis, reCAPTCHA):
                the endpoint may well be open, but this client cannot pass the wall
  payment       402 — payment required
  blocked       429/503 — rate-limited or refused at probe time
  not-found     404 — the documented path is wrong or gone
  error         anything else, including connection failures

A probe is one request from one IP. It is evidence that the endpoint answers
unauthenticated callers at all, not evidence about quota.

Usage: python3 scripts/probe.py [slug ...]
"""
import concurrent.futures as cf
import datetime
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import fetch, DATA  # noqa: E402

OUT = os.path.join(DATA, "probes.json")


BOT_MARKS = ("just a moment", "cf-mitigated", "checking your browser", "recaptcha",
             "making sure you're not a bot", "anubis", "enable javascript and cookies",
             "attention required", "access denied", "captcha")


def is_bot_wall(body: bytes) -> bool:
    head = body[:4000].decode("utf-8", "replace").lower()
    return any(m in head for m in BOT_MARKS)


def verdict(status: int, body: bytes) -> str:
    if status in (401, 403):
        # a 403 that carries a challenge page is an anti-bot wall, not an auth requirement:
        # the two call for completely different responses from a client
        return "bot-wall" if is_bot_wall(body) else "auth"
    if status == 402:
        return "payment"
    if status in (429, 503):
        return "blocked"
    if status == 404:
        return "not-found"
    if 200 <= status < 300:
        head = body[:200].lstrip().lower()
        if head.startswith((b"<!doctype", b"<html")):
            # a 200 HTML page at an API path is usually a login wall or a soft 404
            return "ok-html"
        return "ok"
    return "error"


def probe(p: dict) -> dict:
    url = p.get("api")
    if not url:
        return {"slug": p["slug"], "url": None, "status": 0, "verdict": "none"}
    t0 = time.time()
    res = fetch(url, accept="application/json,application/xml,text/xml,text/html,*/*")
    ms = round((time.time() - t0) * 1000)
    raw = res.pop("raw")
    body_head = raw[:400].decode("utf-8", "replace")
    v = verdict(res["status"], raw)
    return {"slug": p["slug"], "name": p["name"], "url": url, "status": res["status"],
            "verdict": v, "ms": ms, "content_type": res["content_type"],
            "bytes": res["bytes"], "final_url": res["final_url"],
            "rate_headers": res.get("rate_headers") or {},
            "probed_at": res["fetched_at"],
            "body_head": re.sub(r"\s+", " ", body_head)[:400],
            "sha256": res["sha256"]}


def main():
    cands = json.load(open(os.path.join(DATA, "candidates.json")))["providers"]
    want = set(sys.argv[1:])
    if want:
        cands = [p for p in cands if p["slug"] in want]
    prev = json.load(open(OUT)) if os.path.exists(OUT) else {}
    out = dict(prev)
    t0 = time.time()
    with cf.ThreadPoolExecutor(6) as ex:
        futs = {ex.submit(probe, p): p["slug"] for p in cands}
        for f in cf.as_completed(futs):
            slug = futs[f]
            try:
                r = f.result()
            except Exception as e:  # noqa: BLE001
                r = {"slug": slug, "status": 0, "verdict": "error", "error": str(e)[:120]}
            # keep a previous result only when the answer CHANGED, so a throttle stays
            # visible instead of being silently overwritten by a later successful attempt
            prev = out.get(slug) or {}
            if prev.get("verdict") and prev.get("verdict") != r.get("verdict"):
                hist = prev.get("history") or []
                hist.append({k: v for k, v in prev.items() if k != "history"})
                r["history"] = hist[-5:]
            elif prev.get("history"):
                r["history"] = prev["history"]
            out[slug] = r
            print(f"{slug:24s} {r.get('status'):>4} {r.get('verdict'):10s} "
                  f"{r.get('ms', 0):>6}ms {r.get('url', '')}", flush=True)
            json.dump(out, open(OUT, "w"), indent=1, sort_keys=True)
    ok = sum(1 for r in out.values() if str(r.get("verdict", "")).startswith("ok"))
    print(f"\n{len(out)} probed, {ok} answered unauthenticated, {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
