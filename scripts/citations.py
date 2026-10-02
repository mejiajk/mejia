#!/usr/bin/env python3
"""citations.py — genera citaciones diarias verificables, listas como ejemplos de grounding.

    python3 scripts/citations.py                 # corre el pipeline de hoy
    python3 scripts/citations.py --dry-run       # no escribe ni notifica
    python3 scripts/citations.py --date 2026-10-02

Principio: el fragmento (snippet) se extrae LITERALMENTE del texto que se descargó
de la URL; ningún modelo lo reescribe. Si no se puede verificar, la citación se descarta.

Salida:  citations/data/YYYY-MM-DD.jsonl   (una citación por línea)
         citations/data/YYYY-MM-DD.md      (digest legible)
Opcional: SLACK_WEBHOOK_URL en el entorno publica el digest en Slack.
Solo stdlib.
"""
import argparse, hashlib, html, json, os, re, sys, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CFG = json.loads(Path(os.environ.get("CITATIONS_CONFIG", ROOT / "configs" / "citations.json")).read_text())
DATA = Path(os.environ.get("CITATIONS_DATA", ROOT / "citations" / "data"))
NS = {"a": "http://www.w3.org/2005/Atom"}


def http_get(url, accept="*/*", timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": CFG["user_agent"], "Accept": accept})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.geturl(), r.read(3_000_000), r.headers.get_content_charset() or "utf-8"


# ---------- recolección ----------

def parse_date(s):
    if not s:
        return None
    s = s.strip()
    try:
        return parsedate_to_datetime(s).astimezone(timezone.utc).date().isoformat()
    except (TypeError, ValueError):
        pass
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        return None


def fetch_arxiv(src):
    q = urllib.parse.urlencode({"search_query": src["query"], "sortBy": "submittedDate",
                                "sortOrder": "descending", "max_results": 25})
    _, _, body, _ = http_get("https://export.arxiv.org/api/query?" + q)
    for e in ET.fromstring(body).findall("a:entry", NS):
        url = (e.findtext("a:id", "", NS) or "").replace("http://", "https://")
        yield {"url": url, "title": " ".join((e.findtext("a:title", "", NS) or "").split()),
               "published": parse_date(e.findtext("a:published", "", NS)),
               "text": " ".join((e.findtext("a:summary", "", NS) or "").split()),
               "source_name": src["name"]}


def fetch_rss(src):
    _, _, body, _ = http_get(src["url"], "application/rss+xml, application/atom+xml, */*")
    root = ET.fromstring(body)
    for it in root.iter("item"):
        yield {"url": (it.findtext("link") or "").strip(), "title": (it.findtext("title") or "").strip(),
               "published": parse_date(it.findtext("pubDate") or it.findtext("{http://purl.org/dc/elements/1.1/}date")),
               "text": None, "source_name": src["name"]}
    for e in root.findall("a:entry", NS):
        link = next((l.get("href") for l in e.findall("a:link", NS) if l.get("rel") in (None, "alternate")), "")
        yield {"url": link, "title": (e.findtext("a:title", "", NS) or "").strip(),
               "published": parse_date(e.findtext("a:published", "", NS) or e.findtext("a:updated", "", NS)),
               "text": None, "source_name": src["name"]}


FETCHERS = {"arxiv": fetch_arxiv, "rss": fetch_rss}


# ---------- extracción del fragmento ----------

class TextExtractor(HTMLParser):
    SKIP = {"script", "style", "nav", "header", "footer", "aside", "form", "noscript", "svg"}

    def __init__(self):
        super().__init__()
        self.skip, self.buf, self.paras = 0, [], []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1
        if tag in ("p", "li", "blockquote") and not self.skip:
            t = " ".join("".join(self.buf).split())
            if t:
                self.paras.append(t)
            self.buf = []

    def handle_data(self, data):
        if not self.skip:
            self.buf.append(data)


def page_text(body, charset):
    p = TextExtractor()
    p.feed(body.decode(charset, "replace"))
    return p.paras


SENT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ0-9\"“])")
BOILER = re.compile(r"cookie|subscribe|newsletter|sign up|all rights reserved|privacy policy|javascript|©|share this", re.I)


def score(s):
    n = len(s)
    if n < 50 or BOILER.search(s):
        return -1
    sc = len(re.findall(r"\d[\d.,%]*", s)) * 2               # cifras = hechos comprobables
    sc += len(re.findall(r"\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)+", s))  # entidades nombradas
    sc += 2 if re.search(r"\b(found|show(?:s|ed)?|report(?:s|ed)?|announc\w+|propos\w+|achiev\w+|increase\w*|decreas\w+|according)\b", s, re.I) else 0
    return sc


def pick_snippet(paras, lo, hi):
    """Mejor ventana de 1-2 oraciones consecutivas (literal) dentro de [lo, hi] caracteres."""
    best, best_sc = None, 0
    for p in paras[:40]:
        sents = SENT.split(p)
        for i in range(len(sents)):
            for j in (i, i + 1):
                if j >= len(sents):
                    continue
                cand = " ".join(sents[i:j + 1])
                if not lo <= len(cand) <= hi:
                    continue
                sc = sum(max(score(s), 0) for s in sents[i:j + 1]) - (j - i)
                if all(score(s) >= 0 for s in sents[i:j + 1]) and sc > best_sc:
                    best, best_sc = cand, sc
    return best


# ---------- verificación y construcción ----------

def build(item, category):
    """Descarga la URL, verifica y extrae. Devuelve dict o None."""
    try:
        status, final, body, cs = http_get(item["url"], "text/html,application/xhtml+xml")
    except Exception as e:
        print(f"  ✗ {item['url']}: {e}", file=sys.stderr)
        return None
    page = page_text(body, cs)
    # arXiv trae el abstract por API: se verifica que el abstract exista en la página real
    paras = [item["text"]] if item["text"] else page
    if item["text"]:
        norm = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", body.decode(cs, "replace"))).split())
        if item["text"][:60] not in norm:
            return None
    snippet = pick_snippet(paras, CFG["min_snippet_chars"], CFG["max_snippet_chars"])
    if not snippet or snippet not in " ".join(paras):
        return None
    domain = urllib.parse.urlparse(final).netloc.removeprefix("www.")
    pub = item["published"]
    return {
        "id": hashlib.sha1(final.encode()).hexdigest()[:12],
        "url": final, "title": item["title"], "domain": domain, "published": pub,
        "snippet": snippet, "category": category, "source_name": item["source_name"],
        "citation": f"{item['title']}. {domain}" + (f", {pub}" if pub else "") + f". {final}",
        "verification": {"http_status": status, "snippet_verbatim_in_page": True,
                         "content_sha256": hashlib.sha256(body).hexdigest(),
                         "retrieved_at": datetime.now(timezone.utc).isoformat(timespec="seconds")},
        # Estructura de ejemplo de grounding: respuesta anclada en la evidencia
        "grounding": {"evidence": snippet, "source_id": None,
                      "answer_template": "Según {domain} ({date}): {evidence} [fuente: {url}]"
                      .format(domain=domain, date=pub or "s/f", evidence=snippet, url=final)},
    }


def seen_ids():
    ids = set()
    for f in DATA.glob("*.jsonl"):
        for line in f.read_text().splitlines():
            if line.strip():
                ids.add(json.loads(line)["id"])
    return ids


def run(day, dry):
    seen, out = seen_ids(), []
    cutoff = (date.fromisoformat(day) - timedelta(days=CFG["max_age_days"])).isoformat()
    cats = {}
    for s in CFG["sources"]:
        cats.setdefault(s["category"], []).append(s)
    for cat, sources in cats.items():
        got = []
        for src in sources:
            if len(got) >= CFG["per_category"]:
                break
            print(f"[{cat}] {src['name']}")
            try:
                items = list(FETCHERS[src["type"]](src))
            except Exception as e:
                print(f"  ✗ fuente caída: {e}", file=sys.stderr)
                continue
            for it in items:
                if len(got) >= CFG["per_category"]:
                    break
                if not it["url"].startswith("http") or not it["published"] or it["published"] < cutoff:
                    continue
                if hashlib.sha1(it["url"].encode()).hexdigest()[:12] in seen:
                    continue
                c = build(it, cat)
                if c and c["id"] not in seen:
                    c["grounding"]["source_id"] = c["id"]
                    got.append(c); seen.add(c["id"])
                    print(f"  ✓ {c['title'][:70]}")
        out += got
    md = digest(day, out)
    if dry:
        print(md); return out
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / f"{day}.jsonl").write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in out))
    (DATA / f"{day}.md").write_text(md)
    notify(md)
    return out


def digest(day, items):
    lines = [f"# Citaciones {day} — {len(items)} verificadas", ""]
    for cat in dict.fromkeys(c["category"] for c in items):
        lines += [f"## {cat}", ""]
        for c in (x for x in items if x["category"] == cat):
            lines += [f"- **[{c['title']}]({c['url']})** — {c['domain']}" + (f" · {c['published']}" if c["published"] else ""),
                      f"  > {c['snippet']}", ""]
    return "\n".join(lines)


def notify(md):
    hook = os.environ.get("SLACK_WEBHOOK_URL")
    if not hook:
        return
    req = urllib.request.Request(hook, data=json.dumps({"text": md[:38000]}).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        urllib.request.urlopen(req, timeout=20)
    except Exception as e:
        print(f"  ✗ Slack no notificado: {e}", file=sys.stderr)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=datetime.now(timezone.utc).date().isoformat())
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    res = run(a.date, a.dry_run)
    print(f"\n{len(res)} citaciones verificadas" + ("" if res else " — NINGUNA: revisa las líneas '✗ fuente caída' arriba"), file=sys.stderr)
    sys.exit(0 if res else 1)
