import time
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import mysql.connector
path = 'D:/images/'
opts = Options()
opts.headless = True
opts.add_argument("--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
d=uc.Chrome(version_main=109)
mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_dat"
)
cur = mydb.cursor()
cur.execute("SELECT image_url,model_no,id FROM `data_team_no_image_find` where image_download is null")
my_result = cur.fetchall()

for fetch in my_result:
    url = fetch[0]
    img_name = fetch[1]
    id = fetch[2]

    d.get(url)

    time.sleep(5)
    img = d.find_element(By.XPATH,'/html/body/img')
    img.screenshot(path+"/"+str(img_name) + '.png')
    st = 'done'
    sql = ("UPDATE `data_team_no_image_find` SET image_download ='" + str(st) + "' WHERE   id='" + str(id) + "'")
    cur.execute(sql)
    mydb.commit()
    print(cur.rowcount, "records successful Done")



