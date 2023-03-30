import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import mysql.connector

mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    passwd="Raptorpwa2020",
    database='ansu_data_check'
)
mycursor = mydb.cursor()

driver = webdriver.Chrome(executable_path=r"C:\Users\nextgenraptor\Downloads\chromedriver_win32 (3)\chromedriver.exe")
url = 'https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=100A10&Website_CategoryName=Sprockets&Website_Code=SP1'
driver.get(url)
driver.maximize_window()
time.sleep(3)
attr_lst1 = []
value_lst1 = []
L3 = "Roller Chain Sprockets"

a = 0
for title in driver.find_elements(By.TAG_NAME,'Span'):
    a += 1
    if a == 1:
        continue
    elif a == 2:
        TITLE = title.text
        print(TITLE)
    elif a==3:
        Mpn = title.text
        print(Mpn)
    else:
        continue

a = 0
for upc in driver.find_elements(By.XPATH, "/html/body/div/div[2]/div/div[2]/div"):
    a += 1
    if a == 1:
        UPC = upc.text
        print(UPC)
    elif a == 2:
        DESCRIPTION = upc.text
        print(DESCRIPTION)
    else:
        continue
        
for image in driver.find_elements(By.TAG_NAME,'img'):
    IMAGE = image.get_attribute('src')
    print(IMAGE)
time.sleep(3)

a = 0
for td in driver.find_elements(By.TAG_NAME,'td'):
    a += 1
    if a % 2 == 1 and td.text != None:
        attr_lst1.append(td.text)
        attr_lst1 =  list(filter(None, attr_lst1))
    if a % 2 == 0 and td.text != None:
        value_lst1.append(td.text)
        value_lst1 =  list(filter(None, value_lst1))
print(attr_lst1)
print(value_lst1)

driver.find_element(By.LINK_TEXT,"Misc Info").click()

a = 0
for td in driver.find_elements(By.TAG_NAME,'td'):
    a += 1
    if a % 2 == 1 and td.text != None:
        attr_lst1.append(td.text)
        attr_lst1 = list(filter(None, attr_lst1))

    if a % 2 == 0 and td.text != None:
        value_lst1.append(td.text)
        value_lst1 = list(filter(None, value_lst1))
print(attr_lst1)
print(value_lst1)

# sql = "INSERT INTO scrape_roller_data1 (l3, title,mpn,upc,description,image) VALUES (%s, %s,%s, %s,%s, %s)"
# val = (L3, TITLE, Mpn,UPC, DESCRIPTION, IMAGE)
# mycursor.executemany(sql, (val,))
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")


# for x,y in zip(attr_lst1,value_lst1):
#     sql = "INSERT INTO scrape_roller (model_no,attr_name, attr_value) VALUES (%s, %s, %s)"
#     val = (Mpn,x,y)
#     mycursor.executemany(sql, (val,))
#     mydb.commit()
#     print(mycursor.rowcount, "record inserted.")