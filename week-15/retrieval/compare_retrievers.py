"""
compare_retrievers.py

과제 요구사항 C

5개 이상 질의 비교
"""

import pandas as pd


TEST_QUERIES = [

    "Who directed Interstellar?",

    "movie about dreams",

    "SF movies",

    "actors in Nolan movies",

    "Dune director"
]


def compare(

    dense,

    sparse,

    hybrid
):

    rows = []

    for q in TEST_QUERIES:

        dense_docs = dense.invoke(q)

        sparse_docs = sparse.invoke(q)

        hybrid_docs = hybrid.invoke(q)

        rows.append({

            "query": q,

            "dense":

                dense_docs[0]
                .page_content[:100],

            "sparse":

                sparse_docs[0]
                .page_content[:100],

            "hybrid":

                hybrid_docs[0]
                .page_content[:100]
        })

    df = pd.DataFrame(
        rows
    )

    df.to_csv(

        "retriever_compare.csv",

        index=False
    )

    return df