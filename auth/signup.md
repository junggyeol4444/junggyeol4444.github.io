---
layout: default
title: 회원가입
permalink: /auth/signup/
---

<main class="tgd-container">
  <div class="tgd-card">
    <h1>회원가입</h1>

    <form id="signup-form" style="display:grid;gap:10px;max-width:360px">
      <label>
        이메일
        <input class="input" type="email" name="email" required autocomplete="email" />
      </label>
      <label>
        비밀번호
        <input class="input" type="password" name="password" required minlength="8" autocomplete="new-password" />
      </label>
      <label>
        비밀번호 확인
        <input class="input" type="password" name="password2" required minlength="8" autocomplete="new-password" />
      </label>
      <label style="display:flex;gap:8px;align-items:center">
        <input type="checkbox" name="agree" required />
        <span>이용약관 및 개인정보 처리방침에 동의합니다.</span>
      </label>
      <button class="btn primary" type="submit">회원가입</button>
    </form>

    <div class="hr"></div>

    <div style="display:flex;gap:10px;flex-wrap:wrap">
      <button class="btn" data-provider="twitch">Twitch로 가입</button>
      <button class="btn" data-provider="youtube">YouTube로 가입</button>
    </div>

    <p class="muted" style="margin-top:10px">
      이미 계정이 있으신가요?
      <a href="{{ '/auth/login/' | relative_url }}">로그인</a>
    </p>
  </div>
</main>

<script>
  // 데모용: 백엔드 연동 전까지 기본 동작을 막고 안내만 띄웁니다.
  document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('signup-form');
    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const pw = form.password.value;
        const pw2 = form.password2.value;
        if (pw !== pw2) {
          alert('비밀번호가 일치하지 않습니다.');
          return;
        }
        alert('회원가입은 추후 인증 연동 후 활성화됩니다.');
      });
    }
    document.querySelectorAll('[data-provider]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        alert((btn.dataset.provider || '소셜') + ' 회원가입은 추후 연동 후 이용 가능합니다.');
      });
    });
  });
</script>
