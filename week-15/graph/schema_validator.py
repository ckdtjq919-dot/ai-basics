"""
schema_validator.py

확장 기능

Cypher Validation
"""

VALID_NODE_TYPES = {

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


def validate_cypher(
    cypher: str
):

    for rel in VALID_RELATIONS:

        if rel in cypher:
            return True

    return False


def validate_or_raise(
    cypher: str
):

    if not validate_cypher(
        cypher
    ):

        raise ValueError(

            f"Invalid Cypher\n{cypher}"
        )

    return True