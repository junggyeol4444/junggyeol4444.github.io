
---
layout: default
title: 회원가입
permalink: /auth/signup/
---

<div id="auth-area"></div>

<h1>회원가입</h1>
<p class="badge">이메일/비밀번호 또는 플랫폼 계정으로 시작할 수 있습니다.</p>

<form id="signup-form" class="tgd-card" onsubmit="return false">
  <label>표시 이름</label>
  <input class="input" name="display_name" placeholder="예) 홍길동" required>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px">
    <div>
      <label>이메일</label>
      <input class="input" type="email" name="email" required>
    </div>
    <div>
      <label>비밀번호</label>
      <input class="input" type="password" name="password" minlength="6" required>
    </div>
  </div>
  <div style="display:flex;gap:10px;margin-top:12px">
    <button class="btn primary" type="submit">가입하기</button>
    <a class="btn" href="/auth/login/">로그인</a>
  </div>
</form>

<div class="tgd-card" style="margin-top:12px">
  <div style="display:flex;gap:10px;flex-wrap:wrap">
    <button class="btn" data-oauth="google">Google(YouTube)로 계속</button>
    <button class="btn" data-oauth="twitch">Twitch로 계속</button>
  </div>
  <p style="color:var(--tgd-muted);font-size:13px;margin-top:8px">
    치지직/SoopTV는 별도 OAuth가 없어 <a href="/auth/link-platform/">플랫폼 ID 연결</a>로 등록하세요.
  </p>
</div>
<script src="/assets/js/auth.config.js"></script>
<script type="module" src="/assets/js/auth.js"></script>
