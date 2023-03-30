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
        title=d.find_element_by_class_name("productView-title").text
        print("Product Name"+title)
    except:
        pass
    try:
        price=d.find_element_by_class_name("price--withoutTax").text
        print("Price"+price)
    except:
        pass
    try:
        image=d.find_element_by_xpath("//*[@id='product-images-container']/div[1]/div[1]/div/div/div/div/li/figure/img").get_attribute("src")
        print("Image-"+image)
    except:
        pass
    try:
        att=d.find_elements_by_class_name("productView-info-name")
        val=d.find_elements_by_class_name("productView-info-value")
        list=[]
        for i in range(0,len(att)):

            list.append(att[i].text)
            list.append(val[i].text)
    except:
        pass
    s="-"
    print(list)

    try:
        check=d.find_element_by_xpath("//*[@id='tab-description']/ul/li[1]")
        rp=d.find_element_by_xpath("//*[@id='tab-description']/p[3]").text
        for i in range(0,10):
            ele=d.find_element_by_xpath("//*[@id='tab-description']/ul/li["+str(i)+"]")
            save_details: TextIO = open("ams2.txt", "a+", encoding="utf-8")
            save_details.write("\n" + list[x]+"\t"+title+"\t"+price+"\t"+image+"\t"+s.join(list)+"\t"+rp+"\t"+ele )
            save_details.close()
            print("\n**Record stored into txt file.**")
    except:
        save_details: TextIO = open("ams2.txt", "a+", encoding="utf-8")
        save_details.write("\n" + listt[x] + "\t" + title + "\t" + price.strip() + "\t"+ "\t"+ image.strip() + "\t"  + s.join(list) )
        save_details.close()
        print("\n**Record stored into txt file.**")




if __name__ == '__main__':

     listt =['https://www.ams-samplers.com/flighted-auger-2-1-2-w-tip-1-2-adapter/']
     for x in range(0,10000):
         print(x)
         print(listt[x])
         get_details(listt[x])
