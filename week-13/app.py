import gradio as gr

from tasks.HF_sentiment import analyze_sentiment
from tasks.HF_zeroshot import classify_genre
from tasks.HF_summarization import summarize
from tasks.HF_qa import answer_question


def run_all(review_text, question):
    return {
        "📊 감성 분석": analyze_sentiment(review_text),
        "🎭 장르 분류": classify_genre(review_text),
        "📝 요약": summarize(review_text),
        "💡 QA": answer_question(review_text, question)
    }


with gr.Blocks(theme=gr.themes.Soft(), title="BookLens AI") as app:

    gr.Markdown("# 📚 BookLens AI\n한국어 도서 리뷰 멀티태스크 분석기")

    with gr.Row():
        with gr.Column(scale=2):
            review = gr.Textbox(lines=6, label="📖 리뷰 입력")
            question = gr.Textbox(label="❓ 질문")
            btn = gr.Button("🚀 분석 실행", variant="primary")

        with gr.Column(scale=3):
            output = gr.JSON(label="📊 결과")

    btn.click(run_all, inputs=[review, question], outputs=output)

    gr.Markdown("## 💡 예시")

    gr.Examples(
        examples=[
            ["이 책은 세계관이 독특하고 몰입감이 뛰어나다.", "이 책의 장점은?"],
            ["결말이 너무 급하게 끝난 느낌이다.", "단점은?"],
            ["문장이 아름답고 감정 묘사가 뛰어나다.", "장르는?"]
        ],
        inputs=[review, question]
    )

app.launch()