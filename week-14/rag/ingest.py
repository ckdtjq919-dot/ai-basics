from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

urls = [

"https://rule.konkuk.ac.kr/lmxsrv/main/main.do",

"https://www.kku.ac.kr/cms/FR_CON/index.do?MENU_ID=1350&SCH_GBN=SUM&SCH_YEAR=2026"

]

docs=[]

for url in urls:

    loader = WebBaseLoader(url)

    docs.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(

chunk_size=700,
chunk_overlap=150

)

chunks = splitter.split_documents(docs)

print(len(chunks))

embedding = OpenAIEmbeddings(

model="text-embedding-3-small"

)

db = FAISS.from_documents(

chunks,
embedding

)

db.save_local(

"vectorstore"

)
