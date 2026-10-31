# 인공지능기초 (Artificial Intelligence Basics) 통합 저장소

인공지능기초 교과목의 주차별 실습 코드, 보고서 및 과제 프로젝트를 통합 관리하는 저장소입니다.

---

## 📚 주차별 구성 및 프로젝트 안내

| 주차 | 디렉터리 | 주요 내용 | 산출물 |
| :---: | :--- | :--- | :--- |
| **02주차** | [`week-02/`](./week-02/) | 2주차 AI 기초 개념 및 동향 분석 | 개인보고서(PDF) |
| **03주차** | [`week-03/`](./week-03/) | 3주차 머신러닝/딥러닝 알고리즘 분석 | 개인보고서(PDF) |
| **04주차** | [`week-04/`](./week-04/) | 4주차 AI 모델 적용 사례 발표 | 보고서 & 발표자료(PPT) |
| **05주차** | [`week-05/`](./week-05/) | 5주차 AI 비즈니스 모델 및 활용 연구 | 보고서 & 발표자료(PPT) |
| **07주차** | [`week-07/`](./week-07/) | OpenAI API 기본 연동 및 프롬프트 엔지니어링 | `test2.py`, 보고서 |
| **09주차** | [`week-09/`](./week-09/) | 도서 메타데이터 벡터 임베딩 생성 및 저장 | `embeddingbooks.py`, `embeddings.json` |
| **10주차** | [`week-10/`](./week-10/) | 텍스트 임베딩 모델 비교 및 유사도 분석 | `textembeddingbooks.py`, 보고서 |
| **11주차** | [`week-11/`](./week-11/) | RAG(검색 증강 생성) 인제스천 및 쿼리 엔진 구현 | `RAGengine.py`, `RAGingestion.py`, `RAGmain.py` |
| **13주차** | [`week-13/`](./week-13/) | 한국어 도서 리뷰 감성 분석 및 멀티태스크 NLP 앱 | `app.py`, KoELECTRA 감성분석, 웹 UI |
| **14주차** | [`week-14/`](./week-14/) | LangChain 기반 Campus Agent & RAG 시스템 | Agent, Chains, RAG 파이프라인, VectorStore |
| **15주차** | [`week-15/`](./week-15/) | Graph RAG & Hybrid Vector 검색 파이널 프로젝트 | Graph RAG, Neo4j, Hybrid 검색, 평가 모듈 |

---

## 🛠️ 기술 스택
- **Language**: Python 3.10+
- **LLM / Embedding**: OpenAI (GPT-4o, Text-Embedding-3), KoELECTRA
- **Frameworks**: LangChain, FastAPI / Flask, Streamlit
- **Databases / VectorStore**: Neo4j (Graph DB), Chroma / VectorStore
- **NLP / ML**: PyTorch, Transformers, Scikit-Learn

---

## 🔒 보안 및 환경설정 안내
- 본 저장소의 모든 `.env` 파일은 보안상 제외되어 있으며, 각 주차별 폴더의 `.env.example` 템플릿을 참고하여 API Key를 설정할 수 있습니다.
- 대용량 동영상(`.mp4`) 및 가상환경(`venv/`)은 저장소 용량 최적화를 위해 `.gitignore` 처리되었습니다.
