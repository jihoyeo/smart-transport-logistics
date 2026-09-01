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
1주   환경 준비, 시뮬레이션 개요        ← 첫 시뮬레이션을 돌려 봅니다
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
assignments/  과제 명세 및 제출 안내
materials/    참고자료, 데이터, 코드
```

슬라이드는 `.md`가 원본이고 `.pptx`는 빌드 산출물입니다. 고칠 때는 `.md`를 고치고 다시 빌드합니다:

```bash
python3 ~/.claude/skills/md2pptx/scripts/md2pptx.py slides/week01/week01.md
```
