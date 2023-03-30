
from PIL import Image
import pytesseract

image = Image.open('img1.jpg')
custom_config = r'--psm 6'
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

output = pytesseract.image_to_string(image, config=custom_config,lang='eng')

print(output.strip(''))



