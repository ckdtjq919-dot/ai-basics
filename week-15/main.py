from dotenv import load_dotenv
load_dotenv()

from ingestion.loaders import load_documents
from ingestion.splitters import build_splitters

from retrieval.dense import build_dense_retriever
from retrieval.sparse import build_sparse_retriever
from retrieval.hybrid import build_hybrid_retriever

from graph.build_graph import build_graph
from graph.graph_qa import build_graph_chain

from chains.rag_chains import build_vector_chain, build_hybrid_chain


def main():

    print("Loading documents...")

    docs = load_documents("data/raw")

    print(f"Loaded docs: {len(docs)}")

    print("Splitting...")

    chunks = build_splitters(docs)

    print(f"Chunks: {len(chunks)}")

    print("Building retrievers...")

    dense = build_dense_retriever(chunks)
    sparse = build_sparse_retriever(chunks)
    hybrid = build_hybrid_retriever(dense, sparse)

    print("Building graph...")

    build_graph()

    print("Building chains...")

    vector_chain = build_vector_chain(dense)
    hybrid_chain = build_hybrid_chain(hybrid)
    graph_chain = build_graph_chain()

    print("System ready!")

    while True:

        q = input("\nQuestion > ")

        if q.lower() == "exit":
            break

        print("\n[VECTOR]")
        print(vector_chain.invoke({"query": q})["result"])

        print("\n[HYBRID]")
        print(hybrid_chain.invoke({"query": q})["result"])

        print("\n[GRAPH]")
        print(graph_chain.invoke({"query": q})["result"])


if __name__ == "__main__":
    main()