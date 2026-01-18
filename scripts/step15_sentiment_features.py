import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Yorumları yükle
df = pd.read_csv("data/processed/comments_clean.csv")

# 1) Basit sentiment model (çok iyi olmasa da iş görür)
# Burada IMDb rating yok, yorumlar üzerinden otomatik sınıflandırma yapacağız.
# Eğer çok doğru sonuç istersen, HuggingFace gibi bir model kullanmalısın.

# Örnek olarak "good, love, amazing" gibi kelimeler pozitif; "bad, boring" gibi kelimeler negatif kabul edilecek.
positive_words = ["good", "great", "love", "amazing", "best", "beautiful", "excellent", "awesome"]
negative_words = ["bad", "boring", "worst", "confusing", "hate", "terrible", "awful", "dumb"]

def sentiment_label(text):
    text = str(text).lower()
    pos = sum(word in text for word in positive_words)
    neg = sum(word in text for word in negative_words)
    if pos > neg:
        return "positive"
    elif neg > pos:
        return "negative"
    else:
        return "neutral"

df["sentiment"] = df["clean_text"].apply(sentiment_label)

# Pozitif ve negatif yorumlar
pos_texts = df[df["sentiment"] == "positive"]["clean_text"]
neg_texts = df[df["sentiment"] == "negative"]["clean_text"]

# TF-IDF ile en çok geçen kelimeleri çıkar
def top_tfidf_words(texts, n=15):
    vectorizer = TfidfVectorizer(stop_words="english", max_features=2000)
    X = vectorizer.fit_transform(texts)
    sums = X.sum(axis=0)
    words = vectorizer.get_feature_names_out()
    data = [(words[i], sums[0, i]) for i in range(len(words))]
    data.sort(key=lambda x: x[1], reverse=True)
    return data[:n]

pos_top = top_tfidf_words(pos_texts)
neg_top = top_tfidf_words(neg_texts)

# Grafik: pozitif
plt.figure(figsize=(10, 6))
plt.bar([x[0] for x in pos_top], [x[1] for x in pos_top])
plt.title("En Çok Beğenilen Unsurlar (Pozitif Yorumlar)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/liked_features.png")
plt.close()

# Grafik: negatif
plt.figure(figsize=(10, 6))
plt.bar([x[0] for x in neg_top], [x[1] for x in neg_top])
plt.title("En Çok Beğenilmeyen Unsurlar (Negatif Yorumlar)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/disliked_features.png")
plt.close()

print("Beğenilen/Beğenilmeyen grafiklerini kaydettim: outputs/liked_features.png, outputs/disliked_features.png")
