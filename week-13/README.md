---------------------------------

한국어 도서 리뷰 멀티태스크 NLP 애플리케이션

---------------------------------

## 기능
- 감성 분석 (KoELECTRA)

감성 분석 모델 (Sentiment Analysis)
모델: beomi/KcELECTRA-base

Hugging Face Hub
https://huggingface.co/beomi/KcELECTRA-base

한국어 댓글/리뷰 등 비공식 텍스트(노이즈 데이터)에 강한 ELECTRA 기반 모델

NSMC 등 감성 분석 데이터셋에서 높은 성능

라이선스
MIT License
상업적 사용 가능
수정 및 배포 가능
제한 거의 없는 오픈소스 라이선스




- 제로샷 장르 분류 (XLM-RoBERTa)
모델
joeddav/xlm-roberta-large-xnli

Hugging Face Hub
https://huggingface.co/joeddav/xlm-roberta-large-xnli

XLM-RoBERTa 기반 자연어 추론(NLI) 모델
Zero-shot classification에 특화
한국어 포함 다국어 지원

라이선스
XLM-RoBERTa 기반 → MIT License 계열
Hugging Face discussion 기준으로도 MIT로 사용됨
자유로운 연구/교육/상업 사용 가능



- 텍스트 요약 (KoBART)
텍스트 요약 모델 (Summarization)

모델: gogamza/kobart-summarization

Hugging Face Hub
https://huggingface.co/gogamza/kobart-summarization

KoBART 기반 한국어 abstractive summarization 모델
뉴스/리뷰 요약에 최적화
encoder-decoder 구조

라이선스
MIT License
    자유롭게 사용 가능
    학습/파인튜닝 가능
    배포 제한 없음



- 질문 응답 (KLUE-RoBERTa)
추출형 QA 모델 (Question Answering)
모델: klue/roberta-base

Hugging Face Hub
https://huggingface.co/klue/roberta-base

KLUE benchmark 기반 한국어 RoBERTa 모델
extractive QA (context 기반 답 추출)
한국어 자연어 이해(NLU) 대표 모델

라이선스
KLUE RoBERTa 계열 → Apache 2.0 계열 사용으로 알려짐 (KLUE benchmark 공개 정책 기반)

상업적 사용 가능
수정/배포 가능
특허 라이선스 포함 안전한 오픈소스
---------------------------------

## 기술 스택
- Hugging Face Transformers
- Datasets
- Gradio
- PyTorch

---------------------------------

##  실행 방법

```bash
pip install -r requirements.txt
python app.py
```
---------------------------------