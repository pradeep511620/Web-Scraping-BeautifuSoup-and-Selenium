from typing import TextIO
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


def get_details(url):
    global d
    print("Please wait. Program will work in background.\n")

    opts = Options()
    opts.headless = True
    opts.add_argument("user-agent=""")
    d = webdriver.Chrome("C:/chromedriver.exe", chrome_options=opts)
    d.get(url)
    time.sleep(5)
    try:
        sku=d.find_element_by_xpath("//*[@id='product-page-with-sidenav']/div[2]/div[1]/section/div/div/dl/dd[1]").text
        print(sku)
    except:
        pass


    try:
        for i in range(1, 20):
            head=d.find_element_by_xpath("//*[@id='tab-description']/p[10]").text
            val=d.find_element_by_xpath("//*[@id='tab-description']/ul[1]/li["+str(i)+"]").text

            save_details: TextIO = open("rag-aams4.txt", "a+", encoding="utf-8")
            save_details.write("\n" + listt[x]  +"\t"+ sku+"\t"+head+"\t" + val )
            save_details.close()
            print("\n**Record stored into txt file.**")

    except:
        pass


    try:
        for j in range(1, 20):
            headd=d.find_element_by_xpath("//*[@id='tab-description']/p[11]").text
            val=d.find_element_by_xpath("//*[@id='tab-description']/ul[2]/li["+str(j)+"]").text

            save_details: TextIO = open("rag-aams4.txt", "a+", encoding="utf-8")
            save_details.write("\n" + listt[x]+"\t"+ sku + "\t"+headd+ "\t"+ val )
            save_details.close()
            print("\n**Record stored into txt file.**")

    except:
        pass









if __name__ == '__main__':


     listt =['https://www.ams-samplers.com/deluxe-fiberglass-auger-kit/']

     for x in range(0,10000):
         print(x)
         print(listt[x])
         get_details(listt[x])

