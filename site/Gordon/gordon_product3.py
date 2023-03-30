import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import TextIO
import mysql.connector

mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    passwd="Raptorpwa2020",
    database='ansu_data_check'
)
mycursor = mydb.cursor()
myresults=[
'https://www.gordonelectricsupply.com/p/Appleton-Efdb150102-3Pos-2Ckt-Sel-Switch/5735290?ID=/Appleton-Electric/mfr-1ICG',
'https://www.gordonelectricsupply.com/p/appleton-cpp2510gmt-250w-metal-halide-pendant-fixture/5733356?ID=/Appleton-Electric/mfr-1ICG',
'https://www.gordonelectricsupply.com/p/Appleton-Efdb175U2-1G-2Pb-Unilet/5735322?ID=/Appleton-Electric/mfr-1ICG']
driver = webdriver.Chrome(
            executable_path=r"C:\Users\nextgenraptor\Downloads\chromedriver_win32 (3)\chromedriver.exe")


def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

loc = 0
for result in myresults:
    try:
        loc += 1
        print(loc)
        url = result
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'lxml')
        driver.get(url)
        driver.maximize_window()

        time.sleep(3)
        attr_lst1 = []
        attr_lst2 = []
        value_lst1 = []
        value_lst2 = []
        # L3 = "Roller Chain Sprockets"
        print("###########Title############")
        s = soup.find('h1')
        TITLE = s.text.strip()
        print(TITLE)
        print("###########part no ############")
        for s in driver.find_elements(By.XPATH, '//*[@id="product_content"]/div[1]/form/div[2]/p[3]'):
            part = s.text.split(': ')[1].strip()
            print(part)
        print("###########Breadcrumb############")
        # for s in soup.find_all('div', {'id': 'breadcrumb'}):
        #         #     breadcrumb = s.text.strip()
        #         #     print(breadcrumb)
        breadcrumb = []
        for s in soup.find('div', {'id': 'breadcrumb'}).find_all('a', {'class':'breadcrumblink'}):
            breadcrumb.append(s.text.strip())
        for s in soup.find('div', {'id': 'breadcrumb'}).find_all('span', {'class': 'breadcrumblink'}):
            breadcrumb.append(s.text.strip())
            breadcrumb = " > ".join(breadcrumb)
            print(breadcrumb)

        print("###########Price############")
        for s in soup.find_all('div', {'class': 'price-box'}):
            # print(s.text)
            price = s.text.split('$')[1].split('/')[0].strip()
            print(price)
        print("###########Image############")
        for s in soup.find_all('a', {'id': 'big-image'}):
            image = s['href']
            print(image)
        print("###########Resources############")
        resources = soup.find('div', {'id': 'resourcetable'}).find('ul').find_all('li')
        for r in resources:
            re = r.find('a')
            res = re['href']
            print(res)

        time.sleep(3)
        print("###########Product Specifications############")
        a = 0
        lst2 = []

        for spec in driver.find_elements(By.XPATH, '// *[ @ id = "spectable"] / table / tbody'): #spectable
            a += 1 #//*[@id="spectable"]/table/tbody
            # print(a)
            # print(spec.text)
            lst1 = spec.text.split("\n")
            # print(lst1)
            for elem in lst1:
                lst2.append(elem.split(':  '))
            # print(lst2)
            lst2 = flatten_list(lst2)
            # print(lst2)
            if 'Full Size Image  ' in lst2:
                lst2.remove('Full Size Image  ')
            else:
                print(lst2)
            for i in range(0, len(lst2)): # even and odd indices
                if i % 2:
                    value_lst1.append(lst2[i])
                else:
                    attr_lst1.append(lst2[i])
            for elem in attr_lst1:
                attr_lst2.append(elem.strip())
            for elem in value_lst1:
                value_lst2.append(elem.strip())
            print(len(attr_lst2))
            print(len(value_lst2))
            print(attr_lst2)
            print(value_lst2)
            i = 0
            j = 0
            while i < len(attr_lst2):
                x = (attr_lst2[i].text if attr_lst2 else "not given")
                print(x)
            while j < len(value_lst2):
                z = (value_lst2[j].text if value_lst2 else "not given")
                print(z)
        # for x,y in zip(attr_lst2,value_lst2):
        #     sql = "INSERT INTO gordon(title,breadcrumb,price,image,resources,attr_name, attr_value)\
        #      VALUES (%s, %s,%s, %s,%s, %s,%s)"
        #     val = (TITLE, breadcrumb,price, image, resources,x,y)
        #     mycursor.executemany(sql, (val,))
        #     mydb.commit()
        #     print(mycursor.rowcount, "record inserted.")
        save_details: TextIO = open("gordon-appleton.txt", "a+", encoding="utf-8")
        save_details.write("\n" + url + "\t" + TITLE + "\t" + part + "\t" +\
                           breadcrumb + "\t" + price + "\t" + image + "\t" +\
                           res + "\t" + x + "\t" + z)
        save_details.close()
        print("\n**Record stored into txt file.**")
    except AttributeError:
        pass
driver.close()