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

    save_details: TextIO = open("gra-nap-fi3.txt", "a+", encoding="utf-8")
    save_details.write("\n" + list[x] + "\t" + aa )
    save_details.close()
    print("\n**Record stored into txt file.**")

if __name__ == '__main__':

     list =[
'https://www.grainger.com/product/38WR85',
'https://www.grainger.com/product/38WR86',
'https://www.grainger.com/product/38WR87',
'https://www.grainger.com/product/38WR88',
'https://www.grainger.com/product/38WR89',
'https://www.grainger.com/product/38WR90',
'https://www.grainger.com/product/38WR91',
'https://www.grainger.com/product/38WR92',
'https://www.grainger.com/product/38WR93',
'https://www.grainger.com/product/38WR94',
'https://www.grainger.com/product/38WR95',
'https://www.grainger.com/product/38WR96',
'https://www.grainger.com/product/38WR97',
'https://www.grainger.com/product/38WR98',
'https://www.grainger.com/product/38WR99',
'https://www.grainger.com/product/38WT01',
'https://www.grainger.com/product/38WT02',
'https://www.grainger.com/product/38WT03',
'https://www.grainger.com/product/38WT04',
'https://www.grainger.com/product/38WT05',
'https://www.grainger.com/product/38WT06',
'https://www.grainger.com/product/38WT07',
'https://www.grainger.com/product/38WT08',
'https://www.grainger.com/product/38WT09',
'https://www.grainger.com/product/38WT10',
'https://www.grainger.com/product/38WT11',
'https://www.grainger.com/product/38WT12',
'https://www.grainger.com/product/38WT13',
'https://www.grainger.com/product/38WT14',
'https://www.grainger.com/product/38WT15',
'https://www.grainger.com/product/38WT16',
'https://www.grainger.com/product/38WT17',
'https://www.grainger.com/product/38WT18',
'https://www.grainger.com/product/38WT19',
'https://www.grainger.com/product/38WT20',
'https://www.grainger.com/product/38WT21',
'https://www.grainger.com/product/38WT22',
'https://www.grainger.com/product/38WT23',
'https://www.grainger.com/product/38WT24',
'https://www.grainger.com/product/38WT25',
'https://www.grainger.com/product/38WT26',
'https://www.grainger.com/product/38WT27',
'https://www.grainger.com/product/38WT28',
'https://www.grainger.com/product/38WT29',
'https://www.grainger.com/product/38WT30',
'https://www.grainger.com/product/38WT31',
'https://www.grainger.com/product/38WT32',
'https://www.grainger.com/product/38WT33',
'https://www.grainger.com/product/38WT34',
'https://www.grainger.com/product/38WT35',
'https://www.grainger.com/product/38WT36',
'https://www.grainger.com/product/38WT37',
'https://www.grainger.com/product/38WT38',
'https://www.grainger.com/product/38WT39',
'https://www.grainger.com/product/38WT40',
'https://www.grainger.com/product/38WT41',
'https://www.grainger.com/product/38WT42',
'https://www.grainger.com/product/38WT43',
'https://www.grainger.com/product/38WT44',
'https://www.grainger.com/product/38WT45',
'https://www.grainger.com/product/38WT46',
'https://www.grainger.com/product/38WT47',
'https://www.grainger.com/product/38WT48',
'https://www.grainger.com/product/38WT49',
'https://www.grainger.com/product/38WT50',
'https://www.grainger.com/product/38WT51',
'https://www.grainger.com/product/38WT52',
'https://www.grainger.com/product/38WT53',
'https://www.grainger.com/product/38WT54',
'https://www.grainger.com/product/38WT55',
'https://www.grainger.com/product/38WT56',
'https://www.grainger.com/product/38WT57',
'https://www.grainger.com/product/38WT58',
'https://www.grainger.com/product/38WT59',
'https://www.grainger.com/product/38WT60',
'https://www.grainger.com/product/38WT61',
'https://www.grainger.com/product/38WT62',
'https://www.grainger.com/product/38WT63',
'https://www.grainger.com/product/38WT64',
'https://www.grainger.com/product/38WT65',
'https://www.grainger.com/product/38WT66',
'https://www.grainger.com/product/38WT67',
'https://www.grainger.com/product/38WT68',
'https://www.grainger.com/product/38WT69',
'https://www.grainger.com/product/38WT70',
'https://www.grainger.com/product/38WT71',
'https://www.grainger.com/product/38WT72',
'https://www.grainger.com/product/38WT73',
'https://www.grainger.com/product/38WT74',
'https://www.grainger.com/product/38WT75',
'https://www.grainger.com/product/38WT76',
'https://www.grainger.com/product/38WT77',
'https://www.grainger.com/product/38WT78',
'https://www.grainger.com/product/38WT79',
'https://www.grainger.com/product/38WT80',
'https://www.grainger.com/product/38WT81',
'https://www.grainger.com/product/38WT82',
'https://www.grainger.com/product/38WT83',
'https://www.grainger.com/product/38WT84',
'https://www.grainger.com/product/38WT85',
'https://www.grainger.com/product/38WT86',
'https://www.grainger.com/product/38WT87',
'https://www.grainger.com/product/38WT88',
'https://www.grainger.com/product/38WT89',
'https://www.grainger.com/product/38WT90',
'https://www.grainger.com/product/38WT91',
'https://www.grainger.com/product/38WT92',
'https://www.grainger.com/product/38WT93',
'https://www.grainger.com/product/38WT94',
'https://www.grainger.com/product/38WT95',
'https://www.grainger.com/product/38WT96',
'https://www.grainger.com/product/38WT97',
'https://www.grainger.com/product/38WT98',
'https://www.grainger.com/product/38WT99',
'https://www.grainger.com/product/38WU01',
'https://www.grainger.com/product/38WU02',
'https://www.grainger.com/product/38WU03',
'https://www.grainger.com/product/38WU04',
'https://www.grainger.com/product/38WU05',
'https://www.grainger.com/product/38WU06',
'https://www.grainger.com/product/38WU07',
'https://www.grainger.com/product/38WU08',
'https://www.grainger.com/product/38WU09',
'https://www.grainger.com/product/38WU10',
'https://www.grainger.com/product/38WU11',
'https://www.grainger.com/product/38WU12',
'https://www.grainger.com/product/38WU13',
'https://www.grainger.com/product/38WU14',
'https://www.grainger.com/product/38WU15',
'https://www.grainger.com/product/38WU16',
'https://www.grainger.com/product/38WU17',
'https://www.grainger.com/product/38WU18',
'https://www.grainger.com/product/38WU19',
'https://www.grainger.com/product/38WU20',
'https://www.grainger.com/product/38WU21',
'https://www.grainger.com/product/38WU22',
'https://www.grainger.com/product/38WU23',
'https://www.grainger.com/product/38WU24',
'https://www.grainger.com/product/38WU25',
'https://www.grainger.com/product/38WU26']
     for x in range(0,10000):
         print(x)
         print(list[x])
         get_details(list[x])
