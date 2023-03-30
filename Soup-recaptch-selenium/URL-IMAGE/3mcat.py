
from bs4 import BeautifulSoup
from hurry.filesize import size
import mysql.connector
import requests
import csv
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT categories_url FROM 3mcat ")

myresult=cur.fetchall()
for fetch in myresult:
    categories_url=fetch[0]
    #categories_name = fetch[1]
    page = requests.get(categories_url)
    soup = BeautifulSoup(page.content, "lxml")
    for link in soup.find('div', class_="l3pagehead").find_all('h1'):

        lin =(link.text)
        li=(len(lin))
        #url4=print(len(categories_name))
        response =( requests.get(categories_url))

        sql = (" UPDATE 3mcat SET categories_name='"+str(lin)+"',status='" + str(response) + "',name_len='"+str(li)+"'  WHERE categories_url='" + str(categories_url) + "'")

        cur.execute(sql)

        mydb.commit()

        print(cur.rowcount, "record(s) affected")


