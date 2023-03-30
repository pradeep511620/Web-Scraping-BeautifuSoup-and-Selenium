import requests
from bs4 import BeautifulSoup

import mysql.connector
mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="TESTING"
)
cur = mydb.cursor()
cur.execute("select brand_url,l3_name from `b2b_brand_blank_check` where id = 11")
myresults=cur.fetchall()
for fetch in myresults:
    brand_url=fetch[0]
    l3_name = fetch[1]
    page=requests.get(brand_url)
    soup=BeautifulSoup(page.content,'lxml')
    if(soup.find('div',class_="filterGridRight").find_all('a')):
        flag = 0
        for link in soup.find('div',class_="filterGridRight").find_all('a'):
            li = (link.get("href"))
            a ='https://b2b.raptorsupplies.com/c/'
            if a in li:
                na = link.text
                if na.split() == l3_name.split():
                    # print("match")
                    flag =1
                    break
        if flag ==1 :
            print(l3_name,'same',)
        else:
            print(l3_name,"not same")

            # mycursor = mydb.cursor()
            # sql = "INSERT INTO `brand_cat_link_find` (brand_url, l3_url) VALUES (%s, %s)"
            # val = (brand_url, li)
            # mycursor.execute(sql, val)
            # mydb.commit()
            # print(mycursor.rowcount, "record inserted.")
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
                    print(li)

        else:
            print("pagination not found")
    else:
        print('stand alone product')