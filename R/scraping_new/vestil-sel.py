import urllib.parse
from datetime import datetime
from typing import TextIO
from selenium import webdriver
import time
import sys
from selenium. webdriver. common. keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.remote.webelement


def get_details(url):
    global d
    print("Please wait. Program will work in background.\n")

    opts = Options()
    #opts.headless = True

    opts.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36')
    d = webdriver.Chrome("C:/chromedriver.exe", chrome_options=opts)
    d.get(url)
    time.sleep(5)
    try:
        bc=d.find_element_by_xpath("//*[@id='wrapper']/section[2]/div/div[1]").text
        bc=str(bc)
        bc=bc.replace('\n',' ')
        print(bc)
    except:
        pass

    try:
        ele=d.find_element_by_xpath("//*[@id='MATRIX']/div/div[2]/div/div/ul/li[1]/a")
        ele.click()
    except:
        pass
    try:
        ele2=d.find_element_by_xpath("//*[@id='sample_5_length']/label/select")
        ele2.click()
        ele3=d.find_element_by_xpath("//*[@id='sample_5_length']/label/select/option[4]")
        ele3.click()
    except:
        pass
    try:
        number=d.find_element_by_class_name("dataTables_info").text
        no=str(number)
        noo=no.split("of")[1]
        noo=noo.split()
        fw=noo[0]
        print(fw)
    except:
        pass
    for i in range(1, int(fw)):
        print(i)
        try:
            click=d.find_element_by_xpath("//*[@id='sample_5']/tbody/tr["+str(i)+"]/td[1]/a")
            click.click()
            time.sleep(3)
        except:
            pass
        try:
            iframe=d.find_element_by_css_selector('#fancybox__iframe_1_0')

            d.switch_to.frame(iframe)

        except:
            pass
        try:
            model=d.find_element_by_xpath("/html/body/section[1]/div/div[1]/h1/span").text
            print(model)
        except:
            pass
        try:
            desc=d.find_element_by_xpath("/html/body/section[1]/div/div[3]/div[2]/h2").text
            print(desc)
        except:
            pass
        try:
            img=d.find_element_by_xpath("/html/body/section[1]/div/div[3]/div[1]/div/img").get_attribute("src")
            print(img)
        except:
            pass
        try:
            pdf=d.find_element_by_xpath("/html/body/section[3]/div/div[4]/div/a[1]").get_attribute("href")
            print(pdf)
        except:
            pass

        try:
            but = d.find_element_by_xpath("/html/body/section[2]/div/div/button[1]")
            but.click()
        except:
            pass

        try:
            count=d.find_elements_by_class_name("row")
            for s in range(1,len(count)):
                att=d.find_element_by_xpath("//*[@id='marketing']/div/div/div["+str(s)+"]/div[1]").text
                print(att)
                val=d.find_element_by_xpath("//*[@id='marketing']/div/div/div["+str(s)+"]/div[2]").text
                print(val)
                save_details: TextIO = open("vestl.txt", "a+", encoding="utf-8")
                save_details.write("\n" + list[x] + "\t" + bc + "\t" +model+"\t"+desc+"\t"+img+"\t"+pdf+"\t"+att+"\t"+val )
                save_details.close()
                print("\n**Record stored into txt file.**")
        except:
            pass
        try:

            iframe2 = d.find_element_by_css_selector('#fancybox__iframe_1_0')

            d.switch_to.frame(iframe2)
            print("dfghjkl")

        except:
            pass
        try:
            close=d.find_element_by_xpath("//*[@id='fancybox-2']/div[2]/div/div/div/div/button").click()
            print("iuygfcgvbhnjkl")
        except:
            pass


if __name__ == '__main__':

     list =['https://www.mcmaster.com/92579A101/']
     for x in range(0,10000):
         print(x)
         print(list[x])
         get_details(list[x])
