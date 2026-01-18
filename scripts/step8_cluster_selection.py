import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Embedding yükle
X = np.load("data/processed/comment_embeddings.npy")

sse = []
silhouette_scores = []

K = range(2, 9)

print("🔄 Küme sayıları test ediliyor...")

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)

    sse.append(kmeans.inertia_)
    sil_score = silhouette_score(X, labels)
    silhouette_scores.append(sil_score)

    print(f"K={k} | Silhouette={sil_score:.4f}")

# Grafik
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot(K, sse, marker="o")
plt.title("Elbow Method (SSE)")
plt.xlabel("K")
plt.ylabel("SSE")

plt.subplot(1,2,2)
plt.plot(K, silhouette_scores, marker="o")
plt.title("Silhouette Score")
plt.xlabel("K")
plt.ylabel("Score")

plt.tight_layout()
plt.show()
