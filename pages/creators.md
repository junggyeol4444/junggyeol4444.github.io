
---
layout: default
title: 스트리머
permalink: /creators/
---
<h1>스트리머</h1>
<ul class="card-list">
{% assign items = site.data.creators %}
{% if items and items.size > 0 %}
  {% for c in items %}
    <li class="card">
      <h3><a href="{{ '/creators/' | append: c.id | append: '/' | relative_url }}">{{ c.name }}</a></h3>
      <p class="muted">{{ c.one_liner }}</p>
      {% if c.tags %}<p class="tags">{% for t in c.tags %}<span class="tag">{{ t }}</span>{% endfor %}</p>{% endif %}
    </li>
  {% endfor %}
{% else %}
  <li class="card"><p class="muted">등록된 스트리머가 없습니다.</p></li>
{% endif %}
</ul>
