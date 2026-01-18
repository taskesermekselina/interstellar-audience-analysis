import os
import pandas as pd
from googleapiclient.discovery import build
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

VIDEO_IDS = [
    "j3DuONZb3Ik",
    "zSWdZVtXT7E",
    "BHsFzDON6pA",
    "qhW1HfSuPVQ"
]

youtube = build("youtube", "v3", developerKey=API_KEY)

all_comments = []

def get_replies(parent_id, video_id):
    replies = []
    request = youtube.comments().list(
        part="snippet",
        parentId=parent_id,
        maxResults=100,
        textFormat="plainText"
    )
    while request:
        response = request.execute()
        for item in response["items"]:
            s = item["snippet"]
            replies.append({
                "video_id": video_id,
                "comment_id": item["id"],
                "comment_text": s["textDisplay"],
                "like_count": s["likeCount"],
                "published_at": s["publishedAt"],
                "is_reply": 1
            })
        request = youtube.comments().list_next(request, response)
    return replies


for video_id in VIDEO_IDS:
    print(f"\n➡ Ana yorumlar çekiliyor: {video_id}")
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText",
        order="relevance"
    )

    while request:
        response = request.execute()

        for item in tqdm(response["items"]):
            top = item["snippet"]["topLevelComment"]["snippet"]
            comment_id = item["snippet"]["topLevelComment"]["id"]

            all_comments.append({
                "video_id": video_id,
                "comment_id": comment_id,
                "comment_text": top["textDisplay"],
                "like_count": top["likeCount"],
                "published_at": top["publishedAt"],
                "is_reply": 0
            })

            reply_count = item["snippet"]["totalReplyCount"]
            if reply_count > 0:
                replies = get_replies(comment_id, video_id)
                all_comments.extend(replies)

        request = youtube.commentThreads().list_next(request, response)

df = pd.DataFrame(all_comments)
df.to_csv("data/raw/youtube_comments_raw.csv", index=False, encoding="utf-8")

print("\n✅ Toplam çekilen yorum + reply sayısı:", len(df))
print(df["is_reply"].value_counts())
