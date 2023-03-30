from bs4 import BeautifulSoup
import requests
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT url FROM test WHERE id BETWEEN 10751 AND 11746")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    page=requests.get(url)
    soup=BeautifulSoup(page.content,"lxml")
    status=(page.status_code)
    response=(page.history)
    sql = (" UPDATE test SET status='" + str(status) + "',response='"+str(response)+"'  WHERE url='" + str(url) + "' ")
    cur.execute(sql)
    mydb.commit()
    print(cur.rowcount, "record(s) affected")
