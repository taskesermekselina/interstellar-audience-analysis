import pandas as pd
import re

# Veri yükle
df = pd.read_csv("data/raw/youtube_comments_raw.csv")

# Boş yorumları at
df = df.dropna(subset=["comment_text"])

# Küçük harfe çevir
df["clean_text"] = df["comment_text"].str.lower()

# Linkleri sil
df["clean_text"] = df["clean_text"].apply(
    lambda x: re.sub(r"http\S+", "", x)
)

# Emojiler ve özel karakterleri temizle
df["clean_text"] = df["clean_text"].apply(
    lambda x: re.sub(r"[^a-z\s]", "", x)
)

# Fazla boşlukları temizle
df["clean_text"] = df["clean_text"].apply(
    lambda x: re.sub(r"\s+", " ", x).strip()
)

# Çok kısa yorumları çıkar (anlamsız gürültü)
df = df[df["clean_text"].str.split().str.len() >= 4]

# Gerekli kolonları koru
df = df[["video_id", "clean_text", "like_count", "published_at", "is_reply"]]

# Kaydet
df.to_csv("data/processed/comments_clean.csv", index=False)

print("✅ Temizleme tamamlandı")
print("Kalan yorum sayısı:", df.shape[0])
