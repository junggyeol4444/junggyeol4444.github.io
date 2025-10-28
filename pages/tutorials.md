---
layout: default
title: 튜토리얼
permalink: /tutorials/
---

<h1>튜토리얼</h1>

<ul class="card-list">
{% assign items = site.tutorials %}
{% if items and items.size > 0 %}
  {% for p in items %}
    <li class="card">
      <h3><a href="{{ p.url | relative_url }}">{{ p.title }}</a></h3>
      {% if p.tags %}<p class="tags">{% for t in p.tags %}<span class="tag">{{ t }}</span>{% endfor %}</p>{% endif %}
      <p class="muted">{{ p.date | date: "%Y-%m-%d" }}</p>
    </li>
  {% endfor %}
{% else %}
{% endif %}
</ul>

<div class="empty-hint">
  <p>아직 등록된 항목이 없거나 데이터 파일이 비어 있습니다.</p>
  <p>PR로 <code>/data</code> 또는 <code>/content</code>를 업데이트하면 자동 반영됩니다.</p>
</div>

{% include giscus.html %}
