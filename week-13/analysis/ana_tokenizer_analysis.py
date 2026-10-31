from transformers import AutoTokenizer, BertTokenizer

ko = AutoTokenizer.from_pretrained("beomi/KcELECTRA-base")
en = BertTokenizer.from_pretrained("bert-base-uncased")

texts = [
    "이 책은 정말 재미있었습니다",
    "결말이 아쉬웠다",
    "세계관이 독특하다",
    "몰입감이 좋다",
    "추천할 만하다"
]

for t in texts:
    print("\n문장:", t)
    print("KO:", ko.tokenize(t))
    print("EN:", en.tokenize(t))