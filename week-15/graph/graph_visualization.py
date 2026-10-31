from pyvis.network import Network
from neo4j import GraphDatabase
from dotenv import load_dotenv

import os

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(
        os.getenv("NEO4J_USERNAME"),
        os.getenv("NEO4J_PASSWORD")
    )
)

net = Network(
    height="800px",
    width="100%",
    bgcolor="#ffffff",
    directed=True
)

query = """
MATCH (n)-[r]->(m)
RETURN n,r,m
LIMIT 100
"""

with driver.session() as session:

    result = session.run(query)

    for record in result:

        source = record["n"]
        target = record["m"]
        relation = record["r"]

        source_id = source.element_id
        target_id = target.element_id

        source_label = list(source.labels)[0]
        target_label = list(target.labels)[0]

        net.add_node(
            source_id,
            label=source.get("name", source.get("title", "Unknown")),
            title=source_label
        )

        net.add_node(
            target_id,
            label=target.get("name", target.get("title", "Unknown")),
            title=target_label
        )

        net.add_edge(
            source_id,
            target_id,
            label=relation.type
        )

net.save_graph("graph.html")

print("graph.html 생성 완료")