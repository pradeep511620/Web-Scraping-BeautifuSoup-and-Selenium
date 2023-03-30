import requests
from bs4 import BeautifulSoup
from typing import TextIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

myresult=[

'https://8020.net/40-3102.html',
'https://8020.net/9170.html',
'https://8020.net/25-3681.html',
'https://8020.net/11-4312.html',
'https://8020.net/3940.html',
'https://8020.net/3693.html',
'https://8020.net/13-5510.html',
'https://8020.net/4265-black.html',
'https://8020.net/14053.html',
'https://8020.net/3695.html',
'https://8020.net/3097.html',
'https://8020.net/3344.html',
'https://8020.net/3087.html',
'https://8020.net/4366.html',
'https://8020.net/65-3067.html',
'https://8020.net/75-3638.html',
'https://8020.net/25-3376.html',
'https://8020.net/3604.html',
'https://8020.net/3661.html',
'https://8020.net/25-4132-black.html',
'https://8020.net/3612.html',
'https://8020.net/13184.html',
'https://8020.net/3876.html',
'https://8020.net/3022.html',
'https://8020.net/3106.html',
'https://8020.net/3897.html',
'https://8020.net/40-1968.html',
'https://8020.net/4166.html',
'https://8020.net/3689.html',
'https://8020.net/3085.html',
'https://8020.net/17-6510.html',
'https://8020.net/4152.html',
'https://8020.net/40-4365.html',
'https://8020.net/4338-black.html',
'https://8020.net/3942.html',
'https://8020.net/4312.html',
'https://8020.net/3410.html',
'https://8020.net/3479.html',
'https://8020.net/13-6520.html',
'https://8020.net/3609.html',
'https://8020.net/3325.html',
'https://8020.net/3088.html',
'https://8020.net/13193.html',
'https://8020.net/40-1988.html',
'https://8020.net/13090.html',
'https://8020.net/3839.html',
'https://8020.net/4481-black.html',
'https://8020.net/3414.html',
'https://8020.net/3206.html',
'https://8020.net/25-4151.html',
'https://8020.net/3396.html',
'https://8020.net/19-6312.html',
'https://8020.net/4013.html',
'https://8020.net/4141.html',
'https://8020.net/25-4119-black.html',
'https://8020.net/25-4114.html',
'https://8020.net/3906.html',
'https://8020.net/14098.html',
'https://8020.net/13133.html',
'https://8020.net/14083.html',
'https://8020.net/75-3510.html',
'https://8020.net/4290.html',
'https://8020.net/13-6410.html',
'https://8020.net/13179.html',
'https://8020.net/40-4336-black.html',
'https://8020.net/3055.html',
'https://8020.net/3010.html',
'https://8020.net/4307-black.html',
'https://8020.net/4413.html',
'https://8020.net/4442.html',
'https://8020.net/3048.html',
'https://8020.net/3058.html',
'https://8020.net/19-6042.html',
'https://8020.net/40-4304.html',
'https://8020.net/3896.html',
'https://8020.net/40-4307.html',
'https://8020.net/3628.html',
'https://8020.net/75-3412.html',
'https://8020.net/13-8520.html',
'https://8020.net/4611.html',
'https://8020.net/9253.html',
'https://8020.net/45-4332.html',
'https://8020.net/3601.html',
'https://8020.net/3439.html',
'https://8020.net/14103.html',
'https://8020.net/14081.html',
'https://8020.net/4325.html',
'https://8020.net/40-4345.html',
'https://8020.net/3363.html',
'https://8020.net/3645.html',
'https://8020.net/9140.html',
'https://8020.net/11-6714.html',
'https://8020.net/40-4481.html',
'https://8020.net/14066.html',
'https://8020.net/14125.html',
'https://8020.net/75-3527.html',
'https://8020.net/13123.html',
'https://8020.net/2565.html',
'https://8020.net/13181.html',
'https://8020.net/11-5520.html',
'https://8020.net/13146.html',
'https://8020.net/19-8312.html',
'https://8020.net/3351.html',
'https://8020.net/3369.html']

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
            save_details: TextIO = open("8020byidea1a.txt", "a+", encoding="utf-8")
            save_details.write("\n"+c+"\t"+a+"\t"+a1+"\t"+a2+"\t"+image+"\t"+" , ".join(imagesLst)+"\t"+attr+"\t"+value)
            save_details.close()
            print("**Record stored into txt file.**")

 #
 except AttributeError:

   pass