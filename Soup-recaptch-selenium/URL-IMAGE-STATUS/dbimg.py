import mysql.connector
from bs4 import BeautifulSoup
import requests
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rahul"
)
cur=mydb.cursor()
cur.execute("SELECT url FROM grainger WHERE id=19")

myresult=cur.fetchall()

for fetch in myresult:

    url=fetch[0]

    page = requests.get(url,headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    b = print(url)

    st1=page.status_code
    c=print(st1)

    """sql=(" UPDATE singapore_url SET redirect_type='"+str(a)+"',status='"+str(c)+"'  WHERE url='"+str(b)+"'")

    cur.execute(sql)

    mydb.commit()

    print(cur.rowcount, "record(s) affected")"""