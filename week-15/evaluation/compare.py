"""
compare.py
"""

from evaluation.ragas_eval import (
    run_ragas
)


def compare_systems(

    dense_chain,

    hybrid_chain
):

    dense_scores = run_ragas(
        dense_chain
    )

    hybrid_scores = run_ragas(
        hybrid_chain
    )

    print("\nDense")

    print(
        dense_scores.mean(
            numeric_only=True
        )
    )

    print("\nHybrid")

    print(
        hybrid_scores.mean(
            numeric_only=True
        )
    )