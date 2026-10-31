import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


# [요구사항 2.1.D] 1단계: Retrieve (검색)
def retrieve(query, index, namespace, top_k=3, filter_dict=None):
    query_embedding = client.embeddings.create(
        input=[query], model="text-embedding-3-small"
    ).data[0].embedding
    
    res = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True,
        namespace=namespace,
        filter=filter_dict # [요구사항 2.2 확장] 메타데이터 필터링
    )
    
    # 스크린샷 오타 수정: m 변수로 통일
    docs = [m['metadata']['text'] for m in res['matches']]
    sources = [{"title": m['metadata']['title'], "url": m['metadata']['url']} for m in res['matches']]
    return docs, sources

# [요구사항 2.1.D] 2단계: Augment (프롬프트 구성)
def prompt_with_context_builder(query, docs):
    context = "\n\n---\n\n".join(docs)
    return f"""당신은 전문 비평가입니다. 아래 제공된 [Context]를 바탕으로만 답변하세요.
모르는 내용은 '정보가 부족합니다'라고 답하세요.

[Context]
{context}

[Question]
{query}
"""

# [요구사항 2.1.D] 3단계: Generate (답변 생성)
def question_answering(query, index, namespace, filter_dict=None):
    docs, sources = retrieve(query, index, namespace, filter_dict=filter_dict)
    prompt = prompt_with_context_builder(query, docs)
    
    # [요구사항 1] gpt-4.1-mini 사용
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    
    answer = response.choices[0].message.content
    
    # 출처 자동 첨부
    citation_text = "\n\n**[출처 정보]**\n" + "\n".join([f"- {s['title']} ({s['url']})" for s in sources])
    return answer + citation_text