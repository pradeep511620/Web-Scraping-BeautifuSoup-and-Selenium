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
cur.execute("SELECT url FROM singapore_url WHERE id BETWEEN 19000 AND 20000 AND STATUS IS NULL")

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

    sql=(" UPDATE singapore_url SET redirect_type='"+str(a)+"',status='"+str(c)+"'  WHERE url='"+str(b)+"'")

    cur.execute(sql)

    mydb.commit()

    print(cur.rowcount, "record(s) affected")