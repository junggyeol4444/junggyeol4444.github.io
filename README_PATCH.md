
# TGD 스타일 패치 & 자동 스트리머 생성 (GitHub Pages용)

> **샘플 데이터 없음.** 테마/레이아웃/CI만 포함됩니다.

## 적용 방법 (요약)
1. 이 ZIP을 저장소 루트에 풀고 **덮어쓰기** 커밋합니다.
2. GitHub → Settings → Issues → Issue templates 가 보이면 OK.
3. 이슈에서 **'방송인증 신청 (Creator Verification)'** 템플릿으로 등록 → 운영자가 라벨 **creator:verified** 를 달면 자동으로 스트리머 페이지가 생성/커밋됩니다.
4. 사이트 레이아웃은 `_layouts/default.html` 으로 교체됩니다. (메인/서브 페이지 공통 UI, TGD 유사 다크 테마)
5. 필요하면 `_layouts/creator.html` 을 커스터마이즈하세요.

## 주요 파일
- `assets/css/tgd.css` — TGD 유사 스타일 (왼쪽 사이드바, 다크, 카드형)
- `assets/js/tgd.js` — 현재 페이지 활성화, 모바일 토글
- `_layouts/default.html` — 공통 레이아웃 (사이드바/탑바 포함)
- `_layouts/creator.html` — 스트리머 상세 페이지 레이아웃
- `.github/ISSUE_TEMPLATE/creator-verification.yml` — 방송인증 폼
- `.github/workflows/creator-auto-onboard.yml` — 이슈 라벨 `creator:verified` → 자동 생성
- `.github/workflows/build-out.yml` — push 시 Python 산출물(out/) 생성/커밋 (선택)
- `scripts/ci/add_creator_from_issue.py` — 이슈 값으로 `data/creators.yml` 업데이트 & `creators/<slug>.md` 생성 (샘플 데이터 없음)

## 페이지 이동(내비) & CSS 일원화
- `_layouts/default.html` 내부 사이드바 링크는 다음 경로를 가정합니다.
  - `/creators/`, `/schedule/`, `/tutorials/`, `/community/`, `/gear/`, `/awards/`, `/trends/`, `/about/`
- 각 페이지가 존재한다면 자동으로 잘 연결됩니다. 경로가 다르면 해당 페이지의 permalink 를 맞추거나, 사이드바 href 를 수정하세요.
- 모든 페이지는 공통 카드/테이블/버튼 스타일을 사용합니다.

## 방송인증 자동 생성 흐름
1. 신청자가 이슈 템플릿으로 등록
2. 운영자가 검토 후 라벨 **creator:verified**
3. 워크플로우가 실행되어
   - `data/creators.yml`에 항목 추가(중복 체크)
   - `creators/<slug>.md` 생성 (레이아웃=creator, permalink 포함)
   - (선택) `scripts/validate.py` / `scripts/generate.py` 실행
   - 커밋/푸시

> ※ 템플릿/워크플로우는 **샘플 데이터 없이** 메타만 생성합니다.

## 참고
- `_layouts/default.html` 은 Jekyll Minima 기반이 아니라 **독립 레이아웃**입니다. 기존 커스텀 include가 있다면 이 레이아웃에 다시 include 해주세요.
- `site.title`, `site.giscus.*` 등을 `_config.yml` 에 설정하면 자동 반영됩니다.
- CI에서 Python 패키지로 `pyyaml` 만 추가 설치합니다.
