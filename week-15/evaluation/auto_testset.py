"""
auto_testset.py

확장 기능

Auto Testset
"""

from ragas.testset import (
    TestsetGenerator
)


def build_auto_testset(

    llm,
    embeddings,
    docs
):

    generator = TestsetGenerator(
        llm=llm,
        embedding_model=embeddings
    )

    dataset = generator.generate(
        docs,
        testset_size=20
    )

    dataset.to_pandas().to_csv(

        "auto_testset.csv",

        index=False
    )

    return dataset