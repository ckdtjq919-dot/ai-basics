from dotenv import load_dotenv
load_dotenv()

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from prompts.templates import advisor_prompt

embedding = OpenAIEmbeddings(

model="text-embedding-3-small"

)

db = FAISS.load_local(

"vectorstore",
embedding,
allow_dangerous_deserialization=True

)

retriever = db.as_retriever()

rag_chain = (

{
"context":retriever,
"question":RunnablePassthrough()
}

| advisor_prompt
| StrOutputParser()

)