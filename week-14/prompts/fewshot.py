from langchain_core.prompts import FewShotChatMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate

examples = [

{
"input":"전공 4학점 부족",
"output":"부족영역:전공\n추천:전공선택 수강"
},

{
"input":"교양 2학점 부족",
"output":"부족영역:교양\n추천:교양과목 수강"
}

]

example_prompt = ChatPromptTemplate.from_messages([

("human","{input}"),
("ai","{output}")

])

fewshot_prompt = FewShotChatMessagePromptTemplate(

examples=examples,
example_prompt=example_prompt

)