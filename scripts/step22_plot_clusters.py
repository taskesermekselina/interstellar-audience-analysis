import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# VERİYİ YÜKLE
# ===============================
df = pd.read_csv("data/processed/youtube_comments_clustered.csv")

# ===============================
# KÜME DAĞILIMI
# ===============================
cluster_counts = (
    df.groupby("cluster")
    .size()
    .reset_index(name="comment_count")
    .sort_values("comment_count", ascending=False)
)

# ===============================
# GRAFİK
# ===============================
plt.figure(figsize=(10,6))
plt.bar(cluster_counts["cluster"].astype(str),
        cluster_counts["comment_count"])

plt.xlabel("Küme ID")
plt.ylabel("Yorum Sayısı")
plt.title("Interstellar – İzleyici Yorumlarının Küme Dağılımı")
plt.tight_layout()

# ===============================
# KAYDET
# ===============================
plt.savefig("outputs/cluster_distribution.png")
plt.close()

print("✅ Küme dağılım grafiği oluşturuldu → outputs/cluster_distribution.png")
