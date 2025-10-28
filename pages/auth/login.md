
---
layout: default
title: 로그인
permalink: /auth/login/
---

<div id="auth-area"></div>

<h1>로그인</h1>
<form id="login-form" class="tgd-card" onsubmit="return false">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
    <div>
      <label>이메일</label>
      <input class="input" type="email" name="email" required>
    </div>
    <div>
      <label>비밀번호</label>
      <input class="input" type="password" name="password" required>
    </div>
  </div>
  <div style="display:flex;gap:10px;margin-top:12px">
    <button class="btn primary" type="submit">로그인</button>
    <a class="btn" href="/auth/signup/">회원가입</a>
  </div>
</form>

<div class="tgd-card" style="margin-top:12px">
  <div style="display:flex;gap:10px;flex-wrap:wrap">
    <button class="btn" data-oauth="google">Google(YouTube)로 로그인</button>
    <button class="btn" data-oauth="twitch">Twitch로 로그인</button>
  </div>
  <p style="color:var(--tgd-muted);font-size:13px;margin-top:8px">
    치지직/SoopTV는 로그인 후 <a href="/auth/link-platform/">플랫폼 ID 연결</a>로 등록하세요.
  </p>
</div>
<script src="/assets/js/auth.config.js"></script>
<script type="module" src="/assets/js/auth.js"></script>
