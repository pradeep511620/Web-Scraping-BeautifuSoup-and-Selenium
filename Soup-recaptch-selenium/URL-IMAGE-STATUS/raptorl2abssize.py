import mysql.connector
from bs4 import BeautifulSoup
import requests
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT url FROM raptorl2abs WHERE id between 1 and 32")

myresult=cur.fetchall()

for fetch in myresult:

    url=fetch[0]

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    b = (url)

    st1=page.status_code
    c=(st1)
    size = requests.get(url).content
    s = (len(size))

    sql=(" UPDATE raptorl2abs SET status='"+str(c)+"',size='"+str(s)+"'  WHERE url='"+str(b)+"'")

    cur.execute(sql)

    mydb.commit()

    print(cur.rowcount, "record(s) affected")