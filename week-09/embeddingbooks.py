# =========================================
# 📌 라이브러리
# =========================================
from openai import OpenAI
import streamlit as st
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import os

# =========================================
# 🔑 API 설정 (.env 사용)
# =========================================
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ API 키가 없습니다. .env 파일 확인하세요.")
    st.stop()

client = OpenAI(api_key=api_key)

# =========================================
# 📌 임베딩 함수
# =========================================
def get_embedding(text):
    res = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return res.data[0].embedding

# =========================================
# 📌 GPT (데이터 생성/확장용)
# =========================================
def enrich_text(text):
    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "책 설명을 더 풍부하게 확장해줘"},
            {"role": "user", "content": text}
        ]
    )
    return res.choices[0].message.content

# =========================================
# 📌 코사인 유사도 직접 구현
# =========================================
def cosine_similarity_manual(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# =========================================
# 📌 검증 코드
# =========================================
def verify_cosine(a, b):
    manual = cosine_similarity_manual(a, b)
    lib = cosine_similarity([a], [b])[0][0]
    return manual, lib

# =========================================
# 📌 데이터 생성 (안정화 버전)
# =========================================
def generate_books(n=50):
    books = []
    titles = set()  # 제목 중복 체크

    prompt = """
    책 데이터를 JSON 형식으로 만들어줘.
    반드시 아래 형식만 사용:

    {
      "title": "책 제목",
      "description": "책 설명",
      "review": "리뷰"
    }

    다른 말 절대 하지마.
    절대 중복되지 않게 만들어줘.                        
    리뷰에 대해서는 인물이나 감상을 더 풍부하게 표현해줘.
    """

    while len(books) < n:
        res = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        try:
            data = json.loads(res.choices[0].message.content)
            
            ####### 중복 수정 전 코드 #######
            #if all(k in data for k in ["title", "description", "review"]):
            #books.append(data)

            ####### 중복 수정 후 코드 #######
            if not all(k in data for k in ["title", "description", "review"]):
                continue
            
            title = data["title"]
            
            if title in titles:
                continue

            titles.add(title)
            books.append(data)
            ##############################
        except:
            continue

    return books

# =========================================
# 📌 임베딩 생성 + 캐싱
# =========================================
def create_embeddings(books):
    for book in books:

        if not all(k in book for k in ["title", "description", "review"]):
            continue

        text = f"{book['title']}. {book['description']}. {book['review']}"

        enriched = enrich_text(text)  # ⭐ 풍부한 임베딩
        book["embedding"] = get_embedding(enriched)

    with open("embeddings.json", "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

# =========================================
# 📌 추천 시스템
# =========================================
def recommend_books(query_emb, books):
    results = []

    for book in books:
        if "embedding" not in book:
            continue

        sim = cosine_similarity_manual(query_emb, book["embedding"])
        results.append((sim, book))

    results.sort(reverse=True, key=lambda x: x[0])
    return results[:5]

# =========================================
# 📌 키워드 검색
# =========================================
def keyword_search(query, books):
    return [b for b in books if "description" in b and query in b["description"]]

# =========================================
# 📌 제로샷 분류
# =========================================
genres = [
    "이 책은 판타지 장르이다",
    "이 책은 로맨스 장르이다",
    "이 책은 공포 장르이다",
    "이 책은 과학 장르이다"
]

@st.cache_data
def get_genre_embeddings():
    return [get_embedding(g) for g in genres]

def classify(query_emb, genre_embeddings):
    sims = [
        cosine_similarity_manual(query_emb, g_emb)
        for g_emb in genre_embeddings
    ]
    return genres[np.argmax(sims)]

# =========================================
# 📌 UI
# =========================================
st.title("📚 AI 도서 추천 시스템")

if st.button("📥 데이터 생성 및 임베딩"):
    with st.spinner("데이터 생성 중..."):
        books = generate_books(50)
        create_embeddings(books)
    st.success("완료!")

# 데이터 로드
try:
    with open("embeddings.json", "r", encoding="utf-8") as f:
        books = json.load(f)
except:
    books = []

query = st.text_input("찾고 싶은 책을 설명해보세요")

if query and books:

    with st.spinner("AI가 분석 중입니다..."):
        query_emb = get_embedding(query)

        # 키워드 검색
        st.subheader("🔍 키워드 검색")
        kw_results = keyword_search(query, books)
        if kw_results:
            for b in kw_results:
                st.write("-", b["title"])
        else:
            st.write("결과 없음")

        # 추천
        st.subheader("🤖 AI 추천")
        results = recommend_books(query_emb, books)

        for score, b in results:
            st.write(f"{b['title']} (유사도: {score:.4f})")

        # 분류
        genre_embeddings = get_genre_embeddings()
        genre = classify(query_emb, genre_embeddings)

        st.subheader("📌 예측 장르")
        st.write(genre)

# =========================================
# 📌 코사인 검증
# =========================================
if len(books) >= 2:
    a = books[0]["embedding"]
    b = books[1]["embedding"]

    m, l = verify_cosine(a, b)

    st.subheader("📊 코사인 유사도 검증")
    st.write("직접 구현:", m)
    st.write("라이브러리:", l)