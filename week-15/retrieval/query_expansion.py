"""
query_expansion.py

확장 기능

HyDE
"""

from langchain_openai import (
    ChatOpenAI
)


llm = ChatOpenAI(
    model="gpt-4.1-mini"
)


def generate_hypothetical_document(
    query
):

    prompt = f"""
    Write a short document
    that answers:

    {query}
    """

    return llm.invoke(
        prompt
    ).content


def expand_query(
    query
):

    hypothetical = generate_hypothetical_document(
        query
    )

    return f"""

    {query}

    {hypothetical}

    """