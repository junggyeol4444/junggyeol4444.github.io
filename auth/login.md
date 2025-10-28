---
layout: default
title: 로그인
permalink: /auth/login/
---

<main class="tgd-container">
  <div class="tgd-card">
    <h1>로그인</h1>

    <form id="login-form" style="display:grid;gap:10px;max-width:360px">
      <label>
        이메일
        <input class="input" type="email" name="email" required autocomplete="email" />
      </label>
      <label>
        비밀번호
        <input class="input" type="password" name="password" required autocomplete="current-password" />
      </label>
      <button class="btn primary" type="submit">로그인</button>
    </form>

    <div class="hr"></div>

    <div style="display:flex;gap:10px;flex-wrap:wrap">
      <button class="btn" data-provider="twitch">Twitch로 로그인</button>
      <button class="btn" data-provider="youtube">YouTube로 로그인</button>
    </div>

    <p class="muted" style="margin-top:10px">
      계정이 없으신가요?
      <a href="{{ '/auth/signup/' | relative_url }}">회원가입</a>
    </p>
  </div>
</main>

<script>
  // 데모용: 백엔드 연동 전까지 기본 동작을 막고 안내만 띄워줍니다.
  document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('login-form');
    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        alert('로그인은 추후 인증 연동 후 활성화됩니다.');
      });
    }
    document.querySelectorAll('[data-provider]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        alert((btn.dataset.provider || '소셜') + ' 로그인은 추후 연동 후 이용 가능합니다.');
      });
    });
  });
</script>
