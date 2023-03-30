import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import mysql.connector
path = 'D:/Images/'
opts = Options()
opts.headless = True
opts.add_argument("--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
d = webdriver.Chrome(r"C:/Users/hp/Downloads/chromedriver_win32 (2)//chromedriver.exe", chrome_options=opts)
mydb = mysql.connector.connect(
    host="staging-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="eaton_13_12_22"
)
cur = mydb.cursor()
cur.execute("SELECT DISTINCT image_url1,image_name,is_download,entity_id FROM `product_images` WHERE image_name!='' and is_download is null  ")
my_result = cur.fetchall()

for fetch in my_result:
    url = fetch[0].replace('90x90_96','1000x1000_300').replace('500x500_72','1000x1000_300')
    # print(url)
    img_name = fetch[1]
    is_downlaod = fetch[2]
    entity_id = fetch[3]
    try:
        d.get(url)
        # time.sleep(5)
        img = d.find_element(By.XPATH,'/html/body/img')
        img.screenshot(path+"/"+str(img_name) + '.png')
        st = 'done'
        sql = "UPDATE `product_images` SET is_download = '" + str(st) + "' WHERE entity_id ='" + str(entity_id) + "' "
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "image_download")
    except:
        pass