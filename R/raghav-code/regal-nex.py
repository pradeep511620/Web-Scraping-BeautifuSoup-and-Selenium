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

    opts.add_argument("user-agent=""")
    d = webdriver.Chrome("C:/chromedriver.exe", chrome_options=opts)
    d.implicitly_wait(10)
    d.get(url)
    time.sleep(5)
    title=brand=image=price=bread_=""









    try:
        title=d.find_element_by_xpath("//*[@id='wrapper']/main/div/div[3]/div/div/div[2]/div/div/div[1]/div[6]/div/div/div[1]/div[2]/div/div[2]/div/div").text
        print("product name:"+title)
        save_details: TextIO = open("leeson-regal.txt", "a+", encoding="utf-8")
        save_details.write("\n"+list[x]+"\t"+title)
        save_details.close()
        print("\n**Record stored into txt file.**")
    except:
        return




if __name__ == '__main__':
     list=['https://www.regalrexnord.com/products/motors/low-voltage-nema-motors/general-purpose-low-voltage-nema-motors/nema-general-purpose-single-phase-motors/single-phase-odp-motors/1-hp-general-purpose-motor-1-phase-3600-rpm-115-230-v-56c-frame-odp-E116769-00']
     for x in range(0,1200):
         print(x)
         print(list[x])
         get_details(list[x])
