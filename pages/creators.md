---
layout: default
title: 신규 크리에이터
permalink: /creators/
---

<h1>신규 크리에이터</h1>

<ul class="card-list">
{% assign items = site.data.creators %}
{% if items and items.size > 0 %}
  {% for c in items %}
    <li class="card">
      <h3>{{ c.name }}</h3>
      <p class="muted">{{ c.one_liner }}</p>
      {% if c.channel_url %}<p><a href="{{ c.channel_url }}" rel="noopener">채널</a></p>{% endif %}
      {% if c.tags %}<p class="tags">{% for t in c.tags %}<span class="tag">{{ t }}</span>{% endfor %}</p>{% endif %}
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
