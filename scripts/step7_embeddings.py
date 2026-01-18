import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
from tqdm import tqdm

# Veriyi yükle
df = pd.read_csv("data/processed/comments_clean.csv")

# Modeli yükle
model = SentenceTransformer("all-MiniLM-L6-v2")

texts = df["clean_text"].tolist()

embeddings = []

print("🔄 Embedding başlıyor...")

for text in tqdm(texts):
    emb = model.encode(text)
    embeddings.append(emb)

embeddings = np.array(embeddings)

# Kaydet
np.save("data/processed/comment_embeddings.npy", embeddings)

print("✅ Embedding tamamlandı")
print("Embedding shape:", embeddings.shape)
