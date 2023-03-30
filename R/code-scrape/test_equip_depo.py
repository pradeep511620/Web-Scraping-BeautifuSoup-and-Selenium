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
    save_details: TextIO = open("details.txt", "a+")
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
        for i in range(2,501):

            i=str(i)
            ele = driver.find_element_by_xpath("/html/body/div[1]/div[4]/table[1]/tbody/tr["+i+"]/td[1]/a").get_attribute("href")
            i=int(i)
            i=i+1
            d = webdriver.Chrome("C:/chromedriver.exe", options=chrome_options)
            d.get(ele)
            time.sleep(5)
            product_name1 = product_name2 = price = link = image = brand = model = our_model = upc = condition= breakups=''

            print("\n----------------------------------------------------------\n")

            try:
                product_name1=d.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[1]/div[1]/h1").text
                print("product_name_1 :"+ product_name1)
            except:
                pass
            try:
                product_name2=d.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[1]/div[1]/h2").text
                print("product_name_2 :"+product_name2)
            except:
                pass


            try:
                brand=d.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[2]/table/tbody/tr[1]/td[2]").text
                print("brand :"+brand)
            except:
                pass

            try:
                model=d.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[2]/table/tbody/tr[2]/td[2]").text
                print("model :" +model)
            except:
                pass

            try:
                our_model=d.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[2]/table/tbody/tr[3]/td[2]").text
                print("our_model :"+our_model)
            except:
                pass
            try:
                condition=d.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[2]/table/tbody/tr[4]/td[2]").text
                print("condition :"+condition)
            except:
                pass

            try:
                upc=d.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[2]/table/tbody/tr[5]/td[2]").text
                print("upc :"+upc)
            except:
                pass
            try:
                image=d.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div/a/img[2]").get_attribute("src")
                print("image url :"+image)
            except:
                pass
            try:
                breakups=d.find_element_by_xpath("/html/body/div[1]/div[3]/div").text
                print("breakups :"+breakups)
            except:
                pass
            try:
                price=d.find_element_by_class_name("ctaPrice").text
                print("price :"+price)

            except:
                pass
            save_details: TextIO = open("details.txt", "a+", encoding="utf-8")
            save_details.write("\n" + product_name1 + "\t" +product_name2+ "\t" + brand + "\t" + model + "\t" + our_model + "\t" + condition +"\t"+ upc + "\t"+image+"\t"+breakups+"\t"+price+"\t"+ele)
            save_details.close()
            print("\n**Record stored into txt file.**")

    except:
        d.close()


















if __name__ == '__main__':
    url = "https://www.testequipmentdepot.com/general-tools/pricelist.htm"
    get_details(url)


