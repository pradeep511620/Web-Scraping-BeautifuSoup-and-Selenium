import undetected_chromedriver.v2 as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import socket
from datetime import datetime

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

def main(url,loopp):
    options = webdriver.ChromeOptions()
    #options.headless = True
    driver = uc.Chrome(options=options)
    driver.get(url)
    driver.delete_all_cookies()
    a = 0
    elems = driver.find_element(By.CLASS_NAME, "productLink")
    # print(len(elems))
    #############################################
    for elem in elems:
        a += 1
        link = elem.get_attribute("href")
        print(link)


if __name__ == '__main__':
    list = ['https://www.martinsprocket.com/view/products/product-search?Website_Code=SP1']
    for x in range(0, 7000):
        print(x)
        # time.sleep(1)
        print(list[x])
        main(list[x],x)


# <a class="productLink" href="/views/productinfo.aspx?Part_Number=100A10&amp;Website_CategoryName=Sprockets&amp;Website_Code=SP1">
                                                        # 100A10&nbsp;SPK ROLLER A</a>