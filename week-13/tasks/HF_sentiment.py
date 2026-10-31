from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="beomi/KcELECTRA-base"
)

def analyze_sentiment(text):
    return sentiment_pipeline(text)[0]