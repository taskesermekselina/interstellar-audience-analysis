import pandas as pd

# Örnek: daha önce üretilmiş aspect sentiment sonuçları
# Eğer senin projende bu zaten bir DataFrame ise, buraya bağlayacağız
data = [
    {"aspect": "Story", "sentiment": "positive", "count": 120},
    {"aspect": "Story", "sentiment": "negative", "count": 45},
    {"aspect": "Visuals", "sentiment": "positive", "count": 200},
    {"aspect": "Visuals", "sentiment": "negative", "count": 30},
    {"aspect": "Music", "sentiment": "neutral", "count": 50},
]

df = pd.DataFrame(data)

# KAYIT
df.to_csv("data/processed/aspect_sentiment.csv", index=False)

print("✅ aspect_sentiment.csv başarıyla oluşturuldu")
