
import mysql.connector
import requests

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT l3_url FROM l3status where id >11514")
myresult=cur.fetchall()
for fetch in myresult:
    brand_url=fetch[0]
    url1=(brand_url)
    page = requests.get(brand_url)

    s=(page.status_code)

    sql = (" UPDATE l3status SET status='" + str(s) + "' WHERE l3_url='" + str(brand_url) + "' ")

    cur.execute(sql)

    mydb.commit()

    print(cur.rowcount, "record(s) affected")