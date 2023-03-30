import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



myresult=[]

for row in myresult:
 print(row)
 opts = Options()
 #opts.headless = True
 #opts.add_argument("user-agent=""")
 d = webdriver.Chrome("C:/chromedriver.exe", chrome_options=opts)
 d.get(row)

 try:



    headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}


    #a = (result.content.decode())


    soup = BeautifulSoup(d.page_source,'lxml')

    #print(soup.prettify())


    imgg=soup.find("img",class_="image enhanced-content__carousel-main-image image--loaded")


    y = (imgg.get("src") if imgg else "not given")
    print(y)


    save_details: TextIO = open("fastener-latest-1010.txt", "a+", encoding="utf-8")
    save_details.write("\n"+row+"\t"+y)
    save_details.close()
    print("\n**Record stored into txt file.**")






 except AttributeError:

   pass
