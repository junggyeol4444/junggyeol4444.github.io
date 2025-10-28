
# 패치 v2 — 일정 탭은 '스트리머 페이지' 안에서만 노출

- 전역 내비/탑바의 **'일정' 링크 제거** → 스트리머 상세 페이지에서만 탭으로 노출됩니다.
- `creator.html`에 **프로필/일정 탭**이 추가되었습니다. 데이터는 `data/schedule.yml` 중 `creator_id`가 페이지의 `creator_id`와 일치하는 항목만 표시합니다.
- 방송 인증 후(라벨 `creator:verified`)에만 **해당 이름(slug)으로 페이지 생성**됩니다. 생성되는 Front Matter에는 `creator_id`, `slug`가 포함됩니다.

## 사용 방법
1. 저장소 루트에 덮어쓰기 커밋
2. 이슈 템플릿으로 신청 → 운영자가 **`creator:verified`** 라벨 부여
3. 워크플로가 `creators/<slug>.md`(레이아웃=creator)와 `data/creators.yml`을 업데이트

## 데이터 연결
- `data/schedule.yml` 예시 키만 참고: `creator_id`, `title`, `date_start`, `date_end`, `platform`, `url` 등
- **샘플 데이터는 포함하지 않았습니다.**
