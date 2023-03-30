import requests
from bs4 import BeautifulSoup
from typing import TextIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

myresult=['https://buy.ham-let.com/#']

for row in myresult:

 try:
    opts = Options()
    opts.headless = True
    d = webdriver.Chrome(executable_path=r"C:\Users\nextgenraptor\Downloads\chromedriver_win32 (3)\chromedriver.exe", chrome_options=opts)
    d.get(row)
    time.sleep(5)

    product_url = row
    headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}
    soup = BeautifulSoup(d.page_source,'html.parser')
   ############## Menu #################
    for menu1 in soup.find_all("a",{'class': "menu-link"}):  # done
        a = (menu1['href'] if menu1 else "not given")
        print(a)
    # for menu2 in soup.find_all("span", {'class': "widget block block - category - link - inline"}):
    #     b = (menu2.text.strip() if menu2 else "not given")
    #     print(b)
    # for menu3 in soup.find_all("p",{'class': "groupdrop-title"}): # done
    #     c = (menu3.text.strip() if menu3 else "not given")
    #     print("2",c)
    # for menu4 in soup.find_all("ul", {'class': "groupmenu - drop slidedown"}):  # done
    #     d = (menu4.text.strip() if menu4 else "not given")
    #     print(a)




        save_details: TextIO = open("hamlet_menu2.txt", "a+", encoding="utf-8")
        save_details.write("\n" + a )
        save_details.close()
        print("**Record stored into txt file.**")

 except AttributeError:

   pass