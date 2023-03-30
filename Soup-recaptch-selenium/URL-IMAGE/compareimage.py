
"""import cv2
import numpy as np
image1=cv2.imread("first.jpg")
image2=cv2.imread("product.jpg")
if image1.shape==image2.shape:
    print("the image are same")
    difference=cv2.subtract(image1,image2)

cv2.imshow("image1",image1)
cv2.imshow('image2',image2)
cv2.waitKey(0)
cv2.destroyWindow()"""
"""from PIL import Image
import imagehash
hash0 = imagehash.average_hash(Image.open('first.jpg'))
hash1 = imagehash.average_hash(Image.open('local-filename.jpg'))
cutoff = 5

if hash0 - hash1 < cutoff:
  print('images are similar')
else:
  print('images are not similar')"""
from PIL import Image
import requests
from io import BytesIO
from PIL import Image
import imagehash
import cv2

response = requests.get("https://cdn.raptorsupplies.com/pub/media/catalog/product/lovejoy-68514445872.png")
res=requests.get("https://staging.raptorsupplies.com/pub/media/catalog/product/lovejoy-68514445872.png")
img = Image.open(BytesIO(response.content))
img1= Image.open(BytesIO(res.content))
img.show()
img1.show()
cv2.waitKey(1)
if img==img1:
    print("image is same")
else:
    print("image is not same")




