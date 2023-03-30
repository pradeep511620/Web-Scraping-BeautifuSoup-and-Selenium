import urllib.parse
from datetime import datetime
from typing import TextIO
from selenium import webdriver
import time
from selenium. webdriver. common. keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def get_details(url):
    global d
    print("Please wait. Program will work in background.\n")

    opts = Options()
    #opts.headless = True
    #opts.add_argument("user-agent=""")
    d = webdriver.Chrome("C:/chromedriver.exe", chrome_options=opts)
    d.get(url)

    try:
                link=d.page_source


    except:
                pass

    soup = BeautifulSoup(link,'html.parser')
    #print(soup.prettify())
    data=soup.find_all("a",class_="_1YKa5r")
    for d in data:
     print(d)

    save_details: TextIO = open("-check-.txt", "a+", encoding="utf-8")
    save_details.write()
    save_details.close()
    print("\n**Record stored into txt file.**")

if __name__ == '__main__':

     list =['https://www.grainger.com/category/material-handling/load-securing/bungee-cords-and-bungee-straps?loadDynatraceJsEnable=false&categoryIndex=2']
     for x in range(0,10000):
         print(x)
         print(list[x])
         get_details(list[x])
