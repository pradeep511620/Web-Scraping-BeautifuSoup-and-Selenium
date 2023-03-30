import mysql.connector
from bs4 import BeautifulSoup
import requests
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_supplies_com"
)
cur=mydb.cursor()
cur.execute("SELECT url FROM web_master_status WHERE id BETWEEN 20074 AND 21066")

myresult=cur.fetchall()

for fetch in myresult:

    url=fetch[0]

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    b = (url)

    st = page.history
    a= (st)
    st1=page.status_code
    c=(st1)

    sql=(" UPDATE web_master_status SET response='"+str(a)+"',status='"+str(c)+"'  WHERE url='"+str(b)+"'")

    cur.execute(sql)

    mydb.commit()

    print(cur.rowcount, "record(s) affected")