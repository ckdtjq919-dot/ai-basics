from datasets import load_dataset
from transformers import pipeline

dataset = load_dataset("nsmc", split="test[:100]")

model1 = pipeline("sentiment-analysis", model="beomi/KcELECTRA-base")
model2 = pipeline("sentiment-analysis", model="klue/roberta-base")


def eval_model(model):
    correct = 0

    for d in dataset:
        pred = model(d["document"])[0]["label"]
        if pred in str(d["label"]):
            correct += 1

    return correct / len(dataset)


print("Model1:", eval_model(model1))
print("Model2:", eval_model(model2))