"""
router_chain.py

확장 기능

Vector + Graph Router
"""

GRAPH_KEYWORDS = [

    "relationship",

    "actor",

    "director",

    "genre",

    "count",

    "connected",

    "graph",

    "who acted",

    "who directed"
]


class RAGRouter:

    def __init__(

        self,

        vector_chain,

        hybrid_chain,

        graph_chain
    ):

        self.vector_chain = (
            vector_chain
        )

        self.hybrid_chain = (
            hybrid_chain
        )

        self.graph_chain = (
            graph_chain
        )

    def route(
        self,
        query
    ):

        query_lower = query.lower()

        for keyword in GRAPH_KEYWORDS:

            if keyword in query_lower:

                return "graph"

        return "hybrid"

    def invoke(
        self,
        query
    ):

        target = self.route(
            query
        )

        if target == "graph":

            result = self.graph_chain.invoke(
                {"query": query}
            )

            return {

                "route": "graph",

                "answer":
                result["result"]
            }

        result = self.hybrid_chain.invoke(
            {"query": query}
        )

        return {

            "route": "hybrid",

            "answer":
            result["result"]
        }