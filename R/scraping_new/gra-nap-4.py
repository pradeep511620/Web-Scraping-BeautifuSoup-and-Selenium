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
    d.implicitly_wait(10)
    d.get(url)
    time.sleep(5)







    try:
                d.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div[3]/div[2]/div[2]/div[1]/div[4]/div/p/button").click()
                time.sleep(5)
                inputElement = d.find_element_by_id("rta__delivery-zip-code--input-sidebarlarge")


                inputElement.send_keys('90202')
                inputElement.send_keys(Keys.ENTER)
                d.refresh()
                time.sleep(5)


    except:
                pass

    try:
                link=d.page_source


    except:
                pass

    soup = BeautifulSoup(link,'html.parser')
    title = soup.find("div", class_="rta__copy rta_copy--message")
    aa = (title.text.strip() if title else "not given")
    print(aa)

    save_details: TextIO = open("gra-nap-fi4.txt", "a+", encoding="utf-8")
    save_details.write("\n" + list[x] + "\t" + aa )
    save_details.close()
    print("\n**Record stored into txt file.**")

if __name__ == '__main__':

     list =[]
     for x in range(0,10000):
         print(x)
         print(list[x])
         get_details(list[x])
