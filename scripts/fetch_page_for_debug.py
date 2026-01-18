
import requests

url = "https://www.imdb.com/title/tt0816692/reviews"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

print(f"Fetching {url}...")
try:
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    with open("debug_page.html", "wb") as f:
        f.write(res.content)
    print("Saved to debug_page.html")
except Exception as e:
    print(f"Error: {e}")
