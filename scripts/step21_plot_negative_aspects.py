import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/aspect_summary.csv")

df = df.sort_values("negative", ascending=False)

plt.figure(figsize=(10,6))
plt.barh(df["aspect"], df["negative"])
plt.xlabel("Negatif Yorum Oranı")
plt.title("Interstellar – İzleyicilerin Eleştirdiği Unsurlar")
plt.tight_layout()

plt.savefig("outputs/negative_aspects.png")
plt.close()

print("✅ Eleştirilen unsurlar grafiği oluşturuldu")
