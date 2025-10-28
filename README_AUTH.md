
# 회원가입/로그인 추가 (Supabase 기반)

- 이메일/비밀번호, Google(YouTube) OAuth, Twitch OAuth
- 치지직/SoopTV는 **플랫폼 ID 연결**로 등록(운영자 확인 필요)
- 생성된 계정은 GitHub 이슈 기반 **방송인증**과 연동하여 스트리머 페이지 자동 생성 흐름을 유지

## 설정
1. Supabase 프로젝트 생성 → Project URL / anon key 획득
2. `supabase/schema.sql` 을 SQL Editor에서 실행
3. `assets/js/auth.config.js` 편집
   ```js
   window.AUTH_CONFIG = {
     supabaseUrl: "https://YOUR-PROJECT.supabase.co",
     supabaseAnonKey: "YOUR-ANON-KEY",
     githubRepo: "OWNER/REPO" // 방송인증 이슈를 열 저장소
   };
   ```
4. (선택) Supabase Authentication → Providers에서 **Google** 과 **Twitch** 활성화
   - Google은 OAuth 동의 화면 설정 필요
   - Twitch는 Client ID/Secret 등록 필요
5. GitHub Pages는 정적 호스팅만 하므로, 동적 기능은 Supabase가 담당합니다.

## 사용 흐름
- 회원가입/로그인: `/auth/signup/`, `/auth/login/`
- 마이페이지: `/auth/account/` (연결된 플랫폼 표시, 로그아웃)
- 플랫폼 연결: `/auth/link-platform/` (치지직/SoopTV 등 ID 등록)
- 방송인증 신청: `/auth/verify-creator/` → GitHub 이슈 폼으로 이동
- 운영자가 `creator:verified` 라벨을 달면 기존 워크플로가 스트리머 페이지를 생성합니다.
