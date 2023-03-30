import urllib.parse
from datetime import datetime
from typing import TextIO
from selenium import webdriver
import time
import sys
from selenium. webdriver. common. keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.remote.webelement


def get_details(url):
    global d
    #current_date: object = datetime.now()
    #save_details: TextIO = open("Destacoo.txt", "a+")
    #save_details.write("\nScrapping Started at : " + current_date.strftime("%B %d, %Y - %H:%M:%S") + "\n")
    #save_details.close()
    #print("\nScrapping Started at : " + current_date.strftime("%B %d, %Y - %H:%M:%S") + "\n")

    print("Please wait. Program will work in background.\n")

    opts = Options()
    opts.headless = True
    opts.add_argument("user-agent=""")
    d = webdriver.Chrome("C:/chromedriver.exe", chrome_options=opts)
    d.get(url)


    try:
                link=d.page_source


    except:
                pass


    save_details: TextIO = open("gra-nap-fi1.txt", "a+", encoding="utf-8")
    save_details.write("\n" + list[x] + "\t" + aa )
    save_details.close()
    print("\n**Record stored into txt file.**")

if __name__ == '__main__':

     list =['https://www.mcmaster.com/5887T1/']
     for x in range(0,10000):
         print(x)
         print(list[x])
         get_details(list[x])
