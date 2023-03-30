
# from PIL import Image
# import pytesseract
#
# image = Image.open('C:/Users/ashish/PycharmProjects/pythonProject6/image/3m.png')
# print(type(image))
# # file = Image.open("/home/user/sample.png")
# custom_config = r'--psm 6'
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
#
# output = pytesseract.image_to_string(image, config=custom_config,lang='eng')
#
# print(output.strip(''))
###########################################################################################################
# import mysql.connector
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ritesh"
# )
# mycursor = mydb.cursor()
# from PIL import Image
# import cv2
# import pytesseract
# import os
# import numpy as np
#
#
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# indir = r'C:/Users/ashish/PycharmProjects/pythonProject6/image/photos/'
# for root, dirs, filenames in os.walk(indir):
#     for filename in filenames:
#         fname = filename
#         print('#####################################' + filename + '#####################################')
#         im = Image.open(indir + filename)
#         gray = cv2.cvtColor(np.float32(im), cv2.COLOR_RGB2GRAY)
#         im.show(gray)
#         text = pytesseract.image_to_string(im, lang='eng')
#         ftext = text
#         print(text)
#         sql = "INSERT INTO image_text (image_name, image_text) VALUES (%s, %s)"
#         val = (fname, ftext)
#
#         mycursor.execute(sql, val)
#
#         mydb.commit()
#
#         print(mycursor.rowcount, "record inserted.")

###############################################################################################################
# from PIL import Image
# import pytesseract
# import cv2
#
# image = Image.open('8020.jpg')
#
# custom_config = r'--psm 6'
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
#
# output = pytesseract.image_to_string(image, config=custom_config,lang='eng')
#
# print(output.strip(''))
#########################################################################################################
# import cv2
# from PIL import Image
# import os
# import numpy as np
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# # load image as HSV and select saturation
# img = Image.open('3m.png').convert('RGB').save('new.png')
# img = cv2.imread("new.png")
# hh, ww, cc = img.shape
# custom_config = r'--psm 6'
# # convert to gray
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # threshold the grayscale image
# ret, thresh = cv2.threshold(gray,165,255,0)
#
# # create black image to hold results
# results = np.zeros((hh,ww))
#
# # find contours
# cntrs = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cntrs = cntrs[0] if len(cntrs) == 2 else cntrs[1]
#
# # Contour filtering and copy contour interior to new black image.
# for c in cntrs:
#     area = cv2.contourArea(c)
#     if area > 1000:
#         x,y,w,h = cv2.boundingRect(c)
#         results[y:y+h,x:x+w] = thresh[y:y+h,x:x+w]
#
# # invert the results image so that have black letters on white background
# results = (255 - results)
#
# # write results to disk
# cv2.imwrite("new.png", results)
#
# cv2.imshow("THRESH", thresh)
# cv2.imshow("RESULTS", results)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
# output = pytesseract.image_to_string(results, config=custom_config, lang='eng')
# print(output)

# ------------------------------------------------------------------------------------------

# from PIL import Image
# from pytesseract import pytesseract
#
# path_to_tesseract = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# image_path = r'C:/Users/ashish/PycharmProjects/pythonProject6/image/ACORN.png'
#
# img = Image.open(image_path)
# pytesseract.tesseract_cmd = path_to_tesseract
# text = pytesseract.image_to_string(img,lang='eng')
# t=(text.encode('utf-8'))
# s=(print(t))
# result=s.decode()
# print(result)


"""import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plt
im_1_path = 'C:/Users/ashish/PycharmProjects/pythonProject6/image/ACORN.png'

img='3m.png'
def recognize_text(img_path):


    reader = easyocr.Reader(['en'])
    return reader.readtext(img_path)


# recognize text
result = recognize_text(im_1_path)

    # if OCR prob is over 0.5, overlay bounding box and text
for (bbox, text, prob) in result:

    if prob >= 0:

        # display
        print(f'Detected text: {text} (Probability: {prob:.2f})')

        # get top-left and bottom-right bbox vertices
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = (int(top_left[0]), int(top_left[1]))
        bottom_right = (int(bottom_right[0]), int(bottom_right[1]))

        # create a rectangle for bbox display
        cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(255, 0, 0), thickness=10)

        # put recognized text
        cv2.putText(img=img, text=text, org=(top_left[0], top_left[1] - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 0, 0), thickness=8)
        # show and save image
        axarr=[]
        axarr[1].imshow(img)"""
        # plt.savefig(f'./output/{}_3m.png', bbox_inches='tight')

import io
import requests
import pytesseract
from PIL import Image
custom_config = r'--psm 6'
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
response = requests.get("https://cdn.raptorsupplies.co.uk/pub/media/catalog/product/AMERICAN-TORCH-TIP-001215.JPG")
img = Image.open(io.BytesIO(response.content))
# print( type(img) ) # <class 'PIL.JpegImagePlugin.JpegImageFile'>
text = pytesseract.image_to_string(img,config=custom_config,lang='eng')
print(text.strip(''))
