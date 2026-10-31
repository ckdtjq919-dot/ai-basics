"""
unified_rag.py

최종 시스템
"""

from chains.router_chain import (
    RAGRouter
)

from chains.rag_chains import (

    build_vector_chain,

    build_hybrid_chain
)

from graph.graph_qa import (
    build_graph_chain
)


class UnifiedRAG:

    def __init__(

        self,

        dense_retriever,

        hybrid_retriever
    ):

        self.vector_chain = (

            build_vector_chain(
                dense_retriever
            )
        )

        self.hybrid_chain = (

            build_hybrid_chain(
                hybrid_retriever
            )
        )

        self.graph_chain = (

            build_graph_chain()
        )

        self.router = RAGRouter(

            self.vector_chain,

            self.hybrid_chain,

            self.graph_chain
        )

    def ask(
        self,
        question
    ):

        return self.router.invoke(
            question
        )