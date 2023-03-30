import undetected_chromedriver.v2 as uc
import time
from typing import TextIO
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
import requests
# from time import time, sleep
import socket # Socket programming is a way of connecting two nodes on a network to communicate with each other.
# One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other
# to form a connection
from datetime import datetime

hostname = socket.gethostname() # returns the host name of the current system
IPAddr = socket.gethostbyname(hostname)# accepts hostname argument and returns the IP address in the string format
# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # to string
def main(url,loopp):
    options = webdriver.ChromeOptions()# opens up without any extension or history or cookies, etc
    #options.headless = True

    driver = uc.Chrome(options=options)

    driver.get(url)
    driver.delete_all_cookies()
    a = 0
    elems = driver.find_element(By.CLASS_NAME, "productLink")
    print(len(elems))
    # for elem in elems:
    #     a += 1
    #     link = elem.get_attribute("href")
    #     print(link)


if __name__ == '__main__':
    list = ['https://www.martinsprocket.com/view/products/product-search?Website_Code=SP1']
    for x in range(0, 7000):
        print(x)
        # time.sleep(1)
        print(list[x])
        main(list[x],x)