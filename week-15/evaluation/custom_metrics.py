"""
custom_metrics.py

확장 기능

Response Time
"""

import time


def measure_latency(

    chain,
    question
):

    start = time.time()

    result = chain.invoke(
        {"query": question}
    )

    end = time.time()

    return {

        "latency":

        round(
            end-start,
            3
        ),

        "answer":

        result["result"]
    }