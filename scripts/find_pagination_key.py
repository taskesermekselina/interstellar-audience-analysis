
from bs4 import BeautifulSoup

def find_key():
    try:
        with open("debug_page.html", "r", encoding="utf-8") as f:
            html = f.read()
    except Exception as e:
        print(f"Error: {e}")
        return

    soup = BeautifulSoup(html, "html.parser")
    pagination_div = soup.find("div", {"data-testid": "tturv-pagination"})
    
    if pagination_div:
        print("Found pagination div!")
        print(pagination_div.prettify())
        
        # Check for data-key in children
        key_elem = pagination_div.find(attrs={"data-key": True})
        if key_elem:
            print(f"\n✅ Found Data Key: {key_elem['data-key']}")
        else:
            print("\n❌ No data-key found in pagination div children.")
    else:
        print("pagination div not found.")

if __name__ == "__main__":
    find_key()
