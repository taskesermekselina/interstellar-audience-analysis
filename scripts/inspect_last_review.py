
from bs4 import BeautifulSoup

def inspect_reviews():
    try:
        with open("debug_page.html", "r", encoding="utf-8") as f:
            html = f.read()
    except Exception as e:
        print(f"Error: {e}")
        return

    soup = BeautifulSoup(html, "html.parser")
    # Use the selector we found earlier: class containing 'user-review-item'
    reviews = soup.find_all(lambda tag: tag.name in ['div', 'article'] and tag.get('class') and any('user-review-item' in c for c in tag.get('class')))
    
    print(f"Found {len(reviews)} reviews.")
    
    if reviews:
        last_review = reviews[-1]
        print("\n--- Last Review Attributes ---")
        print(last_review.attrs)
        
        # Check parents for data-key
        parent = last_review.parent
        print("\n--- Parent Attributes ---")
        print(parent.attrs)
        
        # Check specific 'load-more' candidates we might have missed
        # e.g. div with data-key at the bottom of the list
        print("\n--- Searching siblings after the last review ---")
        for sib in last_review.next_siblings:
            if sib.name:
                print(f"Sibling: {sib.name} | Class: {sib.get('class')} | Attrs: {sib.attrs}")

if __name__ == "__main__":
    inspect_reviews()
