import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time



myresult=['https://stage.raptorsupplies.com/pd/morse-drum/86']

for row in myresult:
 opts = Options()
 opts.headless = True
 d = webdriver.Chrome("C:/chromedriver.exe", chrome_options=opts)
 d.get(row)
 time.sleep(2)

 try:
     elements=d.find_elements_by_tag_name("img")
     list=[]
     for ele in elements:
         try:
             list.append(ele.get_attribute("src"))
         except:
             pass
     print(list)


     save_details: TextIO = open("img-src.txt", "a+", encoding="utf-8")
     save_details.write("\n")
     save_details.close()
     print("\n**Record stored into txt file.**")







 except AttributeError:

   pass
