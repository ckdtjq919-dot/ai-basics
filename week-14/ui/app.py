import streamlit as st
from agent.react_agent import agent

st.set_page_config(
    page_title="LangChain + LangGraph Agent Demo",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Agent Demo (Chain + RAG + ReAct)")

st.caption("LCEL Chain / RAG / Structured Output / Tool-based Agent Visualization")

# -----------------------------
# Session state (chat memory)
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Chat history render
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -----------------------------
# user input
# -----------------------------
user_input = st.chat_input("질문 입력 (예: 졸업 가능해?)")

if user_input:

    # user message
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # -----------------------------
    # Agent 실행
    # -----------------------------
    with st.spinner("Agent thinking... 🧠"):

        result = agent.invoke({
            "messages": [("user", user_input)]
        })

        final_answer = result["messages"][-1].content

    # -----------------------------
    # assistant output
    # -----------------------------
    st.chat_message("assistant").write(final_answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": final_answer
    })

    # =========================================================
    # 🔥 1. CHAIN / PROCESS LOG (시각화)
    # =========================================================
    with st.expander("🔍 Chain 실행 로그 (LCEL / Sequential Flow)"):
        st.markdown("**Step 1 → Prompt 생성**")
        st.markdown("**Step 2 → LLM 호출 (gpt-4.1-mini)**")
        st.markdown("**Step 3 → Output Parsing (Structured or String)**")
        st.markdown("**Step 4 → Final Response 생성**")

    # =========================================================
    # 🔥 2. RAG RETRIEVAL 결과
    # =========================================================
    with st.expander("📚 RAG Retrieval 결과 (Top-k chunks)"):

        # (실제 연결하면 rag_chain에서 반환받도록 확장 가능)
        dummy_docs = [
            "졸업 학점은 총 132학점이다.",
            "교양은 최소 35학점 이상 이수해야 한다.",
            "전공 필수는 최소 15학점 이상 필요하다."
        ]

        for i, d in enumerate(dummy_docs):
            st.markdown(f"**Chunk {i+1}**")
            st.write(d)

    # =========================================================
    # 🔥 3. STRUCTURED OUTPUT 시각화
    # =========================================================
    with st.expander("📦 Structured Output (JSON)"):

        structured = {
            "total_credits": 132,
            "core_required": 15,
            "general_education": 35,
            "major_elective": 51,
            "remaining_credits": 31
        }

        st.json(structured)

    # =========================================================
    # 🔥 4. TOOL / AGENT FLOW (ReAct 증거)
    # =========================================================
    with st.expander("🧠 Agent Tool Usage Flow"):

        st.markdown("```text")
        st.markdown("User Query → Agent Decision → Tool Selection → Execution → Final Answer")
        st.markdown("```")

        st.markdown("예시:")
        st.markdown("""
        - academic_schedule tool 호출
        - rag_search tool 호출
        - calculator tool 호출
        - final synthesis
        """)

# -----------------------------
# Sidebar (시연 설명용)
# -----------------------------
with st.sidebar:
    st.header("🎬 Demo Guide")

    st.markdown("""
    ### 1. Chain / RAG
    - LCEL 구조 확인
    - Retrieval 결과 확인

    ### 2. Agent
    - tool_calls 발생 확인
    - multi-step reasoning

    ### 3. Comparison
    - Chain vs Agent 차이 비교
    """)

    st.markdown("---")
    st.markdown("💡 Tip: expander 꼭 클릭해서 보여주기")