import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# ========== VERİLER ==========
df = pd.read_csv("data/processed/youtube_comments_clustered.csv")
embeddings = np.load("data/processed/comment_embeddings.npy")

# güvenlik kontrolü
assert len(df) == embeddings.shape[0], "Embedding sayısı ile yorum sayısı uyuşmuyor!"

clusters = df["cluster"].values

# ========== PCA ==========
pca = PCA(n_components=2, random_state=42)
X_2d = pca.fit_transform(embeddings)

# ========== GÖRSEL ==========
plt.figure(figsize=(10,7))
scatter = plt.scatter(
    X_2d[:, 0],
    X_2d[:, 1],
    c=clusters,
    s=8,
    alpha=0.6
)

plt.xlabel("PCA-1")
plt.ylabel("PCA-2")
plt.title("Interstellar – İzleyici Yorumlarının Küme Dağılımı (Scatter)")
plt.colorbar(scatter, label="Küme ID")

plt.tight_layout()
plt.savefig("outputs/cluster_scatter.png")
plt.close()

print("✅ Kümeleme scatter grafiği başarıyla oluşturuldu")
