
# Patch 내용

이 패치는 다음을 수행합니다(예시/샘플 데이터는 추가하지 않음).

1. **인증 버튼 비활성화(기본값)**  
   - `_config.yml`에 `auth.enable: false`를 추가합니다.
   - `_includes/header.html`, `_layouts/default.html`에서 로그인/회원가입 버튼을 `site.auth.enable`이 `true`일 때만 노출하도록 변경합니다.
   - Supabase 값을 설정하고 `auth.enable: true`로 바꾸면 버튼이 나타납니다.

2. **내비게이션 대상 경로에 빈 페이지 생성**  
   - `schedule/`, `creators/`, `clips/`, `tutorials/`, `community/`, `gear/`, `awards/`, `trends/`, `editorial/`, `contribute/`, `about/` 각각에 `index.md`를 추가하여 404를 방지합니다.
   - 각 파일에는 **프론트매터만** 포함되어 있으며, 본문 컨텐츠는 없습니다.

3. **404/robots 추가**  
   - `404.html`을 추가하여 존재하지 않는 경로에서 사용자 경험을 개선합니다.
   - `robots.txt`를 추가하고, `jekyll-sitemap` 플러그인이 생성하는 `sitemap.xml`을 참조합니다.

## 배포 메모

- GitHub Pages **사용자 사이트**(`username.github.io`)라면 `_config.yml`에서:
  ```yml
  url: "https://<username>.github.io"
  baseurl: ""
  ```
- **프로젝트 사이트**(`username.github.io/<repo>`)라면:
  ```yml
  url: "https://<username>.github.io"
  baseurl: "/<repo>"
  ```

- `scripts/generate.py`는 `out/` (검색 인덱스, RSS, ICS)를 생성합니다. 저장소에서 자동 실행되지 않으므로,
  - 로컬에서 실행 후 `out/` 폴더를 **커밋**하거나,
  - GitHub Actions로 스크립트를 실행/커밋하도록 구성하세요.
  - 샘플 데이터는 이 패치에 포함하지 않았습니다.
