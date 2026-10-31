from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers import StrOutputParser

from prompts.templates import advisor_prompt
from prompts.templates import classification_prompt

llm = ChatOpenAI(

model="gpt-4.1-mini",
temperature=0

)

classification_chain = (

classification_prompt
| llm
| JsonOutputParser()

)

advisor_chain = (

advisor_prompt
| llm
| StrOutputParser()

)