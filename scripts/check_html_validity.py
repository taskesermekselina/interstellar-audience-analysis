
from bs4 import BeautifulSoup

def check_structure():
    try:
        with open("debug_imdb.html", "r", encoding="utf-8") as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    soup = BeautifulSoup(html, "html.parser")
    print(f"Page Title: {soup.title.string if soup.title else 'No Title'}")
    
    # Check for likely block or error messages
    text = soup.get_text()[:1000]
    print(f"\nFirst 1000 chars of text:\n{text}")
    
    # Check for specific review container classes again used by new IMDb
    print("\nChecking for specific classes:")
    candidates = [
        "ipc-html-content", "sc-16ede01-0", "imdb-user-review-card", 
        "lister-item", "review-container"
    ]
    for c in candidates:
        found = soup.find_all(class_=lambda x: x and c in x)
        print(f"Class containing '{c}': {len(found)}")

if __name__ == "__main__":
    check_structure()
