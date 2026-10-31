"""
splitters.py

프로젝트 요구사항 B

1. Recursive Splitter
2. Semantic Splitter

비교 실험 가능
"""

from statistics import mean

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_experimental.text_splitter import (
    SemanticChunker
)

from langchain_openai import (
    OpenAIEmbeddings
)


# --------------------------------
# Recursive Splitter
# --------------------------------

def recursive_split(docs):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1000,

        chunk_overlap=200,

        separators=[
            "\n\n",
            "\n",
            ".",
            " "
        ]
    )

    chunks = splitter.split_documents(
        docs
    )

    return chunks


# --------------------------------
# Semantic Splitter
# --------------------------------

def semantic_split(docs):

    embeddings = OpenAIEmbeddings(

        model="text-embedding-3-small"
    )

    splitter = SemanticChunker(

        embeddings
    )

    chunks = splitter.split_documents(
        docs
    )

    return chunks


# --------------------------------
# 통계 비교
# --------------------------------

def compare_splitters(docs):

    recursive_chunks = recursive_split(
        docs
    )

    semantic_chunks = semantic_split(
        docs
    )

    recursive_lengths = [

        len(c.page_content)

        for c in recursive_chunks
    ]

    semantic_lengths = [

        len(c.page_content)

        for c in semantic_chunks
    ]

    print("\n==========")

    print(
        "Recursive Splitter"
    )

    print(
        f"Chunks: {len(recursive_chunks)}"
    )

    print(
        f"Avg Length: {mean(recursive_lengths):.2f}"
    )

    print("\n==========")

    print(
        "Semantic Splitter"
    )

    print(
        f"Chunks: {len(semantic_chunks)}"
    )

    print(
        f"Avg Length: {mean(semantic_lengths):.2f}"
    )

    return {

        "recursive": recursive_chunks,

        "semantic": semantic_chunks
    }


# --------------------------------
# 기본 사용 Splitter
# --------------------------------

def build_splitters(docs):

    chunks = recursive_split(
        docs
    )

    print(
        f"Final Chunks: {len(chunks)}"
    )

    return chunks


if __name__ == "__main__":

    from loaders import load_documents

    docs = load_documents()

    compare_splitters(
        docs
    )