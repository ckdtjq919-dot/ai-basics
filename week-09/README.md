# 인공지능기초 9주차: 도서 데이터 임베딩 구축

OpenAI 임베딩 모델을 활용하여 도서 메타데이터를 벡터 임베딩으로 변환하고 저장/검색하는 실습 프로젝트입니다.

## 구성
- `embeddingbooks.py`: 도서 데이터 벡터 임베딩 생성 및 저장 스크립트
- `embeddings.json`: 생성된 도서 벡터 임베딩 데이터셋
- `docs/Week09_Report.pdf`: 9주차 실습 보고서
- `.env.example`: 환경변수 설정 파일

## 실행 방법
1. 패키지 설치
   ```bash
   pip install openai python-dotenv
   ```
2. 환경변수 설정
   `.env.example`을 참고하여 `.env`에 OpenAI API Key를 입력합니다.
3. 실행
   ```bash
   python embeddingbooks.py
   ```
