from dotenv import load_dotenv
load_dotenv()

from langgraph.prebuilt import create_react_agent

from langchain_openai import ChatOpenAI

from tools.custom_tools import *

llm = ChatOpenAI(

model="gpt-4.1-mini"

)

agent = create_react_agent(

llm,

tools=[

calculate_graduation,
academic_schedule,
handbook_search

]

)

question = input("질문:")

result = agent.invoke({

"messages":[

("user",question)

]

})

print(result)