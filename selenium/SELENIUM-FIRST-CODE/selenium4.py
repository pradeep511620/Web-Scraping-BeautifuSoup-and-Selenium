import mysql.connector
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
print("sample test case started")

driver = webdriver.Chrome('C:/Users/ashish/Downloads/chromedriver_win32 (1)//chromedriver.exe')

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rahul"
)

cur=mydb.cursor()

s=cur.execute("SELECT product_url from weigthsab  where id between 1 and 5")
myresult=cur.fetchall()

for fetch in myresult:
    url=fetch[0]
    driver.get(url)
    time.sleep(2)
driver.save_screenshot('screen.png')

time.sleep(1)
driver.close()
print("sample test case successfully complete")




