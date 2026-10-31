"""
visualization.py
"""

import pandas as pd
import matplotlib.pyplot as plt


def visualize_scores():

    df = pd.read_csv(
        "ragas_scores.csv"
    )

    metrics = [

        "faithfulness",

        "answer_relevancy",

        "context_precision",

        "context_recall"
    ]

    means = [

        df[m].mean()

        for m in metrics
    ]

    plt.figure(
        figsize=(8,5)
    )

    plt.bar(

        metrics,

        means
    )

    plt.title(
        "RAGAS Evaluation"
    )

    plt.savefig(
        "ragas_chart.png"
    )

    plt.show()