import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# =========================
# VERİ
# =========================
df = pd.read_csv("data/processed/comments_with_aspects.csv")

df = df[df["sentiment"].isin([0, 2])]
df["sentiment_label"] = df["sentiment"].map({0: "Negative", 2: "Positive"})

# =========================
# ASPECT SIRASI (SABİT)
# =========================
aspect_order = [
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

df["aspect"] = pd.Categorical(
    df["aspect"],
    categories=aspect_order,
    ordered=True
)

# =========================
# GROUP
# =========================
grouped = (
    df.groupby(["cluster", "aspect", "sentiment_label"])
    .size()
    .reset_index(name="count")
)

grouped["ratio"] = grouped.groupby(
    ["cluster", "aspect"]
)["count"].transform(lambda x: x / x.sum())

# =========================
# GRAFİK
# =========================
sns.set(style="whitegrid")

g = sns.catplot(
    data=grouped,
    kind="bar",
    x="aspect",
    y="ratio",
    hue="sentiment_label",
    col="cluster",
    col_wrap=2,
    height=5,
    aspect=1.6,
    order=aspect_order,
    palette={"Positive": "#2ecc71", "Negative": "#e74c3c"}
)

g.set_titles("Cluster {col_name}")
g.set_axis_labels("Film Unsuru", "Oran")

# 🔴 ASIL DÜZELTME BURASI
for ax in g.axes.flatten():
    ax.set_xticks(range(len(aspect_order)))
    ax.set_xticklabels(
        aspect_order,
        rotation=45,
        ha="right",
        fontsize=9
    )

plt.subplots_adjust(top=0.88, bottom=0.35)
g.fig.suptitle(
    "Interstellar – Küme Bazlı Beğenilen ve Eleştirilen Film Unsurları",
    fontsize=14
)

plt.savefig(
    "outputs/cluster_positive_negative_aspects.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

print("✅ Etiketleri TAM görünen cluster × aspect grafiği oluşturuldu.")
