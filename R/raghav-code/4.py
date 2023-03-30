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
    save_details: TextIO = open("hubbell4.txt", "a+")
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
            ele = driver.find_element_by_xpath("//*[@id='content']/div[1]/div[3]/form/div[4]/ul/li["+i+"]/div[2]/a").get_attribute("href")
            i=int(i)
            i=i+1
            d = webdriver.Chrome("C:/chromedriver.exe", options=chrome_options)
            d.get(ele)
            time.sleep(5)
            product_name1 = product_name2 = price = link = image = brand = model = our_model = upc = condition= breakups=''

            print("\n----------------------------------------------------------\n")

            try:
                product_name1=d.find_element_by_xpath("//*[@id='content']/div[1]/div[2]/h1").text
                print("product_name_1 :"+ product_name1)
            except:
                pass
            try:
                des=d.find_element_by_xpath("//*[@id='content']/div[1]/div[2]/h1").text
                print("Description :"+des)
            except:
                pass


            try:
                upc=d.find_element_by_xpath("//*[@id='product_content']/div[1]/form/div[2]/p[2]").text
                print("upc :"+upc)
            except:
                pass

            try:
                part=d.find_element_by_xpath("//*[@id='product_content']/div[1]/form/div[2]/p[3]").text
                print("part no. :" +part)
            except:
                pass

            try:
                bc=d.find_element_by_xpath("//*[@id='breadcrumb']").text
                print("breadcrumps :"+bc)
            except:
                pass



            try:
                image=d.find_element_by_xpath("//*[@id='big-image']/img[2]").get_attribute("src")
                print("image url :"+image)
            except:
                pass

            try:
                table1=d.find_element_by_xpath("//*[@id='spectable']/table").text
                print("table :"+table1)

            except:
                table1=" "
            save_details: TextIO = open("hubbell4.txt", "a+", encoding="utf-8")
            save_details.write("\n" + ele + "\t" + product_name1 +  "\t" + des + "\t" + upc + "\t"  + part +"\t"+ bc + "\t"+image+ "\t" +table1)
            save_details.close()
            print("\n**Record stored into txt file.**")

    except:
        d.close()


















if __name__ == '__main__':
    for x in range(256,266):
     x=str(x)
     url = "https://www.gordonelectricsupply.com/s/Hubbell-Wiring-Devices-Kellems/mfr-1IF7?process=search&itemsperpage=60&sortby=availSort&display=thumb&fqall=&fqv=&fq=&sf=&allnstr=&ph=&pl=&qdx=0&nstr=&narrowby=&pagenum="+x
     x=int(x)
     x=x+1
     get_details(url)

