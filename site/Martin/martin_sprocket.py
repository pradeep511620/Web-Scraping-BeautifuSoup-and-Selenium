from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# create webdriver object
driver = webdriver.Chrome(executable_path=r"C:\Users\nextgenraptor\Downloads\chromedriver_win32 (3)\chromedriver.exe")
# get google.co.in
url = "https://www.martinsprocket.com/view/products/product-search?Website_Code=SP1"
driver.get(url)
driver.maximize_window()

a = 0
elems = driver.find_elements(By.XPATH,"//a[@href]")
for elem in elems:
    a += 1
    link = elem.get_attribute("href")
    # print(link)
print(a)

import requests
from bs4 import BeautifulSoup

url = "https://chromedriver.storage.googleapis.com/?delimiter=/&prefix=97.0.4692.71/"
soup = BeautifulSoup(requests.get(url).text, features="xml").find_all("Key")
keys = [f"https://chromedriver.storage.googleapis.com/{k.getText()}" for k in soup]
print("\n".join(keys))
# javascript:void(0);
# https://www.martinsprocket.com/view/power-transmission/sprockets
# https://www.martinsprocket.com/view/products/product-search?Website_Code=SP1

# driver.find_element(By.LINK_TEXT,"Power Transmission").click()
# <a class="productLink" href="/views/productinfo.aspx?Part_Number=100A10&amp;Website_CategoryName=Sprockets&amp;Website_Code=SP1">
                                                      #   100A10&nbsp;SPK ROLLER A</a>

