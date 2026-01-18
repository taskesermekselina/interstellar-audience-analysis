
import requests
from bs4 import BeautifulSoup

IMDB_ID = "tt0816692"
URL = f"https://www.imdb.com/title/{IMDB_ID}/reviews"

def find_pagination_key():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    print(f"Fetching {URL}...")
    res = requests.get(URL, headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")
    
    # Check for Load More button
    # Usually div.load-more-data or button.ipl-load-more__button
    load_more = soup.find(class_="load-more-data")
    if load_more:
        print("Found 'load-more-data' container.")
        key = load_more.get("data-key")
        print(f"Data Key: {key}")
        return
        
    print("Could not find standard 'load-more-data'. Searching for 'data-key' everywhere...")
    tags = soup.find_all(attrs={"data-key": True})
    for t in tags:
        print(f"Tag: {t.name}, Class: {t.get('class')}, Key: {t.get('data-key')}")

if __name__ == "__main__":
    find_pagination_key()
