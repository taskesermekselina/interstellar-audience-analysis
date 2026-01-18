import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# VERİ
# =========================
df = pd.read_csv("data/processed/comments_with_aspects.csv")

# Sadece POZİTİF yorumlar
df = df[df["sentiment"] == 2]

# =========================
# MOTİVASYON HARİTASI
# =========================
motivation_map = {
    "story and plot": "Story & Narrative",
    "ending": "Story & Narrative",

    "emotional impact": "Emotional Experience",
    "characters": "Emotional Experience",

    "science and physics": "Science & Philosophy",
    "clarity and complexity": "Science & Philosophy",

    "visual effects and CGI": "Cinematography",
    "directing and vision": "Cinematography",

    "music and soundtrack": "Music"
}

df["motivation"] = df["aspect"].map(motivation_map)

# Boş gelenleri çıkar
df = df.dropna(subset=["motivation"])

# =========================
# SAYIM
# =========================
motivation_counts = (
    df["motivation"]
    .value_counts()
    .reset_index()
)

motivation_counts.columns = ["Motivation", "Count"]

motivation_counts["Ratio"] = (
    motivation_counts["Count"] / motivation_counts["Count"].sum()
)

# =========================
# GRAFİK
# =========================
sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.barplot(
    data=motivation_counts,
    x="Motivation",
    y="Ratio"
)

plt.title("Interstellar – İzleyici Motivasyon Analizi", fontsize=14)
plt.xlabel("İzleme Motivasyonu")
plt.ylabel("Oran")
plt.xticks(rotation=30, ha="right")

plt.tight_layout()
plt.savefig(
    "outputs/viewer_motivation_analysis.png",
    dpi=300
)
plt.close()

# =========================
# CSV
# =========================
motivation_counts.to_csv(
    "outputs/viewer_motivation_analysis.csv",
    index=False
)

print("✅ İzleyici motivasyon analizi tamamlandı.")
