"""
metadata_builder.py

프로젝트 요구사항 A

모든 Document에
일관된 Metadata 부여
"""

from datetime import datetime


def enrich_metadata(
    docs,
    source_type="unknown"
):

    enriched = []

    for doc in docs:

        metadata = doc.metadata.copy()

        metadata.update({

            "type": source_type,

            "processed_date": datetime.now().strftime(
                "%Y-%m-%d"
            ),

            "project": "Movie Graph RAG",

            "author": "임창섭"
        })

        doc.metadata = metadata

        enriched.append(doc)

    return enriched


def print_metadata_stats(
    docs
):

    print("\nMetadata Sample\n")

    for doc in docs[:3]:

        print(doc.metadata)