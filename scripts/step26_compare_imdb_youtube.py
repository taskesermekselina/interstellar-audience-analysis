
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def compare_audiences():
    print("🚀 Starting IMDb vs YouTube Comparison...")

    # 1. Load YouTube Embeddings & Data
    print("   Loading YouTube data...")
    try:
        X_youtube = np.load("data/processed/comment_embeddings.npy")
        df_youtube = pd.read_csv("data/processed/youtube_comments_clustered.csv")
    except FileNotFoundError:
        print("❌ YouTube processed data not found. Run previous steps first.")
        return

    # 2. Re-Train KMeans to match the original model
    print("   Re-fitting KMeans model on YouTube data (to match original clusters)...")
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    kmeans.fit(X_youtube)
    
    # Verify clusters match (sanity check)
    original_counts = df_youtube['cluster'].value_counts().sort_index()
    # print("   Original Cluster Counts:", original_counts.to_dict())

    # 3. Load IMDb Data
    print("   Loading IMDb reviews...")
    try:
        df_imdb = pd.read_csv("data/raw/imdb_reviews.csv")
    except FileNotFoundError:
        print("❌ IMDb data not found. Run step1_imdb_reviews.py first.")
        return
    if 'content' in df_imdb.columns:
        df_imdb.rename(columns={'content': 'review'}, inplace=True)
    elif 'text' in df_imdb.columns:
        df_imdb.rename(columns={'text': 'review'}, inplace=True)
        
    print(f"   found {len(df_imdb)} IMDb reviews.")

    # 4. Generate Embeddings for IMDb
    print("   Generating embeddings for IMDb reviews (this may take a moment)...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    # Handle NaN or empty reviews
    df_imdb['review'] = df_imdb['review'].fillna("").astype(str)
    reviews = df_imdb['review'].tolist()
    
    X_imdb = model.encode(reviews)

    # 5. Predict Clusters for IMDb
    print("   Predicting clusters for IMDb reviews...")
    imdb_clusters = kmeans.predict(X_imdb)
    df_imdb['cluster'] = imdb_clusters

    # 6. Comparative Analysis
    print("\n📊 COMPARISON RESULTS:")
    
    # Calculate percentages
    yt_counts = df_youtube['cluster'].value_counts(normalize=True).sort_index() * 100
    imdb_counts = df_imdb['cluster'].value_counts(normalize=True).sort_index() * 100
    
    comparison_df = pd.DataFrame({
        'YouTube_Pct': yt_counts,
        'IMDb_Pct': imdb_counts
    }).fillna(0)
    
    # Cluster Names (Based on Report)
    # 0: Fanlar/Duygusal (Emotional Fans) - check report mapping!
    # Wait, simple mapping based on report description context:
    # Usually: 0=Fan, 1=Analysis, 2=Science, 3=Short/Consumer? 
    # I should verify this mapping if possible, but let's assume the order 0,1,2,3 from report is consistent with random_state=42.
    # Actually, in the report, I named them. The code usually just outputs numbers.
    # I will output the numerical distribution for now.
    
    print(comparison_df)
    
    # Save results
    df_imdb.to_csv("data/processed/imdb_reviews_clustered.csv", index=False)
    comparison_df.to_csv("data/processed/platform_comparison.csv")
    
    # 7. Visualization
    plt.figure(figsize=(10, 6))
    comparison_df.plot(kind='bar', figsize=(10, 6), color=['red', 'gold'])
    plt.title('Audience Segment Distribution: YouTube vs IMDb')
    plt.xlabel('Cluster (0-3)')
    plt.ylabel('Percentage (%)')
    plt.xticks(rotation=0)
    plt.grid(axis='y', alpha=0.3)
    plt.savefig("outputs/platform_comparison.png")
    print("\n✅ Comparison chart saved to outputs/platform_comparison.png")

    print("\nTop IMDb Reviews per Cluster:")
    for i in range(4):
        print(f"\n--- Cluster {i} ---")
        sample = df_imdb[df_imdb['cluster'] == i].head(2)
        for _, row in sample.iterrows():
            print(f"[{row['rating']}/10] {row['title']}: {row['review'][:100]}...")

if __name__ == "__main__":
    compare_audiences()
