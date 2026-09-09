# 스마트 교통물류

가천대학교 스마트시티학과 · 2026학년도 2학기 · 학부 3학년 (12주 과정)

한 학기 동안 도시 모빌리티 시뮬레이터를 직접 만들고, 가천대 교내셔틀 무당이를 시뮬레이션해 개선안을 분석합니다.

| 항목 | 내용 |
|---|---|
| 담당 | 여지호 (jihoyeo@gachon.ac.kr) |
| 강의 시간 | 화 13:00–14:50 / 수 15:00–16:50 |
| 강의실 | AI공학관 210호 |
| 운영 기간 | 12주 (2026-09-01 ~ 2026-11-17) |
| 오피스 아워 | 수 17:00–20:00 |
| 후속 과정 | P-실무프로젝트 — 버스 노선 개선, 자유주제 (11-24 ~ 12-11) |

## 문서

- [강의계획서 (syllabus.md)](syllabus.md)
- [주차별 일정 (schedule.md)](schedule.md)

## 주교재

[Urban Mobility Simulation](https://jihoyeo.github.io/mobility-simulation-book/) · [저장소](https://github.com/jihoyeo/mobility-simulation-book)

학기 중 계속 고쳐집니다. 웹으로 읽는 것이 항상 최신본입니다.

## 학기 흐름

```
1주   환경 준비, 시뮬레이션 개요        ← 첫 시뮬레이션을 실행합니다
2주   도로망 데이터
3주   최단경로 직접 구현                ← 다익스트라 · A*
4주   시간대별 속도, GTFS
5주   RAPTOR 직접 구현                  ← 대중교통 경로 탐색
6주   환승·요금·지표                    ← 기말 프로젝트 착수
7주   통행 수요, 결과 읽기
8주   휴강 (온라인 과제)
9주   중간시험
10주  ETA 예측, 배차·물류 최적화
11주  시뮬레이션 루프 직접 구현
12주  기말 프로젝트 발표
```

## 디렉터리

```
lessons/           주차별 교수자용 진행표 (1~12주차)
assignments/       과제 명세, 기말 프로젝트 명세와 양식
slides/            1~2주차에 쓴 슬라이드 (3주차부터 사용하지 않음)
slides/common/     두 과목 공용 덱 (AI 모빌리티가 계속 사용)
materials/         참고자료, 데이터, 코드
```

## 수업 진행 방식

3주차부터 슬라이드 없이 교재 웹과 실습 노트북을 화면에 띄우고 진행합니다. 화요일은 교재 본문을 절 순서대로 실행하며 설명하고, 수요일은 노트북 빈칸과 채점 파일을 구현합니다. 채점받는 세 장(3·6·11장)은 교재 구현 절을 열기 전에 작은 예제에서 빈칸을 먼저 채웁니다.

교수자용 진행표가 `lessons/weekNN.md`입니다. 교재 범위, 화·수 시간표, 서머리에서 고른 강조점, 막히기 쉬운 지점, 사이버캠퍼스 공지 초안이 들어 있습니다.

| 주차 | 진행표 | 교재 |
|---|---|---|
| 1 | `lessons/week01.md` | 오리엔테이션 · 개발 환경 · 0장 · 1장 (슬라이드로 진행, 기록용) |
| 2 | `lessons/week02.md` | 2장 도로망 (화요일은 슬라이드, 수요일부터 교재) |
| 3 | `lessons/week03.md` | 3장 다익스트라·A* (직접 구현 1) |
| 4 | `lessons/week04.md` | 4장 · 5장 |
| 5 | `lessons/week05.md` | 6장 RAPTOR (직접 구현 2) |
| 6 | `lessons/week06.md` | 7장 · 기말 프로젝트 착수 |
| 7 | `lessons/week07.md` | 8장 · 12장 |
| 8 | `lessons/week08.md` | 휴강 · HW3 |
| 9 | `lessons/week09.md` | 중간시험 · 해설 · 중간 점검 |
| 10 | `lessons/week10.md` | 9장 · 10장 |
| 11 | `lessons/week11.md` | 11장 시뮬레이션 루프 (직접 구현 3) |
| 12 | `lessons/week12.md` | 기말 발표 |

1~2주차 슬라이드는 `slides/00_orientation/`, `slides/week01/`, `slides/week02/`에 그대로 있습니다.

## 과제와 프로젝트

- `assignments/hw1.md` ~ `hw3.md`: 과제 명세
- `assignments/project.md`: 기말 프로젝트 명세 (팀 · 가천대 교내셔틀 무당이)
- `assignments/project/`: 양식 — 승하차 조사표, RAPTOR 대조표, 정류장·노선 GeoJSON 예시, 보고서 골격, 채점표, 동료평가, 시나리오 카드

## 공용 슬라이드

`slides/common/`은 AI 모빌리티 과목과 함께 쓰는 덱입니다. 원본이 이 저장소에 있고, 양쪽 과목이 같은 파일을 씁니다. 교재 장 번호나 과제 번호처럼 한 과목에만 해당하는 내용은 넣지 않습니다.

| 덱 | 분량 | 내용 |
|---|---|---|
| `common/dev_env.md` | 60~75분 | VS Code·파이썬 설치, Claude Code·Codex·Antigravity 설치, 권한 모드, 명령어와 토큰 관리 |

공용 덱의 그림은 `slides/tools/make_figures_common.py`가 만듭니다. 교재 데이터를 쓰지 않으므로 matplotlib만 있으면 실행됩니다.

같은 파일의 사본이 AI 모빌리티 저장소의 `slides/common/`에도 있습니다. 원본을 고치고 pptx를 다시 만든 뒤 아래 명령으로 사본을 맞춥니다.

```bash
python slides/tools/sync_common.py           # 사본을 원본에 맞춰 복사
python slides/tools/sync_common.py --check   # 다른 파일이 있는지만 확인
```

공용 덱을 고칠 때는 문체 검사기를 돌린 뒤 빌드합니다. `.md`가 원본이고 `.pptx`는 빌드 산출물입니다.

```bash
python slides/tools/check_style.py slides/common/dev_env.md
python ~/.claude/skills/md2pptx/scripts/md2pptx.py slides/common/dev_env.md
```

빌더는 `python-pptx`, `Pillow`, `lxml`이 설치된 파이썬에서 돌아갑니다. 빌더가 `경고:`를 출력하면 원고를 고치고 다시 빌드합니다.
