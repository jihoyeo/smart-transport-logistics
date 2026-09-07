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
slides/       주차별 강의 슬라이드 — 폴더마다 md 원고 + figures/ + pptx
slides/common/ 두 과목 공용 덱
assignments/  과제 명세 및 제출 안내
materials/    참고자료, 데이터, 코드
```

슬라이드는 개요만 제시하고, 내용과 코드는 교재를 화면에 표시한 상태로 진행합니다. 덱 하나가 교재 한 장을 다루고, 파일 이름은 교재 원고와 같습니다.

| 주차 | 덱 | 교재 |
|---|---|---|
| 1 | `week01/ch01_why.md` · `week01/ch00_setup.md` | 1장 · 0장 |
| 2 | `week02/ch02_road_network.md` | 2장 |
| 3 | `week03/ch03_dijkstra.md` | 3장 |
| 4 | `week04/ch04_speeds_engine.md` · `week04/ch05_gtfs.md` | 4장 · 5장 |
| 5 | `week05/ch06_raptor.md` | 6장 |
| 6 | `week06/ch07_raptor_fare.md` | 7장 |
| 7 | `week07/ch08_demand.md` · `week07/ch12_metrics.md` | 8장 · 12장 |
| 10 | `week10/ch09_eta.md` · `week10/ch10_dispatch.md` | 9장 · 10장 |
| 11 | `week11/ch11_simloop.md` | 11장 |

`slides/common/`은 AI 모빌리티 과목과 함께 쓰는 덱입니다. 원본이 이 저장소에 있고, 양쪽 과목이 같은 파일을 씁니다. 교재 장 번호나 과제 번호처럼 한 과목에만 해당하는 내용은 넣지 않습니다.

| 덱 | 분량 | 내용 |
|---|---|---|
| `common/dev_env.md` | 60~75분 | VS Code·파이썬 설치, Claude Code·Codex·Antigravity 설치, 권한 모드, 명령어와 토큰 관리 |

공용 덱의 그림은 `slides/tools/make_figures_common.py`가 만듭니다. 교재 데이터를 쓰지 않으므로 matplotlib만 있으면 실행됩니다.

그림은 주차별 `slides/tools/make_figures_week*.py`가 교재 데이터로 생성합니다. 교재 저장소의 가상환경에서 실행합니다.

```bash
cd ~/lecture/mobility-simulation-book && .venv/bin/python \
  ~/lecture/smart-transport-logistics/slides/tools/make_figures_week04.py
```

빌드 전에 문체 검사기를 돌립니다.

```bash
python3 slides/tools/check_style.py slides/*/*.md
```

`.md`가 원본이고 `.pptx`는 빌드 산출물입니다. 고칠 때는 `.md`를 고치고 다시 빌드합니다:

```bash
~/miniconda3/bin/python3 ~/.claude/skills/md2pptx/scripts/md2pptx.py slides/week01/ch01_why.md
```

빌더는 `python-pptx`, `Pillow`, `lxml`이 설치된 파이썬에서 돌아갑니다. 시스템 `python3`에는 없으므로 위 경로를 씁니다. 빌더가 `경고:`를 출력하면 원고를 고치고 다시 빌드합니다.
