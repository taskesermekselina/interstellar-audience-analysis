
from bs4 import BeautifulSoup

def analyze_ipc_structure():
    try:
        with open("debug_imdb.html", "r", encoding="utf-8") as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading; {e}")
        return

    soup = BeautifulSoup(html, "html.parser")
    
    # helper to print element info
    def print_el(name, el):
        print(f"[{name}] {el.name} | classes: {el.get('class')} | text: {el.get_text()[:40]}...")

    # Find the content blocks
    contents = soup.find_all(class_=lambda x: x and "ipc-html-content" in x)
    print(f"Found {len(contents)} content blocks.")
    
    if contents:
        sample = contents[0]
        print("\n--- SAMPLE CONTENT BLOCK ---")
        print_el("Content", sample)
        
        # Traverse up to find the card container
        parent = sample.parent
        for _ in range(5):
            if parent:
                print_el(f"Parent ->", parent)
                # Check for sibling that might be title or rating
                if parent.name == "div":
                    # Try to find a rating in this parent tree
                    rating = parent.find(string="10")
                    if rating:
                        print(f"  FOUND POTENTIAL RATING sibling: {rating}")
                parent = parent.parent
            else:
                break
                
    # Search for Title specifically (h3 is common for titles in lists)
    print("\n--- SEARCHING FOR TITLES ---")
    titles = soup.find_all("h3")
    for t in titles[:3]:
        print_el("H3 Title", t)

if __name__ == "__main__":
    analyze_ipc_structure()
