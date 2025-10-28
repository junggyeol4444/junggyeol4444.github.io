---
layout: default
title: 클립
permalink: /clips/
---

<h1>클립</h1>

<ul class="card-list">
{% assign items = site.data.clips %}
{% if items and items.size > 0 %}
  {% for v in items %}
    <li class="card">
      <h3>{{ v.title }}</h3>
      {% if v.platform == 'youtube' and v.video_id %}
        <div class="embed">
          <iframe width="560" height="315" src="https://www.youtube.com/embed/{{ v.video_id }}" title="{{ v.title }}" loading="lazy" frameborder="0" allowfullscreen></iframe>
        </div>
      {% elsif v.url %}
        <p><a href="{{ v.url }}" rel="noopener">보기</a></p>
      {% endif %}
      {% if v.tags %}<p class="tags">{% for t in v.tags %}<span class="tag">{{ t }}</span>{% endfor %}</p>{% endif %}
    </li>
  {% endfor %}
{% else %}
{% endif %}
</ul>
<p class="muted">자동 수집: Actions가 YouTube 채널 RSS를 선택적으로 병합하여 <code>/out/clips-auto.json</code>을 갱신합니다.</p>

<div class="empty-hint">
  <p>아직 등록된 항목이 없거나 데이터 파일이 비어 있습니다.</p>
  <p>PR로 <code>/data</code> 또는 <code>/content</code>를 업데이트하면 자동 반영됩니다.</p>
</div>

{% include giscus.html %}
