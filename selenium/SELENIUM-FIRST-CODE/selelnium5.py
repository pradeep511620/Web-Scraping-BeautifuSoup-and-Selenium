from io import BytesIO
import requests
from PIL import Image
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
print("sample test case started")

driver = webdriver.Chrome('C:/Users/ashish/Downloads/chromedriver_win32 (1)//chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://staging.raptorsupplies.com/pd/lovejoy/68514428875')

#driver.find_element_by_name("q").send_keys("10A239")
time.sleep(1)

#driver.find_element_by_id("searchBtn").send_keys(Keys.ENTER)
for img in driver.find_elements_by_id('xzoom-default'):
    s=(img.get_attribute("xoriginal"))
    z=('https://cdn.raptorsupplies.com/pub/media/catalog/product/LOVEJOY-68514428875-GR0095623.JPG')
    response = (requests.get(z))

    time.sleep(1)
    driver.get(s)

    res = (requests.get(s))
    print(response)
    print(res)

    img2 = Image.open(BytesIO(response.content))
    img1 = Image.open(BytesIO(res.content))
    
    if (img2 == img1):
        print("same")
    else:
        print("not same")

time.sleep(1)
driver.close()
print("sample test case successfully complete")




