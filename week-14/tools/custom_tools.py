from langchain.tools import tool

from rag.rag_chain import rag_chain

@tool
def calculate_graduation(

total:int,
liberal:int,
major_required:int,
major_selective:int

)->str:

    """
    졸업요건 충족 여부 계산
    """

    result=[]

    if total<132:
        result.append("총학점 부족")

    if liberal<35:
        result.append("교양 부족")

    if major_required<15:
        result.append("전필 부족")

    if major_selective<51:
        result.append("전선 부족")

    return ",".join(result)


@tool
def academic_schedule(

keyword:str

)->str:

    """
    학사 일정 조회
    """

    schedules = {

    "개강":"2026-03-03",
    "중간":"2026-04-21",
    "기말":"2026-06-16"

    }

    return schedules.get(

        keyword,
        "없음"

    )


@tool
def handbook_search(

question:str

)->str:

    """
    학칙/수강편람 검색
    """

    return rag_chain.invoke(

        question

    )