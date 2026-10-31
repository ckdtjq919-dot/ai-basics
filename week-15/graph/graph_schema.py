"""
graph_schema.py

Graph schema 명시

Schema Validation용
"""

VALID_NODES = {

    "Movie",

    "Actor",

    "Director",

    "Genre"
}

VALID_RELATIONS = {

    "ACTED_IN",

    "DIRECTED",

    "BELONGS_TO_GENRE"
}


GRAPH_SCHEMA = """

Nodes:

Movie

Actor

Director

Genre


Relationships:

(ACTOR)-[:ACTED_IN]->(MOVIE)

(DIRECTOR)-[:DIRECTED]->(MOVIE)

(MOVIE)-[:BELONGS_TO_GENRE]->(GENRE)

"""