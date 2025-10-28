
import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm";
const cfg = (window.AUTH_CONFIG || {});
let supabase;
try {
  supabase = createClient(cfg.supabaseUrl || "", cfg.supabaseAnonKey || "");
} catch (e) {
  console.warn("Supabase not configured; showing static auth buttons.");
  supabase = null;
}
function qs(s){return document.querySelector(s)}
function qsa(s){return Array.from(document.querySelectorAll(s))}

async function refreshUI(){
  const top = qs(".tgd-top-actions");
  const area = qs("#auth-area");
  const logged = false;
  if (area) area.innerHTML = `<div style="display:flex;gap:8px;flex-wrap:wrap">
    <a class="btn primary" href="/auth/signup/">회원가입</a>
    <a class="btn" href="/auth/login/">로그인</a></div>`;
  if (top) {
    const el = qs("#top-auth-links");
    if (el) el.innerHTML = `<a class="btn" href="/auth/login/">로그인</a> <a class="btn" href="/auth/signup/">회원가입</a>`;
  }
  if (!supabase) return;
  try {
    const { data: { user } } = await supabase.auth.getUser();
    if (user) {
      if (area) area.innerHTML = `<div class="badge">로그인됨: ${user.email || user.id.slice(0,8)}</div>
        <div style="display:flex;gap:8px;margin-top:10px">
          <a class="btn" href="/auth/account/">마이페이지</a>
          <button id="logout-btn" class="btn">로그아웃</button>
        </div>`;
      const el2 = qs("#top-auth-links");
      if (el2) el2.innerHTML = `<a class="btn" href="/auth/account/">마이페이지</a>`;
      const lo = qs("#logout-btn"); if (lo) lo.addEventListener("click", async()=>{ await supabase.auth.signOut(); location.href="/"; });
    }
  } catch(e) { console.warn(e) }
}

document.addEventListener("DOMContentLoaded", refreshUI);
