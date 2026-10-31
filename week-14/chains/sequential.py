from langchain_core.runnables import RunnableLambda

def analyze_credit(x):

    return {

    "missing":max(
        0,
        132 - x["total"]
    ),

    "data":x
    }

def recommend(x):

    if x["missing"]==0:

        return "졸업 가능"

    return f"{x['missing']}학점 부족"

seq_chain = (

RunnableLambda(analyze_credit)
|
RunnableLambda(recommend)

)