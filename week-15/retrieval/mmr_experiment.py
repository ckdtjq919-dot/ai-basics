"""
mmr_experiment.py

과제 요구사항 D
"""

from retrieval.dense import (

    build_dense_retriever,

    build_mmr_retriever
)


def compare_mmr(

    chunks,

    query
):

    similarity = build_dense_retriever(
        chunks
    )

    mmr_low = build_mmr_retriever(

        chunks,

        lambda_mult=0.2
    )

    mmr_high = build_mmr_retriever(

        chunks,

        lambda_mult=0.8
    )

    print("\nSimilarity")

    for doc in similarity.invoke(
        query
    ):

        print(
            doc.page_content[:150]
        )

    print("\nMMR 0.2")

    for doc in mmr_low.invoke(
        query
    ):

        print(
            doc.page_content[:150]
        )

    print("\nMMR 0.8")

    for doc in mmr_high.invoke(
        query
    ):

        print(
            doc.page_content[:150]
        )