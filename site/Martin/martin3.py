import requests
from bs4 import BeautifulSoup

url = "https://www.martinsprocket.com/view/products/product-search?Website_Code=SP1"
soup = BeautifulSoup(requests.get(url).text, features="xml").find_all("a")

keys = [f"https://www.martinsprocket.com/view/products/product-search?Website_Code=SP1/{k.getText()}" for k in soup]
print("\n".join(keys))

# url = "https://chromedriver.storage.googleapis.com/?delimiter=/&prefix=97.0.4692.71/"
# soup = BeautifulSoup(requests.get(url).text, features="xml").find_all("Key")
# keys = [f"https://chromedriver.storage.googleapis.com/{k.getText()}" for k in soup]