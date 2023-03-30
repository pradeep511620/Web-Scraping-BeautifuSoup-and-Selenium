import urllib.parse
from datetime import datetime
from typing import TextIO
from selenium import webdriver
import time
import sys
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.remote.webelement


def get_details(url):
    current_date: object = datetime.now()
    save_details: TextIO = open("leeson2.txt", "a+")
    save_details.write("\nScrapping Started at : " + current_date.strftime("%B %d, %Y - %H:%M:%S") + "\n")
    save_details.close()
    print("\nScrapping Started at : " + current_date.strftime("%B %d, %Y - %H:%M:%S") + "\n")

    print("Please wait. Program will work in background.\n")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome("C:/chromedriver.exe", options=chrome_options)
    driver.get(url)
    time.sleep(5)

    try:
        for i in range(1,61):

            i=str(i)
            ele = driver.find_element_by_xpath("//*[@id='products-list']/div[2]/div["+i+"]/div/div[1]/div[2]/a").get_attribute("href")
            i=int(i)
            i=i+1
            d = webdriver.Chrome("C:/chromedriver.exe", options=chrome_options)
            d.get(ele)
            time.sleep(5)
            product_name1 = product_name2 = price = link = image = brand = model = our_model = upc = condition= breakups=''

            print("\n----------------------------------------------------------\n")

            try:
                product_name1=d.find_element_by_xpath("/html/body/div[2]/main/div[2]/div/div[2]/div[2]/div[2]/div[2]/h1").text
                print("product_name_1 :"+ product_name1)
            except:
                pass
            try:
                brand=d.find_element_by_xpath("/html/body/div[2]/main/div[2]/div/div[2]/div[2]/div[2]/div[1]/ul/li[1]/a/span").text
                print("brand :"+brand)
            except:
                pass


            try:
                model=d.find_element_by_xpath("/html/body/div[2]/main/div[2]/div/div[2]/div[2]/div[2]/div[1]/ul/li[2]/span").text
                print("model :"+model)
            except:
                pass

            try:
                condition=d.find_element_by_xpath("/html/body/div[2]/main/div[2]/div/div[2]/div[2]/div[2]/div[1]/ul/li[3]/span").text
                print("condition :" +condition)
            except:
                pass

            try:
                sku=d.find_element_by_xpath("/html/body/div[2]/main/div[2]/div/div[2]/div[2]/div[2]/div[1]/ul/li[4]/span").text
                print("sku :"+sku)
            except:
                pass
            try:
                price=d.find_element_by_xpath("/html/body/div[2]/main/div[2]/div/div[2]/div[2]/div[3]/div/div[1]/p[1]").text
                print("price :"+price)
            except:
                pass


            try:
                image=d.find_element_by_xpath("/html/body/div[2]/main/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/div/div/img").get_attribute("src")
                print("image url :"+image)
            except:
                pass

            try:
                table1=d.find_element_by_xpath("//*[@id='additionalDescription']/div/div[2]/ul[2]").text
                print("table :"+table1)

            except:
                pass
            save_details: TextIO = open("leeson2.txt", "a+", encoding="utf-8")
            save_details.write("\n" + ele + "\t" + product_name1 +  "\t" + brand + "\t" + model + "\t"  + condition +"\t"+ sku + "\t"+image+"\t"+price+ "\t" +table1)
            save_details.close()
            print("\n**Record stored into txt file.**")

    except:
        d.close()


















if __name__ == '__main__':
    for x in range(37,66):
     x=str(x)
     url = "https://www.mrosupply.com/brands/leeson/?page="+x
     x=int(x)
     x=x+1
     get_details(url)

