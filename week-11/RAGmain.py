import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

from RAGengine import question_answering
from RAGingestion import index
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="비평 RAG 시스템", layout="wide")
st.title("🎬 전문 비평 RAG 시스템 시연")

# [요구사항 2.1.B] 사이드바 네임스페이스 선택
st.sidebar.header("설정")
domain = st.sidebar.selectbox("도메인 선택", ["영화 비평", "도서 비평"])
target_ns = "movie_critics" if domain == "영화 비평" else "book_reviews"

# [요구사항 5.2] 인덱스 상태 시각화
if st.sidebar.button("인덱스 통계 확인"):
    st.sidebar.json(index.describe_index_stats())

query = st.text_input("질문을 입력하세요:")

if query:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. RAG 기반 답변")
        # [요구사항 2.2] 확장 필터 적용 시연
        ans = question_answering(query, index, target_ns, filter_dict={"year": {"$gte": 2024}})
        st.info(ans)
        
    with col2:
        st.subheader("2. Vanilla LLM 답변")
        res = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": query}]
        )
        st.warning(res.choices[0].message.content)