import requests
from bs4 import BeautifulSoup
from typing import TextIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

myresult=[

'https://8020.net/75-3650.html',
'https://8020.net/75-3456.html',
'https://8020.net/75-3449.html',
'https://8020.net/75-3446.html',
'https://8020.net/3845.html',
'https://8020.net/3855.html',
'https://8020.net/75-3444.html',
'https://8020.net/3856.html',
'https://8020.net/75-3522.html',
'https://8020.net/75-3469.html',
'https://8020.net/75-3443.html',
'https://8020.net/3849.html',
'https://8020.net/75-3505.html',
'https://8020.net/75-3441.html',
'https://8020.net/75-3438.html',
'https://8020.net/75-3644.html',
'https://8020.net/75-3466.html',
'https://8020.net/75-3439.html',
'https://8020.net/3824.html',
'https://8020.net/75-3642.html',
'https://8020.net/75-3640.html',
'https://8020.net/3430.html',
'https://8020.net/3429.html',
'https://8020.net/3475.html',
'https://8020.net/75-3849.html',
'https://8020.net/75-3841.html',
'https://8020.net/3464.html',
'https://8020.net/75-3839.html',
'https://8020.net/3530.html',
'https://8020.net/3529.html',
'https://8020.net/75-3837.html',
'https://8020.net/75-3831.html',
'https://8020.net/75-3832.html',
'https://8020.net/3526.html',
'https://8020.net/75-3817.html',
'https://8020.net/3498.html',
'https://8020.net/3494.html',
'https://8020.net/75-3813.html',
'https://8020.net/25-4186.html',
'https://8020.net/75-3811.html',
'https://8020.net/75-3805.html',
'https://8020.net/75-3809.html',
'https://8020.net/75-3807.html',
'https://8020.net/75-3801.html',
'https://8020.net/13001.html',
'https://8020.net/13-8325.html',
'https://8020.net/4626-black.html',
'https://8020.net/12038.html',
'https://8020.net/12035.html',
'https://8020.net/12034.html',
'https://8020.net/12032.html',
'https://8020.net/12033.html',
'https://8020.net/12030.html',
'https://8020.net/12031.html',
'https://8020.net/45-2540-black.html',
'https://8020.net/45-2564-black.html',
'https://8020.net/30-2568-black.html',
'https://8020.net/2541-black.html',
'https://8020.net/2536-black.html',
'https://8020.net/2526-black.html',
'https://8020.net/2526.html',
'https://8020.net/2574-black.html',
'https://8020.net/2573-black.html',
'https://8020.net/4505-black.html',
'https://8020.net/12299.html',
'https://8020.net/4159-black.html'
]

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
   ############## Part No #################h1 class="page-title bold no-margin-top"
    partNo = soup.find("h1",{'class': "page-title bold no-margin-top"})
    a = (partNo.text.strip() if partNo else "not given")
    print(a) # 1030
    ############## Title ################# div class ="value" itemprop="description"
    title = soup.find("div",{'class': "value"})
    a1 = (title.text.strip() if title else "not given")
    print(a1)
    ############## Description ################# <div class="col-md-6 no-padding-left no-padding-right col-md-padding-left-lg margin-bottom-lg">
    desc = soup.find("div", {'class': "col-md-6 no-padding-left no-padding-right col-md-padding-left-lg margin-bottom-lg"})
    a2 = (desc.text.strip() if desc else "not given")
    print(a2)
    ############## Image ################# div class ="fotorama__stage__frame fotorama_vertical_ratio fotorama__loaded fotorama__loaded--img fotorama__active"
    img = soup.find("img",{'class':"fotorama__img"})
                     # {'class': "fotorama__stage__frame fotorama_vertical_ratio fotorama__loaded fotorama__loaded--img fotorama__active"})
    image = (img['src'] if img else "not given")
    print(image)
    ############## Images ################# div class ="fotorama__nav__shaft"
    imagesLst = []
    imgs = soup.find_all("img", {'class': "fotorama__img"})
    for img in imgs:
       images = (img['src'] if img else "not given")
       imagesLst.append(images)
    print(imagesLst)
    c = (product_url)
    print(c)
    ############## Details #################
    prod = soup.find("table").find_all('tr')
    i = 0

    while i < len(prod):
            z = (prod[i].text.strip() if prod else "not given")
            attr = z.split("\n")[0]
            value = z.split("\n")[1]
            print(attr)
            print(value)
            i += 1
            save_details: TextIO = open("8020byidea4a.txt", "a+", encoding="utf-8")
            save_details.write("\n"+c+"\t"+a+"\t"+a1+"\t"+a2+"\t"+image+"\t"+" , ".join(imagesLst)+"\t"+attr+"\t"+value)
            save_details.close()
            print("**Record stored into txt file.**")

 #
 except AttributeError:

   pass