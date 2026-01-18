
from bs4 import BeautifulSoup
import json

def dump_next_data():
    try:
        with open("debug_page.html", "r", encoding="utf-8") as f:
            html = f.read()
    except Exception as e:
        print(f"Error: {e}")
        return

    soup = BeautifulSoup(html, "html.parser")
    next_data = soup.find("script", id="__NEXT_DATA__")
    
    if next_data:
        try:
            data = json.loads(next_data.string)
            with open("debug_next_data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            print("Saved __NEXT_DATA__ to debug_next_data.json")
        except:
            print("Failed to parse JSON")
    else:
        print("__NEXT_DATA__ not found")

if __name__ == "__main__":
    dump_next_data()
