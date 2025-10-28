
---
layout: default
title: 플랫폼 ID 연결
permalink: /auth/link-platform/
---

<div id="auth-area"></div>

<h1>플랫폼 ID 연결</h1>
<p class="badge">치지직/SoopTV 등 OAuth가 없는 플랫폼은 ID/URL 등록 후 운영자 확인으로 인증됩니다.</p>

<form id="link-platform-form" class="tgd-card" onsubmit="return false">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
    <div>
      <label>플랫폼</label>
      <select class="input" name="platform" required>
        <option value="youtube">YouTube</option>
        <option value="twitch">Twitch</option>
        <option value="chzzk">치지직(Chzzk)</option>
        <option value="sooptv">SoopTV</option>
      </select>
    </div>
    <div>
      <label>플랫폼 ID (핸들/채널ID)</label>
      <input class="input" name="external_id" placeholder="@example 또는 UCxxxx" required>
    </div>
  </div>
  <div style="margin-top:10px">
    <label>채널 URL (선택)</label>
    <input class="input" name="url" placeholder="https://...">
  </div>
  <div style="display:flex;gap:10px;margin-top:12px">
    <button class="btn primary" type="submit">등록</button>
    <a class="btn" href="/auth/account/">돌아가기</a>
  </div>
</form>

<script src="/assets/js/auth.config.js"></script>
<script type="module" src="/assets/js/auth.js"></script>
