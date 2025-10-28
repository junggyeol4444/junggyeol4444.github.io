
---
layout: default
title: 마이페이지
permalink: /auth/account/
---

<div id="auth-area"></div>

<h1>마이페이지</h1>
<div id="account-box" class="tgd-card">
  <div><b>이메일:</b> <span data-email>-</span></div>
  <div><b>이름:</b> <span data-name>-</span></div>
  <div style="margin-top:10px;display:flex;gap:10px;flex-wrap:wrap">
    <a class="btn" href="/auth/link-platform/">플랫폼 ID 연결</a>
    <a class="btn" href="/auth/verify-creator/">방송인증 신청</a>
    <button id="logout-btn" class="btn">로그아웃</button>
  </div>
</div>

<h2 style="margin-top:16px">연결된 플랫폼</h2>
<div id="platform-list" class="page-community"></div>

<script src="/assets/js/auth.config.js"></script>
<script type="module" src="/assets/js/auth.js"></script>
