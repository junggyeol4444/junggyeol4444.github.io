
---
layout: default
title: 방송 일정
permalink: /schedule/
---
<h1>방송 일정</h1>
<ul class="card-list">
{% assign items = site.data.schedule %}
{% if items and items.size > 0 %}
  {% for e in items %}
    <li class="card">
      <h3>
        {% if e.creator_id %}
          <a href="{{ '/creators/' | append: e.creator_id | append: '/' | relative_url }}">{{ e.title }}</a>
        {% else %}
          {{ e.title }}
        {% endif %}
      </h3>
      <p class="muted">{{ e.date_start }}{% if e.date_end %}-{{ e.date_end }}{% endif %} · {{ e.platform }}</p>
      {% if e.url %}<p><a href="{{ e.url }}" rel="noopener">바로가기</a></p>{% endif %}
      {% if e.tags %}<p class="tags">{% for t in e.tags %}<span class="tag">{{ t }}</span>{% endfor %}</p>{% endif %}
    </li>
  {% endfor %}
{% else %}
  <li class="card"><p class="muted">등록된 일정이 없습니다.</p></li>
{% endif %}
</ul>
