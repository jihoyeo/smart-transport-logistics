# 강의계획서 — 스마트 교통물류

> 2026학년도 2학기 · 가천대학교 스마트시티학과 · 학부 3학년 · 12주 과정

## 1. 교과목 개요

- 도시 모빌리티 시뮬레이션의 기초 이론과 구현 방법 학습
- 도로망·대중교통·통행 수요 데이터의 전처리 및 분석
- 최단경로 탐색, 대중교통 경로 탐색, 차량 배차, 시뮬레이션 결과 분석 실습
- 가천대학교 교내셔틀 ‘무당이’를 대상으로 한 현황 재현 및 개선안 평가
- 데이터 분석, 최적화, 머신러닝 기법을 시뮬레이션 구성 절차에 맞추어 적용

## 2. 학습 목표

- OpenStreetMap 도로망과 GTFS 대중교통 시간표의 구조 이해 및 분석 데이터 구축
- 최단경로 알고리즘(다익스트라, A\*)과 대중교통 경로 탐색 알고리즘(RAPTOR) 구현
- 구현 결과와 참조 엔진의 비교를 통한 정확도 검증
- 통행 수요 생성 및 승객–차량 배차 알고리즘 비교
- 이산시간 시뮬레이션 루프 구성
- 서비스율, 대기시간, 차량 가동률 등 주요 성과지표 해석
- 실제 대상지의 운영 개선 시나리오 설계 및 효과 분석

### 구현 범위

- 직접 구현
  - 최단경로 탐색: 3주차
  - 대중교통 경로 탐색: 5주차
  - 이산시간 시뮬레이션 루프: 11주차
  - 관련 라이브러리의 알고리즘 구현 기능은 사용하지 않음
- 제공 코드 활용
  - 데이터 전처리, 수요 생성, 지표 산출 등
  - 제공 코드의 구조 확인 및 매개변수 변경 실습
- 외부 엔진 활용
  - 계산량이 큰 작업은 DTUMOS 엔진에 HTTP 요청
  - 엔진 내부 구현 언어인 Rust는 본 교과목의 학습 범위에서 제외

## 3. 운영 정보

| 항목 | 내용 |
|---|---|
| 담당 교수 | 여지호 |
| 연락처 | jihoyeo@gachon.ac.kr |
| 조교 | 정은주 · jeunjoo1211@gachon.ac.kr |
| 강의 시간 | 화 13:00–14:50 / 수 15:00–16:50 |
| 강의실 | AI공학관 210호 |
| 수업 방식 | 대면수업 원칙(보강 시 비대면 수업 활용 가능) |
| 오피스 아워 | 수 17:00–20:00 |
| 운영 기간 | 12주(2026-09-01~2026-11-17) |
| 미팅 링크 | https://gachon.webex.com/meet/jihoyeo |
| 소통 채널 | 카카오톡 단체대화방, 이메일 |

### 선수 지식

- Python 기초 문법
- `pandas` 및 지도 데이터 처리: 2주차 수업에서 필요한 범위 학습

### 실습 환경

- Python 3.11
- 교재 저장소 복제 후 `pip install -r requirements.txt` 실행
- 강의용 공용 시뮬레이션 서버 사용
- 서버 접속이 어려운 경우 교재에 포함된 실행 결과 활용(복습용 별도 엔진 설치 불필요)
- 엔진 내부 확인 실습: 개인 노트북의 Docker 및 사전 빌드 이미지 사용

## 4. 주차별 계획

- 세부 일정: [schedule.md](schedule.md)

### 강의 녹화

수업 녹화본입니다. 링크를 열고 암호를 입력합니다. 매주 수업 후 여기에 추가합니다.

| 날짜 | 주차 | 내용 | 녹화 | 암호 |
|---|---|---|---|---|
| 09-08 (화) | 2주차 | 교재 2장 도로망 데이터 | [Zoom](https://us06web.zoom.us/rec/share/HuLU0NCeTqcm1-h1ixv4VEPXjBjdxUflpCUTxksbt8hz4uIHa6MzvedTmepbFq4.G5TXkrBMCprPvARv) | `GJ1PfSd=` |
| 09-09 (수) | 2주차 | 교재 2장 도로망 실습 | [Zoom](https://us06web.zoom.us/rec/share/KNFq2G26hg-jyKWYHpDIFEqOonGKHyYDD0pFosnDy20OcVdyYSztsM91sZ5YJ_t-.ecEAi0UxzagXTYQW) | `yi*5^0bi` |
| 09-15 (화) | 3주차 | 교재 3장 최단경로 알고리즘 | [Zoom](https://us06web.zoom.us/rec/share/QUY7KkYEjJOksbgxbsRETs4pw9toyWVviVUMwv9fG0fWD9XRiICKPy_M1zSM5Tqm.svGfISzNolq9xTzr) | `m78#MjSt` |
| 09-22 (화) | 4주차 | 교재 4장 시간대별 속도 | [Zoom](https://us06web.zoom.us/rec/share/IGsEw1OD5-ONfh6FEvaXwjB-k86iK4yoELoJWnOt-bp6IFGn_YtSDo3oLHsMdW5U.JbqY1-5iccCowngf) | `^r&%F0*M` |
| 09-23 (수) | 4주차 | 교재 5장 GTFS | [Zoom](https://us06web.zoom.us/rec/share/9Xrv8N2PqHAn_o1QhTdSr4bEwhpUEk00oZ89d2WYVFTd-oXtU1Di_3ekrQ1CVubD.wfh9LgBpw6cVvn2o) | `bRG6+?5W` |

## 5. 평가

| 항목 | 비중 | 비고 |
|---|---|---|
| 중간시험 | 30% | 2026-10-27(화) |
| 기말 개인 프로젝트 | 40% | take-home 시험 · 가천대학교 교내셔틀 무당이 시뮬레이션 및 개선 분석 보고서 |
| 과제 및 참여도 | 20% | HW1~HW3 |
| 출결 | 10% | 결석 1점/회 감점(1회까지 미차감), 지각 0.5점/회 감점(2회까지 미차감) |

- 성적비율
  - A: 30%
  - B: 40%
  - C: 30%

### 중간시험(10-27)

- 시험 범위: 교재 0~8장, 12장
- 단답형: 40%, 폐쇄형 시험(자료 및 요약지 사용 불가)
- 코딩테스트: 60%, 개방형 시험
  - 사이버캠퍼스를 통한 문제 출제
  - 제공된 `ipynb` 파일과 데이터 사용
  - LLM 사용 가능
- 평가 내용: 개념 이해, 데이터 처리 과정, 코드 실행 결과의 해석

### 기말 개인 프로젝트

- 주제: 가천대학교 교내셔틀 무당이 시뮬레이션 및 개선 분석
- 운영 방식: take-home 시험. 학생 개인별로 수행하고 보고서를 제출하며, 발표는 하지 않음
- 수행 기간: 6~12주차
- 주요 과업
  - 무당이 시간표의 GTFS 변환
  - 정류장별·시간대별 승하차 조사
  - 현황 시뮬레이션 재현
  - 개선 시나리오 1개 분석
- 개선 시나리오 예시
  - 배차간격 조정
  - 노선 변경
  - 차량 대수 또는 정원 변경
  - DRT 전환
  - 시간대별 차등 운행
- 평가 기준: 100점
  - 데이터 준비: 20점
  - 경로 탐색 정확도: 20점
  - 시나리오 설계: 20점
  - 지표 해석: 25점
  - 보고서 완성도 및 재현성: 15점
- 세부 요건 및 산출물 일정: [schedule.md](schedule.md)
- 명세와 양식: [assignments/project.md](assignments/project.md), `assignments/project/`

### 과제

| 과제 | 마감 | 내용 |
|---|---|---|
| HW1 | 4주차 | 교재 2장 도로망 통계와 3장 다익스트라 구현 |
| HW2 | 6주차 | 직접 구현한 RAPTOR와 참조 결과 비교 및 차이 분석 |
| HW3 | 9주차 | 무당이 GTFS 작성·검증 및 승하차 조사표(개인 제출, 8주차 휴강 대체) |

## 6. 교재 및 참고문헌

### 주교재

- [Urban Mobility Simulation — Digital Twin for Urban Mobility Systems](https://jihoyeo.github.io/mobility-simulation-book/)
- 학기 중 수시 개정, 최신 자료는 웹 교재 기준
- 실습 코드: [교재 저장소](https://github.com/jihoyeo/mobility-simulation-book)

### 부교재

- [핸즈온 머신러닝 3판](https://www.hanbit.co.kr/store/books/look.php?p_code=B1539397165): 10주차 ETA 예측 모델의 이론적 배경
- [Google OR-Tools](https://developers.google.com/optimization?hl=ko): 10주차 배차 및 물류 최적화 실습

### 참고문헌

- Boeing (2017), *OSMnx: New Methods for Acquiring, Constructing, Analyzing, and Visualizing Complex Street Networks*: 2주차
- Delling, Pajor & Werneck (2015), *Round-Based Public Transit Routing*, Transportation Science: 5~6주차
- Kuhn (1955), *The Hungarian Method for the Assignment Problem*: 10주차
- Alonso-Mora et al. (2017), *On-demand High-capacity Ride-sharing via Dynamic Trip-vehicle Assignment*, PNAS: 10~11주차
- Lopez et al. (2018), *Microscopic Traffic Simulation using SUMO*, IEEE ITSC: 1주차

## 7. 수업 운영 정책

- 수업 구성
  - 화요일: 주요 개념 및 예제 코드. 교재 웹을 화면에 띄우고 절 순서대로 실행
  - 수요일: 구현 실습. 실습 노트북과 채점 파일의 빈칸을 채움
  - 별도 슬라이드 없이 교재 웹과 실습 노트북으로 진행. 운영 안내는 사이버캠퍼스 공지
  - 매 수업 노트북 지참
- LLM 활용
  - ChatGPT, Claude, Gemini 등 사용 가능
  - 원활한 실습을 위해 LLM 서비스 구독 권장
  - 생성 코드의 동작 원리와 오류 원인 설명 필요
  - 중간시험 코딩테스트에서도 사용 가능
- 구현 결과 검증
  - 다익스트라 결과와 NetworkX 결과 비교
  - RAPTOR 결과와 참조 엔진 결과 비교
  - 코드 실행 여부뿐 아니라 결과의 정확성 평가
- 8주차 휴강
  - 일정: 10-20~10-21
  - 사유: 강릉세계총회 참석
  - 온라인 과제로 대체
  - 필요 시 보강기간(11-24~11-25) 활용

## 8. 상담 계획

- 상담 횟수: 학기 중 학생 1인당 1회
- 상담 시간: 화·수 수업 직후
- 상담이 어려운 날짜와 시간은 상담 일정 시트에 기재
<!-- 2026-2 상담일정 시트 링크 -->

## 9. 종강 이후 — P-실무프로젝트

- 기간: 11-24~12-11, 평일 10:00–12:00
- 장소: AI공학관 210호
- 최종발표: 12-11(금)
- 주제: 실제 지자체(내가 사는 동네 권장) 또는 광역교통 대상 대중교통 네트워크 분석과 노선 개편안 제시
- 수행 내용: 정규 수업 및 기말 개인 프로젝트에서 구축한 분석 절차를 새로운 지역에 적용
- 세부 주제 및 제약 조건: [schedule.md](schedule.md)
- 저장소: [p-practical-project](https://github.com/jihoyeo/p-practical-project)
