"""
graph_loader.py

Neo4j connection
"""

import os

from dotenv import load_dotenv

from langchain_community.graphs import (
    Neo4jGraph
)

load_dotenv()


def get_graph():

    graph = Neo4jGraph(

        url=os.getenv(
            "NEO4J_URI"
        ),

        username=os.getenv(
            "NEO4J_USERNAME"
        ),

        password=os.getenv(
            "NEO4J_PASSWORD"
        )
    )

    return graph