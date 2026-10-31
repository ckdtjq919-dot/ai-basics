"""
ragas_eval.py
"""

import pandas as pd

from datasets import Dataset

from ragas import evaluate

from ragas.metrics import (

    faithfulness,

    answer_relevancy,

    context_precision,

    context_recall
)

from evaluation.testset import (
    TESTSET
)


def run_ragas(

    chain
):

    rows = []

    for item in TESTSET:

        result = chain.invoke({

            "query":
            item["question"]
        })

        answer = result["result"]

        contexts = []

        if "source_documents" in result:

            contexts = [

                doc.page_content

                for doc

                in result[
                    "source_documents"
                ]
            ]

        rows.append({

            "question":
            item["question"],

            "answer":
            answer,

            "contexts":
            contexts,

            "ground_truth":
            item["ground_truth"]
        })

    dataset = Dataset.from_pandas(

        pd.DataFrame(rows)
    )

    score = evaluate(

        dataset,

        metrics=[

            faithfulness,

            answer_relevancy,

            context_precision,

            context_recall
        ]
    )

    score_df = score.to_pandas()

    score_df.to_csv(

        "ragas_scores.csv",

        index=False
    )

    return score_df