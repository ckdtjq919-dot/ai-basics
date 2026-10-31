import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from ingestion.loaders import load_documents
from ingestion.splitters import build_splitters

from retrieval.dense import build_dense_retriever
from retrieval.sparse import build_sparse_retriever
from retrieval.hybrid import build_hybrid_retriever

from chains.rag_chains import build_vector_chain, build_hybrid_chain
from graph.graph_qa import build_graph_chain


@st.cache_resource
def init_system():

    docs = load_documents("data/raw")
    chunks = build_splitters(docs)

    dense = build_dense_retriever(chunks)
    sparse = build_sparse_retriever(chunks)
    hybrid = build_hybrid_retriever(dense, sparse)

    vector_chain = build_vector_chain(dense)
    hybrid_chain = build_hybrid_chain(hybrid)
    graph_chain = build_graph_chain()

    return vector_chain, hybrid_chain, graph_chain


vector_chain, hybrid_chain, graph_chain = init_system()

st.set_page_config(page_title="Movie Graph RAG", layout="wide")

st.title("🎬 Movie Graph RAG Dashboard")

query = st.text_input("Ask a question")

if query:

    with st.spinner("Thinking..."):

        vector_answer = vector_chain.invoke({"query": query})["result"]
        hybrid_answer = hybrid_chain.invoke({"query": query})["result"]
        graph_answer = graph_chain.invoke({"query": query})["result"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Vector RAG")
        st.write(vector_answer)

    with col2:
        st.subheader("Hybrid RAG")
        st.write(hybrid_answer)

    with col3:
        st.subheader("Graph RAG")
        st.write(graph_answer)

st.divider()

st.subheader("Graph Visualization")

try:
    with open("graph.html", "r", encoding="utf-8") as f:
        st.components.v1.html(f.read(), height=700)
except:
    st.warning("Graph visualization not found. Run build_graph first.")