import requests as re
import os
from datetime import datetime

url = "https://thispersondoesnotexist.com"
save_dir = "."
    
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
}

def fetch_image():
        
    response = re.get(url, headers=headers, timeout=10)
    response.raise_for_status()
        
    filename = os.path.join(save_dir, "scraped_image.jpg")
        
    with open(filename, "wb") as f:
        f.write(response.content)

    print("Fetched image successfully!")
    return filename
