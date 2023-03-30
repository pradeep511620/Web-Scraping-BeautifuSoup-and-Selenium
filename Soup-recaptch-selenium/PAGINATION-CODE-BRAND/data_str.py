import requests
from bs4 import BeautifulSoup
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='db1'
)
cur=mydb.cursor()
cur.execute("select brand_url from `brand_url` where id>1766")
myresults=cur.fetchall()
for fetch in myresults:
    brand_url=fetch[0]
    page=requests.get(brand_url)
    soup=BeautifulSoup(page.content,'lxml')
    if(soup.find('div',class_="filterGridRight").find_all('a',class_='brand-title')):
        for link in soup.find('div',class_="filterGridRight").find_all('a',class_='brand-title'):
            li = (link.get("href"))
            mycursor = mydb.cursor()
            sql = "INSERT INTO `brand_cat_link_find` (brand_url, l3_url) VALUES (%s, %s)"
            val = (brand_url, li)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        a = 0
        max = 0
        if (soup.find('div', class_="customePagination sectionGap")):
            for links in soup.find('div', class_="customePagination sectionGap").find_all('a'):
                li2 = (links.get("href"))
                tmp = int(li2.split('=')[1])
                if (max < tmp):
                    max = tmp

            for x in range(2, max + 1):
                url =brand_url
                url = url + "?page=" + str(x)

                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")

                for link in soup.find('div',class_="filterGridRight").find_all('a',class_='brand-title'):
                    li =(link.get("href"))
                    mycursor = mydb.cursor()
                    sql = "INSERT INTO `brand_cat_link_find` (brand_url, l3_url) VALUES (%s, %s)"
                    val = (brand_url,li)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record inserted.")

        else:
            print("pagination not found")
    else:
        print('stand alone product')