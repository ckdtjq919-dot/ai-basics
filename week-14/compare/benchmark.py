from rag.rag_chain import rag_chain
from agent.react_agent import agent

questions = [

    "졸업 가능?",
    "개강 언제?",
    "전필 부족하면?",
    "교양 부족인데 추천해줘",
    "학칙 기준 졸업요건"

]

for q in questions:

    print("=" * 60)
    print("QUESTION:", q)

    print("\n[RAG Chain]")

    rag_result = rag_chain.invoke(q)

    print(rag_result)

    print("\n[ReAct Agent]")

    agent_result = agent.invoke({

        "messages":[
            ("user", q)
        ]

    })

    print(
        agent_result["messages"][-1].content
    )

    print()