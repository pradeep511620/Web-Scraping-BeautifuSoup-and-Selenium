import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re
import undetected_chromedriver.v2 as uc
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def main(url):
 opts = Options()
 #opts.headless = True
 d = uc.Chrome(options=opts)

 d.get(url)

 time.sleep(20)
 try:
  for i in range(0,50):

         ele=d.find_element_by_class_name("pagination__button")
         ele.click()
         time.sleep(10)
 except:
   pass

if __name__ == '__main__':
    list=['https://www.truckpro.com/search/truck%20lite/?page=1#brand:truck-lite']
    for x in range(0,len(list)):
     print(x)
     print(list[x])
     main(list[x])