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

    save_details: TextIO = open("gra-nap-fi2.txt", "a+", encoding="utf-8")
    save_details.write("\n" + list[x] + "\t" + aa )
    save_details.close()
    print("\n**Record stored into txt file.**")

if __name__ == '__main__':

     list =[
'https://www.grainger.com/product/31JA65',
'https://www.grainger.com/product/31JA66',
'https://www.grainger.com/product/31JA67',
'https://www.grainger.com/product/31JA88',
'https://www.grainger.com/product/31JA92',
'https://www.grainger.com/product/31JC01',
'https://www.grainger.com/product/31JC09',
'https://www.grainger.com/product/31JC10',
'https://www.grainger.com/product/31JC15',
'https://www.grainger.com/product/31JC64',
'https://www.grainger.com/product/31JD59',
'https://www.grainger.com/product/31JE15',
'https://www.grainger.com/product/31JE16',
'https://www.grainger.com/product/31JE17',
'https://www.grainger.com/product/31JE18',
'https://www.grainger.com/product/31JE19',
'https://www.grainger.com/product/31JE20',
'https://www.grainger.com/product/31JE21',
'https://www.grainger.com/product/31JE22',
'https://www.grainger.com/product/31JE80',
'https://www.grainger.com/product/31JF86',
'https://www.grainger.com/product/31JG92',
'https://www.grainger.com/product/31JH93',
'https://www.grainger.com/product/31JJ42',
'https://www.grainger.com/product/31JJ43',
'https://www.grainger.com/product/31JJ94',
'https://www.grainger.com/product/31JJ95',
'https://www.grainger.com/product/31JJ96',
'https://www.grainger.com/product/31JK02',
'https://www.grainger.com/product/31JK04',
'https://www.grainger.com/product/31JK07',
'https://www.grainger.com/product/31JK09',
'https://www.grainger.com/product/31JK11',
'https://www.grainger.com/product/31JK13',
'https://www.grainger.com/product/31JK74',
'https://www.grainger.com/product/31JL12',
'https://www.grainger.com/product/31JL18',
'https://www.grainger.com/product/31JL24',
'https://www.grainger.com/product/31JL29',
'https://www.grainger.com/product/31JL66',
'https://www.grainger.com/product/31JL67',
'https://www.grainger.com/product/31JL69',
'https://www.grainger.com/product/31JL73',
'https://www.grainger.com/product/31JL79',
'https://www.grainger.com/product/31JL80',
'https://www.grainger.com/product/31JL88',
'https://www.grainger.com/product/31JL91',
'https://www.grainger.com/product/31JL94',
'https://www.grainger.com/product/31JL95',
'https://www.grainger.com/product/31JL97',
'https://www.grainger.com/product/31JM17',
'https://www.grainger.com/product/31JM75',
'https://www.grainger.com/product/31JM81',
'https://www.grainger.com/product/31JM93',
'https://www.grainger.com/product/31JM94',
'https://www.grainger.com/product/31JN23',
'https://www.grainger.com/product/31JP07',
'https://www.grainger.com/product/31JP25',
'https://www.grainger.com/product/31JP75',
'https://www.grainger.com/product/31JP78',
'https://www.grainger.com/product/31JP80',
'https://www.grainger.com/product/31JP83',
'https://www.grainger.com/product/31JP84',
'https://www.grainger.com/product/31JP85',
'https://www.grainger.com/product/31JP86',
'https://www.grainger.com/product/31JP87',
'https://www.grainger.com/product/31JP88',
'https://www.grainger.com/product/31JP89',
'https://www.grainger.com/product/31JP90',
'https://www.grainger.com/product/31JP91',
'https://www.grainger.com/product/31JP92',
'https://www.grainger.com/product/31JP94',
'https://www.grainger.com/product/31JP95',
'https://www.grainger.com/product/31JP96',
'https://www.grainger.com/product/31JR01',
'https://www.grainger.com/product/31JR02',
'https://www.grainger.com/product/31JR03',
'https://www.grainger.com/product/31JR04',
'https://www.grainger.com/product/31JR05',
'https://www.grainger.com/product/31JR26',
'https://www.grainger.com/product/31JR48',
'https://www.grainger.com/product/31JR53',
'https://www.grainger.com/product/31JR54',
'https://www.grainger.com/product/31JR55',
'https://www.grainger.com/product/31JR56',
'https://www.grainger.com/product/31JR59',
'https://www.grainger.com/product/31JR64',
'https://www.grainger.com/product/31JR68',
'https://www.grainger.com/product/31JR69',
'https://www.grainger.com/product/31JR73',
'https://www.grainger.com/product/31JR76',
'https://www.grainger.com/product/31JR77',
'https://www.grainger.com/product/31JR78',
'https://www.grainger.com/product/31JR79',
'https://www.grainger.com/product/31JR81',
'https://www.grainger.com/product/31JR82',
'https://www.grainger.com/product/31JR83',
'https://www.grainger.com/product/31JR84',
'https://www.grainger.com/product/31JR85',
'https://www.grainger.com/product/31JR86']
     for x in range(0,10000):
         print(x)
         print(list[x])
         get_details(list[x])
