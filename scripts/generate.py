
import os, json, yaml, re, datetime, xml.sax.saxutils as sax

ROOT = os.path.dirname(os.path.dirname(__file__))
OUT = os.path.join(ROOT, "out")
os.makedirs(OUT, exist_ok=True)

def read_yaml(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data or []

def ensure_url(permalink, base="/"):
    if permalink:
        return permalink if permalink.startswith("/") else "/" + permalink
    return base

def parse_frontmatter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", content

def load_pages():
    docs = []
    # index
    idx_path = os.path.join(ROOT, "index.md")
    if os.path.exists(idx_path):
        with open(idx_path, "r", encoding="utf-8") as f:
            fm, body = parse_frontmatter(f.read())
        title = "홈"
        m = re.search(r"title:\s*(.+)", fm)
        if m: title = m.group(1).strip()
        docs.append({
            "title": title,
            "url": "/",
            "excerpt": "홈",
            "tags": []
        })
    # pages/*
    pages_dir = os.path.join(ROOT, "pages")
    if os.path.isdir(pages_dir):
        for name in sorted(os.listdir(pages_dir)):
            if not name.endswith((".md",".html")): continue
            p = os.path.join(pages_dir, name)
            with open(p, "r", encoding="utf-8") as f:
                fm, body = parse_frontmatter(f.read())
            title = name
            permalink = None
            m = re.search(r"title:\s*(.+)", fm)
            if m: title = m.group(1).strip()
            m2 = re.search(r"permalink:\s*(.+)", fm)
            if m2: permalink = m2.group(1).strip()
            url = ensure_url(permalink, f"/pages/{name}")
            docs.append({
                "title": title,
                "url": url,
                "excerpt": re.sub(r"\s+"," ", body)[:160],
                "tags": []
            })
    return docs

def write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def gen_ics(schedule):
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//StreamHub//Schedule//KO",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH"
    ]
    def dtfmt(s):
        try:
            dt = datetime.datetime.fromisoformat(s)
        except Exception:
            dt = datetime.datetime.strptime(s, "%Y-%m-%d")
        return dt.strftime("%Y%m%dT%H%M%S")
    for e in schedule:
        start = e.get("date_start")
        end = e.get("date_end") or e.get("date_start")
        uid = (e.get("id","") or "").replace(" ","") + "@streamhub"
        title = e.get("title","")
        desc = (e.get("platform","") + (" — " + e.get("url","") if e.get("url") else "")).strip()
        lines += [
            "BEGIN:VEVENT",
            f"UID:{uid}",
            f"DTSTART:{dtfmt(start)}",
            f"DTEND:{dtfmt(end)}",
            f"SUMMARY:{sax.escape(title)}",
            f"DESCRIPTION:{sax.escape(desc)}",
            "END:VEVENT"
        ]
    lines.append("END:VCALENDAR")
    return "\n".join(lines)

def gen_rss(items, title, link_path):
    now = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")
    xml = [f'<?xml version="1.0" encoding="UTF-8"?>',
           f'<rss version="2.0"><channel>',
           f'<title>{sax.escape(title)}</title>',
           f'<link>{sax.escape(link_path)}</link>',
           f'<description>{sax.escape(title)}</description>',
           f'<lastBuildDate>{now}</lastBuildDate>']
    for it in items:
        t = it.get("title","")
        u = it.get("url","") or it.get("video_id","")
        link = u
        if it.get("platform") == "youtube" and it.get("video_id"):
            link = f"https://www.youtube.com/watch?v={it['video_id']}"
        xml += ["<item>",
                f"<title>{sax.escape(t)}</title>",
                f"<link>{sax.escape(link)}</link>",
                "</item>"]
    xml.append("</channel></rss>")
    return "\n".join(xml)

def main():
    schedule = read_yaml(os.path.join(ROOT, "data", "schedule.yml"))
    clips = read_yaml(os.path.join(ROOT, "data", "clips.yml"))

    # ICS
    ics_text = gen_ics(schedule)
    with open(os.path.join(OUT, "schedule.ics"), "w", encoding="utf-8") as f:
        f.write(ics_text)

    # RSS
    with open(os.path.join(OUT, "schedule.rss"), "w", encoding="utf-8") as f:
        f.write(gen_rss(schedule, "StreamHub 일정", "/schedule/"))
    with open(os.path.join(OUT, "clips.rss"), "w", encoding="utf-8") as f:
        f.write(gen_rss(clips, "StreamHub 클립", "/clips/"))

    # Search Index
    pages = load_pages()
    write_json(os.path.join(OUT, "search-index.json"), pages)

    # Auto-clips placeholder
    write_json(os.path.join(OUT, "clips-auto.json"), [])

if __name__ == "__main__":
    main()
