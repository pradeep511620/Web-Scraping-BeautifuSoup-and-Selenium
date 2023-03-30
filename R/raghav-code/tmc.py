import urllib.parse
from datetime import datetime
from typing import TextIO
from selenium import webdriver
import time
import sys
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.remote.webelement


def get_details(url):

    #current_date: object = datetime.now()
    #save_details: TextIO = open("tcm1.txt", "a+")
    #save_details.write("\nScrapping Started at : " + current_date.strftime("%B %d, %Y - %H:%M:%S") + "\n")
    #save_details.close()
    #print("\nScrapping Started at : " + current_date.strftime("%B %d, %Y - %H:%M:%S") + "\n")

    print("Please wait. Program will work in background.\n")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    d = webdriver.Chrome("C:/chromedriver.exe", options=chrome_options)
    d.get(url)
    time.sleep(5)


    product_name1 = sku  = image   = price = ''


    print("\n----------------------------------------------------------\n")

    try:
                product_name1=d.find_element_by_xpath("//*[@id='shopify-section-product-template']/div[1]/div/div[2]/header/h2/span").text
                print("product_name_1 :"+ product_name1)
    except:
                pass



    try:
                sku=d.find_element_by_class_name("sku-product").text
                print(sku)
    except:
                pass



    try:
                price=d.find_element_by_xpath("//*[@id='shopify-section-product-template']/div[1]/div/div[2]/div[3]/div[1]/span").text
                print("Price : " + price)

    except:
                pass

    try:
        image=d.find_element_by_xpath("//*[@id='shopify-section-product-template']/div[1]/div/div[1]/div/div/div/div/div/a").get_attribute("href")
        print("Image : "+image)
    except:
        pass
    try:
        size=d.find_element_by_xpath("//*[@id='product-variants']/div/div[2]/input[2]").get_attribute("data-value")
        print(size)
    except:
        pass


    save_details: TextIO = open("tm2.txt", "a+", encoding="utf-8")
    save_details.write("\n" + url + "\t" + product_name1 + "\t" + sku  +"\t"+price+ "\t"+image+"\t"+size )

    save_details.close()
    print("\n**Record stored into txt file.**")
















if __name__ == '__main__':
    list=['https://tmcindustries.com/collections/krytox-pfpe-oils-greases/products/krytox-gpl-103-oil',
'https://tmcindustries.com/collections/krytox-pfpe-oils-greases/products/krytox-gpl-106-oil',
'https://tmcindustries.com/collections/krytox-pfpe-oils-greases/products/krytox-eg2000-grease',
'https://tmcindustries.com/collections/krytox-pfpe-oils-greases/products/krytox-gpl-216-grease',
'https://tmcindustries.com/collections/krytox-pfpe-oils-greases/products/krytox-xht-bd-grease',
'https://tmcindustries.com/collections/krytox-pfpe-oils-greases/products/krytox-gpl-295-grease',
'https://tmcindustries.com/collections/krytox-pfpe-oils-greases/products/krytox-gpl-214-grease',
'https://tmcindustries.com/collections/krytox-pfpe-oils-greases/products/krytox-143-az-oil',
'https://tmcindustries.com/collections/krytox-pfpe-oils-greases/products/reclaimed-1514-pfpe-vacuum-pump-fluid',
'https://tmcindustries.com/collections/krytox-pfpe-oils-greases/products/krytox-283-ad-grease',
'https://tmcindustries.com/collections/krytox-pfpe-oils-greases/products/krytox-nrt-8908-grease',
'https://tmcindustries.com/collections/krytox-pfpe-oils-greases/products/krytox-143-ab-oil',
'https://tmcindustries.com/collections/krytox-pfpe-oils-greases/products/krytox-xp-1a3-oil']

    for x in range(0,14):

     url = list[x]

     print(url)

     get_details(url)

