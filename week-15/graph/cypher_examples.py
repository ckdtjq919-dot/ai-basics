"""
cypher_examples.py

확장 기능

Few-shot Cypher Examples
"""

FEW_SHOT_EXAMPLES = [

{
    "question":
    "Who directed Interstellar?",

    "cypher":
    """
    MATCH (m:Movie {title:'Interstellar'})
    <-[:DIRECTED]-(d:Director)
    RETURN d.name
    """
},

{
    "question":
    "Who acted in Titanic?",

    "cypher":
    """
    MATCH (a:Actor)
    -[:ACTED_IN]->
    (m:Movie {title:'Titanic'})

    RETURN a.name
    """
},

{
    "question":
    "Count SF movies",

    "cypher":
    """
    MATCH (m:Movie)
    -[:BELONGS_TO_GENRE]->
    (:Genre {name:'SF'})

    RETURN count(m)
    """
},

{
    "question":
    "Movies directed by Nolan",

    "cypher":
    """
    MATCH (d:Director {
        name:'Christopher Nolan'
    })

    -[:DIRECTED]->
    (m:Movie)

    RETURN m.title
    """
},

{
    "question":
    "Actors in Nolan movies",

    "cypher":
    """
    MATCH (d:Director {
        name:'Christopher Nolan'
    })

    -[:DIRECTED]->
    (m:Movie)

    <-[:ACTED_IN]-
    (a:Actor)

    RETURN a.name
    """
}
]