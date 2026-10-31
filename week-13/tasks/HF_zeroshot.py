from transformers import pipeline

zero_shot = pipeline(
    "zero-shot-classification",
    model="joeddav/xlm-roberta-large-xnli"
)

labels = ["판타지", "로맨스", "추리", "SF", "에세이"]

def classify_genre(text):
    return zero_shot(
        text,
        labels,
        hypothesis_template="이 문장은 {} 장르에 관한 것이다."
    )