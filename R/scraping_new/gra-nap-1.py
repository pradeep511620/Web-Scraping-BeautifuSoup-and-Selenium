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

    save_details: TextIO = open("gra-nap-fi1.txt", "a+", encoding="utf-8")
    save_details.write("\n" + list[x] + "\t" + aa )
    save_details.close()
    print("\n**Record stored into txt file.**")

if __name__ == '__main__':

     list =[
'https://www.grainger.com/product/31JF67',
'https://www.grainger.com/product/31JF68',
'https://www.grainger.com/product/31JF69',
'https://www.grainger.com/product/31JF70',
'https://www.grainger.com/product/31JF71',
'https://www.grainger.com/product/31JF72',
'https://www.grainger.com/product/31JF73',
'https://www.grainger.com/product/31JF74',
'https://www.grainger.com/product/31JF75',
'https://www.grainger.com/product/31JF76',
'https://www.grainger.com/product/31JF77',
'https://www.grainger.com/product/31JF78',
'https://www.grainger.com/product/31JF79',
'https://www.grainger.com/product/31JF80',
'https://www.grainger.com/product/31JF81',
'https://www.grainger.com/product/31JF82',
'https://www.grainger.com/product/31JF83',
'https://www.grainger.com/product/31JF84',
'https://www.grainger.com/product/31JF85',
'https://www.grainger.com/product/31JF87',
'https://www.grainger.com/product/31JF88',
'https://www.grainger.com/product/31JF89',
'https://www.grainger.com/product/31JF90',
'https://www.grainger.com/product/31JF91',
'https://www.grainger.com/product/31JF92',
'https://www.grainger.com/product/31JF93',
'https://www.grainger.com/product/31JF94',
'https://www.grainger.com/product/31JF95',
'https://www.grainger.com/product/31JF96',
'https://www.grainger.com/product/31JF97',
'https://www.grainger.com/product/31JF98',
'https://www.grainger.com/product/31JF99',
'https://www.grainger.com/product/31JG01',
'https://www.grainger.com/product/31JG02',
'https://www.grainger.com/product/31JG03',
'https://www.grainger.com/product/31JG04',
'https://www.grainger.com/product/31JG05',
'https://www.grainger.com/product/31JG06',
'https://www.grainger.com/product/31JG07',
'https://www.grainger.com/product/31JG08',
'https://www.grainger.com/product/31JG09',
'https://www.grainger.com/product/31JG10',
'https://www.grainger.com/product/31JG11',
'https://www.grainger.com/product/31JG12',
'https://www.grainger.com/product/31JG13',
'https://www.grainger.com/product/31JG14',
'https://www.grainger.com/product/31JG15',
'https://www.grainger.com/product/31JG16',
'https://www.grainger.com/product/31JG17',
'https://www.grainger.com/product/31JG23',
'https://www.grainger.com/product/31JG24',
'https://www.grainger.com/product/31JG25',
'https://www.grainger.com/product/31JG26',
'https://www.grainger.com/product/31JG27',
'https://www.grainger.com/product/31JG28',
'https://www.grainger.com/product/31JG29',
'https://www.grainger.com/product/31JG30',
'https://www.grainger.com/product/31JG31',
'https://www.grainger.com/product/31JG32',
'https://www.grainger.com/product/31JG33',
'https://www.grainger.com/product/31JG34',
'https://www.grainger.com/product/31JG35',
'https://www.grainger.com/product/31JG36',
'https://www.grainger.com/product/31JG37',
'https://www.grainger.com/product/31JG38',
'https://www.grainger.com/product/31JG39',
'https://www.grainger.com/product/31JG40',
'https://www.grainger.com/product/31JG41',
'https://www.grainger.com/product/31JG42',
'https://www.grainger.com/product/31JG43',
'https://www.grainger.com/product/31JG44',
'https://www.grainger.com/product/31JG45',
'https://www.grainger.com/product/31JG46',
'https://www.grainger.com/product/31JG47',
'https://www.grainger.com/product/31JG48',
'https://www.grainger.com/product/31JG49',
'https://www.grainger.com/product/31JG50',
'https://www.grainger.com/product/31JG51',
'https://www.grainger.com/product/31JG52',
'https://www.grainger.com/product/31JG53',
'https://www.grainger.com/product/31JG54',
'https://www.grainger.com/product/31JG55',
'https://www.grainger.com/product/31JG56',
'https://www.grainger.com/product/31JG57',
'https://www.grainger.com/product/31JG58',
'https://www.grainger.com/product/31JG59',
'https://www.grainger.com/product/31JG60',
'https://www.grainger.com/product/31JG61',
'https://www.grainger.com/product/31JG62',
'https://www.grainger.com/product/31JG63',
'https://www.grainger.com/product/31JG64',
'https://www.grainger.com/product/31JG65',
'https://www.grainger.com/product/31JG66',
'https://www.grainger.com/product/31JG67',
'https://www.grainger.com/product/31JG68',
'https://www.grainger.com/product/31JG69',
'https://www.grainger.com/product/31JG70',
'https://www.grainger.com/product/31JG71',
'https://www.grainger.com/product/31JG72',
'https://www.grainger.com/product/31JG73',
'https://www.grainger.com/product/31JG74',
'https://www.grainger.com/product/31JG75',
'https://www.grainger.com/product/31JG76',
'https://www.grainger.com/product/31JG77',
'https://www.grainger.com/product/31JG78',
'https://www.grainger.com/product/31JG79',
'https://www.grainger.com/product/31JG80',
'https://www.grainger.com/product/31JG81',
'https://www.grainger.com/product/31JG82',
'https://www.grainger.com/product/31JG83',
'https://www.grainger.com/product/31JG84',
'https://www.grainger.com/product/31JG85',
'https://www.grainger.com/product/31JG86',
'https://www.grainger.com/product/31JG87',
'https://www.grainger.com/product/31JG88',
'https://www.grainger.com/product/31JG89',
'https://www.grainger.com/product/31JG90',
'https://www.grainger.com/product/31JG91',
'https://www.grainger.com/product/31JG93',
'https://www.grainger.com/product/31JG94',
'https://www.grainger.com/product/31JG95',
'https://www.grainger.com/product/31JG96',
'https://www.grainger.com/product/31JG97',
'https://www.grainger.com/product/31JG98',
'https://www.grainger.com/product/31JG99',
'https://www.grainger.com/product/31JH01',
'https://www.grainger.com/product/31JH02',
'https://www.grainger.com/product/31JH03',
'https://www.grainger.com/product/31JH04',
'https://www.grainger.com/product/31JH05',
'https://www.grainger.com/product/31JH06',
'https://www.grainger.com/product/31JH07',
'https://www.grainger.com/product/31JH08',
'https://www.grainger.com/product/31JH09',
'https://www.grainger.com/product/31JH10',
'https://www.grainger.com/product/31JH11',
'https://www.grainger.com/product/31JH12',
'https://www.grainger.com/product/31JH13',
'https://www.grainger.com/product/31JH14',
'https://www.grainger.com/product/31JH15',
'https://www.grainger.com/product/31JH16',
'https://www.grainger.com/product/31JH17',
'https://www.grainger.com/product/31JH18',
'https://www.grainger.com/product/31JH19',
'https://www.grainger.com/product/31JH20',
'https://www.grainger.com/product/31JH21',
'https://www.grainger.com/product/31JH22',
'https://www.grainger.com/product/31JH23',
'https://www.grainger.com/product/31JH24',
'https://www.grainger.com/product/31JH25',
'https://www.grainger.com/product/31JH26',
'https://www.grainger.com/product/31JH27',
'https://www.grainger.com/product/31JH28',
'https://www.grainger.com/product/31JH29',
'https://www.grainger.com/product/31JH30',
'https://www.grainger.com/product/31JH31',
'https://www.grainger.com/product/31JH32',
'https://www.grainger.com/product/31JH33',
'https://www.grainger.com/product/31JH34',
'https://www.grainger.com/product/31JH35',
'https://www.grainger.com/product/31JH36',
'https://www.grainger.com/product/31JH37',
'https://www.grainger.com/product/31JH38',
'https://www.grainger.com/product/31JH39',
'https://www.grainger.com/product/31JH40',
'https://www.grainger.com/product/31JH41',
'https://www.grainger.com/product/31JH42',
'https://www.grainger.com/product/31JH43',
'https://www.grainger.com/product/31JH44',
'https://www.grainger.com/product/31JH45',
'https://www.grainger.com/product/31JH46',
'https://www.grainger.com/product/31JH47',
'https://www.grainger.com/product/31JH48',
'https://www.grainger.com/product/31JH49',
'https://www.grainger.com/product/31JH50']
     for x in range(0,10000):
         print(x)
         print(list[x])
         get_details(list[x])
