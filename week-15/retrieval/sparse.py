"""
sparse.py

과제 요구사항 C

BM25 Sparse Retrieval
"""

from langchain_community.retrievers import (
    BM25Retriever
)


def build_sparse_retriever(
    chunks,
    k=5
):

    retriever = BM25Retriever.from_documents(
        chunks
    )

    retriever.k = k

    return retriever