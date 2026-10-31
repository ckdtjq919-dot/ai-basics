import os
from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# [요구사항 2.1.A] 인덱스 설계 결정
# text-embedding-3-small(1536차원) 사용, 코사인 유사도(OpenAI 권장) 선택
index_name = "critics-rag-2026"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric='cosine',
        spec=ServerlessSpec(cloud='aws', region='us-east-1')
    )

index = pc.Index(index_name)

def get_embedding(text):
    return client.embeddings.create(input=[text], model="text-embedding-3-small").data[0].embedding

def upsert_data_batch(data_list, namespace):
    """[요구사항 2.1.A/B] 배치 Upsert 및 네임스페이스 분리"""
    vectors = []
    for item in data_list:
        vectors.append({
            "id": item['id'],
            "values": get_embedding(item['text']),
            "metadata": {
                "text": item['text'], 
                "title": item['title'], 
                "url": item['url'],
                "year": item.get('year', 2026) # 확장 기능 필터용
            }
        })
    
    # 100개씩 배치 업로드
    for i in range(0, len(vectors), 100):
        index.upsert(vectors=vectors[i:i+100], namespace=namespace)

# [요구사항 2.1.C] 수명주기 관리 시연
def manage_data(namespace):
    # Update 시연
    index.update(id="doc_1", set_metadata={"title": "Updated Title"}, namespace=namespace)
    # 삭제 시연 (ID, 필터, 전체 삭제 순)
    index.delete(ids=["old_doc"], namespace=namespace)
    index.delete(filter={"year": {"$lt": 2020}}, namespace=namespace)