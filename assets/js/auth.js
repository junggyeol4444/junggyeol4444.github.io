
import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm";

const cfg = (window.AUTH_CONFIG || {});
if (!cfg.supabaseUrl || !cfg.supabaseAnonKey) {
  console.warn("[auth] Missing AUTH_CONFIG. Edit assets/js/auth.config.js");
}
export const supabase = createClient(cfg.supabaseUrl || "https://example.invalid", cfg.supabaseAnonKey || "anon");

function qs(sel){ return document.querySelector(sel); }
function qsa(sel){ return Array.from(document.querySelectorAll(sel)); }

async function refreshUI() {
  const { data: { user } } = await supabase.auth.getUser();
  const area = qs("#auth-area");
  const top = qs(".tgd-top-actions");
  if (area) {
    area.innerHTML = user ? `
      <div class="badge">로그인됨: ${user.email || user.user_metadata?.name || user.id.slice(0,8)}</div>
      <div style="display:flex;gap:8px;margin-top:10px">
        <a class="btn" href="/auth/account/">마이페이지</a>
        <button id="logout-btn" class="btn">로그아웃</button>
      </div>
    ` : `
      <div style="display:flex;gap:8px;flex-wrap:wrap">
        <a class="btn primary" href="/auth/signup/">회원가입</a>
        <a class="btn" href="/auth/login/">로그인</a>
      </div>
    `;
  }
  if (top && !qs("#top-auth-links")) {
    const wrap = document.createElement("span");
    wrap.id = "top-auth-links";
    wrap.style.marginLeft = "8px";
    wrap.innerHTML = user ? `<a class="btn" href="/auth/account/">마이페이지</a>` : `<a class="btn" href="/auth/login/">로그인</a>`;
    top.appendChild(wrap);
  } else if (top) {
    qs("#top-auth-links").innerHTML = user ? `<a class="btn" href="/auth/account/">마이페이지</a>` : `<a class="btn" href="/auth/login/">로그인</a>`;
  }

  const logout = qs("#logout-btn");
  if (logout) logout.addEventListener("click", async () => {
    await supabase.auth.signOut(); location.href = "/";
  });
}

async function handleSignup() {
  const form = qs("#signup-form"); if (!form) return;
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const email = form.email.value.trim();
    const password = form.password.value;
    const display_name = form.display_name.value.trim();
    const { data, error } = await supabase.auth.signUp({ email, password, options: { data: { display_name } } });
    if (error) return alert(error.message);
    alert("회원가입 완료! 이메일 확인 후 로그인하세요.");
    location.href = "/auth/login/";
  });
  qsa("[data-oauth]").forEach(btn => btn.addEventListener("click", async () => {
    const provider = btn.getAttribute("data-oauth");
    await supabase.auth.signInWithOAuth({ provider, options: { redirectTo: location.origin + "/auth/account/" } });
  }));
}

async function handleLogin() {
  const form = qs("#login-form"); if (!form) return;
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const email = form.email.value.trim();
    const password = form.password.value;
    const { error } = await supabase.auth.signInWithPassword({ email, password });
    if (error) return alert(error.message);
    location.href = "/auth/account/";
  });
  qsa("[data-oauth]").forEach(btn => btn.addEventListener("click", async () => {
    const provider = btn.getAttribute("data-oauth");
    await supabase.auth.signInWithOAuth({ provider, options: { redirectTo: location.origin + "/auth/account/" } });
  }));
}

async function handleAccountPage() {
  const box = qs("#account-box"); if (!box) return;
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) { location.href = "/auth/login/"; return; }
  box.querySelector("[data-email]").textContent = user.email || "-";
  box.querySelector("[data-name]").textContent = user.user_metadata?.display_name || user.user_metadata?.name || "";

  // Load linked platforms
  const { data: rows, error } = await supabase.from("platform_accounts").select().eq("user_id", user.id).order("created_at", { ascending: false });
  if (error) console.warn(error);
  const list = qs("#platform-list");
  list.innerHTML = (rows && rows.length) ? rows.map(r => `
    <div class="topic">
      <div>
        <div><b>${r.platform.toUpperCase()}</b> · ${r.external_id || ""}</div>
        <div style="color:var(--tgd-muted);font-size:13px">${r.verified ? "인증됨" : "인증 대기"}</div>
      </div>
      <div>
        ${r.url ? `<a class="btn" href="${r.url}" target="_blank" rel="noopener">채널</a>` : ""}
      </div>
    </div>
  `).join("") : `<p style="color:var(--tgd-muted)">연결된 플랫폼이 없습니다.</p>`;
}

async function handleLinkPlatform() {
  const form = qs("#link-platform-form"); if (!form) return;
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) { location.href = "/auth/login/"; return; }
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const platform = form.platform.value;
    const external_id = form.external_id.value.trim();
    const url = form.url.value.trim();
    if (!platform || !external_id) { alert("플랫폼과 ID를 입력하세요."); return; }
    const { error } = await supabase.from("platform_accounts").insert({ user_id: user.id, platform, external_id, url, verified: false });
    if (error) return alert(error.message);
    alert("등록되었습니다. 운영자 인증 후 창작자 전환이 가능합니다.");
    location.href = "/auth/account/";
  });
}

document.addEventListener("DOMContentLoaded", () => {
  refreshUI();
  handleSignup();
  handleLogin();
  handleAccountPage();
  handleLinkPlatform();
});
