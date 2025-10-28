
# 브랜딩 & 가드 패치
- 푸터를 `_includes/footer.html`로 분리. `_config.yml`에서 아래처럼 바꾸면 즉시 반영됩니다.
  ```yaml
  footer_text: '방게더 — 모두의 방송 커뮤니티'
  footer_links:
    - { text: '약관', url: '/terms/' }
    - { text: '개인정보', url: '/privacy/' }
  ```
- 전역 푸터의 'Powered by Jekyll · Custom TGD-like theme' 문구 제거.
- CI에 **프론트매터 검사** 추가: `pages/`/`creators/`의 `.md`에 맨 윗줄 `---` 없으면 실패 → 'layout: ...' 같은 원치 않는 텍스트 노출 예방.

## 참고
- GitHub Pages 프로젝트 사이트라면 `_config.yml`에 `url:` `baseurl:`을 반드시 맞춰주세요.
  ```yaml
  url: "https://USERNAME.github.io"
  baseurl: "/REPO"   # 사용자/오거나이제이션 사이트는 '' (빈 값)
  ```
