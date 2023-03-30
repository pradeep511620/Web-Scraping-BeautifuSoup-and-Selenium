import io
import cv2
import numpy as np
from PIL import Image
import imagehash
import PIL
from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup
import requests
from PIL import Image
from cv2.cv2 import reduce
from urllib3.util import Url
import urllib.request
url="https://staging.raptorsupplies.com/pd/lovejoy/68514428875"


page=requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")
url2="https://cdn.raptorsupplies.com/pub/media/catalog/product/LOVEJOY-68514428875-GR0095623.JPG"
response = requests.get(url2)
image_bytes = io.BytesIO(response.content)
print(image_bytes)
img = PIL.Image.open(image_bytes)
img.show()
print(img)

urllib.request.urlretrieve(url2, "first.jpg")
for link in soup.find_all('img',class_="xzoom center-block"):
    links=link.get("xoriginal")
    print(links)
    urllib.request.urlretrieve(links,"product.jpg")

    """response1 = requests.get(links)
    image_bytes1 = io.BytesIO(response1.content)
    img1 = PIL.Image.open(image_bytes1)
    print(image_bytes1)
    print(img1)"""


    """hash0 = imagehash.average_hash(Image.open(links))
    hash1 = imagehash.average_hash(Image.open(url2))
    cutoff = 5

    if hash0 - hash1 < cutoff:
        print('images are similar')
    else:
        print('images are not similar')"""