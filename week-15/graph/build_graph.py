"""
build_graph.py

Movie Graph 생성
"""

import os
import pandas as pd

from dotenv import load_dotenv

from neo4j import GraphDatabase

load_dotenv()


URI = os.getenv("NEO4J_URI")

USER = os.getenv(
    "NEO4J_USERNAME"
)

PASSWORD = os.getenv(
    "NEO4J_PASSWORD"
)


driver = GraphDatabase.driver(

    URI,

    auth=(USER, PASSWORD)
)


def create_constraints(tx):

    tx.run(

    """
    CREATE CONSTRAINT movie_title
    IF NOT EXISTS

    FOR (m:Movie)

    REQUIRE m.title IS UNIQUE
    """
    )


def load_movies(tx):

    df = pd.read_csv(
        "data/raw/movies.csv"
    )

    for _, row in df.iterrows():

        tx.run(

        """
        MERGE (m:Movie {
            title:$title
        })

        SET
            m.year=$year
        """,

        title=row["title"],
        year=int(row["year"])
        )


def load_directors(tx):

    df = pd.read_csv(
        "data/raw/movies.csv"
    )

    for _, row in df.iterrows():

        tx.run(

        """
        MERGE (d:Director {
            name:$director
        })

        MERGE (m:Movie {
            title:$title
        })

        MERGE (d)
        -[:DIRECTED]->
        (m)
        """,

        director=row["director"],
        title=row["title"]
        )


def load_actors(tx):

    actors = pd.read_csv(
        "data/raw/actors.csv"
    )

    movie_actor = pd.read_csv(
        "data/raw/movie_actor.csv"
    )

    movies = pd.read_csv(
        "data/raw/movies.csv"
    )

    actor_map = {

        row["actor_id"]: row["name"]

        for _, row

        in actors.iterrows()
    }

    movie_map = {

        row["movie_id"]: row["title"]

        for _, row

        in movies.iterrows()
    }

    for _, row in movie_actor.iterrows():

        tx.run(

        """
        MERGE (a:Actor {
            name:$actor
        })

        MERGE (m:Movie {
            title:$movie
        })

        MERGE (a)
        -[:ACTED_IN]->
        (m)
        """,

        actor=actor_map[
            row["actor_id"]
        ],

        movie=movie_map[
            row["movie_id"]
        ]
        )


def load_genres(tx):

    genres = pd.read_csv(
        "data/raw/movie_genre.csv"
    )

    movies = pd.read_csv(
        "data/raw/movies.csv"
    )

    movie_map = {

        row["movie_id"]: row["title"]

        for _, row

        in movies.iterrows()
    }

    for _, row in genres.iterrows():

        tx.run(

        """
        MERGE (g:Genre {
            name:$genre
        })

        MERGE (m:Movie {
            title:$movie
        })

        MERGE (m)
        -[:BELONGS_TO_GENRE]->
        (g)
        """,

        genre=row["genre"],

        movie=movie_map[
            row["movie_id"]
        ]
        )


def build_graph():

    with driver.session() as session:

        session.execute_write(
            create_constraints
        )

        session.execute_write(
            load_movies
        )

        session.execute_write(
            load_directors
        )

        session.execute_write(
            load_actors
        )

        session.execute_write(
            load_genres
        )

    print(
        "Graph Build Complete"
    )


if __name__ == "__main__":

    build_graph()