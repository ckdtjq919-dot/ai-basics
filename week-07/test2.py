import os
import json
import pdfplumber
import wikipedia
from dotenv import load_dotenv
from openai import OpenAI

# -------------------------------
# 환경변수 로드
# -------------------------------
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -------------------------------
# Guardrails (입력 검증)
# -------------------------------
def validate_input(user_input):
    if len(user_input) > 500:
        return False, "❌ 입력이 너무 깁니다."
    
    blocked_words = ["욕설", "비속어"]
    if any(word in user_input for word in blocked_words):
        return False, "❌ 부적절한 입력입니다."
    
    return True, ""

# -------------------------------
# PDF 텍스트 추출
# -------------------------------
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text

# -------------------------------
# 텍스트 분할
# -------------------------------
def split_text(text, chunk_size=1500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# -------------------------------
# PDF 요약 함수 (Function 1)
# -------------------------------
def summarize_pdf(file_path):
    text = extract_text_from_pdf(file_path)
    chunks = split_text(text)

    summaries = []
    for chunk in chunks:
        res = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Summarize in Korean."},
                {"role": "user", "content": chunk}
            ]
        )
        summaries.append(res.choices[0].message.content)

    final = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Summarize in Korean."},
            {"role": "user", "content": " ".join(summaries)}
        ]
    )

    return final.choices[0].message.content

# -------------------------------
# 퀴즈 생성 함수 (Function 2)
# -------------------------------
def generate_quiz(summary):
    prompt = f"""
    다음 내용을 기반으로 한국어 객관식 문제 3개를 만들어라.
    각 문제는 보기 4개와 정답을 포함해야 한다.

    내용:
    {summary}
    """

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a teacher."},
            {"role": "user", "content": prompt}
        ]
    )

    return res.choices[0].message.content

# -------------------------------
# 외부 API (Function 3)
# -------------------------------
def search_wikipedia(query):
    try:
        return wikipedia.summary(query, sentences=3)
    except:
        return "검색 결과 없음"

# -------------------------------
# Function Calling 정의
# Function Calling 흐름 -> 사용자 입력 -> LLM 판단 -> 함수 호출 여부 결정 -> 함수 실행 -> 결과를 다시 LLM에 전달 -> 최종 답변 생성
# -------------------------------
tools = [
    {
        "type": "function",
        "function": {
            "name": "summarize_pdf",
            "description": "PDF 파일을 요약한다",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {"type": "string"}
                },
                "required": ["file_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "generate_quiz",
            "description": "요약 내용을 기반으로 퀴즈 생성",
            "parameters": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string"}
                },
                "required": ["summary"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_wikipedia",
            "description": "위키피디아 검색",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"}
                },
                "required": ["query"]
            }
        }
    }
]

# -------------------------------
# 메인 에이전트 루프
# -------------------------------
def run_agent():
    print("🤖 AI 학습 도우미 시작 (종료: exit)")

    # 대화 기록(LLM의 기억 역할)
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Always respond in Korean."
        }
    ]

    while True:
        user_input = input("\n👤 사용자: ")

        if user_input.lower() == "exit":
            break

        # Guardrails 적용 -> 입력 검증
        valid, msg = validate_input(user_input)
        if not valid:
            print(msg)
            continue

        #사용자 메세지 추가
        messages.append({"role": "user", "content": user_input})

        # 1단계: LLM에게 판단 맡기기
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            tools=tools,            # 사용할 수 있는 함수 목록 제공
            tool_choice="auto"      # LLM이 직접 함수 호출 여부 결정
        )

        msg = response.choices[0].message

        # 2단계: 함수 호출 여부 확인
        if msg.tool_calls:
            for tool_call in msg.tool_calls:                    # LLM이 함수 사용을 판단한 경우
                name = tool_call.function.name                  # 호출할 함수 이름
                args = json.loads(tool_call.function.arguments) # 인자 파싱

                try:    # 3단계: 실제 Python 함수 실행
                    if name == "summarize_pdf":
                        result = summarize_pdf(args["file_path"])

                    elif name == "generate_quiz":
                        result = generate_quiz(args["summary"])

                    elif name == "search_wikipedia":
                        result = search_wikipedia(args["query"])

                except Exception as e:
                    result = f"에러 발생: {str(e)}"

                # 4단계: LLM에게 "함수 결과" 전달
                messages.append(msg)                # 함수 호출 요청 메시지 저장
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result                # 함수 실행 결과
                })

            # 5단계: 최종 응답 생성
            final = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=messages
            )

            # 대화 기록 저장
            print("\n🤖 AI:", final.choices[0].message.content)
            messages.append({"role": "assistant", "content": final.choices[0].message.content})

        else:
            # 일반 대화
            print("\n🤖 AI:", msg.content)
            messages.append({"role": "assistant", "content": msg.content})

# -------------------------------
# 실행
# -------------------------------
if __name__ == "__main__":
    run_agent()