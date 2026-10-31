"""
Vector

Hybrid

Graph

비교
"""

import pandas as pd


QUESTIONS = [

    "Who directed Interstellar?",

    "Who acted in Inception?",

    "Movies by Christopher Nolan?",

    "Actors in multiple SF films?",

    "Who worked with Nolan?",

    "Count SF movies",

    "Which actors connect Nolan and Villeneuve?",

    "Movies starring Anne Hathaway?"
]


def compare(

    vector_chain,

    hybrid_chain,

    graph_chain
):

    rows = []

    for q in QUESTIONS:

        vector_result = (

            vector_chain.invoke(q)
        )

        hybrid_result = (

            hybrid_chain.invoke(q)
        )

        graph_result = (

            graph_chain.invoke(

                {"query":q}
            )
        )

        rows.append({

            "question":q,

            "vector":

                str(vector_result),

            "hybrid":

                str(hybrid_result),

            "graph":

                str(graph_result)
        })

    df = pd.DataFrame(
        rows
    )

    df.to_csv(

        "vector_hybrid_graph.csv",

        index=False
    )

    return df