import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

df = pd.read_csv("data/processed/youtube_comments_clustered.csv")

def get_top_keywords(cluster_df, n=15):
    vectorizer = TfidfVectorizer(max_features=2000, stop_words='english')
    X = vectorizer.fit_transform(cluster_df['clean_text'])
    feature_names = vectorizer.get_feature_names_out()
    mean_tfidf = np.mean(X.toarray(), axis=0)
    top_indices = mean_tfidf.argsort()[-n:][::-1]
    top_words = [(feature_names[i], mean_tfidf[i]) for i in top_indices]
    return top_words

for cluster_id in sorted(df['cluster'].unique()):
    cluster_df = df[df['cluster'] == cluster_id]
    print(f"\n\n====================")
    print(f"Cluster {cluster_id} - Count: {len(cluster_df)}")
    print(f"====================")

    # Örnek yorumlar
    print("\nÖrnek Yorumlar:")
    for comment in cluster_df['clean_text'].head(8).tolist():
        print(f"- {comment}")

    # TF-IDF ile top kelimeler
    print("\nTop Kelimeler (TF-IDF):")
    keywords = get_top_keywords(cluster_df)
    print(", ".join([w for w, _ in keywords]))
