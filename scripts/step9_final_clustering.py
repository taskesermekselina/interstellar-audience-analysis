import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# Verileri yükle
df = pd.read_csv("data/processed/comments_clean.csv")
X = np.load("data/processed/comment_embeddings.npy")

# KMeans (K=4)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X)

# Küme etiketlerini ekle
df["cluster"] = clusters

# Kaydet
df.to_csv("data/processed/youtube_comments_clustered.csv", index=False)

print("✅ Nihai kümeleme tamamlandı")
print(df["cluster"].value_counts())
