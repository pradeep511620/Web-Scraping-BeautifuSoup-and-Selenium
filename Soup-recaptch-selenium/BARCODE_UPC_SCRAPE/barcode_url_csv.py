import time
from typing import TextIO

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
opts = Options()
opts.headless = True
opts.add_argument(
    "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")


import csv
file = open('C:/Users/hp/Downloads/barcode_url.csv', 'r')
csvreader = csv.reader(file)
for fetch in csvreader:
    url = fetch[4]
    model_no =fetch[1]
    id = fetch[0]
    driver = webdriver.Chrome(options=opts)
    print(id)
    driver.get(url)
    time.sleep(3)
    li = []
    b = 0
    fl = 1
    try:
        n = driver.find_element(By.ID, 'product-search-results')
        f = driver.find_element(By.XPATH, '//*[@id="product-search-body"]/section[2]/div/div/div/div/nav').find_elements(
        By.TAG_NAME, 'li')


        for x in n.find_elements(By.TAG_NAME, 'li'):
            for z in x.find_elements(By.TAG_NAME, 'p'):
                if fl == 1:
                    li.append(z.text)
                    continue
                li.append(z.text.split(':')[-1])
            save_details: TextIO = open("test_upc.txt", "a+", encoding="utf-8")
            save_details.write(
                "\n" + driver.current_url + "\t" + li[0] + "\t" + "rp_" + li[1] + "\t" + "rp_" + li[2] + "\t" + "rp_" +li[3])
            save_details.close()
            li.clear()

    except:
        save_details: TextIO = open("test_upcnot_found.txt", "a+", encoding="utf-8")
        save_details.write("\n" + url)
        save_details.close()
        pass