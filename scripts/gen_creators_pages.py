
import os, yaml, re

ROOT = os.path.dirname(os.path.dirname(__file__))
DATA = os.path.join(ROOT, "data")
OUTDIR = os.path.join(ROOT, "pages", "creators")
os.makedirs(OUTDIR, exist_ok=True)

def load_yaml(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []

def slugify(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9_-]+','-', s)
    return s.strip('-')

def main():
    creators = load_yaml(os.path.join(DATA,"creators.yml"))
    for c in creators:
        cid = c.get("id") or slugify(c.get("name","creator"))
        name = c.get("name","")
        p = os.path.join(OUTDIR, f"{cid}.md")
        body = f'''---
layout: default
title: {name}
permalink: /creators/{cid}/
id: {cid}
---

<h1>{name}</h1>
{{% assign items = site.data.schedule | where: 'creator_id', page.id %}}
{{% if items and items.size > 0 %}}
  <h2>방송 일정</h2>
  <ul class="card-list">
  {{% for e in items %}}
    <li class="card">
      <h3>{{{{ e.title }}}}</h3>
      <p class="muted">{{{{ e.date_start }}}}{{% if e.date_end %}}–{{{{ e.date_end }}}}{{% endif %}} · {{{{ e.platform }}}}</p>
      {{% if e.url %}}<p><a href="{{{{ e.url }}}}" rel="noopener">바로가기</a></p>{{% endif %}}
      {{% if e.tags %}}<p class="tags">{{% for t in e.tags %}}<span class="tag">{{{{ t }}}}</span>{{% endfor %}}</p>{{% endif %}}
    </li>
  {{% endfor %}}
  </ul>
{{% else %}}
  <p class="muted">등록된 일정이 없습니다.</p>
{{% endif %}}
'''
        with open(p,"w",encoding="utf-8") as f:
            f.write(body)

if __name__ == "__main__":
    main()
