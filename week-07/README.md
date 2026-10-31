# 인공지능기초 7주차: OpenAI API 기본 실습 및 프롬프트 테스트

본 저장소는 인공지능기초 7주차 실습 프로젝트입니다. OpenAI API를 활용하여 기본 모델 호출 및 질의응답을 구현합니다.

## 구성
- `test2.py`: OpenAI API 호출 및 프롬프트 테스트 스크립트
- `docs/Week07_Report.pdf`: 7주차 실습 개인보고서
- `.env.example`: 환경변수 템플릿

## 실행 방법
1. 가상환경 생성 및 활성화
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install openai python-dotenv
   ```
2. `.env` 파일 설정
   `.env.example` 파일을 복사하여 `.env`를 생성하고 본인의 OpenAI API Key를 입력합니다.
   ```bash
   cp .env.example .env
   ```
3. 실행
   ```bash
   python test2.py
   ```
