import requests
import pandas as pd

# ⭐ Buraya kendi OMDb API key'inizi yazın
API_KEY = "391a0a6f"
IMDB_ID = "tt0816692"

url = f"http://www.omdbapi.com/?i={IMDB_ID}&apikey={API_KEY}"
data = requests.get(url).json()

rating = data.get("imdbRating")
votes = data.get("imdbVotes")

print("IMDb Rating:", rating)
print("IMDb Votes:", votes)

df = pd.DataFrame([{
    "imdbRating": rating,
    "imdbVotes": votes
}])

df.to_csv("data/processed/imdb_rating.csv", index=False)
print("Saved imdb rating/votes to data/processed/imdb_rating.csv")
