import pandas as pd

# YouTube cluster dosyası
df = pd.read_csv("data/processed/youtube_comments_clustered.csv")

# IMDb rating/votes
imdb = pd.read_csv("data/processed/imdb_rating.csv")

# imdbVotes içindeki virgülü kaldır ve int'e çevir
imdb_votes = int(imdb["imdbVotes"].iloc[0].replace(",", ""))
imdb_rating = float(imdb["imdbRating"].iloc[0])

# Cluster sayısını hesapla
cluster_counts = df["cluster"].value_counts().sort_index()

total_comments = len(df)

summary = pd.DataFrame({
    "cluster": cluster_counts.index,
    "comment_count": cluster_counts.values,
})

summary["comment_ratio"] = summary["comment_count"] / total_comments

# Her cluster için "ağırlık"
summary["cluster_weight"] = summary["comment_ratio"] * imdb_votes

summary["imdb_rating"] = imdb_rating

# Dosyaya kaydet
summary.to_csv("data/processed/cluster_summary.csv", index=False)

print(summary)
