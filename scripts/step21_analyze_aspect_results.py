import pandas as pd

# ===============================
# VERİYİ OKU
# ===============================
df = pd.read_csv("data/processed/aspect_sentiment.csv")

# Beklenen kolonlar:
# aspect | sentiment | count

# ===============================
# POZİTİF & NEGATİF AYIR
# ===============================
positive_df = df[df["sentiment"] == "positive"]
negative_df = df[df["sentiment"] == "negative"]

# ===============================
# EN ÇOK ÖNE ÇIKANLAR
# ===============================
top_positive = positive_df.sort_values(by="count", ascending=False).head(3)
top_negative = negative_df.sort_values(by="count", ascending=False).head(3)

# ===============================
# SONUÇLARI YAZDIR
# ===============================
print("\n🎉 EN OLUMLU DEĞERLENDİRİLEN ASPECTLER:")
for _, row in top_positive.iterrows():
    print(f"- {row['aspect']} ({row['count']} pozitif yorum)")

print("\n⚠️ EN ÇOK ELEŞTİRİ ALAN ASPECTLER:")
for _, row in top_negative.iterrows():
    print(f"- {row['aspect']} ({row['count']} negatif yorum)")

# ===============================
# RAPOR İÇİN KAYIT
# ===============================
summary = pd.concat([
    top_positive.assign(type="Most Positive"),
    top_negative.assign(type="Most Negative")
])

summary.to_csv("data/processed/aspect_insights.csv", index=False)

print("\n✅ aspect_insights.csv oluşturuldu")
