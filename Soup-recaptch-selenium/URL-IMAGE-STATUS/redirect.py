import urllib.request
import requests
from PIL import Image
from hurry.filesize import size
url ="https://cdn.raptorsupplies.com/pub/media/catalog/compressed/150x150/DAYTON-6XJ53.JPG"
image = Image.open(urllib.request.urlopen(url))
width, height = image.size
print (width,height)
size1=requests.get(url).content
print(len(size1))
