import os
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sentence_transformers import SentenceTransformer, util
import matplotlib.pyplot as plt
import numpy as np

# ======================================================
# KLASÖRLER
# ======================================================
os.makedirs("data/processed", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# ======================================================
# VERİ
# ======================================================
df = pd.read_csv("data/processed/youtube_comments_clustered.csv")

# hız için örnekleme (akademik olarak kabul edilebilir)
df = df.sample(6000, random_state=42).reset_index(drop=True)

# ======================================================
# ASPECT TANIMLARI (ANLAMSAL)
# ======================================================
aspects = [
    "story and plot",
    "acting and performances",
    "visual effects and CGI",
    "music and soundtrack",
    "science and physics",
    "emotional impact",
    "characters",
    "ending",
    "clarity and complexity",
    "directing and vision"
]

# ======================================================
# SEMANTIC MODEL (ASPECT EŞLEŞTİRME)
# ======================================================
st_model = SentenceTransformer("all-MiniLM-L6-v2")
aspect_embeddings = st_model.encode(aspects, convert_to_tensor=True)

# ======================================================
# SENTIMENT MODEL
# ======================================================
sent_model_name = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(sent_model_name)
sent_model = AutoModelForSequenceClassification.from_pretrained(sent_model_name)
sent_model.eval()

def predict_sentiment(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=128
    )
    with torch.no_grad():
        outputs = sent_model(**inputs)
    scores = outputs.logits[0]
    return int(torch.argmax(scores))  # 0=neg, 1=neu, 2=pos

# ======================================================
# ASPECT + SENTIMENT ATAMA
# ======================================================
assigned_aspect = []
assigned_sentiment = []

for text in df["clean_text"].astype(str):
    text_emb = st_model.encode(text, convert_to_tensor=True)
    similarity = util.cos_sim(text_emb, aspect_embeddings)[0]
    aspect_idx = int(torch.argmax(similarity))

    assigned_aspect.append(aspects[aspect_idx])
    assigned_sentiment.append(predict_sentiment(text))

df["aspect"] = assigned_aspect
df["sentiment"] = assigned_sentiment

df.to_csv("data/processed/comments_with_aspects.csv", index=False)

# ======================================================
# ASPECT ÖZET TABLOSU
# ======================================================
summary_rows = []

for aspect in aspects:
    sub = df[df["aspect"] == aspect]
    if len(sub) == 0:
        continue

    summary_rows.append({
        "aspect": aspect,
        "positive_ratio": (sub["sentiment"] == 2).mean(),
        "negative_ratio": (sub["sentiment"] == 0).mean(),
        "comment_count": len(sub)
    })

summary_df = pd.DataFrame(summary_rows)
summary_df.to_csv("data/processed/aspect_summary.csv", index=False)

# ======================================================
# GRAFİK (STACKED BAR)
# ======================================================
plt.figure(figsize=(13,6))

plt.bar(
    summary_df["aspect"],
    summary_df["positive_ratio"],
    label="Positive"
)

plt.bar(
    summary_df["aspect"],
    summary_df["negative_ratio"],
    bottom=summary_df["positive_ratio"],
    label="Negative"
)

plt.xticks(rotation=35, ha="right")
plt.ylabel("Ratio")
plt.title("Interstellar – Beğenilen ve Eleştirilen Film Unsurları (Aspect-Based)")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/aspect_sentiment.png")
plt.close()

print("✅ Step 19 tamamlandı: Aspect-based sentiment analizi üretildi.")
