import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/comments_clean.csv")

# CountVectorizer ile kelime sayımı
vectorizer = CountVectorizer(stop_words="english", max_features=2000)
X = vectorizer.fit_transform(df["clean_text"])
words = vectorizer.get_feature_names_out()
counts = X.sum(axis=0).A1

word_freq = pd.DataFrame({"word": words, "count": counts})
word_freq = word_freq.sort_values("count", ascending=False).head(20)

# İzleme sebepleri grafiği
plt.figure(figsize=(12, 6))
plt.bar(word_freq["word"], word_freq["count"])
plt.title("Filmi İzleme Sebepleri (En Çok Geçen Kelimeler)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/watch_reasons.png")
plt.close()

print("İzleme sebepleri grafiğini kaydettim: outputs/watch_reasons.png")
