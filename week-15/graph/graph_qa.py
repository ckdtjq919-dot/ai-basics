"""
graph_qa.py
"""
import re
import os

from dotenv import load_dotenv

from neo4j import GraphDatabase

from langchain_openai import (
    ChatOpenAI
)

load_dotenv()


llm = ChatOpenAI(
    model="gpt-4o"
)

driver = GraphDatabase.driver(

    os.getenv("NEO4J_URI"),

    auth=(

        os.getenv(
            "NEO4J_USERNAME"
        ),

        os.getenv(
            "NEO4J_PASSWORD"
        )
    )
)

def clean_cypher(cypher: str):

    # ```cypher 제거
    cypher = re.sub(
        r"```cypher",
        "",
        cypher,
        flags=re.IGNORECASE
    )

    # ``` 제거
    cypher = re.sub(
        r"```",
        "",
        cypher
    )

    return cypher.strip()

SYSTEM_PROMPT = """
You are a Neo4j Cypher expert.

Graph Schema:

(:Movie)
(:Actor)
(:Director)
(:Genre)

Relationships:

ACTED_IN
DIRECTED
BELONGS_TO_GENRE

Rules:

1. Return ONLY executable Cypher.
2. Do NOT use markdown.
3. Do NOT use ```cypher blocks.
4. Do NOT explain.
5. Return only the query.

Example:

MATCH (d:Director)-[:DIRECTED]->(m:Movie)
RETURN d.name
"""

def generate_cypher(question):

    prompt = f"""
    {SYSTEM_PROMPT}

    Question:
    {question}
    """

    response = llm.invoke(
        prompt
    ).content

    return clean_cypher(
        response
    ) 

def run_cypher(
    cypher
):

    with driver.session() as session:

        result = session.run(
            cypher
        )

        return [

            record.data()

            for record in result
        ]

def invoke(
    self,
    query
):

    q = query["query"]

    cypher = generate_cypher(q)

    print("\n====================")
    print("Generated Cypher")
    print(cypher)
    print("====================")

    result = run_cypher(
        cypher
    )

    return {

        "result": str(result),

        "cypher": cypher
    }

class GraphQAChain:

    def invoke(
        self,
        query
    ):

        q = query["query"]

        cypher = generate_cypher(
            q
        )

        result = run_cypher(
            cypher
        )

        return {

            "result": str(result),

            "cypher": cypher
        }


def build_graph_chain():

    return GraphQAChain()