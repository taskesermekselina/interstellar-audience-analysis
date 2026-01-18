import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV yolu (processed klasörü!)
df = pd.read_csv("data/processed/aspect_sentiment.csv")

# Aspect + sentiment bazlı pivot tablo
pivot = df.pivot_table(
    index="aspect",
    columns="sentiment",
    values="count",
    aggfunc="sum",
    fill_value=0
)

# Oranları hesapla
ratio_df = pivot.div(pivot.sum(axis=1), axis=0)

# Grafik
x = np.arange(len(ratio_df.index))
width = 0.25

plt.figure()
plt.bar(x - width, ratio_df.get("positive", 0), width, label="Positive")
plt.bar(x, ratio_df.get("neutral", 0), width, label="Neutral")
plt.bar(x + width, ratio_df.get("negative", 0), width, label="Negative")

plt.xticks(x, ratio_df.index, rotation=45)
plt.ylabel("Ratio")
plt.title("Aspect-Based Sentiment Distribution")
plt.legend()
plt.tight_layout()
plt.show()
