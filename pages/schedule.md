---
layout: default
title: 일정
permalink: /schedule/
---

<h1>일정</h1>

<ul class="card-list">
{% assign items = site.data.schedule %}
{% if items and items.size > 0 %}
  {% for e in items %}
    <li class="card">
      <h3>{{ e.title }}</h3>
      <p class="muted">{{ e.date_start }}{% if e.date_end %}–{{ e.date_end }}{% endif %} · {{ e.platform }}</p>
      {% if e.url %}<p><a href="{{ e.url }}" rel="noopener">바로가기</a></p>{% endif %}
      {% if e.tags %}<p class="tags">{% for t in e.tags %}<span class="tag">{{ t }}</span>{% endfor %}</p>{% endif %}
    </li>
  {% endfor %}
{% else %}
{% endif %}
</ul>
<p class="muted">캘린더: <a href="{{ '/out/schedule.ics' | relative_url }}">ICS</a> · <a href="{{ '/out/schedule.rss' | relative_url }}">RSS</a></p>

<div class="empty-hint">
  <p>아직 등록된 항목이 없거나 데이터 파일이 비어 있습니다.</p>
  <p>PR로 <code>/data</code> 또는 <code>/content</code>를 업데이트하면 자동 반영됩니다.</p>
</div>

{% include giscus.html %}
