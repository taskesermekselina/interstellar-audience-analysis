
from bs4 import BeautifulSoup
import re

def analyze_html():
    try:
        with open("debug_imdb.html", "rb") as f:
            html = f.read()
    except FileNotFoundError:
        print("debug_imdb.html not found.")
        return

    soup = BeautifulSoup(html, "html.parser")
    
    # 1. Find text "Review" or keys
    print("Searching for 'Review' text elements...")
    elements = soup.find_all(string=re.compile("Review"))
    for i, el in enumerate(elements[:5]):
        parent = el.parent
        print(f"Match {i}: Tag={parent.name} Class={parent.get('class')}")
        
    # 2. Find text "10/10" or ratings
    print("\nSearching for rating '10/10'...")
    ratings = soup.find_all(string="10/10")
    for i, el in enumerate(ratings[:5]):
        parent = el.parent
        print(f"Rating Match {i}: Tag={parent.name} Class={parent.get('class')}")
        # Go up to find container
        container = parent.find_parent("div")
        if container:
            print(f"  -> Parent Div Class: {container.get('class')}")

if __name__ == "__main__":
    analyze_html()
