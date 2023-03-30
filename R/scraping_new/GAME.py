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
    time.sleep(5)

    try:
        link = d.page_source


    except:
        pass

    soup = BeautifulSoup(link, 'html.parser')

    name=soup.find_all("div",class_="tab_item_name")
    index=1
    for ele in name:

        a=d.find_element_by_xpath("//*[@id='NewReleasesRows']/a["+str(index)+"]/div[2]/div/div").text

        print(ele.text+"\t" + a)
        index=index+1
        if index==16:
            break







if __name__ == '__main__':

     list =['0',
'1',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9',
'10',
'11',
'12',
'13',
'14',
'15',
'16',
'17',
'18',
'19',
'20',
'21',
'22',
'23',
'24',
'25',
'26',
'27',
'28',
'29',
'30',
'31',
'32',
'33',
'34',
'35',
'36',
'37',
'38',
'39',
'40',
'41',
'42',
'43',
'44',
'45',
'46',
'47',
'48',
'49',
'50',
'51',
'52',
'53',
'54',
'55',
'56',
'57',
'58',
'59',
'60',
'61',
'62',
'63',
'64',
'65',
'66',
'67',
'68',
'69',
'70',
'71',
'72',
'73',
'74',
'75',
'76',
'77'
,'78']
     for x in range(0,10000):

         get_details('https://store.steampowered.com/tags/en/actioN#p='+str(list[x])+'&tab=NewReleases')
