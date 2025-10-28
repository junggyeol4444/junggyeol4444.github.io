
import os, sys, yaml, re, json

ROOT = os.path.dirname(os.path.dirname(__file__))
DATA = os.path.join(ROOT, "data")
CREATORS = os.path.join(DATA, "creators.yml")

def slugify(s):
    s = (s or "").strip().lower()
    s = re.sub(r'[^a-z0-9_-]+','-', s)
    return s.strip('-') or 'creator'

def load_yaml(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []

def dump_yaml(path, data):
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)

def main():
    os.makedirs(DATA, exist_ok=True)
    creators = load_yaml(CREATORS)

    cid = slugify(os.getenv("CREATOR_ID"))
    name = os.getenv("CREATOR_NAME") or cid
    platform = os.getenv("PLATFORM") or ""
    channel_url = os.getenv("CHANNEL_URL") or ""
    one_liner = os.getenv("ONE_LINER") or ""
    tags = [t.strip() for t in (os.getenv("TAGS") or "").split(",") if t.strip()]

    # update or append
    existing = None
    for c in creators:
        if str(c.get("id","")) == cid:
            existing = c
            break
    if existing:
        existing.update({
            "name": name,
            "one_liner": one_liner,
            "channel_url": channel_url,
            "platform": platform,
            "tags": tags
        })
    else:
        creators.append({
            "id": cid,
            "name": name,
            "one_liner": one_liner,
            "channel_url": channel_url,
            "platform": platform,
            "tags": tags
        })

    dump_yaml(CREATORS, creators)

    # Create page content with placeholders (avoid f-string/Jekyll conflict)
    template = \"\"\"---
layout: default
title: __NAME__
permalink: /creators/__CID__/
id: __CID__
---

<h1>__NAME__</h1>
<p class="muted">__ONE_LINER__</p>
<p><a href="__CHANNEL_URL__" rel="noopener">채널 바로가기</a></p>

<h2>방송 일정</h2>
<ul class="card-list">
{% assign items = site.data.schedule | where: 'creator_id', page.id %}
{% if items and items.size > 0 %}
  {% for e in items %}
    <li class="card">
      <h3>{{ e.title }}</h3>
      <p class="muted">{{ e.date_start }}{% if e.date_end %}-{{ e.date_end }}{% endif %} · {{ e.platform }}</p>
      {% if e.url %}<p><a href="{{ e.url }}" rel="noopener">바로가기</a></p>{% endif %}
      {% if e.tags %}<p class="tags">{% for t in e.tags %}<span class="tag">{{ t }}</span>{% endfor %}</p>{% endif %}
    </li>
  {% endfor %}
{% else %}
  <li class="card"><p class="muted">등록된 일정이 없습니다.</p></li>
{% endif %}
</ul>
\"\"\"
    content = (template
               .replace("__NAME__", name)
               .replace("__CID__", cid)
               .replace("__CHANNEL_URL__", channel_url)
               .replace("__ONE_LINER__", one_liner))
    pages_dir = os.path.join(ROOT, "pages", "creators")
    os.makedirs(pages_dir, exist_ok=True)
    page_path = os.path.join(pages_dir, f"{cid}.md")
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(json.dumps({"created": cid, "page": page_path}, ensure_ascii=False))

if __name__ == "__main__":
    main()
