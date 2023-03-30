import requests
from bs4 import BeautifulSoup
from typing import TextIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

myresult=[

'https://8020.net/3496.html',
'https://8020.net/75-3535.html',
'https://8020.net/20-2570.html',
'https://8020.net/25-4118-black.html',
'https://8020.net/4392.html',
'https://8020.net/4397-black.html',
'https://8020.net/9307.html',
'https://8020.net/13-3957.html',
'https://8020.net/2532.html',
'https://8020.net/25-4149-black.html',
'https://8020.net/13-8535.html',
'https://8020.net/75-3843.html',
'https://8020.net/4626.html',
'https://8020.net/65-4503-black.html',
'https://8020.net/4349-black.html',
'https://8020.net/25-3502.html',
'https://8020.net/75-3423.html',
'https://8020.net/75-3814.html',
'https://8020.net/40-2555.html',
'https://8020.net/4311-black.html',
'https://8020.net/30-4481-black.html',
'https://8020.net/25-2568.html',
'https://8020.net/14174.html',
'https://8020.net/3822.html',
'https://8020.net/75-3808.html',
'https://8020.net/2564.html',
'https://8020.net/40-4341-black.html',
'https://8020.net/3215.html',
'https://8020.net/75-3850.html',
'https://8020.net/4309-black.html',
'https://8020.net/4354.html',
'https://8020.net/13-8540.html',
'https://8020.net/4143-black.html',
'https://8020.net/4004-black.html',
'https://8020.net/30-2565.html',
'https://8020.net/4512-black.html',
'https://8020.net/4196-black.html',
'https://8020.net/13174.html',
'https://8020.net/40-2525-black.html',
'https://8020.net/75-3519.html',
'https://8020.net/45-4340-black.html',
'https://8020.net/3131.html',
'https://8020.net/19-8930.html',
'https://8020.net/25-4195.html',
'https://8020.net/13138.html',
'https://8020.net/3465.html',
'https://8020.net/3133.html',
'https://8020.net/4523-black.html',
'https://8020.net/4423.html',
'https://8020.net/25-4128-black.html',
'https://8020.net/40-4331.html',
'https://8020.net/75-3455.html',
'https://8020.net/4006.html',
'https://8020.net/13-3954.html',
'https://8020.net/3445.html',
'https://8020.net/9330.html',
'https://8020.net/4702.html',
'https://8020.net/4519-black.html',
'https://8020.net/4195-black.html',
'https://8020.net/40-4354.html',
'https://8020.net/4023.html',
'https://8020.net/9290.html',
'https://8020.net/20-4166-black.html',
'https://8020.net/45-4481-black.html',
'https://8020.net/40-4386.html',
'https://8020.net/3762.html',
'https://8020.net/75-3520.html',
'https://8020.net/25-4111-black.html',
'https://8020.net/4002.html',
'https://8020.net/4158.html',
'https://8020.net/3525.html',
'https://8020.net/40-2535-black.html',
'https://8020.net/4360.html',
'https://8020.net/2567-black.html',
'https://8020.net/40-4309.html',
'https://8020.net/30-2570.html',
'https://8020.net/2552.html',
'https://8020.net/30-4335.html',
'https://8020.net/4511-black.html',
'https://8020.net/40-4390.html',
'https://8020.net/4405-black.html',
'https://8020.net/20-2575.html',
'https://8020.net/75-3406.html',
'https://8020.net/25-4141-black.html',
'https://8020.net/4135-black.html',
'https://8020.net/20-4080-black.html',
'https://8020.net/13-1957.html',
'https://8020.net/4315.html',
'https://8020.net/45-2562.html',
'https://8020.net/4251-black.html',
'https://8020.net/3480.html',
'https://8020.net/4395-black.html',
'https://8020.net/75-3847.html',
'https://8020.net/19-1065.html',
'https://8020.net/4121-black.html',
'https://8020.net/75-3467.html',
'https://8020.net/4016-black.html',
'https://8020.net/3872.html',
'https://8020.net/25-4112-black.html',
'https://8020.net/4003.html',
'https://8020.net/3497.html',
'https://8020.net/4174-black.html',
'https://8020.net/3751.html',
'https://8020.net/40-2579.html',
'https://8020.net/30-4376-black.html',
'https://8020.net/3889.html',
'https://8020.net/4416-black.html',
'https://8020.net/45-4303-black.html',
'https://8020.net/13-5312.html',
'https://8020.net/13-3958.html',
'https://8020.net/3484.html',
'https://8020.net/25-2567.html',
'https://8020.net/75-3511.html',
'https://8020.net/2553.html',
'https://8020.net/25-2575-black.html',
'https://8020.net/4187-black.html',
'https://8020.net/3348.html',
'https://8020.net/75-3400.html',
'https://8020.net/2525-black.html'
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
            save_details: TextIO = open("8020byidea3a.txt", "a+", encoding="utf-8")
            save_details.write("\n"+c+"\t"+a+"\t"+a1+"\t"+a2+"\t"+image+"\t"+" , ".join(imagesLst)+"\t"+attr+"\t"+value)
            save_details.close()
            print("**Record stored into txt file.**")

 #
 except AttributeError:

   pass