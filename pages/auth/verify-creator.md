
---
layout: default
title: 방송인증 신청
permalink: /auth/verify-creator/
---

<h1>방송인증 신청</h1>
<p>아래 버튼을 누르면 GitHub 이슈 폼으로 이동합니다. 로그인 중인 계정의 기본 정보가 자동 채워집니다.</p>

<a class="btn primary" id="open-issue">이슈 열기</a>
<p class="badge" style="margin-top:8px">운영자가 이슈에 <code>creator:verified</code> 라벨을 달면 스트리머 페이지가 자동 생성됩니다.</p>

<script src="/assets/js/auth.config.js"></script>
<script type="module">
  import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm";
  const cfg = (window.AUTH_CONFIG || {});
  const supabase = createClient(cfg.supabaseUrl || "", cfg.supabaseAnonKey || "");
  document.getElementById("open-issue").addEventListener("click", async () => {
    const { data: { user } } = await supabase.auth.getUser();
    const dn = (user?.user_metadata?.display_name || "").trim();
    const em = (user?.email || "").trim();
    const title = encodeURIComponent(`[방송인증] ${dn || "이름"}`);
    const body = encodeURIComponent([
      "### 표시 이름 (Display Name)",
      dn || "",
      "",
      "### 주요 플랫폼",
      "",
      "",
      "### 채널 URL",
      "",
      "",
      "### 채널 ID (선택)",
      "",
      "",
      "### 한 줄 소개 (선택)",
      "",
      "",
      "### 아바타/프로필 이미지 URL (선택)",
      "",
      "",
      "---",
      `신청자 이메일: ${em}`
    ].join("\n"));
    // Update the repo path below to your repo "owner/name"
    const repo = (window.AUTH_CONFIG && window.AUTH_CONFIG.githubRepo) || "OWNER/REPO";
    const url = `https://github.com/${repo}/issues/new?template=creator-verification.yml&title=${title}&body=${body}`;
    window.open(url, "_blank");
  });
</script>
