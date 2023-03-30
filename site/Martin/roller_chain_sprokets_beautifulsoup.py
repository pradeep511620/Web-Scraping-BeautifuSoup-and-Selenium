import requests
from bs4 import BeautifulSoup
import time
import mysql.connector

mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    passwd="Raptorpwa2020",
    database='ansu_data_check'
)
mycursor = mydb.cursor()
myresults=[
'https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=40A26&Website_CategoryName=Sprockets&Website_Code=SP1',
'https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=40A26SS&Website_CategoryName=Sprockets&Website_Code=SP1',
'https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=40A27&Website_CategoryName=Sprockets&Website_Code=SP1',
'https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=40A28&Website_CategoryName=Sprockets&Website_Code=SP1',
'https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=40A28SS&Website_CategoryName=Sprockets&Website_Code=SP1',
'https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=40A29&Website_CategoryName=Sprockets&Website_Code=SP1',
'https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=40A30&Website_CategoryName=Sprockets&Website_Code=SP1',
'https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=40A30SS&Website_CategoryName=Sprockets&Website_Code=SP1',
'https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=40A31&Website_CategoryName=Sprockets&Website_Code=SP1',
'https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=40A32&Website_CategoryName=Sprockets&Website_Code=SP1',
'https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=60BS18HT%201%203/8&Website_CategoryName=Sprockets&Website_Code=SP1']

print(len(myresults))

for result in myresults:
    try:
        url = result
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'lxml')

        time.sleep(3)
        attr_lst1 = []
        value_lst1 = []
        L3 = "Roller Chain Sprockets"

        s = soup.find('div', {'style': 'float: left; margin-left: 20px; width: 400px;'})
        TITLE = s.text.strip().split('\n')[0]
        print(TITLE)
        s = soup.find('span', {'style': 'font-weight: bold;'})
        Mpn = s.text.strip()
        print(Mpn)
        s = soup.find('div', {'style': 'margin-top: 10px'})
        UPC = s.text.strip()
        print(UPC)
        a = 0
        for s in soup.find_all('div', {'style': 'margin-top: 10px'}):
            a += 1
            if a == 2:
                DESCRIPTION = s.text.strip()
                print(DESCRIPTION)
        s = soup.find('img', {'style': 'height: 150px;'})
        IMAGE = s['src']
        print(IMAGE)  # print(s.get("src"))
        for s in soup.find_all('td', {
            'style': 'text-align: left; color: black; background-color: #eeeeee; border: 1px solid silver; width: 200px;'}):
            attr_lst1.append(s.text.strip())
        for s in soup.find_all('td', {
            'style': 'text-align: right; background-color: White; border: 1px solid silver; width: 200px;'}):
            value_lst1.append(s.text.strip())
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
    except AttributeError:
        pass




    # driver.close()
    # sql = "INSERT INTO roller_chain_sprockets_data1_soup (l3, title,mpn,upc,description,image) VALUES (%s, %s,%s, %s,%s, %s)"
    # val = (L3, TITLE, Mpn,UPC, DESCRIPTION, IMAGE)
    # mycursor.executemany(sql, (val,))
    # mydb.commit()
    # print(mycursor.rowcount, "record inserted.")
    #
    #
    # for x,y in zip(attr_lst1,value_lst1):
    #     sql = "INSERT INTO roller_chain_sprockets_data2_soup (model_no,attr_name, attr_value) VALUES (%s, %s, %s)"
    #     val = (Mpn,x,y)
    #     mycursor.executemany(sql, (val,))
    #     mydb.commit()
    #     print(mycursor.rowcount, "record inserted.")