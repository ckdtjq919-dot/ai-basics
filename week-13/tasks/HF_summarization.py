from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="gogamza/kobart-summarization"
)

def summarize(text):
    return summarizer(
        text,
        max_length=80,
        min_length=20,
        do_sample=False
    )[0]["summary_text"]