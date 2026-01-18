
from bs4 import BeautifulSoup
import re
import json

def analyze():
    try:
        with open("debug_page.html", "r", encoding="utf-8") as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    soup = BeautifulSoup(html, "html.parser")
    
    # 1. Look for __NEXT_DATA__
    next_data = soup.find("script", id="__NEXT_DATA__")
    if next_data:
        print("✅ Found __NEXT_DATA__ script!")
        try:
            data = json.loads(next_data.string)
            # Recursively search for 'paginationKey' or 'token' in the JSON
            def find_keys(obj, target_key):
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        if target_key in k.lower():
                            print(f"Found potential key in JSON: {k} = {str(v)[:50]}...")
                        find_keys(v, target_key)
                elif isinstance(obj, list):
                    for item in obj:
                        find_keys(item, target_key)
            
            print("Searching JSON for 'cursor', 'token', 'key'...")
            find_keys(data, "cursor")
            find_keys(data, "token")
            find_keys(data, "key")
            find_keys(data, "pagination")
        except:
            print("Failed to parse __NEXT_DATA__ JSON.")
    else:
        print("❌ __NEXT_DATA__ not found.")

    # 2. Look for all elements with 'data-key'
    print("\nSearching for elements with 'data-key'...")
    data_keys = soup.find_all(attrs={"data-key": True})
    for el in data_keys:
        print(f"Element: {el.name} | Class: {el.get('class')} | data-key: {el['data-key'][:50]}")

    # 3. Look for 'Load More' button explicitly
    print("\nSearching for 'Load More' text...")
    buttons = soup.find_all(string=re.compile("Load More", re.IGNORECASE))
    for b in buttons:
        print(f"Button Text: {b} | Parent: {b.parent.name} {b.parent.get('class')}")

if __name__ == "__main__":
    analyze()
