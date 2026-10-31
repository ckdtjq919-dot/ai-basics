# 인공지능기초 11주차: RAG (검색 증강 생성) 엔진 구현

문서 임베딩 수집(Ingestion) 및 질의 기반 검색 증강 생성(RAG Engine) 파이프라인을 구현한 프로젝트입니다.

## 구성
- `RAGingestion.py`: 문서 로드, 청킹 및 벡터스토어 색인(Ingestion)
- `RAGengine.py`: 검색 및 LLM 답변 생성 엔진
- `RAGmain.py`: 통합 실행 인터페이스
- `docs/Week11_Report.pdf`: 11주차 실습 보고서

## 실행 방법
1. 패키지 설치
   ```bash
   pip install openai python-dotenv
   ```
2. `.env`에 OpenAI API Key 설정
3. 실행
   ```bash
   python RAGmain.py
   ```
