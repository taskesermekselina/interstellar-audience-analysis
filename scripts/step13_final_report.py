import pandas as pd

summary = pd.read_csv("data/processed/cluster_summary.csv")

# Segment isimleri
segment_names = {
    0: "Anlamak İsteyenler",
    1: "Fanlar / Duygusal İzleyiciler",
    2: "Bilim Meraklıları",
    3: "Video Tüketicileri"
}

summary["segment"] = summary["cluster"].map(segment_names)

summary.to_csv("data/processed/cluster_final_report.csv", index=False)
print(summary)
