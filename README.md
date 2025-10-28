
# StreamHub — GitHub Pages 정적 사이트

> 정적 우선(Static-first) · Zero-secret · Data-as-content · GitHub Actions 배포

이 저장소는 요청하신 아키텍처(초기+보류 전체 구현의 기반)를 **무비밀** 경로로 운영 가능하게 구성했습니다.
샘플 데이터는 포함하지 않았고, 비어 있어도 에러 없이 동작하도록 처리했습니다.

## 빠른 시작

1. 이 저장소 내용을 GitHub에 업로드(또는 새 private/public 저장소로 push).
2. GitHub → **Settings → Pages** 에서 **Build and deployment = GitHub Actions**로 설정.
3. 저장소의 **Actions** 탭에서 `Build & Deploy (Jekyll)` 워크플로가 통과되면 페이지가 배포됩니다.
4. 데이터는 `/data/*.yml|json` 과 `/content/**`(마크다운)로 관리합니다. PR만으로 반영되며, 스키마 검증/빌드가 자동 수행됩니다.

### (선택) giscus(댓글) 설정
- `_config.yml` 의 `giscus` 섹션에 자신의 리포/카테고리 정보를 입력하면 댓글 영역이 자동 활성화됩니다.
- 비워두면 댓글 영역은 표시되지 않습니다.

### 광고 칸
- **우측 스티키 광고 칸**과 **푸터 광고 칸**이 기본 포함되어 있습니다. 현재는 단순 플레이스홀더입니다.
- 후에 Ads 스크립트를 붙이고자 할 경우 `_includes/ads/right.html`, `_includes/ads/footer.html` 안쪽만 수정하면 됩니다.

## 디렉터리 구조

```
/index.md
/pages/*.md
/_layouts/*.html
/_includes/*.html
/assets/css/main.css
/assets/js/elasticlunr.min.js
/assets/js/search.js
/data/*.yml|json
/content/**
/out/                 # Actions 산출물 (ICS/RSS/검색 인덱스 등)
.github/workflows/*.yml
/scripts/*.py
/schemas/*.json
```

## 개발/배포

- **PR 워크플로우**: 모든 콘텐츠 추가/수정은 PR로만. `scripts/validate.py`에서 스키마 검증이 수행됩니다.
- **정적 산출물**: `scripts/generate.py`가 `out/`에 `schedule.ics`, `schedule.rss`, `clips.rss`, `search-index.json` 등을 생성합니다.
- **나이틀리(Nightly)**: 매일 09:00 KST(= 00:00 UTC)에 집계/수집 잡이 실행됩니다.

## 라이선스
- 코드: MIT (`LICENSE-MIT`). 문서/콘텐츠는 기본적으로 **CC-BY 4.0**(`LICENSE-CC-BY-4.0`)을 권장합니다.
