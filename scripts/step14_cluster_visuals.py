import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/cluster_final_report.csv")

# Pasta grafiği (Cluster dağılımı)
plt.figure(figsize=(8, 8))
plt.pie(df["comment_count"], labels=df["segment"], autopct="%1.1f%%")
plt.title("Cluster Dağılımı (Yorum Oranları)")
plt.savefig("outputs/cluster_distribution_pie.png")
plt.close()

# Bar grafiği (Cluster ağırlıkları)
plt.figure(figsize=(10, 6))
plt.bar(df["segment"], df["cluster_weight"])
plt.title("Cluster Ağırlıkları")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig("outputs/cluster_weight_bar.png")
plt.close()

print("Cluster grafiklerini kaydettim: outputs/cluster_distribution_pie.png, outputs/cluster_weight_bar.png")
