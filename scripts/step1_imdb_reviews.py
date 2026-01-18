
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import re

# IMDb ID for Interstellar
IMDB_ID = "tt0816692"
BASE_URL = f"https://www.imdb.com/title/{IMDB_ID}/reviews"

def get_reviews():
    # Headers to mimic a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    # URL with parameters to get spoilers and sort by helpfulness
    params = {
        "spoiler": "hide", 
        "sort": "helpfulnessScore", 
        "dir": "desc", 
        "ratingFilter": "0" 
    }

    print(f"Fetching reviews from {BASE_URL}...")
    
    # Use session to persist cookies
    session = requests.Session()
    response = session.get(BASE_URL, headers=headers, params=params)
    
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    
    # Try multiple selectors for review containers
    selectors = [
        ("div", "lister-item-content")
    ]
    
    review_containers = []
    for tag, cls in selectors:
        review_containers = soup.find_all(tag, class_=cls)
        if review_containers:
            print(f"Found {len(review_containers)} reviews using selector: {tag}.{cls}")
            break
            
    if not review_containers:
        print("Debugging: Saving HTML to debug_imdb.html")
        with open("debug_imdb.html", "wb") as f:
            f.write(response.content)

    
    reviews_data = []
    
    # Select review containers using the new 'user-review-item' class
    # Use generic 'article' or 'div' to be safe, searching for class substring
    review_containers = soup.find_all(lambda tag: tag.name in ['div', 'article'] and tag.get('class') and any('user-review-item' in c for c in tag.get('class')))

    print(f"Found {len(review_containers)} reviews using selector 'user-review-item'")

    if not review_containers:
        print("❌ No reviews found using 'user-review-item'. Checking for fallback...")
        # Fallback dump of first few divs
        divs = soup.find_all("div")
        if divs:
            print(f"DEBUG: First div classes: {divs[0].get('class')}")
        return []

    for container in review_containers:
        try:
            # Title: h3 class 'ipc-title__text'
            title_tag = container.find("h3", class_=lambda x: x and "ipc-title__text" in x)
            title = title_tag.get_text(strip=True) if title_tag else "No Title"

            # Content: div class 'ipc-html-content'
            content_tag = container.find("div", class_=lambda x: x and "ipc-html-content" in x)
            content = content_tag.get_text(strip=True) if content_tag else ""

            # Rating: look for '10/10' text or star icon
            # Usually in a span with 'ipc-rating-star'
            rating_tag = container.find(class_=lambda x: x and "ipc-rating-star" in x)
            rating_text = rating_tag.get_text(strip=True) if rating_tag else None
            
            rating = None
            if rating_text:
                # rating_text might be "10/10" or "9"
                match = re.search(r"(\d+)", rating_text)
                if match:
                    rating = match.group(1)

            # Date & User:
            # These are often found in a metadata list ul.ipc-inline-list
            date = "Unknown Date"
            user = "Unknown User"
            
            # Metadata list items usually contain Date and User
            metadata_items = container.find_all("li", class_=lambda x: x and "ipc-inline-list__item" in x)
            for item in metadata_items:
                text = item.get_text(strip=True)
                # Heuristic: Date usually contains comma and 4-digit year (e.g., "Nov 7, 2014")
                # Or simplistic check for year
                if re.search(r"\b20\d{2}\b", text):
                    date = text
                # Heuristic: User usually has a link inside the list item
                elif item.find("a"):
                    # Exclude 'Helpful' links if any
                    if "Helpful" not in text:
                        user = text

            reviews_data.append({
                "title": title,
                "rating": rating,
                "user": user,
                "date": date,
                "review": content
            })
            
        except Exception as e:
            print(f"Error parsing review: {e}")
            continue

    return reviews_data

def main():
    reviews = get_reviews()
    
    if reviews:
        df = pd.DataFrame(reviews)
        output_path = "data/raw/imdb_reviews.csv"
        df.to_csv(output_path, index=False, encoding="utf-8")
        print(f"\n✅ Successfully saved {len(df)} reviews to {output_path}")
        print(df.head())
    else:
        print("❌ No reviews found.")

if __name__ == "__main__":
    main()
