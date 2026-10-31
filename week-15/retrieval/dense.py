"""
dense.py

과제 요구사항 C

Dense Retrieval

FAISS 기반

추가:
MMR 지원
"""

from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import (
    FAISS
)


def build_vectorstore(
    chunks
):

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore


def build_dense_retriever(
    chunks,
    k=5
):

    vectorstore = build_vectorstore(
        chunks
    )

    retriever = vectorstore.as_retriever(

        search_type="similarity",

        search_kwargs={
            "k": k
        }
    )

    return retriever


def build_mmr_retriever(
    chunks,
    k=5,
    lambda_mult=0.5
):

    vectorstore = build_vectorstore(
        chunks
    )

    retriever = vectorstore.as_retriever(

        search_type="mmr",

        search_kwargs={

            "k": k,

            "fetch_k": 20,

            "lambda_mult": lambda_mult
        }
    )

    return retriever