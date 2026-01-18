import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt

# 1) Veri yükle
df = pd.read_csv("data/processed/youtube_comments_clustered.csv")

# 2) Sentiment model
model_name = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    outputs = model(**inputs)
    scores = outputs.logits.detach().numpy()[0]
    probs = np.exp(scores) / np.exp(scores).sum()
    label = np.argmax(probs)
    return label  # 0=negative, 1=neutral, 2=positive

# 3) sentiment ekle (örnek olarak ilk 5000 yorum)
df = df.head(5000)  # hız için (dilersen tümünü kullanabiliriz)
df["sentiment"] = df["clean_text"].apply(predict_sentiment)

# 4) her cluster için pozitif/negatif temalar
stopwords = ["movie","film","video","like","just","know","watch","watched","good","really","one",
             "time","think","see","get","make","also","im","ive","would","could","still","well",
             "thing","things","even","go","goes","much","many","us","youre","yeah","oh","lol",
             "wow","thanks","thank","u","ur","gonna","got","doesnt","didnt","dont","cant","did","didnt"]

vectorizer = TfidfVectorizer(stop_words="english", max_features=2000, ngram_range=(1,2))

for cluster in sorted(df["cluster"].unique()):
    cluster_df = df[df["cluster"] == cluster]

    for sentiment_label, sentiment_name in [(2, "positive"), (0, "negative")]:
        texts = cluster_df[cluster_df["sentiment"] == sentiment_label]["clean_text"]
        if len(texts) < 10:
            continue

        X = vectorizer.fit_transform(texts)
        feature_names = vectorizer.get_feature_names_out()
        sums = X.sum(axis=0).A1
        terms = list(zip(feature_names, sums))
        terms_sorted = sorted(terms, key=lambda x: x[1], reverse=True)
        top_terms = [t for t in terms_sorted if t[0] not in stopwords][:12]

        words = [t[0] for t in top_terms]
        scores = [t[1] for t in top_terms]

        plt.figure(figsize=(10,6))
        plt.bar(words, scores)
        plt.title(f"Cluster {cluster} - {sentiment_name} themes")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"outputs/cluster_{cluster}_{sentiment_name}_themes.png")
        plt.close()

print("Beğenilen / Beğenilmeyen temaları kaydettim.")
