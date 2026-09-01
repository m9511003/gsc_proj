# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

- 엑셀(xlsx)·CSV 데이터를 취합하는 모듈
- 취합된 데이터를 분석하는 모듈

현재 저장소는 초기 단계로, `app.py`, `hello.py`에 pandas/numpy 사용 예제 코드만 존재하며
데이터 취합·분석 모듈은 아직 구현되어 있지 않다. `requirements.txt` 등 의존성 관리 파일도 없으므로
pandas, numpy, openpyxl(xlsx 읽기용) 등은 신규 코드 작성 시 직접 설치해야 한다.

## 프로젝트 데이터

- `data` 디렉토리에 원본 xlsx/csv 데이터가 위치할 예정이다(현재 저장소에는 아직 생성되어 있지 않음).
- 새 작업을 시작하기 전, `data` 디렉토리가 존재하면 그 안의 파일 목록과 스키마(컬럼명, 시트 구성)를
  먼저 확인한 뒤 취합/분석 로직을 작성한다.

## 개발 환경

- Python 3.11
- 빌드/린트/테스트 설정(예: pytest, flake8 등)이 아직 구성되어 있지 않다. 관련 도구를 추가할 경우
  이 파일에 실행 명령을 함께 기록한다.
