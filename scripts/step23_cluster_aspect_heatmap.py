import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ========== VERİ ==========
df = pd.read_csv("data/processed/comments_with_aspects.csv")

# cluster + aspect sayım tablosu
pivot = (
    df
    .groupby(["cluster", "aspect"])
    .size()
    .reset_index(name="count")
)

# yüzdeye çevir (her cluster kendi içinde)
pivot["ratio"] = pivot.groupby("cluster")["count"].transform(lambda x: x / x.sum())

heatmap_df = pivot.pivot(
    index="cluster",
    columns="aspect",
    values="ratio"
).fillna(0)

# ========== GÖRSEL ==========
plt.figure(figsize=(14,6))
sns.heatmap(
    heatmap_df,
    annot=True,
    fmt=".2f",
    cmap="YlOrRd"
)

plt.title("Interstellar – İzleyici Kümeleri ve Odaklandıkları Film Unsurları")
plt.xlabel("Film Unsuru (Aspect)")
plt.ylabel("İzleyici Kümesi")

plt.tight_layout()
plt.savefig("outputs/cluster_aspect_heatmap.png")
plt.close()

print("✅ Cluster × Aspect heatmap oluşturuldu")
