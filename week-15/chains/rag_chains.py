from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)


class SimpleRAGChain:

    def __init__(
        self,
        retriever
    ):
        self.retriever = retriever

    def invoke(
        self,
        inputs
    ):

        query = inputs["query"]

        docs = self.retriever.invoke(
            query
        )

        context = "\n\n".join(

            d.page_content

            for d in docs
        )

        prompt = f"""
        Answer using only context.

        Context:
        {context}

        Question:
        {query}
        """

        answer = llm.invoke(
            prompt
        ).content

        return {

            "result": answer,

            "source_documents": docs
        }


def build_vector_chain(
    retriever
):

    return SimpleRAGChain(
        retriever
    )


def build_hybrid_chain(
    retriever
):

    return SimpleRAGChain(
        retriever
    )