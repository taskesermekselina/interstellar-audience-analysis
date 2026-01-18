
import requests

def test_pagination():
    base_url = "https://www.imdb.com/title/tt0816692/reviews/_ajax"
    
    # This is the cursor we found in the JSON
    cursor = "g4xojermtizcsyyg7kwxrmryrhummazt3end56pkdpj3qflcneskid2zpertax674djrxslkahdqxuqgfkhkffq"
    
    params = {
        "ref_": "undefined",
        "paginationKey": cursor,
        "sort": "helpfulnessScore",
        "dir": "desc",
        "ratingFilter": "0"
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    print(f"Testing pagination with cursor: {cursor[:20]}...")
    try:
        res = requests.get(base_url, params=params, headers=headers)
        print(f"Status Code: {res.status_code}")
        print(f"Content Type: {res.headers.get('Content-Type')}")
        print(f"Response Length: {len(res.content)}")
        
        if res.status_code == 200:
            with open("debug_ajax_response.html", "wb") as f:
                f.write(res.content)
            print("Saved response to debug_ajax_response.html")
            
            # Check if we got new reviews
            if b"user-review-item" in res.content or b"review-container" in res.content:
                print("✅ Found review items in response!")
            else:
                print("⚠️ No review items found in response.")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_pagination()
