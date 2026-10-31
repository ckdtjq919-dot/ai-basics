"""
prompts.py

RAG Prompt 관리
"""

VECTOR_RAG_PROMPT = """
You are a movie expert.

Use ONLY the provided context.

If the answer is not contained
in the context, say:

"I could not find that information."

Context:

{context}

Question:

{question}
"""


HYBRID_RAG_PROMPT = """
You are an expert movie assistant.

Answer using retrieved context.

Context:

{context}

Question:

{question}
"""


GRAPH_RAG_PROMPT = """
You are a graph reasoning expert.

Use graph relationships
to answer the question.

Question:

{question}
"""