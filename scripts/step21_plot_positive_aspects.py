import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/aspect_summary.csv")

df = df.sort_values("positive", ascending=False)

plt.figure(figsize=(10,6))
plt.barh(df["aspect"], df["positive"])
plt.xlabel("Pozitif Yorum Oranı")
plt.title("Interstellar – İzleyicilerin Beğendiği Unsurlar")
plt.tight_layout()

plt.savefig("outputs/positive_aspects.png")
plt.close()

print("✅ Beğenilen unsurlar grafiği oluşturuldu")
