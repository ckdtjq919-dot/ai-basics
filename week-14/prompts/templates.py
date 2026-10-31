from langchain_core.prompts import ChatPromptTemplate

advisor_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        너는 건국대학교 글로컬캠퍼스 학사 상담 AI다.
        학칙과 학사일정을 기반으로 답변한다.
        """
    ),
    (
        "human",
        "{question}"
    )
])

classification_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        질문 유형 분류:

        graduation
        schedule
        curriculum
        general
        """
    ),
    ("human","{question}")
])