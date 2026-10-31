class HybridRetriever:

    def __init__(
        self,
        dense,
        sparse
    ):

        self.dense = dense
        self.sparse = sparse

    def invoke(
        self,
        query
    ):

        dense_docs = self.dense.invoke(
            query
        )

        sparse_docs = self.sparse.invoke(
            query
        )

        merged = {}

        for doc in dense_docs + sparse_docs:

            key = doc.page_content

            if key not in merged:
                merged[key] = doc

        return list(
            merged.values()
        )[:5]


def build_hybrid_retriever(
    dense,
    sparse
):

    return HybridRetriever(
        dense,
        sparse
    )